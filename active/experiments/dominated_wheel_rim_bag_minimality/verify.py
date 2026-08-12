#!/usr/bin/env python3
"""Check the exact order-seven wheel residue used by rim-bag minimisation."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")

KERNEL = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_complete_seven_terminal_kernel"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("complete_kernel", KERNEL)
assert SPEC is not None and SPEC.loader is not None
kernel = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kernel)


def main() -> None:
    by_code = dict(kernel.carrier.eligible_graphs())
    codes = ("FCQ`_", "FCQb_", "FCp`_")
    failures = []

    for code in codes:
        q_graph = by_code[code]
        for wheel in kernel.minimal_three_connected_carriers():
            union = tuple(q_graph[v] | wheel[v] for v in range(7))
            if kernel.base.has_dense_minor(union, 5, 9):
                continue
            failures.append((code, q_graph, wheel, union))

    assert len(failures) == 21
    vulnerable_by_code = {code: 0 for code in codes}
    missing_edge_tests = 0

    for code, q_graph, wheel, union in failures:
        degrees = tuple(row.bit_count() for row in wheel)
        assert sorted(degrees) == [3, 3, 3, 3, 3, 3, 6]
        hub = degrees.index(6)

        # Every literal Q edge is already a wheel edge.
        assert all((q_graph[v] & ~wheel[v]) == 0 for v in range(7))
        assert union == wheel

        # One further actual adjacency between two bags is terminal.
        for left, right in itertools.combinations(range(7), 2):
            if kernel.base.adjacent(union, left, right):
                continue
            missing_edge_tests += 1
            augmented = kernel.carrier.add_edges(union, {(left, right)})
            assert kernel.base.has_dense_minor(augmented, 5, 9)

        # A root-free piece can own only carrier edges not already literal
        # Q edges at its retained root.
        vulnerable_here = 0
        for source in range(7):
            if source == hub:
                continue
            ownable = [
                other
                for other in range(7)
                if kernel.base.adjacent(wheel, source, other)
                and not kernel.base.adjacent(q_graph, source, other)
            ]
            if len(ownable) >= 2:
                assert len(ownable) == 2
                assert q_graph[source].bit_count() == 1
                vulnerable_by_code[code] += 1
                vulnerable_here += 1
        assert vulnerable_here == {"FCQ`_": 2, "FCQb_": 1, "FCp`_": 0}[code]

    assert vulnerable_by_code == {"FCQ`_": 20, "FCQb_": 4, "FCp`_": 0}
    assert missing_edge_tests == 189
    print(
        "GREEN dominated wheel rim-bag quotient",
        f"residues={len(failures)}",
        f"missing_edge_tests={missing_edge_tests}",
        f"vulnerable={sorted(vulnerable_by_code.items())}",
    )


if __name__ == "__main__":
    main()
