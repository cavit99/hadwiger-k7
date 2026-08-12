#!/usr/bin/env python3
"""Verify the protected-centre order-ten kernel composition.

Terminals 0,...,6 are the seven vertices of Q and terminal 7 is one other
exceptional centre.  The exact order-ten irreducible kernel has a terminal
C8, with the two nonterminals adjacent to complementary four-sets occurring
cyclically as AABBAABB.  For every labelled normal form, this verifier tries
all sixteen legal nonterminal-owner pairs and every legal absorption of the
terminal-7 bag into a neighbouring Q-rooted bag.  It then tests the resulting
seven-bag quotient, together with the literal Q edges, for K5-minus.

The script is self-contained and uses only the Python standard library.
"""

from __future__ import annotations

from functools import lru_cache
import hashlib
import itertools


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


TERMINALS = tuple(range(8))
PAIRS8 = tuple(itertools.combinations(TERMINALS, 2))
INDEX8 = {edge: index for index, edge in enumerate(PAIRS8)}
PAIRS7 = tuple(itertools.combinations(range(7), 2))

LIVE_Q = ("FCQ`_", "FCQb_", "FCp`_")
EXPECTED_TEMPLATE_DIGEST = (
    "78217d8621685a5839aa55172a51e3470297e6f989516c0455a4884471923418"
)


def decode_graph6(code: str) -> tuple[int, ...]:
    order = ord(code[0]) - 63
    bits: list[int] = []
    for character in code[1:]:
        value = ord(character) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    graph = [0] * order
    position = 0
    for right in range(1, order):
        for left in range(right):
            if bits[position]:
                graph[left] |= 1 << right
                graph[right] |= 1 << left
            position += 1
    return tuple(graph)


def adjacent(graph: tuple[int, ...], left: int, right: int) -> bool:
    return bool(graph[left] & (1 << right))


def edge_count(graph: tuple[int, ...]) -> int:
    return sum(row.bit_count() for row in graph) // 2


def delete_vertex(graph: tuple[int, ...], deleted: int) -> tuple[int, ...]:
    keep = [vertex for vertex in range(len(graph)) if vertex != deleted]
    answer = [0] * len(keep)
    for new_left, old_left in enumerate(keep):
        for new_right in range(new_left + 1, len(keep)):
            old_right = keep[new_right]
            if adjacent(graph, old_left, old_right):
                answer[new_left] |= 1 << new_right
                answer[new_right] |= 1 << new_left
    return tuple(answer)


