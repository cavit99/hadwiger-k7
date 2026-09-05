"""Check explicit short schemes; the unbounded theorem has a written proof.

uv run python3 barriers/triangle_free_bipartite_attachment_verify.py
Add --json to emit all paths of the 24-vertex counterexample.
No SAT solver is used: every connected rooted branch set is considered.
"""

import argparse
import itertools
import json
from functools import lru_cache


def attachment(ell=5, split=True):
    cycle = ["v"] + [f"c{i}" for i in range(1, ell)]
    roots = cycle + ["p", "q", "l1", "l2", "r1", "r2"]
    edges = list(zip(cycle, cycle[1:] + cycle[:1]))
    edges += list(itertools.product(["v", "p", "q"], roots[-4:]))

    def clone(u, v):
        side = "L" if v in {"c1", "l1", "l2"} else "R"
        return f"{u}:{side if split and u in {'v', 'p'} else '0'}"

    paths = [[u, clone(v, u), clone(u, v), v] for u, v in edges]
    return roots, edges, paths


def canonical(roots, edges):
    return roots, edges, [[u, f"{v}:0", f"{u}:0", v] for u, v in edges]


def prepare(roots, edges, paths):
    """Check scheme semantics and the hypotheses of singleton pruning."""
    root_index = {v: i for i, v in enumerate(roots)}
    assert len(root_index) == len(roots) and len(edges) == len(paths)
    target = {frozenset(e) for e in edges}
    assert len(target) == len(edges) and all(len(e) == 2 for e in target)
    hn = [0] * len(roots)
    for u, v in edges:
        hn[root_index[u]] |= 1 << root_index[v]
        hn[root_index[v]] |= 1 << root_index[u]
    usage, adjacency, seen_edges = {}, {}, set()
    for (u, v), path in zip(edges, paths):
        assert len(path) == len(set(path)) == 4
        assert (path[0], path[-1]) == (u, v)
        assert not set(path[1:-1]) & set(roots)
        assert [x.split(":")[0] for x in path] == [u, v, u, v]
        for x in path:
            usage.setdefault(x, []).append({u, v})
        for x, y in zip(path, path[1:]):
            edge = frozenset((x, y))
            assert edge not in seen_edges
            seen_edges.add(edge)
            adjacency.setdefault(x, set()).add(y)
            adjacency.setdefault(y, set()).add(x)
    assert all(set.intersection(*uses) for uses in usage.values())
    nonroots = sorted(set(adjacency) - set(roots))
    index = {v: i for i, v in enumerate(nonroots)}
    rn = [sum(1 << index[x] for x in adjacency[r]) for r in roots]
    adj = [sum(1 << index[x] for x in adjacency[v] if x in index) for v in nonroots]
    assert all(rn[i].bit_count() == hn[i].bit_count() for i in range(len(roots)))
    assert all(not (rn[root_index[u]] & rn[root_index[v]]) for u, v in edges)
    return nonroots, rn, adj, hn, adjacency


def rooted_model(roots, edges, paths):
    nonroots, rn, adj, hn, host = prepare(roots, edges, paths)
    n, k = len(nonroots), len(roots)
    nodes = cases = 0

    @lru_cache(None)
    def boundary(mask):
        out, remaining = 0, mask
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            out |= adj[bit.bit_length() - 1]
        return out & ~mask

    def connected(i, mask):
        seen = mask & rn[i]
        while True:
            newer = seen | (boundary(seen) & mask)
            if newer == seen:
                return seen == mask
            seen = newer

    def contact(i, a, j, b):
        return bool(a & rn[j] or b & rn[i] or boundary(a) & b)

    bags = [[mask for mask in range(1 << n) if connected(i, mask)] for i in range(k)]

    def search(domains, used, chosen):
        nonlocal nodes
        nodes += 1
        if not domains:
            return chosen
        available = n - used.bit_count()
        minimum = {i: min(m.bit_count() for m in dd) for i, dd in domains.items()}
        if sum(minimum.values()) > available:
            return None
        i = min(domains, key=lambda j: len(domains[j]))
        remaining = {j: dd for j, dd in domains.items() if j != i}
        upper = available - sum(minimum[j] for j in remaining)
        for mask in domains[i]:
            if mask.bit_count() > upper:
                continue
            new = {}
            for j, dd in remaining.items():
                valid = [b for b in dd if not b & mask and
                         (not hn[i] >> j & 1 or contact(i, mask, j, b))]
                if not valid:
                    break
                new[j] = valid
            else:
                found = search(new, used | mask, chosen + [(i, mask)])
                if found is not None:
                    return found
        return None

    for singleton_mask in range(1 << k):
        singles = [i for i in range(k) if singleton_mask >> i & 1]
        if any(singleton_mask & hn[i] for i in singles):
            continue
        neighbours = 0
        for i in singles:
            neighbours |= hn[i]
        lower = [0 if i in singles else 1 + (neighbours >> i & 1) for i in range(k)]
        if sum(lower) > n:
            continue
        spare, domains = n - sum(lower), {}
        for i in range(k):
            if i in singles:
                continue
            # Exact root degree forces one distinct host neighbour into
            # each target-neighbour bag, and none into any other bag.
            valid = [m for m in bags[i]
                     if lower[i] <= m.bit_count() <= lower[i] + spare and
                     all((m & rn[s]).bit_count() == (hn[s] >> i & 1) for s in singles)]
            if not valid:
                break
            domains[i] = valid
        else:
            cases += 1
            found = search(domains, 0, [(i, 0) for i in singles])
            if found is not None:
                result = {roots[i]: {roots[i]} | {v for j, v in enumerate(nonroots) if m >> j & 1}
                          for i, m in found}
                # Independently check returned positives by graph traversal.
                used = set()
                for root, bag in result.items():
                    assert root in bag and not used & bag
                    used |= bag
                    reached, todo = {root}, [root]
                    while todo:
                        for v in host[todo.pop()] & bag - reached:
                            reached.add(v)
                            todo.append(v)
                    assert reached == bag
                assert all(any(host[x] & result[v] for x in result[u]) for u, v in edges)
                return result, cases, nodes
    return None, cases, nodes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    cycle = [f"c{i}" for i in range(5)]
    cycle_edges = list(zip(cycle, cycle[1:] + cycle[:1]))
    assert rooted_model(*canonical(cycle, cycle_edges))[0] is not None
    assert rooted_model(*attachment(split=False))[0] is not None
    theta_edges = [("u", "a"), ("a", "v"), ("u", "b"), ("b", "c"),
                   ("c", "v"), ("u", "d"), ("d", "e"), ("e", "v")]
    assert rooted_model(*canonical(sorted({x for e in theta_edges for x in e}), theta_edges))[0] is None
    roots, edges, paths = attachment()
    result, cases, nodes = rooted_model(roots, edges, paths)
    assert result is None
    if args.json:
        print(json.dumps({"roots": roots, "target_edges": edges, "paths": paths,
                          "rooted_model": None, "surviving_singleton_cases": cases,
                          "search_nodes": nodes}, indent=2))
    else:
        print("PASS positive C5 and canonical attachment, negative skewed theta calibrations")
        print(f"PASS 24-vertex scheme: no rooted model; singleton cases={cases}; nodes={nodes}")
        print("Finite check only; the adjacent written proof covers every odd cycle length >=5.")


if __name__ == "__main__":
    main()
