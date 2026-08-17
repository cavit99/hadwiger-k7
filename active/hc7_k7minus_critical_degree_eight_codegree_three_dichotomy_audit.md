# Author-side audit: codegree-three or excess-eighteen dichotomy

**Verdict:** **GREEN** for the theorem at SHA-256

```text
891f937237eff6eb3dd1a111ea6a68611c4b5d3ee7b4c2b4ef0465ff684b0b3e.
```

This is an adversarial self-audit, not an independent or external review.
The finite census and the static pair-deletion obstruction were rerun from
the repository lockfile during this audit.

## Finite census

The generator is exhaustive at order eight.  Every unlabelled graph of
order eight is obtained by deleting one vertex, taking the resulting
order-seven graph from the complete NetworkX atlas, and trying all
neighbourhoods of the restored vertex.  Isomorphism reduction therefore
loses no class.  The filters are exactly those in Lemma 1:

```text
minimum degree at least three,
no K_6^- minor,
clique number at most three,
independence number exactly three.
```

The two added vertices are distinct, nonadjacent and complete to all eight
local vertices.  The exact contraction--deletion engine checks all
partitions obtainable by contractions and deletions and independently
verifies every returned model.  Its positive and negative calibrations run
before the census.  The rerun reproduced

```text
542 local graphs,
486 positive full quotients,
56 target-free full quotients,
degree-three distribution (4:8, 5:13, 6:25, 7:6, 8:4).
```

The positive-model digest and negative-profile digest are respectively

```text
e2e65a34a35d8467054ab5c7b9db2df3bc2f4a2bb4345be1f900cb98d87fb500
a1bf6e4c242e984c46d89ce5a0f642c1ed2ae0811cb6aa0c7938a77f5ffa6bd0.
```

Thus the minimum of four cubic local vertices is certified over the full
finite domain, not inferred from a bounded sample.

## Lift to every degree-eight centre

Assuming outcomes 1 and 2 fail, every degree-eight neighbourhood has
minimum degree at least three because local degree is edge codegree.  The
audited critical-host inputs give `K_4`-freeness, independence number three
and `n_8>=26+tau`; a local `K_6^-` model would be completed by the centre,
so target exclusion rules it out.

The order bound makes every exterior nonempty.  The frozen full-exterior
theorem applies separately at every degree-eight centre and gives one
connected component complete to the neighbourhood.  Contracting that
entire component creates exactly the second nonadjacent universal vertex
of Lemma 1.  No exterior edge to the centre is introduced.  Hence the
finite lemma applies to every centre, and each of its four cubic local
vertices gives an incident edge of codegree exactly three.

Failure of outcome 2 puts all four opposite endpoints in degree at least
ten.  Counting ordered centre--endpoint incidences is appropriate: every
degree-eight centre contributes at least four, while a vertex of degree
`i` can receive at most `i`.  With

```text
h=sum_{i>=10}n_i <= sum_{i>=10}(i-9)n_i=tau,
```

the upper bound is exactly `9h+tau<=10tau`.  Therefore

```text
4(26+tau)<=4n_8<=I<=10tau,
```

which gives `tau>=104/6`; integrality yields `tau>=18`.  There is no lost
factor of two because the counted pairs are ordered by their degree-eight
centre.

## Four-root completion residue

For each of the `56` negative profiles, the verifier checks all seventy
four-sets and every nonedge that can be the sole absent pair of a rooted
`K_4^-`.  The reproduced distribution of the numbers of closing four-sets
is

```text
0:29, 1:8, 2:4, 3:7, 4:3, 5:3, 6:1, 15:1.
```

The digest of explicit models for one canonical closing set in each of the
`27` eliminated profiles is

```text
e6efa5015a79c25f2a20757325b70ce86a52575ece804ded026cf706317269cc.
```

Contracting a rooted model on `C union T` realizes every tested added edge.
If the model's sole missing pair is already an edge of `J[T]`, the resulting
minor is a supergraph of a tested completion.  The corollary therefore has
the right quantifiers.

## Low-endpoint pair deletion

Minimum degree eight makes the low endpoint have degree eight or nine.
The deletion identity is exact because `vx` is present:

```text
|E(G-{v,x})|=|E(G)|-8-d_G(x)+1>=4|V(G-{v,x})|-8.
```

Seven-connectivity leaves a five-connected graph.  Its order is at least
twenty-four, so the eight-vertex exception in Norin--Totschnig Theorem 6 is
excluded.  Spanning enlargement preserves the model, and target exclusion
forces both nominally absent branch-set adjacencies to remain absent.  Each
of the three contact restrictions follows from the displayed seven-bag
models; the last is stronger here because the two removed roots are
adjacent.

The static obstruction was also reproduced.  The quotient `HN~~zpx` has
connectivity four and the exact engine finds no `K_7^-` minor.  Its two
roots have the same four permitted branch-set contacts.  The multiplicity
table has totals `(7,7,3)` or `(7,8,3)` for the two neighbourhood sizes and
their intersection.  The source correctly calls this a route nonclosure,
not a host-graph counterexample or an unbounded negative theorem.

## Pinned files and scope

```text
993278e07663ee5cd10df67917037ff784a743e4b3806813b6ddd8ad0c1e46a3
  active/experiments/sevenconnected_full_exterior_profiles/verify.py
2421f7b00b263ad3ee5f4f747252d7bee23f6ff7bdfd73247033ff2012f2fb76
  active/experiments/pair_deletion_low_endpoint_interface/verify.py
c7cb794dd0298b1cbe98ac4ee1bdbbf04f1e5c546ae26f195fcbb034602b0c0d
  active/hc7_k7minus_critical_degree_eight_full_exterior_reduction.md
2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449
  results/hc7_k7minus_degree_eight_triangle_poor_edge_packing.md
```

No proof defect was found.  The `tau>=18` alternative remains a genuine
unclosed branch, and the low-endpoint branch still needs an internal
two-root alignment argument.  A separate cold audit of the new finite
census would strengthen its promotion status.
