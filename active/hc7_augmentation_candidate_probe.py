"""Targeted discovery checks for two augmentation construction proposals.

Run: uv run python3 active/hc7_augmentation_candidate_probe.py
Add --summary to print only the CI scope after running all checks.
Scope: the two stored eleven-vertex hosts only. No universal conclusion.
Existing partition, colouring and original-host model checkers are reused.
For the singleton question H-z is connected, so unused vertices can be
absorbed into the six other bags. Every minimal footprint found
below has order three; H-S is connected by five-connectivity, so the same
argument makes spanning enumeration complete for its fixed two-bag split.
"""

import argparse
from collections import Counter
from itertools import combinations
import json

import networkx as nx

from hc7_boundary_join_probe import colorable, induced
from hc7_chromatic_exchange_probe import ModelSpace, certify_host, terminal
from hc7_forest_exchange_probe import check_model


def hosts():
    pairs = list(combinations(range(11), 2))
    complements = [
        [e for e in pairs if (e[1] - e[0]) % 11 in (1, 4, 7, 10)],
        [(0, 1), (0, 6), (0, 7), (0, 10), (1, 2), (1, 5), (1, 8),
         (2, 6), (2, 7), (2, 10), (3, 5), (3, 6), (3, 7), (3, 8),
         (4, 5), (4, 6), (4, 8), (4, 10), (5, 9), (7, 9), (8, 9), (9, 10)],
    ]
    colourings = [
        [[0], [1, 2], [3, 7], [4, 8], [5, 9], [6, 10]],
        [[0, 6], [1, 5], [3, 7], [4, 8], [9, 10], [2]],
    ]
    for name, complement, colouring in zip(
            ("circulant", "ownership_trap"), complements, colourings):
        yield name, ModelSpace(11, [e for e in pairs if e not in complement]), colouring


def examine(name, space, colouring):
    host_certificate = certify_host(space, colouring)
    graph = nx.Graph()
    graph.add_nodes_from(range(space.order))
    graph.add_edges_from(space.edges)
    full = (1 << space.order) - 1
    rows = tuple(space.adjacency)
    singletons = {}
    paired_models = {}
    three_plus_four = {}
    near_clique_histogram = Counter()
    for bags in space.partitions(7):
        if not all(space.connected[bag] for bag in bags):
            continue
        objective = space.objective(bags)
        if not terminal(objective):
            continue
        if objective[0] <= 1:
            near_clique_histogram[objective[0]] += 1
            for triple in combinations([bag for bag in bags if bag.bit_count() == 1], 3):
                rest = [bag for bag in bags if bag not in triple]
                if (all(space.hood[left] & right for left, right in combinations(rest, 2))
                        and all(space.hood[left] & right for left in triple for right in rest)):
                    three_plus_four.setdefault(sum(triple), bags)
        universal = [bag for bag in bags
                     if all(bag == other or space.hood[bag] & other for other in bags)]
        for bag in universal:
            if bag.bit_count() == 1:
                singletons.setdefault(space.vertices(bag)[0], bags)
        for left, right in combinations(universal, 2):
            paired_models.setdefault(left | right, bags)

    def four_colourable(mask):
        return colorable(induced(rows, tuple(space.vertices(mask))), 4)

    footprints = []
    for footprint in range(1, full):
        support = space.vertices(footprint)
        if not nx.is_bipartite(graph.subgraph(support)):
            continue
        remainder = full ^ footprint
        if not four_colourable(remainder):
            continue
        if any(four_colourable(remainder | (1 << vertex)) for vertex in support):
            continue
        assert len(support) == 3
        assert nx.is_connected(graph.subgraph(space.vertices(remainder)))
        assert not colorable(induced(rows, tuple(space.vertices(remainder))), 3)
        dominating_splits = [
            (left, right) for left, right in space.splits[footprint]
            if space.hood[left] & right
            and space.hood[left] & remainder == remainder
            and space.hood[right] & remainder == remainder
        ]
        record = {"footprint": support, "connected": space.connected[footprint],
                  "dominating_split": [[space.vertices(part) for part in split]
                                       for split in dominating_splits],
                  "paired_wheel_model": None,
                  "three_singletons_four_clique_model": None}
        if footprint in paired_models:
            record["paired_wheel_model"] = check_model(
                graph, [space.vertices(bag) for bag in paired_models[footprint]])
        if footprint in three_plus_four:
            record["three_singletons_four_clique_model"] = check_model(
                graph, [space.vertices(bag) for bag in three_plus_four[footprint]])
        footprints.append(record)
    vertex_critical = all(colorable(induced(rows, tuple(v for v in range(11) if v != z)), 5)
                          for z in range(11))
    singleton_certificates = {
        str(z): check_model(graph, [space.vertices(bag) for bag in bags])
        for z, bags in sorted(singletons.items())
    }
    return {"name": name, "host": host_certificate, "six_vertex_critical": vertex_critical,
            "K7_and_K7_minus_edge_spanning_models": dict(near_clique_histogram),
            "singleton_universal_Q7_certificates": singleton_certificates,
            "singleton_universal_Q7_absent_vertices": sorted(set(range(11)) - set(singletons)),
            "minimal_bipartite_footprint_summary": {
                "by_order": dict(Counter(len(record["footprint"]) for record in footprints)),
                "connected": sum(record["connected"] for record in footprints),
                "dominating_split": sum(bool(record["dominating_split"]) for record in footprints),
                "paired_wheel_model": sum(record["paired_wheel_model"] is not None
                                          for record in footprints),
                "three_singletons_four_clique_model": sum(
                    record["three_singletons_four_clique_model"] is not None for record in footprints)},
            "minimal_bipartite_footprints": footprints}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args(argv)
    report = {
        "scope": "Two stored eleven-vertex hosts only; exact finite proposal tests, not a theorem.",
        "proposals": [
            "A selected singleton z is universal to six connected Q6 bags in H-z.",
            "A minimal bipartite footprint with four-colourable complement splits into two universal bags of one Q7 model.",
        ],
        "cases": [examine(*host) for host in hosts()],
    }
    print(report['scope'] if args.summary else json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
