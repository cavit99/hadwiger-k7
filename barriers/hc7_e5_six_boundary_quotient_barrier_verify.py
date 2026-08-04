#!/usr/bin/env python3
"""Verify the six-boundary quotient barrier to a forced K_7^- minor."""

from hashlib import sha256
from itertools import combinations


VERTICES = ("s0", "s1", "s2", "s3", "s4", "p", "x", "y", "q", "c")
INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
S = frozenset(range(5))
EXPECTED_DIGEST = "e6f4284228d49e3143df81b07c311cb5a23a77014ac86124a3a2e3d8bb653ded"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pair(left, right):
    require(left != right, "loops are not allowed")
    return tuple(sorted((INDEX[left], INDEX[right])))


EDGES = {
    pair("s0", "s1"),
    pair("s1", "s2"),
    pair("s3", "s4"),
}
EDGES.update(pair("p", vertex) for vertex in ("s0", "s2", "s3"))
EDGES.update(pair(vertex, root) for vertex in ("x", "y") for root in VERTICES[:5])
EDGES.update(pair("q", vertex) for vertex in ("p", "s0", "s2", "s3", "s4"))
EDGES.update(pair("c", vertex) for vertex in VERTICES[:6])

ADJACENCY = [set() for _ in VERTICES]
for left, right in EDGES:
    ADJACENCY[left].add(right)
    ADJACENCY[right].add(left)


def named_neighbours(vertex):
    return {VERTICES[index] for index in ADJACENCY[INDEX[vertex]]}


def check_construction():
    require(len(VERTICES) == 10, "wrong vertex count")
    require(len(EDGES) == 27, "wrong edge count")
    require(
        {edge for edge in EDGES if set(edge) <= S}
        == {pair("s0", "s1"), pair("s1", "s2"), pair("s3", "s4")},
        "wrong graph induced by S",
    )
    require(
        named_neighbours("p") & set(VERTICES[:5]) == {"s0", "s2", "s3"},
        "wrong p contacts",
    )
    require(named_neighbours("x") == set(VERTICES[:5]), "wrong x contacts")
    require(named_neighbours("y") == set(VERTICES[:5]), "wrong y contacts")
    require(named_neighbours("q") == {"p", "s0", "s2", "s3", "s4"}, "wrong q contacts")
    require(named_neighbours("c") == set(VERTICES[:6]), "wrong c contacts")
    exterior = {INDEX[vertex] for vertex in ("x", "y", "q", "c")}
    require(
        not any(set(edge) <= exterior for edge in EDGES),
        "exterior vertices are not independent",
    )


def seven_partitions(items):
    """Yield every unlabelled partition of items into seven nonempty parts."""

    blocks = [[items[0]]]

    def extend(position):
        if position == len(items):
            if len(blocks) == 7:
                yield tuple(tuple(block) for block in blocks)
            return
        if len(blocks) + len(items) - position < 7:
            return

        vertex = items[position]
        for block in blocks:
            block.append(vertex)
            yield from extend(position + 1)
            block.pop()
        if len(blocks) < 7:
            blocks.append([vertex])
            yield from extend(position + 1)
            blocks.pop()

    yield from extend(1)


def connected(branch_set):
    target = set(branch_set)
    reached = {branch_set[0]}
    stack = [branch_set[0]]
    while stack:
        vertex = stack.pop()
        new_vertices = (ADJACENCY[vertex] & target) - reached
        reached.update(new_vertices)
        stack.extend(sorted(new_vertices))
    return reached == target


def missing_branch_pair_count(partition):
    return sum(
        not any(
            vertex_right in ADJACENCY[vertex_left]
            for vertex_left in partition[left]
            for vertex_right in partition[right]
        )
        for left, right in combinations(range(7), 2)
    )


def display(partition):
    return " | ".join(
        "{" + ",".join(VERTICES[vertex] for vertex in branch_set) + "}"
        for branch_set in partition
    )


def verify_minor_exclusion():
    digest = sha256()
    totals = {size: 0 for size in range(7, 11)}
    connected_totals = {size: 0 for size in range(7, 11)}
    minimum_missing = 22
    closest_partition = None

    for size in range(7, 11):
        for used in combinations(range(len(VERTICES)), size):
            for partition in seven_partitions(used):
                totals[size] += 1
                is_connected = all(connected(branch_set) for branch_set in partition)
                missing_count = missing_branch_pair_count(partition) if is_connected else -1
                encoded = ";".join(",".join(map(str, branch_set)) for branch_set in partition)
                # Vertex indices, subset order and restricted-growth block order
                # make this a canonical record independent of hash iteration.
                digest.update(f"{size}:{encoded}:{int(is_connected)}:{missing_count}\n".encode())

                if not is_connected:
                    continue
                connected_totals[size] += 1
                if missing_count < minimum_missing:
                    minimum_missing = missing_count
                    closest_partition = partition

    actual_digest = digest.hexdigest()
    require(totals == {7: 120, 8: 1260, 9: 4620, 10: 5880}, "partition count mismatch")
    require(
        connected_totals == {7: 120, 8: 756, 9: 2002, 10: 2034},
        "connected-partition count mismatch",
    )
    require(minimum_missing == 2, "unexpected minimum number of missing branch pairs")
    require(actual_digest == EXPECTED_DIGEST, "search digest mismatch")

    print("vertices", len(VERTICES), "edges", len(EDGES))
    print("partitions_by_used_order", totals)
    print("connected_branch_partitions", sum(connected_totals.values()))
    print("minimum_missing_branch_pairs", minimum_missing)
    print("closest_partition", display(closest_partition))
    print("search_digest", actual_digest)
    print("VERIFIED: the quotient has no K_7^- minor")


if __name__ == "__main__":
    check_construction()
    verify_minor_exclusion()
