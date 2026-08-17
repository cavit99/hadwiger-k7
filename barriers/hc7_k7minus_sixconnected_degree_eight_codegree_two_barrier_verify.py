#!/usr/bin/env python3
"""Verify the six-connected degree-eight codegree-two barrier.

The graph is the cone over a flipped frequency-two icosahedral
triangulation.  The checker uses only the Python standard library.  It
reconstructs the triangulation, checks its triangular sphere certificate,
exhausts every vertex deletion of order at most four, and verifies all
degrees and codegrees in the cone.

Absence of a K_7^- minor is the short planar argument in the accompanying
note: deleting the cone apex leaves a planar graph, whereas deleting the
apex-containing bag from a target model leaves a non-planar K_6 or K_6^-
minor.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations


BASE_EDGES = (
    (0, 1),
    (0, 5),
    (0, 7),
    (0, 8),
    (0, 11),
    (1, 2),
    (1, 5),
    (1, 6),
    (1, 8),
    (2, 3),
    (2, 6),
    (2, 8),
    (2, 9),
    (3, 4),
    (3, 6),
    (3, 9),
    (3, 10),
    (4, 5),
    (4, 6),
    (4, 10),
    (4, 11),
    (5, 6),
    (5, 11),
    (7, 8),
    (7, 9),
    (7, 10),
    (7, 11),
    (8, 9),
    (9, 10),
    (10, 11),
)

BASE_FACES = tuple(
    tuple(map(int, face.split(",")))
    for face in (
        "0,8,1 0,7,8 0,11,7 0,5,11 0,1,5 "
        "1,2,6 1,8,2 1,6,5 2,3,6 2,9,3 "
        "2,8,9 3,4,6 3,10,4 3,9,10 4,5,6 "
        "4,11,5 4,10,11 7,9,8 7,10,9 7,11,10"
    ).split()
)


def edge(left: int, right: int) -> tuple[int, int]:
    if left == right:
        raise RuntimeError("loops are not allowed")
    return (left, right) if left < right else (right, left)


def add_edge(adjacency: list[set[int]], left: int, right: int) -> None:
    adjacency[left].add(right)
    adjacency[right].add(left)


def remove_edge(adjacency: list[set[int]], left: int, right: int) -> None:
    adjacency[left].remove(right)
    adjacency[right].remove(left)


def edges(adjacency: list[set[int]]) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left in range(len(adjacency))
        for right in sorted(adjacency[left])
        if left < right
    )


def frequency_two_triangulation() -> tuple[list[set[int]], list[frozenset[int]]]:
    """Return the subdivided icosahedron before the diagonal flip."""

    if len(BASE_EDGES) != 30 or len({edge(*base_edge) for base_edge in BASE_EDGES}) != 30:
        raise RuntimeError("malformed icosahedron edge list")

    midpoint = {edge(*base_edge): 12 + index for index, base_edge in enumerate(BASE_EDGES)}
    adjacency = [set() for _ in range(42)]
    for (left, right), middle in midpoint.items():
        add_edge(adjacency, left, middle)
        add_edge(adjacency, middle, right)

    faces: list[frozenset[int]] = []
    for first, second, third in BASE_FACES:
        first_second = midpoint[edge(first, second)]
        second_third = midpoint[edge(second, third)]
        third_first = midpoint[edge(third, first)]
        add_edge(adjacency, first_second, second_third)
        add_edge(adjacency, second_third, third_first)
        add_edge(adjacency, third_first, first_second)
        faces.extend(
            (
                frozenset((first, first_second, third_first)),
                frozenset((second, second_third, first_second)),
                frozenset((third, third_first, second_third)),
                frozenset((first_second, second_third, third_first)),
            )
        )
    return adjacency, faces


def flipped_triangulation() -> tuple[list[set[int]], tuple[frozenset[int], ...]]:
    adjacency, face_list = frequency_two_triangulation()

    # In the subdivided old face 0,1,5, edge 13--18 has opposite vertices
    # 12 and 5.  Replace that diagonal by 12--5.
    remove_edge(adjacency, 13, 18)
    add_edge(adjacency, 12, 5)
    old_faces = {frozenset((5, 13, 18)), frozenset((12, 13, 18))}
    if not old_faces <= set(face_list):
        raise RuntimeError("the diagonal-flip faces were not found")
    faces = [face for face in face_list if face not in old_faces]
    faces.extend((frozenset((5, 12, 13)), frozenset((5, 12, 18))))
    return adjacency, tuple(faces)


def connected_after_deletion(
    adjacency: list[set[int]], deleted: frozenset[int]
) -> bool:
    remaining = set(range(len(adjacency))) - deleted
    if not remaining:
        return True
    reached = {min(remaining)}
    frontier = set(reached)
    while frontier:
        vertex = frontier.pop()
        new = (adjacency[vertex] & remaining) - reached
        reached.update(new)
        frontier.update(new)
    return reached == remaining


def verify_sphere_certificate(
    adjacency: list[set[int]], faces: tuple[frozenset[int], ...]
) -> None:
    graph_edges = set(edges(adjacency))
    if len(adjacency) != 42 or len(graph_edges) != 120 or len(faces) != 80:
        raise RuntimeError("unexpected triangulation parameters")
    if len(set(faces)) != len(faces) or any(len(face) != 3 for face in faces):
        raise RuntimeError("malformed triangular faces")
    face_edge_counts: Counter[tuple[int, int]] = Counter()
    for face in faces:
        for left, right in combinations(sorted(face), 2):
            face_edge_counts[edge(left, right)] += 1
    if set(face_edge_counts) != graph_edges:
        raise RuntimeError("face and graph edge sets differ")
    if set(face_edge_counts.values()) != {2}:
        raise RuntimeError("an edge is not incident with two triangular faces")
    for vertex, neighbours in enumerate(adjacency):
        link_adjacency = {neighbour: set() for neighbour in neighbours}
        for face in faces:
            if vertex not in face:
                continue
            left, right = sorted(face - {vertex})
            link_adjacency[left].add(right)
            link_adjacency[right].add(left)
        if any(len(link_adjacency[neighbour]) != 2 for neighbour in neighbours):
            raise RuntimeError(f"the link of vertex {vertex} is not two-regular")
        reached = {min(neighbours)}
        frontier = set(reached)
        while frontier:
            neighbour = frontier.pop()
            new = link_adjacency[neighbour] - reached
            reached.update(new)
            frontier.update(new)
        if reached != neighbours:
            raise RuntimeError(f"the link of vertex {vertex} is disconnected")
    if len(adjacency) - len(graph_edges) + len(faces) != 2:
        raise RuntimeError("the triangular surface does not have Euler value two")


def cone(base: list[set[int]]) -> list[set[int]]:
    answer = [set(neighbours) for neighbours in base] + [set()]
    apex = len(base)
    for vertex in range(apex):
        add_edge(answer, apex, vertex)
    return answer


def main() -> None:
    base, faces = flipped_triangulation()
    verify_sphere_certificate(base, faces)

    checked = 0
    for cut_order in range(5):
        for cut in combinations(range(42), cut_order):
            checked += 1
            if not connected_after_deletion(base, frozenset(cut)):
                raise RuntimeError(f"cut of order at most four: {cut}")

    base_degrees = Counter(map(len, base))
    if base_degrees != Counter({5: 13, 6: 28, 7: 1}):
        raise RuntimeError(f"unexpected base degrees: {base_degrees}")
    if len(base[12]) != 7:
        raise RuntimeError("the nominated base vertex does not have degree seven")
    if connected_after_deletion(base, frozenset(base[13])):
        raise RuntimeError("the displayed five-cut does not isolate vertex 13")

    host = cone(base)
    host_edges = edges(host)
    if len(host) != 43 or len(host_edges) != 162:
        raise RuntimeError("unexpected cone parameters")
    if len(host[12]) != 8:
        raise RuntimeError("the nominated cone vertex does not have degree eight")

    codegrees = tuple(
        len(host[12].intersection(host[neighbour]))
        for neighbour in sorted(host[12])
    )
    if sorted(codegrees) != [3, 3, 3, 3, 3, 3, 3, 7]:
        raise RuntimeError(f"unexpected incident codegrees: {codegrees}")

    edge_payload = " ".join(f"{left}-{right}" for left, right in host_edges)
    digest = sha256(edge_payload.encode()).hexdigest()
    print("GREEN six-connected degree-eight codegree-two barrier")
    print("base: n=42 m=120 kappa=5 degree_profile=5^13,6^28,7^1")
    print(f"base_deletion_sets_checked={checked}")
    print("host: n=43 m=162=4n-10 kappa=6")
    print("centre=12 degree=8 incident_codegrees=3,3,3,3,3,3,3,7")
    print("target_exclusion=cone_over_planar_triangulation")
    print(f"host_edge_digest={digest}")


if __name__ == "__main__":
    main()
