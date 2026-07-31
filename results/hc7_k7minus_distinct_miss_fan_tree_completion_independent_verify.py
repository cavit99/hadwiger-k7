#!/usr/bin/env python3
"""Independent direct-contraction check of the fan-tree completion.

This checker deliberately does not import or reproduce the retained verifier's
side-state, contact-mask, dominance, or state-combination machinery.  It
regenerates the valid portal-mask orbits, classifies their whole-component
quotients by deletion and edge contraction, builds every surviving sparse
fan-tree graph, and contracts actual graph edges to six connected rooted bags.
Together with the singleton ``{u}``, those bags form a spanning ``K_7^-``
minor model.

The script is deterministic and uses only the Python standard library.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product


ROOTS = tuple(range(6))
X, Y, U, E, F = 6, 7, 8, 9, 10


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def common_six_edges(bridge: bool) -> set[tuple[int, int]]:
    answer = {
        (0, 1), (0, 2), (1, 2),
        (3, 4), (3, 5), (4, 5),
    }
    if bridge:
        answer.add((0, 3))
    return answer


def boundary_edges(
    bridge: bool, x_mask: int, y_mask: int
) -> set[tuple[int, int]]:
    answer = common_six_edges(bridge)
    for root in ROOTS:
        if x_mask >> root & 1:
            answer.add(edge(X, root))
        if y_mask >> root & 1:
            answer.add(edge(Y, root))
    return answer


def is_clique(
    vertices: tuple[int, ...], edges: set[tuple[int, int]]
) -> bool:
    return all(edge(a, b) in edges for a, b in combinations(vertices, 2))


def is_independent(
    vertices: tuple[int, ...], edges: set[tuple[int, int]]
) -> bool:
    return all(edge(a, b) not in edges for a, b in combinations(vertices, 2))


def valid_portal_pair(bridge: bool, x_mask: int, y_mask: int) -> bool:
    edges = boundary_edges(bridge, x_mask, y_mask)
    vertices = tuple(range(8))
    return (
        not any(is_clique(q, edges) for q in combinations(vertices, 4))
        and any(is_independent(q, edges) for q in combinations(vertices, 3))
        and not any(is_independent(q, edges) for q in combinations(vertices, 4))
    )


def root_automorphisms(bridge: bool) -> tuple[tuple[int, ...], ...]:
    expected = common_six_edges(bridge)
    answer = []
    for permutation in permutations(ROOTS):
        image = {
            edge(permutation[a], permutation[b]) for a, b in expected
        }
        if image == expected:
            answer.append(permutation)
    return tuple(answer)


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(1 << permutation[z] for z in ROOTS if mask >> z & 1)


def canonical_portal_pair(
    x_mask: int,
    y_mask: int,
    automorphisms: tuple[tuple[int, ...], ...],
) -> tuple[int, int]:
    images = []
    for permutation in automorphisms:
        first = permute_mask(x_mask, permutation)
        second = permute_mask(y_mask, permutation)
        images.extend(((first, second), (second, first)))
    return min(images)


def component_contacts(
    components: tuple[int, ...], edges: tuple[tuple[int, int], ...]
) -> int:
    owner = {}
    for index, component in enumerate(components):
        vertices = component
        while vertices:
            low_bit = vertices & -vertices
            owner[low_bit.bit_length() - 1] = index
            vertices ^= low_bit
    return len({
        edge(owner[a], owner[b])
        for a, b in edges
        if owner.get(a) is not None
        and owner.get(b) is not None
        and owner[a] != owner[b]
    })


def adjacent_component_pairs(
    components: tuple[int, ...], edges: tuple[tuple[int, int], ...]
) -> tuple[tuple[int, int], ...]:
    owner = {}
    for index, component in enumerate(components):
        vertices = component
        while vertices:
            low_bit = vertices & -vertices
            owner[low_bit.bit_length() - 1] = index
            vertices ^= low_bit
    return tuple(sorted({
        edge(owner[a], owner[b])
        for a, b in edges
        if owner.get(a) is not None
        and owner.get(b) is not None
        and owner[a] != owner[b]
    }))


def quotient_has_k7_minus(
    order: int, edges: set[tuple[int, int]]
) -> bool:
    """Decide the minor directly by deleting and contracting components."""
    edge_tuple = tuple(sorted(edges))

    @lru_cache(maxsize=None)
    def search(components: tuple[int, ...]) -> bool:
        if len(components) < 7:
            return False
        if len(components) == 7:
            return component_contacts(components, edge_tuple) >= 20

        for i, j in adjacent_component_pairs(components, edge_tuple):
            merged = components[i] | components[j]
            next_components = tuple(sorted(
                component for k, component in enumerate(components)
                if k not in (i, j)
            ) + [merged])
            if search(next_components):
                return True

        for deleted in range(len(components)):
            next_components = tuple(
                component for k, component in enumerate(components)
                if k != deleted
            )
            if search(next_components):
                return True
        return False

    return search(tuple(1 << vertex for vertex in range(order)))


def quotient_edges(
    bridge: bool, x_mask: int, y_mask: int
) -> set[tuple[int, int]]:
    answer = boundary_edges(bridge, x_mask, y_mask)
    answer.update(edge(U, vertex) for vertex in range(8))
    answer.update(edge(E, root) for root in ROOTS)
    answer.update(edge(F, root) for root in ROOTS)
    answer.add(edge(E, Y))
    answer.add(edge(F, X))
    return answer


def labelled_trees(vertices: tuple[int, ...]):
    """Generate labelled trees once each, using Prüfer sequences."""
    if len(vertices) <= 1:
        yield ()
        return
    if len(vertices) == 2:
        yield (edge(*vertices),)
        return

    for sequence in product(vertices, repeat=len(vertices) - 2):
        degree = {vertex: 1 for vertex in vertices}
        for vertex in sequence:
            degree[vertex] += 1
        answer = []
        for vertex in sequence:
            leaf = min(v for v in vertices if degree[v] == 1)
            answer.append(edge(leaf, vertex))
            degree[leaf] -= 1
            degree[vertex] -= 1
        leaves = tuple(v for v in vertices if degree[v] == 1)
        require(len(leaves) == 2, "invalid Prüfer decoding")
        answer.append(edge(*leaves))
        yield tuple(sorted(answer))


def fan_tree_graph(
    bridge: bool,
    x_mask: int,
    y_mask: int,
    x_tree: tuple[tuple[int, int], ...],
    y_tree: tuple[tuple[int, int], ...],
) -> tuple[int, set[tuple[int, int]]]:
    edges = boundary_edges(bridge, x_mask, y_mask)
    edges.update(edge(U, vertex) for vertex in range(8))
    next_vertex = 9

    x_limb = {}
    for root in ROOTS:
        if x_mask >> root & 1:
            continue
        x_limb[root] = next_vertex
        edges.update((edge(X, next_vertex), edge(root, next_vertex)))
        next_vertex += 1
    edges.update(edge(x_limb[a], x_limb[b]) for a, b in x_tree)

    y_limb = {}
    for root in ROOTS:
        if y_mask >> root & 1:
            continue
        y_limb[root] = next_vertex
        edges.update((edge(Y, next_vertex), edge(root, next_vertex)))
        next_vertex += 1
    edges.update(edge(y_limb[a], y_limb[b]) for a, b in y_tree)
    return next_vertex, edges


def rooted_spanning_certificate(
    order: int, edges: set[tuple[int, int]]
) -> tuple[int, ...] | None:
    """Contract edges to six root-distinct bags, keeping ``u`` singleton."""
    edge_tuple = tuple(sorted(e for e in edges if U not in e))
    start = tuple(1 << vertex for vertex in range(order) if vertex != U)
    failed: set[tuple[int, ...]] = set()

    def root_count(component: int) -> int:
        return (component & ((1 << 6) - 1)).bit_count()

    def search(components: tuple[int, ...]) -> tuple[int, ...] | None:
        if components in failed:
            return None
        if len(components) == 6:
            if (
                all(root_count(component) == 1 for component in components)
                and component_contacts(components, edge_tuple) >= 14
            ):
                return tuple(sorted(
                    components,
                    key=lambda component: (
                        component & -component
                    ).bit_length() - 1,
                ))
            failed.add(components)
            return None

        pairs = adjacent_component_pairs(components, edge_tuple)
        unrooted = [
            i for i, component in enumerate(components)
            if root_count(component) == 0
        ]
        if not unrooted:
            failed.add(components)
            return None

        incident = {
            i: [pair for pair in pairs if i in pair]
            for i in unrooted
        }
        chosen = min(unrooted, key=lambda i: (len(incident[i]), components[i]))
        candidates = []
        for i, j in incident[chosen]:
            if root_count(components[i]) and root_count(components[j]):
                continue
            merged = components[i] | components[j]
            next_components = tuple(sorted(
                [component for k, component in enumerate(components)
                 if k not in (i, j)] + [merged]
            ))
            candidates.append(next_components)

        for next_components in candidates:
            certificate = search(next_components)
            if certificate is not None:
                return certificate
        failed.add(components)
        return None

    return search(start)


def vertices(mask: int) -> tuple[int, ...]:
    answer = []
    while mask:
        low_bit = mask & -mask
        answer.append(low_bit.bit_length() - 1)
        mask ^= low_bit
    return tuple(answer)


def connected(vertex_set: set[int], edges: set[tuple[int, int]]) -> bool:
    reached = {min(vertex_set)}
    while True:
        expanded = reached | {
            b for a, b in edges if a in reached and b in vertex_set
        } | {
            a for a, b in edges if b in reached and a in vertex_set
        }
        if expanded == reached:
            return reached == vertex_set
        reached = expanded


def validate_spanning_certificate(
    order: int,
    edges: set[tuple[int, int]],
    certificate: tuple[int, ...],
) -> None:
    bags = tuple(set(vertices(component)) for component in certificate) + ({U},)
    require(len(bags) == 7, "certificate does not have seven bags")
    require(all(bags), "certificate has an empty bag")
    require(
        all(connected(bag, edges) for bag in bags),
        "certificate has a disconnected bag",
    )
    require(
        set().union(*bags) == set(range(order))
        and sum(map(len, bags)) == order,
        "certificate bags do not partition the graph",
    )
    require(
        all(root in bags[root] for root in ROOTS),
        "certificate does not preserve all six roots",
    )
    bag_masks = tuple(sum(1 << v for v in bag) for bag in bags)
    require(
        component_contacts(bag_masks, tuple(sorted(edges))) >= 20,
        "certificate is not a K_7^- minor model",
    )


def serialize_certificate(certificate: tuple[int, ...]) -> str:
    return "|".join(
        ",".join(map(str, vertices(component))) for component in certificate
    ) + f"|{U}"


def main() -> None:
    expected = {
        False: {
            "automorphisms": 72,
            "labelled": 1032,
            "orbits": 21,
            "survivors": ((0x01, 0x06), (0x03, 0x05), (0x03, 0x0C)),
        },
        True: {
            "automorphisms": 8,
            "labelled": 1113,
            "orbits": 109,
            "survivors": (
                (0x01, 0x06), (0x02, 0x05), (0x03, 0x05),
                (0x03, 0x06), (0x06, 0x09), (0x06, 0x30),
            ),
        },
    }
    orbit_lines = []
    certificate_lines = []
    summaries = []

    for bridge in (False, True):
        automorphisms = root_automorphisms(bridge)
        orbits = set()
        labelled = 0
        for x_mask in range(64):
            for y_mask in range(64):
                if not valid_portal_pair(bridge, x_mask, y_mask):
                    continue
                labelled += 1
                canonical = canonical_portal_pair(
                    x_mask, y_mask, automorphisms
                )
                orbits.add(canonical)
                orbit_lines.append(
                    f"{int(bridge)}:{x_mask:02x}:{y_mask:02x}:"
                    f"{canonical[0]:02x}:{canonical[1]:02x}"
                )

        require(
            len(automorphisms) == expected[bridge]["automorphisms"],
            f"wrong automorphism count for bridge={int(bridge)}",
        )
        require(
            labelled == expected[bridge]["labelled"],
            f"wrong labelled portal count for bridge={int(bridge)}",
        )
        require(
            len(orbits) == expected[bridge]["orbits"],
            f"wrong portal-orbit count for bridge={int(bridge)}",
        )

        survivors = tuple(
            masks for masks in sorted(orbits)
            if not quotient_has_k7_minus(
                11, quotient_edges(bridge, *masks)
            )
        )
        require(
            survivors == expected[bridge]["survivors"],
            f"wrong quotient survivors for bridge={int(bridge)}: {survivors}",
        )

        tree_counts = []
        for x_mask, y_mask in survivors:
            x_misses = tuple(z for z in ROOTS if not (x_mask >> z & 1))
            y_misses = tuple(z for z in ROOTS if not (y_mask >> z & 1))
            count = 0
            for x_tree in labelled_trees(x_misses):
                for y_tree in labelled_trees(y_misses):
                    order, edges = fan_tree_graph(
                        bridge, x_mask, y_mask, x_tree, y_tree
                    )
                    certificate = rooted_spanning_certificate(order, edges)
                    require(
                        certificate is not None,
                        "no direct-contraction certificate for "
                        f"{int(bridge)}:{x_mask:02x}:{y_mask:02x}:"
                        f"{x_tree}:{y_tree}",
                    )
                    validate_spanning_certificate(
                        order, edges, certificate
                    )
                    certificate_lines.append(
                        f"{int(bridge)}:{x_mask:02x}:{y_mask:02x}:"
                        f"{x_tree}:{y_tree}:{serialize_certificate(certificate)}"
                    )
                    count += 1
            tree_counts.append(count)
        summaries.append((int(bridge), labelled, len(orbits), tree_counts))

    require(
        sum(sum(summary[3]) for summary in summaries) == 7536,
        "wrong total number of checked fan-tree pairs",
    )
    orbit_digest = sha256(
        ("\n".join(orbit_lines) + "\n").encode()
    ).hexdigest()
    certificate_digest = sha256(
        ("\n".join(certificate_lines) + "\n").encode()
    ).hexdigest()
    require(
        orbit_digest
        == "1d653544a19aed2fac36589f1d113583fe29f7a2af58679e90b574558d9f3203",
        "portal-orbit digest changed",
    )
    require(
        certificate_digest
        == "a75aae228f346587a12ab0821c1a1e735b4d25e7ad9181b161a6512bab5c4ce4",
        "direct-contraction certificate digest changed",
    )

    print("GREEN: independent direct-contraction fan-tree check verified")
    for bridge, labelled, orbit_count, tree_counts in summaries:
        print(
            f"bridge={bridge} labelled_valid={labelled} "
            f"valid_orbits={orbit_count} "
            f"quotient_survivor_orbits={len(tree_counts)} "
            f"tree_pair_counts={tuple(tree_counts)}"
        )
    print(f"mask_orbit_digest={orbit_digest}")
    print(f"direct_contraction_certificate_digest={certificate_digest}")


if __name__ == "__main__":
    main()
