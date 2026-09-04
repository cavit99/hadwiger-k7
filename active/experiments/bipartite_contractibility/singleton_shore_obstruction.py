"""Check coloured K(n,n) schemes requiring expansion of both root shores.

Invocation:
    uv run python3 active/experiments/bipartite_contractibility/singleton_shore_obstruction.py
    uv run python3 active/experiments/bipartite_contractibility/singleton_shore_obstruction.py --order 5 --json

Default: 36 vertices, 81 edges, 9 paths; neither complete root shore can
remain singleton in any rooted K3,3 model; an explicit rooted model exists.
This refutes a proposed proof normal form, not bipartite contractibility.
The singleton obstruction permits arbitrary colour mixing in branch sets.
"""

import argparse
import json

import networkx as nx


def construction(n):
    colours = {}
    for i in range(n):
        for v in [f"a{i}", f"Y{i}", f"Z{i}", *(f"x{i}_{k}" for k in range(n))]:
            colours[v] = f"a{i}"
        for v in [f"b{i}", f"y{i}", f"z{i}", *(f"X{i}_{k}" for k in range(n))]:
            colours[v] = f"b{i}"
    paths = {
        f"a{i}b{j}": [f"a{i}", f"X{j}_{(i+1)%n}", f"Z{i}", f"X{j}_{i}",
                       f"Y{i}", f"y{j}", f"x{i}_{j}", f"z{j}",
                       f"x{i}_{(j+1)%n}", f"b{j}"]
        for i in range(n) for j in range(n)
    }
    return colours, paths


def verify_scheme(colours, paths, n):
    roots = {f"{side}{i}" for side in "ab" for i in range(n)}
    graph = nx.Graph()
    incidence = {v: [] for v in colours}
    for path in paths.values():
        ends = {path[0], path[-1]}
        assert len(path) == len(set(path))
        assert set(path) & roots == ends
        assert {colours[v] for v in path} == ends
        for v in path:
            incidence[v].append(ends)
        for u, v in zip(path, path[1:]):
            assert colours[u] != colours[v] and not graph.has_edge(u, v)
            graph.add_edge(u, v)
    assert set(graph) == set(colours) and nx.is_connected(graph)
    for v, path_ends in incidence.items():
        assert set.intersection(*path_ends) == {colours[v]}
        if v not in roots:
            assert len(path_ends) >= 2 and graph.degree(v) >= 4
    return graph


def verify_singleton_obstruction(graph, side, n):
    """Check the terminal partition and separator degree certificate.

    The n opposite branch sets each meet all n disjoint root-neighbour sets
    of size n, exhausting their union. In any branch set, identify the part
    outside that union and the separator with one anchor. Every separator
    vertex then has at most two neighbours. A connected quotient on n
    terminals, s separator vertices and the anchor needs n+s edges but has
    at most 2s, so s>=n. The n branch sets need n*n separator vertices.
    """
    roots = {f"{side}{i}" for i in range(n)}
    neighbourhoods = [set(graph.neighbors(root)) for root in sorted(roots)]
    terminals = set().union(*neighbourhoods)
    assert all(len(t) == n for t in neighbourhoods) and len(terminals) == n * n
    symbols = "YZ" if side == "a" else "yz"
    separator = {f"{symbol}{i}" for symbol in symbols for i in range(n)}
    outside = set(graph) - roots - terminals - separator
    assert outside and all(set(graph[v]) <= roots | separator for v in terminals)
    assert not graph.subgraph(separator).number_of_edges()
    degree_bounds = {}
    for v in sorted(separator):
        neighbours = set(graph[v])
        bound = sum(bool(neighbours & group) for group in neighbourhoods)
        bound += bool(neighbours & outside)
        assert bound <= 2
        degree_bounds[v] = bound
    assert n * n > len(separator)
    return {"singleton_roots": sorted(roots),
            "root_neighbour_sets": [sorted(t) for t in neighbourhoods],
            "separator": sorted(separator), "quotient_degree_bounds": degree_bounds,
            "minimum_separator_vertices_per_opposite_branch": n,
            "required_total": n * n, "available_total": len(separator)}


def verify_model(graph, paths, n):
    branches = {f"a{i}": paths[f"a{i}b{i}"][:5] for i in range(n)}
    branches.update({f"b{j}": paths[f"a{j}b{j}"][5:] for j in range(n)})
    used = set()
    for root, branch in branches.items():
        assert root in branch and not used.intersection(branch)
        assert nx.is_connected(graph.subgraph(branch))
        used.update(branch)
    for i in range(n):
        for j in range(n):
            assert f"Y{i}" in branches[f"a{i}"] and f"y{j}" in branches[f"b{j}"]
            assert graph.has_edge(f"Y{i}", f"y{j}")
    return branches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    n = args.order
    assert n >= 3, "the barrier family is defined for n>=3"
    colours, paths = construction(n)
    graph = verify_scheme(colours, paths, n)
    certificates = {side: verify_singleton_obstruction(graph, side, n) for side in "ab"}
    branches = verify_model(graph, paths, n)
    assert len(graph) == 2*n*n + 6*n and graph.number_of_edges() == 9*n*n
    assert len(paths) == n*n
    if args.json:
        print(json.dumps({"colours": colours, "paths": paths,
                          "singleton_obstructions": certificates,
                          "rooted_model": branches}, indent=2, sort_keys=True))
    else:
        print(f"VALID COLOURED K{n},{n} SCHEME: {len(graph)} vertices, {9*n*n} edges, {n*n} paths")
        for side in "AB":
            print(f"{side} ROOTS ALL SINGLETON: impossible; {n*n} separator vertices required, {2*n} available")
        print(f"ROOTED K{n},{n} MODEL WITH BOTH SHORES EXPANDED: verified")


if __name__ == "__main__":
    main()
