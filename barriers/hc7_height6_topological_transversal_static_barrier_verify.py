#!/usr/bin/env python3
"""Verify the static height-six topological-transversal barrier."""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json


GRAPH6 = "Nwf_POKE?sdkR~KV|VW"
VERTICES = tuple(range(15))
EXPECTED_EDGES = tuple(
    sorted(
        {
            tuple(sorted(edge))
            for edge in (
                (0, 1), (0, 2), (0, 4), (0, 5), (0, 14),
                (1, 2), (1, 5), (1, 12), (1, 14),
                (2, 5), (2, 7), (2, 11), (2, 13), (2, 14),
                (3, 4), (3, 9), (3, 10), (3, 13),
                (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11),
                (4, 12), (4, 14),
                (5, 8), (5, 11), (5, 12),
                (6, 10), (6, 12), (6, 14),
                (7, 11), (7, 12), (7, 13),
                (8, 11), (8, 12), (8, 14),
                (9, 10), (9, 12), (9, 13), (9, 14),
                (10, 12), (10, 13), (10, 14),
                (11, 12), (11, 13),
                (12, 13), (12, 14),
                (13, 14),
            )
        }
    )
)


def decode_graph6(graph6: str) -> tuple[tuple[int, int], ...]:
    """Decode the compact graph6 form used here (order at most 62)."""

    values = [ord(character) - 63 for character in graph6]
    assert values and values[0] == len(VERTICES)
    bits = [
        (value >> shift) & 1
        for value in values[1:]
        for shift in range(5, -1, -1)
    ]
    pairs = [(left, right) for right in range(1, values[0]) for left in range(right)]
    return tuple(sorted(pair for pair, present in zip(pairs, bits) if present))


EDGES = decode_graph6(GRAPH6)
assert EDGES == EXPECTED_EDGES
EDGE_SET = set(EDGES)

SUPPORTS = (
    (0, 1, 2, 5, 8, 14),
    (0, 4, 5, 8, 11, 12),
    (2, 5, 7, 11, 12, 13),
    (3, 4, 9, 10, 11, 13),
    (4, 7, 9, 10, 12, 13),
    (4, 9, 11, 12, 13, 14),
)

PRIVATE_PAIRS = (
    (3, 12),
    (13, 14),
    (4, 14),
    (0, 12),
    (11, 14),
    (5, 10),
)

# support, internal vertex, subdivided-edge ends, missing neighbours of the
# internal vertex among the other three branch vertices, deficiency type
ORIENTED_SUPPORTS = (
    (SUPPORTS[0], 8, 5, 14, {0, 1, 2}, (1, 3, 0)),
    (SUPPORTS[1], 0, 4, 5, {8, 11, 12}, (1, 3, 0)),
    (SUPPORTS[2], 5, 2, 12, {7, 13}, (1, 2, 1)),
    (SUPPORTS[3], 11, 4, 13, {3, 9, 10}, (1, 3, 0)),
    (SUPPORTS[4], 7, 4, 13, {9, 10}, (1, 2, 1)),
    (SUPPORTS[5], 11, 4, 13, {9, 14}, (1, 2, 1)),
)

BAGS = tuple(
    map(
        frozenset,
        (
            (3, 4, 9, 10, 13),
            (4, 6, 10, 12, 14),
            (4, 10, 12, 13, 14),
            (0, 1, 2, 5, 12, 14),
            (0, 2, 4, 5, 12, 14),
            (2, 4, 5, 11, 12, 14),
            (2, 4, 7, 11, 12, 13),
            (2, 4, 11, 12, 13, 14),
            (4, 5, 8, 11, 12, 14),
            (4, 9, 10, 12, 13, 14),
        ),
    )
)

TREE_EDGES = (
    (7, 5), (5, 4), (5, 8), (4, 3), (7, 6),
    (7, 2), (2, 9), (2, 1), (9, 0),
)

COLOUR_CLASSES = (
    (2, 3, 12),
    (4, 5, 13),
    (11, 14),
    (1, 7, 8, 10),
    (0, 6, 9),
)


def adjacent(left: int, right: int) -> bool:
    return tuple(sorted((left, right))) in EDGE_SET


def clique(vertices: tuple[int, ...]) -> bool:
    return all(adjacent(left, right) for left, right in combinations(vertices, 2))


def tk5_witnesses(support: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]:
    """Return (internal, left, right) witnesses for a spanning TK5."""

    witnesses = []
    for internal in support:
        branch_vertices = tuple(vertex for vertex in support if vertex != internal)
        for left, right in combinations(branch_vertices, 2):
            if not (adjacent(internal, left) and adjacent(internal, right)):
                continue
            if all(
                adjacent(x, y)
                for x, y in combinations(branch_vertices, 2)
                if (x, y) != (left, right)
            ):
                witnesses.append((internal, left, right))
    return tuple(witnesses)


def hits(candidate: tuple[int, ...], family: tuple[tuple[int, ...], ...]) -> bool:
    chosen = set(candidate)
    return all(chosen.intersection(support) for support in family)


