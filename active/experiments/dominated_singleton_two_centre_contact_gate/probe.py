#!/usr/bin/env python3
"""Test two avoided exceptional centres against the exact kernel residue.

After deleting two of the four other centres, the common remainder is
three-connected and admits a Q-rooted seven-terminal kernel.  The deleted
centres are independent connected augmentations of the rooted bags.  This
diagnostic determines which lower bounds on their distinct bag-contact sets
would make the finite quotient terminal.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "dominated_singleton_complete_seven_terminal_kernel"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("complete_kernel", SOURCE)
assert SPEC is not None and SPEC.loader is not None
kernel = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kernel)
base = kernel.base
carrier = kernel.carrier


def star_edges(owner: int, contacts: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        tuple(sorted((owner, other)))
        for other in contacts
        if other != owner
    }


def closes_with_two(
    graph: tuple[int, ...],
    first: tuple[int, ...],
    second: tuple[int, ...],
) -> bool:
    return any(
        base.has_dense_minor(
            carrier.add_edges(
                graph,
                star_edges(first_owner, first)
                | star_edges(second_owner, second),
            ),
            5,
            9,
        )
        for first_owner in first
        for second_owner in second
    )


def main() -> None:
    by_code = dict(carrier.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    minimal = kernel.minimal_three_connected_carriers()
    templates = kernel.order_eight_templates()

    failures7 = []
    for code in live_codes:
        q = by_code[code]
        for rooted_carrier in minimal:
            union = tuple(q[v] | rooted_carrier[v] for v in range(7))
            if base.has_dense_minor(union, 5, 9):
                continue
            failures7.append((code, union))

    failures8 = []
    for code in live_codes:
        q = by_code[code]
        for terminal_mask, neighbour_mask in templates:
            owner_unions = []
            for owner in range(7):
                if not neighbour_mask & (1 << owner):
                    continue
                quotient = kernel.owner_quotient(
                    terminal_mask, neighbour_mask, owner
                )
                union = tuple(q[v] | quotient[v] for v in range(7))
                if base.has_dense_minor(union, 5, 9):
                    owner_unions = []
                    break
                owner_unions.append(union)
            if owner_unions:
                failures8.append((code, tuple(owner_unions)))

    assert len(failures7) == 21
    assert len(failures8) == 89

    for first_size, second_size in ((2, 2), (2, 3), (3, 3), (2, 4), (3, 4)):
        pairs = tuple(
            itertools.product(
                itertools.combinations(range(7), first_size),
                itertools.combinations(range(7), second_size),
            )
        )
        bad7 = []
        for code, union in failures7:
            for first, second in pairs:
                if not closes_with_two(union, first, second):
                    bad7.append((code, first, second))
        bad8 = []
        for code, owner_unions in failures8:
            for first, second in pairs:
                if not any(
                    closes_with_two(union, first, second)
                    for union in owner_unions
                ):
                    bad8.append((code, first, second))
        print(
            f"contacts={first_size}+{second_size}",
            f"order7_tests={len(failures7) * len(pairs)}",
            f"order7_failures={len(bad7)}",
            f"order8_tests={len(failures8) * len(pairs)}",
            f"order8_failures={len(bad8)}",
            "order7_failure_intersections="
            f"{sorted({(len(set(a) & set(b)), a == b) for _, a, b in bad7})}",
            "order8_failure_intersections="
            f"{sorted({(len(set(a) & set(b)), a == b) for _, a, b in bad8})}",
        )
        if bad7:
            print("first_order7_failure", bad7[0])
        if bad8:
            print("first_order8_failure", bad8[0])


if __name__ == "__main__":
    main()
