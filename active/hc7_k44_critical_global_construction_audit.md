# Internal audit: critical-host constructions and their stopping points

**Verdict: GREEN** for the corrected internal-edge trace in Section 5 and
the deductions, constructions, literature application and stated nonclosures
in Section 7 of the [designated frontier](hc7_k44_closure_frontier.md).
This is a separate internal audit, not external peer review. It does not
audit the entire frontier or establish any of its global conjectural targets.

**Audited whole-frontier SHA-256:**
`0354f788194a76d32cbd9c919e72fa4e99fcf9fa20eb62cee53cfe1787a668c4`.
The latest check covers only the final marked-scheme completion, failed
Kempe connections and projection nonclosure block before Section 7.6.
Removing it exactly recovers Git
`0f93db9`, at SHA-256
`49f5a7c6415e1c997d0abc733251a38c848398fa60a6cf15c0a20e8c149a875c`.
This byte equality was checked directly against Git.

The preceding check covers only the two-triangle exterior and colouring
nonclosure block before Section 7.6. Removing it exactly recovers Git
`1927a6f`, at SHA-256
`7d0db666392bd8a4dd3083412b07fb38181ff67a68b70b8fea46d29a52fe29f3`.
This byte equality was checked directly against Git.

The preceding check covers only the almost-clique, connected-exterior and
contracted-cycle nonclosure block before Section 7.6. Removing it exactly recovers Git
`dfb86b7`, at SHA-256
`0a732e450f1297a031817261db2e4fc511a067fb3c55fee9bdd46ef9f11c4be6`.
This byte equality was checked directly against Git.

The preceding check covers only the rooted-wheel paragraph before Section 7.6.
Removing it exactly recovers Git `18b4b70`, at SHA-256
`7a9ecfcea0737ce1eab51d954e1f7ee5d1addcdaaa4e84275501ca694d387e21`.
This byte equality was checked directly against Git; all earlier audited
mathematics and provenance are retained.

The preceding check covers only the 24-line neighbourhood-construction block
before Section 7.6. Removing it exactly recovers Git `8da9ebe`, at SHA-256
`62856b184e5705a0cb43f6168e844f9f8b2280340e260958adfde36f90af4318`.
This byte equality was checked directly against Git; all earlier audited
mathematics and the prior provenance below are retained.

The preceding check covers only the new cut deductions and matching criterion
in Section 7.3, expanded density navigation in Section 7.4.1 and the new
companion-candidate block in Section 7.5. Removing both new blocks and
reversing the navigation expansion exactly recovers Git
`8affc0b`, at SHA-256
`83762eaecfd641df2c82bdf924cbf67cf30179f03f3543fa3a4aa39bbc22f46c`.
This byte equality was checked against Git. Earlier audit provenance and
checks below are retained; no older mathematical section was changed.

The preceding scoped check covers only the added three-full-helper criterion
and density-route navigation at the end of Section 7.4.1. Removing those
additions exactly recovers Git `623110a`, at SHA-256
`ccb152686832e05f93555162259977b3ad0dd5d094d2ba5afa463f10d2a91ad8`.
This byte equality was checked directly against Git; all older audited
text is unchanged.

The preceding scoped check covers new Section 7.4.1 and the change from
"The current structural target" to "A retained structural target".
Removing the new subsection and reversing that wording exactly recovers
Git `285f934`, with SHA-256
`da9865bc6e673487b10670e19bb41b3117f56cbfe19963a235aa84e9d9a571de`;
this byte equality was checked directly against Git.

The preceding 7 September 2026 check covers only the new navigation paragraph
in Section 7.4. Removing that paragraph exactly recovers Git `3e0a909`,
with SHA-256
`1bc6088dad59d66394442d2c9610251571d4484147040a335da3e745751777ed`.
The Git diff and byte equality were checked directly. All previously
audited mathematics is unchanged. The two linked drafts have separate
adjacent audits; this navigation check does not extend the scope of the
present audit to their complete statements.

