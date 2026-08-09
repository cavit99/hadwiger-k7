# Current proof work

**Role:** concise navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md); exact hypotheses and
residues are recorded in the linked technical frontiers.

## Primary target

[Norin--Totschnig Conjecture 21](hc7_k7minus_seven_exceptional_frontier.md#1-primary-target-and-exact-finishing-reduction)

> Every graph with no `K_7^-` minor is six-colourable.

This is the sole active target.  It is not `HC_7`: a `K_7^-` minor need not
yield a `K_7` minor.

Selected audited inputs:

- [the critical host is `K_5`-free and has at least 25 degree-eight vertices](../results/hc7_k7minus_degree7_rooted_helper_closure.md#corollary-3-the-critical-host-is-k_5-free-and-has-many-degree-eight-vertices)
- [four independent centres give a rooted `K_5` model or an exact-cut lattice](../results/hc7_k7minus_four_centre_web_cut_lattice.md)
- [the web cut gives a response-carrying strict descent or a deficient colour-indexed fan](../results/hc7_k7minus_four_centre_operation_cut_reduction.md)
- [the rooted-web cut reduces canonically to an adhesion or a generalized-wheel torso](../results/hc7_k7minus_four_centre_tri_separation_reduction.md)
- [boundary replacement and anchored uncrossing give trace-preserving strict descent](../results/hc7_k7minus_four_centre_trace_descent.md)
- [the generalized-wheel outcome reduces to one canonical leaf with no two disjoint connected subgraphs adjacent to the whole boundary](../results/hc7_k7minus_four_centre_wheel_leaf_descent.md)
- [completing the boundary of a minimum exact-cut side gives a four-connected graph and an exact six-terminal rooted-minor criterion](../results/hc7_k7minus_four_centre_completed_side.md)
- [a partition-specific family of connected subgraphs reflects the fixed boundary colouring through an exact seven-cut](../results/hc7_exact7_selected_response_preservation.md)

Immediate barriers:

- [fullness and local root contacts alone do not force one-shore allocation](../barriers/hc7_k7minus_shore_allocation_barrier.md#theorem-2-two-full-shore-mechanism-barrier)
- [the nontriangular exact-cut trace and label-allocation residue](../results/hc7_k7minus_four_centre_web_cut_lattice.md#5-exact-static-limit-of-the-two-shore-quotient)
- [an undecorated mixed reduction does not retain the original boundary endpoint](../barriers/hc7_k7minus_tri_separation_boundary_trace_loss.md)
- [tri-inseparability and local degree conditions alone do not force two connected subgraphs adjacent to the whole boundary](../barriers/hc7_k7minus_tri_inseparable_full_subgraph_barrier.md)
- [internal six-connectivity, a boundary edge and a rooted `K_4` do not force the prescribed `K_6^-` minor](../barriers/hc7_k7minus_internal_six_rooted_k6minus_barrier.md)

## Active finishing route

[Critical-host exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)

A hypothetical counterexample has no degree-seven vertices, no literal
`K_5`, and at least 25 degree-eight vertices.  Thus proving that such a host
has at most 24 degree-eight vertices settles Conjecture 21.  The current
global theorem selects four independent centres.  For each selected root and
deletion-colouring, it returns either a colour-anchored rooted `K_5` avoiding
the other centres or a nontriangular two-shore order-seven cut in an exact
fixed-anchor lattice, with a retained one-sided trace and a Kempe linkage
through another named centre.  On the web side, the selected edge now gives
either a response-carrying smaller order-seven component or a five-spoke fan
with at least two missing limb contacts.  After minimizing the selected
component, every boundary replacement and every tri-separation below the
reduced cut that splits that component gives a smaller exact cut retaining
the fixed colouring and named vertices.  The canonical outcome is therefore
tri-inseparable on the selected component.  In the generalized-wheel
outcome, that component is exactly one canonical leaf; its three-vertex
boundary has an edge, and both
components lack two disjoint connected subgraphs adjacent to every boundary
vertex.  A Fano-plane construction shows that this conclusion cannot be
strengthened from tri-inseparability and degree conditions alone.  The
finishing step must allocate two additional branch sets in the rooted
outcome or, in the exact-cut outcome, realize the fixed boundary colour
classes by disjoint connected branch sets in the canonical region or build
the `K_7^-` minor directly.  Completing the selected boundary gives a
four-connected graph and reduces the wheel branch further to a prescribed
six-terminal `K_6^-` minor.  The small rooted obstruction shows that this
last step must use the full critical-host and component hypotheses.  Another
unlabelled separation or boundary census is not an accepted endpoint.

## Conditional and frozen routes

- [Seven-connected `4n-2` extremal theorem](hc7_k7minus_density_frontier.md):
  still open and sufficient for Conjecture 21, but no longer the primary
  route because it discards proper-minor colouring responses.
- [Auxiliary five-connected `4n-7` theorem](hc7_k7minus_e5_frontier.md):
  still open and stronger than the sufficient extremal theorem.  Further
  E5-specific enumeration is frozen absent an unbounded transferable theorem
  or a genuine counterexample.
- [Bounded-interface `HC_7` composition frontier](hc7_bounded_interface_synchronization_frontier.md):
  frozen; even a proof of Conjecture 21 would not prove `HC_7`.

Superseded work and earlier proof spines are preserved in
[`../archive/`](../archive/).
