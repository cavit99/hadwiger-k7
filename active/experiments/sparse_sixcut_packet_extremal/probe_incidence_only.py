#!/usr/bin/env python3
"""Adversarial probe for singleton-or-one-vertex rooted certificates.

The six boundary roots are independent.  A certificate is required to have
five rooted branch bags, each either a singleton root or a root together with
exactly one internal vertex.  The script compares that deliberately stronger
certificate with the exact unrestricted rooted-model test in ``search.py``.
It is a falsifier, not a proof.
"""

from __future__ import annotations

import argparse
import itertools
import random

from search import (
    any_rooted_assignment,
    bags_touch,
    describe,
    excess,
    internally_six_connected,
    packet_number_one,
    random_instance,
)


def incidence_only_assignment(adjacency, labels):
    """Return ``(roots,bags)`` for a singleton/one-vertex model, if any."""
    order = len(adjacency)
    vertices = range(order)
    for omitted in range(6):
        roots = tuple(root for root in range(6) if root != omitted)
        # At least three bags must be augmented: three stable singleton roots
        # already create three missing pairs.
        for augmented_count in range(3, 6):
            if augmented_count > order:
                continue
            for augmented in itertools.combinations(range(5), augmented_count):
                for assigned in itertools.permutations(vertices, augmented_count):
                    bags = [0] * 5
                    valid = True
                    for bag, vertex in zip(augmented, assigned, strict=True):
                        if not (labels[vertex] >> roots[bag] & 1):
                            valid = False
                            break
                        bags[bag] = 1 << vertex
                    if not valid:
                        continue
                    missing = 0
                    for left, right in itertools.combinations(range(5), 2):
                        if not bags_touch(
                            roots[left], bags[left], roots[right], bags[right],
                            adjacency, labels,
                        ):
                            missing += 1
                            if missing > 1:
                                break
                    if missing <= 1:
                        return roots, tuple(bags)
    return None


def forced_near_clique_instance(order: int, rng: random.Random):
    """Return a random instance whose first five vertices induce ``K5-``."""
    adjacency = [0] * order
    missing = rng.randrange(10)
    for index, (left, right) in enumerate(itertools.combinations(range(5), 2)):
        if index != missing:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    p = rng.uniform(0.18, 0.92)
    for left, right in itertools.combinations(range(order), 2):
        if left < 5 and right < 5:
            continue
        if rng.random() < p:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    q = rng.uniform(0.18, 0.92)
    labels = tuple(
        sum(1 << root for root in range(6) if rng.random() < q)
        for _ in range(order)
    )
    return tuple(adjacency), labels


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=6)
    parser.add_argument("--trials", type=int, default=100_000)
    parser.add_argument("--seed", type=int, default=20260817)
    parser.add_argument("--forced-k5minus", action="store_true")
    parser.add_argument("--minimum-excess", type=int, default=6)
    args = parser.parse_args()
    rng = random.Random(args.seed)

    feasible = packet_one = unrestricted = incidence = 0
    for trial in range(args.trials):
        if args.forced_k5minus:
            adjacency, labels = forced_near_clique_instance(args.order, rng)
        else:
            adjacency, labels = random_instance(args.order, rng)
        if excess(adjacency, labels) < args.minimum_excess:
            continue
        if not internally_six_connected(adjacency, labels):
            continue
        feasible += 1
        if not packet_number_one(adjacency, labels):
            continue
        packet_one += 1
        full = any_rooted_assignment(adjacency, labels)
        if full is None:
            print(f"UNRESTRICTED_COUNTEREXAMPLE trial={trial} {describe(adjacency, labels)}")
            return
        unrestricted += 1
        literal = incidence_only_assignment(adjacency, labels)
        if literal is None:
            roots, bags = full
            print(f"INCIDENCE_ONLY_COUNTEREXAMPLE trial={trial} {describe(adjacency, labels)}")
            print(f"unrestricted_roots={roots} unrestricted_bags={bags}")
            return
        incidence += 1
    print(
        f"NO_COUNTEREXAMPLE_IN_SAMPLE order={args.order} trials={args.trials} "
        f"feasible={feasible} packet_one={packet_one} unrestricted={unrestricted} "
        f"incidence={incidence} forced_k5minus={args.forced_k5minus}"
    )


if __name__ == "__main__":
    main()
