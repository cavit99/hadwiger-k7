#!/usr/bin/env python3
"""Analyse two prescribed centre contacts in the all-terminal order-nine case.

The source catalogue has nine terminals: seven vertices of Q and two
protected centres.  For every static composition failure, this diagnostic
adds a possible contact from each protected centre to a Q-rooted bag and
records the exact forcing relation on the 7 by 7 set of contact pairs.
"""

from __future__ import annotations

import collections
from functools import lru_cache
import hashlib
import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


order9 = load(
    "two_protected_order_nine",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_kernel"
    / "verify_order_nine.py",
)


def add_contacts(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    contacts: tuple[int | None, int | None],
) -> tuple[int, ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    answer = list(adjacency)
    for centre, contact in zip(centres, contacts, strict=True):
        if contact is None:
            continue
        root = roots[contact]
        answer[centre] |= 1 << root
        answer[root] |= 1 << centre
    return tuple(answer)


@lru_cache(maxsize=None)
def contact_family(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    contacts: tuple[int | None, int | None],
) -> tuple[tuple[int, ...], ...]:
    return order9.quotient_family(add_contacts(adjacency, centres, contacts), centres)


def closes(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    contacts: tuple[int | None, int | None],
) -> bool:
    augmented = add_contacts(adjacency, centres, contacts)
    if any(
        order9.has_target(
            tuple(q_graph[vertex] | quotient[vertex] for vertex in range(7))
        )
        for quotient in contact_family(adjacency, centres, contacts)
    ):
        return True
    return order9.has_k7_minus(
        order9.overlay_q_on_carrier(augmented, centres, q_graph)
    )


def balanced_bad_rectangle(rows: tuple[int, ...]) -> int:
    """Largest k with a k by k rectangle containing no forcing pair."""

    bad_rows = tuple(0x7F ^ row for row in rows)
    for size in range(7, 0, -1):
        for selected in itertools.combinations(range(7), size):
            common = 0x7F
            for left in selected:
                common &= bad_rows[left]
            if common.bit_count() >= size:
                return size
    return 0


def bad_rectangle_profile(rows: tuple[int, ...]) -> tuple[int, ...]:
    """For each positive row-set size, maximise common nonforcing columns."""

    bad_rows = tuple(0x7F ^ row for row in rows)
    maxima = []
    for size in range(1, 8):
        maximum = 0
        for selected in itertools.combinations(range(7), size):
            common = 0x7F
            for left in selected:
                common &= bad_rows[left]
            maximum = max(maximum, common.bit_count())
        maxima.append(maximum)
    return tuple(maxima)


def largest_bad_rectangle(
    profile: tuple[int, ...],
) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Return the maximum area and all dimensions attaining it."""

    area = max((left + 1) * right for left, right in enumerate(profile))
    dimensions = tuple(
        (left + 1, right)
        for left, right in enumerate(profile)
        if (left + 1) * right == area
    )
    return area, dimensions


def orbit_digest(orbits: set[tuple[object, ...]]) -> str:
    """Digest a set of canonical fixed-Q configurations deterministically."""

    return hashlib.sha256(repr(sorted(orbits)).encode("ascii")).hexdigest()


def bad_five_rectangles(rows: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    """Return all pairs of five-sets whose Cartesian product is nonforcing."""

    bad_rows = tuple(0x7F ^ row for row in rows)
    answer = []
    for selected in itertools.combinations(range(7), 5):
        common = 0x7F
        for left in selected:
            common &= bad_rows[left]
        for right in itertools.combinations(
            (vertex for vertex in range(7) if common >> vertex & 1),
            5,
        ):
            answer.append(
                (
                    sum(1 << vertex for vertex in selected),
                    sum(1 << vertex for vertex in right),
                )
            )
    return tuple(answer)


def canonical_omitted_pair_profile(
    canonical_q: tuple[int, ...],
    q_graph: tuple[int, ...],
    left_five: int,
    right_five: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Canonicalise the two omitted Q-pairs under one fixed-Q isomorphism."""

    encodings = []
    for permutation in order9.isomorphisms_to_copy(canonical_q, q_graph):
        omitted = []
        for five in (left_five, right_five):
            pair = tuple(
                vertex
                for vertex in range(7)
                if not (five >> permutation[vertex] & 1)
            )
            assert len(pair) == 2
            omitted.append(pair)
        encodings.append(tuple(omitted))
    return min(encodings)


def canonical_bad_contact_profile(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    canonical_q: tuple[int, ...],
    q_graph: tuple[int, ...],
    left_five: int,
    right_five: int,
) -> tuple[object, ...]:
    """Record a bad rectangle and the two existing centre contact sets."""

    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    encodings = []
    for permutation in order9.isomorphisms_to_copy(canonical_q, q_graph):
        omitted = []
        contacts = []
        for index, five in enumerate((left_five, right_five)):
            omitted.append(
                tuple(
                    vertex
                    for vertex in range(7)
                    if not (five >> permutation[vertex] & 1)
                )
            )
            centre = centres[index]
            contacts.append(
                tuple(
                    vertex
                    for vertex in range(7)
                    if adjacency[centre] >> roots[permutation[vertex]] & 1
                )
            )
        encodings.append(
            (
                tuple(omitted),
                tuple(contacts),
                bool(adjacency[centres[0]] >> centres[1] & 1),
                tuple(adjacency[centre].bit_count() for centre in centres),
            )
        )
    return min(encodings)


def update_digest(
    digest: hashlib._Hash,
    carrier_index: int,
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    rows: tuple[int, ...],
) -> None:
    digest.update(carrier_index.to_bytes(1, "big"))
    digest.update(bytes(centres))
    digest.update(bytes(q_graph))
    digest.update(bytes(rows))


def main() -> None:
    carriers = order9.minimal_three_connected_graphs()
    by_code = dict(order9.order11.carrier7.eligible_graphs())
    copies = {
        code: order9.order11.q_copies(by_code[code])
        for code in ("FCQ`_", "FCQb_", "FCp`_")
    }

    expected_failures = {"FCQ`_": 427, "FCQb_": 1_446, "FCp`_": 379}
    for code, q_copies in copies.items():
        failures = 0
        killed_by_first = 0
        killed_by_second = 0
        killed_by_either_single = 0
        forcing_sizes = collections.Counter()
        forcing_projections = collections.Counter()
        single_forcing_sizes = collections.Counter()
        bad_rectangles = collections.Counter()
        bad_rectangle_profiles = collections.Counter()
        bad_five_orbits = set()
        first_bad_five = None
        largest_rectangle_types = collections.Counter()
        maximum_area = 0
        maximum_area_orbits = set()
        bad_five_pair_profiles = collections.Counter()
        bad_five_contact_profiles = collections.Counter()
        bad_five_rectangle_count = 0
        digest = hashlib.sha256()

        for carrier_index, adjacency in enumerate(carriers):
            for centres in itertools.combinations(range(9), 2):
                baseline = order9.quotient_family(adjacency, centres)
                for q_graph in q_copies:
                    if any(
                        order9.has_target(
                            tuple(
                                q_graph[vertex] | quotient[vertex]
                                for vertex in range(7)
                            )
                        )
                        for quotient in baseline
                    ):
                        continue
                    if order9.has_k7_minus(
                        order9.overlay_q_on_carrier(adjacency, centres, q_graph)
                    ):
                        continue

                    failures += 1
                    first = tuple(
                        closes(adjacency, centres, q_graph, (root, None))
                        for root in range(7)
                    )
                    second = tuple(
                        closes(adjacency, centres, q_graph, (None, root))
                        for root in range(7)
                    )
                    rows = tuple(
                        sum(
                            1 << right
                            for right in range(7)
                            if closes(
                                adjacency,
                                centres,
                                q_graph,
                                (left, right),
                            )
                        )
                        for left in range(7)
                    )
                    assert any(rows)

                    first_closes = any(first)
                    second_closes = any(second)
                    killed_by_first += first_closes
                    killed_by_second += second_closes
                    killed_by_either_single += first_closes or second_closes
                    forcing_sizes[sum(row.bit_count() for row in rows)] += 1
                    single_forcing_sizes[
                        (sum(first), sum(second))
                    ] += 1
                    possible_right = 0
                    for row in rows:
                        possible_right |= row
                    forcing_projections[
                        (
                            sum(bool(row) for row in rows),
                            possible_right.bit_count(),
                        )
                    ] += 1
                    bad_rectangles[balanced_bad_rectangle(rows)] += 1
                    rectangle_profile = bad_rectangle_profile(rows)
                    bad_rectangle_profiles[rectangle_profile] += 1
                    area, dimensions = largest_bad_rectangle(rectangle_profile)
                    largest_rectangle_types[(area, dimensions)] += 1
                    canonical = order9.canonical_fixed_q_configuration(
                        adjacency,
                        centres,
                        by_code[code],
                        q_graph,
                    )
                    if area > maximum_area:
                        maximum_area = area
                        maximum_area_orbits = {canonical}
                    elif area == maximum_area:
                        maximum_area_orbits.add(canonical)
                    if rectangle_profile[4] >= 5:
                        bad_five_orbits.add(canonical)
                        for left_five, right_five in bad_five_rectangles(rows):
                            bad_five_rectangle_count += 1
                            bad_five_pair_profiles[
                                canonical_omitted_pair_profile(
                                    by_code[code],
                                    q_graph,
                                    left_five,
                                    right_five,
                                )
                            ] += 1
                            bad_five_contact_profiles[
                                canonical_bad_contact_profile(
                                    adjacency,
                                    centres,
                                    by_code[code],
                                    q_graph,
                                    left_five,
                                    right_five,
                                )
                            ] += 1
                        if first_bad_five is None:
                            first_bad_five = (
                                carrier_index,
                                centres,
                                q_graph,
                                rows,
                                rectangle_profile,
                            )
                    update_digest(digest, carrier_index, centres, q_graph, rows)

        assert failures == expected_failures[code]
        assert bad_rectangles.get(7, 0) == 0
        print(
            code,
            f"static_failures={failures}",
            f"some_first_contact_closes={killed_by_first}",
            f"some_second_contact_closes={killed_by_second}",
            f"some_single_contact_closes={killed_by_either_single}",
        )
        print(code, "forcing_pair_sizes", sorted(forcing_sizes.items()))
        print(code, "forcing_projection_sizes", sorted(forcing_projections.items()))
        print(code, "single_forcing_set_sizes", sorted(single_forcing_sizes.items()))
        print(code, "largest_nonforcing_square", sorted(bad_rectangles.items()))
        global_profile = tuple(
            max(profile[index] for profile in bad_rectangle_profiles)
            for index in range(7)
        )
        print(code, "global_bad_rectangle_profile", global_profile)
        print(
            code,
            "largest_bad_rectangle_types",
            sorted(largest_rectangle_types.items()),
        )
        print(
            code,
            "global_maximum_bad_rectangle",
            f"area={maximum_area}",
            f"fixed_Q_orbits={len(maximum_area_orbits)}",
            f"orbit_digest={orbit_digest(maximum_area_orbits)}",
        )
        print(
            code,
            "bad_5_by_5",
            f"labelled={sum(count for profile, count in bad_rectangle_profiles.items() if profile[4] >= 5)}",
            f"fixed_Q_orbits={len(bad_five_orbits)}",
            f"orbit_digest={orbit_digest(bad_five_orbits)}",
            f"first={first_bad_five}",
        )
        print(
            code,
            "bad_5_by_5_omitted_pair_profiles",
            f"rectangles={bad_five_rectangle_count}",
            sorted(bad_five_pair_profiles.items()),
        )
        print(
            code,
            "bad_5_by_5_contact_profiles",
            sorted(bad_five_contact_profiles.items()),
        )
        print(code, "forcing_relation_digest", digest.hexdigest())

    print("contact_family_cache", contact_family.cache_info())
    print("minor_cache", order9.has_target.cache_info())
    print("k7minus_cache", order9.has_k7_minus.cache_info())


if __name__ == "__main__":
    main()
