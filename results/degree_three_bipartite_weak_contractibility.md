# Bipartite schemes with degree at most three on one shore

**Status:** written proof with a separate internal audit at the exact
revision recorded beside this file. The conclusion preserves all
prescribed roots on the opposite shore. It does not assert
full rooted contractibility, and no novelty or significance comparable to
Norin--Totschnig is claimed.

All graphs are finite and simple. A target `H` has an injective root map
`rho:V(H)->V(G)`. An `H`-scheme consists of paths `P_uv`, one for every
`uv in E(H)`, joining `rho(u)` to `rho(v)` and containing no other root
internally. Whenever a collection of these paths has a common vertex,
its target edges have a common endpoint.

A model consists of pairwise disjoint nonempty connected sets `C_v`, with
an edge between `C_u,C_v` for every `uv in E(H)`. It is rooted on a set
`A subseteq V(H)` if `rho(a) in C_a` for every `a in A`. No prescribed
root containment is required for vertices outside `A`. A graph is weakly
contractible if every scheme of it contains an unrooted minor of it.

## 1. Moving one abstract root

### Lemma 1

Let an `H`-scheme with root map `rho` be given in `G`. Suppose
`x in V(G)-rho(V(H))` lies on every path corresponding to an edge
incident with a specified vertex `b in V(H)`, and lies on no other scheme
path. Define `rho'(b)=x` and `rho'(v)=rho(v)` for `v!=b`. Replacing each
`P_ba` by its subpath from `x` to `rho(a)` gives an `H`-scheme with root
map `rho'` in `G-rho(b)`.

### Proof

The new root map is injective. The unchanged paths avoid `x` by hypothesis.
Each replaced path contains `x` only as an endpoint and contains no other
root internally. It avoids `rho(b)` because it is a suffix of a simple
path oriented from `rho(b)` to its other endpoint. All unchanged paths
also avoid `rho(b)`, since an original root cannot be internal to any
scheme path. Intersections among the new paths are intersections among
the corresponding old paths, so the common-endpoint condition persists.
Thus all new paths lie in the stated vertex-deleted host. The abstract
target `H` is unchanged; only the image of its root `b` moves. QED

## 2. The two-membership packing input

A coloured scheme has a proper map `f:V(G)->V(H)` with
`f(rho(v))=v`, and each `P_uv` alternates colours `u,v`. Its nonroots
have degree at least four. In the underlying graph of a coloured scheme,
the paths are edge-disjoint and every nonroot lies on at least two scheme
paths [1, Definition 3.1 and Remark 3.2(1), (2), (6)].

### Lemma 2

Let `H` be bipartite with bipartition `(A,B)`, and suppose `G` is the
underlying graph of a coloured `H`-scheme. If every nonroot whose colour
lies in `B` belongs to exactly two scheme paths, then `G` contains an
`H`-minor rooted at all prescribed roots.

### Proof

