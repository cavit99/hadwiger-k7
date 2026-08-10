#!/usr/bin/env python3
"""Verify the finite incidence lemma for an order-six equality shore.

The standard-library part of this script enumerates the ten possible
six-vertex core graphs and generates one CNF for each.  In full mode,
CaDiCaL produces a DRAT refutation and drat-trim checks it independently.
Generated formulas and proofs are temporary unless ``--keep-directory`` is
passed.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")

import argparse
import concurrent.futures
import hashlib
import itertools
import shutil
import subprocess
import tempfile
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path


CORE_ORDER = 6
BOUNDARY_ORDER = 7
CORE_VERTICES = tuple(range(CORE_ORDER))
BOUNDARY_VERTICES = tuple(range(BOUNDARY_ORDER))
CORE_PAIRS = tuple(itertools.combinations(CORE_VERTICES, 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(CORE_PAIRS)}

EXPECTED_CORE_COUNT = 10
EXPECTED_CORE_SHA256 = "d9d88730ab2cd9712f1131aca905e15241e06cb790e63f25d64e71344b598c9e"
EXPECTED_CNF_CORPUS_SHA256 = "8540146081d94bc2779d3049e1c5fba807748cb3a6052e8a4b770c6ec854a354"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def edge_bit(left: int, right: int) -> int:
    if left > right:
        left, right = right, left
    return 1 << PAIR_INDEX[left, right]


def complement_edges(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(pair for pair in CORE_PAIRS if mask & edge_bit(*pair))


def permute_mask(mask: int, permutation: Sequence[int]) -> int:
    result = 0
    for left, right in complement_edges(mask):
        result |= edge_bit(permutation[left], permutation[right])
    return result


def canonical_mask(mask: int) -> int:
    return min(
        permute_mask(mask, permutation)
        for permutation in itertools.permutations(CORE_VERTICES)
    )


def core_has_k5(complement_mask: int) -> bool:
    """Return whether the core contains a literal K5."""

    for vertices in itertools.combinations(CORE_VERTICES, 5):
        if all(
            not (complement_mask & edge_bit(*pair))
            for pair in itertools.combinations(vertices, 2)
        ):
            return True
    return False


def core_is_three_colourable(complement_mask: int) -> bool:
    """Test three-colourability of the core by its six-vertex definition."""

    for colours in itertools.product(range(3), repeat=CORE_ORDER):
        if all(
            colours[left] != colours[right] or complement_mask & edge_bit(left, right)
            for left, right in CORE_PAIRS
        ):
            return True
    return False


def core_representatives() -> tuple[int, ...]:
    """Enumerate the relevant cores up to relabelling.

    The mask records the complement of the core.  The density bound gives at
    most four complement edges; literal-K5 exclusion and chromatic number at
    least four are then checked directly.
    """

    representatives: set[int] = set()
    for complement_mask in range(1 << len(CORE_PAIRS)):
        if complement_mask.bit_count() > 4:
            continue
        if core_has_k5(complement_mask):
            continue
        if core_is_three_colourable(complement_mask):
            continue
        representatives.add(canonical_mask(complement_mask))
    return tuple(sorted(representatives))


class Formula:
    """Deterministic CNF builder on the 42 literal incidence variables."""

    def __init__(self) -> None:
        self.variable_count = CORE_ORDER * BOUNDARY_ORDER
        self.clauses: list[tuple[int, ...]] = []

    @staticmethod
    def incidence(core: int, boundary: int) -> int:
        assert core in CORE_VERTICES
        assert boundary in BOUNDARY_VERTICES
        return 1 + core * BOUNDARY_ORDER + boundary

    def add(self, literals: Iterable[int]) -> None:
        clause = tuple(dict.fromkeys(literals))
        if any(-literal in clause for literal in clause):
            return
        self.clauses.append(clause)

    def at_least(self, literals: Sequence[int], required: int) -> None:
        """Encode that at least ``required`` of the literals are true."""

        assert 0 <= required <= len(literals)
        if required == 0:
            return
        for subset in itertools.combinations(literals, len(literals) - required + 1):
            self.add(subset)

    def dimacs(self) -> bytes:
        lines = [f"p cnf {self.variable_count} {len(self.clauses)}\n"]
        lines.extend(" ".join(map(str, clause)) + " 0\n" for clause in self.clauses)
        return "".join(lines).encode("ascii")


def core_neighbourhood(complement_mask: int, vertex_mask: int) -> set[int]:
    result: set[int] = set()
    for outside in CORE_VERTICES:
        if vertex_mask & (1 << outside):
            continue
        if any(
            not (complement_mask & edge_bit(vertex, outside))
            for vertex in CORE_VERTICES
            if vertex_mask & (1 << vertex)
        ):
            result.add(outside)
    return result


def build_formula(complement_mask: int) -> Formula:
    """Build the formula asserting that a counterexample incidence exists."""

    formula = Formula()
    missing_edges = complement_edges(complement_mask)
    missing_degrees = [
        sum(vertex in edge for edge in missing_edges) for vertex in CORE_VERTICES
    ]

    # Minimum degree eight: a core vertex of complement-degree r has at least
    # 3+r neighbours in the seven-vertex boundary.
    for vertex in CORE_VERTICES:
        row = tuple(formula.incidence(vertex, boundary) for boundary in BOUNDARY_VERTICES)
        formula.at_least(row, 3 + missing_degrees[vertex])

    # Relative seven-connectivity.  For nonempty X in the core, its core and
    # boundary neighbourhoods together have order at least seven.
    for vertex_mask in range(1, 1 << CORE_ORDER):
        vertices = tuple(
            vertex for vertex in CORE_VERTICES if vertex_mask & (1 << vertex)
        )
        required = BOUNDARY_ORDER - len(core_neighbourhood(complement_mask, vertex_mask))
        empty_column_count = BOUNDARY_ORDER - required + 1
        for boundary_subset in itertools.combinations(BOUNDARY_VERTICES, empty_column_count):
            formula.add(
                formula.incidence(vertex, boundary)
                for vertex in vertices
                for boundary in boundary_subset
            )

    # A boundary vertex cannot be complete to a core K4, since that would be
    # a literal K5 in the host.
    for vertices in itertools.combinations(CORE_VERTICES, 4):
        if any(
            complement_mask & edge_bit(*pair)
            for pair in itertools.combinations(vertices, 2)
        ):
            continue
        for boundary in BOUNDARY_VERTICES:
            formula.add(-formula.incidence(vertex, boundary) for vertex in vertices)

    # Boundary labels play no role in the finite lemma.  Order their six-bit
    # incidence columns to remove the full 7! symmetry.  Each clause forbids
    # one adjacent inversion.
    for boundary in range(BOUNDARY_ORDER - 1):
        for left_mask in range(1 << CORE_ORDER):
            for right_mask in range(left_mask):
                literals: list[int] = []
                for vertex in CORE_VERTICES:
                    left = formula.incidence(vertex, boundary)
                    right = formula.incidence(vertex, boundary + 1)
                    literals.append(-left if left_mask & (1 << vertex) else left)
                    literals.append(-right if right_mask & (1 << vertex) else right)
                formula.add(literals)

    # Finally assert that every incidence-respecting injection of the six core
    # vertices into the seven boundary vertices leaves at least two core
    # nonedges unrepaired.  For a missing edge uv under injection f, the edge
    # is repaired when f(u) sees v or f(v) sees u.  The distributed clauses
    # below forbid any set of |E(complement)|-1 simultaneous repairs.
    repairs_required = len(missing_edges) - 1
    assert repairs_required >= 1
    for injection in itertools.permutations(BOUNDARY_VERTICES, CORE_ORDER):
        invalid_injection = [
            -formula.incidence(vertex, injection[vertex]) for vertex in CORE_VERTICES
        ]
        repair_pairs = {
            edge: (
                formula.incidence(edge[1], injection[edge[0]]),
                formula.incidence(edge[0], injection[edge[1]]),
            )
            for edge in missing_edges
        }
        for edge_subset in itertools.combinations(missing_edges, repairs_required):
            for choices in itertools.product((0, 1), repeat=repairs_required):
                formula.add(
                    itertools.chain(
                        invalid_injection,
                        (
                            -repair_pairs[edge][choice]
                            for edge, choice in zip(edge_subset, choices, strict=True)
                        ),
                    )
                )

    return formula


@dataclass(frozen=True)
class Case:
    index: int
    complement_mask: int
    complement_edges: tuple[tuple[int, int], ...]
    variable_count: int
    clause_count: int
    cnf_sha256: str


def generated_cases(representatives: Sequence[int]) -> tuple[tuple[Case, ...], str]:
    cases: list[Case] = []
    digests: list[str] = []
    for index, representative in enumerate(representatives):
        formula = build_formula(representative)
        dimacs = formula.dimacs()
        digest = sha256(dimacs)
        digests.append(digest)
        cases.append(
            Case(
                index=index,
                complement_mask=representative,
                complement_edges=complement_edges(representative),
                variable_count=formula.variable_count,
                clause_count=len(formula.clauses),
                cnf_sha256=digest,
            )
        )
    corpus_digest = sha256(("\n".join(digests) + "\n").encode("ascii"))
    return tuple(cases), corpus_digest


def write_case(case: Case, directory: Path) -> tuple[Path, Path]:
    cnf_path = directory / f"case-{case.index:02d}.cnf"
    proof_path = directory / f"case-{case.index:02d}.drat"
    dimacs = build_formula(case.complement_mask).dimacs()
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
    if checked.returncode != 0 or "VERIFIED" not in checked.stdout:
        detail = (checked.stdout + checked.stderr).strip()
        raise RuntimeError(f"case {case.index:02d}: DRAT check failed: {detail}")
    return case.index, proof_path.stat().st_size


def executable(command: str) -> str:
    path = shutil.which(command)
    if path is None:
        raise SystemExit(f"required executable not found: {command}")
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enumerate-only", action="store_true")
    parser.add_argument("--keep-directory", type=Path)
    parser.add_argument("--solver", default="cadical")
    parser.add_argument("--checker", default="drat-trim")
    parser.add_argument("--jobs", type=int, default=4)
    parser.add_argument("--timeout-seconds", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    representatives = core_representatives()
    assert len(representatives) == EXPECTED_CORE_COUNT
    core_digest = sha256(("\n".join(map(str, representatives)) + "\n").encode("ascii"))
    cases, corpus_digest = generated_cases(representatives)

    print(f"core_orbits={len(representatives)}")
    print(f"core_sha256={core_digest}")
    print(f"cnf_corpus_sha256={corpus_digest}")
    print(
        "cnf_variables="
        f"{min(case.variable_count for case in cases)}.."
        f"{max(case.variable_count for case in cases)} "
        "cnf_clauses="
        f"{min(case.clause_count for case in cases)}.."
        f"{max(case.clause_count for case in cases)}"
    )
    for case in cases:
        print(
            f"case={case.index:02d} complement={case.complement_edges} "
            f"clauses={case.clause_count} sha256={case.cnf_sha256}"
        )

    assert core_digest == EXPECTED_CORE_SHA256
    assert corpus_digest == EXPECTED_CNF_CORPUS_SHA256
    if args.enumerate_only:
        return

    solver = executable(args.solver)
    checker = executable(args.checker)
    temporary: tempfile.TemporaryDirectory[str] | None = None
    if args.keep_directory is None:
        temporary = tempfile.TemporaryDirectory(prefix="hc7-order-six-")
        directory = Path(temporary.name)
    else:
        directory = args.keep_directory
        directory.mkdir(parents=True, exist_ok=True)

    try:
        proof_sizes: dict[int, int] = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = (
                pool.submit(
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
        assert set(proof_sizes) == set(range(len(cases)))
        print(
            f"UNSAT_cases={len(proof_sizes)}/{len(cases)} "
            f"DRAT_verified={len(proof_sizes)}/{len(cases)} "
            f"generated_proof_bytes={sum(proof_sizes.values())}"
        )
    finally:
        if temporary is not None:
            temporary.cleanup()


if __name__ == "__main__":
    main()
