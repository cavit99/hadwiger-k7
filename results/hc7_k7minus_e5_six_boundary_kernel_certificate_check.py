#!/usr/bin/env python3
"""Independently check the six-boundary kernel certificates.

The checker imports no code from the certificate generator.  It reconstructs
each labelled host, checks every recorded ``K_7^-`` branch-set model, and
independently enumerates the claimed boundary-mask/missed-root catalogue.  It
also exhaustively checks the six recorded one-edge-below target-free hosts.

Invocation:

    python3 results/hc7_k7minus_e5_six_boundary_kernel_certificate_check.py

or, with an explicit certificate path:

    python3 results/hc7_k7minus_e5_six_boundary_kernel_certificate_check.py \
        results/hc7_k7minus_e5_six_boundary_kernel_certificates.json

Expected final line:

    PASS independent six-boundary kernel certificate check
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator


FORMAT = "rooted-quasi5-boundary-certificates-v1"
TARGET = "K7-minus"
EXPECTED_SHA256 = "4b148b7a4bd2845e1311e5e67a1d6706048c3791d6cd29bf12676cb37e5fd905"
BOUNDARY = tuple(range(6))
BOUNDARY_PAIRS = tuple(itertools.combinations(BOUNDARY, 2))
BOUNDARY_MASK_LIMIT = 1 << len(BOUNDARY_PAIRS)
SIX_FULL_SENTINEL = 6


@dataclass(frozen=True)
class Case:
    kernel: str
    threshold: int
    missed_roots: tuple[int, ...]
    host_order: int


CASES = {
    "adjacent_singletons_k2_five_full": Case("k2", 13, BOUNDARY, 9),
    "crossing_twins_p3_five_full": Case("p3", 13, BOUNDARY, 10),
    "crossing_edge_k3_five_full": Case("k3", 12, BOUNDARY, 10),
    "adjacent_singletons_k2_six_full": Case("k2", 13, (SIX_FULL_SENTINEL,), 9),
    "crossing_twins_p3_six_full": Case("p3", 11, (SIX_FULL_SENTINEL,), 10),
    "crossing_edge_k3_six_full": Case("k3", 10, (SIX_FULL_SENTINEL,), 10),
}

# Each boundary mask has one fewer edge than the threshold in its case.  The
# accompanying missed-root value is 6 precisely in the six-full cases.
SHARPNESS_WITNESSES = {
    "adjacent_singletons_k2_five_full": (4095, 3),
    "crossing_twins_p3_five_full": (29439, 5),
    "crossing_edge_k3_five_full": (13055, 5),
    "adjacent_singletons_k2_six_full": (23550, 6),
    "crossing_twins_p3_six_full": (12927, 6),
    "crossing_edge_k3_six_full": (6463, 6),
}
EXPECTED_PARTITION_COUNTS = {9: 750, 10: 11_880}


class CertificateError(Exception):
    """A malformed or mathematically invalid certificate."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateError(message)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise CertificateError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def add_edge(graph: list[set[int]], left: int, right: int) -> None:
    require(left != right, "host construction attempted a loop")
    graph[left].add(right)
    graph[right].add(left)


def reconstruct_host(
    case: Case, boundary_mask: int, missed_root: int
) -> list[set[int]]:
    """Construct one host directly from the labelled kernel definition."""

    graph = [set() for _ in range(case.host_order)]
    for bit, (left, right) in enumerate(BOUNDARY_PAIRS):
        if boundary_mask >> bit & 1:
            add_edge(graph, left, right)

    if case.kernel == "k2":
        first, second, representative = 6, 7, 8
        add_edge(graph, first, second)
        for root in (0, 1, 2, 3):
            add_edge(graph, first, root)
        for root in (0, 1, 4, 5):
            add_edge(graph, second, root)
    else:
        centre, first, second, representative = 6, 7, 8, 9
        add_edge(graph, centre, first)
        add_edge(graph, centre, second)
        if case.kernel == "k3":
            add_edge(graph, first, second)
        else:
            require(case.kernel == "p3", f"unknown kernel {case.kernel!r}")
        for root in (0, 1, 2):
            add_edge(graph, centre, root)
        for low_vertex in (first, second):
            for root in (0, 3, 4, 5):
                add_edge(graph, low_vertex, root)

    for root in BOUNDARY:
        if missed_root == SIX_FULL_SENTINEL or root != missed_root:
            add_edge(graph, representative, root)
    return graph


