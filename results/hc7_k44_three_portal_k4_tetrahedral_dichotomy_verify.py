#!/usr/bin/env python3
"""Independent orbit audit for K4,4 plus an exterior K4 of 3-portals.

This does not import either primary census.  It independently enumerates
the core K3 models by 4^8 assignments, recovers the 1,170 restricted
failures, classifies them into twelve symmetry orbits, checks fixed K7^-
models for the nine positive orbits, and recognizes the three negative
orbits as the tetrahedral 4-set family.
"""

from __future__ import annotations

import hashlib
import itertools


POSITIVE_ROWS = {
    ((0, 1, 2), (0, 1, 3), (0, 1, 4), (2, 3, 4)): (
        (2, 3, 5, 6), (0, 7), (4, 11), (1,), (8,), (9,), (10,)
    ),
    ((0, 1, 2), (0, 1, 4), (0, 1, 5), (2, 4, 5)): (
        (0, 3, 6, 7), (2, 4), (5, 11), (1,), (8,), (9,), (10,)
    ),
    ((0, 1, 2), (0, 3, 4), (1, 3, 4), (2, 3, 4)): (
        (0, 1, 5, 6), (2, 7, 8), (3,), (4,), (9,), (10,), (11,)
    ),
    ((0, 1, 2), (0, 4, 5), (1, 4, 5), (2, 4, 5)): (
        (0, 1, 6, 7), (2, 8), (3, 4), (5,), (9,), (10,), (11,)
    ),
    ((0, 1, 4), (0, 1, 5), (2, 3, 4), (2, 3, 5)): (
        (0, 4, 8), (1, 6, 9), (2, 7), (3,), (5,), (10,), (11,)
    ),
    ((0, 1, 4), (0, 1, 5), (2, 4, 5), (2, 6, 7)): (
        (2, 3, 6, 11), (0, 7), (4, 10), (1,), (5,), (8,), (9,)
    ),
    ((0, 1, 4), (0, 2, 4), (0, 3, 5), (1, 2, 5)): (
        (1, 2, 6, 7), (0, 5), (3, 10), (4,), (8,), (9,), (11,)
    ),
    ((0, 1, 4), (0, 2, 4), (0, 4, 5), (1, 2, 5)): (
        (1, 3, 6, 7, 11), (2, 5), (0,), (4,), (8,), (9,), (10,)
    ),
    ((0, 1, 4), (0, 2, 5), (1, 3, 5), (2, 3, 4)): (
        (0, 6, 8), (1, 7, 10), (3, 5), (2,), (4,), (9,), (11,)
    ),
}

EXPECTED_GAPS = {
    profile: gap
    for profile, gap in zip(
        POSITIVE_ROWS,
        ((0, 6), (1, 6), (0, 6), (0, 6), (4, 5),
         (4, 5), (3, 6), (1, 4), (4, 5)),
    )
}

NEGATIVE_ROWS = {
    ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)),
    ((0, 1, 2), (0, 1, 4), (0, 2, 4), (1, 2, 4)),
    ((0, 1, 4), (0, 1, 5), (0, 4, 5), (1, 4, 5)),
}

# One 19-contact quotient for each shore-split orbit of the tetrahedral
# family.  Portal vertices 8,9,10,11 are ordered by the displayed profile.
NEGATIVE_NEAR_MISSES = (
    (
        ((1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)),
        ((0, 7), (1, 6), (2,), (3, 5), (8, 11), (9,), (10,)),
    ),
    (
        ((1, 2, 4), (0, 2, 4), (0, 1, 4), (0, 1, 2)),
        ((0, 6), (1, 5), (2,), (3, 4, 8), (7,), (9, 10), (11,)),
    ),
    (
        ((1, 4, 5), (0, 4, 5), (0, 1, 5), (0, 1, 4)),
        ((0, 6), (1,), (2, 5, 9), (3, 4, 8), (7,), (10,), (11,)),
    ),
)


def automorphisms():
    for left in itertools.permutations(range(4)):
        for right0 in itertools.permutations(range(4)):
            right = tuple(4 + x for x in right0)
            yield left + right
            yield right + left


AUT = tuple(automorphisms())


def canonical(profile):
    return min(
        tuple(sorted(tuple(sorted(perm[x] for x in neighborhood))
                     for neighborhood in profile))
        for perm in AUT
    )


def core_connected(mask):
    return mask.bit_count() == 1 or bool(mask & 0x0F) and bool(mask & 0xF0)


def core_contact(left, right):
    return bool((left & 0x0F) and (right & 0xF0)) or bool(
        (left & 0xF0) and (right & 0x0F)
    )


