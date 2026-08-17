#!/usr/bin/env python3
"""Verify the finite full-exterior profiles at a degree-eight centre.

The local graph J has eight vertices, minimum degree at least three, no
K_6^- minor, no K_4 subgraph and independence number three.  The first
test adds a centre complete to J and classifies the target-free quotients.
The second tests every four-root K_4^- completion of the survivors.

Minor testing and order-eight catalogue generation are imported from the
existing degree-eight profile verifier.  NetworkX 3.6.1 is pinned by the
repository lockfile.
"""

from __future__ import annotations

from collections import Counter
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
PROFILES = module_from_spec(SPEC)
SPEC.loader.exec_module(PROFILES)
TOOLS = PROFILES.TOOLS


ROOTED_COMPLETION_RESIDUES = {
    "GhCKN{",
    "GhEJC{",
    "GhEJE{",
    "GjSKLK",
    "GjSKNK",
    "GjSKL[",
    "GjSKN[",
    "GhdM@k",
    "GxaGis",
    "Gpq_is",
    "GhEM`W",
    "GhEMdW",
    "GhEMbW",
    "GhEM`w",
    "GhEMdw",
    "GlO[PK",
    "GMs`KK",
    "GMs`Kk",
    "GhEMLo",
    "GhEMNo",
    "GhEMJw",
    "GhEMNw",
    "GlgGiK",
    "GlgGik",
    "GhMIMc",
    "GhEK~_",
    "GhEKzW",
    "GhEK~c",
    "GhEJ]o",
}


def completed_graph(
    local: nx.Graph, roots: tuple[int, ...], missed_pair: tuple[int, int]
) -> nx.Graph:
    """Add the centre and make ``roots`` a clique minus ``missed_pair``."""

    answer = local.copy()
    answer.add_node(8)
    answer.add_edges_from((8, vertex) for vertex in range(8))
    answer.add_edges_from(
        pair for pair in combinations(roots, 2) if pair != missed_pair
    )
    return answer


def main() -> None:
    TOOLS.calibrate_minor_engine()
    raw_count, representative_count, local_graphs = PROFILES.critical_local_graphs()
    assert raw_count == 27_529
    assert representative_count == 2_590
    assert len(local_graphs) == 542

    survivors: dict[str, nx.Graph] = {}
    positive_certificates: list[str] = []
    for local in local_graphs:
        code = TOOLS.graph_code(local)
        quotient = TOOLS.augmented_graph(local, ())
        model = TOOLS.near_clique_minor_model(TOOLS.adjacency_tuple(quotient), 7)
        if model is None:
            survivors[code] = local
        else:
            positive_certificates.append(f"{code} {TOOLS.model_text(model)}")

    assert len(positive_certificates) == 486
    assert len(survivors) == 56
    cubic_distribution = Counter(
        sum(local.degree(vertex) == 3 for vertex in range(8))
        for local in survivors.values()
    )
    assert cubic_distribution == Counter({4: 8, 5: 13, 6: 25, 7: 6, 8: 4})

    positive_digest = sha256(
        "\n".join(sorted(positive_certificates)).encode()
    ).hexdigest()
    survivor_digest = sha256(
        "\n".join(
            f"{code} "
            f"{sum(local.degree(vertex) == 3 for vertex in range(8))} "
            f"{tuple(sorted(dict(local.degree()).values()))}"
            for code, local in sorted(survivors.items())
        ).encode()
    ).hexdigest()
    assert positive_digest == (
        "e2e65a34a35d8467054ab5c7b9db2df3bc2f4a2bb4345be1f900cb98d87fb500"
    )
    assert survivor_digest == (
        "a1bf6e4c242e984c46d89ce5a0f642c1ed2ae0811cb6aa0c7938a77f5ffa6bd0"
    )

    closing_distribution: Counter[int] = Counter()
    residues: set[str] = set()
    canonical_certificates: list[str] = []
    for code, local in sorted(survivors.items()):
        closing_sets: list[tuple[int, ...]] = []
        first_certificates: list[str] | None = None
        for roots in combinations(range(8), 4):
            possible_misses = [
                pair
                for pair in combinations(roots, 2)
                if not local.has_edge(*pair)
            ]
            assert possible_misses
            certificates: list[str] = []
            for missed_pair in possible_misses:
                completed = completed_graph(local, roots, missed_pair)
                model = TOOLS.near_clique_minor_model(
                    TOOLS.adjacency_tuple(completed), 7
                )
                if model is None:
                    break
                certificates.append(
                    f"{code} {''.join(map(str, roots))} "
                    f"{missed_pair[0]}{missed_pair[1]} {TOOLS.model_text(model)}"
                )
            else:
                closing_sets.append(roots)
                if first_certificates is None:
                    first_certificates = certificates

        closing_distribution[len(closing_sets)] += 1
        if not closing_sets:
            residues.add(code)
        else:
            assert first_certificates is not None
            canonical_certificates.extend(first_certificates)

    assert closing_distribution == Counter(
        {0: 29, 1: 8, 2: 4, 3: 7, 4: 3, 5: 3, 6: 1, 15: 1}
    )
    assert residues == ROOTED_COMPLETION_RESIDUES

    completion_digest = sha256(
        "\n".join(sorted(canonical_certificates)).encode()
    ).hexdigest()
    assert completion_digest == (
        "e6efa5015a79c25f2a20757325b70ce86a52575ece804ded026cf706317269cc"
    )
    print("GREEN full-exterior degree-eight profile classification")
    print(
        f"minimum_degree_three_extensions={raw_count} "
        f"isomorphism_classes={representative_count} critical_local={len(local_graphs)}"
    )
    print(
        f"full_profiles={len(local_graphs)} positive={len(positive_certificates)} "
        f"target_free={len(survivors)}"
    )
    print(f"cubic_vertex_distribution={sorted(cubic_distribution.items())}")
    print(f"positive_certificate_digest={positive_digest}")
    print(f"target_free_profile_digest={survivor_digest}")
    print(f"rooted_completion_distribution={sorted(closing_distribution.items())}")
    print(f"rooted_completion_residues={sorted(residues)}")
    print(f"canonical_completion_digest={completion_digest}")


if __name__ == "__main__":
    main()
