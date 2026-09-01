#!/usr/bin/env python3
"""Targeted finite screen for the literal-K44 minimum-blocker residue.

This is bounded evidence only.  It has two encodings:

* a fully symbolic labelled host through order six, checking every allowed
  two-helper pair; and
* an independent fixed-host encoding on NetworkX's unlabelled graph atlas
  through order seven.  The latter uses only spanning connected
  bipartitions, a necessary subfamily of the two-helper constraints.
"""

from __future__ import annotations

import hashlib
import itertools
import sys
from pathlib import Path

import z3


def load_networkx():
    try:
        import networkx as nx

        return nx
    except ModuleNotFoundError:
        # The repository's locked environment may not be active when the
        # Homebrew Python carrying z3-solver invokes this verifier.
        root = Path(__file__).resolve().parents[3]
        candidates = sorted((root / ".venv" / "lib").glob("python*/site-packages"))
        for candidate in candidates:
            sys.path.insert(0, str(candidate))
        import networkx as nx

        return nx


nx = load_networkx()

D_SIZE = 7
A = 0
B = 1
H = range(1, 7)
K = range(2, 7)

ATLAS_EXPECTED = {
    4: (1, "62073900de6d9451c02333f80b3c4de1105edb4559989fee6cfa91c1365d102b"),
    5: (3, "cf522cd28bc5df189b4691fde206d7c45fda756359d87686e5a6b901137d26c7"),
    6: (17, "5a698eceb9def652a91cada55716a9df0b9a13b195cbd0fbe59bd643fdcb488d"),
    7: (136, "af496d74518fb6a0126ac240981c6201a0d281fd1324f95033ae30eea291eb87"),
}


def vertices(mask: int, order: int) -> list[int]:
    return [v for v in range(order) if mask & (1 << v)]


def bool_or(terms):
    terms = list(terms)
    return z3.Or(terms) if terms else z3.BoolVal(False)


def pb_at_least(terms, bound: int):
    if bound <= 0:
        return z3.BoolVal(True)
    return z3.PbGe([(term, 1) for term in terms], bound)


class SymbolicHost:
    def __init__(self, order: int):
        self.order = order
        self.full = (1 << order) - 1
        self.solver = z3.Solver()
        self.edge = {
            (u, v): z3.Bool(f"edge_{u}_{v}")
            for u in range(order)
            for v in range(u + 1, order)
        }
        self.incidence = {
            (v, d): z3.Bool(f"incidence_{v}_{d}")
            for v in range(order)
            for d in range(D_SIZE)
        }
        self._connected_cache: dict[int, z3.BoolRef] = {}

    def edge_term(self, u: int, v: int):
        if u == v:
            return z3.BoolVal(False)
        return self.edge[min(u, v), max(u, v)]

    def sees(self, mask: int, d: int):
        return bool_or(self.incidence[v, d] for v in vertices(mask, self.order))

    def adjacent(self, left: int, right: int):
        return bool_or(
            self.edge_term(u, v)
            for u in vertices(left, self.order)
            for v in vertices(right, self.order)
        )

    def connected(self, mask: int):
        cached = self._connected_cache.get(mask)
        if cached is not None:
            return cached
        support = vertices(mask, self.order)
        if not support:
            return z3.BoolVal(False)
        root = support[0]
        reached = {v: z3.BoolVal(v == root) for v in support}
        for _ in range(len(support) - 1):
            reached = {
                v: z3.Or(
                    reached[v],
                    *(
                        z3.And(reached[u], self.edge_term(u, v))
                        for u in support
                        if u != v
                    ),
                )
                for v in support
            }
        result = z3.And(*(reached[v] for v in support))
        self._connected_cache[mask] = result
        return result

    def boundary_terms(self, mask: int):
        inside = vertices(mask, self.order)
        internal = [
            bool_or(self.edge_term(u, v) for u in inside)
            for v in range(self.order)
            if not mask & (1 << v)
        ]
        boundary = [self.sees(mask, d) for d in range(D_SIZE)]
        return internal + boundary

    def impose_three_connectivity(self):
        for deleted_order in range(3):
            for deleted_vertices in itertools.combinations(range(self.order), deleted_order):
                deleted = sum(1 << v for v in deleted_vertices)
                remaining = self.full ^ deleted
                anchor = vertices(remaining, self.order)[0]
                rest = remaining ^ (1 << anchor)
                left_without_anchor = rest
                while left_without_anchor:
                    left = left_without_anchor | (1 << anchor)
                    right = remaining ^ left
                    if right:
                        self.solver.add(self.adjacent(left, right))
                    left_without_anchor = (left_without_anchor - 1) & rest
                self.solver.add(self.adjacent(1 << anchor, rest))

    def impose_base_constraints(self):
        for d in range(D_SIZE):
            self.solver.add(self.sees(self.full, d))
        for mask in range(1, self.full + 1):
            terms = self.boundary_terms(mask)
            self.solver.add(pb_at_least(terms, 7))
            if mask != self.full:
                self.solver.add(
                    z3.Implies(
                        z3.And(self.connected(mask), self.sees(mask, A), self.sees(mask, B)),
                        pb_at_least(terms, 8),
                    )
                )

    def impose_all_two_helper_exclusions(self):
        for left in range(1, self.full + 1):
            remaining = self.full ^ left
            right = remaining
            while right:
                premise = z3.And(
                    self.connected(left),
                    self.connected(right),
                    self.adjacent(left, right),
                    self.sees(left, A),
                )
                for omitted in H:
                    missing = []
                    for h in H:
                        if h not in (B, omitted):
                            missing.append(z3.Not(self.sees(left, h)))
                        if h != omitted:
                            missing.append(z3.Not(self.sees(right, h)))
                    self.solver.add(z3.Implies(premise, pb_at_least(missing, 2)))
                right = (right - 1) & remaining


