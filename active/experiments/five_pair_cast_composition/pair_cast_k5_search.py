#!/usr/bin/env python3
"""Search the five-vertex clique quotient for pair-cast noncomposition.

The five clique vertices represent a spanning K5-minor model in the
five-chromatic shore.  A boundary terminal is encoded by the nonempty set
of bags it contacts.  The script asks whether every centre pair can be
separated from one p--q route although no single p--q route leaves all five
centres attached to the remaining clique bags.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement


FULL = (1 << 5) - 1
MASKS = tuple(range(1, FULL + 1))


def bits(mask: int) -> tuple[int, ...]:
    return tuple(i for i in range(5) if mask & (1 << i))


def pq_routes(p_mask: int, q_mask: int) -> tuple[int, ...]:
    """Internal bag sets of all inclusion-minimal p--q paths in K5."""
    routes: set[int] = set()
    for a in bits(p_mask):
        for b in bits(q_mask):
            routes.add(1 << a if a == b else (1 << a) | (1 << b))
    return tuple(sorted(routes, key=lambda m: (m.bit_count(), m)))


def rooted_internal_seven(portals: tuple[int, ...]) -> bool:
    """Check |N_K5(X)|+|N_boundary(X)| >= 7 for every X in K5."""
    for x_mask in MASKS:
        outside = 5 - x_mask.bit_count() if x_mask != FULL else 0
        boundary = sum(bool(mask & x_mask) for mask in portals)
        if outside + boundary < 7:
            return False
    return True


def all_pairs_but_not_full(
    p_mask: int, q_mask: int, centres: tuple[int, ...]
) -> bool:
    routes = pq_routes(p_mask, q_mask)
    if any(all(z & ~route for z in centres) for route in routes):
        return False
    return all(
        any((centres[i] & ~route) and (centres[j] & ~route) for route in routes)
        for i, j in combinations(range(5), 2)
    )


def main() -> None:
    checked = 0
    for p_mask in MASKS:
        for q_mask in range(p_mask, FULL + 1):
            if q_mask == 0:
                continue
            routes = pq_routes(p_mask, q_mask)
            blockers = tuple(z for z in MASKS if any(z & ~r == 0 for r in routes))
            for centres in combinations_with_replacement(blockers, 5):
                checked += 1
                if not all_pairs_but_not_full(p_mask, q_mask, centres):
                    continue
                portals = (p_mask, q_mask, *centres)
                if not rooted_internal_seven(portals):
                    continue
                print("FOUND")
                print("p", bits(p_mask), "q", bits(q_mask))
                for i, z_mask in enumerate(centres):
                    print(f"z{i}", bits(z_mask))
                print("routes", [bits(route) for route in routes])
                print("checked", checked)
                return
    print("NONE", checked)


if __name__ == "__main__":
    main()
