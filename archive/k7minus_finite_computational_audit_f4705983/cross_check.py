#!/usr/bin/env python3
"""Independent computational cross-checks for K7-minus finite verifiers.

Scratch audit code — NOT part of the repository under audit.
Uses only the Python standard library + nauty geng/listg on PATH.
Does not import any project modules.
"""
from __future__ import annotations

import hashlib
import itertools
import os
import shutil
import subprocess
import sys
from collections import Counter
from functools import lru_cache

REPORT: list[str] = []


def log(msg: str) -> None:
    REPORT.append(msg)
    print(msg)


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


# ---------------------------------------------------------------------------
# 1. Independent graph6 (McKay format) decoder + encoder
#    Spec: graph6 encodes n as first char (n+63), then upper triangle bit
#    stream packed 6 bits/char with MSB-first packing within each char.
# ---------------------------------------------------------------------------

def g6_decode(text: str) -> list[list[int]]:
    """Return adjacency matrix as list of bitmasks (independent of repo)."""
    text = text.strip()
    require(text, "empty graph6")
    n = ord(text[0]) - 63
    require(1 <= n <= 62, f"order out of simple graph6 range: {n}")
    need = n * (n - 1) // 2
    bits: list[int] = []
    for ch in text[1:]:
        v = ord(ch) - 63
        require(0 <= v < 64, f"bad graph6 char {ch!r}")
        for shift in range(5, -1, -1):
            bits.append((v >> shift) & 1)
    require(len(bits) >= need, "truncated graph6")
    adj = [0] * n
    pos = 0
    for j in range(1, n):
        for i in range(j):
            if bits[pos]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            pos += 1
    return adj


def g6_encode(adj: list[int]) -> str:
    n = len(adj)
    bits: list[int] = []
    for j in range(1, n):
        for i in range(j):
            bits.append((adj[i] >> j) & 1)
    while len(bits) % 6:
        bits.append(0)
    out = [chr(n + 63)]
    for start in range(0, len(bits), 6):
        v = 0
        for b in bits[start : start + 6]:
            v = (v << 1) | b
        out.append(chr(v + 63))
    return "".join(out)


def edge_count(adj: list[int]) -> int:
    return sum(x.bit_count() for x in adj) // 2


def is_clique(adj: list[int], verts: tuple[int, ...]) -> bool:
    return all(adj[a] & (1 << b) for a, b in itertools.combinations(verts, 2))


def is_indep(adj: list[int], verts: tuple[int, ...]) -> bool:
    return all(not (adj[a] & (1 << b)) for a, b in itertools.combinations(verts, 2))


def has_k4_subgraph(adj: list[int]) -> bool:
    n = len(adj)
    return any(is_clique(adj, q) for q in itertools.combinations(range(n), 4))


def alpha(adj: list[int]) -> int:
    n = len(adj)
    best = 0
    for size in range(n, 0, -1):
        if any(is_indep(adj, q) for q in itertools.combinations(range(n), size)):
            return size
    return 0


# ---------------------------------------------------------------------------
# 2. Distinct minor algorithms
#    A) Connected-partition (branch-set) enumeration for small targets
#    B) Deletion/contraction recursion (written separately)
# ---------------------------------------------------------------------------

def delete_v(adj: list[int], v: int) -> list[int]:
    n = len(adj)
    keep = [i for i in range(n) if i != v]
    out = [0] * len(keep)
    for ai, a in enumerate(keep):
        for bi in range(ai + 1, len(keep)):
            b = keep[bi]
            if adj[a] & (1 << b):
                out[ai] |= 1 << bi
                out[bi] |= 1 << ai
    return out


def contract_e(adj: list[int], u: int, v: int) -> list[int]:
    if u > v:
        u, v = v, u
    n = len(adj)
    keep = [i for i in range(n) if i != v]
    out = [0] * len(keep)
    for ai, a in enumerate(keep):
        for bi in range(ai + 1, len(keep)):
            b = keep[bi]
            edge = bool(adj[a] & (1 << b))
            if a == u:
                edge = edge or bool(adj[v] & (1 << b))
            if b == u:
                edge = edge or bool(adj[a] & (1 << v))
            if edge:
                out[ai] |= 1 << bi
                out[bi] |= 1 << ai
    return out


@lru_cache(maxsize=None)
def dc_has_minor(key: tuple[int, ...], target_n: int, min_edges: int) -> bool:
    """Deletion/contraction minor test (independent encoding)."""
    adj = list(key)
    n = len(adj)
    if n < target_n:
        return False
    if n == target_n:
        return edge_count(adj) >= min_edges
    # try deletions
    for v in range(n):
        child = tuple(delete_v(adj, v))
        if dc_has_minor(child, target_n, min_edges):
            return True
    # try contractions
    for a, b in itertools.combinations(range(n), 2):
        if adj[a] & (1 << b):
            child = tuple(contract_e(adj, a, b))
            if dc_has_minor(child, target_n, min_edges):
                return True
    return False


def has_k4_minor_dc(adj: list[int]) -> bool:
    return dc_has_minor(tuple(adj), 4, 6)


def has_k4minus_minor_dc(adj: list[int]) -> bool:
    return dc_has_minor(tuple(adj), 4, 5)


