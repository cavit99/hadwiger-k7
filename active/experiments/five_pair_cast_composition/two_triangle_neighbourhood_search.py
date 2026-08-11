#!/usr/bin/env python3
"""Classify the two-triangle exceptional-neighbourhood residue.

The eight neighbours are two anticomplete triangles A,B and two
nonadjacent poles p,q.  Only pole--triangle edges vary.  We retain exactly
the patterns with independence number three and no K4, then test for a
K6-minus-edge minor by enumerating connected set partitions.
"""

from __future__ import annotations

import itertools

import networkx as nx


A = (0, 1, 2)
B = (3, 4, 5)
P = 6
Q = 7
VARIABLE = tuple((pole, vertex) for pole in (P, Q) for vertex in A + B)


def clique_number(graph: nx.Graph) -> int:
    return max(map(len, nx.find_cliques(graph)), default=0)


def connected_partitions(graph: nx.Graph, parts: int):
    vertices = tuple(graph)

    def rec(index: int, bags: list[list[int]]):
        if index == len(vertices):
            if len(bags) == parts and all(
                nx.is_connected(graph.subgraph(bag)) for bag in bags
            ):
                yield tuple(frozenset(bag) for bag in bags)
            return
        remaining = len(vertices) - index
        if len(bags) > parts or len(bags) + remaining < parts:
            return
        vertex = vertices[index]
        for bag in bags:
            bag.append(vertex)
            yield from rec(index + 1, bags)
            bag.pop()
        if len(bags) < parts:
            bags.append([vertex])
            yield from rec(index + 1, bags)
            bags.pop()

    # A minor model may omit vertices.  Enumerate every used vertex set.
    for order in range(parts, len(vertices) + 1):
        for used in itertools.combinations(vertices, order):
            induced = graph.subgraph(used).copy()
            old_vertices = vertices
            vertices = tuple(induced)  # type: ignore[misc]
            yield from rec(0, [])
            vertices = old_vertices  # type: ignore[misc]


def k6_minus_model(graph: nx.Graph):
    for bags in connected_partitions(graph, 6):
        misses = 0
        for left, right in itertools.combinations(bags, 2):
            if not any(graph.has_edge(u, v) for u in left for v in right):
                misses += 1
                if misses > 1:
                    break
        if misses <= 1:
            return bags
    return None


def graph_from_mask(mask: int) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(8))
    graph.add_edges_from(itertools.combinations(A, 2))
    graph.add_edges_from(itertools.combinations(B, 2))
    graph.add_edges_from(
        edge for index, edge in enumerate(VARIABLE) if mask & (1 << index)
    )
    return graph


def main() -> None:
    valid = 0
    target_free = []
    for mask in range(1 << len(VARIABLE)):
        graph = graph_from_mask(mask)
        if clique_number(graph) >= 4:
            continue
        if clique_number(nx.complement(graph)) != 3:
            continue
        valid += 1
        model = k6_minus_model(graph)
        if model is None:
            target_free.append(mask)
            print(
                "TARGET_FREE",
                {
                    "pA": sorted(set(graph.neighbors(P)) & set(A)),
                    "pB": sorted(set(graph.neighbors(P)) & set(B)),
                    "qA": sorted(set(graph.neighbors(Q)) & set(A)),
                    "qB": sorted(set(graph.neighbors(Q)) & set(B)),
                },
            )
    print("SUMMARY", {"valid": valid, "target_free": len(target_free)})


if __name__ == "__main__":
    main()
