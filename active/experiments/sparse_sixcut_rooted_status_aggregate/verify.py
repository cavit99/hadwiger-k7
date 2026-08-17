#!/usr/bin/env python3
"""Verify two exact obstructions to the rooted-status aggregate LP.

The graphs in this file are not target-free.  They show that the audited
four-root no-model inequalities, singleton-transfer bounds, incidence
bounds, density identity and packet orientation do not alone encode the
five-root terminal model which excludes them.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations

import networkx as nx


ROOTS = tuple(range(6))
FOUR_SETS = tuple(combinations(ROOTS, 4))

THIN_LABELS = (
    (0, 1, 2, 3),
    (0, 1, 4, 5),
    (2, 3, 4, 5),
)

MU_ONE_LABELS = (
    (0, 1, 5), (1, 3, 4), (1, 2, 4), (0, 3, 4), (1, 3, 4),
    (1, 3, 4), (1, 2, 3), (1, 2, 4), (0, 1, 2), (0, 1, 4),
    (0, 1, 4), (1, 2, 4), (2, 3, 4), (0, 1, 2), (0, 3, 4),
    (0, 2, 4), (0, 3, 4), (0, 2, 3), (0, 2, 4), (0, 1, 4),
)

MU_TWO_LABELS = (
    (0, 1, 5), (2, 3, 4), (0, 1, 4), (1, 2, 4), (1, 3, 4),
    (0, 2, 4), (0, 1, 4), (0, 1, 4), (0, 2, 4), (0, 1, 4),
    (2, 3, 5), (0, 1, 4), (0, 1, 2), (1, 2, 3), (1, 2, 4),
    (2, 3, 4), (0, 1, 3), (0, 2, 3), (0, 2, 4), (1, 3, 4),
)


def mask(vertices: tuple[int, ...]) -> int:
    return sum(1 << vertex for vertex in vertices)


def cycle_square_edges(order: int) -> set[tuple[int, int]]:
    return {
        tuple(sorted((vertex, (vertex + distance) % order)))
        for vertex in range(order)
        for distance in (1, 2)
    }


@dataclass(frozen=True)
class Lobe:
    name: str
    labels: tuple[tuple[int, ...], ...]
    edges: frozenset[tuple[int, int]]
    expected_packet_number: int

    @property
    def order(self) -> int:
        return len(self.labels)

    @property
    def attachment_count(self) -> int:
        return sum(map(len, self.labels))

    @property
    def eta(self) -> int:
        return len(self.edges) + self.attachment_count - 4 * self.order

    def adjacency(self) -> tuple[int, ...]:
        answer = [0] * self.order
        for left, right in self.edges:
            answer[left] |= 1 << right
            answer[right] |= 1 << left
        return tuple(answer)

    def label_masks(self) -> tuple[int, ...]:
        return tuple(map(mask, self.labels))


THIN = Lobe(
    "thin",
    THIN_LABELS,
    frozenset(combinations(range(3), 2)),
    1,
)

RICH_ONE = Lobe(
    "rich-one",
    MU_ONE_LABELS,
    frozenset(cycle_square_edges(20) - {(4, 5), (9, 10), (14, 15)}),
    1,
)

RICH_TWO = Lobe(
    "rich-two",
    MU_TWO_LABELS,
    frozenset(cycle_square_edges(20) - {(4, 5), (14, 15)}),
    2,
)


@dataclass(frozen=True)
class Case:
    name: str
    boundary_edges: frozenset[tuple[int, int]]
    lobes: tuple[Lobe, Lobe, Lobe]
    expected_packet_vector: tuple[int, int, int]


CASES = (
    Case("packet-111", frozenset({(0, 5)}), (RICH_ONE, THIN, THIN), (1, 1, 1)),
    Case("packet-211", frozenset(), (RICH_TWO, THIN, THIN), (2, 1, 1)),
)


def connected(mask_value: int, adjacency: tuple[int, ...]) -> bool:
    if not mask_value:
        return False
    reached = mask_value & -mask_value
    while True:
        expanded = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits ^= bit
            expanded |= adjacency[bit.bit_length() - 1] & mask_value
        if expanded == reached:
            return reached == mask_value
        reached = expanded


def verify_internal_six_connectivity(lobe: Lobe) -> None:
    adjacency = lobe.adjacency()
    labels = lobe.label_masks()
    all_vertices = (1 << lobe.order) - 1
    for subset in range(1, all_vertices + 1):
        boundary_neighbours = 0
        internal_neighbours = 0
        bits = subset
        while bits:
            bit = bits & -bits
            bits ^= bit
            vertex = bit.bit_length() - 1
            boundary_neighbours |= labels[vertex]
            internal_neighbours |= adjacency[vertex] & (all_vertices ^ subset)
        assert boundary_neighbours.bit_count() + internal_neighbours.bit_count() >= 6


def bags_touch(
    root_left: int,
    bag_left: int,
    root_right: int,
    bag_right: int,
    lobe: Lobe,
    boundary_edges: frozenset[tuple[int, int]],
) -> bool:
    if tuple(sorted((root_left, root_right))) in boundary_edges:
        return True
    adjacency = lobe.adjacency()
    labels = lobe.label_masks()
    bits = bag_left
    while bits:
        bit = bits & -bits
        bits ^= bit
        vertex = bit.bit_length() - 1
        if adjacency[vertex] & bag_right or labels[vertex] & (1 << root_right):
            return True
    bits = bag_right
    while bits:
        bit = bits & -bits
        bits ^= bit
        vertex = bit.bit_length() - 1
        if labels[vertex] & (1 << root_left):
            return True
    return False


def rooted_k4_model(
    roots: tuple[int, ...],
    lobe: Lobe,
    boundary_edges: frozenset[tuple[int, int]],
) -> tuple[int, ...] | None:
    """Exhaust every allocation of internal vertices to four rooted bags."""

    adjacency = lobe.adjacency()
    labels = lobe.label_masks()
    candidates: list[list[int]] = []
    for root in roots:
        root_neighbours = sum(
            1 << vertex
            for vertex, label in enumerate(labels)
            if label & (1 << root)
        )
        root_bags = [0]
        for bag in range(1, 1 << lobe.order):
            if connected(bag, adjacency) and bag & root_neighbours:
                root_bags.append(bag)
        candidates.append(root_bags)

    order = sorted(range(4), key=lambda index: len(candidates[index]))
    chosen: dict[int, int] = {}

    def visit(at: int, used: int) -> tuple[int, ...] | None:
        if at == 4:
            return tuple(chosen[index] for index in range(4))
        index = order[at]
        for bag in candidates[index]:
            if bag & used:
                continue
            if not all(
                bags_touch(
                    roots[index], bag, roots[other], other_bag, lobe, boundary_edges
                )
                for other, other_bag in chosen.items()
            ):
                continue
            chosen[index] = bag
            answer = visit(at + 1, used | bag)
            if answer is not None:
                return answer
            del chosen[index]
        return None

    return visit(0, 0)


def two_vertex_rooted_k4(
    roots: tuple[int, ...], lobe: Lobe
) -> tuple[int, ...] | None:
    """Find four bags consisting of one root and one internal vertex."""

    labels = tuple(map(set, lobe.labels))
    candidates = [[v for v, label in enumerate(labels) if root in label] for root in roots]
    chosen: list[int] = []

    def visit(at: int) -> tuple[int, ...] | None:
        if at == 4:
            return tuple(chosen)
        for vertex in candidates[at]:
            if vertex in chosen:
                continue
            if not all(
                tuple(sorted((other_vertex, vertex))) in lobe.edges
                or roots[at] in labels[other_vertex]
                or roots[index] in labels[vertex]
                for index, other_vertex in enumerate(chosen)
            ):
                continue
            chosen.append(vertex)
            answer = visit(at + 1)
            if answer is not None:
                return answer
            chosen.pop()
        return None

    return visit(0)


def five_root_near_clique(
    roots: tuple[int, ...], lobe: Lobe
) -> tuple[int, ...] | None:
    """Find five two-vertex rooted bags with at most one missing pair."""

    labels = tuple(map(set, lobe.labels))
    candidates = [[v for v, label in enumerate(labels) if root in label] for root in roots]
    chosen: list[int] = []

    def visit(at: int, misses: int) -> tuple[int, ...] | None:
        if at == 5:
            return tuple(chosen)
        for vertex in candidates[at]:
            if vertex in chosen:
                continue
            new_misses = misses + sum(
                tuple(sorted((other_vertex, vertex))) not in lobe.edges
                and roots[at] not in labels[other_vertex]
                and roots[index] not in labels[vertex]
                for index, other_vertex in enumerate(chosen)
            )
            if new_misses > 1:
                continue
            chosen.append(vertex)
            answer = visit(at + 1, new_misses)
            if answer is not None:
                return answer
            chosen.pop()
        return None

    return visit(0, 0)


def packet_number(lobe: Lobe) -> int:
    labels = lobe.label_masks()
    all_roots = (1 << 6) - 1
    assert connected((1 << lobe.order) - 1, lobe.adjacency())
    assert all_roots == __import__("functools").reduce(int.__or__, labels, 0)

    root_five_vertices = [
        vertex for vertex, label in enumerate(labels) if label & (1 << 5)
    ]
    if lobe is RICH_ONE:
        assert root_five_vertices == [0]
        return 1
    if lobe is RICH_TWO:
        assert root_five_vertices == [0, 10]
        for packet in ((0, 1), (10, 11)):
            packet_mask = mask(packet)
            assert connected(packet_mask, lobe.adjacency())
            assert __import__("functools").reduce(
                int.__or__, (labels[vertex] for vertex in packet), 0
            ) == all_roots
        return 2

    # Every thin packet has at least two vertices, and two such packets
    # cannot be disjoint in a three-vertex lobe.  Any pair is full.
    assert all(label.bit_count() == 4 for label in labels)
    assert all((labels[left] | labels[right]) == all_roots for left, right in combinations(range(3), 2))
    return 1


def common_four_count(lobe: Lobe, four_set: tuple[int, ...]) -> int:
    required = mask(four_set)
    return sum((label & required) == required for label in lobe.label_masks())


def attachment_counts(lobe: Lobe) -> tuple[int, ...]:
    return tuple(sum(root in label for label in lobe.labels) for root in ROOTS)


def build_host(case: Case) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(ROOTS)
    graph.add_edges_from(case.boundary_edges)
    offset = 6
    for lobe in case.lobes:
        graph.add_nodes_from(range(offset, offset + lobe.order))
        graph.add_edges_from((offset + left, offset + right) for left, right in lobe.edges)
        graph.add_edges_from(
            (offset + vertex, root)
            for vertex, label in enumerate(lobe.labels)
            for root in label
        )
        offset += lobe.order
    return graph


def induced_boundary_edges(
    boundary_edges: frozenset[tuple[int, int]], roots: tuple[int, ...]
) -> int:
    root_set = set(roots)
    return sum(left in root_set and right in root_set for left, right in boundary_edges)


def main() -> None:
    status_transcript: list[str] = []
    five_root_transcript: list[str] = []

    for case in CASES:
        for lobe in set(case.lobes):
            verify_internal_six_connectivity(lobe)
            assert packet_number(lobe) == lobe.expected_packet_number
            assert all(
                lobe.adjacency()[vertex].bit_count() + len(lobe.labels[vertex]) >= 6
                for vertex in range(lobe.order)
            )

        rooted_status: list[set[tuple[int, ...]]] = []
        for lobe_index, lobe in enumerate(case.lobes):
            status: set[tuple[int, ...]] = set()
            for four_set in FOUR_SETS:
                if lobe.name.startswith("rich"):
                    witness_vertices = two_vertex_rooted_k4(four_set, lobe)
                    assert witness_vertices is not None
                    witness = tuple(1 << vertex for vertex in witness_vertices)
                else:
                    found = rooted_k4_model(four_set, lobe, case.boundary_edges)
                    witness = found or ()
                if witness:
                    status.add(four_set)
                status_transcript.append(
                    f"{case.name} {lobe_index} {''.join(map(str, four_set))} "
                    + (",".join(map(str, witness)) if witness else "-")
                )
            rooted_status.append(status)

        assert rooted_status[0] == set(FOUR_SETS)
        if case.name == "packet-211":
            assert rooted_status[1] == rooted_status[2] == set()
        else:
            expected_thin = {
                (0, 1, 2, 5), (0, 1, 3, 5), (0, 1, 4, 5),
                (0, 2, 4, 5), (0, 3, 4, 5),
            }
            assert rooted_status[1] == rooted_status[2] == expected_thin

        # Exact no-root inequalities and common-four singleton capacities.
        for index, lobe in enumerate(case.lobes):
            counts = attachment_counts(lobe)
            for four_set in FOUR_SETS:
                common = common_four_count(lobe, four_set)
                assert common <= 2
                if any(
                    four_set in rooted_status[other]
                    for other in range(3)
                    if other != index
                ):
                    assert common <= 1
                if four_set not in rooted_status[index]:
                    left = (
                        len(lobe.edges)
                        + sum(counts[root] for root in four_set)
                        + induced_boundary_edges(case.boundary_edges, four_set)
                    )
                    assert left <= 3 * lobe.order + 5

            incidence = sum(
                len(tuple(combinations(label, 4))) for label in lobe.labels
            )
            other_roots = set().union(
                *(rooted_status[other] for other in range(3) if other != index)
            )
            assert incidence <= 30 - len(other_roots)

        assert tuple(packet_number(lobe) for lobe in case.lobes) == case.expected_packet_vector
        assert sum(case.expected_packet_vector) <= 4
        for index, status in enumerate(rooted_status):
            if status:
                assert all(
                    case.expected_packet_vector[other] == 1
                    for other in range(3)
                    if other != index
                )

        assert len(case.boundary_edges) + sum(lobe.eta for lobe in case.lobes) == 24

        host = build_host(case)
        assert host.number_of_nodes() == 32
        assert host.number_of_edges() == 128
        assert min(dict(host.degree()).values()) >= 6
        assert nx.node_connectivity(host) == 6

        for omitted in ROOTS:
            roots = tuple(root for root in ROOTS if root != omitted)
            witness = five_root_near_clique(roots, case.lobes[0])
            assert witness is not None
            five_root_transcript.append(
                f"{case.name} omit={omitted} " + ",".join(map(str, witness))
            )

    status_digest = sha256("\n".join(status_transcript).encode()).hexdigest()
    five_root_digest = sha256("\n".join(five_root_transcript).encode()).hexdigest()
    assert status_digest == (
        "f9715fd15b51f3a5aec2845c279ba08c5f930014e8bc82438f1fec60769417d3"
    )
    assert five_root_digest == (
        "438e6fb39a5394cf0d11ab0d6101ab8adee2a2d4befe7cdfbf457a764658eeac"
    )

    print("GREEN sparse-six-cut rooted-status aggregate nonclosure")
    for case in CASES:
        print(
            f"{case.name}: boundary={sorted(case.boundary_edges)} "
            f"etas={[lobe.eta for lobe in case.lobes]} "
            f"packets={case.expected_packet_vector} order=32 size=128 kappa=6"
        )
    print(f"rooted_status_digest={status_digest}")
    print(f"five_root_witness_digest={five_root_digest}")


if __name__ == "__main__":
    main()
