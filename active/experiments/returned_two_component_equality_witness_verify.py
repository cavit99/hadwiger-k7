#!/usr/bin/env python3
"""Verify the aligned-path equality witness for the returned six-cut.

This checks only the arithmetic, six-connectivity, full-component structure,
and failure of the attachment-excess inequalities to force a compatible
pair.  It does not assert that the graph is K_7^--minor-free.
"""

from itertools import combinations


ORDER = 17
BOUNDARY = frozenset(range(6))
LOW_ROOTS = frozenset({0, 1})
COMMON_ROOTS = frozenset({2, 3, 4, 5})
PATHS = (tuple(range(6, 11)), tuple(range(11, 17)))
BOUNDARY_EDGES = {
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 5),
    (3, 4),
}


def build_graph() -> tuple[frozenset[int], ...]:
    adjacency = [set() for _ in range(ORDER)]

    def add_edge(left: int, right: int) -> None:
        assert left != right
        adjacency[left].add(right)
        adjacency[right].add(left)

    for left, right in BOUNDARY_EDGES:
        add_edge(left, right)

    for path in PATHS:
        for left, right in zip(path, path[1:]):
            add_edge(left, right)
        for root in COMMON_ROOTS:
            for vertex in path:
                add_edge(root, vertex)
        add_edge(0, path[0])
        add_edge(1, path[-1])

    return tuple(frozenset(row) for row in adjacency)


def components(
    adjacency: tuple[frozenset[int], ...], deleted: frozenset[int]
) -> tuple[frozenset[int], ...]:
    unseen = set(range(len(adjacency))) - set(deleted)
    answer: list[frozenset[int]] = []
    while unseen:
        start = min(unseen)
        reached = {start}
        stack = [start]
        unseen.remove(start)
        while stack:
            vertex = stack.pop()
            new = (set(adjacency[vertex]) - set(deleted)) & unseen
            unseen -= new
            reached |= new
            stack.extend(new)
        answer.append(frozenset(reached))
    return tuple(answer)


def edge_count(
    adjacency: tuple[frozenset[int], ...],
    left: frozenset[int],
    right: frozenset[int] | None = None,
) -> int:
    if right is None:
        return sum(len(adjacency[vertex] & left) for vertex in left) // 2
    return sum(len(adjacency[vertex] & right) for vertex in left)


def verify() -> None:
    adjacency = build_graph()
    vertices = frozenset(range(ORDER))
    size = edge_count(adjacency, vertices)
    assert size == 68 == 4 * ORDER
    assert edge_count(adjacency, BOUNDARY) == 11

    open_components = components(adjacency, BOUNDARY)
    assert set(open_components) == {frozenset(path) for path in PATHS}
    for component in open_components:
        assert all(
            any(neighbour in component for neighbour in adjacency[root])
            for root in BOUNDARY
        )

    excesses: list[int] = []
    supply_edges: list[frozenset[frozenset[int]]] = []
    for component in map(frozenset, PATHS):
        internal = edge_count(adjacency, component)
        attachments = {
            root: edge_count(adjacency, component, frozenset({root}))
            for root in BOUNDARY
        }
        excess = internal + sum(attachments.values()) - 4 * len(component)
        excesses.append(excess)
        supply = frozenset(
            frozenset({left, right})
            for left, right in combinations(BOUNDARY, 2)
            if excess > attachments[left] + attachments[right]
        )
        supply_edges.append(supply)

    assert excesses == [6, 7]
    assert supply_edges == [frozenset({LOW_ROOTS}), frozenset({LOW_ROOTS})]

    compatible = []
    for common in BOUNDARY:
        for first in BOUNDARY - {common}:
            for second in BOUNDARY - {common, first}:
                if (
                    frozenset({common, first}) in supply_edges[0]
                    and frozenset({common, second}) in supply_edges[1]
                ):
                    compatible.append((common, first, second))
    assert not compatible

    triangles = {
        triple
        for triple in combinations(BOUNDARY, 3)
        if all(right in adjacency[left] for left, right in combinations(triple, 2))
    }
    assert triangles

    checked_deletions = 0
    for order in range(6):
        for deleted_tuple in combinations(range(ORDER), order):
            deleted = frozenset(deleted_tuple)
            assert len(components(adjacency, deleted)) == 1
            checked_deletions += 1
    assert len(components(adjacency, BOUNDARY)) == 2

    print(
        "GREEN returned two-component equality witness",
        f"n={ORDER}",
        f"m={size}",
        "kappa=6",
        f"deletions_checked={checked_deletions}",
        f"excesses={tuple(excesses)}",
        f"boundary_triangles={len(triangles)}",
        "compatible_supply_triples=0",
        "target_status=not_asserted",
    )


if __name__ == "__main__":
    verify()
