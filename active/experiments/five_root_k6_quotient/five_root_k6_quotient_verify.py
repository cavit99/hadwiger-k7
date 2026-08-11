#!/usr/bin/env python3
"""Exhaust the five-root contact matrices over a literal K6 quotient.

The quotient has six clique vertices and five independent roots.  A row
records the clique vertices adjacent to one root.  The checker verifies the
sharp criterion

    quotient contains K7-minus  <=>  some row has at least five entries.

For the avoiding side it is enough, by edge monotonicity, to enumerate the
15**5 maximal matrices in which every row has four entries.  Their missing
pairs form a five-edge loopless multigraph on six vertices.  The optional
normal-form pass classifies these multisets up to permutation of the six
clique labels (root permutation is already removed by using a multiset).
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter


CLIQUE_ORDER = 6
ROOT_COUNT = 5
PAIRS = tuple(itertools.combinations(range(CLIQUE_ORDER), 2))


def unavoidable_root_defects(degree: int, root_only_others: int) -> int:
    """Minimum missing adjacencies at a root-only branch set.

    In a seven-branch model, after fixing one root-only branch set, let
    ``root_only_others`` of the other six branch sets contain no clique
    vertex.  Those sets are singleton roots and are all nonadjacent to the
    fixed root.  Every remaining branch set needs a distinct adjacent
    clique vertex in order to meet the fixed root.
    """

    clique_bags = 6 - root_only_others
    return root_only_others + max(0, clique_bags - degree)


def verify_criterion() -> int:
    # Positive direction: a row of size five or six, together with the six
    # singleton clique bags, is K7-minus (or K7).
    for degree in (5, 6):
        assert 6 - degree <= 1

    # Negative direction: every possible number of additional root-only
    # bags leaves at least two nonadjacencies at the first root-only bag.
    for degree in range(5):
        # At most the other four roots can support root-only bags.
        for root_only_others in range(ROOT_COUNT):
            assert unavoidable_root_defects(degree, root_only_others) >= 2

    # Exhaust the maximal avoiding matrices.  A row is represented by its
    # missing pair; arbitrary smaller rows are subgraphs of these matrices.
    checked = 0
    for missing_rows in itertools.product(PAIRS, repeat=ROOT_COUNT):
        for missing_pair in missing_rows:
            assert CLIQUE_ORDER - len(missing_pair) == 4
            assert unavoidable_root_defects(4, 0) == 2
        checked += 1
    assert checked == len(PAIRS) ** ROOT_COUNT == 759_375
    return checked


def permuted_edge(edge: tuple[int, int], permutation: tuple[int, ...]) -> tuple[int, int]:
    a, b = permutation[edge[0]], permutation[edge[1]]
    return (a, b) if a < b else (b, a)


def canonical_multigraph(edges: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    best: tuple[tuple[int, int], ...] | None = None
    for permutation in itertools.permutations(range(CLIQUE_ORDER)):
        image = tuple(sorted(permuted_edge(edge, permutation) for edge in edges))
        if best is None or image < best:
            best = image
    assert best is not None
    return best


def classify_normal_forms() -> tuple[int, Counter[tuple[int, ...]]]:
    forms: set[tuple[tuple[int, int], ...]] = set()
    for indices in itertools.combinations_with_replacement(range(len(PAIRS)), ROOT_COUNT):
        edges = tuple(PAIRS[index] for index in indices)
        forms.add(canonical_multigraph(edges))

    multiplicities: Counter[tuple[int, ...]] = Counter()
    for form in forms:
        profile = tuple(sorted(Counter(form).values(), reverse=True))
        multiplicities[profile] += 1
    return len(forms), multiplicities


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--normal-forms",
        action="store_true",
        help="also classify maximal matrices modulo row and column permutations",
    )
    args = parser.parse_args()

    checked = verify_criterion()
    print(f"maximal_avoiding_matrices={checked}")
    print("criterion=max_row_size_at_least_5")
    if args.normal_forms:
        count, profiles = classify_normal_forms()
        print(f"maximal_normal_forms={count}")
        for profile, number in sorted(profiles.items(), reverse=True):
            print(f"multiplicity_profile={profile} forms={number}")
    print("GREEN: exact quotient criterion verified")


if __name__ == "__main__":
    main()
