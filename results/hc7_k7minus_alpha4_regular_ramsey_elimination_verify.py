#!/usr/bin/env python3
"""Verify the order-25 regular Ramsey elimination used in the alpha=4 branch.

The script uses only the Python standard library to enumerate the centre-
incidence vectors and generate CNF.  In full verification mode it asks
CaDiCaL to emit a binary DRAT refutation for each of the 40 symmetry classes
and asks the independent drat-trim checker to verify every refutation.

Generated CNFs and proofs live in a temporary directory and are deleted on
success.  Pass ``--keep-directory`` to retain them for inspection.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")

import argparse
import concurrent.futures
import hashlib
import itertools
import os
import shutil
import subprocess
import tempfile
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path


CENTRES = 4
OUTSIDE = 21
ORDER = CENTRES + OUTSIDE
MASKS = tuple(range(1, 1 << CENTRES))
EXPECTED_VECTOR_COUNT = 505
EXPECTED_ORBIT_COUNT = 40

# Filled from the deterministic generator below.  These constants make an
# accidental encoding change visible before any external solver is invoked.
EXPECTED_ORBIT_SHA256 = "8841a5f22d526efdc5b24c889dc40b6d01ea57b186ecca664435756ccd308f31"
EXPECTED_CNF_CORPUS_SHA256 = "a34b94ffa30e693806a83b32bdbacff036c8c091fa7f03e84835530d1a3bc48a"


def permute_mask(mask: int, permutation: Sequence[int]) -> int:
    result = 0
    for old in range(CENTRES):
        if mask & (1 << old):
            result |= 1 << permutation[old]
    return result


def incidence_vectors() -> tuple[tuple[int, ...], ...]:
    """Return all nonnegative solutions of the four degree equations.

    The recursion uses masks in decreasing order of cardinality.  Caching is
    unnecessary at this fixed order once the elementary feasibility tests are
    imposed, and retaining an explicit recursion keeps the enumeration easy to
    audit.
    """

    order = tuple(sorted(MASKS, key=lambda mask: (-mask.bit_count(), mask)))
    values = [0] * len(order)
    solutions: list[tuple[int, ...]] = []

    def visit(position: int, vertices_left: int, degrees_left: tuple[int, ...]) -> None:
        if position == len(order):
            if vertices_left == 0 and degrees_left == (0, 0, 0, 0):
                by_mask = {mask: values[index] for index, mask in enumerate(order)}
                solutions.append(tuple(by_mask[mask] for mask in MASKS))
            return
        if vertices_left < 0 or any(value < 0 for value in degrees_left):
            return

        remaining_masks = order[position:]
        # Every remaining vertex has a nonempty mask, and no centre can receive
        # more remaining incidences than the number of remaining vertices.
        if sum(degrees_left) < vertices_left:
            return
        if any(value > vertices_left for value in degrees_left):
            return
        for centre, required in enumerate(degrees_left):
            if required and not any(mask & (1 << centre) for mask in remaining_masks):
                return

        mask = order[position]
        cap = vertices_left
        for centre in range(CENTRES):
            if mask & (1 << centre):
                cap = min(cap, degrees_left[centre])
        if mask.bit_count() == 1:
            cap = min(cap, 3)

        for count in range(cap + 1):
            values[position] = count
            next_degrees = tuple(
                degrees_left[centre] - count
                if mask & (1 << centre)
                else degrees_left[centre]
                for centre in range(CENTRES)
            )
            visit(position + 1, vertices_left - count, next_degrees)
        values[position] = 0

    visit(0, OUTSIDE, (8, 8, 8, 8))
    return tuple(sorted(solutions))


def orbit_representatives(
    vectors: Iterable[tuple[int, ...]],
) -> tuple[tuple[int, ...], ...]:
    permutations = tuple(itertools.permutations(range(CENTRES)))
    representatives: set[tuple[int, ...]] = set()
    for vector in vectors:
        counts = {mask: vector[mask - 1] for mask in MASKS}
        orbit = (
            tuple(counts[permute_mask(mask, permutation)] for mask in MASKS)
            for permutation in permutations
        )
        representatives.add(min(orbit))
    return tuple(sorted(representatives))


class Formula:
    """Small deterministic Tseitin-CNF builder."""

    def __init__(self) -> None:
        self.variable_count = 0
        self.clauses: list[tuple[int, ...]] = []
        self._edges: dict[tuple[int, int], int] = {}
        self.true = self.variable()
        self.false = self.variable()
        self.add(self.true)
        self.add(-self.false)

    def variable(self) -> int:
        self.variable_count += 1
        return self.variable_count

    def edge(self, left: int, right: int) -> int:
        assert CENTRES <= left < ORDER
        assert CENTRES <= right < ORDER
        assert left != right
        if left > right:
            left, right = right, left
        pair = (left, right)
        variable = self._edges.get(pair)
        if variable is None:
            variable = self.variable()
            self._edges[pair] = variable
        return variable

    def add(self, *literals: int) -> None:
        self.clauses.append(tuple(literals))

    def and_gate(self, left: int, right: int) -> int:
        output = self.variable()
        self.add(-output, left)
        self.add(-output, right)
        self.add(output, -left, -right)
        return output

    def or_gate(self, left: int, right: int) -> int:
        output = self.variable()
        self.add(-left, output)
        self.add(-right, output)
        self.add(-output, left, right)
        return output

    def exact(self, literals: Sequence[int], value: int) -> None:
        """Encode an exact cardinality using prefix threshold gates."""

        assert 0 <= value <= len(literals)
        previous = [self.true] + [self.false] * (value + 1)
        for literal in literals:
            current = [self.true]
            for threshold in range(1, value + 2):
                take = self.and_gate(literal, previous[threshold - 1])
                current.append(self.or_gate(previous[threshold], take))
            previous = current
        self.add(previous[value])
        self.add(-previous[value + 1])

    def dimacs(self) -> bytes:
        lines = [f"p cnf {self.variable_count} {len(self.clauses)}\n"]
        lines.extend(" ".join(map(str, clause)) + " 0\n" for clause in self.clauses)
        return "".join(lines).encode("ascii")


def outside_masks(representative: Sequence[int]) -> tuple[int, ...]:
    result: list[int] = []
    for mask, count in zip(MASKS, representative, strict=True):
        result.extend([mask] * count)
    assert len(result) == OUTSIDE
    return tuple(result)


def fixed_edge(left: int, right: int, masks_by_vertex: Sequence[int]) -> bool | None:
    """Return a fixed centre incidence, or None for an outside pair."""

    if left >= CENTRES and right >= CENTRES:
        return None
    if left > right:
        left, right = right, left
    if right < CENTRES:
        return False
    return bool(masks_by_vertex[right - CENTRES] & (1 << left))


def build_formula(representative: Sequence[int]) -> Formula:
    masks_by_vertex = outside_masks(representative)
    formula = Formula()
    outside_vertices = tuple(range(CENTRES, ORDER))

    for vertex in outside_vertices:
        incident = tuple(
            formula.edge(vertex, other)
            for other in outside_vertices
            if other != vertex
        )
        residual_degree = 8 - masks_by_vertex[vertex - CENTRES].bit_count()
        formula.exact(incident, residual_degree)

    for vertices in itertools.combinations(range(ORDER), 5):
        pairs = tuple(itertools.combinations(vertices, 2))
        statuses = tuple(
            fixed_edge(left, right, masks_by_vertex) for left, right in pairs
        )

        # At least one pair in the five-set is a nonedge.
        if False not in statuses:
            formula.add(
                *(
                    -formula.edge(left, right)
                    for (left, right), status in zip(pairs, statuses, strict=True)
                    if status is None
                )
            )

        # At least one pair in the five-set is an edge.
        if True not in statuses:
            formula.add(
                *(
                    formula.edge(left, right)
                    for (left, right), status in zip(pairs, statuses, strict=True)
                    if status is None
                )
            )

    assert len(formula._edges) == OUTSIDE * (OUTSIDE - 1) // 2
    return formula


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class Case:
    index: int
    representative: tuple[int, ...]
    variable_count: int
    clause_count: int
    cnf_sha256: str


def generated_cases(
    representatives: Sequence[tuple[int, ...]],
) -> tuple[tuple[Case, ...], str]:
    cases: list[Case] = []
    digests: list[str] = []
    for index, representative in enumerate(representatives):
        formula = build_formula(representative)
        dimacs = formula.dimacs()
        digest = sha256(dimacs)
        digests.append(digest)
        cases.append(
            Case(
                index,
                tuple(representative),
                formula.variable_count,
                len(formula.clauses),
                digest,
            )
        )
    corpus = sha256(("\n".join(digests) + "\n").encode("ascii"))
    return tuple(cases), corpus


def write_case(case: Case, directory: Path) -> tuple[Path, Path]:
    cnf_path = directory / f"case-{case.index:02d}.cnf"
    proof_path = directory / f"case-{case.index:02d}.drat"
    dimacs = build_formula(case.representative).dimacs()
    assert sha256(dimacs) == case.cnf_sha256
    cnf_path.write_bytes(dimacs)
    return cnf_path, proof_path


def run_case(
    case: Case,
    directory: Path,
    solver: str,
    checker: str,
    timeout_seconds: int,
) -> tuple[int, int]:
    cnf_path, proof_path = write_case(case, directory)
    command = [solver, "--quiet", "--unsat", "--binary=true"]
    if timeout_seconds:
        command.extend(("-t", str(timeout_seconds)))
    command.extend((str(cnf_path), str(proof_path)))
    solved = subprocess.run(command, check=False, capture_output=True, text=True)
    if solved.returncode != 20:
        detail = (solved.stdout + solved.stderr).strip()
        raise RuntimeError(
            f"case {case.index:02d}: expected UNSAT exit 20, got "
            f"{solved.returncode}: {detail}"
        )

    checked = subprocess.run(
        (checker, str(cnf_path), str(proof_path), "-i"),
        check=False,
        capture_output=True,
        text=True,
    )
    if checked.returncode != 0 or "s VERIFIED" not in checked.stdout:
        detail = (checked.stdout + checked.stderr).strip()
        raise RuntimeError(f"case {case.index:02d}: DRAT check failed: {detail}")
    return case.index, proof_path.stat().st_size


def validate_generation() -> tuple[tuple[Case, ...], str, str]:
    vectors = incidence_vectors()
    assert len(vectors) == EXPECTED_VECTOR_COUNT
    assert all(sum(vector) == OUTSIDE for vector in vectors)
    assert all(
        sum(vector[mask - 1] for mask in MASKS if mask & (1 << centre)) == 8
        for vector in vectors
        for centre in range(CENTRES)
    )
    assert all(vector[(1 << centre) - 1] <= 3 for vector in vectors for centre in range(CENTRES))

    representatives = orbit_representatives(vectors)
    assert len(representatives) == EXPECTED_ORBIT_COUNT
    orbit_text = "".join(
        ",".join(map(str, representative)) + "\n"
        for representative in representatives
    ).encode("ascii")
    orbit_digest = sha256(orbit_text)
    cases, corpus_digest = generated_cases(representatives)
    return cases, orbit_digest, corpus_digest


def resolve_executable(name: str) -> str:
    path = shutil.which(name)
    if path is None:
        raise SystemExit(f"required executable not found: {name}")
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--enumerate-only", action="store_true")
    parser.add_argument("--solver", default="cadical")
    parser.add_argument("--checker", default="drat-trim")
    parser.add_argument("--jobs", type=int, default=min(4, os.cpu_count() or 1))
    parser.add_argument("--timeout-seconds", type=int, default=0)
    parser.add_argument("--keep-directory", type=Path)
    args = parser.parse_args()
    if args.jobs < 1 or args.timeout_seconds < 0:
        parser.error("jobs must be positive and timeout-seconds must be nonnegative")

    cases, orbit_digest, corpus_digest = validate_generation()
    print(f"incidence_vectors={EXPECTED_VECTOR_COUNT} orbits={EXPECTED_ORBIT_COUNT}")
    print(f"orbit_sha256={orbit_digest}")
    print(f"cnf_corpus_sha256={corpus_digest}")
    print(
        "cnf_variables="
        f"{min(case.variable_count for case in cases)}.."
        f"{max(case.variable_count for case in cases)} "
        "cnf_clauses="
        f"{min(case.clause_count for case in cases)}.."
        f"{max(case.clause_count for case in cases)}"
    )

    if EXPECTED_ORBIT_SHA256 != "TO_BE_FILLED":
        assert orbit_digest == EXPECTED_ORBIT_SHA256
    if EXPECTED_CNF_CORPUS_SHA256 != "TO_BE_FILLED":
        assert corpus_digest == EXPECTED_CNF_CORPUS_SHA256
    if args.enumerate_only:
        return

    solver = resolve_executable(args.solver)
    checker = resolve_executable(args.checker)
    if args.keep_directory is None:
        temporary = tempfile.TemporaryDirectory(prefix="hc7-alpha4-")
        directory = Path(temporary.name)
    else:
        temporary = None
        directory = args.keep_directory
        directory.mkdir(parents=True, exist_ok=True)

    try:
        proof_sizes = [0] * len(cases)
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
            futures = (
                executor.submit(
                    run_case,
                    case,
                    directory,
                    solver,
                    checker,
                    args.timeout_seconds,
                )
                for case in cases
            )
            for future in concurrent.futures.as_completed(tuple(futures)):
                index, proof_size = future.result()
                proof_sizes[index] = proof_size
        assert all(proof_sizes)
        print(
            f"UNSAT_cases={len(cases)}/{len(cases)} "
            f"DRAT_verified={len(cases)}/{len(cases)} "
            f"generated_proof_bytes={sum(proof_sizes)}"
        )
    finally:
        if temporary is not None:
            temporary.cleanup()


if __name__ == "__main__":
    main()
