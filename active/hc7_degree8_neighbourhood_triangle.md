# A triangle in every surviving degree-eight neighbourhood

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash.
This is a local consequence for the global companion-minor campaign,
not a proof of a six-colouring conjecture.

Write `Q=K_7^=` for `K_7` with two independent edges deleted. A diamond
is `K_4^-`. Graphs are finite and simple; all contractions take their
simple quotient.

## 1. The eight-vertex lemma

**Lemma 1.** If `H` is a triangle-free graph on eight vertices with
`alpha(H)<=3`, there is a nonempty connected set `C` of at most three
vertices such that `H/C` contains a diamond subgraph.

**Proof.** Suppose otherwise. In particular `H` contains no `K_{2,3}`:
contracting one edge of that subgraph gives a diamond.

Every neighbourhood is independent, so `Delta(H)<=3`. Every triangle-free
graph on six vertices has an independent three-set: a vertex of degree
at least three supplies one in its neighbourhood; otherwise a vertex
has at least three nonneighbours, two of which are nonadjacent, and those
two together with the vertex suffice. Thus a vertex of `H` of degree at
most one would extend an independent three-set among its nonneighbours
to an independent four-set. Therefore `delta(H)>=2`.

First suppose `t` has degree two, with neighbours `a,b`. The remaining
five vertices `W` induce a triangle-free graph with independence number
at most two, since `t` misses all of them. This graph is a five-cycle:
its maximum degree is at most two, while a vertex of degree at most one
could be extended by two nonadjacent nonneighbours to an independent
three-set; hence it is two-regular and triangle-free on five vertices.

The vertices `a,b` are independent. Consequently the vertices of `W`
missed by both form a clique, of size at most two. If exactly two are
missed they are consecutive on the cycle, so the three covered vertices
are consecutive. If at most one is missed, the covered vertices also
contain three consecutive cycle vertices. Contract the connected triple
`{a,t,b}`. Its merged vertex contacts those three consecutive vertices;
their two cycle edges give a diamond in the quotient, a contradiction.

It remains that `H` is cubic. It contains a four-cycle: otherwise a vertex,
its three neighbours and their six other neighbours would be ten distinct
vertices, since neither triangles nor four-cycles are present. Write a
four-cycle as `a,b,c,d,a`. Each cycle vertex has one outside neighbour,
denoted respectively `A,B,C,D`. Adjacent cycle vertices cannot share an
outside neighbour because `H` is triangle-free. Opposite ones cannot
share one because that would give a `K_{2,3}` with their two cycle
neighbours. Thus `A,B,C,D` are the four distinct outside vertices.

Cubic degree implies that `a,c` have no edges to `B,D`. Since `a,c`
are nonadjacent, `alpha(H)<=3` forces the edge `BD`. Contract the connected
triple `{a,b,B}` to `w`. The four distinct vertices `w,c,d,D` have the
five contacts

`wc, wd, wD, cd, dD`,

using respectively `bc, ad, BD, cd, dD` of `H`. They span a diamond,
again a contradiction. QED

## 2. The critical-host application and its exact lift

**Corollary 2.** Let `G` be seven-connected, `delta(G)>=8`, and
`Q`-minor-free. If `d_G(v)=8` and `alpha(G[N(v)])<=3`, then `N(v)`
contains a triangle. In particular `v` belongs to a literal `K_4`.

**Proof.** Use Corollary 6 of the
[connected-set contraction closure](hc7_companion_contraction_closure.md),
at SHA-256
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`:
under these hypotheses, every connected set of order at most three
contracts to a `K_5^-`-subgraph-free graph. If `H=G[N(v)]` were
triangle-free, Lemma 1 would supply a connected set `C subseteq N(v)`
of order at most three and a diamond in `H/C`. This is an actual
contraction in `G`, disjoint from `v`. Each quotient vertex of `H/C`
remains adjacent to `v`, including the merged vertex. The diamond and
`v` therefore give a literal `K_5^-` in `G/C`, a contradiction. QED

For a seven-connected seven-contraction-critical companion-minor-free host the previously
[audited critical reductions](hc7_companion_helper_construction.md#1-audited-input-and-the-missing-edge-extension)
supply minimum degree eight and the stated neighbourhood independence
bound.
The argument above adds the triangle conclusion without finite enumeration.
It does not construct the remaining global minor from that four-clique,
retain criticality in the contracted quotient, or close the global target.
