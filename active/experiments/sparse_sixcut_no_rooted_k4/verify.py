#!/usr/bin/env python3
"""Exact verifier for the independent-boundary equality residue.

The mathematical reduction leaves a tree C of order 5 or 7 and six
boundary roots.  At order 5 each root misses one tree vertex and the
number h(v) of roots missing v satisfies h(v) <= d_C(v).  At order 7
each root misses two tree vertices and the six missed pairs form a
loopless multigraph whose degree at v is exactly d_C(v).

For every resulting profile and every four boundary roots, this verifier
finds four distinct tree vertices v_i such that the four two-vertex bags
{root_i,v_i} are connected and pairwise adjacent.  They are therefore a
rooted K_4 model.  The enumeration uses no non-standard package.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Sequence
from hashlib import sha256
from itertools import combinations, permutations, product


Edge = tuple[int, int]


def tree_from_prufer(sequence: Sequence[int], order: int) -> tuple[Edge, ...]:
    degrees = [1] * order
    for vertex in sequence:
        degrees[vertex] += 1

    edges: list[Edge] = []
    for vertex in sequence:
        leaf = next(index for index, degree in enumerate(degrees) if degree == 1)
        edges.append(tuple(sorted((leaf, vertex))))
        degrees[leaf] -= 1
        degrees[vertex] -= 1
    last = [index for index, degree in enumerate(degrees) if degree == 1]
    assert len(last) == 2
    edges.append(tuple(sorted(last)))
    return tuple(edges)


def canonical_tree_code(edges: Sequence[Edge], order: int) -> str:
    adjacency = [set() for _ in range(order)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)

    alive = set(range(order))
    while len(alive) > 2:
        leaves = [
            vertex
            for vertex in alive
            if len(adjacency[vertex].intersection(alive)) <= 1
        ]
        alive.difference_update(leaves)

    def rooted_code(vertex: int, parent: int) -> str:
        children = sorted(
            rooted_code(child, vertex)
            for child in adjacency[vertex]
            if child != parent
        )
        return "(" + "".join(children) + ")"

    return min(rooted_code(centre, -1) for centre in alive)


def tree_shapes(order: int) -> list[tuple[Edge, ...]]:
    representatives: dict[str, tuple[Edge, ...]] = {}
    sequence_count = 0
    for sequence in product(range(order), repeat=order - 2):
        sequence_count += 1
        edges = tree_from_prufer(sequence, order)
        representatives.setdefault(canonical_tree_code(edges, order), edges)
    assert sequence_count == order ** (order - 2)
    return [representatives[code] for code in sorted(representatives)]


def bounded_compositions(
    total: int, caps: Sequence[int], prefix: tuple[int, ...] = ()
) -> Iterator[tuple[int, ...]]:
    if len(caps) == 1:
        if total <= caps[0]:
            yield prefix + (total,)
        return
    for value in range(min(total, caps[0]) + 1):
        yield from bounded_compositions(
            total - value, caps[1:], prefix + (value,)
        )


def multigraphs_with_degrees(degrees: Sequence[int]) -> Iterator[tuple[Edge, ...]]:
    """Enumerate loopless edge multisets with the prescribed degrees."""

    seen: set[tuple[Edge, ...]] = set()

    def recurse(remaining: tuple[int, ...], edges: tuple[Edge, ...]) -> Iterator[tuple[Edge, ...]]:
        try:
            left = next(index for index, degree in enumerate(remaining) if degree)
        except StopIteration:
            key = tuple(sorted(edges))
            if key not in seen:
                seen.add(key)
                yield key
            return

        mutable = list(remaining)
        mutable[left] -= 1
        for right in range(len(mutable)):
            if right == left or mutable[right] == 0:
                continue
            mutable[right] -= 1
            edge = tuple(sorted((left, right)))
            yield from recurse(tuple(mutable), edges + (edge,))
            mutable[right] += 1

    yield from recurse(tuple(degrees), ())


def degrees(edges: Sequence[Edge], order: int) -> tuple[int, ...]:
    answer = [0] * order
    for left, right in edges:
        answer[left] += 1
        answer[right] += 1
    return tuple(answer)


def verify_two_vertex_bags(
    tree_edges: Sequence[Edge],
    misses: Sequence[frozenset[int]],
    roots: Sequence[int],
    vertices: Sequence[int],
) -> bool:
    """Check the four bags {root_i,vertices[i]} literally."""

    if len(set(vertices)) != 4:
        return False
    if any(vertices[index] in misses[root] for index, root in enumerate(roots)):
        return False

    tree_edge_set = set(tree_edges)
    for first, second in combinations(range(4), 2):
        v_first, v_second = vertices[first], vertices[second]
        r_first, r_second = roots[first], roots[second]
        adjacent = (
            v_second not in misses[r_first]
            or v_first not in misses[r_second]
            or tuple(sorted((v_first, v_second))) in tree_edge_set
        )
        if not adjacent:
            return False
    return True


def first_two_vertex_model(
    tree_edges: Sequence[Edge],
    misses: Sequence[frozenset[int]],
    roots: Sequence[int],
) -> tuple[int, ...] | None:
    order = len(tree_edges) + 1
    for vertices in permutations(range(order), 4):
        if verify_two_vertex_bags(tree_edges, misses, roots, vertices):
            return vertices
    return None


def order_five_profiles(
    tree_edges: Sequence[Edge],
) -> Iterable[tuple[str, tuple[frozenset[int], ...]]]:
    tree_degrees = degrees(tree_edges, 5)
    for missing_counts in bounded_compositions(6, tree_degrees):
        misses = tuple(
            frozenset((vertex,))
            for vertex, count in enumerate(missing_counts)
            for _ in range(count)
        )
        assert len(misses) == 6
        yield repr(missing_counts), misses


def order_seven_profiles(
    tree_edges: Sequence[Edge],
) -> Iterable[tuple[str, tuple[frozenset[int], ...]]]:
    tree_degrees = degrees(tree_edges, 7)
    for missing_edges in multigraphs_with_degrees(tree_degrees):
        misses = tuple(frozenset(edge) for edge in missing_edges)
        assert len(misses) == 6
        assert degrees(missing_edges, 7) == tree_degrees
        yield repr(missing_edges), misses


def verify_order(order: int) -> tuple[int, int, tuple[int, ...], str]:
    shapes = tree_shapes(order)
    expected_shape_count = {5: 3, 7: 11}[order]
    assert len(shapes) == expected_shape_count

    profile_count = 0
    four_set_count = 0
    per_shape: list[int] = []
    transcript = sha256()

    for tree_edges in shapes:
        code = canonical_tree_code(tree_edges, order)
        profile_source = (
            order_five_profiles(tree_edges)
            if order == 5
            else order_seven_profiles(tree_edges)
        )
        shape_profiles = 0
        for profile_code, misses in profile_source:
            profile_count += 1
            shape_profiles += 1
            for roots in combinations(range(6), 4):
                witness = first_two_vertex_model(tree_edges, misses, roots)
                assert witness is not None
                assert verify_two_vertex_bags(tree_edges, misses, roots, witness)
                four_set_count += 1
                transcript.update(
                    f"{order}|{code}|{profile_code}|{roots}|{witness}\n".encode()
                )
        per_shape.append(shape_profiles)

    expected_profiles = {5: 36, 7: 1149}[order]
    assert profile_count == expected_profiles
    assert four_set_count == 15 * profile_count
    return profile_count, four_set_count, tuple(per_shape), transcript.hexdigest()


def main() -> None:
    five = verify_order(5)
    seven = verify_order(7)

    assert five[2] == (12, 13, 11)
    assert seven[2] == (160, 160, 252, 15, 66, 55, 107, 107, 160, 66, 1)
    assert five[3] == "c78743f57d3a36bf6ca87f1a9e339e1f2f09cd53832ad6805f73e9f606ecacf7"
    assert seven[3] == "a5d70b88bfb125047b3cb2d3b3a9f0acfdfd5d7741c5aaac11ec66390c76ae1d"

    print("tree_shapes", {5: 3, 7: 11})
    print("order5_profiles", five[0])
    print("order5_four_sets_verified", five[1])
    print("order5_profiles_by_shape", five[2])
    print("order5_witness_digest", five[3])
    print("order7_profiles", seven[0])
    print("order7_four_sets_verified", seven[1])
    print("order7_profiles_by_shape", seven[2])
    print("order7_witness_digest", seven[3])
    print("verdict GREEN")


if __name__ == "__main__":
    main()
