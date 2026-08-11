#!/usr/bin/env python3
"""Search a literal-K5-free five-chromatic shore for noncomposition.

The shore is the Mycielskian of K4.  Each of the five centre terminals is
first restricted to a singleton portal; p and q use three-vertex portals.
We test rooted internal seven-connectivity, all ten (2,2) casts, and failure
of the full (2,5) cast.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement

import networkx as nx


def mask(vertices: tuple[int, ...] | list[int]) -> int:
    value = 0
    for vertex in vertices:
        value |= 1 << vertex
    return value


def components_after(graph: nx.Graph, removed: int) -> list[int]:
    kept = [v for v in graph if not (removed & (1 << v))]
    return [mask(list(part)) for part in nx.connected_components(graph.subgraph(kept))]


def all_pair_paths(graph: nx.Graph) -> dict[tuple[int, int], tuple[int, ...]]:
    answer = {}
    for p in graph:
        for q in graph:
            if p == q:
                answer[p, q] = (1 << p,)
            else:
                answer[p, q] = tuple({mask(path) for path in nx.all_simple_paths(graph, p, q)})
    return answer


def path_masks(
    pair_paths: dict[tuple[int, int], tuple[int, ...]],
    p_portal: tuple[int, ...],
    q_portal: tuple[int, ...],
) -> tuple[int, ...]:
    paths: set[int] = set()
    for p in p_portal:
        for q in q_portal:
            paths.update(pair_paths[p, q])
    return tuple(sorted(paths, key=lambda value: (value.bit_count(), value)))


def rooted_internal_seven(graph: nx.Graph, portals: tuple[int, ...]) -> bool:
    vertices = tuple(graph)
    full = (1 << len(vertices)) - 1
    for inside in range(1, full + 1):
        boundary_inside = sum(bool(portal & inside) for portal in portals)
        graph_boundary = 0
        for v in vertices:
            if inside & (1 << v):
                continue
            if any(inside & (1 << u) for u in graph.neighbors(v)):
                graph_boundary += 1
        if graph_boundary + boundary_inside < 7:
            return False
    return True


def component_data(
    graph: nx.Graph,
    paths: tuple[int, ...],
    component_cache: dict[int, tuple[int, ...]],
    relation_cache: dict[int, int],
) -> tuple[int, tuple[int, ...]]:
    pair_relation = 0
    components: set[int] = set()
    for path in paths:
        for component in component_cache[path]:
            components.add(component)
            pair_relation |= relation_cache[component]
    maximal = tuple(
        component
        for component in components
        if not any(component != other and component & ~other == 0 for other in components)
    )
    return pair_relation, maximal


def pair_and_full_signatures(
    pair_relation: int, components: tuple[int, ...], roots: tuple[int, ...]
) -> tuple[set[tuple[int, int]], bool]:
    order = 9
    pairs = {
        (i, j)
        for i, j in combinations(range(5), 2)
        if pair_relation & (1 << (roots[i] * order + roots[j]))
    }
    root_support = mask(list(roots))
    full = any(root_support & ~component == 0 for component in components)
    return pairs, full


def main() -> None:
    graph = nx.convert_node_labels_to_integers(nx.mycielskian(nx.complete_graph(4)))
    pair_paths = all_pair_paths(graph)
    all_path_masks = set().union(*pair_paths.values())
    component_cache = {path: tuple(components_after(graph, path)) for path in all_path_masks}
    relation_cache = {}
    for component in {value for row in component_cache.values() for value in row}:
        relation = 0
        for u in range(len(graph)):
            if component & (1 << u):
                for v in range(len(graph)):
                    if component & (1 << v):
                        relation |= 1 << (u * len(graph) + v)
        relation_cache[component] = relation
    triples = tuple(combinations(tuple(graph), 3))
    root_multisets = tuple(combinations_with_replacement(tuple(graph), 5))
    all_pairs = set(combinations(range(5), 2))
    checked = 0
    for p_portal in triples:
        for q_portal in triples:
            paths = path_masks(pair_paths, p_portal, q_portal)
            pair_relation, components = component_data(
                graph, paths, component_cache, relation_cache
            )
            for roots in root_multisets:
                checked += 1
                pairs, full = pair_and_full_signatures(pair_relation, components, roots)
                if full or pairs != all_pairs:
                    continue
                portals = (mask(p_portal), mask(q_portal), *(1 << root for root in roots))
                if not rooted_internal_seven(graph, portals):
                    continue
                print("FOUND")
                print("edges", sorted(graph.edges()))
                print("p", p_portal, "q", q_portal, "roots", roots)
                print("path_masks", len(paths), "checked", checked)
                return
    print("NONE", checked)


if __name__ == "__main__":
    main()
