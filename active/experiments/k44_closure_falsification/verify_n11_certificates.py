#!/usr/bin/env python3
"""Independent verifier for emitted order-11 K7-minus certificates."""

from __future__ import annotations

import hashlib
from itertools import combinations
import sys

import networkx as nx


N = 11
FULL = (1 << N) - 1
EXPECTED_DIGEST = "08b284abc580718e87d2c5561d04b334f47064e5b46254d37440f12c87576ce2"
CUTS = tuple(
    sum(1 << v for v in choice)
    for size in range(7)
    for choice in combinations(range(N), size)
)


def connected_mask(adjacency, mask):
    seen = mask & -mask
    todo = seen
    while todo:
        bit = todo & -todo
        todo ^= bit
        new = adjacency[bit.bit_length() - 1] & mask & ~seen
        seen |= new
        todo |= new
    return seen == mask


def validate(graph, labels):
    assert len(graph) == N and set(labels) == set(range(7))
    adjacency = [sum(1 << w for w in graph[v]) for v in range(N)]
    assert all(connected_mask(adjacency, FULL ^ cut) for cut in CUTS)
    bags = [sum(1 << v for v, label in enumerate(labels) if label == i)
            for i in range(7)]
    assert all(bags) and all(connected_mask(adjacency, bag) for bag in bags)
    quotient_edges = sum(
        any(adjacency[u] & bags[j]
            for u in range(N) if (bags[i] >> u) & 1)
        for i, j in combinations(range(7), 2)
    )
    assert quotient_edges >= 20
    return quotient_edges


def main(path):
    seen = set()
    histogram = {}
    digest = hashlib.sha256()
    with open(path, encoding="ascii") as source:
        for line in source:
            graph6, label_text = line.rstrip("\n").split("\t")
            assert graph6 not in seen
            seen.add(graph6)
            labels = tuple(map(int, label_text))
            graph = nx.from_graph6_bytes(graph6.encode("ascii"))
            quotient_edges = validate(graph, labels)
            histogram[quotient_edges] = histogram.get(quotient_edges, 0) + 1
            digest.update(graph6.encode("ascii") + bytes(labels))
    assert len(seen) == 9940
    assert histogram == {20: 9398, 21: 542}
    assert digest.hexdigest() == EXPECTED_DIGEST
    print(
        "CERTIFICATES_VALID", len(seen),
        "quotient_histogram", histogram,
        "digest", digest.hexdigest(),
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} CERTIFICATES_TSV")
    main(sys.argv[1])
