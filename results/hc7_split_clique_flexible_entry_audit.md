# Separate internal audit: a flexible deleted colour class

**Verdict: GREEN.** Independent mathematical reconstruction on
23 September 2026 by a separate agent. This is an internal audit, not
external peer review.

## Exact source, scope and input

Audited source: [A flexible fixed colour class in the split-clique
neighbourhood](hc7_split_clique_flexible_entry.md), SHA-256

```text
aeee39e55cbd3962da8a93c48e4075508cadbeaee45ab918f8a98a71a707e49a
```

Promotion changed only the status line and relative links. The mathematical
text is unchanged from the independently reconstructed revision
`b39645f8e56dec21b211e09d44a12dfa4e17aa8e1e7a101894cdbf8d4a419d87`.

The quantifiers checked are: for every finite simple graph satisfying
the source's minor-criticality, K7-minor exclusion and exact split-clique
neighbourhood hypotheses, there exists a choice of `p,B` satisfying
assertions 1 and 2, and every inclusion-minimal induced uncolourable `Z`
for that choice satisfies all the properties in assertion 3. The source
does not assert flexibility for every initial choice of `p,B`.

The one proved input invoked is the fully rooted theorem in
[Bipartite contractibility by graphic-matroid reduction](bipartite_contractibility_via_matroid_reduction.md),
SHA-256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
That hash matches the revision covered by its
[separate internal audit](bipartite_contractibility_via_matroid_reduction_audit.md),
whose current SHA-256 is
`1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`.
The input preserves every prescribed root for any finite bipartite scheme;
no singleton-shore conclusion is needed here.

The earlier three-contact proof is useful provenance, but the source
reconstructs its required argument for `Z`. This audit therefore checks
that argument directly rather than assuming that `Z` is an exterior
component. There is no connectivity, induction or edge-response input.

## Reconstruction of the flexible choice

Contracting `up` produces a proper minor. Its colouring with the contracted
vertex in colour six expands to a proper colouring `c` of `G-u`. Every
other neighbour of `u` avoids six because it is adjacent to the contracted
vertex. Thus the entire sixth class `B` is independent, contains `p`, and
has its other vertices outside `N_G[u]`.

Any five-colouring of `K=G-({u} union B)` extends to `G-u` by giving
`B` colour six. If its boundary `A union D` used fewer than five colours,
giving `u` a missing colour would six-colour `G`. Consequently every such
colouring uses all five boundary colours. With `D` fixed to one through
four, exactly one endpoint of the edge `A` has colour five.

Write the original colours as `a_5,b_j`. If a second colouring gives
`a` another colour, it gives `b` five and proves the required flexibility
for `B`. Otherwise, for each `i`, `a` and `d_i` lie in the same five--i
component of the original colouring of `K`: swapping the component at
`a` would otherwise fix every `D` colour and contradict the forced colour.

Delete instead the entire fifth class `B*` of the same original `c`.
It is independent and meets `N_G(u)` exactly at `a`. In `K*`, the palette
is `{1,2,3,4,6}`, and the identical extension argument forces one of
`p,b` to have six. If `p` were always six, the original colouring would
give a six--i path from `p` to every `d_i` as well.

These eight paths are all selected under the same original colouring
`c`; they are not taken from independently relabelled colourings. Their
six prescribed roots `a,p,d_1,d_2,d_3,d_4` have distinct colours. Each
path uses only the colours of its endpoints, so it contains no other
root, and every family of paths meeting at a vertex has the root of that
vertex's colour as a common target endpoint. They form a `K2,4` scheme
in `G-u`.

The rooted input gives six disjoint bags. Its eight cross-shore contacts,
the actual edge `ap`, and the six edges within `D` provide all fifteen
contacts of a `K6` model. The singleton `u` is disjoint from those bags
and adjacent to every one through its retained root, giving `K7`.
Thus `p` is not forced to have six in `K*`. A colouring where it avoids
six gives `b` six; the original colouring gives `p` six and `b` another
colour. Exchanging the names five and six and renaming the deleted vertex
gives exactly assertions 1 and 2 with one fixed independent deleted class.
No criticality of `K` or `K*` is used or asserted.

