#!/usr/bin/env python3
"""Exact two-protected-centre composition for order-eleven kernels.

Terminals 0,...,8 consist of seven Q roots and two protected exterior
centres; 9,10 are the two nonterminals.  Wu's disjoint charge sets leave
two cases.  The charge-complete C9 case is checked by ``probe.py``.  This
verifier generates the one-uncharged-terminal case from its exact bouquet
description, filters for three-connectivity and terminal irreducibility,
and checks every placement of the two protected centres and every labelled
copy of each live Q type.

For each placement it enumerates every connected assignment of the four
non-Q bags (the protected centres and the two nonterminals) to the seven
Q-rooted bags.  The resulting quotient, together with the literal Q edges,
is tested exactly for a K_5^- minor.
"""

from __future__ import annotations

import collections
import functools
import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


ROOT = Path(__file__).resolve().parents[3]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


carrier7 = load(
    "dominated_rooted_seven_carrier",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_rooted_seven_carrier"
    / "verify.py",
)
base = carrier7._base


def connected(adjacency: tuple[int, ...], removed: int = 0) -> bool:
    alive = ((1 << len(adjacency)) - 1) & ~removed
    if not alive:
        return True
    first = (alive & -alive).bit_length() - 1
    reached = 1 << first
    while True:
        old = reached
        scan = reached
        while scan:
            bit = scan & -scan
            vertex = bit.bit_length() - 1
            scan -= bit
            reached |= adjacency[vertex] & alive
        if reached == old:
            return reached == alive


def is_three_connected(adjacency: tuple[int, ...]) -> bool:
    return all(
        connected(adjacency, sum(1 << vertex for vertex in cut))
        for size in range(3)
        for cut in itertools.combinations(range(len(adjacency)), size)
    )


def deletion_is_two_connected(
    adjacency: tuple[int, ...], left: int, right: int
) -> bool:
    removed = (1 << left) | (1 << right)
    return connected(adjacency, removed) and all(
        connected(adjacency, removed | (1 << vertex))
        for vertex in range(len(adjacency))
        if vertex not in (left, right)
    )


