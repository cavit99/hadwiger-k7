# Hadwiger `K_7` research ledger

**Last updated:** 5 September 2026. This is the sole authority for current
research status. Internal audits are not external peer review.

**Standing:** `HC_7` is not proved. T44 and Norin--Totschnig Conjecture 21
also remain unproved.
Universal rooted bipartite contractibility has a written proof and two
separate GREEN internal audits. The subsequent triangle-free classification
and hereditary canonical two-copy sufficiency proposals are refuted.
The requested HC7 or comparable-theorem objective is not declared achieved.

## Three-level frontier

1. **Exhaustive global obligation:** prove `HC_7`, that every finite
   `K_7`-minor-free graph is six-colourable, or obtain an independent theorem
   of reach and significance comparable to Norin--Totschnig.
2. **Principal conditional refinement:** Conjecture 21 asserts that every
   `K_7^-`-minor-free graph is six-colourable. The stronger structural target
   T44 would imply it: every seven-connected graph containing a `K_{4,4}`
   minor contains a `K_7^-` minor. Neither would by itself prove `HC_7`.
3. **Immediate structural laboratory:** the
   [critical-host global construction](active/hc7_k44_closure_frontier.md#7-the-critical-host-global-construction)
   for Conjecture 21, combining proper-minor six-colourings with arbitrary
   `K_{4,4}` branch sets. No global construction or closed induction is
   proved. The
   [technical frontier](active/bipartite_contractibility_frontier.md)
   records the completed bipartite theorem, exact counterexamples and
   application limits; the [T44 frontier](active/hc7_k44_closure_frontier.md)
   retains the conditional HC7-related constructions.

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
