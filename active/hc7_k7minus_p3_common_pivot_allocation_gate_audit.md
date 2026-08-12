# Internal audit: induced-path common-pivot allocation reduction

**Verdict:** GREEN for Theorems 1.1 and 2.1, Proposition 3.1, the
seven-branch-set construction in Section 4, and the stated route
nonclosure.  This is a separate internal mathematical audit, not external
peer review.

## 1. Exact revision and trust boundary

The audited source is
[`hc7_k7minus_p3_common_pivot_allocation_gate.md`](hc7_k7minus_p3_common_pivot_allocation_gate.md),
with SHA-256

```text
a79c4edf7c921725060ddab8a8711fdedcab62480d27d2f67d8bcfd58eec72e6
```

The mathematical text is unchanged from revision
`9ff99e70bfd39affa0b354023060255f0de3b1454f962c1e87171f407335deb0`;
the current revision changes only the status line to link this audit.

The live application uses the audited
[`six-coordinate induced-forest reduction`](../results/hc7_k7minus_six_coordinate_forest_reduction.md)
at revision

```text
cc2b56362d52a3ef23559a4a0e5cbf5eded5abbe7d54b57e73f66f74f1dd3405
```

and is consistent with the separately audited
[`induced-path opposite-coordinate common-model theorem`](../results/hc7_k7minus_p3_opposite_coordinate_common_model.md)
at revision

```text
3a2ded6ee2bbbe1e9735dd43f30bb7b0dcb193395ffc69fc64056ab7964a1cf7
```

The proof also invokes the established case `HC_6`: every six-chromatic
graph has a `K_6` minor.

In the six-coordinate application, if
`X=G-(M_0\cup\{rx,ry\})`, then `X+rx` and `X+ry` are
seven-connected.  Restoring the four edges of `M_0` gives `G-ry` and
`G-rx`, respectively, so the two seven-connectivity hypotheses in Section
1 of the audited note are justified by the cited reduction.

## 2. Connectivity, colourings, and contractions

Deleting one edge from a seven-connected graph leaves a graph of
connectivity at least six.  Applied to `H=(G-a)-b`, this proves
six-connectivity; the identities `H+a=G-b` and `H+b=G-a` give the two
seven-connected restorations.

For every nonempty subset of the two path edges, contracting precisely that
subset and expanding a six-colouring realises precisely the selected
equalities.  The uncontracted path edge does not collapse: the selected
edges form a subforest of the induced path `x-r-y`.  Hence all three
nonempty signatures occur.  The empty signature would remain proper when
both edges were restored and would six-colour `G`.

A five-colouring of `H` can be repaired by assigning one new colour to the
nonadjacent leaves `x,y`; a five-colouring of `G/a/b` can be repaired in
the same way after expansion.  In the latter case every external neighbour
of the contracted path avoids the contraction colour.  These repairs prove
that both graphs are exactly six-chromatic.  Applying `HC_6`, making the
model spanning in the connected contraction, and expanding gives one
spanning `K_6` model whose distinguished bag contains the whole path.

## 3. Structure of a six-cut

Let `T` be a six-cut of `H`.  Since adding either `rx` or `ry` yields a
seven-connected graph, each added edge must reconnect `H-T`.  One edge can
reconnect a disconnected graph only when there are exactly two components
and its ends lie in different components.  Neither end can lie in `T`.
Because the two edges share `r`, the components may therefore be named
`A,B` with `r\in A` and `x,y\in B`.

Six-connectivity makes both components full to `T`.  If `A\ne\{r\}`,
then the only edges of `G-H` leave `r` for `x,y`, so
`N_G(B)=T\mathbin{\dot\cup}\{r\}` and `A-\{r\}` is a nonempty opposite
open side.  If `A=\{r\}`, fullness gives `N_H(r)=T`, whence
`N_G(r)=T\mathbin{\dot\cup}\{x,y\}` and `d_G(r)=8`.  The opposite open
side is nonempty: a component containing the two nonadjacent vertices
`x,y` cannot consist only of them.

Each of the three fixed colourings has a monochromatic omitted edge, and
the displayed side contains an endpoint of every such edge.  Deleting that
side therefore leaves a proper exterior colouring.  If its induced boundary
partition extended through the intact side, colour-name alignment and
gluing would six-colour `G`.  Thus all three partitions are genuinely
rejected as asserted.

## 4. The common Kempe pivot

In the colouring expanded from `G/a/b`, all three path vertices have colour
`alpha`.  Fix an alternate colour `beta`.  If the `alpha,beta` component
through `r` contained neither leaf, switching the component through `x`
and the component through `y` (only once if they coincide) would change both
leaves and not `r`.  Both omitted edges could then be restored properly,
contradicting `chi(G)=7`.  Hence each of the five alternate palettes joins
`r` to at least one leaf.

If two palettes have the opposite singleton leaf sets, switching their
components separately gives the two singleton equality signatures from the
same initial colouring.  Otherwise either every leaf set is the pair
`\{x,y\}`, or a singleton occurs and its leaf belongs to all five sets.
This proves both the exhaustiveness and the exclusivity of Theorem 2.1.

## 5. Response and domination claims

The `alpha,beta` component is bipartite in `H`.  Recolouring `r` with a
third colour repairs whichever of `rx,ry` have both ends in the component,
so `G[C_beta]` is three-colourable.

If `C_beta` is not dominating, its open neighbourhood is an actual
separator because a vertex lies outside `C_beta\cup N_G(C_beta)`.  Its
order is at least seven by `kappa(G)\ge7`.  Removing the component deletes
both monochromatic omitted edges, since they are incident with `r`, and
therefore leaves the fixed proper exterior colouring.  The boundary
partition is rejected by the same gluing argument.  In the singleton-leaf
case, the Kempe switch changes no exterior vertex and supplies the opposite
singleton response on that same exterior partition.

If `C_beta` dominates, a three-colouring of its complement together with
the proved three-colouring of `G[C_beta]`, on disjoint palettes, would
six-colour `G`; hence the complement is at least four-chromatic.  An outside
vertex of colour `alpha` or `beta` could meet the component in `H` only by
joining the same bichromatic component.  Thus the only possible use of
either colour outside is the one leaf incident with an omitted edge and not
in `C_beta`.  The fixed colouring consequently uses at most five colours on
the complement, and at most four if both leaves lie in the component.
This proves (3.1)--(3.2).

A `K_6` model in the complement, together with the connected dominating
set `C_beta`, would form a `K_7` model, and hence a `K_7^-` minor.  The
minor-exclusion conclusion in (3.1) is therefore valid.

## 6. Model split and unresolved conclusion

The two path edges form a forest inside the lifted path bag, so they extend
to a spanning tree of that bag.  Removing them partitions the bag into
three nonempty connected sets containing `x,r,y` and retaining the two
path adjacencies.  Four foreign bags adjacent to all three sets, together
with those three sets, give seven branch sets whose only possibly absent
adjacency is the one between the two leaf pieces.  This is an explicit
`K_7^-` model.

No checked argument assigns a Kempe component to a deficient foreign branch
set, bounds the boundary of a non-dominating component by eight, or turns a
dominating component into the missing fourth triple contact.  Consequently
implication (4.2) remains unsupported exactly as the source records.  The
note does **not** close the induced-path case, the six-coordinate
terminalisation theorem, the `K_7^-` six-colour conjecture, or `HC_7`.  No
finite computation is used.
