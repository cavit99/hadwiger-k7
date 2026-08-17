#!/usr/bin/env python3
"""Random adversarial probe for the six-root incidence core.

This deliberately ignores edges inside the shore.  A positive orientation
certificate therefore gives a rooted K5-minus model using only boundary
incidences; a negative row is merely a candidate requiring further tests.
"""

from __future__ import annotations

import itertools
import random


ROOTS = range(6)


def has_oriented_near_five(masks: tuple[int, ...]) -> bool:
    for omitted in ROOTS:
        roots = tuple(root for root in ROOTS if root != omitted)
        pairs = tuple(itertools.combinations(roots, 2))
        pair_index = {pair: index for index, pair in enumerate(pairs)}
        full = (1 << len(pairs)) - 1
        states = {0}
        for mask in masks:
            additions = {0}
            for centre in roots:
                if not (mask >> centre) & 1:
                    continue
                star = 0
                for other in roots:
                    if other != centre and (mask >> other) & 1:
                        star |= 1 << pair_index[tuple(sorted((centre, other)))]
                additions.add(star)
            states = {state | addition for state in states for addition in additions}
            if any((full ^ state).bit_count() <= 1 for state in states):
                return True
    return False


def pair_sums(masks: tuple[int, ...]) -> bool:
    counts = [sum((mask >> root) & 1 for mask in masks) for root in ROOTS]
    return all(counts[i] + counts[j] >= len(masks) + 1 for i, j in itertools.combinations(ROOTS, 2))


def density_possible(masks: tuple[int, ...]) -> bool:
    c = len(masks)
    incidences = sum(mask.bit_count() for mask in masks)
    return c * (c - 1) // 2 + incidences >= 4 * c + 6


def main() -> None:
    rng = random.Random(0x5EED)
    tested = 0
    candidates = 0
    negatives: dict[int, tuple[int, tuple[int, ...]]] = {}
    for c in range(3, 10):
        for _ in range(300_000):
            masks = tuple(
                sorted(
                    rng.choices(
                        range(1, 64),
                        weights=[1 << (mask.bit_count() + 1) for mask in range(1, 64)],
                        k=c,
                    )
                )
            )
            tested += 1
            if not pair_sums(masks) or not density_possible(masks):
                continue
            candidates += 1
            if has_oriented_near_five(masks):
                continue
            incidences = sum(mask.bit_count() for mask in masks)
            record = (incidences, masks)
            if c not in negatives or record > negatives[c]:
                negatives[c] = record
    print(f"tested={tested} candidates={candidates}")
    for c, (incidences, masks) in sorted(negatives.items()):
        print(c, incidences, [f"{mask:06b}" for mask in masks])


if __name__ == "__main__":
    main()
