#!/usr/bin/env python3
"""Verify the natural-six-boundary three-colouring linkage barrier."""

from __future__ import annotations

from itertools import combinations


BOUNDARY = ("a", "b", "r", "s", "x1", "x2", "x3", "x4")
T = ("r", "s", "x1", "x2", "x3", "x4")
ALPHA_TERMINALS = ("r", "s")
GAMMA_TERMINALS = ("a", "b")

TRIPLES = {
    "a": (1, 1, 2),
    "b": (1, 2, 1),
    "r": (2, 4, 4),
    "s": (2, 2, 2),
    "x1": (3, 3, 5),
    "x2": (4, 3, 6),
    "x3": (5, 5, 3),
    "x4": (6, 6, 3),
    **{f"q{i}": (i, i, i) for i in range(1, 7)},
    "v34": (3, 1, 2),
    "v56": (5, 1, 2),
    "p12": (3, 2, 4),
    "q12": (4, 1, 3),
    "p21": (5, 3, 2),
    "q21": (6, 4, 1),
    "w": (3, 2, 1),
}

E1 = frozenset(("v34", "q5"))
E2 = frozenset(("v56", "q3"))
REMOVED_FROM_CORE = {
    frozenset(("r", "x3")),
    frozenset(("r", "x4")),
    E1,
    E2,
}


def edge(left, right):
    return frozenset((left, right))


def coordinate_edges():
    answer = set()
    for left, right in combinations(TRIPLES, 2):
        if all(a != b for a, b in zip(TRIPLES[left], TRIPLES[right])):
            answer.add(edge(left, right))
    return answer


H_VERTICES = tuple(TRIPLES)
H_EDGES = coordinate_edges() - REMOVED_FROM_CORE
K_VERTICES = H_VERTICES + ("z",)
K_EDGES = H_EDGES | {edge("z", terminal) for terminal in T}
G_VERTICES = K_VERTICES
G_EDGES = K_EDGES | {edge("z", "a"), edge("z", "b"), E1, E2}
J_VERTICES = G_VERTICES
J_EDGES = G_EDGES - {E1, E2}
G_MINUS_Z_EDGES = G_EDGES - {pair for pair in G_EDGES if "z" in pair}


def adjacency(vertices, edges):
    rows = {vertex: set() for vertex in vertices}
    for pair in edges:
        if len(pair) != 2:
            raise RuntimeError("loop in edge set")
        left, right = tuple(pair)
        rows[left].add(right)
        rows[right].add(left)
    return rows


def connected(vertices, edges):
    vertices = set(vertices)
    if not vertices:
        return False
    rows = adjacency(vertices, (pair for pair in edges if pair <= vertices))
    seen = {next(iter(vertices))}
    frontier = list(seen)
    while frontier:
        vertex = frontier.pop()
        new = rows[vertex] - seen
        seen.update(new)
        frontier.extend(new)
    return seen == vertices


def components(vertices, edges):
    vertices = set(vertices)
    rows = adjacency(vertices, (pair for pair in edges if pair <= vertices))
    answer = []
    unseen = set(vertices)
    while unseen:
        start = min(unseen)
        component = {start}
        frontier = [start]
        unseen.remove(start)
        while frontier:
            vertex = frontier.pop()
            new = rows[vertex] & unseen
            unseen.difference_update(new)
            component.update(new)
            frontier.extend(new)
        answer.append(frozenset(component))
    return tuple(answer)


def connectivity_at_least(vertices, edges, order):
    vertices = tuple(vertices)
    for size in range(order):
        for deleted in combinations(vertices, size):
            remaining = set(vertices) - set(deleted)
            if len(remaining) > 1 and not connected(remaining, edges):
                return False
    return True


def minimum_degree(vertices, edges):
    rows = adjacency(vertices, edges)
    return min(len(rows[vertex]) for vertex in vertices)


def proper(colouring, edges):
    return all(colouring[left] != colouring[right] for left, right in map(tuple, edges))


def max_clique(vertices, edges):
    vertices = tuple(vertices)
    best = 0
    for size in range(1, len(vertices) + 1):
        if any(
            all(edge(left, right) in edges for left, right in combinations(part, 2))
            for part in combinations(vertices, size)
        ):
            best = size
    return best


