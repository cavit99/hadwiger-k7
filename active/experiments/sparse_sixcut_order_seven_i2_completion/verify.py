#!/usr/bin/env python3
"""Verify the direct order-seven i=2 completion.

Vertices 0,1 are the deficient singleton bags (the poles), and W is
{2,...,6}.  Root 0 sees both poles.  Root 1+j is matched to W-vertex 2+j.
Only these seven boundary incidences are used.

Template A omits root 0 and puts the poles in two distinct diagonal W-bags.
Template B roots one pole at root 0, omits one T-root, and puts its freed
W-vertex and the other pole in a different diagonal T-bag.
"""

from __future__ import annotations

import itertools


TREES = {
    "path": {(0, 1), (1, 2), (2, 3), (3, 4)},
    "star": {(0, 1), (0, 2), (0, 3), (0, 4)},
    "fork": {(0, 1), (0, 2), (0, 3), (1, 4)},
}

ORBIT_ROWS = {
    "path": [
        ((0, 1), 4, ("A", 1, 0)),
        ((0, 2), 4, ("B", 0, 1, 0)),
        ((0, 3), 4, ("B", 0, 4, 0)),
        ((0, 4), 2, ("A", 4, 0)),
        ((1, 2), 4, ("A", 0, 1)),
        ((1, 3), 2, ("A", 0, 4)),
    ],
    "star": [
        ((0, 1), 8, ("A", 1, 2)),
        ((1, 2), 12, ("A", 2, 1)),
    ],
    "fork": [
        ((0, 1), 2, ("A", 1, 4)),
        ((0, 2), 4, ("A", 2, 3)),
        ((0, 4), 2, ("B", 1, 4, 1)),
        ((1, 2), 4, ("B", 2, 4, 1)),
        ((1, 4), 2, ("A", 4, 1)),
        ((2, 3), 2, ("A", 3, 2)),
        ((2, 4), 4, ("A", 4, 2)),
    ],
}


def make_instance(tree, joined, miss0=None, miss1=None):
    edges = {tuple(sorted((2 + left, 2 + right))) for left, right in tree}
    if joined:
        edges.add((0, 1))
    for vertex in range(5):
        if vertex != miss0:
            edges.add((0, 2 + vertex))
        if vertex != miss1:
            edges.add((1, 2 + vertex))
    adjacency = [0] * 7
    for left, right in edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    root_neighbours = [3] + [1 << (2 + vertex) for vertex in range(5)]
    return adjacency, root_neighbours


def rooted_connected(root, mask, adjacency, root_neighbours):
    if not mask:
        return True
    reached = root_neighbours[root] & mask
    if not reached:
        return False
    while True:
        old = reached
        for vertex in range(7):
            if reached >> vertex & 1:
                reached |= adjacency[vertex] & mask
        if reached == old:
            return reached == mask


def valid(roots, bags, adjacency, root_neighbours):
    if len(set(roots)) != 5:
        return False
    if bags[0] | bags[1] | bags[2] | bags[3] | bags[4] != 127:
        return False
    if sum(bin(mask).count("1") for mask in bags) != 7:
        return False
    if any(
        not rooted_connected(root, mask, adjacency, root_neighbours)
        for root, mask in zip(roots, bags)
    ):
        return False

    contacts = 0
    for left, right in itertools.combinations(range(5), 2):
        touch = bool(
            root_neighbours[roots[left]] & bags[right]
            or root_neighbours[roots[right]] & bags[left]
        )
        if not touch:
            touch = any(
                (bags[left] >> vertex & 1)
                and adjacency[vertex] & bags[right]
                for vertex in range(7)
            )
        contacts += touch
    return contacts >= 9


def certificate_a(adjacency, root_neighbours, first, second):
    roots = [1 + vertex for vertex in range(5)]
    bags = [1 << (2 + vertex) for vertex in range(5)]
    bags[first] |= 1
    bags[second] |= 2
    return valid(roots, bags, adjacency, root_neighbours)


def template_a(adjacency, root_neighbours):
    for first, second in itertools.permutations(range(5), 2):
        if certificate_a(adjacency, root_neighbours, first, second):
            return first, second
    return None


def certificate_b(adjacency, root_neighbours, omitted, host, rooted_pole):
    retained = [vertex for vertex in range(5) if vertex != omitted]
    roots = [0] + [1 + vertex for vertex in retained]
    bags = [1 << rooted_pole] + [1 << (2 + vertex) for vertex in retained]
    bags[1 + retained.index(host)] |= (
        (1 << (2 + omitted)) | (1 << (1 - rooted_pole))
    )
    return valid(roots, bags, adjacency, root_neighbours)


def template_b(adjacency, root_neighbours):
    for omitted in range(5):
        retained = [vertex for vertex in range(5) if vertex != omitted]
        for host in retained:
            for rooted_pole in range(2):
                if certificate_b(
                    adjacency,
                    root_neighbours,
                    omitted,
                    host,
                    rooted_pole,
                ):
                    return omitted, host, rooted_pole
    return None


def orbit(tree, misses):
    images = set()
    for permutation in itertools.permutations(range(5)):
        image_tree = {
            tuple(sorted((permutation[left], permutation[right])))
            for left, right in tree
        }
        if image_tree != tree:
            continue
        image = (permutation[misses[0]], permutation[misses[1]])
        images.add(image)
        images.add((image[1], image[0]))  # exchange the poles
    return images


def main():
    unjoined = 0
    for name, tree in TREES.items():
        adjacency, root_neighbours = make_instance(tree, False)
        assert template_a(adjacency, root_neighbours) is not None, (
            name,
            "unjoined",
        )
        unjoined += 1

    totals = {"A": 0, "B": 0}
    by_tree = {name: {"A": 0, "B": 0} for name in TREES}
    for name, tree in TREES.items():
        for miss0, miss1 in itertools.permutations(range(5), 2):
            adjacency, root_neighbours = make_instance(
                tree, True, miss0, miss1
            )
            if template_a(adjacency, root_neighbours) is not None:
                family = "A"
            elif template_b(adjacency, root_neighbours) is not None:
                family = "B"
            else:
                raise AssertionError((name, miss0, miss1))
            totals[family] += 1
            by_tree[name][family] += 1

    print(f"unjoined universal cases={unjoined}")
    print(f"joined cases by tree={by_tree}")
    print(f"joined template counts={totals}")
    assert unjoined == 3
    assert totals == {"A": 46, "B": 14}
    assert by_tree == {
        "path": {"A": 12, "B": 8},
        "star": {"A": 20, "B": 0},
        "fork": {"A": 14, "B": 6},
    }

    # Check the displayed fifteen-row orbit table and its named witnesses.
    for name, tree in TREES.items():
        remaining = set(itertools.permutations(range(5), 2))
        for misses, expected_size, witness in ORBIT_ROWS[name]:
            images = orbit(tree, misses)
            assert len(images) == expected_size
            assert images <= remaining
            remaining -= images
            adjacency, root_neighbours = make_instance(
                tree, True, misses[0], misses[1]
            )
            if witness[0] == "A":
                assert certificate_a(
                    adjacency, root_neighbours, witness[1], witness[2]
                )
            else:
                assert certificate_b(
                    adjacency,
                    root_neighbours,
                    witness[1],
                    witness[2],
                    witness[3],
                )
        assert not remaining
    assert sum(len(rows) for rows in ORBIT_ROWS.values()) == 15
    print("joined orbit rows=15 coverage=60 witnesses=PASS")
    print("order-seven i=2 direct completion: PASS")


if __name__ == "__main__":
    main()
