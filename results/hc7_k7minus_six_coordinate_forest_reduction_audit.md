# Internal audit: six-coordinate induced-forest reduction

**Verdict:** GREEN for Theorems 2.1--2.3, Corollary 2.1A, Theorem 3.1,
Corollaries 3.2--3.3, Theorem 4.1, and the stated trust boundary.  This is a
separate internal mathematical audit, not external peer review.

## 1. Exact revision and inputs

The audited source is
[`hc7_k7minus_six_coordinate_forest_reduction.md`](hc7_k7minus_six_coordinate_forest_reduction.md),
with SHA-256

```text
cc2b56362d52a3ef23559a4a0e5cbf5eded5abbe7d54b57e73f66f74f1dd3405
```

The source was promoted from `active/` after the original audit.  Corollary
2.1A was added later and cold-audited at the hash above; it composes the
existing audited inputs and changes none of the earlier theorem statements.

The five alternatives come from the separately audited replacement-abundance
draft.  Thus `M_0` is a matching of order four, every edge of `A^*` is
disjoint from `V(M_0)`, and every graph
`G-(M_0 union {a})`, for `a in A^*`, is seven-connected.  The critical-host
inputs include minimum degree eight, at least `4|V(G)|` edges, no literal
`K_5`, no `K_7^-` minor, and order at least twenty-five.

## 2. The six-coordinate host

If two alternatives are disjoint, adjoining them to `M_0` gives a matching
of order six.  Otherwise the five distinct alternatives are pairwise
intersecting.  A pairwise-intersecting family of at least four edges in a
simple graph is a star, because the only non-star possibility is contained
in a triangle.  Two of the five leaves are nonadjacent by literal
`K_5`-exclusion, and their two star edges induce a three-vertex path.
Thus the selected six-edge forest is componentwise induced in both cases.

For the selected edges `a,b`, the identities

```text
X+a = G-(M_0 union {b}),
X+b = G-(M_0 union {a})
```

are exact.  Both completions are seven-connected, so deleting one edge
leaves `X` six-connected.  Deleting the six distinct forest edges gives the
stated density.

For every nonempty `J subseteq F`, a six-colouring of the proper minor
`G/J` expands to `X=G-F`.  A forest edge outside `J` cannot collapse, and
componentwise inducedness excludes any collapsed edge of `G-F`.  Hence the
expanded colouring has signature exactly `J`; an empty signature would
six-colour `G`.  This proves the full punctured `63`-signature cube.

Norin--Totschnig, Theorem 6, supplies the spanning `K_7^vee` model.  If
either nominally missing pair became adjacent when `F` was restored, the
same bags would give `K_7^-`.  The model is consequently exact in a
target-free `G`.

Corollary 2.1A is the direct composition of the audited removable-matching
and replacement-abundance theorems with Theorem 2.1.  More explicitly, let
`M={e_1,...,e_5}` be the removable matching, choose the coordinate `e_i`
and four distinct replacements `A` supplied by replacement abundance, and
put `M_0=M-{e_i}` and `A^*=A union {e_i}`.  The original matching makes
`e_i` disjoint from `V(M_0)`.  Every replacement lies in `G-M` on
`R union V(e_i)`, so it is also disjoint from `V(M_0)`; the five edges are
distinct because `e_i` is absent from `G-M`.  Deleting
`M_0 union {e_i}` gives the original seven-connected host, while deleting
`M_0 union {a}` is seven-connected by the definition of a replacement.
Thus all hypotheses (1.2) hold and Theorem 2.1 applies.  The corollary now
states minor-minimal non-six-colourability explicitly, rather than relying
on that assumption from the prose preceding (1.1).

## 3. One simultaneous cycle

In the matching case, Haggkvist--Thomassen applies directly to the six
independent forest edges in the seven-connected graph `G`.

In the induced-path case, deleting its common vertex `r` leaves a
six-connected graph.  Adding the artificial edge between the two path
leaves preserves connectivity.  That edge and the four edges of `M_0` are
five independent edges, so they lie on one cycle.  Replacing the artificial
edge by the two-edge path through `r` produces a simple cycle of `G`
containing all six coordinates.  Removing the six displayed edges gives
six disjoint connected pieces, one of which is the singleton `r` in the
path case.

