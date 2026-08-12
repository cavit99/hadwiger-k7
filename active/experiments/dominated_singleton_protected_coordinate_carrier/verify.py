#!/usr/bin/env python3
"""Screen the protected-coordinate eight-terminal carrier composition."""

from __future__ import annotations

from functools import lru_cache
import importlib.util
import itertools
from pathlib import Path


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


ROOT = Path(__file__).resolve().parents[3]
BASE_PATH = (
    ROOT / "active" / "experiments" / "dominated_singleton_low_degree_completion" / "verify.py"
)
CARRIER_PATH = ROOT / "active" / "hc7_eight_terminal_rooted_carrier_verify.py"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base = load("dominated_low_degree_base", BASE_PATH)
carrier = load("eight_terminal_carriers", CARRIER_PATH)

LIVE_CODES = ("FCQ`_", "FCQb_", "FCp`_")
Q = tuple(range(7))
W = 7
X = 8


def edge_set(graph: tuple[int, ...]) -> set[tuple[int, int]]:
    return {
        (left, right)
        for left, right in itertools.combinations(range(len(graph)), 2)
        if base.adjacent(graph, left, right)
    }


def graph_from_edges(order: int, edges: set[tuple[int, int]]) -> tuple[int, ...]:
    answer = [0] * order
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


def delete_with_roots(
    graph: tuple[int, ...], roots: tuple[bool, ...], deleted: int
) -> tuple[tuple[int, ...], tuple[bool, ...]]:
    keep = [vertex for vertex in range(len(graph)) if vertex != deleted]
    return base.delete_vertex(graph, deleted), tuple(roots[vertex] for vertex in keep)


def contract_with_roots(
    graph: tuple[int, ...], roots: tuple[bool, ...], left: int, right: int
) -> tuple[tuple[int, ...], tuple[bool, ...]]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(graph)) if vertex != right]
    new_roots = []
    for vertex in keep:
        if vertex == left:
            new_roots.append(roots[left] or roots[right])
        else:
            new_roots.append(roots[vertex])
    return base.contract_edge(graph, left, right), tuple(new_roots)


@lru_cache(maxsize=None)
def rooted_k5minus(graph: tuple[int, ...], roots: tuple[bool, ...]) -> bool:
    """Return whether a K5-minus model exists with every bag meeting Q."""

    rootless = next((i for i, marked in enumerate(roots) if not marked), None)
    if rootless is None:
        return base.has_dense_minor(graph, 5, 9)

    reduced, reduced_roots = delete_with_roots(graph, roots, rootless)
    if rooted_k5minus(reduced, reduced_roots):
        return True
    for neighbour in range(len(graph)):
        if base.adjacent(graph, rootless, neighbour):
            reduced, reduced_roots = contract_with_roots(
                graph, roots, rootless, neighbour
            )
            if rooted_k5minus(reduced, reduced_roots):
                return True
    return False


def carrier_edges(mask: int) -> set[tuple[int, int]]:
    return {
        pair
        for index, pair in enumerate(itertools.combinations(range(8), 2))
        if mask >> index & 1
    }


def composition(code: str, omitted: int, mask: int) -> tuple[int, ...]:
    q_graph = base.decode_graph6(code)
    edges = edge_set(q_graph)
    retained = [vertex for vertex in Q if vertex != omitted]
    image = {index: retained[index] for index in range(6)}
    image[6] = W
    image[7] = X
    for left, right in carrier_edges(mask):
        edges.add(tuple(sorted((image[left], image[right]))))
    edges.add((W, X))
    return graph_from_edges(9, edges)


def main() -> None:
    families = {
        "C8": carrier.CYCLES,
        "K3,5": carrier.K35,
        "F8": carrier.F8,
    }
    total = 0
    failures: list[tuple[str, int, str, int]] = []
    roots = (True,) * 7 + (False, False)
    for code in LIVE_CODES:
        for omitted in Q:
            for kind, masks in families.items():
                bad = []
                for mask in masks:
                    total += 1
                    graph = composition(code, omitted, mask)
                    if not rooted_k5minus(graph, roots):
                        bad.append(mask)
                        failures.append((code, omitted, kind, mask))
                print(code, f"omitted={omitted}", kind, f"failures={len(bad)}")
    print("protected_coordinate_carriers", f"tested={total}", f"failures={len(failures)}")
    if failures:
        print("first_failure", failures[0])


if __name__ == "__main__":
    main()
