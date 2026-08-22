#!/usr/bin/env python3
"""Exact minimal-case screen for full-attachment non-clique seven-sums."""

from __future__ import annotations

import hashlib
from itertools import combinations

import networkx as nx
import z3


def has_k7minus(graph):
    vertices = tuple(graph)
    n = len(vertices)
    label = {v: z3.Int(f"lab_{v}") for v in vertices}
    depth = {v: z3.Int(f"dep_{v}") for v in vertices}
    root = {(v, i): z3.Bool(f"root_{v}_{i}")
            for v in vertices for i in range(7)}
    solver = z3.Solver()
    for v in vertices:
        solver.add(-1 <= label[v], label[v] < 7, 0 <= depth[v], depth[v] < n)
    for i in range(7):
        solver.add(z3.PbEq([(root[v, i], 1) for v in vertices], 1))
        for v in vertices:
            solver.add(z3.Implies(root[v, i],
                                  z3.And(label[v] == i, depth[v] == 0)))
            solver.add(z3.Implies(
                root[v, i],
                z3.And([label[w] != i for w in vertices if w < v]),
            ))
            solver.add(z3.Implies(
                z3.And(label[v] == i, z3.Not(root[v, i])),
                z3.And(
                    depth[v] > 0,
                    z3.Or([
                        z3.And(label[w] == i, depth[w] < depth[v])
                        for w in graph[v]
                    ]),
                ),
            ))
    root_index = [z3.Sum([z3.If(root[v, i], v, 0) for v in vertices])
                  for i in range(7)]
    for i in range(6):
        solver.add(root_index[i] < root_index[i + 1])
    contacts = []
    for i, j in combinations(range(7), 2):
        contacts.append(z3.Or([
            z3.Or(z3.And(label[u] == i, label[v] == j),
                  z3.And(label[u] == j, label[v] == i))
            for u, v in graph.edges
        ]))
    solver.add(z3.PbGe([(contact, 1) for contact in contacts], 20))
    assert solver.check() == z3.sat
    model = solver.model()
    bags = tuple(
        tuple(v for v in vertices if model.eval(label[v]).as_long() == i)
        for i in range(7)
    )
    validate(graph, bags)
    return bags


def validate(graph, bags):
    sets = list(map(set, bags))
    assert len(sets) == 7 and all(sets)
    assert sum(map(len, sets)) == len(set().union(*sets))
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in sets)
    assert sum(
        any(graph.has_edge(u, v) for u in sets[i] for v in sets[j])
        for i, j in combinations(range(7), 2)
    ) >= 20


def edge_minimal_k_connected_seven_vertex_graphs(k):
    if k == 0:
        return [nx.empty_graph(7)]
    if k == 1:
        return list(nx.nonisomorphic_trees(7))
    answer = []
    for graph in nx.graph_atlas_g():
        if len(graph) != 7 or nx.node_connectivity(graph) < k:
            continue
        minimal = True
        for edge in tuple(graph.edges):
            smaller = graph.copy()
            smaller.remove_edge(*edge)
            if nx.node_connectivity(smaller) >= k:
                minimal = False
                break
        if minimal:
            answer.append(graph)
    return answer


def trees(order):
    return ([nx.empty_graph(1)] if order == 1
            else list(nx.nonisomorphic_trees(order)))


def joined_graph(separator, left, right):
    graph = nx.disjoint_union_all((separator, left, right))
    graph.add_edges_from(
        (s, v) for s in range(7) for v in range(7, len(graph))
    )
    return graph


def cases(outside_order):
    separator_connectivity = max(0, 7 - outside_order)
    separators = edge_minimal_k_connected_seven_vertex_graphs(
        separator_connectivity
    )
    for separator in separators:
        for left_order in range(1, outside_order // 2 + 1):
            right_order = outside_order - left_order
            left_trees = trees(left_order)
            right_trees = trees(right_order)
            if left_order == right_order:
                pairs = (
                    (left, right)
                    for i, left in enumerate(left_trees)
                    for right in right_trees[i:]
                )
            else:
                pairs = ((left, right) for left in left_trees
                         for right in right_trees)
            for left, right in pairs:
                yield joined_graph(separator, left, right)


def main():
    expected = {4: 10, 5: 18, 6: 66, 7: 11}
    digest = hashlib.sha256()
    for outside_order in range(4, 8):
        count = 0
        for graph in cases(outside_order):
            assert nx.node_connectivity(graph) == 7
            bags = has_k7minus(graph)
            graph6 = nx.to_graph6_bytes(graph, header=False).strip()
            digest.update(graph6 + repr(bags).encode("ascii"))
            count += 1
        assert count == expected[outside_order]
        print("outside", outside_order, "cases", count, "positive", count)
    print("certificate_digest", digest.hexdigest())


if __name__ == "__main__":
    main()
