#!/usr/bin/env python3
"""Exact finite check for the four-distinct-miss P3 atom.

Run with:
    uv run --with networkx==3.6.1 python \
        active/hc7_k7minus_p3_atom_yuan_verify.py

The target test is K_7^- (at most one missing bag adjacency), not
K_7^vee.  Every model is spanning; this is without loss because every
minor model in a connected graph can be enlarged to a spanning model.
"""

from __future__ import annotations

from functools import lru_cache
import hashlib
import itertools
import json

import networkx as nx


TARGET_ORDER = 7
BOUNDARY_ORDER = 7


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


@lru_cache(maxsize=None)
def restricted_growth_partitions(order: int) -> tuple[tuple[int, ...], ...]:
    """Return partitions into seven nonempty blocks, encoded by bit masks."""
    answer: list[tuple[int, ...]] = []
    blocks: list[list[int]] = []

    def search(position: int) -> None:
        if position == order:
            if len(blocks) == TARGET_ORDER:
                answer.append(
                    tuple(sum(1 << vertex for vertex in block) for block in blocks)
                )
            return
        if len(blocks) + order - position < TARGET_ORDER:
            return
        for block in blocks:
            block.append(position)
            search(position + 1)
            block.pop()
        if len(blocks) < TARGET_ORDER:
            blocks.append([position])
            search(position + 1)
            blocks.pop()

    search(0)
    return tuple(answer)


def adjacency_rows(graph: nx.Graph) -> tuple[int, ...]:
    require(
        tuple(graph) == tuple(range(len(graph))),
        "graph vertices must be consecutive integers",
    )
    rows = [0] * len(graph)
    for left, right in graph.edges:
        rows[left] |= 1 << right
        rows[right] |= 1 << left
    return tuple(rows)


def connected(mask: int, rows: tuple[int, ...]) -> bool:
    reached = mask & -mask
    while True:
        old = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            reached |= rows[bit.bit_length() - 1] & mask
        if reached == old:
            return reached == mask


def validate_k7minus_model(
    graph: nx.Graph, model: tuple[int, ...]
) -> None:
    rows = adjacency_rows(graph)
    require(len(model) == TARGET_ORDER, "model has the wrong number of bags")
    require(all(model), "model contains an empty bag")
    require(
        sum(mask.bit_count() for mask in model) == len(graph),
        "model does not span the graph",
    )
    require(
        not any(
            model[i] & model[j]
            for i, j in itertools.combinations(range(TARGET_ORDER), 2)
        ),
        "model bags overlap",
    )
    require(
        all(connected(mask, rows) for mask in model),
        "model contains a disconnected bag",
    )
    neighbourhoods = []
    for mask in model:
        row = 0
        todo = mask
        while todo:
            bit = todo & -todo
            todo ^= bit
            row |= rows[bit.bit_length() - 1]
        neighbourhoods.append(row)
    missing = sum(
        not bool(neighbourhoods[i] & model[j])
        for i, j in itertools.combinations(range(7), 2)
    )
    require(missing <= 1, "model has more than one missing bag adjacency")


def k7minus_model(graph: nx.Graph) -> tuple[int, ...] | None:
    """Find an exact spanning K_7^- model by exhaustive partition search."""
    rows = adjacency_rows(graph)
    for model in restricted_growth_partitions(len(graph)):
        if not all(connected(mask, rows) for mask in model):
            continue
        neighbourhoods = []
        for mask in model:
            row = 0
            todo = mask
            while todo:
                bit = todo & -todo
                todo ^= bit
                row |= rows[bit.bit_length() - 1]
            neighbourhoods.append(row)
        missing = 0
        for i, j in itertools.combinations(range(7), 2):
            if not neighbourhoods[i] & model[j]:
                missing += 1
                if missing > 1:
                    break
        if missing <= 1:
            validate_k7minus_model(graph, model)
            return model
    return None


def two_packet_quotient(boundary: nx.Graph) -> nx.Graph:
    """Add two nonadjacent vertices complete to the seven-vertex boundary."""
    graph = nx.Graph(boundary)
    graph.add_nodes_from((7, 8))
    for packet in (7, 8):
        graph.add_edges_from((packet, vertex) for vertex in range(7))
    return graph


def p3_quotient(
    boundary: nx.Graph, roles: tuple[int, int, int, int]
) -> nx.Graph:
    """Restore the P3 atom and retain one opposite full component.

    roles=(alpha,beta,gamma,delta): endpoint a misses alpha, endpoint c
    misses gamma, and middle vertex b misses beta and delta.
    Vertices 7,8,9 are a,b,c; vertex 10 is the contracted opposite
    boundary-full component.
    """
    alpha, beta, gamma, delta = roles
    graph = nx.Graph(boundary)
    graph.add_nodes_from((7, 8, 9, 10))
    graph.add_edges_from(((7, 8), (8, 9)))
    for vertex in range(7):
        if vertex != alpha:
            graph.add_edge(7, vertex)
        if vertex not in (beta, delta):
            graph.add_edge(8, vertex)
        if vertex != gamma:
            graph.add_edge(9, vertex)
        graph.add_edge(10, vertex)
    return graph


