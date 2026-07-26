#!/usr/bin/env python3
"""Verify the six-vertex source-rooted K4 lemma without dependencies.

Vertices 0,...,4 are the marked sources and vertex 5 is auxiliary.  The
program exhausts all 2^15 graphs, checks the degree hypotheses, and searches
all four-bag minor models whose bags each contain a source.  It also reduces
the edge-minimal graphs under permutations of the five sources and checks an
explicit branch-set certificate for every resulting core.
"""

from __future__ import annotations

import hashlib
import itertools
import json


VERTICES = tuple(range(6))
SOURCES = frozenset(range(5))
AUXILIARY = 5
EDGES = tuple(itertools.combinations(VERTICES, 2))
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}


def edge_mask(edges: tuple[tuple[int, int], ...]) -> int:
    return sum(1 << EDGE_INDEX[tuple(sorted(edge))] for edge in edges)


def degree(mask: int, vertex: int) -> int:
    return sum(
        1
        for index, edge in enumerate(EDGES)
        if mask >> index & 1 and vertex in edge
    )


def eligible(mask: int) -> bool:
    return all(degree(mask, source) >= 3 for source in SOURCES) and degree(
        mask, AUXILIARY
    ) <= 3


def connected(mask: int, bag: frozenset[int]) -> bool:
    reached = {next(iter(bag))}
    while True:
        enlarged = reached | {
            v
            for index, (u, v) in enumerate(EDGES)
            if mask >> index & 1 and u in reached and v in bag
        } | {
            u
            for index, (u, v) in enumerate(EDGES)
            if mask >> index & 1 and v in reached and u in bag
        }
        if enlarged == reached:
            return len(reached) == len(bag)
        reached = enlarged


def adjacent(mask: int, left: frozenset[int], right: frozenset[int]) -> bool:
    return any(
        mask >> EDGE_INDEX[tuple(sorted((u, v)))] & 1
        for u in left
        for v in right
    )


def candidate_models() -> tuple[tuple[frozenset[int], ...], ...]:
    """Return unlabelled four-bag systems; unused vertices are allowed."""
    answers: set[tuple[frozenset[int], ...]] = set()
    for assignment in itertools.product(range(-1, 4), repeat=6):
        if {label for label in assignment if label >= 0} != set(range(4)):
            continue
        first = tuple(assignment.index(label) for label in range(4))
        if first != tuple(sorted(first)):
            continue
        bags = tuple(
            frozenset(v for v, label in enumerate(assignment) if label == i)
            for i in range(4)
        )
        if all(bag & SOURCES for bag in bags):
            answers.add(bags)
    return tuple(sorted(answers, key=lambda bags: tuple(map(tuple, bags))))


MODELS = candidate_models()


def is_model(mask: int, bags: tuple[frozenset[int], ...]) -> bool:
    return all(connected(mask, bag) for bag in bags) and all(
        adjacent(mask, left, right)
        for left, right in itertools.combinations(bags, 2)
    )


def has_rooted_k4(mask: int) -> bool:
    return any(is_model(mask, bags) for bags in MODELS)


def canonical_edges(mask: int) -> tuple[tuple[int, int], ...]:
    answers = []
    for permutation in itertools.permutations(range(5)):
        relabel = dict(enumerate(permutation))
        relabel[AUXILIARY] = AUXILIARY
        answers.append(
            tuple(
                sorted(
                    tuple(sorted((relabel[u], relabel[v])))
                    for index, (u, v) in enumerate(EDGES)
                    if mask >> index & 1
                )
            )
        )
    return min(answers)


CORE_CERTIFICATES = (
    (
        ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 4), (3, 4)),
        ((0,), (1, 2), (3,), (4,)),
    ),
    (
        ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 4), (3, 5), (4, 5)),
        ((0,), (1, 2), (3, 5), (4,)),
    ),
    (
        ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)),
        ((0,), (1,), (2, 4), (3,)),
    ),
    (
        ((0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5), (3, 4), (3, 5), (4, 5)),
        ((0, 1), (2, 5), (3,), (4,)),
    ),
    (
        ((0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)),
        ((0, 1), (2, 5), (3,), (4,)),
    ),
)


def main() -> None:
    eligible_count = 0
    failures = 0
    minimal_masks = []

    for mask in range(1 << len(EDGES)):
        if not eligible(mask):
            continue
        eligible_count += 1
        if not has_rooted_k4(mask):
            failures += 1
        if all(
            not eligible(mask & ~(1 << index))
            for index in range(len(EDGES))
            if mask >> index & 1
        ):
            minimal_masks.append(mask)

    observed_cores = {canonical_edges(mask) for mask in minimal_masks}
    expected_cores = {edges for edges, _ in CORE_CERTIFICATES}
    assert observed_cores == expected_cores

    for edges, raw_bags in CORE_CERTIFICATES:
        mask = edge_mask(edges)
        bags = tuple(frozenset(bag) for bag in raw_bags)
        assert eligible(mask)
        assert all(bag & SOURCES for bag in bags)
        assert is_model(mask, bags)

    certificate_json = json.dumps(CORE_CERTIFICATES, separators=(",", ":"))
    certificate_sha256 = hashlib.sha256(certificate_json.encode()).hexdigest()

    print(f"eligible_graphs {eligible_count}")
    print(f"edge_minimal_graphs {len(minimal_masks)}")
    print(f"rooted_core_orbits {len(observed_cores)}")
    print(f"rooted_core_certificate_sha256 {certificate_sha256}")
    print(f"failures {failures}")
    assert eligible_count == 1656
    assert len(minimal_masks) == 175
    assert len(observed_cores) == 5
    assert failures == 0
    print("PASS six_vertex_source_rooted_k4")


if __name__ == "__main__":
    main()
