# Selected completed proofs

**Role:** reader navigation only.  This is not a second research ledger and
it is not an exhaustive catalogue of `results/`.  Current status is governed
by [`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md), and the sole live proof
spine is mapped in [`../active/INDEX.md`](../active/INDEX.md).

Directory placement does not establish a claim.  The entries below have
written proofs and adjacent hash-pinned internal audits.  An internal audit
is not external peer review.

The universal bipartite theorem subsumes the earlier bipartite target
families below. Each precursor retains its original proof and exact scope;
the limitations of an earlier argument are not current open bipartite cases.

## Standalone and reusable theorems

| Theorem | Proof and audit | Exact scope |
|---|---|---|
| Every finite bipartite graph is contractible | [Proof](bipartite_contractibility_via_matroid_reduction.md) · [GREEN audit](bipartite_contractibility_via_matroid_reduction_audit.md) · [second GREEN audit](bipartite_contractibility_via_matroid_reduction_second_audit.md) · [manuscript](../paper/bipartite-contractibility/main.pdf) | Every scheme yields the fully prescribed rooted minor. No degree, order or path-length bound. The intended BLR flow assertion follows independently; priority and comparative significance remain qualified. |
| Three-edge bipartite schemes have rooted models of intrinsic radius two | [Proof](bipartite_short_scheme_radius.md) · [GREEN audit](bipartite_short_scheme_radius_audit.md) | Every bag stays within two edges of its original root, internally. Radius one is insufficient. No bound for longer schemes is established. |
| Degree at most three on one bipartition side forces a minor retaining all prescribed roots on the opposite side | [Proof](degree_three_bipartite_weak_contractibility.md) · [GREEN audit](degree_three_bipartite_weak_contractibility_audit.md) | Includes weak contractibility of every `K_{3,n}` and every bipartite subcubic target; does not retain all roots on the degree-bounded side. |
| Universal weak and rooted bipartite contractibility are equivalent | [Proof](bipartite_weak_to_rooted.md) · [GREEN audit](bipartite_weak_to_rooted_audit.md) | An exact polynomial reduction with pendant four-cycles forces prescribed roots in an enlarged target. Neither universal statement is proved by the reduction. |
| Every bipartite graph with degree at most two on one specified side is contractible | [Proof](even_subdivision_contractibility.md) · [GREEN cold audit](even_subdivision_contractibility_audit.md) · [separate GREEN proof and qualified novelty audit](even_subdivision_contractibility_literature_audit.md) | Includes every replacement of the edges of an arbitrary loopless multigraph by paths of positive even length, a family of unbounded treewidth. |
| Every complete bipartite graph `K_{2,n}` is contractible | [Proof](k2n_contractibility_via_matroid_packing.md) · [GREEN audit](k2n_contractibility_via_matroid_packing_audit.md) · [four-page DRAFT](../paper/k2n-contractibility/main.pdf) | Computation-free; answers the `K_{2,4}` half of Kündgen--Pelsmajer--Ramamurthi's Section 8, Question 2. |
| Four literal root edges complete five-root partial routing | [Proof](llru_question61_via_km_property_star.md) · [GREEN audit](llru_question61_via_km_property_star_audit.md) · [second GREEN cold audit](llru_question61_via_km_property_star_second_cold_audit.md) | Answers Lafferty--Liu--Rolek--Yu Question 6.1 and gives their stated eight-connectivity threshold `k>=11`.  It is an application of Kriesell--Mohr property `(*)`. |
| Every three-connected graph has a rooted `K_4^-` minor at any four prescribed roots | [Proof](rooted_k4minus_four_roots.md) · [GREEN audit](rooted_k4minus_four_roots_audit.md) | Elementary unbounded proof.  The missing quotient edge is not prescribed, and the model need not span. |
| Five prescribed roots containing a triangle force a rooted wheel under internal five-connectivity and at least two nonroots | [Proof, Lemma 1](hc7_degree8_two_triangle_exterior.md) · [GREEN audit](hc7_degree8_two_triangle_exterior_audit.md) | No separate degree hypothesis; stopping the root-preserving contraction at two nonroots strengthens the [earlier wheel theorem](hc7_five_root_wheel.md). |
| Nonroot degree seven, with at most five degree-six exceptions, strengthens the five-root wheel to `K_5^-` | [Proof](hc7_five_root_almost_clique.md) · [GREEN audit](hc7_five_root_almost_clique_audit.md) | Under the same rooted boundary and triangle hypotheses, nine contacts survive; the triangle endpoint of the possible missing pair can be designated in advance. No extra helper is guaranteed. |
| Five-root `K_5^-` with unrestricted degree-six nonroots | [Proof](hc7_five_root_degree_six.md) · [GREEN audit](hc7_five_root_degree_six_audit.md) | A nonempty nonroot set, internal five-connectivity and a root triangle suffice when every nonroot has degree at least six. At least two triangle roots can be the missing-edge endpoint; this theorem does not prescribe a particular one. |
| Full regions turn a linkage into a paired clique | [Proof](paired_clique_one_sided_regions.md) · [GREEN audit](paired_clique_one_sided_regions_audit.md) | For disjoint k-sets R,S, a k-linkage and k−1 connected regions full to R, avoiding R and covering S with at least one S terminal each, give k pairwise adjacent R/S-paired bags. This strengthens the [two-sided theorem](paired_clique_full_regions.md); no C19 application is established. |

The later [odd-cycle attachment counterexamples](../barriers/triangle_free_bipartite_attachment_counterexample.md),
with a [separate GREEN audit](../barriers/triangle_free_bipartite_attachment_counterexample_audit.md),
refute triangle-free sufficiency and hereditary canonical-test sufficiency.
Every subgraph of each target passes the canonical two-copy test, while an
explicit scheme has no fully rooted minor. The bipartite theorem is unaffected.

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

For the companion target, the
[cycle-and-triangle](hc7_degree8_cycle_exterior.md) and
[two-triangle](hc7_degree8_two_triangle_exterior.md) exterior theorems, with
their [first](hc7_degree8_cycle_exterior_audit.md) and
[second](hc7_degree8_two_triangle_exterior_audit.md) GREEN audits, make
`G-N[v]` connected and full to all eight neighbours in both remaining
spanning configurations. The cycle case also gives exterior minimum degree
five. Neither theorem supplies the remaining simultaneous allocation.
The [cycle-complement theorem](hc7_cycle_triangle_complement_three_connectivity.md),
with [two](hc7_cycle_triangle_complement_three_connectivity_audit.md)
[GREEN audits](hc7_cycle_triangle_complement_three_connectivity_second_audit.md),
excludes every two-cut of `G-v-C`. The resulting
[complete cycle-case theorem](hc7_degree8_cycle_triangle_closure.md), with
[two](hc7_degree8_cycle_triangle_closure_audit.md)
[GREEN audits](hc7_degree8_cycle_triangle_closure_second_audit.md), uses a
three-region contact construction to close the entire five-cycle case.
The [two-triangle separator theorem](hc7_two_triangle_separator_allocation.md),
with its [GREEN audit](hc7_two_triangle_separator_allocation_audit.md), makes
each A-side two-connected and its minimal torso four-connected. Building
on it, the [complement theorem](hc7_two_triangle_complement_four_connectivity.md),
with [two](hc7_two_triangle_complement_four_connectivity_audit.md)
[GREEN audits](hc7_two_triangle_complement_four_connectivity_second_audit.md),
closes the entire three-cut case: both `G-v-A` and `G-v-B` are four-connected.
Its explicit region and port constructions preserve disjoint original bags.
The [spanning-helper theorem](hc7_two_triangle_exterior_helpers.md), with
its [GREEN audit](hc7_two_triangle_exterior_helpers_audit.md), now makes
the exterior plus `x,y` two-connected and gives two spanning x/y-rooted
parts with all but at most one contact to either specified triangle.
The [two-response theorem](hc7_two_triangle_two_responses.md), with its
[GREEN audit](hc7_two_triangle_two_responses_audit.md), strengthens this:
at most one root of either triangle can occur in an exterior four-boundary
of its complementary deletion, so at least two root deletions succeed.
These responses do not give a common partition for both triangles or the
additional division of the parts needed for the global construction.
The [central-root normalization](hc7_seven_boundary_path_allocation.md),
with its [GREEN audit](hc7_seven_boundary_path_allocation_audit.md),
concentrates a remaining seven-boundary model on three port bags and one
path; distinct boundary contacts in those bags are still not guaranteed.
The [reserved-neighbour theorem](hc7_two_triangle_reserved_neighbours.md),
with its [GREEN audit](hc7_two_triangle_reserved_neighbours_audit.md),
keeps three of four additional neighbours outside a four-rooted clique.
Its four-failure alternative gives an explicit `Q` construction; the
successful rooted-clique alternative still requires a compatible helper.
The [whole-colour-class reservation](hc7_critical_colour_class_reservation.md),
with its [GREEN audit](hc7_critical_colour_class_reservation_audit.md),
keeps all four additional neighbours outside a rooted four-clique under
the critical colouring hypotheses. It also supplies actual-root K5 schemes
for every independent triple reservation, in both matching branches;
rooted K5 extraction and a compatible seven-bag extension remain open.
The two-triangles-and-edge case and Conjecture 19 remain open.

The [colour-path completion](hc7_cycle_colour_path_completion.md), with
its [GREEN audit](hc7_cycle_colour_path_completion_audit.md), extends the
[marked-scheme proof](hc7_marked_k33_scheme_completion.md): any two extra
root connections or the two crossed colour paths suffice. It reduces every
reserved-triple colouring to one two-pair pattern by a single Kempe swap.
The simultaneous endpoint choice in that pattern remains open.

## Selected foundational inputs to the preserved T44 campaign

T44 remains open. Its direct proved inputs are maintained in the
[technical frontier](../active/hc7_k44_closure_frontier.md).
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
technical frontier. The unproved completion obligations remain in the
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
