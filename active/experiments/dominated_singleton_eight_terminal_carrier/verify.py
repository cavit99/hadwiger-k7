#!/usr/bin/env python3
"""Compose the universal eight-terminal carriers at a dominated centre.

The eight roots are T=N(u)={v} union Q, where v is adjacent to every
vertex of Q.  A T-rooted K6-minus model in G-u, together with {u}, is a
K7-minus model in G.  This verifier tests every labelled carrier supplied by
the audited C8/K3,5/F8 trichotomy against each live common-neighbour graph.
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

import hc7_eight_terminal_rooted_carrier_verify as carrier  # noqa: E402


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
PAIRS = tuple(itertools.combinations(range(8), 2))


def boundary_graph(code: str) -> tuple[int, ...]:
    q = base.decode_graph6(code)
    answer = [row for row in q] + [0]
    v = 7
    for vertex in range(7):
        answer[vertex] |= 1 << v
        answer[v] |= 1 << vertex
    return tuple(answer)


def mask_graph(mask: int) -> tuple[int, ...]:
    graph = [0] * 8
    for index, (left, right) in enumerate(PAIRS):
        if mask >> index & 1:
            graph[left] |= 1 << right
            graph[right] |= 1 << left
    return tuple(graph)


def main() -> None:
    kinds = (
        ("C8", carrier.CYCLES),
        ("K3,5", carrier.K35),
        ("F8", carrier.F8),
    )
    total_failures = []
    for code in LIVE_CODES:
        boundary = boundary_graph(code)
        boundary_mask = carrier.adjacency_mask(boundary)
        for kind, masks in kinds:
            failures = [
                mask
                for mask in masks
                if not base.has_dense_minor(mask_graph(boundary_mask | mask), 6, 14)
            ]
            total_failures.extend((code, kind, mask) for mask in failures)
            print(code, kind, f"tested={len(masks)}", f"failures={len(failures)}")
            if failures:
                print(code, kind, "first_failure", failures[0])
    print(
        "eight_terminal_carrier_composition",
        f"tests={len(LIVE_CODES) * len(carrier.ALL_CARRIERS)}",
        f"failures={len(total_failures)}",
    )


if __name__ == "__main__":
    main()
