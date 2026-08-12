#!/usr/bin/env python3
"""Exact composition for all-terminal nine-root kernels.

Every simple three-connected graph on nine terminals contains a spanning
edge-minimal three-connected subgraph.  This verifier generates all such
unlabelled subgraphs, places the two protected centres in every pair of
vertices, and checks every labelled copy of each live seven-vertex graph Q
on the remaining roots.  The centre bags are assigned in every connected
way to the seven Q-rooted bags before an exact K_5^- minor test.
"""

from __future__ import annotations

import collections
import functools
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


exact8 = load(
    "eight_terminal_exact_catalogue",
    ROOT / "active" / "hc7_eight_terminal_exact_bundle_catalogue.py",
)
order11 = load("nine_terminal_order11", HERE / "verify_order_eleven.py")
base = order11.base


def minimal_three_connected_graphs():
    answer = []
    for adjacency in exact8.geng(9):
        if not exact8.three_connected(adjacency):
            continue
        if any(
            exact8.three_connected(exact8.delete_edge(adjacency, left, right))
            for left, right in exact8.edges(adjacency)
        ):
            continue
        answer.append(adjacency)
    assert len(answer) == 57
    assert collections.Counter(
        sum(1 for _ in exact8.edges(graph)) for graph in answer
    ) == {14: 19, 15: 30, 16: 6, 17: 1, 18: 1}
    return tuple(answer)


