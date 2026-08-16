#!/usr/bin/env python3
"""Verify the finite bridge-split lemma for the seven both-full boundaries.

For each promoted boundary type and each unordered pair of missed boundary
vertices, build the twelve-object quotient from Theorem 3.1 of the adjacent
note.  An exact deletion/contraction search returns seven connected bags
with at least twenty of their twenty-one pairwise adjacencies.

The script uses only the Python standard library.  It does not verify the
unbounded lift from a disconnected remote-edge shore; that lift is proved
in the adjacent note.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")

import hashlib
import itertools
from functools import lru_cache


ORDER = 8
QUOTIENT_ORDER = 12
BOUNDARY_TYPES = (
    "GCOcaO",
    "GCOcbO",
    "GCOcbW",
    "GCOe`W",
    "GCOebW",
    "GCQQV?",
    "GCQR@O",
)
EXPECTED_BOUNDARY_DIGEST = (
    "bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0"
)
EXPECTED_CERTIFICATE_DIGEST = (
    "311f08b508413fdc416b5af98e20abe0c45b86dafe890c8c88402b73e1565c8c"
)


def normalized_edge(left: int, right: int) -> tuple[int, int]:
    assert left != right
    return (left, right) if left < right else (right, left)


def decode_graph6(text: str) -> set[tuple[int, int]]:
    """Decode a short graph6 string of order eight."""
    assert text and ord(text[0]) - 63 == ORDER
    bits: list[int] = []
    for character in text[1:]:
        value = ord(character) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))

    answer: set[tuple[int, int]] = set()
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                answer.add((left, right))
            position += 1
    return answer


def bridge_quotient(
    code: str,
    missed_by_left: int,
    missed_by_right: int,
) -> frozenset[tuple[int, int]]:
    """Return X plus two full and two one-miss outside vertices."""
    edges = decode_graph6(code)
    centre, full, left, right = 8, 9, 10, 11
    for boundary in range(ORDER):
        edges.add(normalized_edge(centre, boundary))
        edges.add(normalized_edge(full, boundary))
        if boundary != missed_by_left:
            edges.add(normalized_edge(left, boundary))
        if boundary != missed_by_right:
            edges.add(normalized_edge(right, boundary))
    edges.add((left, right))
    return frozenset(edges)


def bags_touch(
    left: frozenset[int],
    right: frozenset[int],
    edges: frozenset[tuple[int, int]],
) -> bool:
    return any(
        normalized_edge(first, second) in edges
        for first in left
        for second in right
    )


def contact_count(
    bags: tuple[frozenset[int], ...],
    edges: frozenset[tuple[int, int]],
) -> int:
    return sum(
        bags_touch(left, right, edges)
        for left, right in itertools.combinations(bags, 2)
    )


def connected(
    vertices: frozenset[int],
    edges: frozenset[tuple[int, int]],
) -> bool:
    assert vertices
    reached = {min(vertices)}
    while True:
        enlarged = reached | {
            right
            for left, right in edges
            if left in reached and right in vertices
        } | {
            left
            for left, right in edges
            if right in reached and left in vertices
        }
        if enlarged == reached:
            return reached == set(vertices)
        reached = enlarged


def validate_certificate(
    bags: tuple[frozenset[int], ...],
    edges: frozenset[tuple[int, int]],
) -> None:
    assert len(bags) == 7
    assert all(bags)
    assert all(
        left.isdisjoint(right)
        for left, right in itertools.combinations(bags, 2)
    )
    assert all(connected(bag, edges) for bag in bags)
    assert contact_count(bags, edges) >= 20


def minor_certificate(
    edges: frozenset[tuple[int, int]],
) -> tuple[frozenset[int], ...] | None:
    """Exact K7-minus minor search by deletion and edge contraction."""

    @lru_cache(maxsize=None)
    def search(
        canonical_bags: tuple[tuple[int, ...], ...],
    ) -> tuple[frozenset[int], ...] | None:
        bags = tuple(frozenset(bag) for bag in canonical_bags)
        if len(bags) < 7:
            return None
        if len(bags) == 7:
            return bags if contact_count(bags, edges) >= 20 else None

        for first, second in itertools.combinations(range(len(bags)), 2):
            if not bags_touch(bags[first], bags[second], edges):
                continue
            merged = bags[first] | bags[second]
            next_bags = tuple(
                bag
                for index, bag in enumerate(bags)
                if index not in (first, second)
            ) + (merged,)
            key = tuple(sorted(tuple(sorted(bag)) for bag in next_bags))
            answer = search(key)
            if answer is not None:
                return answer

        for deleted in range(len(bags)):
            next_bags = tuple(
                bag for index, bag in enumerate(bags) if index != deleted
            )
            key = tuple(sorted(tuple(sorted(bag)) for bag in next_bags))
            answer = search(key)
            if answer is not None:
                return answer
        return None

    initial = tuple((vertex,) for vertex in range(QUOTIENT_ORDER))
    return search(initial)


def canonical_certificate(bags: tuple[frozenset[int], ...]) -> str:
    masks = sorted(sum(1 << vertex for vertex in bag) for bag in bags)
    return ",".join(map(str, masks))


def digest(lines: list[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(lines)) + "\n").encode()).hexdigest()


def main() -> None:
    boundary_digest = digest(list(BOUNDARY_TYPES))
    assert boundary_digest == EXPECTED_BOUNDARY_DIGEST

    records: list[str] = []
    cases = 0
    for code in BOUNDARY_TYPES:
        for missed_by_left in range(ORDER):
            for missed_by_right in range(missed_by_left, ORDER):
                edges = bridge_quotient(
                    code,
                    missed_by_left,
                    missed_by_right,
                )
                certificate = minor_certificate(edges)
                assert certificate is not None, (
                    code,
                    missed_by_left,
                    missed_by_right,
                )
                validate_certificate(certificate, edges)
                records.append(
                    f"{code} {missed_by_left} {missed_by_right} "
                    f"{canonical_certificate(certificate)}"
                )
                cases += 1

    assert cases == 7 * 36 == 252
    certificate_digest = digest(records)
    print(f"boundary_types={len(BOUNDARY_TYPES)} digest={boundary_digest}")
    print(f"bridge_split_cases={cases} terminal=252 survivors=0")
    print(f"certificate_digest={certificate_digest}")
    assert certificate_digest == EXPECTED_CERTIFICATE_DIGEST
    print("PASS remote two-component shore stability finite lemma")


if __name__ == "__main__":
    main()
