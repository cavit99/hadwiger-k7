#!/usr/bin/env python3
"""Test universal seven-terminal carriers against the dominated centre base.

For every eligible seven-vertex common-neighbour graph Q, this verifier
adds every labelled C7 carrier and every labelled K3,4 carrier supplied by
the universal seven-terminal theorem.  It then checks whether the resulting
seven-vertex quotient contains a K5-minus minor.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


_BASE = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_low_degree_completion"
    / "verify.py"
)
_SPEC = importlib.util.spec_from_file_location("dominated_low_degree_base", _BASE)
assert _SPEC is not None and _SPEC.loader is not None
_base = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_base)


def add_edges(graph: tuple[int, ...], edges: set[tuple[int, int]]) -> tuple[int, ...]:
    answer = list(graph)
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


_PAIRS = tuple(itertools.combinations(range(7), 2))


def edge_mask(graph: tuple[int, ...]) -> int:
    return sum(
        1 << index
        for index, (left, right) in enumerate(_PAIRS)
        if _base.adjacent(graph, left, right)
    )


def relabel_mask(mask: int, image: tuple[int, ...]) -> int:
    index = {edge: position for position, edge in enumerate(_PAIRS)}
    answer = 0
    for position, (left, right) in enumerate(_PAIRS):
        if mask & (1 << position):
            mapped = tuple(sorted((image[left], image[right])))
            answer |= 1 << index[mapped]
    return answer


def cycle_edge_sets() -> list[set[tuple[int, int]]]:
    """Return every undirected labelled Hamilton cycle on seven vertices."""

    seen: set[tuple[tuple[int, int], ...]] = set()
    answer: list[set[tuple[int, int]]] = []
    for order in itertools.permutations(range(1, 7)):
        cycle = (0, *order)
        edges = {
            tuple(sorted((cycle[index], cycle[(index + 1) % 7])))
            for index in range(7)
        }
        key = tuple(sorted(edges))
        if key not in seen:
            seen.add(key)
            answer.append(edges)
    assert len(answer) == 360
    return answer


def biclique_edge_sets() -> list[set[tuple[int, int]]]:
    """Return every labelled K3,4 on seven vertices."""

    answer = []
    for left in itertools.combinations(range(7), 3):
        left_set = set(left)
        right = set(range(7)) - left_set
        answer.append({tuple(sorted((x, y))) for x in left_set for y in right})
    assert len(answer) == 35
    return answer


def rooted_five_fans(roots: tuple[int, ...]) -> list[set[tuple[int, int]]]:
    """Return every labelled K1 join P4 on the prescribed five roots."""

    seen: set[tuple[tuple[int, int], ...]] = set()
    answer: list[set[tuple[int, int]]] = []
    for hub in roots:
        outer = tuple(vertex for vertex in roots if vertex != hub)
        for path in itertools.permutations(outer):
            edges = {
                *(tuple(sorted((hub, vertex))) for vertex in outer),
                *(tuple(sorted((path[index], path[index + 1]))) for index in range(3)),
            }
            key = tuple(sorted(edges))
            if key not in seen:
                seen.add(key)
                answer.append(edges)
    assert len(answer) == 60
    return answer


def independent_five_partitions(
    graph: tuple[int, ...],
) -> list[tuple[tuple[int, ...], ...]]:
    """Return the proper partitions of V(graph) into five nonempty blocks."""

    blocks: list[list[int]] = []
    answer: list[tuple[tuple[int, ...], ...]] = []

    def extend(vertex: int) -> None:
        if vertex == 7:
            if len(blocks) == 5:
                answer.append(tuple(tuple(block) for block in blocks))
            return
        for block in blocks:
            if all(not _base.adjacent(graph, vertex, other) for other in block):
                block.append(vertex)
                extend(vertex + 1)
                block.pop()
        if len(blocks) < 5:
            blocks.append([vertex])
            extend(vertex + 1)
            blocks.pop()

    extend(0)
    return answer


def eligible_graphs() -> list[tuple[str, tuple[int, ...]]]:
    answer = []
    for graph6, graph in _base.triangle_free_graphs(7):
        if _base.independence_number(graph) > 3:
            continue
        if _base.has_dense_minor(graph, 5, 9):
            continue
        if not _base.small_cuts(graph):
            continue
        answer.append((graph6, graph))
    assert len(answer) == 9
    return answer




def automorphisms(graph: tuple[int, ...]) -> list[tuple[int, ...]]:
    mask = edge_mask(graph)
    return [
        image
        for image in itertools.permutations(range(7))
        if relabel_mask(mask, image) == mask
    ]


def main() -> None:
    cycles = cycle_edge_sets()
    bicliques = biclique_edge_sets()
    survivors: list[tuple[str, str, tuple[tuple[int, int], ...]]] = []
    tested = 0

    for graph6, graph in eligible_graphs():
        for kind, carriers in (("C7", cycles), ("K3,4", bicliques)):
            for carrier in carriers:
                tested += 1
                quotient = add_edges(graph, carrier)
                if not _base.has_dense_minor(quotient, 5, 9):
                    survivors.append((graph6, kind, tuple(sorted(carrier))))

    assert tested == 9 * (360 + 35)
    assert len(survivors) == 456
    assert all(kind == "C7" for _graph6, kind, _carrier in survivors)
    counts: dict[tuple[str, str], int] = {}
    for graph6, kind, _ in survivors:
        counts[(graph6, kind)] = counts.get((graph6, kind), 0) + 1
    print(
        "dominated rooted-seven carrier screen "
        f"eligible_Q=9 tested={tested} survivors={len(survivors)}"
    )
    for graph6, _ in eligible_graphs():
        print(
            graph6,
            f"C7={counts.get((graph6, 'C7'), 0)}",
            f"K3,4={counts.get((graph6, 'K3,4'), 0)}",
        )
    if survivors:
        print("first_survivor", survivors[0])
    cycle_orbits = 0
    by_code = {code: graph for code, graph in eligible_graphs()}
    for graph6, graph in by_code.items():
        group = automorphisms(graph)
        masks = {
            edge_mask(add_edges((0,) * 7, set(carrier)))
            for code, kind, carrier in survivors
            if code == graph6 and kind == "C7"
        }
        representatives = {
            min(relabel_mask(mask, image) for image in group) for mask in masks
        }
        cycle_orbits += len(representatives)
        print(graph6, f"C7_orbits={len(representatives)}")
    assert cycle_orbits == 125
    print("C7_survivor_orbits=125")

    minimum_extra_histogram: dict[int, int] = {}
    hardest_records = []
    for graph6, _kind, carrier in survivors:
        graph = add_edges(by_code[graph6], set(carrier))
        missing = [edge for edge in _PAIRS if not _base.adjacent(graph, *edge)]
        minimum = None
        for size in range(1, 5):
            if any(
                _base.has_dense_minor(add_edges(graph, set(extra)), 5, 9)
                for extra in itertools.combinations(missing, size)
            ):
                minimum = size
                break
        assert minimum is not None
        minimum_extra_histogram[minimum] = minimum_extra_histogram.get(minimum, 0) + 1
        if minimum == 4:
            hardest_records.append((graph6, carrier))
    assert minimum_extra_histogram == {1: 381, 2: 61, 3: 13, 4: 1}
    assert len(hardest_records) == 1
    print("C7_minimum_added_edge_histogram", sorted(minimum_extra_histogram.items()))
    print("C7_unique_four_edge_record", hardest_records[0])

    live_codes = {"FCQ`_", "FCQb_", "FCR`o", "FCp`_", "FCpb_"}
    live_survivors = [
        (graph6, carrier)
        for graph6, kind, carrier in survivors
        if kind == "C7" and graph6 in live_codes
    ]
    assert len(live_survivors) == 402
    live_orbits = 0
    for graph6 in sorted(live_codes):
        graph = by_code[graph6]
        group = automorphisms(graph)
        masks = {
            edge_mask(add_edges((0,) * 7, set(carrier)))
            for code, carrier in live_survivors
            if code == graph6
        }
        live_orbits += len(
            {min(relabel_mask(mask, image) for image in group) for mask in masks}
        )
    assert live_orbits == 99
    print("live_C7_residue", "placements=402", "orbits=99")
    residual_codes = {"FCQ`_", "FCQb_", "FCp`_"}
    residual_survivors = [
        (graph6, carrier)
        for graph6, carrier in live_survivors
        if graph6 in residual_codes
    ]
    assert len(residual_survivors) == 326
    residual_orbits = 0
    for graph6 in residual_codes:
        graph = by_code[graph6]
        group = automorphisms(graph)
        masks = {
            edge_mask(add_edges((0,) * 7, set(carrier)))
            for code, carrier in residual_survivors
            if code == graph6
        }
        residual_orbits += len(
            {min(relabel_mask(mask, image) for image in group) for mask in masks}
        )
    assert residual_orbits == 64
    print("post_F5_C7_residue", "placements=326", "orbits=64")
    live_minimum_extra_histogram: dict[int, int] = {}
    for graph6, carrier in live_survivors:
        graph = add_edges(by_code[graph6], set(carrier))
        missing = [edge for edge in _PAIRS if not _base.adjacent(graph, *edge)]
        minimum = next(
            size
            for size in range(1, 5)
            if any(
                _base.has_dense_minor(add_edges(graph, set(extra)), 5, 9)
                for extra in itertools.combinations(missing, size)
            )
        )
        live_minimum_extra_histogram[minimum] = (
            live_minimum_extra_histogram.get(minimum, 0) + 1
        )
    assert live_minimum_extra_histogram == {1: 334, 2: 54, 3: 13, 4: 1}
    print(
        "live_C7_minimum_added_edge_histogram",
        sorted(live_minimum_extra_histogram.items()),
    )

    owner_failures: list[tuple[str, tuple[tuple[int, int], ...], tuple[int, ...]]] = []
    for graph6, carrier in live_survivors:
        base = add_edges(by_code[graph6], set(carrier))
        for contact_count in range(5, 8):
            for contacts in itertools.combinations(range(7), contact_count):
                closes = False
                for owner in contacts:
                    star = {(owner, other) for other in contacts if other != owner}
                    if _base.has_dense_minor(add_edges(base, star), 5, 9):
                        closes = True
                        break
                if not closes:
                    owner_failures.append((graph6, carrier, contacts))
    print(
        "five_bag_connected_owner_screen",
        f"tested={len(live_survivors) * (21 + 7 + 1)}",
        f"failures={len(owner_failures)}",
    )
    owner_failure_histogram: dict[int, int] = {}
    for _graph6, _carrier, contacts in owner_failures:
        owner_failure_histogram[len(contacts)] = (
            owner_failure_histogram.get(len(contacts), 0) + 1
        )
    assert len(owner_failures) == 666
    assert owner_failure_histogram == {5: 538, 6: 114, 7: 14}
    print("five_bag_owner_failure_histogram", sorted(owner_failure_histogram.items()))
    if owner_failures:
        print("first_five_bag_owner_failure", owner_failures[0])

    rooted_k4_failures: list[
        tuple[str, tuple[tuple[int, int], ...], tuple[int, ...]]
    ] = []
    rooted_k4_closing_histogram: dict[int, int] = {}
    for graph6, carrier in live_survivors:
        base = add_edges(by_code[graph6], set(carrier))
        closing = 0
        for roots in itertools.combinations(range(7), 4):
            clique = set(itertools.combinations(roots, 2))
            if _base.has_dense_minor(add_edges(base, clique), 5, 9):
                closing += 1
            else:
                rooted_k4_failures.append((graph6, carrier, roots))
        rooted_k4_closing_histogram[closing] = (
            rooted_k4_closing_histogram.get(closing, 0) + 1
        )
    print(
        "aligned_rooted_K4_screen",
        f"tested={len(live_survivors) * 35}",
        f"failures={len(rooted_k4_failures)}",
        f"closing_histogram={sorted(rooted_k4_closing_histogram.items())}",
    )
    assert len(rooted_k4_failures) == 701
    assert rooted_k4_closing_histogram == {
        0: 1,
        23: 13,
        26: 2,
        29: 8,
        31: 26,
        32: 4,
        33: 87,
        34: 154,
        35: 107,
    }
    if rooted_k4_failures:
        print("first_aligned_K4_failure", rooted_k4_failures[0])
    zero_k4 = []
    for graph6, carrier in live_survivors:
        base = add_edges(by_code[graph6], set(carrier))
        if not any(
            _base.has_dense_minor(
                add_edges(base, set(itertools.combinations(roots, 2))), 5, 9
            )
            for roots in itertools.combinations(range(7), 4)
        ):
            zero_k4.append((graph6, carrier))
    assert len(zero_k4) == 1
    print("aligned_K4_zero_closure", zero_k4[0])

    robust_five_sets: dict[str, set[tuple[int, ...]]] = {}
    fan_tests = 0
    for graph6, graph in eligible_graphs():
        robust_five_sets[graph6] = set()
        for roots in itertools.combinations(range(7), 5):
            closes_every_labelling = True
            for fan in rooted_five_fans(roots):
                fan_tests += 1
                if not _base.has_dense_minor(add_edges(graph, fan), 5, 9):
                    closes_every_labelling = False
            if closes_every_labelling:
                robust_five_sets[graph6].add(roots)
        print(
            graph6,
            f"robust_rooted_F5_five_sets={len(robust_five_sets[graph6])}",
            f"sets={sorted(robust_five_sets[graph6])}",
        )
    assert fan_tests == 9 * 21 * 60
    assert {code: len(sets) for code, sets in robust_five_sets.items()} == {
        "FCQ`_": 0,
        "FCQb_": 0,
        "FCR`o": 1,
        "FCp`_": 0,
        "FCpb_": 1,
        "FCpV?": 3,
        "FCpv?": 6,
        "FCZb_": 6,
        "FCxv?": 21,
    }
    print("rooted_F5_five_set_screen", f"tested={fan_tests}")

    partition_failures: list[
        tuple[str, tuple[tuple[int, ...], ...]]
    ] = []
    partition_counts: dict[str, int] = {}
    for graph6, graph in eligible_graphs():
        partitions = independent_five_partitions(graph)
        partition_counts[graph6] = len(partitions)
        robust = robust_five_sets[graph6]
        for partition in partitions:
            rainbow_sets = {
                tuple(sorted(choice))
                for choice in itertools.product(*partition)
            }
            if rainbow_sets.isdisjoint(robust):
                partition_failures.append((graph6, partition))
        print(
            graph6,
            f"independent_five_partitions={len(partitions)}",
            "rainbow_robust_failures="
            f"{sum(code == graph6 for code, _ in partition_failures)}",
        )
    print(
        "colour_guided_rooted_F5_screen",
        f"partitions={sum(partition_counts.values())}",
        f"failures={len(partition_failures)}",
    )
    assert sum(partition_counts.values()) == 438
    assert len(partition_failures) == 322
    if partition_failures:
        print("first_colour_guided_F5_failure", partition_failures[0])


if __name__ == "__main__":
    main()
