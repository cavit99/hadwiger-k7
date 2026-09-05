"""Finite C5 wedge C4 schemes; no unbounded contractibility conclusion.

uv run python3 active/experiments/bipartite_contractibility/c5_c4_schemes.py
Add --json for every input path and independently checked rooted model.
"""

import argparse
import itertools
import json

import networkx as nx

from scheme_search import model


def scheme(bits):
    roots = list("vabcdefg")
    paths = [["v", "a1", "v1", "a"], ["a", "b1", "a1", "b"],
             ["b", "c1", "b1", "c"], ["c", "v2", "c1", "v"]]
    cycle = list("vdefg")
    for i, u in enumerate(cycle):
        v = cycle[(i + 1) % 5]
        own, other = [u + "1", u + "2"], [v + "1", v + "2"]
        if u == "v" and bits[5]:
            own.reverse()
        if bits[(i + 1) % 5]:
            other.reverse()
        paths.append([u] + [x for pair in zip(other, own) for x in pair] + [v])

    # Check actual scheme semantics independently of the order generator.
    g, usage, all_edges = nx.Graph(), {}, []
    for path in paths:
        assert len(path) == len(set(path))
        assert not set(path[1:-1]) & set(roots)
        ends = {path[0], path[-1]}
        assert all(x[0] in ends for x in path)
        for x in path:
            usage.setdefault(x, []).append(ends)
        g.add_edges_from(zip(path, path[1:]))
        all_edges.extend(frozenset(e) for e in zip(path, path[1:]))
    assert all(set.intersection(*sets) for sets in usage.values())
    assert all(x[0] != y[0] for x, y in g.edges)
    assert all(g.degree(x) >= 4 for x in set(g) - set(roots))
    assert len(all_edges) == len(set(all_edges))
    edges = [(roots.index(p[0]), roots.index(p[-1])) for p in paths]
    return g, roots, edges, paths


def projection_rank(paths, labels):
    """Total rank of actual-membership projections, using union-find."""
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    rank = 0
    for path in paths:
        for i in range(1, len(path) - 1):
            if path[i] in labels:
                x, y = find(path[i - 1]), find(path[i + 1])
                if x != y:
                    parent[x] = y
                    rank += 1
    return rank


def independent_rank_check(g, roots, paths):
    """Check every independent set of the 13 nonroots; retain witnesses."""
    nonroots, checked = sorted(set(g) - set(roots)), 0
    for size in range(1, len(nonroots) + 1):
        for labels in itertools.combinations(nonroots, size):
            chosen = set(labels)
            if any(chosen & set(g[x]) for x in chosen):
                continue
            checked += 1
            rank = projection_rank(paths, chosen)
            if rank <= size:
                return checked, {"labels": labels, "rank": rank}
    return checked, None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    roots = list("abcde")
    edges = [(i, (i + 1) % 5) for i in range(5)]
    positive = nx.Graph((roots[a], roots[b]) for a, b in edges)
    assert model(positive, roots, 8, edges)[0] == "sat"
    negative = nx.Graph(("x", a) for a in roots)
    assert model(negative, roots, 8, edges)[0] == "unsat"
    certificates, counts = [], {"sat": 0, "unsat": 0, "unknown": 0}
    rank_reductions = 0
    for bits in itertools.product(range(2), repeat=6):
        g, roots, edges, paths = scheme(bits)
        status, certificate = model(g, roots, 8, edges)
        checked, reduction = independent_rank_check(g, roots, paths)
        rank_reductions += reduction is not None
        counts[status] += 1
        certificates.append({"bits": bits, "paths": paths, "roots": roots,
                             "target_edges": edges, "status": status,
                             "rooted_model": certificate,
                             "independent_sets_checked": checked,
                             "rank_reduction": reduction})
    if args.json:
        print(json.dumps(certificates, indent=2, sort_keys=True))
    else:
        print(f"64 mixed-multiplicity C5 wedge C4 schemes: {counts}")
        print(f"21 vertices, 37 edges each; independent-set rank reductions={rank_reductions}")
        print("All SAT models independently checked with NetworkX; finite diagnostics only.")


if __name__ == "__main__":
    main()
