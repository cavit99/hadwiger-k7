#!/usr/bin/env python3
"""Verify the full-component contraction connectivity barrier."""

from __future__ import annotations

from itertools import combinations


S = tuple(range(6))
A_BLOCKS = tuple(tuple(range(6 + 2 * i, 8 + 2 * i)) for i in range(6))
B_BLOCKS = tuple(tuple(range(18 + 4 * i, 22 + 4 * i)) for i in range(6))
A = tuple(v for block in A_BLOCKS for v in block)
B = tuple(v for block in B_BLOCKS for v in block)
VERTICES = tuple(range(42))


def add_edge(adjacency: list[int], u: int, v: int) -> None:
    assert u != v
    adjacency[u] |= 1 << v
    adjacency[v] |= 1 << u


def build_graph() -> list[int]:
    adjacency = [0] * len(VERTICES)
    for clique in (A, B):
        for u, v in combinations(clique, 2):
            add_edge(adjacency, u, v)
    for i, s in enumerate(S):
        for v in A_BLOCKS[i] + B_BLOCKS[i]:
            add_edge(adjacency, s, v)
    return adjacency


def mask(vertices: tuple[int, ...]) -> int:
    answer = 0
    for v in vertices:
        answer |= 1 << v
    return answer


def connected_after(adjacency: list[int], deleted: int) -> bool:
    remaining = ((1 << len(adjacency)) - 1) & ~deleted
    if not remaining:
        return True
    reached = remaining & -remaining
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & remaining & ~reached
        reached |= new
        frontier |= new
    return reached == remaining


def component(adjacency: list[int], vertices: tuple[int, ...]) -> bool:
    keep = mask(vertices)
    return connected_after(adjacency, ((1 << len(adjacency)) - 1) & ~keep)


def contract_a(adjacency: list[int]) -> tuple[list[int], int, tuple[tuple[int, ...], ...]]:
    # Quotient labels: S stays 0..5, B stays 6..29, and a is 30.
    quotient = [0] * 31
    b_label = {old: 6 + i for i, old in enumerate(B)}
    a = 30
    for u, v in combinations(B, 2):
        add_edge(quotient, b_label[u], b_label[v])
    quotient_blocks = []
    for i, s in enumerate(S):
        block = tuple(b_label[v] for v in B_BLOCKS[i])
        quotient_blocks.append(block)
        add_edge(quotient, s, a)
        for v in block:
            add_edge(quotient, s, v)
    return quotient, a, tuple(quotient_blocks)


def main() -> None:
    adjacency = build_graph()
    assert len(adjacency) == 42
    assert sum(row.bit_count() for row in adjacency) // 2 == 378

    # Independent exhaustive confirmation that no set of order at most five
    # disconnects the graph.
    checked = 0
    for order in range(6):
        for deleted_tuple in combinations(VERTICES, order):
            assert connected_after(adjacency, mask(deleted_tuple))
            checked += 1
    assert not connected_after(adjacency, mask(S))

    assert component(adjacency, A) and component(adjacency, B)
    s_mask = mask(S)
    for shore in (A, B):
        neighbourhood = 0
        shore_mask = mask(shore)
        for v in shore:
            neighbourhood |= adjacency[v]
        neighbourhood &= ~shore_mask
        assert neighbourhood == s_mask

    quotient, a, quotient_blocks = contract_a(adjacency)
    assert len(quotient) == 31
    for i, s in enumerate(S):
        expected = (1 << a) | mask(quotient_blocks[i])
        assert quotient[s] == expected
        deleted = expected
        assert deleted.bit_count() == 5
        assert not connected_after(quotient, deleted)

    # The first seven vertices of B induce a target-rich K_7 subgraph.
    k7 = B[:7]
    assert all(adjacency[u] & (1 << v) for u, v in combinations(k7, 2))

    print("GREEN full-component contraction connectivity barrier")
    print(f"G: n=42 m=378 kappa=6 deletion_sets_checked={checked}")
    print("G-S: two components A(12), B(24), both full to S")
    print("G/A: n=31, each {a} union B_i is a five-cut isolating s_i")
    print("target_rich: B contains K_24 and hence K_7")


if __name__ == "__main__":
    main()
