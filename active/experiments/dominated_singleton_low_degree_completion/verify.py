#!/usr/bin/env python3
"""Verify the degree-eight/nine dominated-singleton completion.

The finite input is a triangle-free graph Q of order seven or eight with
the contraction-critical independence bound and no K_5^- minor.  A marked
vertex (order seven) or marked pair (order eight) represents model-persistent
edges at the singleton.  The script classifies the cases in which every
vertex cut of order at most two contains all marked vertices, then checks
the exterior-component completion for the surviving marked graphs.
"""

from __future__ import annotations

from functools import lru_cache
import itertools
import os
import shutil
import subprocess


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


def decode_graph6(line: str) -> tuple[int, ...]:
    text = line.strip()
    order = ord(text[0]) - 63
    assert 0 <= order <= 62
    bits: list[int] = []
    for character in text[1:]:
        value = ord(character) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    graph = [0] * order
    position = 0
    for right in range(1, order):
        for left in range(right):
            if bits[position]:
                graph[left] |= 1 << right
                graph[right] |= 1 << left
            position += 1
    return tuple(graph)


def adjacent(graph: tuple[int, ...], left: int, right: int) -> bool:
    return bool(graph[left] & (1 << right))


def edge_count(graph: tuple[int, ...]) -> int:
    return sum(row.bit_count() for row in graph) // 2


def delete_vertex(graph: tuple[int, ...], deleted: int) -> tuple[int, ...]:
    keep = [vertex for vertex in range(len(graph)) if vertex != deleted]
    answer = [0] * len(keep)
    for i, left in enumerate(keep):
        for j in range(i + 1, len(keep)):
            right = keep[j]
            if adjacent(graph, left, right):
                answer[i] |= 1 << j
                answer[j] |= 1 << i
    return tuple(answer)


def contract_edge(
    graph: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(graph)) if vertex != right]
    answer = [0] * len(keep)
    for i, first in enumerate(keep):
        for j in range(i + 1, len(keep)):
            second = keep[j]
            edge = adjacent(graph, first, second)
            if first == left:
                edge |= adjacent(graph, right, second)
            if second == left:
                edge |= adjacent(graph, first, right)
            if edge:
                answer[i] |= 1 << j
                answer[j] |= 1 << i
    return tuple(answer)


@lru_cache(maxsize=None)
def has_dense_minor(graph: tuple[int, ...], order: int, edges: int) -> bool:
    if len(graph) < order:
        return False
    if len(graph) == order:
        return edge_count(graph) >= edges
    if any(
        has_dense_minor(delete_vertex(graph, vertex), order, edges)
        for vertex in range(len(graph))
    ):
        return True
    return any(
        adjacent(graph, left, right)
        and has_dense_minor(contract_edge(graph, left, right), order, edges)
        for left, right in itertools.combinations(range(len(graph)), 2)
    )


def independence_number(graph: tuple[int, ...]) -> int:
    for size in range(len(graph), 0, -1):
        for vertices in itertools.combinations(range(len(graph)), size):
            if all(
                not adjacent(graph, left, right)
                for left, right in itertools.combinations(vertices, 2)
            ):
                return size
    return 0


def components_after(
    graph: tuple[int, ...], deleted: tuple[int, ...]
) -> list[frozenset[int]]:
    remaining = set(range(len(graph))) - set(deleted)
    components: list[frozenset[int]] = []
    while remaining:
        start = remaining.pop()
        reached = {start}
        stack = [start]
        while stack:
            vertex = stack.pop()
            neighbours = {
                other for other in remaining if adjacent(graph, vertex, other)
            }
            remaining -= neighbours
            reached |= neighbours
            stack.extend(neighbours)
        components.append(frozenset(reached))
    return components