The preceding 7 September 2026 addendum audits only the added transfer
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

## Section 7.4.1: contraction closure and the four-clique laboratory

**Verdict: GREEN** within the stated conditional scope. Literal `K_5^-`
exclusion limits every outside vertex to two neighbours in the four-clique,
so the critical host's minimum degree eight gives `delta(G-R)>=6`.
For `J=G-R`, its order is at least seven and `e(J)>=3|V(J)|` exceeds
the retained `K_5`-minor-free bound `3|V(J)|-6`. That external input is
recorded in the linked source at SHA-256
`069bfa0dd96211d44e762cc49aaa2476a4e655f52ba45e63e492bb6445411023`,
matching its adjacent audit; its primary literature was not newly checked
in this scoped update. Three disjoint connected adjacent outside bags
with at most two independent missing root contacts give the claimed
seven-bag minor. The six remaining contacts after the proposed two
cross-mergers are real ownership obligations, not supplied by endpoint
counts. The retained critical-host Corollary 3 at SHA-256
`6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`
does supply a degree-eight vertex: it proves `n_8>=25+tau` with `tau>=0`.
Its hypotheses hold because companion-minor exclusion implies
`K_7^-`-minor exclusion. Combining this with the new neighbourhood result
places a literal four-clique in every critical companion-free host.
Consequently the proposed universal four-clique construction would close
Conjecture 19; that construction itself remains unproved.

The linked five-connected helper, connected-set, two-edge and neighbourhood
proofs have separate adjacent audits. Their summarized conclusions retain
their host and independence hypotheses. Quotient preimages are connected
and disjoint, and order decreases, but these facts do not retain criticality
or minimum degree. A four-cut of a four-vertex-set quotient must contain
the merged vertex, since otherwise it would lift to a four-cut of the
seven-connected original graph. Replacing that vertex by its four original
vertices gives an actual order-seven separator with both open sides
unchanged. Thus the stated next connectivity obstruction and non-iteration
warning are valid. No global existence or closed reduction is established.

## Remaining obligations

The latest additions are **GREEN** within their explicit partial scope.
Here `G-R` is connected. Three disjoint connected full-root sets can be
extended to a partition by a spanning forest rooted at those sets. Each
bag stays connected and keeps its four contacts, and their three-vertex
contact graph is connected. Thus it misses at most one edge, and the four
literal clique roots give the displayed `K_7^-` model. This is a sufficient
criterion, not an existence proof. The density-route summary agrees with
the separate source and audit at source SHA-256
`cac72ab56f48c63732f311d8fafbc3b99ff92cc059cc599dff4c62c827aff8a9`.
It retains the five-connectivity hypothesis, exact component restrictions,
weakened-side-bound failure and missing reduction. The five-connected
global density theorem remains conjectural; no new literature application
or finite computation is used for this scoped addendum.
The added eight-cycle navigation matches the separately audited barrier;
removing all latest additions still exactly recovers Git `623110a`.

No gap was found in these scoped partial statements. Existing imported
finite inputs retain their recorded status; no new finite result is used.
Missing are an ownership-preserving global completion or closed reduction,
compatible bipartite scheme paths with any additional contact reserved,
and a justified continuation after a split. No decreasing rerouting
parameter or valid iterative lift is proved. Literal `K_7^=` completion
does not settle its arbitrary-model case. T44, Conjectures 19/21 and `HC_7`
remain open here; this checkpoint does not achieve the user's objective.

## Section 7.3 cut deductions and matching repair: scoped addendum

**Verdict: GREEN**, independently checked at the current source hash.
Fullness follows from actual cuts of order at most six. For independent
`T`, the set `D union T` is connected and its contraction strictly reduces
order, preserving the untouched component and the four literal roots.
Its colour can be pulled back to `T`, since `T` has no internal edges;
every edge from `T` to the retained side survives at the merged vertex.
That vertex is adjacent to all four roots, so every side admits exactly
the stated five-block boundary partition. Permuting six colour names
therefore permits gluing, without colouring any contracted component.

