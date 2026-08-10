#!/usr/bin/env python3
"""Verify the finite edge-contraction allocation theorem at shore order seven.

NetworkX 3.6.1 supplies its complete atlas of unlabelled graphs through
order seven.  Z3 4.16.0 performs an exact lazy finite search over the 49
possible core-boundary incidences.  Every SAT incidence is checked by an
explicit exhaustive scan of all core-edge contractions and all 7P6 boundary
injections.  A found allocation is blocked symbolically; UNSAT therefore
proves that every structural incidence has a terminal allocation.  The
pinned result digest records only the invariant core/status corpus because
Z3 may enumerate intermediate models in a different order on a cold run.
"""

from __future__ import annotations

if not __debug__:
    raise SystemExit("verification requires assertions; do not run Python with -O")

import argparse
import concurrent.futures
import hashlib
import itertools
import time
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

try:
    import networkx as nx
except ImportError as error:  # pragma: no cover - environment diagnostic
    raise SystemExit("NetworkX 3.6.1 is required") from error

try:
    import z3
except ImportError as error:  # pragma: no cover - environment diagnostic
    raise SystemExit("full verification requires the optional z3-solver package") from error


CORE_ORDER = 7
BOUNDARY_ORDER = 7
CORE_VERTICES = tuple(range(CORE_ORDER))
BOUNDARY_VERTICES = tuple(range(BOUNDARY_ORDER))
CORE_PAIRS = tuple(itertools.combinations(CORE_VERTICES, 2))
INJECTIONS = tuple(itertools.permutations(BOUNDARY_VERTICES, 6))

EXPECTED_NETWORKX_VERSION = "3.6.1"
EXPECTED_Z3_VERSION = "4.16.0"
EXPECTED_CORE_COUNT = 149
EXPECTED_CORE_SHA256 = "39752dbad6b984399f40a66f0b8240aab5c9a1795cd376b4bf12284cdbe20748"
EXPECTED_RESULT_SHA256 = "aaf1904440324ea01e3eb9a9e862da1b3664f9f8b7b7d5bfa578a3c103c3caca"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def graph6_code(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).strip().decode("ascii")


def has_k5(graph: nx.Graph) -> bool:
    return any(
        all(graph.has_edge(left, right) for left, right in itertools.combinations(vertices, 2))
        for vertices in itertools.combinations(CORE_VERTICES, 5)
    )


def three_colourable(graph: nx.Graph) -> bool:
    return any(
        all(colours[left] != colours[right] for left, right in graph.edges())
        for colours in itertools.product(range(3), repeat=CORE_ORDER)
    )


def admissible_core_codes() -> tuple[str, ...]:
    """Return every relevant seven-vertex core in canonical atlas form."""

    codes = {
        graph6_code(graph)
        for graph in nx.graph_atlas_g()
        if len(graph) == CORE_ORDER
        and nx.is_connected(graph)
        and graph.number_of_edges() >= 13
        and not has_k5(graph)
        and not three_colourable(graph)
    }
    return tuple(sorted(codes))


def decode(code: str) -> nx.Graph:
    graph = nx.from_graph6_bytes(code.encode("ascii"))
    assert tuple(graph) == CORE_VERTICES
    return graph


def core_bags(graph: nx.Graph, edge: tuple[int, int]) -> tuple[tuple[int, ...], ...]:
    left, right = edge
    assert graph.has_edge(left, right)
    return ((left, right),) + tuple(
        (vertex,) for vertex in CORE_VERTICES if vertex not in edge
    )


def quotient_nonedges(
    graph: nx.Graph, bags: Sequence[Sequence[int]]
) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in itertools.combinations(range(6), 2)
        if not any(
            graph.has_edge(u, v) for u in bags[left] for v in bags[right]
        )
    )


