#!/usr/bin/env python3
"""Search a minimal opposite-shore, two-rooted-model quotient.

This is a hostile finite diagnostic, not a proof about the critical host.
The host has an order-eight boundary, two anticomplete connected boundary-
full shores of order two, and an explicit spanning exact K7-with-two-
adjacent-edges-missing model.  One selected edge enters each shore and is
internal to a universal model bag.  Deleting both selected edges preserves
the exact model, while contracting either selected edge gives an edge-rooted
K6 model.

The search varies only the allocation of the eight boundary contacts within
each two-vertex shore.  It looks for an allocation with no K7-minus-edge
minor.  Such an allocation would refute any proposed exchange based only on
the cut geometry and the two separately rooted models.  Colour-response
data are deliberately not encoded in this first gate.
"""

from __future__ import annotations

import argparse
import random
from functools import lru_cache
from itertools import combinations


NAMES = (
    "t0",
    "t1",
    "p",
    "x",
    "b",
    "c",
    "u3",
    "u4",
    "c0",
    "c1",
    "d0",
    "d1",
)
INDEX = {name: index for index, name in enumerate(NAMES)}
BOUNDARY = tuple(range(8))
C_SHORE = (INDEX["c0"], INDEX["c1"])
D_SHORE = (INDEX["d0"], INDEX["d1"])
E = tuple(sorted((INDEX["c0"], INDEX["t0"])))
F = tuple(sorted((INDEX["d0"], INDEX["t1"])))


def add_edge(rows: list[int], left: int, right: int) -> None:
    rows[left] |= 1 << right
    rows[right] |= 1 << left


def has_edge(rows: tuple[int, ...], left: int, right: int) -> bool:
    return bool(rows[left] & (1 << right))


def connected(rows: tuple[int, ...]) -> bool:
    seen = 1
    frontier = 1
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = rows[vertex] & ~seen
        seen |= new
        frontier |= new
    return seen == (1 << len(rows)) - 1


