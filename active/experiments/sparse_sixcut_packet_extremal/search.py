#!/usr/bin/env python3
"""Adversarial search for the sparse-six-cut packet extremal conjecture.

This is a development search, not a proof.  The boundary is independent.
Internal vertices are represented by bit adjacency masks and a six-bit
boundary-neighbourhood label.  Every rooted near-K5 test exhausts all
assignments of internal vertices to the five rooted bags or to no bag.
"""

from __future__ import annotations

import argparse
import itertools
import random


ALL_ROOTS = (1 << 6) - 1


def connected(mask: int, adjacency: tuple[int, ...]) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        at = bit.bit_length() - 1
        new = adjacency[at] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def internally_six_connected(
    adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> bool:
    order = len(adjacency)
    full = (1 << order) - 1
    for mask in range(1, full + 1):
        root_neighbours = 0
        internal_neighbours = 0
        rest = full ^ mask
        for vertex in range(order):
            if mask >> vertex & 1:
                root_neighbours |= labels[vertex]
                internal_neighbours |= adjacency[vertex] & rest
        if (root_neighbours.bit_count() + internal_neighbours.bit_count()) < 6:
            return False
    return True


def full_connected_masks(
    adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> tuple[int, ...]:
    answer = []
    for mask in range(1, 1 << len(adjacency)):
        if not connected(mask, adjacency):
            continue
        seen = 0
        for vertex in range(len(adjacency)):
            if mask >> vertex & 1:
                seen |= labels[vertex]
        if seen == ALL_ROOTS:
            answer.append(mask)
    return tuple(answer)


def packet_number_one(adjacency: tuple[int, ...], labels: tuple[int, ...]) -> bool:
    packets = full_connected_masks(adjacency, labels)
    return bool(packets) and not any(a & b == 0 for a, b in itertools.combinations(packets, 2))


def bag_connected(root: int, mask: int, adjacency: tuple[int, ...], labels: tuple[int, ...]) -> bool:
    if mask == 0:
        return True
    root_neighbours = sum(
        1 << vertex
        for vertex, label in enumerate(labels)
        if label >> root & 1
    )
    reached = mask & root_neighbours
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        at = bit.bit_length() - 1
        new = adjacency[at] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def bags_touch(
    root_a: int,
    mask_a: int,
    root_b: int,
    mask_b: int,
    adjacency: tuple[int, ...],
    labels: tuple[int, ...],
) -> bool:
    # The boundary is independent in this search.
    for vertex in range(len(adjacency)):
        if mask_a >> vertex & 1:
            if labels[vertex] >> root_b & 1:
                return True
            if adjacency[vertex] & mask_b:
                return True
        if mask_b >> vertex & 1 and labels[vertex] >> root_a & 1:
            return True
    return False


def rooted_near_k5_for_roots(
    roots: tuple[int, ...], adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> bool:
    order = len(adjacency)
    bags = [0] * 5

    def visit(vertex: int) -> bool:
        if vertex == order:
            if any(
                not bag_connected(root, mask, adjacency, labels)
                for root, mask in zip(roots, bags, strict=True)
            ):
                return False
            missing = sum(
                not bags_touch(roots[i], bags[i], roots[j], bags[j], adjacency, labels)
                for i, j in itertools.combinations(range(5), 2)
            )
            return missing <= 1
        # Unused, or assigned to one of the five rooted bags.
        if visit(vertex + 1):
            return True
        bit = 1 << vertex
        for target in range(5):
            bags[target] |= bit
            if visit(vertex + 1):
                return True
            bags[target] ^= bit
        return False

    return visit(0)


def has_five_rooted_near_k5(
    adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> bool:
    return any(
        rooted_near_k5_for_roots(tuple(r for r in range(6) if r != omitted), adjacency, labels)
        for omitted in range(6)
    )


def packet_pair_witness(
    adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> tuple[int, int] | None:
    packets = full_connected_masks(adjacency, labels)
    return next((pair for pair in itertools.combinations(packets, 2) if pair[0] & pair[1] == 0), None)


def rooted_near_k5_assignment(
    roots: tuple[int, ...], adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> tuple[int, ...] | None:
    """Return one exact five-bag assignment, if one exists."""
    order = len(adjacency)
    bags = [0] * 5

    def visit(vertex: int) -> tuple[int, ...] | None:
        if vertex == order:
            if any(
                not bag_connected(root, mask, adjacency, labels)
                for root, mask in zip(roots, bags, strict=True)
            ):
                return None
            missing = sum(
                not bags_touch(roots[i], bags[i], roots[j], bags[j], adjacency, labels)
                for i, j in itertools.combinations(range(5), 2)
            )
            return tuple(bags) if missing <= 1 else None
        answer = visit(vertex + 1)
        if answer is not None:
            return answer
        bit = 1 << vertex
        for target in range(5):
            bags[target] |= bit
            answer = visit(vertex + 1)
            if answer is not None:
                return answer
            bags[target] ^= bit
        return None

    return visit(0)


def any_rooted_assignment(
    adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    for omitted in range(6):
        roots = tuple(root for root in range(6) if root != omitted)
        assignment = rooted_near_k5_assignment(roots, adjacency, labels)
        if assignment is not None:
            return roots, assignment
    return None


def certificate_edges_for_connected_mask(
    mask: int, adjacency: tuple[int, ...], offset: int = 0
) -> set[int]:
    """Return variable indices of one spanning tree inside ``mask``."""
    if mask.bit_count() <= 1:
        return set()
    order = len(adjacency)
    pairs = tuple(itertools.combinations(range(order), 2))
    pair_index = {pair: offset + index for index, pair in enumerate(pairs)}
    start = (mask & -mask).bit_length() - 1
    reached = 1 << start
    answer: set[int] = set()
    while reached != mask:
        for left in range(order):
            if not (reached >> left & 1):
                continue
            choices = adjacency[left] & mask & ~reached
            if choices:
                bit = choices & -choices
                right = bit.bit_length() - 1
                pair = (left, right) if left < right else (right, left)
                answer.add(pair_index[pair])
                reached |= bit
                break
        else:
            raise AssertionError("mask was not connected")
    return answer


def variable_instance(order: int, present: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    pairs = tuple(itertools.combinations(range(order), 2))
    adjacency = [0] * order
    for index, (left, right) in enumerate(pairs):
        if present >> index & 1:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    labels = [0] * order
    offset = len(pairs)
    for vertex in range(order):
        for root in range(6):
            index = offset + 6 * vertex + root
            if present >> index & 1:
                labels[vertex] |= 1 << root
    return tuple(adjacency), tuple(labels)


def incidence_variable(order: int, vertex: int, root: int) -> int:
    return order * (order - 1) // 2 + 6 * vertex + root


def packet_certificate(
    pair: tuple[int, int], adjacency: tuple[int, ...], labels: tuple[int, ...]
) -> set[int]:
    answer: set[int] = set()
    for mask in pair:
        answer |= certificate_edges_for_connected_mask(mask, adjacency)
        for root in range(6):
            vertex = next(
                vertex
                for vertex in range(len(adjacency))
                if mask >> vertex & 1 and labels[vertex] >> root & 1
            )
            answer.add(incidence_variable(len(adjacency), vertex, root))
    return answer


def rooted_certificate(
    roots: tuple[int, ...],
    bags: tuple[int, ...],
    adjacency: tuple[int, ...],
    labels: tuple[int, ...],
) -> set[int]:
    order = len(adjacency)
    pairs = tuple(itertools.combinations(range(order), 2))
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    answer: set[int] = set()
    # Connect each rooted bag by a tree beginning with one root incidence.
    for root, mask in zip(roots, bags, strict=True):
        if not mask:
            continue
        unprocessed = mask
        while unprocessed:
            seed = (unprocessed & -unprocessed).bit_length() - 1
            component = 1 << seed
            frontier = component
            while frontier:
                bit = frontier & -frontier
                frontier ^= bit
                at = bit.bit_length() - 1
                new = adjacency[at] & mask & ~component
                component |= new
                frontier |= new
            first = next(v for v in range(order) if component >> v & 1 and labels[v] >> root & 1)
            answer.add(incidence_variable(order, first, root))
            reached = 1 << first
            while reached != component:
                for left in range(order):
                    if not (reached >> left & 1):
                        continue
                    choices = adjacency[left] & component & ~reached
                    if choices:
                        bit = choices & -choices
                        right = bit.bit_length() - 1
                        pair = (left, right) if left < right else (right, left)
                        answer.add(pair_index[pair])
                        reached |= bit
                        break
                else:
                    raise AssertionError("internal bag component was not connected")
            unprocessed ^= component
    # Pick one present contact for nine bag pairs.
    contacts: list[int] = []
    for i, j in itertools.combinations(range(5), 2):
        choices: list[int] = []
        for vertex in range(order):
            if bags[i] >> vertex & 1 and labels[vertex] >> roots[j] & 1:
                choices.append(incidence_variable(order, vertex, roots[j]))
            if bags[j] >> vertex & 1 and labels[vertex] >> roots[i] & 1:
                choices.append(incidence_variable(order, vertex, roots[i]))
        for left in range(order):
            if not (bags[i] >> left & 1):
                continue
            for right in range(order):
                if bags[j] >> right & 1 and adjacency[left] >> right & 1:
                    pair = (left, right) if left < right else (right, left)
                    choices.append(pair_index[pair])
        if choices:
            contacts.append(choices[0])
    assert len(contacts) >= 9
    answer.update(contacts[:9])
    return answer


def greedy_maximal_avoider(
    order: int, rng: random.Random, preserve_internal_six: bool = False
) -> tuple[int, tuple[int, ...], tuple[int, ...]] | None:
    variable_count = order * (order - 1) // 2 + 6 * order
    present = (1 << variable_count) - 1
    while True:
        adjacency, labels = variable_instance(order, present)
        packets = packet_pair_witness(adjacency, labels)
        if packets is not None:
            certificate = packet_certificate(packets, adjacency, labels)
            choices = list(certificate)
            if preserve_internal_six:
                choices = [
                    edge
                    for edge in choices
                    if internally_six_connected(*variable_instance(order, present & ~(1 << edge)))
                ]
            if not choices:
                return None
            present &= ~(1 << rng.choice(choices))
            continue
        rooted = any_rooted_assignment(adjacency, labels)
        if rooted is not None:
            roots, bags = rooted
            certificate = rooted_certificate(roots, bags, adjacency, labels)
            choices = list(certificate)
            if preserve_internal_six:
                choices = [
                    edge
                    for edge in choices
                    if internally_six_connected(*variable_instance(order, present & ~(1 << edge)))
                ]
            if not choices:
                return None
            present &= ~(1 << rng.choice(choices))
            continue
        return present.bit_count(), adjacency, labels


def excess(adjacency: tuple[int, ...], labels: tuple[int, ...]) -> int:
    internal_edges = sum(mask.bit_count() for mask in adjacency) // 2
    boundary_edges = sum(mask.bit_count() for mask in labels)
    return internal_edges + boundary_edges - 4 * len(adjacency)


def random_instance(order: int, rng: random.Random) -> tuple[tuple[int, ...], tuple[int, ...]]:
    adjacency = [0] * order
    p = rng.uniform(0.25, 0.95)
    for left, right in itertools.combinations(range(order), 2):
        if rng.random() < p:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
    labels = []
    q = rng.uniform(0.3, 0.95)
    for _ in range(order):
        label = sum(1 << root for root in range(6) if rng.random() < q)
        labels.append(label)
    return tuple(adjacency), tuple(labels)


def describe(adjacency: tuple[int, ...], labels: tuple[int, ...]) -> str:
    edges = [pair for pair in itertools.combinations(range(len(adjacency)), 2) if adjacency[pair[0]] >> pair[1] & 1]
    root_sets = [tuple(root for root in range(6) if label >> root & 1) for label in labels]
    return f"edges={edges} labels={root_sets} eta={excess(adjacency, labels)}"


def exact_small(order: int) -> None:
    """Exhaust every labelled instance through internal order three."""
    if order > 3:
        raise SystemExit("--mode exact-small is deliberately limited to order at most three")
    variable_count = order * (order - 1) // 2 + 6 * order
    feasible = packet_one = avoiding = 0
    best = -10**9
    best_instance = None
    for present in range(1 << variable_count):
        adjacency, labels = variable_instance(order, present)
        if not internally_six_connected(adjacency, labels):
            continue
        feasible += 1
        if not packet_number_one(adjacency, labels):
            continue
        packet_one += 1
        if has_five_rooted_near_k5(adjacency, labels):
            continue
        avoiding += 1
        value = excess(adjacency, labels)
        if value > best:
            best = value
            best_instance = adjacency, labels
    print(
        f"EXACT_SMALL order={order} feasible={feasible} "
        f"packet_one={packet_one} avoiding={avoiding} best_eta={best}"
    )
    if best_instance is not None:
        print(f"best_avoiding {describe(*best_instance)}")
    assert best < 6
    print("NO_COUNTEREXAMPLE_EXACT")


def exact_clique_four() -> None:
    """Exhaust boundary labels on a four-vertex internal clique.

    Vertex symmetry permits nondecreasing labels.  Only instances at the
    conjectured threshold are sent to the exact rooted-model test.
    """
    adjacency = (0b1110, 0b1101, 0b1011, 0b0111)
    threshold = feasible = packet_one = avoiding = 0
    for labels in itertools.combinations_with_replacement(range(64), 4):
        if excess(adjacency, labels) < 6:
            continue
        threshold += 1
        if not internally_six_connected(adjacency, labels):
            continue
        feasible += 1
        if not packet_number_one(adjacency, labels):
            continue
        packet_one += 1
        if has_five_rooted_near_k5(adjacency, labels):
            continue
        avoiding += 1
        raise AssertionError(f"counterexample: {describe(adjacency, labels)}")
    print(
        f"EXACT_CLIQUE_FOUR threshold={threshold} feasible={feasible} "
        f"packet_one={packet_one} avoiding={avoiding}"
    )
    print("NO_COUNTEREXAMPLE_EXACT")


def self_test() -> None:
    universal_edge = ((0b10, 0b01), (ALL_ROOTS, ALL_ROOTS))
    assert internally_six_connected(*universal_edge)
    assert excess(*universal_edge) == 5
    assert not has_five_rooted_near_k5(*universal_edge)
    assert packet_pair_witness(*universal_edge) is not None

    triangle = ((0b110, 0b101, 0b011), (15, 51, 61))
    assert internally_six_connected(*triangle)
    assert excess(*triangle) == 4
    assert packet_number_one(*triangle)
    assert not has_five_rooted_near_k5(*triangle)

    # Carrier packing alone is insufficient: this eta-seven K4 has packing
    # number one, but its exact rooted model is the required alternative.
    carrier_barrier = ((0b1110, 0b1101, 0b1011, 0b0111), (27, 23, 11, 63))
    assert internally_six_connected(*carrier_barrier)
    assert excess(*carrier_barrier) == 7
    assert packet_number_one(*carrier_barrier)
    assert has_five_rooted_near_k5(*carrier_barrier)
    print("SELF_TEST_GREEN")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("random", "exact-small", "exact-clique-four", "self-test"),
        default="random",
    )
    parser.add_argument("--order", type=int, default=7)
    parser.add_argument("--trials", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=20260817)
    args = parser.parse_args()
    if args.mode == "exact-small":
        exact_small(args.order)
        return
    if args.mode == "exact-clique-four":
        exact_clique_four()
        return
    if args.mode == "self-test":
        self_test()
        return
    rng = random.Random(args.seed)
    feasible = packet_one = rooted_tests = 0
    best = -10**9
    best_instance = None
    for trial in range(args.trials):
        adjacency, labels = random_instance(args.order, rng)
        value = excess(adjacency, labels)
        if value < 5 or not internally_six_connected(adjacency, labels):
            continue
        feasible += 1
        if not packet_number_one(adjacency, labels):
            continue
        packet_one += 1
        rooted_tests += 1
        if has_five_rooted_near_k5(adjacency, labels):
            continue
        if value > best:
            best = value
            best_instance = (adjacency, labels)
            print(f"new_best trial={trial} {describe(adjacency, labels)}", flush=True)
        if value >= 6:
            print(f"COUNTEREXAMPLE {describe(adjacency, labels)}")
            return
    print(f"order={args.order} trials={args.trials} feasible={feasible} packet_one={packet_one} rooted_tests={rooted_tests}")
    if best_instance is not None:
        print(f"best_avoiding {describe(*best_instance)}")
    print("NO_COUNTEREXAMPLE_IN_RANDOM_SAMPLE")


if __name__ == "__main__":
    main()
