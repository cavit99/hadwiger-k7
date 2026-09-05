# Hadwiger `K_7` research ledger

**Last updated:** 5 September 2026
**Authoritative status:** `HC_7` is not proved here. T44 and the `K_7^-`
six-colour conjecture remain open. Universal rooted bipartite contractibility now
has a written proof and two separate GREEN internal audits. Internal audits
are not external peer review. This file is the sole authority for current
research status.

## Three-level frontier

1. **Exhaustive global obligation:** prove `HC_7`, that every finite graph
   with no `K_7` minor is six-colourable, or obtain an independent theorem
   of reach and significance comparable to Norin--Totschnig. The universal
   bipartite theorem is a substantial completed result; comparative
   significance and publication priority remain qualified assessments.
2. **Principal conditional refinement:** T44 and Norin--Totschnig
   Conjecture 21 remain preserved conditional routes. T44 asserts that
   every seven-connected graph with a `K_{4,4}` minor has a `K_7^-` minor;
   it would prove Conjecture 21, not `HC_7`. Neither is proved.
3. **Immediate structural laboratory:** pursue the general contractibility
   classification using the new independent-set reduction, while testing
   full-host completion of the T44 singleton residue. The universal
   bipartite theorem proves the intended flow assertion independently,
   but supplies no sufficient `HC_7` reduction. Exact targets, proved
   reductions and remaining inferences are in the
   [designated technical frontier](active/bipartite_contractibility_frontier.md).

## Current frontier and completed campaign

**Conjectural target:** `HC_7` is the sole remaining primary target after
completion of the bipartite contractibility campaign. No audited result
is invoked as a direct sufficient `HC_7` reduction at this checkpoint,
and no counterexample to `HC_7` is established. The new theorem's proof
does not complete T44 or infer extra near-clique contacts from an ordinary
bipartite minor. The [active index](active/INDEX.md) distinguishes the
remaining target from completed results and conditional routes.

**Written proof with two separate GREEN internal audits:** every finite
simple bipartite graph `H` is contractible. Every `H`-scheme in every
finite host contains an `H`-minor rooted at every prescribed vertex.
The [proof](results/bipartite_contractibility_via_matroid_reduction.md)
and [first](results/bipartite_contractibility_via_matroid_reduction_audit.md)
and [second exact-hash audits](results/bipartite_contractibility_via_matroid_reduction_second_audit.md)
cover arbitrary target degrees, host orders, path lengths and vertex
multiplicities. This includes fully rooted `K_{3,3}`, every `K_{m,n}` and
every bipartite theta graph. It settles the bipartite questions in
Kündgen--Pelsmajer--Ramamurthi, Section 8, including exclusion of the
bipartite counterexample sought in Question 4.

The proof normalizes the scheme by root-preserving monochromatic
contractions, then projects onto the shore with fewer nonroots. Edmonds'
matroid union theorem supplies disjoint spanning trees or a nonempty
minimizing label set. In the latter case, equality in its rank formula
simultaneously allocates disjoint trees spanning every required projection
component. Contracting those connected host sets yields a smaller scheme
with all roots preserved. An occurrence of a shared deleted label has
its two ends identified inside its own allocated component, so it does
not reuse a vertex belonging to another branch set. Host order strictly
decreases, and the final model lifts through the fixed disjoint preimages.
The shore orientation may reverse between steps, allowing both original
shores to expand. The proof is computation-free and uses only the finite
matroid union theorem as an external proof input.

**Written corollary and literature clarification:** the same result proves
the intended existence assertion of Biswal--Lee--Rao, Lemma 3.2, with
every terminal retained. For a bipartite demand graph of minimum degree
two, paths for independent demand edges being vertex-disjoint supplies
the required scheme. This uses the arXiv v2 independent-intersection
convention. The apparently reversed published wording is separate from
the substantive failures of the prefix construction: its Lemmas 3.5 and
3.6 remain refuted by the
[audited explicit examples](barriers/bipartite_flow_prefix_construction.md).
The new proof establishes the intended minor-existence statement without
validating those intermediate claims or asserting additional spectral,
separator or bounded-depth conclusions.

