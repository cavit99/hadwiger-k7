#!/usr/bin/env python3
"""Exact nonclosure screen for the degree-eight Rolek--Song augmentation.

For every unlabelled K4-free graph J on eight vertices with alpha(J)=3,
test whether some independent triple S and some matching M of missing edges
of J-S make K1 join (J+M) contain K7-minus as a minor.

The matching condition is precisely what makes the external Rolek--Song
paths pairwise vertex-disjoint.  This checks a finite proof mechanism; it
does not infer an unbounded theorem.
"""

from __future__ import annotations

import itertools
import hashlib
import subprocess


ORDER = 8
EXPECTED_FAILURE_DIGEST = (
    "38666b7761e7ca1eff8174e3165b972ed114e4d4de2b2bf89e9ecb49e86636a6"
)
AUDITED_BOTH_FULL_CODES = {
    "GCOcaO",
    "GCOcbO",
    "GCOcbW",
    "GCOe`W",
    "GCOebW",
    "GCQQV?",
    "GCQR@O",
}


def decode_graph6(line: str) -> tuple[int, ...]:
    text = line.strip()
    assert text and ord(text[0]) - 63 == ORDER
    bits: list[int] = []
    for character in text[1:]:
        value = ord(character) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * ORDER
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def adjacent(graph: tuple[int, ...], left: int, right: int) -> bool:
    return bool(graph[left] & (1 << right))


def independent(graph: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(not adjacent(graph, a, b) for a, b in itertools.combinations(vertices, 2))


def clique(graph: tuple[int, ...], vertices: tuple[int, ...]) -> bool:
    return all(adjacent(graph, a, b) for a, b in itertools.combinations(vertices, 2))


def k4_free_alpha_three(graph: tuple[int, ...]) -> bool:
    if any(clique(graph, q) for q in itertools.combinations(range(ORDER), 4)):
        return False
    if not any(independent(graph, q) for q in itertools.combinations(range(ORDER), 3)):
        return False
    return not any(independent(graph, q) for q in itertools.combinations(range(ORDER), 4))


def set_partitions(items: tuple[int, ...], blocks: int):
    bags: list[int] = []

    def visit(position: int):
        if position == len(items):
            if len(bags) == blocks:
                yield tuple(bags)
            return
        bit = 1 << items[position]
        for index in range(len(bags)):
            bags[index] |= bit
            yield from visit(position + 1)
            bags[index] ^= bit
        if len(bags) < blocks:
            bags.append(bit)
            yield from visit(position + 1)
            bags.pop()

    yield from visit(0)


PARTITIONS = tuple(set_partitions(tuple(range(9)), 7))


def connected(graph: tuple[int, ...], mask: int) -> bool:
    seen = mask & -mask
    todo = seen
    while todo:
        bit = todo & -todo
        todo ^= bit
        vertex = bit.bit_length() - 1
        add = graph[vertex] & mask & ~seen
        seen |= add
        todo |= add
    return seen == mask


def bags_touch(graph: tuple[int, ...], left: int, right: int) -> bool:
    while left:
        bit = left & -left
        left ^= bit
        if graph[bit.bit_length() - 1] & right:
            return True
    return False


def target_model(graph: tuple[int, ...]):
    for bags in PARTITIONS:
        if not all(connected(graph, bag) for bag in bags):
            continue
        misses = []
        for left, right in itertools.combinations(range(7), 2):
            if not bags_touch(graph, bags[left], bags[right]):
                misses.append((left, right))
                if len(misses) > 1:
                    break
        if len(misses) <= 1:
            return bags, tuple(misses)
    return None


def matchings(edges: tuple[tuple[int, int], ...]):
    yield ()
    for order in (1, 2):
        for chosen in itertools.combinations(edges, order):
            ends = tuple(vertex for edge in chosen for vertex in edge)
            if len(set(ends)) == 2 * order:
                yield chosen


def augmented(graph: tuple[int, ...], matching: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    result = list(graph) + [0]
    apex = ORDER
    for vertex in range(ORDER):
        result[vertex] |= 1 << apex
        result[apex] |= 1 << vertex
    for left, right in matching:
        result[left] |= 1 << right
        result[right] |= 1 << left
    return tuple(result)


def witness(graph: tuple[int, ...]):
    for roots in itertools.combinations(range(ORDER), 3):
        if not independent(graph, roots):
            continue
        remainder = tuple(vertex for vertex in range(ORDER) if vertex not in roots)
        missing = tuple(
            edge
            for edge in itertools.combinations(remainder, 2)
            if not adjacent(graph, *edge)
        )
        for matching in matchings(missing):
            model = target_model(augmented(graph, matching))
            if model is not None:
                return roots, matching, model
    return None


def main() -> None:
    lines = subprocess.check_output(("geng", "-q", "8"), text=True).splitlines()
    candidates = []
    failures = []
    matching_sizes: dict[int, int] = {}
    for line in lines:
        graph = decode_graph6(line)
        if not k4_free_alpha_three(graph):
            continue
        candidates.append(line)
        found = witness(graph)
        if found is None:
            failures.append(line)
        else:
            size = len(found[1])
            matching_sizes[size] = matching_sizes.get(size, 0) + 1
    failure_digest = hashlib.sha256(
        ("\n".join(sorted(failures)) + "\n").encode()
    ).hexdigest()
    assert len(PARTITIONS) == 462
    assert len(candidates) == 2076
    assert matching_sizes == {2: 419, 1: 281, 0: 73}
    assert len(failures) == 1303
    assert failure_digest == EXPECTED_FAILURE_DIGEST
    assert AUDITED_BOTH_FULL_CODES <= set(failures)

    print("partitions=462")
    print("candidates=2076 closed=773 failures=1303")
    print("matching_sizes=0:73,1:281,2:419")
    print(f"failure-code sha256={failure_digest}")
    print("audited-both-full-seven closed=0 failures=7")
    print("PASS Rolek-Song matching augmentation nonclosure")


if __name__ == "__main__":
    main()