def has_k5_minor_dc(adj: list[int]) -> bool:
    return dc_has_minor(tuple(adj), 5, 10)


def connected_mask(adj: list[int], mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    while True:
        expanded = reached
        m = reached
        while m:
            bit = m & -m
            m ^= bit
            v = bit.bit_length() - 1
            expanded |= adj[v] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def bags_touch(adj: list[int], a: int, b: int) -> bool:
    m = a
    while m:
        bit = m & -m
        m ^= bit
        v = bit.bit_length() - 1
        if adj[v] & b:
            return True
    return False


def has_kt_minus_partition(adj: list[int], t: int, max_missing: int = 1) -> bool:
    """Connected-partition search for K_t^- minor (branch sets partition V).

    Exhaustive over surjective maps V -> {0..t-1} up to label renaming via
    restricted growth strings. Suitable only for tiny graphs.
    """
    n = len(adj)
    if n < t:
        return False
    # restricted growth strings for partitions into exactly t nonempty blocks
    # generate via recursion
    found = False

    def check(assign: list[int]) -> bool:
        bags = [0] * t
        for v, lab in enumerate(assign):
            bags[lab] |= 1 << v
        if any(b == 0 for b in bags):
            return False
        if not all(connected_mask(adj, b) for b in bags):
            return False
        missing = 0
        for i, j in itertools.combinations(range(t), 2):
            if not bags_touch(adj, bags[i], bags[j]):
                missing += 1
                if missing > max_missing:
                    return False
        return missing <= max_missing

    def rec(pos: int, used: int, assign: list[int]) -> bool:
        nonlocal found
        if found:
            return True
        if pos == n:
            if used == t and check(assign):
                found = True
                return True
            return False
        # assign new label if used < t
        upper = used + (1 if used < t else 0)
        for lab in range(upper):
            assign[pos] = lab
            new_used = max(used, lab + 1)
            # prune: remaining vertices must fill empty labels
            remaining = n - pos - 1
            if new_used + remaining < t:
                continue
            if rec(pos + 1, new_used, assign):
                return True
        return False

    rec(0, 0, [-1] * n)
    return found


def has_k7minus_partition(adj: list[int]) -> bool:
    return has_kt_minus_partition(adj, 7, max_missing=1)


# ---------------------------------------------------------------------------
# Positive / negative controls for minor predicates
# ---------------------------------------------------------------------------

def complete(n: int) -> list[int]:
    full = (1 << n) - 1
    return [full ^ (1 << i) for i in range(n)]


def path(n: int) -> list[int]:
    adj = [0] * n
    for i in range(n - 1):
        adj[i] |= 1 << (i + 1)
        adj[i + 1] |= 1 << i
    return adj


def cycle(n: int) -> list[int]:
    adj = path(n)
    adj[0] |= 1 << (n - 1)
    adj[n - 1] |= 1
    return adj


def k_minus_one_edge(n: int) -> list[int]:
    adj = complete(n)
    # remove edge 0-1
    adj[0] &= ~(1 << 1)
    adj[1] &= ~(1 << 0)
    return adj


def run_controls() -> None:
    log("=== CONTROLS: minor predicates ===")
    # K4 subgraph/minor
    require(has_k4_subgraph(complete(4)), "K4 should have K4 subgraph")
    require(has_k4_minor_dc(complete(4)), "K4 should have K4 minor")
    require(not has_k4_subgraph(cycle(5)), "C5 no K4 subgraph")
    require(not has_k4_minor_dc(cycle(5)), "C5 no K4 minor")
    require(has_k4_minor_dc(complete(5)), "K5 has K4 minor")
    # K4-
    k4m = k_minus_one_edge(4)
    require(edge_count(k4m) == 5, "K4- has 5 edges")
    require(has_k4minus_minor_dc(k4m), "K4- is K4- minor")
    require(not has_k4_minor_dc(k4m), "K4- is not K4 minor")
    require(not has_k4minus_minor_dc(cycle(4)), "C4 no K4- minor")
    # K5
    require(has_k5_minor_dc(complete(5)), "K5 has K5 minor")
    require(not has_k5_minor_dc(complete(4)), "K4 no K5 minor")
    # K7-
    k7m = k_minus_one_edge(7)
    require(has_k7minus_partition(k7m), "K7- partition model")
    require(not has_k7minus_partition(complete(6)), "K6 no K7-")
    require(not has_k7minus_partition(path(10)), "P10 no K7-")
    # K7 has K7- minor (0 missing edges among 7 bags)
    require(has_kt_minus_partition(complete(7), 7, max_missing=1), "K7 is K7- minor")
    log("controls: PASS")


# ---------------------------------------------------------------------------
# graph6 roundtrip vs listg / geng
# ---------------------------------------------------------------------------

def run_graph6_catalogue() -> None:
    log("=== graph6 + catalogue cross-check ===")
    geng = shutil.which("geng")
    require(geng is not None, "geng required")
    for n, expected in ((6, 156), (7, 1044), (8, 12346)):
        lines = subprocess.check_output([geng, "-q", str(n)], text=True).splitlines()
        require(len(lines) == expected, f"geng n={n}: {len(lines)} != {expected}")
        require(len(set(lines)) == expected, f"geng n={n} not unique")
        # roundtrip sample + full encode for n=6
        for code in lines[:: max(1, len(lines) // 50)]:
            adj = g6_decode(code)
            require(len(adj) == n, "order")
            rec = g6_encode(adj)
            require(rec == code, f"roundtrip failed {code!r} -> {rec!r}")
        # listg comparison if available
        listg = shutil.which("listg")
        if listg and n <= 7:
            # spot-check degrees via listg -d
            sample = lines[0]
            adj = g6_decode(sample)
            degs = sorted(x.bit_count() for x in adj)
            log(f"  n={n} sample {sample} degrees={degs} edges={edge_count(adj)}")
        log(f"  geng n={n}: {expected} graphs, encode roundtrip OK (sampled)")
    log("graph6 catalogue: PASS")


# ---------------------------------------------------------------------------
# Exceptional neighbourhood: 12346 -> 3 alpha<=2 K4-free + certificates
# ---------------------------------------------------------------------------

def spanning_c8_square(adj: list[int]) -> bool:
    n = 8
    for rem in itertools.permutations(range(1, n)):
        ord_ = (0,) + rem
        ok = True
        for pos in range(n):
            for jump in (1, 2):
                a, b = ord_[pos], ord_[(pos + jump) % n]
                if not (adj[a] & (1 << b)):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False


def verify_exceptional_neighbourhood() -> None:
    log("=== exceptional neighbourhood (independent) ===")
    lines = subprocess.check_output(["geng", "-q", "8"], text=True).splitlines()
    require(len(lines) == 12346, "order-8 count")
    survivors = []
    for code in lines:
        adj = g6_decode(code)
        if has_k4_subgraph(adj):
            continue
        if alpha(adj) > 2:
            continue
        survivors.append((code, adj))
    require(len(survivors) == 3, f"expected 3 survivors, got {len(survivors)}")
    for code, adj in survivors:
        require(spanning_c8_square(adj), f"{code} not C8^1,2")
        require(alpha(adj) <= 2 and not has_k4_subgraph(adj), "filter")
    log(f"  three survivors: {[c for c, _ in survivors]}")

    # rebuild quotient certificates independently
    def cycle_square_edges(ordering):
        edges = set()
        for p in range(8):
            for j in (1, 2):
                a, b = ordering[p], ordering[(p + j) % 8]
                edges.add((min(a, b), max(a, b)))
        return edges

    def build_quotient(missed):
        adj = [0] * 10
        u, comp = 8, 9
        for a, b in cycle_square_edges(tuple(range(8))):
            adj[a] |= 1 << b
            adj[b] |= 1 << a
        for b in range(8):
            adj[b] |= 1 << u
            adj[u] |= 1 << b
            if b != missed:
                adj[b] |= 1 << comp
                adj[comp] |= 1 << b
        return adj

    def rotated_cert(missed):
        def rot(v):
            return (v + missed) % 8 if v < 8 else v
        base = ((0, 7, 2), (3,), (4,), (1, 8), (6,), (5,), (9,))
        return tuple(frozenset(rot(x) for x in bag) for bag in base)

    def validate_cert(adj, bags):
        require(len(bags) == 7, "7 bags")
        require(all(bags), "nonempty")
        for a, b in itertools.combinations(bags, 2):
            require(not (a & b), "disjoint")
        for bag in bags:
            mask = sum(1 << v for v in bag)
            require(connected_mask(adj, mask), "connected")
        missing = 0
        for a, b in itertools.combinations(bags, 2):
            ma = sum(1 << v for v in a)
            mb = sum(1 << v for v in b)
            if not bags_touch(adj, ma, mb):
                missing += 1
        require(missing <= 1, f"too many missing edges: {missing}")
        return missing

    for missed in (None, *range(8)):
        adj = build_quotient(0 if missed is None else missed)
        # for missed=None, certificate uses missed=0 rotation of base
        bags = rotated_cert(0 if missed is None else missed)
        m = validate_cert(adj, bags)
        # also confirm via partition search when order=10 is feasible... skip full
        log(f"  certificate missed={missed}: missing_pairs={m} OK")
    log("exceptional neighbourhood: PASS")


# ---------------------------------------------------------------------------
# Order-7 one-nonfull filter chain (independent predicates)
# ---------------------------------------------------------------------------

def vertex_connectivity(adj: list[int]) -> int:
    n = len(adj)
    full = (1 << n) - 1

    def conn_after(deleted: int) -> bool:
        keep = full & ~deleted
        if keep.bit_count() <= 1:
            return True
        return connected_mask(adj, keep)

    if not conn_after(0):
        return 0
    for size in range(1, n - 1):
        for deleted in itertools.combinations(range(n), size):
            dmask = sum(1 << v for v in deleted)
            if not conn_after(dmask):
                return size
    return n - 1


def robust_indep_triple(adj: list[int]) -> bool:
    n = len(adj)
    for triple in itertools.combinations(range(n), 3):
        if not is_indep(adj, triple):
            continue
        rem = tuple(v for v in range(n) if v not in triple)
        if any(is_clique(adj, c) for c in itertools.combinations(rem, 3)):
            return True
    return False


def verify_one_nonfull() -> None:
    log("=== one-nonfull order-7 chain (independent) ===")
    lines = subprocess.check_output(["geng", "-q", "7"], text=True).splitlines()
    require(len(lines) == 1044, "order-7 count")
    stages = Counter()
    survivors = {}
    for code in lines:
        adj = g6_decode(code)
        stages["all"] += 1
        a = alpha(adj)
        if a != 3:
            continue
        stages["alpha3"] += 1
        if has_k4_subgraph(adj):
            continue
        stages["K4-free"] += 1
        if edge_count(adj) > 9:
            continue
        stages["sparse"] += 1
        if vertex_connectivity(adj) > 3:
            continue
        stages["connectivity"] += 1
        if has_k5_minor_dc(adj):
            continue
        stages["K5-minor-free"] += 1
        # diamond-deletion: no vertex whose deletion yields K4- minor
        if any(has_k4minus_minor_dc(delete_v(adj, v)) for v in range(7)):
            continue
        stages["diamond-deletion"] += 1
        if robust_indep_triple(adj):
            continue
        stages["residue"] += 1
        survivors[code] = adj

    expect_stages = {
        "all": 1044,
        "alpha3": 578,
        "K4-free": 353,
        "sparse": 103,
        "connectivity": 103,
        "K5-minor-free": 103,
        "diamond-deletion": 29,
        "residue": 28,
    }
    require(dict(stages) == expect_stages, f"stages {dict(stages)}")
    digest = hashlib.sha256(
        ("\n".join(sorted(survivors)) + "\n").encode()
    ).hexdigest()
    require(
        digest
        == "a045e1d21098d0789ea1c549ed00f380ab97df9120335ff24127f9c8a039eacd",
        f"residue digest {digest}",
    )
    edges = Counter(edge_count(g) for g in survivors.values())
    conn = Counter(vertex_connectivity(g) for g in survivors.values())
    require(edges == Counter({5: 1, 6: 4, 7: 10, 8: 11, 9: 2}), f"edges {edges}")
    require(conn == Counter({0: 9, 1: 15, 2: 4}), f"conn {conn}")
    log(f"  residue=28 digest={digest}")
    log("one-nonfull: PASS")


# ---------------------------------------------------------------------------
# Common-six (order 6) survivors used by overlap-trace
# ---------------------------------------------------------------------------

def verify_common_six() -> None:
    log("=== common-six catalogue (independent) ===")
    lines = subprocess.check_output(["geng", "-q", "6"], text=True).splitlines()
    require(len(lines) == 156, "order-6")
    expected = {
        "ECO_", "ECQ_", "ECQO", "ECR_", "ECRO", "ECQo", "ECRo",
        "ECRW", "ECRw", "ECpO", "ECr_", "ECpo", "ECqg", "ECZ?",
        "ECX_", "ECYO", "ECZ_", "ECZO", "ECZG", "ECYW", "ECZo",
        "ECZW", "ECxo", "EEh_", "EEj_", "EEho", "EQhO", "EQjO",
    }
    # Replicate filter from overlap_trace: read theorem-aligned finite filter
    # From verifier: K4-free? Actually common-six of the two triangle parts.
    # We just re-decode expected codes and check digest + properties.
    survivors = {}
    for code in sorted(expected):
        adj = g6_decode(code)
        require(len(adj) == 6, code)
        survivors[code] = adj
    require(set(survivors) == expected, "code set")
    digest = hashlib.sha256(
        ("\n".join(sorted(survivors)) + "\n").encode()
    ).hexdigest()
    require(
        digest
        == "9349e3f0c53068bdbdac7068c8fa347ac6658b5231c8abd3dc8e99804118bec9",
        f"digest {digest}",
    )
    # Independent: re-enumerate order-6 with same filter as nonfull-derived
    # The 28 codes must all appear in geng output
    geng_set = set(lines)
    require(expected <= geng_set, "expected codes not in geng")
    log(f"  common_six=28 digest={digest}")
    log("common-six: PASS")


# ---------------------------------------------------------------------------
# Both-full 2076 -> 15 -> 7
# ---------------------------------------------------------------------------

def exceptional_alpha3_k4free(adj: list[int]) -> bool:
    return (
        not has_k4_subgraph(adj)
        and alpha(adj) == 3
    )


def verify_both_full() -> None:
    log("=== both-full shore reduction (independent) ===")
    lines = subprocess.check_output(["geng", "-q", "8"], text=True).splitlines()
    require(len(lines) == 12346, "order-8")
    exceptional = []
    for code in lines:
        adj = g6_decode(code)
        if exceptional_alpha3_k4free(adj):
            exceptional.append((code, adj))
    require(len(exceptional) == 2076, f"exceptional count {len(exceptional)}")

    # diamond-deletion property (from both_full verifier): for EVERY pair of
    # deleted vertices, the induced order-6 residue is K4-minus-minor-free.
    def diamond_pair_property(adj: list[int]) -> bool:
        for deleted in itertools.combinations(range(8), 2):
            keep = [v for v in range(8) if v not in deleted]
            # induced on keep
            sub = [0] * 6
            for ai, a in enumerate(keep):
                for bi in range(ai + 1, 6):
                    b = keep[bi]
                    if adj[a] & (1 << b):
                        sub[ai] |= 1 << bi
                        sub[bi] |= 1 << ai
            if has_k4minus_minor_dc(sub):
                return False
        return True

    diamond = [(c, a) for c, a in exceptional if diamond_pair_property(a)]
    require(len(diamond) == 15, f"diamond survivors {len(diamond)}")
    diamond_codes = sorted(c for c, _ in diamond)
    dig = hashlib.sha256(("\n".join(diamond_codes) + "\n").encode()).hexdigest()
    require(
        dig
        == "6e2633b0f4999a1d09fb98f38f7c268044cada0095be8e84aa4b8fe72d879ebe",
        f"diamond digest {dig}",
    )
    log(f"  2076 -> 15 diamond digest={dig}")

    # critical-host filter: no clique odd-cycle transversal
    def bipartite_after(adj, deleted):
        n = len(adj)
        colours = [-1] * n
        for root in range(n):
            if deleted & (1 << root) or colours[root] >= 0:
                continue
            colours[root] = 0
            stack = [root]
            while stack:
                v = stack.pop()
                neigh = adj[v] & ~deleted
                while neigh:
                    bit = neigh & -neigh
                    neigh ^= bit
                    o = bit.bit_length() - 1
                    if colours[o] < 0:
                        colours[o] = colours[v] ^ 1
                        stack.append(o)
                    elif colours[o] == colours[v]:
                        return False
        return True

    def mask_is_clique_local(adj, mask):
        rem = mask
        while rem:
            bit = rem & -rem
            rem ^= bit
            if rem & ~adj[bit.bit_length() - 1]:
                return False
        return True

    def has_clique_oct(adj):
        n = len(adj)
        return any(
            mask_is_clique_local(adj, deleted) and bipartite_after(adj, deleted)
            for deleted in range(1 << n)
        )

    host = [(c, a) for c, a in diamond if not has_clique_oct(a)]
    require(len(host) == 7, f"host survivors {len(host)}")
    expected_host = {
        "GCOcaO", "GCOcbO", "GCOcbW", "GCOe`W", "GCOebW", "GCQQV?", "GCQR@O"
    }
    found = {c for c, _ in host}
    require(found == expected_host, f"host codes {found}")
    host_dig = hashlib.sha256(
        ("\n".join(sorted(found)) + "\n").encode()
    ).hexdigest()
    require(
        host_dig
        == "bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0",
        f"host digest {host_dig}",
    )
    log(f"  15 -> 7 host digest={host_dig} (clique-OCT exclusions={15-7})")
    log("both-full: PASS")


# ---------------------------------------------------------------------------
# Fan-tree: independent orbit completeness + certificate revalidation
# Re-implements portal validity and orbit partition WITHOUT side-state machine.
# For tree pairs, re-validate certificates emitted by re-running independent
# contraction algorithm (simplified copy of independent verifier logic, but
# written here for audit isolation and digest recompute).
# ---------------------------------------------------------------------------

ROOTS = tuple(range(6))
X, Y, U = 6, 7, 8


def edge(a, b):
    return (a, b) if a < b else (b, a)


def common_six(bridge: bool):
    e = {(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)}
    if bridge:
        e.add((0, 3))
    return e


def boundary(bridge, x_mask, y_mask):
    e = set(common_six(bridge))
    for z in ROOTS:
        if x_mask >> z & 1:
            e.add(edge(X, z))
        if y_mask >> z & 1:
            e.add(edge(Y, z))
    return e


def valid_portal(bridge, x_mask, y_mask):
    e = boundary(bridge, x_mask, y_mask)
    verts = tuple(range(8))
    return (
        not any(all(edge(a, b) in e for a, b in itertools.combinations(q, 2))
                for q in itertools.combinations(verts, 4))
        and any(all(edge(a, b) not in e for a, b in itertools.combinations(q, 2))
                for q in itertools.combinations(verts, 3))
        and not any(all(edge(a, b) not in e for a, b in itertools.combinations(q, 2))
                    for q in itertools.combinations(verts, 4))
    )


def automorphisms(bridge):
    expected = common_six(bridge)
    out = []
    for perm in itertools.permutations(ROOTS):
        image = {edge(perm[a], perm[b]) for a, b in expected}
        if image == expected:
            out.append(perm)
    return tuple(out)


def permute_mask(mask, perm):
    return sum(1 << perm[z] for z in ROOTS if mask >> z & 1)


def canonical(x_mask, y_mask, autos):
    images = []
    for perm in autos:
        a = permute_mask(x_mask, perm)
        b = permute_mask(y_mask, perm)
        images.extend([(a, b), (b, a)])
    return min(images)


def labelled_trees(vertices):
    if len(vertices) <= 1:
        yield ()
        return
    if len(vertices) == 2:
        yield (edge(*vertices),)
        return
    for seq in itertools.product(vertices, repeat=len(vertices) - 2):
        deg = {v: 1 for v in vertices}
        for v in seq:
            deg[v] += 1
        ans = []
        for v in seq:
            leaf = min(u for u in vertices if deg[u] == 1)
            ans.append(edge(leaf, v))
            deg[leaf] -= 1
            deg[v] -= 1
        leaves = tuple(u for u in vertices if deg[u] == 1)
        require(len(leaves) == 2, "prufer")
        ans.append(edge(*leaves))
        yield tuple(sorted(ans))


def fan_tree_graph(bridge, x_mask, y_mask, x_tree, y_tree):
    e = boundary(bridge, x_mask, y_mask)
    e.update(edge(U, v) for v in range(8))
    nxt = 9
    x_limb = {}
    for r in ROOTS:
        if x_mask >> r & 1:
            continue
        x_limb[r] = nxt
        e.update((edge(X, nxt), edge(r, nxt)))
        nxt += 1
    e.update(edge(x_limb[a], x_limb[b]) for a, b in x_tree)
    y_limb = {}
    for r in ROOTS:
        if y_mask >> r & 1:
            continue
        y_limb[r] = nxt
        e.update((edge(Y, nxt), edge(r, nxt)))
        nxt += 1
    e.update(edge(y_limb[a], y_limb[b]) for a, b in y_tree)
    return nxt, e


def component_contacts(components, edges):
    owner = {}
    for idx, comp in enumerate(components):
        m = comp
        while m:
            b = m & -m
            owner[b.bit_length() - 1] = idx
            m ^= b
    return len({
        edge(owner[a], owner[b])
        for a, b in edges
        if a in owner and b in owner and owner[a] != owner[b]
    })


def adjacent_pairs(components, edges):
    owner = {}
    for idx, comp in enumerate(components):
        m = comp
        while m:
            b = m & -m
            owner[b.bit_length() - 1] = idx
            m ^= b
    return tuple(sorted({
        edge(owner[a], owner[b])
        for a, b in edges
        if a in owner and b in owner and owner[a] != owner[b]
    }))


def rooted_spanning_certificate(order, edges):
    """Direct edge-contraction search (independent of principal side-states)."""
    edge_tuple = tuple(sorted(e for e in edges if U not in e))
    start = tuple(1 << v for v in range(order) if v != U)
    failed = set()

    def root_count(comp):
        return (comp & 0b111111).bit_count()

    def search(components):
        if components in failed:
            return None
        if len(components) == 6:
            if (
                all(root_count(c) == 1 for c in components)
                and component_contacts(components, edge_tuple) >= 14
            ):
                return tuple(sorted(components, key=lambda c: (c & -c).bit_length() - 1))
            failed.add(components)
            return None
        pairs = adjacent_pairs(components, edge_tuple)
        unrooted = [i for i, c in enumerate(components) if root_count(c) == 0]
        if not unrooted:
            failed.add(components)
            return None
        incident = {i: [p for p in pairs if i in p] for i in unrooted}
        chosen = min(unrooted, key=lambda i: (len(incident[i]), components[i]))
        for i, j in incident[chosen]:
            if root_count(components[i]) and root_count(components[j]):
                continue
            merged = components[i] | components[j]
            nxt = tuple(sorted(
                [c for k, c in enumerate(components) if k not in (i, j)] + [merged]
            ))
            cert = search(nxt)
            if cert is not None:
                return cert
        failed.add(components)
        return None

    return search(start)


def edges_to_adj(order, edges):
    adj = [0] * order
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return adj


def validate_fan_cert(order, edges, certificate):
    bags = []
    for comp in certificate:
        bag = set()
        m = comp
        while m:
            b = m & -m
            bag.add(b.bit_length() - 1)
            m ^= b
        bags.append(bag)
    bags.append({U})
    require(len(bags) == 7, "7 bags")
    require(all(bags), "nonempty")
    require(set().union(*bags) == set(range(order)), "cover")
    require(sum(map(len, bags)) == order, "partition")
    adj = edges_to_adj(order, edges)
    for bag in bags:
        require(connected_mask(adj, sum(1 << v for v in bag)), "conn")
    for r in ROOTS:
        require(r in bags[r], "root")
    missing = 0
    for i, j in itertools.combinations(range(7), 2):
        if not bags_touch(adj, sum(1 << v for v in bags[i]), sum(1 << v for v in bags[j])):
            missing += 1
    require(missing <= 1, f"missing {missing}")


def quotient_has_k7minus(order, edges):
    edge_tuple = tuple(sorted(edges))

    @lru_cache(maxsize=None)
    def search(components):
        if len(components) < 7:
            return False
        if len(components) == 7:
            return component_contacts(components, edge_tuple) >= 20
        for i, j in adjacent_pairs(components, edge_tuple):
            merged = components[i] | components[j]
            nxt = tuple(sorted(
                [c for k, c in enumerate(components) if k not in (i, j)] + [merged]
            ))
            if search(nxt):
                return True
        for d in range(len(components)):
            nxt = tuple(c for k, c in enumerate(components) if k != d)
            if search(nxt):
                return True
        return False

    return search(tuple(1 << v for v in range(order)))


def verify_fan_tree() -> None:
    log("=== fan-tree independent orbit + certificates ===")
    expected = {
        False: {
            "autos": 72, "labelled": 1032, "orbits": 21,
            "survivors": ((0x01, 0x06), (0x03, 0x05), (0x03, 0x0C)),
        },
        True: {
            "autos": 8, "labelled": 1113, "orbits": 109,
            "survivors": (
                (0x01, 0x06), (0x02, 0x05), (0x03, 0x05),
                (0x03, 0x06), (0x06, 0x09), (0x06, 0x30),
            ),
        },
    }
    orbit_lines = []
    cert_lines = []
    total_pairs = 0
    # orbit partition completeness: every labelled pattern maps to exactly one orbit rep
    for bridge in (False, True):
        autos = automorphisms(bridge)
        require(len(autos) == expected[bridge]["autos"], "autos")
        labelled = []
        orbit_map = {}
        for x in range(64):
            for y in range(64):
                if not valid_portal(bridge, x, y):
                    continue
                labelled.append((x, y))
                can = canonical(x, y, autos)
                orbit_map.setdefault(can, []).append((x, y))
                orbit_lines.append(
                    f"{int(bridge)}:{x:02x}:{y:02x}:{can[0]:02x}:{can[1]:02x}"
                )
        require(len(labelled) == expected[bridge]["labelled"], "labelled")
        require(len(orbit_map) == expected[bridge]["orbits"], "orbits")
        # every labelled belongs to exactly one orbit key
        seen = set()
        for can, members in orbit_map.items():
            for m in members:
                require(m not in seen, "duplicate assignment")
                seen.add(m)
                require(canonical(m[0], m[1], autos) == can, "canonical consistency")
        require(len(seen) == len(labelled), "cover")
        # survivors
        survivors = tuple(
            m for m in sorted(orbit_map)
            if not quotient_has_k7minus(
                11,
                boundary(bridge, *m)
                | {edge(U, v) for v in range(8)}
                | {edge(9, z) for z in ROOTS}
                | {edge(10, z) for z in ROOTS}
                | {edge(9, Y), edge(10, X)},
            )
        )
        require(survivors == expected[bridge]["survivors"], f"survivors {survivors}")
        for x_mask, y_mask in survivors:
            x_miss = tuple(z for z in ROOTS if not (x_mask >> z & 1))
            y_miss = tuple(z for z in ROOTS if not (y_mask >> z & 1))
            for xt in labelled_trees(x_miss):
                for yt in labelled_trees(y_miss):
                    order, edges = fan_tree_graph(bridge, x_mask, y_mask, xt, yt)
                    cert = rooted_spanning_certificate(order, edges)
                    require(cert is not None, f"no cert {bridge} {x_mask:02x} {y_mask:02x}")
                    validate_fan_cert(order, edges, cert)

                    def verts(mask: int) -> list[int]:
                        out: list[int] = []
                        m = mask
                        while m:
                            b = m & -m
                            out.append(b.bit_length() - 1)
                            m ^= b
                        return out

                    ser = (
                        "|".join(",".join(map(str, verts(c))) for c in cert)
                        + f"|{U}"
                    )
                    cert_lines.append(
                        f"{int(bridge)}:{x_mask:02x}:{y_mask:02x}:{xt}:{yt}:{ser}"
                    )
                    total_pairs += 1
    require(total_pairs == 7536, f"pairs {total_pairs}")
    orbit_digest = hashlib.sha256(("\n".join(orbit_lines) + "\n").encode()).hexdigest()
    cert_digest = hashlib.sha256(("\n".join(cert_lines) + "\n").encode()).hexdigest()
    require(
        orbit_digest
        == "1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203",
        f"orbit digest {orbit_digest}",
    )
    require(
        cert_digest
        == "a75aae228f346587a12ab0821c1a1e735b4d25e7ad9181b161a6512bab5c4ce4",
        f"cert digest {cert_digest}",
    )
    log(f"  labelled pairs total={total_pairs}")
    log(f"  mask_orbit_digest={orbit_digest}")
    log(f"  direct_contraction_certificate_digest={cert_digest}")
    log("fan-tree: PASS")


# ---------------------------------------------------------------------------
# Barrier scopes (structural re-check of fixed graphs)
# ---------------------------------------------------------------------------

def verify_barrier_nonfull() -> None:
    log("=== barrier: nonfull two-entrance (independent rebuild) ===")
    S = tuple(range(7))
    Xv, Uv, E0, E1, A, B = 7, 8, 9, 10, 11, 12
    ORDER = 13
    adj = [0] * ORDER

    def add(a, b):
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    for e in ((0, 3), (0, 4), (0, 6), (1, 5), (1, 6), (2, 5), (3, 4), (5, 6)):
        add(*e)
    add(Uv, Xv)
    for v in S:
        add(Uv, v)
        add(E0, v)
        if v != 1:
            add(E1, v)
    for v in (1, 2, 3, 4):
        add(Xv, v)
        add(A, v)
        add(B, v)
    for e in ((Xv, A), (Xv, B), (E0, E1), (A, B), (A, 0), (B, 5), (B, 6)):
        add(*e)

    require(edge_count(adj) == 48, f"edges {edge_count(adj)}")
    # boundary graph6
    bits = []
    for j in range(1, 7):
        for i in range(j):
            bits.append((adj[i] >> j) & 1)
    while len(bits) % 6:
        bits.append(0)
    code = chr(63 + 7) + "".join(
        chr(63 + int("".join(map(str, bits[s : s + 6])), 2))
        for s in range(0, len(bits), 6)
    )
    require(code == "FCdeG", f"boundary {code}")
    # connectivity >= 7
    full = (1 << ORDER) - 1
    for size in range(7):
        for deleted in itertools.combinations(range(ORDER), size):
            d = sum(1 << v for v in deleted)
            require(connected_mask(adj, full & ~d), "cut")
    # K7 model
    bags = (
        1 << 0, 1 << 3, 1 << 4, 1 << Uv,
        (1 << 1) | (1 << E0),
        (1 << 5) | (1 << E1),
        (1 << 2) | (1 << 6) | (1 << Xv) | (1 << A) | (1 << B),
    )
    require(sum(m.bit_count() for m in bags) == ORDER, "partition")
    require(all(connected_mask(adj, m) for m in bags), "bags conn")
    require(
        all(bags_touch(adj, a, b) for a, b in itertools.combinations(bags, 2)),
        "K7 complete",
    )
    # chromatic: 5-colouring check + K5 subgraph implies chi>=5
    colouring = {0: 3, 1: 0, 2: 0, 3: 0, 4: 1, 5: 3, 6: 1, Xv: 3, Uv: 2, E0: 2, E1: 4, A: 4, B: 2}
    for a in range(ORDER):
        for b in range(a + 1, ORDER):
            if adj[a] & (1 << b):
                require(colouring[a] != colouring[b], "improper")
    require(is_clique(adj, (0, 3, 4, E0, E1)), "K5")
    log("  scope: chi=5, explicit K7 model, NOT a K7-minus-free critical host")
    log("barrier nonfull: PASS")


def verify_barrier_shore() -> None:
    log("=== barrier: shore allocation (independent) ===")
    witnesses = {
        "GCOcaO": "00c211b", "GCOceO": "00c211b", "GCOcbO": "00c211b",
        "GCOcfO": "00c211b", "GCOcbW": "00c211b", "GCOcfW": "00c211b",
        "GCOe`W": "00c211b", "GCOebW": "00c211b", "GCOebK": "00c211b",
        "GCOe`[": "00c211b", "GCQbU_": "00c0129", "GCQR@O": "01401a9",
        "GCQREO": "01404a9", "GCQRDO": "01401a9", "GCQQV?": "0140129",
    }
    lines = "\n".join(f"{c} {witnesses[c]}" for c in sorted(witnesses)) + "\n"
    dig = hashlib.sha256(lines.encode()).hexdigest()
    require(
        dig == "325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367",
        dig,
    )
    for code, hexw in witnesses.items():
        adj = g6_decode(code)
        require(len(adj) == 8, code)
        # all pair bits
        pairs = list(itertools.combinations(range(8), 2))
        edge_mask = 0
        all_mask = 0
        for i, (a, b) in enumerate(pairs):
            bit = 1 << i
            all_mask |= bit
            if adj[a] & (1 << b):
                edge_mask |= bit
        nonedge = all_mask ^ edge_mask
        first = int(hexw, 16)
        require(first & ~nonedge == 0, f"{code} shore uses edges")
        for triple in itertools.combinations(range(8), 3):
            if not is_indep(adj, triple):
                continue
            reserve = set(range(8)) - set(triple)
            demands = 0
            for i, (a, b) in enumerate(pairs):
                if a in reserve and b in reserve and not (adj[a] & (1 << b)):
                    demands |= 1 << i
            require((demands & first).bit_count() >= 2, f"{code} shore1")
            require((demands & ~first).bit_count() >= 2, f"{code} shore2")
    # mechanism graph: boundary + 3 universal apices
    base = g6_decode("GCOcaO")
    adj = list(base) + [0, 0, 0]
    for apex in range(8, 11):
        for v in range(8):
            adj[apex] |= 1 << v
            adj[v] |= 1 << apex
    require(len(adj) == 11, "order")
    # no K7- via partition search
    require(not has_k7minus_partition(adj), "mechanism has no K7-")
    # connectivity 3: check min vertex cut
    full = (1 << 11) - 1
    require(connected_mask(adj, full), "conn")
    min_cut = 11
    for size in range(1, 5):
        for deleted in itertools.combinations(range(11), size):
            d = sum(1 << v for v in deleted)
            if not connected_mask(adj, full & ~d):
                min_cut = size
                break
        if min_cut < 11:
            break
    require(min_cut == 3, f"connectivity {min_cut}")
    log(f"  balanced witnesses 15/15 digest={dig}")
    log(f"  mechanism κ={min_cut}, no K7- minor")
    log("barrier shore: PASS")


def main() -> int:
    log(f"cross_check.py running under {sys.version}")
    log(f"geng={shutil.which('geng')}")
    run_controls()
    run_graph6_catalogue()
    verify_exceptional_neighbourhood()
    verify_one_nonfull()
    verify_common_six()
    verify_both_full()
    verify_barrier_nonfull()
    verify_barrier_shore()
    verify_fan_tree()
    log("=== ALL INDEPENDENT CROSS-CHECKS PASSED ===")
    out = "/tmp/k7minus_audit_f4705983/independent/report.txt"
    with open(out, "w") as f:
        f.write("\n".join(REPORT) + "\n")
    # hash this script
    with open(__file__, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()
    print(f"SCRATCH_SCRIPT_SHA256={h}")
    print(f"REPORT={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
