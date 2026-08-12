#!/usr/bin/env python3
"""Verify the set-endpoint barrier for a colour-rooted five-fan."""

from __future__ import annotations

import itertools


ORDER = 9
Q = frozenset(range(7))
Q_EDGES = {
    (0, 3), (0, 5), (1, 4), (2, 5), (2, 6), (3, 6),
}
FAN_EDGES = {
    (0, 3), (0, 5), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6),
}
CONNECTOR_EDGES = {(1, 7), (4, 7), (5, 8), (6, 8)}
EDGES = frozenset(Q_EDGES | FAN_EDGES | CONNECTOR_EDGES)
COLOUR_BLOCKS = ({0, 1, 2}, {3}, {4}, {5}, {6})


def adjacent(x: int, y: int) -> bool:
    return tuple(sorted((x, y))) in EDGES


def connected(block: tuple[int, ...]) -> bool:
    seen = {block[0]}
    while True:
        new = {
            y
            for x in seen
            for y in set(block) - seen
            if adjacent(x, y)
        }
        if not new:
            return len(seen) == len(block)
        seen |= new


def partitions(items: tuple[int, ...], block_count: int = 5):
    blocks: list[list[int]] = []

    def extend(index: int):
        if index == len(items):
            if len(blocks) == block_count:
                yield tuple(tuple(block) for block in blocks)
            return
        item = items[index]
        for block in blocks:
            block.append(item)
            yield from extend(index + 1)
            block.pop()
        if len(blocks) < block_count:
            blocks.append([item])
            yield from extend(index + 1)
            blocks.pop()

    yield from extend(0)


def has_k5_minus_minor() -> tuple[bool, int, int]:
    tested = 0
    connected_models = 0
    vertices = tuple(range(ORDER))
    for used_order in range(5, ORDER + 1):
        for used in itertools.combinations(vertices, used_order):
            for bags in partitions(used):
                tested += 1
                if not all(connected(bag) for bag in bags):
                    continue
                connected_models += 1
                contacts = sum(
                    any(adjacent(x, y) for x in bags[i] for y in bags[j])
                    for i, j in itertools.combinations(range(5), 2)
                )
                if contacts >= 9:
                    return True, tested, connected_models
    return False, tested, connected_models


def main() -> None:
    assert all(
        not adjacent(x, y)
        for block in COLOUR_BLOCKS
        for x, y in itertools.combinations(block, 2)
    )
    assert set().union(*COLOUR_BLOCKS) == Q

    # Q is the disjoint union of 0-3-6-2-5-0 and the edge 1-4.
    assert Q_EDGES == {
        (0, 3), (3, 6), (2, 6), (2, 5), (0, 5), (1, 4),
    }

    # The rooted fan has hub 3 and path 0-5-4-6.
    assert FAN_EDGES == {
        *(tuple(sorted((3, x))) for x in (0, 5, 4, 6)),
        (0, 5), (4, 5), (4, 6),
    }

    # The two disjoint connectors join colour blocks A-C and D-E.
    assert connected((1, 7, 4))
    assert connected((5, 8, 6))
    assert {1, 7, 4}.isdisjoint({5, 8, 6})

    found, tested, connected_models = has_k5_minus_minor()
    assert not found
    assert tested == 22827
    print(
        "set_endpoint_barrier",
        f"partitions_tested={tested}",
        f"connected_five_bag_models={connected_models}",
        "K5_minus_minor=False",
    )


if __name__ == "__main__":
    main()
