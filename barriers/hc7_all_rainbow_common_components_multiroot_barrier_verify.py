#!/usr/bin/env python3
"""Verify the all-rainbow common-component multiroot barrier."""

from itertools import combinations, product


VERTICES = ("p", "v", "q", "u", "a0", "a1", "b0", "b1", "c0", "c1")
COLOUR = {
    "p": "beta",
    "v": "beta",
    "q": "delta",
    "u": "delta",
    "a0": "gamma1",
    "a1": "gamma1",
    "b0": "gamma2",
    "b1": "gamma2",
    "c0": "gamma3",
    "c1": "gamma3",
}
TRIANGLES = (
    frozenset(("a0", "b0", "c0")),
    frozenset(("a0", "b0", "c1")),
    frozenset(("a0", "b1", "c0")),
    frozenset(("a0", "b1", "c1")),
    frozenset(("a1", "b0", "c0")),
)


def pair(x: str, y: str) -> frozenset[str]:
    return frozenset((x, y))


EDGES = {
    pair(x, y)
    for x, y in combinations(VERTICES, 2)
    if COLOUR[x] != COLOUR[y] and {x, y} != {"p", "q"}
}


def adjacent(x: str, y: str) -> bool:
    return pair(x, y) in EDGES


def connected(vertices: frozenset[str] | set[str]) -> bool:
    remaining = set(vertices)
    if not remaining:
        return False
    reached = {remaining.pop()}
    while remaining:
        new = {v for v in remaining if any(adjacent(v, u) for u in reached)}
        if not new:
            return False
        reached.update(new)
        remaining.difference_update(new)
    return True


def bags_touch(left: set[str], right: set[str]) -> bool:
    return any(adjacent(x, y) for x in left for y in right)


def component(start: str, allowed_colours: set[str]) -> set[str]:
    allowed = {v for v in VERTICES if COLOUR[v] in allowed_colours}
    reached = {start}
    frontier = [start]
    while frontier:
        x = frontier.pop()
        for y in allowed - reached:
            if adjacent(x, y):
                reached.add(y)
                frontier.append(y)
    return reached


def verify_colouring_and_triangles() -> None:
    assert pair("p", "q") not in EDGES
    assert all(COLOUR[x] != COLOUR[y] for x, y in (tuple(e) for e in EDGES))
    for triangle in TRIANGLES:
        assert len({COLOUR[v] for v in triangle}) == 3
        assert all(adjacent(x, y) for x, y in combinations(triangle, 2))


def verify_common_components() -> None:
    gamma_parts = {
        "gamma1": {"a0", "a1"},
        "gamma2": {"b0", "b1"},
        "gamma3": {"c0", "c1"},
    }
    for gamma, contacts in gamma_parts.items():
        assert contacts <= component("p", {"beta", gamma})
        assert contacts <= component("q", {"delta", gamma})
    assert "q" in component("p", {"beta", "delta"})


def verify_connectivity() -> None:
    for size in range(7):
        for deleted in combinations(VERTICES, size):
            surviving = frozenset(set(VERTICES) - set(deleted))
            assert connected(surviving)
    neighbours_of_p = {v for v in VERTICES if adjacent("p", v)}
    assert len(neighbours_of_p) == 7
    surviving = frozenset(set(VERTICES) - neighbours_of_p)
    assert not connected(surviving)


def verify_individual_models() -> None:
    for triangle in TRIANGLES:
        bags = [{"p", "u"}, {"v", "q"}] + [{v} for v in triangle]
        assert all(connected(frozenset(bag)) for bag in bags)
        assert all(bags_touch(left, right) for left, right in combinations(bags, 2))


def simultaneous_model_exists() -> bool:
    core = ("a0", "a1", "b0", "b1", "c0", "c1")
    stable_labels = (0, 1, 2)
    extra_labels = (0, 1, 2, 3, 4, 5)  # stable, p-bag, q-bag, unused

    for assignment in product(stable_labels, repeat=len(core)):
        label = dict(zip(core, assignment, strict=True))
        if any({label[v] for v in triangle} != set(stable_labels) for triangle in TRIANGLES):
            continue
        for u_label, v_label in product(extra_labels, repeat=2):
            bags = [{"p"}, {"q"}, set(), set(), set()]
            for vertex, stable_label in label.items():
                bags[2 + stable_label].add(vertex)
            for vertex, extra_label in (("u", u_label), ("v", v_label)):
                if extra_label < 3:
                    bags[2 + extra_label].add(vertex)
                elif extra_label == 3:
                    bags[0].add(vertex)
                elif extra_label == 4:
                    bags[1].add(vertex)
            if not all(connected(frozenset(bag)) for bag in bags):
                continue
            if all(bags_touch(left, right) for left, right in combinations(bags, 2)):
                return True
    return False


def main() -> None:
    verify_colouring_and_triangles()
    verify_common_components()
    verify_connectivity()
    verify_individual_models()
    assert not simultaneous_model_exists()
    print("GREEN: common components do not force a simultaneous five-triangle model")


if __name__ == "__main__":
    main()
