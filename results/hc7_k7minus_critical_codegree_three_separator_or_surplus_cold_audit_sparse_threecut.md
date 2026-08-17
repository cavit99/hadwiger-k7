# Independent cold audit: critical codegree-three separator or surplus

**Audited source:**
[`hc7_k7minus_critical_codegree_three_separator_or_surplus.md`](hc7_k7minus_critical_codegree_three_separator_or_surplus.md)

**Source SHA-256:**
`fb2083fff6087ea3b192a63800b1aa0e1f7f496d47524e452964f616a12b79e0`

Relative to the mathematical revision audited at SHA-256
`e3d6a2666368a89a79708a9aa162f35739abe6d1e3c895e4bf4612be4108c25b`,
the final revision changes only the status line to record the two GREEN
cold audits.  No hypothesis, conclusion, proof step or scope statement
changed.

**Verdict:** **GREEN for Theorems 1 and 2.**  This is an independent,
computation-free cold proof audit, not external peer review.  Every stated
theorem quantifier, the use of the proved `t=6` case of Hadwiger's
conjecture, and the contraction arithmetic have been checked.  No bound on
the degree of the second endpoint is used.  The two separator neighbourhoods
and the guaranteed boundary containing the specified endpoint are valid.

## 1. Frozen inputs and the external theorem

The four hashes printed in the source agree with the local files:

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2
  results/hc7_adjacent_pair_palette_linkage.md
06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844
  results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md
6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67
  results/hc7_k7minus_degree7_rooted_helper_closure.md
f0e129b30bb9f1c0d8cf8257b39bb70cbc573d15e7231de90c52de62aa33ad79
  active/hc7_k7minus_low_endpoint_joint_two_root_split.md
