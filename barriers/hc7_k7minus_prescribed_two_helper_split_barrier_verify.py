#!/usr/bin/env python3
"""Verify two sharp barriers to a prescribed two-helper factorisation.

The script uses only the Python standard library.  It checks the exact
graphs, six-connectivity, the universal unprescribed factorisation for every
four-set, failure for the displayed prescribed helper pair, and the displayed
K_7^- minor model.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations


Edge = tuple[int, int]
Bag = frozenset[int]


def edge(u: int, v: int) -> Edge:
    assert u != v
    return (u, v) if u < v else (v, u)


def graph(vertices: range, edges: set[Edge]) -> dict[int, set[int]]:
    adj = {v: set() for v in vertices}
    for u, v in edges:
        assert u in adj and v in adj and u != v
        adj[u].add(v)
        adj[v].add(u)
    return adj


def connected(adj: dict[int, set[int]], vertices: set[int] | Bag) -> bool:
    if not vertices:
        return False
    todo = [next(iter(vertices))]
    seen: set[int] = set()
    while todo:
        v = todo.pop()
        if v in seen:
            continue
        seen.add(v)
        todo.extend((adj[v] & set(vertices)) - seen)
    return seen == set(vertices)


def adjacent(adj: dict[int, set[int]], left: set[int] | Bag,
             right: set[int] | Bag) -> bool:
    return any(adj[v] & set(right) for v in left)


def is_factorisation(adj: dict[int, set[int]], roots: set[int],
                     left: set[int], right: set[int]) -> bool:
    vertices = set(adj)
    if not left or not right:
        return False
    if roots | left | right != vertices:
        return False
    if (roots & left) or (roots & right) or (left & right):
        return False
    return (
        connected(adj, left)
        and connected(adj, right)
        and adjacent(adj, left, right)
        and all(adj[z] & left and adj[z] & right for z in roots)
    )


def factorisations(adj: dict[int, set[int]], roots: set[int],
                   prescribed: tuple[int, int] | None = None
                   ) -> list[tuple[set[int], set[int]]]:
    remainder = sorted(set(adj) - roots)
    assert len(roots) == 4 and len(remainder) >= 2
    if prescribed is None:
        fixed_left = remainder[0]
        free = remainder[1:]
        fixed_right = None
    else:
        fixed_left, fixed_right = prescribed
        assert fixed_left in remainder and fixed_right in remainder
        free = [v for v in remainder if v not in prescribed]

    answer = []
    for mask in range(1 << len(free)):
        left = {fixed_left}
        left.update(v for i, v in enumerate(free) if mask & (1 << i))
        right = set(remainder) - left
        if fixed_right is not None and fixed_right not in right:
            continue
        if is_factorisation(adj, roots, left, right):
            answer.append((left, right))
    return answer


def check_six_connectivity(adj: dict[int, set[int]], cut: set[int]) -> None:
    vertices = sorted(adj)
    for order in range(6):
        for deleted_tuple in combinations(vertices, order):
            deleted = set(deleted_tuple)
            assert connected(adj, set(vertices) - deleted)
    assert len(cut) == 6
    assert not connected(adj, set(vertices) - cut)


def check_k7_minus_model(adj: dict[int, set[int]], bags: tuple[Bag, ...],
                         expected_missing: tuple[int, int]) -> None:
    assert len(bags) == 7
    assert all(bags)
    assert all(left.isdisjoint(right) for left, right in combinations(bags, 2))
    assert all(connected(adj, bag) for bag in bags)
    missing = tuple(
        (i, j)
        for i, j in combinations(range(7), 2)
        if not adjacent(adj, bags[i], bags[j])
    )
    assert missing == (expected_missing,)


def universal_counts(adj: dict[int, set[int]]) -> tuple[int, int, str]:
    counts = []
    certificate_lines = []
    for roots_tuple in combinations(sorted(adj), 4):
        roots = set(roots_tuple)
        found = factorisations(adj, roots)
        assert found
        counts.append(len(found))
        left, right = found[0]
        certificate_lines.append(
            f"{','.join(map(str, roots_tuple))}:"
            f"{','.join(map(str, sorted(left)))}|"
            f"{','.join(map(str, sorted(right)))}"
        )
    digest = sha256("\n".join(certificate_lines).encode()).hexdigest()
    return min(counts), max(counts), digest


def first_graph() -> tuple[dict[int, set[int]], set[Edge]]:
    vertices = range(10)
    missing = {
        edge(2, 5), edge(2, 6), edge(2, 8), edge(3, 4), edge(3, 7),
        edge(3, 8), edge(4, 6), edge(4, 9), edge(5, 7), edge(5, 9),
        edge(6, 7),
    }
    edges = {
        edge(u, v)
        for u, v in combinations(vertices, 2)
        if edge(u, v) not in missing
    }
    return graph(vertices, edges), edges


def second_graph() -> tuple[dict[int, set[int]], set[Edge]]:
    # This is a relabelling of the icosahedron used by NetworkX, followed by
    # a universal apex 12 and the four chords 13, 14, 17, 18.
    icosahedron = {
        edge(0, 1), edge(0, 3), edge(0, 5), edge(0, 9), edge(0, 11),
        edge(1, 2), edge(1, 5), edge(1, 6), edge(1, 9),
        edge(2, 6), edge(2, 8), edge(2, 9), edge(2, 10),
        edge(3, 4), edge(3, 8), edge(3, 9), edge(3, 11),
        edge(4, 7), edge(4, 8), edge(4, 10), edge(4, 11),
        edge(5, 6), edge(5, 7), edge(5, 11),
        edge(6, 7), edge(6, 10),
        edge(7, 10), edge(7, 11),
        edge(8, 9), edge(8, 10),
    }
    chords = {edge(1, 3), edge(1, 4), edge(1, 7), edge(1, 8)}
    apex = {edge(12, v) for v in range(12)}
    edges = icosahedron | chords | apex
    assert len(icosahedron) == 30 and len(chords) == 4
    return graph(range(13), edges), edges


def main() -> None:
    h1, edges1 = first_graph()
    assert len(h1) == 10 and len(edges1) == 34 == 4 * len(h1) - 6
    assert min(map(len, h1.values())) == 6
    check_six_connectivity(h1, set(h1[2]))
    z1 = {0, 1, 2, 3}
    assert not factorisations(h1, z1, (4, 5))
    assert sum(not adjacent(h1, {u}, {v}) for u, v in combinations(z1, 2)) == 0
    bags1 = (
        frozenset({0}), frozenset({1}), frozenset({2, 3, 6}),
        frozenset({4}), frozenset({5}), frozenset({7}), frozenset({8}),
    )
    check_k7_minus_model(h1, bags1, (4, 5))
    minimum1, maximum1, digest1 = universal_counts(h1)

    h2, edges2 = second_graph()
    assert len(h2) == 13 and len(edges2) == 46 == 4 * len(h2) - 6
    assert min(map(len, h2.values())) == 6
    check_six_connectivity(h2, set(h2[0]))
    z2 = {0, 1, 2, 12}
    assert not factorisations(h2, z2, (5, 6))
    assert sum(not adjacent(h2, {u}, {v}) for u, v in combinations(z2, 2)) == 1
    bags2 = (
        frozenset({3}), frozenset({7}), frozenset({2, 5, 6, 8}),
        frozenset({1, 9}), frozenset({4, 10}), frozenset({0, 11}),
        frozenset({12}),
    )
    check_k7_minus_model(h2, bags2, (0, 1))
    minimum2, maximum2, digest2 = universal_counts(h2)

    print("GREEN prescribed two-helper split barriers")
    print(
        "H1: n=10 m=34 kappa=6 delta=6 "
        f"universal_factorisations={minimum1}..{maximum1} digest={digest1}"
    )
    print("H1: Z=0123 prescribed=4|5 split=false K7_minus_missing=5|7")
    print(
        "H2: n=13 m=46 kappa=6 delta=6 "
        f"universal_factorisations={minimum2}..{maximum2} digest={digest2}"
    )
    print("H2: Z=012a prescribed=5|6 split=false K7_minus_missing=3|7")


if __name__ == "__main__":
    main()
