#!/usr/bin/env python3
"""Verify that the fixed icosahedral five-support seed cannot extend.

This is a finite, dependency-free check for one labelled graph and one fixed
family of five supports.  It proves no unbounded partition theorem.  In the
notation of the literal-K_{4,4} minimum blocker, it exhausts every possible
support of ``a`` of order at most five and every support of ``b`` implicitly,
subject to the full boundary inequalities and failure of the exact spanning
two-helper split criterion.
"""

from __future__ import annotations

import itertools


if not __debug__:
    raise SystemExit("verification requires assertions; do not use Python -O")


ORDER = 11
FULL = (1 << ORDER) - 1
EDGES = {
    tuple(sorted(edge))
    for edge in (
        (0, 1), (0, 4), (0, 5), (0, 7),
        (1, 2), (1, 5), (1, 7), (1, 8),
        (2, 3), (2, 5), (2, 8), (2, 9),
        (3, 4), (3, 5), (3, 9), (3, 10),
        (4, 5), (4, 10),
        (6, 7), (6, 8), (6, 9), (6, 10),
        (7, 8), (8, 9), (9, 10),
    )
}
SUPPORTS = (
    {0, 1, 2, 3, 4, 5, 8, 9},
    {4, 10},
    {6, 10},
    {6, 7},
    {0, 7},
)
GRAPH6 = "JhfwEDbKgs_"


def graph6_code() -> str:
    """Encode the fixed host in the graph6 bit order."""
    bits = [int((left, right) in EDGES)
            for right in range(1, ORDER) for left in range(right)]
    bits.extend([0] * (-len(bits) % 6))
    payload = "".join(
        chr(63 + sum(bits[start + offset] << (5 - offset)
                     for offset in range(6)))
        for start in range(0, len(bits), 6)
    )
    return chr(63 + ORDER) + payload


def mask(vertices: set[int]) -> int:
    return sum(1 << vertex for vertex in vertices)


def adjacency() -> tuple[int, ...]:
    rows = [0] * ORDER
    for left, right in EDGES:
        rows[left] |= 1 << right
        rows[right] |= 1 << left
    return tuple(rows)


ADJACENCY = adjacency()
SUPPORT_MASKS = tuple(mask(support) for support in SUPPORTS)


def connected(vertices: int) -> bool:
    if vertices == 0:
        return False
    reached = vertices & -vertices
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        new = ADJACENCY[bit.bit_length() - 1] & vertices & ~reached
        reached |= new
        frontier |= new
    return reached == vertices


def boundary(vertices: int) -> int:
    answer = 0
    todo = vertices
    while todo:
        bit = todo & -todo
        todo ^= bit
        answer |= ADJACENCY[bit.bit_length() - 1]
    return answer & ~vertices


def pure_score(vertices: int) -> int:
    return boundary(vertices).bit_count() + sum(
        bool(vertices & support) for support in SUPPORT_MASKS
    )


def split_count(left: int) -> int:
    right = FULL ^ left
    return sum(
        bool(left & support) and bool(right & support)
        for support in SUPPORT_MASKS
    )


