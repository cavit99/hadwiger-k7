#!/usr/bin/env python3
"""Exact marked-edge absorption on the all-terminal order-nine catalogue.

The seven Q roots stay marked.  The two other terminals are ordered as the
protected centre w and its swallowed matching mate x.  After adding the
literal edge wx, contract an existing carrier edge xq into its Q root and
test exactly for a Q-rooted K5-minus minor.
"""

from __future__ import annotations

import collections
import hashlib
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


screen = load(
    "marked_edge_order9_base",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_exact_kernel"
    / "screen_order9.py",
)
base = screen.base


def add_edge(graph: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    answer = list(graph)
    answer[left] |= 1 << right
    answer[right] |= 1 << left
    return tuple(answer)


def absorb_x_into_q(
    graph: tuple[int, ...],
    marked: tuple[bool, ...],
    x: int,
    q: int,
):
    assert marked[q] and not marked[x]
    assert base.adjacent(graph, x, q)
    return screen.contract_marked(graph, marked, x, q)


def update_digest(
    digest,
    code: str,
    carrier_index: int,
    roots: tuple[int, ...],
    w: int,
    x: int,
    q_outcomes: tuple[tuple[int, bool], ...],
) -> None:
    digest.update(code.encode("ascii"))
    digest.update(carrier_index.to_bytes(1, "big"))
    digest.update(bytes(roots))
    digest.update(bytes((w, x)))
    digest.update(repr(q_outcomes).encode("ascii"))


def main() -> None:
    carriers = screen.minimal_carriers()
    expected_baseline = {"FCQ`_": 249, "FCQb_": 740, "FCp`_": 209}

    for code in screen.LIVE_CODES:
        q_graph = base.decode_graph6(code)
        placements = tuple(screen.root_placements(q_graph))
        counts = collections.Counter()
        digest = hashlib.sha256()
        first = {}

        for carrier_index, carrier in enumerate(carriers):
            for roots in placements:
                graph = screen.add_q(carrier, roots, q_graph)
                marked = tuple(vertex in roots for vertex in range(9))
                if screen.rooted_k5minus(graph, marked):
                    continue
                counts["baseline_failures"] += 1
                protected = tuple(
                    vertex for vertex in range(9) if vertex not in roots
                )
                assert len(protected) == 2

                for w, x in (protected, protected[::-1]):
                    counts["ordered_marked_edges"] += 1
                    assert base.adjacent(graph, w, x)
                    q_neighbours = tuple(
                        q for q in roots if base.adjacent(graph, x, q)
                    )
                    assert q_neighbours
                    q_outcomes = []
                    for q in q_neighbours:
                        reduced = absorb_x_into_q(graph, marked, x, q)
                        closes = screen.rooted_k5minus(*reduced)
                        q_outcomes.append((q, closes))
                        counts["existing_xq_tests"] += 1
                        counts["existing_xq_failures"] += not closes
                        if not closes:
                            first.setdefault(
                                "failed_existing_xq",
                                (carrier_index, roots, w, x, q, graph),
                            )

                    outcomes = tuple(q_outcomes)
                    if not any(closes for _, closes in outcomes):
                        counts["no_usable_existing_xq"] += 1
                        first.setdefault(
                            "no_usable_existing_xq",
                            (carrier_index, roots, w, x, outcomes, graph),
                        )
                    if not all(closes for _, closes in outcomes):
                        counts["not_every_existing_xq_usable"] += 1

                    # A stronger diagnostic adds each absent x-Q edge before
                    # contracting it.  This is not inferred by the marked-edge
                    # theorem; it records whether the obstruction is the
                    # location of the actual contact.
                    all_q_outcomes = []
                    for q in roots:
                        augmented = add_edge(graph, x, q)
                        reduced = absorb_x_into_q(augmented, marked, x, q)
                        all_q_outcomes.append(
                            (q, screen.rooted_k5minus(*reduced))
                        )
                    if not any(closes for _, closes in all_q_outcomes):
                        counts["no_usable_arbitrary_xq"] += 1
                    if not all(closes for _, closes in all_q_outcomes):
                        counts["not_every_arbitrary_xq_usable"] += 1

                    update_digest(
                        digest,
                        code,
                        carrier_index,
                        roots,
                        w,
                        x,
                        outcomes,
                    )

        assert counts["baseline_failures"] == expected_baseline[code]
        assert counts["ordered_marked_edges"] == 2 * expected_baseline[code]
        print(code, dict(counts), flush=True)
        print(code, "first", first, flush=True)
        print(code, "digest", digest.hexdigest(), flush=True)

    print("GREEN: marked-edge absorption screen completed")
    print("rooted_minor_cache", screen.rooted_k5minus.cache_info())


if __name__ == "__main__":
    main()
