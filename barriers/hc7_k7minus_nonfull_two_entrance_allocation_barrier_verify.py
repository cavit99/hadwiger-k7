#!/usr/bin/env python3
"""Verify the one-nonfull two-entrance allocation barrier."""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")

from itertools import combinations


S = tuple(range(7))
X = 7
U = 8
E0, E1 = 9, 10
A, B = 11, 12
ORDER = 13


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def add_edge(graph: list[int], left: int, right: int) -> None:
    graph[left] |= 1 << right
    graph[right] |= 1 << left


def build() -> tuple[int, ...]:
    graph = [0] * ORDER
    boundary_edges = (
        (0, 3),
        (0, 4),
        (0, 6),
        (1, 5),
        (1, 6),
        (2, 5),
        (3, 4),
        (5, 6),
    )
    for edge in boundary_edges:
        add_edge(graph, *edge)

    add_edge(graph, U, X)
    for vertex in S:
        add_edge(graph, U, vertex)
        add_edge(graph, E0, vertex)
        if vertex != 1:
            add_edge(graph, E1, vertex)

    for vertex in (1, 2, 3, 4):
        add_edge(graph, X, vertex)
        add_edge(graph, A, vertex)
        add_edge(graph, B, vertex)

    for edge in ((X, A), (X, B), (E0, E1), (A, B), (A, 0), (B, 5), (B, 6)):
        add_edge(graph, *edge)
    return tuple(graph)


def vertices(mask: int):
    while mask:
        bit = mask & -mask
        mask ^= bit
        yield bit.bit_length() - 1


