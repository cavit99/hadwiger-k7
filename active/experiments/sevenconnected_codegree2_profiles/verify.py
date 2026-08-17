#!/usr/bin/env python3
"""Verify the degree-eight full/one-miss quotient classification.

The local graph J has eight vertices, minimum degree at least three, no
K_6^- minor, no K_4 subgraph and independence number three.  We add a
centre complete to J and either one or two nonadjacent exterior vertices,
each of which is complete to J or misses one vertex.

Minor testing and order-eight catalogue generation are imported from the
audited six-connected low-codegree verifier.  NetworkX 3.6.1 is pinned by
the repository lockfile.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, combinations_with_replacement
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[3]
BASE_VERIFY = (
    ROOT / "results" / "hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py"
)
SPEC = spec_from_file_location("low_codegree_verify", BASE_VERIFY)
assert SPEC and SPEC.loader
TOOLS = module_from_spec(SPEC)
SPEC.loader.exec_module(TOOLS)


def clique_number(graph: nx.Graph) -> int:
    return max(map(len, nx.find_cliques(graph)))


def critical_local_graphs() -> tuple[int, int, list[nx.Graph]]:
    bases = [graph for graph in nx.graph_atlas_g() if len(graph) == 7]
    assert len(bases) == 1_044
    raw = [
        graph
        for base in bases
        for graph in TOOLS.extensions_of_atlas_graph(base)
        if min(dict(graph.degree()).values()) >= 3
    ]
    representatives = TOOLS.isomorphism_representatives(raw)
    local = [
        graph
        for graph in representatives
        if TOOLS.near_clique_minor_model(TOOLS.adjacency_tuple(graph), 6) is None
        and clique_number(graph) <= 3
        and clique_number(nx.complement(graph)) == 3
    ]
    return len(raw), len(representatives), local


def two_component_quotient(
    graph: nx.Graph, first_miss: int | None, second_miss: int | None
) -> nx.Graph:
    answer = graph.copy()
    answer.add_nodes_from((8, 9, 10))
    answer.add_edges_from((8, vertex) for vertex in range(8))
    answer.add_edges_from(
        (9, vertex) for vertex in range(8) if vertex != first_miss
    )
    answer.add_edges_from(
        (10, vertex) for vertex in range(8) if vertex != second_miss
    )
    return answer


def one_miss_text(missed: int | None) -> str:
    return "-" if missed is None else str(missed)


ROOTED_COMPLETION_MODELS = {
    (2, 3): ((1, 3), (4,), (2, 5), (6,), (0, 7), (8,), (9,)),
    (2, 4): ((2, 3), (4,), (5,), (6,), (0, 7), (1, 8), (9,)),
    (3, 6): ((2,), (4,), (5,), (6,), (0, 3, 7), (1, 8), (9,)),
    (4, 6): ((2,), (3,), (5,), (6,), (0, 4, 7), (8,), (1, 9)),
}


def verify_exceptional_rooted_completion() -> str:
    """Check the four direct completions used after the finite census."""

    local = nx.from_graph6_bytes(b"GMs`KK")
    base = local.copy()
    base.add_nodes_from((8, 9))
    base.add_edges_from((8, vertex) for vertex in range(8))
    base.add_edges_from((9, vertex) for vertex in range(8) if vertex != 3)

    roots = (2, 3, 4, 6)
    certificates: list[str] = []
    for missed, bags in ROOTED_COMPLETION_MODELS.items():
        quotient = base.copy()
        quotient.add_edges_from(
            pair
            for pair in combinations(roots, 2)
            if pair != missed
        )

        assert sorted(vertex for bag in bags for vertex in bag) == list(range(10))
        assert all(nx.is_connected(quotient.subgraph(bag)) for bag in bags)
        absent = [
            (first, second)
            for first in range(7)
            for second in range(first + 1, 7)
            if not any(
                quotient.has_edge(left, right)
                for left in bags[first]
                for right in bags[second]
            )
        ]
        assert len(absent) <= 1
        certificates.append(
            f"{missed[0]}{missed[1]} "
            + "/".join(".".join(map(str, bag)) for bag in bags)
            + f" absent={absent}"
        )

    digest = sha256("\n".join(certificates).encode()).hexdigest()
    assert digest == "f36610df787fe55c2aa64c339e1c18f2cb485c723747d05259a728eb01218414"
    return digest


def main() -> None:
    TOOLS.calibrate_minor_engine()
    raw_count, representative_count, local = critical_local_graphs()
    assert raw_count == 27_529
    assert representative_count == 2_590
    assert len(local) == 542

    one_negative: list[tuple[str, int | None, tuple[int, ...]]] = []
    one_certificates: list[str] = []
    for graph in local:
        code = TOOLS.graph_code(graph)
        degrees = tuple(graph.degree(vertex) for vertex in range(8))
        for missed in (None, *range(8)):
            missed_tuple = () if missed is None else (missed,)
            quotient = TOOLS.augmented_graph(graph, missed_tuple)
            model = TOOLS.near_clique_minor_model(
                TOOLS.adjacency_tuple(quotient), 7
            )
            if model is None:
                one_negative.append((code, missed, degrees))
            else:
                one_certificates.append(
                    f"{code} {one_miss_text(missed)} {TOOLS.model_text(model)}"
                )

    negative_graphs = {code for code, _, _ in one_negative}
    negative_missed_degree = Counter(
        -1 if missed is None else degrees[missed]
        for _, missed, degrees in one_negative
    )
    graph_multiplicity = Counter(
        Counter(code for code, _, _ in one_negative).values()
    )
    connectivity_profile = Counter(
        nx.node_connectivity(graph)
        for graph in local
        if TOOLS.graph_code(graph) in negative_graphs
    )
    assert len(one_certificates) == 4_215
    assert len(one_negative) == 663
    assert len(negative_graphs) == 155
    assert negative_missed_degree == Counter(
        {-1: 56, 3: 433, 4: 134, 5: 27, 6: 10, 7: 3}
    )
    assert graph_multiplicity == Counter(
        {1: 51, 2: 37, 3: 10, 4: 1, 9: 56}
    )
    assert connectivity_profile == Counter({2: 38, 3: 117})

    attachments = (None, *range(8))
    two_negative: list[tuple[str, int | None, int | None]] = []
    two_certificates: list[str] = []
    for graph in local:
        code = TOOLS.graph_code(graph)
        for first, second in combinations_with_replacement(attachments, 2):
            quotient = two_component_quotient(graph, first, second)
            model = TOOLS.near_clique_minor_model(
                TOOLS.adjacency_tuple(quotient), 7
            )
            if model is None:
                two_negative.append((code, first, second))
            else:
                two_certificates.append(
                    f"{code} {first} {second} "
                    f"{TOOLS.model_text(model)}"
                )

    assert len(two_certificates) == 24_386
    assert set(two_negative) == {
        ("GMs`KK", 3, 5),
        ("GMs`KK", 3, 6),
        ("GMs`KK", 4, 5),
        ("GMs`KK", 4, 6),
    }

    cubic = nx.from_graph6_bytes(b"GMs`KK")
    assert sorted(dict(cubic.degree()).values()) == [3] * 8
    assert nx.node_connectivity(cubic) == 2
    assert sorted(cubic.edges()) == [
        (0, 3),
        (0, 4),
        (0, 7),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 5),
        (2, 6),
        (3, 4),
        (5, 6),
        (5, 7),
        (6, 7),
    ]

    one_digest = sha256("\n".join(sorted(one_certificates)).encode()).hexdigest()
    two_digest = sha256("\n".join(sorted(two_certificates)).encode()).hexdigest()
    assert one_digest == "bb82cf5a05ad28d4cb5bcb323cf3f094c0a189c2a15ca1763a9fe67d2abaf024"
    assert two_digest == "664897369992e2eac75bca74d64911889203787ce9d9eb8d3b720438b7d863c9"
    completion_digest = verify_exceptional_rooted_completion()

    print("GREEN seven-connected degree-eight quotient classification")
    print(
        f"minimum_degree_three_extensions={raw_count} "
        f"isomorphism_classes={representative_count} critical_local={len(local)}"
    )
    print(
        f"one_component_profiles={len(local) * 9} positive={len(one_certificates)} "
        f"negative={len(one_negative)} negative_graphs={len(negative_graphs)}"
    )
    print(f"one_component_certificate_digest={one_digest}")
    print(
        f"two_component_profiles={len(local) * 45} "
        f"positive={len(two_certificates)} negative={two_negative}"
    )
    print(f"two_component_certificate_digest={two_digest}")
    print(f"exceptional_rooted_completion_digest={completion_digest}")
    print("all_one_component_survivors_have_kappa_J_in_{2,3}")


if __name__ == "__main__":
    main()
