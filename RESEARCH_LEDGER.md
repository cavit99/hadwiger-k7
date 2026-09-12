# Hadwiger `K_7` research ledger

**Last updated:** 12 September 2026. This is the sole authority for current
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
   [critical-host construction](active/hc7_k44_closure_frontier.md#7-the-critical-host-global-construction),
   seeking one simultaneous Q-minor construction in the remaining case.
   The six-root bipartite scheme is one sufficient route; retaining those
   roots or leaving v singleton is not a requirement of the objective.
   The [fully rooted K5 construction](active/k5_contractibility_frontier.md)
   remains an alternative extraction route.
   Neither global construction nor a closed induction is proved.
   The
   [technical frontier](active/bipartite_contractibility_frontier.md)
   records the completed bipartite theorem, exact counterexamples and
   application limits; the [T44 frontier](active/hc7_k44_closure_frontier.md)
   retains the conditional HC7-related constructions.

## Current work plan

The goal remains HC7 or an independently substantiated NT-comparable theorem.
Conjecture 19, excluding `Q=K7-2K2`, is the selected exact route; neither
its proof nor its significance assessment is complete. Routes may change
without changing that completion criterion.

**Assessment of the last 20 commits, `a94a809` through `67f528a`.**
The [four-chromatic exterior theorem](results/hc7_two_triangle_exterior_colour_bound.md)
closes one entire remaining chromatic branch for arbitrary host order.
The [four-cut theorem](results/hc7_four_cut_components.md) and
[triangle-and-cycle separator theorem](results/hc7_triangle_four_cycle_separator.md)
close specified separator configurations, not every four-cut.
The [four-connected Q6 theorem](results/four_connected_five_chromatic_minor.md)
is a complete lower-order result; its novelty and NT-level significance
are unestablished. Other refinements supply useful bounds or eliminate
shortcuts, but repeatedly stop at incompatible connected sets, lost
colouring responses or an induction class that is not preserved.
Further normal forms are not the preferred use of the next campaign.

**Exact host and completed cases.** The audited C19 reductions leave a
seven-contraction-critical, seven-connected Q-minor-free graph G of minimum
degree eight, with a degree-eight vertex v. The
[cycle-and-triangle case](results/hc7_degree8_cycle_triangle_closure.md)
is closed. Write the remaining neighbourhood as two triangles A,B and an
edge xy, allowing the recorded extra edges, and put `W=G-N[v]`.
The [wheel colouring corollary](results/hc7_rooted_wheel_extension.md)
closes `chi(G-{x,y})=5`. The exterior theorem proves
`chi(G)<=max{4,chi(W)+2}`. Thus the remaining host has
`chi(G-{x,y})=6` and `chi(W)` equal to five or six.

**Next concentrated checkpoint:** close the whole `chi(W)=5` branch,
using a six-colouring or a simultaneous Q model in the actual host.
The current mechanism seeks two exterior colour classes that can both
use the three neighbourhood colours. Their missing-colour lists must be
compatible in one colouring; separate colourings or separate minor models
do not suffice. Keep all proper-minor six-colourings available. Neither
fixed roots, a singleton v, nor two-class absorption is mandatory.
The [technical frontier](active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction)
records the exact contact constraints and first unsupported exchanges.
The six-chromatic exterior and the full two-triangle case remain open.

Use the [global codegree bound](results/hc7_global_edge_codegree.md),
including its first-quotient bound and suitable paired contraction, when
it helps this construction. The [joint-wheel counterexample](barriers/hc7_joint_wheel_two_sets.md)
refutes relying on five-connectivity, nonplanarity and minimum degree six alone.
Freeze additional separator or relative-linkage refinements unless an
identified application closes a whole remaining case or supplies a closed
induction. All known separator residues remain in the designated frontier.

**Competing global attack:** the [quantitative frontier](active/quantitative_star_contraction_frontier.md)
gives an audited conditional route from an unrestricted connected
contraction reducing independence number at edge cost `O(r^2)` to an
improved double-logarithmic colouring exponent. The required contraction
is unproved. Test this different mechanism independently; do not replace
it with the refuted bounded-bag shortcut or call the conditional implication
an achieved improvement. T44 and [rooted K5 contractibility](active/k5_contractibility_frontier.md)
remain available, without making their auxiliary root requirements mandatory.

Advance a route on a complete proof with a valid lift, a decisive obstruction,
or a changed global mechanism; do not measure progress by commits or lemma
counts. Independently attack its strongest inference before promotion.
The [frozen accumulated plan](archive/hc7_work_plan_before_concentrated_checkpoint_2026-09-12.md)
preserves the earlier detailed summaries; it is not a second status authority.

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

**Written quantitative refinement; separate GREEN internal audit.** For
[schemes with paths of length at most three](results/bipartite_short_scheme_radius.md),
every final bag has intrinsic radius at most two at its original root.
The bound is sharp. At length five the same reduction can create a
root-free component of unbounded intrinsic diameter; this defeats that
invariant, not bounded-radius existence. The refinement does not close
the HC7-related objective or substantiate comparable significance.

**Written corollary.** This independently proves the intended rooted
existence assertion of Biswal--Lee--Rao, Lemma 3.2, under the arXiv v2
independent-intersection convention. Their prefix construction's
intermediate Lemmas 3.5 and 3.6 remain
[refuted](barriers/bipartite_flow_prefix_construction.md). The published
definition's apparent reversal is a separate issue. The corollary makes
no new spectral, separator or bounded-depth claim.

**Assessment.** The [primary-source comparison](paper/bipartite-contractibility/citation_novelty_review.md)
substantiates a universal independent proof and its exact application to
Lee's later flow lemma, including fractional flows and initially
noninjective terminal maps. BLR already intended all roots to be retained;
private four-cycles remove its minimum-degree restriction. Flexible root
families also follow by augmentation. These are not new statement-level
advantages over that intended assertion. Property `(*)` is an equivalent
formulation. Later specialised constructions bypass the disputed
extraction step for some clique-flow applications without proving the
universal rooted theorem. The repair is assessed as a substantial
specialist contribution below NT's demonstrated advance, even granting
first-valid-proof credit; historical firstness remains unresolved.
The objective remains unmet. The [active index](active/INDEX.md) retains `HC_7` as the
sole primary target, with no direct sufficient proved input.

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

**Revision complete, 8 September 2026:** *A matroid proof of bipartite
contractibility* incorporates the [scope review](paper/bipartite-contractibility/citation_novelty_review.md),
states the property `(*)` equivalence and distinguishes the intended BLR
assertion from later specialised bypasses. The shared-label quotient path
and exact host-order decrease are explicit. The five-page British-English
draft has updated exact-hash internal audits and a checked PDF; the
originating theorem source is unchanged. Historical priority and external
specialist review remain open. No author contact is authorized.

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
