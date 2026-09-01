#!/usr/bin/env python3
"""Hostile fixed-graph search for the labelled weighted-splitter theorem.

For a supplied graph6 graph C, search over all 8-label incidence matrices for
one satisfying every boundary inequality, avoiding terminal outcomes A/B/D,
and blocking every graph-theoretically 3-contractible edge by an exact tight
witness X disjoint from its endpoints.

This is exploratory finite evidence, not an unbounded theorem.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from hashlib import sha256
from itertools import combinations

import networkx as nx
import z3


def bit_graph(g: nx.Graph) -> tuple[int, ...]:
    g = nx.convert_node_labels_to_integers(g, ordering="sorted")
    return tuple(sum(1 << w for w in g.neighbors(v)) for v in range(len(g)))


def is_connected(a: tuple[int, ...], mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        new = a[bit.bit_length() - 1] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def is_three_connected(a: tuple[int, ...]) -> bool:
    n = len(a)
    if n < 4:
        return False
    full = (1 << n) - 1
    for k in range(3):
        for deleted in combinations(range(n), k):
            mask = full
            for v in deleted:
                mask ^= 1 << v
            if not is_connected(a, mask):
                return False
    return True


def touches(a: tuple[int, ...], left: int, right: int) -> bool:
    union = 0
    rest = left
    while rest:
        bit = rest & -rest
        rest ^= bit
        union |= a[bit.bit_length() - 1]
    return bool(union & right)


def boundary_mask(a: tuple[int, ...], mask: int) -> int:
    ans = 0
    rest = mask
    while rest:
        bit = rest & -rest
        rest ^= bit
        ans |= a[bit.bit_length() - 1]
    return ans & ~mask


def contract(a: tuple[int, ...], u: int, v: int) -> tuple[int, ...]:
    """Contract edge uv, keeping u's position and deleting v's position."""
    assert u < v and (a[u] >> v) & 1
    old_n = len(a)
    kept = [x for x in range(old_n) if x != v]
    old_to_new = {x: i for i, x in enumerate(kept)}
    edges: set[tuple[int, int]] = set()
    for x in range(old_n):
        for y in range(x + 1, old_n):
            if not ((a[x] >> y) & 1):
                continue
            xx = u if x == v else x
            yy = u if y == v else y
            if xx == yy:
                continue
            edges.add(tuple(sorted((old_to_new[xx], old_to_new[yy]))))
    out = [0] * (old_n - 1)
    for x, y in edges:
        out[x] |= 1 << y
        out[y] |= 1 << x
    return tuple(out)


def connected_masks(a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(m for m in range(1, 1 << len(a)) if is_connected(a, m))


def triangle_models(a: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]:
    cms = connected_masks(a)
    out: list[tuple[int, int, int]] = []
    for i, left in enumerate(cms):
        for j in range(i + 1, len(cms)):
            middle = cms[j]
            if left & middle or not touches(a, left, middle):
                continue
            for right in cms[j + 1:]:
                if (left | middle) & right:
                    continue
                if touches(a, left, right) and touches(a, middle, right):
                    out.append((left, middle, right))
    return tuple(out)


def partitions_of_vertices(vertices: tuple[int, ...], number: int):
    """Unordered partitions of exactly vertices into number nonempty blocks."""
    blocks: list[int] = []

    def rec(index: int, used: int):
        if index == len(vertices):
            if used == number:
                yield tuple(blocks)
            return
        vertex = vertices[index]
        for block_index in range(min(used + 1, number)):
            if block_index == used:
                blocks.append(0)
            blocks[block_index] |= 1 << vertex
            yield from rec(index + 1, max(used, block_index + 1))
            blocks[block_index] ^= 1 << vertex
            if block_index == used:
                blocks.pop()

    yield from rec(0, 0)


def spanning_k4_models(a: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    out = []
    for bags in partitions_of_vertices(tuple(range(len(a))), 4):
        if all(is_connected(a, b) for b in bags) and all(
            touches(a, x, y) for x, y in combinations(bags, 2)
        ):
            out.append(bags)
    return tuple(out)


def quotient_edges(a: tuple[int, ...], bags: tuple[int, ...]) -> int:
    return sum(touches(a, bags[i], bags[j]) for i, j in combinations(range(6), 2))


def k6minus_models(a: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    n = len(a)
    full = (1 << n) - 1
    out: list[tuple[int, ...]] = []
    for used in range(1, full + 1):
        if used.bit_count() < 6:
            continue
        vertices = tuple(v for v in range(n) if (used >> v) & 1)
        for bags in partitions_of_vertices(vertices, 6):
            if all(is_connected(a, b) for b in bags) and quotient_edges(a, bags) >= 14:
                out.append(bags)
    return tuple(out)


def union_count(incidence: list[list[z3.BoolRef]], mask: int) -> z3.ArithRef:
    terms = []
    for label in range(8):
        terms.append(
            z3.If(
                z3.Or(
                    *[
                        incidence[v][label]
                        for v in range(len(incidence))
                        if (mask >> v) & 1
                    ]
                ),
                1,
                0,
            )
        )
    return z3.Sum(terms)


def contractible_edges(a: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    out = []
    for u in range(len(a)):
        for v in range(u + 1, len(a)):
            if (a[u] >> v) & 1 and is_three_connected(contract(a, u, v)):
                out.append((u, v))
    return tuple(out)


def tight_witnesses(a: tuple[int, ...], u: int, v: int) -> tuple[tuple[int, int], ...]:
    """Pairs (X, required weight) that can block contraction of uv."""
    forbidden = (1 << u) | (1 << v)
    out = []
    for mask in range(1, 1 << len(a)):
        if mask & forbidden:
            continue
        boundary = boundary_mask(a, mask)
        if not ((boundary >> u) & 1 and (boundary >> v) & 1):
            continue
        required = 7 - boundary.bit_count()
        if 0 <= required <= 8:
            out.append((mask, required))
    return tuple(out)


def solve_graph(
    g: nx.Graph,
    timeout_ms: int,
    witness_path: str | None,
    require_small_atom: bool,
    atom_size: int | None,
    atom_weight: int | None,
) -> dict:
    a = bit_graph(g)
    assert is_three_connected(a)
    n = len(a)
    triangles = triangle_models(a)
    k4s = spanning_k4_models(a)
    k6s = k6minus_models(a)
    cedges = contractible_edges(a)
    witnesses = {(u, v): tight_witnesses(a, u, v) for u, v in cedges}
    small_atoms: list[tuple[int, int]] = []
    for mask in range(1, 1 << n):
        if mask.bit_count() > 3 or not is_connected(a, mask):
            continue
        boundary = boundary_mask(a, mask)
        required = 7 - boundary.bit_count()
        if not 0 <= required <= 3:
            continue
        if atom_size is not None and mask.bit_count() != atom_size:
            continue
        if atom_weight is not None and required != atom_weight:
            continue
        if any(((boundary >> u) & 1) and ((boundary >> v) & 1) for u, v in cedges):
            small_atoms.append((mask, required))
    incidence = [[z3.Bool(f"x_{v}_{ell}") for ell in range(8)] for v in range(n)]
    counts = {mask: union_count(incidence, mask) for mask in range(1, 1 << n)}
    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    for mask, count in counts.items():
        solver.add(count + boundary_mask(a, mask).bit_count() >= 7)
    for bags in triangles:
        solver.add(z3.Or(*[counts[bag] <= 3 for bag in bags]))
    for bags in k4s:
        solver.add(z3.Or(*[counts[bag] <= 2 for bag in bags]))
    for bags in k6s:
        solver.add(z3.Or(*[counts[bag] == 0 for bag in bags]))
    for edge_witnesses in witnesses.values():
        solver.add(
            z3.Or(
                *[
                    counts[mask] == required
                    for mask, required in edge_witnesses
                ]
            )
        )
    if require_small_atom:
        solver.add(z3.Or(*[counts[mask] == required for mask, required in small_atoms]))

    status = solver.check()
    graph6 = (
        nx.to_graph6_bytes(nx.convert_node_labels_to_integers(g), header=False)
        .strip()
        .decode()
    )
    result = {
        "n": n,
        "graph6": graph6,
        "edges": g.number_of_edges(),
        "degrees": sorted(dict(g.degree()).values()),
        "triangles": len(triangles),
        "k4_models": len(k4s),
        "k6minus_models": len(k6s),
        "contractible_edges": [list(e) for e in cedges],
        "tight_witness_candidates": {f"{u}-{v}": len(witnesses[u, v]) for u, v in cedges},
        "status": str(status),
        "required_small_atom": require_small_atom,
        "small_atom_filter": [atom_size, atom_weight],
        "small_atom_candidates": {
            f"{size}-{weight}": sum(
                mask.bit_count() == size and required == weight
                for mask, required in small_atoms
            )
            for size in range(1, 4)
            for weight in range(4)
        },
    }
    if status == z3.sat:
        model = solver.model()
        labels = []
        for v in range(n):
            mask = 0
            for ell in range(8):
                if z3.is_true(model.eval(incidence[v][ell], model_completion=True)):
                    mask |= 1 << ell
            labels.append(mask)
        chosen = {}
        for edge, edge_witnesses in witnesses.items():
            for mask, required in edge_witnesses:
                value = model.eval(counts[mask], model_completion=True).as_long()
                if value == required:
                    chosen[f"{edge[0]}-{edge[1]}"] = mask
                    break
        result["label_masks"] = labels
        result["chosen_blockers"] = chosen
        result["chosen_small_atoms"] = [
            mask
            for mask, required in small_atoms
            if model.eval(counts[mask], model_completion=True).as_long() == required
        ]
        if witness_path:
            with open(witness_path, "w", encoding="utf-8") as handle:
                json.dump(result, handle, indent=2, sort_keys=True)
                handle.write("\n")
    return result


def read_graph6_lines(stream):
    for raw in stream:
        raw = raw.strip()
        if not raw or raw.startswith(">"):
            continue
        yield nx.from_graph6_bytes(raw.encode())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph6")
    parser.add_argument("--stdin", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("--witness", default="/tmp/k44_splitter_witness.json")
    parser.add_argument("--require-small-atom", action="store_true")
    parser.add_argument("--atom-size", type=int, choices=(1, 2, 3))
    parser.add_argument("--atom-weight", type=int, choices=(0, 1, 2, 3))
    parser.add_argument("--max-cubic", type=int)
    parser.add_argument("--summary-only", action="store_true")
    args = parser.parse_args()

    jobs: list[nx.Graph] = []
    if args.graph6:
        jobs.append(nx.from_graph6_bytes(args.graph6.encode()))
    if args.stdin:
        jobs.extend(read_graph6_lines(sys.stdin))
    records = []
    skipped_cubic = 0
    for g in jobs:
        cubic_vertices = sum(degree == 3 for _, degree in g.degree())
        if args.max_cubic is not None and cubic_vertices > args.max_cubic:
            skipped_cubic += 1
            continue
        a = bit_graph(g)
        if not is_three_connected(a):
            result = {
                "graph6": nx.to_graph6_bytes(g, header=False).strip().decode(),
                "status": "not-3-connected",
            }
            records.append(result)
            if not args.summary_only:
                print(json.dumps(result, sort_keys=True), flush=True)
            continue
        result = solve_graph(
            g,
            args.timeout_ms,
            args.witness,
            args.require_small_atom,
            args.atom_size,
            args.atom_weight,
        )
        records.append(result)
        if not args.summary_only:
            print(json.dumps(result, sort_keys=True), flush=True)
        if result["status"] == "sat":
            return
    if args.summary_only:
        stable_keys = (
            "graph6",
            "status",
            "triangles",
            "k4_models",
            "k6minus_models",
            "contractible_edges",
            "tight_witness_candidates",
            "small_atom_candidates",
        )
        stable_records = sorted(
            ({key: record.get(key) for key in stable_keys} for record in records),
            key=lambda record: record["graph6"],
        )
        encoded = json.dumps(
            stable_records, sort_keys=True, separators=(",", ":")
        ).encode()
        print("input_graphs", len(jobs))
        print("skipped_by_cubic_filter", skipped_cubic)
        print("eligible_graphs", len(records))
        print("statuses", dict(sorted(Counter(r["status"] for r in records).items())))
        print("stable_records_sha256", sha256(encoded).hexdigest())


if __name__ == "__main__":
    main()
