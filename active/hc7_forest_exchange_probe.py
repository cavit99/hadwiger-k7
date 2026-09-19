"""Finite calibration: balanced 18-vertex host, K7 and squared C7.

Run: uv run python3 active/hc7_forest_exchange_probe.py
Add --summary to print only the CI summary after running all checks.
JSON on stdout contains original graphs and complete model traces. This is
not evidence for the five-connected six-chromatic augmentation target:
its full hypotheses are not checked, and the balanced host has a literal K6.
A failed bounded search concerns only its stated initial forest and depth.
"""
import argparse
from collections import deque
from itertools import combinations
import json

import networkx as nx


def edge(u, v):
    return tuple(sorted((u, v)))


def balanced_graph():
    g = nx.Graph()
    g.add_edges_from(combinations((f'c{i}' for i in range(6)), 2))
    g.add_edges_from((f'c{i}', f'{s}{i}') for i in range(6) for s in 'st')
    g.add_edges_from((f'{a}{i}', f'{b}{j}')
                     for i in range(3) for j in range(3, 6) for a in 'st' for b in 'st')
    assert (len(g), g.number_of_edges()) == (18, 63)
    return g


def bags_from_forest(g, forest):
    f = nx.Graph()
    f.add_nodes_from(g)
    f.add_edges_from(forest)
    assert set(forest) <= {edge(*e) for e in g.edges}
    assert len(forest) == len(g) - 7 and nx.is_forest(f)
    return tuple(sorted(tuple(sorted(b)) for b in nx.connected_components(f)))


def check_model(g, bags):
    """Verify bags and all contacts directly, independently of the forest."""
    assert len(bags) == 7 and all(bags)
    vertices = [v for bag in bags for v in bag]
    assert len(vertices) == len(set(vertices)) == len(g) and set(vertices) == set(g)
    adjacency = {v: set(g.neighbors(v)) for v in g}
    for bag in bags:
        reached = {bag[0]}
        queue = deque(reached)
        while queue:
            for v in (adjacency[queue.popleft()] & set(bag)) - reached:
                reached.add(v)
                queue.append(v)
        assert reached == set(bag)
    contacts = []
    missing = []
    for i, j in combinations(range(7), 2):
        witnesses = sorted(edge(u, v) for u in bags[i] for v in bags[j] if v in adjacency[u])
        if witnesses:
            contacts.append({'bags': [i, j], 'edges': witnesses})
        else:
            missing.append((i, j))
    defect = [len(missing), sum(bool(set(e) & set(f)) for e, f in combinations(missing, 2))]
    return {'bags': bags, 'contacts': contacts, 'missing': missing, 'defect': defect,
            'terminal': defect[0] <= 2 and defect[1] == 0}


def exchanges(g, forest):
    for removed in sorted(forest):
        reduced = forest - {removed}
        f = nx.Graph()
        f.add_nodes_from(g)
        f.add_edges_from(reduced)
        owner = {v: i for i, bag in enumerate(nx.connected_components(f)) for v in bag}
        for inserted in sorted(edge(*e) for e in g.edges):
            if inserted != removed and inserted not in reduced and owner[inserted[0]] != owner[inserted[1]]:
                yield reduced | {inserted}, removed, inserted


def search(g, initial, depth_cap):
    initial = frozenset(initial)
    queue = deque([(initial, 0)])
    parents = {initial: None}
    expanded = [0] * (depth_cap + 1)
    checked = [0] * (depth_cap + 1)
    checked[0] = 1
    found = initial if check_model(g, bags_from_forest(g, initial))['terminal'] else None
    while queue and found is None:
        forest, depth = queue.popleft()
        if depth == depth_cap:
            continue
        for following, removed, inserted in exchanges(g, forest):
            if following not in parents:
                parents[following] = (forest, removed, inserted)
                checked[depth + 1] += 1
                if check_model(g, bags_from_forest(g, following))['terminal']:
                    found = following
                    break
                queue.append((following, depth + 1))
        if found is None:
            expanded[depth] += 1
    path = []
    current = found if found is not None else initial
    while current is not None:
        record = {'forest': sorted(current), **check_model(g, bags_from_forest(g, current))}
        prior = parents[current]
        if prior:
            previous, removed, inserted = prior
            before = bags_from_forest(g, previous)
            record['exchange'] = {'removed': removed, 'inserted': inserted,
                                  'kind': 'internal tree pivot' if before == record['bags'] else 'ownership exchange',
                                  'old_parts': sorted(set(before) - set(record['bags'])),
                                  'new_parts': sorted(set(record['bags']) - set(before))}
        path.append(record)
        current = prior[0] if prior else None
    return {'depth_cap': depth_cap, 'found': found is not None,
            'checked_by_depth': checked, 'expanded_by_depth': expanded,
            'discovered_states': len(parents), 'trace': list(reversed(path)),
            'no_escape_within_bound': found is None}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary', action='store_true')
    args = parser.parse_args(argv)
    g = balanced_graph()
    initial = {edge(f'c{i}', f'{s}{i}') for i in range(6) for s in 'st' if (i, s) != (0, 't')}
    cases = [('balanced18', g, initial, 2, True),
             ('K7', nx.relabel_nodes(nx.complete_graph(7), str), set(), 0, True),
             ('square_C7', nx.relabel_nodes(nx.power(nx.cycle_graph(7), 2), str), set(), 0, False)]
    results = []
    for name, graph, forest, cap, expected in cases:
        result = search(graph, forest, cap)
        assert result['found'] == expected
        if name == 'balanced18':
            assert not result['trace'][0]['terminal'] and len(result['trace']) == 2
        else:
            assert list(exchanges(graph, frozenset())) == []
        results.append({'name': name, 'vertices': sorted(graph),
                        'edges': sorted(edge(*e) for e in graph.edges), **result})
    report = {'scope': 'Finite calibration only; full augmentation hypotheses not checked.',
                      'encoding': 'Seven spanning connected bags represented by n-7 forest edges.',
                      'moves': 'Delete one forest edge and insert one host edge. Defect may increase; internal tree pivots are legal.',
                      'trace_labels': 'Bag indices are local to each state; old_parts and new_parts identify ownership changes.',
                      'negative_scope': 'No escape means exhaustive search within the cap from the given forest, not from every tree representation.',
                      'summary': 'PASS: one-exchange balanced18 Q7 model and K7/square-C7 controls.',
                      'cases': results}
    print(report['summary'] if args.summary else json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
