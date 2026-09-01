# Current proof work

**Role:** concise navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md); exact hypotheses and
residues are recorded in the linked technical frontier.

## Primary target

[Seven-connected `K_{4,4}` closure](hc7_k44_closure_frontier.md)

> **T44.** Every seven-connected graph containing a `K_{4,4}` minor
> contains a `K_7^-` minor.

T44 is open.  It would prove Norin--Totschnig Conjecture 21 through the
Kawarabayashi--Toft theorem that every seven-chromatic graph has a `K_7` or
`K_{4,4}` minor.  It does not by itself prove `HC_7`.

Selected audited inputs:

- [the double-cone theorem, two-near-full-model-bridges lemma and exact-cut
  normal form for a vertex-minimal nonliteral model](../results/hc7_k44_branch_model_and_double_cone.md);
- [every exact seven-cut boundary in a seven-connected target-free graph has
  minimum degree at most
  three](../results/hc7_k44_fourconnected_seven_boundary_double_cone.md);
- [the exterior of a literal core is connected and has no separator of
  order at most two](../results/hc7_literal_k44_exterior_threeconnectivity.md);
- [a four-portal exterior triangle is terminal](../results/hc7_k44_four_portal_triangle_completion.md);
- [a three-portal exterior `K_4` is terminal except for the exact
  tetrahedral profile, which spanning portal coverage excludes](../results/hc7_k44_three_portal_k4_tetrahedral_dichotomy.md);
- [failure of every safe contraction reduces directly to a singleton
  all-edge atom with exact one-resource crossing
  blockers](../results/hc7_k44_positive_atom_elimination.md);
- [a minimum nonsingleton crossing blocker is three-connected of minimum
  degree at least four, with multiply attached resources and two exact
  three-cut profiles](../results/hc7_k44_tight_boundary_and_minimum_blocker.md);
- [an adjacent singleton edge has an exact two- or three-component
  contraction trace](../results/hc7_k44_adjacent_singleton_contraction_trace.md);
- [a two-component literal-shore split has exact unbalanced separator and
  balanced endpoint-miss
  profiles](../results/hc7_k44_adjacent_singleton_shore_split_profiles.md).

A [hash-pinned internal cold audit](../results/hc7_k44_closure_local_normal_forms_audit.md)
covers the five local statements other than the separately audited
dense-boundary theorem.  Each of the three newer literal reductions has its
own adjacent hash-pinned GREEN internal audit.

## Falsification checkpoint

[Computer-assisted exact searches and a written reduced-family
argument](experiments/k44_closure_falsification/README.md)
find no counterexample through order eleven and eliminate every
seven-connected member of the full-attachment non-clique seven-sum family.
The first conclusion is a computer-assisted finite result; the second is a
written-unaudited reduction with computer-assisted base cases.  The sharp
local survivor is the 19-contact tetrahedral profile, whose connectivity is
four.

The separate [literal labelled-trichotomy
census](experiments/k44_literal_labelled_trichotomy/README.md) checks every
three-connected exterior through order seven against all eight-label
incidence assignments.  It finds no survivor, but its UNSAT conclusions
depend on Z3 and are bounded evidence only.

The [weighted-splitter hostile screen](experiments/k44_literal_weighted_splitter/README.md)
extends the exact formula to all 1,619 eligible order-eight exteriors and to
targeted four-regular small-atom probes at orders nine and ten.  It also
finds no survivor.  Z3 remains the decisive UNSAT trust boundary, so this is
bounded evidence rather than an unbounded inference.

The [minimum-blocker bisection
screen](experiments/k44_literal_minimum_blocker_bisection/README.md) checks
the exact reduced local formula with a complete labelled encoding through
blocker order six and a separate fixed-host encoding on all 157
three-connected graph-atlas hosts through order seven.  It is independently
audited bounded evidence without an independently checkable UNSAT
certificate.

## Two open obligations

1. **Literal exact-residue completion.**  Prove the minimum-degree-four
   boundary-bisection lemma for a nonsingleton blocker, and eliminate the
   exact adjacent-singleton contraction profiles: the core-concentrated
   rooted-contact case, both two-component literal-shore splits, and the
   three-component whole-shore trace.  Safe contraction and induction then
   give the pure labelled trichotomy; the whole literal core joins its
   six-bag outcome to the target.
2. **Nonliteral model-trace rotation.**  Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target.  Exact cuts alone do not give laminarity,
   a peel side or preserved branch ownership.

Immediate barriers:

- **Barrier/counterexample to local shortcut claims:** [a fat triangle with
  seven local paths and a split edge with six alternate
  paths can both remain target-free](../barriers/hc7_k44_shortcut_certificate_barriers.md);
- **Precise nonsingleton lemma:** [find the closing connected bisection in a
  minimum-degree-four three-connected blocker](../results/hc7_k44_tight_boundary_and_minimum_blocker.md#8-finite-falsification-and-exact-remaining-lemma);
- **Route nonclosure, not a counterexample:** [the `K_3 join (3K_2)` profile
  shows that the three-cut components cannot simply be kept intact in that
  bisection](hc7_k44_closure_frontier.md#41-nonsingleton-minimum-blocker).
  Splitting one component closes the profile; the precise repair is the
  intra-component nonseparating-transversal lemma;
- **Precise singleton profiles:** [the contraction-trace
  dichotomy](../results/hc7_k44_adjacent_singleton_contraction_trace.md#6-exact-scope)
  and [the exact unbalanced and balanced literal-shore
  splits](../results/hc7_k44_adjacent_singleton_shore_split_profiles.md);
- **Recorded route nonclosure:** [a component of an exact-cut complement may
  contain pieces of several branch bags](../results/hc7_k44_branch_model_and_double_cone_audit.md#exact-scope),
  so fullness to the cut cannot be counted as external branch-set contact.

## Preserved secondary work

- [the adjacent true-twin induced-`C_7` chain and its exact RED
  audit](../archive/adjacent-true-twin-c7-2026-08-17/README.md) are archived
  off the active spine;
- the former [exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)
  and its operation/model synchronization machinery remain available as a
  frozen critical-host refinement, not a second primary target;
- the rooted `K_5^-` fallback is not activated unless an actual T44
  counterexample is independently verified.
