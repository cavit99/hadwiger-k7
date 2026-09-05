"""Diagnostic certificates for the bipartite matroid-contraction construction.

uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py
uv run python3 active/experiments/bipartite_contractibility/matroid_reduction.py --order 3 --json

Finite diagnostics only; the universal assertion requires its written proof.
Uses graphic-matroid augmentation, with independent NetworkX rank, component,
scheme, contraction and final rooted-model checks. No solver dependency.
"""

import argparse
from collections import deque
from dataclasses import dataclass
import itertools
import json
import random

import networkx as nx

from scheme_search import generate
from singleton_shore_obstruction import construction


@dataclass
class Scheme:
    roots: dict
    colours: dict
    paths: dict
    parts: tuple

    def graph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.colours)
        for path in self.paths.values():
            graph.add_edges_from(zip(path, path[1:]))
        return graph


def check_scheme(scheme):
    roots = set(scheme.roots.values())
    assert not scheme.parts[0] & scheme.parts[1]
    assert set(scheme.roots) == scheme.parts[0] | scheme.parts[1]
    assert len(roots) == len(scheme.roots)
    assert all(scheme.colours[r] == v for v, r in scheme.roots.items())
    used, edges = set(roots), set()
    for (a, b), path in scheme.paths.items():
        assert a in scheme.parts[0] and b in scheme.parts[1]
        assert (path[0], path[-1]) == (scheme.roots[a], scheme.roots[b])
        assert len(path) == len(set(path)) and not roots.intersection(path[1:-1])
        assert all(scheme.colours[x] in {a, b} for x in path)
        for u, v in zip(path, path[1:]):
            edge = frozenset((u, v))
            assert scheme.colours[u] != scheme.colours[v] and edge not in edges
            edges.add(edge)
        used.update(path)
    assert used == set(scheme.colours)


def initial_scheme(colours, paths, parts):
    paths = {(p[0], p[-1]): p for p in paths}
    scheme = Scheme({v: v for part in parts for v in part}, colours, paths, parts)
    check_scheme(scheme)
    return scheme


def projections(scheme, shore):
    vertices = {a: {x for x, c in scheme.colours.items() if c == a}
                for a in shore}
    edges = {a: {} for a in shore}
    for (u, v), original in scheme.paths.items():
        a, path = (u, original) if u in shore else (v, original[::-1])
        for k in range(1, len(path) - 1, 2):
            x = path[k]
            assert x not in edges[a] and path[k - 1] != path[k + 1]
            edges[a][x] = (path[k - 1], path[k + 1])
    assert all(rank(vertices[a], edges[a], set(edges[a])) == len(vertices[a]) - 1
               for a in shore)
    return vertices, edges


def rank(vertices, edges, labels):
    graph = nx.Graph()
    graph.add_nodes_from(vertices)
    graph.add_edges_from(edges[x] for x in labels if x in edges)
    return len(vertices) - nx.number_connected_components(graph)


def pack(vertices, edges):
    """Shortest augmenting paths; a failed search returns the dual set X."""
    indices = sorted(vertices)
    ground = set().union(*(set(edges[a]) for a in indices))
    trees = {a: set() for a in indices}
    demand = sum(len(vertices[a]) - 1 for a in indices)
    while True:
        used = set().union(*trees.values())
        if len(used) == demand:
            return trees, None
        forests = {}
        for a in indices:
            forest = nx.Graph()
            forest.add_nodes_from(vertices[a])
            forest.add_edges_from((*edges[a][x], {"label": x}) for x in trees[a])
            forests[a] = forest
        previous = {x: None for x in sorted(ground - used)}
        queue = deque(previous)
        terminal = None
        while queue and terminal is None:
            x = queue.popleft()
            for a in indices:
                if x not in edges[a] or x in trees[a]:
                    continue
                u, v = edges[a][x]
                if not nx.has_path(forests[a], u, v):
                    terminal = (x, a)
                    break
                path = nx.shortest_path(forests[a], u, v)
                for p, q in zip(path, path[1:]):
                    y = forests[a][p][q]["label"]
                    if y not in previous:
                        previous[y] = (x, a)
                        queue.append(y)
        if terminal is None:
            xset = set(previous)
            assert len(used) == len(ground - xset) + sum(
                rank(vertices[a], edges[a], xset) for a in indices)
            assert ground - xset <= used
            assert all(len(trees[a] & xset) == rank(vertices[a], edges[a], xset)
                       for a in indices)
            return trees, xset
        x, a = terminal
        additions = [(a, x)]
        removals = []
        while previous[x] is not None:
            before, a = previous[x]
            removals.append((a, x))
            additions.append((a, before))
            x = before
        for a, x in removals:
            trees[a].remove(x)
        for a, x in additions:
            trees[a].add(x)
        assert sum(map(len, trees.values())) == len(used) + 1
        assert len(set().union(*trees.values())) == len(used) + 1
        assert all(rank(vertices[a], edges[a], trees[a]) == len(trees[a])
                   for a in indices)


