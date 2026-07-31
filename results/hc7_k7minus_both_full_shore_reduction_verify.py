#!/usr/bin/env python3
"""Verify the finite boundary census in the both-full exceptional case.

The script enumerates the complete unlabelled order-eight catalogue with
``geng``.  It verifies only finite boundary assertions; the lifts to the
unbounded host are proved in the adjacent theorem.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")

import hashlib
import itertools
import subprocess
from collections import Counter
from functools import lru_cache


ORDER = 8
ALL = (1 << ORDER) - 1
EXPECTED_STRONG_DIGEST = (
    "6e2633b0f4999a1d09fb98f38f7c268044cada0095be8e84aa4b8fe72d879ebe"
)
EXPECTED_HOST_DIGEST = (
    "bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0"
)
EXPECTED_HOST_CODES = {
    "GCOcaO": 8,
    "GCOcbO": 7,
    "GCOcbW": 7,
    "GCOe`W": 7,
    "GCOebW": 6,
    "GCQR@O": 8,
    "GCQQV?": 6,
}


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


def encode_graph6(adjacency: tuple[int, ...]) -> str:
    bits = [
        (adjacency[left] >> right) & 1
        for right in range(1, len(adjacency))
        for left in range(right)
    ]
    while len(bits) % 6:
        bits.append(0)
    values = [len(adjacency)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | bit
        values.append(value)
    return "".join(chr(value + 63) for value in values)


def adjacent(graph: tuple[int, ...], left: int, right: int) -> bool:
    return bool(graph[left] & (1 << right))


def independent(graph: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(
        not adjacent(graph, left, right)
        for left, right in itertools.combinations(vertices, 2)
    )


def clique(graph: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(
        adjacent(graph, left, right)
        for left, right in itertools.combinations(vertices, 2)
    )


def exceptional_boundary(graph: tuple[int, ...]) -> bool:
    return (
        not any(clique(graph, vertices) for vertices in itertools.combinations(range(ORDER), 4))
        and any(independent(graph, vertices) for vertices in itertools.combinations(range(ORDER), 3))
        and not any(independent(graph, vertices) for vertices in itertools.combinations(range(ORDER), 4))
    )


def induced(graph: tuple[int, ...], keep: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(keep)
    positions = {vertex: index for index, vertex in enumerate(keep)}
    for index, vertex in enumerate(keep):
        for other in keep:
            if adjacent(graph, vertex, other):
                answer[index] |= 1 << positions[other]
    return tuple(answer)


def delete_vertex(graph: tuple[int, ...], vertex: int) -> tuple[int, ...]:
    return induced(
        graph,
        tuple(index for index in range(len(graph)) if index != vertex),
    )


def contract_edge(
    graph: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(graph)) if vertex != right]
    answer = [0] * len(keep)
    for first_index, first in enumerate(keep):
        for second_index in range(first_index + 1, len(keep)):
            second = keep[second_index]
            edge = adjacent(graph, first, second)
            if first == left:
                edge |= adjacent(graph, right, second)
            if second == left:
                edge |= adjacent(graph, first, right)
            if edge:
                answer[first_index] |= 1 << second_index
                answer[second_index] |= 1 << first_index
    return tuple(answer)


@lru_cache(maxsize=None)
def has_k4minus_minor(graph: tuple[int, ...]) -> bool:
    """Exact deletion/contraction recursion, used only through order six."""
    order = len(graph)
    if order < 4:
        return False
    if order == 4:
        return sum(row.bit_count() for row in graph) // 2 >= 5
    if any(has_k4minus_minor(delete_vertex(graph, vertex)) for vertex in range(order)):
        return True
    return any(
        adjacent(graph, left, right)
        and has_k4minus_minor(contract_edge(graph, left, right))
        for left, right in itertools.combinations(range(order), 2)
    )


def diamond_deletion_property(graph: tuple[int, ...]) -> bool:
    return all(
        not has_k4minus_minor(
            induced(
                graph,
                tuple(vertex for vertex in range(ORDER) if vertex not in deleted),
            )
        )
        for deleted in itertools.combinations(range(ORDER), 2)
    )


def bipartite_after_deleting(graph: tuple[int, ...], deleted: int) -> bool:
    colours = [-1] * len(graph)
    for root in range(len(graph)):
        if (deleted >> root) & 1 or colours[root] >= 0:
            continue
        colours[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            neighbours = graph[vertex] & ~deleted
            while neighbours:
                bit = neighbours & -neighbours
                neighbours ^= bit
                other = bit.bit_length() - 1
                if colours[other] < 0:
                    colours[other] = colours[vertex] ^ 1
                    stack.append(other)
                elif colours[other] == colours[vertex]:
                    return False
    return True


def mask_is_clique(graph: tuple[int, ...], mask: int) -> bool:
    remainder = mask
    while remainder:
        bit = remainder & -remainder
        remainder ^= bit
        vertex = bit.bit_length() - 1
        if remainder & ~graph[vertex]:
            return False
    return True


def has_clique_odd_cycle_transversal(graph: tuple[int, ...]) -> bool:
    return any(
        mask_is_clique(graph, deleted)
        and bipartite_after_deleting(graph, deleted)
        for deleted in range(1 << ORDER)
    )


def reserve_data(
    graph: tuple[int, ...]
) -> tuple[int, tuple[tuple[int, ...], ...]]:
    records: list[tuple[int, tuple[int, ...]]] = []
    for independent_triple in itertools.combinations(range(ORDER), 3):
        if not independent(graph, independent_triple):
            continue
        reserve = tuple(
            vertex for vertex in range(ORDER) if vertex not in independent_triple
        )
        reserve_graph = induced(graph, reserve)
        edges = sum(row.bit_count() for row in reserve_graph) // 2
        records.append((10 - edges, reserve_graph))
    minimum = min(value for value, _ in records)
    minimizers = tuple(graph for value, graph in records if value == minimum)
    return minimum, minimizers


def connected(graph: tuple[int, ...]) -> bool:
    if not graph:
        return False
    reached = 1
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= graph[bit.bit_length() - 1]
        if expanded == reached:
            return reached == (1 << len(graph)) - 1
        reached = expanded


def reserve_shape(graph: tuple[int, ...]) -> str:
    edges = sum(row.bit_count() for row in graph) // 2
    degrees = sorted(row.bit_count() for row in graph)
    if edges == 4 and degrees == [1, 1, 2, 2, 2] and connected(graph):
        return "P5"
    if edges == 3 and degrees == [1, 1, 1, 1, 2]:
        component_orders: list[int] = []
        unseen = (1 << len(graph)) - 1
        while unseen:
            reached = unseen & -unseen
            while True:
                expanded = reached
                todo = reached
                while todo:
                    bit = todo & -todo
                    todo ^= bit
                    expanded |= graph[bit.bit_length() - 1]
                if expanded == reached:
                    break
                reached = expanded
            component_orders.append(reached.bit_count())
            unseen &= ~reached
        if sorted(component_orders) == [2, 3]:
            return "P3+K2"
    if edges == 2 and degrees == [0, 1, 1, 1, 1]:
        return "2K2+K1"
    return "other"


def digest(codes: list[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(codes)) + "\n").encode()).hexdigest()


def main() -> None:
    lines = subprocess.check_output(("geng", "-q", "8"), text=True).splitlines()
    assert len(lines) == 12_346

    exceptional: list[tuple[str, tuple[int, ...]]] = []
    for line in lines:
        graph = decode_graph6(line)
        assert encode_graph6(graph) == line
        if exceptional_boundary(graph):
            exceptional.append((line, graph))
    assert len(exceptional) == 2_076

    strong: list[tuple[str, tuple[int, ...], int, tuple[tuple[int, ...], ...]]] = []
    lambda_counts: Counter[int] = Counter()
    for code, graph in exceptional:
        if not diamond_deletion_property(graph):
            continue
        minimum, minimizers = reserve_data(graph)
        strong.append((code, graph, minimum, minimizers))
        lambda_counts[minimum] += 1

    strong_codes = [code for code, _, _, _ in strong]
    assert len(strong) == 15
    assert lambda_counts == Counter({5: 1, 6: 7, 7: 5, 8: 2})
    assert digest(strong_codes) == EXPECTED_STRONG_DIGEST

    host = [
        (code, graph, minimum, minimizers)
        for code, graph, minimum, minimizers in strong
        if not has_clique_odd_cycle_transversal(graph)
    ]
    assert len(host) == 7
    assert {code: minimum for code, _, minimum, _ in host} == EXPECTED_HOST_CODES
    assert digest([code for code, _, _, _ in host]) == EXPECTED_HOST_DIGEST

    shape_counts: Counter[str] = Counter()
    for _, graph, minimum, minimizers in host:
        expected = {6: "P5", 7: "P3+K2", 8: "2K2+K1"}[minimum]
        assert all(reserve_shape(graph) == expected for graph in minimizers)
        if minimum == 8:
            assert any(
                clique(graph, vertices)
                for vertices in itertools.combinations(range(ORDER), 3)
            )
        shape_counts[expected] += 1
    assert shape_counts == Counter({"P5": 2, "P3+K2": 3, "2K2+K1": 2})

    print("order-eight graphs=12346 exceptional-alpha3-K4-free=2076")
    print("diamond-deletion survivors=15 lambda=5:1,6:7,7:5,8:2")
    print(f"diamond-code sha256={EXPECTED_STRONG_DIGEST}")
    print("clique-OCT exclusions=8 critical-host survivors=7")
    print("critical-host codes=" + " ".join(sorted(EXPECTED_HOST_CODES)))
    print(f"critical-host-code sha256={EXPECTED_HOST_DIGEST}")
    print("minimum-reserve shapes P5=2 P3+K2=3 2K2+K1=2")
    print("PASS K7-minus both-full boundary reduction")


if __name__ == "__main__":
    main()
