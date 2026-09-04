# Selected completed proofs

**Role:** reader navigation only.  This is not a second research ledger and
it is not an exhaustive catalogue of `results/`.  Current status is governed
by [`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md), and the sole live proof
spine is mapped in [`../active/INDEX.md`](../active/INDEX.md).

Directory placement does not establish a claim.  The entries below have
written proofs and adjacent hash-pinned internal audits.  An internal audit
is not external peer review.

## Standalone and reusable theorems

| Theorem | Proof and audit | Exact scope |
|---|---|---|
| Every bipartite graph with degree at most two on one specified side is contractible | [Proof](even_subdivision_contractibility.md) · [GREEN cold audit](even_subdivision_contractibility_audit.md) · [separate GREEN proof and qualified novelty audit](even_subdivision_contractibility_literature_audit.md) | Includes every replacement of the edges of an arbitrary loopless multigraph by paths of positive even length. Extends `K_{2,n}` to a family of unbounded treewidth; does not settle `K_{3,3}`, all bipartite theta graphs, or a Hadwiger conjecture. |
| Every complete bipartite graph `K_{2,n}` is contractible | [Proof](k2n_contractibility_via_matroid_packing.md) · [GREEN audit](k2n_contractibility_via_matroid_packing_audit.md) · [four-page DRAFT](../paper/k2n-contractibility/main.pdf) | Computation-free; answers the `K_{2,4}` half of Kündgen--Pelsmajer--Ramamurthi's Section 8, Question 2.  It does not settle `K_{3,3}`. |
| Four literal root edges complete five-root partial routing | [Proof](llru_question61_via_km_property_star.md) · [GREEN audit](llru_question61_via_km_property_star_audit.md) · [second GREEN cold audit](llru_question61_via_km_property_star_second_cold_audit.md) | Answers Lafferty--Liu--Rolek--Yu Question 6.1 and gives their stated eight-connectivity threshold `k>=11`.  It is an application of Kriesell--Mohr property `(*)`. |
| Every three-connected graph has a rooted `K_4^-` minor at any four prescribed roots | [Proof](rooted_k4minus_four_roots.md) · [GREEN audit](rooted_k4minus_four_roots_audit.md) | Elementary unbounded proof.  The missing quotient edge is not prescribed, and the model need not span. |

## Structural results for the `K_7^-` critical host

The compact [low-degree manuscript](../paper/k7minus-low-degree/main.pdf)
packages the computation-free baseline: degree seven is excluded,
`delta(G)>=8`, `|E(G)|>=4|V(G)|`, there is no `K_5` subgraph, and
`n_8>=25+tau`.  It is a DRAFT with a
[GREEN internal audit](../paper/k7minus-low-degree/main_audit.md).

Later theorem notes strengthen and extend that snapshot:

| Theorem | Proof and audit | Consequence |
|---|---|---|
| A low-codegree edge at every degree-eight vertex in a six-connected target-free graph | [Proof](hc7_k7minus_sixconnected_degree_eight_low_codegree.md) · [two GREEN internal audits](hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md) | Uses a deterministic finite local lemma and an unbounded host reduction; proves the defect ladder `D(G)>=20+kappa(G)` and upgrades the critical-host count to `n_8>=27+tau`. |
| Capacity of a seven-vertex cut in the critical host | [Proof](hc7_k7minus_critical_seven_cut_capacity.md) · [GREEN audit](hc7_k7minus_critical_seven_cut_capacity_audit.md) | Leaves two or three components and sharply constrains their boundary-full connected subgraphs and boundary colouring. |
| Exclusion of the remaining three-component `3,2,2` cut | [Proof](hc7_k7minus_three_component_seven_cut_exclusion.md) · [GREEN audit](hc7_k7minus_three_component_seven_cut_exclusion_audit.md) | Computation-free; together with the capacity theorem, every seven-vertex cut in the critical host leaves exactly two components. |
| Safe literal-core contractions in the critical host | [First safe edge](hc7_k44_critical_safe_contraction.md) · [preservation refinement](hc7_k44_safe_contraction_preservation.md) · [GREEN audit](hc7_k44_safe_contraction_preservation_audit.md) | The first safe quotient is seven-connected. Exterior order at least eight gives a second safe contraction preserving seven-connectivity. No unbounded induction or literal T44 closure follows. |

These are necessary structural theorems about a hypothetical counterexample.
They do not prove the `K_7^-` six-colour conjecture or `HC_7`.

## Selected foundational inputs to the active T44 campaign

T44 remains open.  The exact current set of direct proved inputs is maintained
only in the [active index](../active/INDEX.md), so it is not duplicated here.
The following are selected foundational results:

- [branch-model normal forms and the double-cone theorem](hc7_k44_branch_model_and_double_cone.md), with [audit](hc7_k44_branch_model_and_double_cone_audit.md);
- [the restriction on exact seven-cut boundaries](hc7_k44_fourconnected_seven_boundary_double_cone.md), with [audit](hc7_k44_fourconnected_seven_boundary_double_cone_audit.md);
- [connectivity of the exterior of a literal `K_{4,4}`](hc7_literal_k44_exterior_threeconnectivity.md), with [audit](hc7_literal_k44_exterior_threeconnectivity_audit.md);
- [four-portal triangle completion](hc7_k44_four_portal_triangle_completion.md), with [audit](hc7_k44_four_portal_triangle_completion_audit.md);
- [the three-portal `K_4` dichotomy](hc7_k44_three_portal_k4_tetrahedral_dichotomy.md), with [audit](hc7_k44_three_portal_k4_tetrahedral_dichotomy_audit.md); and
- [the weighted-splitter small-atom reduction](hc7_k44_weighted_splitter_small_atom_reduction.md), with [audit](hc7_k44_weighted_splitter_small_atom_reduction_audit.md).

The [local-normal-forms cold audit](hc7_k44_closure_local_normal_forms_audit.md)
checks its five named statements at pinned revisions and states explicitly
what it does not prove.  The later direct literal reductions—positive-atom
elimination, the minimum-blocker theorem, the contraction trace, both trace
eliminations, and the joint-contact separator theorem—are navigated from the
active index.  The two unproved completion obligations remain in the
[T44 technical frontier](../active/hc7_k44_closure_frontier.md).

The audited [three-support bond and three-cut
reduction](hc7_k44_three_support_bond_and_threecut_reduction.md) lowers the
terminal threshold to any three split supports, eliminates the entire
four-connected nonsingleton case and proves that every surviving three-cut
has exactly two components.  The adjacent [two-component support normal
form](hc7_k44_two_component_threecut_support_normal_form.md) reduces those
cuts to two exact support-incidence types and then to a smallest
three-support side with a four-connected triangle-boundary torso.  Neither
result proves the remaining torso bisection lemma.

The earlier nonsingleton two-helper criterion also has an audited
[spanning and split-count normal form](hc7_k44_spanning_two_helper_split_count.md):
unused blocker components can be absorbed without increasing defect, after
which the exact threshold is three split supports when the second side sees
`b` and four when it misses `b`.  This remains useful bookkeeping, but the
later `b`-independent three-support construction supersedes it as the live
terminal threshold.

## Finding other material

The directory also contains route-internal lemmas, finite results, audit
notes and historical promoted claims.  Use the repository search and context
tools described in [`../tools/README.md`](../tools/README.md), then check the
ledger and the adjacent audit before relying on a result.  Frozen proof
routes are navigated from the ledger; refuted intermediate principles belong
in [`../barriers/`](../barriers/), and superseded work belongs in
[`../archive/`](../archive/).
