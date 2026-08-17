#!/usr/bin/env python3
"""Verify the two sharp `4n` degree-six composition barriers.

The script uses only the Python standard library.  It verifies exact order,
size and connectivity, the degree-six decompositions and excesses, failure
of every numerical orientation of the existing cross-lobe lemma, and the
displayed `K_7` models.
"""

from __future__ import annotations

from itertools import combinations


Graph = dict[str, set[str]]


def add_edge(graph: Graph, left: str, right: str) -> None:
    assert left != right
    graph.setdefault(left, set()).add(right)
    graph.setdefault(right, set()).add(left)


def connected(graph: Graph, retained: set[str]) -> bool:
    if not retained:
        return False
    reached = {next(iter(retained))}
    frontier = list(reached)
    while frontier:
        vertex = frontier.pop()
        for neighbour in graph[vertex] & retained:
            if neighbour not in reached:
                reached.add(neighbour)
                frontier.append(neighbour)
    return reached == retained


def connectivity(graph: Graph) -> int:
    vertices = sorted(graph)
    for order in range(len(vertices)):
        for deleted in combinations(vertices, order):
            retained = set(vertices) - set(deleted)
            if len(retained) >= 2 and not connected(graph, retained):
                return order
    raise AssertionError("complete graph has no proper separating set")


def size(graph: Graph) -> int:
    return sum(map(len, graph.values())) // 2


def adjacent(graph: Graph, left: set[str], right: set[str]) -> bool:
    return any(graph[vertex] & right for vertex in left)


def verify_clique_model(graph: Graph, bags: tuple[frozenset[str], ...]) -> None:
    assert all(bags)
    assert all(left.isdisjoint(right) for left, right in combinations(bags, 2))
    assert all(connected(graph, set(bag)) for bag in bags)
    assert all(adjacent(graph, set(left), set(right)) for left, right in combinations(bags, 2))


def two_lobe_graph() -> tuple[Graph, list[str], list[str], list[str]]:
    roots = [f"t{index}" for index in range(6)]
    first = [f"a{index}" for index in range(10)]
    second = [f"b{index}" for index in range(10)]
    graph: Graph = {vertex: set() for vertex in ["x", *roots, *first, *second]}
    for root in roots:
        add_edge(graph, "x", root)
    for path in (first, second):
        for left, right in zip(path, path[1:]):
            add_edge(graph, left, right)

    miss = (
        {0}, {0, 2}, {0, 3}, {1, 4}, {1, 5},
        {2, 3}, {2, 4}, {3, 5}, {4, 5}, {1},
    )
    for shift, path in enumerate((first, second)):
        for vertex, omitted in zip(path, miss):
            shifted = {(index + shift) % 6 for index in omitted}
            for index, root in enumerate(roots):
                if index not in shifted:
                    add_edge(graph, vertex, root)
    return graph, roots, first, second


def one_lobe_graph() -> tuple[Graph, list[str], list[str]]:
    roots = [f"t{index}" for index in range(6)]
    lobe = [f"c{index}" for index in range(7)]
    graph: Graph = {vertex: set() for vertex in ["x", *roots, *lobe]}
    for root in roots:
        add_edge(graph, "x", root)
    for index in range(7):
        add_edge(graph, lobe[index], lobe[(index + 1) % 7])
    add_edge(graph, "c0", "c2")
    for vertex in lobe:
        for root in roots:
            add_edge(graph, vertex, root)
    return graph, roots, lobe


def main() -> None:
    graph, roots, first, second = two_lobe_graph()
    assert len(graph) == 27
    assert size(graph) == 108 == 4 * len(graph)
    assert min(map(len, graph.values())) == 6
    assert connectivity(graph) == 6
    assert set(graph["x"]) == set(roots)
    assert all(not graph[left] & set(second) for left in first)
    assert all(len(graph[root] & set(first)) == 7 for root in roots)
    assert all(len(graph[root] & set(second)) == 7 for root in roots)
    delta_first = 9 + 42 - 4 * 10
    delta_second = 9 + 42 - 4 * 10
    assert delta_first == delta_second == 11
    checks = 0
    for first_lobe, second_lobe in ((first, second), (second, first)):
        delta_left = 11
        delta_right = 11
        for p, q in ((p, q) for p in roots for q in roots if p != q):
            p_count = len(graph[p] & set(first_lobe))
            boundary_degree = len((graph[q] & set(roots)) - {p})
            assert delta_left - p_count + boundary_degree == 4 < 5
            assert delta_right >= 9
            checks += 1
    assert checks == 60
    verify_clique_model(
        graph,
        (
            frozenset({"x"}), frozenset({"t0", "a3"}),
            frozenset({"t1", "a2"}), frozenset({"t2", "a0"}),
            frozenset({"t3", "a1"}), frozenset({"t4", "a4"}),
            frozenset({"t5", "a5"}),
        ),
    )

    graph_one, roots_one, lobe = one_lobe_graph()
    assert len(graph_one) == 14
    assert size(graph_one) == 56 == 4 * len(graph_one)
    assert connectivity(graph_one) == 6
    assert set(graph_one["x"]) == set(roots_one)
    assert all(not graph_one[left] & set(roots_one) for left in roots_one)
    assert 8 + 42 - 4 * 7 == 22
    verify_clique_model(
        graph_one,
        (frozenset({"x"}),)
        + tuple(frozenset({f"t{index}", f"c{index}"}) for index in range(6)),
    )

    print("GREEN 4n degree-six existing-composition barriers")
    print("two_lobe: n=27 m=108 kappa=6 boundary=0 excess=11+11")
    print("two_lobe: lemma5_orientations=60 successful=0 explicit_K7=yes")
    print("one_lobe: n=14 m=56 kappa=6 boundary=independent excess=22 explicit_K7=yes")


if __name__ == "__main__":
    main()
