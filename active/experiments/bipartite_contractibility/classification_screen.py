"""Finite M'-contractibility falsification; positives are not scheme proofs.

Uses KPR Theorem 7.7: a stable S, a matching covering N(S), and a
neighbour-shift automorphism of the remaining induced graph. Every positive
certificate and every excluded skewed theta is checked independently.
"""

import argparse
import hashlib
import itertools
import json

import networkx as nx


def triangle_free(graph):
    return all(not (set(graph[u]) & set(graph[v])) for u, v in graph.edges())


def skew_theta(graph):
    index = {v: i for i, v in enumerate(graph)}
    branch_vertices = [v for v in graph if graph.degree(v) >= 3]
    for u, v in itertools.combinations(branch_vertices, 2):
        odd, even = [], []
        for path in nx.all_simple_paths(graph, u, v):
            mask = sum(1 << index[x] for x in path[1:-1])
            (odd if (len(path) - 1) % 2 else even).append((mask, path))
        for (first, p), (second, q) in itertools.combinations(odd, 2):
            if first & second:
                continue
            for third, r in even:
                if not third & (first | second):
                    return [p, q, r]
    return None


def verify_skew(graph, paths):
    assert len(paths) == 3 and len({tuple(p) for p in paths}) == 3
    assert [len(p) % 2 for p in paths] == [0, 0, 1]
    assert len({(p[0], p[-1]) for p in paths}) == 1
    interiors = [set(p[1:-1]) for p in paths]
    for path in paths:
        assert len(path) == len(set(path))
        assert all(graph.has_edge(u, v) for u, v in zip(path, path[1:]))
    assert all(not a & b for a, b in itertools.combinations(interiors, 2))


def one_edge_bipartite(graph):
    for vertices in nx.connected_components(graph):
        component = graph.subgraph(vertices).copy()
        if nx.is_bipartite(component):
            continue
        for u, v in list(component.edges()):
            component.remove_edge(u, v)
            if nx.is_bipartite(component):
                break
            component.add_edge(u, v)
        else:
            return False
    return True


class ShiftMatcher(nx.algorithms.isomorphism.GraphMatcher):
    def semantic_feasibility(self, u, v):
        return self.G1.has_edge(u, v) and super().semantic_feasibility(u, v)


def certificate_for_stable_set(graph, stable):
    stable = set(stable)
    neighborhood = set().union(*(set(graph[v]) for v in stable)) if stable else set()
    if neighborhood & stable or len(neighborhood) > len(stable):
        return None
    bipartite = nx.Graph()
    bipartite.add_nodes_from(sorted(stable | neighborhood))
    bipartite.add_edges_from((u, v) for u in sorted(stable) for v in graph[u])
    matching = nx.bipartite.maximum_matching(bipartite, top_nodes=stable)
    if any(v not in matching for v in neighborhood):
        return None
    residual = graph.subgraph(set(graph) - stable - neighborhood)
    if any(residual.degree(v) == 0 for v in residual):
        return None
    shift = next(ShiftMatcher(residual, residual).isomorphisms_iter(), None)
    if shift is None:
        return None
    certificate = {
        "S": sorted(stable),
        "matching": [[v, matching[v]] for v in sorted(neighborhood)],
        "shift": sorted(shift.items()),
    }
    verify_positive(graph, certificate)
    return certificate


def mprime(graph):
    vertices = sorted(graph)
    index = {v: i for i, v in enumerate(vertices)}
    neighbors = [sum(1 << index[u] for u in graph[v]) for v in vertices]
    for mask in range(1 << len(vertices)):
        rest, boundary = mask, 0
        while rest:
            bit = rest & -rest
            rest -= bit
            v = bit.bit_length() - 1
            if neighbors[v] & mask:
                break
            boundary |= neighbors[v]
        else:
            if boundary.bit_count() <= mask.bit_count():
                stable = [v for i, v in enumerate(vertices) if mask >> i & 1]
                certificate = certificate_for_stable_set(graph, stable)
                if certificate is not None:
                    return certificate
    return None


def verify_positive(graph, certificate):
    stable = set(certificate["S"])
    assert not any(graph.has_edge(u, v) for u, v in itertools.combinations(stable, 2))
    neighborhood = set().union(*(set(graph[v]) for v in stable)) if stable else set()
    matching = certificate["matching"]
    assert len(matching) == len(neighborhood)
    assert {u for u, _ in matching} == neighborhood
    assert len({v for _, v in matching}) == len(matching)
    assert all(v in stable and graph.has_edge(u, v) for u, v in matching)
    residual = set(graph) - stable - neighborhood
    shift = dict(certificate["shift"])
    assert set(shift) == set(shift.values()) == residual
    assert all(graph.has_edge(v, shift[v]) for v in residual)
    assert all(graph.has_edge(u, v) == graph.has_edge(shift[u], shift[v])
               for u, v in itertools.combinations(residual, 2))


def theta(lengths):
    graph = nx.Graph()
    graph.add_nodes_from([0, 1])
    next_vertex = 2
    for length in lengths:
        interior = list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        nx.add_path(graph, [0, *interior, 1])
    return graph


