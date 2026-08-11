#!/usr/bin/env python3
"""Probe simultaneous rainbow-portal/Kempe concentration patterns.

Each of five alpha-coloured centres chooses one transversal triangle in
K_{2,2,2}; the three coordinates are the movable colour classes.  A
coordinate fibre of order one would be a forbidden singleton Kempe
component.  We classify the surviving five-row multisets and test the
literal incidence graph for a K7-minus-edge minor.

This is a finite diagnostic for the abstract palette residue only.  It
does not encode either shore or the critical-host colouring quantifiers.
"""

from __future__ import annotations

import itertools

import z3


CODES = tuple(itertools.product(range(2), repeat=3))
PORTALS = tuple((coordinate, bit) for coordinate in range(3) for bit in range(2))
CENTRES = tuple(("z", index) for index in range(5))


def incidence_graph(
    rows: tuple[tuple[int, int, int], ...]
) -> dict[object, set[object]]:
    graph = {vertex: set() for vertex in PORTALS + CENTRES}
    def add_edge(left: object, right: object) -> None:
        graph[left].add(right)
        graph[right].add(left)

    for left, right in itertools.combinations(PORTALS, 2):
        if left[0] != right[0]:
            add_edge(left, right)
    for centre, row in zip(CENTRES, rows, strict=True):
        for coordinate, bit in enumerate(row):
            add_edge(centre, (coordinate, bit))
    return graph


def symmetric_two_shore_graph(
    rows: tuple[tuple[int, int, int], ...]
) -> dict[object, set[object]]:
    shore_vertices = tuple(
        (shore, coordinate, bit)
        for shore in ("A", "B")
        for coordinate in range(3)
        for bit in range(2)
    )
    poles = ("p", "q")
    graph = {vertex: set() for vertex in shore_vertices + CENTRES + poles}

    def add_edge(left: object, right: object) -> None:
        graph[left].add(right)
        graph[right].add(left)

    for shore in ("A", "B"):
        vertices = tuple(vertex for vertex in shore_vertices if vertex[0] == shore)
        for left, right in itertools.combinations(vertices, 2):
            if left[1] != right[1]:
                add_edge(left, right)
    for centre, row in zip(CENTRES, rows, strict=True):
        for shore in ("A", "B"):
            for coordinate, bit in enumerate(row):
                add_edge(centre, (shore, coordinate, bit))
        for pole in poles:
            add_edge(centre, pole)
    return graph


def cycle_shore_graph(
    rows: tuple[tuple[int, int, int], ...],
    a_portals: tuple[tuple[int, int, int], ...],
) -> dict[object, set[object]]:
    b_vertices = tuple(("B", coordinate, bit) for coordinate in range(3) for bit in range(2))
    a_vertices = tuple(("A", index) for index in range(5))
    poles = ("p", "q")
    graph = {vertex: set() for vertex in b_vertices + a_vertices + CENTRES + poles}

    def add_edge(left: object, right: object) -> None:
        graph[left].add(right)
        graph[right].add(left)

    for left, right in itertools.combinations(b_vertices, 2):
        if left[1] != right[1]:
            add_edge(left, right)
    for index in range(5):
        add_edge(("A", index), ("A", (index + 1) % 5))
    for centre, row, portal in zip(CENTRES, rows, a_portals, strict=True):
        for coordinate, bit in enumerate(row):
            add_edge(centre, ("B", coordinate, bit))
        for index in portal:
            add_edge(centre, ("A", index))
        for pole in poles:
            add_edge(centre, pole)
    for pole in poles:
        for vertex in a_vertices:
            add_edge(pole, vertex)
    add_edge("p", ("B", 0, 0))
    add_edge("q", ("B", 0, 1))
    return graph


def clique_number(graph: dict[object, set[object]]) -> int:
    vertices = tuple(graph)
    answer = 0
    for order in range(1, len(vertices) + 1):
        if any(
            all(right in graph[left] for left, right in itertools.combinations(candidate, 2))
            for candidate in itertools.combinations(vertices, order)
        ):
            answer = order
        else:
            break
    return answer


