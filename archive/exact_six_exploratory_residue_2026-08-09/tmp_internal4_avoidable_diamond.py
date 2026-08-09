#!/usr/bin/env python3
"""Small-order falsifier for marked avoidance in an internally 4-connected pair."""

from itertools import combinations
import subprocess

from tmp_seven_terminal_avoidable_diamond import (
    parse_graph6,
    rooted_diamond_model,
)


def components(mask: int, adjacency: list[int]):
    while mask:
        reached = mask & -mask
        frontier = reached
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            new = adjacency[vertex] & mask & ~reached
            reached |= new
            frontier |= new
        yield reached
        mask &= ~reached


def internally_four_connected(adjacency: list[int], roots: tuple[int, ...]) -> bool:
    n = len(adjacency)
    full = (1 << n) - 1
    root_mask = sum(1 << root for root in roots)
    for count in range(4):
        for removed_vertices in combinations(range(n), count):
            removed = sum(1 << vertex for vertex in removed_vertices)
            remainder = full ^ removed
            parts = tuple(components(remainder, adjacency))
            if len(parts) <= 1:
                continue
            surviving_roots = root_mask & remainder
            if any(not (part & surviving_roots) for part in parts):
                return False
    return True


def main() -> None:
    process = subprocess.Popen(
        ["geng", "-q", "-c", "7"], stdout=subprocess.PIPE, text=True
    )
    assert process.stdout is not None
    instances = failures = 0
    for line in process.stdout:
        graph = parse_graph6(line)
        for roots in combinations(range(7), 4):
            if not internally_four_connected(graph, roots):
                continue
            marked = tuple(vertex for vertex in range(7) if vertex not in roots)
            instances += 1
            if not any(rooted_diamond_model(graph, roots, w) for w in marked):
                failures += 1
                print("FAIL", line.strip(), roots, tuple(graph))
                return
    assert process.wait() == 0
    print(f"instances={instances}")
    print(f"failures={failures}")


if __name__ == "__main__":
    main()
