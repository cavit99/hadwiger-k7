# Audit: colourful sets, a three-connected minor and a rooted wheel

Date: 9 September 2026.

**Verdict: GREEN — separate internal mathematical review.** The reviewed
[source](colourful_five_wheel.md) has SHA-256
`d804335fc68cff69d4eb2de770c246cbb91e0da336eb36a206d93d89378a64a1`.
No unresolved inference was found within its stated hypotheses.

## Strongest checks

- The proof retains the full induction class: ordinary k-colourability
  and absence of a colouring whose marks avoid one special colour.
  Fixing an ordinary colouring before each two-cut replacement certifies
  colourability of either the equal-port quotient or the added-edge side.
- With two internal marks on each side, both ports can be marked
  simultaneously; permitted side colourings would align by permutations
  fixing the special colour. With at most one internal mark on the
  discarded side, the colour-dependent port-mark rule suffices. If that
  mark shares neither port colour, k-1>=3 leaves an unused old colour.
  This checks the endpoint k=4 as well as the full uniform range.
- Two-connectivity gives the disjoint paths to two distinct marks; a
  failed linkage would yield an actual cutvertex. Connected partitions
  of the removed side realise virtual edges and new marks simultaneously.
  Their preimages avoid the retained interior and compose, preserving
  connectedness, disjointness and an original mark in each marked preimage.
- Each replacement strictly decreases vertex count. The induction ends
  by retaining a three-connected pair itself, without any rooted-wheel
  assumption. Its chromatic number is exactly k, so it has at least four
  vertices. Thus the conclusion is the stated marked minor, not merely
  a target-specific reduction.
- The five-colour corollary applies the pinned three-connected input and
  lifts its wheel. For every whole class of every six-colouring, deletion
  leaves chromatic number exactly five and preserves universal
  colourfulness of the surviving set. The deleted class contains a mark
  outside the wheel. The critical-host application uses vertex-deletion
  criticality and the missing-colour extension at v.

## Attribution, inputs and scope

The reviewer directly inspected Martinsson–Steiner,
[Claims 3.8–3.10](https://arxiv.org/html/2209.00594v1#S3). Their four-colour
proof contains the fixed-colouring separator replacements, disjoint
marked path lifts and colour-dependent one-mark transfer. The source
correctly presents the k>=4 formulation as an adaptation of that argument,
not a new separator method. The uniform range and composed marked-minor
conclusion were checked in the complete current proof.

Only the five-colour wheel corollary additionally invokes Section 7 of
[the rooted-wheel theorem](hc7_rooted_wheel_extension.md), source SHA-256
`f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`;
its [audit](hc7_rooted_wheel_extension_audit.md) has SHA-256
`c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178`.
Both pins were checked. That corollary carries the Martinsson–Steiner
Theorem 1.3 and rooted-wheel-extension dependencies.

The reviewer did not author the present separator adaptation, but
participated in earlier rooted-wheel development and audits. This is a
separate whole-source internal review, not external peer review.

The wheel's hub, rim order and representatives are not prescribed.
Other marks may lie inside returned bags; only the deleted class is
guaranteed unused. No sixth compatible bag, C19 closure, priority for
the wheel corollary or NT-comparable significance is established.
