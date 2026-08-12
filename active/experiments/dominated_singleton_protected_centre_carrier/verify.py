#!/usr/bin/env python3
"""Test one protected exterior centre in the eight-terminal carrier family.

Labels 0,...,6 are the seven vertices of Q.  Label 7 is one of the other
degree-eight centres.  For every labelled carrier supplied by the audited
eight-terminal trichotomy, contract the protected-centre bag into each
possible neighbouring Q-bag and test the resulting seven-bag quotient.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


ROOT = Path(__file__).resolve().parents[3]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


carrier8 = load(
    "eight_terminal_carrier",
    ROOT / "active" / "hc7_eight_terminal_rooted_carrier_verify.py",
)
carrier7 = load(
    "dominated_rooted_seven_carrier",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_rooted_seven_carrier"
    / "verify.py",
)
base = carrier7._base


def seven_graph_from_mask(mask: int) -> tuple[int, ...]:
    graph = [0] * 7
    for position, (left, right) in enumerate(carrier8.PAIRS):
        if not (mask & (1 << position)) or 7 in (left, right):
            continue
        graph[left] |= 1 << right
        graph[right] |= 1 << left
    return tuple(graph)


def absorb_protected_centre(mask: int, owner: int) -> tuple[int, ...]:
    graph = list(seven_graph_from_mask(mask))
    neighbours = {
        other
        for other in range(7)
        if mask
        & (1 << carrier8.PAIR_INDEX[tuple(sorted((7, other)))])
    }
    assert owner in neighbours
    for other in neighbours - {owner}:
        graph[owner] |= 1 << other
        graph[other] |= 1 << owner
    return tuple(graph)


def main() -> None:
    by_code = dict(carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    families = (
        ("C8", carrier8.CYCLES),
        ("K35", carrier8.K35),
        ("F8", carrier8.F8),
    )

    failures: list[tuple[str, str, int]] = []
    counts: dict[tuple[str, str], int] = {}
    owner_histogram: dict[int, int] = {}
    for code in live_codes:
        graph_q = by_code[code]
        for kind, family in families:
            for mask in family:
                closing_owners = 0
                for owner in range(7):
                    edge = tuple(sorted((7, owner)))
                    if not mask & (1 << carrier8.PAIR_INDEX[edge]):
                        continue
                    quotient = absorb_protected_centre(mask, owner)
                    union = tuple(
                        graph_q[vertex] | quotient[vertex]
                        for vertex in range(7)
                    )
                    if base.has_dense_minor(union, 5, 9):
                        closing_owners += 1
                owner_histogram[closing_owners] = (
                    owner_histogram.get(closing_owners, 0) + 1
                )
                if not closing_owners:
                    failures.append((code, kind, mask))
                    counts[(code, kind)] = counts.get((code, kind), 0) + 1

    total = 3 * len(carrier8.ALL_CARRIERS)
    print(
        "protected-centre eight-terminal carrier composition",
        f"tests={total}",
        f"failures={len(failures)}",
    )
    print("failure_counts", sorted(counts.items()))
    print("closing_owner_histogram", sorted(owner_histogram.items()))
    if failures:
        print("first_failure", failures[0])

    assert total == 17_808
    assert sum(owner_histogram.values()) == total


if __name__ == "__main__":
    main()
