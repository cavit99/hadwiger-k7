#!/usr/bin/env python3
"""Check the explicit 17-vertex selected-two-system/SCC barrier.

Dependency-free certificate checking only: no colouring, minor or treewidth
search. Run with `uv run python3 active/hc7_two_colouring_region_verify.py`.
This refutes the selected-pair sufficiency claim, not the critical-host case.
"""
from itertools import combinations


def require(condition, message):
    if not condition:
        raise AssertionError(message)


VERTICES = frozenset("u p a b x t s d1 d2 d3 d4 v1 v2 e1 e2 f q".split())
P = frozenset(("p", "a", "b"))
D = frozenset(f"d{i}" for i in range(1, 5))
B = frozenset(("p", "f", "q"))
W = frozenset(("a", "x", "b"))
EDGES = set()


def add_edge(v, w):
    require(v in VERTICES and w in VERTICES and v != w, "invalid edge")
    EDGES.add(frozenset((v, w)))


for clique in (P, D, W):
    for v, w in combinations(sorted(clique), 2):
        add_edge(v, w)
for v in P | D:
    add_edge("u", v)
for v, w in (("p", "x"), ("x", "s"), ("s", "d3"), ("s", "d4"),
             ("t", "d1"), ("t", "d2"), ("x", "q"), ("q", "d3"), ("q", "d4")):
    add_edge(v, w)
for i in (1, 2):
    for w in ("a", "b", "t"):
        add_edge(f"v{i}", w)
    for v, w in (("p", f"e{i}"), (f"e{i}", "f"), ("f", f"d{i}")):
        add_edge(v, w)
ADJ = {v: {w for w in VERTICES if frozenset((v, w)) in EDGES} for v in VERTICES}

phi = {"p": 6, "a": 5, "b": 4, "x": 3, "t": 5, "s": 5, "f": 6, "q": 6}
phi.update({f"d{i}": i for i in range(1, 5)})
phi.update({f"{prefix}{i}": i for prefix in ("v", "e") for i in (1, 2)})
psi = dict(phi, a=3, b=5, x=4)


def check_colouring(colouring, domain):
    require(set(colouring) == set(domain), "wrong colouring domain")
    require(all(1 <= c <= 6 for c in colouring.values()), "colour outside [6]")
    for edge in EDGES:
        v, w = tuple(edge)
        if v in domain and w in domain:
            require(colouring[v] != colouring[w], f"monochromatic edge {v}-{w}")


def check_path(path, colouring):
    require(len(path) == len(set(path)), "path repeats a vertex")
    require(all(frozenset((v, w)) in EDGES for v, w in zip(path, path[1:])), "missing path edge")
    palette = {colouring[path[0]], colouring[path[-1]]}
    require(len(palette) == 2, "equal endpoint colours")
    require(all(colouring[v] in palette for v in path), "path leaves endpoint colours")


require(len(VERTICES) == 17 and len(EDGES) == 39, "wrong graph size")
require(ADJ["u"] == P | D, "wrong literal neighbourhood")
require(all(frozenset((v, w)) in EDGES for clique in (P, D) for v, w in combinations(clique, 2)), "missing clique edge")
require(all(frozenset((v, w)) not in EDGES for v in P for w in D), "cross edge in neighbourhood")
side = {"a", "b", "v1", "v2"}
require(set().union(*(ADJ[v] for v in side)) - side == {"u", "p", "x", "t"}, "wrong four-cut")
for colouring in (phi, psi):
    check_colouring(colouring, VERTICES - {"u"})
    require({v for v, c in colouring.items() if c == 6} == B, "wrong sixth class")
    require(all(colouring[f"d{i}"] == i for i in range(1, 5)), "D not fixed")
require(tuple(phi[v] for v in ("p", "a", "b")) == (6, 5, 4), "wrong phi root state")
require(tuple(psi[v] for v in ("p", "a", "b")) == (6, 3, 5), "wrong psi root state")
require({v for v in phi if phi[v] != psi[v]} == W, "wrong disagreement support")

path_count = 0
for colouring, root, targets in ((phi, "a", (1, 2, 3)), (psi, "b", (1, 2, 4))):
    for i in targets:
        root_path = [root, f"v{i}", "t", f"d{i}"] if i in (1, 2) else [root, "x", "s", f"d{i}"]
        p_path = ["p", f"e{i}", "f", f"d{i}"] if i in (1, 2) else ["p", "x", "q", f"d{i}"]
        for path in (root_path, p_path):
            check_path(path, colouring)
            path_count += 1
require(path_count == 12, "wrong number of required paths")

# Build the whole transition digraph on G-u. Agreement vertices have no
# incoming or outgoing transition arcs; W induces the stated directed cycle.
arcs = {(v, w) for v in phi for w in ADJ[v] if w in phi and psi[v] == phi[w]}
require(arcs == {("a", "x"), ("x", "b"), ("b", "a")}, "wrong transition arcs")
for source in W:
    reached = {source}
    for _ in W:
        reached |= {w for v, w in arcs if v in reached}
    require(reached == W, "W not one strongly connected component")

# This fixed elimination trace is a width-five certificate: at each step
# complete the remaining neighbourhood to a clique, then delete the vertex.
trace = [
    ("e1", "f p"), ("e2", "f p"), ("f", "d1 d2 p"),
    ("q", "d3 d4 x"), ("s", "d3 d4 x"),
    ("d3", "d1 d2 d4 u x"), ("d4", "d1 d2 u x"),
    ("d1", "d2 p t u x"), ("d2", "p t u x"),
    ("p", "a b t u x"), ("u", "a b t x"),
    ("v1", "a b t"), ("v2", "a b t"),
    ("a", "b t x"), ("b", "t x"), ("t", "x"), ("x", ""),
]
filled = {v: set(neighbours) for v, neighbours in ADJ.items()}
maximum = 0
for v, expected in trace:
    require(v in filled and filled[v] == set(expected.split()), f"wrong elimination neighbourhood at {v}")
    neighbours = filled[v]
    maximum = max(maximum, len(neighbours))
    require(len(neighbours) <= 5, "elimination width exceeds five")
    for w in neighbours:
        filled[w].update(neighbours - {w})
        filled[w].remove(v)
    del filled[v]
require(not filled and maximum == 5, "incomplete width-five certificate")

extension = {"u": 5, "x": 5, "p": 6, "f": 6, "q": 6,
             "a": 1, "b": 2, "t": 3, "s": 1, "v1": 4, "v2": 4,
             "e1": 1, "e2": 2}
extension.update({f"d{i}": i for i in range(1, 5)})
check_colouring(extension, VERTICES)
require({v for v, c in extension.items() if c == 6} == B, "extension changes sixth class")
require(all(extension[f"d{i}"] == i for i in range(1, 5)), "extension changes D")

print("PASS: 17 vertices, 39 edges; literal K3 + K4 neighbourhood")
print("PASS: two proper root-normalized colourings; same whole sixth class {p,f,q}")
print("PASS: all 12 specified bichromatic paths; disagreement is exactly the SCC a -> x -> b -> a")
print("PASS: 17-step elimination certificate of width 5, hence no K7 minor")
print("PASS: explicit six-colouring of G retains the same sixth class and fixed D")
print("SCOPE: selected-two-system/SCC sufficiency fails; no critical-host counterexample")
