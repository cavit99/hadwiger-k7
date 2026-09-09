# Audit of the four-root degree-five exception theorem

**Verdict: GREEN — separate internal audit of the complete written proof.**
No mathematical gap or source correction was found. This is internal
review, not external peer review or a conclusion about C19 or HC7.

## Exact source and provenance

The reviewed source is [the four-root proof](four_root_degree_five_exceptions.md),
SHA-256 `a9bda26dcd8057cad14e2b52b33bec0700ecf8b2c64d60642afd1962e7d34067`.
Route-assessment independently read the complete source after its
construction and did not develop or edit its proof. The review checked
the reductions and their small endpoints, the four-root alternatives,
and the planar degree count. No finite computation is a proof premise.

The recorded Norin--Totschnig Theorem 8 input and its audit were read and
their hashes checked against disk:

- [Recorded statement](../results/hc7_five_root_almost_clique.md):
  `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`.
- [Input audit](../results/hc7_five_root_almost_clique_audit.md):
  `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.

This review relies on that pinned primary-source inspection; it does not
claim a fresh literature inspection. In particular the trisection has a
common two-vertex intersection and no edges between its open parts.

## Strongest checks

1. **Two-nonroot endpoint.** Both nonroots are universal. Any root edge
   gives the displayed four disjoint rooted bags; without a root edge,
   at least two root bags are singleton and cannot contact. Thus the
   exceptional graph is exactly `K2 join I4`. One nonroot cannot have
   degree five in a graph with only four other vertices.
2. **Both reductions close.** A surviving nonroot has no adjacency to
   the old absorbed root, so replacing the absorbed nonroot by its root
   image preserves every surviving degree and nonroot-set boundary
   injectively. The number of degree-five exceptions cannot increase.
   At the first reduction's two-nonroot endpoint, the merged root has
   degree at least four, excluding the exceptional graph. In the
   trisection reduction, the two cross edges produce an actual edge
   between the merged roots, also excluding that endpoint. A remaining
   singleton nonroot contradicts its preserved degree bound. The root
   preimages are disjoint and connected, and nonroot order decreases.
3. **Trisection normalization.** Nonroots in an isolated-root open part
   would have at most three neighbours. If the common two-set contained
   a root, the nonempty remaining nonroot set would likewise have at
   most three neighbours. Thus both ports are nonroots, and both
   isolated roots see exactly those two ports after normalization.
4. **The facial count is strict.** Normalized roots have two nonroot
   neighbours. After any one deletion every component contains a
   nonroot, and the four-neighbour bound forces at least three roots
   into each component. This proves two-connectivity. With facial
   length `4+h`, the upper bound is `2e<=6|D|+10-2h`; the lower bound
   is `6|D|-5+8+max(0,8-2h)`. Their difference is exactly one for
   `h<=4`, and at least one for `h>=4`. Root-to-nonroot incidences and
   facial root-to-root incidences are counted separately.

## Scope

The conclusion requires at least three nonroots, the boundary condition
for every nonempty nonroot subset, and at most five degree-five
nonroots. It supplies one rooted K4. It does not preserve a reserved
complement or the hypotheses of an arbitrary subsequent contraction,
and it does not close the current critical-host construction.

Promotion to `results/` changed only the source status line and audit link;
its mathematical body is byte-identical to the reviewed draft at SHA-256
`98256f47d7f0fdd449710fc63432e930e5f99acc598e9199ca391a626a295bdb`. The current source hash above includes that editorial change.
