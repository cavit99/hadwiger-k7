#!/usr/bin/env python3
"""Exhaust the justified eight-cell model-anchored contact quotients."""

from __future__ import annotations

from itertools import combinations, product


NAMES = ("Y", "R0", "P", "B", "C", "U2", "U3", "U4")
ORDER = len(NAMES)
Y, R0, P, B, C, U2, U3, U4 = range(ORDER)
FOREIGN = (P, B, C, U2, U3, U4)
POSSIBLE_FAR = (B, C, U2, U3, U4)

# For an old R--D contact, the split bag can meet D on the Y side, the R0
# side, or both sides.  At least one contact is compulsory.
Y_ONLY, R0_ONLY, BOTH = range(3)
CONTACTS = {
    Y_ONLY: (True, False),
    R0_ONLY: (False, True),
    BOTH: (True, True),
}


def empty_graph() -> list[int]:
    return [0] * ORDER


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def has_edge(adjacency: list[int], left: int, right: int) -> bool:
    return bool(adjacency[left] & (1 << right))


def base_graph() -> list[int]:
    """Return the fixed contacts after splitting the universal bag R."""

    adjacency = empty_graph()
    add_edge(adjacency, Y, R0)

    # B,C,U2,U3,U4 are five members of the foreign K6 and hence form K5.
    dense_foreign = (B, C, U2, U3, U4)
    for left, right in combinations(dense_foreign, 2):
        add_edge(adjacency, left, right)

    # P is universal only to the four old universal bags.  R has been split.
    for universal in (U2, U3, U4):
        add_edge(adjacency, P, universal)
    return adjacency


def make_profile(statuses: tuple[int, ...]) -> list[int]:
    adjacency = base_graph()
    for bag, status in zip(FOREIGN, statuses, strict=True):
        on_y, on_r0 = CONTACTS[status]
        if on_y:
            add_edge(adjacency, Y, bag)
        if on_r0:
            add_edge(adjacency, R0, bag)
    return adjacency


def missing_edges(adjacency: list[int], vertices: tuple[int, ...]) -> int:
    return sum(
        not has_edge(adjacency, left, right)
        for left, right in combinations(vertices, 2)
    )


def has_k7_minus_minor(adjacency: list[int]) -> bool:
    """Test K7-minus exactly on an eight-vertex quotient."""

    vertices = tuple(range(ORDER))

    # Seven singleton branch sets.
    for omitted in vertices:
        retained = tuple(vertex for vertex in vertices if vertex != omitted)
        if missing_edges(adjacency, retained) <= 1:
            return True

    # One connected two-vertex branch set and six singleton branch sets.
    for left, right in combinations(vertices, 2):
        if not has_edge(adjacency, left, right):
            continue
        retained = tuple(vertex for vertex in vertices if vertex not in (left, right))
        missing = missing_edges(adjacency, retained)
        missing += sum(
            not (
                has_edge(adjacency, left, vertex)
                or has_edge(adjacency, right, vertex)
            )
            for vertex in retained
        )
        if missing <= 1:
            return True
    return False


def clique_number(adjacency: list[int]) -> int:
    vertices = tuple(range(ORDER))
    for size in range(ORDER, 0, -1):
        if any(
            missing_edges(adjacency, chosen) == 0
            for chosen in combinations(vertices, size)
        ):
            return size
    raise AssertionError("the empty graph still has one-vertex cliques")


def minimum_degree(adjacency: list[int]) -> int:
    return min(map(int.bit_count, adjacency))


def edge_names(adjacency: list[int]) -> tuple[str, ...]:
    return tuple(
        f"{NAMES[left]}-{NAMES[right]}"
        for left, right in combinations(range(ORDER), 2)
        if has_edge(adjacency, left, right)
    )


def possible_mate_cells(adjacency: list[int], endpoint_cell: int) -> tuple[int, ...]:
    """Cells in which an incident coordinate mate can occur statically.

    A mate in the same cell gives an internal coordinate edge.  A mate in
    another cell requires that the restored quotient contain that contact.
    The quotient does not assert that an internal branch-set connection uses
    the coordinate edge; the exact model already lives in its deletion host.
    """

    return tuple(
        cell
        for cell in range(ORDER)
        if cell == endpoint_cell or has_edge(adjacency, endpoint_cell, cell)
    )