def max_independent(vertices, edges):
    vertices = tuple(vertices)
    best = 0
    for size in range(1, len(vertices) + 1):
        if any(
            all(edge(left, right) not in edges for left, right in combinations(part, 2))
            for part in combinations(vertices, size)
        ):
            best = size
    return best


def anchored_six_colourings(vertices, edges):
    """Enumerate all colourings after fixing colour(q_i)=i."""

    vertices = tuple(vertices)
    rows = adjacency(vertices, edges)
    colouring = {f"q{i}": i for i in range(1, 7)}
    uncoloured = tuple(vertex for vertex in vertices if vertex not in colouring)
    domains = {}
    for vertex in uncoloured:
        domains[vertex] = tuple(
            colour
            for colour in range(1, 7)
            if f"q{colour}" not in rows[vertex]
        )

    answer = []

    def search(remaining):
        if not remaining:
            answer.append(dict(colouring))
            return

        choices = []
        for vertex in remaining:
            allowed = tuple(
                colour
                for colour in domains[vertex]
                if all(colouring.get(neighbour) != colour for neighbour in rows[vertex])
            )
            if not allowed:
                return
            choices.append((len(allowed), vertex, allowed))

        _, vertex, allowed = min(choices)
        rest = tuple(other for other in remaining if other != vertex)
        for colour in allowed:
            colouring[vertex] = colour
            search(rest)
            del colouring[vertex]

    search(uncoloured)
    return tuple(answer)


def verify_graphs():
    expected = {
        "H": (H_VERTICES, H_EDGES, 21, 129, 8, 8),
        "K": (K_VERTICES, K_EDGES, 22, 135, 6, 6),
        "J": (J_VERTICES, J_EDGES, 22, 137, 8, 8),
        "G": (G_VERTICES, G_EDGES, 22, 139, 8, 8),
    }
    for name, (vertices, edges, order, size, delta, connectivity) in expected.items():
        if len(vertices) != order or len(edges) != size:
            raise RuntimeError(f"wrong {name} order or size")
        if minimum_degree(vertices, edges) != delta:
            raise RuntimeError(f"wrong {name} minimum degree")
        if not connectivity_at_least(vertices, edges, connectivity):
            raise RuntimeError(f"{name} has connectivity below {connectivity}")

    # The minimum degree gives the upper bound eight for H and G; T is a
    # six-cut of K and z has degree six there.
    if len(adjacency(K_VERTICES, K_EDGES)["z"]) != 6:
        raise RuntimeError("z does not certify kappa(K)<=6")

    boundary_edges = {pair for pair in G_EDGES if pair <= set(BOUNDARY)}
    if max_clique(BOUNDARY, boundary_edges) != 3:
        raise RuntimeError("wrong boundary clique number")
    if max_independent(BOUNDARY, boundary_edges) != 3:
        raise RuntimeError("wrong boundary independence number")

    core_side = set(H_VERTICES) - set(T)
    if not connected(core_side, H_EDGES):
        raise RuntimeError("nonsingleton side is disconnected")
    h_rows = adjacency(H_VERTICES, H_EDGES)
    if any(not (h_rows[terminal] & core_side) for terminal in T):
        raise RuntimeError("nonsingleton side is not T-full")
    k_components = set(components(set(K_VERTICES) - set(T), K_EDGES))
    if k_components != {frozenset(("z",)), frozenset(core_side)}:
        raise RuntimeError("wrong components behind the natural six-cut")

    if E1 & E2 or any(endpoint in BOUNDARY for endpoint in E1 | E2):
        raise RuntimeError("matching edges are not disjoint and remote")
    if edge("v34", "v56") in G_EDGES:
        raise RuntimeError("oriented repair ends are adjacent")


def displayed_colourings():
    answer = []
    for coordinate in range(3):
        colouring = {
            vertex: triple[coordinate] for vertex, triple in TRIPLES.items()
        }
        colouring["z"] = 1
        answer.append(colouring)
    return tuple(answer)


EXPECTED_PARTITIONS = (
    (("a", "b"), ("r", "s"), ("x1",), ("x2",), ("x3",), ("x4",)),
    (("a",), ("b", "s"), ("x1", "x2"), ("r",), ("x3",), ("x4",)),
    (("b",), ("a", "s"), ("x3", "x4"), ("r",), ("x1",), ("x2",)),
)
EXPECTED_SIGNATURES = (
    {edge("z", "a"), edge("z", "b")},
    {edge("z", "a")},
    {edge("z", "b")},
)


