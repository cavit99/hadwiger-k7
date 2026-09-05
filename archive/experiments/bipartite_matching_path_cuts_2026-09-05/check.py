"""Frozen finite diagnostic: cuts of supplied matching paths are insufficient.

uv run python3 archive/experiments/bipartite_matching_path_cuts_2026-09-05/check.py
"""

import argparse
import itertools
import json

import networkx as nx


PATHS = [p.split() for p in [
    "a0 b0_1 a0_1 b0", "a0 b1_1 a0_1 b1",
    "a0 b2_0 a0_0 b2", "a0 b3_0 a0_0 b3",
    "a1 b0_0 a1_0 b0", "a1 b1_0 a1_1 b1",
    "a1 b2_0 a1_0 b2", "a1 b3_0 a1_1 b3",
    "a2 b0_1 a2_1 b0", "a2 b1_1 a2_0 b1",
    "a2 b2_1 a2_1 b2", "a2 b3_1 a2_0 b3",
    "a3 b0_0 a3_0 b0", "a3 b1_0 a3_1 b1",
    "a3 b2_1 a3_0 b2", "a3 b3_1 a3_1 b3",
]]
MODEL = {f"b{j}": {f"b{j}"} for j in range(4)}
MODEL.update({f"a{i}": {f"a{i}", f"a{i}_0", f"a{i}_1", *labels}
              for i, labels in enumerate([
                  ["b0_1", "b3_0"], ["b1_0", "b2_0"],
                  ["b1_1", "b2_1"], ["b0_0", "b3_1"]])})


def contacts(graph, bags):
    return all(any(graph.has_edge(u, v) for u in bags[f"a{i}"] for v in bags[f"b{j}"])
               for i, j in itertools.product(range(4), repeat=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    roots = {f"{s}{i}" for s in "ab" for i in range(4)}
    graph, usage, edges = nx.Graph(), {}, set()
    for p in PATHS:
        assert len(p) == len(set(p)) and not roots.intersection(p[1:-1])
        for x in p:
            assert x.split("_")[0] in {p[0], p[-1]}
            usage.setdefault(x, []).append({p[0], p[-1]})
        for u, v in zip(p, p[1:]):
            assert u[0] != v[0] and frozenset((u, v)) not in edges
            edges.add(frozenset((u, v)))
            graph.add_edge(u, v)
    assert len(graph) == 24 and graph.number_of_edges() == 48
    assert all(set.intersection(*uses) for uses in usage.values())
    assert all(len(usage[x]) == 2 and graph.degree(x) == 4 for x in set(graph) - roots)
    assert set(MODEL) == roots and sum(map(len, MODEL.values())) == len(set().union(*MODEL.values()))
    assert all(r in bag and bag <= set(graph) and nx.is_connected(graph.subgraph(bag))
               for r, bag in MODEL.items())
    assert contacts(graph, MODEL)
    checked = 0
    for permutation in itertools.permutations(range(4)):
        chosen = [PATHS[4*i + permutation[i]] for i in range(4)]
        assert len(set().union(*map(set, chosen))) == 16
        for cuts in itertools.product(range(1, 4), repeat=4):
            bags = {}
            for i, (p, k) in enumerate(zip(chosen, cuts)):
                bags[f"a{i}"] = set(p[:k])
                bags[f"b{permutation[i]}"] = set(p[k:])
            assert not contacts(graph, bags)
            checked += 1
    assert checked == 24 * 3**4
    result = {"verified": True, "matching_cut_models_checked": checked,
              "matching_cut_models_found": 0, "paths": PATHS,
              "rooted_model": {r: sorted(b) for r, b in MODEL.items()}}
    print(json.dumps(result, indent=2, sort_keys=True) if args.json else
          "verified: coloured K4,4 scheme; 1944 supplied-matching cuts fail; explicit rooted model passes")


if __name__ == "__main__":
    main()
