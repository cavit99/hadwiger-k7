#!/usr/bin/env python3
"""Verify the finite quotients in the returned type-VII elimination.

The six boundary vertices are 0,...,5.  A pattern entry is 0 when only
the first end of a K2 component sees that boundary vertex, 1 when only
the second end sees it, and 2 when both ends see it.

The target oracle is an exact deletion/contraction search.  It also returns
and independently validates a branch-set certificate for every positive
profile.  Only the Python standard library is used.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json


BOUNDARY_EDGES = frozenset(
    tuple(sorted(map(int, token)))
    for token in "01 02 03 14 24 35 45".split()
)
PATTERNS = tuple(product(range(3), repeat=6))


def minimum_degree_feasible(pattern: tuple[int, ...]) -> bool:
    """Each end has its K2 mate and therefore needs five boundary neighbours."""
    first_degree = sum(entry in (0, 2) for entry in pattern)
    second_degree = sum(entry in (1, 2) for entry in pattern)
    return first_degree >= 5 and second_degree >= 5


def quotient(patterns: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    """Build the exact quotient, contracting every unlisted full component."""
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
        component_image = next_vertex
        next_vertex += 1
        for root in range(6):
            edges.add((root, component_image))

    adjacency = [0] * next_vertex
    for left, right in edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    return tuple(adjacency)


def touches(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    while left:
        bit = left & -left
        left ^= bit
        if adjacency[bit.bit_length() - 1] & right:
            return True
    return False


def connected(adjacency: tuple[int, ...], vertices: int) -> bool:
    if not vertices:
        return False
    reached = 0
    frontier = vertices & -vertices
    while frontier:
        reached |= frontier
        neighbours = 0
        scan = frontier
        while scan:
            bit = scan & -scan
            scan ^= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        frontier = neighbours & vertices & ~reached
    return reached == vertices


def validate_model(adjacency: tuple[int, ...], bags: tuple[int, ...]) -> None:
    if len(bags) != 7:
        raise RuntimeError(f"model has {len(bags)} bags")
    used = 0
    for bag in bags:
        if used & bag:
            raise RuntimeError("model bags overlap")
        used |= bag
        if not connected(adjacency, bag):
            raise RuntimeError(f"disconnected model bag {bag}")
    contacts = sum(
        touches(adjacency, left, right) for left, right in combinations(bags, 2)
    )
    if contacts < 20:
        raise RuntimeError(f"model has only {contacts} bag contacts")


def target_model(adjacency: tuple[int, ...]) -> tuple[int, ...] | None:
    """Return an exact K7-minus branch-set model, or None if none exists."""

    @lru_cache(maxsize=None)
    def search(bags: tuple[int, ...]) -> tuple[int, ...] | None:
        if len(bags) == 7:
            contacts = sum(
                touches(adjacency, left, right)
                for left, right in combinations(bags, 2)
            )
            return bags if contacts >= 20 else None
        if len(bags) < 7:
            return None

        for left_index, right_index in combinations(range(len(bags)), 2):
            if not touches(adjacency, bags[left_index], bags[right_index]):
                continue
            merged = [
                bag
                for index, bag in enumerate(bags)
                if index not in (left_index, right_index)
            ]
            merged.append(bags[left_index] | bags[right_index])
            model = search(tuple(sorted(merged)))
            if model is not None:
                return model

        for deleted_index in range(len(bags)):
            model = search(bags[:deleted_index] + bags[deleted_index + 1 :])
            if model is not None:
                return model
        return None

    model = search(tuple(1 << vertex for vertex in range(len(adjacency))))
    if model is not None:
        validate_model(adjacency, model)
    return model


def serialise_model(model: tuple[int, ...]) -> list[list[int]]:
    return [
        [vertex for vertex in range(64) if bag & (1 << vertex)]
        for bag in model
    ]


def profile_key(case: str, patterns: tuple[tuple[int, ...], ...]) -> str:
    encoded = "/".join("".join(map(str, pattern)) for pattern in patterns)
    return f"{case}:{encoded}"


def main() -> None:
    complete_seven = tuple((1 << 7) - 1 - (1 << vertex) for vertex in range(7))
    if target_model(complete_seven) is None:
        raise RuntimeError("positive control K7 was rejected")

    negative_edges = set(combinations(range(7), 2)) - {(0, 1), (0, 2)}
    negative_adjacency = [0] * 7
    for left, right in negative_edges:
        negative_adjacency[left] |= 1 << right
        negative_adjacency[right] |= 1 << left
    if target_model(tuple(negative_adjacency)) is not None:
        raise RuntimeError("negative control K7 with two incident edges absent")

    same = tuple(
        pattern
        for pattern in PATTERNS
        if pattern[1] == pattern[2] == 2 and minimum_degree_feasible(pattern)
    )
    first_only = tuple(
        pattern
        for pattern in PATTERNS
        if pattern[1] == 2
        and pattern[2] != 2
        and minimum_degree_feasible(pattern)
    )
    second_only = tuple(
        pattern
        for pattern in PATTERNS
        if pattern[2] == 2
        and pattern[1] != 2
        and minimum_degree_feasible(pattern)
    )

    if (len(same), len(first_only), len(second_only)) != (21, 10, 10):
        raise RuntimeError(
            "unexpected feasible pattern counts "
            f"{len(same)}, {len(first_only)}, {len(second_only)}"
        )

    certificates: dict[str, list[list[int]]] = {}
    for pattern in same:
        patterns = (pattern,)
        model = target_model(quotient(patterns))
        if model is None:
            raise RuntimeError(f"same-component profile lacks target: {pattern}")
        certificates[profile_key("same", patterns)] = serialise_model(model)

    for first in first_only:
        for second in second_only:
            patterns = (first, second)
            model = target_model(quotient(patterns))
            if model is None:
                raise RuntimeError(f"split-component profile lacks target: {patterns}")
            certificates[profile_key("split", patterns)] = serialise_model(model)

    if len(certificates) != 121:
        raise RuntimeError(f"expected 121 certificates, got {len(certificates)}")

    payload = "\n".join(
        json.dumps((key, certificates[key]), separators=(",", ":"))
        for key in sorted(certificates)
    )
    digest = sha256(payload.encode()).hexdigest()

    print("GREEN returned type-VII quotient elimination")
    print("same_component_feasible_profiles=21")
    print("split_component_first_profiles=10")
    print("split_component_second_profiles=10")
    print("split_component_profile_pairs=100")
    print("target_certificates=121")
    print(f"certificate_digest={digest}")


if __name__ == "__main__":
    main()
