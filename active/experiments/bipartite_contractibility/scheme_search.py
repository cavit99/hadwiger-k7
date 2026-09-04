"""Deterministic exploratory K3,3-scheme search; no unbounded conclusion.

uv run python3 active/experiments/bipartite_contractibility/scheme_search.py
Uses the Z3 command-line executable, not an undeclared Python dependency.
SAT models are checked independently with NetworkX. UNSAT is only a lead.
"""

import argparse
import itertools
import random
import re
import shutil
import subprocess

import networkx as nx


def pool(counts, rng, prefix):
    """Supports of size two or three with the prescribed three incidences."""
    options = []
    for triples in range(min(counts) + 1):
        pairs = [counts[i] + counts[j] - counts[k] - triples
                 for i, j, k in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]]
        if all(x >= 0 and x % 2 == 0 for x in pairs):
            options.append((triples, [x // 2 for x in pairs]))
    if not options:
        return None
    triples, pairs = rng.choice(options)
    supports = [(0, 1, 2)] * triples
    for pair, count in zip([(0, 1), (0, 2), (1, 2)], pairs):
        supports += [pair] * count
    return {f"{prefix}_{i}": support for i, support in enumerate(supports)}


def generate(rng):
    while True:
        sizes = [[rng.randint(1, 4) for _ in range(3)] for _ in range(3)]
        aa = [pool(sizes[i], rng, f"a{i}") for i in range(3)]
        bb = [pool([sizes[i][j] for i in range(3)], rng, f"b{j}")
              for j in range(3)]
        if all(p is not None for p in aa + bb):
            break
    paths = []
    colours = {f"{s}{i}": 3 * (s == "b") + i for s in "ab" for i in range(3)}
    for i, p in enumerate(aa + bb):
        colours.update({v: i for v in p})
    for i, j in itertools.product(range(3), repeat=2):
        av = [v for v, support in aa[i].items() if j in support]
        bv = [v for v, support in bb[j].items() if i in support]
        rng.shuffle(av)
        rng.shuffle(bv)
        paths.append([f"a{i}"] + [v for pair in zip(bv, av) for v in pair]
                     + [f"b{j}"])
    g = nx.Graph()
    for p in paths:
        g.add_edges_from(zip(p, p[1:]))
    roots = [f"{s}{i}" for s in "ab" for i in range(3)]
    # Independent of the incidence generator: check actual path semantics.
    usage = {v: [] for v in g}
    edges = []
    for p in paths:
        assert len(p) == len(set(p)) and not set(p[1:-1]) & set(roots)
        ends = {p[0], p[-1]}
        assert all(colours[v] in {colours[x] for x in ends} for v in p)
        for v in p:
            usage[v].append(ends)
        edges += [frozenset(e) for e in zip(p, p[1:])]
    assert len(edges) == len(set(edges))
    assert all(set.intersection(*sets) for sets in usage.values())
    assert all(colours[u] != colours[v] for u, v in g.edges)
    assert all(g.degree(v) >= 4 for v in set(g) - set(roots))
    return g, roots, paths


def model(g, roots, timeout):
    vertices = roots + sorted(set(g) - set(roots))
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    lines = [f"(set-option :timeout {timeout * 1000})", "(set-logic QF_LIA)"]
    for i in range(n):
        lines += [f"(declare-const c{i} Int)", f"(declare-const d{i} Int)"]
    for i, v in enumerate(vertices):
        lines += [f"(assert (and (<= -1 c{i}) (<= c{i} 5) (<= 0 d{i}) (<= d{i} {n})))"]
        if i < 6:
            lines += [f"(assert (= c{i} {i}))", f"(assert (= d{i} 0))"]
        else:
            descent = " ".join(f"(and (= c{i} c{index[w]}) (< d{index[w]} d{i}))"
                               for w in g[v])
            lines.append(f"(assert (=> (>= c{i} 0) (or {descent})))")
    for a, b in itertools.product(range(3), range(3, 6)):
        contacts = []
        for u, v in g.edges:
            i, j = index[u], index[v]
            contacts += [f"(and (= c{i} {a}) (= c{j} {b}))",
                         f"(and (= c{i} {b}) (= c{j} {a}))"]
        lines.append(f"(assert (or {' '.join(contacts)}))")
    lines += ["(check-sat)", f"(get-value ({' '.join(f'c{i}' for i in range(n))}))"]
    result = subprocess.run([shutil.which("z3"), "-in"], input="\n".join(lines),
                            text=True, capture_output=True, timeout=timeout + 5)
    status = result.stdout.splitlines()[0]
    if status not in {"sat", "unsat", "unknown"}:
        raise RuntimeError(result.stdout + result.stderr)
    if status != "sat":
        return status, result.stdout
    values = {int(i): int(v.replace(" ", "").replace("(", "").replace(")", ""))
              for i, v in re.findall(r"\(c(\d+)\s+(-?\d+|\(-\s+\d+\))\)", result.stdout)}
    bags = [{vertices[i] for i in range(n) if values[i] == a} for a in range(6)]
    assert all(roots[a] in bags[a] and nx.is_connected(g.subgraph(bags[a]))
               for a in range(6))
    assert all(any(g.has_edge(u, v) for u in bags[a] for v in bags[b])
               for a, b in itertools.product(range(3), range(3, 6)))
    return status, [sorted(bag) for bag in bags]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=30)
    parser.add_argument("--seed", type=int, default=44033)
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()
    if not shutil.which("z3"):
        parser.error("Z3 executable required")
    positive = nx.complete_bipartite_graph(3, 3)
    assert model(positive, list(range(6)), args.timeout)[0] == "sat"
    assert model(positive, [0, 1, 3, 2, 4, 5], args.timeout)[0] == "unsat"
    rng = random.Random(args.seed)
    counts = {"sat": 0, "unsat": 0, "unknown": 0}
    for sample in range(args.samples):
        g, roots, paths = generate(rng)
        status, certificate = model(g, roots, args.timeout)
        counts[status] += 1
        print(f"sample={sample} vertices={len(g)} edges={g.number_of_edges()} {status}", flush=True)
        if status != "sat":
            print({"paths": paths, "solver_output": certificate}, flush=True)
    print(f"seed={args.seed} samples={args.samples} counts={counts}")


if __name__ == "__main__":
    main()
