#!/usr/bin/env python3
"""Independent orbit audit for the K4,4 + four-portal triangle fallback.

The primary screen leaves 1,140 unordered triples of missed core vertices.
This script quotients them by Aut(K4,4), verifies that there are ten orbits,
and checks a fixed human-readable K7^- branch-set certificate for each orbit
representative.  It deliberately does not call the exhaustive seven-bag
fallback search.
"""

from __future__ import annotations

import hashlib
import itertools


ROWS = {
    ((0, 1), (2, 3, 4, 5), (2, 3, 6, 7)): (
        (0, 4, 10), (1, 5), (2, 6), (3,), (7,), (8,), (9,)
    ),
    ((0, 1, 2), (0, 3, 4, 5), (0, 3, 6, 7)): (
        (0, 4, 10), (1, 5), (2, 6), (3,), (7,), (8,), (9,)
    ),
    ((0, 1, 2, 3), (0, 1, 4, 5), (0, 1, 6, 7)): (
        (0, 4, 10), (1, 6), (2, 5), (3,), (7,), (8,), (9,)
    ),
    ((0, 1, 2, 4), (0, 1, 3, 5), (0, 1, 6, 7)): (
        (0, 1, 4), (3, 6), (5, 8), (2,), (7,), (9,), (10,)
    ),
    ((0, 1, 2, 4), (0, 3, 4, 5), (0, 3, 6, 7)): (
        (0, 4, 10), (1, 5), (2, 6), (3,), (7,), (8,), (9,)
    ),
    ((0, 1, 2, 4), (0, 3, 4, 5), (0, 4, 6, 7)): (
        (0, 1, 4), (3, 6), (5, 8), (2,), (7,), (9,), (10,)
    ),
    ((0, 1, 4), (2, 3, 4, 5), (2, 3, 6, 7)): (
        (0, 4, 10), (1, 5), (2, 6), (3,), (7,), (8,), (9,)
    ),
    ((0, 1, 4, 5), (0, 1, 6, 7), (2, 3, 4, 5)): (
        (0, 4), (1, 5), (2, 6), (3, 8), (7,), (9,), (10,)
    ),
    ((0, 1, 4, 5), (0, 1, 6, 7), (2, 3, 4, 6)): (
        (0, 4, 9), (1, 6), (2, 5), (3,), (7,), (8,), (10,)
    ),
    ((0, 1, 4, 5), (0, 2, 4, 6), (0, 3, 4, 7)): (
        (0, 5, 6), (1, 10), (3, 4), (2,), (7,), (8,), (9,)
    ),
}

EXPECTED_GAPS = {
    profile: gap
    for profile, gap in zip(
        ROWS,
        ((3, 6), (3, 6), (3, 5), (4, 6), (3, 6),
         (4, 6), (3, 6), (4, 5), (3, 6), (3, 6)),
    )
}


def automorphisms():
    for left in itertools.permutations(range(4)):
        for right0 in itertools.permutations(range(4)):
            right = tuple(4 + x for x in right0)
            yield left + right
            yield right + left


AUT = tuple(automorphisms())


def canonical(profile):
    # Sorting the three masks quotients the S3 symmetry of the triangle.
    return min(
        tuple(sorted(tuple(sorted(perm[x] for x in mask)) for mask in profile))
        for perm in AUT
    )


def core_connected(mask):
    """Connectivity in K4,4, independently of the primary enumerator."""
    return mask.bit_count() == 1 or bool(mask & 0x0F) and bool(mask & 0xF0)


def core_contact(left, right):
    return bool((left & 0x0F) and (right & 0xF0)) or bool(
        (left & 0xF0) and (right & 0x0F)
    )


def independent_bad_profiles():
    """Regenerate the primary fallback list by a different enumeration.

    Each core vertex is assigned to one of four labelled bags or to the
    unused class.  Canonical sorted bag masks remove the 4! label symmetry.
    This 5^8 assignment enumeration is intentionally independent of the
    integer-partition branch-set generator in the primary scripts.
    """
    models = set()
    for assignment in itertools.product(range(5), repeat=8):
        bags = tuple(
            sum(1 << v for v, label in enumerate(assignment) if label == bag)
            for bag in range(4)
        )
        if not all(bags) or not all(core_connected(bag) for bag in bags):
            continue
        if not all(core_contact(bags[i], bags[j]) for i, j in itertools.combinations(range(4), 2)):
            continue
        models.add(tuple(sorted(bags)))
    models = tuple(sorted(models))

    neighborhoods = tuple(mask for mask in range(256) if mask.bit_count() >= 4)
    zero = []
    one = []
    for neighborhood in neighborhoods:
        zbits = obits = 0
        for index, model in enumerate(models):
            misses = sum(not (bag & neighborhood) for bag in model)
            if misses == 0:
                zbits |= 1 << index
            elif misses == 1:
                obits |= 1 << index
        zero.append(zbits)
        one.append(obits)

    bad = []
    for i in range(len(neighborhoods)):
        for j in range(i, len(neighborhoods)):
            for k in range(j, len(neighborhoods)):
                certificate = (
                    (zero[i] & zero[j] & zero[k])
                    | (one[i] & zero[j] & zero[k])
                    | (zero[i] & one[j] & zero[k])
                    | (zero[i] & zero[j] & one[k])
                )
                if certificate:
                    continue
                bad.append(
                    tuple(
                        tuple(v for v in range(8) if not (neighborhoods[t] >> v) & 1)
                        for t in (i, j, k)
                    )
                )
    return models, bad


def graph_for(misses):
    graph = [0] * 11

    def add(x, y):
        graph[x] |= 1 << y
        graph[y] |= 1 << x

    for x in range(4):
        for y in range(4, 8):
            add(x, y)
    for x, y in ((8, 9), (8, 10), (9, 10)):
        add(x, y)
    for portal, missed in zip((8, 9, 10), misses):
        for core in range(8):
            if core not in missed:
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


def main():
    models, bad = independent_bad_profiles()
    orbit_counts = {}
    for profile in bad:
        representative = canonical(profile)
        orbit_counts[representative] = orbit_counts.get(representative, 0) + 1

    assert len(models) == 1656
    assert len(bad) == 1140
    assert set(orbit_counts) == set(ROWS)
    assert sorted(orbit_counts.values()) == [36, 36, 36, 72, 96, 144, 144, 144, 144, 288]

    for misses, bags in ROWS.items():
        graph = graph_for(misses)
        assert len(bags) == 7
        assert all(bags)
        assert sum(map(len, bags)) == len(set().union(*map(set, bags)))
        assert all(connected(graph, bag) for bag in bags)
        gaps = tuple(
            (i, j)
            for i, j in itertools.combinations(range(7), 2)
            if not contact(graph, bags[i], bags[j])
        )
        assert gaps == (EXPECTED_GAPS[misses],)

    normalized = tuple(sorted(canonical(profile) for profile in bad))
    payload = repr(normalized).encode()
    print("core_models", len(models))
    print("fallback_profiles", len(bad))
    print("orbits", len(orbit_counts))
    print("orbit_sizes", sorted(orbit_counts.values()))
    print("sha256", hashlib.sha256(payload).hexdigest())
    print("all_ten_certificates_valid")


if __name__ == "__main__":
    main()