def structural_solver(
    graph: nx.Graph,
) -> tuple[z3.Solver, tuple[tuple[z3.BoolRef, ...], ...]]:
    """Encode all incidence hypotheses for one fixed core."""

    incidence = tuple(
        tuple(z3.Bool(f"a_{vertex}_{boundary}") for boundary in BOUNDARY_VERTICES)
        for vertex in CORE_VERTICES
    )
    solver = z3.Solver()

    # Minimum degree eight inside the closed shore.
    for vertex in CORE_VERTICES:
        required = 8 - graph.degree(vertex)
        solver.add(z3.PbGe([(incidence[vertex][s], 1) for s in BOUNDARY_VERTICES], required))

    # The five-root DLY bound at c=7: e(C)+e(C,S)<=43.
    solver.add(
        z3.PbLe(
            [(incidence[v][s], 1) for v in CORE_VERTICES for s in BOUNDARY_VERTICES],
            43 - graph.number_of_edges(),
        )
    )

    # Relative seven-connectivity for every nonempty subset of the core.
    for mask in range(1, 1 << CORE_ORDER):
        subset = tuple(vertex for vertex in CORE_VERTICES if mask & (1 << vertex))
        core_neighbours = {
            outside
            for outside in CORE_VERTICES
            if not mask & (1 << outside)
            and any(graph.has_edge(vertex, outside) for vertex in subset)
        }
        solver.add(
            z3.PbGe(
                [
                    (z3.Or(*(incidence[vertex][s] for vertex in subset)), 1)
                    for s in BOUNDARY_VERTICES
                ],
                BOUNDARY_ORDER - len(core_neighbours),
            )
        )

    # Literal-K5 exclusion at a core K4 plus one boundary vertex.
    for clique in itertools.combinations(CORE_VERTICES, 4):
        if all(graph.has_edge(*edge) for edge in itertools.combinations(clique, 2)):
            for boundary in BOUNDARY_VERTICES:
                solver.add(z3.Not(z3.And(*(incidence[v][boundary] for v in clique))))

    # The finite statement is invariant under boundary relabelling.
    column_codes = tuple(
        z3.Sum(*(z3.If(incidence[v][s], 1 << v, 0) for v in CORE_VERTICES))
        for s in BOUNDARY_VERTICES
    )
    for boundary in range(BOUNDARY_ORDER - 1):
        solver.add(column_codes[boundary] <= column_codes[boundary + 1])

    return solver, incidence


def model_sets(
    model: z3.ModelRef, incidence: Sequence[Sequence[z3.BoolRef]]
) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(
            boundary
            for boundary in BOUNDARY_VERTICES
            if z3.is_true(model.eval(incidence[vertex][boundary], model_completion=True))
        )
        for vertex in CORE_VERTICES
    )


@dataclass(frozen=True)
class Allocation:
    edge: tuple[int, int]
    image: tuple[int, ...]

    def record(self) -> str:
        return f"{self.edge[0]}-{self.edge[1]}:" + "".join(map(str, self.image))


def find_allocation(
    graph: nx.Graph, neighbourhoods: Sequence[frozenset[int]]
) -> Allocation | None:
    """Exhaustively find the first terminal edge-contraction allocation."""

    for edge in sorted(graph.edges()):
        bags = core_bags(graph, edge)
        nonedges = quotient_nonedges(graph, bags)
        for image in INJECTIONS:
            if any(
                not any(image[index] in neighbourhoods[v] for v in bag)
                for index, bag in enumerate(bags)
            ):
                continue
            repaired = sum(
                any(image[left] in neighbourhoods[v] for v in bags[right])
                or any(image[right] in neighbourhoods[u] for u in bags[left])
                for left, right in nonedges
            )
            if repaired >= len(nonedges) - 1:
                return Allocation(edge, image)
    return None


def block_allocation(
    solver: z3.Solver,
    incidence: Sequence[Sequence[z3.BoolRef]],
    graph: nx.Graph,
    allocation: Allocation,
) -> None:
    """Add the exact symbolic assertion that this allocation is not terminal."""

    bags = core_bags(graph, allocation.edge)
    nonedges = quotient_nonedges(graph, bags)
    valid = z3.And(
        *(
            z3.Or(*(incidence[v][allocation.image[index]] for v in bag))
            for index, bag in enumerate(bags)
        )
    )
    repaired = tuple(
        z3.Or(
            *(incidence[v][allocation.image[left]] for v in bags[right]),
            *(incidence[u][allocation.image[right]] for u in bags[left]),
        )
        for left, right in nonedges
    )
    if len(nonedges) <= 1:
        solver.add(z3.Not(valid))
    else:
        solver.add(
            z3.Implies(
                valid,
                z3.PbLe([(value, 1) for value in repaired], len(nonedges) - 2),
            )
        )


