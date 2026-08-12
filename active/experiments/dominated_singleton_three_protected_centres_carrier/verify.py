#!/usr/bin/env python3
"""Compose three protected centres with the eight-terminal carrier family.

Delete two Q vertices from the five-connected graph H.  Labels 0,...,4 are
the remaining Q roots and 5,6,7 are three exterior exceptional centres.
For every labelled C8/K3,5/F8 carrier, enumerate every connected absorption
of the centre bags into the five Q-rooted bags, restore the omitted Q
vertices as singletons, and test the resulting seven-bag quotient.
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


def adjacent(mask: int, left: int, right: int) -> bool:
    if left == right:
        return False
    edge = tuple(sorted((left, right)))
    return bool(mask & (1 << carrier8.PAIR_INDEX[edge]))


def connected(mask: int, vertices: tuple[int, ...]) -> bool:
    reached = {vertices[0]}
    while True:
        old = set(reached)
        reached |= {
            vertex
            for vertex in vertices
            if any(adjacent(mask, vertex, seen) for seen in reached)
        }
        if reached == old:
            return len(reached) == len(vertices)


def absorbed_quotients(mask: int):
    seen = set()
    for owners in itertools.product(range(5), repeat=3):
        groups = [[root] for root in range(5)]
        for centre, owner in zip(range(5, 8), owners, strict=True):
            groups[owner].append(centre)
        if not all(connected(mask, tuple(group)) for group in groups):
            continue
        quotient = [0] * 5
        for left, right in itertools.combinations(range(5), 2):
            if any(
                adjacent(mask, vertex_left, vertex_right)
                for vertex_left in groups[left]
                for vertex_right in groups[right]
            ):
                quotient[left] |= 1 << right
                quotient[right] |= 1 << left
        encoded = tuple(quotient)
        if encoded not in seen:
            seen.add(encoded)
            yield encoded


def lift(
    quotient: tuple[int, ...], protected: tuple[int, ...]
) -> tuple[int, ...]:
    graph = [0] * 7
    for left, right in itertools.combinations(range(5), 2):
        if quotient[left] >> right & 1:
            old_left, old_right = protected[left], protected[right]
            graph[old_left] |= 1 << old_right
            graph[old_right] |= 1 << old_left
    return tuple(graph)


def main() -> None:
    by_code = dict(carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    families = (
        ("C8", carrier8.CYCLES),
        ("K35", carrier8.K35),
        ("F8", carrier8.F8),
    )
    print("carrier_counts", {kind: len(family) for kind, family in families})

    for code in live_codes:
        graph_q = by_code[code]
        universal_omissions = []
        profiles = []
        for omitted in itertools.combinations(range(7), 2):
            protected = tuple(vertex for vertex in range(7) if vertex not in omitted)
            counts = []
            for _kind, family in families:
                failures = 0
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
                        for lifted in (lift(quotient, protected),)
                    ):
                        failures += 1
                counts.append(failures)
            profiles.append((omitted, *counts))
            if not any(counts):
                universal_omissions.append(omitted)
        print(code, "universal_omissions", universal_omissions)
        print(code, "failure_profiles", profiles)


if __name__ == "__main__":
    main()
