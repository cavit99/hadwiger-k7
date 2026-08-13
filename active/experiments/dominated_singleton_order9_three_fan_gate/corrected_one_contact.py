#!/usr/bin/env python3
"""Recompute the order-nine one-contact screen with exactly one added edge.

The historical helper passed `(contact, 0)` to a two-contact routine and
therefore added a hidden edge at the other protected centre.  This script
uses a literal one-edge augmentation and reports replacement counts.
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


order9 = load(
    "corrected_one_contact_base",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_kernel"
    / "verify_order_nine.py",
)


def add_single_contact(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    selected: int,
    contact: int,
) -> tuple[int, ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    centre = centres[selected]
    root = roots[contact]
    answer = list(adjacency)
    answer[centre] |= 1 << root
    answer[root] |= 1 << centre
    return tuple(answer)


def closes(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
) -> bool:
    return any(
        order9.has_target(
            tuple(
                q_graph[vertex] | quotient[vertex]
                for vertex in range(7)
            )
        )
        for quotient in order9.quotient_family(adjacency, centres)
    )


def main() -> None:
    carriers = order9.minimal_three_connected_graphs()
    by_code = dict(order9.order11.carrier7.eligible_graphs())
    expected = {"FCQ`_": 427, "FCQb_": 1_446, "FCp`_": 379}
    expected_profiles = {
        "FCQ`_": {(True, True): 325, (True, False): 102},
        "FCQb_": {(True, True): 1_242, (True, False): 204},
        "FCp`_": {(True, True): 334, (True, False): 45},
    }
    expected_profiles = {
        "FCQ`_": {(True, True): 325, (True, False): 102},
        "FCQb_": {(True, True): 1_242, (True, False): 204},
        "FCp`_": {(True, True): 334, (True, False): 45},
    }

    for code, expected_static in expected.items():
        copies = order9.order11.q_copies(by_code[code])
        counts = collections.Counter()
        profiles = collections.Counter()
        digest = hashlib.sha256()
        first = {}

        for carrier_index, adjacency in enumerate(carriers):
            for centres in itertools.combinations(range(9), 2):
                for q_graph in copies:
                    if closes(adjacency, centres, q_graph):
                        continue
                    counts["static_failures"] += 1
                    centre_closes = []
                    for selected in range(2):
                        outcomes = tuple(
                            closes(
                                add_single_contact(
                                    adjacency,
                                    centres,
                                    selected,
                                    contact,
                                ),
                                centres,
                                q_graph,
                            )
                            for contact in range(7)
                        )
                        centre_closes.append(any(outcomes))
                        counts["contact_tests"] += len(outcomes)
                        counts["successful_contact_tests"] += sum(outcomes)
                    profile = tuple(centre_closes)
                    profiles[profile] += 1
                    counts["some_centre_closes"] += any(profile)
                    counts["both_centres_close"] += all(profile)
                    if not any(profile):
                        counts["no_single_contact_closes"] += 1
                        first.setdefault(
                            "no_single_contact",
                            (carrier_index, centres, q_graph, adjacency),
                        )
                    digest.update(carrier_index.to_bytes(1, "big"))
                    digest.update(bytes(centres))
                    digest.update(bytes(q_graph))
                    digest.update(bytes(profile))

        assert counts["static_failures"] == expected_static
        assert profiles == expected_profiles[code]
        assert counts["some_centre_closes"] == expected_static
        assert counts["both_centres_close"] == expected_profiles[code][
            (True, True)
        ]
        assert dict(profiles) == expected_profiles[code]
        print(code, dict(counts), flush=True)
        print(code, "profiles", dict(profiles), flush=True)
        print(code, "first", first, flush=True)
        print(code, "digest", digest.hexdigest(), flush=True)

    print("GREEN: corrected one-contact screen completed")
    print("minor_cache", order9.has_target.cache_info())
    print("k7minus_cache", order9.has_k7_minus.cache_info())


if __name__ == "__main__":
    main()