def quotient_family(
    adjacency: tuple[int, ...], centres: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    outcomes = set()
    for owners in itertools.product(range(7), repeat=2):
        groups = [{root} for root in roots]
        for centre, owner in zip(centres, owners, strict=True):
            groups[owner].add(centre)
        if not all(order11.group_is_connected(adjacency, group) for group in groups):
            continue
        quotient = [0] * 7
        for left, right in itertools.combinations(range(7), 2):
            if any(
                adjacency[u] >> v & 1
                for u in groups[left]
                for v in groups[right]
            ):
                quotient[left] |= 1 << right
                quotient[right] |= 1 << left
        outcomes.add(tuple(quotient))
    return tuple(
        sorted(
            outcomes,
            key=lambda graph: sum(row.bit_count() for row in graph),
            reverse=True,
        )
    )


@functools.lru_cache(maxsize=None)
def has_target(adjacency: tuple[int, ...]) -> bool:
    return base.has_dense_minor(adjacency, 5, 9)


@functools.lru_cache(maxsize=None)
def has_k7_minus(adjacency: tuple[int, ...]) -> bool:
    return base.has_dense_minor(adjacency, 7, 20)


def overlay_q_on_carrier(
    adjacency: tuple[int, ...], centres: tuple[int, int], q_graph: tuple[int, ...]
) -> tuple[int, ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    answer = list(adjacency)
    for left, right in itertools.combinations(range(7), 2):
        if q_graph[left] >> right & 1:
            old_left, old_right = roots[left], roots[right]
            answer[old_left] |= 1 << old_right
            answer[old_right] |= 1 << old_left
    return tuple(answer)


def add_two_coordinate_contacts(
    adjacency: tuple[int, ...], centres: tuple[int, int], contacts: tuple[int, int]
) -> tuple[int, ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    answer = list(adjacency)
    for centre, contact in zip(centres, contacts, strict=True):
        old_root = roots[contact]
        answer[centre] |= 1 << old_root
        answer[old_root] |= 1 << centre
    return tuple(answer)


def two_contact_quotient_family(
    adjacency: tuple[int, ...], centres: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    outcomes = {
        quotient
        for contacts in itertools.product(range(7), repeat=2)
        for quotient in quotient_family(
            add_two_coordinate_contacts(adjacency, centres, contacts), centres
        )
    }
    return tuple(
        sorted(
            outcomes,
            key=lambda graph: sum(row.bit_count() for row in graph),
            reverse=True,
        )
    )


def one_contact_quotient_family(
    adjacency: tuple[int, ...], centres: tuple[int, int], selected: int
) -> tuple[tuple[int, ...], ...]:
    outcomes = {
        quotient
        for contact in range(7)
        for quotient in quotient_family(
            add_two_coordinate_contacts(
                adjacency,
                centres,
                (contact, 0) if selected == 0 else (0, contact),
            ),
            centres,
        )
    }
    return tuple(
        sorted(
            outcomes,
            key=lambda graph: sum(row.bit_count() for row in graph),
            reverse=True,
        )
    )


@functools.lru_cache(maxsize=None)
def isomorphisms_to_copy(
    canonical: tuple[int, ...], copy: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    answer = []
    for permutation in itertools.permutations(range(7)):
        if all(
            bool(canonical[left] >> right & 1)
            == bool(copy[permutation[left]] >> permutation[right] & 1)
            for left, right in itertools.combinations(range(7), 2)
        ):
            answer.append(permutation)
    assert answer
    return tuple(answer)


def canonical_fixed_q_configuration(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    canonical_q: tuple[int, ...],
    q_graph: tuple[int, ...],
) -> int:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    encodings = []
    for permutation in isomorphisms_to_copy(canonical_q, q_graph):
        for ordered_centres in (centres, centres[::-1]):
            old_to_new = {
                roots[permutation[new]]: new for new in range(7)
            }
            old_to_new[ordered_centres[0]] = 7
            old_to_new[ordered_centres[1]] = 8
            mask = 0
            for old_left, old_right in itertools.combinations(range(9), 2):
                if not (adjacency[old_left] >> old_right & 1):
                    continue
                new_left, new_right = sorted(
                    (old_to_new[old_left], old_to_new[old_right])
                )
                position = sum(8 - first for first in range(new_left))
                position += new_right - new_left - 1
                mask |= 1 << position
            encodings.append(mask)
    return min(encodings)


def main() -> None:
    carriers = minimal_three_connected_graphs()
    by_code = dict(order11.carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    copies = {code: order11.q_copies(by_code[code]) for code in live_codes}

    tests = collections.Counter()
    failures = collections.Counter()
    direct_targets = collections.Counter()
    first_failure = {}
    failure_carriers = {code: collections.Counter() for code in live_codes}
    failure_centre_pairs = {code: collections.Counter() for code in live_codes}
    two_contact_survivors = collections.Counter()
    two_contact_first = {}
    two_contact_orbits = {code: set() for code in live_codes}
    one_contact_survivors = {code: collections.Counter() for code in live_codes}
    survivor_degree_profiles = {
        code: collections.Counter() for code in live_codes
    }
    asymmetric_profiles = {code: collections.Counter() for code in live_codes}
    family_sizes = collections.Counter()
    for carrier_index, adjacency in enumerate(carriers):
        for centres in itertools.combinations(range(9), 2):
            quotients = quotient_family(adjacency, centres)
            assert quotients
            augmented_quotients = None
            family_sizes[len(quotients)] += 1
            for code in live_codes:
                for q_graph in copies[code]:
                    tests[code] += 1
                    if any(
                        has_target(
                            tuple(
                                q_graph[vertex] | quotient[vertex]
                                for vertex in range(7)
                            )
                        )
                        for quotient in quotients
                    ):
                        continue
                    if has_k7_minus(
                        overlay_q_on_carrier(adjacency, centres, q_graph)
                    ):
                        direct_targets[code] += 1
                        continue
                    failures[code] += 1
                    failure_carriers[code][carrier_index] += 1
                    failure_centre_pairs[code][centres] += 1
                    degrees = tuple(
                        sorted(adjacency[centre].bit_count() for centre in centres)
                    )
                    centre_edge = bool(adjacency[centres[0]] >> centres[1] & 1)
                    survivor_degree_profiles[code][(degrees, centre_edge)] += 1
                    first_failure.setdefault(
                        code, (carrier_index, centres, q_graph)
                    )
                    if augmented_quotients is None:
                        augmented_quotients = two_contact_quotient_family(
                        adjacency, centres
                        )
                    single_closes = []
                    for selected in range(2):
                        single_quotients = one_contact_quotient_family(
                            adjacency, centres, selected
                        )
                        single_closes.append(
                            any(
                                has_target(
                                    tuple(
                                        q_graph[vertex] | quotient[vertex]
                                        for vertex in range(7)
                                    )
                                )
                                for quotient in single_quotients
                            )
                        )
                    one_contact_survivors[code][tuple(single_closes)] += 1
                    if not all(single_closes):
                        asymmetric_profiles[code][
                            (
                                tuple(
                                    adjacency[centre].bit_count()
                                    for centre in centres
                                ),
                                centre_edge,
                                carrier_index,
                            )
                        ] += 1
                    if any(
                        has_target(
                            tuple(
                                q_graph[vertex] | quotient[vertex]
                                for vertex in range(7)
                            )
                        )
                        for quotient in augmented_quotients
                    ):
                        continue
                    if any(
                        has_k7_minus(
                            overlay_q_on_carrier(
                                add_two_coordinate_contacts(
                                    adjacency, centres, contacts
                                ),
                                centres,
                                q_graph,
                            )
                        )
                        for contacts in itertools.product(range(7), repeat=2)
                    ):
                        continue
                    two_contact_survivors[code] += 1
                    two_contact_first.setdefault(
                        code, (carrier_index, centres, q_graph)
                    )
                    two_contact_orbits[code].add(
                        canonical_fixed_q_configuration(
                            adjacency,
                            centres,
                            by_code[code],
                            q_graph,
                        )
                    )

    placements = 57 * 36
    assert sum(family_sizes.values()) == placements
    assert tests == {
        code: placements * len(copies[code]) for code in live_codes
    }
    print("minimal_three_connected_carriers", len(carriers))
    print("protected_centre_placements", placements)
    print("q_copy_counts", {code: len(copies[code]) for code in live_codes})
    print("quotient_family_sizes", dict(sorted(family_sizes.items())))
    print("tests", dict(tests))
    print("direct_targets", dict(direct_targets))
    print("failures", dict(failures))
    print(
        "failure_carriers",
        {code: dict(profile) for code, profile in failure_carriers.items()},
    )
    print(
        "failure_centre_pairs",
        {code: dict(profile) for code, profile in failure_centre_pairs.items()},
    )
    print("first_failure", first_failure)
    print("two_contact_survivors", dict(two_contact_survivors))
    print(
        "one_contact_survivor_counts",
        {code: dict(profile) for code, profile in one_contact_survivors.items()},
    )
    print(
        "survivor_degree_profiles",
        {code: dict(profile) for code, profile in survivor_degree_profiles.items()},
    )
    print(
        "asymmetric_profiles",
        {code: dict(profile) for code, profile in asymmetric_profiles.items()},
    )
    print("two_contact_first", two_contact_first)
    print(
        "two_contact_fixed_q_orbits",
        {code: len(orbits) for code, orbits in two_contact_orbits.items()},
    )
    print("minor_cache", has_target.cache_info())
    print("k7minus_cache", has_k7_minus.cache_info())


if __name__ == "__main__":
    main()
