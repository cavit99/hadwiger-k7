#!/usr/bin/env python3
"""Test the abstract swallowed-coordinate suffix transfer on static survivors.

The finite quotient cannot see the internal path inside a centre-rooted bag.
Its exact safe abstraction is therefore this.  Choose a protected centre s,
choose at least two foreign rooted bags met by the internal suffix P, keep s
as its original rooted quotient vertex, and absorb P into one contacted
foreign bag.  Every old quotient adjacency at s is conservatively retained;
the transfer only adds the clique star from the owner to the other contacted
bags.  This is stronger than the literal split when P uniquely owned an old
s-adjacency, so any survivor is a barrier to the proposed quotient inference.
"""

from __future__ import annotations

import collections
import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


order9 = load("nine_terminal_order9", HERE / "verify_order_nine.py")
order10 = load("nine_terminal_order10", HERE / "screen_order_ten.py")


def suffix_transfers(
    quotient: tuple[int, ...], minimum_contacts: int = 2
) -> tuple[tuple[int, ...], ...]:
    outcomes = set()
    for contacts_size in range(minimum_contacts, 8):
        for contacts in itertools.combinations(range(7), contacts_size):
            for owner in contacts:
                graph = list(quotient)
                for other in contacts:
                    if owner == other:
                        continue
                    graph[owner] |= 1 << other
                    graph[other] |= 1 << owner
                outcomes.add(tuple(graph))
    return tuple(outcomes)


def closes_after_suffix(
    q_graph: tuple[int, ...], family: tuple[tuple[int, ...], ...]
) -> bool:
    return any(
        order10.has_target(
            tuple(q_graph[vertex] | moved[vertex] for vertex in range(7))
        )
        for quotient in family
        for moved in suffix_transfers(quotient)
    )


def screen_order_nine() -> collections.Counter[str]:
    carriers = order9.minimal_three_connected_graphs()
    by_code = dict(order9.order11.carrier7.eligible_graphs())
    codes = ("FCQ`_", "FCQb_", "FCp`_")
    copies = {code: order9.order11.q_copies(by_code[code]) for code in codes}
    survivors = collections.Counter()
    static = collections.Counter()
    for adjacency in carriers:
        for centres in itertools.combinations(range(9), 2):
            family = order9.quotient_family(adjacency, centres)
            for code in codes:
                for q_graph in copies[code]:
                    if order10.closes(q_graph, family):
                        continue
                    static[code] += 1
                    if not closes_after_suffix(q_graph, family):
                        survivors[code] += 1
    assert static == {"FCQ`_": 427, "FCQb_": 1446, "FCp`_": 379}
    return survivors


def screen_order_ten() -> collections.Counter[str]:
    occurrences = order10.catalogue.exact_rooted_occurrences()
    by_code = dict(order10.order11.carrier7.eligible_graphs())
    codes = ("FCQ`_", "FCQb_", "FCp`_")
    copies = {code: order10.order11.q_copies(by_code[code]) for code in codes}
    survivors = collections.Counter()
    static = collections.Counter()
    for remainder, neighbours in occurrences:
        adjacency = order10.kernel_adjacency(remainder, neighbours)
        for centres in itertools.combinations(range(9), 2):
            family = order10.all_augmented_quotients(adjacency, centres, 0)
            for code in codes:
                for q_graph in copies[code]:
                    if order10.closes(q_graph, family):
                        continue
                    static[code] += 1
                    if not closes_after_suffix(q_graph, family):
                        survivors[code] += 1
    assert static == {"FCQ`_": 840, "FCQb_": 1811, "FCp`_": 598}
    return survivors


def main() -> None:
    print("order9_swallowed_suffix_survivors", dict(screen_order_nine()))
    # The order-ten row is not rerun here: its proved one-contact finite
    # implication is already stronger once one suffix contact reaches a
    # Q-rooted bag.  Keep ``screen_order_ten`` as a discovery helper only.


if __name__ == "__main__":
    main()