def calibration():
    for graph, expected in [(nx.cycle_graph(5), True), (theta([2, 3, 3]), False),
                            (theta([1, 3, 4]), False), (theta([1, 4, 4]), True),
                            (nx.complete_bipartite_graph(3, 3), True)]:
        assert (mprime(graph) is not None) == expected
    graph = theta([2, 3, 3])
    tested = negative = 0
    for order in range(len(graph) + 1):
        for vertices in itertools.combinations(graph, order):
            edges = list(graph.subgraph(vertices).edges())
            for mask in range(1 << len(edges)):
                subgraph = nx.Graph()
                subgraph.add_nodes_from(vertices)
                subgraph.add_edges_from(e for i, e in enumerate(edges) if mask >> i & 1)
                tested += 1
                if mprime(subgraph) is None:
                    negative += 1
                    assert set(subgraph) == set(graph) and set(subgraph.edges()) == set(graph.edges())
    assert (tested, negative) == (1279, 1)
    print(json.dumps({"calibration_subgraphs": tested, "negative": negative}), flush=True)


class Recorder:
    def __init__(self, path):
        self.output = open(path, "w") if path else None
        self.digest = hashlib.sha256()

    def record(self, graph, certificate, skew=None):
        if certificate is not None:
            verify_positive(graph, certificate)
        elif skew is not None:
            verify_skew(graph, skew)
        item = {"graph6": nx.to_graph6_bytes(graph, header=False).decode().strip(),
                "certificate": certificate, "skew_theta": skew}
        line = json.dumps(item, sort_keys=True) + "\n"
        self.digest.update(line.encode())
        if self.output:
            self.output.write(line)
        if certificate is None and skew is None:
            print(json.dumps({"candidate_counterexample": item}), flush=True)


def atlas(recorder):
    counts, negative = {}, 0
    for graph in nx.graph_atlas_g():
        if not triangle_free(graph) or not one_edge_bipartite(graph) or skew_theta(graph):
            continue
        certificate = mprime(graph)
        counts[len(graph)] = counts.get(len(graph), 0) + 1
        negative += certificate is None
        recorder.record(graph, certificate)
    print(json.dumps({"atlas_candidate_counts": counts, "Mprime_negative": negative}), flush=True)


def generated_order(order, recorder):
    """Exhaustive up to relabelling; isomorphic representations are retained."""
    for p in range(3, order - 1):
        q = order - p
        tested = positive = negative = candidate_negative = 0
        for choices in itertools.product(range(3), repeat=q):
            first = sum(1 << j for j, x in enumerate(choices) if x == 1)
            second = sum(1 << j for j, x in enumerate(choices) if x == 2)
            if not first or not second:
                continue
            for rest in range(1 << ((p - 2) * q)):
                rows = [first, second] + [(rest >> (q * i)) & ((1 << q) - 1) for i in range(p - 2)]
                if any(not row for row in rows):
                    continue
                graph = nx.Graph()
                graph.add_nodes_from(range(order))
                graph.add_edges_from((i, p + j) for i, row in enumerate(rows)
                                     for j in range(q) if row >> j & 1)
                if not nx.is_connected(graph):
                    continue
                graph.add_edge(0, 1)
                tested += 1
                certificate = mprime(graph)
                skew = skew_theta(graph) if certificate is None else None
                positive += certificate is not None
                negative += certificate is None
                candidate_negative += certificate is None and skew is None
                recorder.record(graph, certificate, skew)
        print(json.dumps({"order": order, "shore_orders": [p, q], "tested": tested,
                          "Mprime_positive": positive, "Mprime_negative": negative,
                          "candidate_negative": candidate_negative}), flush=True)


def even_subdivisions(recorder):
    tested = maximum_order = 0
    for base in nx.graph_atlas_g():
        if not 3 <= len(base) <= 6 or not nx.is_connected(base) or base.number_of_edges() < len(base):
            continue
        for x, y in itertools.combinations(base, 2):
            for default_length in (2, 4, 6):
                graph = nx.Graph()
                graph.add_nodes_from(base)
                next_vertex, stable = len(base), []
                for u, v in base.edges():
                    length = max(default_length, 4) if {u, v} == {x, y} else default_length
                    interior = list(range(next_vertex, next_vertex + length - 1))
                    next_vertex += length - 1
                    stable.extend(interior[::2])
                    nx.add_path(graph, [u, *interior, v])
                graph.add_edge(x, y)
                assert triangle_free(graph)
                certificate = certificate_for_stable_set(graph, stable)
                assert certificate is not None
                recorder.record(graph, certificate)
                tested += 1
                maximum_order = max(maximum_order, len(graph))
    print(json.dumps({"even_subdivision_samples": tested, "maximum_order": maximum_order}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, choices=(8, 9), help="exhaustive connected one-edge-bipartite generation")
    parser.add_argument("--even-subdivisions", action="store_true")
    parser.add_argument("--certificates", help="optional JSON-lines certificate output; bulk data stays outside Git")
    args = parser.parse_args()
    calibration()
    recorder = Recorder(args.certificates)
    atlas(recorder)
    if args.order:
        generated_order(args.order, recorder)
    if args.even_subdivisions:
        even_subdivisions(recorder)
    if recorder.output:
        recorder.output.close()
    print(json.dumps({"certificate_stream_sha256": recorder.digest.hexdigest()}))


if __name__ == "__main__":
    main()
