#!/usr/bin/env python3
"""Verify two scoped barriers to boundary-only shore allocation."""

from __future__ import annotations

import hashlib
import itertools
from functools import lru_cache


ORDER = 8
BALANCED_WITNESSES = {
    "GCOcaO": "00c211b",
    "GCOceO": "00c211b",
    "GCOcbO": "00c211b",
    "GCOcfO": "00c211b",
    "GCOcbW": "00c211b",
    "GCOcfW": "00c211b",
    "GCOe`W": "00c211b",
    "GCOebW": "00c211b",
    "GCOebK": "00c211b",
    "GCOe`[": "00c211b",
    "GCQbU_": "00c0129",
    "GCQR@O": "01401a9",
    "GCQREO": "01404a9",
    "GCQRDO": "01401a9",
    "GCQQV?": "0140129",
}
EXPECTED_WITNESS_DIGEST = (
    "325a008189de182c099d60990d72c94f02fe78709e4858bc5aa48ec8eba59367"
)


def decode_graph6(code: str) -> tuple[int, ...]:
    assert code and ord(code[0]) - 63 == ORDER
    bits: list[int] = []
    for character in code[1:]:
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
    return all(
        not adjacent(graph, left, right)
        for left, right in itertools.combinations(vertices, 2)
    )


def pair_masks(graph: tuple[int, ...]) -> tuple[int, int]:
    edge_mask = 0
    all_mask = 0
    for index, (left, right) in enumerate(itertools.combinations(range(ORDER), 2)):
        bit = 1 << index
        all_mask |= bit
        if adjacent(graph, left, right):
            edge_mask |= bit
    return edge_mask, all_mask


def reserve_nonedge_mask(
    graph: tuple[int, ...], independent_triple: tuple[int, ...]
) -> int:
    reserve = set(range(ORDER)) - set(independent_triple)
    answer = 0
    for index, (left, right) in enumerate(itertools.combinations(range(ORDER), 2)):
        if left in reserve and right in reserve and not adjacent(graph, left, right):
            answer |= 1 << index
    return answer


def verify_balanced_witnesses() -> None:
    for code, hexadecimal in BALANCED_WITNESSES.items():
        graph = decode_graph6(code)
        edge_mask, all_mask = pair_masks(graph)
        nonedge_mask = all_mask ^ edge_mask
        first_shore = int(hexadecimal, 16)
        assert first_shore & ~nonedge_mask == 0
        for independent_triple in itertools.combinations(range(ORDER), 3):
            if not independent(graph, independent_triple):
                continue
            demands = reserve_nonedge_mask(graph, independent_triple)
            first_count = (demands & first_shore).bit_count()
            second_count = (demands & ~first_shore).bit_count()
            assert first_count >= 2
            assert second_count >= 2

    lines = "\n".join(
        f"{code} {BALANCED_WITNESSES[code]}" for code in sorted(BALANCED_WITNESSES)
    ) + "\n"
    assert hashlib.sha256(lines.encode()).hexdigest() == EXPECTED_WITNESS_DIGEST


def mechanism_graph() -> tuple[int, ...]:
    boundary = decode_graph6("GCOcaO")
    graph = list(boundary) + [0, 0, 0]
    for apex in range(ORDER, ORDER + 3):
        for vertex in range(ORDER):
            graph[apex] |= 1 << vertex
            graph[vertex] |= 1 << apex
    return tuple(graph)


