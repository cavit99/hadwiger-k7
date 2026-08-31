#!/usr/bin/env python3
"""Exact bounded falsification of the proposed labelled K4,4 capstone.

For every unlabeled 3-connected graph C of order 4 through 7 in the
NetworkX graph atlas, assign an arbitrary subset of eight labels to every
vertex.  Thus the exact assignment universe for a fixed order n is the
full set of 8-by-n Boolean incidence matrices, of cardinality 2^(8n).

Write w(X) for the number of labels used on X.  The solver asks for an
assignment satisfying

    |N_C(X)| + w(X) >= 7                         (all nonempty X <= V(C))

while simultaneously avoiding:

  A. three disjoint, connected, pairwise-touching bags of weight at least 4;
  B. a spanning four-bag K4 model, every bag of weight at least 3;
  D. a six-bag K6-minus model, every bag of positive weight.

Outcome D is the useful new direct-target certificate: the entire connected
literal K4,4 core is a seventh bag, giving 14+6=20 quotient contacts.

UNSAT is a bounded result only.  Z3 is the decisive unsatisfiability engine.
If SAT ever occurs, a separate concrete bit-mask evaluator below validates
the returned assignment before it is reported as a counterexample.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations

import networkx as nx
import z3


def bit_graph(graph: nx.Graph) -> tuple[int, ...]:
    return tuple(
        sum(1 << neighbour for neighbour in graph.neighbors(vertex))
        for vertex in range(len(graph))
    )


def connected(graph: tuple[int, ...], mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        new = graph[bit.bit_length() - 1] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def three_connected(graph: tuple[int, ...]) -> bool:
    n = len(graph)
    if n < 4:
        return False
    full = (1 << n) - 1
    for deleted_size in range(3):
        for deleted in combinations(range(n), deleted_size):
            left = full ^ sum(1 << vertex for vertex in deleted)
            if not connected(graph, left):
                return False
    return True


def touches(graph: tuple[int, ...], left: int, right: int) -> bool:
    return any(
        graph[vertex] & right
        for vertex in range(len(graph))
        if left >> vertex & 1
    )


def boundary_size(graph: tuple[int, ...], mask: int) -> int:
    boundary = 0
    for vertex in range(len(graph)):
        if mask >> vertex & 1:
            boundary |= graph[vertex]
    return (boundary & ~mask).bit_count()


def connected_masks(graph: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        mask
        for mask in range(1, 1 << len(graph))
        if connected(graph, mask)
    )


def triangle_models(graph: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]:
    masks = connected_masks(graph)
    answer = []
    for i, left in enumerate(masks):
        for j in range(i + 1, len(masks)):
            middle = masks[j]
            if left & middle or not touches(graph, left, middle):
                continue
            for right in masks[j + 1 :]:
                if (left | middle) & right:
                    continue
                if touches(graph, left, right) and touches(graph, middle, right):
                    answer.append((left, middle, right))
    return tuple(answer)


def set_partitions(n: int, number: int):
    """Every unordered partition of all n vertices into number blocks."""
    blocks: list[int] = []

    def search(vertex: int, used: int):
        if vertex == n:
            if used == number:
                yield tuple(blocks)
            return
        for index in range(min(used + 1, number)):
            if index == used:
                blocks.append(0)
            blocks[index] |= 1 << vertex
            yield from search(vertex + 1, max(used, index + 1))
            blocks[index] ^= 1 << vertex
            if index == used:
                blocks.pop()

    yield from search(0, 0)


def spanning_k4_models(graph: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    answer = []
    for bags in set_partitions(len(graph), 4):
        if not all(connected(graph, bag) for bag in bags):
            continue
        if all(touches(graph, a, b) for a, b in combinations(bags, 2)):
            answer.append(bags)
    return tuple(answer)


def quotient_edges(graph: tuple[int, ...], bags: tuple[int, ...]) -> int:
    return sum(touches(graph, bags[i], bags[j]) for i, j in combinations(range(6), 2))


def k6minus_models(graph: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Every six-bag model for n <= 7, with unused vertices allowed."""
    n = len(graph)
    answer = []
    if n == 6:
        bags = tuple(1 << vertex for vertex in range(6))
        if quotient_edges(graph, bags) >= 14:
            answer.append(bags)
    elif n == 7:
        full = (1 << 7) - 1
        for unused in range(7):
            bags = tuple(1 << vertex for vertex in range(7) if vertex != unused)
            if quotient_edges(graph, bags) >= 14:
                answer.append(bags)
        for left, right in combinations(range(7), 2):
            if not (graph[left] >> right & 1):
                continue
            pair = (1 << left) | (1 << right)
            bags = (pair,) + tuple(
                1 << vertex
                for vertex in range(7)
                if not (pair >> vertex & 1)
            )
            if quotient_edges(graph, bags) >= 14:
                answer.append(bags)
    return tuple(answer)


