#!/usr/bin/env python3
"""Verify the finite boundary census in the one-nonfull reduction.

Run from the repository root with nauty's ``geng`` on ``PATH``:

    python3 results/hc7_k7minus_nonfull_attachment_reduction_verify.py

The script enumerates all unlabelled graphs of order seven and checks only
the finite predicates in Theorem 3.  The lift from an actual separation in
the unbounded host graph is proved in the adjacent theorem.
"""

from __future__ import annotations

import hashlib
import itertools
import shutil
import subprocess
from collections import Counter
from functools import lru_cache


ORDER = 7
EXPECTED_CODES = {
    "FCOc_",
    "FCOe_",
    "FCOf_",
    "FCOeo",
    "FCOfo",
    "FCOfw",
    "FCQ`_",
    "FCQaO",
    "FCQe_",
    "FCQb_",
    "FCQeO",
    "FCQbO",
    "FCQfO",
    "FCQeo",
    "FCQbo",
    "FCQQO",
    "FCQUO",
    "FCQRO",
    "FCQVO",
    "FCR`o",
    "FCQrO",
    "FCQrW",
    "FCp`_",
    "FCpd_",
    "FCpb_",
    "FCXe_",
    "FCdb?",
    "FCdeG",
}
EXPECTED_DIGEST = "a045e1d21098d0789ea1c549ed00f380ab97df9120335ff24127f9c8a039eacd"


def decode_graph6(text: str) -> tuple[int, ...]:
    text = text.strip()
    assert text and ord(text[0]) - 63 == ORDER
    bits: list[int] = []
    for character in text[1:]:
        value = ord(character) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    graph = [0] * ORDER
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                graph[left] |= 1 << right
                graph[right] |= 1 << left
            position += 1
    return tuple(graph)


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


def alpha_three(graph: tuple[int, ...]) -> bool:
    vertices = range(len(graph))
    triples = itertools.combinations(vertices, 3)
    quadruples = itertools.combinations(vertices, 4)
    return any(independent(graph, choice) for choice in triples) and not any(
        independent(graph, choice) for choice in quadruples
    )