def connected_indices(indices: object, adjacency: list[set[int]]) -> bool:
    remaining = set(indices)
    if not remaining:
        return True
    seen = {next(iter(remaining))}
    stack = list(seen)
    while stack:
        current = stack.pop()
        for neighbour in (adjacency[current] & remaining) - seen:
            seen.add(neighbour)
            stack.append(neighbour)
    return seen == remaining


def verify_tree_decomposition() -> None:
    tree_adjacency = [set() for _ in BAGS]
    for left, right in TREE_EDGES:
        tree_adjacency[left].add(right)
        tree_adjacency[right].add(left)

    assert len(TREE_EDGES) == len(BAGS) - 1
    assert connected_indices(range(len(BAGS)), tree_adjacency)
    assert max(map(len, BAGS)) - 1 == 5
    assert all(any({left, right} <= bag for bag in BAGS) for left, right in EDGES)
    assert all(
        connected_indices(
            (index for index, bag in enumerate(BAGS) if vertex in bag),
            tree_adjacency,
        )
        for vertex in VERTICES
    )


def main() -> None:
    literal_k5 = tuple(support for support in combinations(VERTICES, 5) if clique(support))
    six_vertex_tk5 = tuple(
        support for support in combinations(VERTICES, 6) if tk5_witnesses(support)
    )
    family = literal_k5 + six_vertex_tk5

    assert literal_k5 == (
        (4, 6, 10, 12, 14),
        (4, 9, 10, 12, 14),
        (9, 10, 12, 13, 14),
    )
    assert (len(literal_k5), len(six_vertex_tk5), len(family)) == (3, 48, 51)

    assert not any(
        hits(candidate, family)
        for order in range(3)
        for candidate in combinations(VERTICES, order)
    )
    assert hits((0, 4, 12), family)

    relative_family = literal_k5 + SUPPORTS
    assert not any(
        hits(candidate, relative_family)
        for order in range(3)
        for candidate in combinations(VERTICES, order)
    )

    for index, (support, private_pair) in enumerate(zip(SUPPORTS, PRIVATE_PAIRS)):
        assert support in six_vertex_tk5
        assert not any(set(clique_support) <= set(support) for clique_support in literal_k5)
        assert set(support).isdisjoint(private_pair)
        assert hits(private_pair, literal_k5 + SUPPORTS[:index] + SUPPORTS[index + 1 :])
        missed_orders = [
            len(candidate)
            for candidate in family
            if set(candidate).isdisjoint(private_pair)
        ]
        assert min(missed_orders) == 6

    for support, internal, left, right, expected_missing, expected_type in ORIENTED_SUPPORTS:
        assert tk5_witnesses(support) == ((internal, min(left, right), max(left, right)),)
        assert not adjacent(left, right)

        branch_vertices = set(support) - {internal}
        defect_left = {
            vertex for vertex in branch_vertices - {left} if not adjacent(left, vertex)
        }
        other_branch_vertices = branch_vertices - {left, right}
        defect_internal = {
            vertex for vertex in other_branch_vertices if not adjacent(internal, vertex)
        }
        observed_type = (
            len(defect_left),
            len(defect_internal),
            len(other_branch_vertices - defect_internal),
        )

        assert defect_left == {right}
        assert defect_internal == expected_missing
        assert observed_type == expected_type

    assert any(
        set(first).isdisjoint(second)
        for first, second in combinations(PRIVATE_PAIRS, 2)
    )

    verify_tree_decomposition()
    assert set().union(*(set(colour_class) for colour_class in COLOUR_CLASSES)) == set(VERTICES)
    assert all(
        not any(adjacent(left, right) for left, right in combinations(colour_class, 2))
        for colour_class in COLOUR_CLASSES
    )
    assert literal_k5  # Together with the five-colouring, this gives chi(J)=5.

    cut = {4, 9, 10, 13}
    assert not any(adjacent(3, vertex) for vertex in set(VERTICES) - cut - {3})

    edge_payload = json.dumps(EDGES, separators=(",", ":"))
    family_payload = json.dumps(family, separators=(",", ":"))
    edge_digest = sha256(edge_payload.encode()).hexdigest()
    family_digest = sha256(family_payload.encode()).hexdigest()
    assert edge_digest == "ba8924dea37e6343a51fddd5818d34a4bf5e8650309c34f303f73c01f5cfd65d"
    assert family_digest == "a5890f1aca440564136fa8714a1f7727a0c0958ccfcd6b2e749dc945bc29d428"

    print("GREEN height-six topological-transversal static barrier")
    print("graph vertices=15 edges=50 literal_K5=3 six_vertex_TK5=48 tau=3")
    print("relative_kernel=6 types=(1,3,0):3,(1,2,1):3 private_disjoint=yes")
    print("treewidth_upper_bound=5 chromatic_number=5 seven_connected=no")
    print(f"edge_sha256={edge_digest}")
    print(f"family_sha256={family_digest}")


if __name__ == "__main__":
    main()
