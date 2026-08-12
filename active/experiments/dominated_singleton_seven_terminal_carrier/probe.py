#!/usr/bin/env python3
"""Probe seven-terminal carriers against dominated degree-eight boundaries.

For each eligible seven-vertex common-neighbour graph Q, add every labelled
C7 and K3,4 carrier supplied by the universal seven-terminal theorem and
test whether the resulting seven-label quotient contains K5 minus one edge
as a minor.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


_BASE = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_low_degree_completion"
    / "verify.py"
)
_SPEC = importlib.util.spec_from_file_location("dominated_low_degree_base", _BASE)
assert _SPEC is not None and _SPEC.loader is not None
_base = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_base)


def add_edges(graph: tuple[int, ...], edges: list[tuple[int, int]]) -> tuple[int, ...]:
    answer = list(graph)
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


def canonical_cycles() -> list[tuple[int, ...]]:
    return [
        (0, *tail)
        for tail in itertools.permutations(range(1, 7))
        if tail[0] < tail[-1]
    ]


def main() -> None:
    eligible: list[tuple[str, tuple[int, ...]]] = []
    for graph6, graph in _base.triangle_free_graphs(7):
        if _base.independence_number(graph) > 3:
            continue
        if _base.has_dense_minor(graph, 5, 9):
            continue
        if not _base.small_cuts(graph):
            continue
        eligible.append((graph6, graph))
    assert len(eligible) == 9

    cycle_survivors: list[tuple[str, tuple[int, ...]]] = []
    closing_chord_counts: list[int] = []
    minimum_extra_edges: list[int] = []
    cycles = canonical_cycles()
    assert len(cycles) == 360
    for graph6, graph in eligible:
        for cycle in cycles:
            edges = [
                (cycle[index], cycle[(index + 1) % 7])
                for index in range(7)
            ]
            host = add_edges(graph, edges)
            if not _base.has_dense_minor(host, 5, 9):
                cycle_survivors.append((graph6, cycle))
                closing = 0
                for left, right in itertools.combinations(range(7), 2):
                    if host[left] & (1 << right):
                        continue
                    if _base.has_dense_minor(add_edges(host, [(left, right)]), 5, 9):
                        closing += 1
                closing_chord_counts.append(closing)
                nonedges = [
                    (left, right)
                    for left, right in itertools.combinations(range(7), 2)
                    if not host[left] & (1 << right)
                ]
                minimum = 1 if closing else len(nonedges)
                if not closing:
                    for size in range(2, len(nonedges) + 1):
                        if any(
                            _base.has_dense_minor(add_edges(host, list(extra)), 5, 9)
                            for extra in itertools.combinations(nonedges, size)
                        ):
                            minimum = size
                            break
                minimum_extra_edges.append(minimum)

    biclique_survivors: list[tuple[str, tuple[int, ...]]] = []
    for graph6, graph in eligible:
        for left in itertools.combinations(range(7), 3):
            left_set = set(left)
            right = [vertex for vertex in range(7) if vertex not in left_set]
            edges = [(x, y) for x in left for y in right]
            host = add_edges(graph, edges)
            if not _base.has_dense_minor(host, 5, 9):
                biclique_survivors.append((graph6, left))

    print(
        "eligible_Q=",
        len(eligible),
        "cycle_placements=",
        len(eligible) * len(cycles),
        "cycle_survivors=",
        len(cycle_survivors),
        "biclique_placements=",
        len(eligible) * 35,
        "biclique_survivors=",
        len(biclique_survivors),
    )
    print("cycle_survivor_types=", sorted({code for code, _ in cycle_survivors}))
    print("biclique_survivor_types=", sorted({code for code, _ in biclique_survivors}))
    print(
        "closing_chord_count_range=",
        (min(closing_chord_counts), max(closing_chord_counts))
        if closing_chord_counts
        else (),
        "zero_closing=",
        sum(count == 0 for count in closing_chord_counts),
        "minimum_extra_edge_distribution=",
        {
            value: minimum_extra_edges.count(value)
            for value in sorted(set(minimum_extra_edges))
        },
    )
    live_codes = {"FCQ`_", "FCQb_", "FCR`o", "FCp`_", "FCpb_"}
    live_survivor_minima = [
        minimum
        for (code, _), minimum in zip(cycle_survivors, minimum_extra_edges)
        if code in live_codes
    ]
    print(
        "live_cycle_survivors=",
        len(live_survivor_minima),
        "live_minimum_extra_edge_distribution=",
        {
            value: live_survivor_minima.count(value)
            for value in sorted(set(live_survivor_minima))
        },
    )
    if cycle_survivors:
        print("first_cycle_survivor=", cycle_survivors[0])
    if biclique_survivors:
        print("first_biclique_survivor=", biclique_survivors[0])


if __name__ == "__main__":
    main()
