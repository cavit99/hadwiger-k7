#!/usr/bin/env python3
"""Verify two-exterior completion at a dominated degree-eight singleton.

The finite boundary graph Q has order seven, is triangle-free, has
independence number at most three, has no K_5^- minor, and has a vertex cut
of order at most two.  Two contracted exterior components are anticomplete;
each is adjacent to at least seven of the eight vertices in {v} union Q.
Every resulting quotient must contain a K_7^- minor.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


_BASE = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_low_degree_completion"
    / "verify.py"
)
_SPEC = importlib.util.spec_from_file_location("dominated_low_degree_base", _BASE)
assert _SPEC is not None and _SPEC.loader is not None
_base = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_base)


def add_two_exterior_components(
    graph: tuple[int, ...], missed_1: tuple[int, ...], missed_2: tuple[int, ...]
) -> tuple[int, ...]:
    """Add dominated apices u,v and two anticomplete component vertices."""

    order = len(graph)
    v, u, component_1, component_2 = order, order + 1, order + 2, order + 3
    answer = list(graph) + [0, 0, 0, 0]

    def add_edge(left: int, right: int) -> None:
        answer[left] |= 1 << right
        answer[right] |= 1 << left

    add_edge(u, v)
    for vertex in range(order):
        add_edge(u, vertex)
        add_edge(v, vertex)

    interface = [*range(order), v]
    for component, missed in (
        (component_1, set(missed_1)),
        (component_2, set(missed_2)),
    ):
        for vertex in interface:
            if vertex not in missed:
                add_edge(component, vertex)

    # There is deliberately no u--component or component_1--component_2 edge.
    return tuple(answer)


def main() -> None:
    eligible: list[tuple[str, tuple[int, ...]]] = []
    for graph6, graph in _base.triangle_free_graphs(7):
        if _base.independence_number(graph) > 3:
            continue
        if _base.has_dense_minor(graph, 5, 9):
            continue
        if not _base.small_cuts(graph):
            continue
        eligible.append((graph6, graph))

    assert len(eligible) == 9
    interface = tuple(range(8))  # Q together with v
    miss_profiles = [()] + [(vertex,) for vertex in interface]

    profiles = 0
    for graph6, graph in eligible:
        for missed_1, missed_2 in itertools.product(miss_profiles, repeat=2):
            profiles += 1
            host = add_two_exterior_components(graph, missed_1, missed_2)
            assert _base.has_dense_minor(host, 7, 20), (
                graph6,
                missed_1,
                missed_2,
            )

    assert profiles == 729

    # A single contracted exterior component is deliberately screened as a
    # hostile quotient gate.  The live host has more structure than this
    # quotient, but the count shows that near-complete attachment alone does
    # not finish the connected-exterior case.
    one_component_survivors: list[tuple[str, tuple[int, ...]]] = []
    for graph6, graph in eligible:
        for missed in miss_profiles:
            host = _base.add_dominated_apices_and_component(graph, missed)
            if not _base.has_dense_minor(host, 7, 20):
                one_component_survivors.append((graph6, missed))

    survivor_counts: dict[str, int] = {}
    for graph6, _ in one_component_survivors:
        survivor_counts[graph6] = survivor_counts.get(graph6, 0) + 1
    assert len(one_component_survivors) == 46
    assert sorted(survivor_counts.values()) == [1, 9, 9, 9, 9, 9]

    # In the live connected-exterior host, the component either sees the
    # whole interface (order-eight boundary) or misses precisely v
    # (order-seven boundary).  Exactly five base graphs survive both
    # profiles.
    v = 7
    live_profile_survivors = [
        (graph6, missed)
        for graph6, missed in one_component_survivors
        if missed in ((), (v,))
    ]
    live_survivor_counts: dict[str, int] = {}
    for graph6, _ in live_profile_survivors:
        live_survivor_counts[graph6] = live_survivor_counts.get(graph6, 0) + 1
    assert len(live_profile_survivors) == 10
    assert sorted(live_survivor_counts.values()) == [2, 2, 2, 2, 2]
    assert set(live_survivor_counts) == {
        "FCQ`_",
        "FCQb_",
        "FCR`o",
        "FCp`_",
        "FCpb_",
    }

    print(
        "GREEN dominated degree-eight singleton two-exterior completion "
        "eligible_Q=9 profiles=729 "
        "one_component_survivors=46 survivor_graphs=6 "
        "live_profile_survivors=10 live_graphs=5"
    )


if __name__ == "__main__":
    main()
