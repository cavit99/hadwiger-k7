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
| Every complete bipartite graph `K_{2,n}` is contractible | [Proof](k2n_contractibility_via_matroid_packing.md) · [GREEN audit](k2n_contractibility_via_matroid_packing_audit.md) | Computation-free; answers the `K_{2,4}` half of Kündgen--Pelsmajer--Ramamurthi's Section 8, Question 2.  It does not settle `K_{3,3}`. |
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

These are necessary structural theorems about a hypothetical counterexample.
They do not prove the `K_7^-` six-colour conjecture or `HC_7`.

## Direct proved inputs to the active T44 campaign

T44 remains open.  Its direct proved inputs are kept deliberately small in
the [active index](../active/INDEX.md):

- [branch-model normal forms and the double-cone theorem](hc7_k44_branch_model_and_double_cone.md), with [audit](hc7_k44_branch_model_and_double_cone_audit.md);
- [the restriction on exact seven-cut boundaries](hc7_k44_fourconnected_seven_boundary_double_cone.md), with [audit](hc7_k44_fourconnected_seven_boundary_double_cone_audit.md);
- [connectivity of the exterior of a literal `K_{4,4}`](hc7_literal_k44_exterior_threeconnectivity.md), with [audit](hc7_literal_k44_exterior_threeconnectivity_audit.md);
- [four-portal triangle completion](hc7_k44_four_portal_triangle_completion.md), with [audit](hc7_k44_four_portal_triangle_completion_audit.md); and
- [the three-portal `K_4` dichotomy](hc7_k44_three_portal_k4_tetrahedral_dichotomy.md), with [audit](hc7_k44_three_portal_k4_tetrahedral_dichotomy_audit.md).

The [local-normal-forms cold audit](hc7_k44_closure_local_normal_forms_audit.md)
checks the package at its pinned revisions and states explicitly what it does
not prove.  The two unproved completion obligations remain in the
[T44 technical frontier](../active/hc7_k44_closure_frontier.md).

## Finding other material

The directory also contains route-internal lemmas, finite results, audit
notes and historical promoted claims.  Use the repository search and context
tools described in [`../tools/README.md`](../tools/README.md), then check the
ledger and the adjacent audit before relying on a result.  Frozen proof
routes are navigated from the ledger; refuted intermediate principles belong
in [`../barriers/`](../barriers/), and superseded work belongs in
[`../archive/`](../archive/).
