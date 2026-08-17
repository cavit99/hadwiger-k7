#!/usr/bin/env python3
"""Exact recursive verifier for the returned order-two dense-lobe theorem.

The nine quotient vertices are

    0,...,5 : the separator S,
    6,7     : the two ends x,y of the order-two component,
    8       : the opposite component contracted to one vertex b.

At equality, |E(S)|=e and |E({x,y},S)|=21-e.  Fullness says that
each separator vertex is adjacent to x or y.  Consequently exactly
e-9 separator vertices are adjacent to only one of x,y, and every other
separator vertex is adjacent to both.

For each labelled equality profile, the minor search starts with singleton
bags and recursively deletes a bag or merges two touching bags.  It accepts
exactly at seven connected bags having at most one nonadjacent pair.  This
is an exact K_7-minus minor search, not a subgraph search.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product


ORDER = 9
SEPARATOR = tuple(range(6))
LEFT = 6
RIGHT = 7
POLE = 8
SEPARATOR_EDGES = tuple(combinations(SEPARATOR, 2))


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def touching(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    return any(
        adjacency[vertex] & right
        for vertex in range(ORDER)
        if left & (1 << vertex)
    )


def near_clique_minor(
    adjacency: tuple[int, ...], target_order: int = 7
) -> tuple[int, ...] | None:
    """Return a K_target-minus model, or None when none exists."""

    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> tuple[int, ...] | None:
        if len(bags) == target_order:
            missing = sum(
                not touching(adjacency, left, right)
                for left, right in combinations(bags, 2)
            )
            return bags if missing <= 1 else None

        if len(bags) < target_order:
            return None

        for left_index, right_index in combinations(range(len(bags)), 2):
            if not touching(
                adjacency, bags[left_index], bags[right_index]
            ):
                continue
            merged = [
                bag
                for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            answer = search(tuple(sorted(merged)))
            if answer is not None:
                return answer

        for deleted_index in range(len(bags)):
            answer = search(
                bags[:deleted_index] + bags[deleted_index + 1 :]
            )
            if answer is not None:
                return answer
        return None

    return search(tuple(1 << vertex for vertex in range(ORDER)))


def equality_statuses(edge_count: int) -> tuple[tuple[int, ...], ...]:
    """Return all equality attachment strings.

    Status 0 means left-only, 1 means right-only, and 2 means both.
    """

    single_count = edge_count - 9
    return tuple(
        status
        for status in product(range(3), repeat=6)
        if sum(value != 2 for value in status) == single_count
    )


def quotient(
    separator_mask: int, status: tuple[int, ...]
) -> tuple[int, ...]:
    adjacency = [0] * ORDER
    for bit, edge in enumerate(SEPARATOR_EDGES):
        if separator_mask & (1 << bit):
            add_edge(adjacency, *edge)

    add_edge(adjacency, LEFT, RIGHT)
    for vertex, value in enumerate(status):
        if value != 1:
            add_edge(adjacency, LEFT, vertex)
        if value != 0:
            add_edge(adjacency, RIGHT, vertex)
        add_edge(adjacency, POLE, vertex)
    return tuple(adjacency)


def calibrate() -> None:
    positive = [0] * ORDER
    for left, right in combinations(range(7), 2):
        if (left, right) != (0, 1):
            add_edge(positive, left, right)
    assert near_clique_minor(tuple(positive)) is not None

    negative = [0] * ORDER
    for left, right in combinations(range(6), 2):
        add_edge(negative, left, right)
    assert near_clique_minor(tuple(negative)) is None


def main() -> None:
    calibrate()
    certificate_hash = sha256()
    grand_total = 0

    for edge_count in (9, 10, 11):
        checked = 0
        positive = 0
        statuses = equality_statuses(edge_count)
        for separator_mask in range(1 << len(SEPARATOR_EDGES)):
            if separator_mask.bit_count() != edge_count:
                continue
            for status in statuses:
                checked += 1
                model = near_clique_minor(quotient(separator_mask, status))
                if model is None:
                    raise AssertionError(
                        "counterexample: "
                        f"eS={edge_count} separator_mask={separator_mask} "
                        f"status={status}"
                    )
                positive += 1
                certificate_hash.update(
                    (
                        f"{edge_count}:{separator_mask}:"
                        f"{''.join(map(str, status))}:"
                        f"{','.join(map(str, model))}\n"
                    ).encode("ascii")
                )

        expected = (
            len(tuple(combinations(range(15), edge_count)))
            * len(statuses)
        )
        assert checked == expected == positive
        grand_total += checked
        print(
            f"eS={edge_count} checked={checked} positive={positive}"
        )

    assert grand_total == 122_941
    print("controls=PASS")
    print(f"total={grand_total}")
    print(f"certificate_digest={certificate_hash.hexdigest()}")


if __name__ == "__main__":
    main()