def compositions(total: int, parts: int):
    if parts == 1:
        if total >= 2:
            yield (total,)
        return
    for first in range(2, total - 2 * (parts - 1) + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def exact_one_uncharged_skeletons():
    """Generate the exact canonical finite skeleton list.

    Vertex 8 is the uncharged terminal z, 9 and 10 are the ordered
    nonterminals, and 0,...,7 are their four-plus-four charged terminals.
    Every possible bouquet path-length composition, charge assignment and
    choice of xz,yz,xy is generated before the exact host filters are used.
    """

    survivors = []
    generated = 0
    for path_count in range(1, 5):
        for lengths in compositions(8, path_count):
            terminal_edges = []
            position = 0
            for length in lengths:
                path = tuple(range(position, position + length))
                position += length
                terminal_edges.extend(((8, path[0]), (8, path[-1])))
                terminal_edges.extend(zip(path, path[1:]))

            for x_tuple in itertools.combinations(range(8), 4):
                x_neighbours = set(x_tuple)
                y_neighbours = set(range(8)) - x_neighbours
                for optional in range(8):
                    generated += 1
                    adjacency = [0] * 11
                    for left, right in terminal_edges:
                        add_edge(adjacency, left, right)
                    for terminal in x_neighbours:
                        add_edge(adjacency, 9, terminal)
                    for terminal in y_neighbours:
                        add_edge(adjacency, 10, terminal)
                    for bit, edge in enumerate(((9, 8), (10, 8), (9, 10))):
                        if optional >> bit & 1:
                            add_edge(adjacency, *edge)

                    encoded = tuple(adjacency)
                    if not is_three_connected(encoded):
                        continue
                    legal_edges = {
                        tuple(sorted((nonterminal, neighbour)))
                        for nonterminal in (9, 10)
                        for neighbour in range(11)
                        if adjacency[nonterminal] >> neighbour & 1
                    }
                    if any(
                        deletion_is_two_connected(encoded, *edge)
                        for edge in legal_edges
                    ):
                        continue
                    # The structural branch presently generated assumes
                    # terminal 8 is outside the union of the *complete*
                    # Wu-special neighbour sets.  Exclude parameters in
                    # which it is itself a special neighbour of x or y;
                    # those belong to the charge-complete branch checked
                    # independently by probe.py.
                    if adjacency[8].bit_count() == 3:
                        terminal_neighbours = tuple(
                            vertex
                            for vertex in range(9)
                            if adjacency[8] >> vertex & 1
                        )
                        assert len(terminal_neighbours) == 2
                        if any(
                            adjacency[nonterminal] >> 8 & 1
                            and all(
                                deletion_is_two_connected(
                                    encoded, 8, terminal
                                )
                                for terminal in terminal_neighbours
                            )
                            for nonterminal in (9, 10)
                        ):
                            continue
                    survivors.append((lengths, x_tuple, optional, encoded))

    assert generated == 13 * 70 * 8
    assert len(survivors) == 34
    assert collections.Counter(lengths for lengths, *_ in survivors) == {
        (8,): 2,
        (4, 4): 32,
    }
    return tuple(survivors)


def q_copies(adjacency: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    answer = set()
    for permutation in itertools.permutations(range(7)):
        graph = [0] * 7
        for left, right in itertools.combinations(range(7), 2):
            if adjacency[left] >> right & 1:
                image_left, image_right = permutation[left], permutation[right]
                graph[image_left] |= 1 << image_right
                graph[image_right] |= 1 << image_left
        answer.add(tuple(graph))
    return tuple(sorted(answer))


def group_is_connected(adjacency: tuple[int, ...], group: set[int]) -> bool:
    first = min(group)
    reached = {first}
    while True:
        old = set(reached)
        reached |= {
            vertex
            for vertex in group
            if any(adjacency[vertex] >> seen & 1 for seen in reached)
        }
        if reached == old:
            return reached == group


def quotient_family(
    adjacency: tuple[int, ...], centres: tuple[int, int]
) -> tuple[tuple[int, ...], ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    extras = centres + (9, 10)
    outcomes = set()
    for owners in itertools.product(range(7), repeat=4):
        groups = [{root} for root in roots]
        for extra, owner in zip(extras, owners, strict=True):
            groups[owner].add(extra)
        if not all(group_is_connected(adjacency, group) for group in groups):
            continue
        quotient = [0] * 7
        for left, right in itertools.combinations(range(7), 2):
            if any(
                adjacency[u] >> v & 1
                for u in groups[left]
                for v in groups[right]
            ):
                quotient[left] |= 1 << right
                quotient[right] |= 1 << left
        outcomes.add(tuple(quotient))
    return tuple(
        sorted(
            outcomes,
            key=lambda graph: sum(row.bit_count() for row in graph),
            reverse=True,
        )
    )


@functools.lru_cache(maxsize=None)
def has_target(adjacency: tuple[int, ...]) -> bool:
    return base.has_dense_minor(adjacency, 5, 9)


def main() -> None:
    skeletons = exact_one_uncharged_skeletons()
    by_code = dict(carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    copies = {code: q_copies(by_code[code]) for code in live_codes}
    assert {code: len(family) for code, family in copies.items()} == {
        "FCQ`_": 252,
        "FCQb_": 2520,
        "FCp`_": 360,
    }

    tests = collections.Counter()
    failures = collections.Counter()
    first_failure = {}
    family_sizes = collections.Counter()
    for lengths, x_tuple, optional, adjacency in skeletons:
        for centres in itertools.combinations(range(9), 2):
            quotients = quotient_family(adjacency, centres)
            assert quotients
            family_sizes[len(quotients)] += 1
            for code in live_codes:
                for q_graph in copies[code]:
                    tests[code] += 1
                    if any(
                        has_target(
                            tuple(
                                q_graph[vertex] | quotient[vertex]
                                for vertex in range(7)
                            )
                        )
                        for quotient in quotients
                    ):
                        continue
                    failures[code] += 1
                    first_failure.setdefault(
                        code,
                        (lengths, x_tuple, optional, centres, q_graph),
                    )

    expected_placements = 34 * 36
    assert sum(family_sizes.values()) == expected_placements
    assert tests == {
        code: expected_placements * len(copies[code]) for code in live_codes
    }
    assert not failures
    assert not first_failure
    print("canonical_skeletons", len(skeletons))
    print("protected_centre_placements", expected_placements)
    print("q_copy_counts", {code: len(copies[code]) for code in live_codes})
    print("quotient_family_sizes", dict(sorted(family_sizes.items())))
    print("tests", dict(tests))
    print("failures", dict(failures))
    print("first_failure", first_failure)
    print("minor_cache", has_target.cache_info())


if __name__ == "__main__":
    main()
