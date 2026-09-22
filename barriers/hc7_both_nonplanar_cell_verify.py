"""Verify the finite data of the two-nonplanar-sides cell construction.

Standard library only. The accompanying note gives planar annuli and the
resulting K7 exclusion. Connectivity uses exhaustive vertex-cut checks.
"""

from itertools import combinations


def build():
    rings = {s: [f"{s}{i}" for i in range(n)]
             for s, n in (("a", 5), ("b", 5), ("c", 7),
                          ("d", 7), ("e", 7), ("f", 7))}
    planar = {"p", "z"} | set().union(*map(set, rings.values()))
    neighbours = {v: set() for v in planar | {"h0", "h1"}}

    def add(a, b):
        neighbours[a].add(b)
        neighbours[b].add(a)

    for ring in rings.values():
        for i, v in enumerate(ring):
            add(v, ring[(i + 1) % len(ring)])

    def annulus(first, second, runs):
        j = 0
        for v, length in zip(rings[first], runs, strict=True):
            for step in range(length + 1):
                add(v, rings[second][(j + step) % len(rings[second])])
            j += length
        assert j == len(rings[second])

    for first, second, runs in (
        ("a", "b", [1] * 5), ("a", "c", [2, 2, 1, 1, 1]),
        ("b", "d", [2, 2, 1, 1, 1]),
        ("c", "e", [1] * 7), ("d", "f", [1] * 7),
    ):
        annulus(first, second, runs)
    for cap, ring in (("p", "e"), ("z", "f")):
        for v in rings[ring]:
            add(cap, v)

    omitted = {"a0", "a1", "b0", "b1"}
    for v in planar | {"h0"}:
        add("h1", v)
    for v in planar - omitted:
        add("h0", v)
    return neighbours, planar, omitted


def main():
    neighbours, planar, omitted = build()
    vertices = set(neighbours)

    def connected(remaining):
        if not remaining:
            return True
        reached = {min(remaining)}
        pending = list(reached)
        while pending:
            new = (neighbours[pending.pop()] & remaining) - reached
            reached.update(new)
            pending.extend(new)
        return reached == remaining

    def boundary(selected, allowed=vertices):
        return (set().union(*(neighbours[v] for v in selected)) & allowed) - selected

    assert len(planar) == 40 and len(vertices) == 42
    assert sum(len(neighbours[v] & planar) for v in planar) // 2 == 114
    assert sum(map(len, neighbours.values())) // 2 == 191
    checks = 0
    for size in range(5):
        for cut in combinations(sorted(planar), size):
            assert connected(planar - set(cut)), cut
            checks += 1
    for size in range(1, 5):
        for subset in combinations(sorted(omitted), size):
            assert len(boundary(set(subset), planar)) >= 6
    assert min(map(len, neighbours.values())) == 7

    # For planar vertices the forbidden independent sets have small order.
    for v in planar:
        forbidden_size = len(neighbours[v]) - 4
        for candidate in combinations(sorted(neighbours[v]), forbidden_size):
            assert any(b in neighbours[a] for a, b in combinations(candidate, 2)), v
    # Seven disjoint c_i e_i edges bound independence in either apex neighbourhood.
    for h in ("h0", "h1"):
        matching = [{f"c{i}", f"e{i}"} for i in range(7)]
        assert all(edge <= neighbours[h] for edge in matching)
        assert all(f"e{i}" in neighbours[f"c{i}"] for i in range(7))
        assert len(neighbours[h]) - 7 <= len(neighbours[h]) - 5

    cell = {"z"} | {f"b{i}" for i in range(5)} | {
        f"{s}{i}" for s in ("d", "f") for i in range(7)
    }
    gates = {"h1", "a3", "a4"}
    path = ["a0", "a1", "a2", "h0"]
    clique = {"h0", "h1", "p", "e0", "e1"}
    assert connected(cell) and boundary(cell) == gates | set(path)
    assert not (cell & clique) and set(path) & clique == {"h0"}
    assert not (neighbours["p"] & cell)
    assert all(b in neighbours[a] for a, b in combinations(clique, 2))
    assert all((path[j] in neighbours[path[i]]) == (j == i + 1)
               for i, j in combinations(range(4), 2))
    assert not any({path[0], path[-1]} <= neighbours[v] for v in cell)

    side = cell | gates
    assert all(b in neighbours[a] for a, b in combinations(gates, 2))
    for size in range(4):
        for cut in combinations(sorted(side), size):
            assert connected(side - set(cut)), cut
    assert not connected(side - {"h1", "b0", "b3", "b4"})
    for apex, allowed in (("h1", side), ("h0", cell | set(path))):
        bags = [{apex}, {"z"}, {"f0"}, {"f1"},
                {f"f{i}" for i in range(2, 7)}]
        assert sum(map(len, bags)) == len(set().union(*bags))
        assert all(bag <= allowed and connected(bag) for bag in bags)
        assert all(any(neighbours[v] & second for v in first)
                   for first, second in combinations(bags, 2))

    classes = [
        {"a1", "a4", "c5", "d0", "d2", "d5", "e0", "e2", "e4", "z"},
        {"a0", "a2", "b4", "c6", "d4", "e1", "e3", "e5", "f1", "f3", "f6"},
        {"a3", "b0", "b2", "c0", "c2", "c4", "d3", "d6", "e6", "f2", "f5"},
        {"b1", "b3", "c1", "c3", "d1", "f0", "f4", "p"},
        {"h0"}, {"h1"},
    ]
    assert sum(map(len, classes)) == len(vertices)
    assert set().union(*classes) == vertices
    assert all(b not in neighbours[a]
               for colour in classes for a, b in combinations(colour, 2))
    print(f"Verified: 42 vertices, 191 edges; {checks} planar-base cut checks.")
    print("Connectivity 7, Dirac bounds, exact boundary, induced ports and outside K5.")
    print("Both sides have explicit K5 models; gate side connectivity 4; six-colouring.")


if __name__ == "__main__":
    main()
