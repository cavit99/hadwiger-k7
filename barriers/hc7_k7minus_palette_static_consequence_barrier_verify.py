#!/usr/bin/env python3
"""Verify the target-rich palette-surjectivity static falsifiers.

Run with

    UV_CACHE_DIR=/tmp/uv-cache uv run python \
      barriers/hc7_k7minus_palette_static_consequence_barrier_verify.py
"""

from __future__ import annotations

from collections import Counter

import networkx as nx


PARTS = tuple((2 * index, 2 * index + 1) for index in range(5))
CORE = tuple(range(10))
TERMINALS = tuple(range(10, 17))
POLE = 17


def build_graph(assignments: tuple[int, ...]) -> nx.Graph:
    assert len(assignments) == len(TERMINALS)
    assert set(assignments) == set(range(5))
    graph = nx.Graph()
    graph.add_nodes_from(range(18))

    for left_index in range(5):
        for right_index in range(left_index + 1, 5):
            graph.add_edges_from(
                (left, right)
                for left in PARTS[left_index]
                for right in PARTS[right_index]
            )

    for terminal, assigned_part in zip(TERMINALS, assignments, strict=True):
        missed = set(PARTS[assigned_part])
        graph.add_edges_from(
            (terminal, core_vertex)
            for core_vertex in CORE
            if core_vertex not in missed
        )

    graph.add_edges_from((POLE, vertex) for vertex in range(17))
    return graph


def proper_six_colourings(graph: nx.Graph):
    """Enumerate all labelled proper colourings with colours 0,...,5."""

    order = (POLE,) + tuple(part[0] for part in PARTS) + tuple(
        part[1] for part in PARTS
    ) + TERMINALS
    colours = [-1] * len(graph)

    def search(position: int):
        if position == len(order):
            yield tuple(colours)
            return
        vertex = order[position]
        forbidden = {
            colours[neighbour]
            for neighbour in graph[vertex]
            if colours[neighbour] >= 0
        }
        for colour in range(6):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            yield from search(position + 1)
        colours[vertex] = -1

    yield from search(0)


def verify(assignments: tuple[int, ...], expected_profile: tuple[int, ...]) -> int:
    graph = build_graph(assignments)
    assert len(graph) == 18
    assert graph.number_of_edges() == 113
    assert graph.number_of_edges() >= 4 * len(graph)
    assert nx.node_connectivity(graph) == 9
    assert graph.subgraph(TERMINALS).number_of_edges() == 0
    assert set(graph[POLE]) == set(range(17))

    explicit_colouring = {POLE: 5}
    for part_index, part in enumerate(PARTS):
        explicit_colouring.update({vertex: part_index for vertex in part})
    explicit_colouring.update(
        {
            terminal: assigned_part
            for terminal, assigned_part in zip(
                TERMINALS, assignments, strict=True
            )
        }
    )
    assert all(
        explicit_colouring[left] != explicit_colouring[right]
        for left, right in graph.edges()
    )

    clique_six = (POLE,) + tuple(part[0] for part in PARTS)
    assert graph.subgraph(clique_six).number_of_edges() == 15

    target_vertices = clique_six + (TERMINALS[0],)
    target = graph.subgraph(target_vertices)
    assert target.number_of_edges() == 20
    assert not graph.has_edge(TERMINALS[0], PARTS[assignments[0]][0])

    colouring_count = 0
    for colouring in proper_six_colourings(graph):
        colouring_count += 1
        pole_colour = colouring[POLE]
        terminal_colours = [colouring[vertex] for vertex in TERMINALS]
        assert set(terminal_colours) == set(range(6)) - {pole_colour}
        assert tuple(sorted(Counter(terminal_colours).values(), reverse=True)) == (
            expected_profile
        )
        for terminal, assigned_part in zip(
            TERMINALS, assignments, strict=True
        ):
            assert colouring[terminal] == colouring[PARTS[assigned_part][0]]

    assert colouring_count == 720
    return colouring_count


def main() -> None:
    profiles = (
        ((0, 0, 0, 1, 2, 3, 4), (3, 1, 1, 1, 1)),
        ((0, 0, 1, 1, 2, 3, 4), (2, 2, 1, 1, 1)),
    )
    for assignments, profile in profiles:
        count = verify(assignments, profile)
        print(f"profile={profile} proper_six_colourings={count}")
    print("GREEN target-rich palette static-consequence falsifiers")


if __name__ == "__main__":
    main()
