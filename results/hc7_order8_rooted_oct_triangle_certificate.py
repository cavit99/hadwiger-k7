#!/usr/bin/env python3
"""Generate the order-eight rooted OCT/triangle certificates.

The finite statement checked is:

    Let H be an eight-vertex graph with alpha(H) <= 3 such that H-Z has
    no K4 minor for every two-set Z.  Mark two endpoint misses, allowing
    either endpoint to be boundary-full and requiring two actual misses
    to be distinct.  Then the marked parity constraints admit an
    odd-cycle transversal of size at most two, or both misses are actual
    vertices and H minus those vertices contains a triangle.

Nauty's ``geng -q 8`` supplies one representative of every isomorphism
class.  The optional certificate contains one canonical record for every
ordered marked pair (H,r,s).  The companion checker independently rebuilds
the catalogue and validates every record without importing this module.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import shutil
import subprocess
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
TWO_SETS = tuple(
    sum(1 << vertex for vertex in vertices)
    for vertices in itertools.combinations(range(ORDER), 2)
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


def decode_graph6(code: str) -> tuple[int, ...]:
    """Decode a short graph6 word into adjacency bitsets."""

    values = [ord(character) - 63 for character in code]
    if not values or values[0] != ORDER:
        raise ValueError(f"expected an order-{ORDER} graph6 code: {code!r}")
    bits = [
        (value >> shift) & 1
        for value in values[1:]
        for shift in range(5, -1, -1)
    ]
    rows = [0] * ORDER
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                rows[left] |= 1 << right
                rows[right] |= 1 << left
            position += 1
    return tuple(rows)


def graph6_catalogue() -> list[tuple[str, tuple[int, ...]]]:
    """Return nauty's complete canonical catalogue of order-eight graphs."""

    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("missing dependency: install nauty so that `geng` is on PATH")
    result = subprocess.run(
        [executable, "-q", str(ORDER)],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    catalogue = sorted(
        (line, decode_graph6(line))
        for line in result.stdout.splitlines()
        if line and not line.startswith(">")
    )
    if len(catalogue) != EXPECTED_GRAPHS:
        raise RuntimeError(
            f"expected {EXPECTED_GRAPHS} graph6 records, got {len(catalogue)}"
        )
    if len({code for code, _ in catalogue}) != EXPECTED_GRAPHS:
        raise RuntimeError("geng returned duplicate graph6 records")
    return catalogue


def has_k4_minor(
    rows: tuple[int, ...], active: int = ALL_VERTICES
) -> bool:
    """Recognize a K4 minor by exact degree-at-most-two suppression."""

    adjacency = list(rows)
    while active.bit_count() >= 4:
        vertex = next(
            (
                candidate
                for candidate in range(ORDER)
                if active >> candidate & 1
                and (adjacency[candidate] & active).bit_count() <= 2
            ),
            None,
        )
        if vertex is None:
            return True
        neighbours = adjacency[vertex] & active
        if neighbours.bit_count() == 2:
            first_bit = neighbours & -neighbours
            second_bit = neighbours ^ first_bit
            first = first_bit.bit_length() - 1
            second = second_bit.bit_length() - 1
            adjacency[first] |= second_bit
            adjacency[second] |= first_bit
        active ^= 1 << vertex
    return False


def independent(rows: tuple[int, ...], vertices: int) -> bool:
    while vertices:
        bit = vertices & -vertices
        vertices ^= bit
        if rows[bit.bit_length() - 1] & vertices:
            return False
    return True


def eligible(rows: tuple[int, ...]) -> bool:
    if any(
        independent(rows, vertices)
        for vertices in (
            sum(1 << vertex for vertex in choice)
            for choice in itertools.combinations(range(ORDER), 4)
        )
    ):
        return False
    return all(
        not has_k4_minor(rows, ALL_VERTICES ^ deleted)
        for deleted in TWO_SETS
    )


def bipartite_after_deleting(rows: tuple[int, ...], deleted: int) -> bool:
    colours = [-1] * ORDER
    for root in range(ORDER):
        if deleted >> root & 1 or colours[root] >= 0:
            continue
        colours[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            neighbours = rows[vertex] & ~deleted
            while neighbours:
                bit = neighbours & -neighbours
                neighbours ^= bit
                other = bit.bit_length() - 1
                if colours[other] < 0:
                    colours[other] = colours[vertex] ^ 1
                    stack.append(other)
                elif colours[other] == colours[vertex]:
                    return False
    return True


def first_oct(rows: tuple[int, ...]) -> int | None:
    return next(
        (
            deleted
            for deleted in DELETION_MASKS
            if bipartite_after_deleting(rows, deleted)
        ),
        None,
    )


def first_triangle(rows: tuple[int, ...], first: int, second: int) -> int | None:
    available = [
        vertex for vertex in range(ORDER) if vertex not in (first, second)
    ]
    for vertices in itertools.combinations(available, 3):
        if all(
            rows[left] >> right & 1
            for left, right in itertools.combinations(vertices, 2)
        ):
            return sum(1 << vertex for vertex in vertices)
    return None


def marked_rows(
    rows: tuple[int, ...], first: int, second: int
) -> tuple[int, ...]:
    answer = list(rows)
    if first != FULL and second != FULL:
        answer[first] |= 1 << second
        answer[second] |= 1 << first
    return tuple(answer)


def mark_text(mark: int) -> str:
    return "F" if mark == FULL else str(mark)


def main() -> None:
    if not __debug__:
        raise SystemExit("certificate checks require normal Python mode (without -O)")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="path for the generated canonical certificate",
    )
    arguments = parser.parse_args()

    records: list[str] = []
    eligible_graphs = 0
    oct_witnesses = [0, 0, 0]
    triangle_witnesses = [0, 0, 0]
    for code, rows in graph6_catalogue():
        if not eligible(rows):
            continue
        eligible_graphs += 1
        for first, second in PROFILES:
            miss_count = int(first != FULL) + int(second != FULL)
            oct_mask = first_oct(marked_rows(rows, first, second))
            if oct_mask is not None:
                kind = "OCT"
                witness = oct_mask
                oct_witnesses[miss_count] += 1
            else:
                if miss_count != 2:
                    raise AssertionError(
                        "unexpected hard profile: "
                        f"graph6={code} roots=({first},{second})"
                    )
                kind = "TRI"
                witness = first_triangle(rows, first, second)
                if witness is None:
                    raise AssertionError(
                        "counterexample: "
                        f"graph6={code} roots=({first},{second})"
                    )
                triangle_witnesses[miss_count] += 1
            records.append(
                f"{code}\t{mark_text(first)}\t{mark_text(second)}\t"
                f"{kind}\t{witness:02x}"
            )

    payload = ("\n".join(records) + "\n").encode("ascii")
    digest = hashlib.sha256(payload).hexdigest()
    observed = (
        eligible_graphs,
        len(records),
        tuple(oct_witnesses),
        tuple(triangle_witnesses),
        digest,
    )
    expected = (
        EXPECTED_ELIGIBLE,
        EXPECTED_PROFILES,
        (185, 2_960, 10_102),
        (0, 0, EXPECTED_TRIANGLES),
        EXPECTED_SHA256,
    )
    if observed != expected:
        raise AssertionError((observed, expected))

    if arguments.output is not None:
        header = (
            "# hc7 order-eight rooted OCT/triangle certificate v1\n"
            f"# graphs={EXPECTED_GRAPHS} eligible={EXPECTED_ELIGIBLE}\n"
            f"# marked_profiles={EXPECTED_PROFILES} oct={EXPECTED_OCT} "
            f"triangles={EXPECTED_TRIANGLES}\n"
            f"# records_sha256={EXPECTED_SHA256}\n"
        )
        arguments.output.write_bytes(header.encode("ascii") + payload)

    print(f"graphs {EXPECTED_GRAPHS}")
    print(f"eligible_graphs {eligible_graphs}")
    print(f"marked_profiles {len(records)}")
    print(f"oct_witnesses {sum(oct_witnesses)} by_miss_count={oct_witnesses}")
    print(
        f"triangle_witnesses {sum(triangle_witnesses)} "
        f"by_miss_count={triangle_witnesses}"
    )
    print(f"records_sha256 {digest}")
    print("PASS")


if __name__ == "__main__":
    main()
