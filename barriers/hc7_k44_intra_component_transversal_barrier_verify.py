#!/usr/bin/env python3
"""Verify the order-nine first-profile transversal barrier."""

from itertools import combinations


Q = (0, 1, 2)  # t0,t1,t2
W = tuple(tuple(range(3 + 2 * i, 5 + 2 * i)) for i in range(3))
N = 9
ALL = (1 << N) - 1

adj = [0] * N


def add_edge(u: int, v: int) -> None:
    adj[u] |= 1 << v
    adj[v] |= 1 << u


for u, v in combinations(Q, 2):
    add_edge(u, v)
for block in W:
    add_edge(*block)
    for q in Q:
        for v in block:
            add_edge(q, v)

# Boundary order: a,b,c1,c2,e1,e2,e3.
support = [0] * 7
support[0] = (1 << 0) | sum(1 << block[1] for block in W)
for block in W:
    support[1] |= 1 << block[0]
    support[2] |= 1 << block[0]
    support[3] |= 1 << block[1]
for i, block in enumerate(W):
    support[4 + i] = (1 << block[0]) | (1 << block[1])


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


def seen_resources(mask: int) -> int:
    answer = 0
    for resource, resource_support in enumerate(support):
        if mask & resource_support:
            answer |= 1 << resource
    return answer


def pop(mask: int) -> int:
    return mask.bit_count()


# Three-connectivity, minimum degree, fullness and tightness.
assert min(pop(adj[vertex]) for vertex in range(N)) == 4
for deleted_size in range(3):
    for deleted in combinations(range(N), deleted_size):
        remainder = ALL
        for vertex in deleted:
            remainder ^= 1 << vertex
        assert connected(remainder)
assert all(resource_support for resource_support in support)
assert pop(seen_resources(ALL)) == 7

# Every relative boundary inequality, and strict blocker minimality for every
# proper connected set seeing both a and b.
minimum_value = 100
strict_minimum = 100
for mask in range(1, ALL + 1):
    value = pop(internal_boundary(mask)) + pop(seen_resources(mask))
    minimum_value = min(minimum_value, value)
    assert value >= 7, (mask, value)
    seen = seen_resources(mask)
    if mask != ALL and connected(mask) and (seen & 0b11) == 0b11:
        strict_minimum = min(strict_minimum, value)
        assert value >= 8, (mask, value)

# Multiple attachment and the special vertex p=t0.
assert all(pop(support[resource]) >= 2 for resource in range(2, 7))
p = 0
assert support[0] & (1 << p)
assert pop(seen_resources(ALL ^ (1 << p)) & 0b1111110) == 6
assert pop(seen_resources(1 << p) & 0b1111100) <= 2

# Q is a three-cut with the first exact component profile.
qmask = sum(1 << q for q in Q)
assert not connected(ALL ^ qmask)
for i, block in enumerate(W):
    block_mask = sum(1 << vertex for vertex in block)
    assert connected(block_mask)
    assert support[2] & block_mask  # c1 meets every component.
    assert support[3] & block_mask  # c2 meets every component.
    assert support[4 + i] == block_mask  # e_i is exclusive and doubled.

# Exhaust the proposed component-local repair witnesses.
repair_count = 0
for i, block in enumerate(W):
    other_indices = [j for j in range(3) if j != i]
    for local_mask in range(1, 1 << len(block)):
        mask = sum(
            1 << block[position]
            for position in range(len(block))
            if local_mask >> position & 1
        )
        if not connected(mask) or not connected(ALL ^ mask):
            continue
        seen_v = seen_resources(mask)
        seen_u = seen_resources(ALL ^ mask)
        v_required = (1 << 1) | (1 << 2) | (1 << 3) | (1 << (4 + i))
        for j in other_indices:
            u_required = (
                (1 << 0)
                | (1 << 2)
                | (1 << 3)
                | (1 << (4 + i))
                | (1 << (4 + j))
            )
            if (
                seen_v & v_required == v_required
                and seen_u & u_required == u_required
            ):
                repair_count += 1
assert repair_count == 0

# Exhaust all spanning two-helper witnesses.  Resource indices 1,...,6 are H.
h_mask = sum(1 << resource for resource in range(1, 7))
spanning_witnesses = []
for u_mask in range(1, ALL):
    v_mask = ALL ^ u_mask
    if not connected(u_mask) or not connected(v_mask):
        continue
    if not (seen_resources(u_mask) & 1):
        continue
    seen_u = seen_resources(u_mask)
    seen_v = seen_resources(v_mask)
    for h0 in range(1, 7):
        first = h_mask & ~seen_u & ~(1 << 1) & ~(1 << h0)
        second = h_mask & ~seen_v & ~(1 << h0)
        if pop(first) + pop(second) <= 1:
            spanning_witnesses.append((u_mask, v_mask, h0, first, second))
            break