## The list obstruction and its four contacts

All neighbours of the component `X` in `K-X` lie in `D`. An L-colouring
of `X` would therefore combine with either fixed colouring of `K-X`:
the lists exclude precisely the relevant fixed `D` colours and additionally
exclude five at `a,b`. This would contradict assertion 2. Hence a minimal
induced uncolourable `Z` exists.

If `a` were absent from `Z`, the colouring with `a_5` and `b` avoiding
five would respect every list on `Z`. The opposite colouring excludes
the possibility that `b` is absent. Connectedness follows by colouring
components separately. The inequality `d_Z(v)>=|L(v)|` follows by extending
an L-colouring of the proper induced subgraph `Z-v`; it does not require
such a colouring to extend anywhere outside `Z`.

Fix any proper colouring of `G[Z union D]` that assigns `d_i` colour `i`.
Its restriction to `Z` would be an L-colouring unless one of `a,b` has
five. As `ab` is an edge, their colours are exactly five and some `j`.
If `Z` misses `d_i` with `i != j`, swapping five and `i` on all of `Z`
preserves properness in this restricted graph: `D` has no five, and `Z`
has no edge to its root of colour `i`. It removes five from both A vertices,
a contradiction. Thus if `Z` misses any D vertex, it misses exactly one,
say `d_4`, and every compatible colouring forces A to use exactly four
and five. This conclusion is about every compatible restricted colouring,
not only ones that extend to all of `K`.

Now choose one actual global colouring of `G-u` obtained from assertion 1,
with `a_4,b_5,p_6` and `Q=D-{d_4}` in colours one through three. For a
fixed `q_i`, consider the four--i component at `a` in `G[Z union Q]`.
If it missed `q_i`, swapping it would still give a compatible colouring
of `G[Z union D]`. No other Q root has either swapped colour; the component
has no edge to a vertex of these colours outside itself in `Z union Q`;
and `Z` has no edge to `d_4`. The swap would change the forced pair of
A colours. Hence an `a--q_i` path exists in this original layer. The
five--i component argument gives the corresponding `b--q_i` path.

These swaps are hypothetical tests confined to `Z union D`. Their
possible conflicts with `X-Z` are irrelevant: no swapped colouring is
extended to `K` or used to select another path. All six paths just forced
are chosen in the restriction of the same unswapped global colouring.

For each `i=1,2,3`, the global six--i component at `p` must contain `q_i`.
Otherwise swapping it in all of `G-u` removes colour six from `N_G(u)`:
`p` is the only boundary vertex of colour six, and `q_i` is the only one
of colour `i`. Colouring `u` six is then a contradiction. These three
paths are selected in the same global colouring as the six restricted
paths. Their colours exclude `a,b,d_4`, and all nine paths avoid `u,d_4`.

## Scheme compatibility, ownership and scope

The nine simple paths form a `K3,3` scheme with prescribed roots
`P={p,a,b}` and `Q`. The six root colours are distinct. At a common vertex
of any collection of paths, its single global colour identifies a root
that is an endpoint of every path in that collection. This verifies the
full intersection condition, not just disjointness for pairs of target
edges without a common endpoint. No other prescribed root can be internal
to a path because its colour is outside that path's endpoint palette.

Applying the rooted theorem in `G-{u,d_4}` gives six pairwise disjoint
connected bags containing their six distinct prescribed roots. The nine
P--Q contacts and the three literal edges of each triangle give all
fifteen `K6` contacts. Adding the singleton bag `{u}` supplies the remaining
six contacts through the prescribed roots. Neither growth of a rooted
bag nor a reused vertex among scheme paths creates an ownership problem:
the input theorem supplies disjoint bags and retains all roots.

No gap was found in the asserted universal existence of a flexible class
or in the four-contact conclusion for every minimal `Z` arising from that
class. No additional hypothesis beyond the stated graph assumptions and
the pinned rooted input is required.

The result supplies neither an L-colouring of all of `X-h` nor a compatible
original-host edge-deletion colouring. It does not make `Z` minor-critical
or supply an induction and lift. A minimal list obstruction contacting
all four roots is the remaining construction problem, not a completed
split-clique case or a proof of `HC_7`.
