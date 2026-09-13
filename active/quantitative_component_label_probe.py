#!/usr/bin/env python3
"""Finite tests of simultaneous monochromatic-component contractions.

Run: uv run python3 active/quantitative_component_label_probe.py
Expected: two verified surplus models and one negative control.
These fixed tests establish no universal construction or density bound.
"""

from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from random import Random

import networkx as nx


def maximum_clique(graph):
    """Exact branching, bounded by proper greedy colourings of candidates."""
    vertices = list(graph)
    index = {v: i for i, v in enumerate(vertices)}
    neighbours = [sum(1 << index[w] for w in graph[v]) for v in vertices]
    best = []

    def colour(candidates):
        order, bounds, number = [], [], 0
        while candidates:
            number += 1
            available = candidates
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                candidates ^= bit
                available = (available ^ bit) & ~neighbours[v]
                order.append(v)
                bounds.append(number)
        return order, bounds

    def expand(candidates, chosen):
        nonlocal best
        order, bounds = colour(candidates)
        for i in range(len(order) - 1, -1, -1):
            if len(chosen) + bounds[i] <= len(best):
                return
            v = order[i]
            remaining = candidates & neighbours[v]
            if remaining:
                expand(remaining, chosen + [v])
            elif len(chosen) + 1 > len(best):
                best = chosen + [v]
            candidates &= ~(1 << v)

    expand((1 << len(vertices)) - 1, [])
    return [vertices[i] for i in best]


def check_clique_search():
    graphs = [nx.empty_graph(0), nx.empty_graph(6), nx.complete_graph(7),
              nx.path_graph(8), nx.cycle_graph(7), nx.complete_bipartite_graph(3, 3)]
    graphs += [nx.gnp_random_graph(14, p, seed=seed)
               for p in (0.35, 0.7) for seed in (0, 1)]
    for graph in graphs:
        found = maximum_clique(graph)
        assert all(graph.has_edge(u, v) for u, v in combinations(found, 2))
        assert len(found) == max(map(len, nx.find_cliques(graph)), default=0)


def components(graph, q, seed):
    rng = Random(seed)
    labels = {v: rng.randrange(q) for v in graph}
    seen, bags = set(), []
    for v in graph:
        if v in seen:
            continue
        bag, stack = {v}, [v]
        seen.add(v)
        while stack:
            u = stack.pop()
            for w in graph[u]:
                if w not in seen and labels[w] == labels[v]:
                    seen.add(w)
                    bag.add(w)
                    stack.append(w)
        bags.append(bag)
    return labels, bags


def contact_graph(original, labels, bags):
    assert sum(map(len, bags)) == len(original) == len(set().union(*bags))
    owner = {v: i for i, bag in enumerate(bags) for v in bag}
    for bag in bags:
        assert bag and nx.is_connected(original.subgraph(bag))
        assert len({labels[v] for v in bag}) == 1
    graph = nx.Graph()
    graph.add_nodes_from(range(len(bags)))
    for u, v in original.edges:
        # Together with connectivity, this checks component maximality.
        if labels[u] == labels[v]:
            assert owner[u] == owner[v]
        if owner[u] != owner[v]:
            graph.add_edge(owner[u], owner[v])
    return graph


def verify_clique_model(original, bags):
    assert bags and all(bag and nx.is_connected(original.subgraph(bag)) for bag in bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    for left, right in combinations(bags, 2):
        assert any(original.has_edge(u, v) for u in left for v in right)


def cases():
    rng = Random(0)
    planted = nx.Graph()
    planted.add_nodes_from(range(216))
    planted.add_edges_from((u, v) for u, v in combinations(planted, 2)
                          if u // 6 != v // 6 and rng.random() < 0.6)
    a = max(map(len, nx.find_cliques(nx.complement(planted))))
    assert a == 9
    yield "planted216", planted, 36, a, {v: v // 6 for v in planted}, 54, 0, 47, None

    cube = nx.convert_node_labels_to_integers(nx.hypercube_graph(4))
    blown = nx.convert_node_labels_to_integers(nx.lexicographic_product(cube, nx.complete_graph(32)))
    # Q4 has an independent bipartition of size eight and a perfect matching:
    # alpha(Q4[K32]) = alpha(Q4) = 8.
    assert all(cube.has_edge(v, v ^ 1) for v in cube)
    colouring = {v: 32 * ((v // 32).bit_count() % 2) + v % 32 for v in blown}
    yield "cube512", blown, 64, 8, colouring, 96, 1, 65, 52

    # Two K4s joined at one vertex have a width-three tree decomposition.
    # Every minor has treewidth at most three, hence is four-colourable.
    # Thus all minor independence ratios are at most four.
    negative = nx.compose(nx.complete_graph([0, 1, 2, 3]), nx.complete_graph([0, 4, 5, 6]))
    colouring = dict(enumerate([0, 1, 2, 3, 1, 2, 3]))
    yield "two_k4_one_sum", negative, 4, 2, colouring, 6, 3, 4, None


def digest(value):
    return sha256(json.dumps(value, separators=(",", ":")).encode()).hexdigest()


def main():
    check_clique_search()
    successes = 0
    for name, original, r, a, colouring, q, seed, expected, largest_expected in cases():
        n, m = len(original), original.number_of_edges()
        assert n * n <= r**3
        assert len(set(colouring.values())) <= r
        assert all(colouring[u] != colouring[v] for u, v in original.edges)
        # The explicit r-colouring rules out ratio > r in every induced subgraph.
        surplus = m > r * r * a
        assert surplus == (name != "two_k4_one_sum")
        labels, all_bags = components(original, q, seed)
        graph = contact_graph(original, labels, all_bags)
        chosen = maximum_clique(graph)
        bags = [all_bags[i] for i in chosen]
        verify_clique_model(original, bags)
        assert len(bags) == expected
        successes += len(bags) > r
        record = {
            "case": name, "scope": "finite deterministic component-model test",
            "n": n, "m": m, "alpha": a, "r": r, "q": q, "label_seed": seed,
            "surplus": str(Fraction(m, r * r * a)), "found": len(bags) > r,
            "component_count": len(all_bags), "max_component": max(map(len, all_bags)),
            "minor_n": len(bags), "minor_alpha": 1,
            "graph_sha256": digest([n, sorted(sorted(edge) for edge in original.edges)]),
            "model_sha256": digest(sorted(sorted(bag) for bag in bags)),
            "bags": sorted(sorted(bag) for bag in bags),
        }
        if name == "planted216":
            record["generation"] = {"class_size": 6, "crossedge_probability": 0.6, "seed": 0}
        if largest_expected is not None:
            largest = {}
            for bag in all_bags:
                label = labels[next(iter(bag))]
                largest[label] = max(largest.get(label, 0), len(bag))
            eligible = [i for i, bag in enumerate(all_bags)
                        if len(bag) == largest[labels[next(iter(bag))]]]
            # Same-labelled components are anticomplete. Keeping all ties
            # therefore optimises over every largest-per-label tie choice.
            restricted = len(maximum_clique(graph.subgraph(eligible)))
            assert restricted == largest_expected
            record["best_largest_per_label_clique_number"] = restricted
            record["comparison_scope"] = "clique numbers, not maximum induced-subgraph independence ratios"
        print(json.dumps(record, sort_keys=True))
    assert successes == 2
    print("PASS: 3 finite cases; 2 verified surplus models; 1 negative control; 10 clique-search cross-checks.")


if __name__ == "__main__":
    main()
