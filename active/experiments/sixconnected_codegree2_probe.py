#!/usr/bin/env python3
"""Probe the local quotients relevant to a codegree-two strengthening.

This is a discovery script, not a proof.  It enumerates the eight-vertex
graphs of minimum degree at least three which have no K_6^- minor and tests
the quotient obtained by adding two nonadjacent vertices complete to the
eight-vertex graph.
"""

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[2]
VERIFY = ROOT / "results" / "hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py"
SPEC = spec_from_file_location("low_codegree_verify", VERIFY)
assert SPEC and SPEC.loader
TOOLS = module_from_spec(SPEC)
SPEC.loader.exec_module(TOOLS)


def main() -> None:
    bases = [graph for graph in nx.graph_atlas_g() if len(graph) == 7]
    raw = [
        graph
        for base in bases
        for graph in TOOLS.extensions_of_atlas_graph(base)
        if min(dict(graph.degree()).values()) >= 3
    ]
    representatives = TOOLS.isomorphism_representatives(raw)
    local = [
        graph
        for graph in representatives
        if TOOLS.near_clique_minor_model(TOOLS.adjacency_tuple(graph), 6) is None
    ]
    full_survivors = []
    for graph in local:
        quotient = TOOLS.augmented_graph(graph, ())
        if TOOLS.near_clique_minor_model(TOOLS.adjacency_tuple(quotient), 7) is None:
            full_survivors.append(graph)

    split_full_survivors = []
    for graph in full_survivors:
        host = graph.copy()
        host.add_nodes_from((8, 9, 10))
        host.add_edges_from((8, vertex) for vertex in range(8))
        host.add_edges_from((9, vertex) for vertex in range(8))
        host.add_edges_from((10, vertex) for vertex in range(8))
        host.add_edge(9, 10)
        if nx.node_connectivity(host) < 6:
            continue
        if TOOLS.near_clique_minor_model(TOOLS.adjacency_tuple(host), 7) is None:
            split_full_survivors.append(host)

    degree_profiles = Counter(
        tuple(sorted(dict(graph.degree()).values())) for graph in full_survivors
    )
    print("DISCOVERY six-connected codegree-two quotient probe")
    print(f"raw_minimum_three={len(raw)}")
    print(f"isomorphism_classes={len(representatives)}")
    print(f"K6minus_free_local_classes={len(local)}")
    print(f"full_augmentation_survivors={len(full_survivors)}")
    print(f"sixconnected_split_full_survivors={len(split_full_survivors)}")
    print(f"degree_profiles={sorted(degree_profiles.items())}")
    print("survivors=")
    for graph in sorted(full_survivors, key=TOOLS.graph_code):
        print(TOOLS.graph_code(graph), tuple(graph.degree(v) for v in range(8)))


if __name__ == "__main__":
    main()
