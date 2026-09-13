# Hadwiger `K_7` research ledger

**Last updated:** 13 September 2026. This is the sole authority for current
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
2. **Selected conditional theorem:** every five-connected six-chromatic
   graph of minimum degree at least six and order at least seven contains
   `Q7=K7-2K2`, with independent missing edges. This
   [augmentation target](active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction)
   would close all Conjecture 19 by the audited triangle-quotient reduction.
   It remains unproved; neither C19 nor its comparable significance is
   assumed to follow from a partial construction. The actual critical-host
   formulation and quantitative R remain alternatives.
3. **Immediate laboratory:** discover a simultaneous branch-set exchange
   on graphs satisfying the augmentation target's full hypotheses. Compare
   an explicitly obstructed construction with a successful unrestricted
   model in the same host. Use the resulting operation to attempt an
   arbitrary-order proof, allowing all bags and selected roots to change.
   Finite models are discovery evidence, not a case closure.
   The [bipartite frontier](active/bipartite_contractibility_frontier.md)
   retains the completed theorem and its application limits.

## Current work plan

The next sustained campaign targets the augmentation theorem above. Unlike
our hypothetical critical counterexample, its hypotheses admit concrete
positive hosts on which competing constructions can be compared. It drops
proper-minor criticality, so it may be harder than the original problem;
its experimental accessibility is the reason for this choice, not evidence
of a proof. A triangle through the degree-eight vertex in the actual C19
host contracts to a graph satisfying all these hypotheses. A Q7 model in
that quotient lifts through the fixed triangle preimage, covering both
remaining exterior cases without a separate restoration argument.

**Compute to expose the missing operation.** Reuse existing model checkers
and graph generators. Certify chromatic number, connectivity and minimum
degree for each input. Separate already-covered hosts from those on which
a candidate construction stalls: literal K6, universal-vertex and existing
wheel certificates are controls. A failed search is not an absence proof.
Find and independently check unrestricted Q7 models in the same hosts;
record how ownership changes between those models. Minimise informative
instances while retaining the hypotheses and both certificates. Do not
spend the campaign collecting easy models or enumerating neighbourhoods
without their exteriors.

The [forest-exchange calibration](active/hc7_forest_exchange_probe.py)
checks the existing eighteen-vertex barrier host and two controls. One
exchange merges two bags and splits another, making the two missing
contacts disjoint. The host has a literal K6; this calibrates the search
and is not evidence for the general theorem.

**Develop one shared construction.** A proof builder, computational
challenger and independent reconstructor work with the same graph states,
failed move and successful model; the coordinating agent develops the
full implication and integrates repairs. Permit root reselection, expansion
of every bag, simultaneous transfers and temporary loss of contacts. A
model entirely away from a chosen root is also a valid exit. The squared-
cycle and minimum-model barriers prohibit treating a fixed sixth-root
extension or a locally optimal clique model as sufficient.

Turn the observed exchange into a construction for arbitrary host order.
If recursion requires a larger marked class, prove its initialisation,
preservation, strict decrease and fixed-preimage lift; intermediates need
not satisfy the original target if the enlarged class is valid. Each
proposed move must specify the retained colouring information, roots and
contacts. Independent review attacks its first new inference before any
promotion. Exhausting a move set may motivate a larger exchange; it is
neither a counterexample to the theorem nor a reason to end discovery at
the first failed idea. Reassess when the experiments and proof attempts
cease to distinguish mechanisms, rather than resetting after each lemma.

**Reserved routes and standing.** The preceding comparison found no common
triangle-colouring response and no R-scale contraction. The quantitative
low-neighbourhood-cover operation preserves chromatic number, but neither
eligible-centre selection nor sufficient accumulated loss is proved. Its
[maximum-star charge barrier](barriers/quantitative_neighbourhood_cover_charge.md)
leaves favourable global choice possible. Retain R and the stronger density
target in their [frontier](active/quantitative_star_contraction_frontier.md);
component labelling, uniform allocation and the old exterior recolouring
mechanism remain paused. No full theorem or high likelihood of success is
established by this plan. Completion requires the proof, its audited
implication chain and a substantiated comparison with the user's benchmark.

**Earlier exact campaign, `a94a809` through `67f528a`.**
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

**Retained exact checkpoint:** close the whole `chi(W)=5` branch by a
six-colouring or a simultaneous Q model in the actual host. The
[technical frontier](active/hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction)
retains the contact constraints and failed palette and ownership exchanges.
Any restoration must handle the entire omitted independent set in one
response. No such construction is proved; neither roots nor two-class
absorption are mandatory. Further repairs of the current recolouring
mechanism are paused. The six-chromatic exterior also remains open.

**Comparison outcome.** Neither the exterior recolouring nor quantitative
criticalisation attempt produced a whole-case closure or a closed decreasing
reduction. The [one-buffer counterexample](barriers/hc7_one_buffer_recolouring.md)
defeats that response form in a six-colourable host with the same literal
neighbourhood and five-chromatic exterior, but fails the actual critical
hypotheses. The [integer order-and-edge construction](barriers/quantitative_order_edge_potential.md)
shows that the new degree and loss bounds alone cannot give the cubic
colouring improvement; it is not a graph counterexample to R.
The comparison justified replacing the tested constructions. The subsequent
density campaign also left its spanning construction open; neither route
may infer graph structure from the scalar losses alone.

