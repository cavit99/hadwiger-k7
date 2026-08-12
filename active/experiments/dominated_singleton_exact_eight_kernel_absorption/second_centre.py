#!/usr/bin/env python3
"""Test a second protected centre against the exact order-eight residue.

This is a finite structural diagnostic, not a host theorem.  It tests two
precise sufficient conditions: two resistant quotients realised on the same
seven Q-rooted bags, and one additional centre-bearing connected set with a
specified set of Q-bag contacts.
"""

from __future__ import annotations

import collections
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


classification = load("exact_residue_classification", HERE / "classify.py")
rooted = load(
    "protected_coordinate_rooted_minor",
    HERE.parent / "dominated_singleton_protected_coordinate_carrier" / "verify.py",
)
exact = classification.exact
base = classification.base


def add_edge(graph: list[int], left: int, right: int) -> None:
    graph[left] |= 1 << right
    graph[right] |= 1 << left


def one_centre_graph(code: str, carrier: int, contacts: tuple[int, ...]):
    """Add a second centre-bearing set as vertex 8 with Q contacts."""

    graph = list(base.decode_graph6(code)) + [0, 0]
    for index, (left, right) in enumerate(exact.PAIRS):
        if carrier >> index & 1:
            add_edge(graph, left, right)
    for root in contacts:
        add_edge(graph, root, 8)
    return tuple(graph)


def two_quotient_graph(code: str, first: int, second: int):
    """Realise two resistant quotients on common Q-rooted singleton bags."""

    graph = list(base.decode_graph6(code)) + [0, 0]
    for carrier, protected_root in ((first, 7), (second, 8)):
        for index, (left, right) in enumerate(exact.PAIRS):
            if not (carrier >> index & 1):
                continue
            image_left = protected_root if left == 7 else left
            image_right = protected_root if right == 7 else right
            add_edge(graph, image_left, image_right)
    return tuple(graph)


def rooted_target(graph: tuple[int, ...]) -> bool:
    return rooted.rooted_k5minus(graph, (True,) * 7 + (False, False))


def robust_carriers(code: str, masks: tuple[int, ...]) -> tuple[int, ...]:
    fixed = classification.probe.q_mask(code)
    return tuple(
        mask
        for mask in masks
        if not classification.probe.closes(fixed, mask)
        and not classification.closes_with_some_root_edge(fixed, (mask,))
    )


def main() -> None:
    _unlabelled, masks = exact.order_eight_catalogue()
    for code in classification.probe.LIVE_CODES:
        robust = robust_carriers(code, masks)
        group = classification.automorphisms(code)
        representatives = tuple(
            sorted(
                {
                    classification.canonical_family((carrier,), group)[0]
                    for carrier in robust
                }
            )
        )

        pair_failures = sum(
            not rooted_target(two_quotient_graph(code, first, second))
            for first, second in itertools.product(robust, repeat=2)
        )
        print(
            code,
            "common_Q_bag_pairs",
            f"tested={len(robust) ** 2}",
            f"failures={pair_failures}",
        )
        assert pair_failures == 0

        for carrier in representatives:
            failures_by_contacts = collections.Counter()
            for size in range(1, 8):
                failures_by_contacts[size] = sum(
                    not rooted_target(one_centre_graph(code, carrier, contacts))
                    for contacts in itertools.combinations(range(7), size)
                )
            shape = classification.robust_order_eight_shape(carrier)
            print(
                code,
                shape,
                "second_centre_contact_failures",
                dict(failures_by_contacts),
            )
            assert all(failures_by_contacts[size] == 0 for size in range(4, 8))


if __name__ == "__main__":
    main()
