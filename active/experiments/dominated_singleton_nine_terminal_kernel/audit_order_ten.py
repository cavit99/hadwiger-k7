#!/usr/bin/env python3
"""Independent audit of the order-ten one-contact composition.

This script does not import the discovery catalogue, composition screen or
their minor routine.  It independently decodes the nauty stream, applies
the deletion form of the contractibility criterion, generates the three Q
families, and detects K_5^- minors by connected five-bag partitions.
"""

from __future__ import annotations

import collections
import functools
import hashlib
import itertools
import subprocess


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


def decode_graph6(line: bytes) -> tuple[int, ...]:
    data = line.strip()
    order = data[0] - 63
    bits = []
    for value in data[1:]:
        value -= 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * order
    position = 0
    for right in range(1, order):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def connected(adjacency: tuple[int, ...], alive: int) -> bool:
    if not alive:
        return True
    reached = alive & -alive
    while True:
        old = reached
        scan = reached
        while scan:
            bit = scan & -scan
            scan -= bit
            reached |= adjacency[bit.bit_length() - 1] & alive
        if reached == old:
            return reached == alive


def two_connected_after_pair(
    adjacency: tuple[int, ...], left: int, right: int
) -> bool:
    alive = ((1 << len(adjacency)) - 1) & ~(1 << left) & ~(1 << right)
    return connected(adjacency, alive) and all(
        connected(adjacency, alive & ~(1 << vertex))
        for vertex in range(len(adjacency))
        if alive >> vertex & 1
    )


def three_connected(adjacency: tuple[int, ...]) -> bool:
    all_vertices = (1 << len(adjacency)) - 1
    return all(
        connected(
            adjacency,
            all_vertices & ~sum(1 << vertex for vertex in cut),
        )
        for size in range(3)
        for cut in itertools.combinations(range(len(adjacency)), size)
    )


def edge_mask(adjacency: tuple[int, ...]) -> int:
    position = 0
    answer = 0
    for right in range(1, len(adjacency)):
        for left in range(right):
            if adjacency[left] >> right & 1:
                answer |= 1 << position
            position += 1
    return answer


def rooted_occurrences():
    process = subprocess.Popen(
        ["geng", "-Cq", "-d2", "9"], stdout=subprocess.PIPE
    )
    assert process.stdout is not None
    answer = []
    for line in process.stdout:
        remainder = decode_graph6(line)
        degree_two = tuple(
            vertex for vertex in range(9) if remainder[vertex].bit_count() == 2
        )
        if len(degree_two) < 4:
            continue
        optional = tuple(vertex for vertex in range(9) if vertex not in degree_two)
        for selection in range(1 << len(optional)):
            neighbours = set(degree_two) | {
                vertex
                for index, vertex in enumerate(optional)
                if selection >> index & 1
            }
            kernel = list(remainder) + [0]
            for vertex in neighbours:
                kernel[vertex] |= 1 << 9
                kernel[9] |= 1 << vertex
            kernel = tuple(kernel)
            if not three_connected(kernel):
                continue
            if any(
                two_connected_after_pair(kernel, 9, vertex)
                for vertex in neighbours
            ):
                continue
            answer.append((remainder, frozenset(neighbours), kernel))
    assert process.wait() == 0
    assert len(answer) == 1_153
    return tuple(answer)


def occurrence_digest(occurrences) -> str:
    digest = hashlib.sha256()
    for remainder, neighbours, _kernel in sorted(
        occurrences,
        key=lambda item: (edge_mask(item[0]), sum(1 << v for v in item[1])),
    ):
        digest.update(edge_mask(remainder).to_bytes(5, "big"))
        digest.update(sum(1 << v for v in neighbours).to_bytes(2, "big"))
    return digest.hexdigest()


def labelled_copies(code: str) -> tuple[int, ...]:
    base = decode_graph6(code.encode())
    answer = set()
    for permutation in itertools.permutations(range(7)):
        mask = 0
        position = 0
        for right in range(1, 7):
            for left in range(right):
                old_left = permutation[left]
                old_right = permutation[right]
                if base[old_left] >> old_right & 1:
                    mask |= 1 << position
                position += 1
        answer.add(mask)
    return tuple(sorted(answer))


