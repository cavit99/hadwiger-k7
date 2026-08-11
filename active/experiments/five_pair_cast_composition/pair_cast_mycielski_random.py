#!/usr/bin/env python3
"""Random screen for a K5-free five-chromatic all-casts obstruction."""

from __future__ import annotations

import itertools
import random

import networkx as nx

from pair_cast_mycielski_search import (
    all_pair_paths,
    components_after,
    mask,
    rooted_internal_seven,
)


def clique_masks(graph: nx.Graph) -> tuple[int, ...]:
    answer = []
    for size in range(1, 5):
        for vertices in itertools.combinations(graph, size):
            if all(graph.has_edge(u, v) for u, v in itertools.combinations(vertices, 2)):
                answer.append(mask(list(vertices)))
    return tuple(answer)


def main() -> None:
    rng = random.Random(20260810)
    graph = nx.convert_node_labels_to_integers(nx.mycielskian(nx.complete_graph(4)))
    pair_paths = all_pair_paths(graph)
    component_cache = {
        path: tuple(components_after(graph, path))
        for path in set().union(*pair_paths.values())
    }
    cliques = clique_masks(graph)
    arbitrary = tuple(range(1, 1 << len(graph)))

    for trial in range(2_000_000):
        p_portal = rng.choice(arbitrary)
        q_portal = rng.choice(arbitrary)
        paths = {
            path
            for p in range(len(graph))
            if p_portal & (1 << p)
            for q in range(len(graph))
            if q_portal & (1 << q)
            for path in pair_paths[p, q]
        }
        components = {
            component for path in paths for component in component_cache[path]
        }
        roots = tuple(rng.choice(cliques) for _ in range(5))

        # Every four-root subset, hence every pair, must be feasible.
        if any(
            not any(all(component & roots[i] for i in retained) for component in components)
            for retained in itertools.combinations(range(5), 4)
        ):
            continue
        if any(all(component & root for root in roots) for component in components):
            continue
        portals = (p_portal, q_portal, *roots)
        if not rooted_internal_seven(graph, portals):
            continue

        print("FOUND", {"trial": trial, "p": p_portal, "q": q_portal, "roots": roots})
        return
    print("NONE", {"trials": 2_000_000})


if __name__ == "__main__":
    main()
