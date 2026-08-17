#!/usr/bin/env python3
"""Falsify the two-exceptional-neighbourhood linkage proposal.

The test uses the first cubic exceptional boundary surviving the one-centre
quotient screen.  Two copies are joined by identifying seven boundary
vertices, as obtained after contracting seven disjoint paths between two
degree-eight centres.  We search all omitted vertices and bijections, and
stop at the first quotient without a ``K_7^-`` minor.

This is an exploratory route test, not a promoted finite theorem.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations


BOUNDARY_EDGES = {
    (0, 3), (0, 4), (0, 7),
    (1, 2), (1, 3), (1, 4),
    (2, 5), (2, 6),
    (3, 4),
    (5, 6), (5, 7),
    (6, 7),
}
ORDER = 11


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def linked_quotient(first_omitted: int, second_omitted: int,
                    second_order: tuple[int, ...]) -> tuple[int, ...]:
    adjacency = [0] * ORDER
    first_remaining = [vertex for vertex in range(8) if vertex != first_omitted]
    second_remaining = [vertex for vertex in range(8) if vertex != second_omitted]
    first_image = {vertex: index for index, vertex in enumerate(first_remaining)}
    first_image[first_omitted] = 7
    second_image = {
        vertex: second_order[index]
        for index, vertex in enumerate(second_remaining)
    }
    second_image[second_omitted] = 8

    for left, right in BOUNDARY_EDGES:
        add_edge(adjacency, first_image[left], first_image[right])
        add_edge(adjacency, second_image[left], second_image[right])

    for vertex in range(7):
        add_edge(adjacency, 9, vertex)
        add_edge(adjacency, 10, vertex)
    add_edge(adjacency, 9, 7)
    add_edge(adjacency, 10, 8)
    return tuple(adjacency)


def has_k7minus_minor(adjacency: tuple[int, ...]) -> bool:
    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> bool:
        if len(bags) == 7:
            contacts = 0
            for left, right in combinations(bags, 2):
                if any(
                    adjacency[vertex] & right
                    for vertex in range(ORDER)
                    if left & (1 << vertex)
                ):
                    contacts += 1
            return contacts >= 20

        touching: list[tuple[int, int]] = []
        for left_index, right_index in combinations(range(len(bags)), 2):
            left, right = bags[left_index], bags[right_index]
            if any(
                adjacency[vertex] & right
                for vertex in range(ORDER)
                if left & (1 << vertex)
            ):
                touching.append((left_index, right_index))
        for left_index, right_index in touching:
            merged = [
                bag for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            if search(tuple(sorted(merged))):
                return True
        for deleted_index in range(len(bags)):
            reduced = bags[:deleted_index] + bags[deleted_index + 1:]
            if search(reduced):
                return True
        return False

    return search(tuple(1 << vertex for vertex in range(ORDER)))


def edge_list(adjacency: tuple[int, ...]) -> str:
    return " ".join(
        f"{left}-{right}"
        for left, right in combinations(range(ORDER), 2)
        if adjacency[left] & (1 << right)
    )


def main() -> None:
    tested = 0
    common = tuple(range(7))
    for first_omitted in range(8):
        for second_omitted in range(8):
            for second_order in permutations(common):
                quotient = linked_quotient(
                    first_omitted, second_omitted, second_order
                )
                tested += 1
                if not has_k7minus_minor(quotient):
                    print(
                        "SURVIVOR",
                        f"first_omitted={first_omitted}",
                        f"second_omitted={second_omitted}",
                        f"second_order={second_order}",
                        f"tested={tested}",
                    )
                    print(f"edges={edge_list(quotient)}")
                    return
    print(f"PASS tested={tested}")


if __name__ == "__main__":
    main()
