#!/usr/bin/env python3
"""Host-realised three-arm gate on the faithful order-nine residue.

The expanded graphs make the fan arms, the two centre edges, and every
owned contact literal.  Boundary-colouring extension languages remain
outside the finite encoding.
"""

from __future__ import annotations

import collections
import functools
import hashlib
import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


split = load(
    "three_fan_faithful_split",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_exact_eight_kernel_absorption"
    / "swallowed_mate_split.py",
)
rooted = load(
    "three_fan_rooted_minor",
    ROOT
    / "active"
    / "experiments"
    / "dominated_singleton_nine_terminal_exact_kernel"
    / "screen_order9.py",
)
order9 = split.order9

# Exact ownership memberships available in a theta source bag with pieces
# P_i={x,a_i}.  A label cannot be owned by exactly two of the three pieces.
ARM_MEMBERSHIPS = (0b000, 0b001, 0b010, 0b100, 0b111)


def add_edge(graph: list[int], left: int, right: int) -> None:
    assert left != right
    graph[left] |= 1 << right
    graph[right] |= 1 << left


def delete_incident_edges(graph: list[int], vertex: int) -> None:
    for neighbour in range(len(graph)):
        if graph[vertex] >> neighbour & 1:
            graph[neighbour] &= ~(1 << vertex)
    graph[vertex] = 0


def augment_carrier(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    arm_roots: tuple[tuple[int, int, int] | None, tuple[int, int, int] | None],
) -> tuple[int, ...]:
    answer = list(adjacency)
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    for selected, chosen in enumerate(arm_roots):
        if chosen is None:
            continue
        centre = centres[selected]
        for root_index in chosen:
            add_edge(answer, centre, roots[root_index])
    return tuple(answer)


def quotient_is_terminal(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
) -> bool:
    if order9.has_k7_minus(
        order9.overlay_q_on_carrier(adjacency, centres, q_graph)
    ):
        return True
    return any(
        order9.has_target(
            tuple(
                q_graph[vertex] | quotient[vertex]
                for vertex in range(7)
            )
        )
        for quotient in order9.quotient_family(adjacency, centres)
    )


def ownership_realisations(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    selected: int,
    q_roots: tuple[int, int, int],
):
    """Yield endpoint-realised owner triples for fixed distinct arm ends."""

    centre = centres[selected]
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    arm_vertices = tuple(roots[index] for index in q_roots)
    neighbours = tuple(
        vertex for vertex in range(9) if adjacency[centre] >> vertex & 1
    )
    assert all(vertex in neighbours for vertex in arm_vertices)

    free = tuple(vertex for vertex in neighbours if vertex not in arm_vertices)
    # Each literal arm contact a_i q_i forces membership exactly in P_i.
    forced = {vertex: 1 << arm for arm, vertex in enumerate(arm_vertices)}
    for free_memberships in itertools.product(
        ARM_MEMBERSHIPS, repeat=len(free)
    ):
        membership = dict(forced)
        membership.update(zip(free, free_memberships, strict=True))
        owners = tuple(
            sum(
                1 << vertex
                for vertex, pattern in membership.items()
                if pattern >> arm & 1
            )
            for arm in range(3)
        )
        if any(owner.bit_count() < 2 for owner in owners):
            continue
        yield owners, tuple(arm_vertices), tuple(
            membership[vertex] for vertex in neighbours
        )


def transfers_are_nonterminal(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    selected: int,
    realisation,
) -> bool:
    owners, absorptions, _ = realisation
    return all(
        not split.closes(
            adjacency,
            centres,
            q_graph,
            selected,
            owner,
            absorb,
        )
        for owner, absorb in zip(owners, absorptions, strict=True)
    )


def first_quotient_survivor(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    selected: int,
):
    for q_roots in itertools.combinations(range(7), 3):
        arm_roots: list[tuple[int, int, int] | None] = [None, None]
        arm_roots[selected] = q_roots
        augmented = augment_carrier(
            adjacency, centres, tuple(arm_roots)  # type: ignore[arg-type]
        )
        if quotient_is_terminal(augmented, centres, q_graph):
            continue
        for realisation in ownership_realisations(
            augmented, centres, selected, q_roots
        ):
            if transfers_are_nonterminal(
                augmented, centres, q_graph, selected, realisation
            ):
                return q_roots, augmented, realisation
    return None