def partition_on_boundary(colouring):
    blocks = {}
    for vertex in BOUNDARY:
        blocks.setdefault(colouring[vertex], []).append(vertex)
    return {frozenset(block) for block in blocks.values()}


def verify_colourings():
    colourings = displayed_colourings()
    selected = {edge("z", "a"), edge("z", "b"), E1, E2}
    for index, colouring in enumerate(colourings):
        if not proper(colouring, K_EDGES):
            raise RuntimeError(f"coordinate colouring {index} is not proper on K")
        if not proper(colouring, G_MINUS_Z_EDGES):
            raise RuntimeError(f"coordinate colouring {index} is not proper on G-z")
        signature = {
            pair
            for pair in selected
            if colouring[tuple(pair)[0]] == colouring[tuple(pair)[1]]
        }
        if signature != EXPECTED_SIGNATURES[index]:
            raise RuntimeError(f"wrong selected-edge signature in colouring {index}")
        expected = {frozenset(block) for block in EXPECTED_PARTITIONS[index]}
        if partition_on_boundary(colouring) != expected:
            raise RuntimeError(f"wrong boundary partition in colouring {index}")
        counts = sorted(
            sum(colouring[terminal] == colour for terminal in T)
            for colour in range(1, 7)
        )
        if counts != [0, 1, 1, 1, 1, 2]:
            raise RuntimeError(f"wrong T multiplicities in colouring {index}")

    diagonal = tuple(f"q{i}" for i in range(1, 7))
    if not all(edge(left, right) in H_EDGES for left, right in combinations(diagonal, 2)):
        raise RuntimeError("diagonal vertices do not induce K6")

    h_colourings = anchored_six_colourings(H_VERTICES, H_EDGES)
    if len(h_colourings) != 22:
        raise RuntimeError(f"wrong anchored H colouring count: {len(h_colourings)}")
    if any({colouring[v] for v in BOUNDARY} != set(range(1, 7)) for colouring in h_colourings):
        raise RuntimeError("an H colouring omits a boundary colour")

    gz_colourings = tuple(
        colouring
        for colouring in h_colourings
        if colouring[tuple(E1)[0]] != colouring[tuple(E1)[1]]
        and colouring[tuple(E2)[0]] != colouring[tuple(E2)[1]]
    )
    if len(gz_colourings) != 18:
        raise RuntimeError(f"wrong anchored G-z colouring count: {len(gz_colourings)}")
    if any({colouring[v] for v in BOUNDARY} != set(range(1, 7)) for colouring in gz_colourings):
        raise RuntimeError("a G-z colouring omits a boundary colour")

    # The diagonal K6 fixes all six colour names.  Boundary surjectivity
    # makes a sixth colour unavailable at z, while colour 7 always works.
    seven_colouring = dict(colourings[0])
    seven_colouring["z"] = 7
    if not proper(seven_colouring, G_EDGES):
        raise RuntimeError("displayed seven-colouring is not proper")

    return colourings, h_colourings, gz_colourings


def induced_edges(vertices, edges):
    vertices = set(vertices)
    return {pair for pair in edges if pair <= vertices}


def bag_model_is_valid(bags, roots, vertices, edges):
    if any(root not in bag for root, bag in zip(roots, bags)):
        return False
    if any(left & right for left, right in combinations(bags, 2)):
        return False
    if any(not connected(bag, edges) for bag in bags):
        return False
    return all(
        any(edge(left, right) in edges for left in bags[i] for right in bags[j])
        for i, j in combinations(range(len(bags)), 2)
    )


def all_simple_paths(vertices, edges, source, target):
    rows = adjacency(vertices, edges)
    answer = []

    def search(path):
        if path[-1] == target:
            answer.append(tuple(path))
            return
        for neighbour in sorted(rows[path[-1]] - set(path)):
            search(path + [neighbour])

    search([source])
    return tuple(answer)


