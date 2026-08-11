#!/usr/bin/env python3
"""Verify the paired-donor overlap and private-inflation barrier."""

from __future__ import annotations

from itertools import combinations


def add_edge(graph: dict[str, set[str]], left: str, right: str) -> None:
    graph[left].add(right)
    graph[right].add(left)


def build_graph() -> dict[str, set[str]]:
    vertices = {
        *(f"{letter}{index}" for index in (1, 2) for letter in "abcrw"),
        *(f"t{index}" for index in range(1, 6)),
        "f",
    }
    graph = {vertex: set() for vertex in vertices}
    for index in (1, 2):
        donor = tuple(f"{letter}{index}" for letter in "abcr")
        for left, right in combinations(donor, 2):
            add_edge(graph, left, right)
        add_edge(graph, f"r{index}", f"w{index}")
        add_edge(graph, f"c{index}", f"w{index}")
        for terminal in range(1, 6):
            add_edge(graph, f"a{index}", f"t{terminal}")
        for terminal in range(2, 6):
            add_edge(graph, f"r{index}", f"t{terminal}")
    add_edge(graph, "a1", "a2")
    add_edge(graph, "f", "w1")
    add_edge(graph, "f", "w2")
    add_edge(graph, "f", "t1")
    return graph


def edges(graph: dict[str, set[str]]) -> set[frozenset[str]]:
    return {
        frozenset((left, right))
        for left in graph
        for right in graph[left]
        if left < right
    }


def neighbourhood(graph: dict[str, set[str]], vertices: set[str]) -> set[str]:
    return set().union(*(graph[vertex] for vertex in vertices)) - vertices


def connected(
    graph: dict[str, set[str]], vertices: set[str], removed: set[str] | None = None
) -> bool:
    kept = vertices - (removed or set())
    if not kept:
        return True
    reached = {next(iter(kept))}
    frontier = list(reached)
    while frontier:
        vertex = frontier.pop()
        for neighbour in graph[vertex] & kept - reached:
            reached.add(neighbour)
            frontier.append(neighbour)
    return reached == kept


def components_after(
    graph: dict[str, set[str]], removed: set[str]
) -> list[set[str]]:
    unseen = set(graph) - removed
    components = []
    while unseen:
        component = {next(iter(unseen))}
        frontier = list(component)
        unseen -= component
        while frontier:
            vertex = frontier.pop()
            new = graph[vertex] & unseen
            unseen -= new
            component |= new
            frontier.extend(new)
        components.append(component)
    return components


def verify_tree_decomposition(graph: dict[str, set[str]]) -> int:
    bags = (
        frozenset({"a1", "a2", "f", "r1", "r2"}),
        frozenset({"a1", "a2", "r1", "r2", "t2"}),
        frozenset({"a1", "a2", "r1", "r2", "t3"}),
        frozenset({"a1", "a2", "r1", "r2", "t4"}),
        frozenset({"a1", "a2", "r1", "r2", "t5"}),
        frozenset({"a1", "a2", "f", "t1"}),
        frozenset({"a1", "b1", "c1", "r1"}),
        frozenset({"a1", "c1", "r1", "w1"}),
        frozenset({"a1", "f", "r1", "w1"}),
        frozenset({"a2", "b2", "c2", "r2"}),
        frozenset({"a2", "c2", "r2", "w2"}),
        frozenset({"a2", "f", "r2", "w2"}),
    )
    tree_edges = {
        frozenset((0, index)) for index in (1, 2, 3, 4, 5, 8, 11)
    } | {frozenset((8, 7)), frozenset((7, 6)), frozenset((11, 10)), frozenset((10, 9))}
    tree = {index: set() for index in range(len(bags))}
    for edge in tree_edges:
        left, right = tuple(edge)
        tree[left].add(right)
        tree[right].add(left)
    assert len(tree_edges) == len(bags) - 1
    assert connected(tree, set(tree))
    assert set().union(*bags) == set(graph)
    assert all(any(edge <= bag for bag in bags) for edge in edges(graph))
    for vertex in graph:
        containing = {index for index, bag in enumerate(bags) if vertex in bag}
        assert connected(tree, containing)
    return max(map(len, bags)) - 1


