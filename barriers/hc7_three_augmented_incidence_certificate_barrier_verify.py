#!/usr/bin/env python3
"""Verify the first barrier to the three-augmented literal certificate."""

from __future__ import annotations

from itertools import combinations, permutations


ROOTS = frozenset(range(6))
VERTICES = frozenset(range(5))
EDGES = frozenset(
    tuple(sorted(edge))
    for edge in (
        (0, 1), (0, 3), (0, 4), (1, 2),
        (1, 3), (1, 4), (2, 3), (2, 4),
    )
)
LABELS = (
    frozenset((1, 2, 4)),
    frozenset((0, 3, 4)),
    frozenset((1, 2, 4)),
    frozenset((0, 1, 2, 3, 4)),
    frozenset((0, 3, 4, 5)),
)


def internal_neighbours(vertex: int) -> set[int]:
    return {
        other
        for other in VERTICES - {vertex}
        if tuple(sorted((vertex, other))) in EDGES
    }


def connected(vertices: frozenset[int]) -> bool:
    if not vertices:
        return False
    reached: set[int] = set()
    todo = [next(iter(vertices))]
    while todo:
        vertex = todo.pop()
        if vertex in reached:
            continue
        reached.add(vertex)
        todo.extend((internal_neighbours(vertex) & set(vertices)) - reached)
    return reached == set(vertices)


def contact(left: int, root_left: int, right: int, root_right: int) -> bool:
    return (
        tuple(sorted((left, right))) in EDGES
        or root_right in LABELS[left]
        or root_left in LABELS[right]
    )


def three_augmented_certificate() -> tuple[object, ...] | None:
    for vertices in combinations(sorted(VERTICES), 3):
        common = set.intersection(*(set(LABELS[vertex]) for vertex in vertices))
        for singleton_pair in combinations(sorted(common), 2):
            remaining = ROOTS - set(singleton_pair)
            for omitted in remaining:
                assigned_roots = remaining - {omitted}
                if len(assigned_roots) != 3:
                    continue
                for assignment in permutations(sorted(assigned_roots)):
                    if not all(
                        root in LABELS[vertex]
                        for vertex, root in zip(vertices, assignment, strict=True)
                    ):
                        continue
                    if all(
                        contact(vertices[left], assignment[left], vertices[right], assignment[right])
                        for left, right in combinations(range(3), 2)
                    ):
                        return vertices, singleton_pair, omitted, assignment
    return None


def main() -> None:
    neighbourhood_orders = []
    full_packets = []
    for order in range(1, 6):
        for subset_tuple in combinations(sorted(VERTICES), order):
            subset = frozenset(subset_tuple)
            root_neighbours = set().union(*(LABELS[vertex] for vertex in subset))
            external_internal = set().union(
                *(internal_neighbours(vertex) for vertex in subset)
            ) - set(subset)
            neighbourhood_orders.append(len(root_neighbours) + len(external_internal))
            if connected(subset) and root_neighbours == set(ROOTS):
                full_packets.append(subset)
    assert min(neighbourhood_orders) == 6
    assert full_packets
    assert all(4 in packet for packet in full_packets)
    assert not any(
        left.isdisjoint(right) for left, right in combinations(full_packets, 2)
    )
    assert three_augmented_certificate() is None

    # Omit root 0.  Each integer is the internal vertex in the corresponding
    # root bag; None denotes the singleton root bag.
    roots = (1, 2, 3, 4, 5)
    owners = (2, 3, 1, None, 4)
    missing = []
    for left, right in combinations(range(5), 2):
        if owners[left] is None:
            touches = roots[left] in LABELS[owners[right]]  # type: ignore[index]
        elif owners[right] is None:
            touches = roots[right] in LABELS[owners[left]]
        else:
            touches = contact(
                owners[left], roots[left], owners[right], roots[right]
            )
        if not touches:
            missing.append((roots[left], roots[right]))
    assert missing == [(2, 5)]

    incidence = sum(map(len, LABELS))
    eta = len(EDGES) + incidence - 4 * len(VERTICES)
    assert (len(EDGES), incidence, eta) == (8, 18, 6)

    print("GREEN three-augmented incidence-certificate barrier")
    print(f"internal-six minimum neighbourhood={min(neighbourhood_orders)}")
    print(f"full packets={len(full_packets)}; common hitting vertex=4")
    print("three-augmented literal certificates=0 (exhaustive)")
    print("four-augmented rooted K5-minus missing pair=(2,5)")
    print(f"eta={eta}")


if __name__ == "__main__":
    main()
