#!/usr/bin/env python3
"""Verify the residual two-portal quotient tables.

The mandatory quotient has packet vertices p1,p2 complete to Z union R,
outer vertices A,D complete to S=Z union Q, and matching edges r1-q1,
r2-q2.  Optional edges are r1-r2, the two crossed R-Q edges (at most one),
and the eight R-Z incidences.

The first table covers every three-optional-edge profile.  The second checks
all two-edge profiles and leaves exactly the two equality orbits stated in
the adjacent theorem.
"""

from itertools import combinations, permutations


NAMES = ("p1", "p2", "z0", "z1", "z2", "z3", "q1", "q2", "r1", "r2", "A", "D")
POS = {name: index for index, name in enumerate(NAMES)}
Z_PERMUTATIONS = tuple(permutations(range(4)))


def permute_mask(mask, permutation):
    return sum(1 << permutation[index] for index in range(4) if mask & (1 << index))


def canonical(profile):
    """Canonicalise under S_4 on Z and simultaneous exchange of the portals/Q."""

    edge, cross1, cross2, z1, z2 = profile
    images = []
    for permutation in Z_PERMUTATIONS:
        first = permute_mask(z1, permutation)
        second = permute_mask(z2, permutation)
        images.append((edge, cross1, cross2, first, second))
        images.append((edge, cross2, cross1, second, first))
    return min(images)


def add_edge(adjacency, left, right):
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def quotient(profile):
    edge, cross1, cross2, z1, z2 = profile
    adjacency = [0] * len(NAMES)

    for packet in (POS["p1"], POS["p2"]):
        for root in range(POS["z0"], POS["z3"] + 1):
            add_edge(adjacency, packet, root)
        add_edge(adjacency, packet, POS["r1"])
        add_edge(adjacency, packet, POS["r2"])

    for outer in (POS["A"], POS["D"]):
        for root in range(POS["z0"], POS["q2"] + 1):
            add_edge(adjacency, outer, root)

    add_edge(adjacency, POS["r1"], POS["q1"])
    add_edge(adjacency, POS["r2"], POS["q2"])
    if cross1:
        add_edge(adjacency, POS["r1"], POS["q2"])
    if cross2:
        add_edge(adjacency, POS["r2"], POS["q1"])
    if edge:
        add_edge(adjacency, POS["r1"], POS["r2"])

    for bit in range(4):
        if z1 & (1 << bit):
            add_edge(adjacency, POS["r1"], POS[f"z{bit}"])
        if z2 & (1 << bit):
            add_edge(adjacency, POS["r2"], POS[f"z{bit}"])
    return tuple(adjacency)


def bag(*members):
    return sum(1 << POS[member] for member in members)


