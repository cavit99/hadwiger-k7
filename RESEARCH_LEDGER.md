# Hadwiger `K_7` research ledger

**Last updated:** 8 September 2026. This is the sole authority for current
research status. Internal audits are not external peer review.

**Standing:** `HC_7` is not proved. T44 and Norin--Totschnig Conjectures
19 and 21 also remain unproved.
Universal rooted bipartite contractibility has a written proof and two
separate GREEN internal audits. The subsequent triangle-free classification
and hereditary canonical two-copy sufficiency proposals are refuted.
The requested HC7 or comparable-theorem objective is not declared achieved.

## Three-level frontier

1. **Exhaustive global obligation:** prove `HC_7`, that every finite
   `K_7`-minor-free graph is six-colourable, or obtain an independent theorem
   of reach and significance comparable to Norin--Totschnig.
2. **Immediate theorem target:** Conjecture 19 asserts that every
   `K_7^=`-minor-free graph is six-colourable, where the two deleted edges
   are independent. This gives a concrete proposed comparison with
   Norin--Totschnig; it is unproved. The stronger Conjecture 21 and its
   sufficient structural target T44 remain available conditional routes.
3. **Immediate structural laboratory:** the
   [critical-host global construction](active/hc7_k44_closure_frontier.md#7-the-critical-host-global-construction)
   for the companion conjectures, combining proper-minor six-colourings with near-clique
   or `K_{4,4}` models. No global construction or closed induction is proved.
   The
   [technical frontier](active/bipartite_contractibility_frontier.md)
   records the completed bipartite theorem, exact counterexamples and
   application limits; the [T44 frontier](active/hc7_k44_closure_frontier.md)
   retains the conditional HC7-related constructions.

## Current work plan

The immediate target is Conjecture 19. Its audited critical-host reductions
leave two spanning degree-eight neighbourhood configurations: a five-cycle
and a triangle, or two triangles and an edge. Extra edges remain allowed.
The priority is a complete construction in the cycle case, using the full
proper-minor six-colourability hypothesis, followed by the other case and
an audit of the whole implication. Neither case is closed.

The [technical frontier](active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction)
records the exact constructions and ownership requirements. In the cycle
case the bipartite theorem supplies a rooted five-clique; a compatible
connected helper through the omitted triangle vertex would complete the
case. The
[cycle-and-triangle](results/hc7_degree8_cycle_exterior.md) and
[two-triangle](results/hc7_degree8_two_triangle_exterior.md) exterior
proofs make `G-N[v]` connected and full to all eight neighbours in both
configurations. The latter also proves the five-root wheel lemma without
a separate degree hypothesis. Their audits and the frontier retain the
exact statements and port constructions. Finding the helper inside the
remaining single component is still open.

The audited [colour-path completion](results/hc7_cycle_colour_path_completion.md)
proves two terminal path constructions and a colouring reduction: every
reserved-triple colouring admits one Kempe swap to repeated pairs
`{a0,3}` and `{0,2}`, after relabelling the cycle. The
[flexible-root theorem](results/bipartite_flexible_root_families.md), with a
separate GREEN internal audit, allows prescribed root families on both
shores of any finite simple bipartite target. It retains each individual
root in a separate bag while permitting the endpoints of family contacts
to change. Its application completes the colouring state in which the
cycle uses three colours and the triangle uses three other colours.
Consequently, in the retained two-pair colouring, `1` must be
bichromatically connected to `3` in their two colours. The four additional
connections sufficient for a complete cycle-case construction are still
unproved. No old model is assumed to survive a recolouring. The cycle
case, the other spanning case and the global objective remain open.

The [cycle-colouring theorem](results/hc7_cycle_colour_cross.md), with a
separate GREEN internal audit, converts the new restriction into two
disjoint crossing paths on the cycle. After deleting the whole colour
class of any triangle root uniquely coloured on `N(v)`, every resulting
five-colouring uses at least four cycle colours, so such a cross exists
outside that class. The four cycle branch roots are retained; the other
triangle roots may lie on the paths. The next construction must combine
this cross with the triangle while retaining the full colouring condition.
Neither an isolated cross nor paths from separate colourings suffice.
The audited [palette counterexamples](barriers/hc7_cycle_palette_extension_barrier.md)
also show that the full quantified five-colouring condition alone does not
force the minor. They violate the actual host's literal `K_5^-` exclusion;
the construction must retain more of that host's hypotheses.
A second exact construction contracts a cycle edge and obtains two
connected helpers, each meeting all four cycle bags. It would complete the
case if the helpers could be chosen to put triangle vertices on both sides;
that simultaneous partition remains unproved. The
[frontier](active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction)
records its density bound, fixed lift and missing exchange.
The [new three-connectivity theorem](results/hc7_cycle_triangle_complement_three_connectivity.md),
with two separate GREEN internal audits, closes every two-vertex-separator
case in `G-v-C`: a flow and one bridge exchange make the required donations
simultaneously. The retained graph is therefore three-connected. This still
does not establish the triangle-splitting helper partition or close the cycle case.
The [almost-clique theorem](results/hc7_five_root_almost_clique.md) and
[deficient-bag reduction](results/hc7_near_clique_deficient_bag_normalization.md)
remain available with their exact preservation limits.

The [density and boundary-colouring routes](active/hc7_k44_closure_frontier.md#7-the-critical-host-global-construction)
and T44 remain conditional alternatives, not mandatory intermediate
statements. An original proof of Conjecture 19 is the present concrete
candidate for the Norin--Totschnig comparison; its proof and comparative
assessment are still outstanding. Local results and commits do not meet
the user's completion criterion.

Resume from this ledger and the designated frontier; revisit history only
for a disputed dependency or changed claim. The bipartite paper's primary-
source originality review and final manuscript review remain pending after
this proof effort unless they supply a needed input. No author contact is
authorized.

## Current frontier and completed campaign

**Written proof; two separate GREEN internal audits.** Every scheme of
every finite simple bipartite target `H` contains an `H`-minor rooted at
all prescribed vertices. There is no degree, order, path-length or
intersection-multiplicity bound. The
[proof](results/bipartite_contractibility_via_matroid_reduction.md),
[first audit](results/bipartite_contractibility_via_matroid_reduction_audit.md)
and [second audit](results/bipartite_contractibility_via_matroid_reduction_second_audit.md)
cover the full statement, including `K_{3,3}`, all `K_{m,n}` and bipartite
theta graphs. It answers Kündgen--Pelsmajer--Ramamurthi's bipartite scheme
questions in Section 8.

The proof uses matroid union to allocate disjoint trees spanning all
required projection components. Either they directly give the rooted
model, or their simultaneous contraction produces a smaller valid scheme.
Host order strictly decreases; fixed disjoint preimages preserve every
root and lift the final model. Both original shores may expand. The
[technical explanation](active/bipartite_contractibility_frontier.md#the-decisive-reduction)
records the ownership argument.

**Written corollary.** This independently proves the intended rooted
existence assertion of Biswal--Lee--Rao, Lemma 3.2, under the arXiv v2
independent-intersection convention. Their prefix construction's
intermediate Lemmas 3.5 and 3.6 remain
[refuted](barriers/bipartite_flow_prefix_construction.md). The published
definition's apparent reversal is a separate issue. The corollary makes
no new spectral, separator or bounded-depth claim.

**Assessment.** This is a substantial universal theorem and an independent
proof of an older broad flow assertion. The
[internal reach assessment](results/bipartite_contractibility_via_matroid_reduction_audit.md#mathematical-reach-and-the-norin--totschnig-comparison)
does not establish equal significance to Norin--Totschnig. Our demonstrated
contribution has not yet met that benchmark: no sufficient HC7 reduction
is proved, and the exact originality and literature positioning remain
unfinished. The [active index](active/INDEX.md) therefore retains `HC_7`
as the sole primary target, with no direct sufficient proved input.

## Durable results and preserved proofs

**Unbounded counterexamples; written proofs and a separate GREEN audit.**
For every odd `ell>=5`, join `C_ell` to `K_{3,4}` at a vertex in its
three-vertex shore. The
[explicit scheme](barriers/triangle_free_bipartite_attachment_counterexample.md)
has `ell+8` nonroots, whereas any fully rooted model would require
`ell+9`. The target is triangle-free, has no skewed theta and has only
one odd cycle. Moreover, every subgraph passes the canonical two-copy
test. Thus both proposed sufficiency statements are false. The proof
allows arbitrary branch-set allocation; its exhaustive finite checker
only confirms the smallest example. The former
[classification campaign](archive/bipartite_contractibility_frontier_2026-09-05_before_attachment_obstruction.md)
is frozen.

The following audited inputs retain their exact statements:

- [Independent-set scheme reduction and pseudoforest host theorem](results/general_scheme_independent_set_reduction.md):
  valid for arbitrary targets under their stated host hypotheses.
- [Necessary odd-cycle-edge condition and series-class parity theorem](results/triangle_free_contractibility_odd_cycle_edge.md):
  the proposed converse is refuted; these necessary results are unchanged.
- [Even subdivisions](results/even_subdivision_contractibility.md),
  [degree three with one shore's roots preserved](results/degree_three_bipartite_weak_contractibility.md),
  [weak-to-rooted equivalence](results/bipartite_weak_to_rooted.md) and
  [`K_{2,n}` contractibility](results/k2n_contractibility_via_matroid_packing.md):
  preserved precursor proofs, now covered by the universal conclusion.

Earlier [odd-subdivision](barriers/triangle_free_odd_subdivision_contractibility.md),
[attachment](barriers/scheme_articulation_colour_fibre.md),
[singleton-shore](barriers/bipartite_scheme_singleton_shore_barrier.md) and
prefix-construction barriers retain their precise intermediate scopes.
They do not refute the universal bipartite theorem, `HC_7` or T44.

The [selected-results map](results/README.md) also preserves the five-root
partial-routing theorem, the four-root `K_4^-` theorem and audited
critical-host results. It is navigation, not a second status ledger.

## Manuscript status

The five-page [bipartite manuscript](paper/bipartite-contractibility/main.pdf)
is the current DRAFT, with its [source](paper/bipartite-contractibility/main.tex)
and [internal audit](paper/bipartite-contractibility/main_audit.md).

**Pending paper work:** complete the primary-source originality review and
final manuscript review. Account explicitly for BLR Lemma 3.4's intended
retention of every terminal, leaf/component extensions of the
minimum-degree-two statement, and the exact scope of later applications.
Position the contribution as an independent proof, with any stronger
novelty claim requiring evidence. No author contact is authorized.

The [manuscript map](paper/README.md) distinguishes preserved earlier drafts.
The low-degree `K_7^-` manuscript remains a frozen snapshot with
`n_8>=25+tau`; the later audited repository bound is `n_8>=27+tau`.
Existing theorem and manuscript sources remain at their audited revisions.

## Preserved conditional routes and historical check

The [T44 frontier](active/hc7_k44_closure_frontier.md) retains three separate
obligations: singleton separator completion, nonsingleton connected
two-sided boundary allocation, and the nonliteral branch-model lift.
An induction must also preserve its full hypothesis class and decrease a
well-founded parameter. Closing only the literal residues would not prove
T44. The [root-expansion result and local barrier](barriers/hc7_k44_expanding_separator_roots.md)
close only the stated fixed-model subcase; global model reselection remains
possible. The critical-host refinement has two safe contractions, with no
closed unbounded induction. The latest independent audit confirms that
equal-endpoint colourings exist in both connectivity cases, while a cut
through an internal branch edge meets at most six model bags. The full
boundary-colouring families are now explicit; converting their
incompatibility into a terminal model remains unproved. The companion
Conjecture 19 has a short complete literal-core construction, but its
arbitrary-model exchange also lacks a decreasing parameter. Neither
conjecture has been settled by this work.

The [exceptional-centre programme](active/hc7_k7minus_seven_exceptional_frontier.md)
retains `n_8>=27+tau`, where `tau=sum_(i>=10)(i-9)n_i`; an upper bound
`n_8<=26` in the same critical host would prove Conjecture 21. Colouring
and branch-model compatibility remain unresolved. The
[six-connected density programme](active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md)
and other earlier routes retain their conditional or frozen status.

The [chronology review](archive/research_chronology_review_2026-09-04.md)
was checked against initial commit `a14eb38`, fortnightly snapshots
`df001e9`, `92b8722`, `f85e51c`, T44 checkpoint `2c17559` and intervening
retractions, including off-main `15f824c`. The
[previous ledger](archive/RESEARCH_LEDGER_2026-09-05_before_documentation_cleanup.md)
preserves the fuller account and earlier result inventory.

## Trust boundary and navigation

Promoted proofs and adjacent audits are tied to exact source hashes.
Finite computations establish only their stated finite or explicitly
reduced conclusions. Internal audits do not establish external acceptance,
priority or comparative significance.

- [Active index](active/INDEX.md): sole primary target and direct dependencies.
- [Technical frontier](active/bipartite_contractibility_frontier.md):
  global target, completed theorem, application limits and refuted routes.
- [Results](results/README.md) and [manuscripts](paper/README.md): navigation.
- [Archive](archive/): preserved history, retractions and frozen directions.