Use [the audited packing lemma, Lemma 2.1](even_subdivision_contractibility.md#2-a-packing-lemma-with-partially-shared-labels).
Here labels are defined by actual path membership, not by all neighbours
of their target colour.

For `a in A`, put `W_a=f^{-1}(a)`. Its projected multigraph `M_a` has
vertex set `W_a`. Whenever a nonroot `x` of colour `b in B` occurs on
`P_ab`, replace its occurrence by an edge joining its two neighbours on
that path, labelled by the actual vertex `x`. Those neighbours are
distinct vertices of `W_a`. After all such replacements and removal of
the terminal root `rho(b)`, the path `P_ab` becomes a path `Q_ab` in
`M_a` containing `rho(a)`.

For fixed `a`, the paths `Q_ab` partition the edge labels of `M_a` and
cover its vertices. Every nonroot in `W_a` belongs to at least two of
these paths. Each label `x` occurs in precisely two projections, because
its two actual scheme paths have target edges with its colour `b` as
their common endpoint and with two distinct endpoints in `A`. Thus all
hypotheses of the audited packing lemma hold. It supplies spanning trees
whose sets of labels `T_a` are pairwise disjoint.

Set `C_a=W_a union T_a` and `C_b={rho(b)}`. A projected tree edge lifts
to the two-edge path through its label, so each `C_a` is connected.
These branch sets are disjoint and contain their prescribed roots. The
last edge of `P_ab` joins `rho(b)` to a vertex of `W_a`, supplying every
required adjacency. Isolated colours have only their root, and their
projection is the permitted one-vertex graph. QED

## 3. Degree three with every opposite-shore root preserved

### Theorem 3

Let `H` be bipartite with a specified bipartition `(A,B)` and
`d_H(b)<=3` for every `b in B`. Every `H`-scheme in every finite host
`G` contains an `H`-minor rooted on `A`.

Consequently every such target `H` is weakly contractible.

### Proof

First remove isolated target vertices and their prescribed host roots.
No scheme path contains these roots. Once a model for the remaining
target has been constructed in the remaining host, restore the isolated
vertices as their original singleton roots. If there are no target edges,
these singleton sets already suffice. We may therefore assume the target
has no isolated vertices.

For this fixed target and bipartition, use strong induction on the host
order. Kündgen--Pelsmajer--Ramamurthi [1, Lemma 3.3] give a
root-preserving minor `K` of `G` which is the underlying graph of a
coloured `H`-scheme. Relabel the current root images by an injective map
`rho_K`. We have `|V(K)|<=|V(G)|`. It is enough to construct the model
rooted on `A` in `K`: composing with the root-preserving minor model
recovers every original `A` root in `G`.

Suppose there is a nonroot `x` of colour `b in B` which belongs to every
path incident with `b`. Any path containing `x` has `b` as one of its
endpoint colours, so no other path contains `x`. Lemma 1 therefore gives
an `H`-scheme in `K-rho_K(b)`, with only the root of `b` moved to `x`.
Its host order is strictly smaller than `|V(G)|`. The induction hypothesis
supplies an `H`-minor rooted on `A` in that host, since none of those
root images changed. This is the required model in `K`.

It remains to consider the case with no such nonroot. Every nonroot of a
`B` colour lies on at least two paths. A degree-one colour has no such
vertex. A nonroot of a degree-two colour would belong to both incident
paths and would be in the preceding case; hence none remains. For a
degree-three colour, three memberships would likewise put the vertex in
the preceding case. Every remaining `B` nonroot therefore has exactly
two actual path memberships. Lemma 2 supplies a fully rooted model in
`K`, in particular one rooted on `A`.

These cases exhaust all coloured schemes. The only recursive step deletes
one current root from a host of order at most the original order, so the
induction is well-founded. Every lift preserves the required `A` roots.
This proves the theorem. QED

## 4. Reach and limits

Taking `A` to be the part of order three shows that every `K_{3,n}` is
weakly contractible, with its three prescribed `A` roots retained in the
model. More generally the theorem covers every bipartite target whose
degrees on one side are at most three, allowing arbitrary degrees on the
other side. This is an unbounded target class and includes one-subdivisions
of arbitrary graphs, so it has unbounded treewidth.

The roots in `B` may move during the induction. In particular, for
`K_{3,3}` the theorem retains either chosen shore of three roots, but
does not establish a model retaining all six prescribed roots. The
existing degree-two-side theorem remains stronger about roots in its
own target class.

A universal weak-to-rooted reduction does not upgrade this conclusion:
attaching many four-cycles at a `B` root raises its target degree beyond
three. The weak-contractibility input needed for that enlarged target is
not provided by Theorem 3. No conclusion about full bipartite
contractibility, T44, Conjecture 21 or `HC_7` is asserted.

This is an independent proof. Publication priority is unresolved:
Biswal--Lee--Rao's Lemma 3.2 claims a broader unrooted flow statement,
but the [audited prefix-construction counterexamples](../barriers/bipartite_flow_prefix_construction.md)
identify gaps in its supplied proof under its intended intersection
convention. That statement is not an input here. In [1], Theorem 5.3
proves weak contractibility of `K_{3,3}`; no claim that the present theorem
is the first proof of every included special case is intended.

## References

1. A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in graphs
   with a given path structure*, Journal of Graph Theory 79 (2015), 30--47,
   [primary preprint](https://arxiv.org/pdf/1207.6141),
   [DOI](https://doi.org/10.1002/jgt.21812). Definition 3.1, Remark 3.2,
   and Lemma 3.3 are the external inputs used above.
2. [Even subdivisions are contractible](even_subdivision_contractibility.md),
   Lemma 2.1, with its adjacent hash-pinned internal audits. Lemma 2 above
   is a written application to actual path memberships; it does not assume
   that the target colours themselves have degree two.