def connected_mask(graph: tuple[int, ...], mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= graph[bit.bit_length() - 1] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def connected_after_deleting(graph: tuple[int, ...], deleted: int) -> bool:
    keep = ((1 << len(graph)) - 1) & ~deleted
    return connected_mask(graph, keep)


def spanning_k7minus_model(graph: tuple[int, ...]) -> tuple[int, ...] | None:
    """Exact restricted-growth search for seven spanning connected bags."""
    order = len(graph)
    target = 7
    blocks: list[list[int]] = []

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        return connected_mask(graph, mask)

    def accepted(masks: list[int]) -> bool:
        neighbourhoods = []
        for mask in masks:
            neighbours = 0
            todo = mask
            while todo:
                bit = todo & -todo
                todo ^= bit
                neighbours |= graph[bit.bit_length() - 1]
            neighbourhoods.append(neighbours)
        contacts = sum(
            bool(neighbourhoods[left] & masks[right])
            for left, right in itertools.combinations(range(target), 2)
        )
        return contacts >= 20

    def search(position: int) -> tuple[int, ...] | None:
        if position == order:
            if len(blocks) != target:
                return None
            masks = [sum(1 << vertex for vertex in block) for block in blocks]
            if all(connected(mask) for mask in masks) and accepted(masks):
                return tuple(masks)
            return None
        if len(blocks) + order - position < target:
            return None
        for block in blocks:
            block.append(position)
            witness = search(position + 1)
            block.pop()
            if witness is not None:
                return witness
        if len(blocks) < target:
            blocks.append([position])
            witness = search(position + 1)
            blocks.pop()
            if witness is not None:
                return witness
        return None

    return search(0)


def rooted_near_model_exists(
    boundary: tuple[int, ...], independent_triple: tuple[int, ...]
) -> bool:
    roots = tuple(vertex for vertex in range(ORDER) if vertex not in independent_triple)
    # A one-shore quotient has the five roots and one universal nonroot.
    for owner in (-1, *range(5)):
        bags = [{root} for root in roots]
        if owner >= 0:
            bags[owner].add(ORDER)
        contacts = 0
        for left, right in itertools.combinations(range(5), 2):
            touch = any(
                x == ORDER or y == ORDER or adjacent(boundary, x, y)
                for x in bags[left]
                for y in bags[right]
            )
            contacts += touch
        if contacts >= 9:
            return True
    return False


def k_colourable(graph: tuple[int, ...], colour_count: int) -> bool:
    """Exact backtracking check, used only on the 8- and 11-vertex witnesses."""
    colours = [-1] * len(graph)

    def search(coloured: int) -> bool:
        if coloured == len(graph):
            return True
        uncoloured = [vertex for vertex, colour in enumerate(colours) if colour < 0]
        vertex = max(
            uncoloured,
            key=lambda item: (
                len({colours[nbr] for nbr in range(len(graph)) if adjacent(graph, item, nbr) and colours[nbr] >= 0}),
                graph[item].bit_count(),
            ),
        )
        forbidden = {
            colours[nbr]
            for nbr in range(len(graph))
            if adjacent(graph, vertex, nbr) and colours[nbr] >= 0
        }
        for colour in range(colour_count):
            if colour in forbidden:
                continue
            colours[vertex] = colour
            if search(coloured + 1):
                return True
            colours[vertex] = -1
        return False

    return search(0)


def verify_mechanism() -> int:
    boundary = decode_graph6("GCOcaO")
    assert sorted(row.bit_count() for row in boundary) == [
        1, 1, 2, 2, 2, 2, 2, 2
    ]
    assert sum(
        all(
            adjacent(boundary, left, right)
            for left, right in itertools.combinations(choice, 2)
        )
        for choice in itertools.combinations(range(ORDER), 3)
    ) == 2
    assert any(independent(boundary, choice) for choice in itertools.combinations(range(ORDER), 3))
    assert not any(independent(boundary, choice) for choice in itertools.combinations(range(ORDER), 4))
    assert not any(
        all(adjacent(boundary, left, right) for left, right in itertools.combinations(choice, 2))
        for choice in itertools.combinations(range(ORDER), 4)
    )

    graph = mechanism_graph()
    assert all(
        connected_after_deleting(graph, sum(1 << vertex for vertex in deleted))
        for size in range(3)
        for deleted in itertools.combinations(range(len(graph)), size)
    )
    apex_mask = sum(1 << vertex for vertex in range(ORDER, ORDER + 3))
    assert not connected_after_deleting(graph, apex_mask)
    assert k_colourable(graph, 4)
    assert not k_colourable(graph, 3)
    assert spanning_k7minus_model(graph) is None

    triples = 0
    for independent_triple in itertools.combinations(range(ORDER), 3):
        if not independent(boundary, independent_triple):
            continue
        triples += 1
        assert not rooted_near_model_exists(boundary, independent_triple)
    assert triples == 18
    return triples


def main() -> None:
    verify_balanced_witnesses()
    triples = verify_mechanism()
    print("balanced global shore labels=15/15 every rotation keeps 2 demands per shore")
    print(f"balanced-witness sha256={EXPECTED_WITNESS_DIGEST}")
    print("mechanism graph vertices=11 connectivity=3 chromatic_number=4")
    print(f"mechanism independent triples={triples} shore-rooted K5-minus=0")
    print("mechanism K7-minus minor=no")
    print("PASS K7-minus shore-allocation barriers")


if __name__ == "__main__":
    main()
