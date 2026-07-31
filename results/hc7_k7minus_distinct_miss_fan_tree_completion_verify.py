#!/usr/bin/env python3
"""Verify the finite fan-tree completion in the distinct-miss residue.

The boundary convention is fixed throughout:

* ``Z = {0,1,2} disjoint-union {3,4,5}``;
* the optional cross edge is ``0--3``;
* ``x=6``, ``y=7``, ``u=8``;
* the first exterior component is adjacent to ``y`` and all of ``Z``;
* the second exterior component is adjacent to ``x`` and all of ``Z``.

For every surviving portal pattern, an ``x``--``Z`` fan through the second
component and a ``y``--``Z`` fan through the first component reduce to two
finite fan-tree gadgets.  The verifier exhausts every labelled tree in both
gadgets and constructs six connected ``Z``-rooted bags with at least
fourteen of the fifteen pairwise adjacencies.  The singleton ``{u}`` then
completes a ``K_7^-`` minor.

This script is deterministic and uses only the Python standard library.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product


ROOTS = tuple(range(6))
X = 6
Y = 7
U = 8
E = 9
F = 10
UNUSED = 6
PAIR_BIT = {
    pair: bit for bit, pair in enumerate(combinations(ROOTS, 2))
}


def normalized_edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def edge_bit(a: int, b: int) -> int:
    return 1 << PAIR_BIT[normalized_edge(a, b)]


def z_edges(bridge: bool) -> set[tuple[int, int]]:
    edges = {
        (0, 1),
        (0, 2),
        (1, 2),
        (3, 4),
        (3, 5),
        (4, 5),
    }
    if bridge:
        edges.add((0, 3))
    return edges


def boundary_edges(
    bridge: bool, x_neighbors: int, y_neighbors: int
) -> set[tuple[int, int]]:
    edges = z_edges(bridge)
    for z in ROOTS:
        if x_neighbors >> z & 1:
            edges.add((z, X))
        if y_neighbors >> z & 1:
            edges.add((z, Y))
    return edges


def is_clique(
    vertices: tuple[int, ...], edges: set[tuple[int, int]]
) -> bool:
    return all(normalized_edge(a, b) in edges for a, b in combinations(vertices, 2))


def is_independent(
    vertices: tuple[int, ...], edges: set[tuple[int, int]]
) -> bool:
    return all(normalized_edge(a, b) not in edges for a, b in combinations(vertices, 2))


def valid_portal_pattern(
    bridge: bool, x_neighbors: int, y_neighbors: int
) -> bool:
    edges = boundary_edges(bridge, x_neighbors, y_neighbors)
    vertices = tuple(range(8))
    return (
        not any(is_clique(q, edges) for q in combinations(vertices, 4))
        and any(is_independent(q, edges) for q in combinations(vertices, 3))
        and not any(is_independent(q, edges) for q in combinations(vertices, 4))
    )


def boundary_automorphisms(bridge: bool) -> tuple[tuple[int, ...], ...]:
    expected = z_edges(bridge)
    answer = []
    for permutation in permutations(ROOTS):
        image = {
            normalized_edge(permutation[a], permutation[b])
            for a, b in expected
        }
        if image == expected:
            answer.append(permutation)
    return tuple(answer)


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(
        1 << permutation[z] for z in ROOTS if mask >> z & 1
    )


def canonical_portal_pair(
    x_neighbors: int,
    y_neighbors: int,
    automorphisms: tuple[tuple[int, ...], ...],
) -> tuple[int, int]:
    images = []
    for permutation in automorphisms:
        first = permute_mask(x_neighbors, permutation)
        second = permute_mask(y_neighbors, permutation)
        images.extend(((first, second), (second, first)))
    return min(images)


def quotient_edges(
    bridge: bool, x_neighbors: int, y_neighbors: int
) -> set[tuple[int, int]]:
    edges = boundary_edges(bridge, x_neighbors, y_neighbors)
    edges.update((U, z) for z in range(8))
    edges.update((z, E) for z in ROOTS)
    edges.update((z, F) for z in ROOTS)
    edges.add((Y, E))
    edges.add((X, F))
    return {normalized_edge(a, b) for a, b in edges}


def bag_adjacencies(
    bags: tuple[frozenset[int], ...], edges: set[tuple[int, int]]
) -> tuple[tuple[int, int], ...]:
    answer = []
    for i, first in enumerate(bags):
        for j in range(i + 1, len(bags)):
            second = bags[j]
            if any(
                normalized_edge(a, b) in edges
                for a in first
                for b in second
            ):
                answer.append((i, j))
    return tuple(answer)


def quotient_minor_certificate(
    edges: set[tuple[int, int]],
) -> tuple[frozenset[int], ...] | None:
    initial = tuple(frozenset((vertex,)) for vertex in range(11))

    @lru_cache(maxsize=None)
    def search(
        canonical_bags: tuple[tuple[int, ...], ...],
    ) -> tuple[frozenset[int], ...] | None:
        bags = tuple(frozenset(bag) for bag in canonical_bags)
        if len(bags) == 7:
            return bags if len(bag_adjacencies(bags, edges)) >= 20 else None

        adjacencies = bag_adjacencies(bags, edges)
        for i, j in adjacencies:
            merged = bags[i] | bags[j]
            next_bags = tuple(
                bag for k, bag in enumerate(bags) if k not in (i, j)
            ) + (merged,)
            key = tuple(sorted(tuple(sorted(bag)) for bag in next_bags))
            certificate = search(key)
            if certificate is not None:
                return certificate

        for deleted in range(len(bags)):
            next_bags = tuple(
                bag for k, bag in enumerate(bags) if k != deleted
            )
            key = tuple(sorted(tuple(sorted(bag)) for bag in next_bags))
            certificate = search(key)
            if certificate is not None:
                return certificate
        return None

    key = tuple(tuple(bag) for bag in initial)
    return search(key)


def connected(
    vertices: set[int], edges: set[tuple[int, int]]
) -> bool:
    if not vertices:
        return False
    reached = {min(vertices)}
    while True:
        enlarged = reached | {
            b
            for a, b in edges
            if a in reached and b in vertices
        } | {
            a
            for a, b in edges
            if b in reached and a in vertices
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def validate_minor_certificate(
    bags: tuple[frozenset[int], ...],
    edges: set[tuple[int, int]],
    required_adjacencies: int,
) -> None:
    assert all(bags)
    assert all(connected(set(bag), edges) for bag in bags)
    assert sum(len(bag) for bag in bags) == len(set().union(*bags))
    assert len(bag_adjacencies(bags, edges)) >= required_adjacencies


def labelled_trees(vertices: tuple[int, ...]):
    """Generate every labelled tree on ``vertices`` exactly once."""
    if len(vertices) <= 1:
        yield frozenset()
        return
    if len(vertices) == 2:
        yield frozenset((normalized_edge(*vertices),))
        return

    for sequence in product(vertices, repeat=len(vertices) - 2):
        degree = {vertex: 1 for vertex in vertices}
        for vertex in sequence:
            degree[vertex] += 1
        edges = []
        for vertex in sequence:
            leaf = min(
                candidate
                for candidate in vertices
                if degree[candidate] == 1
            )
            edges.append(normalized_edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        final = tuple(
            vertex for vertex in vertices if degree[vertex] == 1
        )
        assert len(final) == 2
        edges.append(normalized_edge(*final))
        yield frozenset(edges)


@dataclass(frozen=True)
class SideState:
    contact_mask: int
    assignment: tuple[int, ...]


def side_graph(
    neighbor_mask: int, tree: tuple[tuple[int, int], ...]
) -> tuple[int, tuple[tuple[int, int], ...], tuple[int, ...]]:
    misses = tuple(z for z in ROOTS if not (neighbor_mask >> z & 1))
    limb_vertex = {z: 7 + index for index, z in enumerate(misses)}
    edges = []
    for z in ROOTS:
        if neighbor_mask >> z & 1:
            edges.append((X, z))
        else:
            edges.extend(((X, limb_vertex[z]), (limb_vertex[z], z)))
    edges.extend(
        (limb_vertex[a], limb_vertex[b]) for a, b in tree
    )
    return 7 + len(misses), tuple(edges), misses


@lru_cache(maxsize=None)
def side_states(
    neighbor_mask: int, tree: tuple[tuple[int, int], ...]
) -> tuple[SideState, ...]:
    order, edges, _ = side_graph(neighbor_mask, tree)
    witnesses: dict[int, tuple[int, ...]] = {}

    for assignment in product(range(7), repeat=order - 6):
        labels = tuple(ROOTS) + assignment
        if any(
            not connected(
                {
                    vertex
                    for vertex in range(order)
                    if labels[vertex] == root
                },
                set(edges),
            )
            for root in ROOTS
        ):
            continue

        contact_mask = 0
        for a, b in edges:
            first, second = labels[a], labels[b]
            if first < 6 and second < 6 and first != second:
                contact_mask |= edge_bit(first, second)
        witnesses.setdefault(contact_mask, assignment)

    maximal = []
    for mask in sorted(
        witnesses, key=lambda value: (-value.bit_count(), value)
    ):
        if not any(mask | kept.contact_mask == kept.contact_mask for kept in maximal):
            maximal.append(SideState(mask, witnesses[mask]))
    return tuple(maximal)


def fan_tree_edges_and_maps(
    bridge: bool,
    x_neighbors: int,
    y_neighbors: int,
    x_tree: tuple[tuple[int, int], ...],
    y_tree: tuple[tuple[int, int], ...],
) -> tuple[
    set[tuple[int, int]],
    tuple[int, ...],
    tuple[int, ...],
]:
    edges = boundary_edges(bridge, x_neighbors, y_neighbors)
    edges.update((U, vertex) for vertex in range(8))
    next_vertex = 9

    x_misses = tuple(z for z in ROOTS if not (x_neighbors >> z & 1))
    x_limb = {}
    for z in x_misses:
        x_limb[z] = next_vertex
        edges.add((X, next_vertex))
        edges.add(normalized_edge(z, next_vertex))
        next_vertex += 1
    edges.update(
        normalized_edge(x_limb[a], x_limb[b]) for a, b in x_tree
    )

    y_misses = tuple(z for z in ROOTS if not (y_neighbors >> z & 1))
    y_limb = {}
    for z in y_misses:
        y_limb[z] = next_vertex
        edges.add((Y, next_vertex))
        edges.add(normalized_edge(z, next_vertex))
        next_vertex += 1
    edges.update(
        normalized_edge(y_limb[a], y_limb[b]) for a, b in y_tree
    )

    x_map = (X,) + tuple(x_limb[z] for z in x_misses)
    y_map = (Y,) + tuple(y_limb[z] for z in y_misses)
    return (
        {normalized_edge(a, b) for a, b in edges},
        x_map,
        y_map,
    )


def rooted_fan_tree_certificate(
    bridge: bool,
    x_neighbors: int,
    y_neighbors: int,
    x_tree: tuple[tuple[int, int], ...],
    y_tree: tuple[tuple[int, int], ...],
) -> tuple[frozenset[int], ...] | None:
    base_mask = 0
    for a, b in z_edges(bridge):
        base_mask |= edge_bit(a, b)

    x_states = side_states(x_neighbors, x_tree)
    y_states = side_states(y_neighbors, y_tree)
    selected = None
    for x_state in x_states:
        for y_state in y_states:
            if (
                base_mask
                | x_state.contact_mask
                | y_state.contact_mask
            ).bit_count() >= 14:
                selected = (x_state, y_state)
                break
        if selected is not None:
            break
    if selected is None:
        return None

    edges, x_map, y_map = fan_tree_edges_and_maps(
        bridge,
        x_neighbors,
        y_neighbors,
        x_tree,
        y_tree,
    )
    bags = [set((root,)) for root in ROOTS]
    for vertex, label in zip(x_map, selected[0].assignment):
        if label < 6:
            bags[label].add(vertex)
    for vertex, label in zip(y_map, selected[1].assignment):
        if label < 6:
            bags[label].add(vertex)
    certificate = tuple(frozenset(bag) for bag in bags)

    for root, bag in enumerate(certificate):
        assert root in bag
    validate_minor_certificate(certificate, edges, 14)
    assert all(
        normalized_edge(U, root) in edges for root in ROOTS
    )
    return certificate


def serialize_bags(bags: tuple[frozenset[int], ...]) -> str:
    return "|".join(
        ",".join(str(vertex) for vertex in sorted(bag))
        for bag in bags
    )


def main() -> None:
    expected = {
        False: {
            "automorphisms": 72,
            "labelled_valid": 1032,
            "valid_orbits": 21,
            "survivors": ((0x01, 0x06), (0x03, 0x05), (0x03, 0x0C)),
        },
        True: {
            "automorphisms": 8,
            "labelled_valid": 1113,
            "valid_orbits": 109,
            "survivors": (
                (0x01, 0x06),
                (0x02, 0x05),
                (0x03, 0x05),
                (0x03, 0x06),
                (0x06, 0x09),
                (0x06, 0x30),
            ),
        },
    }

    mask_digest_lines = []
    quotient_digest_lines = []
    tree_digest_lines = []
    summary = []

    for bridge in (False, True):
        automorphisms = boundary_automorphisms(bridge)
        orbits: dict[tuple[int, int], list[tuple[int, int]]] = {}
        labelled_valid = 0
        for x_neighbors in range(64):
            for y_neighbors in range(64):
                if not valid_portal_pattern(
                    bridge, x_neighbors, y_neighbors
                ):
                    continue
                labelled_valid += 1
                canonical = canonical_portal_pair(
                    x_neighbors, y_neighbors, automorphisms
                )
                orbits.setdefault(canonical, []).append(
                    (x_neighbors, y_neighbors)
                )
                mask_digest_lines.append(
                    f"{int(bridge)}:{x_neighbors:02x}:{y_neighbors:02x}:"
                    f"{canonical[0]:02x}:{canonical[1]:02x}"
                )

        assert len(automorphisms) == expected[bridge]["automorphisms"]
        assert labelled_valid == expected[bridge]["labelled_valid"]
        assert len(orbits) == expected[bridge]["valid_orbits"]

        survivors = []
        for canonical in sorted(orbits):
            edges = quotient_edges(bridge, *canonical)
            certificate = quotient_minor_certificate(edges)
            if certificate is None:
                survivors.append(canonical)
                quotient_digest_lines.append(
                    f"{int(bridge)}:{canonical[0]:02x}:"
                    f"{canonical[1]:02x}:NONE"
                )
            else:
                validate_minor_certificate(certificate, edges, 20)
                quotient_digest_lines.append(
                    f"{int(bridge)}:{canonical[0]:02x}:"
                    f"{canonical[1]:02x}:{serialize_bags(certificate)}"
                )

        assert tuple(survivors) == expected[bridge]["survivors"]

        tree_counts = []
        for x_neighbors, y_neighbors in survivors:
            x_misses = tuple(
                z for z in ROOTS if not (x_neighbors >> z & 1)
            )
            y_misses = tuple(
                z for z in ROOTS if not (y_neighbors >> z & 1)
            )
            x_trees = tuple(labelled_trees(x_misses))
            y_trees = tuple(labelled_trees(y_misses))
            count = 0
            for x_tree in x_trees:
                x_key = tuple(sorted(x_tree))
                for y_tree in y_trees:
                    y_key = tuple(sorted(y_tree))
                    certificate = rooted_fan_tree_certificate(
                        bridge,
                        x_neighbors,
                        y_neighbors,
                        x_key,
                        y_key,
                    )
                    assert certificate is not None
                    tree_digest_lines.append(
                        f"{int(bridge)}:{x_neighbors:02x}:"
                        f"{y_neighbors:02x}:{x_key}:{y_key}:"
                        f"{serialize_bags(certificate)}"
                    )
                    count += 1
            tree_counts.append(count)

        summary.append(
            (
                int(bridge),
                labelled_valid,
                len(orbits),
                len(survivors),
                tuple(tree_counts),
            )
        )

    mask_digest = sha256(
        ("\n".join(mask_digest_lines) + "\n").encode()
    ).hexdigest()
    quotient_digest = sha256(
        ("\n".join(quotient_digest_lines) + "\n").encode()
    ).hexdigest()
    tree_digest = sha256(
        ("\n".join(tree_digest_lines) + "\n").encode()
    ).hexdigest()
    expected_digests = (
        "1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203",
        "cb251c5518e05b5b1ba79a9149600226777cee5e8677f6bf9a8af90b18b626c3",
        "5c19a21365f7380afef89b6164dcbee3752db001198cb04aa9270bc4aad33785",
    )
    assert (mask_digest, quotient_digest, tree_digest) == expected_digests

    print("GREEN: distinct-miss fan-tree completion verified")
    for (
        bridge,
        labelled_valid,
        valid_orbits,
        survivor_count,
        tree_counts,
    ) in summary:
        print(
            f"bridge={bridge} labelled_valid={labelled_valid} "
            f"valid_orbits={valid_orbits} "
            f"quotient_survivor_orbits={survivor_count} "
            f"tree_pair_counts={tree_counts}"
        )
    print(f"mask_orbit_digest={mask_digest}")
    print(f"quotient_certificate_digest={quotient_digest}")
    print(f"fan_tree_certificate_digest={tree_digest}")


if __name__ == "__main__":
    main()