def set_partitions(elements: tuple[int, ...], parts: int):
    if parts == 1:
        yield (sum(1 << element for element in elements),)
        return
    first = elements[0]
    tail = elements[1:]
    for size in range(0, len(tail) + 1):
        for chosen in itertools.combinations(tail, size):
            block = (1 << first) | sum(1 << element for element in chosen)
            remaining = tuple(element for element in tail if element not in chosen)
            if len(remaining) < parts - 1:
                continue
            for partition in set_partitions(remaining, parts - 1):
                yield (block,) + partition


PARTITIONS = tuple(
    partition
    for size in range(5, 8)
    for subset in itertools.combinations(range(7), size)
    for partition in set_partitions(subset, 5)
)


def mask_adjacency(mask: int) -> tuple[int, ...]:
    answer = [0] * 7
    position = 0
    for right in range(1, 7):
        for left in range(right):
            if mask >> position & 1:
                answer[left] |= 1 << right
                answer[right] |= 1 << left
            position += 1
    return tuple(answer)


@functools.lru_cache(maxsize=None)
def has_k5_minus(mask: int) -> bool:
    adjacency = mask_adjacency(mask)
    for partition in PARTITIONS:
        if not all(connected(adjacency, bag) for bag in partition):
            continue
        contacts = sum(
            any(
                adjacency[vertex] & right
                for vertex in range(7)
                if left >> vertex & 1
            )
            for left, right in itertools.combinations(partition, 2)
        )
        if contacts >= 9:
            return True
    return False


def quotient_mask(
    adjacency: tuple[int, ...],
    roots: tuple[int, ...],
    extras: tuple[int, int, int],
    owners: tuple[int, int, int],
) -> int:
    groups = [{root} for root in roots]
    for extra, owner in zip(extras, owners, strict=True):
        groups[owner].add(extra)
    mask = 0
    position = 0
    for right in range(1, 7):
        for left in range(right):
            if any(
                adjacency[u] >> v & 1
                for u in groups[left]
                for v in groups[right]
            ):
                mask |= 1 << position
            position += 1
    return mask


def one_contact_family(
    kernel: tuple[int, ...], centres: tuple[int, int]
) -> tuple[int, ...]:
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    extras = centres + (9,)
    outcomes = set()
    for selected in range(2):
        for contact in range(7):
            adjacency = list(kernel)
            centre = centres[selected]
            root = roots[contact]
            adjacency[centre] |= 1 << root
            adjacency[root] |= 1 << centre
            adjacency = tuple(adjacency)
            owner_sets = tuple(
                tuple(
                    owner
                    for owner, root_vertex in enumerate(roots)
                    if adjacency[extra] >> root_vertex & 1
                )
                for extra in extras
            )
            for owners in itertools.product(*owner_sets):
                outcomes.add(quotient_mask(adjacency, roots, extras, owners))
    return tuple(sorted(outcomes, key=int.bit_count, reverse=True))


def main() -> None:
    occurrences = rooted_occurrences()
    digest = occurrence_digest(occurrences)
    # The discovery screen already ranges over every labelled Q copy.  This
    # independent replay uses one canonical labelled copy of each type while
    # ranging over every centre placement in each unlabelled rooted kernel;
    # it is a materially different, smaller orbit-level check.
    copies = {
        code: edge_mask(decode_graph6(code.encode()))
        for code in ("FCQ`_", "FCQb_", "FCp`_")
    }

    tests = collections.Counter()
    failures = collections.Counter()
    for _remainder, _neighbours, kernel in occurrences:
        for centres in itertools.combinations(range(9), 2):
            quotients = one_contact_family(kernel, centres)
            assert quotients
            for code, q_mask in copies.items():
                tests[code] += 1
                if not any(has_k5_minus(q_mask | quotient) for quotient in quotients):
                    failures[code] += 1

    expected = 1_153 * 36
    assert tests == {code: expected for code in copies}
    assert not failures
    print("independent_order_ten_occurrences", len(occurrences))
    print("occurrence_digest", digest)
    print("tests", dict(tests))
    print("one_contact_failures", dict(failures))
    print("partition_count", len(PARTITIONS))
    print("minor_cache", has_k5_minus.cache_info())


if __name__ == "__main__":
    main()
