#!/usr/bin/env python3
"""Verify the minimum-path rooted internal-transversal counterexample."""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations


VERTICES = frozenset(range(8))
EDGES = {
    frozenset(edge)
    for edge in (
        (0, 3), (0, 4), (0, 5), (0, 7),
        (1, 3), (1, 5), (1, 6), (1, 7),
        (2, 4), (2, 5), (2, 6), (2, 7),
        (3, 4), (3, 6), (3, 7),
        (4, 6), (4, 7), (5, 7),
    )
}
SUPPORTS = (
    frozenset((0, 1, 2, 3, 6)),  # R_a
    frozenset((5,)),              # R_b
    frozenset((0, 2, 3, 4, 7)),  # E_L
    frozenset((2, 4, 6)),         # E_R
    frozenset((0, 5)),            # F_1
    frozenset((1, 5)),            # F_2
    frozenset((1, 6)),            # F_3
)
A, B = 0, 1
K = range(2, 7)
P = 2
Z = 5
U = frozenset((0, 1, 5, 6))


def neighbours(vertex: int) -> frozenset[int]:
    return frozenset(
        next(iter(edge - {vertex})) for edge in EDGES if vertex in edge
    )


ADJACENCY = tuple(neighbours(vertex) for vertex in VERTICES)


def connected(vertices: frozenset[int]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    queue = deque(reached)
    while queue:
        vertex = queue.popleft()
        for neighbour in ADJACENCY[vertex] & vertices:
            if neighbour not in reached:
                reached.add(neighbour)
                queue.append(neighbour)
    return reached == set(vertices)


def boundary(vertices: frozenset[int]) -> frozenset[int]:
    return frozenset().union(*(ADJACENCY[vertex] for vertex in vertices)) - vertices


def subsets(vertices: frozenset[int]):
    ordered = sorted(vertices)
    for order in range(len(ordered) + 1):
        for choice in combinations(ordered, order):
            yield frozenset(choice)


def is_bond(side: frozenset[int]) -> bool:
    return connected(side) and connected(VERTICES - side)


def split_supports(side: frozenset[int]) -> frozenset[int]:
    other = VERTICES - side
    return frozenset(
        index for index in K if SUPPORTS[index] & side and SUPPORTS[index] & other
    )


def main() -> None:
    assert len(EDGES) == 18
    assert min(map(len, ADJACENCY)) == 4
    assert all(
        connected(VERTICES - deleted)
        for order in range(4)
        for deleted in map(frozenset, combinations(VERTICES, order))
    )
    assert not connected(VERTICES - frozenset((0, 1, 2, 7)))

    lambda_histogram: Counter[int] = Counter()
    minimum_q = 99
    bonds = []
    for side in subsets(VERTICES):
        if not side:
            continue
        represented = sum(bool(side & support) for support in SUPPORTS)
        boundary_score = len(boundary(side)) + represented
        assert boundary_score >= 7
        lambda_histogram[boundary_score] += 1
        if side != VERTICES and connected(side):
            q_score = len(boundary(side)) + sum(
                bool(side & SUPPORTS[index]) for index in K
            )
            assert q_score >= 6
            minimum_q = min(minimum_q, q_score)
            if side & SUPPORTS[A] and side & SUPPORTS[B]:
                assert boundary_score >= 8
            if connected(VERTICES - side):
                bonds.append(side)

    assert lambda_histogram == Counter({9: 77, 10: 72, 8: 43, 11: 40, 7: 15, 12: 8})
    assert minimum_q == 6

    assert P in SUPPORTS[A]
    assert all((VERTICES - {P}) & SUPPORTS[index] for index in range(1, 7))
    assert sum(P in SUPPORTS[index] for index in K) == 2
    assert all(len(SUPPORTS[index]) >= 2 for index in K)

    complement = VERTICES - U
    assert is_bond(U)
    assert {
        edge for edge in EDGES if edge <= U
    } == {
        frozenset((0, 5)), frozenset((5, 1)), frozenset((1, 6))
    }
    assert U & SUPPORTS[B]
    assert all(U & SUPPORTS[index] for index in K)
    assert split_supports(U) == frozenset((2, 3))
    assert SUPPORTS[2] & U == {0}
    assert SUPPORTS[3] & U == {6}
    assert all(SUPPORTS[index] <= U for index in (4, 5, 6))
    assert all(ADJACENCY[vertex] & complement for vertex in U)
    assert len(ADJACENCY[0] & complement) == 3
    assert len(ADJACENCY[6] & complement) == 3

    support_full_sides = [
        side
        for side in bonds
        if P not in side and all(side & SUPPORTS[index] for index in K)
    ]
    assert min(map(len, support_full_sides)) == len(U) == 4

    rooted_internal = [
        side
        for side in bonds
        if P in side and Z not in side and {4, 5, 6} <= split_supports(side)
    ]
    assert rooted_internal == []

    closing_side = frozenset((0, 4))
    assert is_bond(closing_side)
    assert closing_side & SUPPORTS[A]
    assert (VERTICES - closing_side) & SUPPORTS[B]
    assert {2, 3, 4} <= split_supports(closing_side)

    print("PASS graph6=GEnbvw connectivity=4 delta=4")
    print(f"PASS minimum_q={minimum_q} minimum_support_full_order={len(U)}")
    print("PASS rooted_internal_transversal_bonds=0 explicit_closing_bond={0,4}")


if __name__ == "__main__":
    main()