def small_cuts(graph: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [
        cut
        for size in range(3)
        for cut in itertools.combinations(range(len(graph)), size)
        if len(components_after(graph, cut)) >= 2
    ]


def triangle_free_graphs(order: int) -> list[tuple[str, tuple[int, ...]]]:
    executable = os.environ.get("GENG") or shutil.which("geng")
    if executable is None:
        raise SystemExit("geng from nauty is required (or set GENG)")
    process = subprocess.run(
        [executable, "-q", "-t", str(order)],
        check=True,
        capture_output=True,
        text=True,
    )
    return [(line, decode_graph6(line)) for line in process.stdout.splitlines()]


def marked_survivors(
    order: int, alpha_bound: int, marked_order: int
) -> tuple[int, int, list[tuple[str, tuple[int, ...]]]]:
    eligible = 0
    marked_instances = 0
    survivors: list[tuple[str, tuple[int, ...]]] = []
    for graph6, graph in triangle_free_graphs(order):
        if independence_number(graph) > alpha_bound:
            continue
        if has_dense_minor(graph, 5, 9):
            continue
        cuts = small_cuts(graph)
        if not cuts:
            continue
        eligible += 1
        for marked in itertools.combinations(range(order), marked_order):
            marked_instances += 1
            if all(set(marked) <= set(cut) for cut in cuts):
                survivors.append((graph6, marked))
    return eligible, marked_instances, survivors


def add_dominated_apices_and_component(
    graph: tuple[int, ...], missed: tuple[int, ...]
) -> tuple[int, ...]:
    """Add u,v and a contracted exterior component c.

    Vertices 0,...,q-1 induce Q; v=q and u=q+1 are adjacent and complete
    to Q.  The component vertex c=q+2 sees all of {v}+Q except ``missed``.
    It is nonadjacent to u because it came from G-N[u].
    """

    order = len(graph)
    v, u, component = order, order + 1, order + 2
    answer = list(graph) + [0, 0, 0]

    def add_edge(left: int, right: int) -> None:
        answer[left] |= 1 << right
        answer[right] |= 1 << left

    add_edge(u, v)
    for vertex in range(order):
        add_edge(u, vertex)
        add_edge(v, vertex)
    missed_set = set(missed)
    for vertex in [*range(order), v]:
        if vertex not in missed_set:
            add_edge(component, vertex)
    return tuple(answer)


def check_exterior_completion(graph6: str) -> int:
    graph = decode_graph6(graph6)
    interface = [*range(len(graph)), len(graph)]  # Q together with v
    maximum_misses = len(interface) - 7
    profiles = 0
    for size in range(maximum_misses + 1):
        for missed in itertools.combinations(interface, size):
            profiles += 1
            host = add_dominated_apices_and_component(graph, missed)
            assert has_dense_minor(host, 7, 20), (graph6, missed)
    return profiles


def main() -> None:
    # Exact-minor positive and negative controls.
    k5_minus = tuple(((1 << 5) - 1) ^ (1 << vertex) for vertex in range(5))
    k5_minus = list(k5_minus)
    k5_minus[0] &= ~(1 << 1)
    k5_minus[1] &= ~(1 << 0)
    assert has_dense_minor(tuple(k5_minus), 5, 9)
    assert not has_dense_minor((0, 0, 0, 0, 0), 5, 9)

    order7 = marked_survivors(7, 3, 1)
    order8 = marked_survivors(8, 4, 2)
    assert order7 == (9, 63, [("FCxv?", (0,)), ("FCxv?", (5,))])
    assert order8 == (158, 4424, [("G?rF`w", (6, 7))])

    profiles7 = check_exterior_completion("FCxv?")
    profiles8 = check_exterior_completion("G?rF`w")
    assert profiles7 == 9
    assert profiles8 == 46

    print("GREEN dominated-singleton low-degree completion")
    print(
        "order7 eligible=9 marked=63 survivors=2 "
        "graph6=FCxv? exterior_profiles=9"
    )
    print(
        "order8 eligible=158 marked=4424 survivors=1 "
        "graph6=G?rF`w exterior_profiles=46"
    )


if __name__ == "__main__":
    main()
