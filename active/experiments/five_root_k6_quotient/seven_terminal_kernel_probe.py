#!/usr/bin/env python3
"""Probe the seven-terminal three-connected kernel in the support-five case."""

from __future__ import annotations

import itertools
import os
import subprocess

import networkx as nx


def graphs(order: int) -> list[nx.Graph]:
    data = subprocess.check_output(["geng", "-q", str(order)], text=True)
    return [
        nx.from_graph6_bytes(line.encode())
        for line in data.splitlines()
        if line
    ]


def augmented(
    kernel: nx.Graph,
    a: int,
    w: int,
    extra: int | None,
    first: frozenset[int],
) -> nx.Graph:
    answer = nx.relabel_nodes(kernel, lambda v: f"m{v}")
    centres = set(kernel) - {a, w} - ({extra} if extra is not None else set())
    second = centres - set(first)
    names = ("b", "c", "s", "t")
    answer.add_nodes_from(names)
    answer.add_edges_from(
        [
            (f"m{a}", "b"),
            (f"m{a}", "c"),
            (f"m{a}", "s"),
            (f"m{a}", "t"),
            ("b", "c"),
            ("b", "t"),
            ("s", "c"),
            ("s", "t"),
        ]
    )
    for z in first:
        answer.add_edge(f"m{z}", "b")
        answer.add_edge(f"m{z}", "c")
    for z in second:
        answer.add_edge(f"m{z}", "s")
        answer.add_edge(f"m{z}", "t")
    return answer


def rooted_k7_minus_model(
    graph: nx.Graph, roots: tuple[str, ...]
) -> tuple[frozenset[str], ...] | bool:
    """Find seven near-clique bags, one rooted at each prescribed vertex."""
    root_set = set(roots)
    extras = tuple(set(graph) - root_set)
    for assignment in itertools.product(range(-1, 7), repeat=len(extras)):
        bags = [set([root]) for root in roots]
        for vertex, target in zip(extras, assignment, strict=True):
            if target >= 0:
                bags[target].add(vertex)
        if any(not nx.is_connected(graph.subgraph(bag)) for bag in bags):
            continue
        missing = 0
        for i, j in itertools.combinations(range(7), 2):
            if not any(
                graph.has_edge(u, v)
                for u in bags[i]
                for v in bags[j]
            ):
                missing += 1
                if missing > 1:
                    break
        if missing <= 1:
            return tuple(frozenset(bag) for bag in bags)
    return False


def unrooted_k7_minus_model(graph: nx.Graph) -> tuple[frozenset[str], ...] | bool:
    """Exact set-partition search for an unrooted near-seven-clique minor."""
    vertices = tuple(graph)
    order = len(vertices)
    index_of = {vertex: index for index, vertex in enumerate(vertices)}
    adjacency = [
        sum(1 << index_of[neighbor] for neighbor in graph.neighbors(vertex))
        for vertex in vertices
    ]
    connected = [False] * (1 << order)
    neighbourhood = [0] * (1 << order)
    for mask in range(1, 1 << order):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        neighbourhood[mask] = neighbourhood[mask ^ bit] | adjacency[vertex]
        reached = bit
        frontier = bit
        while frontier:
            edge = frontier & -frontier
            frontier ^= edge
            at = edge.bit_length() - 1
            new = adjacency[at] & mask & ~reached
            reached |= new
            frontier |= new
        connected[mask] = reached == mask

    bags: list[int] = []

    def visit(index: int) -> tuple[frozenset[str], ...] | bool:
        remaining = len(vertices) - index
        if len(bags) > 7 or len(bags) + remaining < 7:
            return False
        if index == len(vertices):
            if len(bags) != 7:
                return False
            if any(not connected[bag] for bag in bags):
                return False
            missing = 0
            for i, j in itertools.combinations(range(7), 2):
                if not neighbourhood[bags[i]] & bags[j]:
                    missing += 1
                    if missing > 1:
                        return False
            return tuple(
                frozenset(vertices[v] for v in range(order) if bag & (1 << v))
                for bag in bags
            )

        # Leaving a vertex unused is permitted in a minor model.
        answer = visit(index + 1)
        if answer:
            return answer
        bit = 1 << index
        for position in range(len(bags)):
            bags[position] |= bit
            answer = visit(index + 1)
            bags[position] ^= bit
            if answer:
                return answer
        if len(bags) < 7:
            bags.append(bit)
            answer = visit(index + 1)
            bags.pop()
            if answer:
                return answer
        return False

    return visit(0)