def check_model(graph, roots, target_edges, bags):
    used, vertices = set(), set(graph)
    assert set(bags) == set(roots)
    for v, bag in bags.items():
        assert bag <= vertices
        assert roots[v] in bag and not used.intersection(bag)
        assert nx.is_connected(graph.subgraph(bag))
        used.update(bag)
    assert all(any(graph.has_edge(x, y) for x in bags[a] for y in bags[b])
               for a, b in target_edges)


def erase_walk(walk):
    path, positions = [], {}
    for x in walk:
        if x in positions:
            for y in path[positions[x] + 1:]:
                del positions[y]
            path = path[:positions[x] + 1]
        else:
            positions[x] = len(path)
            path.append(x)
    return path


def solve(original):
    scheme = original
    lifts = {x: {x} for x in scheme.colours}
    records = []
    while True:
        graph = scheme.graph()
        counts = [sum(c in part and x != scheme.roots[c]
                      for x, c in scheme.colours.items()) for part in scheme.parts]
        shore = scheme.parts[0 if counts[0] <= counts[1] else 1]
        vertices, edges = projections(scheme, shore)
        trees, xset = pack(vertices, edges)
        record = {"order": len(scheme.colours), "shore": sorted(shore),
                  "ranks": {a: len(vertices[a]) - 1 for a in sorted(shore)},
                  "forests": {a: sorted(trees[a]) for a in sorted(shore)}}
        if xset is None:
            bags = {a: vertices[a] | trees[a] for a in shore}
            bags.update({b: {r} for b, r in scheme.roots.items() if b not in shore})
            check_model(graph, scheme.roots, scheme.paths, bags)
            record["terminal"] = True
            records.append(record)
            result = {v: set().union(*(lifts[x] for x in bag)) for v, bag in bags.items()}
            check_model(original.graph(), original.roots, original.paths, result)
            return result, records
        assert xset
        pieces, image = {}, {}
        for a in sorted(shore):
            projection = nx.Graph()
            projection.add_nodes_from(vertices[a])
            projection.add_edges_from(edges[a][x] for x in xset if x in edges[a])
            for component in nx.connected_components(projection):
                labels = {x for x in trees[a] & xset if edges[a][x][0] in component}
                piece = set(component) | labels
                representative = (scheme.roots[a] if scheme.roots[a] in component
                                  else min(component))
                pieces[representative] = piece
                image.update({x: representative for x in component})
                assert nx.is_connected(graph.subgraph(piece))
        used = set().union(*pieces.values())
        assert sum(map(len, pieces.values())) == len(used)
        assert all(len(piece & set(scheme.roots.values())) <= 1 for piece in pieces.values())
        for x in set(scheme.colours) - used - xset:
            pieces[x] = {x}
            image[x] = x
        new_paths = {}
        for edge, path in scheme.paths.items():
            for k, x in enumerate(path[1:-1], 1):
                if x in xset:
                    assert image[path[k - 1]] == image[path[k + 1]]
            new_paths[edge] = erase_walk([image[x] for x in path if x not in xset])
        new_roots = {v: image[r] for v, r in scheme.roots.items()}
        retained = set(new_roots.values()).union(*map(set, new_paths.values()))
        new_colours = {x: scheme.colours[x] for x in retained}
        reduced = Scheme(new_roots, new_colours, new_paths, scheme.parts)
        check_scheme(reduced)
        # Every retained edge must be an actual edge between disjoint pieces.
        assert all(any(graph.has_edge(p, q) for p in pieces[x] for q in pieces[y])
                   for x, y in reduced.graph().edges)
        assert all(scheme.roots[v] in pieces[r] for v, r in new_roots.items())
        assert len(reduced.colours) < len(scheme.colours)
        record.update({"X": sorted(xset), "pieces": {x: sorted(pieces[x]) for x in sorted(retained)},
                       "reduced_paths": [new_paths[e] for e in sorted(new_paths)],
                       "reduced_roots": new_roots})
        records.append(record)
        lifts = {x: set().union(*(lifts[y] for y in pieces[x])) for x in retained}
        scheme = reduced


