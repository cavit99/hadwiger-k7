#!/usr/bin/env python3
"""Compose two protected centres with the eight-terminal carrier family.

Delete one Q vertex before applying the eight-terminal rooted-carrier theorem.
Labels 0,...,5 are the remaining Q roots and 6,7 are two exterior centres.
For every labelled C8/K3,5/F8 carrier, enumerate every connected absorption
of the two centre bags into the six Q-rooted bags, restore the omitted Q
vertex as a singleton, and test the resulting seven-bag quotient.
"""

from __future__ import annotations

import importlib.util
import itertools
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


def carrier_adjacent(mask: int, left: int, right: int) -> bool:
    if left == right:
        return False
    return bool(mask & (1 << carrier8.PAIR_INDEX[tuple(sorted((left, right)))]))


def connected_group(mask: int, vertices: tuple[int, ...]) -> bool:
    if len(vertices) <= 1:
        return True
    reached = {vertices[0]}
    while True:
        old = set(reached)
        reached |= {
            vertex
            for vertex in vertices
            if any(carrier_adjacent(mask, vertex, seen) for seen in reached)
        }
        if reached == old:
            return len(reached) == len(vertices)


def absorbed_quotients(mask: int):
    """Yield six-vertex quotients after assigning centres 6,7 to Q roots."""

    seen = set()
    for owner6, owner7 in itertools.product(range(6), repeat=2):
        groups = [[root] for root in range(6)]
        groups[owner6].append(6)
        groups[owner7].append(7)
        if not all(connected_group(mask, tuple(group)) for group in groups):
            continue
        quotient = [0] * 6
        for left, right in itertools.combinations(range(6), 2):
            if any(
                carrier_adjacent(mask, vertex_left, vertex_right)
                for vertex_left in groups[left]
                for vertex_right in groups[right]
            ):
                quotient[left] |= 1 << right
                quotient[right] |= 1 << left
        encoded = tuple(quotient)
        if encoded not in seen:
            seen.add(encoded)
            yield encoded


def lift_with_omitted_q(
    quotient: tuple[int, ...], protected: tuple[int, ...], omitted: int
) -> tuple[int, ...]:
    graph = [0] * 7
    for left, right in itertools.combinations(range(6), 2):
        if quotient[left] >> right & 1:
            old_left, old_right = protected[left], protected[right]
            graph[old_left] |= 1 << old_right
            graph[old_right] |= 1 << old_left
    assert omitted not in protected
    return tuple(graph)


def main() -> None:
    by_code = dict(carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    families = (
        ("C8", carrier8.CYCLES),
        ("K35", carrier8.K35),
        ("F8", carrier8.F8),
    )
    family_totals = {kind: len(family) for kind, family in families}
    print("carrier_counts", family_totals)

    failures: dict[tuple[str, int, str], int] = {}
    universal_omissions: dict[str, list[int]] = {}
    for code in live_codes:
        graph_q = by_code[code]
        universal_omissions[code] = []
        for omitted in range(7):
            protected = tuple(vertex for vertex in range(7) if vertex != omitted)
            omission_failures = 0
            for kind, family in families:
                kind_failures = 0
                for mask in family:
                    if not any(
                        base.has_dense_minor(
                            tuple(
                                graph_q[vertex] | lifted[vertex]
                                for vertex in range(7)
                            ),
                            5,
                            9,
                        )
                        for quotient in absorbed_quotients(mask)
                        for lifted in (
                            lift_with_omitted_q(quotient, protected, omitted),
                        )
                    ):
                        kind_failures += 1
                failures[(code, omitted, kind)] = kind_failures
                omission_failures += kind_failures
            if omission_failures == 0:
                universal_omissions[code].append(omitted)
        print(code, "universal_omissions", universal_omissions[code])
        print(
            code,
            "failure_profiles",
            [
                (
                    omitted,
                    *(failures[(code, omitted, kind)] for kind, _ in families),
                )
                for omitted in range(7)
            ],
        )

    assert family_totals == {"C8": 2_520, "K35": 56, "F8": 3_360}


if __name__ == "__main__":
    main()
