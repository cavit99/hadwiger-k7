#!/usr/bin/env python3
"""Verify the finite quotient used by the degree-seven reduction.

For every seven-vertex graph F of maximum degree at most two, form R=K_7-F.
Add a vertex v complete to R and a vertex c adjacent to either all of R or
all but one prescribed vertex.  The script constructs and checks a K_7^-
minor model in every resulting nine-vertex graph.

The 29 isomorphism types of F are generated directly as disjoint unions of
paths and cycles.  No graph library, solver, or stored bulk data is used.
"""

from __future__ import annotations

import hashlib
import itertools
from collections.abc import Iterator, Sequence


ROOTS = tuple(range(7))
V = 7
C = 8
ORDER = 9


def require(condition: bool, message: str) -> None:
    """Raise an always-active verification error when condition fails."""

    if not condition:
        raise RuntimeError(message)


def component_multisets(
    remaining: int = 7,
    minimum: tuple[int, str] = (1, "P"),
) -> Iterator[tuple[tuple[int, str], ...]]:
    """Generate the isomorphism types of max-degree-two graphs on 7 vertices."""

    choices = tuple(
        sorted(
            [(size, "P") for size in range(1, 8)]
            + [(size, "C") for size in range(3, 8)]
        )
    )
    if remaining == 0:
        yield ()
        return
    for choice in choices:
        if choice < minimum or choice[0] > remaining:
            continue
        for tail in component_multisets(remaining - choice[0], choice):
            yield (choice,) + tail


def complement_type(signature: Sequence[tuple[int, str]]) -> tuple[int, ...]:
    """Return adjacency masks for the path/cycle union encoded by signature."""

    adjacency = [0] * 7
    first = 0
    for size, kind in signature:
        vertices = tuple(range(first, first + size))
        for left, right in zip(vertices, vertices[1:]):
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
        if kind == "C":
            require(size >= 3, "a cycle component must have order at least three")
            adjacency[vertices[0]] |= 1 << vertices[-1]
            adjacency[vertices[-1]] |= 1 << vertices[0]
        first += size
    require(first == 7, "component signature does not have order seven")
    require(max(mask.bit_count() for mask in adjacency) <= 2, "degree bound failed")
    return tuple(adjacency)


def quotient(complement: Sequence[int], missed_root: int | None) -> tuple[int, ...]:
    """Build the nine-vertex quotient from F and its exterior attachment set."""

    full_roots = (1 << 7) - 1
    adjacency = [0] * ORDER
    for root in ROOTS:
        adjacency[root] = (full_roots ^ (1 << root) ^ complement[root]) | (1 << V)
        adjacency[V] |= 1 << root
        if root != missed_root:
            adjacency[root] |= 1 << C
            adjacency[C] |= 1 << root
    return tuple(adjacency)


def set_partitions(items: Sequence[int], blocks: int) -> Iterator[tuple[int, ...]]:
    """Yield each partition of items into the requested number of bitmask blocks."""

    bags: list[int] = []

    def visit(index: int) -> Iterator[tuple[int, ...]]:
        if index == len(items):
            if len(bags) == blocks:
                yield tuple(bags)
            return
        bit = 1 << items[index]
        for position in range(len(bags)):
            bags[position] |= bit
            yield from visit(index + 1)
            bags[position] ^= bit
        if len(bags) < blocks:
            bags.append(bit)
            yield from visit(index + 1)
            bags.pop()

    yield from visit(0)


def model_candidates() -> Iterator[tuple[int, ...]]:
    """Enumerate every possible seven-bag model on at most nine vertices."""

    vertices = tuple(range(ORDER))
    for used_order in range(7, ORDER + 1):
        for used in itertools.combinations(vertices, used_order):
            yield from set_partitions(used, 7)


CANDIDATES = tuple(model_candidates())


