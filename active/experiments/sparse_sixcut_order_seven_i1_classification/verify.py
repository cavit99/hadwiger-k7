#!/usr/bin/env python3
"""Exhaust the six-vertex core in the order-seven i=1 Hall return."""

from itertools import combinations, permutations


ORDER = 6
FULL = (1 << ORDER) - 1
VERTICES = tuple(range(ORDER))
PAIRS = tuple(combinations(VERTICES, 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
PERMUTATIONS = tuple(permutations(VERTICES))


def set_partitions(vertices, count):
    """Yield each unlabelled partition into ``count`` nonempty blocks once."""
    vertices = tuple(vertices)
    blocks = []

    def visit(position):
        if position == len(vertices):
            if len(blocks) == count:
                yield tuple(
                    sum(1 << vertex for vertex in block) for block in blocks
                )
            return

        vertex = vertices[position]
        for block in blocks:
            block.append(vertex)
            yield from visit(position + 1)
            block.pop()
        if len(blocks) < count:
            blocks.append([vertex])
            yield from visit(position + 1)
            blocks.pop()

    yield from visit(0)


def vertices(mask):
    return tuple(vertex for vertex in VERTICES if mask >> vertex & 1)


SPANNING_K4_MODELS = tuple(set_partitions(VERTICES, 4))
NONSPANNING_K4_MODELS = tuple(
    partition
    for used in range(1, FULL)
    if used.bit_count() >= 4
    for partition in set_partitions(vertices(used), 4)
)
K5_MODELS = tuple(
    partition
    for used in range(1, FULL + 1)
    if used.bit_count() >= 5
    for partition in set_partitions(vertices(used), 5)
)


def adjacency(graph):
    answer = [0] * ORDER
    for index, (left, right) in enumerate(PAIRS):
        if graph >> index & 1:
            answer[left] |= 1 << right
            answer[right] |= 1 << left
    return tuple(answer)


def connected(mask, neighbourhoods):
    reached = mask & -mask
    while True:
        old = reached
        for vertex in VERTICES:
            if reached >> vertex & 1:
                reached |= neighbourhoods[vertex] & mask
        if reached == old:
            return reached == mask


def is_near_clique_model(partition, neighbourhoods):
    if any(not connected(bag, neighbourhoods) for bag in partition):
        return False
    missing = 0
    for left, right in combinations(partition, 2):
        if not any(
            neighbourhoods[vertex] & right
            for vertex in VERTICES
            if left >> vertex & 1
        ):
            missing += 1
            if missing > 1:
                return False
    return True


def has_model(partitions, neighbourhoods):
    return any(
        is_near_clique_model(partition, neighbourhoods)
        for partition in partitions
    )


def edge_mask(edges):
    return sum(
        1 << PAIR_INDEX[tuple(sorted(edge))]
        for edge in edges
    )


def theta(lengths):
    edges = []
    next_vertex = 2
    for length in lengths:
        path = [0]
        path.extend(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        path.append(1)
        edges.extend(zip(path, path[1:]))
    assert next_vertex == ORDER
    return edge_mask(edges)


def permuted(graph, permutation):
    answer = 0
    for index, (left, right) in enumerate(PAIRS):
        if graph >> index & 1:
            image = tuple(sorted((permutation[left], permutation[right])))
            answer |= 1 << PAIR_INDEX[image]
    return answer


def canonical(graph):
    return min(permuted(graph, permutation) for permutation in PERMUTATIONS)


def main():
    assert len(SPANNING_K4_MODELS) == 65
    assert len(NONSPANNING_K4_MODELS) == 75
    assert len(K5_MODELS) == 21

    theta_classes = {
        canonical(theta((2, 2, 3))): ("Theta(2,2,3)", 180),
        canonical(theta((1, 2, 4))): ("Theta(1,2,4)", 360),
        canonical(theta((1, 3, 3))): ("Theta(1,3,3)", 180),
    }
    assert len(theta_classes) == 3

    survivors = []
    class_counts = {representative: 0 for representative in theta_classes}
    for graph in range(1 << len(PAIRS)):
        neighbourhoods = adjacency(graph)
        if not has_model(SPANNING_K4_MODELS, neighbourhoods):
            continue
        if has_model(NONSPANNING_K4_MODELS, neighbourhoods):
            continue
        if has_model(K5_MODELS, neighbourhoods):
            continue
        representative = canonical(graph)
        assert representative in theta_classes
        assert graph.bit_count() == 7
        survivors.append(graph)
        class_counts[representative] += 1

    assert len(survivors) == 720
    for representative, (name, expected) in theta_classes.items():
        actual = class_counts[representative]
        assert actual == expected
        print(f"{name}: labelled_survivors={actual}")
    print("total_labelled_survivors=720 all_have_7_edges")
    print("order-seven i=1 core classification: PASS")


if __name__ == "__main__":
    main()