For the one-edge case, three components would give the previously checked
three-full-helper construction. With two, the degree sum at `T` gives
at least `24-2-6=16` exterior edges. One component `B` has at least eight,
independently of the later choice of `r`. Each vertex of `B` loses at most
`2-1_{xr in E}` neighbours when the other roots are deleted. Summing gives
the displayed edge inequality, and fullness plus `ab` supplies its last
two edges: `e(F)>=3|V(F)|-6` for every `r`. Adding `R-{r}` to a prohibited
rooted cut produces at most six actual separating vertices; the opposite
component survives. Thus the internally four-connected hypothesis holds.
[Norin–Totschnig Lemma 9 and the rooted-connectivity definition](https://arxiv.org/html/2507.03244v1#S2)
were freshly inspected in the primary text. Their no-model bound is one
edge smaller, so the four-root models follow with all other roots avoided.

The guaranteed eight-bag contact graph is two `K_5` graphs sharing `K_2`,
with nineteen edges and no isolated vertex. Every seven-bag model loses
an edge by deletion or contraction, excluding the nineteen-edge target;
the extra three contacts are not implicit.
If the stated matching exists, one cross contraction leaves three
universal bags. The two within-triple edges and two remaining matching
edges give a four-cycle on the other bags, proving `Q` with disjoint
preimages. Different choices of `r` are not simultaneous, and a transfer
can lose another required contact. No global matching or reduction follows.
The density navigation matches its separately audited final source,
including cross-side gluing and the elementary triangulation contraction;
it retains the unresolved general equality sides and induction obligations.

The new Section 7.5 implication is **GREEN**, conditional on finding its
six bags: deleting degree-eight `v` gives connectivity at least six and
`e(F)>=4|F|-4`. At least nine root contacts, five helper contacts and the
five contacts through the chosen neighbours give `Q`; the two possible
missing pairs are independent, and extra contacts are harmless. The
universal five-connected, `4n-9`, every-five-set statement is stronger
and unproved. Neither deleting occupied helpers nor finite probes supplies
its missing ownership-preserving construction or the weaker critical case.

## Section 7.5 neighbourhood constructions: scoped addendum

**Verdict: GREEN.** The new block matches the separately audited
four-cycle exclusion and spanning-configuration source at
`a0be7837d03dffd565313c8f29faf20226f5b116ec053ee8a82f27fd83865d10`
and cycle-and-triangle source at
`b3c43b4682c4554c2100d75dd14ea9df07aa898686b1cb6e3a1d9603985f68fe`.
The critical hypotheses supply every input, and the endpoint construction
gives `Q` directly. In the cycle-and-triangle case its at most one
cross-edge permits an omitted triangle vertex anticomplete to the cycle;
the two nonadjacent omitted cycle vertices then complete an independent
triple. The rooted five-clique construction and sufficient extra-helper
condition apply with their original-host ownership intact. The block
correctly leaves that helper's existence and the other spanning case open;
three occupied bag labels do not give an actual separator of order six.

## Section 7.5 rooted-wheel application: scoped addendum

**Verdict: GREEN.** The added paragraph matches the independently audited
[five-root wheel theorem](../results/hc7_five_root_wheel.md), source SHA-256
`f0fbab79d23d8079b91ff1a812b83db96059aa4fb0024c809b1037f3f533f62a`.
Its hypotheses now explicitly include a nonempty nonroot set. The strict
root-preserving reduction and connected-prefix construction are summarized
accurately. Under the standing critical-host hypotheses, Corollaries 3–4
exclude the actual three-cut and give four-connectivity of the
cycle-and-triangle exterior. The ledger and selected-results summary
match this scope. The paragraph retains the missing simultaneous helper
or three-part allocation; it does not claim a second application after
occupied bags are deleted or completion of a global conjecture.

## Section 7.5 almost-clique and exterior: scoped addendum

**Verdict: GREEN.** The new block and current ledger paragraph match the
separately audited almost-clique source at
`de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`
and exterior source at
`6c5196ea71f77a1426d8bc24ef040e7fe85805ac0cb784d2d62d152a67303eb3`.
The first retains the wheel theorem's other hypotheses and guarantees
all contacts except possibly one of `rb,rc`, with `r` fixed in advance.
Its extension permits at most five degree-six nonroots: both transfers
preserve surviving degrees, and the two-connected cofacial alternative
has degree-sum discrepancy at least `max(2h,6)-5>0`.
The second applies in the stated cycle-and-triangle configuration and
proves a nonempty connected exterior full to all eight neighbours, with
minimum degree five and the stated individual cycle-contact restriction.
Its cutvertex corollary excludes a component with only one triangle-root
contact, using the actual boundary of `L union M` and three disjoint
apex bags full to a contracted four-cycle. The added frontier sentence
matches exactly this scope and does not assert that the exterior is two-connected.
The wheel assemblies use actual root preimages and disjoint exterior
components. Neither summary asserts a reserved sixth helper, a three-part
allocation, or a global colouring conclusion.

For the recorded attempted packet, each exterior vertex loses at most
one neighbour when the two disjoint cycle edges are contracted. Degree
six therefore requires adjacency to the deleted triangle root and both
ends of one contracted edge. Two such vertices for the same edge would
give a literal `K_5^-` after contracting the centre to that triangle root;
the checked contraction closure excludes this. Hence there are at most
two deficits. In contrast, the retained boundary lower bound is only
`7-1-2=4`, and the deleted triangle root has no guaranteed contacts to
the three returned cycle bags. The paragraph records these two failures
without claiming a counterexample to the desired global construction.

## Section 7.5 two-triangle exterior: scoped addendum

**Verdict: GREEN.** The new block and ledger retain the five-root triangle
and at-least-two-nonroots hypotheses of the degree-free wheel, and match
the separately audited exterior source at SHA-256
`e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`.
The simultaneous port replacement and unused-root helper prove connectedness
and full contact, with no claim that a helper survives in the single component.
Contracting `{v,0,2}` and expanding the independent pair gives its common
colour, absent from the other six neighbours. Those six must use all five
remaining colours, or `v` could be coloured; hence the stated multiplicities
are exact. This does not assert Kempe equivalence. A changed colour class
does not lift an old model, and a contracted component's colour need not
extend over its internal edges. The stated global ownership gap remains open.

## Section 7.5 marked-scheme completion: scoped addendum

**Verdict: GREEN.** The block and ledger match the separately audited
marked-scheme source at SHA-256
`fb55cc00b52e0f3fb6f6e547f08b29ed6aae37cb25c4176a7c7fb96ada05dc2f`.
The final theorem needs the connection to `1` and one to `3,4` in the
same reserved-triple colouring. Its independent auxiliary inductions,
strict recursive parameter and fixed preimages are summarized accurately;
the pair only to `3,4` remains excluded. Failure at `1` permits the stated
two-pair swap because its `a0` component avoids both `0,2`. If `1` succeeds,
both other connections fail; their components exclude the corresponding
cycle-adjacent marker, but may contain the other. The separately audited
one-path barrier at `7b6ee34368f1b8d6828d5291e9559b05c192b22ad148671a7c69e4aec810b768`
does not satisfy the critical-host hypotheses.

In the recorded nonclosure, endpoint labels can be loops, so a minimizing
set of those labels need not give any positive-rank component contraction.
The stated simultaneous packing would be terminal: the two `a0` components
separate the markers, so one contains `a0` and a marker; disjoint full
`a1,a2` trees give a rooted `K_{2,3}` avoiding it and both markers.
The elementary helper construction then applies. Identifying the two
markers in a projection, however, supplies no connected original preimage
for that virtual vertex. No packing existence or deficient-case lift is
claimed, and no global colouring conclusion follows from this block.
