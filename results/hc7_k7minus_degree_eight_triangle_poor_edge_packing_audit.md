# Internal audit: degree-eight triangle-poor edge packing

**Verdict:** **GREEN.**  All eight statements, including the
computation-free three-triangle conclusion and the strict Jakobsen-defect
improvement `D>=26`, are correct at the pinned revision.  This is an
internal mathematical audit, not external peer review.

## Exact revisions

The audited theorem is
[`hc7_k7minus_degree_eight_triangle_poor_edge_packing.md`](hc7_k7minus_degree_eight_triangle_poor_edge_packing.md),
SHA-256

```text
2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449
```

The retained cross-check is
[`hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py`](hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py),
SHA-256

```text
dc205fccdef1859a66ac1338ad11418a347b4165687f556f4291027d4ee6c951
```

## 1. The complement lemma and the four-triangle bound

For `J` on eight vertices with minimum degree at least five,
`H=\overline J` has maximum degree at most two.  In an edge-maximal
supergraph `H'` subject to that bound, a path of order at least three can be
closed, and deficient vertices in distinct components can be joined.  Thus
the only deficient component is `K_1` or `K_2`; all others are cycles.  The
integer partitions of eight give exactly the seven types listed in (1).

Every nonsingleton bag in table (2) is connected in `\overline{H'}`.  Direct
pairwise checking gives exactly the one displayed possible nonadjacency in
each row.  Since `overline{H'}` is a spanning subgraph of `J`, this proves a
genuine `K_6^-` minor in `J`.  Adding the degree-eight centre gives Theorem
2.  Choosing one such edge per centre and identifying duplicates loses a
factor of at most two, so Corollary 3 is exact.

Jakobsen's strict noncockade inequality is correctly converted to

\[
                         2m\le9n-25.
\]

The degree identity `2m=9n-n_8+\tau` then gives
`n_8>=25+\tau`, proving Corollary 4.

## 2. Rooted deletion lemma

The connectivity reduction in Lemma 5 is exhaustive.

- Minimum degree four excludes a disconnected graph and a cutvertex on
  eight vertices.
- Behind a two-cut, every component has order at least three.  Hence there
  are exactly two three-vertex components, each a triangle complete to the
  cut.  An edge in the cut gives a `K_4`; an independent cut gives
  independence number two.  Both contradict the hypotheses.

If `J` is four-connected, `J-r` is three-connected.  Wood and Woodall's
Lemma 4.2.1 states exactly that a three-connected `K_5^-`-minor-free graph
is a wheel, the triangular prism, or `K_{3,3}`.  At order seven only the
wheel remains.  Minimum degree forces `r` to see all six rim vertices;
`K_4`-freeness forces it to miss the hub.  The resulting graph is precisely
`\overline{K_2}\vee C_6`.  The bags in (10) prove that every rim vertex is
good, and those rim vertices totally dominate the graph.

If `J` has a three-cut `S`, every complementary component has order at
least two, so their orders are two and three.  The order-two component `A`
is an edge complete to the independent set `S`.  The other component `B`
has minimum internal degree one and is therefore `P_3` or `K_3`.

For `B=P_3`, its ends are complete to `S` and its middle sees at least two
members of `S`.  The displays (11), (12), and (13) respectively certify
goodness after deleting a vertex of `A`, an end of `B`, and the middle of
`B`; every claimed bag is connected and the named `A-B` pair is the only
missing pair.  For `B=K_3`, degree and `K_4`-freeness make the missing
`B-S` incidences a perfect matching.  Displays (14) and (15) certify the
deletions from `A` and `B`.  Symmetry handles the other vertices.  The good
vertices in `A\cup B` totally dominate because `A` is an edge, `B` has no
isolated vertex, and `A` is complete to `S`.  Lemma 5 follows without finite
enumeration.

## 3. Exterior lift and three-triangle conclusion