@dataclass(frozen=True)
class CaseResult:
    code: str
    edges: int
    rounds: int
    allocation_sha256: str
    elapsed_seconds: float

    def digest_record(self) -> str:
        return f"{self.code} {self.edges} UNSAT"


def run_case(code: str, timeout_milliseconds: int) -> CaseResult:
    graph = decode(code)
    solver, incidence = structural_solver(graph)
    if timeout_milliseconds:
        solver.set(timeout=timeout_milliseconds)
    allocations: list[str] = []
    start = time.monotonic()
    while True:
        verdict = solver.check()
        if verdict == z3.unsat:
            digest = sha256(("\n".join(allocations) + "\n").encode("ascii"))
            return CaseResult(
                code=code,
                edges=graph.number_of_edges(),
                rounds=len(allocations),
                allocation_sha256=digest,
                elapsed_seconds=time.monotonic() - start,
            )
        if verdict == z3.unknown:
            raise RuntimeError(f"{code}: Z3 returned unknown: {solver.reason_unknown()}")
        neighbourhoods = model_sets(solver.model(), incidence)
        allocation = find_allocation(graph, neighbourhoods)
        if allocation is None:
            raise RuntimeError(
                f"{code}: structural counterexample: "
                + repr(tuple(tuple(sorted(row)) for row in neighbourhoods))
            )
        allocations.append(allocation.record())
        block_allocation(solver, incidence, graph, allocation)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enumerate-only", action="store_true")
    parser.add_argument("--jobs", type=int, default=1)
    parser.add_argument("--timeout-milliseconds", type=int, default=0)
    parser.add_argument("--case", action="append", default=[])
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if nx.__version__ != EXPECTED_NETWORKX_VERSION:
        raise SystemExit(
            f"expected NetworkX {EXPECTED_NETWORKX_VERSION}, found {nx.__version__}"
        )
    if z3.get_version_string() != EXPECTED_Z3_VERSION:
        raise SystemExit(
            f"expected Z3 {EXPECTED_Z3_VERSION}, found {z3.get_version_string()}"
        )

    codes = admissible_core_codes()
    assert len(codes) == EXPECTED_CORE_COUNT
    core_digest = sha256(("\n".join(codes) + "\n").encode("ascii"))
    print(f"core_orbits={len(codes)}")
    print(f"core_sha256={core_digest}")
    if EXPECTED_CORE_SHA256 != "TO_BE_FILLED":
        assert core_digest == EXPECTED_CORE_SHA256
    if args.enumerate_only:
        return

    selected = tuple(args.case) if args.case else codes
    if any(code not in codes for code in selected):
        raise SystemExit("--case must name one of the enumerated graph6 cores")
    start = time.monotonic()
    results: list[CaseResult] = []
    if args.jobs == 1:
        for code in selected:
            results.append(run_case(code, args.timeout_milliseconds))
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.jobs) as pool:
            futures = {
                pool.submit(run_case, code, args.timeout_milliseconds): code
                for code in selected
            }
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
    results.sort(key=lambda result: result.code)
    for result in results:
        print(
            f"case={result.code} edges={result.edges} rounds={result.rounds} "
            f"allocation_sha256={result.allocation_sha256} "
            f"seconds={result.elapsed_seconds:.3f}"
        )
    result_digest = sha256(
        ("\n".join(result.digest_record() for result in results) + "\n").encode("ascii")
    )
    print(f"UNSAT_cases={len(results)}/{len(selected)}")
    print(f"result_sha256={result_digest}")
    print(f"elapsed_seconds={time.monotonic() - start:.3f}")
    if not args.case:
        assert result_digest == EXPECTED_RESULT_SHA256


if __name__ == "__main__":
    main()