def verify_linkage_and_kempe(colourings):
    first = colourings[0]
    beta_vertices = {
        vertex for vertex in H_VERTICES if first[vertex] in {3, 4, 5, 6}
    }
    beta_edges = induced_edges(beta_vertices, G_MINUS_Z_EDGES)
    bags = (
        frozenset(("x1", "q4")),
        frozenset(("x2", "v34")),
        frozenset(("x3", "q6")),
        frozenset(("x4", "v56")),
    )
    if not bag_model_is_valid(
        bags, ("x1", "x2", "x3", "x4"), beta_vertices, beta_edges
    ):
        raise RuntimeError("displayed beta-rooted K4 model is invalid")

    two_colour_vertices = {
        vertex for vertex in H_VERTICES if first[vertex] in {1, 2}
    }
    two_colour_edges = induced_edges(two_colour_vertices, G_MINUS_Z_EDGES)
    expected_edges = {
        edge("a", "r"),
        edge("b", "r"),
        edge("r", "q1"),
        edge("s", "q1"),
        edge("q1", "q2"),
    }
    if two_colour_vertices != {"a", "b", "r", "s", "q1", "q2"}:
        raise RuntimeError("wrong alpha-gamma vertex set")
    if two_colour_edges != expected_edges:
        raise RuntimeError("wrong alpha-gamma edge set")

    traces = []
    for component in components(two_colour_vertices, two_colour_edges):
        traces.append(
            (
                len(component & set(ALPHA_TERMINALS)),
                len(component & set(GAMMA_TERMINALS)),
            )
        )
    if traces != [(2, 2)]:
        raise RuntimeError(f"wrong alpha-gamma component trace: {traces}")

    terminal_paths = []
    for alpha in ALPHA_TERMINALS:
        for gamma in GAMMA_TERMINALS:
            terminal_paths.extend(
                (alpha, gamma, path)
                for path in all_simple_paths(
                    two_colour_vertices, two_colour_edges, alpha, gamma
                )
            )
    if any(
        left[0] != right[0]
        and left[1] != right[1]
        and set(left[2]).isdisjoint(right[2])
        for left, right in combinations(terminal_paths, 2)
    ):
        raise RuntimeError("the forbidden disjoint terminal paths exist")

    # Directly test every simultaneous interchange on every bichromatic
    # component family in each of the three displayed G-z colourings.
    for colouring in colourings:
        for low, high in combinations(range(1, 7), 2):
            vertices = {
                vertex
                for vertex in H_VERTICES
                if colouring[vertex] in {low, high}
            }
            pair_edges = induced_edges(vertices, G_MINUS_Z_EDGES)
            pair_components = components(vertices, pair_edges)
            for mask in range(1 << len(pair_components)):
                swapped = dict(colouring)
                for index, component in enumerate(pair_components):
                    if not (mask & (1 << index)):
                        continue
                    for vertex in component:
                        swapped[vertex] = high if colouring[vertex] == low else low
                if not proper(swapped, G_MINUS_Z_EDGES):
                    raise RuntimeError("Kempe interchange lost properness")
                if {swapped[v] for v in BOUNDARY} != set(range(1, 7)):
                    raise RuntimeError("Kempe interchange lost a boundary colour")


def verify_scope():
    witness = tuple(f"q{i}" for i in range(1, 7)) + ("s",)
    witness_edges = induced_edges(witness, G_EDGES)
    if len(witness_edges) != 20:
        raise RuntimeError("displayed seven vertices do not induce K7-minus")
    missing = {edge(left, right) for left, right in combinations(witness, 2)} - witness_edges
    if missing != {edge("q2", "s")}:
        raise RuntimeError(f"wrong missing edge in K7-minus witness: {missing}")


def main():
    verify_graphs()
    colourings, h_colourings, gz_colourings = verify_colourings()
    verify_linkage_and_kempe(colourings)
    verify_scope()
    print("GREEN natural-six-boundary three-colouring clean-linkage barrier")
    print(
        "graphs: H=(21,129,kappa=8) K=(22,135,kappa=6)",
        "J=(22,137,kappa=8) G=(22,139,kappa=8,chi=7)",
    )
    print(
        "boundary: alpha=3 omega=3",
        f"H_colourings={len(h_colourings)}",
        f"G_minus_z_colourings={len(gz_colourings)}",
        "all_surjective=yes",
    )
    print("signatures: both=za,zb first=za second=zb beta_rooted_K4=yes")
    print(
        "alpha_gamma: trace=(2,2) edges=5 disjoint_terminal_paths=no",
        "arbitrary_Kempe_sequences_safe=yes",
    )
    print("scope: induced_K7_minus=q1,q2,q3,q4,q5,q6,s")


if __name__ == "__main__":
    main()
