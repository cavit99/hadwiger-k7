# Separate internal audit: forbidden-signature Kempe coupling

**Verdict:** GREEN for Theorems 2.1 and 3.1--3.3 and for the
lock-or-separator dichotomy (3.12).  Section 4 accurately records a route
nonclosure and does not assert an exhaustive impossibility theorem.  This
is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_matching_forbidden_signature_kempe_coupling.md`](hc7_k7minus_matching_forbidden_signature_kempe_coupling.md),
with SHA-256

```text
0159743557cc9c0de8a0d9e9f3969b9ecde20bb2bf50d5e8716cf6e54a1297d1
```

The promoted source differs from the initially audited revision
`fe30c71257b49c88aef9da7c37b72d79ccb0b4b41226bdfb90ef6113f0211afd`
only in its status header and the replacement of the historical word
"draft" by "theorem" in cross-references.  Its mathematical content is
unchanged.

## 1. Unique unlocked palette

Start from the original `(equal,proper)` colouring.  If the equal pair is
unlocked in colours `i,j`, switching the component at either endpoint
makes that pair proper.  The other edge must then become monochromatic;
otherwise the forbidden all-proper signature would colour `G`.  A
two-colour switch can merge its two endpoint colours only when they are
exactly `i,j` and precisely one endpoint is switched.  Applying this
argument independently at both equal-pair endpoints puts one end of each
deleted edge in each of the two components.  Switching either component
therefore gives the opposite singleton signature.  Since the proper
pair's two colours are fixed, at most one alternate palette can be
unlocked.  This proves every item of Theorem 2.1.

## 2. One crossed component

Each crossed component is bipartite in `G`, because neither restored edge
lies inside it.  Switching it changes only its vertices, so the two
opposite responses agree literally on the complement.  If it is
nondominating, its open neighbourhood is an actual separator and has order
at least seven.  A closed-side colouring inducing the same equality
partition would align and glue to the exterior colouring, contradicting
`chi(G)=7`.

If the component dominates, a four-colouring of its complement together
with two fresh colours on the bipartite component would colour `G`.
Conversely a `K_6` model in the complement, together with the connected
dominating component, would give a `K_7` model.  `HC_6` therefore makes
the complement exactly five-chromatic and `K_6`-minor-free.  This checks
Theorem 3.1.  The theorem supplies no upper bound on the separator order.

## 3. The crossed union and domination exclusion

The two bichromatic components have no edge between them in `H`; restoring
the two independent coordinates makes their union connected and at most
three-chromatic.  Every external neighbour has one of the four remaining
colours.  Hence a nondominating union has a four-coloured, exterior-realised
and intact-side-rejected separator.  If the union dominates, its complement
is exactly four-chromatic and `K_6`-minor-free.

If both individual components dominated, the two restored coordinates
would be their only cross-edges.  Each component would therefore consist
of its two coordinate endpoints, forming an induced four-cycle in `G`.
Contracting the cycle gives an exactly six-chromatic proper minor: a
five-colouring would expand by using its old colour on one independent
pair and a fresh sixth colour on the other.  Lift a spanning `K_6` model
from that contraction.  Both dominating components meet all five foreign
bags and each other, producing an explicit `K_7` model.  This proves
Theorem 3.2(3) and the lock-or-separator dichotomy.

Theorem 3.3 is a valid auxiliary statement under its displayed induced
endpoint-cycle hypothesis.  The same contraction argument gives exact
six-chromaticity.  A cut avoiding the contraction vertex lifts unchanged;
a cut containing it gains three vertices, so seven-connectivity gives
connectivity at least four and an order-four cut lifts to an order-seven
response separation.  A spanning `K_6` model lifts with all four cycle
vertices in one bag.  Removing the cycle from that connected bag and
assigning each remaining component to either connected seed edge it meets
gives both displayed connected splits.  The theorem is logically
auxiliary because Theorem 3.2 already excludes the both-dominating cycle
in the target-free critical host.

## 4. Exact unresolved inference

After all response-bearing separators are excluded, every singleton
response has all five alternate palettes locked.  The proof does not turn
those five bichromatic paths into four foreign bags adjacent to both sides
of a split in the independently selected common `K_6` model.  The palette
components and branch bags are unrelated vertex partitions; the paths
need not be disjoint or respect model labels.

If an unlocked palette returns a separator, its order can exceed eight.
No anchored descent or common original-shore partition is obtained at that
larger boundary.  These are the unresolved all-lock and unbounded-response
gaps recorded in Section 4.  They are route nonclosures, not
counterexamples.  The source does not prove the matching row, the
`K_7^-` six-colour conjecture, or `HC_7`.

The external input is the Robertson--Seymour--Thomas case `HC_6`.
Everything else in the theorem proofs is elementary Kempe switching,
minor-model lifting, connectivity and colouring gluing.  The results are
unbounded and computation-free.
