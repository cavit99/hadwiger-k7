#!/usr/bin/env python3
"""Verify the connected-full bridge quotient barrier.

The quotient has an eight-vertex boundary, one full singleton pole, and a
two-vertex connected full component whose bridge deletion leaves two
one-miss pieces.  The final search enumerates every family of seven
disjoint nonempty connected branch sets: unused vertices are deleted and
touching bags are contracted from the singleton state.  A K7-minus model
would occur exactly when one reachable seven-bag state had at least twenty
of its twenty-one bag contacts.

Only the Python standard library is used.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")

import hashlib
import itertools
from collections import Counter


BOUNDARY_ORDER = 8
QUOTIENT_ORDER = 11
BOUNDARY_CODE = "G@aIZ_"
EXPECTED_STATE_COUNTS = {
    11: 1,
    10: 44,
    9: 810,
    8: 8076,
    7: 47385,
}
EXPECTED_STATE_DIGEST = (
    "8e76ba088cc1a21e772d160c5284bb6d38df807af33651eb848a712d304a5642"
)
EXPECTED_CONTACT_HISTOGRAM = {
    7: 5,
    8: 11,
    9: 18,
    10: 183,
    11: 596,
    12: 1200,
    13: 3416,
    14: 7196,
    15: 10150,
    16: 12248,
    17: 8866,
    18: 2906,
    19: 590,
}


def normalized_edge(left: int, right: int) -> tuple[int, int]:
    assert left != right
    return (left, right) if left < right else (right, left)


def decode_graph6(code: str) -> frozenset[tuple[int, int]]:
    """Decode a short graph6 string."""
    assert code and ord(code[0]) - 63 == BOUNDARY_ORDER
    bits: list[int] = []
    for character in code[1:]:
        value = ord(character) - 63
        assert 0 <= value < 64
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))

    edges: set[tuple[int, int]] = set()
    position = 0
    for right in range(1, BOUNDARY_ORDER):
        for left in range(right):
            if bits[position]:
                edges.add((left, right))
            position += 1
    return frozenset(edges)


def encode_graph6(edges: frozenset[tuple[int, int]]) -> str:
    bits = [
        int((left, right) in edges)
        for right in range(1, BOUNDARY_ORDER)
        for left in range(right)
    ]
    bits.extend([0] * (-len(bits) % 6))
    return chr(BOUNDARY_ORDER + 63) + "".join(
        chr(
            63
            + sum(
                bits[position + offset] << (5 - offset)
                for offset in range(6)
            )
        )
        for position in range(0, len(bits), 6)
    )


def adjacent(
    edges: frozenset[tuple[int, int]],
    left: int,
    right: int,
) -> bool:
    return normalized_edge(left, right) in edges


def clique_number(edges: frozenset[tuple[int, int]]) -> int:
    for order in range(BOUNDARY_ORDER, 0, -1):
        if any(
            all(adjacent(edges, left, right) for left, right in itertools.combinations(vertices, 2))
            for vertices in itertools.combinations(range(BOUNDARY_ORDER), order)
        ):
            return order
    raise AssertionError("the empty set is not needed")


def independence_number(edges: frozenset[tuple[int, int]]) -> int:
    for order in range(BOUNDARY_ORDER, 0, -1):
        if any(
            all(not adjacent(edges, left, right) for left, right in itertools.combinations(vertices, 2))
            for vertices in itertools.combinations(range(BOUNDARY_ORDER), order)
        ):
            return order
    raise AssertionError("the empty set is not needed")


def quotient_edges(
    boundary_edges: frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]]:
    # Boundary: 0,...,7; full pole z=8; split images a=9 and b=10.
    answer = set(boundary_edges)
    pole, left, right = 8, 9, 10
    for boundary in range(BOUNDARY_ORDER):
        answer.add(normalized_edge(pole, boundary))
        if boundary != 0:
            answer.add(normalized_edge(left, boundary))
        if boundary != 1:
            answer.add(normalized_edge(right, boundary))
    answer.add((left, right))
    return frozenset(answer)


def adjacency_masks(
    edges: frozenset[tuple[int, int]],
) -> tuple[int, ...]:
    answer = [0] * QUOTIENT_ORDER
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


def neighbours_in(
    adjacency: tuple[int, ...],
    vertices: frozenset[int],
    targets: frozenset[int],
) -> frozenset[int]:
    answer = 0
    for vertex in vertices:
        answer |= adjacency[vertex]
    return frozenset(
        vertex for vertex in targets if (answer >> vertex) & 1
    )


def connected_components(
    adjacency: tuple[int, ...],
    vertices: frozenset[int],
) -> tuple[frozenset[int], ...]:
    remaining = set(vertices)
    answer = []
    while remaining:
        reached = {min(remaining)}
        while True:
            enlarged = reached | {
                neighbour
                for vertex in reached
                for neighbour in remaining
                if (adjacency[vertex] >> neighbour) & 1
            }
            if enlarged == reached:
                break
            reached = enlarged
        answer.append(frozenset(reached))
        remaining -= reached
    return tuple(sorted(answer, key=lambda component: min(component)))


def bags_touch(
    adjacency: tuple[int, ...],
    left: int,
    right: int,
) -> bool:
    todo = left
    while todo:
        bit = todo & -todo
        todo ^= bit
        if adjacency[bit.bit_length() - 1] & right:
            return True
    return False


def connected_mask(adjacency: tuple[int, ...], vertices: int) -> bool:
    assert vertices
    reached = vertices & -vertices
    while True:
        enlarged = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            enlarged |= adjacency[bit.bit_length() - 1] & vertices
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def contact_count(adjacency: tuple[int, ...], bags: tuple[int, ...]) -> int:
    return sum(
        bags_touch(adjacency, left, right)
        for left, right in itertools.combinations(bags, 2)
    )


def next_states(
    adjacency: tuple[int, ...],
    state: tuple[int, ...],
) -> set[tuple[int, ...]]:
    """Apply one vertex deletion or one legal edge contraction."""
    answer = {
        state[:deleted] + state[deleted + 1 :]
        for deleted in range(len(state))
    }
    for first, second in itertools.combinations(range(len(state)), 2):
        if not bags_touch(adjacency, state[first], state[second]):
            continue
        merged = state[first] | state[second]
        new_state = tuple(
            bag
            for index, bag in enumerate(state)
            if index not in (first, second)
        ) + (merged,)
        answer.add(tuple(sorted(new_state)))
    return answer


def state_record(order: int, state: tuple[int, ...]) -> str:
    return f"{order}:" + ",".join(map(str, state))


def main() -> None:
    boundary = decode_graph6(BOUNDARY_CODE)
    assert encode_graph6(boundary) == BOUNDARY_CODE
    assert len(boundary) == 10
    omega = clique_number(boundary)
    alpha = independence_number(boundary)
    assert omega == 3
    assert alpha == 3

    edges = quotient_edges(boundary)
    adjacency = adjacency_masks(edges)
    boundary_vertices = frozenset(range(BOUNDARY_ORDER))
    outside_vertices = frozenset(range(BOUNDARY_ORDER, QUOTIENT_ORDER))
    pole, left, right = 8, 9, 10

    assert len(edges) == 33
    assert connected_components(adjacency, outside_vertices) == (
        frozenset({pole}),
        frozenset({left, right}),
    )
    assert neighbours_in(adjacency, frozenset({pole}), boundary_vertices) == boundary_vertices
    assert neighbours_in(adjacency, frozenset({left}), boundary_vertices) == boundary_vertices - {0}
    assert neighbours_in(adjacency, frozenset({right}), boundary_vertices) == boundary_vertices - {1}
    assert neighbours_in(adjacency, frozenset({left, right}), boundary_vertices) == boundary_vertices
    assert adjacent(edges, left, right)
    assert {
        edge
        for edge in edges
        if edge[0] in outside_vertices and edge[1] in outside_vertices
    } == {(left, right)}

    states = {tuple(1 << vertex for vertex in range(QUOTIENT_ORDER))}
    records: list[str] = []
    observed_counts: dict[int, int] = {}
    for order in range(QUOTIENT_ORDER, 7, -1):
        observed_counts[order] = len(states)
        records.extend(state_record(order, state) for state in sorted(states))
        following: set[tuple[int, ...]] = set()
        for state in states:
            following.update(next_states(adjacency, state))
        states = following

    observed_counts[7] = len(states)
    records.extend(state_record(7, state) for state in sorted(states))
    assert observed_counts == EXPECTED_STATE_COUNTS

    for state in states:
        assert len(state) == 7
        assert all(state)
        assert all(
            not (left & right)
            for left, right in itertools.combinations(state, 2)
        )
        assert all(connected_mask(adjacency, bag) for bag in state)

    histogram = Counter(contact_count(adjacency, state) for state in states)
    assert dict(sorted(histogram.items())) == EXPECTED_CONTACT_HISTOGRAM
    assert max(histogram) == 19
    assert sum(
        multiplicity
        for contacts, multiplicity in histogram.items()
        if contacts >= 20
    ) == 0

    state_digest = hashlib.sha256(
        ("\n".join(records) + "\n").encode()
    ).hexdigest()
    assert state_digest == EXPECTED_STATE_DIGEST

    counts_text = ",".join(
        f"{order}:{observed_counts[order]}"
        for order in range(QUOTIENT_ORDER, 6, -1)
    )
    histogram_text = ",".join(
        f"{contacts}:{multiplicity}"
        for contacts, multiplicity in sorted(histogram.items())
    )
    print(
        f"boundary_graph6={BOUNDARY_CODE} order=8 edges=10 "
        f"omega={omega} alpha={alpha}"
    )
    print(
        "quotient_order=11 edges=33 "
        "profiles=z:full,a:miss-0,b:miss-1 joined_component:full"
    )
    print(f"reachable_states={counts_text}")
    print(f"state_digest={state_digest}")
    print(f"seven_bag_contact_histogram={histogram_text}")
    print("seven_bag_states=47385 max_contacts=19 k7minus_models=0")
    print("PASS connected-full bridge quotient barrier")


if __name__ == "__main__":
    main()
