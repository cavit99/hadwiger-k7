#!/usr/bin/env python3
"""Finite boundary checks for the exact-six-connectivity closure.

This verifier is dependency-free.  It does not verify the unbounded rooted
minor theorems or connectivity arguments.  It independently checks every
six-vertex boundary calculation used in the proof:

* the four-component boundary conditions are inconsistent with minimum
  boundary degree two;
* the two-component conditions force K6 minus a perfect matching;
* the three-component conditions force a cubic boundary;
* the ordered-nonedge incidence coefficients in the three-component excess
  sum are exactly those claimed.
"""

from __future__ import annotations

import hashlib
import itertools
import json

N = 6
PAIRS = tuple(itertools.combinations(range(N), 2))
PAIR_INDEX = {edge: i for i, edge in enumerate(PAIRS)}


def has_edge(mask: int, u: int, v: int) -> bool:
    if u > v:
        u, v = v, u
    return bool(mask & (1 << PAIR_INDEX[(u, v)]))


def edge_count(mask: int, vertices: tuple[int, ...] | range) -> int:
    return sum(has_edge(mask, u, v) for u, v in itertools.combinations(vertices, 2))


def degrees(mask: int) -> tuple[int, ...]:
    return tuple(sum(has_edge(mask, v, u) for u in range(N) if u != v) for v in range(N))


def complement_edges(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(edge for edge in PAIRS if not (mask & (1 << PAIR_INDEX[edge])))


def is_perfect_matching(edges: tuple[tuple[int, int], ...]) -> bool:
    if len(edges) != 3:
        return False
    used = [0] * N
    for u, v in edges:
        used[u] += 1
        used[v] += 1
    return all(value == 1 for value in used)


def main() -> None:
    total = 1 << len(PAIRS)
    r4_survivors: list[int] = []
    r2_survivors: list[int] = []
    r3_cubic: list[int] = []

    for mask in range(total):
        deg = degrees(mask)

        # Four full components: every boundary triple must span at most one
        # edge, while minimum degree in the boundary would have to be two.
        if min(deg) >= 2 and all(
            edge_count(mask, triple) <= 1
            for triple in itertools.combinations(range(N), 3)
        ):
            r4_survivors.append(mask)

        # Two full components: every five-set spans at most eight edges and
        # every boundary vertex has boundary degree at least four.
        if min(deg) >= 4 and all(
            edge_count(mask, tuple(v for v in range(N) if v != omitted)) <= 8
            for omitted in range(N)
        ):
            r2_survivors.append(mask)

        # Three full components after the rooted-diamond step: the boundary
        # has minimum degree at least three and maximum degree at most three.
        if min(deg) >= 3 and max(deg) <= 3:
            r3_cubic.append(mask)

    assert not r4_survivors

    assert len(r2_survivors) == 15
    assert {edge_count(mask, range(N)) for mask in r2_survivors} == {12}
    for mask in r2_survivors:
        missing = complement_edges(mask)
        assert is_perfect_matching(missing)
        for p, q in missing:
            roots = tuple(v for v in range(N) if v not in (p, q))
            assert edge_count(mask, roots) == 4

    assert len(r3_cubic) == 70
    for mask in r3_cubic:
        assert degrees(mask) == (3, 3, 3, 3, 3, 3)
        assert edge_count(mask, range(N)) == 9

        ordered_nonedges = tuple(
            (q, p)
            for q in range(N)
            for p in range(N)
            if p != q and not has_edge(mask, q, p)
        )
        assert len(ordered_nonedges) == 12

        vertex_occurrences = [0] * N
        root_edge_occurrences = {edge: 0 for edge in PAIRS if has_edge(mask, *edge)}
        root_edge_total = 0
        for q, p in ordered_nonedges:
            vertex_occurrences[q] += 1
            vertex_occurrences[p] += 1
            roots = tuple(v for v in range(N) if v not in (q, p))
            root_edge_total += edge_count(mask, roots)
            for edge in root_edge_occurrences:
                if edge[0] in roots and edge[1] in roots:
                    root_edge_occurrences[edge] += 1

        assert vertex_occurrences == [4] * N
        assert set(root_edge_occurrences.values()) == {4}
        assert root_edge_total == 36

    summary = {
        "six_vertex_graphs": total,
        "four_component_survivors": len(r4_survivors),
        "two_component_boundaries": len(r2_survivors),
        "two_component_edge_counts": sorted(
            {edge_count(mask, range(N)) for mask in r2_survivors}
        ),
        "three_component_cubic_boundaries": len(r3_cubic),
        "ordered_nonedge_checks": "PASS",
    }
    payload = json.dumps(summary, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(payload).hexdigest()

    for key, value in summary.items():
        print(f"{key}={value}")
    print(f"summary_sha256={digest}")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
