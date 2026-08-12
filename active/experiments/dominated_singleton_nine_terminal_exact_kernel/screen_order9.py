#!/usr/bin/env python3
"""Screen the all-terminal branch of the protected nine-terminal kernel."""

from __future__ import annotations

from functools import lru_cache
import importlib.util
import itertools
from pathlib import Path
import shutil
import subprocess


if not __debug__:
    raise SystemExit("screen requires assertions; do not run with -O")


ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = (
    ROOT / "active" / "experiments" / "dominated_singleton_low_degree_completion" / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("dominated_base", BASE_PATH)
assert SPEC is not None and SPEC.loader is not None
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)

LIVE_CODES = ("FCQ`_", "FCQb_", "FCp`_")


def geng(order: int):
    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("nauty geng is required")
    process = subprocess.Popen(
        [executable, "-cq", "-d3", str(order)], stdout=subprocess.PIPE
    )
    assert process.stdout is not None
    for line in process.stdout:
        yield base.decode_graph6(line.decode().strip())
    assert process.wait() == 0


def connected(graph: tuple[int, ...], removed: tuple[int, ...]) -> bool:
    return len(base.components_after(graph, removed)) <= 1


def three_connected(graph: tuple[int, ...]) -> bool:
    return all(
        connected(graph, removed)
        for size in range(3)
        for removed in itertools.combinations(range(len(graph)), size)
    )


def delete_edge(graph: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    answer = list(graph)
    answer[left] &= ~(1 << right)
    answer[right] &= ~(1 << left)
    return tuple(answer)


def minimal_carriers() -> tuple[tuple[int, ...], ...]:
    answer = []
    for graph in geng(9):
        if not three_connected(graph):
            continue
        if any(
            three_connected(delete_edge(graph, left, right))
            for left, right in itertools.combinations(range(9), 2)
            if base.adjacent(graph, left, right)
        ):
            continue
        answer.append(graph)
    return tuple(answer)


def add_q(graph: tuple[int, ...], roots: tuple[int, ...], q: tuple[int, ...]):
    answer = list(graph)
    for left, right in itertools.combinations(range(7), 2):
        if base.adjacent(q, left, right):
            u, v = roots[left], roots[right]
            answer[u] |= 1 << v
            answer[v] |= 1 << u
    protected = tuple(vertex for vertex in range(9) if vertex not in roots)
    assert len(protected) == 2
    left, right = protected
    answer[left] |= 1 << right
    answer[right] |= 1 << left
    return tuple(answer)


def delete_marked(
    graph: tuple[int, ...], roots: tuple[bool, ...], deleted: int
) -> tuple[tuple[int, ...], tuple[bool, ...]]:
    return (
        base.delete_vertex(graph, deleted),
        roots[:deleted] + roots[deleted + 1 :],
    )


def contract_marked(
    graph: tuple[int, ...], roots: tuple[bool, ...], left: int, right: int
) -> tuple[tuple[int, ...], tuple[bool, ...]]:
    if left > right:
        left, right = right, left
    reduced = base.contract_edge(graph, left, right)
    new_roots = []
    for vertex in range(len(graph)):
        if vertex == right:
            continue
        new_roots.append(
            roots[left] or roots[right] if vertex == left else roots[vertex]
        )
    return reduced, tuple(new_roots)


@lru_cache(maxsize=None)
def rooted_k5minus(graph: tuple[int, ...], roots: tuple[bool, ...]) -> bool:
    nonroot = next((vertex for vertex, root in enumerate(roots) if not root), None)
    if nonroot is None:
        return base.has_dense_minor(graph, 5, 9)
    reduced = delete_marked(graph, roots, nonroot)
    if rooted_k5minus(*reduced):
        return True
    for neighbour in range(len(graph)):
        if base.adjacent(graph, nonroot, neighbour):
            if rooted_k5minus(*contract_marked(graph, roots, nonroot, neighbour)):
                return True
    return False


def automorphisms(q: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        image
        for image in itertools.permutations(range(7))
        if all(
            base.adjacent(q, left, right)
            == base.adjacent(q, image[left], image[right])
            for left, right in itertools.combinations(range(7), 2)
        )
    )


def root_placements(q: tuple[int, ...]):
    """One representative per Q-automorphism; protected roots are unordered."""

    group = automorphisms(q)
    seen = set()
    for protected in itertools.combinations(range(9), 2):
        available = tuple(vertex for vertex in range(9) if vertex not in protected)
        for roots in itertools.permutations(available):
            orbit = tuple(sorted(tuple(roots[i] for i in image) for image in group))
            canonical = orbit[0]
            if canonical in seen:
                continue
            seen.add(canonical)
            yield canonical


def main() -> None:
    carriers = minimal_carriers()
    print("order9_unlabelled_minimal_carriers", len(carriers), flush=True)
    total = 0
    failures = []
    for code in LIVE_CODES:
        q = base.decode_graph6(code)
        placements = tuple(root_placements(q))
        print(code, "placements_per_carrier", len(placements), flush=True)
        code_failures = 0
        for carrier_index, carrier in enumerate(carriers):
            for roots in placements:
                total += 1
                graph = add_q(carrier, roots, q)
                marked = tuple(vertex in roots for vertex in range(9))
                if not rooted_k5minus(graph, marked):
                    failures.append((code, carrier_index, roots))
                    code_failures += 1
        print(code, f"failures={code_failures}", flush=True)
        if code_failures:
            print(code, "first_failure", next(f for f in failures if f[0] == code))
    print("order9_protected_kernel", f"tested={total}", f"failures={len(failures)}")


if __name__ == "__main__":
    main()