def symbolic_exact(order: int):
    encoding = SymbolicHost(order)
    encoding.impose_three_connectivity()
    encoding.impose_base_constraints()
    encoding.impose_all_two_helper_exclusions()
    status = encoding.solver.check()
    assert status == z3.unsat, (order, status)


class FixedHost:
    def __init__(self, graph):
        self.graph = nx.convert_node_labels_to_integers(graph)
        self.order = len(self.graph)
        self.full = (1 << self.order) - 1
        self.solver = z3.Solver()
        self.incidence = {
            (v, d): z3.Bool(f"incidence_{v}_{d}")
            for v in range(self.order)
            for d in range(D_SIZE)
        }

    def sees(self, mask: int, d: int):
        return bool_or(self.incidence[v, d] for v in vertices(mask, self.order))

    def connected(self, mask: int) -> bool:
        support = vertices(mask, self.order)
        return bool(support) and nx.is_connected(self.graph.subgraph(support))

    def internal_boundary_order(self, mask: int) -> int:
        inside = set(vertices(mask, self.order))
        boundary: set[int] = set()
        for v in inside:
            boundary.update(self.graph.neighbors(v))
        return len(boundary - inside)

    def impose_base_constraints(self):
        for d in range(D_SIZE):
            self.solver.add(self.sees(self.full, d))
        for mask in range(1, self.full + 1):
            internal_order = self.internal_boundary_order(mask)
            terms = [self.sees(mask, d) for d in range(D_SIZE)]
            self.solver.add(pb_at_least(terms, 7 - internal_order))
            if mask != self.full and self.connected(mask):
                self.solver.add(
                    z3.Implies(
                        z3.And(self.sees(mask, A), self.sees(mask, B)),
                        pb_at_least(terms, 8 - internal_order),
                    )
                )

    def impose_minimum_blocker_consequences(self):
        for k in K:
            self.solver.add(
                pb_at_least((self.incidence[v, k] for v in range(self.order)), 2)
            )
        choices = []
        for p in range(self.order):
            complement = self.full ^ (1 << p)
            choices.append(
                z3.And(
                    self.incidence[p, A],
                    *(self.sees(complement, h) for h in H),
                    z3.PbLe([(self.incidence[p, k], 1) for k in K], 2),
                )
            )
        self.solver.add(z3.Or(*choices))

    def impose_spanning_two_helper_exclusions(self):
        for left in range(1, self.full):
            right = self.full ^ left
            if not self.connected(left) or not self.connected(right):
                continue
            missed_k = [z3.Not(self.sees(left, k)) for k in K]
            supported_in_left = [z3.Not(self.sees(right, h)) for h in H]
            self.solver.add(
                z3.Implies(
                    self.sees(left, A),
                    pb_at_least(missed_k + supported_in_left, 3),
                )
            )


def atlas_hosts(order: int):
    hosts = [
        nx.convert_node_labels_to_integers(graph)
        for graph in nx.graph_atlas_g()
        if len(graph) == order and nx.node_connectivity(graph) >= 3
    ]
    codes = sorted(nx.to_graph6_bytes(graph, header=False).decode().strip() for graph in hosts)
    digest = hashlib.sha256(("\n".join(codes) + "\n").encode()).hexdigest()
    expected_count, expected_digest = ATLAS_EXPECTED[order]
    assert len(hosts) == expected_count
    assert digest == expected_digest
    return hosts, digest


def atlas_spanning(order: int):
    hosts, digest = atlas_hosts(order)
    for graph in hosts:
        encoding = FixedHost(graph)
        encoding.impose_base_constraints()
        encoding.impose_minimum_blocker_consequences()
        encoding.impose_spanning_two_helper_exclusions()
        status = encoding.solver.check()
        assert status == z3.unsat, (
            order,
            nx.to_graph6_bytes(graph, header=False).decode().strip(),
            status,
        )
    return len(hosts), digest


def main():
    print(f"z3_version={z3.get_version_string()} networkx_version={nx.__version__}")
    for order in range(4, 7):
        symbolic_exact(order)
        print(f"symbolic_exact order={order} status=UNSAT")
    for order in range(4, 8):
        count, digest = atlas_spanning(order)
        print(
            f"atlas_spanning order={order} hosts={count} status=UNSAT "
            f"host_digest={digest}"
        )
    print("GREEN bounded literal-K44 minimum-blocker bisection screen")


if __name__ == "__main__":
    main()
