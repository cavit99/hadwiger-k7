#!/usr/bin/env python3
"""Generate the exact order-11 census and emit K7-minus certificates."""

from __future__ import annotations

import ctypes
import hashlib
from itertools import combinations
from pathlib import Path
import sys
import time

import networkx as nx
import pynauty


N = 11
FULL = (1 << N) - 1
EXPECTED_COUNTS = (1, 2, 4, 11, 23, 62, 150, 424, 1165, 3547, 10946)
EXPECTED_DIGEST = "08b284abc580718e87d2c5561d04b334f47064e5b46254d37440f12c87576ce2"
CUTS = tuple(
    sum(1 << v for v in choice)
    for size in range(1, 7)
    for choice in combinations(range(N), size)
)
FOUR_SETS = tuple(
    sum(1 << v for v in choice) for choice in combinations(range(N), 4)
)
SEVEN_SETS = tuple(
    sum(1 << v for v in choice) for choice in combinations(range(N), 7)
)


def certificate(graph: nx.Graph) -> bytes:
    return pynauty.certificate(
        pynauty.Graph(
            len(graph), adjacency_dict={v: list(graph[v]) for v in graph}
        )
    )


def unlabelled_subcubic_order_eleven():
    graphs = [nx.empty_graph(0)]
    counts = []
    for order in range(1, N + 1):
        unique = {}
        for parent in graphs:
            eligible = [v for v in parent if parent.degree(v) < 3]
            for size in range(min(3, len(eligible)) + 1):
                for neighbours in combinations(eligible, size):
                    child = parent.copy()
                    child.add_node(order - 1)
                    child.add_edges_from((order - 1, v) for v in neighbours)
                    key = certificate(child)
                    if key not in unique:
                        unique[key] = child
        graphs = list(unique.values())
        counts.append(len(graphs))
        if order <= 7:
            atlas_count = sum(
                len(g) == order and max(dict(g.degree).values(), default=0) <= 3
                for g in nx.graph_atlas_g()
            )
            assert atlas_count == len(graphs)
    assert tuple(counts) == EXPECTED_COUNTS
    return graphs


def adjacency_masks(graph: nx.Graph):
    masks = [0] * N
    for u, v in graph.edges:
        masks[u] |= 1 << v
        masks[v] |= 1 << u
    return masks


def connected_after_cut(adjacency, cut):
    left = FULL ^ cut
    seen = left & -left
    todo = seen
    while todo:
        bit = todo & -todo
        todo ^= bit
        new = adjacency[bit.bit_length() - 1] & left & ~seen
        seen |= new
        todo |= new
    return seen == left


def seven_connected(adjacency):
    return min(map(int.bit_count, adjacency)) >= 7 and all(
        connected_after_cut(adjacency, cut) for cut in CUTS
    )


def literal_k44(adjacency):
    for left in FOUR_SETS:
        common = FULL ^ left
        todo = left
        while todo:
            bit = todo & -todo
            todo ^= bit
            common &= adjacency[bit.bit_length() - 1]
        if common.bit_count() >= 4:
            return True
    return False


def target_subgraph(complement_adjacency):
    for chosen in SEVEN_SETS:
        twice_edges = 0
        todo = chosen
        while todo:
            bit = todo & -todo
            todo ^= bit
            twice_edges += (
                complement_adjacency[bit.bit_length() - 1] & chosen
            ).bit_count()
        if twice_edges <= 2:
            return True
    return False


def bag_connected(adjacency, vertices):
    mask = sum(1 << v for v in vertices)
    seen = mask & -mask
    todo = seen
    while todo:
        bit = todo & -todo
        todo ^= bit
        new = adjacency[bit.bit_length() - 1] & mask & ~seen
        seen |= new
        todo |= new
    return seen == mask


def validate_labels(adjacency, labels):
    bags = [[v for v in range(N) if labels[v] == i] for i in range(7)]
    assert all(bags) and all(bag_connected(adjacency, bag) for bag in bags)
    quotient_edges = sum(
        any((adjacency[u] >> v) & 1 for u in bags[i] for v in bags[j])
        for i, j in combinations(range(7), 2)
    )
    assert quotient_edges >= 20
    return quotient_edges


def main(library_path: str, output_path: str):
    library = ctypes.CDLL(library_path)
    checker = library.has_k7minus11
    checker.argtypes = [
        ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_ubyte)
    ]
    checker.restype = ctypes.c_int

    started = time.time()
    complements = unlabelled_subcubic_order_eleven()
    total_7connected = literal = literal_subgraph = literal_proper = 0
    quotient_histogram = {}
    digest = hashlib.sha256()
    with open(output_path, "w", encoding="ascii", newline="\n") as output:
        for sparse in complements:
            sparse_adjacency = adjacency_masks(sparse)
            adjacency = [
                FULL ^ (1 << v) ^ sparse_adjacency[v] for v in range(N)
            ]
            if not seven_connected(adjacency):
                continue
            total_7connected += 1
            has_literal = literal_k44(adjacency)
            literal += has_literal
            if has_literal and target_subgraph(sparse_adjacency):
                literal_subgraph += 1

            raw_adjacency = (ctypes.c_uint16 * N)(*adjacency)
            raw_labels = (ctypes.c_ubyte * N)()
            assert checker(raw_adjacency, raw_labels) == 1
            labels = list(raw_labels)
            quotient_edges = validate_labels(adjacency, labels)
            quotient_histogram[quotient_edges] = (
                quotient_histogram.get(quotient_edges, 0) + 1
            )
            if has_literal and not target_subgraph(sparse_adjacency):
                literal_proper += 1

            graph = nx.from_graph6_bytes(
                nx.to_graph6_bytes(nx.complement(sparse), header=False).strip()
            )
            graph6 = nx.to_graph6_bytes(graph, header=False).decode().strip()
            label_text = "".join(map(str, labels))
            output.write(f"{graph6}\t{label_text}\n")
            digest.update(graph6.encode("ascii") + bytes(labels))

    assert total_7connected == 9940
    assert literal == 9844
    assert literal_subgraph == 3871
    assert literal_proper == 5973
    assert quotient_histogram == {20: 9398, 21: 542}
    assert digest.hexdigest() == EXPECTED_DIGEST
    print(
        "EXACT_N11",
        "subcubic", len(complements),
        "seven_connected", total_7connected,
        "literal_k44", literal,
        "literal_subgraph", literal_subgraph,
        "literal_proper_minor", literal_proper,
        "quotient_histogram", quotient_histogram,
        "digest", digest.hexdigest(),
        "seconds", round(time.time() - started, 3),
    )


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {sys.argv[0]} CHECKER_SO CERTIFICATES_TSV")
    main(sys.argv[1], sys.argv[2])
