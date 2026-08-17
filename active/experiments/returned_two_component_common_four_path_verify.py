#!/usr/bin/env python3
"""Verify the explicit K7-minus model in the aligned equality witness."""

from itertools import combinations

from returned_two_component_equality_witness_verify import build_graph


MODEL = (
    frozenset({0, 1, 2, 6, 7, 8, 9, 10}),
    frozenset({3}),
    frozenset({4}),
    frozenset({5, 11}),
    frozenset({14}),
    frozenset({15}),
    frozenset({16}),
)


def connected_bag(adjacency: tuple[frozenset[int], ...], bag: frozenset[int]) -> bool:
    reached = {min(bag)}
    stack = list(reached)
    while stack:
        vertex = stack.pop()
        new = (set(adjacency[vertex]) & set(bag)) - reached
        reached |= new
        stack.extend(new)
    return reached == set(bag)


def adjacent_bags(
    adjacency: tuple[frozenset[int], ...],
    left: frozenset[int],
    right: frozenset[int],
) -> bool:
    return any(adjacency[vertex] & right for vertex in left)


def verify() -> None:
    adjacency = build_graph()
    assert len(MODEL) == 7
    assert all(MODEL)
    assert all(left.isdisjoint(right) for left, right in combinations(MODEL, 2))
    assert all(connected_bag(adjacency, bag) for bag in MODEL)

    missing = tuple(
        (left, right)
        for left, right in combinations(range(7), 2)
        if not adjacent_bags(adjacency, MODEL[left], MODEL[right])
    )
    assert missing == ((4, 6),)

    print(
        "GREEN common-four-path K7-minus model",
        f"bags={len(MODEL)}",
        "adjacent_pairs=20",
        "missing_pair=(4,6)",
        "unused_vertices=(12,13)",
    )


if __name__ == "__main__":
    verify()
