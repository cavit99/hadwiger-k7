# Independent-set reduction for general graph schemes

**Status:** written proofs with a separate internal audit at the exact
source hash recorded beside this file. The terminal pseudoforest theorem
and reduction lemma have their explicit hypotheses below. The broader
classification conjecture remains open. Neither this result nor additional
structure of a hypothetical counterexample completes the user's global
objective. Current status is governed by the
[research ledger](../RESEARCH_LEDGER.md).

All graphs are finite and simple; projection graphs may have parallel
edges. An `H`-scheme has the meaning in the
[audited bipartite theorem](bipartite_contractibility_via_matroid_reduction.md).
Write `rho(v)` for the prescribed root of target vertex `v`, and `R` for
the set of prescribed roots. A **properly coloured scheme** here means
that its underlying graph has a proper map `f:V(G)->V(H)`, with
`f(rho(v))=v`, and every scheme path uses only its endpoint colours.
This term does not impose a minimum degree on nonroots.

## 1. Projection from an independent set of host vertices

Let a properly coloured `H`-scheme be given, with no assumption that `H`
is bipartite. Delete unused host vertices and edges, retaining isolated
roots. Put `J=G-R`. Let `T` be a nonempty independent set in `J`.

For every target vertex `v`, form a multigraph `M_v` on

`W_v = f^{-1}(v)-T`.

Whenever `x in T` occurs on a scheme path whose other endpoint colour
is `v`, insert an edge labelled `x` between the two neighbours of `x`
on that path. Those neighbours are outside `T` by independence, have
colour `v`, and are distinct. A label appears at most once in `M_v`:
the colour of `x` determines the other target endpoint, and there is
only one path for each target edge. Every element of `T` is a nonloop
edge in at least one projection. Projections may be disconnected.

Regard the graphic matroids as matroids on the common ground set `T`,
with absent labels declared loops, and denote their ranks by `r_v`.
Every nonroot vertex incident with a projected edge belongs to `N_J(T)`.
The projection contains its own root even when that root is isolated.
Consequently

`sum_v r_v(T) <= |N_J(T)|`.                                      (1)

Indeed, in a colour class with `k` nonroot neighbours of `T`, all other
nonroot vertices of the projection are isolated, and the graph on those
`k` neighbours and its root has rank at most `k`.

### Lemma 1: a root-preserving decreasing reduction

Suppose `T` is a nonempty independent set of host nonroots and

`sum_v r_v(T) <= |T|`.                                         (2)

Then `G` has a root-preserving minor of strictly smaller order containing
a properly coloured `H`-scheme. In particular, this conclusion holds if

`|N_J(T)| <= |T|`.                                             (3)

