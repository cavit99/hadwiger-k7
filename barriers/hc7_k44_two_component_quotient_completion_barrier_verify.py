#!/usr/bin/env python3
"""Exact finite check of the two-component quotient-completion barrier.

The graph checked here is only a contracted local quotient.  It is not an
instance of the unbounded blocker theorem: its component-contained supports
have order one, and its three cut vertices violate the six-boundary
inequality.  See the adjacent mathematical note for the exact scope.
"""

from functools import lru_cache
from itertools import combinations


VERTICES = (
    "a",
    "b",
    "k0",
    "k1",
    "k2",
    "k3",
    "k4",
    "f",
    "P",
    "Q",
    "t0",
    "t1",
    "t2",
)
INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
LEFT = frozenset(("a", "k0", "k1", "f"))
RIGHT = frozenset(("b", "k2", "k3", "k4"))


def bit(vertex: str) -> int:
    return 1 << INDEX[vertex]


def add_edge(adjacency: list[int], left: str, right: str) -> None:
    adjacency[INDEX[left]] |= bit(right)
    adjacency[INDEX[right]] |= bit(left)


def barrier_graph() -> list[int]:
    adjacency = [0] * len(VERTICES)

    for left in LEFT:
        for right in RIGHT:
            add_edge(adjacency, left, right)

    for cut_vertex in ("t0", "t1", "t2"):
        add_edge(adjacency, "P", cut_vertex)
        add_edge(adjacency, "Q", cut_vertex)

    for root in ("a", "b", "k0", "k1", "k2"):
        add_edge(adjacency, root, "P")
    for root in ("k0", "k1", "k3", "k4"):
        add_edge(adjacency, root, "Q")

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


def contact_count(parts: tuple[int, ...], adjacency: list[int]) -> int:
    return sum(
        touches(parts[left], parts[right], adjacency)
        for left, right in combinations(range(len(parts)), 2)
    )


def exact_minor_optimum(adjacency: list[int]) -> tuple[int, int]:
    """Return the exact best contact count among seven branch sets.

    Deleting a current part represents unused vertices.  Contracting two
    adjacent current parts represents one edge of a spanning tree inside a
    connected branch set.  Starting from singleton parts, these operations
    reach every family of seven disjoint connected branch sets.
    """

    @lru_cache(maxsize=None)
    def search(parts: tuple[int, ...]) -> int:
        if len(parts) == 7:
            return contact_count(parts, adjacency)

        best = 0
        for index in range(len(parts)):
            best = max(best, search(parts[:index] + parts[index + 1 :]))

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
            best = max(best, search(next_parts))

        return best

    optimum = search(tuple(bit(vertex) for vertex in VERTICES))
    return optimum, search.cache_info().currsize


def connected(vertices: int, adjacency: list[int]) -> bool:
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
        frontier = neighbours & vertices & ~reached
        reached |= frontier
    return reached == vertices


def skeleton_bond_maximum() -> tuple[int, int]:
    """Check every bond of the five-vertex `K_{2,3}` skeleton."""

    vertices = ("P", "Q", "t0", "t1", "t2")
    index = {vertex: position for position, vertex in enumerate(vertices)}
    adjacency = [0] * len(vertices)

    for cut_vertex in vertices[2:]:
        for component in ("P", "Q"):
            left = index[component]
            right = index[cut_vertex]
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left

    supports = (
        {index["P"], index["Q"]},
        {index["P"], index["Q"]},
        {index["P"]},
        {index["Q"]},
        {index["Q"]},
    )
    full_set = (1 << len(vertices)) - 1
    bond_count = 0
    maximum = 0

    for shore in range(1, full_set):
        complement = full_set ^ shore
        if shore > complement:
            continue
        if not connected(shore, adjacency) or not connected(complement, adjacency):
            continue
        bond_count += 1
        shore_set = {
            position for position in range(len(vertices)) if shore >> position & 1
        }
        maximum = max(
            maximum,
            sum(
                bool(support & shore_set) and bool(support - shore_set)
                for support in supports
            ),
        )

    return bond_count, maximum


def main() -> None:
    adjacency = barrier_graph()
    edge_count = sum(neighbours.bit_count() for neighbours in adjacency) // 2
    optimum, state_count = exact_minor_optimum(adjacency)
    bond_count, split_maximum = skeleton_bond_maximum()

    assert edge_count == 31
    assert optimum == 19
    assert bond_count == 11
    assert split_maximum == 2

    print(
        f"PASS vertices={len(VERTICES)} edges={edge_count} "
        f"exact_minor_optimum={optimum}"
    )
    print(f"PASS canonical_states={state_count}")
    print(
        f"PASS skeleton_bonds={bond_count} "
        f"maximum_split_supports={split_maximum}"
    )
    print("NOTE local contracted quotient only; q>=6 and support multiplicity fail")


if __name__ == "__main__":
    main()
