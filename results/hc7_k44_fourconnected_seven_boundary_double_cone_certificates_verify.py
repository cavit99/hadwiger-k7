#!/usr/bin/env python3
"""Independent validator for the delta(S)>=4 double-cone witnesses."""

from __future__ import annotations

import hashlib
from itertools import combinations
import sys

import networkx as nx


def double_cone(separator):
    graph = nx.disjoint_union(separator, nx.empty_graph(2))
    graph.add_edges_from((s, apex) for s in range(7) for apex in (7, 8))
    return graph


def validate(graph, labels):
    assert len(graph) == 9 and len(labels) == 9
    assert set(labels) == set(range(7))
    bags = [{v for v, label in enumerate(labels) if label == i} for i in range(7)]
    assert all(bags) and all(nx.is_connected(graph.subgraph(bag)) for bag in bags)
    contacts = sum(
        any(graph.has_edge(u, v) for u in bags[i] for v in bags[j])
        for i, j in combinations(range(7), 2)
    )
    assert contacts >= 20


def main(path):
    digest = hashlib.sha256()
    seen = set()
    with open(path, encoding="ascii") as source:
        for line in source:
            graph6, label_text = line.rstrip("\n").split("\t")
            assert graph6 not in seen
            seen.add(graph6)
            separator = nx.from_graph6_bytes(graph6.encode("ascii"))
            assert len(separator) == 7
            assert min(dict(separator.degree).values()) >= 4
            labels = tuple(map(int, label_text))
            validate(double_cone(separator), labels)
            digest.update(graph6.encode("ascii") + bytes(labels))
    assert len(seen) == 29
    print("DOUBLE_CONE_CERTIFICATES_VALID", len(seen), "digest", digest.hexdigest())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} CERTIFICATES_TSV")
    main(sys.argv[1])
