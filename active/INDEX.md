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
- [every three-support bond in a nonsingleton blocker is terminal; the
  four-connected case is impossible, the selected minimum support-full bond
  shore opposite the specified `p` is a sequential path, and every surviving
  three-cut has exactly two
  components](../results/hc7_k44_three_support_bond_and_threecut_reduction.md);
- [at a surviving two-component three-cut, each support meets the cut at
  most once, the five supports have one of two exact incidence types, and
  every choice of a two-element pair in a whole support on each side and a
  cross-component pair in a bridge support is weakly linkable; a
  smallest three-support component has a four-connected triangle-boundary
  torso](../results/hc7_k44_two_component_threecut_support_normal_form.md);
- [an adjacent singleton edge has an exact two- or three-component
  contraction trace](../results/hc7_k44_adjacent_singleton_contraction_trace.md);
- [every unbalanced or balanced two-component literal-shore split yields an
  explicit `K_7^-` minor](../results/hc7_k44_two_component_shore_split_elimination.md);
- [every three-component whole-shore trace yields an explicit `K_7^-`
  minor](../results/hc7_k44_three_component_trace_elimination.md); and
- [the sole core-concentrated trace has joint endpoint-contact rank at most
  three; its one-defect split is target-producing, and under target-free
  hypotheses failure returns a marked proper connected separator
  side](../results/hc7_k44_core_concentrated_joint_contact_reduction.md).

A [hash-pinned internal cold audit](../results/hc7_k44_closure_local_normal_forms_audit.md)
covers the five local statements other than the separately audited
dense-boundary theorem.  Each newer literal reduction has its own adjacent
hash-pinned GREEN internal audit.

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

The [spanning-split hostile
screen](experiments/k44_literal_spanning_split_search/README.md) checks both
the exact and stronger anchored negations on all 422 eligible
minimum-degree-four order-eight hosts and three targeted order-nine families.
It finds no survivor.  This is independently audited bounded evidence with
Z3 as the decisive trust boundary, not an unbounded theorem.

## Two open obligations

1. **Literal exact-residue completion.**  Prove the triangle-boundary torso
   bisection lemma for a nonsingleton blocker.  The selected minimum
   support-full bond shore opposite the specified `p` is already a path with
   two split endpoint supports and three
   sequential internal supports, and every survivor has connectivity exactly
   three.  Every three-cut already has exactly two components, both meeting
   the minimum path.  Its supports have the two exact incidence types in the
   audited normal form, and a smallest component meeting three supports has
   a four-connected torso.  Find inside that component a connected
   nonseparating set meeting every external support and splitting every whole
   support.  For the sole
   adjacent-singleton residue, eliminate
   the entire core-concentrated target-free profile.  The present reduction
   returns a marked separator, but neither an exact-seven completion theorem
   nor a well-founded descent through larger separators is proved.  Closing
   both local residues must also establish the
   [hypothesis-class closure needed for induction](hc7_k44_closure_frontier.md#44-the-hypothesis-class-needed-for-induction)
   before the pure labelled trichotomy or the literal theorem follows.
2. **Nonliteral model-trace rotation.**  Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target.  Exact cuts alone do not give laminarity,
   a peel side or preserved branch ownership.

Immediate nonsingleton lemma: [prove the triangle-boundary torso bisection
lemma in the selected four-connected three-support
torso](../results/hc7_k44_two_component_threecut_support_normal_form.md#4-exact-localized-completion-lemma).

Immediate barriers:

- **Barrier/counterexample to local shortcut claims:** [a fat triangle with
  seven local paths and a split edge with six alternate
  paths can both remain target-free](../barriers/hc7_k44_shortcut_certificate_barriers.md);
- **Barrier to a prescribed local path step:** [the path data and boundary
  inequalities do not force a bond which separates a fixed anchor from a
  fixed `b`-support vertex while splitting the three prescribed internal
  supports](../barriers/hc7_k44_minimum_path_internal_transversal_barrier.md).
  The example has other three-support bonds, so it does not refute the
  triangle-boundary torso bisection lemma;
- **Barrier to quotient-only completion:** [the mandatory two-component
  support incidences alone admit a thirteen-vertex literal-core quotient
  whose exact `K_7^-` contact optimum is
  nineteen](../barriers/hc7_k44_two_component_quotient_completion_barrier.md).
  It fails `q>=6`, support multiplicity and the minimum-path normal form, so
  the live proof must use that uncontracted structure;
- **Barrier to a stripped torso proof:** [a `K_5` triangle-boundary torso can
  satisfy every local three-support inequality but have no connected
  nonseparating set meeting both external supports and splitting the whole
  support](../barriers/hc7_k44_three_support_torso_bisection_barrier.md).
  This proves only that the local torso hypotheses are insufficient; the
  global bond restriction, support provenance, complementary supports,
  minimum path and distinguished incidences remain available;
- **Singleton reduction and exact remaining target:** [the core-concentrated
  joint-contact reduction](../results/hc7_k44_core_concentrated_joint_contact_reduction.md)
  forces joint contact rank at most three and, in the target-free profile,
  returns a marked proper connected separator side if the one-defect
  two-helper split fails.  A verified
  [order-three incidence profile](../barriers/hc7_k44_core_concentrated_bisection_incidence_barrier.md)
  shows that the local boundary inequalities alone do not force that split;
  the remaining theorem must eliminate the whole profile.  Making the new
  separator exact is only a milestone until exact-seven completion is proved;
  using its excess requires a descent with an explicit decreasing quantity;
- **Recorded route nonclosure:** [a component of an exact-cut complement may
  contain pieces of several branch bags](../results/hc7_k44_branch_model_and_double_cone_audit.md#exact-scope),
  so fullness to the cut cannot be counted as external branch-set contact.

The [cold-start handoff](hc7_k44_closure_frontier.md#43-cold-start-handoff)
states both literal residues with their exact quantifiers and gives the
re-entry verification commands.

## Preserved secondary work

- [even-subdivision contractibility](../results/even_subdivision_contractibility.md),
  with two separate internal audits, is a completed independent theorem;
  it extends the earlier `K_{2,n}` result and is not a T44 input;
- [the adjacent true-twin induced-`C_7` chain and its exact RED
  audit](../archive/adjacent-true-twin-c7-2026-08-17/README.md) are archived
  off the active spine;
- the former [exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)
  and its operation/model synchronization machinery remain available as a
  frozen critical-host refinement, not a second primary target;
- the rooted `K_5^-` fallback is not activated unless an actual T44
  counterexample is independently verified.
