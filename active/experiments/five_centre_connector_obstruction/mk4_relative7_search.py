#!/usr/bin/env python3
"""Test minimal portal augmentations of the M(K4) connector obstruction."""

from itertools import combinations

import networkx as nx


X_VERTICES = tuple(range(9))
Z = tuple(f"z{i}" for i in range(5))
TERMINALS = Z + ("p", "q")
BASE = {
    "z0": {5, 8},
    "z1": {3, 5},
    "z2": {0, 2},
    "z3": {2, 7},
    "z4": {0, 5},
    "p": {0, 7},
    "q": {2, 5},
}


def x_graph() -> nx.Graph:
    return nx.mycielskian(nx.complete_graph(4))


def boundary_size(graph: nx.Graph, portals: dict[str, set[int]], side: set[int]) -> int:
    outside = set().union(*(set(graph.neighbors(v)) for v in side)) - side
    boundary_terminals = sum(bool(side & portals[t]) for t in TERMINALS)
    return len(outside) + boundary_terminals


def is_relative_seven(graph: nx.Graph, portals: dict[str, set[int]]) -> bool:
    for order in range(1, len(X_VERTICES) + 1):
        for side_tuple in combinations(X_VERTICES, order):
            if boundary_size(graph, portals, set(side_tuple)) < 7:
                return False
    return True


def z_connected_after_deleting(
    graph: nx.Graph, portals: dict[str, set[int]], deleted: set[int]
) -> bool:
    residual = graph.subgraph(set(X_VERTICES) - deleted).copy()
    residual.add_nodes_from(Z)
    residual.add_edges_from(
        (z, v) for z in Z for v in portals[z] if v not in deleted
    )
    component = nx.node_connected_component(residual, Z[0])
    return all(z in component for z in Z)


def has_connector_pair(graph: nx.Graph, portals: dict[str, set[int]]) -> bool:
    for mask in range(1 << len(X_VERTICES)):
        used = {v for v in X_VERTICES if mask & (1 << v)}
        if not used & portals["p"] or not used & portals["q"]:
            continue
        subgraph = graph.subgraph(used)
        if not any(
            nx.has_path(subgraph, a, b)
            for a in used & portals["p"]
            for b in used & portals["q"]
        ):
            continue
        if z_connected_after_deleting(graph, portals, used):
            return True
    return False


def clique_number(graph: nx.Graph) -> int:
    return max(map(len, nx.find_cliques(graph)), default=0)


def valid_terminal_neighbourhood(
    graph: nx.Graph, terminal: str, neighbours: set[int]
) -> bool:
    if clique_number(graph.subgraph(neighbours)) >= 4:
        return False
    if terminal in Z:
        if len(neighbours) > 6:
            return False
        if clique_number(nx.complement(graph.subgraph(neighbours))) > 2:
            return False
    return True


def main() -> None:
    graph = x_graph()
    complete = nx.complete_graph(X_VERTICES)
    missing_edges = tuple(sorted(set(complete.edges()) - set(graph.edges())))
    edge_tested = 0
    edge_k5_free = 0
    edge_relative = 0
    for mask in range(1 << len(missing_edges)):
        candidate = graph.copy()
        candidate.add_edges_from(
            edge for index, edge in enumerate(missing_edges) if mask & (1 << index)
        )
        edge_tested += 1
        host = candidate.copy()
        host.add_nodes_from(TERMINALS)
        host.add_edges_from((t, v) for t in TERMINALS for v in BASE[t])
        if clique_number(host) >= 5:
            continue
        edge_k5_free += 1
        if not is_relative_seven(candidate, BASE):
            continue
        edge_relative += 1
        if not has_connector_pair(candidate, BASE):
            print(
                "FOUND_EDGE_SUPERGRAPH",
                {
                    "added_edges": sorted(set(candidate.edges()) - set(graph.edges())),
                    "portals": {t: sorted(BASE[t]) for t in TERMINALS},
                },
            )
            return
    print(
        "NO_EDGE_SUPERGRAPH",
        {
            "tested": edge_tested,
            "k5_free": edge_k5_free,
            "relative_seven": edge_relative,
        },
    )

    choices4 = tuple(combinations(TERMINALS, 3))
    choices6 = tuple(combinations(TERMINALS, 3))
    choices7 = tuple(combinations(tuple(t for t in TERMINALS if t != "z3" and t != "p"), 1))
    choices8 = tuple(combinations(tuple(t for t in TERMINALS if t != "z0"), 2))
    tested = 0
    locally_valid = 0
    forest_free = 0
    for at4 in choices4:
        for at6 in choices6:
            for at7 in choices7:
                for at8 in choices8:
                    tested += 1
                    portals = {t: set(BASE[t]) for t in TERMINALS}
                    for vertex, attached in ((4, at4), (6, at6), (7, at7), (8, at8)):
                        for terminal in attached:
                            portals[terminal].add(vertex)
                    if not all(
                        valid_terminal_neighbourhood(graph, t, portals[t])
                        for t in TERMINALS
                    ):
                        continue
                    locally_valid += 1
                    if has_connector_pair(graph, portals):
                        continue
                    forest_free += 1
                    if is_relative_seven(graph, portals):
                        print("FOUND", {t: sorted(portals[t]) for t in TERMINALS})
                        return
    print(
        "NONE",
        {"tested": tested, "locally_valid": locally_valid, "forest_free": forest_free},
    )


if __name__ == "__main__":
    main()
