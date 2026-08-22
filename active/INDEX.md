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

- [four prescribed roots in a three-connected graph have a rooted
  `K_4^-` model](../results/rooted_k4minus_four_roots.md);
- [the double-cone theorem, two-near-full-model-bridges lemma and exact-cut
  normal form for a vertex-minimal nonliteral model](../results/hc7_k44_branch_model_and_double_cone.md);
- [every exact seven-cut boundary has minimum degree at most
  three](../results/hc7_k44_fourconnected_seven_boundary_double_cone.md);
- [the exterior of a literal core is three-connected](../results/hc7_literal_k44_exterior_threeconnectivity.md);
- [a four-portal exterior triangle is terminal](../results/hc7_k44_four_portal_triangle_completion.md);
- [a three-portal exterior `K_4` is terminal except for the exact
  tetrahedral profile, which spanning portal coverage excludes](../results/hc7_k44_three_portal_k4_tetrahedral_dichotomy.md);
- [one hash-pinned cold audit covers the five local statements other than
  the separately audited dense-boundary theorem](../results/hc7_k44_closure_local_normal_forms_audit.md).

## Falsification checkpoint

[Exact searches and certificate checks](experiments/k44_closure_falsification/README.md)
find no counterexample through order eleven and eliminate the whole
full-attachment non-clique seven-sum family.  These are bounded/family
results only.  The sharp local survivor is the 19-contact tetrahedral
profile, whose connectivity is four.

The separate [literal labelled-trichotomy
census](experiments/k44_literal_labelled_trichotomy/README.md) checks every
three-connected exterior through order seven against all eight-label
incidence assignments.  It finds no survivor, but its UNSAT conclusions
depend on Z3 and are bounded evidence only.

## Two open obligations

1. **Literal portal exchange.**  Prove the pure labelled trichotomy:
   a triangle of three four-portal bags, a spanning `K_4` of four
   three-portal bags, or six positive-portal bags forming a `K_6^-` model.
   The whole literal core joins the last outcome to the target.
2. **Nonliteral model-trace rotation.**  Use the exact seven-cut through an
   internal branch edge to construct a strictly smaller labelled
   `K_{4,4}` model or the target.  Exact cuts alone do not give laminarity,
   a peel side or preserved branch ownership.

Immediate barriers:

- [a fat triangle with seven local paths and a split edge with six alternate
  paths can both remain target-free](../barriers/hc7_k44_shortcut_certificate_barriers.md);
- the existing core-sensitive trichotomy is the whole literal theorem in
  structured form, not a proved intermediate capstone;
- a component of an exact-cut complement may contain pieces of several
  branch bags, so fullness to the cut cannot be counted as external
  branch-set contact.

## Preserved secondary work

- [the adjacent true-twin induced-`C_7` chain and its exact RED
  audit](../archive/adjacent-true-twin-c7-2026-08-17/README.md) are archived
  off the active spine;
- the former [exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)
  and its operation/model synchronization machinery remain available as a
  frozen critical-host refinement, not a second primary target;
- the rooted `K_5^-` fallback is not activated unless an actual T44
  counterexample is independently verified.
