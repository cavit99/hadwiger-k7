#!/usr/bin/env python3
"""Verify the order-seven theta-singleton completion table."""

from itertools import combinations, permutations


VERTICES = tuple(range(6))
U = ("u", 0)


CASES = {
    "223": {
        "edges": "02 03 04 12 13 15 45",
        "rows": (
            ((0, 1), "P", (4, 5), ((0, 1), (1, 0))),
            ((0, 5), "F", (1, 2, 3), ((0, 5), (1, 4))),
            ((2, 3), "P", (4, 5), ((2, 3), (3, 2))),
            ((2, 4), "F", (0, 3, 5), ((2, 4), (2, 5), (3, 4), (3, 5))),
            ((4, 1), "F", (0, 2, 3), ((4, 1), (5, 0))),
            ((4, 2), "F", (0, 3, 5), ((4, 2), (4, 3), (5, 2), (5, 3))),
        ),
    },
    "124": {
        "edges": "01 02 03 12 15 34 45",
        "rows": (
            ((0, 4), "F", (1, 0, 2), ((0, 4), (1, 4))),
            ((0, 5), "P", (3, 4), ((0, 5), (1, 3))),
            ((2, 3), "P", (4, 5), ((2, 3), (2, 5))),
            ((2, 4), "F", (0, 3, 5), ((2, 4),)),
            ((3, 1), "P", (4, 5), ((3, 1), (5, 0))),
            ((3, 2), "P", (4, 5), ((3, 2), (5, 2))),
            ((3, 5), "F", (0, 1, 2), ((3, 5), (5, 3))),
            ((4, 0), "F", (0, 1, 2), ((4, 0), (4, 1))),
            ((4, 2), "F", (0, 3, 5), ((4, 2),)),
        ),
    },
    "133": {
        "edges": "01 02 04 13 15 23 45",
        "rows": (
            ((0, 3), "P", (4, 5), ((0, 3), (0, 5), (1, 2), (1, 4))),
            ((2, 1), "P", (4, 5), ((2, 1), (3, 0), (4, 1), (5, 0))),
            ((2, 4), "F", (0, 1, 3), ((2, 4), (3, 5), (4, 2), (5, 3))),
            ((2, 5), "F", (0, 1, 3), ((2, 5), (3, 4), (4, 3), (5, 2))),
        ),
    },
}


def parse_edges(text):
    return {tuple(sorted((int(item[0]), int(item[1])))) for item in text.split()}


def image_edge(edge, permutation):
    return tuple(sorted((permutation[edge[0]], permutation[edge[1]])))


def image_arc(arc, permutation):
    return permutation[arc[0]], permutation[arc[1]]


def automorphisms(edges):
    return tuple(
        permutation
        for permutation in permutations(VERTICES)
        if {image_edge(edge, permutation) for edge in edges} == edges
    )


def adjacent(left, right, w_edges, extra_arc):
    if left[0] == "w" and right[0] == "w":
        return tuple(sorted((left[1], right[1]))) in w_edges
    if left[0] == "s" and right[0] == "w":
        return left[1] == right[1] or (left[1], right[1]) == extra_arc
    if left[0] == "w" and right[0] == "s":
        return right[1] == left[1] or (right[1], left[1]) == extra_arc
    return (left == U and right[0] == "w") or (right == U and left[0] == "w")


def connected(bag, w_edges, extra_arc):
    seen = {next(iter(bag))}
    while True:
        new = {
            vertex
            for vertex in bag - seen
            if any(adjacent(vertex, old, w_edges, extra_arc) for old in seen)
        }
        if not new:
            return seen == bag
        seen |= new


def bags_for(kind, parameters):
    if kind == "P":
        omitted, universal = parameters
        bags = {
            index: {("s", index), ("w", index)}
            for index in VERTICES
            if index != omitted
        }
        bags[universal] |= {U, ("w", omitted)}
        return omitted, bags

    assert kind == "F"
    omitted, folded, universal = parameters
    bags = {
        index: {("s", index), ("w", index)}
        for index in VERTICES
        if index != omitted
    }
    bags[folded].add(("w", omitted))
    bags[universal].add(U)
    return omitted, bags


def verify_model(w_edges, extra_arc, kind, parameters):
    omitted, bags = bags_for(kind, parameters)
    assert set(bags) == set(VERTICES) - {omitted}
    assert all(("s", index) in bag for index, bag in bags.items())
    assert all(("s", other) not in bag for index, bag in bags.items() for other in VERTICES if other != index)

    bag_values = tuple(bags.values())
    assert all(bag_values[i].isdisjoint(bag_values[j]) for i in range(5) for j in range(i))
    assert all(connected(bag, w_edges, extra_arc) for bag in bag_values)

    missing = []
    for left, right in combinations(sorted(bags), 2):
        if not any(
            adjacent(x, y, w_edges, extra_arc)
            for x in bags[left]
            for y in bags[right]
        ):
            missing.append((left, right))
    assert len(missing) <= 1, (w_edges, extra_arc, kind, parameters, missing)


def main():
    checked_models = 0
    for name, case in CASES.items():
        edges = parse_edges(case["edges"])
        assert len(edges) == 7
        automorphism_group = automorphisms(edges)

        directed_nonedges = {
            (left, right)
            for left in VERTICES
            for right in VERTICES
            if left != right and tuple(sorted((left, right))) not in edges
        }
        displayed = set()
        for representative, _kind, _parameters, stated_orbit in case["rows"]:
            actual_orbit = {
                image_arc(representative, automorphism)
                for automorphism in automorphism_group
            }
            assert actual_orbit == set(stated_orbit), (name, representative)
            assert displayed.isdisjoint(actual_orbit)
            displayed |= actual_orbit
        assert displayed == directed_nonedges
        assert len(displayed) == 16

        # A perfect matching may impose any of the 6! simultaneous labels on W.
        for relabelling in permutations(VERTICES):
            relabelled_edges = {image_edge(edge, relabelling) for edge in edges}
            for representative, kind, parameters, stated_orbit in case["rows"]:
                for arc in stated_orbit:
                    orbit_map = next(
                        automorphism
                        for automorphism in automorphism_group
                        if image_arc(representative, automorphism) == arc
                    )
                    orbit_parameters = tuple(orbit_map[x] for x in parameters)
                    relabelled_arc = image_arc(arc, relabelling)
                    relabelled_parameters = tuple(
                        relabelling[x] for x in orbit_parameters
                    )
                    verify_model(
                        relabelled_edges,
                        relabelled_arc,
                        kind,
                        relabelled_parameters,
                    )
                    checked_models += 1

        # Six diagonal incidences and both directions on seven W-edges give 20.
        assert 6 + 2 * len(edges) == 20

    assert checked_models == 3 * 720 * 16
    print(f"checked_models={checked_models}")
    print("order-seven theta singleton completion: PASS")


if __name__ == "__main__":
    main()
