#!/usr/bin/env python3
"""Verify the static obstruction in the low-endpoint pair-deletion model."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[3]
BASE_VERIFY = (
    ROOT / "results" / "hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py"
)
SPEC = spec_from_file_location("low_codegree_verify", BASE_VERIFY)
assert SPEC and SPEC.loader
TOOLS = module_from_spec(SPEC)
SPEC.loader.exec_module(TOOLS)


def contact_quotient() -> nx.Graph:
    """Return K_7^vee with two adjacent roots sharing four contacts."""

    # 0=P, 1=B, 2=C and 3,4,5,6=U_1,U_2,U_3,U_4.
    graph = nx.complete_graph(7)
    graph.remove_edges_from(((0, 1), (0, 2)))
    graph.add_nodes_from((7, 8))
    graph.add_edge(7, 8)
    for root in (7, 8):
        graph.add_edges_from((root, bag) for bag in (1, 2, 3, 4))
    return graph


def verify_multiplicities(extra_x_neighbour: bool) -> None:
    """Check a degree/codegree allocation with the same bag contacts."""

    # Each tuple is (common, v-only, x-only) within the named branch set.
    rows = {
        "P": (0, 0, 0),
        "B": (1, 0, 0),
        "C": (1, 0, 0),
        "U1": (1, 2, 2),
        "U2": (0, 2, 2 + int(extra_x_neighbour)),
        "U3": (0, 0, 0),
        "U4": (0, 0, 0),
    }
    v_neighbours = sum(common + v_only for common, v_only, _ in rows.values())
    x_neighbours = sum(common + x_only for common, _, x_only in rows.values())
    common_neighbours = sum(common for common, _, _ in rows.values())
    v_contacts = {
        bag for bag, (common, v_only, _) in rows.items() if common + v_only
    }
    x_contacts = {
        bag for bag, (common, _, x_only) in rows.items() if common + x_only
    }
    assert v_neighbours == 7
    assert x_neighbours == 7 + int(extra_x_neighbour)
    assert common_neighbours == 3
    assert v_contacts == x_contacts == {"B", "C", "U1", "U2"}


def main() -> None:
    TOOLS.calibrate_minor_engine()
    graph = contact_quotient()
    assert nx.to_graph6_bytes(graph, header=False).decode().strip() == "HN~~zpx"
    assert nx.node_connectivity(graph) == 4
    assert TOOLS.near_clique_minor_model(TOOLS.adjacency_tuple(graph), 7) is None
    verify_multiplicities(False)
    verify_multiplicities(True)

    print("GREEN low-endpoint pair-deletion static-interface obstruction")
    print("graph6=HN~~zpx target_free=True")
    print("root_contacts=B,C,U1,U2")
    print("degree_pairs=(8,8),(8,9) codegree=3 are arithmetically feasible")


if __name__ == "__main__":
    main()