def expanded_graph(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    arm_data: tuple[
        tuple[tuple[int, int, int], tuple[int, ...]] | None,
        tuple[tuple[int, int, int], tuple[int, ...]] | None,
    ],
) -> tuple[tuple[int, ...], tuple[bool, ...]]:
    """Build the literal two-centre graph for one or two three-arm bags."""

    # Original terminal vertices remain 0,...,8.  For each centre add its
    # swallowed mate; if it carries a fan, add a_0,a_1,a_2 as well.
    graph = list(order9.overlay_q_on_carrier(adjacency, centres, q_graph))
    original_order = len(graph)
    extras: list[tuple[int, tuple[int, int, int] | None]] = []
    for selected in range(2):
        q_roots = None if arm_data[selected] is None else arm_data[selected][0]
        extras.append((len(graph), q_roots))
        graph.append(0)  # swallowed matching mate
        if q_roots is not None:
            graph.extend((0, 0, 0))

    # Extend the old bit rows after adding vertices.
    assert all(row >> original_order == 0 for row in graph[:original_order])
    roots = tuple(vertex for vertex in range(9) if vertex not in centres)
    old_neighbourhoods = tuple(adjacency[centre] for centre in centres)
    for centre in centres:
        delete_incident_edges(graph, centre)

    endpoint_maps: list[dict[int, int]] = []
    for selected, centre in enumerate(centres):
        mate, q_roots = extras[selected]
        add_edge(graph, centre, mate)  # original protected-centre edge
        endpoint_map: dict[int, int] = {}
        if q_roots is None:
            # Realise every quotient contact away from the literal centre.
            for neighbour in range(9):
                if old_neighbourhoods[selected] >> neighbour & 1:
                    endpoint_map[neighbour] = mate
        else:
            assert arm_data[selected] is not None
            _, membership_vector = arm_data[selected]
            neighbours = tuple(
                vertex
                for vertex in range(9)
                if adjacency[centre] >> vertex & 1
            )
            membership = dict(
                zip(neighbours, membership_vector, strict=True)
            )
            arms = (mate + 1, mate + 2, mate + 3)
            for arm_vertex in arms:
                add_edge(graph, centre, arm_vertex)
                add_edge(graph, mate, arm_vertex)
            for neighbour, pattern in membership.items():
                if pattern == 0b111:
                    endpoint_map[neighbour] = mate
                elif pattern in (0b001, 0b010, 0b100):
                    endpoint_map[neighbour] = arms[pattern.bit_length() - 1]
                else:
                    assert pattern == 0
                    endpoint_map[neighbour] = centre
            for arm, root_index in enumerate(q_roots):
                q_vertex = roots[root_index]
                assert membership[q_vertex] == 1 << arm
        endpoint_maps.append(endpoint_map)

    # Recreate every old carrier edge.  When both ends are protected bags,
    # use non-centre endpoints on both sides, preserving centre independence.
    for left, right in itertools.combinations(range(9), 2):
        if not (adjacency[left] >> right & 1):
            continue
        if left in centres:
            left_index = centres.index(left)
            new_left = endpoint_maps[left_index][right]
        else:
            new_left = left
        if right in centres:
            right_index = centres.index(right)
            new_right = endpoint_maps[right_index][left]
        else:
            new_right = right
        add_edge(graph, new_left, new_right)

    assert not (graph[centres[0]] >> centres[1] & 1)
    marked = tuple(vertex in roots for vertex in range(len(graph)))
    return tuple(graph), marked


@functools.lru_cache(maxsize=None)
def expanded_is_terminal(
    graph: tuple[int, ...], marked: tuple[bool, ...]
) -> bool:
    # A full K7-minus scan on the expanded 13/17-vertex graph is too slow
    # for this discovery gate.  The exact root-sensitive K5-minus test is
    # the terminal composition actually used here; a survivor is therefore
    # only a nonclosure for that local inference.
    return rooted.rooted_k5minus(graph, marked)


def first_literal_survivor(
    adjacency: tuple[int, ...],
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    selected: int,
):
    for q_roots in itertools.combinations(range(7), 3):
        arm_roots: list[tuple[int, int, int] | None] = [None, None]
        arm_roots[selected] = q_roots
        augmented = augment_carrier(
            adjacency, centres, tuple(arm_roots)  # type: ignore[arg-type]
        )
        if quotient_is_terminal(augmented, centres, q_graph):
            continue
        for realisation in ownership_realisations(
            augmented, centres, selected, q_roots
        ):
            if not transfers_are_nonterminal(
                augmented, centres, q_graph, selected, realisation
            ):
                continue
            arm_data: list[
                tuple[tuple[int, int, int], tuple[int, ...]] | None
            ] = [None, None]
            arm_data[selected] = (q_roots, realisation[2])
            graph, marked = expanded_graph(
                augmented,
                centres,
                q_graph,
                tuple(arm_data),  # type: ignore[arg-type]
            )
            if not expanded_is_terminal(graph, marked):
                return q_roots, augmented, realisation, graph
    return None


