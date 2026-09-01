#!/usr/bin/env python3
"""Independent concrete check of a SAT assignment from splitter search.

This source deliberately does not import the Z3 search encoding.  It checks
boundary inequalities and contracted labelled graphs directly with NetworkX,
then independently enumerates the three terminal model types.  A reported
SAT assignment passes only if every contractible edge is unsafe and no
terminal model exists.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product

import networkx as nx


def weight(labels: dict[int, int], vertices: set[int]) -> int:
    mask = 0
    for vertex in vertices:
        mask |= labels[vertex]
    return mask.bit_count()


def boundary(graph: nx.Graph, vertices: set[int]) -> set[int]:
    answer: set[int] = set()
    for vertex in vertices:
        answer.update(graph.neighbors(vertex))
    return answer - vertices


def inequalities(graph: nx.Graph, labels: dict[int, int]):
    nodes = tuple(graph.nodes())
    bad = []
    for mask in range(1, 1 << len(nodes)):
        vertices = {nodes[i] for i in range(len(nodes)) if (mask >> i) & 1}
        value = len(boundary(graph, vertices)) + weight(labels, vertices)
        if value < 7:
            bad.append((vertices, value))
    return bad


def touches(graph: nx.Graph, left: set[int], right: set[int]) -> bool:
    return any(graph.has_edge(u, v) for u in left for v in right)


def terminal_assignment(
    graph: nx.Graph, labels: dict[int, int], number: int, threshold: int
):
    nodes = tuple(graph.nodes())
    # For A category 0 means unused.  For spanning B no category is unused.
    choices = range(number + 1) if number == 3 else range(number)
    for assignment in product(choices, repeat=len(nodes)):
        if number == 3:
            bags = [
                {nodes[i] for i, value in enumerate(assignment) if value == j}
                for j in range(1, 4)
            ]
        else:
            bags = [
                {nodes[i] for i, value in enumerate(assignment) if value == j}
                for j in range(4)
            ]
        if any(not bag for bag in bags):
            continue
        if any(not nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        if any(
            not touches(graph, bags[i], bags[j])
            for i in range(number)
            for j in range(i + 1, number)
        ):
            continue
        if all(weight(labels, bag) >= threshold for bag in bags):
            return [sorted(bag) for bag in bags]
    return None


def set_partitions(vertices: tuple[int, ...], number: int):
    """Unordered partitions of ``vertices`` into ``number`` nonempty sets."""
    blocks: list[set[int]] = []

    def search(index: int, used: int):
        if index == len(vertices):
            if used == number:
                yield tuple(frozenset(block) for block in blocks)
            return
        vertex = vertices[index]
        for block_index in range(min(used + 1, number)):
            if block_index == used:
                blocks.append(set())
            blocks[block_index].add(vertex)
            yield from search(index + 1, max(used, block_index + 1))
            blocks[block_index].remove(vertex)
            if block_index == used:
                blocks.pop()

    yield from search(0, 0)


def terminal_d(graph: nx.Graph, labels: dict[int, int]):
    nodes = tuple(graph.nodes())
    for used_size in range(6, len(nodes) + 1):
        for used in combinations(nodes, used_size):
            for bags in set_partitions(used, 6):
                if any(not nx.is_connected(graph.subgraph(bag)) for bag in bags):
                    continue
                quotient_edges = sum(
                    touches(graph, set(bags[i]), set(bags[j]))
                    for i, j in combinations(range(6), 2)
                )
                if quotient_edges < 14:
                    continue
                if all(weight(labels, set(bag)) >= 1 for bag in bags):
                    return [sorted(bag) for bag in bags]
    return None


def contracted_instance(graph: nx.Graph, labels: dict[int, int], u: int, v: int):
    contracted = nx.contracted_nodes(graph, u, v, self_loops=False, copy=True)
    contracted_labels = {x: labels[x] for x in contracted.nodes()}
    contracted_labels[u] = labels[u] | labels[v]
    return contracted, contracted_labels


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness")
    args = parser.parse_args()
    with open(args.witness, encoding="utf-8") as handle:
        record = json.load(handle)
    graph = nx.from_graph6_bytes(record["graph6"].encode())
    assert len(record["label_masks"]) == len(graph)
    assert all(
        isinstance(mask, int) and 0 <= mask < (1 << 8)
        for mask in record["label_masks"]
    )
    labels = {vertex: mask for vertex, mask in enumerate(record["label_masks"])}
    assert nx.node_connectivity(graph) >= 3
    assert not inequalities(graph, labels)

    contractible = []
    violations = {}
    for u, v in graph.edges():
        contracted, merged_labels = contracted_instance(graph, labels, u, v)
        if nx.node_connectivity(contracted) < 3:
            continue
        edge = tuple(sorted((u, v)))
        contractible.append(edge)
        bad = inequalities(contracted, merged_labels)
        if bad:
            violations[f"{edge[0]}-{edge[1]}"] = [sorted(bad[0][0]), bad[0][1]]
    assert sorted(contractible) == sorted(map(tuple, record["contractible_edges"]))
    assert len(violations) == len(contractible)

    blocker_checks = {}
    for edge_name, mask in record["chosen_blockers"].items():
        u, v = map(int, edge_name.split("-"))
        vertices = {x for x in graph if (mask >> x) & 1}
        exterior = boundary(graph, vertices)
        blocker_checks[edge_name] = {
            "vertices": sorted(vertices),
            "boundary": sorted(exterior),
            "weight": weight(labels, vertices),
        }
        assert u not in vertices and v not in vertices
        assert u in exterior and v in exterior
        assert len(exterior) + weight(labels, vertices) == 7

    terminal_a = terminal_assignment(graph, labels, 3, 4)
    terminal_b = terminal_assignment(graph, labels, 4, 3)
    terminal_six = terminal_d(graph, labels)
    assert terminal_a is None
    assert terminal_b is None
    assert terminal_six is None
    print("PASS independent weighted-splitter counterexample validation")
    print("graph6", record["graph6"], "kappa", nx.node_connectivity(graph))
    print("boundary_inequalities", (1 << len(graph)) - 1, "all_pass")
    print("contractible_edges", len(contractible), "all_fail_after_explicit_contraction")
    print("terminal_A", terminal_a)
    print("terminal_B", terminal_b)
    print("terminal_D", terminal_six)
    print("first_blocker", next(iter(blocker_checks.items())))


if __name__ == "__main__":
    main()
