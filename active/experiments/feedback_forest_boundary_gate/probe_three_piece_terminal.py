#!/usr/bin/env python3
"""Verify the contact-only ``7,6,7`` quotient counterexample.

The verifier is deliberately standard-library-only so that the repository's
official verifier runner can reproduce the certificate without an activated
project environment.
"""

from __future__ import annotations

from collections.abc import Iterable
from itertools import combinations


Graph = dict[int, set[int]]
P, Q = 0, 1
CYCLE = tuple(range(2, 7))


def add_edge(graph: Graph, left: int, right: int) -> None:
    graph.setdefault(left, set()).add(right)
    graph.setdefault(right, set()).add(left)


def add_edges(graph: Graph, edge_set: Iterable[tuple[int, int]]) -> None:
    for left, right in edge_set:
        add_edge(graph, left, right)


def edges(graph: Graph) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left in sorted(graph)
        for right in sorted(graph[left])
        if left < right
    )


def boundary() -> tuple[Graph, tuple[int, ...]]:
    leaves = tuple(range(7, 11))
    graph: Graph = {vertex: set() for vertex in range(11)}
    add_edge(graph, P, Q)
    add_edges(graph, ((root, vertex) for root in (P, Q) for vertex in CYCLE))
    add_edges(
        graph,
        (
            (CYCLE[index], CYCLE[(index + 1) % len(CYCLE)])
            for index in range(len(CYCLE))
        ),
    )
    add_edges(graph, ((P, leaf) for leaf in leaves))
    return graph, leaves


def augment(base: Graph, leaves: tuple[int, ...]) -> tuple[Graph, tuple[int, int, int]]:
    graph = {vertex: set(neighbours) for vertex, neighbours in base.items()}
    a, b, c = len(base), len(base) + 1, len(base) + 2
    for vertex in (a, b, c):
        graph[vertex] = set()
    add_edges(graph, ((a, b), (b, c)))
    add_edges(
        graph,
        (
            (piece, vertex)
            for piece in (a, c)
            for vertex in (P, Q, CYCLE[0], *leaves)
        ),
    )
    add_edges(graph, ((b, vertex) for vertex in (P, Q, *leaves)))
    return graph, (a, b, c)


def is_clique(graph: Graph, vertices: tuple[int, ...]) -> bool:
    return all(right in graph[left] for left, right in combinations(vertices, 2))


def maximum_clique_order(graph: Graph) -> int:
    vertices = tuple(graph)
    for size in range(len(vertices), 0, -1):
        if any(is_clique(graph, choice) for choice in combinations(vertices, size)):
            return size
    return 0


def connected_indices(indices: set[int], links: tuple[tuple[int, int], ...]) -> bool:
    if not indices:
        return False
    adjacency = {index: set() for index in indices}
    for left, right in links:
        if left in indices and right in indices:
            adjacency[left].add(right)
            adjacency[right].add(left)
    seen = {next(iter(indices))}
    stack = list(seen)
    while stack:
        for neighbour in adjacency[stack.pop()] - seen:
            seen.add(neighbour)
            stack.append(neighbour)
    return seen == indices


def validate_tree_decomposition(
    graph: Graph,
    bags: tuple[frozenset[int], ...],
    links: tuple[tuple[int, int], ...],
    maximum_width: int,
) -> None:
    all_indices = set(range(len(bags)))
    if len(links) != len(bags) - 1 or not connected_indices(all_indices, links):
        raise AssertionError("decomposition graph is not a tree")
    if max(map(len, bags), default=0) > maximum_width + 1:
        raise AssertionError("decomposition exceeds the claimed width")
    if set().union(*bags) != set(graph):
        raise AssertionError("decomposition does not cover every vertex")
    for left, right in edges(graph):
        if not any(left in bag and right in bag for bag in bags):
            raise AssertionError(f"edge {left, right} is not covered")
    for vertex in graph:
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        if not connected_indices(containing, links):
            raise AssertionError(f"bags containing {vertex} are disconnected")


def displayed_tree_decomposition(
    pieces: tuple[int, int, int], leaves: tuple[int, ...]
) -> tuple[tuple[frozenset[int], ...], tuple[tuple[int, int], ...]]:
    a, b, c = pieces
    r0, r1, r2, r3, r4 = CYCLE
    bags = (
        frozenset((P, Q, r0, r3, r4)),
        frozenset((P, Q, r0, r2, r3)),
        frozenset((P, Q, r0, r1, r2)),
        frozenset((P, Q, r0, a, c)),
        frozenset((P, Q, a, b, c)),
        *(frozenset((P, a, b, c, leaf)) for leaf in leaves),
    )
    links = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        *((4, index) for index in range(5, len(bags))),
    )
    return bags, links


def k_colourable(graph: Graph, colour_count: int) -> bool:
    assigned: dict[int, int] = {}

    def extend() -> bool:
        if len(assigned) == len(graph):
            return True
        vertex = max(
            (item for item in graph if item not in assigned),
            key=lambda item: (
                len({assigned[w] for w in graph[item] if w in assigned}),
                len(graph[item]),
            ),
        )
        forbidden = {assigned[w] for w in graph[vertex] if w in assigned}
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if extend():
                return True
            del assigned[vertex]
        return False

    return extend()


def graph6(graph: Graph) -> str:
    order = len(graph)
    if tuple(sorted(graph)) != tuple(range(order)) or order > 62:
        raise AssertionError("compact graph6 encoder requires labels 0,...,n-1 and n<=62")
    bits = [int(right in graph[left]) for right in range(order) for left in range(right)]
    bits.extend([0] * (-len(bits) % 6))
    payload = "".join(
        chr(63 + sum(bit << (5 - offset) for offset, bit in enumerate(bits[start : start + 6])))
        for start in range(0, len(bits), 6)
    )
    return chr(63 + order) + payload


def main() -> None:
    base, leaves = boundary()
    graph, pieces = augment(base, leaves)
    a, b, c = pieces
    bags, links = displayed_tree_decomposition(pieces, leaves)
    validate_tree_decomposition(graph, bags, links, 4)

    if k_colourable(base, 4) or not k_colourable(base, 5):
        raise AssertionError("boundary is not exactly five-chromatic")
    clique_order = maximum_clique_order(graph)
    if clique_order >= 5:
        raise AssertionError("literal K5 detected")
    if c in graph[a] or b not in graph[a] or c not in graph[b]:
        raise AssertionError("the exterior vertices do not induce a path")
    contacts = tuple(len(graph[piece] & set(base)) for piece in (a, b, c))
    if contacts[0] < 7 or contacts[1] < 6 or contacts[2] < 7:
        raise AssertionError(f"insufficient boundary contacts: {contacts}")

    print(f"boundary_order={len(base)}")
    print(f"host_order={len(graph)}")
    print(f"pendant_count={len(leaves)}")
    print(f"outer_core={(P, Q, CYCLE[0])}")
    print(f"middle_core={(P, Q)}")
    print(f"pendants={leaves}")
    print(f"contacts={contacts}")
    print(f"maximum_clique={clique_order}")
    print(f"treewidth_upper_bound={max(map(len, bags)) - 1}")
    print(f"graph6={graph6(graph)}")
    print("COUNTEREXAMPLE_TO_CONTACT_ONLY_767_QUOTIENT")


if __name__ == "__main__":
    main()
