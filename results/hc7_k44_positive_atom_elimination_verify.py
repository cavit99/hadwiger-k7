#!/usr/bin/env python3
"""Exact verifier for the seven-portal exterior-triangle profile theorem.

The literal core is K_{4,4} on vertices 0,...,7, with shores 0,...,3
and 4,...,7.  Vertices 8,9,10 form an exterior triangle.  For q=1,2,3:

* Q is a q-subset of the core;
* every member of Q is adjacent to at least two triangle vertices; and
* seven minus q other core vertices are split into nonempty groups of
  sizes 1, 1, and 5-q, one group adjacent to each triangle vertex.

Extra incidences are harmless, so these are the edge-minimal profiles.  The
script quotients them by Aut(K_{4,4}) x S_3 and checks a spanning K_7^- minor
model for every orbit representative.  The search is exact: all 63,987 set
partitions of eleven vertices into seven nonempty bags are considered in a
fixed restricted-growth order.

The same search also classifies the three symmetry orbits of disjoint
distinguished 5/1/1 portal profiles used for the singleton residue, and
checks all ten one-edge completions of its unique negative orbit.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from functools import reduce


EXPECTED_DIGEST = "48afac546bfa7bb92768b77581a774eeb735faf477a870886ea03f02b3a2c3f5"
EXPECTED_RAW = {1: 20_160, 2: 161_280, 3: 645_120}
EXPECTED_UNORDERED = {1: 3_360, 2: 26_880, 3: 107_520}
EXPECTED_ORBITS = {1: 20, 2: 77, 3: 198}
EXPECTED_SINGLETON_SURVIVOR = (55, 8, 64)
EXPECTED_SINGLETON_DIGEST = "a0812a66b38384445f877fa4cac909b4bea11a13d36364643cf9e1100ae2c6e8"
EXPECTED_ADDITION_DIGEST = "ce2f0641c454480ccd151d3d4679cc320b7a15abfd7a559622273240893e8565"


def automorphisms() -> tuple[tuple[int, ...], ...]:
    maps = set()
    for left in itertools.permutations(range(4)):
        for right0 in itertools.permutations(range(4)):
            right = tuple(4 + x for x in right0)
            maps.add(left + right)
            maps.add(right + left)
    result = tuple(sorted(maps))
    assert len(result) == 1_152
    return result


AUTOMORPHISMS = automorphisms()


def transform_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    while mask:
        bit = mask & -mask
        mask ^= bit
        result |= 1 << permutation[bit.bit_length() - 1]
    return result


def canonical(profile: tuple[int, int, int]) -> tuple[int, int, int]:
    return min(
        tuple(sorted(transform_mask(mask, permutation) for mask in profile))
        for permutation in AUTOMORPHISMS
    )


def canonical_with_distinguished_first(
    profile: tuple[int, int, int]
) -> tuple[int, int, int]:
    first, second, third = profile
    return min(
        (
            transform_mask(first, permutation),
            *sorted(
                (transform_mask(second, permutation),
                 transform_mask(third, permutation))
            ),
        )
        for permutation in AUTOMORPHISMS
    )


def orbit_representatives(
    profiles: set[tuple[int, int, int]], *, distinguished_first: bool = False
) -> tuple[tuple[int, int, int], ...]:
    """Quotient an invariant profile set without canonicalising every row."""
    remaining = set(profiles)
    representatives = []
    while remaining:
        seed = min(remaining)
        if distinguished_first:
            first, second, third = seed
            orbit = {
                (
                    transform_mask(first, permutation),
                    *sorted((
                        transform_mask(second, permutation),
                        transform_mask(third, permutation),
                    )),
                )
                for permutation in AUTOMORPHISMS
            }
        else:
            orbit = {
                tuple(sorted(
                    transform_mask(mask, permutation) for mask in seed
                ))
                for permutation in AUTOMORPHISMS
            }
        representative = min(orbit)
        assert representative in remaining
        representatives.append(representative)
        remaining.difference_update(orbit)
    return tuple(sorted(representatives))


def ordered_groups(
    elements: tuple[int, ...], sizes: tuple[int, int, int]
):
    first_size, second_size, _ = sizes
    for first in itertools.combinations(elements, first_size):
        first_set = set(first)
        remainder = tuple(x for x in elements if x not in first_set)
        for second in itertools.combinations(remainder, second_size):
            second_set = set(second)
            third = tuple(x for x in remainder if x not in second_set)
            yield first, second, third


def profiles(q: int) -> tuple[int, set[tuple[int, int, int]]]:
    """Return the labelled count and the profiles after quotienting S_3."""
    labelled_count = 0
    unordered = set()
    for common in itertools.combinations(range(8), q):
        common_set = set(common)
        outside = tuple(x for x in range(8) if x not in common_set)
        for omitted in outside:
            represented = tuple(x for x in outside if x != omitted)
            for sizes in sorted(set(itertools.permutations((1, 1, 5 - q)))):
                for groups in ordered_groups(represented, sizes):
                    base = tuple(sum(1 << x for x in group) for group in groups)
                    for supports in itertools.product((3, 5, 6, 7), repeat=q):
                        row = list(base)
                        for label, support in zip(common, supports):
                            for bag in range(3):
                                if support >> bag & 1:
                                    row[bag] |= 1 << label
                        labelled_count += 1
                        unordered.add(tuple(sorted(row)))
    return labelled_count, unordered


def restricted_growth_partitions() -> tuple[tuple[int, ...], ...]:
    result: list[tuple[int, ...]] = []

    def extend(vertex: int, bags: list[int]) -> None:
        if vertex == 11:
            if len(bags) == 7:
                result.append(tuple(bags))
            return
        if len(bags) > 7 or len(bags) + 11 - vertex < 7:
            return
        bit = 1 << vertex
        for index in range(len(bags)):
            bags[index] |= bit
            extend(vertex + 1, bags)
            bags[index] ^= bit
        if len(bags) < 7:
            bags.append(bit)
            extend(vertex + 1, bags)
            bags.pop()

    extend(1, [1])
    assert len(result) == 63_987
    return tuple(result)


PARTITIONS = restricted_growth_partitions()


def graph_for(profile: tuple[int, int, int]) -> tuple[int, ...]:
    graph = [0] * 11

    def add(left: int, right: int) -> None:
        graph[left] |= 1 << right
        graph[right] |= 1 << left

    for left in range(4):
        for right in range(4, 8):
            add(left, right)
    for left, right in itertools.combinations(range(8, 11), 2):
        add(left, right)
    for exterior, neighborhood in zip(range(8, 11), profile):
        for core in range(8):
            if neighborhood >> core & 1:
                add(exterior, core)
    return tuple(graph)


def mask_tables(graph: tuple[int, ...]) -> tuple[list[bool], list[int]]:
    connected = [False] * (1 << 11)
    neighborhood = [0] * (1 << 11)
    for mask in range(1, 1 << 11):
        bit = mask & -mask
        rest = mask ^ bit
        neighborhood[mask] = neighborhood[rest] | graph[bit.bit_length() - 1]

        seen = bit
        todo = bit
        while todo:
            current = todo & -todo
            todo ^= current
            new = graph[current.bit_length() - 1] & mask & ~seen
            seen |= new
            todo |= new
        connected[mask] = seen == mask
    return connected, neighborhood


def first_model(profile: tuple[int, int, int]) -> tuple[int, ...] | None:
    connected, neighborhood = mask_tables(graph_for(profile))
    for bags in PARTITIONS:
        if not all(connected[bag] for bag in bags):
            continue
        missing = 0
        for left, right in itertools.combinations(range(7), 2):
            if not neighborhood[bags[left]] & bags[right]:
                missing += 1
                if missing == 2:
                    break
        if missing <= 1:
            return bags
    return None


def validate_model(profile: tuple[int, int, int], bags: tuple[int, ...]) -> None:
    assert len(bags) == 7
    assert all(bags)
    assert all(not left & right for left, right in itertools.combinations(bags, 2))
    assert reduce(int.__or__, bags) == (1 << 11) - 1
    connected, neighborhood = mask_tables(graph_for(profile))
    assert all(connected[bag] for bag in bags)
    contacts = sum(
        bool(neighborhood[bags[left]] & bags[right])
        for left, right in itertools.combinations(range(7), 2)
    )
    assert contacts >= 20


def singleton_atom_profiles() -> tuple[
    tuple[tuple[int, int, int], ...],
    dict[tuple[int, int, int], tuple[int, ...] | None],
]:
    """Classify the disjoint 5/1/1 profiles with the 5-set distinguished."""
    unordered = set()
    for large in itertools.combinations(range(8), 5):
        large_mask = sum(1 << x for x in large)
        remainder = tuple(x for x in range(8) if x not in large)
        for first, second in itertools.permutations(remainder, 2):
            unordered.add((large_mask, *sorted((1 << first, 1 << second))))
    assert len(unordered) == 168

    representatives = orbit_representatives(unordered, distinguished_first=True)
    assert len(representatives) == 3
    models = {profile: first_model(profile) for profile in representatives}
    assert sum(model is not None for model in models.values()) == 2
    assert tuple(profile for profile, model in models.items() if model is None) == (
        EXPECTED_SINGLETON_SURVIVOR,
    )
    for profile, model in models.items():
        if model is not None:
            validate_model(profile, model)
    return representatives, models


def main() -> None:
    records = []
    print("partitions", len(PARTITIONS))
    for q in (1, 2, 3):
        labelled_count, unordered = profiles(q)
        representatives = orbit_representatives(unordered)
        assert labelled_count == EXPECTED_RAW[q]
        assert len(unordered) == EXPECTED_UNORDERED[q]
        assert len(representatives) == EXPECTED_ORBITS[q]

        for profile in representatives:
            model = first_model(profile)
            assert model is not None
            validate_model(profile, model)
            records.append((q, profile, model))
        print("q", q, "positive", len(representatives))

    payload = json.dumps(records, separators=(",", ":")).encode()
    digest = hashlib.sha256(payload).hexdigest()
    assert digest == EXPECTED_DIGEST
    print("digest", digest)

    singleton_representatives, singleton_models = singleton_atom_profiles()
    print("singleton_5_1_1_orbits", len(singleton_representatives))
    print("singleton_5_1_1_positive", sum(
        model is not None for model in singleton_models.values()
    ))
    print("singleton_5_1_1_survivor", EXPECTED_SINGLETON_SURVIVOR)
    singleton_digest = hashlib.sha256(json.dumps(
        [(profile, singleton_models[profile]) for profile in singleton_representatives],
        separators=(",", ":"),
    ).encode()).hexdigest()
    assert singleton_digest == EXPECTED_SINGLETON_DIGEST
    print("singleton_5_1_1_digest", singleton_digest)

    large, first, second = EXPECTED_SINGLETON_SURVIVOR
    addition_records = []
    for small_index in (1, 2):
        for portal in range(8):
            if not large >> portal & 1:
                continue
            row = [large, first, second]
            row[small_index] |= 1 << portal
            profile = tuple(row)
            model = first_model(profile)
            assert model is not None
            validate_model(profile, model)
            addition_records.append((small_index, portal, profile, model))
    assert len(addition_records) == 10
    addition_digest = hashlib.sha256(
        json.dumps(addition_records, separators=(",", ":")).encode()
    ).hexdigest()
    assert addition_digest == EXPECTED_ADDITION_DIGEST
    print("singleton_big_to_small_additions", len(addition_records))
    print("singleton_addition_digest", addition_digest)

if __name__ == "__main__":
    main()
