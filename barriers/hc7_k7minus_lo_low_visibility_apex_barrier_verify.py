#!/usr/bin/env python3
"""Verify the four-visible one-apex icosahedral Lo barrier.

Run with

    UV_CACHE_DIR=/tmp/uv-cache uv run python \
      barriers/hc7_k7minus_lo_low_visibility_apex_barrier_verify.py
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def touching(graph: nx.Graph, left: set[int], right: set[int]) -> bool:
    return any(graph.has_edge(x, y) for x in left for y in right)


def model_profile(
    graph: nx.Graph,
    bags: tuple[set[int], ...],
    roots: set[int],
) -> tuple[int, int]:
    assert len(bags) == 6
    assert all(bags)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(left.isdisjoint(right) for left, right in combinations(bags, 2))
    missing = sum(
        not touching(graph, left, right)
        for left, right in combinations(bags, 2)
    )
    visible = sum(bool(bag & roots) for bag in bags)
    return missing, visible


def main() -> None:
    base = nx.icosahedral_graph()
    assert len(base) == 12
    assert base.number_of_edges() == 30
    assert nx.node_connectivity(base) == 5
    assert nx.check_planarity(base)[0]

    graph = base.copy()
    apex = 12
    graph.add_node(apex)
    graph.add_edges_from((apex, vertex) for vertex in base)

    assert len(graph) == 13
    assert graph.number_of_edges() == 42 == 4 * len(graph) - 10
    assert nx.node_connectivity(graph) == 6

    vertex = 0
    deletion = graph.copy()
    deletion.remove_node(vertex)
    assert len(deletion) == 12
    assert deletion.number_of_edges() == 36
    assert nx.node_connectivity(deletion) == 5
    assert min(dict(deletion.degree()).values()) == 5
    assert not nx.check_planarity(deletion)[0]

    bags = (
        {1},
        {2},
        {3},
        {5, 6},
        {4, 7, 8, 10},
        {apex},
    )
    assert model_profile(deletion, bags, set(graph[vertex])) == (1, 4)

    # The proof uses only these two sharp planarity calibrations.
    k6_minus = nx.complete_graph(6)
    k6_minus.remove_edge(0, 1)
    assert not nx.check_planarity(k6_minus)[0]
    assert 15 - 2 > 3 * 6 - 6

    print("GREEN one-apex icosahedral low-visibility Lo barrier")
    print("host_order=13 host_size=42 connectivity=6 density_gap_to_4n=10")
    print("deletion_order=12 deletion_size=36 connectivity=5 delta=5")
    print("displayed_model_missing=1 visibility=4")
    print("maximum_visibility=4 by planar six-vertex edge bound")


if __name__ == "__main__":
    main()