def contract_edge(
    graph: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    assert adjacent(graph, left, right)
    keep = [vertex for vertex in range(len(graph)) if vertex != right]
    answer = [0] * len(keep)
    for new_left, old_left in enumerate(keep):
        for new_right in range(new_left + 1, len(keep)):
            old_right = keep[new_right]
            edge = adjacent(graph, old_left, old_right)
            if old_left == left:
                edge |= adjacent(graph, right, old_right)
            if old_right == left:
                edge |= adjacent(graph, old_left, right)
            if edge:
                answer[new_left] |= 1 << new_right
                answer[new_right] |= 1 << new_left
    return tuple(answer)


@lru_cache(maxsize=None)
def has_k5_minus_minor(graph: tuple[int, ...]) -> bool:
    """Exact deletion/contraction test for a K5-minus minor."""

    if len(graph) < 5:
        return False
    if len(graph) == 5:
        return edge_count(graph) >= 9
    if any(
        has_k5_minus_minor(delete_vertex(graph, vertex))
        for vertex in range(len(graph))
    ):
        return True
    return any(
        adjacent(graph, left, right)
        and has_k5_minus_minor(contract_edge(graph, left, right))
        for left, right in itertools.combinations(range(len(graph)), 2)
    )


def labelled_cycles() -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return every undirected labelled C8 with one cyclic order."""

    answer: dict[int, tuple[int, ...]] = {}
    for tail in itertools.permutations(range(1, 8)):
        cycle = (0, *tail)
        if cycle[1] > cycle[-1]:
            continue
        mask = 0
        for index in range(8):
            edge = tuple(sorted((cycle[index], cycle[(index + 1) % 8])))
            mask |= 1 << INDEX8[edge]
        answer[mask] = cycle
    assert len(answer) == 2_520
    return tuple(sorted(answer.items()))


def exact_templates() -> tuple[int, ...]:
    """Encode (terminal C8, first nonterminal neighbourhood)."""

    templates = set()
    for cycle_mask, cycle in labelled_cycles():
        for shift in range(4):
            first = sum(
                1 << cycle[index]
                for index in range(8)
                if ((index - shift) % 4) in (0, 1)
            )
            templates.add((cycle_mask << 8) | first)
    result = tuple(sorted(templates))
    assert len(result) == 10_080
    digest = hashlib.sha256(
        b"".join(template.to_bytes(8, "big") for template in result)
    ).hexdigest()
    assert digest == EXPECTED_TEMPLATE_DIGEST
    return result


def add_edge(mask: int, left: int, right: int) -> int:
    if left == right:
        return mask
    return mask | (1 << INDEX8[tuple(sorted((left, right)))])


def owner_quotient(template: int, owner_first: int, owner_second: int) -> int:
    terminal_mask = template >> 8
    first = template & 0xFF
    second = 0xFF ^ first
    assert first >> owner_first & 1
    assert second >> owner_second & 1
    answer = terminal_mask
    for owner, neighbours in ((owner_first, first), (owner_second, second)):
        for other in TERMINALS:
            if other != owner and neighbours >> other & 1:
                answer = add_edge(answer, owner, other)
    return answer


def centre_neighbours(mask: int) -> tuple[int, ...]:
    return tuple(
        vertex
        for vertex in range(7)
        if mask >> INDEX8[(vertex, 7)] & 1
    )


def absorb_centre(mask: int, owner: int) -> tuple[int, ...]:
    neighbours = set(centre_neighbours(mask))
    assert owner in neighbours
    graph = [0] * 7
    for left, right in PAIRS7:
        present = bool(mask >> INDEX8[(left, right)] & 1)
        if owner == left and right in neighbours:
            present = True
        if owner == right and left in neighbours:
            present = True
        if present:
            graph[left] |= 1 << right
            graph[right] |= 1 << left
    return tuple(graph)


def union_graph(
    first: tuple[int, ...], second: tuple[int, ...]
) -> tuple[int, ...]:
    return tuple(left | right for left, right in zip(first, second, strict=True))


def first_witness(
    graph_q: tuple[int, ...], template: int
) -> tuple[int, int, int] | None:
    first = template & 0xFF
    second = 0xFF ^ first
    for owner_first in TERMINALS:
        if not (first >> owner_first & 1):
            continue
        for owner_second in TERMINALS:
            if not (second >> owner_second & 1):
                continue
            quotient = owner_quotient(template, owner_first, owner_second)
            for centre_owner in centre_neighbours(quotient):
                graph = union_graph(graph_q, absorb_centre(quotient, centre_owner))
                if has_k5_minus_minor(graph):
                    return owner_first, owner_second, centre_owner
    return None


def main() -> None:
    templates = exact_templates()
    witness_digest = hashlib.sha256()
    failures: list[tuple[str, int]] = []
    for code in LIVE_Q:
        graph_q = decode_graph6(code)
        assert len(graph_q) == 7
        code_failures = 0
        for template in templates:
            witness = first_witness(graph_q, template)
            if witness is None:
                failures.append((code, template))
                code_failures += 1
                continue
            witness_digest.update(code.encode("ascii"))
            witness_digest.update(template.to_bytes(8, "big"))
            witness_digest.update(bytes(witness))
        print(code, f"templates={len(templates)}", f"failures={code_failures}")

    print(
        "protected-centre order-ten composition",
        f"templates={len(templates)}",
        f"q_types={len(LIVE_Q)}",
        f"failures={len(failures)}",
    )
    print("witness_digest", witness_digest.hexdigest())
    assert not failures


if __name__ == "__main__":
    main()
