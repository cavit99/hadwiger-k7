"""Exact exchange checks on two eleven-vertex full-hypothesis hosts.

Run: uv run python3 active/hc7_chromatic_exchange_probe.py
Add --summary to print only the CI summary after running all checks.
The second host was found among complements of triangle-free four-regular
NetworkX graphs (random_regular_graph(4, 11, seed=8093)). Explicit edges
make this check deterministic. Results concern these two hosts only.
A move splits one connected bag into two connected parts and merges two
adjacent resulting parts. Every spanning-tree representation is covered.
"""
import argparse
from collections import Counter
from itertools import combinations
import json

from hc7_forest_exchange_probe import check_model
import networkx as nx


class ModelSpace:
    def __init__(self, order, edges):
        self.order = order
        self.edges = tuple(sorted(tuple(sorted(e)) for e in edges))
        self.adjacency = [0] * order
        for u, v in self.edges:
            self.adjacency[u] |= 1 << v
            self.adjacency[v] |= 1 << u
        self.hood = [0] * (1 << order)
        self.connected = [False] * (1 << order)
        for mask in range(1, 1 << order):
            bit = mask & -mask
            self.hood[mask] = self.hood[mask ^ bit] | self.adjacency[bit.bit_length() - 1]
            reached = bit
            while True:
                following = reached | (self.hood[reached] & mask)
                if following == reached:
                    self.connected[mask] = reached == mask
                    break
                reached = following
        self.splits = {}
        for mask in range(1, 1 << order):
            pairs = []
            part = (mask - 1) & mask
            while part:
                other = mask ^ part
                if part & (mask & -mask) and self.connected[part] and self.connected[other]:
                    pairs.append((part, other))
                part = (part - 1) & mask
            self.splits[mask] = pairs

    def vertices(self, mask):
        return [v for v in range(self.order) if mask >> v & 1]

    def masks(self, bags):
        return tuple(sorted(sum(1 << v for v in bag) for bag in bags))

    def partitions(self, count):
        bags = []

        def extend(v):
            if len(bags) + self.order - v < count:
                return
            if v == self.order:
                if len(bags) == count:
                    yield tuple(sorted(bags))
                return
            for j in range(len(bags)):
                bags[j] |= 1 << v
                yield from extend(v + 1)
                bags[j] ^= 1 << v
            if len(bags) < count:
                bags.append(1 << v)
                yield from extend(v + 1)
                bags.pop()

        yield from extend(0)

    def objective(self, bags):
        missing = [(i, j) for i, j in combinations(range(len(bags)), 2)
                   if not self.hood[bags[i]] & bags[j]]
        degrees = Counter(v for pair in missing for v in pair)
        return (len(missing), sum(d * (d - 1) // 2 for d in degrees.values()),
                sum(b.bit_count() ** 2 for b in bags))

    def moves(self, bags):
        seen = set()
        for i, bag in enumerate(bags):
            for left, right in self.splits[bag]:
                parts = [b for j, b in enumerate(bags) if j != i] + [left, right]
                for a, b in combinations(range(8), 2):
                    if not self.hood[parts[a]] & parts[b]:
                        continue
                    changed = tuple(sorted([m for j, m in enumerate(parts) if j not in (a, b)]
                                           + [parts[a] | parts[b]]))
                    if changed not in seen:
                        seen.add(changed)
                        yield changed

    def checked_trace(self, trace):
        graph = nx.Graph()
        graph.add_nodes_from(range(self.order))
        graph.add_edges_from(self.edges)
        masks = [self.masks(bags) for bags in trace]
        for before, after in zip(masks, masks[1:]):
            assert after in set(self.moves(before))
        return [{**check_model(graph, [self.vertices(b) for b in bags]),
                 'objective': self.objective(bags)} for bags in masks]


def terminal(value):
    return value[0] <= 2 and value[1] == 0


def certify_host(space, colouring):
    assert space.order == 11
    assert sorted(v for bag in colouring for v in bag) == list(range(11))
    assert len(colouring) == 6
    assert all(not space.adjacency[u] >> v & 1
               for bag in colouring for u, v in combinations(bag, 2))
    assert all(any(space.adjacency[u] >> v & 1 for u, v in combinations(triple, 2))
               for triple in combinations(range(11), 3))
    degree = [a.bit_count() for a in space.adjacency]
    assert min(degree) >= 6
    full = (1 << space.order) - 1
    # All deletions of at most four vertices are checked, rather than relying
    # on a connectivity routine's absence of a returned small cut.
    for size in range(5):
        assert all(space.connected[full ^ sum(1 << v for v in cut)]
                   for cut in combinations(range(11), size))
    return {'order': 11, 'edges': space.edges, 'minimum_degree': min(degree),
            'six_colouring': colouring, 'lower_bound': 'No independent triple; ceil(11/2)=6.',
            'connectivity_check': 'Every deletion of at most four vertices leaves a connected graph.'}


def examine(space):
    total = 0
    states = {}
    for bags in space.partitions(7):
        total += 1
        if all(space.connected[b] for b in bags):
            states[bags] = space.objective(bags)
    strict_traps = []
    balanced_traps = []
    for bags, value in states.items():
        if terminal(value):
            continue
        following = [states[other] for other in space.moves(bags)]
        if not any(other[:2] < value[:2] for other in following):
            strict_traps.append(bags)
        if not any(other < value for other in following):
            balanced_traps.append(bags)
    return {'all_seven_partitions': total, 'connected_seven_partitions': len(states),
            'missing_contact_histogram': dict(sorted(Counter(v[0] for v in states.values()).items())),
            'Q7_models': sum(terminal(v) for v in states.values()),
            'K7_models': sum(v[0] == 0 for v in states.values()),
            'two_coordinate_local_minima': len(strict_traps),
            'three_coordinate_local_minima': len(balanced_traps)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args(argv)
    pairs = tuple(combinations(range(11), 2))
    circulant = ModelSpace(11, [e for e in pairs if (e[1] - e[0]) % 11 in (2, 3, 5, 6, 8, 9)])
    complement = [(0, 1), (0, 6), (0, 7), (0, 10), (1, 2), (1, 5), (1, 8),
                  (2, 6), (2, 7), (2, 10), (3, 5), (3, 6), (3, 7), (3, 8),
                  (4, 5), (4, 6), (4, 8), (4, 10), (5, 9), (7, 9), (8, 9), (9, 10)]
    host = ModelSpace(11, [e for e in pairs if e not in complement])
    colourings = [[list(range(i, i + 2)) for i in range(0, 10, 2)] + [[10]],
                  [[0, 6], [1, 5], [3, 7], [4, 8], [9, 10], [2]]]
    results = []
    for name, space, colouring, expected in zip(
            ['circulant_control', 'ownership_trap'], [circulant, host], colourings,
            [(16093, 792, 0, 0), (16082, 681, 24, 3)]):
        result = {'name': name, **certify_host(space, colouring), **examine(space)}
        assert result['all_seven_partitions'] == 63987
        assert tuple(result[k] for k in ('connected_seven_partitions', 'Q7_models',
                                         'two_coordinate_local_minima', 'K7_models')) == expected
        assert result['three_coordinate_local_minima'] == 0
        results.append(result)
    trace = [
        [[1], [3], [0, 2, 5], [6], [4, 7, 8], [9], [10]],
        [[1], [2, 3], [0, 5], [6], [4, 7, 8], [9], [10]],
        [[2, 3], [0, 5], [6], [4, 7], [8], [1, 9], [10]],
    ]
    results[1]['trace'] = host.checked_trace(trace)
    initial = host.masks(trace[0])
    one_move = list(host.moves(initial))
    histogram = Counter(host.objective(b)[:2] for b in one_move)
    assert len(one_move) == 103 and min(histogram) == (3, 0)
    assert histogram[(3, 0)] == 12
    assert [item['objective'] for item in results[1]['trace']] == [(3, 0, 23), (3, 0, 21), (2, 0, 19)]
    results[1]['one_move_count_including_unchanged'] = len(one_move)
    results[1]['one_move_defect_histogram'] = {str(k): v for k, v in sorted(histogram.items())}
    report = {'scope': 'Two explicit eleven-vertex hosts only; no universal exchange theorem.',
                      'moves': 'Connected split followed by adjacent merge; roots and ownership may change.',
                      'objectives': ['missing contacts', 'pairs of missing contacts sharing a bag',
                                     'sum of squared bag sizes'],
                      'summary': 'PASS: genuine strict-defect trap, shortest two-move plateau escape, and finite balance refinement.',
                      'cases': results}
    print(report['summary'] if args.summary else json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
