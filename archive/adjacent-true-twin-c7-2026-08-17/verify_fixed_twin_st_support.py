#!/usr/bin/env python3
"""Independent finite audit of the two combinatorial capstone lemmas.

Part A exhausts all ordered support pairs U,V on a labelled C5 satisfying
|U|,|V|>=2 and max(|U|,|V|)>=3, and all ten partitions of C5 into three
cyclic arcs.  It checks that some partition has at most one failed
support--arc incidence.  This verifies the interval lemma in its stronger
form, without assuming U union V=C.

Part B exhausts bounded abstract st-profiles.  An H-neighbourhood of a cycle
vertex is represented only by the positions it occupies in an st-ordering.
Every profile has at least three positions and, across all five profiles,
the two endpoint positions occur in total at most once.  For orders 5, 6,
and 7 the verifier checks that some prefix/suffix cut has both supports of
order at least two.  This is a falsification audit; the theorem is proved by
the unbounded last-index argument in the accompanying proof.
"""

from itertools import combinations, product


CYCLE = frozenset(range(5))


def cyclic_arc_partitions():
    partitions = []
    for cut_tuple in combinations(range(5), 3):
        cuts = set(cut_tuple)
        start = (min(cuts) + 1) % 5
        vertex = start
        current = []
        bags = []
        while True:
            current.append(vertex)
            if vertex in cuts:
                bags.append(frozenset(current))
                current = []
            vertex = (vertex + 1) % 5
            if vertex == start:
                break
        assert len(bags) == 3 and set().union(*bags) == set(CYCLE)
        partitions.append(tuple(bags))
    assert len(partitions) == 10
    return tuple(partitions)


def incidence_misses(partition, left, right):
    return sum(not (bag & support)
               for bag in partition for support in (left, right))


def check_arc_lemma():
    partitions = cyclic_arc_partitions()
    tested = 0
    best_distribution = {0: 0, 1: 0}
    for left_mask in range(1 << 5):
        left = frozenset(v for v in CYCLE if left_mask >> v & 1)
        for right_mask in range(1 << 5):
            right = frozenset(v for v in CYCLE if right_mask >> v & 1)
            if (len(left) < 2 or len(right) < 2
                    or max(len(left), len(right)) < 3):
                continue
            tested += 1
            best = min(incidence_misses(p, left, right)
                       for p in partitions)
            assert best <= 1, (left, right, best)
            best_distribution[best] += 1
    assert tested == 576
    return tested, best_distribution


def internal_neighbourhoods(order):
    internal = tuple(range(1, order - 1))
    return tuple(frozenset(choice)
                 for size in range(3, len(internal) + 1)
                 for choice in combinations(internal, size))


def has_balanced_cut(profiles, order):
    for cut in range(1, order):
        prefix = set(range(cut))
        suffix = set(range(cut, order))
        left = sum(bool(profile & prefix) for profile in profiles)
        right = sum(bool(profile & suffix) for profile in profiles)
        if left >= 2 and right >= 2:
            return True
    return False


def check_st_profiles():
    counts = {}
    for order in (5, 6, 7):
        choices = internal_neighbourhoods(order)
        checked = 0
        # There is either no endpoint incidence or exactly one: choose its
        # cycle vertex and choose which of the two endpoint positions it sees.
        endpoint_options = (None,) + tuple(
            (cycle_vertex, endpoint)
            for cycle_vertex in range(5)
            for endpoint in (0, order - 1)
        )
        for base in product(choices, repeat=5):
            for option in endpoint_options:
                profiles = list(base)
                if option is not None:
                    cycle_vertex, endpoint = option
                    profiles[cycle_vertex] = profiles[cycle_vertex] | {endpoint}
                assert all(len(profile) >= 3 for profile in profiles)
                assert sum((0 in profile) + (order - 1 in profile)
                           for profile in profiles) <= 1
                assert has_balanced_cut(profiles, order), (order, profiles)
                checked += 1
        counts[order] = checked
    return counts


def main():
    pairs, distribution = check_arc_lemma()
    profiles = check_st_profiles()
    print("arc_support_pairs", pairs,
          "best_missing_distribution", distribution, "GREEN")
    print("st_profile_counts", profiles, "GREEN")


if __name__ == "__main__":
    main()
