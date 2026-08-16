# Internal audit: remote removable edge and centred operation cube

**Verdict:** GREEN.  This is a separate internal mathematical audit, not
external peer review.

## 1. Exact revision and scope

The audited source is
[`hc7_k7minus_remote_removable_edge_operation_cube.md`](hc7_k7minus_remote_removable_edge_operation_cube.md),
with SHA-256

```text
2f7c69fd57319f898d84c9884907ac70e3e1f2064b3a5753d19da8531406ecf9
```

The audit covers the general remote-edge theorem, its critical-host
application, all `80` mixed operation patterns, the exact connectivity and
model conclusions, and the order-seven/eight opposite-shore interface.
It also covers the visible boundary-response rank in Corollary 3.5.

## 2. Chu's prescribed-set theorem

Theorem 2.2 of Chu's preprint has the exact form used.  For a
`k`-connected graph, a prescribed set `W`, `U=V(G)-W`, nonempty
`E(G[U])`, and degree at least `max\{k+1,|W|\}` at every vertex of `U`, it
returns a `k`-removable edge in `G[U]` unless `|W|=k+1` and `G[U]` is a
forest with an additional leaf structure.  The source needs only the
forest conclusion in the exception.

In Theorem 1.1, if `G[U]` were edgeless then every vertex of `U` would be
complete to the `(k+1)`-set `W`.  The order hypothesis supplies a
`K_{k,k}` subgraph, and contracting a perfect matching gives the forbidden
`K_k` minor.  In Chu's forest alternative, disjoint palettes colour `G[W]`
and `G[U]` with `\chi(G[W])+2` colours.  Finally `z` is isolated in
`G[U]`, so the returned edge has both ends outside the closed neighbourhood,
not merely outside `z`.

For the critical-host application, `|U|=|V(G)|-8\ge17`, exclusion of a
`K_7^-` minor excludes a `K_7` minor, and the degree hypotheses match with
`k=7`.  The exceptional-neighbourhood theorem supplies an independent
triple.  The proof that the remaining five-vertex `K_4`-free graph is
three-colourable is correct: a hypothetical four-critical subgraph has
minimum degree three, and the only terminal five-vertex complement-matching
case avoiding `K_4` is `K_5-2K_2`, which has the displayed three-colouring.

## 3. The mixed-operation cube

The forest `T=K_{1,3}\dot\cup K_2` is componentwise induced: the three
leaves are independent and the remote edge is vertex-disjoint from the
closed neighbourhood of the centre.  For any nontrivial labelled
keep/delete/contract pattern, expanding a hypothetical five-colouring and
recolouring the centre and, when needed, one remote-edge end with a fresh
sixth colour repairs every operated edge.  The two recoloured vertices are
nonadjacent.  Kept edges were represented in the minor, and no other edge
collapses under expansion.  This proves exact six-chromaticity for all
`3^4-1=80` patterns.

The same componentwise-induced argument gives every nonempty deletion-host
signature and excludes the empty signature.  The all-delete and
all-contract cases correctly yield `\chi(G-T)=\chi(G/T)=6`.

## 4. Connectivity and minor models

Put `J=G-f`, which is seven-connected.  In the three-spoke deletion host,
the centre has degree five.  A cut of order at most four either contains
the centre, in which case it is also a cut of `J`, or, after the centre is
added, gives a cut of `J` of order at most five.  The fact that the centre
component remains nontrivial follows from `d(z)=5>|S|`.  Hence connectivity
is exactly five.  The identical argument with two deleted spokes gives
exact connectivity six.

Both hosts exceed the `4|V|-8` density threshold and have order at least
25, so Norin--Totschnig Theorem 6 applies and its `K_{2,2,2,2}` exception
does not.  Making the `K_7^\vee` model spanning is valid.  If either
nominally missing bag pair were adjacent anywhere in `G`, whether already
in the deletion host or after restoration, the bags would form a
`K_7^-` model.  Thus the model is exact in `G`.

The exactly six-chromatic contractions have spanning `K_6` models by
`HC_6`.  On expansion, the star contraction image and remote-edge
contraction image belong to branch sets which may be the same.  The source
now states this qualification and does not claim that the lifted model
exists after those internal edges are deleted.

## 5. Opposite-shore interface

For the component `C` of `G-N[z]` containing `f`, its boundary `Q` is a
subset of the eight-set `N(z)`.  It separates `C` from `z`, so
seven-connectivity gives `7\le|Q|\le8`; the opposite open shore contains
`z`, making the separation actual.

Every nonempty star-only signature has all of its restored defects incident
with `z` and keeps `f` proper, so it restricts properly to `G[C\cup Q]`.
The `f`-only signature has both defect ends in `C`, so it restricts properly
to `G-C`.  Standard colour-name alignment proves rejection in the opposite
directions.  Equality between the remote partition and any star-labelled
partition would glue the two proper closed-shore colourings and six-colour
`G`; the asserted disjointness is therefore valid.

For Corollary 3.5, in a centre-star signature indexed by
`A\subseteq I`, the visible part on `Q` of the colour block containing
`z` is exactly `A\cap Q`.  All other leaves differ from `z` by signature
exactness, and every vertex of `N(z)-I` differs from `z` across a kept
edge.  If two unlabelled boundary partitions coincide, any two nonempty
selected traces are blocks of that same partition and therefore are equal
or disjoint.  The triple and its three two-subsets are pairwise
intersecting and unequal when all three leaves are visible, giving four
star partitions; one singleton and the visible pair give two when only
two leaves are visible.  The remote partition lies outside the whole star
family by the preceding gluing argument.  Hence the claimed totals five
and three do not rely on matching colour names across different
colourings.  This corollary was separately cold-read at the displayed
source hash.

## 6. Trust boundary

The choices of remote edge for different exceptional centres need not be
distinct, form a matching, or occupy prescribed bags of one fixed minor
model.  The result does not close the remaining operation-to-model
allocation theorem, Conjecture 21 or `HC_7`.  These are scope limitations,
not gaps in the proved statements.