def mask_vertices(mask: int, order: int) -> set[int]:
    return {vertex for vertex in range(order) if mask >> vertex & 1}


def connected(graph: list[set[int]], vertices: set[int]) -> bool:
    if not vertices:
        return False
    reached = {min(vertices)}
    frontier = list(reached)
    while frontier:
        vertex = frontier.pop()
        for neighbour in graph[vertex] & vertices - reached:
            reached.add(neighbour)
            frontier.append(neighbour)
    return reached == vertices


def validate_model(graph: list[set[int]], raw_bags: object, context: str) -> int:
    require(type(raw_bags) is list, f"{context}: bags must be a list")
    bags = raw_bags
    require(len(bags) == 7, f"{context}: expected seven branch sets")
    require(
        all(type(mask) is int and mask > 0 for mask in bags),
        f"{context}: branch-set masks must be positive integers",
    )

    full_mask = (1 << len(graph)) - 1
    used_mask = 0
    branch_sets: list[set[int]] = []
    for index, mask in enumerate(bags):
        require(
            mask & ~full_mask == 0,
            f"{context}: bag {index} exceeds the host order",
        )
        require(
            mask & used_mask == 0,
            f"{context}: bag {index} overlaps an earlier bag",
        )
        vertices = mask_vertices(mask, len(graph))
        require(connected(graph, vertices), f"{context}: bag {index} is disconnected")
        used_mask |= mask
        branch_sets.append(vertices)

    missing_pairs = 0
    for first, second in itertools.combinations(range(7), 2):
        adjacent = any(
            graph[vertex] & branch_sets[second]
            for vertex in branch_sets[first]
        )
        if not adjacent:
            missing_pairs += 1
    require(
        missing_pairs <= 1,
        f"{context}: branch-set quotient has {missing_pairs} missing pairs",
    )
    return missing_pairs


def expected_keys(case: Case) -> set[tuple[int, int]]:
    return {
        (boundary_mask, missed_root)
        for boundary_mask in range(BOUNDARY_MASK_LIMIT)
        if boundary_mask.bit_count() >= case.threshold
        for missed_root in case.missed_roots
    }


def partitions_into_seven(
    vertices: tuple[int, ...],
) -> Iterator[tuple[frozenset[int], ...]]:
    """Yield every unlabelled partition of ``vertices`` into seven blocks."""

    blocks: list[set[int]] = []

    def extend(index: int) -> Iterator[tuple[frozenset[int], ...]]:
        remaining = len(vertices) - index
        if len(blocks) > 7 or len(blocks) + remaining < 7:
            return
        if index == len(vertices):
            if len(blocks) == 7:
                yield tuple(frozenset(block) for block in blocks)
            return

        vertex = vertices[index]
        for block in blocks:
            block.add(vertex)
            yield from extend(index + 1)
            block.remove(vertex)
        if len(blocks) < 7:
            blocks.append({vertex})
            yield from extend(index + 1)
            blocks.pop()

    yield from extend(0)


def exhaustive_minor_search(graph: list[set[int]]) -> tuple[bool, int]:
    """Test every seven-branch-set model, allowing unused host vertices."""

    checked = 0
    for used_order in range(7, len(graph) + 1):
        for used in itertools.combinations(range(len(graph)), used_order):
            for branch_sets in partitions_into_seven(used):
                checked += 1
                if not all(
                    connected(graph, set(branch_set))
                    for branch_set in branch_sets
                ):
                    continue
                missing_pairs = sum(
                    not any(
                        graph[vertex] & branch_sets[second]
                        for vertex in branch_sets[first]
                    )
                    for first, second in itertools.combinations(range(7), 2)
                )
                if missing_pairs <= 1:
                    return True, checked
    return False, checked


