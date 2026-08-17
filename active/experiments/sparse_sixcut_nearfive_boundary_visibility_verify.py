#!/usr/bin/env python3
"""Exhaust Lemma 1 of the near-five boundary-visibility note.

Families are unordered five-multisets of subsets of a labelled six-set.
Repetitions are therefore included.  We retain precisely the hypotheses
|H_i| >= 2, at most two size-two occurrences, and union H_i = S, and test
all complementary bipartitions of S for Property B.
"""

from itertools import combinations_with_replacement


FULL = (1 << 6) - 1
SUBSETS = tuple(mask for mask in range(1, FULL + 1) if mask.bit_count() >= 2)
# Exactly one representative from each unordered complementary pair.
COLOUR_CLASSES = tuple(range(1, 1 << 5))


def is_split(family: tuple[int, ...], colour_class: int) -> bool:
    other = FULL ^ colour_class
    return all(edge & colour_class and edge & other for edge in family)


def main() -> None:
    eligible = 0
    covering = 0
    by_two_occurrences = [0, 0, 0]

    for family in combinations_with_replacement(SUBSETS, 5):
        two_occurrences = sum(edge.bit_count() == 2 for edge in family)
        if two_occurrences > 2:
            continue
        eligible += 1

        union = 0
        for edge in family:
            union |= edge
        if union != FULL:
            continue

        covering += 1
        by_two_occurrences[two_occurrences] += 1
        assert any(is_split(family, side) for side in COLOUR_CLASSES), family

    assert eligible == 5_194_959
    assert covering == 4_619_110
    assert by_two_occurrences == [1_279_600, 2_008_605, 1_330_905]
    print(
        "GREEN: exhaustive Property-B census; "
        f"eligible={eligible}, covering={covering}, "
        f"by_two_occurrences={by_two_occurrences}, counterexamples=0"
    )


if __name__ == "__main__":
    main()
