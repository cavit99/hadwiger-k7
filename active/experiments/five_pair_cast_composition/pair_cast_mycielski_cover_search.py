#!/usr/bin/env python3
"""Exact minimal-cover search for all-four-cast noncomposition on M(K4)."""

from __future__ import annotations

import itertools

import networkx as nx

from pair_cast_mycielski_search import (
    all_pair_paths,
    components_after,
    mask,
    path_masks,
    rooted_internal_seven,
)


def clique_masks(graph: nx.Graph) -> tuple[int, ...]:
    answer = []
    for size in range(1, 5):
        for vertices in itertools.combinations(graph, size):
            if all(graph.has_edge(u, v) for u, v in itertools.combinations(vertices, 2)):
                answer.append(mask(list(vertices)))
    return tuple(answer)


def minimal_cover_types(
    defect_types: tuple[int, ...], universe_order: int
) -> tuple[int, ...] | None:
    full = (1 << universe_order) - 1
    for private in itertools.combinations(range(universe_order), 5):
        private_mask = sum(1 << bit for bit in private)
        choices = [
            tuple(
                defect
                for defect in defect_types
                if defect & private_mask == 1 << bit
            )
            for bit in private
        ]
        if any(not row for row in choices):
            continue

        def choose(index: int, selected: tuple[int, ...], covered: int) -> tuple[int, ...] | None:
            if index == 5:
                return selected if covered == full else None
            possible_future = covered
            for row in choices[index:]:
                possible_future |= max(row, key=lambda value: value.bit_count())
            if possible_future != full:
                # This is only a cheap sufficient prune when one row happens
                # to contain every bit available from that position onward.
                possible_future = covered
                for row in choices[index:]:
                    for value in row:
                        possible_future |= value
                if possible_future != full:
                    return None
            for defect in choices[index]:
                answer = choose(index + 1, selected + (defect,), covered | defect)
                if answer is not None:
                    return answer
            return None

        answer = choose(0, (), 0)
        if answer is not None:
            return answer
    return None


def main() -> None:
    graph = nx.convert_node_labels_to_integers(nx.mycielskian(nx.complete_graph(4)))
    pair_paths = all_pair_paths(graph)
    component_cache = {
        path: tuple(components_after(graph, path))
        for path in set().union(*pair_paths.values())
    }
    cliques = clique_masks(graph)
    triples = tuple(itertools.combinations(tuple(graph), 3))
    checked = 0
    cover_rows = 0
    for p_portal in triples:
        for q_portal in triples:
            checked += 1
            paths = path_masks(pair_paths, p_portal, q_portal)
            components = {component for path in paths for component in component_cache[path]}
            maximal = tuple(
                component
                for component in components
                if not any(
                    component != other and component & ~other == 0
                    for other in components
                )
            )
            representatives: dict[int, list[int]] = {}
            for portal in cliques:
                defect = sum(
                    1 << index
                    for index, component in enumerate(maximal)
                    if not component & portal
                )
                if defect:
                    representatives.setdefault(defect, []).append(portal)
            defects = minimal_cover_types(tuple(representatives), len(maximal))
            if defects is None:
                continue
            cover_rows += 1
            for roots in itertools.product(*(representatives[defect] for defect in defects)):
                portals = (mask(list(p_portal)), mask(list(q_portal)), *roots)
                if rooted_internal_seven(graph, portals):
                    print(
                        "FOUND",
                        {
                            "p": p_portal,
                            "q": q_portal,
                            "roots": roots,
                            "maximal_components": maximal,
                            "checked": checked,
                            "cover_rows": cover_rows,
                        },
                    )
                    return
    print("NONE", {"checked": checked, "cover_rows": cover_rows})


if __name__ == "__main__":
    main()