def induced(graph: tuple[int, ...], keep: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * len(keep)
    for left_index, left in enumerate(keep):
        for right_index in range(left_index + 1, len(keep)):
            right = keep[right_index]
            if adjacent(graph, left, right):
                answer[left_index] |= 1 << right_index
                answer[right_index] |= 1 << left_index
    return tuple(answer)


def delete_vertex(graph: tuple[int, ...], vertex: int) -> tuple[int, ...]:
    return induced(
        graph,
        tuple(index for index in range(len(graph)) if index != vertex),
    )


def contract_edge(graph: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
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
def has_minor(graph: tuple[int, ...], target: str) -> bool:
    """Test K5 or K4-minus by exact deletion/contraction recursion."""
    target_order = 5 if target == "K5" else 4
    target_edges = 10 if target == "K5" else 5
    if len(graph) < target_order:
        return False
    if len(graph) == target_order:
        return edge_count(graph) >= target_edges
    if any(
        has_minor(delete_vertex(graph, vertex), target)
        for vertex in range(len(graph))
    ):
        return True
    return any(
        adjacent(graph, left, right)
        and has_minor(contract_edge(graph, left, right), target)
        for left, right in itertools.combinations(range(len(graph)), 2)
    )


def edge_count(graph: tuple[int, ...]) -> int:
    return sum(row.bit_count() for row in graph) // 2


def connected_after_deleting(graph: tuple[int, ...], deleted: int) -> bool:
    remaining = ((1 << len(graph)) - 1) & ~deleted
    if remaining.bit_count() <= 1:
        return True
    reached = remaining & -remaining
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= graph[bit.bit_length() - 1] & remaining
        if expanded == reached:
            return reached == remaining
        reached = expanded


def vertex_connectivity(graph: tuple[int, ...]) -> int:
    order = len(graph)
    if not connected_after_deleting(graph, 0):
        return 0
    for size in range(1, order - 1):
        for deleted_vertices in itertools.combinations(range(order), size):
            deleted = sum(1 << vertex for vertex in deleted_vertices)
            if not connected_after_deleting(graph, deleted):
                return size
    return order - 1


def robust_independent_triple(graph: tuple[int, ...]) -> bool:
    vertices = range(len(graph))
    for triple in itertools.combinations(vertices, 3):
        if not independent(graph, triple):
            continue
        remainder = tuple(vertex for vertex in vertices if vertex not in triple)
        if any(clique(graph, choice) for choice in itertools.combinations(remainder, 3)):
            return True
    return False


def bipartite_after_deleting(graph: tuple[int, ...], deleted: int) -> bool:
    colours = [-1] * len(graph)
    for root in range(len(graph)):
        if deleted & (1 << root) or colours[root] >= 0:
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
        if remainder & ~graph[bit.bit_length() - 1]:
            return False
    return True


def minimum_clique_oct_order(graph: tuple[int, ...]) -> int | None:
    witnesses = [
        mask.bit_count()
        for mask in range(1 << len(graph))
        if mask_is_clique(graph, mask) and bipartite_after_deleting(graph, mask)
    ]
    return min(witnesses, default=None)


def k_colourable(graph: tuple[int, ...], colours: int) -> bool:
    order = sorted(range(len(graph)), key=lambda vertex: -graph[vertex].bit_count())
    assigned = [-1] * len(graph)

    def extend(position: int) -> bool:
        if position == len(order):
            return True
        vertex = order[position]
        forbidden = {
            assigned[other]
            for other in range(len(graph))
            if adjacent(graph, vertex, other) and assigned[other] >= 0
        }
        for colour in range(colours):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if extend(position + 1):
                return True
        assigned[vertex] = -1
        return False

    return extend(0)


def chromatic_number(graph: tuple[int, ...]) -> int:
    return next(colours for colours in range(1, len(graph) + 1) if k_colourable(graph, colours))


def digest(codes: set[str]) -> str:
    payload = "\n".join(sorted(codes)) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


def main() -> None:
    geng = shutil.which("geng")
    if geng is None:
        raise SystemExit("nauty's `geng` executable is required")
    lines = subprocess.check_output((geng, "-q", str(ORDER)), text=True).splitlines()
    assert len(lines) == 1_044
    assert len(set(lines)) == len(lines)

    stages: Counter[str] = Counter()
    survivors: dict[str, tuple[int, ...]] = {}
    for code in lines:
        graph = decode_graph6(code)
        stages["all"] += 1
        if not alpha_three(graph):
            continue
        stages["alpha3"] += 1
        if any(
            clique(graph, choice)
            for choice in itertools.combinations(range(ORDER), 4)
        ):
            continue
        stages["K4-free"] += 1
        if edge_count(graph) > 9:
            continue
        stages["sparse"] += 1
        if vertex_connectivity(graph) > 3:
            continue
        stages["connectivity"] += 1
        if has_minor(graph, "K5"):
            continue
        stages["K5-minor-free"] += 1
        if any(
            has_minor(delete_vertex(graph, vertex), "K4-")
            for vertex in range(ORDER)
        ):
            continue
        stages["diamond-deletion"] += 1
        if robust_independent_triple(graph):
            continue
        stages["residue"] += 1
        survivors[code] = graph

    assert stages == Counter(
        {
            "all": 1_044,
            "alpha3": 578,
            "K4-free": 353,
            "sparse": 103,
            "connectivity": 103,
            "K5-minor-free": 103,
            "diamond-deletion": 29,
            "residue": 28,
        }
    )
    assert set(survivors) == EXPECTED_CODES
    assert digest(set(survivors)) == EXPECTED_DIGEST

    edges = Counter(edge_count(graph) for graph in survivors.values())
    connectivity = Counter(vertex_connectivity(graph) for graph in survivors.values())
    triangles = Counter(
        sum(
            clique(graph, choice)
            for choice in itertools.combinations(range(ORDER), 3)
        )
        for graph in survivors.values()
    )
    chromatic = Counter(chromatic_number(graph) for graph in survivors.values())
    oct_order = Counter(minimum_clique_oct_order(graph) for graph in survivors.values())
    assert edges == Counter({5: 1, 6: 4, 7: 10, 8: 11, 9: 2})
    assert connectivity == Counter({0: 9, 1: 15, 2: 4})
    assert triangles == Counter({0: 5, 1: 12, 2: 9, 3: 2})
    assert chromatic == Counter({3: 28})
    assert oct_order == Counter({1: 21, 2: 4, None: 3})
    assert {
        code for code, graph in survivors.items() if vertex_connectivity(graph) == 2
    } == {"FCR`o", "FCp`_", "FCpd_", "FCpb_"}
    assert {
        code
        for code, graph in survivors.items()
        if minimum_clique_oct_order(graph) == 2
    } == {"FCQUO", "FCQVO", "FCQrW", "FCdeG"}
    assert {
        code
        for code, graph in survivors.items()
        if minimum_clique_oct_order(graph) is None
    } == {"FCQQO", "FCQRO", "FCQrO"}

    print("order-seven graphs=1044 alpha3=578 K4-free=353 sparse=103")
    print("diamond-deletion=29 one-nonfull-residue=28")
    print(f"residue sha256={EXPECTED_DIGEST}")
    print("edges 5:1 6:4 7:10 8:11 9:2; connectivity 0:9 1:15 2:4; chi3=28")
    print("clique-OCT vertex:21 edge:4 none:3")
    print("PASS K7-minus one-nonfull boundary census")


if __name__ == "__main__":
    main()
