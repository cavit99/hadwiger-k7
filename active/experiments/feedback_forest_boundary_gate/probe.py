#!/usr/bin/env python3
"""Hostile screen for two contracted forest components.

For every unlabelled graph Q of order seven or eight which is not
four-colourable and has no K5 subgraph, and every two subsets A,B of order
at least seven, add two nonadjacent vertices with neighbourhoods A and B.
Test exactly whether the augmented graph has a K7-minus-edge minor.

This is a bounded diagnostic only.  It does not prove the corresponding
statement for boundaries of order at most fourteen.
"""

from __future__ import annotations

import itertools
import subprocess
import sys

import networkx as nx


sys.path.insert(0, "active/experiments/five_centre_two_cut_local_quotient")
from probe import has_k7_minus_minor  # noqa: E402


def k_colourable(graph: nx.Graph, colours: int) -> bool:
    vertices = sorted(graph, key=graph.degree, reverse=True)
    assigned: dict[int, int] = {}

    def extend() -> bool:
        if len(assigned) == len(vertices):
            return True
        unassigned = [v for v in vertices if v not in assigned]
        vertex = max(
            unassigned,
            key=lambda v: (
                len({assigned[w] for w in graph[v] if w in assigned}),
                graph.degree(v),
            ),
        )
        forbidden = {assigned[w] for w in graph[vertex] if w in assigned}
        for colour in range(colours):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if extend():
                return True
            del assigned[vertex]
        return False

    return extend()


def k5_free(graph: nx.Graph) -> bool:
    return not any(
        graph.subgraph(vertices).number_of_edges() == 10
        for vertices in itertools.combinations(graph, 5)
    )


def subsets_at_least_seven(order: int):
    vertices = tuple(range(order))
    for size in range(7, order + 1):
        yield from itertools.combinations(vertices, size)


def augment(graph: nx.Graph, left: tuple[int, ...], right: tuple[int, ...]):
    answer = graph.copy()
    x, y = len(graph), len(graph) + 1
    answer.add_nodes_from((x, y))
    answer.add_edges_from((x, vertex) for vertex in left)
    answer.add_edges_from((y, vertex) for vertex in right)
    return answer


def main() -> None:
    eligible = 0
    cases = 0
    for order in (7, 8):
        lines = subprocess.check_output(("geng", "-q", str(order)), text=True)
        for line in lines.splitlines():
            graph = nx.from_graph6_bytes(line.encode())
            graph = nx.convert_node_labels_to_integers(graph)
            if not k5_free(graph) or k_colourable(graph, 4):
                continue
            eligible += 1
            subsets = tuple(subsets_at_least_seven(order))
            for left in subsets:
                for right in subsets:
                    cases += 1
                    host = augment(graph, left, right)
                    if has_k7_minus_minor(host) is None:
                        print(
                            "COUNTEREXAMPLE",
                            f"boundary={line.strip()}",
                            f"left={left}",
                            f"right={right}",
                        )
                        return
    print(f"eligible_boundaries={eligible}")
    print(f"augmented_cases={cases}")
    print("GREEN_BOUNDED_SCREEN")


if __name__ == "__main__":
    main()