def mixed_k44(rng):
    """Every colour uses all pairs or all triples, each with incidence three."""
    parts = tuple({f"{s}{i}" for i in range(4)} for s in "ab")
    colours = {v: v for part in parts for v in part}
    supports = {}
    for side in "ab":
        for i in range(4):
            v = f"{side}{i}"
            supports[v] = {}
            for k, subset in enumerate(itertools.combinations(range(4), rng.choice((2, 3)))):
                x = f"{v}_{k}"
                supports[v][x] = subset
                colours[x] = v
    paths = []
    for i, j in itertools.product(range(4), repeat=2):
        aa = [x for x, subset in supports[f"a{i}"].items() if j in subset]
        bb = [x for x, subset in supports[f"b{j}"].items() if i in subset]
        rng.shuffle(aa)
        rng.shuffle(bb)
        paths.append([f"a{i}"] + [x for pair in zip(bb, aa) for x in pair] + [f"b{j}"])
    return initial_scheme(colours, paths, parts)


def check_small_packing():
    """Compare augmentation with every assignment; independence uses union-find."""
    rng = random.Random(7121)
    labels = [f"x{i}" for i in range(6)]
    vertices = {str(a): set(range(3)) for a in range(3)}
    for case in range(21):
        edges = {a: {} for a in vertices}
        for x in labels:
            for a in edges:
                if case == 0:
                    edges[a][x] = (1, 2) if x == "x0" else (0, 1)
                elif rng.randrange(4):
                    edges[a][x] = tuple(rng.sample(range(3), 2))
        maximum = 0
        for assignment in itertools.product([None, *edges], repeat=len(labels)):
            parents = {a: list(range(3)) for a in vertices}
            size = 0
            for x, a in zip(labels, assignment):
                if a is None:
                    continue
                if x not in edges[a]:
                    break
                u, v = edges[a][x]
                while parents[a][u] != u:
                    u = parents[a][u]
                while parents[a][v] != v:
                    v = parents[a][v]
                if u == v:
                    break
                parents[a][u] = v
                size += 1
            else:
                maximum = max(maximum, size)
        trees, _ = pack(vertices, edges)
        assert sum(map(len, trees.values())) == maximum
        if case == 0:
            assert maximum == 4


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=3)
    parser.add_argument("--samples", type=int, default=30)
    parser.add_argument("--seed", type=int, default=44033)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    colours, paths = construction(args.order)
    parts = tuple({f"{s}{i}" for i in range(args.order)} for s in "ab")
    scheme = initial_scheme(colours, list(paths.values()), parts)
    bags, records = solve(scheme)
    if args.json:
        print(json.dumps({"colours": colours, "paths": list(paths.values()),
                          "reductions": records, "model": {v: sorted(b) for v, b in bags.items()},
                          "verified": True}, sort_keys=True, indent=2))
        return
    check_small_packing()
    print("graphic-matroid augmentation: exact assignment check passed on 21 systems")
    print(f"singleton-shore barrier n={args.order}: verified; orders="
          f"{[r['order'] for r in records]}; shores={[r['shore'][0][0] for r in records]}")
    rng = random.Random(args.seed)
    for _ in range(args.samples):
        _, roots, paths = generate(rng)
        usage = {}
        for path in paths:
            for x in path:
                usage[x] = usage.get(x, {path[0], path[-1]}) & {path[0], path[-1]}
        colours = {x: next(iter(support)) for x, support in usage.items()}
        parts = (set(roots[:3]), set(roots[3:]))
        solve(initial_scheme(colours, paths, parts))
    print(f"variable-support K3,3 samples={args.samples} seed={args.seed}: all verified")
    for _ in range(args.samples):
        solve(mixed_k44(rng))
    print(f"pair/triple-support K4,4 samples={args.samples}: all verified")


if __name__ == "__main__":
    main()
