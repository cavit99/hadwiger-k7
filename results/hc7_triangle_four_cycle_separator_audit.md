# Audit of the triangle and four-cycle separator theorem

**Verdict: GREEN — separate cold whole-source internal audit.**
The [complete proof](hc7_triangle_four_cycle_separator.md) was read at
SHA-256 `30c85706951d2ba28fcf3d8834aebece78fb0e4a796012b3d9085dbf03c4b64b`.
No mathematical gap or correction was found. This is internal review,
not external peer review or completion of C19, HC7 or the full objective.

## Inputs and provenance

The parent authored the consolidated statement from route-assessment's
boundary-allocation construction. This reviewer did not develop that
construction and independently checked the entire frozen source.
Both invoked statements and adjacent audits were read; all four pins
match the actual files:

- [Five-root degree-six theorem](../results/hc7_five_root_degree_six.md):
  `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`;
  [audit](../results/hc7_five_root_degree_six_audit.md):
  `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
- [Four-cut theorem](../results/hc7_four_cut_components.md):
  `2986fb1f55c2cbaa4572b7c88e287ed5aa4230f34ab3b63dabe4d840e247e03f`;
  [audit](../results/hc7_four_cut_components_audit.md):
  `7a9d05d3874f6a6da0fabda90493660ee893fb0fd7e29ab5afe8ef42ae3fa437`.

Their recorded literature inspections are inherited. No fresh primary
inspection, finite verification premise or additional reviewer is claimed.

## Strongest checks

1. **Both side hypotheses hold simultaneously.** The two unions C,E
   are nonempty and anticomplete, even when disconnected. Every nonempty
   subset of one leaves the other outside its neighbourhood, giving an
   actual boundary of at least seven. Its side graph omits only two
   possible neighbours, so retains boundary at least five and degree
   at least six. No cut-vertex degree condition is needed.

2. **The returned models have compatible ownership.** Their hosts
   intersect exactly in the three prescribed triangle roots. Each model
   keeps these roots in separate bags. Uniting corresponding bags is
   connected and creates no intersection with any other resulting bag.
   All six contacts between the four helper bags are present: two from
   the side models and four from the literal four-cycle. Distinct
   admissible triangle endpoints can be chosen since each side offers
   at least two. Any two holes then have different triangle ends and
   helper ends in disjoint opposite pairs, so they are independent.

3. **Both applications use actual disjoint bags.** If C misses r, the
   seven-set `(R-{r}) union S` genuinely separates C from the nonempty
   `D union {r}`; that latter set need not be connected. For the second
   construction, `K union {r}` is connected, avoids the packet and D,
   and is full to its five bags. D contacts K, both helper roots and
   at least two triangle roots. Selecting an admissible endpoint among
   these last contacts makes its possible omission independent of the
   packet's possible hole.

4. **The four-vertex shape deduction is exhaustive.** With w the unique
   S-neighbour of r, K={w} excludes degree at least two at w. If wz is
   its sole S edge, K={w,z} excludes both remaining vertices as neighbours
   of z. The component of w is therefore a path, possibly a single vertex.
   A cycle elsewhere can only be a triangle on the other three vertices.

The general theorem needs neither critical colouring nor the particular
degree-eight neighbourhood. The missed-root applications do not cover
two components both full to R. No iterable reduction or global closure
is inferred.

Promotion to `results/` changed only the source status line and audit link;
its mathematical body is byte-identical to the reviewed draft at SHA-256
`33c7c7529403f792f149dc4322a1dee9a6064dd4ac0d4763a80319a41b323238`. The current source hash above includes that editorial change.
