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
leave two spanning degree-eight neighbourhood configurations. The
[cycle-and-triangle theorem](results/hc7_degree8_cycle_triangle_closure.md),
with two separate internal audits, closes the entire five-cycle case for
arbitrary host order. The two-triangles-and-edge case remains open.

Write its neighbourhood as triangles `A,B` and edge `xy`. The
[complement theorem](results/hc7_two_triangle_complement_four_connectivity.md)
makes both `G-v-A` and `G-v-B` four-connected. The new
[spanning-helper theorem](results/hc7_two_triangle_exterior_helpers.md),
with a separate internal audit, makes `G-N[v]+{x,y}` two-connected and
partitions it into connected x/y-rooted parts with all but at most one
of their six contacts to `A`. The A roots remain singleton, and all B
roots are excluded from both parts. The symmetric assertion holds for B.
A simultaneous global allocation is still missing; even making both parts
full to both triangles would not alone give the required minor.

The [reserved-neighbour theorem](results/hc7_two_triangle_reserved_neighbours.md)
now obtains a four-clique rooted at the other four triangle vertices while
reserving three of `a,b,x,y`, where these four vertices induce only `xy`.
Four failed reservations would themselves give `Q` through four disjoint
exterior regions. The [degree-six theorem](results/hc7_five_root_degree_six.md)
also removes the earlier bound on degree-six nonroots in the five-root
almost-clique construction, with two possible triangle endpoints for the
missing edge. Both have separate internal audits; neither supplies the
additional compatible helper or closes the two-triangle case.
The [two-response theorem](results/hc7_two_triangle_two_responses.md),
with a separate internal audit, strengthens the boundary application:
across all exterior four-boundaries in `G-v-B`, at most one A root can
occur, and its other three boundary vertices lie in the exterior.
At least two A-root deletions therefore give the prescribed rooted
four-clique; the models may differ. The symmetric assertion holds for B.
The remaining boundary's opposite side is connected after deleting v.
The audited [central-root normalization](results/hc7_seven_boundary_path_allocation.md)
removes unused components and concentrates the unallocated vertices on
one path. A matching to three distinct port bags in the same model would
close this boundary case under the frontier's stated centre condition;
neither that matching nor the full two-triangle construction is proved.

The [earlier full-helper partition](active/hc7_two_triangle_helper_partition.md)
and [fixed colour-core response](active/hc7_two_triangle_fixed_colour_core.md)
remain audited resources for that allocation. The latter preserves a
fixed four-chromatic graph across all its four-colourings, giving either
a minor rooted at four triangle vertices or five compatible endpoint
paths. Neither result licenses combining independently chosen models.

The next task is a complete construction in this actual critical host,
using proper-minor six-colourings and preserving disjoint branch sets,
followed by an audit of the whole implication to Conjecture 19. The
[designated frontier](active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction)
records the exact gaps, including why arbitrary absorption or path
contraction is not a proved reduction. Conjecture 19 and the user's
HC7-or-comparable-theorem objective remain unmet.

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
