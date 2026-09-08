"""Exact rooted-model check for the ten-vertex full-colour-class barrier.

Run: uv run python3 barriers/k5_scheme_full_colour_class_obstruction_verify.py
Standard library only; the written barrier proof does not depend on this check.
"""

from collections import Counter
from itertools import combinations, product


def graph(vertices, edges):
    adjacency = {v: set() for v in vertices}
    for u, v in edges:
        assert u != v
        adjacency[u].add(v)
        adjacency[v].add(u)
    return adjacency


def connected(adjacency, bag):
    reached = {next(iter(bag))}
    pending = list(reached)
    while pending:
        fresh = adjacency[pending.pop()] & bag - reached
        reached.update(fresh)
        pending.extend(fresh)
    return reached == bag


def models(adjacency, roots, nonroots):
    """Every nonroot is unused or belongs to exactly one named root bag."""
    for owners in product(range(len(roots) + 1), repeat=len(nonroots)):
        bags = [{r} for r in roots]
        for vertex, owner in zip(nonroots, owners):
            if owner < len(roots):
                bags[owner].add(vertex)
        if not all(connected(adjacency, bag) for bag in bags):
            continue
        if all(
            any(adjacency[v] & bags[j] for v in bags[i])
            for i, j in combinations(range(len(roots)), 2)
        ):
            yield bags


def main():
    roots = tuple("abcde")
    nonroots = ("u", "B", "C", "D", "E")
    paths = ("aBub", "aCuc", "aDud", "aEue", "bCBc", "dEDe",
             "bd", "be", "cd", "ce")
    adjacency = graph(roots + nonroots, (
        edge for path in paths for edge in zip(path, path[1:])
    ))
    colours = dict(zip(roots + nonroots, roots + roots))
    assert len({frozenset((p[0], p[-1])) for p in paths}) == 10
    assert all(colours[u] != colours[v]
               for u in adjacency for v in adjacency[u])
    for path in paths:
        assert len(path) == len(set(path))
        assert not set(path[1:-1]) & set(roots)
        assert set(map(colours.__getitem__, path)) == {path[0], path[-1]}
    for vertex in adjacency:
        incident = [{p[0], p[-1]} for p in paths if vertex in p]
        assert set.intersection(*incident)

    # Calibrate both positive and negative rooted instances.
    complete = graph(roots, combinations(roots, 2))
    cycle = graph(roots, zip(roots, roots[1:] + roots[:1]))
    assert len(list(models(complete, roots, ()))) == 1
    assert not list(models(cycle, roots, ()))
    canonical = graph(roots + nonroots, (
        (u, v) for u, v in combinations(roots + nonroots, 2)
        if colours[u] != colours[v] and not ({u, v} <= set(roots))
    ))
    canonical_models = list(models(canonical, roots, nonroots))
    assert any(any(x in bag for x, bag in zip(nonroots, bags))
               for bags in canonical_models)

    found = list(models(adjacency, roots, nonroots))
    witness = [set("a"), set("bC"), set("cB"), set("dE"), set("eD")]
    assert witness in found
    assert len(found) == 21
    assert not any(any(x in bag for x, bag in zip(nonroots, bags))
                   for bags in found)
    singleton_counts = Counter(
        tuple(r for r, bag in zip(roots, bags) if len(bag) == 1)
        for bags in found
    )
    assert singleton_counts == Counter({("a",): 5, (): 4,
                                       ("b",): 3, ("c",): 3,
                                       ("d",): 3, ("e",): 3})
    print("PASS: proper K5 scheme; 7,776 allocations; 21 rooted models;"
          " no own-colour pair in any bag")
    print("PASS: literal K5 positive, rooted C5 negative,"
          " canonical two-copy K5 has an own-colour-pair model")


if __name__ == "__main__":
    main()