def contract(rows: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    keep = tuple(vertex for vertex in range(len(rows)) if vertex != right)
    position = {vertex: index for index, vertex in enumerate(keep)}
    answer = [0] * len(keep)
    merged = (rows[left] | rows[right]) & ~((1 << left) | (1 << right))
    for old_left, old_right in combinations(keep, 2):
        present = (
            bool(merged & (1 << old_right))
            if old_left == left
            else bool(merged & (1 << old_left))
            if old_right == left
            else has_edge(rows, old_left, old_right)
        )
        if present:
            add_edge(answer, position[old_left], position[old_right])
    return tuple(answer)


def contract_pairs(
    rows: tuple[int, ...], pairs: tuple[tuple[int, int], ...]
) -> tuple[int, ...]:
    parent = list(range(len(rows)))

    def root(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    for left, right in pairs:
        left_root, right_root = root(left), root(right)
        if left_root != right_root:
            parent[right_root] = left_root
    roots = sorted({root(vertex) for vertex in range(len(rows))})
    position = {old: index for index, old in enumerate(roots)}
    answer = [0] * len(roots)
    for left, right in combinations(range(len(rows)), 2):
        if not has_edge(rows, left, right):
            continue
        new_left, new_right = position[root(left)], position[root(right)]
        if new_left != new_right:
            add_edge(answer, new_left, new_right)
    return tuple(answer)


def k_colourable(rows: tuple[int, ...], colour_count: int) -> bool:
    colours = [-1] * len(rows)

    def extend(coloured: int) -> bool:
        if coloured == len(rows):
            return True
        candidates = [vertex for vertex, colour in enumerate(colours) if colour < 0]
        vertex = max(
            candidates,
            key=lambda item: (
                len(
                    {
                        colours[other]
                        for other in range(len(rows))
                        if colours[other] >= 0 and has_edge(rows, item, other)
                    }
                ),
                rows[item].bit_count(),
            ),
        )
        forbidden = {
            colours[other]
            for other in range(len(rows))
            if colours[other] >= 0 and has_edge(rows, vertex, other)
        }
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            if extend(coloured + 1):
                return True
            colours[vertex] = -1
        return False

    return extend(0)


def chromatic_number(rows: tuple[int, ...]) -> int:
    for colours in range(1, 7):
        if k_colourable(rows, colours):
            return colours
    return 7


def canonical(rows: tuple[int, ...]) -> tuple[int, ...]:
    """Cheap invariant-preserving key; labels are retained intentionally."""

    return rows


def k7_minus_model(rows: tuple[int, ...]) -> tuple[bool, int]:
    """Exact contraction search for K7 minus at most one edge."""

    if not connected(rows):
        raise RuntimeError("the contraction oracle expects a connected host")
    calls = 0

    @lru_cache(maxsize=None)
    def search(graph: tuple[int, ...]) -> bool:
        nonlocal calls
        calls += 1
        order = len(graph)
        if order < 7:
            return False
        if order == 7:
            return sum(row.bit_count() for row in graph) // 2 >= 20
        # Dense contractions first usually expose a positive model quickly.
        edges = [
            (left, right)
            for left, right in combinations(range(order), 2)
            if has_edge(graph, left, right)
        ]
        edges.sort(
            key=lambda pair: (graph[pair[0]] | graph[pair[1]]).bit_count(),
            reverse=True,
        )
        return any(search(contract(graph, left, right)) for left, right in edges)

    return search(canonical(rows)), calls


def base_rows() -> list[int]:
    rows = [0] * len(NAMES)
    # The five boundary bags P={p,x}, B={b}, C={c}, U3={u3}, U4={u4}
    # induce K5 with PB and PC absent.
    for left, right in (
        ("p", "x"),
        ("p", "u3"),
        ("p", "u4"),
        ("b", "c"),
        ("b", "u3"),
        ("b", "u4"),
        ("c", "u3"),
        ("c", "u4"),
        ("u3", "u4"),
    ):
        add_edge(rows, INDEX[left], INDEX[right])
    add_edge(rows, *C_SHORE)
    add_edge(rows, *D_SHORE)
    return rows


def build(c_bits: int, d_bits: int) -> tuple[int, ...]:
    """Allocate one contact per boundary vertex, plus two forced backups.

    Bit zero assigns a boundary contact to the first shore vertex and bit
    one to the second.  At t0 on the C shore and t1 on the D shore both
    contacts are present: one is the selected coordinate and the other
    keeps its model bag connected after the coordinate is deleted.
    """

    rows = base_rows()
    for boundary in BOUNDARY:
        add_edge(rows, C_SHORE[(c_bits >> boundary) & 1], boundary)
        add_edge(rows, D_SHORE[(d_bits >> boundary) & 1], boundary)
    add_edge(rows, INDEX["c0"], INDEX["t0"])
    add_edge(rows, INDEX["c1"], INDEX["t0"])
    add_edge(rows, INDEX["d0"], INDEX["t1"])
    add_edge(rows, INDEX["d1"], INDEX["t1"])
    return tuple(rows)


def remove_edges(rows: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    answer = list(rows)
    for left, right in edges:
        answer[left] &= ~(1 << right)
        answer[right] &= ~(1 << left)
    return tuple(answer)


def model_checks(rows: tuple[int, ...]) -> None:
    x_rows = remove_edges(rows, (E, F))
    bags = (
        frozenset(INDEX[name] for name in ("p", "x")),
        frozenset({INDEX["b"]}),
        frozenset({INDEX["c"]}),
        frozenset({INDEX["u3"]}),
        frozenset({INDEX["u4"]}),
        frozenset((*C_SHORE, INDEX["t0"])),
        frozenset((*D_SHORE, INDEX["t1"])),
    )
    for bag in bags:
        induced = tuple(
            sum(1 << other for other in bag if has_edge(x_rows, vertex, other))
            for vertex in bag
        )
        # The bags have order at most three; a direct reachability check is
        # clearer than depending on their inherited vertex labels.
        reached = {next(iter(bag))}
        while True:
            enlarged = reached | {
                vertex
                for vertex in bag
                if any(has_edge(x_rows, vertex, old) for old in reached)
            }
            if enlarged == reached:
                break
            reached = enlarged
        if reached != set(bag):
            raise RuntimeError(f"disconnected model bag {bag}; local={induced}")
    missing = []
    for left, right in combinations(range(7), 2):
        if not any(has_edge(x_rows, u, v) for u in bags[left] for v in bags[right]):
            missing.append((left, right))
    if missing != [(0, 1), (0, 2)]:
        raise RuntimeError(f"model is not exact K7-two-edge: {missing}")


def boundary_partitions() -> tuple[tuple[int, ...], ...]:
    """Canonical proper equality partitions of the eight-set into <=6 blocks."""

    answer: list[tuple[int, ...]] = []
    labels = [-1] * len(BOUNDARY)

    def extend(position: int, maximum: int) -> None:
        if position == len(BOUNDARY):
            answer.append(tuple(labels))
            return
        for label in range(min(maximum + 1, 5) + 1):
            if label > maximum + 1:
                break
            labels[position] = label
            extend(position + 1, max(maximum, label))

    labels[0] = 0
    extend(1, 0)
    return tuple(answer)


PARTITIONS = boundary_partitions()


def partition_is_proper(rows: tuple[int, ...], partition: tuple[int, ...]) -> bool:
    return all(
        partition[left] != partition[right]
        for left, right in combinations(BOUNDARY, 2)
        if has_edge(rows, left, right)
    )


def extend_partition(
    rows: tuple[int, ...],
    partition: tuple[int, ...],
    signature: tuple[bool, bool],
    required_fan: tuple[int, int, int] | None = None,
) -> tuple[int, ...] | None:
    """Extend a fixed boundary partition to H=G-{e,f} with exact signature."""

    host = remove_edges(rows, (E, F))
    colours = list(partition) + [-1] * 4
    used = max(partition) + 1
    internal = C_SHORE + D_SHORE
    signature_edges = (E, F)

    def coloured_fan_exists(coordinate: tuple[int, int, int]) -> bool:
        open_end, mate, boundary_end = coordinate
        alpha = colours[open_end]
        if colours[boundary_end] != alpha:
            return False
        used_ends = {boundary_end}
        for beta in set(range(6)) - {alpha}:
            direct = next(
                (
                    vertex
                    for vertex in BOUNDARY
                    if vertex not in used_ends
                    and has_edge(rows, open_end, vertex)
                    and colours[vertex] == beta
                ),
                None,
            )
            if direct is not None:
                used_ends.add(direct)
                continue
            if colours[mate] != beta or not has_edge(rows, open_end, mate):
                return False
            indirect = next(
                (
                    vertex
                    for vertex in BOUNDARY
                    if vertex not in used_ends
                    and has_edge(rows, mate, vertex)
                    and colours[vertex] == alpha
                ),
                None,
            )
            if indirect is None:
                return False
            used_ends.add(indirect)
        return True

    def compatible(vertex: int, colour: int) -> bool:
        if any(
            colours[other] == colour
            for other in range(len(colours))
            if colours[other] >= 0 and has_edge(host, vertex, other)
        ):
            return False
        for (left, right), equal in zip(signature_edges, signature, strict=True):
            if vertex not in (left, right):
                continue
            other = right if vertex == left else left
            if colours[other] < 0:
                continue
            if (colour == colours[other]) != equal:
                return False
        return True

    def extend(position: int, next_colour: int) -> bool:
        if position == len(internal):
            return all(
                (colours[left] == colours[right]) == equal
                for (left, right), equal in zip(signature_edges, signature, strict=True)
            ) and (required_fan is None or coloured_fan_exists(required_fan))
        vertex = internal[position]
        for colour in range(min(next_colour + 1, 6)):
            if not compatible(vertex, colour):
                continue
            colours[vertex] = colour
            if extend(position + 1, max(next_colour, colour + 1)):
                return True
            colours[vertex] = -1
        return False

    return tuple(colours) if extend(0, used) else None


def response_screen(rows: tuple[int, ...]) -> dict[str, object]:
    proper_partitions = tuple(
        partition for partition in PARTITIONS if partition_is_proper(rows, partition)
    )
    signatures = {
        "PP": (False, False),
        "EP": (True, False),
        "PE": (False, True),
        "EE": (True, True),
    }
    languages: dict[str, dict[tuple[int, ...], tuple[int, ...]]] = {}
    for name, signature in signatures.items():
        language = {}
        for partition in proper_partitions:
            colouring = extend_partition(rows, partition, signature)
            if colouring is not None:
                language[partition] = colouring
        languages[name] = language

    fan_ep = next(
        (
            colouring
            for partition in proper_partitions
            if (
                colouring := extend_partition(
                    rows,
                    partition,
                    signatures["EP"],
                    (INDEX["c0"], INDEX["c1"], INDEX["t0"]),
                )
            )
            is not None
        ),
        None,
    )
    fan_pe = next(
        (
            colouring
            for partition in proper_partitions
            if (
                colouring := extend_partition(
                    rows,
                    partition,
                    signatures["PE"],
                    (INDEX["d0"], INDEX["d1"], INDEX["t1"]),
                )
            )
            is not None
        ),
        None,
    )
    return {
        "proper_boundary_partitions": len(proper_partitions),
        "language_sizes": {name: len(language) for name, language in languages.items()},
        "EP_PE_common": set(languages["EP"]) & set(languages["PE"]),
        "witnesses": {
            name: next(iter(language.values()), None) for name, language in languages.items()
        },
        "fan_EP": fan_ep,
        "fan_PE": fan_pe,
    }


def strict_subset_neighbourhoods(rows: tuple[int, ...]) -> dict[str, dict[str, int]]:
    answer: dict[str, dict[str, int]] = {}
    for name, shore in (("C", C_SHORE), ("D", D_SHORE)):
        shore_data = {}
        for vertex in shore:
            shore_data[NAMES[vertex]] = rows[vertex].bit_count()
        answer[name] = shore_data
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=731_119)
    parser.add_argument("--require-square-fans", action="store_true")
    parser.add_argument("--require-disjoint-singletons", action="store_true")
    parser.add_argument("--require-exact-contractions", action="store_true")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    assignments = [(rng.randrange(256), rng.randrange(256)) for _ in range(args.samples)]
    assignments[:4] = [(0, 0), (0, 255), (255, 0), (0b10101010, 0b01010101)]
    tested = 0
    states = 0
    for c_bits, d_bits in assignments:
        rows = build(c_bits, d_bits)
        model_checks(rows)
        contraction_chromatic = (
            chromatic_number(contract_pairs(rows, (E,))),
            chromatic_number(contract_pairs(rows, (F,))),
            chromatic_number(contract_pairs(rows, (E, F))),
        )
        if args.require_exact_contractions and contraction_chromatic != (6, 6, 6):
            continue
        responses = response_screen(rows)
        strict = strict_subset_neighbourhoods(rows)
        has_strict = any(
            order == 7 for shore in strict.values() for order in shore.values()
        )
        if args.require_square_fans and (
            responses["fan_EP"] is None
            or responses["fan_PE"] is None
            or has_strict
            or any(size == 0 for size in responses["language_sizes"].values())
        ):
            continue
        if args.require_disjoint_singletons and responses["EP_PE_common"]:
            continue
        has_target, calls = k7_minus_model(rows)
        tested += 1
        states += calls
        if not has_target:
            print("SURVIVOR")
            print(f"c_bits={c_bits:08b} d_bits={d_bits:08b}")
            print(f"vertices={len(rows)} edges={sum(row.bit_count() for row in rows) // 2}")
            print(f"contraction_states={calls}")
            print(f"strict_singleton_neighbourhoods={strict}")
            print(f"proper_boundary_partitions={responses['proper_boundary_partitions']}")
            print(f"language_sizes={responses['language_sizes']}")
            print(f"EP_PE_common={len(responses['EP_PE_common'])}")
            for name, colouring in responses["witnesses"].items():
                print(f"{name}_colouring={colouring}")
            print(f"EP_direct_six_fan_colouring={responses['fan_EP']}")
            print(f"PE_direct_six_fan_colouring={responses['fan_PE']}")
            print(
                "chromatic_numbers="
                f"G:{chromatic_number(rows)} "
                f"G/e:{contraction_chromatic[0]} "
                f"G/f:{contraction_chromatic[1]} "
                f"G/e/f:{contraction_chromatic[2]}"
            )
            return
    print(f"minor_tests={tested} contraction_states={states}")
    print("NO_SURVIVOR_IN_RANDOM_GATE")


if __name__ == "__main__":
    main()
