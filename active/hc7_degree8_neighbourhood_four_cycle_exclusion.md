# No four-cycle in a surviving degree-eight neighbourhood

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. This is a critical-host reduction, not a proof of
Conjecture 19, Conjecture 21, or HC7.

All graphs are finite and simple. Put `Q=K_7^=`, with two independent
edges deleted, and call `K_4^-` a diamond.

**Theorem.** Let `G` be seven-connected, with `delta(G)>=8` and no
`Q` minor. If `d_G(v)=8` and `alpha(G[N(v)])<=3`, then `G[N(v)]`
contains no four-cycle.

## 1. Audited inputs

We use the following exact revisions, with their adjacent internal audits:

- [Connected-set contraction closure](hc7_companion_contraction_closure.md),
  SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`:
  under the theorem's connectivity, minimum-degree and exclusion
  hypotheses, contracting any nonempty connected set of at most three
  vertices gives a graph with no diamond joined to a universal vertex
  (that is, no literal `K_5^-`). This includes `G` itself.
- [Rooted-helper input](../results/hc7_k7minus_degree7_rooted_helper_closure.md),
  SHA-256 `6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`:
  Norin--Totschnig, Lemma 12, supplies a four-rooted two-helper model in
  an internally four-connected pair with at least `4n-9` edges.
- [Spanning helpers, Lemma 3](hc7_companion_helper_construction.md),
  SHA-256 `0c1ac8052f7734d8d0267381c030e177bd70010eded63d15fdca8c0db6d1f375`:
  in a five-connected graph, such a model can have its four prescribed
  roots singleton and its two connected, adjacent helpers partition all
  other vertices. Each helper contacts each root.

Write `q=e(G)-4|V(G)|`. Minimum degree eight gives
`q>=0` and `sum_w(d_G(w)-8)=2q`.

## 2. Retaining two actual adjacent vertices

**Lemma 1.** Suppose `z-a-b-c-z` is a four-cycle in `G[N(v)]` and
`|N_G(v) intersect N_G(z)|>=4`. Then `d_G(z)>=q+11`.

**Proof.** Suppose instead that `d_G(z)<=q+10`. The neighbourhood
`G[N(v)]` has no diamond, by the first input with no nontrivial
contraction. In particular `zb` is absent. Choose distinct common
neighbours `x,y` of `v,z` outside `{a,c}`. They are different from `b`,
and all six vertices `z,a,b,c,x,y` are distinct.

Put `F=G-{v,z}` and `Z={a,b,c,x}`. Deleting two actual vertices retains
five-connectivity, and the edge `vz` gives the exact count

`e(F)=e(G)-8-d_G(z)+1
      >=4|V(G)|-17=4|V(F)|-9`.

The two rooted inputs give adjacent connected helpers `U,V` partitioning
`V(F)-Z`, each contacting all four singleton roots. Interchange their
names so that `y` belongs to `V`. The seven bags

`{v}, {z}, {a}, {b}, {c}, U union {x}, V`

are disjoint and connected. The four bags `{v},{z},U union {x},V` are
pairwise adjacent: use `vz`, the old helper contact, the edges from
`v,z` to `x`, and their edges to `y`. All four contact each of `a,b,c`,
except possibly the pair `z,b`; the contacts of the enlarged helper
remain those of `U`. The path `a-b-c` supplies two root-root contacts.
Only `ac` and `zb` may be missing, and those pairs are independent.
Thus the bags give `Q`, a contradiction. QED

This construction gives the companion minor directly. It does not
assert the stronger intermediate five-rooted `K_5^-` with a full helper:
here the two possible omissions are among the five neighbour-rooted
bags, while the retained helper contains another neighbour `y` of `v`.

## 3. The eight-vertex neighbourhood argument

Put `H=G[N(v)]`. The contraction input implies that `H/C` has no diamond
for every nonempty connected `C` of order at most three: all its vertices,
including the merged vertex, remain adjacent to the untouched `v` in
`G/C`. Suppose `r_0r_1r_2r_3r_0` is a four-cycle of `H`, and let `X`
be the four remaining vertices. Indices below are modulo four.

Every vertex of `X` has at most one neighbour on the rim. Two adjacent
rim contacts give a house; contracting the opposite rim edge gives a
diamond. Two opposite contacts give a `K_{2,3}` subgraph, and contracting
one of its edges gives a diamond. Both contradict the same input.

Let `A_i` consist of the vertices of `X` whose unique rim neighbour is
`r_i`, and let `O` contain those with none. The opposite rim vertices
`r_1,r_3` are independent, so `alpha(H)<=3` forces
`A_0 union A_2 union O` to be a clique: a nonadjacent pair there would
extend the rim pair to an independent four-set. Likewise
`A_1 union A_3 union O` is a clique.

The classes `A_0,A_2` cannot both be nonempty. If `u in A_0` and
`w in A_2`, the forced edge `uw` makes `{r_0,u,w}` connected.
Contracting that triple retains the rim cycle and adds its diagonal to
`r_2`, giving a diamond. Similarly `A_1,A_3` cannot both be nonempty.
Thus at most two attachment classes are nonempty, at adjacent rim
vertices if there are two.

If `|O|>=2`, take two members of `O` and the other two vertices of `X`.
Each chosen member of `O` is adjacent to all three others, so these four
vertices contain a diamond. If `|O|=1`, the other three vertices lie in
at most two attachment classes; some `A_i` has at least two members.
Those two, the member of `O`, and `r_i` again contain a diamond.
Consequently `O` is empty.

Each `A_i` has at most two members, since it is a clique complete to
`r_i`, and three members would give a `K_4`. All four vertices of `X`
therefore form two classes of size two at distinct adjacent rim vertices.
Each of those rim vertices has four neighbours in `H`. Lemma 1 forces
both of their degrees in `G` to be at least `q+11`. They contribute at
least `2(q+3)>2q` to `sum_w(d_G(w)-8)=2q`, while every other contribution
is nonnegative. This contradiction proves the theorem. QED

## 4. Two spanning configurations

**Corollary 2.** Under the theorem's hypotheses, `H=G[N(v)]` contains
a spanning subgraph isomorphic to `2K_3` disjoint-union `K_2` or to
`C_5` disjoint-union `K_3`. In the latter case there is at most one edge
between the cycle and the triangle. This is a statement about spanning
subgraphs; additional edges are permitted in the first configuration.

**Proof.** The [audited triangle theorem](hc7_degree8_neighbourhood_triangle.md),
at SHA-256
`907384c665975c47f7850ee49da2d7f389802b077837c4285a3f00a81f5ef824`,
gives a triangle in `H`. The theorem above excludes four-cycles, and
the same connected-set contraction restriction remains available.

First suppose that `H` has disjoint triangles `A,B`, with remaining
vertices `x,y`. Each vertex outside either triangle has at most one
neighbour in it, since two contacts would give a diamond. Thus the edges
between `A,B` form a matching; two such edges would give a four-cycle,
so there is at most one.

If `xy` were absent, let `A_0,B_0` consist of triangle vertices missed
by both `x,y`. These sets are nonempty. Every pair in `A_0 times B_0`
must be adjacent, or it and `{x,y}` form an independent four-set.
There is at most one cross-edge, so `A_0={a_0}`, `B_0={b_0}`, and
`a_0b_0` is that edge. Relabel the other triangle vertices so that
`x` contacts `a_1,b_1` and `y` contacts `a_2,b_2`. Contract the connected
triple `{a_1,x,b_1}` to `w`. The four vertices `w,a_0,b_0,a_2` have the
five contacts `wa_0,wb_0,wa_2,a_0b_0,a_0a_2`, giving a diamond.
This contradiction proves `xy` is an edge, giving the first spanning
configuration.

Now suppose that no two triangles of `H` are disjoint. Fix a triangle
`T={t_1,t_2,t_3}` and put `J=H-T`. The five-vertex graph `J` is
triangle-free. Give each vertex of `J` its unique neighbour's label in
`T`, if it has such a neighbour, and otherwise leave it unlabelled.
An edge or a two-edge path in `J` cannot join vertices of distinct
nonzero labels: contracting its two or three vertices gives a vertex
adjacent to two vertices of `T`, and hence a diamond.

Suppose that `J` has an independent triple `I`. It must have one vertex
`x_i` of each label `i`: otherwise an omitted `t_i` extends it to an
independent four-set. Consider either of the two vertices outside `I`.
If it were unlabelled, at most one neighbour in `I` would leave two
nonneighbours which, together with it and the remaining `T` vertex,
form an independent four-set. But two neighbours in `I` would give the
forbidden two-edge path between distinct labels. Therefore both remaining
vertices are labelled. A remaining vertex of label `i` cannot contact
`x_j` for `j!=i`, and must contact `x_i`, or it extends `I` to an
independent four-set. If the two remaining labels differ, their two
edges to the corresponding `x_i`, together with their `T` roots, give
two disjoint triangles. If their labels agree, the two vertices, their
common `x_i`, and `t_i` give a diamond. Both are contradictions.

Consequently `alpha(J)<=2`. A triangle-free graph on five vertices
with independence number at most two is a five-cycle: its maximum degree
is at most two, since every neighbourhood is independent; a vertex of
degree at most one would extend a nonadjacent pair among its at least
three nonneighbours to an independent triple. Thus every degree is two.
This gives the second spanning configuration.

Finally, distinct nonzero labels cannot both occur on the five-cycle,
whose diameter is two, by the same path-contraction argument. A single
triangle vertex cannot contact two cycle vertices at distance two,
because that gives a four-cycle. If its two contacts are adjacent,
contract the three internal vertices of the other four-edge cycle arc;
the merged vertex, the two contacts and the triangle vertex form a
diamond. Thus there is at most one cycle--triangle cross-edge. QED

## 5. Remaining global obligation

The global construction must now handle these two spanning configurations
using actual critical-host neighbours and compatible root/helper ownership.
Neither configuration is asserted to occur in a critical counterexample,
and the corollary does not construct the requested global companion minor.
The five-neighbour construction, with flexible choices in the original
critical host, remains open. The stronger universal five-root theorem is
optional, not a necessary intermediate target.
