#!/usr/bin/env python3
"""Exact screen for the three-mark private-root quotient (standard library)."""

from itertools import combinations, product


ROOTS = range(4)
V, W, A1, A2, A3 = range(4, 9)


def add_edge(adj: list[int], x: int, y: int) -> None:
    adj[x] |= 1 << y
    adj[y] |= 1 << x


def connected(adj: list[int], bag: int) -> bool:
    seen = bag & -bag
    frontier = seen
    while frontier:
        xbit = frontier & -frontier
        frontier ^= xbit
        x = xbit.bit_length() - 1
        new = adj[x] & bag & ~seen
        seen |= new
        frontier |= new
    return seen == bag


def candidate_partitions() -> list[tuple[int, ...]]:
    vertices = tuple(range(9))
    out: list[tuple[int, ...]] = []

    # Seven used vertices: seven singleton bags.
    for used in combinations(vertices, 7):
        out.append(tuple(1 << x for x in used))

    # Eight used vertices: one pair and six singleton bags.
    for omitted in vertices:
        used = tuple(x for x in vertices if x != omitted)
        for pair in combinations(used, 2):
            pair_set = set(pair)
            out.append(((1 << pair[0]) | (1 << pair[1]),) + tuple(
                1 << x for x in used if x not in pair_set
            ))

    # Nine used vertices: one triple, or two pairs, and remaining singletons.
    for triple in combinations(vertices, 3):
        triple_set = set(triple)
        out.append((sum(1 << x for x in triple),) + tuple(
            1 << x for x in vertices if x not in triple_set
        ))

    for four in combinations(vertices, 4):
        a, b, c, d = four
        for p, q in (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))):
            paired = set(four)
            out.append(((1 << p[0]) | (1 << p[1]),
                        (1 << q[0]) | (1 << q[1])) + tuple(
                1 << x for x in vertices if x not in paired
            ))
    return out


PARTITIONS = candidate_partitions()


def k7minus_model(adj: list[int]) -> tuple[int, ...] | None:
    for bags in PARTITIONS:
        if not all(connected(adj, bag) for bag in bags):
            continue
        missing = 0
        for i, left in enumerate(bags):
            neighbours = 0
            scan = left
            while scan:
                bit = scan & -scan
                scan ^= bit
                neighbours |= adj[bit.bit_length() - 1]
            for right in bags[i + 1:]:
                if not neighbours & right:
                    missing += 1
                    if missing > 1:
                        break
            if missing > 1:
                break
        if missing <= 1:
            return bags
    return None


def build(root_masks: tuple[int, ...]) -> list[int]:
    adj = [0] * 9
    for i, j in combinations(ROOTS, 2):
        if (i, j) != (0, 1):
            add_edge(adj, i, j)
    for root in ROOTS:
        add_edge(adj, V, root)
        add_edge(adj, W, root)
    for atom in (A1, A2, A3):
        add_edge(adj, V, atom)
        add_edge(adj, W, atom)
    add_edge(adj, A1, A2)
    add_edge(adj, A2, A3)
    for root, mask in enumerate(root_masks):
        for offset, atom in enumerate((A1, A2, A3)):
            if mask & (1 << offset):
                add_edge(adj, root, atom)
    return adj


def fmt_bags(bags: tuple[int, ...]) -> list[list[int]]:
    return [[x for x in range(9) if bag & (1 << x)] for bag in bags]


def main() -> None:
    valid = 0
    survivors: list[tuple[int, ...]] = []
    first_model = None
    for masks in product(range(1, 8), repeat=4):
        # The two nonadjacent singleton roots have the same four neighbours
        # in the lifted boundary, hence identical piece-incidence masks.
        if masks[0] != masks[1]:
            continue
        # Neither leaf piece nor either leaf-plus-middle piece is root-full.
        if all(mask & 1 for mask in masks):
            continue
        if all(mask & 4 for mask in masks):
            continue
        if not any(mask == 4 for mask in masks):
            continue
        if not any(mask == 1 for mask in masks):
            continue
        valid += 1
        model = k7minus_model(build(masks))
        if model is None:
            survivors.append(masks)
        elif first_model is None:
            first_model = (masks, fmt_bags(model))

    print(f"partitions={len(PARTITIONS)}")
    print(f"valid_incidence_patterns={valid}")
    print(f"target_free_patterns={len(survivors)}")
    if first_model:
        print(f"first_model={first_model}")
    if survivors:
        print("survivors=")
        for row in survivors[:50]:
            print(row)


if __name__ == "__main__":
    main()
