#!/usr/bin/env python3
"""Discovery screen for the nine-terminal, two-nonterminal kernel.

The seven vertices 0,...,6 are the common-neighbour graph Q, 7 and 8 are
two protected exterior centres, and 9,10 are the two nonterminals.  This
first screen treats the charge-complete normal form: the terminal graph is
a 9-cycle, and the two nonterminals see complementary colour classes of
orders four and five with cyclic runs 2,2 and 2,3.

For every labelled normal form and each of the three live Q types, the
screen tries every legal absorption of the two nonterminals and every
connected assignment of the two protected-centre bags to Q-rooted bags.
The final seven-vertex quotient is tested exactly for a K_5^- minor.
"""

from __future__ import annotations

import functools
import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


ROOT = Path(__file__).resolve().parents[3]
PAIRS9 = tuple(itertools.combinations(range(9), 2))
PAIR9 = {edge: index for index, edge in enumerate(PAIRS9)}


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


def edge_mask(edges: tuple[tuple[int, int], ...]) -> int:
    return sum(1 << PAIR9[tuple(sorted(edge))] for edge in edges)


def adjacent(mask: int, left: int, right: int) -> bool:
    if left == right:
        return False
    return bool(mask >> PAIR9[tuple(sorted((left, right)))] & 1)


def labelled_cycles():
    for tail in itertools.permutations(range(1, 9)):
        cycle = (0,) + tail
        if cycle[1] > cycle[-1]:
            continue
        yield cycle


def cyclic_runs(bits: tuple[int, ...]) -> tuple[int, ...]:
    assert len(set(bits)) == 2
    start = next(index for index in range(9) if bits[index] != bits[index - 1])
    answer = []
    current = bits[start]
    length = 0
    for offset in range(9):
        value = bits[(start + offset) % 9]
        if value != current:
            answer.append(length)
            current = value
            length = 0
        length += 1
    answer.append(length)
    return tuple(answer)


PATTERNS = tuple(
    bits
    for bits in itertools.product((0, 1), repeat=9)
    if sum(bits) == 4
    and len(cyclic_runs(bits)) == 4
    and min(cyclic_runs(bits)) >= 2
)


def quotient_after_absorption(
    cycle: tuple[int, ...], a_vertices: frozenset[int], owner_x: int, owner_y: int
) -> tuple[int, ...]:
    graph = [0] * 9
    for index in range(9):
        left, right = cycle[index], cycle[(index + 1) % 9]
        graph[left] |= 1 << right
        graph[right] |= 1 << left
    b_vertices = set(range(9)) - a_vertices
    for owner, neighbours in ((owner_x, a_vertices), (owner_y, b_vertices)):
        for other in neighbours:
            if other == owner:
                continue
            graph[owner] |= 1 << other
            graph[other] |= 1 << owner
    return tuple(graph)


def connected_assignment(graph: tuple[int, ...], owner7: int, owner8: int) -> bool:
    for root in range(7):
        group = {root}
        if owner7 == root:
            group.add(7)
        if owner8 == root:
            group.add(8)
        if len(group) == 1:
            continue
        reached = {root}
        while True:
            old = set(reached)
            reached |= {
                vertex
                for vertex in group
                if any(graph[vertex] >> seen & 1 for seen in reached)
            }
            if reached == old:
                break
        if reached != group:
            return False
    return True


def absorb_centres(
    graph: tuple[int, ...], owner7: int, owner8: int
) -> tuple[int, ...]:
    groups = [{root} for root in range(7)]
    groups[owner7].add(7)
    groups[owner8].add(8)
    quotient = [0] * 7
    for left, right in itertools.combinations(range(7), 2):
        if any(
            graph[u] >> v & 1
            for u in groups[left]
            for v in groups[right]
        ):
            quotient[left] |= 1 << right
            quotient[right] |= 1 << left
    return tuple(quotient)


@functools.lru_cache(maxsize=None)
def closes(q_graph: tuple[int, ...], quotient: tuple[int, ...]) -> bool:
    union = tuple(q_graph[index] | quotient[index] for index in range(7))
    return base.has_dense_minor(union, 5, 9)


def main() -> None:
    assert len(PATTERNS) == 9
    by_code = dict(carrier7.eligible_graphs())
    live_codes = ("FCQ`_", "FCQb_", "FCp`_")
    failures = {code: 0 for code in live_codes}
    tests = 0
    first = {}

    for cycle in labelled_cycles():
        for bits in PATTERNS:
            a_vertices = frozenset(cycle[index] for index, bit in enumerate(bits) if bit)
            b_vertices = set(range(9)) - a_vertices
            for code in live_codes:
                q_graph = by_code[code]
                tests += 1
                closed = False
                for owner_x in a_vertices:
                    if closed:
                        break
                    for owner_y in b_vertices:
                        graph = quotient_after_absorption(
                            cycle, a_vertices, owner_x, owner_y
                        )
                        for owner7, owner8 in itertools.product(range(7), repeat=2):
                            if not connected_assignment(graph, owner7, owner8):
                                continue
                            quotient = absorb_centres(graph, owner7, owner8)
                            if closes(q_graph, quotient):
                                closed = True
                                break
                        if closed:
                            break
                if not closed:
                    failures[code] += 1
                    first.setdefault(code, (cycle, bits))

    assert tests == 20_160 * 9 * 3
    assert not any(failures.values())
    assert not first
    print("patterns", len(PATTERNS), "tests", tests)
    print("failures", failures)
    print("first", first)
    print("minor_cache", closes.cache_info())


if __name__ == "__main__":
    main()