def main() -> None:
    graph = build_graph()
    assert len(graph) == 16
    assert len(edges(graph)) == 38

    deleted_edge = frozenset(("a1", "a2"))
    fixed_colouring = {
        "a1": 0,
        "a2": 0,
        "f": 0,
        "r1": 1,
        "r2": 1,
        "t1": 1,
        "b1": 2,
        "b2": 2,
        "t2": 2,
        "c1": 3,
        "c2": 3,
        "t3": 3,
        "w1": 4,
        "w2": 4,
        "t4": 4,
        "t5": 5,
    }
    monochromatic = {
        edge
        for edge in edges(graph)
        if len({fixed_colouring[vertex] for vertex in edge}) == 1
    }
    assert monochromatic == {deleted_edge}

    four_colouring = {
        "a1": 0,
        "a2": 1,
        "b1": 3,
        "b2": 3,
        "c1": 2,
        "c2": 2,
        "f": 3,
        "r1": 1,
        "r2": 0,
        "t1": 2,
        "t2": 2,
        "t3": 2,
        "t4": 2,
        "t5": 2,
        "w1": 0,
        "w2": 1,
    }
    assert all(
        four_colouring[left] != four_colouring[right]
        for left, right in map(tuple, edges(graph))
    )

    palette = set(range(6))
    donors = {}
    for index, other in ((1, 2), (2, 1)):
        donor = {f"a{index}", f"b{index}", f"c{index}", f"r{index}"}
        bag = donor | {f"w{index}"}
        boundary = neighbourhood(graph, donor)
        expected_boundary = {
            f"a{other}",
            f"w{index}",
            *(f"t{terminal}" for terminal in range(1, 6)),
        }
        assert boundary == expected_boundary
        assert connected(graph, donor)
        assert connected(graph, bag - donor)
        assert "f" not in boundary and not graph["f"] & donor
        components = components_after(graph, boundary)
        assert any(donor <= component for component in components)
        assert any("f" in component for component in components)

        endpoint = f"a{index}"
        endpoint_list = palette - {
            fixed_colouring[vertex] for vertex in graph[endpoint] & boundary
        }
        assert endpoint_list == set()

        smaller = {f"r{index}"}
        smaller_boundary = neighbourhood(graph, smaller)
        assert len(smaller_boundary) == 8 > len(boundary) == 7
        assert connected(graph, smaller)
        assert connected(graph, bag - smaller)
        smaller_components = components_after(graph, smaller_boundary)
        assert any(smaller <= component for component in smaller_components)
        assert any("f" in component for component in smaller_components)
        protected = {f"w{index}", *(f"t{terminal}" for terminal in range(2, 6))}
        assert protected <= smaller_boundary
        smaller_list = palette - {
            fixed_colouring[vertex]
            for vertex in graph[f"r{index}"] & smaller_boundary
        }
        assert smaller_list == {1}
        assert fixed_colouring[f"r{index}"] in smaller_list
        donors[index] = (donor, boundary)

    donor_union = donors[1][0] | donors[2][0]
    joint_boundary = neighbourhood(graph, donor_union)
    assert joint_boundary == {"w1", "w2", *(f"t{index}" for index in range(1, 6))}
    assert len(joint_boundary) == 7
    for endpoint in ("a1", "a2"):
        allowed = palette - {
            fixed_colouring[vertex] for vertex in graph[endpoint] & joint_boundary
        }
        assert allowed == {0}
    assert "a2" in donors[1][1] and "a1" in donors[2][1]
    assert donors[1][1] & donors[2][1] == {
        *(f"t{index}" for index in range(1, 6))
    }

    vertices = set(graph)
    assert all(
        connected(graph, vertices, set(removed))
        for order in range(3)
        for removed in combinations(vertices, order)
    )
    assert not connected(graph, vertices, set(graph["b1"]))
    assert min(map(len, graph.values())) == 3

    width = verify_tree_decomposition(graph)
    assert width == 4
    print(
        "GREEN paired-donor overlap barrier:",
        {"vertices": 16, "edges": 38, "connectivity": 3, "treewidth_upper_bound": width},
    )


if __name__ == "__main__":
    main()
