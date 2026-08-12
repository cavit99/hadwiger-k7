#!/usr/bin/env python3
"""Verify the fixed opposite-shore coordinate-square survivor.

The survivor is a finite abstraction.  It is not seven-connected and its
empty signature is present, so it is not a counterexample to the active
critical-host theorem or to HC7.
"""

from __future__ import annotations

from itertools import combinations

import search_quotient as sq


C_BITS = 0b00000101
D_BITS = 0b00000110


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def bag_connected(rows: tuple[int, ...], bag: frozenset[int]) -> bool:
    reached = {next(iter(bag))}
    while True:
        enlarged = reached | {
            vertex
            for vertex in bag
            if any(sq.has_edge(rows, vertex, old) for old in reached)
        }
        if enlarged == reached:
            return reached == set(bag)
        reached = enlarged


def bags_adjacent(rows: tuple[int, ...], left: frozenset[int], right: frozenset[int]) -> bool:
    return any(sq.has_edge(rows, u, v) for u in left for v in right)


def verify_common_model(rows: tuple[int, ...]) -> None:
    host = sq.remove_edges(rows, (sq.E, sq.F))
    bags = (
        frozenset((*sq.C_SHORE, sq.INDEX["t0"])),
        frozenset((*sq.D_SHORE, sq.INDEX["t1"])),
        frozenset({sq.INDEX["b"]}),
        frozenset({sq.INDEX["c"]}),
        frozenset({sq.INDEX[name] for name in ("u3", "p", "x")}),
        frozenset({sq.INDEX["u4"]}),
    )
    require(set().union(*bags) == set(range(len(rows))), "common K6 model is not spanning")
    require(sum(map(len, bags)) == len(rows), "common K6 bags overlap")
    require(all(bag_connected(host, bag) for bag in bags), "common K6 bag is disconnected")
    require(
        all(
            bags_adjacent(host, bags[left], bags[right])
            for left, right in combinations(range(6), 2)
        ),
        "common K6 bags are not pairwise adjacent",
    )
    require(set(sq.E) <= bags[0], "first coordinate is not co-bagged")
    require(set(sq.F) <= bags[1], "second coordinate is not co-bagged")


def maximum_double_contacts(rows: tuple[int, ...], shore: str) -> int:
    if shore == "C":
        own = frozenset((*sq.C_SHORE, sq.INDEX["t0"]))
        first, second = sq.E
        other = frozenset((*sq.D_SHORE, sq.INDEX["t1"]))
    else:
        own = frozenset((*sq.D_SHORE, sq.INDEX["t1"]))
        first, second = sq.F
        other = frozenset((*sq.C_SHORE, sq.INDEX["t0"]))
    foreign = (
        other,
        frozenset({sq.INDEX["b"]}),
        frozenset({sq.INDEX["c"]}),
        frozenset({sq.INDEX[name] for name in ("u3", "p", "x")}),
        frozenset({sq.INDEX["u4"]}),
    )
    maximum = 0
    movable = tuple(own - {first, second})
    for choices in range(1 << len(movable)):
        left = {first}
        left.update(
            vertex for index, vertex in enumerate(movable) if choices & (1 << index)
        )
        right = set(own) - left
        if not right or second not in right:
            continue
        if not bag_connected(rows, frozenset(left)) or not bag_connected(
            rows, frozenset(right)
        ):
            continue
        count = sum(
            bags_adjacent(rows, frozenset(left), bag)
            and bags_adjacent(rows, frozenset(right), bag)
            for bag in foreign
        )
        maximum = max(maximum, count)
    return maximum


def open_neighbourhood(rows: tuple[int, ...], vertices: frozenset[int]) -> frozenset[int]:
    answer = set()
    for vertex in vertices:
        answer.update(
            other
            for other in range(len(rows))
            if other not in vertices and sq.has_edge(rows, vertex, other)
        )
    return frozenset(answer)


def connected_after_deletion(rows: tuple[int, ...], deleted: frozenset[int]) -> bool:
    remaining = set(range(len(rows))) - set(deleted)
    if len(remaining) <= 1:
        return True
    root = min(remaining)
    reached = {root}
    stack = [root]
    while stack:
        vertex = stack.pop()
        for other in remaining - reached:
            if sq.has_edge(rows, vertex, other):
                reached.add(other)
                stack.append(other)
    return reached == remaining


def vertex_connectivity(rows: tuple[int, ...]) -> int:
    for order in range(len(rows) - 1):
        for deleted in combinations(range(len(rows)), order):
            if not connected_after_deletion(rows, frozenset(deleted)):
                return order
    return len(rows) - 1


