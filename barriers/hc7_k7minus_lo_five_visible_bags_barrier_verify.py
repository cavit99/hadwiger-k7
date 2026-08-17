#!/usr/bin/env python3
"""Verify the K_{2,2,2,2} five-visible-bag Lo barrier.

Run with

    UV_CACHE_DIR=/tmp/uv-cache uv run python \
      barriers/hc7_k7minus_lo_five_visible_bags_barrier_verify.py
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations

import networkx as nx


def encoded_graph(graph: nx.Graph) -> tuple[tuple[int, ...], tuple[int, ...]]:
    nodes = tuple(sorted(graph))
    position = {vertex: index for index, vertex in enumerate(nodes)}
    adjacency = tuple(
        sum(1 << position[neighbour] for neighbour in graph[vertex])
        for vertex in nodes
    )
    return nodes, adjacency


def touching(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    remaining = left
    while remaining:
        bit = remaining & -remaining
        index = bit.bit_length() - 1
        if adjacency[index] & right:
            return True
        remaining -= bit
    return False


def connected(adjacency: tuple[int, ...], bag: int) -> bool:
    reached = bag & -bag
    while reached:
        expanded = reached
        remaining = reached
        while remaining:
            bit = remaining & -remaining
            index = bit.bit_length() - 1
            expanded |= adjacency[index] & bag
            remaining -= bit
        if expanded == reached:
            return reached == bag
        reached = expanded
    return False


def missing_pairs(
    adjacency: tuple[int, ...], bags: tuple[int, ...]
) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left_index, right_index)
        for left_index, right_index in combinations(range(len(bags)), 2)
        if not touching(
            adjacency, bags[left_index], bags[right_index]
        )
    )


def all_near_models(
    graph: nx.Graph, target_order: int
) -> tuple[tuple[int, ...], ...]:
    nodes, adjacency = encoded_graph(graph)
    answers: set[tuple[int, ...]] = set()

    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> None:
        if len(bags) == target_order:
            if len(missing_pairs(adjacency, bags)) <= 1:
                assert all(connected(adjacency, bag) for bag in bags)
                answers.add(bags)
            return

        for deleted_index in range(len(bags)):
            search(bags[:deleted_index] + bags[deleted_index + 1 :])

        for left_index, right_index in combinations(range(len(bags)), 2):
            if not touching(
                adjacency, bags[left_index], bags[right_index]
            ):
                continue
            merged = [
                bag
                for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            search(tuple(sorted(merged)))

    search(tuple(1 << index for index in range(len(nodes))))
    return tuple(sorted(answers))


def has_safe_split(
    adjacency: tuple[int, ...], bags: tuple[int, ...], roots: int
) -> bool:
    visible = [bag for bag in bags if bag & roots]
    invisible = [bag for bag in bags if not bag & roots]
    assert len(visible) == 5 and len(invisible) == 1

    for split_index, bag in enumerate(visible):
        proper = (bag - 1) & bag
        while proper:
            left = proper
            right = bag ^ left
            proper = (proper - 1) & bag
            if left > right:
                continue
            if not left & roots or not right & roots:
                continue
            if not connected(adjacency, left) or not connected(adjacency, right):
                continue
            candidate = tuple(
                sorted(
                    [
                        other
                        for index, other in enumerate(visible)
                        if index != split_index
                    ]
                    + [left, right]
                )
            )
            if len(missing_pairs(adjacency, candidate)) <= 1:
                return True
    return False


def main() -> None:
    graph = nx.complete_multipartite_graph(2, 2, 2, 2)
    vertex = 0
    roots_as_vertices = set(graph[vertex])

    assert len(graph) == 8
    assert graph.number_of_edges() == 24 == 4 * len(graph) - 8
    assert nx.node_connectivity(graph) == 6
    assert not all_near_models(graph, 7)

    deletion = graph.copy()
    deletion.remove_node(vertex)
    nodes, adjacency = encoded_graph(deletion)
    position = {name: index for index, name in enumerate(nodes)}
    roots = sum(1 << position[root] for root in roots_as_vertices)

    assert len(deletion) == 7
    assert deletion.number_of_edges() == 18
    assert min(dict(deletion.degree()).values()) == 5
    assert nx.node_connectivity(deletion) == 5
    assert not nx.check_planarity(deletion)[0]

    left = (1, 2, 3)
    right = (4, 5, 6, 7)
    assert all(deletion.has_edge(x, y) for x in left for y in right)

    models = all_near_models(deletion, 6)
    profile = Counter()
    for bags in models:
        visibility = sum(bool(bag & roots) for bag in bags)
        misses = len(missing_pairs(adjacency, bags))
        profile[(visibility, misses)] += 1
        assert not has_safe_split(adjacency, bags, roots)

    assert len(models) == 12
    assert profile == Counter({(5, 1): 12})

    displayed_vertex_bags = ({1}, {3}, {2, 4}, {5}, {6}, {7})
    displayed = tuple(
        sorted(
            sum(1 << position[vertex] for vertex in bag)
            for bag in displayed_vertex_bags
        )
    )
    assert displayed in models

    positive = nx.complete_graph(7)
    positive.remove_edge(0, 1)
    assert all_near_models(positive, 7)

    print("GREEN K2222 five-visible-bag Lo barrier")
    print("host_order=8 host_size=24 connectivity=6 density_gap_to_4n=8")
    print("deletion_order=7 deletion_size=18 connectivity=5 delta=5 nonplanar=true")
    print("near_six_models=12 visibility_profile={(5,1):12} safe_splits=0")
    print("K7_minus_minor=false")


if __name__ == "__main__":
    main()
