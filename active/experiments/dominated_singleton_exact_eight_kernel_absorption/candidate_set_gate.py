#!/usr/bin/env python3
"""Test whether the exceptional five-bag sets are locally selectable.

The two `C5`-based bad rectangles have one side inducing `C5` and the
other inducing `P3 + K2` or `P5`.  This diagnostic fixes an independent
triple `I`, fixes one of those graphs on the other five vertices `R`, and
enumerates every set of edges between `I` and `R`.

It retains exactly the local exceptional-neighbourhood conditions used by
the matching construction: independence number three, no `K4` subgraph,
and no `K6` minus one edge minor.  The last condition follows in the host
from target exclusion after adjoining the degree-eight centre.
"""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


HERE = Path(__file__).resolve().parent
BASE_PATH = (
    HERE.parent
    / "dominated_singleton_low_degree_completion"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("dominated_base", BASE_PATH)
assert SPEC is not None and SPEC.loader is not None
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


I = (0, 1, 2)
R = (3, 4, 5, 6, 7)
CROSS_EDGES = tuple(itertools.product(I, R))
PATTERNS = {
    "C5": ((0, 1), (1, 2), (2, 3), (3, 4), (4, 0)),
    "P3+K2": ((0, 1), (1, 2), (3, 4)),
    "P5": ((0, 1), (1, 2), (2, 3), (3, 4)),
}
EXPECTED = {
    "C5": (12_363, 315),
    "P3+K2": (8_904, 0),
    "P5": (10_296, 0),
}
WITNESSES = {
    "C5": (216, 184, 120, 151, 47, 86, 165, 75),
    "P3+K2": (248, 248, 232, 23, 43, 23, 135, 71),
    "P5": (232, 216, 184, 23, 46, 85, 163, 71),
}


def build(pattern: tuple[tuple[int, int], ...], mask: int) -> tuple[int, ...]:
    adjacency = [0] * 8
    for left, right in pattern:
        left += 3
        right += 3
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    for index, (left, right) in enumerate(CROSS_EDGES):
        if mask >> index & 1:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    return tuple(adjacency)


def independent_sets_of_order_three(
    graph: tuple[int, ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        vertices
        for vertices in itertools.combinations(range(8), 3)
        if all(
            not base.adjacent(graph, left, right)
            for left, right in itertools.combinations(vertices, 2)
        )
    )


def locally_admissible(graph: tuple[int, ...]) -> bool:
    if any(
        all(
            not base.adjacent(graph, left, right)
            for left, right in itertools.combinations(vertices, 2)
        )
        for vertices in itertools.combinations(range(8), 4)
    ):
        return False
    if any(
        all(
            base.adjacent(graph, left, right)
            for left, right in itertools.combinations(vertices, 2)
        )
        for vertices in itertools.combinations(range(8), 4)
    ):
        return False
    return not base.has_dense_minor(graph, 6, 14)


def connected(graph: tuple[int, ...]) -> bool:
    seen = {0}
    pending = [0]
    while pending:
        vertex = pending.pop()
        for neighbour in range(8):
            if base.adjacent(graph, vertex, neighbour) and neighbour not in seen:
                seen.add(neighbour)
                pending.append(neighbour)
    return len(seen) == 8


def main() -> None:
    for name, pattern in PATTERNS.items():
        selectable = 0
        exact_supported_set = 0
        for mask in range(1 << len(CROSS_EDGES)):
            graph = build(pattern, mask)
            if not locally_admissible(graph):
                continue
            triples = independent_sets_of_order_three(graph)
            assert I in triples
            selectable += 1
            if triples == (I,):
                exact_supported_set += 1

        assert (selectable, exact_supported_set) == EXPECTED[name]
        witness = WITNESSES[name]
        assert locally_admissible(witness)
        assert connected(witness)
        assert min(row.bit_count() for row in witness) >= 4
        if name == "C5":
            assert independent_sets_of_order_three(witness) == (I,)

        print(
            name,
            f"selectable_R={selectable}",
            f"R_equals_N_minus_K={exact_supported_set}",
            f"witness={witness}",
        )

    print("GREEN: exceptional matching-candidate local gate verified")


if __name__ == "__main__":
    main()
