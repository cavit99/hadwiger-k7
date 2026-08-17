#!/usr/bin/env python3
"""Verify the six-connected degree-eight low-codegree finite lemma.

Run with

    UV_CACHE_DIR=/tmp/uv-cache uv run python \
      results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py

Every graph on eight vertices occurs among the extensions of the 1,044
unlabelled order-seven graphs in NetworkX's graph atlas.  We retain one
representative of every isomorphism class with minimum degree at least four,
discard those having a K_6^- minor, and test every augmentation by

* a centre complete to the eight-vertex graph; and
* a nonadjacent exterior vertex with at least six neighbours there.

Minor testing is exact: starting from singleton bags, it recursively deletes
bags or merges touching bags until six or seven bags remain.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations

import networkx as nx


def adjacency_tuple(graph: nx.Graph) -> tuple[int, ...]:
    order = len(graph)
    assert set(graph) == set(range(order))
    return tuple(sum(1 << y for y in graph[x]) for x in range(order))


def touching(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    return any(
        adjacency[x] & right
        for x in range(len(adjacency))
        if left & (1 << x)
    )


def connected(adjacency: tuple[int, ...], bag: int) -> bool:
    reached = bag & -bag
    while reached:
        expanded = reached
        for x in range(len(adjacency)):
            if reached & (1 << x):
                expanded |= adjacency[x] & bag
        if expanded == reached:
            return reached == bag
        reached = expanded
    return False


def verify_model(
    adjacency: tuple[int, ...], bags: tuple[int, ...], target_order: int
) -> None:
    assert len(bags) == target_order
    assert all(bag and connected(adjacency, bag) for bag in bags)
    assert all(left & right == 0 for left, right in combinations(bags, 2))
    misses = sum(
        not touching(adjacency, left, right)
        for left, right in combinations(bags, 2)
    )
    assert misses <= 1


def near_clique_minor_model(
    adjacency: tuple[int, ...], target_order: int
) -> tuple[int, ...] | None:
    """Return a K_target^- model, or ``None`` if none exists."""

    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> tuple[int, ...] | None:
        if len(bags) == target_order:
            misses = sum(
                not touching(adjacency, left, right)
                for left, right in combinations(bags, 2)
            )
            return bags if misses <= 1 else None

        for left_index, right_index in combinations(range(len(bags)), 2):
            if not touching(adjacency, bags[left_index], bags[right_index]):
                continue
            merged = [
                bag
                for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            answer = search(tuple(sorted(merged)))
            if answer is not None:
                return answer

        for deleted_index in range(len(bags)):
            answer = search(bags[:deleted_index] + bags[deleted_index + 1 :])
            if answer is not None:
                return answer
        return None

    initial = tuple(1 << vertex for vertex in range(len(adjacency)))
    answer = search(initial)
    if answer is not None:
        verify_model(adjacency, answer, target_order)
    return answer


def extensions_of_atlas_graph(base: nx.Graph):
    for neighbours in range(1 << 7):
        graph = nx.Graph()
        graph.add_nodes_from(range(8))
        graph.add_edges_from(base.edges())
        graph.add_edges_from(
            (vertex, 7) for vertex in range(7) if neighbours & (1 << vertex)
        )
        yield graph


def invariant(graph: nx.Graph) -> tuple[tuple[int, ...], str]:
    return (
        tuple(sorted(dict(graph.degree()).values())),
        nx.weisfeiler_lehman_graph_hash(graph),
    )


def isomorphism_representatives(graphs) -> list[nx.Graph]:
    buckets: dict[tuple[tuple[int, ...], str], list[nx.Graph]] = defaultdict(list)
    representatives: list[nx.Graph] = []
    for graph in graphs:
        key = invariant(graph)
        if any(nx.is_isomorphic(graph, other) for other in buckets[key]):
            continue
        copy = graph.copy()
        buckets[key].append(copy)
        representatives.append(copy)
    return representatives


def augmented_graph(graph: nx.Graph, missed: tuple[int, ...]) -> nx.Graph:
    """Add centre 8 complete to J and exterior 9 missing ``missed``."""

    answer = graph.copy()
    answer.add_nodes_from((8, 9))
    answer.add_edges_from((8, vertex) for vertex in range(8))
    answer.add_edges_from(
        (9, vertex) for vertex in range(8) if vertex not in missed
    )
    return answer


def graph_code(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode().strip()


def model_text(bags: tuple[int, ...]) -> str:
    return "/".join(
        ".".join(str(vertex) for vertex in range(16) if bag & (1 << vertex))
        for bag in bags
    )


def calibrate_minor_engine() -> None:
    positive_seven = nx.complete_graph(7)
    positive_seven.remove_edge(0, 1)
    assert near_clique_minor_model(adjacency_tuple(positive_seven), 7)
    assert near_clique_minor_model(adjacency_tuple(nx.complete_graph(6)), 7) is None

    positive_six = nx.complete_graph(6)
    positive_six.remove_edge(0, 1)
    assert near_clique_minor_model(adjacency_tuple(positive_six), 6)
    assert near_clique_minor_model(adjacency_tuple(nx.cycle_graph(8)), 6) is None


def main() -> None:
    calibrate_minor_engine()

    bases = [graph for graph in nx.graph_atlas_g() if len(graph) == 7]
    assert len(bases) == 1_044

    raw_minimum_four = [
        graph
        for base in bases
        for graph in extensions_of_atlas_graph(base)
        if min(dict(graph.degree()).values()) >= 4
    ]
    assert len(raw_minimum_four) == 4_443

    representatives = isomorphism_representatives(raw_minimum_four)
    assert len(representatives) == 424

    local_survivors = [
        graph
        for graph in representatives
        if near_clique_minor_model(adjacency_tuple(graph), 6) is None
    ]
    assert len(local_survivors) == 55

    certificate_lines: list[str] = []
    negative_profiles: list[tuple[str, tuple[int, ...], tuple[int, ...]]] = []
    profile_count = 0
    for graph in local_survivors:
        code = graph_code(graph)
        adjacency = adjacency_tuple(graph)
        degrees = tuple(graph.degree(vertex) for vertex in range(8))
        for miss_order in range(3):
            for missed in combinations(range(8), miss_order):
                profile_count += 1
                quotient = augmented_graph(graph, missed)
                model = near_clique_minor_model(adjacency_tuple(quotient), 7)
                if model is None:
                    negative_profiles.append((code, missed, degrees))
                else:
                    certificate_lines.append(
                        f"{code} {','.join(map(str, missed)) or '-'} {model_text(model)}"
                    )

        # The local graph itself remains target-compatible by construction.
        assert near_clique_minor_model(adjacency, 6) is None

    assert profile_count == 55 * (1 + 8 + 28) == 2_035
    assert len(certificate_lines) == 2_031
    assert negative_profiles == [
        ("GLNM^_", (5, 6), (4, 4, 4, 4, 4, 4, 4, 4)),
        ("Gfwhmk", (0, 1), (4, 4, 4, 5, 4, 4, 4, 5)),
        ("Gfwhm{", (0, 1), (4, 4, 4, 5, 5, 4, 4, 6)),
        ("GxNg~k", (0, 1), (4, 4, 6, 4, 4, 6, 4, 6)),
    ]

    # In every negative profile the missed pair is an edge, is unique for
    # that labelled graph, and both its ends have local degree four.
    for code, missed, degrees in negative_profiles:
        graph = nx.from_graph6_bytes(code.encode())
        graph = nx.convert_node_labels_to_integers(graph, ordering="sorted")
        assert graph.has_edge(*missed)
        assert all(degrees[vertex] == 4 for vertex in missed)
        alternatives = []
        for other in combinations(range(8), 2):
            quotient = augmented_graph(graph, other)
            if near_clique_minor_model(adjacency_tuple(quotient), 7) is None:
                alternatives.append(other)
        assert alternatives == [missed]

    digest = sha256("\n".join(sorted(certificate_lines)).encode()).hexdigest()
    print("GREEN six-connected degree-eight low-codegree finite lemma")
    print(f"atlas_order_seven={len(bases)}")
    print(f"minimum_degree_four_extensions={len(raw_minimum_four)}")
    print(f"minimum_degree_four_isomorphism_classes={len(representatives)}")
    print(f"K6minus_free_local_classes={len(local_survivors)}")
    print(f"augmentation_profiles={profile_count}")
    print(f"positive_K7minus_certificates={len(certificate_lines)}")
    print("negative_profiles=" + repr(negative_profiles))
    print(f"certificate_digest={digest}")


if __name__ == "__main__":
    main()