def coloured_fan_paths(
    rows: tuple[int, ...], colouring: tuple[int, ...], shore: str
) -> tuple[tuple[int, ...], ...]:
    if shore == "C":
        open_end, mate, boundary_end = (
            sq.INDEX["c0"],
            sq.INDEX["c1"],
            sq.INDEX["t0"],
        )
    else:
        open_end, mate, boundary_end = (
            sq.INDEX["d0"],
            sq.INDEX["d1"],
            sq.INDEX["t1"],
        )
    alpha = colouring[open_end]
    require(colouring[boundary_end] == alpha, "coordinate ends have different colours")
    paths: list[tuple[int, ...]] = [(open_end, boundary_end)]
    used_ends = {boundary_end}
    for beta in sorted(set(range(6)) - {alpha}):
        direct = next(
            (
                vertex
                for vertex in sq.BOUNDARY
                if vertex not in used_ends
                and sq.has_edge(rows, open_end, vertex)
                and colouring[vertex] == beta
            ),
            None,
        )
        if direct is not None:
            paths.append((open_end, direct))
            used_ends.add(direct)
            continue
        require(colouring[mate] == beta, f"missing first edge for colour {beta}")
        indirect = next(
            (
                vertex
                for vertex in sq.BOUNDARY
                if vertex not in used_ends
                and sq.has_edge(rows, mate, vertex)
                and colouring[vertex] == alpha
            ),
            None,
        )
        require(indirect is not None, f"missing indirect boundary end for colour {beta}")
        paths.append((open_end, mate, indirect))
        used_ends.add(indirect)
    require(len(paths) == 6 and len(used_ends) == 6, "fan does not have six distinct ends")
    internal = [set(path[1:-1]) for path in paths]
    require(
        all(not (internal[left] & internal[right]) for left, right in combinations(range(6), 2)),
        "fan paths have intersecting interiors",
    )
    return tuple(paths)


def main() -> None:
    rows = sq.build(C_BITS, D_BITS)
    sq.model_checks(rows)
    verify_common_model(rows)
    double_contacts = {
        "C": maximum_double_contacts(rows, "C"),
        "D": maximum_double_contacts(rows, "D"),
    }
    require(double_contacts == {"C": 2, "D": 2}, "unexpected split contacts")

    host_without_boundary = set(range(len(rows))) - set(sq.BOUNDARY)
    require(host_without_boundary == set(sq.C_SHORE + sq.D_SHORE), "wrong open shores")
    require(sq.has_edge(rows, *sq.C_SHORE), "C shore is disconnected")
    require(sq.has_edge(rows, *sq.D_SHORE), "D shore is disconnected")
    require(
        not any(sq.has_edge(rows, left, right) for left in sq.C_SHORE for right in sq.D_SHORE),
        "open shores are not anticomplete",
    )
    require(
        open_neighbourhood(rows, frozenset(sq.C_SHORE)) == frozenset(sq.BOUNDARY),
        "C is not boundary-full",
    )
    require(
        open_neighbourhood(rows, frozenset(sq.D_SHORE)) == frozenset(sq.BOUNDARY),
        "D is not boundary-full",
    )

    singleton_orders = sq.strict_subset_neighbourhoods(rows)
    require(
        singleton_orders == {"C": {"c0": 8, "c1": 3}, "D": {"d0": 8, "d1": 3}},
        "unexpected proper-subset neighbourhood orders",
    )
    require(
        all(order != 7 for shore in singleton_orders.values() for order in shore.values()),
        "a strict order-seven response subset survives",
    )

    responses = sq.response_screen(rows)
    require(
        responses["proper_boundary_partitions"] == 408,
        "unexpected number of proper boundary partitions",
    )
    require(
        responses["language_sizes"] == {"PP": 361, "EP": 56, "PE": 56, "EE": 14},
        "unexpected signature-language sizes",
    )
    require(not responses["EP_PE_common"], "singleton response languages intersect")
    require(responses["fan_EP"] is not None, "EP colouring has no prescribed six-fan")
    require(responses["fan_PE"] is not None, "PE colouring has no prescribed six-fan")
    c_paths = coloured_fan_paths(rows, responses["fan_EP"], "C")
    d_paths = coloured_fan_paths(rows, responses["fan_PE"], "D")

    chromatic = {
        "G": sq.chromatic_number(rows),
        "G/e": sq.chromatic_number(sq.contract_pairs(rows, (sq.E,))),
        "G/f": sq.chromatic_number(sq.contract_pairs(rows, (sq.F,))),
        "G/e/f": sq.chromatic_number(sq.contract_pairs(rows, (sq.E, sq.F))),
    }
    require(chromatic == {"G": 5, "G/e": 6, "G/f": 6, "G/e/f": 6}, "wrong chromatic data")

    has_target, states = sq.k7_minus_model(rows)
    require(not has_target, "survivor contains K7 minus an edge")
    connectivity = vertex_connectivity(rows)
    require(connectivity == 3, "unexpected vertex connectivity")

    print("GREEN opposite-shore coordinate-square finite survivor")
    print(f"contact_bits C={C_BITS:08b} D={D_BITS:08b}")
    print(f"vertices={len(rows)} edges={sum(row.bit_count() for row in rows) // 2}")
    print("boundary_order=8 full_components=2,2 strict_order7_subset=no")
    print("common_spanning_K6=yes both_coordinate_pairs_cobagged=yes")
    print(f"maximum_foreign_bags_meeting_both_split_sides={double_contacts}")
    print(f"signature_language_sizes={responses['language_sizes']}")
    print("EP_PE_common_boundary_partition=no")
    print(f"C_coloured_six_fan={c_paths}")
    print(f"D_coloured_six_fan={d_paths}")
    print(f"chromatic_numbers={chromatic}")
    print(f"K7_minus_minor=no contraction_states={states}")
    print(f"vertex_connectivity={connectivity} empty_signature=present")


if __name__ == "__main__":
    main()
