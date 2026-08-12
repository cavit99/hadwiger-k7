#!/usr/bin/env python3
"""Compose the complete seven-terminal kernel catalogue with the live Q.

The catalogue quantifiers are exact:

* every labelled edge-minimal three-connected carrier on the seven roots;
* every labelled order-eight irreducible template, for which at least one
  neighbour of the extra vertex may be chosen as its owner.
"""

from __future__ import annotations

import importlib.util
import itertools
import os
from pathlib import Path
import shutil
import subprocess


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


_CARRIER = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_rooted_seven_carrier"
    / "verify.py"
)
_SPEC = importlib.util.spec_from_file_location("rooted_seven_carrier", _CARRIER)
assert _SPEC is not None and _SPEC.loader is not None
carrier = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(carrier)
base = carrier._base

PAIRS = tuple(itertools.combinations(range(7), 2))
PAIR_INDEX = {edge: position for position, edge in enumerate(PAIRS)}


def connected_after(graph: tuple[int, ...], deleted: frozenset[int]) -> bool:
    remaining = set(range(len(graph))) - set(deleted)
    if not remaining:
        return True
    reached = {remaining.pop()}
    stack = list(reached)
    while stack:
        vertex = stack.pop()
        neighbours = {
            other
            for other in remaining
            if base.adjacent(graph, vertex, other)
        }
        remaining -= neighbours
        reached |= neighbours
        stack.extend(neighbours)
    return not remaining


def three_connected(graph: tuple[int, ...]) -> bool:
    return len(graph) >= 4 and all(
        connected_after(graph, frozenset(cut))
        for size in range(3)
        for cut in itertools.combinations(range(len(graph)), size)
    )