def contract_split(adjacency: list[int]) -> list[int]:
    """Contract Y--R0 and return the seven-cell adjacency matrix."""

    old_cells = ((Y, R0), (P,), (B,), (C,), (U2,), (U3,), (U4,))
    contracted = [0] * len(old_cells)
    for i, j in combinations(range(len(old_cells)), 2):
        if any(
            has_edge(adjacency, left, right)
            for left in old_cells[i]
            for right in old_cells[j]
        ):
            contracted[i] |= 1 << j
            contracted[j] |= 1 << i
    return contracted


def is_exact_k7_vee_after_contraction(adjacency: list[int]) -> bool:
    contracted = contract_split(adjacency)
    missing = {
        (left, right)
        for left, right in combinations(range(7), 2)
        if not bool(contracted[left] & (1 << right))
    }
    # Contracted order: R,P,B,C,U2,U3,U4.  Only P--B and P--C are absent.
    return missing == {(1, 2), (1, 3)}


def profile_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for far in POSSIBLE_FAR:
        counts = {"admissible": 0, "target_free": 0}
        best: tuple[int, tuple[int, ...], list[int]] | None = None
        distinct_mate_pair_counts: list[int] = []
        common_mate_counts: list[int] = []

        for statuses in product(CONTACTS, repeat=len(FOREIGN)):
            status = dict(zip(FOREIGN, statuses, strict=True))

            # The named far bag is anticomplete to Y, while the old
            # R--far contact survives through R0.
            if status[far] != R0_ONLY:
                continue

            # The nominated coordinate endpoints p in Y and q in R0 were
            # both selected as P-neighbours.  Thus P contacts both pieces.
            if status[P] != BOTH:
                continue

            adjacency = make_profile(statuses)
            assert is_exact_k7_vee_after_contraction(adjacency)
            assert not has_edge(adjacency, Y, far)
            assert has_edge(adjacency, R0, far)
            counts["admissible"] += 1

            if has_k7_minus_minor(adjacency):
                continue
            counts["target_free"] += 1

            p_mates = set(possible_mate_cells(adjacency, Y))
            q_mates = set(possible_mate_cells(adjacency, R0))
            # The singleton signature of qq* is exterior-proper on Y only
            # when q's mate lies in Y.  Every profile permits that placement
            # statically because Y and R0 are adjacent.
            assert Y in q_mates
            # Equal cell labels still permit two distinct actual mate
            # vertices inside one connected branch set.
            distinct_mate_pair_counts.append(len(p_mates) * len(q_mates))
            # This is the cell support if p,q are the leaves of the sole
            # possible induced P3 and hence have one common mate.
            common_mate_counts.append(len(p_mates & q_mates))

            candidate = (minimum_degree(adjacency), statuses, adjacency)
            if best is None or candidate[:2] > best[:2]:
                best = candidate

        assert best is not None
        rows.append(
            {
                "far": NAMES[far],
                **counts,
                "best_min_degree": best[0],
                "best_statuses": best[1],
                "best_edges": edge_names(best[2]),
                "best_omega": clique_number(best[2]),
                "mate_pairs_min": min(distinct_mate_pair_counts),
                "mate_pairs_max": max(distinct_mate_pair_counts),
                "common_mate_min": min(common_mate_counts),
                "common_mate_max": max(common_mate_counts),
            }
        )
    return rows


def saturated_twin_far_survivor() -> list[int]:
    """Return the strongest retaining-core contact profile.

    P,U2,U3,U4 meet both pieces, R0 retains every old foreign contact, and
    Y is anticomplete precisely to the two deficient twins B,C.
    """

    statuses = (BOTH, R0_ONLY, R0_ONLY, BOTH, BOTH, BOTH)
    adjacency = make_profile(statuses)
    assert is_exact_k7_vee_after_contraction(adjacency)
    assert all(has_edge(adjacency, R0, bag) for bag in FOREIGN)
    assert all(has_edge(adjacency, Y, bag) for bag in (P, U2, U3, U4))
    assert all(not has_edge(adjacency, Y, bag) for bag in (B, C))
    # Realise the eight cells as singleton vertices and nominate Y--R0 as
    # the selected edge.  Then R0 dominates Y's actual neighbourhood, and
    # both selected ends are already visible to P.  This is stronger than
    # a generic cell-adjacency inference and is asserted only for this
    # singleton realisation.
    assert has_edge(adjacency, Y, R0)
    assert all(
        has_edge(adjacency, R0, vertex)
        for vertex in range(ORDER)
        if vertex != R0 and has_edge(adjacency, Y, vertex)
    )
    assert has_edge(adjacency, P, Y)
    assert has_edge(adjacency, P, R0)
    assert not has_k7_minus_minor(adjacency)
    assert minimum_degree(adjacency) == 5
    assert clique_number(adjacency) == 6
    return adjacency


