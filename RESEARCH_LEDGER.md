# Hadwiger `K_7` research ledger

**Last updated:** 5 September 2026
**Authoritative status:** `HC_7` is not proved here. Neither is the
`K_7^-` six-colour conjecture or the new bipartite contractibility target.
Internal audits are not external peer review.
This file is the sole authority for current research status.

## Three-level frontier

1. **Exhaustive global obligation:** prove `HC_7`, or obtain an independent
   theorem of comparable significance to Norin--Totschnig. The completed
   even-subdivision theorem has not received such a significance assessment.
2. **Principal conditional refinement:** the sole primary proof campaign is
   now the conjecture that every finite bipartite graph is contractible.
   It seeks the independent-theorem alternative; no implication to `HC_7`
   is claimed. Conjecture 21 and T44 remain preserved conditional routes.
3. **Immediate structural laboratory:** arbitrary coloured `K_{3,3}` schemes
   test the extension from labels occurring in two projections to labels
   occurring in three. A proof must permit more flexible branch sets or
   replace the packing construction. Detailed claims belong in the
   [technical frontier](active/bipartite_contractibility_frontier.md).

## Current frontier

**Conjectural target:** every finite simple bipartite graph `H` is
contractible: every `H`-scheme has an `H`-minor rooted at its designated
vertices. By subgraph closure it suffices to handle all `K_{n,n}`.
The user authorized this change of primary target after the historical
assessment. Further T44 residue refinement is paused; its complete prior
status is preserved in the
[4 September snapshot](archive/RESEARCH_LEDGER_2026-09-04_T44.md) and its
[technical frontier](active/hc7_k44_closure_frontier.md).

The direct audited input is the
[even-subdivision theorem](results/even_subdivision_contractibility.md).
It proves contractibility when one bipartition class has maximum degree
two, using simultaneous graphic-matroid packing with partially shared
labels. The full target remains open: the same rank argument does not
handle labels participating in three projections. Restricted packing
failure is not failure of the required rooted minor.

**Audited barrier, not a counterexample to the target:** for every `n>=3`,
[an explicit coloured `K_{n,n}`-scheme](barriers/bipartite_scheme_singleton_shore_barrier.md)
has a rooted model but no model leaving either entire root shore singleton.
This refutes the fixed-shore extension even with arbitrary colour mixing
or trees joining only the required terminals. Both shores must be allowed
to expand. A separate split-off attempt also fails to lift arbitrary
returned models with their ownership preserved; its exact quantifier gap
is recorded in the technical frontier. These findings eliminate proposed
proof mechanisms and do not meet the requested positive-theorem standard.

A finite search of only the shortest one-copy-per-colour schemes would
miss the question: Kündgen--Pelsmajer--Ramamurthi already prove all
bipartite graphs `M'`-contractible. Exact source statements, research
findings and the completion standard are in the designated frontier.

## Durable recent results

- **Written proof with two separate internal audits, 4 September 2026:**
  every bipartite graph with degree at most two on one specified side is
  contractible. The [proof](results/even_subdivision_contractibility.md),
  [cold audit](results/even_subdivision_contractibility_audit.md), and
  [separate proof and literature audit](results/even_subdivision_contractibility_literature_audit.md)
  extend the two-projection `K_{2,n}` argument to arbitrarily many graphic
  matroids with partially shared labels. Every label belongs to at most two
  projections, which verifies the simultaneous matroid union inequality.
  Consequently every replacement of the edges of an arbitrary loopless
  multigraph by paths of positive even length is contractible. This gives a
  family of unbounded treewidth and covers the even-path portion of
  Kündgen--Pelsmajer--Ramamurthi's bipartite-theta question. It does not cover
  the three-odd-path case or `K_{3,3}`, and does not advance a specific
  `HC_7` subcase. Targeted literature checks found no matching theorem;
  priority and significance comparable to Norin--Totschnig remain
  unestablished. The earlier audited proof and manuscript are preserved.
- Every complete bipartite graph `K_{2,n}` is contractible in the sense of
  graph schemes. The [computation-free proof](results/k2n_contractibility_via_matroid_packing.md)
  has an adjacent [hash-pinned GREEN internal audit](results/k2n_contractibility_via_matroid_packing_audit.md)
  and a separate [four-page manuscript DRAFT](paper/k2n-contractibility/main.pdf)
  ready for specialist review.
- The [five-root partial-routing theorem](results/llru_question61_via_km_property_star.md),
  with a [GREEN audit](results/llru_question61_via_km_property_star_audit.md)
  and a [second GREEN cold audit](results/llru_question61_via_km_property_star_second_cold_audit.md),
  answers Lafferty--Liu--Rolek--Yu Question 6.1 when the five roots lie in
  pairwise disjoint vertex sets and every nonadjacent root pair is linked
  within the union of its two sets. It lowers their stated
  eight-connectivity threshold from `k>=17` to `k>=11`, but does not close
  the remaining degree-eight connector problem.
- Every three-connected graph has a `K_4^-` minor rooted at any four
  prescribed distinct vertices, with the missing quotient edge unspecified.
  The [elementary unbounded proof](results/rooted_k4minus_four_roots.md) has
  a [GREEN internal audit](results/rooted_k4minus_four_roots_audit.md).
