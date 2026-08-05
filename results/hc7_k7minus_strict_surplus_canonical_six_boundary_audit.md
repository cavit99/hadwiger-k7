# Internal audit: canonical sparse six-boundaries at strict surplus

**Verdict:** GREEN for the exact source revision below.

**Audited source:**
`results/hc7_k7minus_strict_surplus_canonical_six_boundary.md`

**SHA-256:**

```text
b1fdb62070dda275a9f2e6ddd1bc1642f16b7d55df4ab5de7565375a0d7db5d8
```

Two independent hostile internal checks found no unresolved mathematical
defect in this revision.  This is an internal audit, not external peer
review.

## 1. Six-vertex lemma

The complement classification was checked both directly and by exhaustive
enumeration.  A four-edge graph on six vertices with independence number at
most three is exactly one of

\[
 K_1\mathbin{\dot\cup}K_2\mathbin{\dot\cup}K_3,
 \qquad K_2\mathbin{\dot\cup}P_4.
\]

In each case the contraction named in the source is an edge of the original
eleven-edge graph and its ends have exactly one common neighbour.  The
contraction therefore loses two edges and leaves a five-vertex, nine-edge
graph, necessarily `K_5^-`.  The passage from at least eleven edges to an
eleven-edge spanning subgraph preserves both exclusions used in the proof.

## 2. Order and clique visibility

For a strict-surplus minimum counterexample, the audited Mader--Schmidt
reduction gives minimal seven-connectivity and `|L|-|F|>=2`.  Jakobsen's
bound gives

\[
 |V(G)|\ge21+2q\ge23,
\]

because a seven-connected graph is not a nontrivial four-sum cockade and
neither base exception can be the present host.  Hence `|L|>=13`.

A literal `K_4` in `N(x)` is equivalent to a literal `K_5` containing `x`.
The audited two-clique theorem permits at most one such `K_5`, so at most
five of the at least thirteen degree-seven vertices see a neighbourhood
`K_4`.  The conclusion that at least eight are reserve-blind is exact.

## 3. The prescribed canonical cut

For every selected `x,y`, the set `T_y=N(x)-{y}` has order six and isolates
`x` in `G-xy`.  The essential-edge theorem supplies six-connectivity of
`G-xy`.  Seven-connectivity of `G` then proves directly that the rest is one
connected component `B_y`; six-connectivity makes both components full to
`T_y`.

The source no longer relies on the existential cut in the statement of the
essential-edge theorem for the remaining prescribed-cut claims.  Contracting
`B_y` and retaining `{x}` gives `K_2` joined to `G[T_y]`, proving that the
boundary has no `K_5^-` minor.  The direct edge partition gives

\[
 \delta_{B_y}=19+q-|E(G[T_y])|.
\]

Combining this with the six-vertex lemma gives
`\delta_{B_y}>=9+q`.  The internal six-connectivity argument correctly
turns any forbidden rooted separation into a cut of order at most five in
`G-xy`.

## 4. Existing model and contact concentration

Deleting `x` from the seven-connected graph leaves a six-connected graph
`J_x` with

\[
 |E(J_x)|=4|V(J_x)|-5+q\ge4|V(J_x)|-4.
\]

Its order is at least 22.  Norin--Totschnig Theorem 6 therefore applies
well above its `4n-8` threshold, and its eight-vertex exception is
impossible.  Assigning each component outside the initial model union to an
adjacent branch set makes the `K_7^vee` model spanning.  If either nominally
missing adjacency appeared, the model would already contain `K_7^-`, so
the spanning model is exact.  Absorbing the deficient bag into a universal
bag gives a spanning `K_6` model.

The strengthened contact conclusion is correct.  Five `K_6` branch sets
meeting `T_y`, together with `{x}`, would be seven disjoint connected bags
with at most the sixth `x`--bag adjacency absent.  They would form a
`K_7^-` model.  Thus every `K_6` model meets `T_y` in at most four bags.

## 5. Visible-stratum inequality

For `x` in the unique possible `K_5`, the proof re-establishes the
prescribed full two-shore cut rather than importing the narrower scope of
Theorem 2.  The general six-cut reserve theorem applies to both shores.
The direct identity

\[
 \delta_{\{x\}}+\delta_{B_y}
 =15+q-t-\varepsilon
\]

and the exact degree count give

\[
 d(p)+d(q)\ge15+q+\varepsilon.
\]

Summing over the three pairs gives the displayed charge inequality.  No
aggregation beyond the unique-`K_5` stratum is claimed.

## 6. Dependency pins and unresolved scope

The checked repository inputs are:

```text
1a8531ffaec27ff17673b53798169c0952a3cf156e8c6a55763eb633ec13227e  results/hc7_k7minus_strict_surplus_minimal_enemy.md
421544721b5084fe5dff280cd2299f0e4cb214ba39bc2b2fde5648fc393bcd83  results/hc7_k7minus_two_literal_k5_exclusion.md
0a652b431e9e0bd92fcc0aa76fa120c4ffcbc7c61a0d0198b2cc475a3ce79b92  results/hc7_k7minus_essential_edge_six_separation.md
997dd39a178d7b8e3f528aa25d5c7db8b4cfd0eeb61619b0e5a427124f9ff929  results/hc7_k7minus_six_cut_k4_reserve_inequality.md
```

The theorem does not eliminate `q>0`.  It does not split a contacted
`K_6` bag, produce five boundary-meeting bags, force a smaller canonical
shore, or uncross two canonical cuts.  The statement that direct canonical
vertexwise reserve aggregation is blind outside the unique possible
literal `K_5` is a route nonclosure only.  It does not exclude a different
essential-edge boundary or an indirect use of the reserve inequality.
