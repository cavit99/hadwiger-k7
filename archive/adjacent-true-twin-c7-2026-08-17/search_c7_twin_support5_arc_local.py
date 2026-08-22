#!/usr/bin/env python3
"""Exact MILP falsification of the arc-local C7 support-five split.

For a fixed exterior graph D, seek seven portal neighbourhoods A_0,...,A_6
which satisfy all currently proved target-free constraints:

* every portal has at least four neighbours in D;
* every exterior vertex sees at most three portals and no two of them are
  at cyclic distance three (equivalently its support lies in a three-vertex
  arc of C7);
* d_D(v)+w(v)>=8;
* |N_D(X)|+w(X)>=7 for every nonempty connected proper X;

but no connected bipartition has support at least five on both shores.
An answer is only a weighted-interface counterexample, not automatically a
literal target-free host.  Infeasibility is bounded evidence only.
"""

import sys

from milp_twin_pole_bipartition_support2 import Model
from milp_twin_pole_bipartition_counterexample import connected


def cyclic_distance(i, j):
    d = abs(i-j)
    return min(d, 7-d)


def search(adj, time_limit=120):
    n = len(adj)
    full = (1 << n) - 1
    model = Model()
    x = [[model.var(("x", t, v)) for v in range(n)] for t in range(7)]

    # Literal portal degrees and the target-free arc-local vertex profiles.
    for t in range(7):
        model.row({x[t][v]: 1 for v in range(n)}, lo=4)
    for v in range(n):
        model.row({x[t][v]: 1 for t in range(7)}, lo=max(0, 8-adj[v].bit_count()), hi=3)
        for i in range(7):
            for j in range(i+1, 7):
                if cyclic_distance(i, j) == 3:
                    model.row({x[i][v]: 1, x[j][v]: 1}, hi=1)

    subsets = [s for s in range(1, full + 1) if connected(s, adj)]
    hit = {}
    for s in subsets:
        vs = [v for v in range(n) if s >> v & 1]
        for t in range(7):
            h = model.var(("hit", s, t))
            hit[s, t] = h
            for v in vs:
                model.row({h: 1, x[t][v]: -1}, lo=0)
            terms = {h: 1}
            terms.update({x[t][v]: -1 for v in vs})
            model.row(terms, hi=0)
        if s != full:
            outside = 0
            for v in vs:
                outside |= adj[v] & ~s
            model.row({hit[s, t]: 1 for t in range(7)},
                      lo=7-outside.bit_count())

    good = {}
    for s in subsets:
        g = model.var(("good5", s))
        good[s] = g
        terms = {hit[s, t]: 1 for t in range(7)}
        terms[g] = -5
        model.row(terms, lo=0)
        terms = {hit[s, t]: 1 for t in range(7)}
        terms[g] = -3
        model.row(terms, hi=4)
    for s in subsets:
        other = full ^ s
        if s < other and connected(other, adj):
            model.row({good[s]: 1, good[other]: 1}, hi=1)

    ans = model.solve(time_limit=time_limit)
    if not ans.success:
        return None, ans.message
    masks = [sum(1 << v for v in range(n) if ans.x[x[t][v]] > .5)
             for t in range(7)]
    return masks, ans.message


def complete(n):
    return [((1 << n)-1) ^ (1 << v) for v in range(n)]


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    print(search(complete(n)))