def independent_bad_profiles():
    models = set()
    for assignment in itertools.product(range(4), repeat=8):
        bags = tuple(
            sum(1 << v for v, label in enumerate(assignment) if label == bag)
            for bag in range(3)
        )
        if not all(bags) or not all(core_connected(bag) for bag in bags):
            continue
        if not all(core_contact(bags[i], bags[j])
                   for i, j in itertools.combinations(range(3), 2)):
            continue
        models.add(tuple(sorted(bags)))
    models = tuple(sorted(models))

    attachments = tuple(mask for mask in range(256) if mask.bit_count() == 3)
    zero = []
    one = []
    for attachment in attachments:
        zbits = obits = 0
        for index, model in enumerate(models):
            misses = sum(not (bag & attachment) for bag in model)
            if misses == 0:
                zbits |= 1 << index
            elif misses == 1:
                obits |= 1 << index
        zero.append(zbits)
        one.append(obits)

    bad = []
    for i in range(56):
        for j in range(i, 56):
            for k in range(j, 56):
                for ell in range(k, 56):
                    certificate = (
                        zero[i] & zero[j] & zero[k] & zero[ell]
                        | one[i] & zero[j] & zero[k] & zero[ell]
                        | zero[i] & one[j] & zero[k] & zero[ell]
                        | zero[i] & zero[j] & one[k] & zero[ell]
                        | zero[i] & zero[j] & zero[k] & one[ell]
                    )
                    if certificate:
                        continue
                    bad.append(
                        tuple(
                            tuple(v for v in range(8) if attachments[t] >> v & 1)
                            for t in (i, j, k, ell)
                        )
                    )
    return models, bad


def graph_for(profile):
    graph = [0] * 12

    def add(x, y):
        graph[x] |= 1 << y
        graph[y] |= 1 << x

    for x in range(4):
        for y in range(4, 8):
            add(x, y)
    for x, y in itertools.combinations(range(8, 12), 2):
        add(x, y)
    for portal, neighborhood in zip(range(8, 12), profile):
        for core in neighborhood:
            add(portal, core)
    return graph


def connected(graph, bag):
    mask = sum(1 << x for x in bag)
    seen = mask & -mask
    todo = seen
    while todo:
        bit = todo & -todo
        todo ^= bit
        new = graph[bit.bit_length() - 1] & mask & ~seen
        seen |= new
        todo |= new
    return seen == mask


def contact(graph, left, right):
    return any((graph[x] >> y) & 1 for x in left for y in right)


def has_k7minus_on_eight(graph):
    # Seven bags on eight vertices are seven singletons with one deletion,
    # or one connected pair and six singletons.
    for unused in range(8):
        bags = tuple((v,) for v in range(8) if v != unused)
        if sum(contact(graph, bags[i], bags[j])
               for i, j in itertools.combinations(range(7), 2)) >= 20:
            return True
    for x, y in itertools.combinations(range(8), 2):
        if not ((graph[x] >> y) & 1):
            continue
        bags = ((x, y),) + tuple((v,) for v in range(8) if v not in (x, y))
        if sum(contact(graph, bags[i], bags[j])
               for i, j in itertools.combinations(range(7), 2)) >= 20:
            return True
    return False


def completed_core(s):
    graph = [0] * 8

    def add(x, y):
        graph[x] |= 1 << y
        graph[y] |= 1 << x

    for x in range(4):
        for y in range(4, 8):
            add(x, y)
    for x, y in itertools.combinations(s, 2):
        add(x, y)
    return graph


def k8_minus_matching():
    graph = [0] * 8
    for x, y in itertools.combinations(range(8), 2):
        if y == x + 4:
            continue
        graph[x] |= 1 << y
        graph[y] |= 1 << x
    return graph


def main():
    models, bad = independent_bad_profiles()
    orbit_counts = {}
    for profile in bad:
        representative = canonical(profile)
        orbit_counts[representative] = orbit_counts.get(representative, 0) + 1

    assert len(models) == 3784
    assert len(bad) == 1170
    assert set(orbit_counts) == set(POSITIVE_ROWS) | NEGATIVE_ROWS
    assert sorted(orbit_counts.values()) == [2, 32, 32, 36, 36, 48, 48, 72, 144, 144, 288, 288]

    for profile, bags in POSITIVE_ROWS.items():
        graph = graph_for(profile)
        assert len(set().union(*map(set, bags))) == sum(map(len, bags))
        assert all(connected(graph, bag) for bag in bags)
        gaps = tuple(
            (i, j)
            for i, j in itertools.combinations(range(7), 2)
            if not contact(graph, bags[i], bags[j])
        )
        assert gaps == (EXPECTED_GAPS[profile],)

    for profile in NEGATIVE_ROWS:
        s = set().union(*map(set, profile))
        assert len(s) == 4
        assert set(map(frozenset, profile)) == {
            frozenset(s - {vertex}) for vertex in s
        }
        assert not has_k7minus_on_eight(completed_core(s))
    assert not has_k7minus_on_eight(k8_minus_matching())

    for profile, bags in NEGATIVE_NEAR_MISSES:
        graph = graph_for(profile)
        assert len(set().union(*map(set, bags))) == sum(map(len, bags))
        assert all(connected(graph, bag) for bag in bags)
        assert sum(
            contact(graph, bags[i], bags[j])
            for i, j in itertools.combinations(range(7), 2)
        ) == 19

    negative_count = sum(orbit_counts[row] for row in NEGATIVE_ROWS)
    normalized = tuple(sorted(canonical(profile) for profile in bad))
    digest = hashlib.sha256(repr(normalized).encode()).hexdigest()
    print("core_models", len(models))
    print("restricted_failures", len(bad))
    print("orbits", len(orbit_counts), "positive", len(POSITIVE_ROWS), "negative", len(NEGATIVE_ROWS))
    print("negative_profiles", negative_count)
    print("orbit_sizes", sorted(orbit_counts.values()))
    print("sha256", digest)
    print("tetrahedral_near_miss_orbits", len(NEGATIVE_NEAR_MISSES), "quotient_edges", 19)
    print("classification_and_certificates_valid")


if __name__ == "__main__":
    main()