def main() -> None:
    tested = 0

    # Order seven: labels are fixed as three early centres, two late
    # centres, the common support vertex, and one vertex in Q.  It is
    # enough to test graphs minimal under deletion of a non-forced edge.
    vertices = tuple(range(7))
    first = frozenset((0, 1, 2))
    a, w = 5, 6
    centres = set(range(5))
    forced = frozenset((min(a, z), max(a, z)) for z in centres)
    optional = tuple(edge for edge in itertools.combinations(vertices, 2) if edge not in forced)
    minimal = []
    masks = () if os.environ.get("HC7_ORDER8_ONLY") else range(1 << len(optional))
    for mask in masks:
        kernel = nx.Graph()
        kernel.add_nodes_from(vertices)
        kernel.add_edges_from(forced)
        kernel.add_edges_from(edge for index, edge in enumerate(optional) if mask & (1 << index))
        if nx.node_connectivity(kernel) < 3:
            continue
        deletable = False
        for edge in optional:
            if not kernel.has_edge(*edge):
                continue
            reduced = kernel.copy()
            reduced.remove_edge(*edge)
            if nx.node_connectivity(reduced) >= 3:
                deletable = True
                break
        if deletable:
            continue
        minimal.append(kernel)
    print("ORDER7_MINIMAL", len(minimal))
    for index, kernel in enumerate(minimal):
        tested += 1
        graph = augmented(kernel, a, w, None, first)
        model = unrooted_k7_minus_model(graph)
        if not model:
            print(
                "SURVIVOR",
                {
                    "order": 7,
                    "graph_index": index,
                    "edges": sorted(kernel.edges()),
                    "tested": tested,
                },
            )
            return
    print("ORDER_GREEN", 7, tested)

    # With one nonterminal, Wu's theorem supplies at least four neighbours
    # of that vertex which have degree three.  This filter is a necessary
    # condition on the terminal-irreducible kernel.
    for index, kernel in enumerate(graphs(8)):
        if nx.node_connectivity(kernel) < 3:
            continue
        for extra in kernel:
            if any(
                nx.node_connectivity(
                    nx.contracted_edge(kernel, (extra, neighbour), self_loops=False)
                )
                >= 3
                for neighbour in kernel.neighbors(extra)
            ):
                continue
            if sum(kernel.degree(v) == 3 for v in kernel.neighbors(extra)) < 4:
                continue
            terminals = set(kernel) - {extra}
            for a in terminals:
                for w in terminals - {a}:
                    centres = terminals - {a, w}
                    if any(not kernel.has_edge(a, z) for z in centres):
                        continue
                    for first_tuple in itertools.combinations(sorted(centres), 3):
                        tested += 1
                        graph = augmented(kernel, a, w, extra, frozenset(first_tuple))
                        print(
                            "ORDER8_CASE",
                            index,
                            a,
                            w,
                            extra,
                            first_tuple,
                            flush=True,
                        )
                        model = unrooted_k7_minus_model(graph)
                        if not model:
                            print(
                                "SURVIVOR",
                                {
                                    "order": 8,
                                    "graph_index": index,
                                    "graph6": nx.to_graph6_bytes(kernel, header=False).decode().strip(),
                                    "edges": sorted(kernel.edges()),
                                    "a": a,
                                    "w": w,
                                    "extra": extra,
                                    "first": sorted(first_tuple),
                                    "tested": tested,
                                },
                            )
                            return
    print("ALL_GREEN", tested)


if __name__ == "__main__":
    main()
