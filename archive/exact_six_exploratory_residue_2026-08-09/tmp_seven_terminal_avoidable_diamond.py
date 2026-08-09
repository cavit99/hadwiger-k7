#!/usr/bin/env python3
"""Falsify the proposed three-avoidance rooted-diamond lemma.

This disposable screen checks the complete seven-terminal irreducible-kernel
catalogue.  It uses no non-standard Python dependency.
"""

from __future__ import annotations

from itertools import combinations, product
import subprocess


def parse_graph6(line: str) -> list[int]:
    data = [ord(char) - 63 for char in line.strip()]
    n = data[0]
    assert n <= 62
    bits = []
    for value in data[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * n
    position = 0
    for right in range(1, n):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return adjacency


def connected(mask: int, adjacency: list[int]) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def three_connected(adjacency: list[int]) -> bool:
    n = len(adjacency)
    if n < 4:
        return False
    full = (1 << n) - 1
    for count in range(3):
        for removed_vertices in combinations(range(n), count):
            removed = sum(1 << vertex for vertex in removed_vertices)
            if not connected(full ^ removed, adjacency):
                return False
    return True


def without_edge(adjacency: list[int], left: int, right: int) -> list[int]:
    result = adjacency.copy()
    result[left] &= ~(1 << right)
    result[right] &= ~(1 << left)
    return result


def edges(adjacency: list[int]):
    for left in range(len(adjacency)):
        for right in range(left + 1, len(adjacency)):
            if adjacency[left] & (1 << right):
                yield left, right


def minimal_order_seven_carriers() -> list[list[int]]:
    process = subprocess.Popen(
        ["geng", "-q", "-c", "-d3", "7"],
        stdout=subprocess.PIPE,
        text=True,
    )
    assert process.stdout is not None
    carriers = []
    for line in process.stdout:
        graph = parse_graph6(line)
        if not three_connected(graph):
            continue
        if any(three_connected(without_edge(graph, *edge)) for edge in edges(graph)):
            continue
        carriers.append(graph)
    assert process.wait() == 0
    return carriers


def graph_from_edges(n: int, edge_set) -> list[int]:
    adjacency = [0] * n
    for left, right in edge_set:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    return adjacency


def order_eight_templates() -> list[list[int]]:
    cycle = {(i, (i + 1) % 7) for i in range(7)}
    cycle = {tuple(sorted(edge)) for edge in cycle}
    templates = []

    templates.append(graph_from_edges(8, cycle | {(7, vertex) for vertex in range(7)}))

    mandatory = {1, 2, 4, 5, 6}
    for optional in (set(), {0}, {3}, {0, 3}):
        edge_set = cycle | {(0, 3)} | {(7, vertex) for vertex in mandatory | optional}
        templates.append(graph_from_edges(8, edge_set))

    mandatory = {2, 3, 5, 6}
    for optional_bits in range(8):
        optional = {
            vertex
            for bit, vertex in enumerate((0, 1, 4))
            if optional_bits & (1 << bit)
        }
        edge_set = cycle | {(0, 4), (1, 4)} | {
            (7, vertex) for vertex in mandatory | optional
        }
        templates.append(graph_from_edges(8, edge_set))

    assert len(templates) == 13
    assert all(three_connected(graph) for graph in templates)
    return templates


def rooted_diamond_model(
    adjacency: list[int], roots: tuple[int, ...], deleted: int
) -> tuple[int, ...] | None:
    assert len(roots) == 4 and deleted not in roots
    root_set = set(roots)
    extras = [
        vertex
        for vertex in range(len(adjacency))
        if vertex not in root_set and vertex != deleted
    ]
    for assignment in product(range(5), repeat=len(extras)):
        bags = [1 << root for root in roots]
        for vertex, owner in zip(extras, assignment):
            if owner < 4:
                bags[owner] |= 1 << vertex
        if not all(connected(bag, adjacency) for bag in bags):
            continue
        contacts = 0
        for left, right in combinations(range(4), 2):
            neighbourhood = 0
            mask = bags[left]
            while mask:
                bit = mask & -mask
                mask ^= bit
                neighbourhood |= adjacency[bit.bit_length() - 1]
            contacts += bool(neighbourhood & bags[right])
        if contacts >= 5:
            return tuple(bags)
    return None


def main() -> None:
    carriers = minimal_order_seven_carriers()
    templates = order_eight_templates()
    failures = []
    certificates = 0
    tests = 0
    for kind, graphs in (("order7", carriers), ("order8", templates)):
        for graph_index, graph in enumerate(graphs):
            terminals = tuple(range(7))
            for roots in combinations(terminals, 4):
                marked = tuple(vertex for vertex in terminals if vertex not in roots)
                tests += 1
                witnesses = []
                for deleted in marked:
                    model = rooted_diamond_model(graph, roots, deleted)
                    if model is not None:
                        witnesses.append((deleted, model))
                if not witnesses:
                    failures.append((kind, graph_index, roots, graph))
                else:
                    certificates += 1
    print(f"order7_carriers={len(carriers)}")
    print(f"order8_presentations={len(templates)}")
    print(f"root_assignments={tests}")
    print(f"assignments_with_avoidable_diamond={certificates}")
    print(f"failures={len(failures)}")
    for kind, graph_index, roots, graph in failures[:20]:
        print("FAIL", kind, graph_index, roots, tuple(graph))


if __name__ == "__main__":
    main()
