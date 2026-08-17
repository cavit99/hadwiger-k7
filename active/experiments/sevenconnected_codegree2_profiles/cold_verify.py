#!/usr/bin/env python3
"""Independent partition check for the four exceptional quotients and rows.

This checker does not import the main experiment's contraction recursion.
It enumerates every seven-block set partition of every vertex support in
each exceptional eleven-vertex quotient.
"""

from itertools import combinations


J_EDGES = {
    tuple(sorted(edge))
    for edge in (
        (0, 3),
        (0, 4),
        (0, 7),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (3, 4),
        (5, 6),
        (5, 7),
        (6, 7),
    )
}


def quotient(first_miss: int, second_miss: int) -> set[tuple[int, int]]:
    edges = set(J_EDGES)
    edges.update((x, 8) for x in range(8))
    edges.update((x, 9) for x in range(8) if x != first_miss)
    edges.update((x, 10) for x in range(8) if x != second_miss)
    return {tuple(sorted(edge)) for edge in edges}


def connected(block: set[int], edges: set[tuple[int, int]]) -> bool:
    reached = {next(iter(block))}
    while True:
        expanded = reached | {
            y
            for x in reached
            for y in block
            if x != y and tuple(sorted((x, y))) in edges
        }
        if expanded == reached:
            return reached == block
        reached = expanded


def partitions(
    items: list[int], target: int, blocks: list[set[int]] | None = None
):
    """Generate each unlabelled partition into ``target`` blocks once."""

    if blocks is None:
        blocks = []
    if not items:
        if len(blocks) == target:
            yield tuple(frozenset(block) for block in blocks)
        return
    if len(blocks) > target or len(blocks) + len(items) < target:
        return
    x, *rest = items
    for index in range(len(blocks)):
        blocks[index].add(x)
        yield from partitions(rest, target, blocks)
        blocks[index].remove(x)
    if len(blocks) < target:
        blocks.append({x})
        yield from partitions(rest, target, blocks)
        blocks.pop()


def has_near_k7(edges: set[tuple[int, int]]) -> tuple[bool, int]:
    vertices = tuple(range(11))
    checked = 0
    for support_size in range(7, 12):
        for support in combinations(vertices, support_size):
            for bags in partitions(list(support), 7):
                checked += 1
                if not all(connected(set(bag), edges) for bag in bags):
                    continue
                misses = sum(
                    not any(
                        tuple(sorted((x, y))) in edges
                        for x in left
                        for y in right
                    )
                    for left, right in combinations(bags, 2)
                )
                if misses <= 1:
                    return True, checked
    return False, checked


def check_rows() -> dict[tuple[int, int], list[tuple[int, int]]]:
    # Compress each rooted bag R_i to vertex i and include only the
    # guaranteed rooted-model adjacencies.  Vertex 8 is v and vertex 9 is C.
    rows = {
        (2, 3): ((1, 3), (4,), (2, 5), (6,), (0, 7), (8,), (9,)),
        (2, 4): ((2, 3), (4,), (5,), (6,), (0, 7), (1, 8), (9,)),
        (3, 6): ((2,), (4,), (5,), (6,), (0, 3, 7), (1, 8), (9,)),
        (4, 6): ((2,), (3,), (5,), (6,), (0, 4, 7), (8,), (1, 9)),
    }
    base = {edge for edge in quotient(3, 99) if 10 not in edge}
    results = {}
    roots = (2, 3, 4, 6)
    for omitted, bags in rows.items():
        edges = base | {
            tuple(sorted(pair))
            for pair in combinations(roots, 2)
            if pair != omitted
        }
        assert sorted(x for bag in bags for x in bag) == list(range(10))
        assert all(connected(set(bag), edges) for bag in bags)
        absent = [
            (first, second)
            for first, second in combinations(range(7), 2)
            if not any(
                tuple(sorted((x, y))) in edges
                for x in bags[first]
                for y in bags[second]
            )
        ]
        assert len(absent) <= 1
        results[omitted] = absent
    return results


def main() -> None:
    for misses in ((3, 5), (3, 6), (4, 5), (4, 6)):
        found, checked = has_near_k7(quotient(*misses))
        assert not found
        assert checked == 159_027
        print(f"negative misses={misses} partitions={checked}")
    print(f"rows={check_rows()}")
    print("GREEN independent partition and completion check")


if __name__ == "__main__":
    main()