def check_sharpness() -> list[tuple[str, int, int, int]]:
    """Exhaustively verify the six one-edge-below target-free hosts."""

    results = []
    for name, case in CASES.items():
        boundary_mask, missed_root = SHARPNESS_WITNESSES[name]
        require(
            boundary_mask.bit_count() == case.threshold - 1,
            f"{name}: sharpness witness is not one edge below threshold",
        )
        require(
            missed_root in case.missed_roots,
            f"{name}: invalid sharpness missed root",
        )
        graph = reconstruct_host(case, boundary_mask, missed_root)
        found, checked = exhaustive_minor_search(graph)
        require(not found, f"{name}: purported sharpness witness contains K7-minus")
        require(
            checked == EXPECTED_PARTITION_COUNTS[case.host_order],
            f"{name}: incomplete partition enumeration ({checked})",
        )
        results.append((name, boundary_mask, missed_root, checked))
    return results


def check_certificate(path: Path) -> None:
    raw = path.read_bytes()
    try:
        payload = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CertificateError(f"cannot decode certificate: {error}") from error

    require(type(payload) is dict, "top-level JSON value must be an object")
    require(
        set(payload) == {"format", "target", "coverage", "records"},
        "unexpected top-level certificate fields",
    )
    require(payload["format"] == FORMAT, "unexpected certificate format")
    require(payload["target"] == TARGET, "unexpected target")
    require(type(payload["coverage"]) is dict, "coverage must be an object")
    require(type(payload["records"]) is list, "records must be a list")

    catalogues = {name: expected_keys(case) for name, case in CASES.items()}
    expected_coverage = {name: len(keys) for name, keys in catalogues.items()}
    require(payload["coverage"] == expected_coverage, "incorrect coverage summary")

    seen = {name: set() for name in CASES}
    quotient_counts: Counter[int] = Counter()
    for index, raw_record in enumerate(payload["records"]):
        context = f"record {index}"
        require(type(raw_record) is dict, f"{context}: record must be an object")
        require(
            set(raw_record)
            == {"case", "boundary_mask", "boundary_edge_count", "missed_root", "bags"},
            f"{context}: unexpected record fields",
        )

        case_name = raw_record["case"]
        require(
            type(case_name) is str and case_name in CASES,
            f"{context}: unknown case",
        )
        case = CASES[case_name]
        boundary_mask = raw_record["boundary_mask"]
        edge_count = raw_record["boundary_edge_count"]
        missed_root = raw_record["missed_root"]
        require(
            type(boundary_mask) is int and 0 <= boundary_mask < BOUNDARY_MASK_LIMIT,
            f"{context}: invalid boundary mask",
        )
        require(type(edge_count) is int, f"{context}: invalid boundary edge count")
        require(
            edge_count == boundary_mask.bit_count(),
            f"{context}: boundary edge count does not match its mask",
        )
        require(edge_count >= case.threshold, f"{context}: boundary is below threshold")
        require(
            type(missed_root) is int and missed_root in case.missed_roots,
            f"{context}: invalid missed root",
        )

        key = (boundary_mask, missed_root)
        require(key not in seen[case_name], f"{context}: duplicate case key")
        seen[case_name].add(key)
        graph = reconstruct_host(case, boundary_mask, missed_root)
        quotient_counts[validate_model(graph, raw_record["bags"], context)] += 1

    for name in CASES:
        require(
            seen[name] == catalogues[name],
            f"{name}: certificate does not equal the independent catalogue",
        )

    digest = hashlib.sha256(raw).hexdigest()
    require(
        digest == EXPECTED_SHA256,
        f"certificate SHA-256 is {digest}, expected {EXPECTED_SHA256}",
    )
    require(
        quotient_counts == Counter({1: 11_462, 0: 452}),
        "unexpected quotient-model counts",
    )

    sharpness = check_sharpness()

    print(f"records={len(payload['records'])}")
    for name in CASES:
        print(f"{name}={len(seen[name])}")
    print(
        f"quotient_K7={quotient_counts[0]} "
        f"quotient_exact_K7minus={quotient_counts[1]}"
    )
    for name, boundary_mask, missed_root, checked in sharpness:
        print(
            f"sharpness_{name}: mask={boundary_mask} missed_root={missed_root} "
            f"partitions={checked} target_free"
        )
    print(f"certificate_sha256={digest}")
    print("PASS independent six-boundary kernel certificate check")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name(
            "hc7_k7minus_e5_six_boundary_kernel_certificates.json"
        ),
    )
    arguments = parser.parse_args()
    try:
        check_certificate(arguments.certificate)
    except (CertificateError, OSError) as error:
        raise SystemExit(f"FAIL: {error}") from error


if __name__ == "__main__":
    main()
