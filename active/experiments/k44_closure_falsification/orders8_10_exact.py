#!/usr/bin/env python3
"""Exact K7-minus census for all seven-connected graphs of orders 8--10."""

from __future__ import annotations

from itertools import combinations

import networkx as nx

from full_attachment_seven_sum import has_k7minus


def component_multisets(order):
    # Every maximum-degree-two graph is a disjoint union of paths and cycles.
    # Type (0,s) is P_s (including an isolated P_1); type (1,s) is C_s.
    types = [(0, size) for size in range(1, order + 1)]
    types += [(1, size) for size in range(3, order + 1)]
    types.sort()

    def recurse(remaining, first):
        if remaining == 0:
            yield ()
            return
        for index in range(first, len(types)):
            kind, size = types[index]
            if size > remaining:
                continue
            for rest in recurse(remaining - size, index):
                yield ((kind, size),) + rest

    yield from recurse(order, 0)


def graph_from_components(types):
    return nx.disjoint_union_all(
        nx.path_graph(size) if kind == 0 else nx.cycle_graph(size)
        for kind, size in types
    )


def target_subgraph(graph):
    return any(
        graph.subgraph(vertices).number_of_edges() >= 20
        for vertices in combinations(graph, 7)
    )


def literal_k44(graph):
    vertices = set(graph)
    for left in combinations(graph, 4):
        common = vertices - set(left)
        for vertex in left:
            common.intersection_update(graph[vertex])
        if len(common) >= 4:
            return True
    return False


def main():
    expected = {
        8: (46, 1, 1, 1, 0),
        9: (70, 5, 5, 4, 1),
        10: (106, 87, 87, 47, 40),
    }
    for order in range(8, 11):
        generated = seven_connected = literal = subgraph = proper = 0
        for types in component_multisets(order):
            generated += 1
            graph = nx.complement(graph_from_components(types))
            if nx.node_connectivity(graph) < 7:
                continue
            seven_connected += 1
            literal += literal_k44(graph)
            if target_subgraph(graph):
                subgraph += 1
            else:
                bags = has_k7minus(graph)
                assert bags is not None
                proper += 1
        row = (generated, seven_connected, literal, subgraph, proper)
        assert row == expected[order]
        print(
            "order", order, "generated", generated,
            "seven_connected", seven_connected, "literal_k44", literal,
            "target_subgraph", subgraph, "proper_minor", proper,
        )


if __name__ == "__main__":
    main()