In Theorem 6, let `x` be the unique possible nonneighbour of the exterior
vertex `c`, or any vertex if `c` is full.  Lemma 5 supplies a good neighbour
`r` of `x`; hence `cr` is present.  The bag `{c,r}` sees every bag of the
`K_5^-` model in `J-r`: `c` supplies the contact unless that bag is the
singleton `{x}`, in which case `rx` supplies it.  Together with singleton
`{z}`, these are seven disjoint connected bags and inherit only the one
possible missing pair of the `K_5^-` model.  This is an exact `K_7^-` lift.

For Corollary 7, a component `C` of `G-N[v]` has all its external neighbours
in `N(v)`, and that neighbourhood separates `C` from `v`.  Seven-connectivity
therefore makes `C` adjacent to at least seven of the eight boundary
vertices.  Contracting `C` gives exactly Theorem 6.  If there is no exterior,
seven-connectivity instead gives minimum degree at least six in `G[N(v)]`,
and Lemma 1 applies.  Hence the neighbourhood has a vertex of degree at most
three.  Its degree there equals the codegree of the corresponding incident
edge, so the edge lies in at most three triangles.

## 4. Defect arithmetic and contraction

Under Corollary 8, degree summation gives

\[
 2m=9n-b+\tau,
 \qquad D=b-\tau=9n-2m.
\]

Jakobsen applied to the seven-connected target-free host gives `D>=25` and
therefore `b>=25+\tau`; in particular the graph has at least twenty-five
vertices and a degree-eight vertex.

Contracting any edge of a seven-connected graph leaves a six-connected
graph.  A cut of order at most five not containing the contracted vertex
would itself lift, while a cut containing it lifts after replacing it by
the two ends and has order at most six.  The quotient here has order at
least twenty-four, is target-free, and cannot be either base cockade or a
nontrivial cockade with a four-cut.  Jakobsen therefore applies again.  With
`c(e)` common neighbours,

\[
 |E(G/e)|=m-1-c(e)
\]

and direct rearrangement gives `D+2c(e)>=32`.  Corollary 7 supplies an edge
with `c(e)<=3`, so `D>=26`.  Selecting one such edge at every degree-eight
vertex and deduplicating gives at least `ceil(b/2)` edges, establishing the
packing bound in (21).

The stated critical-host specialisation uses two already audited facts at
their current promoted revisions:

- the degree-seven rooted-helper closure gives minimum degree eight and no
  literal `K_5`;
- the exceptional-neighbourhood theorem gives independence number three in
  each degree-eight neighbourhood.

Thus those neighbourhoods satisfy (17), and the elimination of `D=25` is a
valid new deduction.

## 5. Verifier coverage and calibration

The verifier is not needed for the proof, but its coverage is exact.  Every
eight-vertex graph is isomorphic to an extension of one of the 1,044
unlabelled seven-vertex atlas graphs.  Filtering all 128 extensions gives
352 eligible representations and 42 isomorphism classes.  For every class,
the script tests all eight deletions for a `K_5^-` minor, verifies total
domination by the successful deletions, and tests the full and all eight
one-miss exterior augmentations for `K_7^-`.

The minor recursion is exhaustive: from singleton bags it considers every
deletion and every merge of touching bags.  Every connected minor-model bag
can be obtained through such a sequence, and every returned model is
independently checked for connectivity, disjointness, and at most one
missing adjacency.

The pinned run returns

```text
GREEN exceptional-neighbourhood finite cross-check
atlas_order_seven=1044
eligible_extension_representations=352
eligible_isomorphism_classes=42
rooted_deletion_checks=336
almost_full_augmentation_checks=378
negative_calibration=GMs`KK full exterior augmentation is target-free
certificate_sha256=6024f1bcececd88038a16700c6c867570524a774f312e5d3acc5a27934e58047
```

The cubic negative calibration has minimum degree three, is `K_4`-free with
independence number three, and its full two-pole augmentation is exactly
rejected.  It therefore validates the recorded barrier to lowering the
local threshold without importing that computation into the theorem proof.

## 6. Scope

The result eliminates the exact defect layer `D=25` and supplies a global
packing of three-triangle edges.  It does not eliminate `D>=26`, prove the
`4n-2` extremal conjecture, or produce a six-colouring.  The source's
assessment that it remains below the Norin--Totschnig benchmark is accurate.
