#!/usr/bin/env python3
"""Classify representative choices in exceptional order-eight neighbourhoods.

This is a bounded diagnostic.  It enumerates all unlabelled eight-vertex
graphs ``L`` with no ``K_4`` and ``alpha(L)=3``.  For every vertex ``x`` it
tests exactly whether ``L-x`` contains a ``K_5^-`` minor, and for every
independent triple ``I`` records which such vertices remain in ``L-I``.

The script does not infer a host-level theorem from the finite catalogue.
Its intended use is to test the representative-selection step in the
five-crossing omitted-coordinate theorem.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")

import argparse
from functools import lru_cache
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


def edge_count(graph: tuple[int, ...]) -> int:
    return sum(row.bit_count() for row in graph) // 2


def independent(graph: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(
        not adjacent(graph, left, right)
        for left, right in itertools.combinations(vertices, 2)
    )


def is_k4_free(graph: tuple[int, ...]) -> bool:
    return not any(
        all(
            adjacent(graph, left, right)
            for left, right in itertools.combinations(vertices, 2)
        )
        for vertices in itertools.combinations(range(len(graph)), 4)
    )


def independence_number(graph: tuple[int, ...]) -> int:
    for size in range(len(graph), 0, -1):
        if any(
            independent(graph, vertices)
            for vertices in itertools.combinations(range(len(graph)), size)
        ):
            return size
    return 0


def delete_vertex(graph: tuple[int, ...], deleted: int) -> tuple[int, ...]:
    keep = [vertex for vertex in range(len(graph)) if vertex != deleted]
    answer = [0] * len(keep)
    for first_index, first in enumerate(keep):
        for second_index in range(first_index + 1, len(keep)):
            second = keep[second_index]
            if adjacent(graph, first, second):
                answer[first_index] |= 1 << second_index
                answer[second_index] |= 1 << first_index
    return tuple(answer)


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
def has_k5_minus_minor(graph: tuple[int, ...]) -> bool:
    """Exact deletion/contraction test for a ``K_5^-`` minor."""

    if len(graph) < 5:
        return False
    if len(graph) == 5:
        return edge_count(graph) >= 9
    if any(
        has_k5_minus_minor(delete_vertex(graph, vertex))
        for vertex in range(len(graph))
    ):
        return True
    return any(
        adjacent(graph, left, right)
        and has_k5_minus_minor(contract_edge(graph, left, right))
        for left, right in itertools.combinations(range(len(graph)), 2)
    )


def connected_mask(graph: tuple[int, ...], vertices: int) -> bool:
    reached = vertices & -vertices
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= graph[bit.bit_length() - 1] & vertices
        if expanded == reached:
            return reached == vertices
        reached = expanded


def partitions_into_five(vertices: tuple[int, ...]) -> list[tuple[int, ...]]:
    answer: list[tuple[int, ...]] = []

    def extend(index: int, blocks: list[int]) -> None:
        if index == len(vertices):
            if len(blocks) == 5:
                answer.append(tuple(blocks))
            return
        remaining = len(vertices) - index
        if len(blocks) > 5 or len(blocks) + remaining < 5:
            return
        bit = 1 << vertices[index]
        for block_index in range(len(blocks)):
            blocks[block_index] |= bit
            extend(index + 1, blocks)
            blocks[block_index] ^= bit
        if len(blocks) < 5:
            blocks.append(bit)
            extend(index + 1, blocks)
            blocks.pop()

    extend(0, [])
    return answer


MODEL_PARTITIONS = tuple(
    partition
    for size in range(5, 8)
    for vertices in itertools.combinations(range(7), size)
    for partition in partitions_into_five(vertices)
)
assert len(MODEL_PARTITIONS) == 266


@lru_cache(maxsize=None)
def has_k5_minus_branch_model(graph: tuple[int, ...]) -> bool:
    """Independent branch-set enumeration for seven-vertex inputs."""

    assert len(graph) == 7
    for partition in MODEL_PARTITIONS:
        if not all(connected_mask(graph, block) for block in partition):
            continue
        missing = 0
        for left, right in itertools.combinations(partition, 2):
            left_neighbours = 0
            todo = left
            while todo:
                bit = todo & -todo
                todo ^= bit
                left_neighbours |= graph[bit.bit_length() - 1]
            if not left_neighbours & right:
                missing += 1
                if missing > 1:
                    break
        if missing <= 1:
            return True
    return False


def degree_sequence(graph: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted((row.bit_count() for row in graph), reverse=True))


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
    if not connected_after_deleting(graph, 0):
        return 0
    for order in range(1, len(graph) - 1):
        for vertices in itertools.combinations(range(len(graph)), order):
            deleted = sum(1 << vertex for vertex in vertices)
            if not connected_after_deleting(graph, deleted):
                return order
    return len(graph) - 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="print histograms and representative graph6 records",
    )
    args = parser.parse_args()

    lines = subprocess.check_output(("geng", "-q", "8"), text=True).splitlines()
    assert len(lines) == 12_346

    eligible = 0
    good_count_histogram: dict[int, int] = {}
    best_triple_histogram: dict[int, int] = {}
    worst_triple_histogram: dict[int, int] = {}
    no_selectable_good: list[tuple[str, tuple[int, ...], int, int, int]] = []
    fewer_than_five_good: list[
        tuple[str, tuple[int, ...], int, int, int]
    ] = []
    no_good_by_edges: dict[int, int] = {}
    no_good_by_connectivity: dict[int, int] = {}
    no_good_by_minimum_degree: dict[int, int] = {}
    best_range_by_edges: dict[int, tuple[int, int]] = {}
    densest_no_good: list[tuple[str, tuple[int, ...], int, int, int]] = []
    three_connected_no_good: list[
        tuple[str, tuple[int, ...], int, int, int]
    ] = []

    for line in lines:
        graph = decode_graph6(line)
        if not is_k4_free(graph) or independence_number(graph) != 3:
            continue
        eligible += 1

        good = {
            vertex
            for vertex in range(ORDER)
            if has_k5_minus_minor(delete_vertex(graph, vertex))
        }
        branch_model_good = {
            vertex
            for vertex in range(ORDER)
            if has_k5_minus_branch_model(delete_vertex(graph, vertex))
        }
        assert good == branch_model_good
        triples = [
            triple
            for triple in itertools.combinations(range(ORDER), 3)
            if independent(graph, triple)
        ]
        assert triples
        remaining_good_counts = [len(good - set(triple)) for triple in triples]
        best = max(remaining_good_counts)
        worst = min(remaining_good_counts)
        edges = edge_count(graph)
        if edges not in best_range_by_edges:
            best_range_by_edges[edges] = (best, best)
        else:
            current_minimum, current_maximum = best_range_by_edges[edges]
            best_range_by_edges[edges] = (
                min(current_minimum, best),
                max(current_maximum, best),
            )

        good_count_histogram[len(good)] = good_count_histogram.get(len(good), 0) + 1
        best_triple_histogram[best] = best_triple_histogram.get(best, 0) + 1
        worst_triple_histogram[worst] = worst_triple_histogram.get(worst, 0) + 1

        record = (
            line.strip(),
            degree_sequence(graph),
            edge_count(graph),
            len(good),
            len(triples),
        )
        if best == 0:
            no_selectable_good.append(record)
            no_good_by_edges[record[2]] = no_good_by_edges.get(record[2], 0) + 1
            connectivity = vertex_connectivity(graph)
            no_good_by_connectivity[connectivity] = (
                no_good_by_connectivity.get(connectivity, 0) + 1
            )
            minimum_degree = min(row.bit_count() for row in graph)
            no_good_by_minimum_degree[minimum_degree] = (
                no_good_by_minimum_degree.get(minimum_degree, 0) + 1
            )
            if not densest_no_good or record[2] > densest_no_good[0][2]:
                densest_no_good = [record]
            elif record[2] == densest_no_good[0][2]:
                densest_no_good.append(record)
            if connectivity >= 3:
                three_connected_no_good.append(record)
        if best < 5:
            fewer_than_five_good.append(record)

    assert eligible == 2_076
    assert len(no_selectable_good) == 756
    assert len(fewer_than_five_good) == 1_836
    five_bad_vertices_possible = sum(
        count
        for good_count, count in good_count_histogram.items()
        if good_count <= 3
    )
    assert five_bad_vertices_possible == 1_484
    assert all(lower >= 1 for edges, (lower, _) in best_range_by_edges.items() if edges >= 16)
    assert all(lower == 5 for edges, (lower, _) in best_range_by_edges.items() if edges >= 19)
    assert any(record[0] == "GCrb`o" for record in three_connected_no_good)

    print(f"eligible_neighbourhoods={eligible}")
    print(f"no_selectable_good_vertex={len(no_selectable_good)}")
    print(f"best_triple_fewer_than_five_good={len(fewer_than_five_good)}")
    print("selectable_good_vertex_forced_at_edges=16")
    print("five_good_vertices_forced_at_edges=19")
    print("wagner_graph_obstruction=GCrb`o")

    if args.verbose:
        print(f"number_of_good_vertices={dict(sorted(good_count_histogram.items()))}")
        print(f"five_bad_vertices_possible={five_bad_vertices_possible}")
        print(f"best_triple_histogram={dict(sorted(best_triple_histogram.items()))}")
        print(f"worst_triple_histogram={dict(sorted(worst_triple_histogram.items()))}")
        print(f"no_selectable_good_by_edges={dict(sorted(no_good_by_edges.items()))}")
        print(f"best_choice_range_by_edges={dict(sorted(best_range_by_edges.items()))}")
        print(
            "no_selectable_good_by_connectivity="
            f"{dict(sorted(no_good_by_connectivity.items()))}"
        )
        print(
            "no_selectable_good_by_minimum_degree="
            f"{dict(sorted(no_good_by_minimum_degree.items()))}"
        )
        print(f"densest_no_selectable_good={densest_no_good[:20]}")
        print(f"first_3_connected_no_selectable_good={three_connected_no_good[:20]}")

    print("GREEN: representative-selection diagnostic verified")


if __name__ == "__main__":
    main()
