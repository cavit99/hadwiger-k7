#!/usr/bin/env python3
"""Exact finite check for the three-support literal-bond quotient.

This script corroborates the computation-free case table in the adjacent
written theorem.  It does not prove an unbounded graph-theoretic statement.

After the seven boundary-rooted paths and the two bond shores are
contracted, the relevant minor has ten vertices: eight vertices of a
literal K_{4,4}, together with adjacent helper vertices A and Z.  The
boundary terminals are a,b,j1,j2,j3,k,l; f is the unused core vertex.
The helpers A and Z both see j1,j2,j3, A also sees a,b, and each of k,l
is assigned to at least one helper.  It is enough to retain one such owner.

For every allowed 3+4 colouring of the seven boundary terminals and every
owner assignment for k,l, the verifier computes the exact maximum number
of contacts in a seven-branch-set minor model.  The recursion is exhaustive:
unused vertices may be deleted, while an edge inside a connected branch set
may be contracted.  Conversely every operation made by the recursion
preserves connected branch sets.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product


VERTICES = ("a", "b", "j1", "j2", "j3", "k", "l", "f", "A", "Z")
INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
BOUNDARY = VERTICES[:7]
CORE = VERTICES[:8]
HELPERS = ("A", "Z")

EXPECTED_CASES = 160
EXPECTED_DISTRIBUTION = {20: 136, 21: 24}
# Filled from the canonical certificate stream produced below.
EXPECTED_CERTIFICATE_SHA256 = (
    "a21f18a19ad4618c1cf4569f05cbd2b25201f924de140a5f78eb04aa9a3c4b17"
)


def bit(vertex: str) -> int:
    return 1 << INDEX[vertex]


def add_edge(adjacency: list[int], left: str, right: str) -> None:
    adjacency[INDEX[left]] |= bit(right)
    adjacency[INDEX[right]] |= bit(left)


def quotient_graph(colours: tuple[int, ...], owners: tuple[str, str]) -> list[int]:
    """Build the minimal ten-vertex quotient for one finite case."""

    colour = dict(zip(BOUNDARY, colours, strict=True))
    zero_boundary = colours.count(0)
    colour["f"] = 0 if zero_boundary == 3 else 1

    adjacency = [0] * len(VERTICES)
    for left, right in combinations(CORE, 2):
        if colour[left] != colour[right]:
            add_edge(adjacency, left, right)

    add_edge(adjacency, "A", "Z")
    for terminal in ("a", "b", "j1", "j2", "j3"):
        add_edge(adjacency, "A", terminal)
    for terminal in ("j1", "j2", "j3"):
        add_edge(adjacency, "Z", terminal)
    add_edge(adjacency, owners[0], "k")
    add_edge(adjacency, owners[1], "l")
    return adjacency


def touches(left: int, right: int, adjacency: list[int]) -> bool:
    scan = left
    while scan:
        least_bit = scan & -scan
        vertex = least_bit.bit_length() - 1
        if adjacency[vertex] & right:
            return True
        scan ^= least_bit
    return False


def connected(vertices: int, adjacency: list[int]) -> bool:
    if not vertices:
        return False
    reached = vertices & -vertices
    frontier = reached
    while frontier:
        neighbours = 0
        scan = frontier
        while scan:
            least_bit = scan & -scan
            vertex = least_bit.bit_length() - 1
            neighbours |= adjacency[vertex]
            scan ^= least_bit
        frontier = (neighbours & vertices) & ~reached
        reached |= frontier
    return reached == vertices


def contact_count(parts: tuple[int, ...], adjacency: list[int]) -> int:
    return sum(
        touches(parts[left], parts[right], adjacency)
        for left, right in combinations(range(len(parts)), 2)
    )


def exact_optimum(adjacency: list[int]) -> tuple[int, tuple[int, ...]]:
    """Return the exact optimum and lexicographically first optimal model."""

    @lru_cache(maxsize=None)
    def search(parts: tuple[int, ...]) -> tuple[int, tuple[int, ...]]:
        if len(parts) == 7:
            return contact_count(parts, adjacency), parts

        candidates: list[tuple[int, tuple[int, ...]]] = []

        # Delete a whole current branch set.  This represents vertices unused
        # by the final minor model.
        for index in range(len(parts)):
            candidates.append(search(parts[:index] + parts[index + 1 :]))

        # Contract an edge between two current connected branch sets.
        for left, right in combinations(range(len(parts)), 2):
            if not touches(parts[left], parts[right], adjacency):
                continue
            merged = parts[left] | parts[right]
            next_parts = tuple(
                sorted(
                    parts[:left]
                    + parts[left + 1 : right]
                    + parts[right + 1 :]
                    + (merged,)
                )
            )
            candidates.append(search(next_parts))

        best_score = max(score for score, _ in candidates)
        best_model = min(model for score, model in candidates if score == best_score)
        return best_score, best_model

    singletons = tuple(bit(vertex) for vertex in VERTICES)
    return search(singletons)


def bag_text(vertices: int) -> str:
    return "+".join(
        vertex for vertex in VERTICES if vertices & bit(vertex)
    )


def validate_model(
    model: tuple[int, ...], adjacency: list[int], expected_contacts: int
) -> None:
    assert len(model) == 7
    assert all(model)
    assert all(left & right == 0 for left, right in combinations(model, 2))
    assert all(connected(part, adjacency) for part in model)
    assert contact_count(model, adjacency) == expected_contacts


def main() -> None:
    distribution: dict[int, int] = {}
    certificate_lines: list[str] = []

    for colours in product((0, 1), repeat=len(BOUNDARY)):
        if colours[INDEX["a"]] == colours[INDEX["b"]]:
            continue
        if colours.count(0) not in (3, 4):
            continue

        colour_text = "".join(str(colour) for colour in colours)
        for owners in product(HELPERS, repeat=2):
            adjacency = quotient_graph(colours, owners)
            optimum, model = exact_optimum(adjacency)
            validate_model(model, adjacency, optimum)
            assert optimum >= 20

            distribution[optimum] = distribution.get(optimum, 0) + 1
            certificate_lines.append(
                " ".join(
                    (
                        f"colours={colour_text}",
                        f"owners={''.join(owners)}",
                        f"optimum={optimum}",
                        "bags=" + "|".join(bag_text(part) for part in model),
                    )
                )
            )

    certificate = "\n".join(certificate_lines).encode("ascii")
    digest = sha256(certificate).hexdigest()

    assert len(certificate_lines) == EXPECTED_CASES
    assert distribution == EXPECTED_DISTRIBUTION
    assert digest == EXPECTED_CERTIFICATE_SHA256

    distribution_text = ",".join(
        f"{contacts}:{distribution[contacts]}" for contacts in sorted(distribution)
    )
    print(f"PASS cases={len(certificate_lines)} minimum_optimum={min(distribution)}")
    print(f"PASS optimum_distribution={distribution_text}")
    print(f"PASS certificate_sha256={digest}")
    print("NOTE bounded corroboration only; the unbounded lemma uses its written proof")


if __name__ == "__main__":
    main()