def union_at_least(
    incidence: list[list[z3.BoolRef]], mask: int, threshold: int
) -> z3.BoolRef:
    n = len(incidence)
    return z3.PbGe(
        [
            (
                z3.Or(
                    [
                        incidence[vertex][label]
                        for vertex in range(n)
                        if mask >> vertex & 1
                    ]
                ),
                1,
            )
            for label in range(8)
        ],
        threshold,
    )


def weight(label_masks: tuple[int, ...], mask: int) -> int:
    labels = 0
    for vertex, vertex_labels in enumerate(label_masks):
        if mask >> vertex & 1:
            labels |= vertex_labels
    return labels.bit_count()


def validate_counterexample(
    graph: tuple[int, ...],
    labels: tuple[int, ...],
    triangles: tuple[tuple[int, int, int], ...],
    k4_models: tuple[tuple[int, ...], ...],
    k6_models: tuple[tuple[int, ...], ...],
) -> None:
    full = (1 << len(graph)) - 1
    assert all(
        boundary_size(graph, mask) + weight(labels, mask) >= 7
        for mask in range(1, full + 1)
    )
    assert not any(
        all(weight(labels, bag) >= 4 for bag in model)
        for model in triangles
    )
    assert not any(
        all(weight(labels, bag) >= 3 for bag in model)
        for model in k4_models
    )
    assert not any(
        all(weight(labels, bag) >= 1 for bag in model)
        for model in k6_models
    )


def solve(graph: tuple[int, ...]):
    n = len(graph)
    triangles = triangle_models(graph)
    k4_models = spanning_k4_models(graph)
    k6_models = k6minus_models(graph)
    incidence = [
        [z3.Bool(f"edge_{vertex}_{label}") for label in range(8)]
        for vertex in range(n)
    ]
    solver = z3.Solver()
    full = (1 << n) - 1
    for mask in range(1, full + 1):
        solver.add(
            union_at_least(
                incidence, mask, max(0, 7 - boundary_size(graph, mask))
            )
        )
    for model in triangles:
        solver.add(
            z3.Not(
                z3.And([union_at_least(incidence, bag, 4) for bag in model])
            )
        )
    for model in k4_models:
        solver.add(
            z3.Not(
                z3.And([union_at_least(incidence, bag, 3) for bag in model])
            )
        )
    for model in k6_models:
        solver.add(
            z3.Not(
                z3.And([union_at_least(incidence, bag, 1) for bag in model])
            )
        )
    status = solver.check()
    labels = None
    if status == z3.sat:
        model = solver.model()
        labels = tuple(
            sum(
                1 << label
                for label in range(8)
                if z3.is_true(model.eval(incidence[vertex][label]))
            )
            for vertex in range(n)
        )
        validate_counterexample(graph, labels, triangles, k4_models, k6_models)
    return status, labels, (len(triangles), len(k4_models), len(k6_models))


def main() -> None:
    by_order: dict[int, int] = {}
    totals: dict[int, list[int]] = {}
    records = []
    for atlas_graph in nx.graph_atlas_g():
        n = len(atlas_graph)
        if not 4 <= n <= 7:
            continue
        graph = bit_graph(atlas_graph)
        if not three_connected(graph):
            continue
        by_order[n] = by_order.get(n, 0) + 1
        status, labels, counts = solve(graph)
        totals.setdefault(n, [0, 0, 0])
        for index, count in enumerate(counts):
            totals[n][index] += count
        graph6 = nx.to_graph6_bytes(atlas_graph, header=False).decode().strip()
        records.append((n, graph6, counts, str(status)))
        if labels is not None:
            print("COUNTEREXAMPLE", n, graph6, [hex(mask) for mask in labels])
            raise SystemExit(1)

    assert by_order == {4: 1, 5: 3, 6: 17, 7: 136}
    assert all(record[-1] == "unsat" for record in records)
    digest = sha256(repr(records).encode()).hexdigest()
    print("PASS labelled portal trichotomy through order seven")
    print("three_connected_graphs", by_order, "total", len(records))
    print("assignment_universe_per_graph 2^(8n)")
    print("model_totals_by_order", totals)
    print("all_instances_unsat", len(records))
    print("records_sha256", digest)


if __name__ == "__main__":
    main()