def update_digest(
    digest,
    code: str,
    carrier_index: int,
    centres: tuple[int, int],
    q_graph: tuple[int, ...],
    outcomes,
) -> None:
    digest.update(code.encode("ascii"))
    digest.update(carrier_index.to_bytes(1, "big"))
    digest.update(bytes(centres))
    digest.update(bytes(q_graph))
    digest.update(repr(outcomes).encode("ascii"))


def main() -> None:
    carriers = order9.minimal_three_connected_graphs()
    by_code = dict(order9.order11.carrier7.eligible_graphs())
    expected = {"FCQ`_": 256, "FCQb_": 1_022, "FCp`_": 256}

    for code, expected_survivors in expected.items():
        copies = order9.order11.q_copies(by_code[code])
        counts = collections.Counter()
        digest = hashlib.sha256()
        first = {}

        for carrier_index, adjacency in enumerate(carriers):
            for centres in itertools.combinations(range(9), 2):
                baseline = order9.quotient_family(adjacency, centres)
                for q_graph in copies:
                    if any(
                        order9.has_target(
                            tuple(
                                q_graph[vertex] | quotient[vertex]
                                for vertex in range(7)
                            )
                        )
                        for quotient in baseline
                    ):
                        continue
                    if order9.has_k7_minus(
                        order9.overlay_q_on_carrier(
                            adjacency, centres, q_graph
                        )
                    ):
                        continue
                    if split.analyse_mode(
                        adjacency, centres, q_graph, q_only=False
                    )[0]:
                        continue

                    counts["faithful_survivors"] += 1
                    quotient_outcomes = tuple(
                        first_quotient_survivor(
                            adjacency, centres, q_graph, selected
                        )
                        for selected in range(2)
                    )
                    quotient_available = tuple(
                        outcome is not None for outcome in quotient_outcomes
                    )
                    counts["quotient_some_centre"] += any(
                        quotient_available
                    )
                    counts["quotient_both_centres"] += all(
                        quotient_available
                    )

                    literal_outcomes = [None, None]
                    for selected in range(2):
                        if quotient_outcomes[selected] is not None:
                            literal_outcomes[selected] = first_literal_survivor(
                                adjacency, centres, q_graph, selected
                            )
                    literal_available = tuple(
                        outcome is not None for outcome in literal_outcomes
                    )
                    counts["literal_some_centre"] += any(literal_available)
                    counts["literal_both_centres"] += all(literal_available)

                    common_literal = None
                    if all(literal_available):
                        left = literal_outcomes[0]
                        right = literal_outcomes[1]
                        assert left is not None and right is not None
                        common_augmented = augment_carrier(
                            adjacency,
                            centres,
                            (left[0], right[0]),
                        )
                        if (
                            not quotient_is_terminal(
                                common_augmented, centres, q_graph
                            )
                            and transfers_are_nonterminal(
                                common_augmented,
                                centres,
                                q_graph,
                                0,
                                left[2],
                            )
                            and transfers_are_nonterminal(
                                common_augmented,
                                centres,
                                q_graph,
                                1,
                                right[2],
                            )
                        ):
                            arm_data = (
                                (left[0], left[2][2]),
                                (right[0], right[2][2]),
                            )
                            common_graph, common_marked = expanded_graph(
                                common_augmented,
                                centres,
                                q_graph,
                                arm_data,
                            )
                            if not expanded_is_terminal(
                                common_graph, common_marked
                            ):
                                common_literal = (
                                    left[0],
                                    right[0],
                                    left[2],
                                    right[2],
                                    common_graph,
                                )
                                counts["common_first_choices"] += 1

                    if any(literal_available):
                        first.setdefault(
                            "literal",
                            (
                                carrier_index,
                                centres,
                                q_graph,
                                literal_available,
                                next(
                                    outcome
                                    for outcome in literal_outcomes
                                    if outcome is not None
                                ),
                            ),
                        )
                    if common_literal is not None:
                        first.setdefault(
                            "common_literal",
                            (
                                carrier_index,
                                centres,
                                q_graph,
                                common_literal,
                            ),
                        )
                    update_digest(
                        digest,
                        code,
                        carrier_index,
                        centres,
                        q_graph,
                        (
                            quotient_available,
                            literal_available,
                            common_literal is not None,
                        ),
                    )

        assert counts["faithful_survivors"] == expected_survivors
        print(code, dict(counts), flush=True)
        print(code, "first", first, flush=True)
        print(code, "digest", digest.hexdigest(), flush=True)

    print("GREEN: explicit three-arm gate completed")
    print("split_cache", split.closes.cache_info())
    print("minor_cache", order9.has_target.cache_info())
    print("k7minus_cache", order9.has_k7_minus.cache_info())
    print("expanded_minor_cache", expanded_is_terminal.cache_info())


if __name__ == "__main__":
    main()
