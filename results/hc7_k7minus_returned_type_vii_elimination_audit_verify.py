#!/usr/bin/env python3
"""Independent graph-state check of the 121 type-VII quotient cases."""

from functools import lru_cache
from itertools import combinations, product


BOUNDARY_EDGES = frozenset(
    tuple(sorted(map(int, token)))
    for token in "01 02 03 14 24 35 45".split()
)
PATTERNS = tuple(product(range(3), repeat=6))


def feasible(pattern: tuple[int, ...]) -> bool:
    first = sum(entry in (0, 2) for entry in pattern)
    second = sum(entry in (1, 2) for entry in pattern)
    return first >= 5 and second >= 5


def quotient(patterns: tuple[tuple[int, ...], ...]):
    edges = set(BOUNDARY_EDGES)
    next_vertex = 6
    for pattern in patterns:
        first, second = next_vertex, next_vertex + 1
        next_vertex += 2
        edges.add((first, second))
        for root, entry in enumerate(pattern):
            if entry in (0, 2):
                edges.add(tuple(sorted((root, first))))
            if entry in (1, 2):
                edges.add(tuple(sorted((root, second))))
    for _ in range(3 - len(patterns)):
        for root in range(6):
            edges.add((root, next_vertex))
        next_vertex += 1
    return tuple(sorted(edges)), next_vertex


def delete(edges, order: int, vertex: int):
    relabel = {
        old: old if old < vertex else old - 1
        for old in range(order)
        if old != vertex
    }
    image = {
        tuple(sorted((relabel[left], relabel[right])))
        for left, right in edges
        if left != vertex and right != vertex
    }
    return tuple(sorted(image)), order - 1


def contract(edges, order: int, left: int, right: int):
    image = set()
    for first, second in edges:
        first = left if first == right else first
        second = left if second == right else second
        if first != second:
            image.add(tuple(sorted((first, second))))
    return delete(image, order, right)


@lru_cache(maxsize=None)
def has_target(edges, order: int) -> bool:
    """Exact graph-state deletion/contraction search, independent of bags."""
    if order == 7:
        return len(edges) >= 20
    if order < 7:
        return False
    for left, right in edges:
        contracted, new_order = contract(edges, order, left, right)
        if has_target(contracted, new_order):
            return True
    for vertex in range(order):
        deleted, new_order = delete(edges, order, vertex)
        if has_target(deleted, new_order):
            return True
    return False


def main() -> None:
    same = tuple(
        pattern
        for pattern in PATTERNS
        if pattern[1] == pattern[2] == 2 and feasible(pattern)
    )
    first = tuple(
        pattern
        for pattern in PATTERNS
        if pattern[1] == 2 and pattern[2] != 2 and feasible(pattern)
    )
    second = tuple(
        pattern
        for pattern in PATTERNS
        if pattern[2] == 2 and pattern[1] != 2 and feasible(pattern)
    )
    if (len(same), len(first), len(second)) != (21, 10, 10):
        raise RuntimeError("independent pattern counts changed")

    checked = 0
    for pattern in same:
        edges, order = quotient((pattern,))
        if not has_target(edges, order):
            raise RuntimeError(f"same-component failure: {pattern}")
        checked += 1
    for first_pattern in first:
        for second_pattern in second:
            edges, order = quotient((first_pattern, second_pattern))
            if not has_target(edges, order):
                raise RuntimeError(
                    f"split-component failure: {first_pattern}, {second_pattern}"
                )
            checked += 1

    print("GREEN independent type-VII graph-state audit")
    print(f"quotients_checked={checked}")
    print(f"search_states={has_target.cache_info().currsize}")


if __name__ == "__main__":
    main()
