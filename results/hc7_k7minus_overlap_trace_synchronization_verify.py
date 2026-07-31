#!/usr/bin/env python3
"""Verify the finite common-six census and the 3K2 trace barrier.

Run from the repository root with nauty's ``geng`` on ``PATH``:

    python3 results/hc7_k7minus_overlap_trace_synchronization_verify.py

The script checks only the bounded claims in Corollary 4 and in the
adjacent barrier.  The host-level trace and minor lifts are written proofs.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")

import hashlib
import itertools
import shutil
import subprocess
from collections import Counter
from functools import lru_cache


ORDER = 6
EXPECTED_CODES = {
    "ECO_", "ECQ_", "ECQO", "ECR_", "ECRO", "ECQo", "ECRo",
    "ECRW", "ECRw", "ECpO", "ECr_", "ECpo", "ECqg", "ECZ?",
    "ECX_", "ECYO", "ECZ_", "ECZO", "ECZG", "ECYW", "ECZo",
    "ECZW", "ECxo", "EEh_", "EEj_", "EEho", "EQhO", "EQjO",
}
EXPECTED_DIGEST = "9349e3f0c53068bdbdac7068c8fa347ac6658b5231c8abd3dc8e99804118bec9"


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


def edge_count(graph: tuple[int, ...]) -> int:
    return sum(row.bit_count() for row in graph) // 2


@lru_cache(maxsize=None)
def has_four_vertex_minor(graph: tuple[int, ...], target_edges: int) -> bool:
    """Test for K4 (six edges) or K4-minus (five edges)."""
    if len(graph) < 4:
        return False
    if len(graph) == 4:
        return edge_count(graph) >= target_edges
    if any(
        has_four_vertex_minor(delete_vertex(graph, vertex), target_edges)
        for vertex in range(len(graph))
    ):
        return True
    return any(
        adjacent(graph, left, right)
        and has_four_vertex_minor(
            contract_edge(graph, left, right), target_edges
        )
        for left, right in itertools.combinations(range(len(graph)), 2)
    )


def mask_is_clique(graph: tuple[int, ...], mask: int) -> bool:
    vertices = tuple(
        vertex for vertex in range(len(graph)) if mask & (1 << vertex)
    )
    return clique(graph, vertices)


def k_colourable(graph: tuple[int, ...], colours: int) -> bool:
    if not graph:
        return True
    if colours == 0:
        return False
    order = sorted(
        range(len(graph)), key=lambda vertex: -graph[vertex].bit_count()
    )
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


def minimum_reflection_demand(graph: tuple[int, ...]) -> int:
    best = len(graph)
    for mask in range(1 << len(graph)):
        if not mask_is_clique(graph, mask):
            continue
        remainder = induced(
            graph,
            tuple(
                vertex
                for vertex in range(len(graph))
                if not mask & (1 << vertex)
            ),
        )
        chromatic = next(
            colours
            for colours in range(len(remainder) + 1)
            if k_colourable(remainder, colours)
        )
        best = min(best, chromatic)
    return best


def connected(graph: tuple[int, ...]) -> bool:
    if not graph:
        return True
    seen = 1
    while True:
        expanded = seen
        todo = seen
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= graph[bit.bit_length() - 1]
        if expanded == seen:
            return seen == (1 << len(graph)) - 1
        seen = expanded


def is_net(graph: tuple[int, ...]) -> bool:
    return (
        connected(graph)
        and sorted(row.bit_count() for row in graph) == [1, 1, 1, 3, 3, 3]
        and sum(
            clique(graph, triple)
            for triple in itertools.combinations(range(ORDER), 3)
        ) == 1
    )


def is_two_triangles(graph: tuple[int, ...]) -> bool:
    triangles = [
        frozenset(triple)
        for triple in itertools.combinations(range(ORDER), 3)
        if clique(graph, triple)
    ]
    return (
        edge_count(graph) == 6
        and len(triangles) == 2
        and triangles[0].isdisjoint(triangles[1])
    )


def set_partitions(order: int) -> tuple[tuple[int, ...], ...]:
    answer: list[tuple[int, ...]] = []

    def extend(vertex: int, blocks: list[int]) -> None:
        if vertex == order:
            answer.append(tuple(blocks))
            return
        bit = 1 << vertex
        for index in range(len(blocks)):
            blocks[index] |= bit
            extend(vertex + 1, blocks)
            blocks[index] ^= bit
        blocks.append(bit)
        extend(vertex + 1, blocks)
        blocks.pop()

    extend(0, [])
    return tuple(answer)


def mask_is_independent(graph: tuple[int, ...], mask: int) -> bool:
    vertices = tuple(
        vertex for vertex in range(len(graph)) if mask & (1 << vertex)
    )
    return independent(graph, vertices)


def verify_matching_language_barrier() -> None:
    matching = [0] * ORDER
    for left, right in ((0, 1), (2, 3), (4, 5)):
        matching[left] |= 1 << right
        matching[right] |= 1 << left
    graph = tuple(matching)
    proper = [
        partition
        for partition in set_partitions(ORDER)
        if len(partition) <= 4
        and all(mask_is_independent(graph, block) for block in partition)
    ]
    assert proper
    assert all(len(partition) + 2 <= 6 for partition in proper)

    for mask in range(1, 1 << ORDER):
        if not mask_is_independent(graph, mask):
            continue
        parities = {
            len(partition) % 2
            for partition in proper
            if mask in partition
        }
        assert parities == {0, 1}

    # Add nonadjacent x,y, each complete to Z, and check the stated
    # independence and literal-clique properties of the eight-set.
    central = list(graph) + [0, 0]
    for root in (6, 7):
        for vertex in range(ORDER):
            central[root] |= 1 << vertex
            central[vertex] |= 1 << root
    central_graph = tuple(central)
    assert any(
        independent(central_graph, triple)
        for triple in itertools.combinations(range(8), 3)
    )
    assert not any(
        independent(central_graph, four)
        for four in itertools.combinations(range(8), 4)
    )
    assert not any(
        clique(central_graph, four)
        for four in itertools.combinations(range(8), 4)
    )


def digest(codes: set[str]) -> str:
    payload = "\n".join(sorted(codes)) + "\n"
    return hashlib.sha256(payload.encode()).hexdigest()


def main() -> None:
    geng = shutil.which("geng")
    if geng is None:
        raise SystemExit("nauty's `geng` executable is required")
    lines = subprocess.check_output((geng, "-q", str(ORDER)), text=True).splitlines()
    assert len(lines) == 156
    assert len(set(lines)) == len(lines)

    survivors: dict[str, tuple[int, ...]] = {}
    demands: Counter[int] = Counter()
    triangle_count = 0
    for code in lines:
        graph = decode_graph6(code)
        if any(
            independent(graph, choice)
            for choice in itertools.combinations(range(ORDER), 4)
        ):
            continue
        if has_four_vertex_minor(graph, 6):
            continue
        if any(
            has_four_vertex_minor(delete_vertex(graph, vertex), 5)
            for vertex in range(ORDER)
        ):
            continue
        survivors[code] = graph
        demand = minimum_reflection_demand(graph)
        demands[demand] += 1
        triangle_count += int(
            any(
                clique(graph, triple)
                for triple in itertools.combinations(range(ORDER), 3)
            )
        )

    assert set(survivors) == EXPECTED_CODES
    assert digest(set(survivors)) == EXPECTED_DIGEST
    assert demands == Counter({1: 1, 2: 26, 3: 1})
    assert triangle_count == 16
    assert is_net(survivors["ECqg"])
    assert is_two_triangles(survivors["EQhO"])
    assert all(
        minimum_reflection_demand(graph) == 2
        for graph in survivors.values()
        if not any(
            clique(graph, triple)
            for triple in itertools.combinations(range(ORDER), 3)
        )
    )

    verify_matching_language_barrier()

    print(f"common_six_survivors={len(survivors)} digest={EXPECTED_DIGEST}")
    print("reflection_demand_distribution=1:1,2:26,3:1")
    print("triangular=16 triangle_free=12")
    print("unique_demand_one=ECqg(net) unique_demand_three=EQhO(2K3)")
    print("matching_parity_languages=PASS")
    print("PASS overlap_trace_synchronization_finite_checks")


if __name__ == "__main__":
    main()
