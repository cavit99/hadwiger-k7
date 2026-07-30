#!/usr/bin/env python3
"""Verify the finite order-eight classification and explicit K7-minus models.

This script proves only the bounded Lemma 1 and the displayed quotient
certificates.  The host-level lift is the written argument in the adjacent
theorem file.
"""

from __future__ import annotations

import itertools
import subprocess


ORDER = 8


def decode_graph6(line: str) -> tuple[int, ...]:
    text = line.strip()
    assert text and ord(text[0]) - 63 == ORDER
    bits: list[int] = []
    for character in text[1:]:
        value = ord(character) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * ORDER
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def adjacent(graph: tuple[int, ...], left: int, right: int) -> bool:
    return bool(graph[left] & (1 << right))


def is_independent(graph: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(not adjacent(graph, left, right) for left, right in itertools.combinations(vertices, 2))


def is_k4_free(graph: tuple[int, ...]) -> bool:
    return not any(
        all(adjacent(graph, left, right) for left, right in itertools.combinations(vertices, 2))
        for vertices in itertools.combinations(range(ORDER), 4)
    )


def alpha_at_most_two(graph: tuple[int, ...]) -> bool:
    return not any(is_independent(graph, vertices) for vertices in itertools.combinations(range(ORDER), 3))


def cycle_square_edges(ordering: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    edges: set[tuple[int, int]] = set()
    for position in range(ORDER):
        for jump in (1, 2):
            edges.add(tuple(sorted((ordering[position], ordering[(position + jump) % ORDER]))))
    return tuple(sorted(edges))


def contains_spanning_cycle_square(graph: tuple[int, ...]) -> bool:
    # Fix one cyclic position to remove rotations.
    for remainder in itertools.permutations(range(1, ORDER)):
        ordering = (0,) + remainder
        if all(adjacent(graph, left, right) for left, right in cycle_square_edges(ordering)):
            return True
    return False


def quotient(missed: int | None) -> tuple[int, ...]:
    u, component = 8, 9
    graph = [0] * 10
    for left, right in cycle_square_edges(tuple(range(ORDER))):
        graph[left] |= 1 << right
        graph[right] |= 1 << left
    for boundary in range(ORDER):
        graph[boundary] |= 1 << u
        graph[u] |= 1 << boundary
        if boundary != missed:
            graph[boundary] |= 1 << component
            graph[component] |= 1 << boundary
    return tuple(graph)


def connected(graph: tuple[int, ...], bag: frozenset[int]) -> bool:
    reached = {next(iter(bag))}
    while True:
        expanded = reached | {
            neighbour
            for vertex in reached
            for neighbour in bag
            if adjacent(graph, vertex, neighbour)
        }
        if expanded == reached:
            return reached == set(bag)
        reached = expanded


def bags_touch(graph: tuple[int, ...], left: frozenset[int], right: frozenset[int]) -> bool:
    return any(adjacent(graph, x, y) for x in left for y in right)


def rotated_certificate(missed: int) -> tuple[frozenset[int], ...]:
    def rotate(vertex: int) -> int:
        return (vertex + missed) % ORDER if vertex < ORDER else vertex

    base = ((0, 7, 2), (3,), (4,), (1, 8), (6,), (5,), (9,))
    return tuple(frozenset(rotate(vertex) for vertex in bag) for bag in base)


def verify_certificate(missed: int | None) -> None:
    graph = quotient(missed)
    certificate = rotated_certificate(0 if missed is None else missed)
    assert len(certificate) == 7
    assert all(certificate)
    assert all(not (left & right) for left, right in itertools.combinations(certificate, 2))
    assert all(connected(graph, bag) for bag in certificate)
    missing_pairs = sum(
        not bags_touch(graph, left, right)
        for left, right in itertools.combinations(certificate, 2)
    )
    assert missing_pairs <= 1


def main() -> None:
    lines = subprocess.check_output(("geng", "-q", "8"), text=True).splitlines()
    assert len(lines) == 12_346

    candidates = []
    for line in lines:
        graph = decode_graph6(line)
        if is_k4_free(graph) and alpha_at_most_two(graph):
            candidates.append(graph)

    assert len(candidates) == 3
    assert all(contains_spanning_cycle_square(graph) for graph in candidates)

    for missed in (None, *range(ORDER)):
        verify_certificate(missed)

    print("order-eight graphs=12346; K4-free alpha<=2=3; spanning C8^1,2=3")
    print("near-full exterior K7-minus certificates=9/9")


if __name__ == "__main__":
    main()
