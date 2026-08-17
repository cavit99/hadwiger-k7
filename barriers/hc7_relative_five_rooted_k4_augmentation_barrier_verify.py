#!/usr/bin/env python3
"""Verify the relative-five rooted-K4 augmentation counterexample."""

from __future__ import annotations

from itertools import combinations, product


ROOTS = frozenset(range(5))
U, V, W = 5, 6, 7
INTERNAL = frozenset((U, V, W))


def build_graph() -> dict[int, set[int]]:
    adjacency = {vertex: set() for vertex in ROOTS | INTERNAL}
    edges = {(U, V), (U, W)}
    edges.update((U, root) for root in (0, 1, 2))
    edges.update((V, root) for root in (0, 1, 2, 4))
    edges.update((W, root) for root in (0, 1, 2, 3))
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    return adjacency


def connected(adjacency: dict[int, set[int]], vertices: set[int]) -> bool:
    if not vertices:
        return False
    reached: set[int] = set()
    todo = [next(iter(vertices))]
    while todo:
        vertex = todo.pop()
        if vertex in reached:
            continue
        reached.add(vertex)
        todo.extend((adjacency[vertex] & vertices) - reached)
    return reached == vertices


def adjacent(
    adjacency: dict[int, set[int]], left: set[int], right: set[int]
) -> bool:
    return any(adjacency[vertex] & right for vertex in left)


def neighbourhood(adjacency: dict[int, set[int]], vertices: set[int]) -> set[int]:
    return set().union(*(adjacency[vertex] for vertex in vertices)) - vertices


def has_rooted_k5minus(adjacency: dict[int, set[int]]) -> bool:
    for allocation in product(range(6), repeat=3):
        bags = [{root} for root in sorted(ROOTS)]
        for vertex, owner in zip(sorted(INTERNAL), allocation, strict=True):
            if owner:
                bags[owner - 1].add(vertex)
        if not all(connected(adjacency, bag) for bag in bags):
            continue
        missing = sum(
            not adjacent(adjacency, bags[left], bags[right])
            for left, right in combinations(range(5), 2)
        )
        if missing <= 1:
            return True
    return False


def main() -> None:
    adjacency = build_graph()
    assert not any(adjacency[root] & ROOTS for root in ROOTS)
    expected_neighbourhoods = (5, 5, 5, 5, 5, 6, 5)
    observed = []
    for order in range(1, 4):
        for subset in combinations(sorted(INTERNAL), order):
            observed.append(len(neighbourhood(adjacency, set(subset))))
    assert tuple(observed) == expected_neighbourhoods

    bags = ({0}, {1, V}, {2, U}, {3, W})
    assert all(connected(adjacency, set(bag)) for bag in bags)
    assert all(
        adjacent(adjacency, set(bags[left]), set(bags[right]))
        for left, right in combinations(range(4), 2)
    )
    assert not has_rooted_k5minus(adjacency)

    internal_edges = 2
    incidences = sum(len(adjacency[vertex] & ROOTS) for vertex in INTERNAL)
    surrogate = internal_edges + incidences - 3 * len(INTERNAL)
    assert (internal_edges, incidences, surrogate) == (2, 11, 4)

    print("GREEN relative-five rooted-K4 augmentation barrier")
    print(f"nonterminal neighbourhood sizes={tuple(observed)}")
    print("rooted K4 bags=({0},{1,v},{2,u},{3,w})")
    print("rooted K5-minus models=0 (216 allocations exhausted)")
    print(f"five-root surrogate={surrogate}")


if __name__ == "__main__":
    main()