def has_k7_minus_minor(graph: dict[object, set[object]]) -> bool:
    vertices = tuple(graph)
    labels = range(7)
    solver = z3.Solver()
    assigned = {(v, i): z3.Bool(f"x_{vertices.index(v)}_{i}") for v in vertices for i in labels}
    root = {(v, i): z3.Bool(f"r_{vertices.index(v)}_{i}") for v in vertices for i in labels}
    rank = {(v, i): z3.Int(f"d_{vertices.index(v)}_{i}") for v in vertices for i in labels}

    for vertex in vertices:
        solver.add(z3.PbLe([(assigned[vertex, i], 1) for i in labels], 1))
    for label in labels:
        solver.add(z3.PbEq([(root[vertex, label], 1) for vertex in vertices], 1))
        for vertex in vertices:
            solver.add(z3.Implies(root[vertex, label], assigned[vertex, label]))
            solver.add(rank[vertex, label] >= 0, rank[vertex, label] < len(vertices))
            solver.add(z3.Implies(root[vertex, label], rank[vertex, label] == 0))
            descent = [
                z3.And(assigned[neighbour, label], rank[neighbour, label] < rank[vertex, label])
                for neighbour in graph[vertex]
            ]
            solver.add(
                z3.Implies(
                    z3.And(assigned[vertex, label], z3.Not(root[vertex, label])),
                    z3.And(rank[vertex, label] > 0, z3.Or(descent)),
                )
            )

    misses = []
    for left, right in itertools.combinations(labels, 2):
        missing = z3.Bool(f"m_{left}_{right}")
        contacts = []
        for u in vertices:
            for v in graph[u]:
                if vertices.index(u) >= vertices.index(v):
                    continue
                contacts.extend(
                    (
                        z3.And(assigned[u, left], assigned[v, right]),
                        z3.And(assigned[u, right], assigned[v, left]),
                    )
                )
        solver.add(z3.Or(missing, *contacts))
        misses.append(missing)
    solver.add(z3.PbLe([(missing, 1) for missing in misses], 1))
    return solver.check() == z3.sat


def canonical(rows: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    images = []
    for coordinate_order in itertools.permutations(range(3)):
        for flips in itertools.product(range(2), repeat=3):
            image = tuple(
                sorted(
                    tuple(row[coordinate_order[index]] ^ flips[index] for index in range(3))
                    for row in rows
                )
            )
            images.append(image)
    return min(images)


def main() -> None:
    forms = set()
    for rows in itertools.combinations_with_replacement(CODES, 5):
        fibre_sizes = [
            sum(row[coordinate] == bit for row in rows)
            for coordinate in range(3)
            for bit in range(2)
        ]
        if 1 in fibre_sizes:
            continue
        support = sum(any(row[coordinate] == bit for row in rows) for coordinate, bit in PORTALS)
        if support < 5:
            continue
        forms.add(canonical(rows))

    target_free = []
    for rows in sorted(forms):
        if not has_k7_minus_minor(incidence_graph(rows)):
            target_free.append(rows)
    print(
        "SUMMARY",
        {"forms": len(forms), "target_free": len(target_free)},
    )
    for rows in target_free:
        print("TARGET_FREE", rows)
    symmetric_survivors = []
    for rows in target_free:
        graph = symmetric_two_shore_graph(rows)
        if clique_number(graph) < 5 and not has_k7_minus_minor(graph):
            symmetric_survivors.append(rows)
    print("SYMMETRIC_TWO_SHORE_SURVIVORS", len(symmetric_survivors))
    for rows in symmetric_survivors:
        print("TWO_SHORE_TARGET_FREE", rows)

    triples = tuple(itertools.combinations(range(5), 3))
    for rows in target_free:
        for a_portals in itertools.combinations_with_replacement(triples, 5):
            if set().union(*(set(portal) for portal in a_portals)) != set(range(5)):
                continue
            graph = cycle_shore_graph(rows, a_portals)
            if clique_number(graph) >= 5:
                continue
            if not has_k7_minus_minor(graph):
                print("CYCLE_SHORE_TARGET_FREE", rows, a_portals)
                return
        # One B-incidence form is enough for this diagnostic search.
        break
    print("NO_CYCLE_SHORE_TARGET_FREE")


if __name__ == "__main__":
    main()
