#!/usr/bin/env python3
"""Finite falsification probe; no reduction from an HC7-critical host is claimed.

Run: uv run python3 active/hc7_degree7_exceptional_layers_probe.py
Each graph has 10--12 vertices, a K3+K4 boundary, one deleted equality
edge xy, two u-essential endpoint layers, and three internal endpoint
layers containing the three singleton boundary roots. Exact K7 detection
uses connected-subset compatibility; tree decompositions independently
certify some negative cases. These are selected-response models only.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


def clique_minor(graph: nx.Graph, order: int) -> list[list[str]] | None:
    nodes = list(graph)
    n = len(nodes)
    position = {v: i for i, v in enumerate(nodes)}
    adjacency = [0] * n
    for u, v in graph.edges():
        adjacency[position[u]] |= 1 << position[v]
        adjacency[position[v]] |= 1 << position[u]
    neighbours = [0] * (1 << n)
    candidates = []
    for mask in range(1, 1 << n):
        bit = mask & -mask
        neighbours[mask] = neighbours[mask ^ bit] | adjacency[bit.bit_length() - 1]
        if mask.bit_count() > n - order + 1:
            continue
        reached = bit
        while True:
            enlarged = reached | (neighbours[reached] & mask)
            if enlarged == reached:
                break
            reached = enlarged
        if reached == mask:
            candidates.append(mask)
    candidates.sort(key=lambda mask: (mask.bit_count(), mask))
    compatible = [0] * len(candidates)
    for i, left in enumerate(candidates):
        for j in range(i + 1, len(candidates)):
            right = candidates[j]
            if not left & right and neighbours[left] & right:
                compatible[i] |= 1 << j

    def search(chosen: list[int], allowed: int, used: int):
        remaining = order - len(chosen)
        if remaining == 0:
            return chosen
        if allowed.bit_count() < remaining or n - used.bit_count() < remaining:
            return None
        while allowed:
            bit = allowed & -allowed
            allowed ^= bit
            index = bit.bit_length() - 1
            if n - (used | candidates[index]).bit_count() < remaining - 1:
                continue
            result = search(chosen + [index], allowed & compatible[index],
                            used | candidates[index])
            if result is not None:
                return result
        return None

    result = search([], (1 << len(candidates)) - 1, 0)
    if result is None:
        return None
    bags = [[nodes[i] for i in range(n) if candidates[j] & (1 << i)] for j in result]
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert all(any(graph.has_edge(a, b) for a in bags[i] for b in bags[j])
               for i, j in combinations(range(order), 2))
    return bags


def build(crossed: bool, pinches: int) -> tuple[nx.Graph, dict[str, int]]:
    boundary = ["b1", "b2", "c1", "c2", "r3", "r4", "r5"]
    graph = nx.Graph()
    graph.add_nodes_from(["u", "x", "y"] + boundary)
    left = ["b1", "c2" if crossed else "c1", "r3"]
    right = [v for v in boundary if v not in left]
    graph.add_edges_from(combinations(left, 2))
    graph.add_edges_from(combinations(right, 2))
    graph.add_edges_from(("u", v) for v in boundary)
    graph.add_edges_from([("x", "y"), ("x", "b1"), ("y", "b2"),
                          ("x", "c1"), ("y", "c2")])
    graph.add_edges_from((v, root) for v in ("x", "y") for root in boundary[4:])
    colours = {"u": 0, "x": 0, "y": 0, "b1": 1, "b2": 1,
               "c1": 2, "c2": 2, "r3": 3, "r4": 4, "r5": 5}
    if pinches >= 1:
        graph.add_edges_from([("z", "b1"), ("z", "c2")])
        colours["z"] = 0
    if pinches >= 2:
        graph.add_edges_from([("w", "b2"), ("w", "c1")])
        colours["w"] = 0
    return graph, colours


def verify_trace(graph: nx.Graph, colours: dict[str, int]) -> None:
    deleted = graph.copy()
    deleted.remove_edge("x", "y")
    assert all(colours[v] != colours[w] for v, w in deleted.edges())
    assert graph.degree("u") == 7
    for colour in range(1, 6):
        layer = deleted.subgraph(v for v in graph if colours[v] in (0, colour))
        assert nx.has_path(layer, "x", "y")
        interior = layer.copy()
        interior.remove_node("u")
        assert nx.has_path(interior, "x", "y") == (colour >= 3)
        if colour >= 3:
            assert nx.has_path(interior, "x", f"r{colour}")


def verify_decomposition(graph: nx.Graph, decomposition: nx.Graph, width: int) -> None:
    assert nx.is_tree(decomposition)
    bags = list(decomposition)
    assert max(map(len, bags)) - 1 == width
    assert set().union(*bags) == set(graph)
    assert all(any(v in bag and w in bag for bag in bags) for v, w in graph.edges())
    for vertex in graph:
        containing = [bag for bag in bags if vertex in bag]
        assert nx.is_connected(decomposition.subgraph(containing))


def main() -> None:
    assert clique_minor(nx.complete_graph([str(i) for i in range(7)]), 7)
    assert clique_minor(nx.path_graph([str(i) for i in range(10)]), 7) is None
    for crossed in (False, True):
        for pinches in range(3):
            graph, colours = build(crossed, pinches)
            verify_trace(graph, colours)
            model = clique_minor(graph, 7)
            width, decomposition = nx.approximation.treewidth_min_fill_in(graph)
            verify_decomposition(graph, decomposition, width)
            print(f"crossed={crossed} pinches={pinches} n={len(graph)} "
                  f"k7={model is not None} treewidth_upper={width} "
                  f"connectivity={nx.node_connectivity(graph)}", flush=True)
            if model:
                print(f"  bags={model}", flush=True)
            elif width <= 5:
                print("  no K7: independently checked width-at-most-five decomposition", flush=True)
    print("PASS six selected-response quotient probes; no critical-host reduction claimed")


if __name__ == "__main__":
    main()
