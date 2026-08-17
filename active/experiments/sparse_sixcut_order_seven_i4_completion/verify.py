#!/usr/bin/env python3
"""Verify the fourteen-row order-seven i=4 completion table."""

from itertools import combinations, permutations


U = frozenset(range(4))
W = frozenset(range(4, 7))
PATH_EDGES = {(4, 5), (5, 6)}


# missing U-edge, four U-to-W neighbourhoods, unmatched U vertex,
# omitted matched vertex, five internal bag parts in root order.
ROWS = (
    (False, ("12", "0", "0", ""), 0, 4, ((1,), (2,), (3,), (4, 5), (0, 6))),
    (False, ("2", "1", "0", ""), 0, 2, ((1,), (3,), (2, 4), (5,), (0, 6))),
    (False, ("02", "1", "1", ""), 0, 4, ((1,), (2,), (3,), (5,), (0, 6))),
    (True, ("12", "0", "0", "0"), 0, 4, ((1,), (2,), (3,), (4, 5), (0, 6))),
    (True, ("2", "1", "0", "0"), 0, 1, ((2,), (3,), (4,), (1, 5), (0, 6))),
    (True, ("2", "0", "1", "0"), 0, 4, ((1,), (2,), (3,), (4, 5), (0, 6))),
    (True, ("2", "1", "1", "0"), 0, 3, ((1,), (2,), (3, 4), (5,), (0, 6))),
    (True, ("2", "2", "1", "0"), 0, 3, ((1,), (2,), (3, 4), (5,), (0, 6))),
    (True, ("1", "0", "2", "0"), 2, 4, ((0,), (1,), (3,), (4, 5), (2, 6))),
    (True, ("1", "1", "2", "0"), 2, 3, ((0,), (1,), (3, 4), (5,), (2, 6))),
    (True, ("0", "0", "12", "0"), 2, 4, ((0,), (1,), (3,), (4, 5), (2, 6))),
    (True, ("2", "0", "1", "1"), 0, 1, ((2,), (3,), (1, 4), (5,), (0, 6))),
    (True, ("02", "1", "1", "1"), 0, 4, ((1,), (2,), (3,), (5,), (0, 6))),
    (True, ("1", "1", "02", "1"), 2, 4, ((0,), (1,), (3,), (5,), (2, 6))),
)


def incidence_mask(neighbourhoods):
    return sum(
        1 << (3 * vertex + int(target))
        for vertex, neighbourhood in enumerate(neighbourhoods)
        for target in neighbourhood
    )


def valid(mask, missing_u_edge):
    row_degrees = [
        sum((mask >> (3 * vertex + target)) & 1 for target in range(3))
        for vertex in range(4)
    ]
    column_degrees = [
        sum((mask >> (3 * vertex + target)) & 1 for vertex in range(4))
        for target in range(3)
    ]
    return (
        all(column_degrees)
        and sum(degree == 0 for degree in row_degrees)
        + int(missing_u_edge)
        <= 1
    )


def minimal(mask, missing_u_edge):
    return valid(mask, missing_u_edge) and all(
        not valid(mask ^ (1 << edge), missing_u_edge)
        for edge in range(12)
        if mask >> edge & 1
    )


def image(mask, u_permutation, w_permutation):
    answer = 0
    for vertex in range(4):
        for target in range(3):
            if mask >> (3 * vertex + target) & 1:
                answer |= 1 << (
                    3 * u_permutation[vertex] + w_permutation[target]
                )
    return answer


def symmetry_group(missing_u_edge):
    u_permutations = tuple(
        permutation
        for permutation in permutations(range(4))
        if not missing_u_edge
        or {permutation[0], permutation[1]} == {0, 1}
    )
    w_permutations = ((0, 1, 2), (2, 1, 0))
    return tuple(
        (u_permutation, w_permutation)
        for u_permutation in u_permutations
        for w_permutation in w_permutations
    )


def graph_edges(mask, missing_u_edge):
    edges = set(PATH_EDGES)
    edges |= set(combinations(range(4), 2))
    if missing_u_edge:
        edges.remove((0, 1))
    for vertex in range(4):
        for target in range(3):
            if mask >> (3 * vertex + target) & 1:
                edges.add((vertex, 4 + target))
    return edges


def connected(part, edges):
    part = set(part)
    reached = {next(iter(part))}
    while True:
        old = set(reached)
        reached |= {
            right
            for left, right in edges
            if left in reached and right in part
        }
        reached |= {
            left
            for left, right in edges
            if right in reached and left in part
        }
        if reached == old:
            return reached == part


def verify_bags(row):
    missing_u_edge, neighbourhoods, unmatched, omitted, parts = row
    mask = incidence_mask(neighbourhoods)
    edges = graph_edges(mask, missing_u_edge)
    anchors = sorted(((U - {unmatched}) | W) - {omitted})
    assert len(anchors) == len(parts) == 5
    assert all(anchor in part for anchor, part in zip(anchors, parts))
    assert all(connected(part, edges) for part in parts)
    assert all(
        set(parts[left]).isdisjoint(parts[right])
        for left, right in combinations(range(5), 2)
    )
    contacts = sum(
        any(
            tuple(sorted((left_vertex, right_vertex))) in edges
            for left_vertex in parts[left]
            for right_vertex in parts[right]
        )
        for left, right in combinations(range(5), 2)
    )
    assert contacts >= 9


def main():
    for row in ROWS:
        verify_bags(row)

    for missing_u_edge, expected_valid, expected_minimal, expected_orbits in (
        (False, 3221, 60, 3),
        (True, 2161, 48, 11),
    ):
        group = symmetry_group(missing_u_edge)
        minimal_masks = {
            mask for mask in range(1 << 12) if minimal(mask, missing_u_edge)
        }
        valid_masks = {
            mask for mask in range(1 << 12) if valid(mask, missing_u_edge)
        }
        displayed = set()
        rows = [row for row in ROWS if row[0] == missing_u_edge]
        assert len(rows) == expected_orbits
        for row in rows:
            representative = incidence_mask(row[1])
            orbit = {
                image(representative, u_permutation, w_permutation)
                for u_permutation, w_permutation in group
            }
            assert displayed.isdisjoint(orbit)
            displayed |= orbit
        assert len(valid_masks) == expected_valid
        assert len(minimal_masks) == expected_minimal
        assert displayed == minimal_masks
        assert all(
            any(representative & mask == representative for representative in displayed)
            for mask in valid_masks
        )
        name = "K4-minus-edge" if missing_u_edge else "K4"
        print(
            f"{name}: valid={len(valid_masks)} "
            f"minimal={len(minimal_masks)} orbits={len(rows)}"
        )

    print("order-seven i=4 completion table: PASS")


if __name__ == "__main__":
    main()