def connected(graph: tuple[int, ...], mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    while True:
        expanded = reached
        for vertex in vertices(reached):
            expanded |= graph[vertex] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def components(graph: tuple[int, ...], mask: int) -> tuple[int, ...]:
    answer = []
    unseen = mask
    while unseen:
        reached = unseen & -unseen
        while True:
            expanded = reached
            for vertex in vertices(reached):
                expanded |= graph[vertex] & unseen
            if expanded == reached:
                break
            reached = expanded
        answer.append(reached)
        unseen &= ~reached
    return tuple(answer)


def support(graph: tuple[int, ...], mask: int) -> int:
    answer = 0
    for root in S:
        if graph[root] & mask:
            answer |= 1 << root
    return answer


def adjacent_sets(graph: tuple[int, ...], left: int, right: int) -> bool:
    return any(graph[vertex] & right for vertex in vertices(left))


def graph6_boundary(graph: tuple[int, ...]) -> str:
    bits = []
    for right in range(1, 7):
        for left in range(right):
            bits.append((graph[left] >> right) & 1)
    bits.extend([0] * ((-len(bits)) % 6))
    encoded = [chr(63 + 7)]
    for start in range(0, len(bits), 6):
        value = 0
        for bit in bits[start : start + 6]:
            value = (value << 1) | bit
        encoded.append(chr(63 + value))
    return "".join(encoded)


def independent(graph: tuple[int, ...], chosen: tuple[int, ...]) -> bool:
    return all(not (graph[left] & (1 << right)) for left, right in combinations(chosen, 2))


def clique(graph: tuple[int, ...], chosen: tuple[int, ...]) -> bool:
    return all(graph[left] & (1 << right) for left, right in combinations(chosen, 2))


def maximum_disjoint(family: tuple[int, ...]) -> int:
    best = 0
    for size in range(1, len(family) + 1):
        if any(
            all(not (left & right) for left, right in combinations(choice, 2))
            for choice in combinations(family, size)
        ):
            best = size
    return best


def main() -> None:
    graph = build()
    all_vertices = (1 << ORDER) - 1
    boundary_mask = (1 << 7) - 1

    require(graph6_boundary(graph) == "FCdeG", "wrong boundary graph6 code")
    require(graph[U] == boundary_mask | (1 << X), "wrong degree-eight centre")
    require(graph[U].bit_count() == 8, "centre must have degree eight")

    neighbourhood = S + (X,)
    independent_triples = tuple(
        choice for choice in combinations(neighbourhood, 3) if independent(graph, choice)
    )
    independent_fours = tuple(
        choice for choice in combinations(neighbourhood, 4) if independent(graph, choice)
    )
    four_cliques = tuple(
        choice for choice in combinations(neighbourhood, 4) if clique(graph, choice)
    )
    require(independent_triples, "exceptional neighbourhood needs alpha at least three")
    require(not independent_fours, "exceptional neighbourhood must have alpha three")
    require(not four_cliques, "exceptional neighbourhood must be K4-free")

    outside_closed_neighbourhood = all_vertices & ~((1 << U) | graph[U])
    exterior = components(graph, outside_closed_neighbourhood)
    require(
        set(exterior) == {(1 << E0) | (1 << E1), (1 << A) | (1 << B)},
        "wrong exterior components",
    )
    require(support(graph, exterior[0]) == boundary_mask or support(graph, exterior[1]) == boundary_mask, "components must be S-full")
    require(not (graph[X] & ((1 << E0) | (1 << E1))), "E must miss x")
    require(graph[X] & (1 << A) and graph[X] & (1 << B), "x needs two F entrances")
    require((graph[X] & boundary_mask).bit_count() == 4, "x needs four S-neighbours")

    deleted_checks = 0
    for size in range(7):
        for deleted in combinations(range(ORDER), size):
            deleted_checks += 1
            deleted_mask = sum(1 << vertex for vertex in deleted)
            require(connected(graph, all_vertices & ~deleted_mask), "cut smaller than seven")
    require(deleted_checks == 4096, "wrong small-cut census")
    require(
        len(components(graph, all_vertices & ~graph[X])) >= 2,
        "the seven neighbours of x must be a cut",
    )

    e_mask = (1 << E0) | (1 << E1)
    rich_mask = (1 << U) | (1 << X) | (1 << A) | (1 << B)
    connected_e = tuple(
        mask
        for mask in range(1, 1 << ORDER)
        if not (mask & ~e_mask) and connected(graph, mask)
    )
    connected_rich = tuple(
        mask
        for mask in range(1, 1 << ORDER)
        if not (mask & ~rich_mask) and connected(graph, mask)
    )
    e_full = tuple(mask for mask in connected_e if support(graph, mask) == boundary_mask)
    rich_full = tuple(mask for mask in connected_rich if support(graph, mask) == boundary_mask)
    rich_near = tuple(mask for mask in connected_rich if support(graph, mask).bit_count() >= 5)
    require(maximum_disjoint(e_full) == 1, "E packing number must be one")
    require(maximum_disjoint(rich_full) == 2, "rich packing number must be two")

    allocations = tuple(
        (left, right, third)
        for left, right in combinations(rich_full, 2)
        if not (left & right)
        for third in rich_near
        if not (third & (left | right))
    )
    require(not allocations, "unexpected two-full-plus-defect-two allocation")

    five_colouring = {
        0: 3,
        1: 0,
        2: 0,
        3: 0,
        4: 1,
        5: 3,
        6: 1,
        X: 3,
        U: 2,
        E0: 2,
        E1: 4,
        A: 4,
        B: 2,
    }
    require(
        all(five_colouring[left] != five_colouring[right] for left in range(ORDER) for right in range(left + 1, ORDER) if graph[left] & (1 << right)),
        "displayed five-colouring is improper",
    )
    require(clique(graph, (0, 3, 4, E0, E1)), "displayed K5 is absent")

    k7_bags = (
        1 << 0,
        1 << 3,
        1 << 4,
        1 << U,
        (1 << 1) | (1 << E0),
        (1 << 5) | (1 << E1),
        (1 << 2) | (1 << 6) | (1 << X) | (1 << A) | (1 << B),
    )
    require(sum(mask.bit_count() for mask in k7_bags) == ORDER, "K7 bags must partition the host")
    require(all(connected(graph, mask) for mask in k7_bags), "disconnected K7 bag")
    require(
        all(adjacent_sets(graph, left, right) for left, right in combinations(k7_bags, 2)),
        "missing K7 bag contact",
    )

    print("PASS K7-minus one-nonfull two-entrance allocation barrier")
    print("order=13 edges=48 boundary=FCdeG alpha_Nu=3 K4_Nu=no")
    print("cuts_le6=4096 connectivity=7 packing=(1,2)")
    print("x_boundary_contacts=4 x_F_entrances=2 defect2_allocations=0")
    print("chromatic_number=5 explicit_K7_model=yes")
    print("scope=violates K7-minus exclusion and seven-chromatic criticality")


if __name__ == "__main__":
    main()
