#!/usr/bin/env python3
"""Random screen: does one guaranteed rooted diamond close a small 7-cut atom?"""

from __future__ import annotations

import itertools
import random
import sys

sys.path.insert(0, "active")
from hc7_k7minus_p3_atom_yuan_verify import k7minus_model

import networkx as nx


def quotient(boundary_edges, atom_kind, misses, roots, diamond_miss):
    g = nx.Graph()
    atom_n = {"K2": 2, "P3": 3, "K3": 3}[atom_kind]
    g.add_nodes_from(range(7 + atom_n))
    g.add_edges_from(boundary_edges)
    if atom_kind == "K2":
        g.add_edge(7, 8)
    elif atom_kind == "P3":
        g.add_edges_from(((7, 8), (8, 9)))
    else:
        g.add_edges_from(((7, 8), (8, 9), (7, 9)))
    for i, miss in enumerate(misses):
        for s in range(7):
            if s not in miss:
                g.add_edge(7 + i, s)
    # Replace the literal root-root graph by the adjacency guaranteed by
    # the rooted K4^- model.  Other incidences stay literal.
    for a, b in itertools.combinations(roots, 2):
        if tuple(sorted((a, b))) != diamond_miss:
            g.add_edge(a, b)
        elif g.has_edge(a, b):
            g.remove_edge(a, b)
    return g


def robustly_closes(boundary_edges, atom_kind, misses):
    for roots in itertools.combinations(range(7), 4):
        outcomes = [None, *itertools.combinations(roots, 2)]
        ok = True
        for pair in outcomes:
            dm = (-1, -1) if pair is None else tuple(pair)
            if k7minus_model(quotient(boundary_edges, atom_kind, misses, roots, dm)) is None:
                ok = False
                break
        if ok:
            return roots
    return None


def random_misses(kind, rng):
    internal_deg = {"K2": [1, 1], "P3": [1, 2, 1], "K3": [2, 2, 2]}[kind]
    ans = []
    for d in internal_deg:
        max_miss = d  # degree >=7 across a seven-boundary
        m = rng.randrange(max_miss + 1)
        ans.append(frozenset(rng.sample(range(7), m)))
    return tuple(ans)


def main():
    rng = random.Random(847221)
    for kind in ("K2", "P3", "K3"):
        survive = None
        for _ in range(5000):
            boundary = [e for e in itertools.combinations(range(7), 2) if rng.random() < .28]
            misses = random_misses(kind, rng)
            roots = robustly_closes(boundary, kind, misses)
            if roots is None:
                survive = (boundary, misses)
                break
        print(kind, "survivor", survive)


if __name__ == "__main__":
    main()
