#!/usr/bin/env python3
"""Verify the two finite inputs for the exact-defect regular elimination.

The order-eight enumeration is complete because every graph on eight
vertices is obtained by adjoining one vertex to one of the 1,044
unlabelled order-seven graphs in NetworkX's graph atlas.

For every eligible neighbourhood H, the first check adds a centre complete
to H and two pairwise anticomplete component images, each missing exactly
one vertex of H.  Equal and distinct misses are both tested.  Attachments
which miss no vertex are supergraphs of tested distinct-miss profiles.

The minor test is an exact deletion/contraction search over connected branch
sets.  It is used for K_7^- and K_5, with positive and negative controls.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, combinations_with_replacement

import networkx as nx


BOUNDARY_ORDER = 8


def atlas_graphs_of_order(order: int) -> list[nx.Graph]:
    return [graph for graph in nx.graph_atlas_g() if len(graph) == order]


def adjacency_from_extension(base: nx.Graph, neighbours: int) -> tuple[int, ...]:
    adjacency = [0] * BOUNDARY_ORDER
    for left, right in base.edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    for vertex in range(7):
        if neighbours & (1 << vertex):
            adjacency[vertex] |= 1 << 7
            adjacency[7] |= 1 << vertex
    return tuple(adjacency)


def is_clique(adjacency: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(adjacency[left] & (1 << right) for left, right in combinations(vertices, 2))


def is_independent(adjacency: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(not adjacency[left] & (1 << right) for left, right in combinations(vertices, 2))


def eligible(adjacency: tuple[int, ...], minimum_degree: int) -> bool:
    vertices = tuple(range(BOUNDARY_ORDER))
    return (
        min(row.bit_count() for row in adjacency) >= minimum_degree
        and not any(is_clique(adjacency, group) for group in combinations(vertices, 4))
        and any(is_independent(adjacency, group) for group in combinations(vertices, 3))
        and not any(is_independent(adjacency, group) for group in combinations(vertices, 4))
    )


def touches(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    while left:
        bit = left & -left
        left ^= bit
        if adjacency[bit.bit_length() - 1] & right:
            return True
    return False


def has_minor(
    adjacency: tuple[int, ...], *, branch_count: int, required_contacts: int
) -> bool:
    """Test for a minor with the stated order and number of bag contacts."""

    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> bool:
        if len(bags) == branch_count:
            contacts = sum(
                touches(adjacency, left, right)
                for left, right in combinations(bags, 2)
            )
            return contacts >= required_contacts

        touching_pairs: list[tuple[int, int, int]] = []
        for left_index, right_index in combinations(range(len(bags)), 2):
            left, right = bags[left_index], bags[right_index]
            if touches(adjacency, left, right):
                # Prefer merges involving the three added quotient vertices.
                outside_score = -int(bool(left & 0x700)) - int(bool(right & 0x700))
                touching_pairs.append((outside_score, left_index, right_index))
        touching_pairs.sort()

        for _, left_index, right_index in touching_pairs:
            merged = [
                bag
                for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            if search(tuple(sorted(merged))):
                return True

        for deleted_index in range(len(bags)):
            reduced = bags[:deleted_index] + bags[deleted_index + 1 :]
            if search(reduced):
                return True
        return False

    return search(tuple(1 << vertex for vertex in range(len(adjacency))))


def has_k7minus_minor(adjacency: tuple[int, ...]) -> bool:
    return has_minor(adjacency, branch_count=7, required_contacts=20)


def has_k5_minor(adjacency: tuple[int, ...]) -> bool:
    return has_minor(adjacency, branch_count=5, required_contacts=10)


def quotient(
    adjacency: tuple[int, ...], first_miss: int, second_miss: int
) -> tuple[int, ...]:
    answer = list(adjacency) + [0, 0, 0]
    centre, first_component, second_component = 8, 9, 10
    for vertex in range(BOUNDARY_ORDER):
        answer[centre] |= 1 << vertex
        answer[vertex] |= 1 << centre
        if vertex != first_miss:
            answer[first_component] |= 1 << vertex
            answer[vertex] |= 1 << first_component
        if vertex != second_miss:
            answer[second_component] |= 1 << vertex
            answer[vertex] |= 1 << second_component
    return tuple(answer)


def to_networkx(adjacency: tuple[int, ...]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(len(adjacency)))
    graph.add_edges_from(
        (left, right)
        for left, right in combinations(range(len(adjacency)), 2)
        if adjacency[left] & (1 << right)
    )
    return graph


def from_networkx(graph: nx.Graph) -> tuple[int, ...]:
    vertices = sorted(graph)
    assert vertices == list(range(len(vertices)))
    adjacency = [0] * len(vertices)
    for left, right in graph.edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    return tuple(adjacency)


def hexagonal_bipyramid() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(8))
    graph.add_edges_from((vertex, (vertex + 1) % 6) for vertex in range(6))
    graph.add_edges_from((pole, vertex) for pole in (6, 7) for vertex in range(6))
    return graph


def controls() -> None:
    target = nx.complete_graph(7)
    target.remove_edge(0, 1)
    assert has_k7minus_minor(from_networkx(target))

    two_holes = nx.complete_graph(7)
    two_holes.remove_edges_from(((0, 1), (2, 3)))
    assert not has_k7minus_minor(from_networkx(two_holes))

    assert has_k5_minor(from_networkx(nx.complete_graph(5)))
    assert not has_k5_minor(from_networkx(nx.complete_bipartite_graph(2, 3)))

    path_cycle_join = nx.disjoint_union(nx.path_graph(4), nx.cycle_graph(6))
    for path_vertex in range(4):
        for cycle_vertex in range(4, 10):
            path_cycle_join.add_edge(path_vertex, cycle_vertex)
    assert has_k7minus_minor(from_networkx(path_cycle_join))


def main() -> None:
    controls()
    bases = atlas_graphs_of_order(7)
    assert len(bases) == 1_044

    eligible_count = 0
    profile_count = 0
    k5_minor_free_count = 0
    hexagonal_count = 0
    reference = hexagonal_bipyramid()

    for base in bases:
        for neighbours in range(1 << 7):
            adjacency = adjacency_from_extension(base, neighbours)
            if not eligible(adjacency, minimum_degree=4):
                continue
            eligible_count += 1

            for first_miss, second_miss in combinations_with_replacement(range(8), 2):
                profile_count += 1
                assert has_k7minus_minor(
                    quotient(adjacency, first_miss, second_miss)
                )

            if not has_k5_minor(adjacency):
                k5_minor_free_count += 1
                assert nx.is_isomorphic(to_networkx(adjacency), reference)
                hexagonal_count += 1

    assert eligible_count == 352
    assert profile_count == 12_672
    assert k5_minor_free_count == 2
    assert hexagonal_count == 2

    # Exact obstruction to repeating the exterior argument when D=26:
    # this cubic eligible neighbourhood with two distinct misses survives.
    cubic = nx.from_graph6_bytes(b"GMs`KK")
    cubic_adjacency = from_networkx(cubic)
    assert eligible(cubic_adjacency, minimum_degree=3)
    assert all(row.bit_count() == 3 for row in cubic_adjacency)
    assert not has_k7minus_minor(quotient(cubic_adjacency, 3, 5))

    print(
        "GREEN defect25 regular elimination finite inputs: "
        f"bases={len(bases)} extensions={len(bases) * 128} "
        f"eligible={eligible_count} exact_miss_profiles={profile_count} "
        f"k5_minor_free={k5_minor_free_count} hexagonal={hexagonal_count}; "
        "D26_static_survivor=GMs`KK misses=3,5"
    )


if __name__ == "__main__":
    main()
