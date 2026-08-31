# Branch-model normal forms and a double-cone theorem for `K_7^-`

Status: the theorems in Sections 1--4 have complete proofs.  Section 5
records exact shortcut barriers.  These results materially constrain a
branch-set proof of the proposed `7`-connected `K_{4,4}` closure, but they do
not prove that closure, Conjecture 21, or `(HC_7)`.

Throughout, `K_7^-` is `K_7` with one edge deleted.  A branch set *meets* a
connected set when there is an edge between the two sets.

## 1. Two universal vertices force the target

### Theorem 1.1 (double-cone theorem)

Let `H` be a finite simple five-connected graph.  Add two new vertices `x,y`,
make each of them adjacent to every vertex of `H`, and choose the edge `xy`
arbitrarily (present or absent).  The resulting graph contains a `K_7^-`
minor.

### Proof

Choose a vertex `v` of `H` and five distinct neighbours

`q,r_1,r_2,r_3,r_4`.

The graph `H-{v,q}` is three-connected.  The universal four-root diamond
theorem in `rooted_k4minus_four_roots.md`, applied to
`r_1,r_2,r_3,r_4`, supplies four disjoint connected bags
`D_1,D_2,D_3,D_4`, with `r_i in D_i`, having at least five of their six
mutual contacts.  Thus

`{v},D_1,D_2,D_3,D_4`

is a `K_5^-` model in `H-q`: the bag `{v}` meets every `D_i` through the edge
`vr_i`.

Now take the seven bags

`{x}, {y,q}, {v}, D_1,D_2,D_3,D_4`.

They are disjoint and connected.  The first two bags meet through `xq`, so
the status of `xy` is irrelevant.  Each of the first two bags meets every one
of the last five because `x` and `y` are complete to `H`.  Among the last
five bags at most the single missing contact of the rooted diamond is absent.
Their quotient is therefore `K_7^-` or `K_7`.  QED

### Corollary 1.2 (dominating pair in a seven-connected graph)

If a seven-connected graph has two vertices each adjacent to every other
vertex, then it contains a `K_7^-` minor.

Indeed, deleting the two vertices leaves a five-connected graph, and
Theorem 1.1 applies.  This includes both `K_2 join H` and
`overline{K_2} join H` for every five-connected `H`.

The nonedge in `overline{K_2}` is not a barrier: absorbing `q` into one apex
bag creates the missing apex--apex contact.  Any argument that simply removes
the two apices and asks for a `K_5` minor overlooks this exchange.

### Corollary 1.3 (the boundary of an exact seven-cut is not five-connected)

Let `G` be seven-connected and `K_7^-`-minor-free, and let `S` be a
seven-vertex cut.  Then `G[S]` has no five-connected minor; in particular,
`G[S]` is not five-connected.

Every component of `G-S` is adjacent to every vertex of `S`.  Otherwise, if
`s in S` had no neighbour in a component `C`, then `S-{s}` would still
separate `C` from another component, contradicting seven-connectivity.
Contract two components of `G-S` separately to vertices `x,y` and delete all
other components.  The vertices `x,y` are anticomplete and each is complete
to `G[S]`.  If `G[S]` had a five-connected minor `H`, carry out that minor
inside `S`; the resulting graph contains `overline{K_2} join H`, which has a
`K_7^-` minor by Theorem 1.1.  This lifts to `G`, a contradiction.  QED

Combined with Theorem 4.2, every internal edge of a nonliteral minimal
`K_{4,4}` branch bag lies in an exact seven-cut whose seven-vertex boundary
has a secondary separation of order at most three.  This is a substantially
sharper interface than mere noncontractibility.

### Corollary 1.4 (dense exact-cut boundaries are impossible)

In fact every exact seven-cut `S` in a seven-connected target-free graph
satisfies

`delta(G[S])<=3`.

The stronger [seven-vertex double-cone
theorem](hc7_k44_fourconnected_seven_boundary_double_cone.md) proves that
every graph on seven vertices of minimum degree at least four either has a
`K_5` minor or is the pentagonal bipyramid, and closes the double cone in
both cases.  Contracting two components behind the cut gives that double
cone.  The separate [cold
audit](hc7_k44_fourconnected_seven_boundary_double_cone_audit.md) includes
an independent census of all 1,044 boundary graphs.

## 2. Apex and clique-sum candidate families

### Proposition 2.1 (no seven-connected apex graph)

No finite simple seven-connected graph is apex.

