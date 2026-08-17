# Cold audit: low-endpoint joint two-root split

**Verdict:** **GREEN** for the source at SHA-256

```text
f0e129b30bb9f1c0d8cf8257b39bb70cbc573d15e7231de90c52de62aa33ad79
```

This is an independent proof audit.  The result is computation-free, so
there is no finite verifier to rerun.  I checked the chromatic entrance,
the imported palette and five-path theorem, every branch-set contact, the
target-sensitive missing-pair count and the exact separator conclusion.

## 1. Frozen dependencies

The source hashes match the displayed frozen inputs:

```text
2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2
  results/hc7_adjacent_pair_palette_linkage.md
6bce1f570c12a93a7d1830f53905cb1e033bd2e40abed948a70a21ce5100c03d
  results/hc7_atomic_two_pole_contact_trichotomy.md
6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67
  results/hc7_k7minus_degree7_rooted_helper_closure.md
891f937237eff6eb3dd1a111ea6a68611c4b5d3ee7b4c2b4ef0465ff684b0b3e
  active/hc7_k7minus_critical_degree_eight_codegree_three_dichotomy.md
```

The exact `n_8>=26+tau` order input ultimately comes from Corollary 8 of

```text
2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449
  results/hc7_k7minus_degree_eight_triangle_poor_edge_packing.md
```

under the critical-host hypotheses.  It is unconditional within that
setting, not contingent on failure of the low-endpoint alternative.  The
primary statement of Norin--Totschnig, Theorem 6, is exactly the form used:
a four-connected graph with at least `4|V|-8` edges has a `K_7^vee` minor,
apart from `K_{2,2,2,2}`.

## 2. Chromatic entrance

The critical-host minimum degree and `d(x)<=9` give
`d(x) in {8,9}`.  Vertex deletion makes `H=G-{v,x}` a proper minor, so it
is six-colourable, while deleting two vertices can lower chromatic number
by at most two.  Hence `5<=chi(H)<=6`.

Suppose a five-colouring of `H` exists.  Fix one colour with no common
neighbour of `v,x`.  Recolour every vertex of that colour adjacent to `v`
with a new sixth colour, give `v` the old colour and give `x` the new one.
The recoloured vertices are independent and none is adjacent to `x`; all
old-colour neighbours of `v` have been recoloured.  This is a proper
six-colouring of `G`.  Therefore each of the five colours would have to
occur on a common neighbour, requiring at least five distinct common
neighbours and contradicting codegree three.  Thus `chi(H)=6`.

Seven-connectivity leaves `H` five-connected.  Exact deletion of the
present edge `vx` gives

```text
|E(H)|=|E(G)|-8-d(x)+1 >= 4|V(H)|-8.
```

The defect count gives `|V(G)|>=26`, hence `|V(H)|>=24`, so the
eight-vertex Norin--Totschnig exception is impossible.  A `K_7^vee` model
exists.  Merging its deficient branch set with one of the four branch
sets adjacent to it yields six connected, pairwise adjacent bags and
therefore a `K_6` model.  Connectedness of `H` permits the usual spanning
enlargement.

## 3. Palette saturation and five disjoint paths

The hypotheses now match the frozen palette theorem.  Independently, its
two ingredients check as follows.

First, a six-colouring of the proper minor `G-vx` gives the two ends one
common colour `alpha`; otherwise restoring `vx` would still be proper.
Neither pole has an `alpha`-neighbour.  If either pole missed another
colour, recolouring that pole would again restore `vx`, so all five other
colours occur at neighbours of each pole.  The colour `alpha` must occur
in `H`, since otherwise `H` would be five-colourable.

For any chosen neighbour of each non-`alpha` colour at each pole, the two
five-element terminal sets `A,B` have distinct members on each side.  Put
`I=A cap B` and use its members as trivial paths.  Since `H` is
five-connected, `H-I` is `(5-|I|)`-connected.  Its two remaining,
disjoint terminal sets each have order `5-|I|`; the set form of Menger's
theorem supplies that many vertex-disjoint paths.  Truncating at the first
and last selected terminals makes every terminal an endpoint.  Together
with the trivial paths this gives all five paths, with the two endpoint
palettes paired by a permutation.  No same-colour pairing or bichromatic
interior is asserted.

Thus all of item 3, not merely the saturation fragment later used in the
split proof, is justified.

## 4. Joint contact bound

Fix any spanning `K_6` model in `H` and let `C_v,C_x` be the rows contacted
by the two poles.  The connected bag `{v,x}` and the six clique rows form
a `K_7` model if the bag meets all six rows, and a `K_7^-` model if it
meets exactly five.  Target exclusion therefore gives the sharp bound

```text
|C_v union C_x| <= 4.
```

This is the stronger `K_7^-`-sensitive count reproved in the source; it is
not being imported from the ordinary `K_7` contact theorem.

The three common-neighbour vertices lie in the spanning row partition.
If two lie in one row, those two vertices themselves give the required
distinct `v`- and `x`-roots.  Otherwise they lie in three distinct common
rows.  If no common row contains distinct pole neighbours, the nonempty
pole-neighbourhoods in each common row must be the same singleton.  Hence
these three rows are all the common rows and their portals are precisely
the three common-neighbour vertices.

Those portals use at most three of the five saturated colours.  Choose a
non-`alpha` colour absent from them.  Its neighbours at the two poles
cannot coincide, and cannot lie in the same row, because either event
would create another common portal or distinct pole neighbours in one
common row.  Their two rows are therefore distinct and exclusive.  Along
with the three common rows this makes at least five rows in
`C_v union C_x`, contradicting the contact bound.  Thus every spanning
model has the claimed splittable common row.

## 5. Split bags and actual separator

Deleting any edge on the `a-b` path of a spanning tree of the common row
partitions its vertex set into nonempty connected sets `X_v,X_x`, with the
named roots on the required sides.  The deleted tree edge also makes the
two sets adjacent.  After adjoining the appropriate poles, these two
bags are adjacent through `vx`; the five foreign rows remain pairwise
adjacent.  The only possible misses among the seven bags are consequently
the ten pole-piece--foreign-row pairs.

At most one such miss would be a `K_7^-` model, so at least two are absent.
For any absent pair, the corresponding piece `Y` and its adjoined pole are
both anticomplete to the nonempty foreign row.  In particular, `Y` is
connected and anticomplete to that row.  Its full external neighbourhood
`N_G(Y)` therefore separates `Y` from the foreign row.  This is an actual
host separator, not a model-relative duty set.

Seven-connectivity gives only `|N_G(Y)|>=7`.  If equality holds, deleting
this boundary leaves both `Y` and a component containing the missed
foreign row.  A component which missed one boundary vertex would have
neighbourhood of order at most six and would be separated from the other
component, contradicting seven-connectivity.  Hence every returned
component is full at equality.

## 6. Scope

No upper bound on `|N_G(Y)|` follows from the proof.  Only an exact
order-seven output enters the full seven-boundary interface; a larger
separator still needs a density, colouring or minimality descent.  The
theorem does not eliminate the low-endpoint branch by itself, and the
five palette paths are retained only up to a permutation.  The source
states each of these limitations accurately.  No proof defect was found.
