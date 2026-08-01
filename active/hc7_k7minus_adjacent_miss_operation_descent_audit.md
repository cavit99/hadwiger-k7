# Internal audit: operation-labelled descent for distinct adjacent misses

**Verdict:** GREEN for the claims actually stated.

**Audited source:**
`active/hc7_k7minus_adjacent_miss_operation_descent.md`

**SHA-256:**

```text
a1f51c15a2edd00f5d3c6b9cbc490d159f4fca500bff526186ff301913724dfe
```

This is a separate internal mathematical audit, not external peer review.
The source is an unbounded reduction.  It does **not** eliminate the
distinct-adjacent-miss case or prove exceptional-centre connectivity.

## 1. Shore linkage and the missed edge

Lemma 1 correctly preserves the four first edges supplied by one fixed
`G-xy` colouring.  After the direct boundary edges are retained, failure
to link the remaining `4-r` first neighbours to the selected boundary
vertices gives a separator of order at most `3-r`.  The selected
component then has external neighbourhood of order at most

```text
2 + r + 1 + (3-r) = 6,
```

contrary to seven-connectivity.  The proof permits a permutation of the
four boundary ends and makes no stronger colour-label claim.

Lemma 2 is also correct.  A five-colouring of `G-{x,y}` would force all
five colours onto common neighbours of `x,y`.  At least four of those
neighbours lie in `Z`; they must be pairwise nonadjacent, since an adjacent
pair together with `x,y` would be a literal `K_4` in `G[N(u)]`.  This
contradicts the established equality `alpha(G[N(u)])=3`.  Hence
`chi(G-{x,y})=6`.

## 2. The coupled paths and prescribed fans

The hypotheses of the audited palette-permutation linkage theorem apply
to `H=G-{x,y}`.  The five selected neighbours at each pole have distinct
non-`alpha` colours, and `u` is retained as the trivial `beta` path.
Prepending and appending the named edges therefore gives the five
internally disjoint `x`--`y` paths asserted in Theorem 3.  The other four
paths avoid `u` and must meet `Z`, because they start in `F union Z`, end
in `E union Z`, and `E,F` are anticomplete.

The ordinary six-fan argument in Corollary 4 is valid.  A failed fan would
give an `x`-side component with at most seven neighbours.  Equality would
force that component to be `{x}`, contradicting the already proved
minimum degree eight in this two-component branch.  The subsequent
gammoid is explicitly restricted to neighbours of `x`; this restriction
is essential, and makes matroid augmentation preserve incident first
edges.  The same argument applies at `y`.

## 3. The four-root opportunity

For `R=G-{u,x,y}`, deleting three vertices from a seven-connected graph
does give four-connectivity.  Exterior vertices have degree at least seven
in `R`, boundary vertices in `Z` have degree at least five, and each
exterior component has at least two vertices.  Thus

```text
sum(6-d_R(v)) <= 6-|E|-|F| <= 2,
```

which contradicts the planar Euler bound `sum(6-d(v))>=12`.

Fabila-Monroy and Wood, Theorem 6, consequently supplies a point-rooted
`K_4` model at the four selected vertices of `Z`.  The source correctly
stops there.  That theorem does not ensure that the bag rooted at `z_i`
avoids the other three operation-labelled paths.  Absorbing whole paths
can therefore destroy branch-set disjointness.

Contracting the four paths first does not repair the argument: a small
separator in the quotient may contain a contracted path vertex, whose
expansion is an entire path rather than one vertex.  It consequently need
not lift to an order-four separator of `R`, or to an order-seven separator
of `G`.  No cited repository theorem supplies this missing set-rooted,
label-preserving absorption step.

## 4. Exact-seven descent

Theorem 6 matches Theorem 3.1 of the audited critical-edge fan/descent
result with boundary `S_x`, component `C_x`, base vertex `x`, boundary
endpoint `y`, and deleted edge `xy`.  The five first-hit vertices occupy
at most five boundary vertices, so the cited target-retaining hypothesis
holds.  In the separation outcome, the exact neighbourhood has order
seven and retains the restricted `G-xy` colouring.

The returned connected set lies properly inside `F`: it cannot contain
`u`, which is adjacent to all of `S_x`, and equality with `F` would leave
no room for the required four disjoint internal separator vertices.
The symmetric application uses the same fixed colouring.  Corollary 7 is
therefore valid, but it is only a two-sided normalization; the returned
side need not itself be an exceptional-neighbourhood instance.

## 5. Dependency revisions and scope

The principal checked dependency revisions are:

```text
d359b4a14520fc4d558ebc600c4e64b7f6bf65ef9fa425b107effa498afc3bfa  results/hc7_exact7_critical_edge_fan_descent.md
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2  results/hc7_adjacent_pair_palette_linkage.md
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd  results/hc7_k7minus_exceptional_neighbourhood_completion.md
e1b54acdd971831786c0d8912d5e4189aaeedd84184540ed438e594aadb9b2e4  results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md
```

No finite computation is used in this note.  It may be cited for the
non-double-critical edge, coupled five-path packing, two prescribed full
shore fans, four-connected nonplanar residual, and the clean-packing or
strict exact-seven-separation alternative.  It may not be cited as a
`K_7^-` construction, a set-rooted absorption theorem, an elimination of
adjacent misses, or a proof of exceptional-centre connectivity.
