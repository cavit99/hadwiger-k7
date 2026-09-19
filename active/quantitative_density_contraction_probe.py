#!/usr/bin/env python3
"""Finite exploratory density-minor probe; no universal conclusion.

Run: uv run python3 active/quantitative_density_contraction_probe.py
Add --summary to print only the CI summary after running all checks.
Expected: six successful models and two unsuccessful negative controls.
The negative controls lack density surplus; the positive control already
has the required ratio. Failure to find a model is not a certificate of minor
exclusion. NetworkX is pinned; all choices and random graph seeds are fixed.
"""

import argparse
from fractions import Fraction
from hashlib import sha256
import json

import networkx as nx


def alpha(graph):
    """Exact existing repository encoding: cliques in the complement."""
    return max((len(c) for c in nx.find_cliques(nx.complement(graph))), default=0)


def quotient(original, bags):
    graph = nx.Graph()
    graph.add_nodes_from(range(len(bags)))
    owner = {v: i for i, bag in enumerate(bags) for v in bag}
    for u, v in original.edges:
        if u in owner and v in owner and owner[u] != owner[v]:
            graph.add_edge(owner[u], owner[v])
    return graph


def verify(original, bags, graph):
    """Check connectivity, ownership and every original contact separately."""
    assert bags and all(bag and nx.is_connected(original.subgraph(bag)) for bag in bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    assert set(graph) == set(range(len(bags)))
    for i, left in enumerate(bags):
        for j in range(i + 1, len(bags)):
            contact = any(original.has_edge(u, v) for u in left for v in bags[j])
            assert graph.has_edge(i, j) == contact


def probe(original, r):
    bags = [{v} for v in original]
    graph = quotient(original, bags)
    best = Fraction(len(graph), alpha(graph))
    best_bags = [set(bag) for bag in bags]
    contractions = 0
    while graph:
        # Inspect induced subgraphs along this one deletion sequence only.
        smaller = graph.copy()
        while smaller:
            ratio = Fraction(len(smaller), alpha(smaller))
            if ratio > best:
                best = ratio
                best_bags = [set(bags[v]) for v in sorted(smaller)]
            if best > r:
                model = quotient(original, best_bags)
                verify(original, best_bags, model)
                return best_bags, contractions
            v = min(smaller, key=lambda x: (smaller.degree(x), x))
            smaller.remove_node(v)

        # Discard low-degree vertices when the resulting core is nonempty.
        core = nx.k_core(graph, k=r)
        if core and len(core) < len(graph):
            bags = [bags[v] for v in sorted(core)]
            graph = quotient(original, bags)
            verify(original, bags, graph)
            continue
        if not graph.number_of_edges():
            break
        u, v = min(
            graph.edges,
            key=lambda edge: (
                len(set(graph[edge[0]]) & set(graph[edge[1]])),
                edge,
            ),
        )
        bags[u] |= bags[v]
        del bags[v]
        graph = quotient(original, bags)
        verify(original, bags, graph)
        contractions += 1
    verify(original, best_bags, quotient(original, best_bags))
    return best_bags, contractions


def suite():
    yield "positive_clique", nx.complete_graph(10), 5, "control", True
    # Forest minors have independence ratio at most two.
    yield "negative_path", nx.path_graph(9), 3, "control", False
    # K3,3 has ratio two. Order-reducing minors have at most five vertices
    # and fewer than ten edges; edge deletions cannot raise the ratio.
    yield "negative_bipartite", nx.complete_bipartite_graph(3, 3), 4, "control", False
    for n, seed, r in [(27, 1, 9), (40, 0, 12), (50, 0, 14)]:
        yield f"random_{n}_{seed}", nx.gnp_random_graph(n, 0.8, seed=seed), r, "target", True
    base = nx.gnp_random_graph(20, 0.7, seed=7)
    blowup = nx.convert_node_labels_to_integers(nx.lexicographic_product(base, nx.complete_graph(2)))
    yield "clique_blowup", blowup, 12, "target", True
    base = nx.complete_multipartite_graph(4, 4, 4, 4)
    blowup = nx.convert_node_labels_to_integers(nx.lexicographic_product(base, nx.complete_graph(4)))
    yield "multipartite_k4", blowup, 16, "target", True


def digest(value):
    return sha256(json.dumps(value, separators=(",", ":")).encode()).hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args(argv)
    successes = 0
    for name, original, r, kind, expected in suite():
        n, m, a = len(original), original.number_of_edges(), alpha(original)
        if kind == "target":
            assert n * n <= r**3 and m > r * r * a and n <= r * a
        bags, steps = probe(original, r)
        model = quotient(original, bags)
        verify(original, bags, model)
        ratio = Fraction(len(model), alpha(model))
        found = ratio > r
        assert found == expected, (name, found, ratio)
        successes += found
        record = {
            "case": name, "kind": kind, "n": n, "m": m, "alpha": a, "r": r,
            "surplus": str(Fraction(m, r * r * a)), "found": found,
            "minor_n": len(model), "minor_alpha": alpha(model), "ratio": str(ratio),
            "contractions": steps, "max_bag": max(map(len, bags)),
            "graph_sha256": digest([n, sorted(sorted(edge) for edge in original.edges)]),
            "model_sha256": digest(sorted(sorted(bag) for bag in bags)),
            "bags": sorted(sorted(bag) for bag in bags),
        }
        if not args.summary:
            print(json.dumps(record, sort_keys=True))
    assert successes == 6
    print("PASS: 8 finite cases; 6 verified models; 2 negative controls.")


if __name__ == "__main__":
    main()
