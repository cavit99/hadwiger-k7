#!/usr/bin/env python3
"""Verify and exhaust the static two-coordinate split profiles."""

from __future__ import annotations

from itertools import combinations, product


ORDER = 8
VERTICES = tuple(range(ORDER))
FOREIGN = (4, 5, 6, 7)
PAIR_STATUS = ((True, False), (False, True), (True, True))
CROSS_EDGES = ((0, 2), (0, 3), (1, 2), (1, 3))


def empty_graph() -> list[int]:
    return [0] * ORDER


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def has_edge(adjacency: list[int], left: int, right: int) -> bool:
    return bool(adjacency[left] & (1 << right))


def base_profile() -> list[int]:
    adjacency = empty_graph()
    add_edge(adjacency, 0, 1)
    add_edge(adjacency, 2, 3)
    for left, right in combinations(FOREIGN, 2):
        add_edge(adjacency, left, right)
    return adjacency


def profile(choices: tuple[int, ...], cross_mask: int) -> tuple[list[int], int, int]:
    adjacency = base_profile()
    first_statuses = [choice // 3 for choice in choices]
    second_statuses = [choice % 3 for choice in choices]

    for index, bag in enumerate(FOREIGN):
        for side, present in enumerate(PAIR_STATUS[first_statuses[index]]):
            if present:
                add_edge(adjacency, side, bag)
        for side, present in enumerate(PAIR_STATUS[second_statuses[index]]):
            if present:
                add_edge(adjacency, 2 + side, bag)

    for bit, edge in enumerate(CROSS_EDGES):
        if cross_mask & (1 << bit):
            add_edge(adjacency, *edge)

    first_root_double = bool(cross_mask & 0b0011) and bool(cross_mask & 0b1100)
    second_root_double = bool(cross_mask & 0b0101) and bool(cross_mask & 0b1010)
    first_score = sum(status == 2 for status in first_statuses) + first_root_double
    second_score = sum(status == 2 for status in second_statuses) + second_root_double
    return adjacency, first_score, second_score


def missing_edges(adjacency: list[int], vertices: tuple[int, ...]) -> int:
    return sum(
        not has_edge(adjacency, left, right)
        for left, right in combinations(vertices, 2)
    )


def has_k7_minus_minor(adjacency: list[int]) -> bool:
    """Test K7-minus exactly for a connected graph of order eight."""

    for omitted in VERTICES:
        retained = tuple(vertex for vertex in VERTICES if vertex != omitted)
        if missing_edges(adjacency, retained) <= 1:
            return True

    for left, right in combinations(VERTICES, 2):
        if not has_edge(adjacency, left, right):
            continue
        retained = tuple(vertex for vertex in VERTICES if vertex not in (left, right))
        missing = missing_edges(adjacency, retained)
        missing += sum(
            not (has_edge(adjacency, left, vertex) or has_edge(adjacency, right, vertex))
            for vertex in retained
        )
        if missing <= 1:
            return True
    return False


def has_k5_subgraph(adjacency: list[int]) -> bool:
    return any(
        missing_edges(adjacency, vertices) == 0
        for vertices in combinations(VERTICES, 5)
    )


def vertex_connectivity(adjacency: list[int]) -> int:
    def connected_without(removed: set[int]) -> bool:
        retained = set(VERTICES) - removed
        if len(retained) <= 1:
            return True
        reached = {next(iter(retained))}
        boundary = list(reached)
        while boundary:
            vertex = boundary.pop()
            for neighbour in retained - reached:
                if has_edge(adjacency, vertex, neighbour):
                    reached.add(neighbour)
                    boundary.append(neighbour)
        return reached == retained

    for order in range(ORDER - 1):
        if any(
            not connected_without(set(removed))
            for removed in combinations(VERTICES, order)
        ):
            return order
    return ORDER - 1


def explicit_barrier() -> list[int]:
    adjacency = empty_graph()
    missing = {frozenset(edge) for edge in ((0, 6), (1, 7), (2, 4), (3, 5))}
    for left, right in combinations(VERTICES, 2):
        if frozenset((left, right)) not in missing:
            add_edge(adjacency, left, right)
    return adjacency


def verify_explicit_barrier() -> None:
    adjacency = explicit_barrier()
    bags = ((0, 1), (2, 3), (4,), (5,), (6,), (7,))
    assert all(has_edge(adjacency, *bag) for bag in bags[:2])
    assert all(
        any(has_edge(adjacency, left, right) for left in bags[i] for right in bags[j])
        for i, j in combinations(range(6), 2)
    )

    first_score = sum(
        any(has_edge(adjacency, 0, vertex) for vertex in bag)
        and any(has_edge(adjacency, 1, vertex) for vertex in bag)
        for bag in bags[1:]
    )
    second_foreign = (bags[0],) + bags[2:]
    second_score = sum(
        any(has_edge(adjacency, 2, vertex) for vertex in bag)
        and any(has_edge(adjacency, 3, vertex) for vertex in bag)
        for bag in second_foreign
    )
    assert (first_score, second_score) == (3, 3)
    assert not has_k5_subgraph(adjacency)
    assert missing_edges(adjacency, FOREIGN) == 0
    assert vertex_connectivity(adjacency) == 6
    assert not has_k7_minus_minor(adjacency)

    signature_witnesses = {
        "EE": (0, 0, 1, 1, 2, 3, 4, 5),
        "EP": (0, 0, 1, 2, 1, 2, 3, 4),
        "PE": (0, 1, 2, 2, 3, 4, 0, 1),
        "PP": (0, 1, 2, 3, 2, 3, 0, 1),
    }
    for signature, colouring in signature_witnesses.items():
        observed = (
            ("E" if colouring[0] == colouring[1] else "P")
            + ("E" if colouring[2] == colouring[3] else "P")
        )
        assert observed == signature
        assert all(
            colouring[left] != colouring[right]
            for left, right in combinations(VERTICES, 2)
            if has_edge(adjacency, left, right)
            and (left, right) not in ((0, 1), (2, 3))
        )


def exhaustive_counts() -> dict[str, int]:
    counts = {
        "total": 0,
        "blocked": 0,
        "target_free": 0,
        "omega_at_most_four": 0,
        "maximal_blocked_omega_four": 0,
        "degree_six_maximal": 0,
    }
    for choices in product(range(9), repeat=4):
        for cross_mask in range(1, 16):
            adjacency, first_score, second_score = profile(choices, cross_mask)
            counts["total"] += 1
            if first_score > 3 or second_score > 3:
                continue
            counts["blocked"] += 1
            if has_k7_minus_minor(adjacency):
                continue
            counts["target_free"] += 1
            no_k5 = not has_k5_subgraph(adjacency)
            if no_k5:
                counts["omega_at_most_four"] += 1
            if first_score == second_score == 3 and no_k5:
                counts["maximal_blocked_omega_four"] += 1
            if first_score == second_score == 3 and min(map(int.bit_count, adjacency)) >= 6:
                counts["degree_six_maximal"] += 1
                missing = [
                    (left, right)
                    for left, right in combinations(VERTICES, 2)
                    if not has_edge(adjacency, left, right)
                ]
                assert len(missing) == 4
                assert len({vertex for edge in missing for vertex in edge}) == 8
    return counts


def main() -> None:
    verify_explicit_barrier()
    counts = exhaustive_counts()
    expected = {
        "total": 98_415,
        "blocked": 84_928,
        "target_free": 79_768,
        "omega_at_most_four": 30_652,
        "maximal_blocked_omega_four": 384,
        "degree_six_maximal": 24,
    }
    assert counts == expected, counts
    print("GREEN static two-split profile barrier")
    print("graph=K_8-4K_2 connectivity=6 omega=4 split_scores=(3,3)")
    print("K7_minus_minor=false PP_signature=true")
    for key, value in counts.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
