#!/usr/bin/env python3
"""Generate exact one-nonterminal kernels for nine labelled terminals.

Every terminal-irreducible order-ten kernel has one nonterminal x.  Put
J=K-x.  Wu gives at least four degree-two vertices of J adjacent to x.
Conversely, this generator enumerates every unlabelled two-connected J of
order nine, every superset of its degree-two vertices which can be N_K(x),
and retains exactly the three-connected kernels for which no edge at x is
contractible.  The resulting rooted occurrences are then expanded over all
terminal label permutations, with exact owner quotients deduplicated.
"""

from __future__ import annotations

import collections
import importlib.util
import itertools
from pathlib import Path
import subprocess


if not __debug__:
    raise SystemExit("verification requires assertions; do not run with -O")


ROOT = Path(__file__).resolve().parents[3]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


exact8 = load(
    "eight_terminal_exact_catalogue",
    ROOT / "active" / "hc7_eight_terminal_exact_bundle_catalogue.py",
)

TERMINALS = tuple(range(9))
PAIRS = tuple(itertools.combinations(TERMINALS, 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}


def exact_rooted_occurrences():
    answer = []
    process = subprocess.Popen(
        ["geng", "-Cq", "-d2", "9"], stdout=subprocess.PIPE
    )
    assert process.stdout is not None
    for line in process.stdout:
        remainder = exact8.graph6_adjacency(line)
        charged = tuple(
            vertex for vertex in TERMINALS if remainder[vertex].bit_count() == 2
        )
        if len(charged) < 4:
            continue
        optional = tuple(vertex for vertex in TERMINALS if vertex not in charged)
        for choice in range(1 << len(optional)):
            neighbours = frozenset(charged) | {
                vertex
                for index, vertex in enumerate(optional)
                if choice >> index & 1
            }
            adjacency = list(remainder) + [0]
            for vertex in neighbours:
                adjacency[vertex] |= 1 << 9
                adjacency[9] |= 1 << vertex
            adjacency = tuple(adjacency)
            if not exact8.three_connected(adjacency):
                continue
            if any(
                exact8.contractible(adjacency, 9, vertex)
                for vertex in neighbours
            ):
                continue
            answer.append((remainder, neighbours))
    if process.wait() != 0:
        raise RuntimeError("geng failed")
    assert len(answer) == 1_153
    return tuple(answer)


def terminal_mask(remainder: tuple[int, ...], permutation: tuple[int, ...]) -> int:
    return sum(
        1 << PAIR_INDEX[tuple(sorted((permutation[left], permutation[right])))]
        for left, right in exact8.edges(remainder)
    )


def owner_family(base_mask: int, neighbour_mask: int) -> tuple[int, ...]:
    outcomes = set()
    for owner in TERMINALS:
        if not (neighbour_mask >> owner & 1):
            continue
        quotient = base_mask
        for other in TERMINALS:
            if other != owner and neighbour_mask >> other & 1:
                quotient |= 1 << PAIR_INDEX[tuple(sorted((owner, other)))]
        outcomes.add(quotient)
    return tuple(sorted(outcomes))


def exact_owner_families():
    occurrences = exact_rooted_occurrences()
    families = set()
    templates = set()
    for remainder, neighbours in occurrences:
        for permutation in itertools.permutations(TERMINALS):
            base_mask = terminal_mask(remainder, permutation)
            neighbour_mask = sum(1 << permutation[vertex] for vertex in neighbours)
            template = (base_mask << 9) | neighbour_mask
            if template in templates:
                continue
            templates.add(template)
            families.add(owner_family(base_mask, neighbour_mask))
    assert len(families) <= len(templates)
    return occurrences, tuple(sorted(templates)), tuple(sorted(families))


def main() -> None:
    occurrences = exact_rooted_occurrences()
    print("rooted_occurrences", len(occurrences))
    print(
        "root_degree_profile",
        dict(
            sorted(
                collections.Counter(
                    len(neighbours) for _remainder, neighbours in occurrences
                ).items()
            )
        ),
    )
    print(
        "remainder_edge_profile",
        dict(
            sorted(
                collections.Counter(
                    sum(1 for _ in exact8.edges(item[0])) for item in occurrences
                ).items()
            )
        ),
    )


if __name__ == "__main__":
    main()
