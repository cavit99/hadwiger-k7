"""Diagnostic exact-six r=3 arithmetic screen using only valid inequalities."""

from itertools import combinations

import networkx as nx
import z3


V = range(6)


def e_without(edges, omitted):
    return sum(not (set(edge) & set(omitted)) for edge in edges)


def admissible(edges, deg):
    return len(edges) <= 8 and max(deg) <= 3 and all(
        e_without(edges, set(V) - set(q)) <= 4 for q in combinations(V, 4)
    )


def lobe(sol, tag, edges, deg):
    c = z3.Int(f"c_{tag}")
    e = z3.Int(f"e_{tag}")
    p = [z3.Int(f"p_{tag}_{s}") for s in V]
    delta = e + z3.Sum(p) - 4 * c
    sol.add(c >= 1, e >= c - 1, e >= 0)
    sol.add(2 * e <= c * (c - 1))
    sol.add(2 * e + z3.Sum(p) >= 7 * c)
    for ps in p:
        sol.add(ps >= 1, ps <= c)
    # Rooted K4 exclusions from the audited ordered-nonedge construction.
    for q in V:
        if deg[q] != 3:
            continue
        for omitted in V:
            if omitted == q or tuple(sorted((q, omitted))) in edges:
                continue
            sol.add(
                e + z3.Sum(p) - p[q] - p[omitted]
                + e_without(edges, {q, omitted}) <= 3 * c + 5
            )
    return c, e, p, delta


def main():
    checked = 0
    survivors = []
    for G in nx.graph_atlas_g():
        if len(G) != 6:
            continue
        edges = {tuple(sorted(x)) for x in G.edges()}
        deg = [G.degree(v) for v in V]
        if not admissible(edges, deg):
            continue
        checked += 1
        sol = z3.Solver()
        lobes = [lobe(sol, f"{checked}_{i}", edges, deg) for i in range(3)]
        sol.add(z3.Sum([x[3] for x in lobes]) == 22 - len(edges))
        # Boundary vertices have degree at least seven.
        for s in V:
            sol.add(z3.Sum([x[2][s] for x in lobes]) + deg[s] >= 7)
        # Generalised Lemma 5: the unused third full component replaces the
        # degree-six singleton in the one-terminal cross-lobe composition.
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                di, pi = lobes[i][3], lobes[i][2]
                dj = lobes[j][3]
                for p in V:
                    for q in V:
                        if p == q:
                            continue
                        local = deg[q] - int(tuple(sorted((p, q))) in edges)
                        helper = di - pi[p] + local >= 5
                        clique = dj + len(edges) - deg[q] >= 9
                        sol.add(z3.Not(z3.And(helper, clique)))
        if sol.check() == z3.sat:
            m = sol.model()
            data = []
            for c, e, p, d in lobes:
                data.append((m.eval(c), m.eval(e), tuple(m.eval(x) for x in p), m.eval(d)))
            survivors.append((sorted(edges), deg, data))
            print("SAT", sorted(edges), deg, data)
    print("checked", checked, "survivors", len(survivors))


if __name__ == "__main__":
    main()