For if `G-a` is planar, then every vertex of `G-a` has degree at least six in
`G-a`, since it has degree at least seven in `G` and loses at most the edge to
`a`.  Every finite simple planar graph has a vertex of degree at most five, a
contradiction.  QED

### Proposition 2.2 (target-free seven-connected graphs are clique-sum prime)

Let `G` be seven-connected and `K_7^-`-minor-free.  There do not exist proper
subgraphs `G_1,G_2` with `G=G_1 union G_2`, no edge between
`V(G_1)-V(G_2)` and `V(G_2)-V(G_1)`, and `G_1 cap G_2` a clique.

The common vertex set is a separator, so seven-connectivity makes its order
at least seven.  But then it contains a literal `K_7`, a contradiction.  QED

Thus apex constructions and all nontrivial clique-sum/cockade constructions
are unavailable as counterexamples to the proposed seven-connected closure.
This does not exclude non-clique exact seven-sums.

## 3. A branch-set version of the two-component completion

### Lemma 3.1 (two near-full model bridges)

Let `G` contain a `K_{4,4}` model with branch sets

`A_1,A_2,A_3,A_4; B_1,B_2,B_3,B_4`.

Let `C,D` be disjoint connected sets outside all eight branch sets, with no
edge between `C` and `D`.  If each of `C,D` meets at least seven of the eight
branch sets, then `G` contains a `K_7^-` minor.

### Proof

At least six model branch sets meet both `C` and `D`; at least two of them lie
on each shore.  Choose a common branch set `A_a` and a common branch set
`B_b` as singleton model bags.  Pair the other three `A` branch sets with the
other three `B` branch sets.  A pairing can be chosen so that no paired bag
consists precisely of the branch set missed by `C` and the branch set missed
by `D`: there is at most one forbidden cross pair, and `K_{3,3}` has a perfect
matching avoiding one prescribed edge.

For each matched pair, take the union of its `A` and `B` branch sets and one
model edge between them.  Together with `A_a` and `B_b` these are five
disjoint connected, pairwise adjacent bags.  Every one contains a branch set
met by `C` and a branch set met by `D`.  Adding `C` and `D` gives seven bags
whose sole possible missing contact is `CD`.  QED

### Corollary 3.2 (support concentration)

Fix a `K_{4,4}` model in a seven-connected `K_7^-`-minor-free graph, and let
`M` be the union of its branch sets.  At most one component of `G-M` meets
seven or eight model branch sets.  Every other component has at least seven
distinct neighbours in `M` by seven-connectivity, but those neighbours are
concentrated in at most six branch sets.  In particular, some model branch
set contains at least two of its attachment vertices.

This is the exact point at which the literal-core proof ceases to apply:
connectivity counts attachment *vertices*, whereas the quotient completion
needs attachment *branch sets*.

## 4. Minimal branch models are saturated by exact seven-cuts

### Lemma 4.1 (contraction/cut equivalence)

Let `G` be `k`-connected and let `e=uv`.  After suppressing parallel edges,
`G/e` is not `k`-connected if and only if some `k`-vertex cut of `G` contains
both `u` and `v`.

For the forward direction, let `w` be the contracted vertex and let `T` be a
cut of `G/e` of order at most `k-1`.  If `w` is not in `T`, then `T` cuts
`G`, impossible.  Hence `w in T`, and

`(T-{w}) union {u,v}`

cuts `G`.  Its order is at most `k`; `k`-connectivity makes both inequalities
equalities.  The reverse direction follows by replacing `u,v` in the given
`k`-cut by `w`, producing a cut of order `k-1` in `G/e`.  QED

### Theorem 4.2 (minimal-counterexample branch normal form)

Assume a counterexample exists to

> every seven-connected graph with a `K_{4,4}` minor has a `K_7^-` minor,

and choose one with the fewest vertices.  Fix any `K_{4,4}` model in it.
Every edge internal to a nontrivial branch set is contained in an exact
seven-vertex cut of `G`.

Indeed, contracting such an edge preserves the displayed `K_{4,4}` model
and preserves target-freeness, since both properties are inherited in the
required directions under taking minors.  Minimality therefore says that
the contraction is not seven-connected.  Lemma 4.1 gives the exact cut.
QED

### Corollary 4.3 (eight-connected reduction to a literal model)

