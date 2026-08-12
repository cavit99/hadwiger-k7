#!/usr/bin/env python3
"""Exhaust the exact model-anchored appendage contact quotients.

This is a bounded diagnostic.  It tests only the quotient hypotheses stated
in the adjacent README and makes no inference about the uncontracted host.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, product


FOREIGN = ("P", "B", "C", "U2", "U3", "U4")
TWINS = ("B", "C")
UNIVERSALS = ("U2", "U3", "U4")


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def has_edge(adjacency: tuple[int, ...] | list[int], left: int, right: int) -> bool:
    return bool(adjacency[left] & (1 << right))


def delete_vertex(adjacency: tuple[int, ...], removed: int) -> tuple[int, ...]:
    kept = [vertex for vertex in range(len(adjacency)) if vertex != removed]
    index = {vertex: new for new, vertex in enumerate(kept)}
    result = [0] * len(kept)
    for old_left, old_right in combinations(kept, 2):
        if has_edge(adjacency, old_left, old_right):
            add_edge(result, index[old_left], index[old_right])
    return tuple(result)


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    """Contract one edge, keeping ``left`` as the merged position."""

    assert left < right and has_edge(adjacency, left, right)
    cells: list[tuple[int, ...]] = []
    for vertex in range(len(adjacency)):
        if vertex == left:
            cells.append((left, right))
        elif vertex != right:
            cells.append((vertex,))

    result = [0] * len(cells)
    for new_left, new_right in combinations(range(len(cells)), 2):
        if any(
            has_edge(adjacency, old_left, old_right)
            for old_left in cells[new_left]
            for old_right in cells[new_right]
        ):
            add_edge(result, new_left, new_right)
    return tuple(result)


def edge_count(adjacency: tuple[int, ...]) -> int:
    return sum(mask.bit_count() for mask in adjacency) // 2


@lru_cache(maxsize=None)
def minor_search(graph: tuple[int, ...]) -> bool:
    """Search all contractions and deletions, sharing subproblems globally."""

    order = len(graph)
    if order == 7:
        return edge_count(graph) >= 20

    # Contractions are tried first because the quotients already contain a
    # dense seven-bag near-clique model.  The global cache is important:
    # different portal profiles have many identical order-eight and
    # order-nine minors.
    for left, right in combinations(range(order), 2):
        if has_edge(graph, left, right) and minor_search(
            contract_edge(graph, left, right)
        ):
            return True
    return any(
        minor_search(delete_vertex(graph, vertex)) for vertex in range(order)
    )


def has_k7_minus_minor(adjacency: tuple[int, ...]) -> bool:
    """Test the target exactly by all contractions and deletions to order 7."""

    assert len(adjacency) >= 7
    return minor_search(adjacency)


def make_profile(
    appendages: int, portal_masks: tuple[int, ...]
) -> tuple[tuple[str, ...], tuple[int, ...]]:
    pieces = ("K", "R0") + tuple(f"A{i + 1}" for i in range(appendages))
    names = pieces + FOREIGN
    position = {name: index for index, name in enumerate(names)}
    adjacency = [0] * len(names)

    # K joins the retained branch-set complement and every appendage.
    add_edge(adjacency, position["K"], position["R0"])
    for index in range(appendages):
        add_edge(adjacency, position["K"], position[f"A{index + 1}"])

    # Exact K7^vee foreign model: B,C,U2,U3,U4 form K5; P sees only U2-U4.
    for left, right in combinations(("B", "C", *UNIVERSALS), 2):
        add_edge(adjacency, position[left], position[right])
    for universal in UNIVERSALS:
        add_edge(adjacency, position["P"], position[universal])

    for foreign, mask in zip(FOREIGN, portal_masks, strict=True):
        for bit, piece in enumerate(pieces):
            if mask & (1 << bit):
                add_edge(adjacency, position[piece], position[foreign])

    return names, tuple(adjacency)


def ownership_sets(
    appendages: int, portal_masks: tuple[int, ...]
) -> tuple[frozenset[str], ...]:
    sets = []
    for index in range(appendages):
        singleton_mask = 1 << (index + 2)
        sets.append(
            frozenset(
                foreign
                for foreign, mask in zip(FOREIGN, portal_masks, strict=True)
                if mask == singleton_mask
            )
        )
    return tuple(sets)


def admissible_profiles(appendages: int, far: str):
    piece_count = 2 + appendages
    all_masks = tuple(range(1, 1 << piece_count))
    far_index = FOREIGN.index(far)
    r0_only = 1 << 1
    appendage_masks = {1 << (index + 2) for index in range(appendages)}

    for other_masks in product(all_masks, repeat=len(FOREIGN) - 1):
        masks = list(other_masks)
        masks.insert(far_index, r0_only)
        portal_masks = tuple(masks)
        owners = ownership_sets(appendages, portal_masks)
        if not all(len(owner) >= 2 for owner in owners):
            continue
        if any(far in owner for owner in owners):
            continue
        if any(left & right for left, right in combinations(owners, 2)):
            continue
        # These are the actual monopoly sets, not merely chosen subsets.
        assert all(
            mask not in appendage_masks
            for foreign, mask in zip(FOREIGN, portal_masks, strict=True)
            if all(foreign not in owner for owner in owners)
        )
        yield portal_masks, owners


def verify_model(names: tuple[str, ...], adjacency: tuple[int, ...], far: str) -> None:
    position = {name: index for index, name in enumerate(names)}
    appendages = tuple(name for name in names if name.startswith("A"))

    assert has_edge(adjacency, position["K"], position["R0"])
    for appendage in appendages:
        assert has_edge(adjacency, position["K"], position[appendage])
        assert not has_edge(adjacency, position["R0"], position[appendage])
    for left, right in combinations(appendages, 2):
        assert not has_edge(adjacency, position[left], position[right])

    for member in ("K", *appendages):
        assert not has_edge(adjacency, position[member], position[far])
    assert has_edge(adjacency, position["R0"], position[far])

    assert not has_edge(adjacency, position["P"], position["B"])
    assert not has_edge(adjacency, position["P"], position["C"])
    for left, right in combinations(("B", "C", *UNIVERSALS), 2):
        assert has_edge(adjacency, position[left], position[right])
    for universal in UNIVERSALS:
        assert has_edge(adjacency, position["P"], position[universal])

    # The union R=K+R0+appendages has a contact to every foreign bag.
    pieces = ("K", "R0", *appendages)
    for foreign in FOREIGN:
        assert any(
            has_edge(adjacency, position[piece], position[foreign])
            for piece in pieces
        )


def run_case(appendages: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for far in FOREIGN:
        total = 0
        target_free = 0
        ownership_counts: dict[tuple[int, ...], list[int]] = {}
        survivor: tuple[tuple[int, ...], tuple[frozenset[str], ...]] | None = None

        for masks, owners in admissible_profiles(appendages, far):
            names, adjacency = make_profile(appendages, masks)
            verify_model(names, adjacency, far)
            total += 1
            key = tuple(sorted(map(len, owners)))
            counts = ownership_counts.setdefault(key, [0, 0])
            counts[0] += 1
            if has_k7_minus_minor(adjacency):
                continue
            target_free += 1
            counts[1] += 1
            if survivor is None:
                survivor = (masks, owners)

        rows.append(
            {
                "appendages": appendages,
                "far": far,
                "profiles": total,
                "target_free": target_free,
                "ownership_counts": ownership_counts,
                "survivor": survivor,
            }
        )
    return rows


def verify_controls() -> None:
    complete = tuple(((1 << 7) - 1) ^ (1 << vertex) for vertex in range(7))
    assert has_k7_minus_minor(complete)

    exact_vee = [0] * 7
    for left, right in combinations(range(7), 2):
        if (left, right) not in {(0, 1), (0, 2)}:
            add_edge(exact_vee, left, right)
    assert not has_k7_minus_minor(tuple(exact_vee))


def format_survivor(row: dict[str, object]) -> str:
    survivor = row["survivor"]
    if survivor is None:
        return "none"
    masks, owners = survivor
    appendages = int(row["appendages"])
    pieces = ("K", "R0") + tuple(f"A{i + 1}" for i in range(appendages))
    contacts = []
    for foreign, mask in zip(FOREIGN, masks, strict=True):
        support = "+".join(piece for bit, piece in enumerate(pieces) if mask & (1 << bit))
        contacts.append(f"{foreign}:{support}")
    ownership = ";".join(
        f"A{index + 1}={','.join(sorted(owner))}"
        for index, owner in enumerate(owners)
    )
    return f"contacts={','.join(contacts)} ownership={ownership}"


def main() -> None:
    verify_controls()
    rows = run_case(1) + run_case(2)

    observed = {
        (int(row["appendages"]), str(row["far"])): (
            int(row["profiles"]),
            int(row["target_free"]),
        )
        for row in rows
    }
    expected = {
        (1, "P"): (2551, 1401),
        (1, "B"): (2551, 1883),
        (1, "C"): (2551, 1883),
        (1, "U2"): (2551, 2073),
        (1, "U3"): (2551, 2073),
        (1, "U4"): (2551, 2073),
        (2, "P"): (410, 326),
        (2, "B"): (410, 368),
        (2, "C"): (410, 368),
        (2, "U2"): (410, 382),
        (2, "U3"): (410, 382),
        (2, "U4"): (410, 382),
    }
    assert observed == expected, observed

    print("GREEN model-anchored appendage quotient gate")
    print("minor_test=all_vertex_deletions_and_edge_contractions_to_order_7")
    print("model_spanning=false response_colouring_encoded=false")
    for row in rows:
        ownership = ",".join(
            f"{key}:{value[0]}/{value[1]}"
            for key, value in sorted(row["ownership_counts"].items())
        )
        print(
            " ".join(
                (
                    f"t={row['appendages']}",
                    f"far={row['far']}",
                    f"profiles={row['profiles']}",
                    f"target_free={row['target_free']}",
                    f"ownership(total/free)={ownership}",
                )
            )
        )
        print(f" survivor {format_survivor(row)}")


if __name__ == "__main__":
    main()
