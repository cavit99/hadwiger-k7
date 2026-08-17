#!/usr/bin/env python3
"""Exact verifier for the gate--clique incidence-certificate barrier."""

from __future__ import annotations

import itertools


ROOTS = tuple(range(6))
GATES = tuple(range(6, 12))
CLIQUE = tuple(range(12, 18))
SECOND = tuple(range(18, 24))
SHORE = GATES + CLIQUE


def add_edge(adjacency: list[set[int]], left: int, right: int) -> None:
    adjacency[left].add(right)
    adjacency[right].add(left)


def host() -> list[set[int]]:
    adjacency = [set() for _ in range(24)]
    for index in range(6):
        add_edge(adjacency, ROOTS[index], GATES[index])
    for gate in GATES:
        for core in CLIQUE:
            add_edge(adjacency, gate, core)
    for left, right in itertools.combinations(CLIQUE, 2):
        add_edge(adjacency, left, right)
    for left, right in itertools.combinations(SECOND, 2):
        add_edge(adjacency, left, right)
    for root in ROOTS:
        for vertex in SECOND:
            add_edge(adjacency, root, vertex)
    return adjacency


def connected_set(vertices: set[int], adjacency: list[set[int]]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    frontier = list(reached)
    while frontier:
        at = frontier.pop()
        for neighbour in adjacency[at] & vertices - reached:
            reached.add(neighbour)
            frontier.append(neighbour)
    return reached == vertices


def check_six_connectivity(adjacency: list[set[int]]) -> None:
    universe = set(range(len(adjacency)))
    for order in range(6):
        for deleted_tuple in itertools.combinations(range(len(adjacency)), order):
            remaining = universe - set(deleted_tuple)
            assert connected_set(remaining, adjacency), deleted_tuple


def local_checks(adjacency: list[set[int]]) -> None:
    shore_set = set(SHORE)
    packets: list[set[int]] = []
    for code in range(1, 1 << len(SHORE)):
        subset = {SHORE[index] for index in range(len(SHORE)) if code >> index & 1}
        external = set().union(*(adjacency[vertex] for vertex in subset)) - subset
        assert len(external) >= 6, subset
        if connected_set(subset, adjacency) and set(ROOTS) <= external:
            packets.append(subset)
    assert packets
    assert all(left & right for left, right in itertools.combinations(packets, 2))
    assert all(set(GATES) <= packet for packet in packets)

    internal_edges = sum(len(adjacency[v] & shore_set) for v in SHORE) // 2
    boundary_edges = sum(len(adjacency[v] & set(ROOTS)) for v in SHORE)
    assert internal_edges == 51
    assert boundary_edges == 6
    assert internal_edges + boundary_edges - 4 * len(SHORE) == 9


def bags_touch(left: set[int], right: set[int], adjacency: list[set[int]]) -> bool:
    return any(adjacency[vertex] & right for vertex in left)


def no_incidence_only_model(adjacency: list[set[int]]) -> None:
    for omitted in ROOTS:
        roots = tuple(root for root in ROOTS if root != omitted)
        # -1 means that the rooted bag is a singleton.  Nonnegative entries
        # are distinct shore vertices appended to the corresponding root.
        choices = (-1,) + SHORE
        for assignment in itertools.product(choices, repeat=5):
            used = tuple(vertex for vertex in assignment if vertex >= 0)
            if len(set(used)) != len(used):
                continue
            bags: list[set[int]] = []
            legal = True
            for root, vertex in zip(roots, assignment, strict=True):
                bag = {root} if vertex < 0 else {root, vertex}
                if vertex >= 0 and root not in adjacency[vertex]:
                    legal = False
                    break
                bags.append(bag)
            if not legal:
                continue
            missing = sum(
                not bags_touch(bags[left], bags[right], adjacency)
                for left, right in itertools.combinations(range(5), 2)
            )
            assert missing > 1, (omitted, assignment)


def explicit_rooted_model(adjacency: list[set[int]]) -> None:
    bags = [
        {ROOTS[index], GATES[index], CLIQUE[index]}
        for index in range(5)
    ]
    assert all(connected_set(bag, adjacency) for bag in bags)
    assert all(
        bags_touch(bags[left], bags[right], adjacency)
        for left, right in itertools.combinations(range(5), 2)
    )


def main() -> None:
    adjacency = host()
    assert not any(adjacency[root] & set(ROOTS) for root in ROOTS)
    after_cut = set(range(24)) - set(ROOTS)
    assert connected_set(set(SHORE), adjacency)
    assert connected_set(set(SECOND), adjacency)
    assert not any(adjacency[v] & set(SECOND) for v in SHORE)
    assert after_cut == set(SHORE) | set(SECOND)
    local_checks(adjacency)
    no_incidence_only_model(adjacency)
    explicit_rooted_model(adjacency)
    check_six_connectivity(adjacency)
    print("GATE_CLIQUE_BARRIER_EXACT_GREEN")


if __name__ == "__main__":
    main()