def connected(mask: int, adjacency: Sequence[int]) -> bool:
    """Test connectivity of one nonempty branch set."""

    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adjacency[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def touch(first: int, second: int, adjacency: Sequence[int]) -> bool:
    """Return whether two branch sets have an edge between them."""

    neighbours = 0
    scan = first
    while scan:
        bit = scan & -scan
        scan ^= bit
        neighbours |= adjacency[bit.bit_length() - 1]
    return bool(neighbours & second)


def missing_pairs(bags: Sequence[int], adjacency: Sequence[int]) -> tuple[tuple[int, int], ...]:
    """List pairs of nonadjacent branch-set indices."""

    return tuple(
        (left, right)
        for left, right in itertools.combinations(range(len(bags)), 2)
        if not touch(bags[left], bags[right], adjacency)
    )


def find_model(adjacency: Sequence[int]) -> tuple[int, ...] | None:
    """Find an exact certificate for a K_7^- minor, if one exists."""

    for bags in CANDIDATES:
        if not all(connected(bag, adjacency) for bag in bags):
            continue
        if len(missing_pairs(bags, adjacency)) <= 1:
            return bags
    return None


def check_model(bags: Sequence[int], adjacency: Sequence[int]) -> None:
    """Independently check the structural conditions of a returned model."""

    require(len(bags) == 7, "wrong number of branch sets")
    require(all(bags), "empty branch set")
    union = 0
    for bag in bags:
        require(not union & bag, "branch sets overlap")
        union |= bag
        require(connected(bag, adjacency), "disconnected branch set")
    require(len(missing_pairs(bags, adjacency)) <= 1, "more than one missing adjacency")


def self_test() -> None:
    """Test the model search on small known positive and negative examples."""

    k7_minus = [0] * ORDER
    for left, right in itertools.combinations(range(7), 2):
        if (left, right) == (0, 1):
            continue
        k7_minus[left] |= 1 << right
        k7_minus[right] |= 1 << left
    require(find_model(k7_minus) is not None, "positive K_7^- self-test failed")

    k6 = [0] * ORDER
    for left, right in itertools.combinations(range(6), 2):
        k6[left] |= 1 << right
        k6[right] |= 1 << left
    require(find_model(k6) is None, "negative K_6 self-test failed")

    k2222 = [0] * ORDER
    parts = (0, 0, 1, 1, 2, 2, 3, 3)
    for left, right in itertools.combinations(range(8), 2):
        if parts[left] == parts[right]:
            continue
        k2222[left] |= 1 << right
        k2222[right] |= 1 << left
    require(find_model(k2222) is None, "negative K_{2,2,2,2} self-test failed")


def main() -> None:
    self_test()
    signatures = tuple(component_multisets())
    require(len(signatures) == 29, f"expected 29 complement types, found {len(signatures)}")
    require(len(set(signatures)) == 29, "duplicate complement signature")
    require(len(CANDIDATES) == 750, f"unexpected model-candidate count {len(CANDIDATES)}")

    certificate_lines: list[str] = []
    support_orders: dict[int, int] = {}
    for signature in signatures:
        complement = complement_type(signature)
        for missed_root in (None,) + ROOTS:
            adjacency = quotient(complement, missed_root)
            model = find_model(adjacency)
            require(model is not None, f"no model for {signature}, miss={missed_root}")
            check_model(model, adjacency)
            used_order = sum(bag.bit_count() for bag in model)
            support_orders[used_order] = support_orders.get(used_order, 0) + 1
            certificate_lines.append(
                f"{signature}|{missed_root}|{','.join(map(str, model))}|"
                f"{missing_pairs(model, adjacency)}"
            )

    require(len(certificate_lines) == 232, "wrong number of attachment cases")
    digest = hashlib.sha256("\n".join(certificate_lines).encode()).hexdigest()
    expected_digest = "b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306"
    require(digest == expected_digest, f"certificate digest changed: {digest}")

    print(f"complement types: {len(signatures)}")
    print(f"full-or-one-missed attachment cases: {len(certificate_lines)}")
    print(f"model support orders: {dict(sorted(support_orders.items()))}")
    print(f"certificate digest: {digest}")
    print("GREEN: every quotient contains a certified K_7^- minor")


if __name__ == "__main__":
    main()
