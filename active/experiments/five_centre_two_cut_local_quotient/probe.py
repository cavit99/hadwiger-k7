#!/usr/bin/env python3
"""Probe the retained-centre ten-vertex quotient.

Y has seven vertices, alpha(Y) <= 2, and no K4 subgraph.  Add a centre z
complete to Y plus x, with x anticomplete to Y, and an exterior connected
bag e adjacent to all but at most one vertex of Y plus x.  Test whether the
result always contains K7 minus an edge as a minor.

This is an exploratory exhaustive check over the NetworkX graph atlas.
"""

from __future__ import annotations

import argparse
from itertools import combinations

import networkx as nx


def set_partitions_exact(items: tuple[int, ...], blocks: int):
    """Yield canonical set partitions of items into exactly blocks blocks."""
    if not items:
        if blocks == 0:
            yield ()
        return
    first, rest = items[0], items[1:]
    for partition in set_partitions_exact(rest, blocks - 1):
        yield ((first,),) + partition
    for partition in set_partitions_exact(rest, blocks):
        for index in range(len(partition)):
            yield partition[:index] + (partition[index] + (first,),) + partition[index + 1 :]


def candidate_partitions():
    vertices = tuple(range(10))
    for size in range(7, 11):
        for selected in combinations(vertices, size):
            yield from set_partitions_exact(selected, 7)


def candidate_partitions_n(vertex_count: int):
    vertices = tuple(range(vertex_count))
    for size in range(7, vertex_count + 1):
        for selected in combinations(vertices, size):
            yield from set_partitions_exact(selected, 7)


PARTITIONS_BY_ORDER = {
    order: tuple(candidate_partitions_n(order)) for order in (9, 10, 11)
}
PARTITIONS = PARTITIONS_BY_ORDER[10]
PARTITIONS_11 = PARTITIONS_BY_ORDER[11]


def alpha_at_most_two(graph: nx.Graph) -> bool:
    return all(graph.subgraph(triple).number_of_edges() > 0 for triple in combinations(graph, 3))


def k4_free(graph: nx.Graph) -> bool:
    return all(graph.subgraph(four).number_of_edges() < 6 for four in combinations(graph, 4))


def has_k7_minus_minor(graph: nx.Graph):
    adjacency = {v: set(graph[v]) for v in graph}
    partitions = PARTITIONS_BY_ORDER[len(graph)]
    for partition in partitions:
        if any(len(block) > 1 and not nx.is_connected(graph.subgraph(block)) for block in partition):
            continue
        missing = []
        for i, j in combinations(range(7), 2):
            if not any(v in adjacency[u] for u in partition[i] for v in partition[j]):
                missing.append((i, j))
                if len(missing) > 1:
                    break
        if len(missing) <= 1:
            return partition, tuple(missing)
    return None


def quotient(y_graph: nx.Graph, missed: int | None) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(10))
    graph.add_edges_from(y_graph.edges())
    x, z, exterior = 7, 8, 9
    graph.add_edges_from((z, v) for v in range(8))
    graph.add_edges_from((exterior, v) for v in range(8) if v != missed)
    return graph


def quotient_two_exteriors(y_graph: nx.Graph, missed_1: int | None, missed_2: int | None) -> nx.Graph:
    graph = quotient(y_graph, missed_1)
    graph.add_node(10)
    graph.add_edges_from((10, v) for v in range(8) if v != missed_2)
    return graph


def neighbourhood_with_ears(y_graph: nx.Graph, y: int, ends: tuple[int, int]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(9))
    graph.add_edges_from(y_graph.edges())
    x, z = 7, 8
    graph.add_edges_from((z, v) for v in range(8))
    graph.add_edges_from((y, end) for end in ends)
    return graph


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skip-ears",
        action="store_true",
        help="verify only the recorded one- and two-exterior phases",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates = []
    for graph in nx.graph_atlas_g():
        if graph.number_of_nodes() != 7:
            continue
        if not alpha_at_most_two(graph) or not k4_free(graph):
            continue
        candidates.append(graph)

    blockers = []
    witnesses = {}
    for index, y_graph in enumerate(candidates):
        for missed in (None, *range(8)):
            witness = has_k7_minus_minor(quotient(y_graph, missed))
            if witness is None:
                blockers.append((index, missed, nx.to_graph6_bytes(y_graph, header=False).strip().decode()))
            else:
                witnesses[(index, missed)] = witness

    print({"partitions": len(PARTITIONS), "candidate_Y": len(candidates), "cases": 9 * len(candidates)})
    print({"blockers": len(blockers)})
    for blocker in blockers[:50]:
        print("BLOCKER", blocker)

    two_exterior_blockers = []
    for index, missed_1, _ in blockers:
        y_graph = candidates[index]
        for missed_2 in (None, *range(8)):
            if has_k7_minus_minor(quotient_two_exteriors(y_graph, missed_1, missed_2)) is None:
                two_exterior_blockers.append((index, missed_1, missed_2))
    print({"partitions_11": len(PARTITIONS_11), "two_exterior_cases": 9 * len(blockers)})
    print({"two_exterior_blockers": len(two_exterior_blockers)})
    for blocker in two_exterior_blockers[:50]:
        print("TWO_EXTERIOR_BLOCKER", blocker)

    if args.skip_ears:
        return

    ear_blockers = []
    for index, y_graph in enumerate(candidates):
        for y in y_graph:
            if y_graph.degree(y) != 3:
                continue
            missing_ends = tuple(v for v in range(7) if v != y and not y_graph.has_edge(y, v)) + (7,)
            for ends in combinations(missing_ends, 2):
                if has_k7_minus_minor(neighbourhood_with_ears(y_graph, y, ends)) is None:
                    ear_blockers.append((index, y, ends))
    print({"two_ear_cases": sum(1 for g in candidates for y in g if g.degree(y) == 3) * 6})
    print({"two_ear_blockers": len(ear_blockers)})
    for blocker in ear_blockers[:50]:
        print("TWO_EAR_BLOCKER", blocker)


if __name__ == "__main__":
    main()