If the vertex-minimal counterexample in Theorem 4.2 is eight-connected, every
branch set of every `K_{4,4}` model in it is a singleton.  Contraction lowers
vertex connectivity by at most one, so contracting an internal edge would
leave a smaller seven-connected target-free graph with a `K_{4,4}` minor,
contrary to the minimality among all seven-connected counterexamples.

More carefully, this corollary is a reduction to the *seven-connected*
literal-core closure.  It is not by itself a proof for eight-connected
graphs, because that literal closure remains open.

Theorem 4.2 identifies the nonliteral residue precisely: a branch tree is
not merely complicated; every one of its internal edges carries an exact
order-seven separation certificate.  A valid global proof must either
reconstruct across those cuts or derive a target from two compatible cut
certificates.

### Lemma 4.4 (the first safe separator trace)

Let `Z` be an exact seven-cut in a seven-connected target-free graph, and
fix a `K_{4,4}` model `M`.  If `Z` meets at least seven branch sets of `M`,
then at most one component of `G-Z` is disjoint from the union of the model.

Every component of `G-Z` is full to `Z`.  If two components `C,D` were
disjoint from the whole model, then each would meet every branch set which
contains a vertex of `Z`.  The two components are connected, disjoint and
anticomplete, so seven traced branch sets would satisfy Lemma 3.1 and force
the target.  QED

A branch set avoiding `Z` lies wholly in one component of `G-Z`.  Two such
bags on opposite shores lie in the same component, because their model edge
also avoids `Z`.  Nothing here bounds the number of traced bags: a component
which contains part of a branch bag is not an exterior model bridge, and its
adjacency to a cut vertex in that bag cannot be counted as a new external
contact.  In particular, Lemma 4.4 does not justify a `six`-trace bound or a
peel.

## 5. Exact shortcut barriers

### 5.1 One fat triangle on a shore is insufficient

For positive integers `a,b,c` with
`a+b+c=7`, form the graph consisting of a literal `K_{4,4}` and an
`F_{a,b,c}` fat triangle rooted at three vertices of one shore, with every
fat-triangle path subdivided exactly once and with no other edges.

`../barriers/hc7_k44_fat_triangle_certificate_barrier_verify.c` exhausts
all fifteen ordered profiles.  No
one of the fifteen graphs contains a `K_7^-` minor.  The densest seven-bag
quotient has only 18 of the required 20 contacts.  Depending on the profile,
the program checks between `4,770,608` and `4,823,168` spanning forests.

The enumeration is complete.  In a connected graph, unused components of
any minor model can be absorbed into adjacent branch sets, so a model may be
assumed spanning.  A spanning seven-bag model on `n` vertices has a spanning
forest of exactly `n-7` edges inside its bags.  The program enumerates every
such edge set and tests the quotient.

Consequently the fat-triangle theorem for seven-connected graphs cannot by
itself complete the literal `K_{4,4}` route.  The rest of the host and its
attachments to the linkage paths must be used.

### 5.2 Alternate paths across one split edge are insufficient

Split one shore vertex of `K_{4,4}` into adjacent vertices `s,t`, distributing
its four opposite-shore contacts as `1+3`, `2+2`, or `3+1`.  Add from one to
six internally disjoint length-two `s-t` paths and no other edges.

`../barriers/hc7_k44_one_split_theta_certificate_barrier_verify.c` exhausts
every seven-bag minor model in
all eighteen graphs.  None contains `K_7^-`; the maximum quotient density is
15.  Thus even the six alternate paths supplied abstractly by Menger across
a split edge do not repair a nonliteral model.  Seven-connectivity must be
used through additional attachments of those path interiors, not solely
through their existence.

These barrier graphs are not seven-connected (their new internal vertices
have degree two).  They refute the proposed *certificate implications*, not
the global seven-connected theorem.

The promoted source and verifier hashes are pinned in
`hc7_k44_closure_local_normal_forms_audit.md`.

## 6. Exact remaining global obligation

The results leave two genuinely different interfaces.

1. **Literal interface.**  The audited exterior theorem makes the exterior
   three-connected.  One still needs a core-sensitive trichotomy producing
   a portal-rich spanning `K_4`, a rich triangle, or a direct target.
2. **Nonliteral interface.**  Theorem 4.2 supplies an exact seven-cut through
   every internal branch edge.  One needs a reconstruction theorem across
   those cuts, or a proof that two compatible certificates force the two
   near-full model bridges of Lemma 3.1.

Neither a single kite, a single fat triangle, nor a pure theta across one
split edge supplies the missing compatibility.
