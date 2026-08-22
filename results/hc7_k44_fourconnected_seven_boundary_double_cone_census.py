#!/usr/bin/env python3
"""Exact atlas census for the two-component seven-cut quotient.

For every unlabelled seven-vertex graph S, test whether two anticomplete
vertices complete to S together with S contain a K7-minus minor.  The target
checker is an exhaustive spanning-forest enumeration on the resulting
nine-vertex connected graph.
"""

from __future__ import annotations

from collections import Counter
import hashlib
from itertools import combinations
import sys

import networkx as nx


def double_cone(separator):
    graph = nx.disjoint_union(separator, nx.empty_graph(2))
    graph.add_edges_from((s, apex) for s in range(7) for apex in (7, 8))
    return graph


def quotient_edges(graph, labels):
    return sum(
        any(labels[u] == i and labels[v] == j
            or labels[u] == j and labels[v] == i
            for u, v in graph.edges)
        for i, j in combinations(range(7), 2)
    )


def target_witness(graph):
    # Every minor model in a connected graph can be made spanning.  With
    # nine vertices and seven branch bags, a spanning forest has two edges.
    edges = tuple(graph.edges)
    for first, second in combinations(edges, 2):
        parent = list(range(9))

        def find(vertex):
            while parent[vertex] != vertex:
                parent[vertex] = parent[parent[vertex]]
                vertex = parent[vertex]
            return vertex

        def unite(left, right):
            left, right = find(left), find(right)
            if left == right:
                return False
            parent[right] = left
            return True

        assert unite(*first) and unite(*second)  # two simple distinct edges
        roots = {}
        labels = []
        for vertex in range(9):
            root = find(vertex)
            if root not in roots:
                roots[root] = len(roots)
            labels.append(roots[root])
        assert len(roots) == 7
        if quotient_edges(graph, labels) >= 20:
            validate(graph, labels)
            return tuple(labels)
    return None


def validate(graph, labels):
    assert len(labels) == 9 and set(labels) == set(range(7))
    bags = [{v for v, label in enumerate(labels) if label == i} for i in range(7)]
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    assert quotient_edges(graph, labels) >= 20


def main(certificate_path, census_path):
    separators = [graph for graph in nx.graph_atlas_g() if len(graph) == 7]
    assert len(separators) == 1044
    rows = []
    by_connectivity = Counter()
    positive_by_connectivity = Counter()
    for separator in separators:
        connectivity = nx.node_connectivity(separator)
        witness = target_witness(double_cone(separator))
        by_connectivity[connectivity] += 1
        positive_by_connectivity[connectivity] += witness is not None
        rows.append((separator, witness))

    positive = sum(witness is not None for _, witness in rows)
    negatives = [separator for separator, witness in rows if witness is None]
    delta_four_rows = [
        (separator, witness) for separator, witness in rows
        if min(dict(separator.degree).values()) >= 4
    ]
    assert positive == 344 and len(negatives) == 700
    assert dict(sorted(by_connectivity.items())) == {
        0: 191, 1: 385, 2: 332, 3: 111, 4: 21, 5: 3, 6: 1,
    }
    assert dict(sorted(positive_by_connectivity.items())) == {
        0: 27, 1: 73, 2: 129, 3: 90, 4: 21, 5: 3, 6: 1,
    }
    assert len(delta_four_rows) == 29
    assert all(witness is not None for _, witness in delta_four_rows)

    maximal_negatives = []
    for separator in negatives:
        extensions = []
        for edge in nx.non_edges(separator):
            extension = separator.copy()
            extension.add_edge(*edge)
            extensions.append(extension)
        if all(target_witness(double_cone(extension)) is not None
               for extension in extensions):
            maximal_negatives.append(separator)
    assert len(maximal_negatives) == 21

    digest = hashlib.sha256()
    with open(certificate_path, "w", encoding="ascii", newline="\n") as output:
        for separator, witness in rows:
            if min(dict(separator.degree).values()) < 4:
                continue
            assert witness is not None
            graph6 = nx.to_graph6_bytes(separator, header=False).decode().strip()
            labels = "".join(map(str, witness))
            output.write(f"{graph6}\t{labels}\n")
            digest.update(graph6.encode("ascii") + bytes(witness))

    lines = [
        "DOUBLE_CONE_ATLAS total=1044 positive=344 negative=700",
        f"connectivity_totals={dict(sorted(by_connectivity.items()))}",
        f"connectivity_positive={dict(sorted(positive_by_connectivity.items()))}",
        "minimum_degree_at_least_four=29 positive=29",
        f"negative_edge_histogram={dict(sorted(Counter(map(lambda g: len(g.edges), negatives)).items()))}",
        "maximal_negative_graph6=" + repr(sorted(
            nx.to_graph6_bytes(graph, header=False).decode().strip()
            for graph in maximal_negatives
        )),
        "minimum_degree_at_least_four_certificates=29",
        "certificate_digest=" + digest.hexdigest(),
    ]
    with open(census_path, "w", encoding="ascii", newline="\n") as output:
        output.write("\n".join(lines) + "\n")
    print(*lines, sep="\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {sys.argv[0]} CERTIFICATES_TSV CENSUS_TXT")
    main(sys.argv[1], sys.argv[2])