**Qualified independent assessment:** this is a terminal universal theorem
resolving a published rooted-minor question, with substantially broader
reach than the preceding degree-two and degree-three results. The
[separate assessment](results/bipartite_contractibility_via_matroid_reduction_audit.md#mathematical-reach-and-the-norin--totschnig-comparison)
identifies it as a credible candidate for the user's independent-theorem
alternative. It does not certify equal significance to Norin--Totschnig;
BLR's older broad assertion also prevents an unsupported first-result
claim. Specialist assessment of originality and comparative significance
remains outstanding. The full user objective is not declared achieved.

The [pre-promotion ledger](archive/RESEARCH_LEDGER_2026-09-05_before_universal_bipartite.md)
and [technical snapshot](archive/bipartite_contractibility_frontier_2026-09-05_before_universal.md)
preserve the earlier status and failed mechanisms. The
[singleton-shore barrier](barriers/bipartite_scheme_singleton_shore_barrier.md)
remains valid: its rooted models require expansion on both shores. The
new reduction explicitly permits this and avoids the archived arbitrary
split-and-lift ownership conflict. Frozen local attempts are no longer
live proof obligations for the completed bipartite theorem.

## Durable results and preserved proofs

**Continuation after the universal theorem.** The
[general scheme reduction](results/general_scheme_independent_set_reduction.md)
has a written proof and separate internal audit. It contracts simultaneously
from independent sets of actual host nonroots for arbitrary targets,
preserving every root and decreasing host order. A minimum counterexample
therefore has strict independent-neighbour expansion outside its roots.
The same file gives a complete rooted construction for every target when
the graph outside the prescribed roots is a pseudoforest. These are
supporting results for the conjecture that contractibility is equivalent
to every target subgraph's canonical two-copy scheme having its rooted
minor. That general sufficiency direction, including full rooted `K_5`
and `K_6`, remains open; the restricted host result is not completion.

The [odd-subdivision obstruction](barriers/triangle_free_odd_subdivision_contractibility.md)
adds an unbounded barrier to a proposed two-family classification:
triangle-free totally odd subdivisions of `K_4` are noncontractible even
though they contain neither of those proposed obstructions. The proof
uses explicit positive edge weights and KPR's exact two-copy criterion.
It leaves the stronger hereditary two-copy conjecture possible.

A further [written theorem with a separate internal audit](results/triangle_free_contractibility_odd_cycle_edge.md)
shows that every connected triangle-free contractible graph is bipartite
or becomes bipartite after one edge deletion. The signed-minor extraction
checks both parity and disjoint branch preimages before applying the
primary odd-cycle packing theorem. Together with skewed-theta exclusion,
this gives the proved necessary half of a concrete triangle-free
classification candidate. Its sufficiency is the next positive scheme
construction being investigated; no classification is claimed.

On the HC7 route, [expanding separator roots](barriers/hc7_k44_expanding_separator_roots.md)
closes the fixed-model case `C_a=C_p`, `|C_a|=3`, `|R|>=2` of the
singleton residue. An explicit planar boundary graph refutes the broader
local completion even when all separator-root bags may expand. These
boundary conditions cannot by themselves supply the scheme needed by
matroid contraction. The example does not realize a globally
seven-connected target-free host; model reselection in the other open
side remains possible and is now an explicit necessary part of this
approach. Full singleton completion, the nonsingleton residue and the
nonliteral lift remain open.

- **Written proof with a separate internal audit, 5 September 2026:**
  [universal rooted bipartite contractibility](results/bipartite_contractibility_via_matroid_reduction.md),
  with the full scope and proof mechanism stated above.
- The [degree-three theorem preserving the opposite shore's roots](results/degree_three_bipartite_weak_contractibility.md)
  and [universal weak-to-rooted equivalence](results/bipartite_weak_to_rooted.md)
  retain their original proofs and adjacent audits. The former permits
  its degree-three-side roots to move; the latter uses high-degree
  attachments. Neither restricted argument alone supplied the universal
  conclusion, whose new proof is independent of those reductions.
- The [even-subdivision theorem](results/even_subdivision_contractibility.md),
  with its [cold audit](results/even_subdivision_contractibility_audit.md)
  and [separate literature audit](results/even_subdivision_contractibility_literature_audit.md),
  remains a computation-free proof using simultaneous packing when
  each label occurs in at most two projections. Its original manuscript
  and the earlier [audited `K_{2,n}` theorem](results/k2n_contractibility_via_matroid_packing.md)
  are preserved. Their target classes are now included in the universal
  theorem without changing their audited content.
- The [five-root partial-routing theorem](results/llru_question61_via_km_property_star.md),
  with its [first](results/llru_question61_via_km_property_star_audit.md)
  and [second](results/llru_question61_via_km_property_star_second_cold_audit.md)
  GREEN audits, answers Lafferty--Liu--Rolek--Yu Question 6.1 under its
  precise disjoint-set hypotheses and lowers their stated connectivity
  threshold from `k>=17` to `k>=11`.
- Every three-connected graph has a `K_4^-` minor rooted at any four
  distinct prescribed vertices, with the missing edge unspecified. The
  [written proof](results/rooted_k4minus_four_roots.md) has a separate
  [GREEN audit](results/rooted_k4minus_four_roots_audit.md).
- The [degree-eight low-codegree and defect theorem](results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md),
  with [two internal audits](results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md),
  combines a deterministic finite local lemma with an unbounded reduction.
  It proves `D(G)>=20+kappa(G)` and the critical-host bound `n_8>=27+tau`.
- The [three-component order-seven-cut exclusion](results/hc7_k7minus_three_component_seven_cut_exclusion.md)
  and [critical seven-cut capacity theorem](results/hc7_k7minus_critical_seven_cut_capacity.md)
  have adjacent internal audits and imply that every seven-vertex cut in
  the specified critical host leaves exactly two components.
- The [critical literal-core safe-contraction result](results/hc7_k44_critical_safe_contraction.md)
  and [preservation refinement](results/hc7_k44_safe_contraction_preservation.md)
  retain their adjacent audits. They supply two safe contractions under
  the stated exterior-order hypothesis, without a closed unbounded
  induction.

The [selected-results map](results/README.md) is navigation, not a second
status authority. These completed statements are not all direct inputs
to the current `HC_7` target.

## Manuscript status

The five-page [universal bipartite contractibility manuscript](paper/bipartite-contractibility/main.pdf)
is the current manuscript candidate, with its [source](paper/bipartite-contractibility/main.tex)
and [manuscript audit](paper/bipartite-contractibility/main_audit.md) beside it.
Its mathematical source is the promoted universal theorem and its two
exact-hash internal audits. The
[even-subdivision manuscript](paper/even-subdivision-contractibility/main.tex)
and earlier [`K_{2,n}` manuscript](paper/k2n-contractibility/main.pdf)
are preserved with their existing audits.

The eight-page [low-degree manuscript](paper/k7minus-low-degree/main.pdf)
remains a frozen computation-free snapshot with its
[GREEN audit](paper/k7minus-low-degree/main_audit.md). It proves the baseline
`n_8>=25+tau`, rather than the later `27+tau` bound. The former
[rooted-web manuscript](archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf)
remains historical. None of these manuscripts proves `HC_7` or
Conjecture 21.

## Preserved conditional routes and historical check

The [T44 frontier](active/hc7_k44_closure_frontier.md) retains the literal
singleton separator residue, nonsingleton connected two-sided allocation,
closure of the induction hypotheses, and the nonliteral ownership-preserving
lift. All remain open. The [exceptional-centre programme](active/hc7_k7minus_seven_exceptional_frontier.md)
retains `n_8>=27+tau`, where `tau=sum_(i>=10)(i-9)n_i`; an upper bound
`n_8<=26` in that same critical host would prove Conjecture 21. Its
operation-sensitive colouring/model alignment remains unresolved. The
[six-connected `4n` programme](active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md),
the stronger density route, E5 and direct `HC_7` bridge composition remain
conditional or frozen programmes.

The requested historical orientation was checked against Git after reading
the [chronology review](archive/research_chronology_review_2026-09-04.md):
initial `a14eb38`, approximately fortnightly `df001e9`, `92b8722` and
`f85e51c`, then the T44 checkpoint `2c17559` and intervening retractions.
The off-main `15f824c` confirms the invalid separator-degree subtraction
that retracted the claimed exact-six closure. The contemporary initial
spine already distinguished reversible rotations from descent. These
checks motivated attacking the global ownership and termination inference,
which the new simultaneous component contraction proves directly.

## Trust boundary and navigation

Promoted theorems have written proofs and adjacent internal audits at exact
source hashes. Computer-assisted results retain only their finite or
explicitly reduced scopes; no finite experiment is needed for the new
universal proof. Barriers to intermediate claims are not counterexamples
to `HC_7` or T44. Existing audited material remains at its recorded revision.

- [Active index](active/INDEX.md): the sole primary target and concise links.
- [Designated technical frontier](active/bipartite_contractibility_frontier.md):
  remaining `HC_7` target, completed universal theorem and application limits.
- [T44 frontier](active/hc7_k44_closure_frontier.md): all preserved conditional
  obligations and relevant barriers.
- [Results map](results/README.md) and [manuscript map](paper/README.md):
  non-authoritative navigation.
- [Archive](archive/): frozen proof directions, historical status and
  preserved negative findings.
