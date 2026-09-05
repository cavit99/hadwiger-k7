"""Check two counterexamples to the prefix construction in arXiv:0808.0148v2.

Run with uv run python3 and this path. Prints two JSON certificates.
Refutes Lemmas 3.5/3.6 about the construction, not Lemma 3.2 or contractibility.
"""

import itertools
import json

import networkx as nx


ROOTS = {f"{side}{i}" for side in "ab" for i in range(2)}


def verify_flow(paths):
    graph = nx.Graph()
    incidence = {}
    assert set(paths) == set(itertools.product(range(2), repeat=2))
    for (i, j), path in paths.items():
        assert path[0] == f"a{i}" and path[-1] == f"b{j}"
        assert len(path) == len(set(path))
        ends = {path[0], path[-1]}
        assert set(path) & ROOTS == ends
        graph.add_edges_from(zip(path, path[1:]))
        for vertex in path:
            incidence.setdefault(vertex, []).append(ends)
    for first, second in itertools.combinations(paths, 2):
        if first[0] != second[0] and first[1] != second[1]:
            assert set(paths[first]).isdisjoint(paths[second])
    assert all(set.intersection(*ends) for ends in incidence.values())
    return graph


def prefix_construction(paths):
    stars = {root: set().union(*(set(p) for p in paths.values()
                                if root in {p[0], p[-1]})) for root in ROOTS}
    prefixes = {}
    branches = {}
    for (i, j), path in paths.items():
        stop = next((k for k, v in enumerate(path) if v in stars[f"a{1-i}"]), len(path))
        prefixes[i, j] = set(path[:stop])
    for i in range(2):
        branches[f"a{i}"] = prefixes[i, 0] | prefixes[i, 1]
    for j in range(2):
        branches[f"b{j}"] = stars[f"b{j}"] - branches["a0"] - branches["a1"]
    return prefixes, branches


def verify_model(graph, branches):
    assert set(branches) == ROOTS
    used = set()
    for root, branch in branches.items():
        assert root in branch and set(branch).isdisjoint(used)
        assert nx.is_connected(graph.subgraph(branch))
        used.update(branch)
    for i, j in itertools.product(range(2), repeat=2):
        assert any(graph.has_edge(u, v) for u in branches[f"a{i}"]
                   for v in branches[f"b{j}"])


def check(coloured):
    if coloured:
        paths = {(i, j): [f"a{i}", f"b{j}'", f"a{i}'", f"b{j}"]
                 for i, j in itertools.product(range(2), repeat=2)}
        expected = {f"a{i}": {f"a{i}"} for i in range(2)}
        expected.update({f"b{j}": {f"b{j}", f"b{j}'", "a0'", "a1'"} for j in range(2)})
        model = {f"a{i}": {f"a{i}"} for i in range(2)}
        model.update({f"b{j}": {f"b{j}", f"b{j}'", f"a{j}'"} for j in range(2)})
    else:
        paths = {(i, 0): [f"a{i}", "x", f"y{i}", "b0"] for i in range(2)}
        paths.update({(i, 1): [f"a{i}", f"y{i}", "b1"] for i in range(2)})
        expected = {f"a{i}": {f"a{i}", f"y{i}"} for i in range(2)}
        expected.update({"b0": {"x", "b0"}, "b1": {"b1"}})
        model = {**expected, "b0": {"b0"}}
    graph = verify_flow(paths)
    prefixes, branches = prefix_construction(paths)
    assert branches == expected
    verify_model(graph, model)
    failures35 = {f"P{i}{j}": sorted(set(path) - prefixes[i, j] - branches[f"b{j}"])
                  for (i, j), path in paths.items()}
    failures36 = {f"a{i}": sorted(set(paths[i, 0]) & set(paths[i, 1]) - branches[f"a{i}"])
                  for i in range(2)}
    if coloured:
        colour = {v: v.rstrip("'") for v in graph}
        assert all(colour[u] != colour[v] for u, v in graph.edges())
        assert all({colour[v] for v in p} == {p[0], p[-1]} for p in paths.values())
        assert all(graph.degree(v) >= 4 for v in set(graph) - ROOTS)
        assert failures36 == {"a0": ["a0'"], "a1": ["a1'"]}
        assert branches["b0"] & branches["b1"] == {"a0'", "a1'"}
    else:
        assert failures35 == {"P00": ["y0"], "P01": [], "P10": ["y1"], "P11": []}
        assert not nx.is_connected(graph.subgraph(branches["b0"]))
    return {"example": "Lemma 3.6" if coloured else "Lemma 3.5", "verified": True,
            "vertices": len(graph), "edges": graph.number_of_edges(),
            "paths": {f"P{i}{j}": p for (i, j), p in paths.items()},
            "prefixes": {f"P{i}{j}": sorted(p) for (i, j), p in prefixes.items()},
            "proposed_branches": {v: sorted(c) for v, c in branches.items()},
            "failures_3_5": failures35, "failures_3_6": failures36,
            "rooted_model": {v: sorted(c) for v, c in model.items()}}


if __name__ == "__main__":
    for coloured_example in (False, True):
        print(json.dumps(check(coloured_example), indent=2, sort_keys=True))
