#!/usr/bin/env python3
"""Test a protected-root bag split carrying a swallowed matching mate.

For every static failure in the all-terminal order-nine catalogue, choose a
protected centre `w`.  A suffix of its rooted branch bag owns a set `O` of
at least two quotient adjacencies and is absorbed into an owned Q-rooted bag
`q`.  At quotient level this removes the edges from `w` to `O`, restores
`wq` through the matching edge, and transfers every other edge in `O` to
`q`.  The diagnostic tests every such ownership pattern.

The quotient operation is exact once the rooted suffix and its ownership
set exist.  This script does not prove that a host model supplies a suffix
with any particular ownership pattern.
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
    "swallowed_mate_order_nine",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_kernel"
    / "verify_order_nine.py",
)


def transfer_suffix(
    adjacency: tuple[int, ...],
    centre: int,
    owned: int,
    absorb: int,
) -> tuple[int, ...]:
    """Transfer the centre-bag suffix and absorb it at `absorb`."""

    assert owned >> absorb & 1
    answer = list(adjacency)
    for neighbour in range(9):
        if not (owned >> neighbour & 1):
            continue
        answer[centre] &= ~(1 << neighbour)
        answer[neighbour] &= ~(1 << centre)
        if neighbour != absorb:
            answer[absorb] |= 1 << neighbour
            answer[neighbour] |= 1 << absorb
    answer[centre] |= 1 << absorb
    answer[absorb] |= 1 << centre
    return tuple(answer)


@lru_cache(maxsize=None)
def closes(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    selected: int,
    owned: int,
    absorb: int,
) -> bool:
    transformed = transfer_suffix(adjacency, centres[selected], owned, absorb)
    if order9.has_k7_minus(
        order9.overlay_q_on_carrier(transformed, centres, q_graph)
    ):
        return True
    return any(
        order9.has_target(
            tuple(q_graph[vertex] | quotient[vertex] for vertex in range(7))
        )
        for quotient in order9.quotient_family(transformed, centres)
    )


def ownership_patterns(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    selected: int,
    q_only: bool,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    centre = centres[selected]
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    allowed = adjacency[centre]
    if q_only:
        allowed &= sum(1 << root for root in roots)
    neighbours = tuple(vertex for vertex in range(9) if allowed >> vertex & 1)
    answer = []
    for size in range(2, len(neighbours) + 1):
        for chosen in itertools.combinations(neighbours, size):
            owned = sum(1 << vertex for vertex in chosen)
            absorptions = tuple(vertex for vertex in roots if owned >> vertex & 1)
            if absorptions:
                answer.append((owned, absorptions))
    return tuple(answer)


def analyse_mode(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    q_only: bool,
) -> tuple[bool, bool, tuple[bool, bool], tuple[int, int]]:
    """Return existential and ownership-robust closure information."""

    existential = []
    robust = []
    failed_ownerships = []
    for selected in range(2):
        patterns = ownership_patterns(adjacency, centres, selected, q_only)
        pattern_outcomes = []
        failures = 0
        for owned, absorptions in patterns:
            outcome = any(
                closes(
                    adjacency,
                    centres,
                    q_graph,
                    selected,
                    owned,
                    absorb,
                )
                for absorb in absorptions
            )
            pattern_outcomes.append(outcome)
            failures += not outcome
        existential.append(any(pattern_outcomes))
        robust.append(bool(pattern_outcomes) and all(pattern_outcomes))
        failed_ownerships.append(failures)
    return (
        any(existential),
        any(robust),
        tuple(robust),
        tuple(failed_ownerships),
    )


def update_digest(
    digest,
    carrier_index: int,
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    mode_result: tuple[object, ...],
) -> None:
    digest.update(carrier_index.to_bytes(1, "big"))
    digest.update(bytes(centres))
    digest.update(bytes(q_graph))
    digest.update(repr(mode_result).encode("ascii"))


def main() -> None:
    carriers = order9.minimal_three_connected_graphs()
    by_code = dict(order9.order11.carrier7.eligible_graphs())
    expected = {"FCQ`_": 427, "FCQb_": 1_446, "FCp`_": 379}

    for code in expected:
        copies = order9.order11.q_copies(by_code[code])
        static = 0
        results = {
            False: collections.Counter(),
            True: collections.Counter(),
        }
        existential_failure_orbits = {False: set(), True: set()}
        robust_failure_orbits = {False: set(), True: set()}
        digests = {False: hashlib.sha256(), True: hashlib.sha256()}
        failure_carriers = collections.Counter()
        failure_signatures = collections.Counter()
        first_failure = None

        for carrier_index, adjacency in enumerate(carriers):
            for centres in itertools.combinations(range(9), 2):
                baseline = order9.quotient_family(adjacency, centres)
                for q_graph in copies:
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
                        order9.overlay_q_on_carrier(
                            adjacency, centres, q_graph
                        )
                    ):
                        continue
                    static += 1
                    canonical = order9.canonical_fixed_q_configuration(
                        adjacency,
                        centres,
                        by_code[code],
                        q_graph,
                    )
                    mode_results = {}
                    for q_only in (True, False):
                        result = analyse_mode(
                            adjacency, centres, q_graph, q_only
                        )
                        mode_results[q_only] = result
                        results[q_only][result] += 1
                        if not result[0]:
                            existential_failure_orbits[q_only].add(canonical)
                        if not result[1]:
                            robust_failure_orbits[q_only].add(canonical)
                        update_digest(
                            digests[q_only],
                            carrier_index,
                            centres,
                            q_graph,
                            result,
                        )
                    assert mode_results[True][0] == mode_results[False][0]
                    if not mode_results[False][0]:
                        roots = tuple(
                            vertex
                            for vertex in range(9)
                            if vertex not in centres
                        )
                        q_contacts = tuple(
                            sum(adjacency[centre] >> root & 1 for root in roots)
                            for centre in centres
                        )
                        carrier_edges = sum(row.bit_count() for row in adjacency) // 2
                        failure_carriers[carrier_index] += 1
                        signature = (
                            carrier_edges,
                            tuple(sorted(row.bit_count() for row in adjacency)),
                            tuple(adjacency[centre].bit_count() for centre in centres),
                            q_contacts,
                            bool(adjacency[centres[0]] >> centres[1] & 1),
                        )
                        failure_signatures[signature] += 1
                        if first_failure is None:
                            first_failure = (
                                carrier_index,
                                centres,
                                q_graph,
                                adjacency,
                                signature,
                            )

        assert static == expected[code]
        print(code, f"static_failures={static}")
        for q_only in (True, False):
            label = "Q_owned" if q_only else "all_owned"
            counter = results[q_only]
            existential_failures = sum(
                count for result, count in counter.items() if not result[0]
            )
            robust_failures = sum(
                count for result, count in counter.items() if not result[1]
            )
            print(
                code,
                label,
                f"existential_failures={existential_failures}",
                f"existential_failure_orbits={len(existential_failure_orbits[q_only])}",
                f"ownership_robust_failures={robust_failures}",
                f"ownership_robust_failure_orbits={len(robust_failure_orbits[q_only])}",
                f"digest={digests[q_only].hexdigest()}",
            )
            print(code, label, "profiles", sorted(counter.items()))
        print(code, "existential_failure_carriers", sorted(failure_carriers.items()))
        print(code, "existential_failure_signatures", sorted(failure_signatures.items()))
        print(code, "first_existential_failure", first_failure)

    print("split_cache", closes.cache_info())
    print("minor_cache", order9.has_target.cache_info())
    print("k7minus_cache", order9.has_k7_minus.cache_info())


if __name__ == "__main__":
    main()
