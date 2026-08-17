#!/usr/bin/env python3
"""Verify the one-miss connected-exterior reduction at degree eight."""

from __future__ import annotations

from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[3]
BASE = (
    ROOT
    / "active"
    / "experiments"
    / "sevenconnected_codegree2_profiles"
    / "verify.py"
)
SPEC = spec_from_file_location("sevenconnected_profiles", BASE)
assert SPEC and SPEC.loader
TOOLS = module_from_spec(SPEC)
SPEC.loader.exec_module(TOOLS)


CANONICAL_CLOSERS = {
    ("G_{PNk", 7): (0, 1, 2, 5),
    ("Gh_gns", 7): (0, 1, 3, 6),
    ("Gh_gn{", 7): (0, 1, 3, 6),
    ("GMo`M{", 7): (0, 3, 5, 6),
    ("GhEKf[", 7): (1, 2, 4, 5),
    ("GhEKf{", 7): (1, 2, 4, 5),
    ("GGEF~w", 6): (0, 1, 2, 3),
    ("GGEF~w", 7): (0, 1, 2, 3),
    ("GBZENw", 7): (0, 2, 3, 5),
}

RESIDUES = {
    ("GhCKN{", 7),
    ("GhEJE{", 7),
    ("GjSKN[", 7),
    ("GhEMNw", 7),
}

EXPECTED_CLOSING_COUNTS = {
    ("G_{PNk", 7): 5,
    ("Gh_gns", 7): 3,
    ("Gh_gn{", 7): 3,
    ("GMo`M{", 7): 3,
    ("GhEKf[", 7): 3,
    ("GhEKf{", 7): 5,
    ("GGEF~w", 6): 15,
    ("GGEF~w", 7): 15,
    ("GBZENw", 7): 6,
    ("GhCKN{", 7): 0,
    ("GhEJE{", 7): 0,
    ("GjSKN[", 7): 0,
    ("GhEMNw", 7): 0,
}


def completed_graph(
    local: nx.Graph, roots: tuple[int, ...], missed_pair: tuple[int, int]
) -> nx.Graph:
    answer = local.copy()
    answer.add_node(8)
    answer.add_edges_from((8, vertex) for vertex in range(8))
    answer.add_edges_from(
        pair for pair in combinations(roots, 2) if pair != missed_pair
    )
    return answer


def main() -> None:
    TOOLS.TOOLS.calibrate_minor_engine()
    _, _, local_graphs = TOOLS.critical_local_graphs()

    profiles: dict[tuple[str, int], nx.Graph] = {}
    for local in local_graphs:
        code = TOOLS.TOOLS.graph_code(local)
        for missed in range(8):
            if local.degree(missed) < 6:
                continue
            quotient = TOOLS.TOOLS.augmented_graph(local, (missed,))
            model = TOOLS.TOOLS.near_clique_minor_model(
                TOOLS.TOOLS.adjacency_tuple(quotient), 7
            )
            if model is None:
                profiles[(code, missed)] = local

    assert set(profiles) == set(EXPECTED_CLOSING_COUNTS)
    assert set(profiles) == set(CANONICAL_CLOSERS) | RESIDUES

    canonical_certificates: list[str] = []
    closing_counts: dict[tuple[str, int], int] = {}
    for profile, local in sorted(profiles.items()):
        code, missed = profile
        attachment = set(range(8)) - {missed}
        closing_sets: list[tuple[int, ...]] = []
        for roots in combinations(sorted(attachment), 4):
            possible_misses = [
                pair
                for pair in combinations(roots, 2)
                if not local.has_edge(*pair)
            ]
            assert possible_misses
            certificates: list[str] = []
            for missed_pair in possible_misses:
                completed = completed_graph(local, roots, missed_pair)
                model = TOOLS.TOOLS.near_clique_minor_model(
                    TOOLS.TOOLS.adjacency_tuple(completed), 7
                )
                if model is None:
                    break
                certificates.append(
                    f"{code} {missed} {''.join(map(str, roots))} "
                    f"{missed_pair[0]}{missed_pair[1]} "
                    f"{TOOLS.TOOLS.model_text(model)}"
                )
            else:
                closing_sets.append(roots)
                if CANONICAL_CLOSERS.get(profile) == roots:
                    canonical_certificates.extend(certificates)

        closing_counts[profile] = len(closing_sets)
        if profile in CANONICAL_CLOSERS:
            assert CANONICAL_CLOSERS[profile] in closing_sets
        else:
            assert not closing_sets

    assert closing_counts == EXPECTED_CLOSING_COUNTS
    digest = sha256(
        "\n".join(sorted(canonical_certificates)).encode()
    ).hexdigest()
    assert digest == (
        "7f684013b80ac226fddbc73405c7698a9040a01aaf1e58c0d8d9d1b432fa0500"
    )

    print("GREEN connected one-miss exterior reduction")
    print(f"degree_viable_profiles={len(profiles)}")
    print(f"rooted_completion_eliminated={len(CANONICAL_CLOSERS)}")
    print(f"residues={sorted(RESIDUES)}")
    print(f"canonical_completion_digest={digest}")


if __name__ == "__main__":
    main()
