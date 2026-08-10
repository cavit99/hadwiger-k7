# Internal audit: Boolean replacement cuts and critical-edge colourings

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_k7minus_boolean_replacement_edge_coupling.md`](hc7_k7minus_boolean_replacement_edge_coupling.md)

**Audited source SHA-256:**

```text
c155030145a46a70c789302188a3220af2bf8ca5c537ad1c78d2325fa33946da
```

This is a separate internal mathematical audit, not external peer review.
Three independent passes reconstructed the path, colouring, separator and
minor-model arguments.  The mathematical revision independently audited as
GREEN had SHA-256
`8b0a3282c0ace6e54cb8ed6c8a6876f63cd179afc90091ec923122c0e2a8a204`.
The final revision only removes trailing spaces and restores the closing
display-math delimiter after (4.3); its statements and proofs are unchanged.

## Pinned inputs

The local inputs have adjacent GREEN audits at these source revisions:

- common colouring and simultaneous replacement cuts:
  `8c1c27b99edbd5b73ccc6254eafb10dfddeed62d3b271e4e8ba527783a08412a`;
- localisation at an order-six cut:
  `f2a4480d27556996620117a68a8a7924dd61cf37bf5ec9e8cce4c953dfcc88af`;
- palette linkage at a non-double-critical adjacent pair:
  `2b0c30b9d8566f6da4959df145bf0f527249bf887dfa844d19a98e524080a9f2`;
- bichromatic connections after two named edge contractions:
  `753dbf0fc251584dac8a67d907988737ac8dda30daa3dcc24b6fbabd949cf467`.

The use of Hadwiger's conjecture for chromatic number six is supported by
Robertson, Seymour and Thomas, *Combinatorica* **13** (1993), 279--361,
<https://doi.org/10.1007/BF01202354>.

## 1. Common linkage coordinates

For fixed `P` and `R subseteq W_P`, the vertices `a` and `b` lie on opposite
sides of every separator `S_W`, `W subseteq R`.  Seven-connectivity gives
seven internally disjoint `a`--`b` paths.  Since each `S_W` has order seven,
every path meets it once and the seven intersections exhaust `S_W`.

Comparing `S_emptyset` with `S_{\{u\}}` fixes six path labels and puts
`u,x_{uP}` on the seventh path.  The orientations of the two exact cuts
show that `x_{uP}` immediately precedes `u`; hence their literal edge is a
path edge.  Distinct coordinates start on distinct vertices of
`S_emptyset`, so their edges lie on distinct paths.  This proves the full
Boolean-family statement, not only the four-cut square.

## 2. Endpoint signatures and shore restrictions

The replacement edges form a matching.  Contracting any nonempty subset
and colouring the resulting proper minor gives equal colours exactly on
the contracted pairs after the matching edges are deleted.  If every pair
had different colours, restoring the matching would six-colour `G`.

For a coordinate `u`, the closed side `A_W` contains both endpoints exactly
when `u notin W`, while `B_W` contains both exactly when `u in W`.  This
gives both equivalences in (3.3).  Each separator contains one endpoint of
every replacement edge, so every induced boundary colouring is proper.
No proof step identifies the colourings belonging to different signatures.

## 3. One-coordinate deletion

After deleting `ux`, the displayed six-set `Q` separates exactly the two
full connected components `L,R'`.  The edge `ux` was their only cross-edge.
If at most five vertices disconnected the deletion graph, adding `ux`
would place its endpoints in the two resulting components.  Neither
endpoint component can be a singleton by minimum degree, and adjoining
one endpoint to the alleged cut contradicts seven-connectivity.  Thus the
deletion graph is six-connected and exactly six-chromatic.

A `K_5^-` model in `G[Q]`, together with the two full sides and `ux`, would
give a `K_7^-` model.  The order-six localisation theorem therefore applies
and yields the five-vertex and six-vertex boundary bounds.  With
`sigma=|E(G)|-4|V(G)|`, its exact accounting identity becomes

\[
 \delta_L+\delta_{R'}=\sigma+23-|E(G[Q])|\ge\sigma+12.
\]

Every common neighbour of `u,x` lies in `T_P`, so there are at most three.
A five-colouring of `G-\{u,x\}` would force a common neighbour in each of
its five colour classes: otherwise one class can be recoloured with a fresh
sixth colour and `ux` restored.  Hence `chi(G-\{u,x\})=6`, as claimed.

For the endpoint-type proposition, boundary colour names may be aligned and
the unused names permuted independently.  The only failures are a common
named boundary colour or the sole colour absent from a five-block boundary.
If the common endpoint colour is absent from `Q`, the five two-colour
endpoint paths cross `Q` in all five other colours.  Six boundary vertices
therefore induce partition shape `2+1+1+1+1`.

## 4. Two-coordinate deletion

Deleting both replacement edges leaves the exact five-set `F` and the two
full components stated in Corollary 5.1.  For a cut of order at most four,
the component graph becomes connected after two edges are restored and has
at most three vertices.  Removing the appropriate crossing endpoint or
endpoints then gives a cut of `G` of order at most six.  The only apparent
exception would force `|V(G)|<=8`; seven-connectivity would then make `G`
equal to `K_8`, which already contains the excluded minor.  Thus the common
edge-deletion graph is five-connected.

A five-colouring can be repaired at the independent vertices `u,v` with one
fresh colour, contradicting `chi(G)=7`; hence the graph is exactly
six-chromatic.  The three nonempty endpoint signatures and the forbidden
fourth signature follow from the contraction argument.  The audited
two-edge theorem gives three bichromatic connections for one pair, or four
when `xy` is a cross-edge between the contracted pairs.

## 5. The `P_4` and `C_4` adjacency subcase

If `xy` were an edge, use the five disjoint pieces, replacing `P` by
`P-\{x,y\}`.  Fullness of the replacement cut preserves every interaction
edge incident with `P` and every adjacency from the two unused centres to
the modified piece.  Adding those centres to `C` and to a suitable region
makes the corresponding two branch sets universal among the five pieces.
The other three regions induce `P_3`, so the five piece bags miss at most
one adjacency.  The connected bags `\{u,x\}` and `\{v,y\}` meet each other
through `xy` and meet all five piece bags.  The seven bags form a
`K_7^-` model.  The same construction leaves two missing pairs for `2K_2`,
so the proposition correctly excludes that case.

## Scope

The note does not prove the proposed one-edge vertex-transfer lemma.  Its
proper-minor colourings need not have aligned boundary partitions, and the
replacement square need not be based at the minimum selected component.
The remaining task is to turn the endpoint-type obstruction into matching
shore partitions, the prescribed rooted `K_6^-` model, or strict
trace-preserving descent.  No unresolved assumption or gap remains in the
stated results.
