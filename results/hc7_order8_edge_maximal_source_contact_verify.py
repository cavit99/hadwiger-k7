#!/usr/bin/env python3
"""Verify the conditional edge-maximal source-contact census.

The labelled vertices are ``t,c0,c1,c2,c3,c4,q``.  The five edges from
``t`` to the sources ``c0,...,c4`` are required, while the other sixteen
edges vary.  A retained graph ``J`` satisfies

* ``J`` has no ``K5`` minor;
* ``d_J(c0) <= 3``; and
* adding any missing edge creates a ``K5`` minor.

For every retained graph the program checks that ``J-c0`` has a spanning
four-bag ``K4``-minor model and that ``c0`` is adjacent to exactly three of
its bags.  This is a finite conditional statement: the program does not
prove that a host column system can be made abstractly edge-maximal.

Expected output::

    labelled_graphs 65536
    edge_maximal_survivors 562
    unlabelled_types 6
    type_counts 007fff:10 00efff:192 01d7ff:120 01deff:84 05cdff:144 05defb:12
    spanning_k4_failures 0
    PASS order8_edge_maximal_source_contact
"""

from __future__ import annotations

import itertools


VERTICES = tuple(range(7))
T, C0, C1, C2, C3, C4, Q = VERTICES
SOURCES = (C0, C1, C2, C3, C4)
EDGES = tuple(itertools.combinations(VERTICES, 2))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
FIXED_EDGES = tuple((T, source) for source in SOURCES)
VARIABLE_EDGES = tuple(edge for edge in EDGES if edge not in FIXED_EDGES)


def edge_bit(u: int, v: int) -> int:
    return 1 << EDGE_INDEX[tuple(sorted((u, v)))]


FIXED_MASK = sum(edge_bit(*edge) for edge in FIXED_EDGES)
VARIABLE_BITS = tuple(edge_bit(*edge) for edge in VARIABLE_EDGES)


def graph_mask(variable_mask: int) -> int:
    mask = FIXED_MASK
    for index, bit in enumerate(VARIABLE_BITS):
        if variable_mask >> index & 1:
            mask |= bit
    return mask


def neighbourhoods(mask: int) -> tuple[int, ...]:
    answer = [0] * len(VERTICES)
    for index, (u, v) in enumerate(EDGES):
        if mask >> index & 1:
            answer[u] |= 1 << v
            answer[v] |= 1 << u
    return tuple(answer)


def set_partitions(vertices: tuple[int, ...], count: int) -> tuple[tuple[int, ...], ...]:
    """Return each unordered partition as a tuple of nonempty bit masks."""
    blocks: list[int] = []
    answer: list[tuple[int, ...]] = []

    def visit(index: int) -> None:
        if index == len(vertices):
            if len(blocks) == count:
                answer.append(tuple(blocks))
            return
        if len(blocks) + len(vertices) - index < count:
            return
        bit = 1 << vertices[index]
        for block_index in range(len(blocks)):
            blocks[block_index] |= bit
            visit(index + 1)
            blocks[block_index] ^= bit
        if len(blocks) < count:
            blocks.append(bit)
            visit(index + 1)
            blocks.pop()

    visit(0)
    return tuple(answer)


def k5_models() -> tuple[tuple[int, ...], ...]:
    answer = []
    for size in (5, 6, 7):
        for subset in itertools.combinations(VERTICES, size):
            answer.extend(set_partitions(subset, 5))
    return tuple(answer)


K5_MODELS = k5_models()
SPANNING_K4_MODELS = set_partitions((T, C1, C2, C3, C4, Q), 4)
assert len(K5_MODELS) == 266
assert len(SPANNING_K4_MODELS) == 65


def model_tables(mask: int) -> tuple[tuple[int, ...], tuple[bool, ...]]:
    adjacent = neighbourhoods(mask)
    union = [0] * (1 << len(VERTICES))
    connected = [False] * (1 << len(VERTICES))
    for block in range(1, 1 << len(VERTICES)):
        bit = block & -block
        union[block] = union[block ^ bit] | adjacent[bit.bit_length() - 1]
        reached = bit
        while True:
            enlarged = reached
            remainder = reached
            while remainder:
                next_bit = remainder & -remainder
                enlarged |= adjacent[next_bit.bit_length() - 1] & block
                remainder ^= next_bit
            if enlarged == reached:
                connected[block] = reached == block
                break
            reached = enlarged
    return tuple(union), tuple(connected)


def is_model(
    bags: tuple[int, ...], union: tuple[int, ...], connected: tuple[bool, ...]
) -> bool:
    return all(connected[bag] for bag in bags) and all(
        union[left] & right for left, right in itertools.combinations(bags, 2)
    )


def has_k5_minor(mask: int) -> bool:
    union, connected = model_tables(mask)
    return any(is_model(bags, union, connected) for bags in K5_MODELS)


def has_required_spanning_k4(mask: int) -> bool:
    adjacent = neighbourhoods(mask)
    union, connected = model_tables(mask)
    return any(
        is_model(bags, union, connected)
        and sum(bool(adjacent[C0] & bag) for bag in bags) == 3
        for bags in SPANNING_K4_MODELS
    )


def permuted_mask(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(
        edge_bit(permutation[u], permutation[v])
        for index, (u, v) in enumerate(EDGES)
        if mask >> index & 1
    )


def canonical_unlabelled(mask: int) -> int:
    return min(
        permuted_mask(mask, permutation)
        for permutation in itertools.permutations(VERTICES)
    )


EXPECTED_TYPES = {
    0x007FFF: 10,
    0x00EFFF: 192,
    0x01D7FF: 120,
    0x01DEFF: 84,
    0x05CDFF: 144,
    0x05DEFB: 12,
}


def main() -> None:
    graphs = tuple(graph_mask(mask) for mask in range(1 << len(VARIABLE_EDGES)))
    has_k5 = tuple(has_k5_minor(mask) for mask in graphs)

    survivors = []
    for variable_mask, mask in enumerate(graphs):
        if has_k5[variable_mask] or neighbourhoods(mask)[C0].bit_count() > 3:
            continue
        if all(
            has_k5[variable_mask | (1 << index)]
            for index in range(len(VARIABLE_EDGES))
            if not variable_mask >> index & 1
        ):
            survivors.append(mask)

    failures = sum(not has_required_spanning_k4(mask) for mask in survivors)
    type_counts: dict[int, int] = {}
    for mask in survivors:
        canonical = canonical_unlabelled(mask)
        type_counts[canonical] = type_counts.get(canonical, 0) + 1

    assert len(graphs) == 65_536
    assert len(survivors) == 562
    assert all(neighbourhoods(mask)[C0].bit_count() == 3 for mask in survivors)
    assert all(mask.bit_count() == 15 for mask in survivors)
    assert type_counts == EXPECTED_TYPES
    assert failures == 0

    encoded_types = " ".join(
        f"{code:06x}:{count}" for code, count in sorted(type_counts.items())
    )
    print(f"labelled_graphs {len(graphs)}")
    print(f"edge_maximal_survivors {len(survivors)}")
    print(f"unlabelled_types {len(type_counts)}")
    print(f"type_counts {encoded_types}")
    print(f"spanning_k4_failures {failures}")
    print("PASS order8_edge_maximal_source_contact")


if __name__ == "__main__":
    main()
