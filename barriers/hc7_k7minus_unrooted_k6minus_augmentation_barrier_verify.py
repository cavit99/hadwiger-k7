#!/usr/bin/env python3
"""Check the one-apex icosahedral unrooted-augmentation barrier.

Run with

    UV_CACHE_DIR=/tmp/hadwiger-uv-cache uv run python \
      barriers/hc7_k7minus_unrooted_k6minus_augmentation_barrier_verify.py

The exclusion of a K_7^- minor is proved by planarity in the accompanying
note.  This checker verifies the construction, connectivity, density and the
displayed K_6^- branch-set certificate independently of Lo's theorem.
"""

from itertools import combinations

import networkx as nx


def touching(graph: nx.Graph, left: set[int], right: set[int]) -> bool:
    return any(graph.has_edge(x, y) for x in left for y in right)


def check_near_clique_model(
    graph: nx.Graph, bags: tuple[set[int], ...]
) -> int:
    assert all(bag for bag in bags)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(left.isdisjoint(right) for left, right in combinations(bags, 2))
    missing = sum(
        not touching(graph, left, right)
        for left, right in combinations(bags, 2)
    )
    assert missing <= 1
    return missing


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

    bags = (
        {7},
        {0, 1, 2, 3, 4, 5, 6, 8},
        {9},
        {10},
        {11},
        {apex},
    )
    assert check_near_clique_model(graph, bags) == 1
    assert not nx.check_planarity(nx.complete_graph(6))[0]
    k6_minus = nx.complete_graph(6)
    k6_minus.remove_edge(0, 1)
    assert not nx.check_planarity(k6_minus)[0]

    print("GREEN unrooted K6-minus augmentation barrier")
    print("order=13 size=42 connectivity=6 density_gap_to_4n=10")
    print("base=icosahedron order=12 size=30 connectivity=5 planar=true")
    print("K6_minus_certificate_missing_pair=9|11")
    print("K7_minus_minor=false_by_planar_base_argument")


if __name__ == "__main__":
    main()
