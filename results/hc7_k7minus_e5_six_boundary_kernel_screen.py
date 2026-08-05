#!/usr/bin/env python3
"""Exact finite screens for the E5 six-boundary kernel reduction.

This script proves six bounded statements by exhaustive enumeration of the
15 possible edges on a labelled six-vertex boundary P and by producing an
explicit K_7^- branch-set certificate for every enumerated case.

No unbounded graph-theoretic claim is encoded here.

Usage from the repository root:
    python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py sanity
    python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py generate \
        --output /tmp/e5-six-boundary-kernel-certificates.json
    python3 results/hc7_k7minus_e5_six_boundary_kernel_screen.py check \
        results/hc7_k7minus_e5_six_boundary_kernel_certificates.json

The three labelled kernels and their five-full and six-full ranges are
defined in the adjacent theorem note.  The companion certificate checker is
an implementation-independent validation path.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence

TARGET_ORDER = 7
MAX_MISSING = 1
BOUNDARY_ORDER = 6
BOUNDARY_EDGES = tuple(itertools.combinations(range(BOUNDARY_ORDER), 2))


@dataclass(frozen=True)
class CaseSpec:
    name: str
    kernel: str
    host_order: int
    min_boundary_edges: int
    missed_roots: tuple[int, ...]


FIVE_FULL_ROOTS = tuple(range(BOUNDARY_ORDER))
SIX_FULL_ROOT = (BOUNDARY_ORDER,)  # sentinel: the high representative sees all six roots

CASES = (
    CaseSpec("adjacent_singletons_k2_five_full", "adjacent_singletons_k2", 9, 13, FIVE_FULL_ROOTS),
    CaseSpec("crossing_twins_p3_five_full", "crossing_twins_p3", 10, 13, FIVE_FULL_ROOTS),
    CaseSpec("crossing_edge_k3_five_full", "crossing_edge_k3", 10, 12, FIVE_FULL_ROOTS),
    CaseSpec("adjacent_singletons_k2_six_full", "adjacent_singletons_k2", 9, 13, SIX_FULL_ROOT),
    CaseSpec("crossing_twins_p3_six_full", "crossing_twins_p3", 10, 11, SIX_FULL_ROOT),
    CaseSpec("crossing_edge_k3_six_full", "crossing_edge_k3", 10, 10, SIX_FULL_ROOT),
)

# Each tuple is (label, kernel, boundary mask, missed-root sentinel).  The
# boundary has exactly one edge fewer than the corresponding positive range,
# and exhaustive seven-bag enumeration finds no K_7^- model.  The independent
# checker reconstructs and verifies the same six witnesses separately.
SHARPNESS_WITNESSES = (
    ("K2 five-full", "adjacent_singletons_k2", 4095, 3),
    ("P3 five-full", "crossing_twins_p3", 29439, 5),
    ("K3 five-full", "crossing_edge_k3", 13055, 5),
    ("K2 six-full", "adjacent_singletons_k2", 23550, BOUNDARY_ORDER),
    ("P3 six-full", "crossing_twins_p3", 12927, BOUNDARY_ORDER),
    ("K3 six-full", "crossing_edge_k3", 6463, BOUNDARY_ORDER),
)


def add_edge(adj: list[int], u: int, v: int) -> None:
    adj[u] |= 1 << v
    adj[v] |= 1 << u


def boundary_mask_edges(mask: int) -> int:
    return mask.bit_count()


def build_kernel(case_name: str, boundary_mask: int, missed_root: int) -> list[int]:
    """Return adjacency bitmasks for one labelled kernel.

    Boundary vertices are 0,...,5.  The high-shore representative is adjacent
    to all boundary vertices except ``missed_root``.

    adjacent_singletons_k2:
        low vertices d,w form K2;
        N_P(d)={0,1,2,3}, N_P(w)={0,1,4,5}.

    crossing_twins_p3:
        low vertices d,f1,f2 induce P3 with centre d;
        N_P(d)={0,1,2}, N_P(f_i)={0,3,4,5}.

    crossing_edge_k3:
        same contacts, but d,f1,f2 induce K3.
    """
    if not 0 <= missed_root <= BOUNDARY_ORDER:
        raise ValueError("missed_root must lie in 0,...,6; 6 denotes a six-full representative")

    n = 9 if case_name == "adjacent_singletons_k2" else 10
    adj = [0] * n

    for i, (u, v) in enumerate(BOUNDARY_EDGES):
        if (boundary_mask >> i) & 1:
            add_edge(adj, u, v)

    if case_name == "adjacent_singletons_k2":
        d, w, high = 6, 7, 8
        add_edge(adj, d, w)
        for root in (0, 1, 2, 3):
            add_edge(adj, d, root)
        for root in (0, 1, 4, 5):
            add_edge(adj, w, root)
    elif case_name in {"crossing_twins_p3", "crossing_edge_k3"}:
        d, f1, f2, high = 6, 7, 8, 9
        add_edge(adj, d, f1)
        add_edge(adj, d, f2)
        if case_name == "crossing_edge_k3":
            add_edge(adj, f1, f2)
        for root in (0, 1, 2):
            add_edge(adj, d, root)
        for f in (f1, f2):
            for root in (0, 3, 4, 5):
                add_edge(adj, f, root)
    else:
        raise ValueError(f"unknown case: {case_name}")

    for root in range(BOUNDARY_ORDER):
        if missed_root == BOUNDARY_ORDER or root != missed_root:
            add_edge(adj, high, root)

    return adj


def restricted_growth_partitions(items: Sequence[int], blocks: int) -> Iterator[tuple[int, ...]]:
    """Yield set partitions as tuples of bitmasks, without label duplicates."""
    n = len(items)
    if n < blocks:
        return

    labels = [0] * n

    def rec(index: int, max_label: int) -> Iterator[tuple[int, ...]]:
        if index == n:
            if max_label == blocks - 1:
                out = [0] * blocks
                for vertex, label in zip(items, labels):
                    out[label] |= 1 << vertex
                yield tuple(out)
            return

        upper = min(max_label + 1, blocks - 1)
        for label in range(upper + 1):
            labels[index] = label
            new_max = max(max_label, label)
            if new_max + (n - index - 1) >= blocks - 1:
                yield from rec(index + 1, new_max)

    labels[0] = 0
    yield from rec(1, 0)


def all_candidate_partitions(host_order: int) -> tuple[tuple[int, ...], ...]:
    """Precompute every possible seven-bag model using any host subset."""
    out: list[tuple[int, ...]] = []
    vertices = tuple(range(host_order))
    for used_order in range(TARGET_ORDER, host_order + 1):
        for used in itertools.combinations(vertices, used_order):
            out.extend(restricted_growth_partitions(used, TARGET_ORDER))
    return tuple(out)


PARTITIONS = {order: all_candidate_partitions(order) for order in {7, 8, *(spec.host_order for spec in CASES)}}


def connected_subsets(adj: Sequence[int]) -> list[bool]:
    n = len(adj)
    connected = [False] * (1 << n)
    for mask in range(1, 1 << n):
        first = mask & -mask
        seen = first
        frontier = first
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            new = adj[vertex] & mask & ~seen
            seen |= new
            frontier |= new
        connected[mask] = seen == mask
    return connected


def neighbourhood_unions(adj: Sequence[int]) -> list[int]:
    n = len(adj)
    unions = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        vertex = bit.bit_length() - 1
        unions[mask] = unions[mask ^ bit] | adj[vertex]
    return unions


def find_k7minus_model(adj: Sequence[int]) -> tuple[int, ...] | None:
    """Find seven connected bags whose quotient has at most one missing pair."""
    connected = connected_subsets(adj)
    neighbour_union = neighbourhood_unions(adj)

    for bags in PARTITIONS[len(adj)]:
        if any(not connected[bag] for bag in bags):
            continue

        missing = 0
        for i in range(TARGET_ORDER):
            neighbours = neighbour_union[bags[i]]
            for j in range(i + 1, TARGET_ORDER):
                if not (neighbours & bags[j]):
                    missing += 1
                    if missing > MAX_MISSING:
                        break
            if missing > MAX_MISSING:
                break

        if missing <= MAX_MISSING:
            return bags

    return None


def validate_model(adj: Sequence[int], bags: Sequence[int]) -> None:
    if len(bags) != TARGET_ORDER:
        raise AssertionError("certificate must contain exactly seven bags")
    if any(bag == 0 for bag in bags):
        raise AssertionError("branch sets must be nonempty")

    used = 0
    connected = connected_subsets(adj)
    for bag in bags:
        if used & bag:
            raise AssertionError("branch sets are not disjoint")
        used |= bag
        if not connected[bag]:
            raise AssertionError("a branch set is disconnected")

    neighbour_union = neighbourhood_unions(adj)
    missing = 0
    for i in range(TARGET_ORDER):
        for j in range(i + 1, TARGET_ORDER):
            if not (neighbour_union[bags[i]] & bags[j]):
                missing += 1
    if missing > MAX_MISSING:
        raise AssertionError(f"quotient has {missing} missing pairs")


def masks_with_at_least(min_edges: int) -> Iterator[int]:
    for edge_count in range(min_edges, len(BOUNDARY_EDGES) + 1):
        for chosen in itertools.combinations(range(len(BOUNDARY_EDGES)), edge_count):
            mask = 0
            for index in chosen:
                mask |= 1 << index
            yield mask


def expected_case_count(spec: CaseSpec) -> int:
    boundary_graphs = sum(
        math.comb(len(BOUNDARY_EDGES), k)
        for k in range(spec.min_boundary_edges, len(BOUNDARY_EDGES) + 1)
    )
    return len(spec.missed_roots) * boundary_graphs


def generate_certificates(output: Path) -> None:
    records: list[dict[str, object]] = []
    summary: dict[str, int] = {}

    for spec in CASES:
        count = 0
        for boundary_mask in masks_with_at_least(spec.min_boundary_edges):
            for missed_root in spec.missed_roots:
                adj = build_kernel(spec.kernel, boundary_mask, missed_root)
                model = find_k7minus_model(adj)
                if model is None:
                    raise AssertionError(
                        f"uncovered case: {spec.name}, mask={boundary_mask}, miss={missed_root}"
                    )
                validate_model(adj, model)
                records.append(
                    {
                        "case": spec.name,
                        "boundary_mask": boundary_mask,
                        "boundary_edge_count": boundary_mask_edges(boundary_mask),
                        "missed_root": missed_root,
                        "bags": list(model),
                    }
                )
                count += 1

        expected = expected_case_count(spec)
        if count != expected:
            raise AssertionError(f"coverage mismatch for {spec.name}: {count} != {expected}")
        summary[spec.name] = count

    payload = {
        "format": "rooted-quasi5-boundary-certificates-v1",
        "target": "K7-minus",
        "coverage": summary,
        "records": records,
    }
    output.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")), encoding="utf-8")
    digest = hashlib.sha256(output.read_bytes()).hexdigest()

    print(f"wrote {output}")
    for name, count in summary.items():
        print(f"  {name}: {count} cases")
    print(f"  total: {len(records)} cases")
    print(f"  sha256: {digest}")


def check_certificates(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise AssertionError("certificate payload must be an object")
    if payload.get("format") != "rooted-quasi5-boundary-certificates-v1":
        raise AssertionError("unexpected certificate format")
    if payload.get("target") != "K7-minus":
        raise AssertionError("unexpected certificate target")
    if not isinstance(payload.get("records"), list):
        raise AssertionError("certificate records must be a list")

    seen: dict[str, set[tuple[int, int]]] = {spec.name: set() for spec in CASES}
    specs = {spec.name: spec for spec in CASES}

    for record in payload["records"]:
        if not isinstance(record, dict):
            raise AssertionError("each certificate record must be an object")
        case_name = record["case"]
        if case_name not in specs:
            raise AssertionError(f"unknown certificate case: {case_name}")
        spec = specs[case_name]
        boundary_mask = int(record["boundary_mask"])
        missed_root = int(record["missed_root"])
        bags = tuple(int(value) for value in record["bags"])

        if not 0 <= boundary_mask < 1 << len(BOUNDARY_EDGES):
            raise AssertionError("boundary mask lies outside the fifteen-edge range")
        if int(record["boundary_edge_count"]) != boundary_mask_edges(boundary_mask):
            raise AssertionError("recorded boundary edge count is incorrect")
        if boundary_mask_edges(boundary_mask) < spec.min_boundary_edges:
            raise AssertionError("certificate lies outside the claimed edge range")
        if missed_root not in spec.missed_roots:
            raise AssertionError("missed root lies outside the claimed case")
        if any(not 0 < bag < 1 << spec.host_order for bag in bags):
            raise AssertionError("branch-set mask lies outside the host")
        key = (boundary_mask, missed_root)
        if key in seen[case_name]:
            raise AssertionError("duplicate certificate")
        seen[case_name].add(key)

        adj = build_kernel(spec.kernel, boundary_mask, missed_root)
        validate_model(adj, bags)

    for spec in CASES:
        expected_keys = {
            (mask, missed_root)
            for mask in masks_with_at_least(spec.min_boundary_edges)
            for missed_root in spec.missed_roots
        }
        if seen[spec.name] != expected_keys:
            missing = expected_keys - seen[spec.name]
            extra = seen[spec.name] - expected_keys
            raise AssertionError(
                f"coverage failure for {spec.name}: missing={len(missing)}, extra={len(extra)}"
            )

    expected_coverage = {spec.name: expected_case_count(spec) for spec in CASES}
    if payload.get("coverage") != expected_coverage:
        raise AssertionError("coverage metadata does not match the exhaustive ranges")

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"verified {path}")
    print(f"  records: {sum(len(values) for values in seen.values())}")
    print(f"  sha256: {digest}")


def graph_from_edges(order: int, edges: Iterable[tuple[int, int]]) -> list[int]:
    adj = [0] * order
    for u, v in edges:
        add_edge(adj, u, v)
    return adj


def sanity() -> None:
    # K_7^- is positive.
    k7minus_edges = [
        (u, v)
        for u, v in itertools.combinations(range(7), 2)
        if (u, v) != (0, 1)
    ]
    if find_k7minus_model(graph_from_edges(7, k7minus_edges)) is None:
        raise AssertionError("failed positive sanity check on K_7^-")

    # K_7^vee itself is negative: it has two incident missing edges and no
    # contraction is possible without reducing the order below seven.
    k7vee_edges = [
        (u, v)
        for u, v in itertools.combinations(range(7), 2)
        if (u, v) not in {(0, 1), (0, 2)}
    ]
    if find_k7minus_model(graph_from_edges(7, k7vee_edges)) is not None:
        raise AssertionError("false positive on K_7^vee")

    # The repository's eight-vertex complement-of-P8 local barrier is negative.
    p8_edges = {(i, i + 1) for i in range(7)}
    complement_p8 = [
        (u, v)
        for u, v in itertools.combinations(range(8), 2)
        if (u, v) not in p8_edges
    ]
    if find_k7minus_model(graph_from_edges(8, complement_p8)) is not None:
        raise AssertionError("false positive on complement(P8)")

    for label, kernel, boundary_mask, missed_root in SHARPNESS_WITNESSES:
        if find_k7minus_model(build_kernel(kernel, boundary_mask, missed_root)) is not None:
            raise AssertionError(f"false positive on one-edge-below witness: {label}")

    print("sanity checks passed: K7^- positive; K7^vee and complement(P8) negative")
    print("sharpness checks passed: all six one-edge-below labelled hosts are target-free")
    for order, partitions in sorted(PARTITIONS.items()):
        print(f"  host order {order}: {len(partitions)} candidate branch-set partitions")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="enumerate all cases and write certificates")
    generate.add_argument("--output", type=Path, required=True)

    check = subparsers.add_parser("check", help="independently validate a certificate file")
    check.add_argument("path", type=Path)

    subparsers.add_parser("sanity", help="run known positive and negative examples")
    return parser.parse_args()


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O: certificate validation requires assertions")
    args = parse_args()
    if args.command == "generate":
        generate_certificates(args.output)
    elif args.command == "check":
        check_certificates(args.path)
    elif args.command == "sanity":
        sanity()
    else:
        raise AssertionError("unreachable")


if __name__ == "__main__":
    main()
