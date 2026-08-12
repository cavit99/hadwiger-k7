#!/usr/bin/env python3
"""Screen exact order-ten kernels without nine-terminal labelling blow-up.

For each of the 1,153 unlabelled rooted occurrences, choose the two
protected-centre positions and embed every labelled Q copy on the other
seven terminal positions.  The unique nonterminal is assigned together
with the two centre bags to Q-rooted bags in every connected way.  Static,
one-contact and two-contact closures are reported separately.
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


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


catalogue = load("nine_terminal_order_ten", HERE / "order_ten_catalogue.py")
order11 = load("nine_terminal_order_eleven", HERE / "verify_order_eleven.py")
base = order11.base


def kernel_adjacency(
    remainder: tuple[int, ...], neighbours: frozenset[int]
) -> tuple[int, ...]:
    answer = list(remainder) + [0]
    for terminal in neighbours:
        answer[terminal] |= 1 << 9
        answer[9] |= 1 << terminal
    return tuple(answer)


def add_contacts(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    roots: tuple[int, ...],
    contacts: tuple[int | None, int | None],
) -> tuple[int, ...]:
    answer = list(adjacency)
    for centre, contact in zip(centres, contacts, strict=True):
        if contact is None:
            continue
        root = roots[contact]
        answer[centre] |= 1 << root
        answer[root] |= 1 << centre
    return tuple(answer)


def quotient_family(
    adjacency: tuple[int, ...], centres: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    extras = centres + (9,)
    outcomes = set()
    for owners in itertools.product(range(7), repeat=3):
        groups = [{root} for root in roots]
        for extra, owner in zip(extras, owners, strict=True):
            groups[owner].add(extra)
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


def all_augmented_quotients(
    adjacency: tuple[int, ...], centres: tuple[int, int], contact_count: int
) -> tuple[tuple[int, ...], ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    if contact_count == 0:
        contact_patterns = ((None, None),)
    elif contact_count == 1:
        contact_patterns = tuple(
            (contact, None) for contact in range(7)
        ) + tuple((None, contact) for contact in range(7))
    elif contact_count == 2:
        contact_patterns = tuple(itertools.product(range(7), repeat=2))
    else:
        raise ValueError(contact_count)

    outcomes = set()
    for contacts in contact_patterns:
        augmented = add_contacts(adjacency, centres, roots, contacts)
        eligible_owners = []
        for extra in centres + (9,):
            eligible_owners.append(
                tuple(
                    owner
                    for owner, root in enumerate(roots)
                    if augmented[extra] >> root & 1
                )
            )
        if any(not owners for owners in eligible_owners):
            continue
        for owners in itertools.product(*eligible_owners):
            groups = [{root} for root in roots]
            for extra, owner in zip(centres + (9,), owners, strict=True):
                groups[owner].add(extra)
            quotient = [0] * 7
            for left, right in itertools.combinations(range(7), 2):
                if any(
                    augmented[u] >> v & 1
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


def closes(q_graph: tuple[int, ...], family: tuple[tuple[int, ...], ...]) -> bool:
    return any(
        has_target(
            tuple(q_graph[vertex] | quotient[vertex] for vertex in range(7))
        )
        for quotient in family
    )


def main() -> None:
    occurrences = catalogue.exact_rooted_occurrences()
    by_code = dict(order11.carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    copies = {code: order11.q_copies(by_code[code]) for code in live_codes}

    tests = collections.Counter()
    static_failures = collections.Counter()
    one_contact_failures = collections.Counter()
    two_contact_failures = collections.Counter()
    failure_profiles = {code: collections.Counter() for code in live_codes}

    for occurrence, (remainder, neighbours) in enumerate(occurrences):
        adjacency = kernel_adjacency(remainder, neighbours)
        for centres in itertools.combinations(range(9), 2):
            roots = tuple(vertex for vertex in range(9) if vertex not in centres)
            static_family = all_augmented_quotients(adjacency, centres, 0)
            assert static_family

            for code in live_codes:
                for q_graph in copies[code]:
                    tests[code] += 1
                    if closes(q_graph, static_family):
                        continue
                    static_failures[code] += 1
                    profile = (
                        len(neighbours),
                        tuple(sorted(adjacency[c].bit_count() for c in centres)),
                        bool(adjacency[centres[0]] >> centres[1] & 1),
                    )
                    failure_profiles[code][profile] += 1
                    one_family = all_augmented_quotients(adjacency, centres, 1)
                    if closes(q_graph, one_family):
                        continue
                    one_contact_failures[code] += 1
                    two_family = all_augmented_quotients(adjacency, centres, 2)
                    if closes(q_graph, two_family):
                        continue
                    two_contact_failures[code] += 1
                    print(
                        "first_two_contact_failure",
                        code,
                        occurrence,
                        centres,
                        profile,
                        q_graph,
                    )
                    raise SystemExit(1)

    expected_placements = 1_153 * 36
    assert tests == {
        code: expected_placements * len(copies[code]) for code in live_codes
    }
    print("rooted_occurrences", len(occurrences))
    print("protected_centre_placements", expected_placements)
    print("q_copy_counts", {code: len(copies[code]) for code in live_codes})
    print("tests", dict(tests))
    print("static_failures", dict(static_failures))
    print("one_contact_failures", dict(one_contact_failures))
    print("two_contact_failures", dict(two_contact_failures))
    print(
        "static_failure_profiles",
        {code: dict(profile) for code, profile in failure_profiles.items()},
    )
    print("minor_cache", has_target.cache_info())


if __name__ == "__main__":
    main()