THREE_EDGE_TABLE = {
    (0, 0, 0, 0, 7): (
        bag("p1", "z0", "r1"), bag("p2", "z3"), bag("z1"), bag("z2"),
        bag("q1", "A"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 0, 1, 3): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 0, 1, 6): (
        bag("p1", "z0", "r1"), bag("p2", "z3"), bag("z1"), bag("z2"),
        bag("q1", "A"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 1, 0, 3): (
        bag("p1", "z0"), bag("p2", "z2"), bag("z1"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 1, 1, 1): (
        bag("p1", "z1", "z2"), bag("p2", "z3"), bag("z0"),
        bag("q1", "r1"), bag("q2", "r2"), bag("A"), bag("D"),
    ),
    (0, 0, 1, 1, 2): (
        bag("p1", "z0"), bag("p2", "z2"), bag("z1"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 1, 3, 0): (
        bag("p1", "z0"), bag("p2", "z2"), bag("z1"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (1, 0, 0, 0, 3): (
        bag("p1", "z0"), bag("p2", "z2"), bag("z1"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (1, 0, 0, 1, 1): (
        bag("p1", "z1", "z2"), bag("p2", "z3"), bag("z0"),
        bag("q1", "r1"), bag("q2", "r2"), bag("A"), bag("D"),
    ),
    (1, 0, 0, 1, 2): (
        bag("p1", "z0"), bag("p2", "z2"), bag("z1"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (1, 0, 1, 0, 1): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (1, 0, 1, 1, 0): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
}


TWO_EDGE_BAD_TABLE = {
    (0, 0, 0, 0, 3): (
        bag("p1", "z2", "r1"), bag("p2", "z3"), bag("z0"), bag("z1"),
        bag("q1", "A"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 0, 1, 1): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 1, 0, 1): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (0, 0, 1, 1, 0): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
    (1, 0, 0, 0, 1): (
        bag("p1", "z1"), bag("p2", "z2"), bag("z0"), bag("z3", "A"),
        bag("q1", "r1"), bag("q2", "r2"), bag("D"),
    ),
}

TWO_EDGE_SAFE = {
    (0, 0, 0, 1, 2),  # distinct singleton Z-neighbours, no portal/cross edge
    (1, 0, 1, 0, 0),  # portal edge, one cross edge, no Z-neighbour
}


def connected(adjacency, mask):
    reached = mask & -mask
    while True:
        expanded = reached
        frontier = reached
        while frontier:
            vertex_bit = frontier & -frontier
            frontier ^= vertex_bit
            vertex = vertex_bit.bit_length() - 1
            expanded |= adjacency[vertex] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def contact(adjacency, left, right):
    union = 0
    scan = left
    while scan:
        bit = scan & -scan
        scan ^= bit
        union |= adjacency[bit.bit_length() - 1]
    return bool(union & right)


def verify_witness(profile, bags):
    adjacency = quotient(profile)
    assert len(bags) == 7
    used = 0
    for current in bags:
        assert current and not (used & current)
        assert connected(adjacency, current)
        used |= current
    contacts = sum(
        contact(adjacency, bags[left], bags[right])
        for left, right in combinations(range(7), 2)
    )
    assert contacts >= 20
    return contacts


def profiles_with_optional_count(count):
    for edge in range(2):
        for cross1 in range(2):
            for cross2 in range(2):
                if cross1 + cross2 > 1:
                    continue
                for z1 in range(16):
                    for z2 in range(16):
                        if edge + cross1 + cross2 + z1.bit_count() + z2.bit_count() == count:
                            yield (edge, cross1, cross2, z1, z2)


def optional_edges(profile):
    edge, cross1, cross2, z1, z2 = profile
    result = []
    if edge:
        result.append(("edge", 0))
    if cross1:
        result.append(("cross1", 0))
    if cross2:
        result.append(("cross2", 0))
    result.extend(("z1", bit) for bit in range(4) if z1 & (1 << bit))
    result.extend(("z2", bit) for bit in range(4) if z2 & (1 << bit))
    return result


def subprofile(selected):
    edge = cross1 = cross2 = z1 = z2 = 0
    for kind, bit in selected:
        if kind == "edge":
            edge = 1
        elif kind == "cross1":
            cross1 = 1
        elif kind == "cross2":
            cross2 = 1
        elif kind == "z1":
            z1 |= 1 << bit
        else:
            assert kind == "z2"
            z2 |= 1 << bit
    return edge, cross1, cross2, z1, z2


def main():
    minimal_three = tuple(profiles_with_optional_count(3))
    three_orbits = {canonical(profile) for profile in minimal_three}
    assert len(minimal_three) == 156
    assert three_orbits == set(THREE_EDGE_TABLE)
    three_contacts = [
        verify_witness(profile, THREE_EDGE_TABLE[profile]) for profile in sorted(three_orbits)
    ]

    all_profiles = []
    reductions = 0
    for edge in range(2):
        for cross1 in range(2):
            for cross2 in range(2):
                if cross1 + cross2 > 1:
                    continue
                for z1 in range(16):
                    for z2 in range(16):
                        profile = (edge, cross1, cross2, z1, z2)
                        all_profiles.append(profile)
                        optional = optional_edges(profile)
                        if len(optional) >= 3:
                            assert all(
                                canonical(subprofile(chosen)) in THREE_EDGE_TABLE
                                for chosen in combinations(optional, 3)
                            )
                            reductions += 1
    assert len(all_profiles) == 1536

    minimal_two = tuple(profiles_with_optional_count(2))
    two_orbits = {canonical(profile) for profile in minimal_two}
    assert len(minimal_two) == 54
    assert two_orbits == set(TWO_EDGE_BAD_TABLE) | TWO_EDGE_SAFE
    two_contacts = [
        verify_witness(profile, TWO_EDGE_BAD_TABLE[profile])
        for profile in sorted(TWO_EDGE_BAD_TABLE)
    ]

    print(f"three_edge_profiles={len(minimal_three)} canonical_orbits={len(three_orbits)}")
    print(f"full_profiles={len(all_profiles)} profiles_reduced={reductions}")
    print(f"three_edge_witnesses={len(three_contacts)} min_contacts={min(three_contacts)}")
    print(
        f"two_edge_profiles={len(minimal_two)} canonical_orbits={len(two_orbits)} "
        f"bad_orbits={len(TWO_EDGE_BAD_TABLE)} safe_orbits={len(TWO_EDGE_SAFE)}"
    )
    print(f"two_edge_bad_witnesses={len(two_contacts)} min_contacts={min(two_contacts)}")
    print("PASS")


if __name__ == "__main__":
    main()
