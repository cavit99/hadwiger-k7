# Internal audit: critical-host constructions and their stopping points

**Verdict: GREEN** for the corrected internal-edge trace in Section 5 and
the deductions, constructions, literature application and stated nonclosures
in Section 7 of the [designated frontier](hc7_k44_closure_frontier.md).
This is a separate internal audit, not external peer review. It does not
audit the entire frontier or establish any of its global conjectural targets.

**Audited whole-frontier SHA-256:**
`1bc6088dad59d66394442d2c9610251571d4484147040a335da3e745751777ed`.
The latest 7 September 2026 addendum audits only the added transfer
paragraph in Section 7.6 and new Section 7.8. Removing those exact additions
recovers Git `672e779`, with SHA-256
`acb131d53c6f323e3ee23c144d7c049381fe5558b5c6331bc79c1e12ae189166`.
All other bytes are unchanged; this was checked against Git directly.

The preceding 7 September 2026 addendum audited Sections 7.6–7.7 at that
preceding whole-frontier hash.
Removing those sections exactly recovers Git `46669f6`, with SHA-256
`87c8d865dc3ffa0b109c3462af211fafe12930ae42d0173ded67e3ca1635d5e0`;
this equality was checked against Git, not inferred from the author's
description. All previously audited text is byte-identical.

The earlier 7 September 2026 extension audited only new Section 7.5 at
that preceding whole-frontier hash. Removing that
section exactly recovers the frontier at Git `HEAD=9307ce3`, with SHA-256
`49b39443e977c772609e0561c8700211a3f0b62cbe709e883e4316125d8724ff`.
Sections 5 and 7.1–7.4 are byte-identical. Their 5 September audit and
literature checks below are retained, not newly repeated. The author had
restored the required target-free hypothesis in Section 7.1 before that
earlier revision was checked.

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

## Section 7.5: singleton-vertex criterion and nonclosure

For the six specified bags, `q` counts those intersecting `N_G(v)`.
The seven bags including `{v}` have exactly `e+q` contact pairs. At least
twenty is necessary and sufficient for these bags to model `K_7^-`.
Since `e<=15` and `q<=6`, the alternatives are precisely `e=15,q>=5`
or `e=14,q=6`. This does not constrain a model in which `v` belongs to a
larger bag, and it proves no existence or monotone exchange theorem.
The [separately audited capacity family](../barriers/prescribed_clique_roots_capacity_audit.md)
refutes the general prescribed-root claim, with first parameter `t=9`.
It does not refute the six-clique five-root proposal or a flexible choice
of neighbours. Menger paths require an additional ownership-preserving
construction; neither distinct selectors nor positive probes supplies it.
No online literature or finite enumeration was used for this addendum.

## Sections 7.6–7.7: 7 September 2026 scoped addendum

**Verdict: GREEN** for the two new sections, within their expressly partial
scope. This check does not renew the older literature or finite-result
audits and does not assert a global completion.

Section 7.6 accurately applies the
[deficient-bag reduction](../results/hc7_near_clique_deficient_bag_normalization.md)
at SHA-256
`537e885c1ef8930fadde8a8bf12423044e8d20a99b6c2f78a4b379e17870c4f2`.
Its [separate audit](../results/hc7_near_clique_deficient_bag_normalization_audit.md)
checks the complete promoted source, including the added no-triangle
conclusion. Three-connectivity and absence of a `K_7^-` minor are retained.
The reduction fixes the two missed bags, enlarges the other original core
bags only by inclusion, and shrinks `D` inside its original vertex set.
The minimum order-two conclusion is about the component outside the core;
it does not assert that the deficient edge is a bridge of the whole host.
The six-neighbour assertion counts actual vertices in two bags. Neither
it nor the absence of a triangle supplies a small separator or a
connectivity-preserving contraction. The frontier states these limits.

For Section 7.7, the existing
[paired-colourful barrier](../barriers/hc7_paired_colourful_planar_core_barrier.md)
was read at SHA-256
`25d436688ed47f624fafc465249165ac889c43839e1c3a83d4930a90f1118630`.
Only its explicit core and written Propositions 2.1–2.2 are used here.
The unique independent triple `012`, together with the complementary
six-cycle on the other vertices, gives exactly the two displayed
four-colour partitions, in both of which each marked set meets every
colour. For the paired model, its common marked vertex `0` must form a
singleton bag. The six possible root pairs for the other three bags
have only the two displayed perfect matchings, each of which requires
two bags to own the same additional vertex. This independently confirms
the paired-model exclusion; it permits unused vertices and arbitrarily
chosen connected bags. The explicit core's four-connectivity is also
consistent with its edge list: its minimum degree is four, and its
complement gives any two vertices at most two common neighbours. Thus
it has no complete bipartite subgraph on side sizes `2,4` or `3,3`,
excluding the remaining possible separations of order at most three on
nine vertices. The extension's computer-assisted exclusion of
an unrooted `K_6` minor is not invoked or re-audited.

