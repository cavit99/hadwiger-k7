#!/usr/bin/env python3
"""Exact small-order probe: all 3--2 carriers versus rooted K5-minus.

This is a falsification probe, not a proof.  It checks every graph in the
NetworkX atlas and every five-set of prescribed roots.
"""

from __future__ import annotations

import itertools

import networkx as nx


def connected(graph: nx.Graph, vertices: frozenset[int]) -> bool:
    return bool(vertices) and nx.is_connected(graph.subgraph(vertices))


def has_carriers(graph: nx.Graph, roots: tuple[int, ...]) -> bool:
    vertices = frozenset(graph)
    extras = tuple(vertices.difference(roots))
    for poles in itertools.combinations(roots, 2):
        pole_set = frozenset(poles)
        triple = frozenset(roots).difference(pole_set)
        feasible = False
        # Each extra vertex is unused, assigned to the triple carrier, or
        # assigned to the pole carrier.
        for assignment in itertools.product(range(3), repeat=len(extras)):
            left = triple.union(
                extra for extra, side in zip(extras, assignment, strict=True) if side == 1
            )
            right = pole_set.union(
                extra for extra, side in zip(extras, assignment, strict=True) if side == 2
            )
            if connected(graph, left) and connected(graph, right):
                feasible = True
                break
        if not feasible:
            return False
    return True


def has_rooted_k5minus(graph: nx.Graph, roots: tuple[int, ...]) -> bool:
    extras = tuple(set(graph).difference(roots))
    # Each extra vertex is unused or assigned to one of the five root bags.
    for assignment in itertools.product(range(6), repeat=len(extras)):
        bags = [set((root,)) for root in roots]
        for extra, target in zip(extras, assignment, strict=True):
            if target:
                bags[target - 1].add(extra)
        if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        missing = 0
        for left, right in itertools.combinations(bags, 2):
            if not any(graph.has_edge(u, v) for u in left for v in right):
                missing += 1
        if missing <= 1:
            return True
    return False


def has_rooted_k4(graph: nx.Graph, roots: tuple[int, ...]) -> bool:
    assert len(roots) == 4
    extras = tuple(set(graph).difference(roots))
    for assignment in itertools.product(range(5), repeat=len(extras)):
        bags = [set((root,)) for root in roots]
        for extra, target in zip(extras, assignment, strict=True):
            if target:
                bags[target - 1].add(extra)
        if not all(nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        if all(
            any(graph.has_edge(u, v) for u in left for v in right)
            for left, right in itertools.combinations(bags, 2)
        ):
            return True
    return False


def internally_five_connected(graph: nx.Graph, roots: tuple[int, ...]) -> bool:
    nonroots = tuple(set(graph).difference(roots))
    for size in range(1, len(nonroots) + 1):
        for subset in itertools.combinations(nonroots, size):
            shore = set(subset)
            neighbourhood = set().union(*(set(graph[vertex]) for vertex in shore)) - shore
            if len(neighbourhood) <= 4:
                return False
    return True


def main() -> None:
    tested = 0
    feasible = 0
    rooted_five_feasible = 0
    first_counterexample = None
    best_surrogate = None
    four_connected_instances = 0
    rooted_k4_without_near_k5 = 0
    first_rooted_k4_without_near_k5 = None
    best_rooted_k4_surrogate = None
    stable_rooted_k4_without_near_k5 = 0
    for graph in nx.graph_atlas_g():
        if graph.number_of_nodes() < 5 or not nx.is_connected(graph):
            continue
        for roots in itertools.combinations(tuple(graph), 5):
            tested += 1
            if nx.node_connectivity(graph) >= 4:
                four_connected_instances += 1
                if not has_rooted_k5minus(graph, roots):
                    print(
                        "FOUR_CONNECTED_COUNTEREXAMPLE",
                        nx.to_graph6_bytes(graph, header=False).decode().strip(),
                        roots,
                    )
                    return
            nonroots = set(graph).difference(roots)
            if (
                nonroots
                and internally_five_connected(graph, roots)
                and not has_rooted_k5minus(graph, roots)
            ):
                rooted_foursets = [
                    subset
                    for subset in itertools.combinations(roots, 4)
                    if has_rooted_k4(graph, subset)
                ]
                if rooted_foursets:
                    rooted_k4_without_near_k5 += 1
                    incident = sum(
                        1
                        for u, v in graph.edges()
                        if u in nonroots or v in nonroots
                    )
                    record = (
                        incident - 3 * len(nonroots),
                        nx.to_graph6_bytes(graph, header=False).decode().strip(),
                        roots,
                        rooted_foursets,
                    )
                    if first_rooted_k4_without_near_k5 is None:
                        first_rooted_k4_without_near_k5 = record
                    if best_rooted_k4_surrogate is None or record > best_rooted_k4_surrogate:
                        best_rooted_k4_surrogate = record
                    if graph.subgraph(roots).number_of_edges() == 0:
                        stable_rooted_k4_without_near_k5 += 1
                        print(
                            "STABLE_ROOTED_K4_WITHOUT_NEAR_K5",
                            nx.to_graph6_bytes(graph, header=False).decode().strip(),
                            roots,
                            rooted_foursets,
                        )
                        return
            if not has_carriers(graph, roots):
                continue
            feasible += 1
            if not has_rooted_k5minus(graph, roots):
                if first_counterexample is None:
                    first_counterexample = (
                        nx.to_graph6_bytes(graph, header=False).decode().strip(),
                        roots,
                    )
                if internally_five_connected(graph, roots):
                    incident = sum(
                        1
                        for u, v in graph.edges()
                        if u in nonroots or v in nonroots
                    )
                    surrogate = incident - 3 * len(nonroots)
                    record = (
                        surrogate,
                        nx.to_graph6_bytes(graph, header=False).decode().strip(),
                        roots,
                    )
                    if best_surrogate is None or record > best_surrogate:
                        best_surrogate = record
            if internally_five_connected(graph, roots):
                rooted_five_feasible += 1
    print(
        f"GREEN internally-five atlas; rooted instances={tested}, "
        f"carrier-feasible={feasible}, internally-five feasible={rooted_five_feasible}, "
        f"four-connected={four_connected_instances}, first-unrestricted={first_counterexample}, "
        f"rooted-k4-without-near-k5={rooted_k4_without_near_k5}, "
        f"stable-rooted-k4-without-near-k5={stable_rooted_k4_without_near_k5}, "
        f"first-rooted-k4={first_rooted_k4_without_near_k5}, "
        f"best-rooted-k4-surrogate={best_rooted_k4_surrogate}, "
        f"best-surrogate={best_surrogate}"
    )


if __name__ == "__main__":
    main()
