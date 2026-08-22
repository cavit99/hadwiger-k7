#!/usr/bin/env python3
"""Verify the two exceptional orbits in the C7 two-support lemma."""

from collections import Counter
from itertools import combinations


T = frozenset(range(7))
SUPPORTS = tuple(frozenset(c) for k in range(5, 8)
                 for c in combinations(range(7), k))


def residual_path(p, q):
    """The C7-p-q path after deleting adjacent p,q."""
    start = (2 * q - p) % 7
    path = [start]
    while len(path) < 5:
        u = path[-1]
        path.append(next(v for v in ((u - 1) % 7, (u + 1) % 7)
                         if v not in (p, q) and v not in path))
    return tuple(path)


def interval_partitions(path):
    for i in range(1, 4):
        for j in range(i + 1, 5):
            yield (frozenset(path[:i]), frozenset(path[i:j]),
                   frozenset(path[j:]))


def restricted_works(a, b):
    for p in a:
        for q in b:
            if (p - q) % 7 not in (1, 6):
                continue
            if any(all(block & a and block & b for block in partition)
                   for partition in interval_partitions(residual_path(p, q))):
                return True
    return False


def transform(s, shift, reflect):
    return frozenset(((-v if reflect else v) + shift) % 7 for v in s)


def canonical_missing_pair(a, b):
    forms = []
    for shift in range(7):
        for reflect in (False, True):
            aa = transform(a, shift, reflect)
            bb = transform(b, shift, reflect)
            forms.append((tuple(sorted(T - aa)), tuple(sorted(T - bb))))
            forms.append((tuple(sorted(T - bb)), tuple(sorted(T - aa))))
    return min(forms)


def main():
    failures = [(a, b) for a in SUPPORTS for b in SUPPORTS
                if not restricted_works(a, b)]
    orbits = Counter(canonical_missing_pair(a, b) for a, b in failures)
    expected = {
        ((0, 1), (3, 4)): 14,
        ((0, 1), (3, 5)): 14,
    }
    assert len(SUPPORTS) == 29
    assert len(failures) == 28
    assert dict(orbits) == expected
    print("GREEN", "support_pairs", len(SUPPORTS) ** 2,
          "restricted_failures", len(failures), "orbits", dict(orbits))


if __name__ == "__main__":
    main()
