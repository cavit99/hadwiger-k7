#!/usr/bin/env python3
"""Hostile order-8/9 screen for the literal-K44 spanning split residue.

This is bounded falsification machinery, not an unbounded proof.  The graph
generator supplies unlabelled connected hosts of minimum degree at least four;
we retain only three-connected hosts and ask Z3 for boundary incidences.

Two logically distinct negations are available:

* ``anchored``: no eligible distinguished vertex p belongs to the first side
  of a connected spanning partition whose second side sees b and which splits
  at least three K-supports;
* ``full``: no oriented connected spanning partition satisfies the exact
  three/four split-count criterion.

Every SAT model is checked again by solver-free exhaustive Python code.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import z3

if not __debug__:
    raise SystemExit("verification requires assertions; do not use Python -O")


def load_networkx():
    try:
        import networkx as nx

        return nx
    except ModuleNotFoundError:
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


def vertices(mask: int, order: int) -> list[int]:
    return [vertex for vertex in range(order) if mask & (1 << vertex)]


def bool_or(terms):
    terms = list(terms)
    return z3.Or(terms) if terms else z3.BoolVal(False)


def pb_at_least(terms, bound: int):
    terms = list(terms)
    if bound <= 0:
        return z3.BoolVal(True)
    if bound > len(terms):
        return z3.BoolVal(False)
    return z3.PbGe([(term, 1) for term in terms], bound)


def pb_at_most(terms, bound: int):
    terms = list(terms)
    if bound < 0:
        return z3.BoolVal(False)
    if bound >= len(terms):
        return z3.BoolVal(True)
    return z3.PbLe([(term, 1) for term in terms], bound)


@dataclass(frozen=True)
class HostData:
    graph6: str
    graph: object
    order: int
    full: int
    connected_masks: frozenset[int]
    internal_boundaries: tuple[int, ...]
    three_cut_components: tuple[tuple[int, ...], ...]
    spanning_partitions: tuple[int, ...]

    @classmethod
    def from_graph6(cls, code: str):
        graph = nx.from_graph6_bytes(code.encode())
        graph = nx.convert_node_labels_to_integers(graph)
        order = len(graph)
        full = (1 << order) - 1
        connected_masks = frozenset(
            mask
            for mask in range(1, full + 1)
            if nx.is_connected(graph.subgraph(vertices(mask, order)))
        )
        internal_boundaries = []
        for mask in range(full + 1):
            inside = set(vertices(mask, order))
            boundary: set[int] = set()
            for vertex in inside:
                boundary.update(graph.neighbors(vertex))
            internal_boundaries.append(len(boundary - inside))

        cut_components = []
        for cut in itertools.combinations(range(order), 3):
            remaining = set(range(order)) - set(cut)
            subgraph = graph.subgraph(remaining)
            components = list(nx.connected_components(subgraph))
            if len(components) > 1:
                masks = tuple(
                    sorted(sum(1 << vertex for vertex in component) for component in components)
                )
                cut_components.append(masks)

        spanning_partitions = tuple(
            left
            for left in range(1, full)
            if left in connected_masks and (full ^ left) in connected_masks
        )
        return cls(
            graph6=code,
            graph=graph,
            order=order,
            full=full,
            connected_masks=connected_masks,
            internal_boundaries=tuple(internal_boundaries),
            three_cut_components=tuple(cut_components),
            spanning_partitions=spanning_partitions,
        )


class IncidenceEncoding:
    def __init__(self, host: HostData, mode: str):
        self.host = host
        self.mode = mode
        self.solver = z3.Solver()
        self.incidence = {
            (vertex, resource): z3.Bool(f"i_{vertex}_{resource}")
            for vertex in range(host.order)
            for resource in range(D_SIZE)
        }

    def sees(self, mask: int, resource: int):
        return bool_or(
            self.incidence[vertex, resource]
            for vertex in vertices(mask, self.host.order)
        )

    def support_wholly_in(self, resource: int, mask: int):
        return z3.And(
            self.sees(mask, resource),
            *(
                z3.Not(self.incidence[vertex, resource])
                for vertex in range(self.host.order)
                if not mask & (1 << vertex)
            ),
        )

    def eligible(self, vertex: int):
        complement = self.host.full ^ (1 << vertex)
        return z3.And(
            self.incidence[vertex, A],
            *(self.sees(complement, resource) for resource in H),
            pb_at_most((self.incidence[vertex, resource] for resource in K), 2),
        )

    def impose_boundary_and_minimality(self):
        for resource in range(D_SIZE):
            self.solver.add(self.sees(self.host.full, resource))

        for mask in range(1, self.host.full + 1):
            internal_order = self.host.internal_boundaries[mask]
            represented = [self.sees(mask, resource) for resource in range(D_SIZE)]
            self.solver.add(pb_at_least(represented, 7 - internal_order))
            if mask != self.host.full and mask in self.host.connected_masks:
                self.solver.add(
                    z3.Implies(
                        z3.And(self.sees(mask, A), self.sees(mask, B)),
                        pb_at_least(represented, 8 - internal_order),
                    )
                )

    def impose_attachment_and_anchor(self):
        # In the singleton-atom normal form P=N_X(a) has order 1 through 5.
        self.solver.add(
            pb_at_most(
                (self.incidence[vertex, A] for vertex in range(self.host.order)),
                5,
            )
        )
        for resource in K:
            self.solver.add(
                pb_at_least(
                    (
                        self.incidence[vertex, resource]
                        for vertex in range(self.host.order)
                    ),
                    2,
                )
            )
        # The five K-resources are interchangeable.  Sorting their incidence
        # bit-vectors removes only names, not mathematical models.
        support_values = [
            z3.Sum(
                *(
                    z3.If(self.incidence[vertex, resource], 1 << vertex, 0)
                    for vertex in range(self.host.order)
                )
            )
            for resource in K
        ]
        self.solver.add(
            *(support_values[index] <= support_values[index + 1] for index in range(4))
        )
        self.solver.add(
            z3.Or(*(self.eligible(vertex) for vertex in range(self.host.order)))
        )

    def profile_one(self, components: tuple[int, int, int]):
        alternatives = []
        for universal in itertools.combinations(K, 2):
            exclusive = tuple(resource for resource in K if resource not in universal)
            for assigned_components in itertools.permutations(components):
                terms = [
                    self.sees(component, resource)
                    for resource in universal
                    for component in components
                ]
                terms.extend(
                    self.support_wholly_in(resource, component)
                    for resource, component in zip(exclusive, assigned_components)
                )
                alternatives.append(z3.And(*terms))
        return z3.Or(*alternatives)

    def profile_two(self, components: tuple[int, int, int]):
        alternatives = []
        for exceptional_index in range(3):
            exceptional = components[exceptional_index]
            others = tuple(
                component
                for index, component in enumerate(components)
                if index != exceptional_index
            )
            for crossing in itertools.combinations(K, 3):
                crossing = tuple(crossing)
                exclusive = tuple(resource for resource in K if resource not in crossing)
                for assigned in (exclusive, tuple(reversed(exclusive))):
                    terms = [
                        self.support_wholly_in(A, exceptional),
                        self.support_wholly_in(B, exceptional),
                    ]
                    for resource in crossing:
                        wholly_somewhere = z3.Or(
                            *(self.support_wholly_in(resource, component) for component in components)
                        )
                        terms.extend(
                            [z3.Not(wholly_somewhere), self.sees(exceptional, resource)]
                        )
                    terms.extend(
                        self.support_wholly_in(resource, component)
                        for resource, component in zip(assigned, others)
                    )
                    for component in others:
                        terms.append(
                            pb_at_least(
                                (self.sees(component, resource) for resource in crossing),
                                2,
                            )
                        )
                    alternatives.append(z3.And(*terms))
        return z3.Or(*alternatives)

    def impose_three_cut_profiles(self):
        for components in self.host.three_cut_components:
            if len(components) > 3:
                self.solver.add(z3.BoolVal(False))
            elif len(components) == 3:
                self.solver.add(
                    z3.Or(self.profile_one(components), self.profile_two(components))
                )

    def split_terms(self, left: int, right: int):
        return [
            z3.And(self.sees(left, resource), self.sees(right, resource))
            for resource in K
        ]

    def impose_anchored_failure(self):
        for vertex in range(self.host.order):
            for left in self.host.spanning_partitions:
                if not left & (1 << vertex):
                    continue
                right = self.host.full ^ left
                self.solver.add(
                    z3.Implies(
                        z3.And(self.eligible(vertex), self.sees(right, B)),
                        pb_at_most(self.split_terms(left, right), 2),
                    )
                )

    def impose_full_failure(self):
        for left in self.host.spanning_partitions:
            right = self.host.full ^ left
            premise = self.sees(left, A)
            split = self.split_terms(left, right)
            self.solver.add(
                z3.Implies(
                    z3.And(premise, self.sees(right, B)), pb_at_most(split, 2)
                )
            )
            self.solver.add(
                z3.Implies(
                    z3.And(premise, z3.Not(self.sees(right, B))),
                    pb_at_most(split, 3),
                )
            )

    def impose(self):
        self.impose_boundary_and_minimality()
        self.impose_attachment_and_anchor()
        self.impose_three_cut_profiles()
        if self.mode == "anchored":
            self.impose_anchored_failure()
        elif self.mode == "full":
            self.impose_full_failure()
        else:
            raise ValueError(self.mode)

    def solve(self):
        self.impose()
        status = self.solver.check()
        if status != z3.sat:
            return status, None
        model = self.solver.model()
        supports = tuple(
            frozenset(
                vertex
                for vertex in range(self.host.order)
                if z3.is_true(model.eval(self.incidence[vertex, resource], model_completion=True))
            )
            for resource in range(D_SIZE)
        )
        return status, supports


def components_after_three_cut(host: HostData) -> bool:
    return all(len(components) <= 3 for components in host.three_cut_components)


def eligible_vertices(supports, order: int) -> list[int]:
    all_vertices = set(range(order))
    return [
        vertex
        for vertex in supports[A]
        if all(supports[resource] & (all_vertices - {vertex}) for resource in H)
        and sum(vertex in supports[resource] for resource in K) <= 2
    ]


def direct_profile_one(supports, components: tuple[int, int, int], order: int) -> bool:
    component_sets = tuple(set(vertices(mask, order)) for mask in components)
    for universal in itertools.combinations(K, 2):
        if not all(supports[resource] & component for resource in universal for component in component_sets):
            continue
        exclusive = tuple(resource for resource in K if resource not in universal)
        for assignment in itertools.permutations(component_sets):
            if all(supports[resource] <= component for resource, component in zip(exclusive, assignment)):
                return True
    return False


def direct_profile_two(supports, components: tuple[int, int, int], order: int) -> bool:
    component_sets = tuple(set(vertices(mask, order)) for mask in components)
    for exceptional_index, exceptional in enumerate(component_sets):
        if not supports[A] <= exceptional or not supports[B] <= exceptional:
            continue
        others = tuple(
            component for index, component in enumerate(component_sets) if index != exceptional_index
        )
        for crossing_choice in itertools.combinations(K, 3):
            crossing = set(crossing_choice)
            if any(any(supports[resource] <= component for component in component_sets) for resource in crossing):
                continue
            if not all(supports[resource] & exceptional for resource in crossing):
                continue
            exclusive = tuple(resource for resource in K if resource not in crossing)
            for assignment in (exclusive, tuple(reversed(exclusive))):
                if not all(supports[resource] <= component for resource, component in zip(assignment, others)):
                    continue
                if all(
                    sum(bool(supports[resource] & component) for resource in crossing) >= 2
                    for component in others
                ):
                    return True
    return False


def direct_witnesses(host: HostData, supports):
    anchored = []
    full = []
    eligible = eligible_vertices(supports, host.order)
    for left in host.spanning_partitions:
        right = host.full ^ left
        left_set = set(vertices(left, host.order))
        right_set = set(vertices(right, host.order))
        splits = tuple(
            resource
            for resource in K
            if supports[resource] & left_set and supports[resource] & right_set
        )
        if supports[A] & left_set:
            epsilon = int(not bool(supports[B] & right_set))
            if len(splits) >= 3 + epsilon:
                full.append((left, right, splits, epsilon))
        if supports[B] & right_set and len(splits) >= 3:
            for vertex in eligible:
                if vertex in left_set:
                    anchored.append((vertex, left, right, splits))
    return anchored, full


def validate_survivor(host: HostData, supports, mode: str):
    assert nx.node_connectivity(host.graph) >= 3
    assert min(dict(host.graph.degree()).values()) >= 4
    assert components_after_three_cut(host)
    assert all(supports[resource] for resource in range(D_SIZE))
    assert 1 <= len(supports[A]) <= 5
    assert all(len(supports[resource]) >= 2 for resource in K)
    assert eligible_vertices(supports, host.order)

    for mask in range(1, host.full + 1):
        inside = set(vertices(mask, host.order))
        represented = sum(bool(supports[resource] & inside) for resource in range(D_SIZE))
        boundary = host.internal_boundaries[mask] + represented
        assert boundary >= 7, (mask, boundary)
        if mask != host.full and mask in host.connected_masks:
            if supports[A] & inside and supports[B] & inside:
                assert boundary >= 8, (mask, boundary, "minimality")

    for components in host.three_cut_components:
        if len(components) == 3:
            assert direct_profile_one(supports, components, host.order) or direct_profile_two(
                supports, components, host.order
            )

    anchored, full = direct_witnesses(host, supports)
    if mode == "anchored":
        assert not anchored
    elif mode == "full":
        assert not full
    else:
        raise ValueError(mode)
    return anchored, full


def canonical_graph6(graphs, labelg: str):
    raw = "".join(
        nx.to_graph6_bytes(graph, header=False).decode()
        for graph in graphs
    )
    completed = subprocess.run(
        [labelg, "-q"],
        check=True,
        input=raw,
        capture_output=True,
        text=True,
    )
    return tuple(sorted(set(line.strip() for line in completed.stdout.splitlines() if line.strip())))


def join_perturbation_hosts(order: int, labelg: str):
    if order != 9:
        raise ValueError("K3-join-3K2 perturbations have order nine")
    base = nx.Graph()
    base.add_nodes_from(range(9))
    base.add_edges_from(itertools.combinations(range(3), 2))
    base.add_edges_from(((3, 4), (5, 6), (7, 8)))
    base.add_edges_from((centre, outer) for centre in range(3) for outer in range(3, 9))
    optional = tuple(
        edge
        for edge in itertools.combinations(range(3, 9), 2)
        if not base.has_edge(*edge)
    )
    graphs = []
    for added_order in range(3):
        for added in itertools.combinations(optional, added_order):
            graph = base.copy()
            graph.add_edges_from(added)
            graphs.append(graph)
    return canonical_graph6(graphs, labelg)


def generated_hosts(
    order: int,
    geng: str,
    max_degree: int | None,
    family: str,
    planarg: str | None,
    labelg: str | None,
):
    if family == "join-perturbations":
        if not labelg:
            raise RuntimeError("nauty labelg is required for the join family")
        codes = join_perturbation_hosts(order, labelg)
        digest = hashlib.sha256(("\n".join(codes) + "\n").encode()).hexdigest()
        return codes, digest

    command = [geng, "-q", "-c", "-d4"]
    if max_degree is not None:
        command.append(f"-D{max_degree}")
    command.append(str(order))
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    generated = completed.stdout
    if family == "planar":
        if not planarg:
            raise RuntimeError("nauty planarg is required for the planar family")
        filtered = subprocess.run(
            [planarg, "-q"],
            check=True,
            input=generated,
            capture_output=True,
            text=True,
        )
        generated = filtered.stdout
    codes = tuple(sorted(line.strip() for line in generated.splitlines() if line.strip()))
    digest = hashlib.sha256(("\n".join(codes) + "\n").encode()).hexdigest()
    return codes, digest


def support_text(supports) -> str:
    names = ("a", "b", "k1", "k2", "k3", "k4", "k5")
    return " ".join(
        f"{name}={{{','.join(map(str, sorted(support)))}}}"
        for name, support in zip(names, supports)
    )


def search(
    order: int,
    mode: str,
    geng: str,
    stop_after: int | None,
    max_degree: int | None,
    family: str,
    min_connectivity: int,
    planarg: str | None,
    labelg: str | None,
    show_progress: bool = True,
    expected: tuple[int, str, int] | None = None,
):
    codes, digest = generated_hosts(
        order, geng, max_degree, family, planarg, labelg
    )
    if expected is not None:
        expected_generated, expected_digest, _ = expected
        if len(codes) != expected_generated or digest != expected_digest:
            raise AssertionError(
                "host generation mismatch: "
                f"got count={len(codes)} digest={digest}; "
                f"expected count={expected_generated} digest={expected_digest}"
            )
    degree_range = "delta>=4" if max_degree is None else f"4<=degree<={max_degree}"
    print(
        f"order={order} mode={mode} family={family} degree_range={degree_range} "
        f"min_connectivity={min_connectivity} generated={len(codes)} "
        f"graph6_digest={digest}"
    )
    examined = 0
    eligible_hosts = 0
    hosts = [HostData.from_graph6(code) for code in codes]
    hosts.sort(key=lambda host: (host.graph.number_of_edges(), host.graph6))
    for host in hosts:
        code = host.graph6
        if (
            nx.node_connectivity(host.graph) < min_connectivity
            or not components_after_three_cut(host)
        ):
            continue
        eligible_hosts += 1
        encoding = IncidenceEncoding(host, mode)
        status, supports = encoding.solve()
        examined += 1
        if show_progress and examined % 50 == 0:
            print(
                f"progress order={order} mode={mode} examined={examined}",
                flush=True,
            )
        if status == z3.unknown:
            raise RuntimeError(f"Z3 returned unknown on {code}")
        if status == z3.sat:
            anchored, full = validate_survivor(host, supports, mode)
            print(
                f"SAT order={order} mode={mode} graph6={code} "
                f"eligible_p={eligible_vertices(supports, order)}"
            )
            print(support_text(supports))
            print(
                f"direct_validation=GREEN anchored_witnesses={len(anchored)} "
                f"full_witnesses={len(full)}"
            )
            return 1
        if stop_after is not None and examined >= stop_after:
            print(
                f"INCOMPLETE order={order} mode={mode} examined={examined} "
                f"eligible_hosts_seen={eligible_hosts}"
            )
            return 2
    print(
        f"UNSAT order={order} mode={mode} examined={examined} "
        f"eligible_hosts={eligible_hosts}"
    )
    if expected is not None:
        expected_eligible = expected[2]
        if examined != expected_eligible or eligible_hosts != expected_eligible:
            raise AssertionError(
                "eligible-host mismatch: "
                f"examined={examined} eligible={eligible_hosts}; "
                f"expected={expected_eligible}"
            )
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, choices=(8, 9), required=True)
    parser.add_argument("--mode", choices=("anchored", "full"), required=True)
    parser.add_argument("--stop-after", type=int)
    parser.add_argument("--max-degree", type=int)
    parser.add_argument(
        "--family",
        choices=("all", "planar", "join-perturbations"),
        default="all",
    )
    parser.add_argument("--min-connectivity", type=int, default=3)
    parser.add_argument("--geng", default=shutil.which("geng"))
    parser.add_argument("--planarg", default=shutil.which("planarg"))
    parser.add_argument("--labelg", default=shutil.which("labelg"))
    args = parser.parse_args()
    if not args.geng:
        parser.error("nauty geng is required (or pass --geng PATH)")
    print(
        f"z3_version={z3.get_version_string()} networkx_version={nx.__version__} "
        "nauty_tools=available"
    )
    if args.max_degree is not None and args.max_degree < 4:
        parser.error("--max-degree must be at least four")
    if args.min_connectivity < 3:
        parser.error("--min-connectivity must be at least three")
    if args.family == "join-perturbations" and args.max_degree is not None:
        parser.error("--max-degree does not apply to the join family")
    raise SystemExit(
        search(
            args.order,
            args.mode,
            args.geng,
            args.stop_after,
            args.max_degree,
            args.family,
            args.min_connectivity,
            args.planarg,
            args.labelg,
            True,
        )
    )


if __name__ == "__main__":
    main()