The list-extension assertion has the following exact elementary meaning.
For a vertex partition `V(G)=V(R) union P` and a proper colouring
`phi:V(R)->{1,...,6}`, define

```text
L_phi(p) = {1,...,6} minus phi(N_G(p) intersect V(R)),  p in P.
```

The colouring `phi` extends to a six-colouring of `G` exactly when
`G[P]` has a proper colouring from these lists: the lists enforce every
cross edge and properness enforces edges inside `P`. Consequently `G`
is not six-colourable exactly when every such `phi` has no list-colouring
extension. Restricting the check to core colourings using at most four
or five colours checks only a subfamily, hence supplies only a necessary
condition for non-six-colourability. This is the precise sense of the
frontier's lost colouring responses; it does not assert that a
seven-chromatic host itself has a five- or six-colouring. The barrier
refutes simultaneous selection from colourful-set information alone,
not a construction using these full extension obstructions.

No new external input or finite minor search supports this addendum.
There is no identified gap in the two scoped additions. The global
singleton and two-pair constructions, and the conversion of full
colouring obstructions into compatible minor models, remain open.

## Section 7.6 transfer paragraph and Section 7.8: scoped addendum

**Verdict: GREEN** for these additions at the current whole-frontier hash.
The [transfer and centroid source](../barriers/hc7_near_clique_global_exchange.md)
remains at SHA-256
`6e48f030621358a37d99a963dc2125999a1decabed31bb6921df30e6a396e076`.
Its [adjacent audit](../barriers/hc7_near_clique_global_exchange_audit.md)
checks the full construction. The summary retains its companion-target
scope, valid connected transfer, exact gain/loss classification and absence
of a decreasing continuation. The centroid examples refute only the
specified weaker conditions, not seven-connectivity or a critical host.

For Section 7.8, triangle-freeness makes `S,T` disjoint. Deleting the two
endpoints lowers connectivity by at most two, and every remaining vertex
loses at most one neighbour, giving the stated connectivity and degree
bounds. Proper-minor colourability gives `chi(F)<=6`. In a hypothetical
five-colouring, the recoloured part of `S` is independent and has no
neighbour at `y`; the fresh colour causes no conflict elsewhere. Giving
the freed colour to `x` and the fresh colour to `y` therefore colours every
edge of `G`, proving `chi(F)=6` by contradiction.

The six detours also exist for adjacent endpoints. Deleting one edge
from a seven-connected graph leaves a six-connected graph: after deleting
at most five vertices, the original remaining graph is two-connected,
so removing that edge cannot disconnect it. Apply nonadjacent Menger to
`x,y` in `G-xy`, then remove the endpoints and truncate if necessary.
This gives six vertex-disjoint `S`--`T` paths in `F`, with no assertion
that they are bichromatic.

The missing-colour law quantifies over every six-colouring of `F`. Two
distinct representatives extend to the adjacent endpoints; if both sets
are nonempty and no such representatives exist, each is the same singleton.
Two colours absent from `S union T` would contradict that law. Deleting
vertex `0` from the recorded barrier removes `03,0w` and leaves only `s3`
missing, so its stated `K_7^-` subgraph is present.

All three sufficient constructions have disjoint connected bags and
actual endpoint contacts. A `K_6` plus `{x,y}` has at least `15+5=20`
contacts. A four-rim wheel plus the two singleton endpoints has all
contacts except the two disjoint rim diagonals. Replacing that wheel by
`K_5^-` leaves just one missing contact. None of these counts proves
existence of the stipulated models or preserves them through arbitrary
path contractions. No new external source or finite enumeration was used.

## Remaining obligations

No gap was found in these scoped partial statements. Existing imported
finite inputs retain their recorded status; no new finite result is used.
Missing are an ownership-preserving global completion or closed reduction,
compatible bipartite scheme paths with any additional contact reserved,
and a justified continuation after a split. No decreasing rerouting
parameter or valid iterative lift is proved. Literal `K_7^=` completion
does not settle its arbitrary-model case. T44, Conjectures 19/21 and `HC_7`
remain open here; this checkpoint does not achieve the user's objective.
