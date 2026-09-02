#!/usr/bin/env python3
"""Verify the scoped five-support/rooted-K5 extension counterexample."""

from __future__ import annotations

import itertools

if not __debug__:
    raise SystemExit("verification requires assertions; do not use Python -O")

ORDER = 11
FULL = (1 << ORDER) - 1
EDGES = {
    tuple(sorted(edge))
    for edge in (
        (0, 1), (0, 4), (0, 5), (0, 7),
        (1, 2), (1, 5), (1, 7), (1, 8),
        (2, 3), (2, 5), (2, 8), (2, 9),
        (3, 4), (3, 5), (3, 9), (3, 10),
        (4, 5), (4, 10),
        (6, 7), (6, 8), (6, 9), (6, 10),
        (7, 8), (8, 9), (9, 10),
    )
}
SUPPORTS = (
    {0, 1, 2, 3, 4, 5, 8, 9},
    {4, 10},
    {6, 10},
    {6, 7},
    {0, 7},
)
GRAPH6 = "JhfwEDbKgs_"


def graph6_code(order: int, edges: set[tuple[int, int]]) -> str:
    """Encode a graph of order at most 62 in the graph6 bit order."""
    bits = [int((left, right) in edges)
            for right in range(1, order) for left in range(right)]
    bits.extend([0] * (-len(bits) % 6))
    payload = "".join(
        chr(63 + sum(bits[start + offset] << (5 - offset)
                     for offset in range(6)))
        for start in range(0, len(bits), 6)
    )
    return chr(63 + order) + payload


def adjacency(order: int, edges: set[tuple[int, int]]) -> tuple[int, ...]:
    answer = [0] * order
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


X_ADJ = adjacency(ORDER, EDGES)


def connected(graph: tuple[int, ...], vertices: int) -> bool:
    if vertices == 0:
        return False
    reached = vertices & -vertices
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= graph[bit.bit_length() - 1] & vertices
        if expanded == reached:
            return reached == vertices
        reached = expanded


def boundary(graph: tuple[int, ...], vertices: int) -> int:
    answer = 0
    todo = vertices
    while todo:
        bit = todo & -todo
        todo ^= bit
        answer |= graph[bit.bit_length() - 1]
    return answer & ~vertices


def support_mask(support: set[int]) -> int:
    return sum(1 << vertex for vertex in support)


SUPPORT_MASKS = tuple(support_mask(support) for support in SUPPORTS)


def split_count(left: int, right: int) -> int:
    return sum(bool(left & support) and bool(right & support)
               for support in SUPPORT_MASKS)


def verify_exterior() -> tuple[dict[int, int], dict[int, int]]:
    assert graph6_code(ORDER, EDGES) == GRAPH6
    assert len(EDGES) == 25
    degrees = sorted(neighbours.bit_count() for neighbours in X_ADJ)
    assert degrees == [4] * 5 + [5] * 6
    assert all(support.bit_count() >= 2 for support in SUPPORT_MASKS)

    for deleted_order in range(4):
        for deleted_vertices in itertools.combinations(range(ORDER), deleted_order):
            deleted = sum(1 << vertex for vertex in deleted_vertices)
            assert connected(X_ADJ, FULL ^ deleted)

    q_histogram: dict[int, int] = {}
    for vertices in range(1, FULL):
        if not connected(X_ADJ, vertices):
            continue
        q_value = boundary(X_ADJ, vertices).bit_count() + sum(
            bool(vertices & support) for support in SUPPORT_MASKS
        )
        assert q_value >= 6
        q_histogram[q_value] = q_histogram.get(q_value, 0) + 1
    assert q_histogram == {6: 32, 7: 155, 8: 398, 9: 508,
                           10: 317, 11: 73, 12: 2}

    bond_histogram: dict[int, int] = {}
    for left in range(1, FULL):
        if not left & 1:  # Count each unordered bond once.
            continue
        right = FULL ^ left
        if connected(X_ADJ, left) and connected(X_ADJ, right):
            splits = split_count(left, right)
            assert splits <= 3
            bond_histogram[splits] = bond_histogram.get(splits, 0) + 1
    assert bond_histogram == {1: 52, 2: 172, 3: 243}
    return q_histogram, bond_histogram


def augmented_graph() -> tuple[int, ...]:
    order = ORDER + 5
    edges = set(EDGES)
    roots = range(ORDER, order)
    edges.update(itertools.combinations(roots, 2))
    for root, support in zip(roots, SUPPORTS):
        edges.update((root, vertex) for vertex in support)
    return adjacency(order, edges)


def verify_augmentation() -> int:
    graph = augmented_graph()
    order = len(graph)
    full = (1 << order) - 1
    assert sum(neighbours.bit_count() for neighbours in graph) // 2 == 51
    assert min(neighbours.bit_count() for neighbours in graph) == 6
    for deleted_order in range(6):
        for deleted_vertices in itertools.combinations(range(order), deleted_order):
            deleted = sum(1 << vertex for vertex in deleted_vertices)
            assert connected(graph, full ^ deleted)

    # Exhaust every pair of disjoint nonempty connected exterior bags while
    # keeping the five new clique vertices as singleton roots.
    maximum_contacts = 0
    for first in range(1, FULL + 1):
        if not connected(X_ADJ, first):
            continue
        available = FULL ^ first
        second = available
        while second:
            if connected(X_ADJ, second):
                root_contacts = sum(bool(first & support) + bool(second & support)
                                    for support in SUPPORT_MASKS)
                contacts = 10 + root_contacts + bool(boundary(X_ADJ, first) & second)
                maximum_contacts = max(maximum_contacts, contacts)
                assert contacts <= 19
            second = (second - 1) & available
    assert maximum_contacts == 19

    # This model deliberately uses some clique roots inside larger bags.  It
    # shows that the barrier is rooted, not an unrooted target-free graph.
    q1, q2, q3, q4, q5 = range(ORDER, ORDER + 5)
    bags = (
        {0, 5, q3, q5},
        {10},
        {6},
        {1, 9, q1},
        {2, 3, 8},
        {7},
        {4, q2, q4},
    )
    bag_masks = tuple(sum(1 << vertex for vertex in bag) for bag in bags)
    assert sum(map(len, bags)) == order
    assert len(set().union(*bags)) == order
    assert all(connected(graph, bag) for bag in bag_masks)
    contacts = {
        (left, right)
        for left, right in itertools.combinations(range(7), 2)
        if boundary(graph, bag_masks[left]) & bag_masks[right]
    }
    assert len(contacts) == 20
    assert set(itertools.combinations(range(7), 2)) - contacts == {(1, 5)}
    return maximum_contacts


def main() -> None:
    q_histogram, bond_histogram = verify_exterior()
    maximum_contacts = verify_augmentation()
    print(f"graph6={GRAPH6} order=11 edges=25 connectivity=4 minimum_degree=4")
    print(f"connected_set_q_histogram={q_histogram}")
    print(f"unordered_bond_split_histogram={bond_histogram}")
    print("augmentation_order=16 edges=51 connectivity=6")
    print(f"maximum_canonical_rooted_contacts={maximum_contacts}")
    print("GREEN scoped six-connected K5 rooted-extension barrier")


if __name__ == "__main__":
    main()
