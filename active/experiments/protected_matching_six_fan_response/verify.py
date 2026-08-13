#!/usr/bin/env python3
"""Verify the ten-vertex common-attachment counterprofile.

The exact minor routines are imported from the retained order-nine kernel
screens.  The script verifies one finite route obstruction; it does not
encode contraction-criticality or a boundary-colouring response.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rooted = load(
    "six_fan_rooted_minor",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_exact_kernel"
    / "screen_order9.py",
)
order9 = load(
    "six_fan_unrooted_minor",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_kernel"
    / "verify_order_nine.py",
)


GRAPH = (592, 352, 928, 704, 641, 326, 555, 540, 550, 477)
Q_ROOTS = (0, 2, 3, 4, 5, 6, 7)
W = 8
X = 9


def induced(graph: tuple[int, ...], vertices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        sum(
            1 << right
            for right, old_right in enumerate(vertices)
            if graph[old_left] >> old_right & 1
        )
        for old_left in vertices
    )


def main() -> None:
    assert len(GRAPH) == 10
    assert all(not (row >> len(GRAPH)) for row in GRAPH)
    assert all(
        bool(GRAPH[left] >> right & 1) == bool(GRAPH[right] >> left & 1)
        for left, right in itertools.combinations(range(len(GRAPH)), 2)
    )
    assert all(not (GRAPH[vertex] >> vertex & 1) for vertex in range(10))

    expected_q = rooted.base.decode_graph6("FCQ`_")
    actual_q = induced(GRAPH, Q_ROOTS)
    assert all(actual_q[vertex] | expected_q[vertex] == actual_q[vertex]
               for vertex in range(7))
    assert sum(row.bit_count() for row in actual_q) // 2 == 8

    assert rooted.three_connected(GRAPH)
    assert not rooted.connected(GRAPH, (5, 6, 8))
    assert GRAPH[W] >> X & 1
    q_neighbours = tuple(root for root in Q_ROOTS if GRAPH[X] >> root & 1)
    assert q_neighbours == (0, 2, 3, 4, 6, 7)
    assert GRAPH[X].bit_count() == 7

    assert not order9.has_k7_minus(GRAPH)
    marked = tuple(vertex in Q_ROOTS for vertex in range(len(GRAPH)))
    assert not rooted.rooted_k5minus(GRAPH, marked)

    print(
        "GREEN protected matching six-fan counterprofile:",
        "kappa=3, six direct arms, no K7-minus or Q-rooted K5-minus minor",
    )


if __name__ == "__main__":
    main()
