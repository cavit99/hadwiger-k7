#!/usr/bin/env python3
"""Directly verify a scoped failure of minimum-K-full-bond selection.

The example satisfies every local minimum-blocker hypothesis but has a unique
minimum-cardinality K-full bond side; that side is a three-vertex path and its
maximum split count is only three.  It is not a counterexample to the
spanning-split target: an explicit anchored closing partition is checked too.
"""

from __future__ import annotations

import itertools

ORDER = 8
FULL = (1 << ORDER) - 1
A, B = 0, 1
K = range(2, 7)

EDGES = {
    tuple(sorted(edge))
    for edge in (
        (0, 3), (0, 4), (0, 6), (0, 7),
        (1, 4), (1, 5), (1, 6), (1, 7),
        (2, 4), (2, 5), (2, 6), (2, 7),
        (3, 5), (3, 6), (3, 7),
        (4, 7), (5, 7), (6, 7),
    )
}

SUPPORTS = (
    {1, 2, 3, 4, 5},       # a
    {6},                    # b
    {0, 3},                 # k1
    {0, 4},                 # k2
    {1, 2, 4},              # k3
    {3, 5},                 # k4
    {0, 1, 2, 5, 6},        # k5
)


def vertex_set(mask: int) -> set[int]:
    return {vertex for vertex in range(ORDER) if mask & (1 << vertex)}


def mask(vertices) -> int:
    return sum(1 << vertex for vertex in vertices)


def neighbours(vertex: int) -> set[int]:
    return {
        other
        for other in range(ORDER)
        if other != vertex and tuple(sorted((vertex, other))) in EDGES
    }


def connected(vertices: set[int]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            vertex
            for old in reached
            for vertex in neighbours(old)
            if vertex in vertices
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def internal_boundary(vertices: set[int]) -> set[int]:
    return set().union(*(neighbours(vertex) for vertex in vertices)) - vertices


def articulation_vertices(vertices: set[int]) -> set[int]:
    if len(vertices) <= 2:
        return set()
    return {
        vertex
        for vertex in vertices
        if not connected(vertices - {vertex})
    }


def split_resources(left: set[int], right: set[int]) -> tuple[int, ...]:
    return tuple(
        resource
        for resource in K
        if SUPPORTS[resource] & left and SUPPORTS[resource] & right
    )


def main():
    all_vertices = set(range(ORDER))
    assert len(EDGES) == 18
    assert min(len(neighbours(vertex)) for vertex in all_vertices) == 4

    # Connectivity after deleting fewer than four vertices, together with
    # minimum degree four, certifies vertex-connectivity exactly four.
    for deleted_order in range(4):
        for deleted in itertools.combinations(range(ORDER), deleted_order):
            assert connected(all_vertices - set(deleted))

    assert all(SUPPORTS)
    assert 1 <= len(SUPPORTS[A]) <= 5
    assert all(len(SUPPORTS[resource]) >= 2 for resource in K)

    eligible = tuple(
        vertex
        for vertex in SUPPORTS[A]
        if all(SUPPORTS[resource] - {vertex} for resource in range(1, 7))
        and sum(vertex in SUPPORTS[resource] for resource in K) <= 2
    )
    assert eligible == (1, 2, 3, 4, 5)

    connected_masks = []
    bond_masks = []
    for subset_mask in range(1, FULL + 1):
        subset = vertex_set(subset_mask)
        boundary_order = len(internal_boundary(subset)) + sum(
            bool(SUPPORTS[resource] & subset) for resource in range(7)
        )
        assert boundary_order >= 7
        if connected(subset):
            connected_masks.append(subset_mask)
            if subset != all_vertices:
                if SUPPORTS[A] & subset and SUPPORTS[B] & subset:
                    assert boundary_order >= 8
                complement = all_vertices - subset
                if connected(complement):
                    bond_masks.append(subset_mask)

    # There are no three-cuts, so both exact three-cut profiles are vacuous.
    for deleted in itertools.combinations(range(ORDER), 3):
        assert connected(all_vertices - set(deleted))

    k_full_bonds = [
        subset_mask
        for subset_mask in bond_masks
        if all(SUPPORTS[resource] & vertex_set(subset_mask) for resource in K)
    ]
    minimum_order = min(subset_mask.bit_count() for subset_mask in k_full_bonds)
    minimum_sides = [
        subset_mask
        for subset_mask in k_full_bonds
        if subset_mask.bit_count() == minimum_order
    ]
    assert minimum_order == 3
    assert minimum_sides == [mask({0, 3, 4})]

    minimum_side = vertex_set(minimum_sides[0])
    complement = all_vertices - minimum_side
    assert articulation_vertices(minimum_side) == {0}
    assert {
        edge for edge in EDGES if set(edge) <= minimum_side
    } == {(0, 3), (0, 4)}
    boundary_in_side = {
        vertex
        for vertex in minimum_side
        if neighbours(vertex) & complement
    }
    assert boundary_in_side == minimum_side
    minimum_splits = split_resources(minimum_side, complement)
    assert minimum_splits == (4, 5, 6)

    anchored_count = 0
    full_count = 0
    for left_mask in bond_masks:
        left = vertex_set(left_mask)
        right = all_vertices - left
        splits = split_resources(left, right)
        if SUPPORTS[A] & left:
            epsilon_b = int(not bool(SUPPORTS[B] & right))
            if len(splits) >= 3 + epsilon_b:
                full_count += 1
        if SUPPORTS[B] & right and len(splits) >= 3:
            anchored_count += sum(vertex in left for vertex in eligible)
    assert (anchored_count, full_count) == (182, 95)

    closing_left = {1, 4}
    closing_right = all_vertices - closing_left
    assert 1 in eligible
    assert connected(closing_left) and connected(closing_right)
    assert SUPPORTS[B] & closing_right
    assert split_resources(closing_left, closing_right) == (3, 4, 6)

    print("graph6=GCxvf{ order=8 edges=18 connectivity=4 three_cuts=0")
    print("eligible_p=1,2,3,4,5")
    print(
        "minimum_K_full_bond_order=3 minimum_sides=1 "
        "U=0,3,4 articulation=0 boundary_in_U=0,3,4 split_count=3"
    )
    print(
        "closing_partition_U=1,4 closing_partition_V=0,2,3,5,6,7 "
        "eligible_p=1 split_resources=k2,k3,k5"
    )
    print("anchored_witnesses=182 full_witnesses=95")
    print("GREEN scoped minimum-K-full-bond route nonclosure")


if __name__ == "__main__":
    main()
