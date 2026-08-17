#!/usr/bin/env python3
"""Verify the five-connected degree-eight two-component barrier."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations


Edge = tuple[int, int]


def edge(u: int, v: int) -> Edge:
    assert u != v
    return (u, v) if u < v else (v, u)


def adjacency_tuple(order: int, edges: set[Edge]) -> tuple[int, ...]:
    adjacency = [0] * order
    for u, v in edges:
        assert 0 <= u < order and 0 <= v < order and u != v
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    return tuple(adjacency)


def vertex_mask(vertices: tuple[int, ...] | set[int]) -> int:
    answer = 0
    for vertex in vertices:
        answer |= 1 << vertex
    return answer


def connected_after(adjacency: tuple[int, ...], deleted: int) -> bool:
    remaining = ((1 << len(adjacency)) - 1) & ~deleted
    if not remaining:
        return True
    reached = remaining & -remaining
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & remaining & ~reached
        reached |= new
        frontier |= new
    return reached == remaining


def touching(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    return any(
        adjacency[vertex] & right
        for vertex in range(len(adjacency))
        if left & (1 << vertex)
    )


def near_clique_minor_search(
    adjacency: tuple[int, ...], target_order: int
) -> tuple[tuple[int, ...] | None, int]:
    states = 0

    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> tuple[int, ...] | None:
        nonlocal states
        states += 1
        if len(bags) == target_order:
            misses = sum(
                not touching(adjacency, left, right)
                for left, right in combinations(bags, 2)
            )
            return bags if misses <= 1 else None

        for left_index, right_index in combinations(range(len(bags)), 2):
            if not touching(adjacency, bags[left_index], bags[right_index]):
                continue
            merged = [
                bag
                for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            answer = search(tuple(sorted(merged)))
            if answer is not None:
                return answer

        for deleted_index in range(len(bags)):
            answer = search(bags[:deleted_index] + bags[deleted_index + 1 :])
            if answer is not None:
                return answer
        return None

    initial = tuple(1 << vertex for vertex in range(len(adjacency)))
    answer = search(initial)
    return answer, states


def barrier_graph() -> tuple[tuple[int, ...], set[Edge]]:
    cube_edges = {
        edge(0, 1), edge(0, 5), edge(0, 6), edge(1, 2),
        edge(1, 7), edge(2, 3), edge(2, 6), edge(3, 4),
        edge(3, 7), edge(4, 5), edge(4, 6), edge(5, 7),
    }
    centre_edges = {edge(8, vertex) for vertex in range(8)}
    first_exterior = {edge(9, vertex) for vertex in (3, 4, 5, 6, 7)}
    second_exterior = {edge(10, vertex) for vertex in (0, 1, 2, 6, 7)}
    edges = cube_edges | centre_edges | first_exterior | second_exterior
    return adjacency_tuple(11, edges), edges


def calibrate_minor_search() -> None:
    positive_edges = {
        edge(u, v)
        for u, v in combinations(range(7), 2)
        if edge(u, v) != (0, 1)
    }
    positive, _ = near_clique_minor_search(
        adjacency_tuple(7, positive_edges), 7
    )
    assert positive is not None

    complete_six = {
        edge(u, v) for u, v in combinations(range(6), 2)
    }
    negative, _ = near_clique_minor_search(
        adjacency_tuple(6, complete_six), 7
    )
    assert negative is None


def main() -> None:
    calibrate_minor_search()
    adjacency, edges = barrier_graph()
    assert len(adjacency) == 11 and len(edges) == 30

    checked = 0
    for order in range(5):
        for deleted_tuple in combinations(range(11), order):
            assert connected_after(adjacency, vertex_mask(set(deleted_tuple)))
            checked += 1
    first_neighbourhood = {3, 4, 5, 6, 7}
    assert not connected_after(adjacency, vertex_mask(first_neighbourhood))

    centre = 8
    assert adjacency[centre].bit_count() == 8
    closed_neighbourhood = vertex_mask(set(range(9)))
    exterior = ((1 << 11) - 1) & ~closed_neighbourhood
    assert exterior == (1 << 9) | (1 << 10)
    assert not (adjacency[9] & (1 << 10))
    for vertex in range(8):
        common = adjacency[centre] & adjacency[vertex]
        assert common.bit_count() == 3

    model, states = near_clique_minor_search(adjacency, 7)
    assert model is None

    print("GREEN five-connected degree-eight two-component barrier")
    print(f"G: n=11 m=30 kappa=5 deletion_sets_checked={checked}")
    print("centre_degree=8 incident_codegrees=3,3,3,3,3,3,3,3")
    print("exterior_components={9},{10} attachment_orders=5,5")
    print(f"K7_minus_minor=false exact_search_states={states}")


if __name__ == "__main__":
    main()