def verify_host_and_fixed_supports() -> tuple[list[int], list[int]]:
    assert graph6_code() == GRAPH6
    assert len(EDGES) == 25
    assert sorted(row.bit_count() for row in ADJACENCY) == [4] * 5 + [5] * 6
    assert all(support.bit_count() >= 2 for support in SUPPORT_MASKS)

    # Four-connectivity is checked directly by all deletions of at most three
    # vertices.  The empty deletion is included.
    for deleted_order in range(4):
        for deleted_vertices in itertools.combinations(range(ORDER), deleted_order):
            deleted = sum(1 << vertex for vertex in deleted_vertices)
            assert connected(FULL ^ deleted)

    connected_score_histogram: dict[int, int] = {}
    for vertices in range(1, FULL):
        if not connected(vertices):
            continue
        score = pure_score(vertices)
        assert score >= 6
        connected_score_histogram[score] = (
            connected_score_histogram.get(score, 0) + 1
        )
    assert connected_score_histogram == {
        6: 32, 7: 155, 8: 398, 9: 508, 10: 317, 11: 73, 12: 2,
    }

    bond_histogram: dict[int, int] = {}
    oriented_three_split_bonds = []
    for left in range(1, FULL):
        right = FULL ^ left
        if not connected(left) or not connected(right):
            continue
        splits = split_count(left)
        assert splits <= 3
        if splits == 3:
            oriented_three_split_bonds.append(left)
        if left & 1:  # Count each unordered bond once.
            bond_histogram[splits] = bond_histogram.get(splits, 0) + 1
    assert bond_histogram == {1: 52, 2: 172, 3: 243}
    assert len(oriented_three_split_bonds) == 486

    base_five = [vertices for vertices in range(1, FULL + 1)
                 if pure_score(vertices) == 5]
    base_six = [vertices for vertices in range(1, FULL + 1)
                if pure_score(vertices) == 6]
    assert base_five == [FULL]
    assert len(base_six) == 32
    assert min(pure_score(vertices) for vertices in range(1, FULL + 1)) == 5
    return oriented_three_split_bonds, base_six


def verify_no_full_extension(
    oriented_three_split_bonds: list[int], base_six: list[int]
) -> dict[str, int]:
    """Exhaust all possible ``a`` supports and eliminate ``b`` monotonically.

    Let ``A`` and ``B`` be the supports of the boundary resources ``a`` and
    ``b``.  Since no bond splits four fixed supports, failure of the full
    split criterion says that, for every oriented three-split bond ``(U,V)``
    met by ``A`` on ``U``, ``B`` must avoid ``V``.  Hence ``B`` is contained
    in the intersection of all such ``U``.  Taking this whole intersection
    is optimal for every remaining condition, all of which are monotone in
    ``B``.

    The only pure-score-five set is the whole host, so nonempty ``A,B`` meet
    it automatically.  Each pure-score-six set must meet at least one of
    ``A,B`` for the full seven-resource boundary inequality.
    """

    counts = {
        "a_supports": 0,
        "nonempty_allowed_b_regions": 0,
        "full_boundary_extensions": 0,
        "exact_blocker_extensions": 0,
    }

    for a_support in range(1, FULL + 1):
        if a_support.bit_count() > 5:
            continue
        counts["a_supports"] += 1

        allowed_b = FULL
        for left in oriented_three_split_bonds:
            if a_support & left:
                allowed_b &= left
        if allowed_b == 0:
            continue
        counts["nonempty_allowed_b_regions"] += 1

        # If maximal allowed_b misses a required set which A also misses,
        # every subset of allowed_b misses it as well.  Conversely, maximal
        # allowed_b itself witnesses all monotone boundary requirements.
        if any(not (a_support & vertices) and not (allowed_b & vertices)
               for vertices in base_six):
            continue
        counts["full_boundary_extensions"] += 1

        # This line is unreachable.  Were it reached, the strict inequality
        # for a proper connected set seeing both a and b would hold because
        # its fixed-support score is already at least six.  The distinguished
        # eligible-p requirement could only reduce the count further.
        counts["exact_blocker_extensions"] += 1

    assert counts == {
        "a_supports": 1023,
        "nonempty_allowed_b_regions": 12,
        "full_boundary_extensions": 0,
        "exact_blocker_extensions": 0,
    }
    return counts


def main() -> None:
    bonds, base_six = verify_host_and_fixed_supports()
    counts = verify_no_full_extension(bonds, base_six)
    print(f"graph6={GRAPH6} order=11 edges=25 connectivity=4 minimum_degree=4")
    print("oriented_three_split_bonds=486 pure_score_six_sets=32")
    print(
        "a_supports={a_supports} nonempty_allowed_b_regions="
        "{nonempty_allowed_b_regions} full_boundary_extensions="
        "{full_boundary_extensions} exact_blocker_extensions="
        "{exact_blocker_extensions}".format(**counts)
    )
    print("GREEN fixed icosahedral seed has no full a,b blocker extension")


if __name__ == "__main__":
    main()
