#!/usr/bin/env python3
"""Exploratory screen for the low-Jakobsen-defect neighbourhood route.

Every graph on eight vertices is obtained by adjoining one vertex to one of
the 1,044 unlabelled graphs on seven vertices in NetworkX's graph atlas.  We
therefore need no external ``geng`` binary.  The search stops at the first
exceptional neighbourhood of minimum degree at least three whose canonical
two-distinct-miss quotient has no ``K_7^-`` minor.

This is an exploratory falsifier, not a promoted finite theorem.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations

import networkx as nx


BOUNDARY_ORDER = 8
QUOTIENT_ORDER = 11


def atlas_graphs_of_order(order: int) -> list[nx.Graph]:
    return [graph for graph in nx.graph_atlas_g() if len(graph) == order]


def adjacency_from_extension(base: nx.Graph, neighbours: int) -> tuple[int, ...]:
    adjacency = [0] * BOUNDARY_ORDER
    for left, right in base.edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    for vertex in range(7):
        if neighbours & (1 << vertex):
            adjacency[vertex] |= 1 << 7
            adjacency[7] |= 1 << vertex
    return tuple(adjacency)


def is_clique(adjacency: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(adjacency[left] & (1 << right) for left, right in combinations(vertices, 2))


def is_independent(adjacency: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(not adjacency[left] & (1 << right) for left, right in combinations(vertices, 2))


def exceptional_minimum_three(adjacency: tuple[int, ...]) -> bool:
    vertices = range(BOUNDARY_ORDER)
    return (
        min(row.bit_count() for row in adjacency) >= 3
        and not any(is_clique(adjacency, group) for group in combinations(vertices, 4))
        and any(is_independent(adjacency, group) for group in combinations(vertices, 3))
        and not any(is_independent(adjacency, group) for group in combinations(vertices, 4))
    )


def quotient(adjacency: tuple[int, ...], first_miss: int, second_miss: int) -> tuple[int, ...]:
    answer = list(adjacency) + [0, 0, 0]
    centre, first, second = 8, 9, 10
    for vertex in range(BOUNDARY_ORDER):
        answer[centre] |= 1 << vertex
        answer[vertex] |= 1 << centre
        if vertex != first_miss:
            answer[first] |= 1 << vertex
            answer[vertex] |= 1 << first
        if vertex != second_miss:
            answer[second] |= 1 << vertex
            answer[vertex] |= 1 << second
    return tuple(answer)


def connected(adjacency: tuple[int, ...], bag: int) -> bool:
    reached = bag & -bag
    while reached:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= adjacency[bit.bit_length() - 1] & bag
        if expanded == reached:
            return reached == bag
        reached = expanded
    return False


def has_k7minus_minor(adjacency: tuple[int, ...]) -> bool:
    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> bool:
        if len(bags) == 7:
            contacts = 0
            for left, right in combinations(bags, 2):
                if any(adjacency[vertex] & right for vertex in range(QUOTIENT_ORDER) if left & (1 << vertex)):
                    contacts += 1
            return contacts >= 20

        touching: list[tuple[int, int, int]] = []
        for left_index, right_index in combinations(range(len(bags)), 2):
            left, right = bags[left_index], bags[right_index]
            if any(adjacency[vertex] & right for vertex in range(QUOTIENT_ORDER) if left & (1 << vertex)):
                outside_score = -int(bool(left & 0x700)) - int(bool(right & 0x700))
                touching.append((outside_score, left_index, right_index))
        touching.sort()
        for _, left_index, right_index in touching:
            merged = [bag for index, bag in enumerate(bags) if index not in (left_index, right_index)]
            merged.append(bags[left_index] | bags[right_index])
            if search(tuple(sorted(merged))):
                return True
        for deleted_index in range(len(bags)):
            reduced = bags[:deleted_index] + bags[deleted_index + 1 :]
            if search(reduced):
                return True
        return False

    return search(tuple(1 << vertex for vertex in range(QUOTIENT_ORDER)))


def graph6(adjacency: tuple[int, ...]) -> str:
    graph = nx.Graph()
    graph.add_nodes_from(range(BOUNDARY_ORDER))
    graph.add_edges_from(
        (left, right)
        for left, right in combinations(range(BOUNDARY_ORDER), 2)
        if adjacency[left] & (1 << right)
    )
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def main() -> None:
    bases = atlas_graphs_of_order(7)
    assert len(bases) == 1_044
    eligible = 0
    for base_index, base in enumerate(bases):
        for neighbours in range(1 << 7):
            adjacency = adjacency_from_extension(base, neighbours)
            if not exceptional_minimum_three(adjacency):
                continue
            eligible += 1
            for first_miss, second_miss in combinations(range(BOUNDARY_ORDER), 2):
                if not has_k7minus_minor(quotient(adjacency, first_miss, second_miss)):
                    print(
                        "SURVIVOR",
                        f"graph6={graph6(adjacency)}",
                        f"misses={first_miss},{second_miss}",
                        f"base={base_index}",
                        f"extension={neighbours}",
                        f"eligible_seen={eligible}",
                    )
                    return
        if base_index % 100 == 0:
            print(f"progress base={base_index} eligible={eligible}", flush=True)
    print(f"PASS eligible_extension_representations={eligible}")


if __name__ == "__main__":
    main()