For retained C19 work, use the [global codegree bound](results/hc7_global_edge_codegree.md),
including its first-quotient bound and suitable paired contraction, when
it helps this construction. The [joint-wheel counterexample](barriers/hc7_joint_wheel_two_sets.md)
refutes relying on five-connectivity, nonplanarity and minimum degree six alone.
Freeze additional separator or relative-linkage refinements unless an
identified application closes a whole remaining case or supplies a closed
induction. All known separator residues remain in the designated frontier.

**Reserved density construction.** The
[retained history](active/quantitative_star_contraction_frontier.md#density-surplus-and-a-retained-contraction-history)
allows intermediate ratio loss and a final selection of connected bags
from different stages. Minimum-codegree contractions costing at most r
fit the required edge budget. An audited private-neighbour inequality
constrains more expensive contractions, but no bound on their combined
cost is proved; repeated use of the same original vertices remains the gap.
The [uniform-capacity allocation](barriers/quantitative_uniform_allocation.md)
now fails even for connected graphs in the all-minor independence class.
Those examples have no density surplus: they refute the proposed deficit-
to-minor inference, not the density theorem. Budgets on a maximum
independent set can localise a deficit to a dense induced subgraph, but
that subgraph may be the whole host, so the proposed induction need not
decrease. A construction using the surplus across this spanning case is
still missing; neither this allocation nor the retained history is mandatory.
The [sharp order example](barriers/quantitative_density_contraction_order.md)
has arbitrarily large surplus and requires `r/2` order loss before the
first independence decrease; an explicit batch attains this and succeeds.
It does not refute the target. The retained probe checks five surplus
inputs and three controls, returning six verified models; three surplus
inputs need only deletion. These are finite experiments, not a global
construction theorem. The density inequality, critical reduction R and
improved colouring bound remain unproved. Do not promote another count or
extremal reformulation as closing the missing graph construction.

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

**Collection revised, 13 September 2026.** The
[manuscript map](paper/README.md) separates three current drafts in editorial
order, preserved precursors and further theorem packages. This packages
existing proved work; it does not advance the global completion claim.

1. **Primary manuscript:** [A matroid proof of bipartite contractibility](paper/bipartite-contractibility/main.pdf),
   with [source](paper/bipartite-contractibility/main.tex) and an updated
   [separate GREEN internal audit](paper/bipartite-contractibility/main_audit.md).
   The seven-page draft adds the sharp intrinsic-radius-two theorem for
   paths of at most three edges, its invariant proof and six-vertex
   sharpness example. It explicitly excludes the general BLR Lemma 3.13
   depth assertion. The longer invariant obstruction remains outside the
   paper. Its earlier [scope review](paper/bipartite-contractibility/citation_novelty_review.md)
   retains its dated provenance; historical priority is still unresolved.
2. **Selected next standalone package:** [Paired clique minors from connected regions](paper/paired-clique-regions/main.pdf),
   with [source](paper/paired-clique-regions/main.tex) and a
   [separate GREEN internal audit](paper/paired-clique-regions/main_audit.md).
   The six-page draft proves the one-sided theorem, derives the two-sided
   linkage equivalence and includes the sharp region requirement and
   polynomial construction. The [focused primary-source assessment](paper/paired-clique-regions/citation_novelty_review.md)
   identifies the rainbow-clique-minor connection and finds no direct
   subsumption by the inspected statements; originality and priority
   remain unresolved.
3. **Structural manuscript:** [Degree, defect and separators in critical graphs](paper/k7minus-low-degree/main.pdf),
   with [source](paper/k7minus-low-degree/main.tex),
   [manuscript audit](paper/k7minus-low-degree/main_audit.md), and
   [dependencies and finite reproduction](paper/k7minus-low-degree/README.md).
   The 17-page draft incorporates the computation-free bound `n_8>=26+tau` and incident
   codegree-three conclusion; the broader theorem `9n-2m>=20+r` for
   r-connected, `K_7^-`-minor-free graphs with `r>=6` and `m>=4n`, giving
   `n_8>=27+tau`; and the computation-free two-component seven-cut closure.
   The broader theorem explicitly depends on both the nine- and ten-vertex
   quotient checks. Its abstract, proofs, bibliography and audit are revised
   together. These remain necessary conditions, not a proof of Conjecture 21.

The [even-subdivision](paper/even-subdivision-contractibility/README.md)
and [K2,n](paper/k2n-contractibility/README.md) manuscripts are preserved
unchanged as precursors, not separate current publication candidates.
The original low-degree `25+tau` snapshot and its audit remain in Git
at `f7b52aff0dfb2578bc30ade68f75df12671cf966`; its old verdict is not an
audit of the strengthened manuscript. All three current PDFs have been
rebuilt and visually checked; their audits identify exact source revisions.
An academic language edit covers all three current manuscripts. The structural
draft is shortened from 19 to 17 pages by consolidating intermediate results
and contraction accounting, with finite-profile data retained in its
reproducibility note. Its requested mathematical conclusions are unchanged.

The wheel/colouring package remains the next alternative, with its complete
four-connected `K_6-2K_2` exclusion theorem and its own originality
assessment still to be done. The attachment and canonical-test
counterexamples are reserved for a separate possible note. The
[collection map](paper/README.md#further-theorem-packages) links both packages.
No external specialist review, publication priority or NT-equivalence is
established by these manuscript revisions.

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
