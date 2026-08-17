#!/usr/bin/env python3
"""Verify the relative-five all-carrier/rooted-K5-minus barrier.

The checker uses only the Python standard library.  It verifies the local
six-root shore, all ten three--two carrier instances after one root is
punctured, and exhausts every possible allocation of the two internal
vertices to five rooted branch bags.
"""

from __future__ import annotations

from itertools import combinations, product


Vertex = int
Bag = frozenset[Vertex]


ROOTS = frozenset(range(6))
PUNCTURE = 5
FIVE_ROOTS = ROOTS - {PUNCTURE}
U, V = 6, 7
INTERNAL = frozenset({U, V})


def build_graph() -> dict[Vertex, set[Vertex]]:
    vertices = ROOTS | INTERNAL
    adjacency = {vertex: set() for vertex in vertices}
    edges = {(U, V)}
    edges.update((U, root) for root in range(5))
    edges.update((V, root) for root in range(4))
    edges.add((V, PUNCTURE))
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    return adjacency


def connected(adjacency: dict[Vertex, set[Vertex]], bag: Bag) -> bool:
    if not bag:
        return False
    seen: set[Vertex] = set()
    todo = [next(iter(bag))]
    while todo:
        vertex = todo.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        todo.extend((adjacency[vertex] & set(bag)) - seen)
    return seen == set(bag)


def adjacent(
    adjacency: dict[Vertex, set[Vertex]], left: Bag, right: Bag
) -> bool:
    return any(adjacency[vertex] & set(right) for vertex in left)


def external_neighbourhood(
    adjacency: dict[Vertex, set[Vertex]], shore: Bag
) -> set[Vertex]:
    return set().union(*(adjacency[vertex] for vertex in shore)) - set(shore)


def check_internal_six_connectivity(
    adjacency: dict[Vertex, set[Vertex]],
) -> tuple[int, int, int]:
    sizes = []
    for order in range(1, len(INTERNAL) + 1):
        for shore_tuple in combinations(sorted(INTERNAL), order):
            shore = frozenset(shore_tuple)
            size = len(external_neighbourhood(adjacency, shore))
            assert size >= 6
            sizes.append(size)
    return tuple(sizes)  # type: ignore[return-value]


def check_all_three_two_carriers(
    adjacency: dict[Vertex, set[Vertex]],
) -> tuple[int, ...]:
    counts = []
    for pair_tuple in combinations(sorted(FIVE_ROOTS), 2):
        pair = frozenset(pair_tuple)
        triple = FIVE_ROOTS - pair
        feasible_allocations = 0
        for allocation in product(range(3), repeat=2):
            # 0 means unused, 1 means assigned to the pair carrier, and
            # 2 means assigned to the triple carrier.
            pair_bag = pair | {
                vertex
                for vertex, side in zip((U, V), allocation, strict=True)
                if side == 1
            }
            triple_bag = triple | {
                vertex
                for vertex, side in zip((U, V), allocation, strict=True)
                if side == 2
            }
            if (
                pair_bag.isdisjoint(triple_bag)
                and connected(adjacency, frozenset(pair_bag))
                and connected(adjacency, frozenset(triple_bag))
            ):
                feasible_allocations += 1
        assert feasible_allocations > 0

        # Check the simple certificates used in the written proof.
        if PUNCTURE - 1 in pair:  # terminal 4
            displayed_pair = pair | {U}
            displayed_triple = triple | {V}
        else:
            displayed_pair = pair | {V}
            displayed_triple = triple | {U}
        assert connected(adjacency, frozenset(displayed_pair))
        assert connected(adjacency, frozenset(displayed_triple))
        assert displayed_pair.isdisjoint(displayed_triple)
        counts.append(feasible_allocations)
    return tuple(counts)


def has_rooted_k5_minus(adjacency: dict[Vertex, set[Vertex]]) -> bool:
    roots = tuple(sorted(FIVE_ROOTS))
    # Each internal vertex is unused (0) or allocated to one of five bags
    # (1,...,5).  This exhausts all rooted models because the root bags are
    # disjoint and each already contains its prescribed root.
    for allocation in product(range(6), repeat=2):
        bags = [set((root,)) for root in roots]
        for vertex, target in zip((U, V), allocation, strict=True):
            if target:
                bags[target - 1].add(vertex)
        frozen = tuple(frozenset(bag) for bag in bags)
        if not all(connected(adjacency, bag) for bag in frozen):
            continue
        missing = sum(
            not adjacent(adjacency, left, right)
            for left, right in combinations(frozen, 2)
        )
        if missing <= 1:
            return True
    return False


def main() -> None:
    adjacency = build_graph()
    assert set(adjacency) == ROOTS | INTERNAL
    assert not any(adjacency[root] & ROOTS for root in ROOTS)
    assert adjacency[U] == {V, 0, 1, 2, 3, 4}
    assert adjacency[V] == {U, 0, 1, 2, 3, PUNCTURE}

    neighbourhood_sizes = check_internal_six_connectivity(adjacency)
    carrier_counts = check_all_three_two_carriers(adjacency)
    assert not has_rooted_k5_minus(adjacency)

    internal_edges = sum(V in adjacency[U] for _ in (0,))
    boundary_incidence = sum(len(adjacency[vertex] & ROOTS) for vertex in INTERNAL)
    eta = internal_edges + boundary_incidence - 4 * len(INTERNAL)
    assert (internal_edges, boundary_incidence, eta) == (1, 10, 3)

    punctured_incidence = sum(
        len(adjacency[vertex] & FIVE_ROOTS) for vertex in INTERNAL
    )
    punctured_excess = internal_edges + punctured_incidence - 4 * len(INTERNAL)
    assert punctured_excess == 2

    print("GREEN relative-five all-carrier/rooted-K5-minus barrier")
    print(f"internal-six neighbourhood sizes={neighbourhood_sizes}")
    print(f"three-two feasible allocation counts={carrier_counts}")
    print("punctured rooted K5-minus models=0 (36 allocations exhausted)")
    print(f"six-root eta={eta}; punctured five-root excess={punctured_excess}")


if __name__ == "__main__":
    main()
