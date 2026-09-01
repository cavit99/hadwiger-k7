#!/usr/bin/env python3
"""Verify the order-three local core-concentrated bisection barrier."""

from itertools import combinations


R = (0, 1, 2)  # r0,r1,r2
N = len(R)
ALL = (1 << N) - 1

# R is K3.
adj = [ALL ^ (1 << vertex) for vertex in R]

# Boundary order: a,p,t0,t1,t2,t3,t4.
support = (
    (1 << 1) | (1 << 2),
    (1 << 0) | (1 << 2),
    1 << 0,
    ALL,
    1 << 1,
    ALL,
    ALL,
)

# Rooted-model contact sets, indexed by t0,...,t4.
contact_a = 0b11010  # t1,t3,t4
contact_p = 0b11010


def vertices(mask: int):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def connected(mask: int) -> bool:
    if not mask:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adj[vertex] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def internal_boundary(mask: int) -> int:
    answer = 0
    for vertex in vertices(mask):
        answer |= adj[vertex]
    return answer & ~mask & ALL


def seen_boundary(mask: int) -> int:
    answer = 0
    for root, root_support in enumerate(support):
        if mask & root_support:
            answer |= 1 << root
    return answer


def seen_t(mask: int) -> int:
    return seen_boundary(mask) >> 2


def defect(mask: int, contact: int) -> int:
    return 5 - (seen_t(mask) | contact).bit_count()


# Exact graph, fullness, unique common endpoint neighbour, and contact rank.
assert all(connected(sum(1 << v for v in choice)) for size in range(1, 4)
           for choice in combinations(R, size))
assert all(root_support for root_support in support)
assert (support[0] & support[1]) == 1 << 2
assert (contact_a | contact_p).bit_count() == 3

# All seven relative boundary inequalities, with exact tight-set count.
boundary_values = {}
for mask in range(1, ALL + 1):
    value = internal_boundary(mask).bit_count() + seen_boundary(mask).bit_count()
    boundary_values[mask] = value
    assert value >= 7, (mask, value)
assert min(boundary_values.values()) == 7
assert sum(value == 7 for value in boundary_values.values()) == 6
assert sum(mask != ALL and value == 7 for mask, value in boundary_values.items()) == 5

# Exhaust all ordered, disjoint, nonempty connected endpoint-anchored pairs.
anchored_pairs = []
for u_mask in range(1, ALL + 1):
    if not connected(u_mask) or not (u_mask & support[0]):
        continue
    for v_mask in range(1, ALL + 1):
        if u_mask & v_mask:
            continue
        if not connected(v_mask) or not (v_mask & support[1]):
            continue
        anchored_pairs.append((u_mask, v_mask, defect(u_mask, contact_a)
                                + defect(v_mask, contact_p)))

assert anchored_pairs
minimum_defect = min(value for _, _, value in anchored_pairs)
assert minimum_defect == 2
assert not any(value <= 1 for _, _, value in anchored_pairs)

# Explicit degree-seven-compatible extra endpoint neighbours.  Tokens with
# different names denote distinct vertices inside the indicated rooted bag.
a_extra = ((1, "a1"), (1, "a2"), (3, "a3"), (4, "a4"))
p_extra = ((1, "p1"), (1, "p2"), (3, "p3"), (4, "p4"))
assert len({name for _, name in a_extra + p_extra}) == 8
assert {bag for bag, _ in a_extra} == {1, 3, 4}
assert {bag for bag, _ in p_extra} == {1, 3, 4}
assert 1 + support[0].bit_count() + len(a_extra) == 7  # neighbour p
assert 1 + support[1].bit_count() + len(p_extra) == 7  # neighbour a

print(f"order_R={N}")
print(f"minimum_relative_boundary={min(boundary_values.values())}")
print(f"tight_nonempty_sets={sum(v == 7 for v in boundary_values.values())}")
print(f"tight_proper_sets={sum(m != ALL and v == 7 for m, v in boundary_values.items())}")
print(f"unique_common_R_neighbours={(support[0] & support[1]).bit_count()}")
print(f"joint_contact_rank={(contact_a | contact_p).bit_count()}")
print(f"anchored_disjoint_pairs={len(anchored_pairs)}")
print(f"minimum_total_defect={minimum_defect}")
print("degree_seven_compatible=True")
print("GREEN local core-concentrated bisection incidence barrier")
