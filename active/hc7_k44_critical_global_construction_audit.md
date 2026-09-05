# Internal audit: critical-host constructions and their stopping points

**Verdict: GREEN** for the corrected internal-edge trace in Section 5 and
the deductions, constructions, literature application and stated nonclosures
in Section 7 of the [designated frontier](hc7_k44_closure_frontier.md).
This is a separate internal audit, not external peer review. It does not
audit the entire frontier or establish any of its global conjectural targets.

**Audited whole-frontier SHA-256:**
`49b39443e977c772609e0561c8700211a3f0b62cbe709e883e4316125d8724ff`.
Checked 5 September 2026. The author restored the required target-free
hypothesis in Section 7.1 before this final revision was checked.

## Quantifiers, colourings and ownership

- An internal-edge seven-cut meets at most six displayed bags, since two
  cut vertices occupy one bag. At least two bags avoid it; they need not
  belong to opposite shores. An avoiding opposite-shore pair lies in one
  component through its model edge. The earlier seven-bag trace lemma
  therefore cannot be applied to this cut.
- For every edge of a seven-contraction-critical graph, both proper minors
  have chromatic number exactly six: five colours would allow one endpoint
  to receive a sixth colour and colour the original graph. Every colouring
  of the edge deletion identifies its endpoints. A Kempe swap separating
  them would colour the original graph, proving all five connections.
  This quantifies anew over every colouring and does not reserve paths,
  fixed colour names, or branch-set ownership.
- The two-component input is necessary and is supplied by the cited
  three-component exclusion, Corollary 2. Identical boundary partitions
  permit colour-name permutations and gluing, giving precisely the stated
  intersection and nonintersection conclusions for the two families.
- Seven-connectivity makes both components full to the seven-cut. The
  audited minimum degree eight excludes singleton components. Contracting
  the opposite component reduces order by its order minus one, so the
  apex graph is a proper minor. The apex excludes its colour from the
  whole boundary. Pullback is only to the untouched side; it supplies no
  colouring of the contracted component and no induction on criticality.

## Minor construction and imported inputs

- In the six-contact construction, zero or one missed label is immediate.
  Two same-shore misses can be paired with distinct contacted opposite
  labels; opposite misses use the crossed pairing displayed in the source.
  Thus both mixed bags and all four pure bags meet the exterior set.
  The only possible core noncontacts are the disjoint pure-shore pairs.
  Every merger uses an original model edge and disjoint original bags.
  This gives `K_7^=`, not necessarily `K_7^-`. For a literal core, every
  exterior component has at least seven core neighbours; the empty-exterior
  case is a seven-connected eight-vertex graph, necessarily `K_8`.
- The two safe-contraction sources match their adjacent GREEN audits:
  [critical safe contraction](../results/hc7_k44_critical_safe_contraction.md),
  `51e9b3b574e44a3a12efa7c986b16b3e40489503501e4f01064417a60eda9a45`;
  [preservation](../results/hc7_k44_safe_contraction_preservation.md),
  `b62fe795c22992858da26ca5eba12e3886b960d782edcf4e5dbaf9cf40ca8ac5`.
  Their target-free hypotheses, exterior-order bounds, degree-nine bound
  and exactly two preserved contractions are retained. The one-edge
  neighbourhood argument does not justify a third contraction.
- The [two-component corollary](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
  and [degree-eight bound](../results/hc7_k7minus_degree7_rooted_helper_closure.md)
  also match their adjacent audits, at hashes respectively
  `1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96`
  and `6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`.
- [Kawarabayashi--Toft's primary publication](https://doi.org/10.1007/s00493-005-0019-1)
  states the seven-chromatic minor alternative in its title and abstract;
  [Norin--Totschnig](https://arxiv.org/html/2507.03244v1) Theorem 3 repeats
  it. Their Theorem 4 and Conjectures 19/21 have the asserted distinct
  targets. Minor-minimal non-six-colourability gives the critical host;
  a full proof of the Section 7 target would therefore prove Conjecture 21.
- [Johnson--Thomas (2.3)](https://thomas.math.gatech.edu/PAP/gener.pdf)
  applies: `K_7^vee` is four-connected, is a proper minor of the
  seven-connected host, has no degree-three vertices, and meets none of
  the exceptional cases. All special extensions need degree-three
  vertices; an addition contains `K_7^-`. The remaining split need not
  be internally four-connected, as Section 3 explicitly warns. The
  edge-partition definition and degree-three triangle obstruction were
  checked; the announced stronger Section 3 theorem is not invoked.

## Remaining obligations

No gap was found in these scoped partial statements. Existing imported
finite inputs retain their recorded status; no new finite result is used.
Missing are an ownership-preserving global completion or closed reduction,
compatible bipartite scheme paths with any additional contact reserved,
and a justified continuation after a split. No decreasing rerouting
parameter or valid iterative lift is proved. Literal `K_7^=` completion
does not settle its arbitrary-model case. T44, Conjectures 19/21 and `HC_7`
remain open here; this checkpoint does not achieve the user's objective.
