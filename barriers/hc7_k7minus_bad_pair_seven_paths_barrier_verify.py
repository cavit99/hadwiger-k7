#!/usr/bin/env python3
"""Verify the 11-vertex nonadjacent bad-pair seven-path barrier."""

from itertools import combinations


VERTICES = ("u", "v", "p", "q", "x1", "x2", "y1", "y2", "y3", "z1", "z2")


def edge(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


EDGES = {
    *(edge("u", x) for x in ("p", "x1", "x2", "y1", "y2", "y3", "z1", "z2")),
    *(edge("v", x) for x in ("q", "x1", "x2", "y1", "y2", "y3", "z1", "z2")),
    edge("p", "x1"),
    edge("p", "x2"),
    edge("q", "x1"),
    edge("q", "x2"),
    edge("x1", "x2"),
    edge("y1", "y2"),
    edge("y1", "y3"),
    edge("y2", "y3"),
    edge("z1", "z2"),
}


def adjacent(a: str, b: str) -> bool:
    return edge(a, b) in EDGES


def neighbours(v: str) -> set[str]:
    return {w for w in VERTICES if w != v and adjacent(v, w)}


def independence_number(vertices: set[str]) -> int:
    for size in range(len(vertices), 0, -1):
        for subset in combinations(sorted(vertices), size):
            if all(not adjacent(a, b) for a, b in combinations(subset, 2)):
                return size
    return 0


def contains_clique(vertices: set[str], size: int) -> bool:
    return any(
        all(adjacent(a, b) for a, b in combinations(subset, 2))
        for subset in combinations(sorted(vertices), size)
    )


def verify_tree_decomposition() -> int:
    bags = {
        "B0": {"u", "v", "x1", "x2"},
        "Bp": {"u", "p", "x1", "x2"},
        "Bq": {"v", "q", "x1", "x2"},
        "By": {"u", "v", "y1", "y2", "y3"},
        "Bz": {"u", "v", "z1", "z2"},
    }
    tree_edges = {edge("B0", leaf) for leaf in ("Bp", "Bq", "By", "Bz")}

    assert set().union(*bags.values()) == set(VERTICES)
    assert all(any({a, b} <= bag for bag in bags.values()) for a, b in EDGES)

    for vertex in VERTICES:
        containing = {name for name, bag in bags.items() if vertex in bag}
        reached = {next(iter(containing))}
        while True:
            expanded = reached | {
                name
                for name in containing - reached
                if any(edge(name, old) in tree_edges for old in reached)
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == containing

    return max(map(len, bags.values()))


def main() -> None:
    nu, nv = neighbours("u"), neighbours("v")
    assert len(VERTICES) == 11 and len(EDGES) == 25
    assert not adjacent("u", "v") and len(nu) == len(nv) == 8
    assert independence_number(nu) == independence_number(nv) == 3
    assert not contains_clique(nu, 4) and not contains_clique(nv, 4)

    internal = {"x1", "x2", "y1", "y2", "y3", "z1", "z2"}
    assert all(adjacent("u", s) and adjacent(s, "v") for s in internal)
    assert len(internal) == 7

    max_bag_size = verify_tree_decomposition()
    assert max_bag_size == 5

    print("GREEN K7-minus bad-pair seven-path barrier")
    print("graph vertices=11 edges=25 degrees_u_v=8,8 uv_edge=no")
    print("neighbourhoods=K3+K3+K2 alpha=3 K4=no")
    print("internally_disjoint_u_v_paths=7")
    print("tree_decomposition=yes max_bag_size=5 treewidth_upper_bound=4")
    print("K7_minus_minor=no")


if __name__ == "__main__":
    main()