def verify_retaining_core_family() -> tuple[int, int]:
    """Check the direct retaining-core subfamily.

    R0 retains every old contact, while Y misses both deficient twins.
    Only the three optional Y--Ui contacts remain free.
    """

    total = 0
    target_free = 0
    for universal_statuses in product((R0_ONLY, BOTH), repeat=3):
        statuses = (BOTH, R0_ONLY, R0_ONLY, *universal_statuses)
        adjacency = make_profile(statuses)
        assert all(has_edge(adjacency, R0, bag) for bag in FOREIGN)
        assert all(not has_edge(adjacency, Y, bag) for bag in (B, C))
        total += 1
        target_free += not has_k7_minus_minor(adjacency)
    assert (total, target_free) == (8, 8)
    return total, target_free


def verify_positive_control() -> None:
    """Check that one extra twin contact triggers the expected target."""

    # Y misses B but meets C; every other split contact is doubled.
    statuses = (BOTH, R0_ONLY, BOTH, BOTH, BOTH, BOTH)
    adjacency = make_profile(statuses)
    assert is_exact_k7_vee_after_contraction(adjacency)
    assert has_k7_minus_minor(adjacency)


def main() -> None:
    rows = profile_rows()
    observed = {
        row["far"]: (row["admissible"], row["target_free"])
        for row in rows
    }
    expected = {
        "B": (81, 51),
        "C": (81, 51),
        "U2": (81, 48),
        "U3": (81, 48),
        "U4": (81, 48),
    }
    assert observed == expected, observed
    saturated = saturated_twin_far_survivor()
    mate_ranges = {
        row["far"]: (
            row["mate_pairs_min"],
            row["mate_pairs_max"],
            row["common_mate_min"],
            row["common_mate_max"],
        )
        for row in rows
    }
    expected_mate_ranges = {
        "B": (24, 48, 3, 6),
        "C": (24, 48, 3, 6),
        "U2": (24, 42, 3, 5),
        "U3": (24, 42, 3, 5),
        "U4": (24, 42, 3, 5),
    }
    assert mate_ranges == expected_mate_ranges, mate_ranges

    saturated_p_mates = possible_mate_cells(saturated, Y)
    saturated_q_mates = possible_mate_cells(saturated, R0)
    assert tuple(NAMES[cell] for cell in saturated_p_mates) == (
        "Y",
        "R0",
        "P",
        "U2",
        "U3",
        "U4",
    )
    assert saturated_q_mates == tuple(range(ORDER))
    retaining_total, retaining_target_free = verify_retaining_core_family()
    verify_positive_control()

    print("GREEN model-anchored terminal quotient gate")
    print("endpoint_labels=p_in_Y,q_in_R0; both_are_P_neighbours")
    print("response_cube_encoded=false")
    print("second_coordinate_response_visible_only_when_q_mate_in_Y")
    print("host_connectivity_encoded=false")
    print("positive_target_control=true")
    for row in rows:
        print(
            " ".join(
                (
                    f"far={row['far']}",
                    f"admissible={row['admissible']}",
                    f"target_free={row['target_free']}",
                    f"best_delta={row['best_min_degree']}",
                    f"best_omega={row['best_omega']}",
                    f"mate_pairs={row['mate_pairs_min']}..{row['mate_pairs_max']}",
                    f"common_mates={row['common_mate_min']}..{row['common_mate_max']}",
                )
            )
        )
    print("saturated_survivor=K8_minus_K2,2")
    print("saturated_singleton_realisation_has_dominated_Y_R0_edge=true")
    print("saturated_both_edge_ends_already_P_visible=true")
    print(
        f"retaining_core_profiles={retaining_total} "
        f"retaining_core_target_free={retaining_target_free}"
    )
    print("saturated_missing=Y-B,Y-C,P-B,P-C")
    print(
        "saturated_p_mate_cells="
        + ",".join(NAMES[cell] for cell in saturated_p_mates)
    )
    print(
        "saturated_q_mate_cells="
        + ",".join(NAMES[cell] for cell in saturated_q_mates)
    )
    print("saturated_distinct_mate_cell_pairs=48 common_mate_cells=6")
    print("saturated_same_coordinate_edge_possible=true")
    print("saturated_edges=" + ",".join(edge_names(saturated)))


if __name__ == "__main__":
    main()
