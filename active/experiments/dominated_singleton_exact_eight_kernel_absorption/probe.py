#!/usr/bin/env python3
"""Test the exact eight-terminal kernel bundle after absorbing centre root 7.

This is a discovery probe.  It retains all contacts of the audited terminal
kernel rather than reducing them to C8/K3,5/F8.  Exact quantifiers are:

* order 8: every labelled edge-minimal three-connected carrier;
* order 9: every exact template, with an adaptive owner for the nonterminal;
* order 10: every exact template, with adaptive owners for both
  nonterminals.

After those owner choices the rooted bag containing terminal 7 is absorbed
into an adjacent bag rooted in Q={0,...,6}.  The final quotient is tested
for K5-minus after adding the literal Q edges.
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
import hc7_eight_terminal_exact_bundle_catalogue as exact  # noqa: E402


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
PAIRS7 = tuple(itertools.combinations(range(7), 2))
INDEX7 = {edge: index for index, edge in enumerate(PAIRS7)}


def q_mask(code: str) -> int:
    graph = base.decode_graph6(code)
    return sum(
        1 << INDEX7[(left, right)]
        for left, right in PAIRS7
        if base.adjacent(graph, left, right)
    )


def final_mask(carrier: int, owner: int) -> int:
    """Absorb terminal 7 into owner and return the 21-bit Q quotient."""

    answer = 0
    for index, (left, right) in enumerate(PAIRS7):
        present = bool(carrier >> exact.PAIR_INDEX[(left, right)] & 1)
        if left == owner:
            present |= bool(carrier >> exact.PAIR_INDEX[(right, 7)] & 1)
        if right == owner:
            present |= bool(carrier >> exact.PAIR_INDEX[(left, 7)] & 1)
        if present:
            answer |= 1 << index
    return answer


def centre_neighbours(carrier: int) -> tuple[int, ...]:
    return tuple(
        vertex
        for vertex in range(7)
        if carrier >> exact.PAIR_INDEX[(vertex, 7)] & 1
    )


def graph_from_mask(mask: int) -> tuple[int, ...]:
    graph = [0] * 7
    for index, (left, right) in enumerate(PAIRS7):
        if mask >> index & 1:
            graph[left] |= 1 << right
            graph[right] |= 1 << left
    return tuple(graph)


def closes(code_mask: int, carrier: int) -> bool:
    return any(
        base.has_dense_minor(graph_from_mask(code_mask | final_mask(carrier, owner)), 5, 9)
        for owner in centre_neighbours(carrier)
    )


def degree_sequence(carrier: int) -> tuple[int, ...]:
    """Return the degree sequence of an eight-terminal carrier."""

    return tuple(
        sorted(
            sum(
                bool(carrier >> exact.PAIR_INDEX[tuple(sorted((left, right)))] & 1)
                for right in range(8)
                if right != left
            )
            for left in range(8)
        )
    )


def protected_root_edge_screen(
    code: str,
    failures: list[tuple[int, ...]],
) -> int:
    """Test every absent edge from protected root 7 to a Q-root.

    This deliberately grants the strongest quotient-level effect of
    reselecting the protected centre's matching representative: the new
    coordinate is allowed to add any previously absent rooted-bag adjacency.
    """

    fixed = q_mask(code)
    forcing_histogram: dict[int, int] = {}
    resistant_profiles: dict[tuple[tuple[int, ...], int], int] = {}
    for family in failures:
        assert len(family) == 1
        carrier = family[0]
        forcing = 0
        for other in range(7):
            edge_bit = 1 << exact.PAIR_INDEX[(other, 7)]
            if carrier & edge_bit:
                continue
            if closes(fixed, carrier | edge_bit):
                forcing += 1
        forcing_histogram[forcing] = forcing_histogram.get(forcing, 0) + 1
        if forcing == 0:
            root_degree = sum(
                bool(carrier >> exact.PAIR_INDEX[(other, 7)] & 1)
                for other in range(7)
            )
            profile = (degree_sequence(carrier), root_degree)
            resistant_profiles[profile] = resistant_profiles.get(profile, 0) + 1

    print(code, "order8_extra_root_edge_forcing", sorted(forcing_histogram.items()))
    print(code, "order8_extra_root_edge_resistant_profiles", sorted(resistant_profiles.items()))

    expected_histograms = {
        "FCQ`_": {0: 30, 2: 80, 3: 40, 4: 60},
        "FCQb_": {0: 6, 2: 24, 3: 18, 4: 26},
        "FCp`_": {0: 15, 1: 28, 2: 35, 3: 14, 4: 49},
    }
    expected_profiles = {
        "FCQ`_": {
            ((3, 3, 3, 3, 3, 3, 3, 5), 5): 20,
            ((3, 3, 3, 3, 3, 3, 3, 7), 7): 10,
        },
        "FCQb_": {
            ((3, 3, 3, 3, 3, 3, 3, 5), 5): 4,
            ((3, 3, 3, 3, 3, 3, 3, 7), 7): 2,
        },
        "FCp`_": {
            ((3, 3, 3, 3, 3, 3, 3, 5), 5): 14,
            ((3, 3, 3, 3, 3, 3, 3, 7), 7): 1,
        },
    }
    assert forcing_histogram == expected_histograms[code]
    assert resistant_profiles == expected_profiles[code]
    return forcing_histogram.get(0, 0)


def screen_families(
    name: str,
    families: tuple[tuple[int, ...], ...],
) -> list[tuple[str, tuple[int, ...]]]:
    failures = []
    for code in LIVE_CODES:
        fixed = q_mask(code)
        bad = [family for family in families if not any(closes(fixed, carrier) for carrier in family)]
        failures.extend((code, family) for family in bad)
        print(code, name, f"tested={len(families)}", f"failures={len(bad)}", flush=True)
        if bad:
            print(code, name, "first_failure", bad[0], flush=True)
    return failures


def main() -> None:
    _unlabelled8, masks8 = exact.order_eight_catalogue()
    failures8 = screen_families("order8", tuple((mask,) for mask in masks8))
    print("order8_total_failures", len(failures8), flush=True)
    failures8_by_code = {
        code: [family for failure_code, family in failures8 if failure_code == code]
        for code in LIVE_CODES
    }
    resistant_total = sum(
        protected_root_edge_screen(code, failures8_by_code[code])
        for code in LIVE_CODES
    )
    assert resistant_total == 51

    if "--all" not in sys.argv:
        return

    _rooted9, _edge9, _degree9, _templates9, families9 = exact.order_nine_catalogue()
    failures9 = screen_families("order9", families9)
    print("order9_total_failures", len(failures9), flush=True)

    _templates10, families10 = exact.order_ten_normal_form_catalogue()
    failures10 = screen_families("order10", families10)
    print("order10_total_failures", len(failures10), flush=True)


if __name__ == "__main__":
    main()
