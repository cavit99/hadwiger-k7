#!/usr/bin/env python3
"""Compose the complete seven-terminal kernel catalogue with the live bases.

The audited rooted-kernel theorem has a universal order-seven branch and a
universal/existential order-eight branch.  For each of the three surviving
seven-vertex common-neighbour graphs Q, this verifier checks exactly

* every labelled edge-minimal three-connected order-seven carrier F; and
* every labelled order-eight irreducible kernel family, accepting the family
  when at least one legal owner quotient closes.

Closure means that Q union the carrier has a K5-minus minor.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path
import sys


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


ACTIVE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ACTIVE))

from hc7_overlap_two_order_six_adaptive_kernel_probe import (  # noqa: E402
    LOCAL_PAIRS,
    exact_order_eight_families,
    minimal_order_seven_carriers,
)


BASE_PATH = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_low_degree_completion"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("dominated_low_degree_base", BASE_PATH)
assert SPEC is not None and SPEC.loader is not None
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


LIVE_CODES = ("FCQ`_", "FCQb_", "FCp`_")


def graph_mask(graph: tuple[int, ...]) -> int:
    return sum(
        1 << index
        for index, (left, right) in enumerate(LOCAL_PAIRS)
        if base.adjacent(graph, left, right)
    )


def mask_graph(mask: int) -> tuple[int, ...]:
    graph = [0] * 7
    for index, (left, right) in enumerate(LOCAL_PAIRS):
        if mask >> index & 1:
            graph[left] |= 1 << right
            graph[right] |= 1 << left
    return tuple(graph)


def closes(base_mask: int, carrier_mask: int) -> bool:
    return base.has_dense_minor(mask_graph(base_mask | carrier_mask), 5, 9)


def relabel_mask(mask: int, image: tuple[int, ...]) -> int:
    index = {edge: position for position, edge in enumerate(LOCAL_PAIRS)}
    answer = 0
    for position, (left, right) in enumerate(LOCAL_PAIRS):
        if mask >> position & 1:
            answer |= 1 << index[tuple(sorted((image[left], image[right])))]
    return answer


def automorphisms(mask: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        image
        for image in itertools.permutations(range(7))
        if relabel_mask(mask, image) == mask
    )


def mask_orbits(
    masks: list[int], group: tuple[tuple[int, ...], ...]
) -> tuple[int, list[int]]:
    representatives = {
        min(relabel_mask(mask, image) for image in group) for mask in masks
    }
    return len(representatives), sorted(representatives)


def family_orbits(
    families: list[tuple[int, ...]], group: tuple[tuple[int, ...], ...]
) -> tuple[int, list[tuple[int, ...]]]:
    representatives = {
        min(
            tuple(sorted(relabel_mask(mask, image) for mask in family))
            for image in group
        )
        for family in families
    }
    return len(representatives), sorted(representatives)


def degree_sequence(mask: int) -> tuple[int, ...]:
    return tuple(sorted((row.bit_count() for row in mask_graph(mask)), reverse=True))


def missing_edges(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        edge
        for position, edge in enumerate(LOCAL_PAIRS)
        if not (mask >> position & 1)
    )


def minimum_forcing_edges(mask: int) -> tuple[int, tuple[tuple[int, int], ...]]:
    missing = missing_edges(mask)
    for size in range(1, 5):
        for extra in itertools.combinations(missing, size):
            addition = sum(
                1 << LOCAL_PAIRS.index(edge) for edge in extra
            )
            if closes(mask, addition):
                return size, extra
    return 5, ()


def all_single_forcing_edges(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(edge for edge in missing_edges(mask) if closes(mask, 1 << LOCAL_PAIRS.index(edge)))


def main() -> None:
    order_seven = minimal_order_seven_carriers()
    order_eight = exact_order_eight_families()
    assert len(order_seven) == 5_495
    assert len(order_eight) == 30_600

    all_order_seven_failures: list[tuple[str, int]] = []
    all_order_eight_failures: list[tuple[str, tuple[int, ...]]] = []

    for code in LIVE_CODES:
        q_mask = graph_mask(base.decode_graph6(code))
        failures_seven = [
            carrier for carrier in order_seven if not closes(q_mask, carrier)
        ]
        failures_eight = [
            family
            for family in order_eight
            if not any(closes(q_mask, owner) for owner in family)
        ]
        all_order_seven_failures.extend((code, carrier) for carrier in failures_seven)
        all_order_eight_failures.extend((code, family) for family in failures_eight)
        group = automorphisms(q_mask)
        order_seven_orbits, order_seven_representatives = mask_orbits(
            failures_seven, group
        )
        order_eight_orbits, order_eight_representatives = family_orbits(
            failures_eight, group
        )
        print(
            code,
            f"order7_failures={len(failures_seven)}",
            f"order7_orbits={order_seven_orbits}",
            f"order8_family_failures={len(failures_eight)}",
            f"order8_family_orbits={order_eight_orbits}",
        )
        for representative in order_seven_representatives:
            union = q_mask | representative
            print(
                code,
                "order7_orbit",
                representative,
                f"carrier_edges={representative.bit_count()}",
                f"union_edges={union.bit_count()}",
                f"union_degrees={degree_sequence(union)}",
                f"minimum_forcing_edges={minimum_forcing_edges(union)}",
                f"single_forcing_edges={all_single_forcing_edges(union)}",
                f"Q_edges={tuple(edge for index, edge in enumerate(LOCAL_PAIRS) if q_mask >> index & 1)}",
                f"carrier_edges={tuple(edge for index, edge in enumerate(LOCAL_PAIRS) if representative >> index & 1)}",
            )
        for representative in order_eight_representatives:
            unions = tuple(q_mask | owner for owner in representative)
            print(
                code,
                "order8_family_orbit",
                representative,
                f"owners={len(representative)}",
                f"union_edges={tuple(mask.bit_count() for mask in unions)}",
                f"union_degrees={tuple(degree_sequence(mask) for mask in unions)}",
                "minimum_forcing_edges="
                f"{tuple(minimum_forcing_edges(mask) for mask in unions)}",
            )

    print(
        "complete_kernel_composition",
        f"order7_tests={len(LIVE_CODES) * len(order_seven)}",
        f"order7_failures={len(all_order_seven_failures)}",
        f"order8_family_tests={len(LIVE_CODES) * len(order_eight)}",
        f"order8_family_failures={len(all_order_eight_failures)}",
    )


if __name__ == "__main__":
    main()
