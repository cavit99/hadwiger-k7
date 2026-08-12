#!/usr/bin/env python3
"""Test the three-piece repair of the tight adjacent-pair obstruction.

The adjacent 6/6 screen returns one obstruction on the boundary encoded by
``GCpU}{``.  Keep its two terminal neighbourhoods fixed, replace their edge
by a path through a third exterior vertex, and give that middle vertex every
boundary neighbourhood of order at least five.  This is a targeted bounded
diagnostic, not an unbounded theorem.
"""

from __future__ import annotations

import itertools
import sys

import networkx as nx


sys.path.insert(0, "active/experiments/five_centre_two_cut_local_quotient")
from probe import has_k7_minus_minor  # noqa: E402


BOUNDARY = "GCpU}{"
LEFT = (0, 1, 2, 3, 4, 6)
RIGHT = (0, 1, 2, 3, 4, 7)


def adjacent_pair(graph: nx.Graph) -> nx.Graph:
    answer = graph.copy()
    x, y = len(graph), len(graph) + 1
    answer.add_edge(x, y)
    answer.add_edges_from((x, vertex) for vertex in LEFT)
    answer.add_edges_from((y, vertex) for vertex in RIGHT)
    return answer


def three_piece_path(graph: nx.Graph, middle_set: tuple[int, ...]) -> nx.Graph:
    answer = graph.copy()
    x, middle, y = len(graph), len(graph) + 1, len(graph) + 2
    answer.add_edges_from(((x, middle), (middle, y)))
    answer.add_edges_from((x, vertex) for vertex in LEFT)
    answer.add_edges_from((middle, vertex) for vertex in middle_set)
    answer.add_edges_from((y, vertex) for vertex in RIGHT)
    return answer


def main() -> None:
    graph = nx.convert_node_labels_to_integers(
        nx.from_graph6_bytes(BOUNDARY.encode())
    )
    if has_k7_minus_minor(adjacent_pair(graph)) is not None:
        raise RuntimeError("the recorded adjacent-pair obstruction did not reproduce")

    cases = 0
    for size in range(5, len(graph) + 1):
        for middle_set in itertools.combinations(range(len(graph)), size):
            cases += 1
            if has_k7_minus_minor(three_piece_path(graph, middle_set)) is None:
                print("COUNTEREXAMPLE", f"middle={middle_set}")
                return

    print(f"boundary={BOUNDARY}")
    print(f"middle_neighbourhoods={cases}")
    print("GREEN_TARGETED_REPAIR_SCREEN")


if __name__ == "__main__":
    main()
