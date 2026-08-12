#!/usr/bin/env python3
"""Test the universal five-terminal fan against eligible boundaries."""

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


def f5_edges(order: tuple[int, ...]) -> set[tuple[int, int]]:
    hub, a, b, c, d = order
    edges = {(min(hub, x), max(hub, x)) for x in (a, b, c, d)}
    edges.update((min(x, y), max(x, y)) for x, y in ((a, b), (b, c), (c, d)))
    return edges


def add_edges(
    graph: tuple[int, ...], edges: set[tuple[int, int]]
) -> tuple[int, ...]:
    answer = list(graph)
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


def f5_edge_sets(roots: tuple[int, ...]) -> tuple[set[tuple[int, int]], ...]:
    """Return the 60 distinct labelled F5 graphs on the five roots."""

    seen: set[tuple[tuple[int, int], ...]] = set()
    answer: list[set[tuple[int, int]]] = []
    for order in itertools.permutations(roots):
        edges = f5_edges(order)
        key = tuple(sorted(edges))
        if key not in seen:
            seen.add(key)
            answer.append(edges)
    assert len(answer) == 60
    return tuple(answer)


def five_block_partitions(graph: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    """Enumerate equality partitions of Q arising in proper five-colourings."""

    partitions: set[tuple[tuple[int, ...], ...]] = set()
    for colours in itertools.product(range(5), repeat=7):
        if set(colours) != set(range(5)):
            continue
        if any(
            colours[left] == colours[right]
            for left, right in itertools.combinations(range(7), 2)
            if graph[left] & (1 << right)
        ):
            continue
        blocks = tuple(
            sorted(
                tuple(vertex for vertex, colour in enumerate(colours) if colour == value)
                for value in range(5)
            )
        )
        partitions.add(blocks)
    return sorted(partitions)


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

    robust_sets: dict[str, list[tuple[int, ...]]] = {}
    best_worst: dict[str, int] = {}
    exact_robust_sets: dict[str, list[tuple[int, ...]]] = {}
    partition_failures: dict[str, list[tuple[tuple[int, ...], ...]]] = {}
    universal_root_failures: dict[str, list[int]] = {}
    partition_adaptive_failures: dict[
        str, list[tuple[tuple[int, ...], ...]]
    ] = {}
    kempe_matching_failures: dict[str, list[tuple[tuple[int, ...], ...]]] = {}
    for graph6, graph in eligible:
        best = 0
        good: list[tuple[int, ...]] = []
        for roots in itertools.combinations(range(7), 5):
            minimum_edges = 10
            for order in itertools.permutations(roots):
                edges = f5_edges(order)
                edges.update(
                    (left, right)
                    for left, right in itertools.combinations(roots, 2)
                    if graph[left] & (1 << right)
                )
                minimum_edges = min(minimum_edges, len(edges))
            best = max(best, minimum_edges)
            if minimum_edges >= 9:
                good.append(roots)
        best_worst[graph6] = best
        if good:
            robust_sets[graph6] = good

        exact_good: list[tuple[int, ...]] = []
        for roots in itertools.combinations(range(7), 5):
            if all(
                _base.has_dense_minor(add_edges(graph, fan), 5, 9)
                for fan in f5_edge_sets(roots)
            ):
                exact_good.append(roots)
        if exact_good:
            exact_robust_sets[graph6] = exact_good

        failed = []
        exact_good_set = set(exact_good)
        for partition in five_block_partitions(graph):
            rainbow_sets = {
                tuple(sorted(choice)) for choice in itertools.product(*partition)
            }
            if not (rainbow_sets & exact_good_set):
                failed.append(partition)
        if failed:
            partition_failures[graph6] = failed

        failed_roots = []
        for root in range(7):
            star = {
                tuple(sorted((root, other)))
                for other in range(7)
                if other != root
            }
            if not _base.has_dense_minor(add_edges(graph, star), 5, 9):
                failed_roots.append(root)
        if failed_roots:
            universal_root_failures[graph6] = failed_roots

        adaptive_failed = []
        for partition in five_block_partitions(graph):
            closed = False
            for rainbow in itertools.product(*partition):
                rainbow_set = set(rainbow)
                for hub in rainbow:
                    others = tuple(vertex for vertex in rainbow if vertex != hub)
                    for path in itertools.permutations(others):
                        fan = {
                            *(tuple(sorted((hub, vertex))) for vertex in others),
                            *(tuple(sorted((path[index], path[index + 1]))) for index in range(3)),
                        }
                        if _base.has_dense_minor(add_edges(graph, fan), 5, 9):
                            closed = True
                            break
                    if closed:
                        break
                if closed:
                    break
            if not closed:
                adaptive_failed.append(partition)
        if adaptive_failed:
            partition_adaptive_failures[graph6] = adaptive_failed

        kempe_failed = []
        for partition in five_block_partitions(graph):
            colours = range(5)
            closed = False
            for four_colours in itertools.combinations(colours, 4):
                a, b, c, d = four_colours
                for pairs in (
                    ((a, b), (c, d)),
                    ((a, c), (b, d)),
                    ((a, d), (b, c)),
                ):
                    robust = True
                    for first in itertools.product(
                        partition[pairs[0][0]], partition[pairs[0][1]]
                    ):
                        for second in itertools.product(
                            partition[pairs[1][0]], partition[pairs[1][1]]
                        ):
                            edges = {
                                tuple(sorted(first)),
                                tuple(sorted(second)),
                            }
                            if not _base.has_dense_minor(
                                add_edges(graph, edges), 5, 9
                            ):
                                robust = False
                                break
                        if not robust:
                            break
                    if robust:
                        closed = True
                        break
                if closed:
                    break
            if not closed:
                kempe_failed.append(partition)
        if kempe_failed:
            kempe_matching_failures[graph6] = kempe_failed

    print("eligible_Q=", [code for code, _ in eligible])
    print("robust_types=", sorted(robust_sets))
    print("best_worst_edges=", best_worst)
    for code, roots in robust_sets.items():
        print(code, roots[:3])
    print(
        "exact_robust_root_sets=",
        {code: len(roots) for code, roots in exact_robust_sets.items()},
    )
    print(
        "five_colour_partition_failures=",
        {code: len(partitions) for code, partitions in partition_failures.items()},
    )
    for code, partitions in partition_failures.items():
        print("first_partition_failure", code, partitions[0])
    print("universal_root_failures=", universal_root_failures)
    print(
        "adaptive_f5_partition_failures=",
        {code: len(partitions) for code, partitions in partition_adaptive_failures.items()},
    )
    for code, partitions in partition_adaptive_failures.items():
        print("first_adaptive_failure", code, partitions[0])
    print(
        "robust_disjoint_kempe_matching_failures=",
        {code: len(partitions) for code, partitions in kempe_matching_failures.items()},
    )
    for code, partitions in kempe_matching_failures.items():
        print("first_kempe_matching_failure", code, partitions[0])


if __name__ == "__main__":
    main()
