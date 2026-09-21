#!/usr/bin/env python3
"""Exact finite probes of the C21 five-root, two-helper candidate.

Vertices 0..4 are prescribed roots; all other vertices are nonroots.
Root-root edges are irrelevant to both 4-lightness and this minor target,
so the generators omit them.  This is a finite test, not an unbounded proof.

Run with ``uv run python3 active/hc7_c21_helper_search.py sanity`` or
``... exhaustive --nonroots 4`` or ``... random --trials 1000``.
Only the standard library is used.  The production solver enumerates every
connected helper pair and minimal connected root-bag candidates.  A separate
checker enumerates vertex assignments for small sanity examples.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
import json
import random
import subprocess
import time

Graph = tuple[int, ...]
Model = tuple[int, ...]


def bits(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def graph(m: int, internal: int, columns: tuple[int, ...]) -> Graph:
    adj = [0] * (m + 5)
    edges = [(r, v + 5) for r, column in enumerate(columns) for v in bits(column)]
    edges.extend((a + 5, b + 5) for k, (a, b) in enumerate(combinations(range(m), 2)) if internal >> k & 1)
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return tuple(adj)


def from_edges(n: int, edges: list[tuple[int, int]]) -> Graph:
    adj = [0] * n
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return tuple(adj)


def neighbourhood(adj: Graph, mask: int) -> int:
    result = 0
    for v in bits(mask):
        result |= adj[v]
    return result & ~mask


def connected(adj: Graph, mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    while True:
        new = (reached | neighbourhood(adj, reached)) & mask
        if reached == new:
            return reached == mask
        reached = new


def density(adj: Graph) -> int:
    return sum((adj[v] & ~31).bit_count() for v in range(5)) + sum((adj[v] & ~31).bit_count() for v in range(5, len(adj))) // 2 - 4 * (len(adj) - 5)


def light_witness(adj: Graph) -> tuple[int, int, int] | None:
    """Return a violating set, its external boundary, and excess; else None."""
    for sub in range(1, 1 << (len(adj) - 5)):
        chosen = sub << 5
        boundary = neighbourhood(adj, chosen)
        if boundary.bit_count() > 4:
            continue
        internal = sum((adj[v] & chosen).bit_count() for v in bits(chosen)) // 2
        crossing = sum((adj[v] & ~chosen).bit_count() for v in bits(chosen))
        excess = internal + crossing - 4 * sub.bit_count()
        if excess > 0:
            return chosen, boundary, excess
    return None


def check_model(adj: Graph, model: Model) -> int:
    """Independent check of a returned certificate using explicit vertex sets."""
    assert len(model) == 7
    bags = [set(bits(mask)) for mask in model]
    assert all(bags)
    assert all(bags[a].isdisjoint(bags[b]) for a, b in combinations(range(7), 2))
    assert all(r in bags[r] and not (bags[r] & (set(range(5)) - {r})) for r in range(5))
    assert not (bags[5] | bags[6]) & set(range(5))
    for bag in bags:
        reached = {min(bag)}
        while True:
            new = reached | {b for a in reached for b in bag if adj[a] >> b & 1}
            if new == reached:
                break
            reached = new
        assert reached == bag
    contacts = sum(any(adj[a] >> b & 1 for a in bags[i] for b in bags[j]) for i, j in [(r, h) for r in range(5) for h in (5, 6)] + [(5, 6)])
    assert contacts >= 10
    return contacts


def model(adj: Graph) -> Model | None:
    m = len(adj) - 5
    if m < 2:
        return None
    all_nonroots = ((1 << m) - 1) << 5
    subsets = sorted((sub << 5 for sub in range(1, 1 << m)), key=lambda sub: (sub.bit_count(), sub))
    helpers = [(sub, neighbourhood(adj, sub)) for sub in subsets if connected(adj, sub)]
    rooted = [tuple(sub for sub in [0, *subsets] if connected(adj, sub | (1 << r))) for r in range(5)]
    for ai, (a, na) in enumerate(helpers):
        for b, nb in helpers[ai + 1:]:
            if a & b:
                continue
            budget = int(bool(na & b))  # no helper contact consumes the one missing contact
            remaining = all_nonroots & ~(a | b)
            choices = []
            for r in range(5):
                candidates = []
                for sub in rooted[r]:
                    if sub & ~remaining:
                        continue
                    bag = sub | (1 << r)
                    missing = 2 - bool(bag & na) - bool(bag & nb)
                    if missing > budget:
                        continue
                    # A smaller bag with no more missing contacts dominates it.
                    if any(old & sub == old and cost <= missing for old, cost in candidates):
                        continue
                    candidates.append((sub, missing))
                if not candidates:
                    break
                choices.append((r, tuple(candidates)))
            if len(choices) != 5:
                continue
            choices.sort(key=lambda item: len(item[1]))

            @lru_cache(None)
            def pack(index: int, used: int, missing_left: int):
                if index == 5:
                    return ()
                root, options = choices[index]
                for sub, missing in options:
                    if sub & used or missing > missing_left:
                        continue
                    result = pack(index + 1, used | sub, missing_left - missing)
                    if result is not None:
                        return ((root, sub | (1 << root)), *result)
                return None

            packing = pack(0, 0, budget)
            if packing is not None:
                result = tuple(dict(packing)[r] for r in range(5)) + (a, b)
                check_model(adj, result)
                return result
    return None


def assignment_model(adj: Graph) -> Model | None:
    """Independent exhaustive assignment algorithm, including unused vertices."""
    for owners in product(range(8), repeat=len(adj) - 5):
        bags = [1 << r for r in range(5)] + [0, 0]
        for v, owner in enumerate(owners, 5):
            if owner < 7:
                bags[owner] |= 1 << v
        if not bags[5] or not bags[6]:
            continue
        if not all(connected(adj, bag) for bag in bags):
            continue
        contacts = sum(bool(neighbourhood(adj, bags[r]) & bags[h]) for r in range(5) for h in (5, 6)) + bool(neighbourhood(adj, bags[5]) & bags[6])
        if contacts >= 10:
            return tuple(bags)
    return None


def describe(adj: Graph) -> dict:
    return {"vertices": len(adj), "rho4": density(adj), "light_violation": light_witness(adj), "edges": [(a, b) for a in range(len(adj)) for b in range(a + 1, len(adj)) if adj[a] >> b & 1]}


def sanity() -> None:
    full = graph(2, 0, (3,) * 5)
    two_missing = graph(2, 1, (1, 2, 3, 3, 3))
    one_missing = graph(2, 1, (1, 3, 3, 3, 3))
    assert density(full) == density(one_missing) == 2
    assert density(two_missing) == 1
    assert model(full) and model(one_missing)
    assert model(two_missing) is None
    assert light_witness(full) is None
    # The documented star-replacement counterexample: roots 0..4; v,a,b,y=5..8.
    star = from_edges(9, [(5, r) for r in range(5)] + [(5, 7)] + [(a, r) for a in (6, 7) for r in (0, 1, 2)] + [(6, 7)] + [(8, a) for a in (5, 6, 7, 3, 4)])
    quotient = from_edges(8, [(a, b) for a, b in describe(star)["edges"] if b != 8] + [(5, 6)])
    assert density(star) == density(quotient) == 2
    assert light_witness(star) is None
    assert light_witness(quotient) is not None
    rng = random.Random(21)
    agree = 0
    for m in (2, 3, 4):
        for _ in range(35):
            adj = graph(m, rng.randrange(1 << (m * (m - 1) // 2)), tuple(rng.randrange(1 << m) for _ in range(5)))
            fast, independent = model(adj), assignment_model(adj)
            assert (fast is None) == (independent is None), describe(adj)
            if fast:
                check_model(adj, fast)
            agree += 1
    print(json.dumps({"sanity": "pass", "independent_assignment_comparisons": agree, "star_model": model(star), "quotient_violation": light_witness(quotient)}), flush=True)


def exhaustive(m: int, max_excess: int) -> None:
    """All labelled internal graphs; all root incidences up to root permutation."""
    start = time.monotonic()
    counts = {"density_eligible": 0, "light": 0, "models": 0}
    internal_edges = m * (m - 1) // 2
    by_weight: dict[int, list[tuple[int, ...]]] = {}
    for columns in combinations_with_replacement(range(1 << m), 5):
        by_weight.setdefault(sum(col.bit_count() for col in columns), []).append(columns)
    for internal in range(1 << internal_edges):
        for excess in range(2, max_excess + 1):
            weight = 4 * m + excess - internal.bit_count()
            for columns in by_weight.get(weight, []):
                adj = graph(m, internal, columns)
                counts["density_eligible"] += 1
                if light_witness(adj) is not None:
                    continue
                counts["light"] += 1
                result = model(adj)
                if result is None:
                    print(json.dumps({"COUNTEREXAMPLE": describe(adj), "counts": counts}), flush=True)
                    return
                counts["models"] += 1
    print(json.dumps({"exhaustive_nonroots": m, "rho_range": [2, max_excess], **counts, "seconds": round(time.monotonic() - start, 3)}), flush=True)


def randomized(trials: int, seed: int) -> None:
    rng = random.Random(seed)
    start = time.monotonic()
    counts = {"generated": 0, "light": 0, "models": 0}
    for trial in range(trials):
        m = 3 + trial % 6
        pairs = list(combinations(range(m), 2))
        kind = (trial // 6) % 4
        if kind == 0:  # random tree
            inside = {(rng.randrange(v), v) for v in range(1, m)}
        elif kind == 1:  # cycle
            inside = {tuple(sorted((v, (v + 1) % m))) for v in range(m)}
        elif kind == 2:  # arbitrary nonroot graph
            inside = {edge for edge in pairs if rng.random() < 0.5}
        else:  # clique pieces sharing a cut vertex
            split = m // 2
            inside = {edge for edge in pairs if edge[1] <= split or edge[0] >= split}
        weight = 4 * m + 2 - len(inside)
        if not 0 <= weight <= 5 * m:
            continue
        root_edges = rng.sample(range(5 * m), weight)
        columns = [0] * 5
        for edge in root_edges:
            columns[edge // m] |= 1 << (edge % m)
        internal = sum(1 << k for k, edge in enumerate(pairs) if edge in inside)
        adj = graph(m, internal, tuple(columns))
        counts["generated"] += 1
        assert density(adj) == 2
        if light_witness(adj) is not None:
            continue
        counts["light"] += 1
        result = model(adj)
        if result is None:
            print(json.dumps({"COUNTEREXAMPLE": describe(adj), "trial": trial, "seed": seed, "counts": counts}), flush=True)
            return
        counts["models"] += 1
    print(json.dumps({"random_seed": seed, **counts, "nonroots_range": [3, 8], "rho4": 2, "seconds": round(time.monotonic() - start, 3)}), flush=True)


def graph6_decode(raw: bytes) -> Graph:
    """Decode the short graph6 format used here (at most eight vertices)."""
    data = [value - 63 for value in raw.strip()]
    n = data[0]
    assert 0 <= n <= 8
    stream = [(value >> shift) & 1 for value in data[1:] for shift in range(5, -1, -1)]
    edges = [(a, b) for index, (a, b) in enumerate((a, b) for b in range(1, n) for a in range(b)) if stream[index]]
    return from_edges(n, edges)


def rooted_star(adj: Graph, roots: tuple[int, ...], forbidden: int) -> Model | None:
    """Exact K1,4 rooted model; its centre root must avoid forbidden."""
    outside = tuple(v for v in range(len(adj)) if v not in roots)
    for owners in product(range(6), repeat=len(outside)):
        bags = [1 << r for r in roots]
        for v, owner in zip(outside, owners):
            if owner < 5:
                bags[owner] |= 1 << v
        if not all(connected(adj, bag) for bag in bags):
            continue
        for index, root in enumerate(roots):
            if forbidden >> root & 1:
                continue
            adjacent = neighbourhood(adj, bags[index])
            if all(index == other or adjacent & bag for other, bag in enumerate(bags)):
                return tuple(bags)
    return None


def star_lemma() -> None:
    """Exhaust all small H/X/Z instances using nauty's unlabeled census."""
    # Independent explicit positive and negative examples.
    assert rooted_star(from_edges(5, [(0, r) for r in range(1, 5)]), tuple(range(5)), 0)
    assert rooted_star(from_edges(5, [(0, r) for r in range(1, 4)]), tuple(range(5)), 0) is None
    start = time.monotonic()
    for n in range(5, 9):
        counts = {"graphs": 0, "HX": 0, "HXZ": 0}
        process = subprocess.Popen(["geng", "-q", f"-d{min(4, n - 3)}", str(n)], stdout=subprocess.PIPE)
        assert process.stdout is not None
        for line in process.stdout:
            adj = graph6_decode(line)
            counts["graphs"] += 1
            for size in range(9 - n):
                for xtuple in combinations(range(n), size):
                    x = sum(1 << v for v in xtuple)
                    if any(adj[v] & x for v in xtuple):
                        continue
                    if any(adj[v].bit_count() < (5 - size if x >> v & 1 else 4) for v in range(n)):
                        continue
                    counts["HX"] += 1
                    for extra in combinations(tuple(v for v in range(n) if not x >> v & 1), 5 - size):
                        roots = tuple(sorted((*xtuple, *extra)))
                        counts["HXZ"] += 1
                        if rooted_star(adj, roots, x) is None:
                            print(json.dumps({"STAR_COUNTEREXAMPLE": {"n": n, "graph6": line.strip().decode(), "X": xtuple, "Z": roots, "adjacency": adj}, "counts": counts}), flush=True)
                            process.terminate()
                            process.wait()
                            return
        assert process.wait() == 0
        print(json.dumps({"star_lemma_order": n, **counts, "counterexamples": 0, "seconds": round(time.monotonic() - start, 3)}), flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("sanity", "exhaustive", "random", "star"))
    parser.add_argument("--nonroots", type=int, default=3)
    parser.add_argument("--max-excess", type=int, default=2)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=21092026)
    args = parser.parse_args()
    if args.mode == "sanity":
        sanity()
    elif args.mode == "exhaustive":
        exhaustive(args.nonroots, args.max_excess)
    elif args.mode == "star":
        star_lemma()
    else:
        randomized(args.trials, args.seed)


if __name__ == "__main__":
    main()
