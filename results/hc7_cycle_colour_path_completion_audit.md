# Internal audit of the two cycle-and-triangle path completions

**Verdict: GREEN.** This audit pins
[the source](hc7_cycle_colour_path_completion.md) at SHA-256
`a7f4a6df568ffa1c9158a1714c2e2b0b71a74f940a2c149ee586bba30aaefa31`.
The mathematical text is byte-identical to the fully reviewed active
revision `a7b7b52aaa4c1f4019de5f39f080a3905564eb1dfd8409e177c6d6c364e01bb1`
after removing the status paragraph and normalizing its three moved links.

## Review provenance and inputs

The `literature_repair` agent directly read and checked the whole source,
including both main theorems and the critical-colouring corollary. During
review it also independently derived the one-hair auxiliary used in the
root-hit repair. Separately, `route_assessment` reported a cold whole-file
GREEN verdict on the same active revision, covering Sections 1–7. That
second verdict is recorded as a separately reported review, not as another
review performed by this audit's writer. Both reviewers independently
verified the status-and-links-only transition to the pinned promoted source.
Neither review is external peer review.

The three source pins were checked against the files:

- [Universal bipartite contractibility](bipartite_contractibility_via_matroid_reduction.md):
  `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
- [Marked scheme completion](hc7_marked_k33_scheme_completion.md):
  `fb55cc00b52e0f3fb6f6e547f08b29ed6aae37cb25c4176a7c7fb96ada05dc2f`.
- [Reserved-triple colouring construction](../active/hc7_degree8_cycle_triangle_construction.md):
  `b3c43b4682c4554c2100d75dd14ea9df07aa898686b1cb6e3a1d9603985f68fe`.

## Strongest inference checks

- **Auxiliary dependencies.** L and C work for every omitted cross-edge:
  an unused marker completes the literal path on the three `B` roots,
  while a root-marker component uses the complete remaining `K_{2,3}`
  core. H is proved independently using L when its hair reaches root `4`.
  Theorem 1 then precedes Theorem 2. No induction cycle is present.
- **Root-hit repair.** A prefix of `L3` ending at `3`, or at `2` followed
  by `23`, avoids its original endpoint `0`. If the other hair avoids
  `0`, discard the unused suffix before absorbing `0` into root `4`.
  H applies with the remaining marker `2`, even if that marker also lies
  on the main path. The argument does not invoke a two-marker theorem
  after one marker has already been absorbed into a root preimage.
- **Normalization and descent.** A single-membership `a1` or `a2`
  nonroot lies on no other retained path. Its contracted triple contains
  at most one prescribed `B` root and no marker or `v`. Walk cleanup is
  followed by the required terminal checks and fresh rank counts.
  Restricted reverse grounds exclude endpoint markers; all remaining
  labels are actual internal nonloops. Every recursive reduction therefore
  strictly decreases path-union order, preserving its induction class.
- **Projection reductions.** The hair projections are connected through
  their actual intersections with the old core. Their endpoint occurrences
  are not silently counted as reverse edges. Removed internal traversals
  are replaced inside their specifically allocated connected components.
  A marker collision uses C with a connected original preimage; the
  abstract identification of the two markers is never contracted in `G`.
- **Rank-one allocation.** The normalized two-projection component count
  proves simultaneous full rank. Augmentation retains the old union of
  labels and takes its new label from `I_0`, since every ground label was
  allocated. Every ordinary maximum connects the markers, by the modified
  rank inequality. Hence the exchanged `I_0` has exactly two components,
  with both markers together. All three size ranges are exhausted.
- **Actual terminal bags.** In the separate-root case retain the vertex
  `k` inside the marked component, not its foreign-owned adjacent label.
  A marked leaf different from `k` can be transferred while preserving
  the other marker and the contact at `k`. The cut edge restores the third
  cross-contact. The possible missing pairs lie in different shores, and
  every final bag meets `v` through an original named neighbour. The final
  `Q` construction may merge original roots; no fully rooted `K_{3,3}`
  conclusion is asserted for that terminal operation.
- **One-swap corollary.** All bichromatic paths used by either theorem
  belong to the same original reserved-triple colouring. In the second
  case the swapped neighbourhood vertices are exactly `a0,2,3`, giving
  the stated two pairs and the explicit dihedral relabelling. The new
  repeated cycle partner is not their common cycle neighbour. No old
  model is assumed to survive the recolouring.

No unresolved mathematical gap was found in these statements. They prove
two conditional path completions and the specified one-swap reduction.
The subsequent two-pair critical-host construction remains unproved; this
audit certifies neither Conjecture 19, Conjecture 21, `HC_7`, nor a novelty
or significance comparison with the Norin–Totschnig paper.
