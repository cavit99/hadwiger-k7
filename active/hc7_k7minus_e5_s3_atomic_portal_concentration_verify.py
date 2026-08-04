#!/usr/bin/env python3
"""Verify the atomic portal-concentration obstructions in the E5 s=3 row.

The four graphs retain the two helpers and four rooted bags of a
``Z``-rooted ``K^*_{4,2}`` model.  The vertices of the exceptional
three- or four-separator are all placed in the rooted bag ``r0``.  Thus a
tiny side adjacent to every separator vertex has only one neighbour among
the six contracted model bags.  The two edge cases retain both endpoints
of the tiny side.

The canonical legitimate boundary orientation has
``J-t=P_2 disjoint union K_2`` with root edges ``r0r1,r2r3``, the edge
``tr0``, and ``q`` adjacent to ``r0,r1``.  In the singleton ``T3`` case the
residual vertex ``b`` is also placed in ``r0``; in the ``T4`` cases the
residual anchor ``p`` is placed there.  Their forced ``q``- or
``{t,q}``-contacts are therefore already represented by existing edges.

This is a finite quotient check, not a host counterexample and not a proof
of E5.  In particular, the internal order and excess of the rooted bag are
not encoded.

Run:

    python3 active/hc7_k7minus_e5_s3_atomic_portal_concentration_verify.py

Expected final line:

    VERIFIED: all four atomic portal-concentration quotients exclude K_7^-
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Iterator, Sequence


ROOTS = (0, 1, 2, 3)
U = 4
V = 5
X = 6
Y = 7
T = 8
Q = 9


def require(condition: bool, message: str) -> None:
    """Raise an always-active verification error when a check fails."""

    if not condition:
        raise RuntimeError(message)


def edge(left: int, right: int) -> tuple[int, int]:
    require(left != right, "loops are not allowed")
    return tuple(sorted((left, right)))


def common_edges() -> set[tuple[int, int]]:
    """Return the edges common to all four concentrated quotients."""

    edges = {
        edge(0, 1),
        edge(2, 3),
        edge(U, V),
        edge(X, T),
        edge(Y, T),
        edge(T, Q),
        edge(T, 0),
        edge(Q, 0),
        edge(Q, 1),
    }
    edges.update(edge(helper, root) for helper in (U, V) for root in ROOTS)
    edges.update(edge(singleton, root) for singleton in (X, Y) for root in ROOTS)
    return edges


@dataclass(frozen=True)
class Instance:
    name: str
    names: tuple[str, ...]
    edges: frozenset[tuple[int, int]]
    expected_connected: tuple[int, ...]
    expected_minimum_defect: int

    @property
    def order(self) -> int:
        return len(self.names)


def instances() -> tuple[Instance, ...]:
    """Construct the four exact atomic quotient graphs."""

    base = common_edges()

    t3_singleton = base | {
        edge(10, T),
        edge(10, Q),
        edge(10, 0),
    }
    t3_edge = base | {
        # The two endpoint-incidence rows have the same contracted graph:
        # b sees every portal, while p sees two or three of them.
        edge(10, 11),
        edge(10, T),
        edge(10, Q),
        edge(11, Q),
        edge(10, 0),
        edge(11, 0),
    }
    t4_singleton = base | {
        edge(10, Q),
        edge(10, 0),
    }
    t4_edge = base | {
        # Likewise c sees all four portals and b sees three or four.
        edge(10, 11),
        edge(10, Q),
        edge(10, 0),
        edge(11, 0),
    }

    common_names = ("r0", "r1", "r2", "r3", "U", "V", "x", "y", "t", "q")
    return (
        Instance(
            "T3-singleton-p",
            common_names + ("p",),
            frozenset(t3_singleton),
            (330, 2352, 7728, 13002, 9127),
            2,
        ),
        Instance(
            "T3-edge-pb",
            common_names + ("p", "b"),
            frozenset(t3_edge),
            (792, 6510, 26264, 61140, 79303, 44945),
            2,
        ),
        Instance(
            "T4-singleton-b",
            common_names + ("b",),
            frozenset(t4_singleton),
            (330, 2268, 7231, 11772, 7964),
            2,
        ),
        Instance(
            "T4-edge-bc",
            common_names + ("b", "c"),
            frozenset(t4_edge),
            (792, 6090, 23268, 51125, 62187, 32850),
            2,
        ),
    )


def adjacency_masks(order: int, edges: Sequence[tuple[int, int]]) -> tuple[int, ...]:
    adjacency = [0] * order
    for left, right in edges:
        require(
            0 <= left < order and 0 <= right < order,
            "edge endpoint out of range",
        )
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    return tuple(adjacency)


def seven_partitions(items: Sequence[int]) -> Iterator[tuple[int, ...]]:
    """Yield every unlabelled partition of ``items`` into seven bitmasks."""

    bags: list[int] = []

    def visit(position: int) -> Iterator[tuple[int, ...]]:
        if position == len(items):
            if len(bags) == 7:
                yield tuple(bags)
            return
        if len(bags) + len(items) - position < 7:
            return

        bit = 1 << items[position]
        for index in range(len(bags)):
            bags[index] |= bit
            yield from visit(position + 1)
            bags[index] ^= bit
        if len(bags) < 7:
            bags.append(bit)
            yield from visit(position + 1)
            bags.pop()

    yield from visit(0)


def connected(mask: int, adjacency: Sequence[int]) -> bool:
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


def touches(first: int, second: int, adjacency: Sequence[int]) -> bool:
    neighbours = 0
    scan = first
    while scan:
        bit = scan & -scan
        scan ^= bit
        neighbours |= adjacency[bit.bit_length() - 1]
    return bool(neighbours & second)


def defect(partition: Sequence[int], adjacency: Sequence[int]) -> int:
    return sum(
        not touches(partition[left], partition[right], adjacency)
        for left, right in combinations(range(7), 2)
    )


def self_test() -> None:
    """Check the defect encoding on one positive and one negative graph."""

    singleton_partition = tuple(1 << vertex for vertex in range(7))
    k7_minus_edges = {
        edge(left, right)
        for left, right in combinations(range(7), 2)
        if (left, right) != (0, 1)
    }
    require(
        defect(singleton_partition, adjacency_masks(7, k7_minus_edges)) == 1,
        "positive K_7^- self-test failed",
    )

    k6_edges = {edge(left, right) for left, right in combinations(range(6), 2)}
    require(
        defect(singleton_partition, adjacency_masks(7, k6_edges)) == 6,
        "negative K_6 self-test failed",
    )


def display(partition: Sequence[int], names: Sequence[str]) -> str:
    bags = []
    for mask in partition:
        members = ",".join(
            names[vertex]
            for vertex in range(len(names))
            if mask >> vertex & 1
        )
        bags.append("{" + members + "}")
    return " | ".join(bags)


def verify(
    instance: Instance,
) -> tuple[tuple[int, ...], tuple[int, ...], int, tuple[int, ...]]:
    adjacency = adjacency_masks(instance.order, instance.edges)
    total_by_order = [0] * (instance.order + 1)
    connected_by_order = [0] * (instance.order + 1)
    minimum_defect = 22
    closest: tuple[int, ...] = ()

    for used_order in range(7, instance.order + 1):
        for used in combinations(range(instance.order), used_order):
            for partition in seven_partitions(used):
                total_by_order[used_order] += 1
                if not all(connected(bag, adjacency) for bag in partition):
                    continue
                connected_by_order[used_order] += 1
                current = defect(partition, adjacency)
                if current < minimum_defect:
                    minimum_defect = current
                    closest = partition

    require(minimum_defect >= 2, f"{instance.name} contains a K_7^- minor")
    return (
        tuple(total_by_order[7:]),
        tuple(connected_by_order[7:]),
        minimum_defect,
        closest,
    )


def main() -> None:
    self_test()
    cases = instances()
    require(len(cases) == 4, "wrong number of atomic cases")
    for instance in cases:
        total_counts, connected_counts, minimum_defect, closest = verify(instance)
        expected_totals = (
            (330, 4620, 25410, 64680, 63987)
            if instance.order == 11
            else (792, 13860, 101640, 388080, 767844, 627396)
        )
        require(
            total_counts == expected_totals,
            f"{instance.name}: partition count changed",
        )
        require(
            connected_counts == instance.expected_connected,
            f"{instance.name}: connected-partition count changed",
        )
        require(
            minimum_defect == instance.expected_minimum_defect,
            f"{instance.name}: minimum defect changed",
        )
        print(
            instance.name,
            f"vertices={instance.order}",
            f"edges={len(instance.edges)}",
            f"partitions_by_used_order={total_counts}",
            f"connected_by_used_order={connected_counts}",
            f"minimum_defect={minimum_defect}",
        )
        print("closest", display(closest, instance.names))

    print("VERIFIED: all four atomic portal-concentration quotients exclude K_7^-")


if __name__ == "__main__":
    main()
