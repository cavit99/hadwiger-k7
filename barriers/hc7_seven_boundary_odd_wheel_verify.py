"""Check the finite data of the seven-boundary odd-wheel barrier.

Standard library only. Planarity and K7 exclusion use the written proofs.
"""

from itertools import combinations


def main():
    planar = {"p", "z"} | {f"a{i}" for i in range(5)} | {
        f"b{i}" for i in range(5)
    }
    vertices = planar | {"h0", "h1"}
    neighbours = {v: set() for v in vertices}

    def add(a, b):
        neighbours[a].add(b)
        neighbours[b].add(a)

    for i in range(5):
        a, an = f"a{i}", f"a{(i + 1) % 5}"
        b, bn = f"b{i}", f"b{(i + 1) % 5}"
        for edge in (("p", a), ("z", b), (a, an), (b, bn), (b, a), (b, an)):
            add(*edge)
    for h in ("h0", "h1"):
        for v in vertices - {h}:
            add(h, v)

    def connected(remaining):
        reached = {next(iter(remaining))}
        pending = list(reached)
        while pending:
            new = (neighbours[pending.pop()] & remaining) - reached
            reached.update(new)
            pending.extend(new)
        return reached == remaining

    for size in range(5):
        assert all(
            connected(planar - set(cut))
            for cut in combinations(sorted(planar), size)
        )
    assert min(map(len, neighbours.values())) == 7
    for v in planar:
        local = neighbours[v] & planar
        assert len(local) == 5 and connected(local)
        assert all(len(neighbours[w] & local) == 2 for w in local)
    for v in vertices:
        forbidden_size = len(neighbours[v]) - 4
        assert all(
            any(b in neighbours[a] for a, b in combinations(candidate, 2))
            for candidate in combinations(sorted(neighbours[v]), forbidden_size)
        )

    cell = {"z"} | {f"b{i}" for i in range(5)}
    gates = {"h0", "h1", "a4"}
    path = [f"a{i}" for i in range(4)]
    clique = {"h0", "h1", "p", "a3", "a4"}
    boundary = set().union(*(neighbours[v] for v in cell)) - cell
    assert boundary == gates | set(path)
    assert connected(cell) and not (cell & clique)
    assert all(b in neighbours[a] for a, b in combinations(clique, 2))
    assert set(path) & clique == {"a3"}
    assert all(
        (path[j] in neighbours[path[i]]) == (j == i + 1)
        for i, j in combinations(range(4), 2)
    )
    assert not any({"a0", "a3"} <= neighbours[v] for v in cell)
    assert len(cell) == 6
    internal_edges = sum(len(neighbours[v] & cell) for v in cell) // 2
    gate_edges = sum(len(neighbours[v] & gates) for v in cell)
    assert internal_edges == 10 and gate_edges == 14
    assert all(len(neighbours[v] & cell) == 2 for v in path)
    for pair in combinations(path, 2):
        roots = gates | set(pair)
        rooted_vertices = cell | roots
        port_edges = sum(len(neighbours[v] & set(pair)) for v in cell)
        assert port_edges == 4
        assert internal_edges + gate_edges + port_edges - 4 * len(cell) == 4
        for size in range(1, len(cell) + 1):
            for subset in combinations(sorted(cell), size):
                selected = set(subset)
                external = set().union(*(neighbours[v] for v in selected))
                assert len((external & rooted_vertices) - selected) >= 5
    side = cell | gates
    for size in range(4):
        assert all(
            connected(side - set(cut))
            for cut in combinations(sorted(side), size)
        )
    assert not connected(side - {"h0", "h1", "b3", "b4"})
    classes = [
        {"p", "b1", "b3"}, {"z", "a0", "a2"},
        {"a1", "a3", "b4"}, {"a4", "b0", "b2"}, {"h0"}, {"h1"},
    ]
    assert set().union(*classes) == vertices
    assert sum(map(len, classes)) == len(vertices)
    assert all(
        b not in neighbours[a]
        for colour in classes for a, b in combinations(colour, 2)
    )
    print("Odd-wheel barrier verified: connectivity 7, side connectivity 4,")
    print("Dirac bounds, labelled cell hypotheses and explicit six-colouring.")
    print("All six root choices: rooted density 4 and internal five-connectivity.")


if __name__ == "__main__":
    main()
