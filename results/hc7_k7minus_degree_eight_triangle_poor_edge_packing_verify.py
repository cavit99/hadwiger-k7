#!/usr/bin/env python3
"""Independent finite cross-check for the exceptional-neighbourhood lemmas.

Run with

    UV_CACHE_DIR=/tmp/uv-cache uv run python \
      results/hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py

Every graph of order eight occurs among the extensions of the 1,044
unlabelled order-seven graphs in NetworkX's graph atlas.  The script checks
the rooted deletion conclusion and the almost-full exterior augmentation for
every eligible isomorphism class.  Minor testing is exact: it recursively
deletes branch sets and merges adjacent branch sets until the target order is
reached.
"""

from __future__ import annotations

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
    """Return an exact ``K_target^-`` model, or ``None`` if none exists."""

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


def induced_adjacency(
    adjacency: tuple[int, ...], retained: tuple[int, ...]
) -> tuple[int, ...]:
    position = {old: new for new, old in enumerate(retained)}
    return tuple(
        sum(
            1 << position[y]
            for y in retained
            if adjacency[x] & (1 << y)
        )
        for x in retained
    )


def is_clique(graph: nx.Graph, vertices: tuple[int, ...]) -> bool:
    return all(graph.has_edge(left, right) for left, right in combinations(vertices, 2))


def is_independent(graph: nx.Graph, vertices: tuple[int, ...]) -> bool:
    return all(
        not graph.has_edge(left, right)
        for left, right in combinations(vertices, 2)
    )


def eligible(graph: nx.Graph, minimum_degree: int = 4) -> bool:
    vertices = tuple(graph)
    return (
        min(dict(graph.degree()).values()) >= minimum_degree
        and not any(is_clique(graph, group) for group in combinations(vertices, 4))
        and any(is_independent(graph, group) for group in combinations(vertices, 3))
        and not any(is_independent(graph, group) for group in combinations(vertices, 4))
    )


def extensions_of_atlas_graph(base: nx.Graph):
    for neighbours in range(1 << 7):
        graph = nx.Graph()
        graph.add_nodes_from(range(8))
        graph.add_edges_from(base.edges())
        graph.add_edges_from(
            (vertex, 7) for vertex in range(7) if neighbours & (1 << vertex)
        )
        yield graph


def isomorphism_representatives(graphs: list[nx.Graph]) -> list[nx.Graph]:
    representatives: list[nx.Graph] = []
    for graph in graphs:
        if not any(nx.is_isomorphic(graph, other) for other in representatives):
            representatives.append(graph)
    return representatives


def augmented_graph(graph: nx.Graph, miss: int | None) -> nx.Graph:
    """Add a centre 8 complete to J and an exterior vertex 9 missing ``miss``."""

    answer = graph.copy()
    answer.add_nodes_from((8, 9))
    answer.add_edges_from((8, vertex) for vertex in range(8))
    answer.add_edges_from(
        (9, vertex) for vertex in range(8) if vertex != miss
    )
    return answer


def model_text(bags: tuple[int, ...]) -> str:
    return "/".join(
        ".".join(str(vertex) for vertex in range(16) if bag & (1 << vertex))
        for bag in bags
    )


def calibrate_minor_engine() -> None:
    positive_seven = nx.complete_graph(7)
    positive_seven.remove_edge(0, 1)
    assert near_clique_minor_model(adjacency_tuple(positive_seven), 7) is not None
    assert near_clique_minor_model(adjacency_tuple(nx.complete_graph(6)), 7) is None

    positive_five = nx.complete_graph(5)
    positive_five.remove_edge(0, 1)
    assert near_clique_minor_model(adjacency_tuple(positive_five), 5) is not None
    assert near_clique_minor_model(adjacency_tuple(nx.cycle_graph(7)), 5) is None


def main() -> None:
    calibrate_minor_engine()

    bases = [graph for graph in nx.graph_atlas_g() if len(graph) == 7]
    assert len(bases) == 1_044
    eligible_extensions = [
        graph
        for base in bases
        for graph in extensions_of_atlas_graph(base)
        if eligible(graph)
    ]
    assert len(eligible_extensions) == 352

    representatives = isomorphism_representatives(eligible_extensions)
    assert len(representatives) == 42

    certificate_lines: list[str] = []
    rooted_checks = 0
    augmentation_checks = 0
    for graph in representatives:
        adjacency = adjacency_tuple(graph)
        code = nx.to_graph6_bytes(graph, header=False).decode().strip()
        good_models: dict[int, tuple[int, ...]] = {}
        for deleted in range(8):
            retained = tuple(vertex for vertex in range(8) if vertex != deleted)
            reduced = induced_adjacency(adjacency, retained)
            model = near_clique_minor_model(reduced, 5)
            rooted_checks += 1
            if model is not None:
                # Translate the certificate back to the original labels.
                translated = tuple(
                    sum(
                        1 << retained[new]
                        for new in range(7)
                        if bag & (1 << new)
                    )
                    for bag in model
                )
                verify_model(adjacency, translated, 5)
                good_models[deleted] = translated
                certificate_lines.append(
                    f"good {code} {deleted} {model_text(translated)}"
                )

        assert all(
            any(neighbour in good_models for neighbour in graph[vertex])
            for vertex in range(8)
        )

        for miss in (None, *range(8)):
            quotient = augmented_graph(graph, miss)
            model = near_clique_minor_model(adjacency_tuple(quotient), 7)
            assert model is not None
            augmentation_checks += 1
            certificate_lines.append(
                f"augment {code} {miss} {model_text(model)}"
            )

    # Sharp negative calibration: lowering minimum degree from four to three
    # makes even the full exterior augmentation false.
    cubic = nx.from_graph6_bytes(b"GMs`KK")
    cubic = nx.convert_node_labels_to_integers(cubic, ordering="sorted")
    assert eligible(cubic, minimum_degree=3)
    assert min(dict(cubic.degree()).values()) == 3
    negative = augmented_graph(cubic, None)
    assert near_clique_minor_model(adjacency_tuple(negative), 7) is None

    digest = sha256("\n".join(sorted(certificate_lines)).encode()).hexdigest()
    print("GREEN exceptional-neighbourhood finite cross-check")
    print(f"atlas_order_seven={len(bases)}")
    print(f"eligible_extension_representations={len(eligible_extensions)}")
    print(f"eligible_isomorphism_classes={len(representatives)}")
    print(f"rooted_deletion_checks={rooted_checks}")
    print(f"almost_full_augmentation_checks={augmentation_checks}")
    print("negative_calibration=GMs`KK full exterior augmentation is target-free")
    print(f"certificate_sha256={digest}")


if __name__ == "__main__":
    main()
