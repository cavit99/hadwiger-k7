#!/usr/bin/env python3
"""Verify the stripped three-support torso-bisection counterexample."""

from itertools import combinations


VERTICES = frozenset(("u", "v", "t0", "t1", "t2"))
EDGES = frozenset(frozenset(edge) for edge in combinations(VERTICES, 2))
P = frozenset(("u", "v"))
SUPPORTS = (
    frozenset(("u", "v")),
    frozenset(("u", "t1")),
    frozenset(("v", "t2")),
)


def connected(vertices: frozenset[str]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            vertex
            for vertex in vertices - reached
            if any(frozenset((vertex, seen)) in EDGES for seen in reached)
        }
        if enlarged == reached:
            return reached == set(vertices)
        reached = enlarged


def vertex_connectivity() -> int:
    ordered = sorted(VERTICES)
    for size in range(len(ordered)):
        for deleted in combinations(ordered, size):
            remaining = VERTICES - set(deleted)
            if len(remaining) <= 1 or not connected(frozenset(remaining)):
                return size
    raise AssertionError("no vertex cut found")


def main() -> None:
    connectivity = vertex_connectivity()
    # H is K5, so N_H(W)=V(H)-W.
    local_sets = (frozenset(("u",)), frozenset(("v",)), P)
    scores = tuple(
        len(VERTICES - shore)
        + sum(bool(support & shore) for support in SUPPORTS)
        for shore in local_sets
    )

    candidates = 0
    for size in range(1, len(P) + 1):
        for chosen in combinations(sorted(P), size):
            shore = frozenset(chosen)
            meets_external = bool(shore & SUPPORTS[1]) and bool(
                shore & SUPPORTS[2]
            )
            splits_whole = bool(shore & SUPPORTS[0]) and bool(
                SUPPORTS[0] - shore
            )
            if meets_external and splits_whole:
                candidates += 1

    assert connectivity == 4
    assert scores == (6, 6, 6)
    assert candidates == 0
    print(f"PASS order=5 connectivity={connectivity} local_scores=6,6,6")
    print("PASS candidate_bisections=0")
    print("NOTE stripped local torso claim only; global support provenance is absent")


if __name__ == "__main__":
    main()