def delete_edge(
    graph: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    answer = list(graph)
    answer[left] &= ~(1 << right)
    answer[right] &= ~(1 << left)
    return tuple(answer)


def relabel(graph: tuple[int, ...], image: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(graph)
    for left, right in itertools.combinations(range(len(graph)), 2):
        if base.adjacent(graph, left, right):
            mapped_left, mapped_right = image[left], image[right]
            answer[mapped_left] |= 1 << mapped_right
            answer[mapped_right] |= 1 << mapped_left
    return tuple(answer)


def minimal_three_connected_carriers() -> set[tuple[int, ...]]:
    executable = os.environ.get("GENG") or shutil.which("geng")
    if executable is None:
        raise SystemExit("geng from nauty is required (or set GENG)")
    process = subprocess.run(
        [executable, "-q", "-c", "-d3", "7"],
        check=True,
        capture_output=True,
        text=True,
    )
    unlabelled = []
    for line in process.stdout.splitlines():
        graph = base.decode_graph6(line)
        if not three_connected(graph):
            continue
        edges = [
            (left, right)
            for left, right in PAIRS
            if base.adjacent(graph, left, right)
        ]
        if all(not three_connected(delete_edge(graph, *edge)) for edge in edges):
            unlabelled.append(graph)
    assert len(unlabelled) == 5
    labelled = {
        relabel(graph, image)
        for graph in unlabelled
        for image in itertools.permutations(range(7))
    }
    assert len(labelled) == 5_495
    return labelled


def cycle_edges(order: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        tuple(sorted((order[index], order[(index + 1) % 7])))
        for index in range(7)
    }


def order_eight_templates() -> set[tuple[int, int]]:
    """Return (terminal-edge mask, extra-neighbour mask)."""

    templates: set[tuple[int, int]] = set()
    for cycle in carrier.cycle_edge_sets():
        edge_mask = sum(1 << PAIR_INDEX[edge] for edge in cycle)
        order = next(
            permutation
            for permutation in itertools.permutations(range(1, 7))
            if cycle_edges((0, *permutation)) == cycle
        )
        order = (0, *order)

        templates.add((edge_mask, (1 << 7) - 1))

        for index in range(7):
            ends = (order[index], order[(index + 3) % 7])
            chord = tuple(sorted(ends))
            terminal_mask = edge_mask | (1 << PAIR_INDEX[chord])
            mandatory = set(range(7)) - set(ends)
            for optional_size in range(3):
                for optional in itertools.combinations(ends, optional_size):
                    neighbours = mandatory | set(optional)
                    templates.add(
                        (terminal_mask, sum(1 << vertex for vertex in neighbours))
                    )

        for index in range(7):
            centre = order[index]
            leaves = (order[(index - 3) % 7], order[(index + 3) % 7])
            chords = {tuple(sorted((centre, leaf))) for leaf in leaves}
            terminal_mask = edge_mask | sum(
                1 << PAIR_INDEX[chord] for chord in chords
            )
            optional_vertices = (centre, *leaves)
            mandatory = set(range(7)) - set(optional_vertices)
            for optional_size in range(4):
                for optional in itertools.combinations(
                    optional_vertices, optional_size
                ):
                    neighbours = mandatory | set(optional)
                    templates.add(
                        (terminal_mask, sum(1 << vertex for vertex in neighbours))
                    )

    assert len(templates) == 30_600
    return templates


def graph_from_mask(mask: int) -> tuple[int, ...]:
    graph = [0] * 7
    for position, (left, right) in enumerate(PAIRS):
        if mask & (1 << position):
            graph[left] |= 1 << right
            graph[right] |= 1 << left
    return tuple(graph)


def owner_quotient(
    terminal_mask: int, neighbour_mask: int, owner: int
) -> tuple[int, ...]:
    graph = graph_from_mask(terminal_mask)
    owner_edges = {
        tuple(sorted((owner, other)))
        for other in range(7)
        if other != owner and neighbour_mask & (1 << other)
    }
    return carrier.add_edges(graph, owner_edges)


def main() -> None:
    by_code = dict(carrier.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    minimal = minimal_three_connected_carriers()
    templates = order_eight_templates()

    order_seven_failures = []
    order_seven_failure_counts: dict[str, int] = {}
    for code in live_codes:
        graph = by_code[code]
        for rooted_carrier in minimal:
            quotient = tuple(
                graph[vertex] | rooted_carrier[vertex] for vertex in range(7)
            )
            if not base.has_dense_minor(quotient, 5, 9):
                order_seven_failures.append((code, rooted_carrier))
                order_seven_failure_counts[code] = (
                    order_seven_failure_counts.get(code, 0) + 1
                )

    order_eight_failures = []
    order_eight_failure_counts: dict[str, int] = {}
    owner_histogram: dict[int, int] = {}
    for code in live_codes:
        graph = by_code[code]
        for terminal_mask, neighbour_mask in templates:
            closing_owners = 0
            for owner in range(7):
                if not neighbour_mask & (1 << owner):
                    continue
                quotient = owner_quotient(terminal_mask, neighbour_mask, owner)
                union = tuple(
                    graph[vertex] | quotient[vertex] for vertex in range(7)
                )
                if base.has_dense_minor(union, 5, 9):
                    closing_owners += 1
            owner_histogram[closing_owners] = (
                owner_histogram.get(closing_owners, 0) + 1
            )
            if not closing_owners:
                order_eight_failures.append(
                    (code, terminal_mask, neighbour_mask)
                )
                order_eight_failure_counts[code] = (
                    order_eight_failure_counts.get(code, 0) + 1
                )

    print(
        "complete seven-terminal dominated-centre composition",
        f"order7_carriers={len(minimal)}",
        f"order7_failures={len(order_seven_failures)}",
        f"order8_templates={len(templates)}",
        f"order8_failures={len(order_eight_failures)}",
    )
    print("order7_failure_counts", sorted(order_seven_failure_counts.items()))
    print("order8_failure_counts", sorted(order_eight_failure_counts.items()))
    order_seven_profiles: dict[tuple[int, ...], int] = {}
    for _code, rooted_carrier in order_seven_failures:
        profile = tuple(sorted(row.bit_count() for row in rooted_carrier))
        order_seven_profiles[profile] = order_seven_profiles.get(profile, 0) + 1
    order_eight_profiles: dict[tuple[int, int], int] = {}
    for _code, terminal_mask, neighbour_mask in order_eight_failures:
        profile = (terminal_mask.bit_count() - 7, neighbour_mask.bit_count())
        order_eight_profiles[profile] = order_eight_profiles.get(profile, 0) + 1
    print("order7_failure_degree_profiles", sorted(order_seven_profiles.items()))
    print("order8_failure_chord_contact_profiles", sorted(order_eight_profiles.items()))
    assert len(order_seven_failures) == 21
    assert order_seven_failure_counts == {
        "FCQ`_": 10,
        "FCQb_": 4,
        "FCp`_": 7,
    }
    assert order_seven_profiles == {((3, 3, 3, 3, 3, 3, 6)): 21}
    assert len(order_eight_failures) == 89
    assert order_eight_failure_counts == {
        "FCQ`_": 50,
        "FCQb_": 10,
        "FCp`_": 29,
    }
    assert order_eight_profiles == {
        (0, 7): 13,
        (1, 5): 19,
        (1, 6): 38,
        (1, 7): 19,
    }
    order_seven_orbits = 0
    order_eight_orbits = 0
    for code in live_codes:
        automorphisms = carrier.automorphisms(by_code[code])
        seven_masks = {
            carrier.edge_mask(rooted_carrier)
            for failure_code, rooted_carrier in order_seven_failures
            if failure_code == code
        }
        seven_orbits = {
            min(carrier.relabel_mask(mask, image) for image in automorphisms)
            for mask in seven_masks
        }
        order_seven_orbits += len(seven_orbits)

        eight_pairs = {
            (terminal_mask, neighbour_mask)
            for failure_code, terminal_mask, neighbour_mask in order_eight_failures
            if failure_code == code
        }

        def relabel_pair(
            pair: tuple[int, int], image: tuple[int, ...]
        ) -> tuple[int, int]:
            terminal_mask, neighbour_mask = pair
            return (
                carrier.relabel_mask(terminal_mask, image),
                sum(
                    1 << image[vertex]
                    for vertex in range(7)
                    if neighbour_mask & (1 << vertex)
                ),
            )

        eight_orbits = {
            min(relabel_pair(pair, image) for image in automorphisms)
            for pair in eight_pairs
        }
        order_eight_orbits += len(eight_orbits)
        print(
            code,
            f"order7_failure_orbits={len(seven_orbits)}",
            f"order8_failure_orbits={len(eight_orbits)}",
        )
    assert order_seven_orbits == 4
    assert order_eight_orbits == 13
    print(
        "kernel_failure_orbits",
        f"order7={order_seven_orbits}",
        f"order8={order_eight_orbits}",
    )
    print("order8_closing_owner_histogram", sorted(owner_histogram.items()))
    assert owner_histogram == {
        0: 89,
        3: 428,
        4: 9_013,
        5: 31_336,
        6: 36_201,
        7: 14_733,
    }

    order_seven_four_contact_failures = []
    for code, rooted_carrier in order_seven_failures:
        graph = by_code[code]
        union = tuple(
            graph[vertex] | rooted_carrier[vertex] for vertex in range(7)
        )
        for contacts in itertools.combinations(range(7), 4):
            if not any(
                base.has_dense_minor(
                    carrier.add_edges(
                        union,
                        {(owner, other) for other in contacts if other != owner},
                    ),
                    5,
                    9,
                )
                for owner in contacts
            ):
                order_seven_four_contact_failures.append(
                    (code, rooted_carrier, contacts)
                )

    order_eight_four_contact_failures = []
    for code, terminal_mask, neighbour_mask in order_eight_failures:
        graph = by_code[code]
        for contacts in itertools.combinations(range(7), 4):
            closes = False
            for kernel_owner in range(7):
                if not neighbour_mask & (1 << kernel_owner):
                    continue
                quotient = owner_quotient(
                    terminal_mask, neighbour_mask, kernel_owner
                )
                for augmentation_owner in contacts:
                    if augmentation_owner == kernel_owner:
                        continue
                    star = {
                        (augmentation_owner, other)
                        for other in contacts
                        if other != augmentation_owner
                    }
                    union = tuple(
                        graph[vertex] | quotient[vertex]
                        for vertex in range(7)
                    )
                    if base.has_dense_minor(
                        carrier.add_edges(union, star), 5, 9
                    ):
                        closes = True
                        break
                if closes:
                    break
            if not closes:
                order_eight_four_contact_failures.append(
                    (code, terminal_mask, neighbour_mask, contacts)
                )

    print(
        "four_contact_refinement_screen",
        f"order7_tests={len(order_seven_failures) * 35}",
        f"order7_failures={len(order_seven_four_contact_failures)}",
        f"order8_tests={len(order_eight_failures) * 35}",
        f"order8_failures={len(order_eight_four_contact_failures)}",
    )
    if order_seven_failures:
        print("first_order7_failure", order_seven_failures[0])
    if order_eight_failures:
        print("first_order8_failure", order_eight_failures[0])

    assert order_seven_failures
    assert order_eight_failures
    assert not order_seven_four_contact_failures
    assert not order_eight_four_contact_failures


if __name__ == "__main__":
    main()
