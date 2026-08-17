#!/usr/bin/env python3
"""Verify the sixteen arithmetic bag profiles in the order-eight theorem."""

from __future__ import annotations

import itertools


def partitions(total, parts, maximum=None):
    """Yield nonincreasing positive integer partitions."""
    if parts == 0:
        if total == 0:
            yield ()
        return
    if maximum is None:
        maximum = total
    for first in range(min(maximum, total - parts + 1), 0, -1):
        for rest in partitions(total - first, parts - 1, first):
            yield (first,) + rest


def main():
    shapes = tuple(partitions(8, 5))
    assert shapes == (
        (4, 1, 1, 1, 1),
        (3, 2, 1, 1, 1),
        (2, 2, 2, 1, 1),
    )

    profiles = set()
    for shape in shapes:
        for size in range(1, 6):
            for selected in itertools.combinations(range(5), size):
                shore_order = sum(shape[index] for index in selected)
                surplus = shore_order - size
                if surplus > 1:
                    continue
                selected_sizes = tuple(sorted(shape[index] for index in selected))
                assert surplus in (0, 1)
                if surplus == 0:
                    assert all(value == 1 for value in selected_sizes)
                    profile_type = "singleton"
                else:
                    assert selected_sizes.count(2) == 1
                    assert all(value in (1, 2) for value in selected_sizes)
                    profile_type = "one-edge-bag"
                profiles.add((shape, profile_type, size, selected_sizes))

    expected = set()
    for size in range(1, 5):
        expected.add(((4, 1, 1, 1, 1), "singleton", size, (1,) * size))
    for size in range(1, 4):
        expected.add(((3, 2, 1, 1, 1), "singleton", size, (1,) * size))
    for size in range(1, 5):
        expected.add(
            ((3, 2, 1, 1, 1), "one-edge-bag", size, (1,) * (size - 1) + (2,))
        )
    for size in range(1, 3):
        expected.add(((2, 2, 2, 1, 1), "singleton", size, (1,) * size))
    for size in range(1, 4):
        expected.add(
            ((2, 2, 2, 1, 1), "one-edge-bag", size, (1,) * (size - 1) + (2,))
        )

    assert profiles == expected
    assert len(profiles) == 16

    # Check the numerical Hall consequences used in the theorem.
    for shape, profile_type, size, selected_sizes in sorted(profiles):
        shore_order = sum(selected_sizes)
        surplus = shore_order - size
        root_set = size - 1
        complement = 8 - shore_order
        other_roots = 6 - root_set
        if profile_type == "singleton":
            assert surplus == 0
            assert complement == other_roots + 1
        else:
            assert surplus == 1
            assert complement == other_roots
        # The two Hall matchings use all six roots and leave two shore vertices.
        matched_vertices = root_set + min(complement, other_roots)
        assert matched_vertices == 6
        assert 8 - matched_vertices == 2

    summary = {}
    for shape, profile_type, size, _ in profiles:
        summary.setdefault((shape, profile_type), []).append(size)
    for key in sorted(summary):
        print(key, tuple(sorted(summary[key])))
    print(f"profiles={len(profiles)} matched_vertices=6 unmatched_vertices=2")
    print("order-eight Hall profile classification: PASS")


if __name__ == "__main__":
    main()