For Theorem 2.3, a seven-fan from a prescribed vertex to seven distinct
points of the cycle divides it into seven edge-disjoint cyclic intervals.
At most six intervals contain a distinguished forest edge.  Replacing an
empty interval by its two fan paths gives a cycle through the prescribed
vertex and all six coordinates.  This argument inserts one prescribed
vertex only; the source correctly declines the corresponding simultaneous
multi-portal conclusion.

## 4. Exact order-six cuts

Let `S` be a six-cut of `X`.  Since `X+a-S` is connected, the single edge
`a` joins exactly two components of `X-S`; applying the same argument to
`b` proves that both selected edges cross the same two-component split.
Six-connectivity makes both components adjacent to every vertex of `S`.

The two full components are adjacent in `G` through either restorer.  A
`K_5^-` model in `G[S]`, together with those two components, would be a
`K_7^-` model.  Therefore `G[S]` is `K_5^-`-minor-free.  The numerical
bound of eleven edges is valid: in a twelve-edge spanning subgraph on six
vertices, deleting a vertex of degree at most three leaves a `K_5^-`
subgraph, while minimum degree four forces `K_6-3K_2`, where contracting an
edge between different missing pairs gives `K_5^-`.

A singleton component must contain a common endpoint of `a,b`.  This is
impossible in the matching case and forces the common star vertex `r` in
the path case.  Then six-connectivity and restoration give

```text
N_X(r)=S,  d_G(r)=8,  N_G(r)=S dot-union {x,y}.
```

The signature `{rx,ry}` restores `M_0` properly and becomes a colouring of
`G-r`.  All six colours must occur on `N_G(r)`, so `x,y` form one repeated
class and `S` uses the other five colours with one repetition.  The
displayed multiplicities `2,2,1,1,1,1` follow.

For every original star leaf `x_i`, the graph
`H_i=G-(M_0 union {rx_i})` is seven-connected and the seven-set
`T_i=N_G(r)-{x_i}` is the neighbourhood of `r` there.  The component of
`H_i-T_i` containing `x_i` is full to `T_i`; otherwise at most six vertices
separate it from the singleton component `{r}`.  Restoring `rx_i` joins
the two full connected sets.  A `K_5^-` model in `G[T_i]` would therefore
give `K_7^-`, proving all five deletion-boundary exclusions.

## 5. The two exact lifts

In Corollary 3.2, selecting one endpoint from each of the two crossing
matching edges meets every edge between the two open shores.  If one shore
vanished, the singleton case is already excluded.  It must therefore
consist of the two selected endpoints, one from each crossing edge.  Each
has only eight possible neighbours, so minimum degree forces adjacency to
the whole six-cut, to the other selected vertex, and to its matching mate.
In the signature whose equality set is the two crossing edges, swapping the
two colours on those selected vertices preserves every internal and
boundary edge and repairs both crossing edges.  This would six-colour `G`,
so both residual shores are nonempty and every displayed order-eight cut is
proper.

In Corollary 3.3, when the selected edges form `x-r-y` and no edge of
`M_0` crosses the cut, deleting `r` meets all cross-shore edges.  Unless its
shore is the singleton `{r}`, this gives the asserted actual order-seven
separation of `G`.

## 6. The seven-connected model row

For the exact spanning model `P,B,C,U_1,...,U_4`, the connected bag `B`
lies outside `P union N_X(P)`.  If `X` is seven-connected, the separator
`N_X(P)` has order at least seven and lies in the four universal bags, so
one universal bag contains two literal `P`-portals.

Rerunning the audited retaining-core/opposite-gate proof with this
prescribed pair is legitimate.  In an avoidable-core separator, the
returned piece contains the avoided portal.  In the opposite-gate case,
the two gates contain the two selected portals; unless one gate is the
separator, the proof constructs `K_7^-`.  Target exclusion therefore gives
a connected proper bag piece `Y`, with connected complement and an actual
separator in `G`, containing one literal vertex of `N_X(P)`.  Theorem 2.3
then puts that vertex and all six forest edges on one cycle.

## 7. Trust boundary

The source does not infer that this cycle uses the particular edge from
the selected portal into `P`, nor that two named model portals can be put on
one cycle.  It also does not infer branch-bag placement, a common boundary
partition, or compatible colourings from the punctured cube.  The exact
order-six cut still has unresolved crossing patterns, and the model-bag
separator still has an edge-label mismatch.  No terminal conclusion is
claimed or used in this audit.
