# Hadwiger `K_7` research ledger

**Last updated:** 21 September 2026. This is the sole authority for current
research status. Internal audits are not external peer review.

**Standing:** `HC_7` is not proved. T44 and Norin–Totschnig Conjecture 21
remain unproved. Conjecture 19 is resolved in an external preprint; see below.
Universal rooted bipartite contractibility has a written proof and two
separate GREEN internal audits. The subsequent triangle-free classification
and hereditary canonical two-copy sufficiency proposals are refuted.
The requested HC7 or comparable-theorem objective is not declared achieved.

## Three-level frontier

1. **Global obligation:** prove `HC_7`, or obtain our own independent theorem
   of reach and significance comparable to Norin–Totschnig.
2. **Sole selected conditional target:** Norin–Totschnig Conjecture 21:
   every finite `K7^-`-minor-free graph is six-colourable. The former C19
   target has been resolved externally; reproducing it would not meet the
   user's originality and significance criterion.
3. **Immediate construction:** improve the rooted five-boundary construction
   to leave at most one missing helper contact, and compose it without
   losing density, roots or branch-set ownership. The
   [technical construction](active/hc7_c21_rooted_density_construction.md)
   states the candidate and its exact unresolved contraction case.

## Current work plan

**Changed input, 21 September.** Dvořák–Norin–Rahman,
[arXiv:2609.17760v1](https://arxiv.org/html/2609.17760v1), submitted
15 September, prove C19 in Theorem 1.1. Their Theorem 1.3 also directly
excludes our former selected host: it is five-connected, has order at
least nine, and has `e>=4n>=4n-7`. Both exterior-colouring cases are covered
by that external result. We inspected the primary statements and this
application, not an independent reconstruction of the entire proof.
This is not our own theorem and does not achieve HC7.

**Selected attack.** Use the new rooted-density machinery to construct
`K7^-` in the actual critical host. Our existing audited reduction already
gives `delta>=8`, `e>=4n` and no literal K5. The new paper's `4n-2`
critical-host lower bound therefore does not improve our reduction.
Its rooted constructions are the materially new input. A broader
six-connected `4n` theorem is sufficient, but is not mandatory.

**Current gap.** The published two-helper construction permits two missing
contacts. Reducing that number to one is unproved. In the tested induction,
a quotient's positive four-boundary fragment can lift to a five-boundary
side of density one, outside the proposed density-two induction class.
A star replacement has a valid minor lift and may preserve the density
budget; its preservation of lightness still needs proof. The candidate
alone would not close C21 without the remaining global composition.

**Actual progress.** The [audited five-root density application](results/hc7_five_root_density_sixcut.md)
closes every three-component six-cut with four, five or six boundary edges
in the retained `4n` host, for arbitrary order. Boundaries with zero to
three edges remain; at three edges all three excesses must equal seven.
The two-component case also remains. This is a bounded set of complete
separator cases, not C21 or the user's significance benchmark.

**Execution.** Concentrate builders on that construction and its separator
application, sharing exact successful operations and failed lifts. The
coordinator integrates them and assigns independent challenges to the
strongest inference. Capacity is eight agents including the coordinator,
not a quota. T44, asymptotic improvements, standalone manuscripts and Lean
receive no parallel discovery allocation. Check existing barriers before
reusing a mechanism; all bags and colour choices may change.

**Acceptance.** A reduction must preserve its exact successor class,
colouring constraints and disjoint preimages, strictly decrease a stated
parameter, and lift its conclusion. A proper minor cannot inherit
seven-contraction-criticality. Complete separator cases and local lemmas
are checkpoints; completion requires the user's theorem and an audited
implication chain. No high likelihood of success has been established.

The [frozen C19 plan](archive/hc7_c19_campaign_before_external_resolution_2026-09-21.md)
preserves the previous constructions and their nonclosures. Existing
proofs and barriers remain valid within their stated hypotheses; Q-free
constraints do not automatically transfer to a `K7^-`-free host.

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
incompatibility into a terminal model remains unproved. The former
C19 construction had a short literal-core proof but lacked a decreasing
arbitrary-model exchange. Its external resolution does not repair that
exchange or establish C21. Neither conjecture was settled by our work.

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