# The explicit cross-component witness is U={t0,l1,l2}, h0=c2.
explicit_u = (1 << 0) | (1 << 3) | (1 << 5)
explicit_v = ALL ^ explicit_u
explicit_h0 = 3
seen_u = seen_resources(explicit_u)
seen_v = seen_resources(explicit_v)
first = h_mask & ~seen_u & ~(1 << 1) & ~(1 << explicit_h0)
second = h_mask & ~seen_v & ~(1 << explicit_h0)
assert connected(explicit_u) and connected(explicit_v)
assert first == 1 << 6 and second == 0
assert len(spanning_witnesses) == 231

print(f"order={N}")
print(f"minimum_relative_value={minimum_value}")
print(f"minimum_proper_connected_ab_value={strict_minimum}")
print(f"minimum_internal_degree={min(pop(adj[v]) for v in range(N))}")
print(f"repair_witnesses={repair_count}")
print(f"spanning_two_helper_witnesses={len(spanning_witnesses)}")
print("explicit_cross_component_defects=1,0")
print("GREEN first intra-component profile")

# Second profile: the b-contact need not be supplied by U because Lemma 4.1
# gives that contact through the crossing edge ab.
support = [0] * 7
support[0] = sum((1 << block[0]) | (1 << block[1]) for block in W)
support[1] = 1 << 2
for block in W:
    support[2] |= 1 << block[0]
    support[3] |= 1 << block[1]
for i, block in enumerate(W):
    support[4 + i] = (1 << block[0]) | (1 << block[1])

minimum_value = 100
strict_minimum = 100
for mask in range(1, ALL + 1):
    value = pop(internal_boundary(mask)) + pop(seen_resources(mask))
    minimum_value = min(minimum_value, value)
    assert value >= 7, (mask, value)
    seen = seen_resources(mask)
    if mask != ALL and connected(mask) and (seen & 0b11) == 0b11:
        strict_minimum = min(strict_minimum, value)
        assert value >= 8, (mask, value)

assert all(pop(support[resource]) >= 2 for resource in range(2, 7))
p = 3  # l1
assert support[0] & (1 << p)
assert pop(seen_resources(ALL ^ (1 << p)) & 0b1111110) == 6
assert pop(seen_resources(1 << p) & 0b1111100) == 2
for i, block in enumerate(W):
    block_mask = sum(1 << vertex for vertex in block)
    assert support[2] & block_mask
    assert support[3] & block_mask
    assert support[4 + i] == block_mask

local_mode = 0
for i, block in enumerate(W):
    other_indices = [j for j in range(3) if j != i]
    for local_mask in range(1, 1 << len(block)):
        mask = sum(
            1 << block[position]
            for position in range(len(block))
            if local_mask >> position & 1
        )
        if not connected(mask) or not connected(ALL ^ mask):
            continue
        seen_v = seen_resources(mask)
        seen_u = seen_resources(ALL ^ mask)
        v_required = (1 << 1) | (1 << 2) | (1 << 3) | (1 << (4 + i))
        for j in other_indices:
            u_required = (
                (1 << 0)
                | (1 << 2)
                | (1 << 3)
                | (1 << (4 + i))
                | (1 << (4 + j))
            )
            if (
                seen_v & v_required == v_required
                and seen_u & u_required == u_required
            ):
                local_mode += 1
assert local_mode == 0

b_requiring_cross_mode = 0
b_free_cross_mode = 0
for u_mask in range(1, ALL):
    v_mask = ALL ^ u_mask
    if not connected(u_mask) or not connected(v_mask):
        continue
    seen_u = seen_resources(u_mask)
    seen_v = seen_resources(v_mask)
    if not (seen_u & 1):
        continue
    if pop(seen_u & 0b1111100) < 3:
        continue
    if pop(seen_v & 0b1111110) != 6:
        continue
    b_free_cross_mode += 1
    if seen_u & 2:
        b_requiring_cross_mode += 1
assert b_requiring_cross_mode == 0
assert b_free_cross_mode == 54

explicit_u = (1 << 0) | (1 << 3) | (1 << 5)
explicit_v = ALL ^ explicit_u
explicit_h0 = 3
seen_u = seen_resources(explicit_u)
seen_v = seen_resources(explicit_v)
first = h_mask & ~seen_u & ~(1 << 1) & ~(1 << explicit_h0)
second = h_mask & ~seen_v & ~(1 << explicit_h0)
assert connected(explicit_u) and connected(explicit_v)
assert first == 1 << 6 and second == 0

print("second_order=9")
print(f"second_minimum_relative_value={minimum_value}")
print(f"second_minimum_proper_connected_ab_value={strict_minimum}")
print(f"second_local_mode_witnesses={local_mode}")
print(f"b_requiring_cross_mode_witnesses={b_requiring_cross_mode}")
print(f"b_free_cross_mode_witnesses={b_free_cross_mode}")
print("second_explicit_cross_component_defects=1,0")
print("GREEN blocker repair barriers")