- The [degree-eight low-codegree and defect theorem](results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md),
  with [two GREEN internal audits](results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md),
  combines one deterministic finite local lemma with an unbounded host
  reduction. It proves the defect ladder `D(G)>=20+kappa(G)` and the current
  critical-host bound `n_8>=27+tau`.
- The computation-free [three-component order-seven-cut exclusion](results/hc7_k7minus_three_component_seven_cut_exclusion.md)
  and its [GREEN audit](results/hc7_k7minus_three_component_seven_cut_exclusion_audit.md),
  combined with the separately audited [critical seven-cut capacity theorem](results/hc7_k7minus_critical_seven_cut_capacity.md),
  show that every seven-vertex cut in the critical host leaves exactly two
  components.
- The [critical literal-core safe-contraction
  corollary](results/hc7_k44_critical_safe_contraction.md), with its adjacent
  audit, combines the singleton-atom theorem with Dirac's neighbourhood
  inequality. Its [audited preservation refinement](results/hc7_k44_safe_contraction_preservation.md)
  gives two safe contractions preserving seven-connectivity when the
  exterior has order at least eight, without an unbounded induction.

The [selected-results map](results/README.md) is a non-authoritative reader
guide to these proofs and the direct proved inputs to T44.

## Manuscript status

The new minimal [even-subdivision DRAFT](paper/even-subdivision-contractibility/main.tex)
is the primary manuscript candidate. It presents the full computation-free
proof in four pages. The earlier four-page
[`K_{2,n}` DRAFT](paper/k2n-contractibility/main.pdf) is preserved. It is computation-free, has a
[GREEN internal audit](paper/k2n-contractibility/main_audit.md) and is
independent of the Hadwiger programme.

The compact eight-page [low-degree DRAFT](paper/k7minus-low-degree/main.pdf)
is a frozen, computation-free snapshot with a [GREEN internal audit](paper/k7minus-low-degree/main_audit.md).
It proves the baseline `n_8>=25+tau`, not the later `27+tau` strengthening.
The former rooted-web manuscript is retained only as a clearly marked
[historical DRAFT](archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf).
Neither manuscript proves Conjecture 21 or `HC_7`.

## Preserved frozen routes

The former exceptional-centre campaign remains a frozen critical-host
refinement. Its sound chain, including the audited low-codegree theorem
linked above, gives

`n_8 >= 27 + tau`, where `tau=sum_{i>=10}(i-9)n_i`.

Thus an upper bound `n_8<=26` in the hypothetical critical host would prove
Conjecture 21. Its first unresolved inference is the operation-sensitive
alignment of colouring responses with a fixed exact minor model. The remote
interface, induced-forest and fan/static-profile programmes are not parallel
active targets under the bipartite-contractibility pivot.

The six-connected `4n` theorem, the stronger `4n-2` density programme, E5
and direct `HC_7` bridge composition remain conditional or frozen routes.
Their priority can be reconsidered when a new argument offers a stronger
justified prospect; T44 need not first be falsified.

The [historical review through the former HEAD](archive/research_chronology_review_2026-09-04.md)
records the initial commit, fortnightly snapshots and intervening
retractions, including the off-main August exact-six closure. Across those
changes the repeated failure was preservation of a complete colouring
partition or rooted model in a class closed under the proposed reduction.
The independent judgement is therefore to require a terminal theorem or a
proved decreasing reduction before counting additional counterexample
structure as progress. The even-subdivision theorem is a concrete outcome
of assessing the standalone packing route on that basis, while T44 remains
open.

## Trust boundary

- Promoted theorems have written proofs and adjacent internal audits at exact
  source hashes. Directory placement alone is not treated as promotion.
- Computer-assisted claims are restricted to their finite or explicitly
  reduced-family scopes. The order-eleven and Z3 generation environments are
  research-only; the claim-critical deterministic promoted-result checks are
  separately registered and hash-pinned.
- The shortcut profiles are barriers to local intermediate implications.
  They are not seven-connected and are not counterexamples to T44.
- External inputs are cited beside the results that use them. Recent
  preprints, including Chu's removable-matching theorem, are identified as
  preprints; checking the statement and its use is not an audit of the
  external proof.

## Navigation

- [`active/INDEX.md`](active/INDEX.md): concise live navigation.
- [`results/README.md`](results/README.md): selected completed and audited
  proofs, grouped by scope.
- [`paper/README.md`](paper/README.md): manuscript status and exact contents.
- [Bipartite contractibility frontier](active/bipartite_contractibility_frontier.md):
  the sole primary target, direct proof mechanism and exact failure points.
- [T44 technical frontier](active/hc7_k44_closure_frontier.md): preserved exact
  hypotheses, two open obligations, barriers and stop rules.
- [T44 falsification checkpoint](active/experiments/k44_closure_falsification/README.md):
  bounded and reduced-family computational evidence.
- [Frozen exceptional-centre frontier](active/hc7_k7minus_seven_exceptional_frontier.md):
  preserved critical-host reduction and operation/model alignment barrier.
- [Frozen six-connected `4n` frontier](active/hc7_k7minus_sixconnected_4n_sparse_threecut_frontier.md):
  conditional sparse-cut programme.
- [`archive/`](archive/): superseded proof spines and historical ledgers.
