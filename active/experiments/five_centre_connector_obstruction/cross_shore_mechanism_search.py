#!/usr/bin/env python3
"""Search the exact polarized shore mechanism for a target-free example."""

from __future__ import annotations

import itertools
import random

import networkx as nx
import z3


Z = tuple(f"z{i}" for i in range(5))
P = "p"
Q = "q"


def clique_number(graph: nx.Graph) -> int:
    return max(map(len, nx.find_cliques(graph)), default=0)


def alpha(graph: nx.Graph) -> int:
    return clique_number(nx.complement(graph))


def shore_a() -> nx.Graph:
    graph = nx.relabel_nodes(nx.wheel_graph(6), lambda vertex: f"a{vertex}")
    return graph


def shore_b() -> nx.Graph:
    graph = nx.relabel_nodes(
        nx.mycielskian(nx.complete_graph(4)), lambda vertex: f"b{vertex}"
    )
    return graph


def k7_minus_model(
    graph: nx.Graph, timeout_ms: int = 30_000
) -> dict[str, object] | bool | None:
    """Return a K7-minus-edge model, False if absent, or None on timeout."""
    vertices = tuple(graph)
    labels = range(7)
    solver = z3.Solver()
    solver.set(timeout=timeout_ms)
    assigned = {(v, i): z3.Bool(f"x_{v}_{i}") for v in vertices for i in labels}
    root = {(v, i): z3.Bool(f"r_{v}_{i}") for v in vertices for i in labels}
    rank = {(v, i): z3.Int(f"d_{v}_{i}") for v in vertices for i in labels}

    for v in vertices:
        solver.add(z3.PbLe([(assigned[v, i], 1) for i in labels], 1))
    for i in labels:
        solver.add(z3.PbEq([(root[v, i], 1) for v in vertices], 1))
        for v in vertices:
            solver.add(z3.Implies(root[v, i], assigned[v, i]))
            solver.add(rank[v, i] >= 0, rank[v, i] < len(vertices))
            solver.add(z3.Implies(root[v, i], rank[v, i] == 0))
            descent = [
                z3.And(assigned[u, i], rank[u, i] < rank[v, i])
                for u in graph.neighbors(v)
            ]
            solver.add(
                z3.Implies(
                    z3.And(assigned[v, i], z3.Not(root[v, i])),
                    z3.And(rank[v, i] > 0, z3.Or(descent)),
                )
            )

    missing = {}
    for i, j in itertools.combinations(labels, 2):
        missing[i, j] = z3.Bool(f"missing_{i}_{j}")
        contacts = []
        for u, v in graph.edges():
            contacts.append(z3.And(assigned[u, i], assigned[v, j]))
            contacts.append(z3.And(assigned[u, j], assigned[v, i]))
        solver.add(z3.Or(missing[i, j], *contacts))
    solver.add(z3.PbEq([(variable, 1) for variable in missing.values()], 1))

    verdict = solver.check()
    if verdict == z3.unknown:
        return None
    if verdict != z3.sat:
        return False
    model = solver.model()
    branch_sets = {
        i: sorted(v for v in vertices if z3.is_true(model.eval(assigned[v, i])))
        for i in labels
    }
    missed_pair = next(
        (i, j) for (i, j), variable in missing.items() if z3.is_true(model.eval(variable))
    )
    return {"branch_sets": branch_sets, "allowed_missing_pair": missed_pair}


def build_graph(
    a_sets: dict[str, set[str]],
    b_sets: dict[str, set[str]],
    p_b: set[str],
    q_b: set[str],
) -> nx.Graph:
    a_graph = shore_a()
    b_graph = shore_b()
    graph = nx.compose(a_graph, b_graph)
    graph.add_nodes_from(Z + (P, Q))
    graph.add_edges_from((z, v) for z in Z for v in a_sets[z] | b_sets[z])
    graph.add_edges_from((pole, v) for pole in (P, Q) for v in a_graph)
    graph.add_edges_from((P, v) for v in p_b)
    graph.add_edges_from((Q, v) for v in q_b)
    graph.add_edges_from((pole, z) for pole in (P, Q) for z in Z[:2])
    return graph


def candidates() -> tuple[list[frozenset[str]], ...]:
    a_graph = shore_a()
    b_graph = shore_b()
    a_three = [
        frozenset(vertices)
        for vertices in itertools.combinations(a_graph, 3)
        if alpha(a_graph.subgraph(vertices)) == 2
        and clique_number(a_graph.subgraph(vertices)) <= 2
    ]
    a_triangles = [frozenset(cycle) for cycle in nx.simple_cycles(a_graph, length_bound=3) if len(cycle) == 3]
    a_triangles = sorted(set(a_triangles), key=sorted)
    b_triangles = []
    for vertices in itertools.combinations(b_graph, 3):
        vertex_set = frozenset(vertices)
        if clique_number(b_graph.subgraph(vertices)) != 3:
            continue
        if not vertex_set & {"b0", "b4"} or not vertex_set & {"b1", "b5"}:
            continue
        b_triangles.append(vertex_set)
    b_fives = [
        frozenset(vertices)
        for vertices in itertools.combinations(b_graph, 5)
        if alpha(b_graph.subgraph(vertices)) <= 2
        and clique_number(b_graph.subgraph(vertices)) <= 3
    ]
    return a_three, a_triangles, b_triangles, b_fives


def main() -> None:
    rng = random.Random(20260810)
    a_three, a_triangles, b_triangles, b_fives = candidates()
    structural = 0
    for trial in range(200_000):
        p_b = {"b0", "b4"}
        q_b = {"b1", "b5"}
        for vertex in ("b2", "b3", "b6", "b7", "b8"):
            choice = rng.randrange(3)
            if choice != 1:
                p_b.add(vertex)
            if choice != 0:
                q_b.add(vertex)
        if len(p_b) + len(q_b) > 12:
            continue
        a_sets = {
            "z0": set(rng.choice(a_three)),
            "z1": set(rng.choice(a_three)),
            "z2": set(rng.choice(a_triangles)),
            "z3": set(rng.choice(a_triangles)),
            "z4": set(rng.choice(a_triangles)),
        }
        b_sets = {
            "z0": set(rng.choice(b_triangles)),
            "z1": set(rng.choice(b_triangles)),
            "z2": set(rng.choice(b_fives)),
            "z3": set(rng.choice(b_fives)),
            "z4": set(rng.choice(b_fives)),
        }
        if set().union(*a_sets.values()) != set(shore_a()):
            continue
        if set().union(*b_sets.values()) != set(shore_b()):
            continue
        graph = build_graph(a_sets, b_sets, p_b, q_b)
        if any(graph.degree(z) != 8 for z in Z):
            continue
        if any(alpha(graph.subgraph(graph.neighbors(z))) != 3 for z in Z):
            continue
        if clique_number(graph) >= 5:
            continue
        if nx.node_connectivity(graph) < 7:
            continue
        structural += 1
        target = k7_minus_model(graph)
        print(
            "CANDIDATE",
            {
                "trial": trial,
                "structural": structural,
                "connectivity": nx.node_connectivity(graph),
                "edges": graph.number_of_edges(),
                "a_sets": {z: sorted(a_sets[z]) for z in Z},
                "b_sets": {z: sorted(b_sets[z]) for z in Z},
                "p_b": sorted(p_b),
                "q_b": sorted(q_b),
                "k7_minus_minor": target,
            },
        )
        if target is False:
            return
        if structural >= 20:
            return
    print("NO_STRUCTURAL_CANDIDATE", {"trials": 200_000, "structural": structural})


if __name__ == "__main__":
    main()
