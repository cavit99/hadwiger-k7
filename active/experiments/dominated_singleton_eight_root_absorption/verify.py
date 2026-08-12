#!/usr/bin/env python3
"""Absorb an eighth exceptional-centre root into a Q-rooted carrier.

Apply the audited eight-terminal carrier theorem in H=G-{u,v} to the seven
common-neighbour roots Q and one further exceptional centre w.  For each
labelled C8, K3,5 or F8 carrier, this verifier asks whether some carrier
neighbour q of w can own the w-bag so that the resulting seven Q-rooted
quotient, together with the literal graph Q, contains K5-minus.
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
import hc7_eight_terminal_rooted_carrier_verify as carriers  # noqa: E402


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
PAIRS8 = tuple(itertools.combinations(range(8), 2))
INDEX8 = {edge: index for index, edge in enumerate(PAIRS8)}
PAIRS7 = tuple(itertools.combinations(range(7), 2))


def absorb_eighth(mask: int, owner: int) -> tuple[int, ...]:
    """Contract carrier vertex 7 into owner, then delete the old label 7."""

    graph = [0] * 7
    for left, right in PAIRS7:
        present = bool(mask >> INDEX8[(left, right)] & 1)
        if left == owner:
            present |= bool(mask >> INDEX8[(right, 7)] & 1)
        if right == owner:
            present |= bool(mask >> INDEX8[(left, 7)] & 1)
        if present:
            graph[left] |= 1 << right
            graph[right] |= 1 << left
    return tuple(graph)


def neighbours_of_eighth(mask: int) -> tuple[int, ...]:
    return tuple(
        vertex
        for vertex in range(7)
        if mask >> INDEX8[(vertex, 7)] & 1
    )


def main() -> None:
    kinds = (
        ("C8", carriers.CYCLES),
        ("K3,5", carriers.K35),
        ("F8", carriers.F8),
    )
    all_failures = []
    for code in LIVE_CODES:
        q = base.decode_graph6(code)
        for kind, family in kinds:
            failures = []
            for mask in family:
                closes = False
                for owner in neighbours_of_eighth(mask):
                    quotient = absorb_eighth(mask, owner)
                    union = tuple(q[v] | quotient[v] for v in range(7))
                    if base.has_dense_minor(union, 5, 9):
                        closes = True
                        break
                if not closes:
                    failures.append(mask)
            all_failures.extend((code, kind, mask) for mask in failures)
            print(code, kind, f"tested={len(family)}", f"failures={len(failures)}")
            if failures:
                print(code, kind, "first_failure", failures[0])
    print(
        "eight_root_absorption",
        f"tests={len(LIVE_CODES) * len(carriers.ALL_CARRIERS)}",
        f"failures={len(all_failures)}",
    )


if __name__ == "__main__":
    main()