**Proof.** Let `q` be the maximum total size of pairwise disjoint
projection forests `I_v`. The matroid union formula and its equality
consequence are [Lemma 1 of the audited theorem](bipartite_contractibility_via_matroid_reduction.md#1-a-consequence-of-the-matroid-union-rank-formula).

If `q<|T|`, choose a minimizing set `X subseteq T`. Its expression is
`|T-X|+sum_v r_v(X)=q`; hence `X` is nonempty. The forests
`F_v=I_v cap X` span every component of `M_v(X)` simultaneously.
If `q=|T|`, condition (2) forces `q=sum_v r_v(T)`, so take `X=T`
and `F_v=I_v`. Again every component is spanned simultaneously.
These two cases exhaust the possibilities because `q<=|T|`.

For each component `K` of `M_v(X)`, take

`D_(v,K) = V(K) union {x in F_v: its projected edge belongs to K}`.

This set is connected in the actual host: its allocated forest edges
lift to two-edge paths through their actual labels. The sets are
pairwise disjoint. Their base vertices partition `V(G)-T` by colour
and component, and their added labels lie in `T` and are allocated
at most once. Each contains at most one prescribed root; it can contain
only the root of its base colour. No root belongs to `T`.

Contract these sets, delete the unallocated vertices of `X`, and retain
every vertex of `T-X` separately. Colour a component vertex by its base
colour, and colour each retained vertex of `T-X` by its original colour.
Retain the images of original edges whose endpoints both avoid `X`.
Such an edge either has both endpoints in `V(G)-T`, or one endpoint
there and the other in `T-X`. Its endpoint colours are distinct, so its
image remains a properly coloured edge. Edges incident with labels
allocated to the wrong component can be deleted; none is required by
the following construction.

Traverse an original scheme path. If a vertex `x in X` occurs, both
neighbours lie outside `T`, in the same component of the projection
for their colour. Thus deleting that occurrence identifies its two
neighbours. This identification is realized by the tree allocated to
that component, whether or not `x` itself was allocated there. It never
requires a label owned by another component. Every step not using `X`
maps to one of the retained actual edges. The resulting sequence,
with consecutive repeated vertices suppressed, is a walk between the
two required root images and uses only their two endpoint colours.

Erase closed excursions. The resulting path contains no other root
internally: all other roots have other colours, and its terminal root
images are distinct. Any collection of resulting paths meeting at a
vertex shares its colour as a target endpoint. Hence they form a
properly coloured `H`-scheme. The replacement walks before contraction
are not asserted to form a scheme.

The quotient map is injective on roots and specifies disjoint connected
preimages. A rooted model in the quotient therefore lifts by replacing
each vertex by its preimage, preserving all roots, connectivity,
disjointness and target contacts.

Finally, `X` is nonempty and every label in `X` is a nonloop in some
projection. The total rank on `X` is positive. At least one allocated
edge contracts its two distinct base vertices and its label, so the
host order strictly decreases. Condition (3) implies (2) by (1). QED

The new ingredient relative to the bipartite theorem is that label
vertices are removed from **all** projection vertex sets. A vertex is
therefore never both an allocated label and an independently owned base
vertex. Independence of `T` guarantees that each required pair of
neighbours remains available as base vertices.

## 2. Exact necessary condition in a minimal counterexample

### Corollary 2

Fix a target graph `H`. Suppose `G` has minimum order among underlying
properly coloured `H`-schemes with no prescribed rooted `H` minor. Put
`J=G-R`. Then every nonempty independent set `T` in `J` satisfies

`|N_J(T)| > |T|`.                                             (4)

In particular, if `J` is nonempty then `delta(J)>=2`,
`alpha(J)<|V(J)|/2`, and no component of `J` is bipartite.

**Proof.** A violation of (4) invokes Lemma 1 and gives a smaller
properly coloured scheme of the same target, with every root preserved.
A model there would lift to `G`, contradicting minimality. The degree
bound follows by taking a singleton. For an independent set `T`, its
neighbourhood is contained in `V(J)-T`, giving the independence bound.
A larger shore of a bipartite component would violate (4). QED

An ordinary counterexample, if one exists, can be normalized to a
properly coloured one by the root-preserving normalization in the audited
theorem. Thus considering the above minimum does not change the rooted
contractibility question. The conclusion is a necessary condition on
a hypothetical counterexample, not a classification or a terminal
positive result for a new target class.

No equivalence with fractional perfect matchings is used here. Such an
equivalence would need its own exact cited statement or proof.

## 3. A terminal host theorem: a pseudoforest outside the roots

A **pseudoforest** is a graph whose every connected component contains
at most one cycle.

### Theorem 3

Let `H` be any finite simple graph. If an `H`-scheme in a finite host
`G` has prescribed root set `R` and `G-R` is a pseudoforest, then `G`
contains an `H` minor rooted at every prescribed root.

**Proof.** A root-preserving minor preserves the condition on the
nonroot graph. Indeed, the connected preimage of every nonroot quotient
vertex avoids all prescribed original roots. After removing the quotient
roots, these preimages give a minor model entirely in `G-R`.
Pseudoforests are minor-closed: deleting edges or vertices and contracting
edges cannot create two cycles in one component of a pseudoforest.

Apply Kündgen--Pelsmajer--Ramamurthi [1, Lemma 3.3] to obtain the
underlying graph of a coloured scheme in a root-preserving minor, in
which every nonroot lies on at least two paths. This is the stronger
normalization of [1, Definition 3.1 and Remark 3.2], not merely the
proper colouring used in Lemma 1. Isolated roots can be removed first
and restored at the end. The new nonroot graph is still a pseudoforest.
We work in this normalized host.

Let `x` be a nonroot used by `s>=2` paths. Each such path gives two
distinct neighbours of `x`, both of its opposite endpoint colour. At
most one of those neighbours is a prescribed root: there is only one
root of that colour, and no other root can occur internally. Thus each
path gives at least one nonroot neighbour. The paths are edge-disjoint
by [1, Remark 3.2(2)], so the nonroot degree of `x` is at least `s>=2`.

A finite pseudoforest with minimum degree at least two consists of
cycles. Hence every nonroot has exactly two nonroot neighbours. Equality
in the preceding count forces `s=2`, and each of its two scheme paths
gives exactly one nonroot and one root neighbour. Its two nonroot
neighbours have different colours, because the two target edges using
`x` have different opposite endpoints in the simple target graph.

Orient each nonroot cycle cyclically. Write its vertices as
`x_0,...,x_(k-1)` and their colours as `v_0,...,v_(k-1)`, with indices
modulo `k`. The preceding paragraph shows that `x_i` is adjacent to
the prescribed root of each of `v_(i-1),v_(i+1)`. Assign `x_i` to the
branch set of `v_(i-1)`. For every target vertex `v`, let `C_v` consist
of its prescribed root and all vertices assigned to it. These sets
are disjoint connected stars, allowing a singleton star.

It remains to check all contacts, including repeated colours on a cycle.
A scheme path using any nonroot edge `x_i x_(i+1)` is exactly

`rho(v_(i+1)), x_i, x_(i+1), rho(v_i)`.

At either nonroot, the corresponding path has a root as its other
neighbour. Thus every scheme path is either a literal root-to-root
edge or one of these paths of length three. For the target edge
`v_i v_(i+1)`, the next cycle edge `x_(i+1) x_(i+2)` joins `C_(v_i)`
to `C_(v_(i+1))`. The two colours are distinct. Each nonliteral demand
is therefore realized, even if a target colour occurs on several
cycles or more than once on one cycle. Literal root-to-root edges
remain available because every branch contains its root.

These stars give the required rooted model in the normalized host.
Lifting its root-preserving minor model gives the rooted model in the
original host. QED

This is a terminal theorem for arbitrary target graphs under a host
hypothesis. It does not assert contractibility of all target graphs.
It does not follow merely from the raw host being bipartite: bipartiteness
is not preserved by the normalization, whereas the pseudoforest
condition on the graph outside the prescribed roots is preserved.

## 4. Classification route and first missing inference

**Conjectural target, not established here:** a graph is contractible
if and only if every one of its subgraphs is `M'`-contractible, where
`M'(F)` is the two-copy graph of [1, Definition 7.2]. Necessity follows
from subgraph closure of contractibility and the canonical scheme in
`M'(F)`. Sufficiency would go far beyond these results.

The first missing inference is to turn an arbitrary minimal coloured
scheme satisfying (4) into a one-copy-per-colour scheme for a subgraph
of its target, or into a valid simultaneous root rotation. Strict
independent-neighbour expansion alone supplies neither a bounded host
order nor such a rotation. In particular, it does not force exactly
one nonroot of each colour, prescribe a shift automorphism, or justify
identifying multiple vertices of the same colour.

For complete targets, their only independent target sets are singletons.
Projecting from one complete target colour produces a family of paths
whose ranks simply count label memberships; every normalized nonroot
has at least two memberships. Thus choosing independent **target**
sets alone never gives the required descent there. Lemma 1 enlarges
the choices to independent host sets, but its strict-expansion residue
is still unclosed. Full rooted `K_5` and `K_6` contractibility do not
follow, and no significance comparison with Norin--Totschnig is claimed.

## Reference

[1] A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in
graphs with a given path structure*, Journal of Graph Theory 79 (2015),
30--47, [primary preprint](https://arxiv.org/pdf/1207.6141),
[DOI](https://doi.org/10.1002/jgt.21812). Definitions 3.1 and 7.2,
Remark 3.2, Lemma 3.3, and Section 8 give the exact external terminology,
normalization and open-question context used here.