```

The primary publisher record for N. Robertson, P. Seymour and R. Thomas,
*Hadwiger's conjecture for `K_6`-free graphs*, Combinatorica **13** (1993),
279--361, DOI
[`10.1007/BF01202354`](https://link.springer.com/article/10.1007/BF01202354),
states the authors' convention explicitly: a graph not contractible to
`K_{t+1}` should be `t`-colourable, and their result establishes the
`t=5` case (via the Four Colour Theorem).  In the modern clique-indexed
convention this is precisely the proved `HC_6` statement

```text
no K_6 minor  =>  five-colourable,
```

whose contrapositive is the source's only use: every six-chromatic graph
has a `K_6` minor.

## 2. Chromatic entrance, connectivity and spanning model

For `H=G-{v,x}`, the inequality `chi(G)<=chi(H)+2` and proper-minor
six-colourability give `5<=chi(H)<=6`.  If a five-colouring of `H` had a
colour with no common neighbour of `v,x`, moving all `v`-neighbours of
that colour to a fresh sixth colour, assigning the vacated colour to `v`,
and assigning the fresh colour to `x` is proper.  The moved vertices are
independent, none is adjacent to `x`, and every old-colour neighbour of
`v` was moved.  Hence all five colours would require distinct common
neighbours, contradicting codegree at most four.  Thus `chi(H)=6`.

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  The verified `HC_6` input supplies a `K_6` model
in `H`.  Because `H` is connected, each component outside the current six
bags has an edge to a bag and can be absorbed wholesale into that bag.
Iteration makes the model spanning without changing any clique contact.
This proves items 1--2 for the full degree-free range `3<=c(vx)<=4`.

The palette source assumes seven-connectivity, seven-chromaticity,
proper-minor six-colourability and `chi(G-{v,x})=6`; it has no endpoint-
degree hypothesis.  Its saturation and five-path conclusions therefore
apply literally, verifying item 3.

## 3. The arbitrary-spanning-model quantifier

Fix any spanning `K_6` model.  The connected bag `{v,x}` together with
the six model bags would have at most one missing adjacency if it contacted
at least five model bags.  Target exclusion consequently gives

```text
|C_v union C_x|<=4.                                   (A)
```

Let `W=N(v) cap N(x)`, with `3<=|W|<=4`.  Two members of `W` in one bag
already give distinct pole roots there.  Otherwise they occupy distinct
common-contact bags.  If no common-contact bag contains distinct pole
roots, both pole-neighbour sets in each such bag must equal the same
singleton, and those singletons are exactly `W`.

The edge-deletion palette gives both poles a neighbour in every one of the
five non-pole colours.  Choose a colour absent from `W`.  Its two selected
pole-neighbours cannot be the same vertex, cannot occupy an old common bag,
and cannot occupy the same new bag: every possibility either contradicts
the colour choice or gives distinct pole roots in a common-contact bag.
They therefore lie in two distinct exclusive bags.  Together with the
`|W|` common bags this contradicts (A), since `|W|+2>=5`.  The argument
started from an arbitrary spanning model, so item 4 has exactly the stated
universal quantifier.

## 4. Every root-respecting split and the returned separator

For any partition of the mixed bag into nonempty connected adjacent pieces
with the nominated roots on their respective sides, adjoining the two poles
gives two connected bags.  These and the five foreign model bags form seven
disjoint connected bags.  The two split bags are adjacent through `vx`, and
the five foreign bags are pairwise adjacent.  Thus only the ten split--
foreign contacts can fail.  At most one failure would be a `K_7^-` model,
so target exclusion forces at least two.

For any failed contact on side `p`, the piece `X_p` is anticomplete to the
corresponding nonempty foreign bag, even after `p` is adjoined.  Therefore
`N_G(X_p)` is an actual separator, and it contains `p` because `X_p`
contains its nominated `p`-neighbour.  The pole-piece `{p} union X_p` is
also connected and anticomplete to that same foreign bag.  Hence

```text
N_G({p} union X_p)
```

is also an actual separator.  The other pole `q` belongs to this boundary
through the edge `pq`.  Thus, regardless of the failed side, one of these
two separators contains the specified endpoint `v`; in Theorem 2 this is
the degree-eight endpoint.

Seven-connectivity gives both separators order at least seven.  If either
has order seven and a component misses a boundary vertex, that component's
neighbourhood has order at most six and still separates it from another
component.  This proves the stated fullness claim for both neighbourhoods.
No upper bound on either separator order is inferred.

## 5. Critical-host dichotomy and exact arithmetic

Minor-minimality makes every proper minor six-colourable and gives
`chi(G)=7`; the audited critical-host package gives seven-connectivity,
minimum degree eight, a degree-eight vertex `v`, and `m(G)>=4n(G)`.  The
generic six-connected degree-eight theorem applies to this seven-connected
host and supplies an incident edge `vx` of codegree at most three.

If its codegree is three, it lies in Theorem 1's range and yields outcome
2.  If `c=c(vx)<=2`, put `Q=G/vx`.  Edge contraction lowers connectivity by
at most one, target-freeness passes to minors, and exact simplification
deletes one vertex and exactly `1+c` edges.  Hence

```text
m(Q)=m(G)-1-c
    >=4n(G)-3
     =4(n(G)-1)+1
     =4n(Q)+1.
```

The proper minor `Q` is six-colourable.  A five-colouring would split its
contraction vertex, leave `x` in the old colour, and give `v` a fresh sixth
colour, contradicting the choice of `G`; thus `chi(Q)=6`.

Finally, in any six-colouring of `Q`, the contraction colour is absent from
all seven vertices of `T=N_G(v)-{x}`.  If one of the other five colours
were absent from `T`, splitting the contracted vertex and assigning that
colour to `v` would restore a proper six-colouring of `G`.  Thus every one
of those five colours occurs on `T`, with the universal quantifier stated
in outcome 1.

The theorem is a genuine separator-or-positive-surplus reduction.  It does
not exclude the unbounded separator or the six-connected `4n+1` quotient,
and therefore does not by itself prove Conjecture 21 or `HC_7`.