def triangle_quotient(misses: tuple[frozenset[int], ...]) -> nx.Graph:
    """Add a degree-seven triangle atom and one opposite full component."""
    require(len(misses) == 3, "triangle requires three miss sets")
    graph = nx.empty_graph(11)
    graph.add_edges_from(((7, 8), (8, 9), (7, 9)))
    for index, miss in enumerate(misses):
        for vertex in range(7):
            if vertex not in miss:
                graph.add_edge(7 + index, vertex)
    graph.add_edges_from((10, vertex) for vertex in range(7))
    return graph


def non_good_vertices(
    boundary: nx.Graph, roles: tuple[int, int, int, int]
) -> tuple[int, ...]:
    """Boundary vertices with no incident P3 edge having at most four common neighbours.

    Four is the worst-case density-safe threshold q+3, since q>=1.
    """
    alpha, beta, gamma, delta = roles
    answer = []
    for vertex in range(7):
        degree = boundary.degree(vertex)
        counts = []
        if vertex != alpha:
            counts.append(
                degree
                - int(boundary.has_edge(vertex, alpha))
                + int(vertex not in (beta, delta))
            )
        if vertex not in (beta, delta):
            counts.append(
                degree
                - int(boundary.has_edge(vertex, beta))
                - int(boundary.has_edge(vertex, delta))
                + int(vertex != alpha)
                + int(vertex != gamma)
            )
        if vertex != gamma:
            counts.append(
                degree
                - int(boundary.has_edge(vertex, gamma))
                + int(vertex not in (beta, delta))
            )
        require(bool(counts), "boundary vertex has no neighbour in the path")
        if min(counts) > 4:
            answer.append(vertex)
    return tuple(answer)


def main() -> None:
    require(nx.__version__ == "3.6.1", "unexpected NetworkX version")
    atlas_boundaries = [graph for graph in nx.graph_atlas_g() if len(graph) == 7]
    require(len(atlas_boundaries) == 1044, "unexpected graph-atlas count")
    roles = tuple(itertools.permutations(range(7), 4))
    require(len(roles) == 840, "unexpected role-assignment count")

    surviving_boundaries: list[nx.Graph] = []
    for boundary in atlas_boundaries:
        if k7minus_model(two_packet_quotient(boundary)) is None:
            surviving_boundaries.append(boundary)
    require(
        len(surviving_boundaries) == 700,
        "unexpected two-packet survivor count",
    )

    counts = [0, 0, 0, 0]
    exceptional_records = []
    certificate_records = []
    for boundary in surviving_boundaries:
        graph6 = nx.to_graph6_bytes(boundary, header=False).strip().decode("ascii")
        for role_assignment in roles:
            bad = non_good_vertices(boundary, role_assignment)
            require(len(bad) <= 3, "more than three non-good boundary vertices")
            counts[len(bad)] += 1
            if len(bad) != 3:
                continue
            exceptional_records.append((graph6, role_assignment, bad))
            expanded = p3_quotient(boundary, role_assignment)
            model = k7minus_model(expanded)
            require(model is not None, "expanded P3 case has no K7-minus model")
            validate_k7minus_model(expanded, model)
            certificate_records.append(
                (graph6, role_assignment, bad, tuple(sorted(model)))
            )

    require(
        counts == [451944, 121820, 14128, 108],
        "unexpected non-good distribution",
    )
    require(len(exceptional_records) == 108, "unexpected exceptional-case count")
    require(
        {record[0] for record in exceptional_records} == {"FD^Ww"},
        "unexpected exceptional boundary",
    )
    require(
        len(certificate_records) == 108,
        "not every exceptional case has a certificate",
    )

    # These two target-free quotients delimit the scope of the P3 decoder.
    # They are the exact q=1 triangle-atom miss patterns, up to relabelling.
    triangle_patterns = (
        (frozenset((0,)), frozenset((1,)), frozenset((2, 3))),
        (frozenset((0,)), frozenset((1, 3)), frozenset((2, 3))),
    )
    triangle_graph6 = []
    for misses in triangle_patterns:
        triangle = triangle_quotient(misses)
        require(
            k7minus_model(triangle) is None,
            "diagnostic triangle quotient unexpectedly contains K7-minus",
        )
        triangle_graph6.append(
            nx.to_graph6_bytes(triangle, header=False).strip().decode("ascii")
        )

    exceptional_digest = hashlib.sha256(
        json.dumps(exceptional_records, separators=(",", ":")).encode()
    ).hexdigest()
    certificate_digest = hashlib.sha256(
        json.dumps(certificate_records, separators=(",", ":")).encode()
    ).hexdigest()

    print(f"networkx_version={nx.__version__}")
    print("atlas_boundaries=1044")
    print("role_assignments_per_boundary=840")
    print("two_packet_target_free_boundaries=700")
    print(f"non_good_distribution={tuple(counts)}")
    print("three_non_good_cases=108")
    print("three_non_good_graph6=FD^Ww")
    print("expanded_P3_K7minus_certificates=108")
    print("expanded_P3_survivors=0")
    print(f"triangle_q1_static_survivors={tuple(triangle_graph6)}")
    print(f"exceptional_digest={exceptional_digest}")
    print(f"certificate_digest={certificate_digest}")


if __name__ == "__main__":
    main()
