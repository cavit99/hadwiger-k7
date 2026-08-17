#!/usr/bin/env python3
"""Falsify the independent-root K4-to-K5-minus augmentation conjecture.

The exact mode enumerates every graph with five prescribed independent
roots and three internal vertices.  Random mode samples larger internal
graphs and attachment systems.  This is evidence only, not a proof.
"""

from __future__ import annotations

import argparse
import itertools
import random


def adjacent(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    vertices = left
    while vertices:
        bit = vertices & -vertices
        vertex = bit.bit_length() - 1
        if adjacency[vertex] & right:
            return True
        vertices ^= bit
    return False


def connected(adjacency: tuple[int, ...], vertices: int) -> bool:
    if not vertices:
        return False
    reached = vertices & -vertices
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        vertex = bit.bit_length() - 1
        frontier ^= bit
        new = adjacency[vertex] & vertices & ~reached
        reached |= new
        frontier |= new
    return reached == vertices


def relative_five(adjacency: tuple[int, ...], internal_mask: int) -> bool:
    subset = internal_mask
    while subset:
        neighbourhood = 0
        vertices = subset
        while vertices:
            bit = vertices & -vertices
            vertex = bit.bit_length() - 1
            neighbourhood |= adjacency[vertex]
            vertices ^= bit
        if (neighbourhood & ~subset).bit_count() < 5:
            return False
        subset = (subset - 1) & internal_mask
    return True


def rooted_model(
    adjacency: tuple[int, ...], roots: tuple[int, ...], allowed_internal: tuple[int, ...],
    missing_budget: int,
) -> bool:
    """Exact rooted clique/near-clique test by allocation of every extra."""
    bag_count = len(roots)
    for allocation in itertools.product(range(bag_count + 1), repeat=len(allowed_internal)):
        bags = [1 << root for root in roots]
        for vertex, owner in zip(allowed_internal, allocation, strict=True):
            if owner:
                bags[owner - 1] |= 1 << vertex
        if not all(connected(adjacency, bag) for bag in bags):
            continue
        missing = sum(
            not adjacent(adjacency, bags[left], bags[right])
            for left, right in itertools.combinations(range(bag_count), 2)
        )
        if missing <= missing_budget:
            return True
    return False


def build(order: int, internal_edges: int, labels: tuple[int, ...]) -> tuple[int, ...]:
    total = 5 + order
    adjacency = [0] * total
    edge_index = 0
    for left, right in itertools.combinations(range(order), 2):
        if internal_edges & (1 << edge_index):
            u, v = 5 + left, 5 + right
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
        edge_index += 1
    for offset, label in enumerate(labels):
        vertex = 5 + offset
        for root in range(5):
            if label & (1 << root):
                adjacency[vertex] |= 1 << root
                adjacency[root] |= 1 << vertex
    return tuple(adjacency)


def inspect(order: int, adjacency: tuple[int, ...]) -> tuple[bool, bool, bool]:
    internal = tuple(range(5, 5 + order))
    internal_mask = sum(1 << vertex for vertex in internal)
    if not relative_five(adjacency, internal_mask):
        return False, False, False
    near_five = rooted_model(adjacency, tuple(range(5)), internal, 1)
    if near_five:
        return True, False, True
    # The omitted fifth root is deleted, rather than being available as an
    # unrooted branch-set vertex.  This matches a punctured four-root model.
    rooted_four = any(
        rooted_model(
            adjacency,
            tuple(root for root in range(5) if root != omitted),
            internal,
            0,
        )
        for omitted in range(5)
    )
    return True, rooted_four, False


def graph6_like(order: int, internal_edges: int, labels: tuple[int, ...]) -> str:
    return f"order={order} internal_edges={internal_edges:#x} labels={labels}"


def exact_three() -> None:
    order = 3
    relative = rooted_four = avoiding = 0
    best = None
    for internal_edges in range(1 << 3):
        for packed in range(1 << 15):
            labels = tuple((packed >> (5 * index)) & 31 for index in range(order))
            adjacency = build(order, internal_edges, labels)
            is_relative, has_four, has_five = inspect(order, adjacency)
            if not is_relative:
                continue
            relative += 1
            if not has_five:
                avoiding += 1
            if has_four:
                rooted_four += 1
                incident = internal_edges.bit_count() + sum(label.bit_count() for label in labels)
                record = (incident - 3 * order, internal_edges, labels)
                if best is None or record > best:
                    best = record
                raise AssertionError(
                    "COUNTEREXAMPLE " + graph6_like(order, internal_edges, labels)
                )
    print(
        "GREEN exact independent-root augmentation order=3 "
        f"relative={relative} rooted-model-free={avoiding} "
        f"rooted-K4/no-K5minus={rooted_four} best={best}"
    )


def random_probe(order: int, trials: int, seed: int) -> None:
    rng = random.Random(seed)
    relative = avoiding = rooted_four = 0
    for trial in range(trials):
        edge_mask = 0
        for index in range(order * (order - 1) // 2):
            if rng.random() < rng.uniform(0.25, 0.85):
                edge_mask |= 1 << index
        labels = tuple(
            sum(1 << root for root in range(5) if rng.random() < rng.uniform(0.25, 0.9))
            for _ in range(order)
        )
        adjacency = build(order, edge_mask, labels)
        is_relative, has_four, has_five = inspect(order, adjacency)
        if not is_relative:
            continue
        relative += 1
        if not has_five:
            avoiding += 1
        if has_four:
            rooted_four += 1
            raise AssertionError(
                f"COUNTEREXAMPLE trial={trial} "
                + graph6_like(order, edge_mask, labels)
            )
    print(
        "GREEN random independent-root augmentation "
        f"order={order} trials={trials} seed={seed} relative={relative} "
        f"rooted-model-free={avoiding} rooted-K4/no-K5minus={rooted_four}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("exact-three", "random"), required=True)
    parser.add_argument("--order", type=int, default=5)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260817)
    args = parser.parse_args()
    if args.mode == "exact-three":
        exact_three()
    else:
        if not 3 <= args.order <= 7:
            parser.error("random order must lie between 3 and 7")
        random_probe(args.order, args.trials, args.seed)


if __name__ == "__main__":
    main()
