#!/usr/bin/env python3
"""Independently check the order-eight rooted OCT/triangle certificate.

This checker imports no generator code.  It recognizes K4 minors directly
from the branch-set definition, rebuilds the complete marked catalogue, and
validates every recorded OCT or triangle witness.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ORDER = 8
ALL_VERTICES = (1 << ORDER) - 1
FULL = ORDER
EXPECTED_GRAPHS = 12_346
EXPECTED_ELIGIBLE = 185
EXPECTED_PROFILES = 13_505
EXPECTED_OCT = 13_247
EXPECTED_TRIANGLES = 258
EXPECTED_SHA256 = "c7a4323ec9f23faa1499d8891c33eced2f11ca7270db98bb44dcc8832bb0520d"

DELETION_MASKS = tuple(
    sum(1 << vertex for vertex in vertices)
    for size in range(3)
    for vertices in itertools.combinations(range(ORDER), size)
)
PROFILES = (
    ((FULL, FULL),)
    + tuple((FULL, vertex) for vertex in range(ORDER))
    + tuple((vertex, FULL) for vertex in range(ORDER))
    + tuple(
        (first, second)
        for first in range(ORDER)
        for second in range(ORDER)
        if first != second
    )
)


def catalogue_codes() -> list[str]:
    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("missing dependency: install nauty so that `geng` is on PATH")
    result = subprocess.run(
        [executable, "-q", str(ORDER)],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    codes = sorted(
        line
        for line in result.stdout.splitlines()
        if line and not line.startswith(">")
    )
    if len(codes) != EXPECTED_GRAPHS or len(set(codes)) != EXPECTED_GRAPHS:
        raise AssertionError(
            f"expected {EXPECTED_GRAPHS} distinct catalogue entries, got {len(codes)}"
        )
    return codes


def graph6_edges(code: str) -> frozenset[tuple[int, int]]:
    """Decode graph6 directly as an unordered edge set."""

    values = [ord(character) - 63 for character in code]
    if not values or values[0] != ORDER:
        raise AssertionError(f"not an order-{ORDER} graph6 code: {code!r}")
    bits = [
        (value >> shift) & 1
        for value in values[1:]
        for shift in range(5, -1, -1)
    ]
    pairs = [
        (left, right)
        for right in range(1, ORDER)
        for left in range(right)
    ]
    return frozenset(
        edge for edge, bit in zip(pairs, bits, strict=False) if bit
    )


def adjacency_rows(edges: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    rows = [0] * ORDER
    for left, right in edges:
        rows[left] |= 1 << right
        rows[right] |= 1 << left
    return tuple(rows)


def connected(rows: tuple[int, ...], vertices: int) -> bool:
    reached = vertices & -vertices
    while reached:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            neighbours |= rows[bit.bit_length() - 1]
        reached |= neighbours & vertices
        if reached == old:
            return reached == vertices
    return False


def has_k4_minor(
    edges: frozenset[tuple[int, int]], allowed: int = ALL_VERTICES
) -> bool:
    """Search directly for four valid K4-minor branch sets."""

    rows = adjacency_rows(edges)
    neighbourhoods = [0] * (1 << ORDER)
    for mask in range(1, 1 << ORDER):
        bit = mask & -mask
        neighbourhoods[mask] = (
            neighbourhoods[mask ^ bit] | rows[bit.bit_length() - 1]
        )
    branch_sets = [
        mask
        for mask in range(1, 1 << ORDER)
        if not mask & ~allowed and connected(rows, mask)
    ]
    for first_index, first in enumerate(branch_sets):
        for second_index in range(first_index + 1, len(branch_sets)):
            second = branch_sets[second_index]
            if first & second or not neighbourhoods[first] & second:
                continue
            for third_index in range(second_index + 1, len(branch_sets)):
                third = branch_sets[third_index]
                if (
                    third & (first | second)
                    or not neighbourhoods[first] & third
                    or not neighbourhoods[second] & third
                ):
                    continue
                for fourth in branch_sets[third_index + 1 :]:
                    if (
                        fourth & (first | second | third)
                        or not neighbourhoods[first] & fourth
                        or not neighbourhoods[second] & fourth
                        or not neighbourhoods[third] & fourth
                    ):
                        continue
                    return True
    return False


def independence_number_at_most_three(
    edges: frozenset[tuple[int, int]],
) -> bool:
    for vertices in itertools.combinations(range(ORDER), 4):
        if all(
            tuple(sorted((left, right))) not in edges
            for left, right in itertools.combinations(vertices, 2)
        ):
            return False
    return True


def eligible(edges: frozenset[tuple[int, int]]) -> bool:
    if not independence_number_at_most_three(edges):
        return False
    return all(
        not has_k4_minor(
            edges,
            ALL_VERTICES
            ^ sum(1 << vertex for vertex in deleted),
        )
        for deleted in itertools.combinations(range(ORDER), 2)
    )


def bipartite_after_deleting(
    edges: frozenset[tuple[int, int]], deleted: set[int]
) -> bool:
    remaining = set(range(ORDER)) - deleted
    neighbours = {vertex: set() for vertex in remaining}
    for left, right in edges:
        if left in remaining and right in remaining:
            neighbours[left].add(right)
            neighbours[right].add(left)
    colours: dict[int, int] = {}
    for root in sorted(remaining):
        if root in colours:
            continue
        colours[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            for other in neighbours[vertex]:
                if other not in colours:
                    colours[other] = 1 - colours[vertex]
                    stack.append(other)
                elif colours[other] == colours[vertex]:
                    return False
    return True


def marked_edges(
    edges: frozenset[tuple[int, int]], first: int, second: int
) -> frozenset[tuple[int, int]]:
    if first == FULL or second == FULL:
        return edges
    return edges | {tuple(sorted((first, second)))}


def parse_mark(text: str) -> int:
    if text == "F":
        return FULL
    try:
        mark = int(text)
    except ValueError as error:
        raise AssertionError(f"invalid endpoint mark {text!r}") from error
    if text != str(mark) or not 0 <= mark < ORDER:
        raise AssertionError(f"invalid endpoint mark {text!r}")
    return mark


def validate_oct(
    code: str,
    first: int,
    second: int,
    witness: str,
    edges: frozenset[tuple[int, int]],
) -> None:
    try:
        deleted_mask = int(witness, 16)
    except ValueError as error:
        raise AssertionError(f"{code}: invalid OCT mask {witness!r}") from error
    if (
        witness != f"{deleted_mask:02x}"
        or deleted_mask >= 1 << ORDER
        or deleted_mask.bit_count() > 2
    ):
        raise AssertionError(f"{code}: invalid OCT mask {witness!r}")
    deleted = {
        vertex for vertex in range(ORDER) if deleted_mask >> vertex & 1
    }
    if not bipartite_after_deleting(marked_edges(edges, first, second), deleted):
        raise AssertionError(
            f"{code}: {witness} is not an OCT for roots ({first},{second})"
        )


def validate_triangle(
    code: str,
    first: int,
    second: int,
    witness: str,
    edges: frozenset[tuple[int, int]],
) -> None:
    try:
        triangle_mask = int(witness, 16)
    except ValueError as error:
        raise AssertionError(f"{code}: invalid triangle mask {witness!r}") from error
    if (
        witness != f"{triangle_mask:02x}"
        or triangle_mask >= 1 << ORDER
        or triangle_mask.bit_count() != 3
        or first == FULL
        or second == FULL
        or triangle_mask & ((1 << first) | (1 << second))
    ):
        raise AssertionError(f"{code}: invalid triangle mask {witness!r}")
    triangle = [
        vertex for vertex in range(ORDER) if triangle_mask >> vertex & 1
    ]
    if any(
        tuple(sorted((left, right))) not in edges
        for left, right in itertools.combinations(triangle, 2)
    ):
        raise AssertionError(f"{code}: {witness} does not induce a triangle")

    augmented = marked_edges(edges, first, second)
    for deleted_mask in DELETION_MASKS:
        deleted = {
            vertex
            for vertex in range(ORDER)
            if deleted_mask >> vertex & 1
        }
        if bipartite_after_deleting(augmented, deleted):
            raise AssertionError(
                f"{code}: TRI record has OCT {deleted_mask:02x}"
            )


def check_certificate(certificate: Path) -> None:
    lines = certificate.read_text(encoding="ascii").splitlines()
    records = [line for line in lines if line and not line.startswith("#")]
    payload = ("\n".join(records) + "\n").encode("ascii")
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(
            f"certificate digest {digest} != {EXPECTED_SHA256}"
        )

    graph_edges = {
        code: graph6_edges(code) for code in catalogue_codes()
    }
    eligible_graphs = {
        code
        for code, edges in graph_edges.items()
        if eligible(edges)
    }
    if len(eligible_graphs) != EXPECTED_ELIGIBLE:
        raise AssertionError(
            f"expected {EXPECTED_ELIGIBLE} eligible graphs, "
            f"got {len(eligible_graphs)}"
        )

    expected_keys = {
        (code, first, second)
        for code in eligible_graphs
        for first, second in PROFILES
    }
    seen: set[tuple[str, int, int]] = set()
    counts = {
        "OCT": [0, 0, 0],
        "TRI": [0, 0, 0],
    }
    for line in records:
        fields = line.split("\t")
        if len(fields) != 5:
            raise AssertionError(f"malformed certificate line: {line!r}")
        code, first_text, second_text, kind, witness = fields
        first = parse_mark(first_text)
        second = parse_mark(second_text)
        key = (code, first, second)
        if key in seen or key not in expected_keys:
            raise AssertionError(f"duplicate or unexpected marked pair: {key}")
        seen.add(key)
        edges = graph_edges[code]
        if kind == "OCT":
            validate_oct(code, first, second, witness, edges)
        elif kind == "TRI":
            validate_triangle(code, first, second, witness, edges)
        else:
            raise AssertionError(f"{code}: unknown witness kind {kind!r}")
        miss_count = int(first != FULL) + int(second != FULL)
        counts[kind][miss_count] += 1

    if seen != expected_keys:
        raise AssertionError(
            f"certificate misses {len(expected_keys - seen)} marked pairs"
        )
    expected_counts = {
        "OCT": [185, 2_960, 10_102],
        "TRI": [0, 0, EXPECTED_TRIANGLES],
    }
    if counts != expected_counts:
        raise AssertionError(f"unexpected witness counts: {counts}")

    print(f"graphs {len(graph_edges)}")
    print(f"eligible_graphs {len(eligible_graphs)}")
    print(f"marked_profiles {len(seen)}")
    print(
        f"oct_witnesses {sum(counts['OCT'])} "
        f"by_miss_count={counts['OCT']}"
    )
    print(
        f"triangle_witnesses {sum(counts['TRI'])} "
        f"by_miss_count={counts['TRI']}"
    )
    print(f"records_sha256 {digest}")
    print("PASS")


def main() -> None:
    if not __debug__:
        raise SystemExit("certificate checks require normal Python mode (without -O)")

    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path, nargs="?")
    arguments = parser.parse_args()
    if arguments.certificate is not None:
        check_certificate(arguments.certificate)
        return

    generator = Path(__file__).with_name(
        "hc7_order8_rooted_oct_triangle_certificate.py"
    )
    with tempfile.TemporaryDirectory(prefix="hc7-order8-rooted-oct-") as temporary:
        certificate = Path(temporary) / "certificate.txt"
        subprocess.run(
            [sys.executable, str(generator), "--output", str(certificate)],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        check_certificate(certificate)


if __name__ == "__main__":
    main()
