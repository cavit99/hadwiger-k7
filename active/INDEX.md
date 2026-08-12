# Current proof work

**Role:** concise navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md); exact hypotheses and
residues are recorded in the linked technical frontier.

## Primary target

[Norin--Totschnig Conjecture 21](hc7_k7minus_seven_exceptional_frontier.md#1-primary-target-and-exact-finishing-reduction)

> Every graph with no `K_7^-` minor is six-colourable.

This is the sole active target.  It is not `HC_7`: a `K_7^-` minor need not
yield a `K_7` minor.

Selected audited inputs:

- [the critical host is seven-connected, `K_5`-free, has minimum degree at
  least eight and at least 25 degree-eight vertices](../results/hc7_k7minus_degree7_rooted_helper_closure.md#corollary-3-the-critical-host-is-k_5-free-and-has-many-degree-eight-vertices)
- [the six-coordinate host has the complete punctured signature cube, an
  exact spanning `K_7^vee` model and one cycle through all coordinates](../results/hc7_k7minus_six_coordinate_forest_reduction.md)
- [coordinate localisation reduces the six-cut row to a strict response or
  an order-eight or order-nine boundary with two or three full components](../results/hc7_k7minus_six_cut_coordinate_localisation.md)
- [the final six-cut shores have full-boundary fans and coordinate-specific
  six-fans; only their labels remain unaligned with the minor models](../results/hc7_k7minus_six_cut_fan_model_alignment.md)
- [the seven-connected row either grows to eight coordinates or has a
  feedback vertex set of order at most fourteen](../results/hc7_k7minus_six_coordinate_growth_or_feedback.md)
- [the feedback forest has exactly three structural outcomes: a full
  order-seven shore, a `7,6,7` three-piece path, or six large-contact
  components](../results/hc7_k7minus_feedback_forest_component_reduction.md)
- [a full order-seven separator cannot have a forest component, eliminating
  the first feedback outcome](../results/hc7_k7minus_forest_shore_four_colour_extension.md)
- [four-of-five incidence with one `K_5` model terminally closes the
  three-piece outcome](../results/hc7_k7minus_three_piece_k5_composition.md)
- [a portal edge and all six coordinates reduce to two cycles or an
  order-seven separation](../results/hc7_k7minus_portal_edge_cycle_threshold.md)

Immediate barriers:

- [contact data in a five-chromatic boundary do not alone force a two-set-
  transversal rooted `K_5` model](../barriers/hc7_feedback_boundary_rooted_k5_transversal_barrier.md)
- [three full components and ordinary boundary colouring do not force the
  adjacent-pair partition needed for four-colour gluing](../barriers/hc7_k7minus_three_full_component_partition_barrier.md)

## Immediate finishing route

[Critical-host exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)

Let `G` be a minor-minimal counterexample.  The removable-matching and
replacement theorems give a six-edge forest

\[
 F\cong6K_2\quad\hbox{or}\quad4K_2\mathbin{\dot\cup}P_3,
 \qquad X=G-F,
\]

where `X` is six-connected, two distinguished edges separately restore
seven-connectivity, every nonempty forest signature occurs, and `X` has an
exact spanning `K_7^vee` model.  The immediate target is the
**six-coordinate induced-forest terminalization theorem**.

If `kappa(X)=6`, each lifted coordinate either gives a strict
response-bearing separator or lies in a full component.  Excluding all
strict responses leaves only a boundary of order eight or nine and exactly
two or three full components.  Every completed shore has a full-boundary
fan, and every singleton coordinate supplies a shore-confined six-fan that
retains five prescribed Kempe first edges.  The immediate gap is one
boundary-respecting fan-to-model exchange: assign those paths to an
edge-rooted `K_6` model, glue the response, or return strict labelled
descent.

If `kappa(X)>=7`, either an eight-coordinate exact-model host exists or a
feedback set `T` of order at most fourteen does.  In the feedback row the
six centre edges can all be chosen across `T`; the forest reduction then
returns a full order-seven shore, a `7,6,7` three-piece path, or six
components each with at least eight neighbours in `T`.  The first outcome
is now impossible.  The three-piece case is terminal as soon as one `K_5`
model in `G[T]` meets each piece in at least four branch bags.  The remaining
work is to force that incidence, or to compose the six large-contact
components using the common cycle and the co-bagged `K_6` model.

In the direct exact-model row, one portal edge and all six coordinates lie
on at most two disjoint cycles.  The narrow composition target is to merge
those cycles using the exact model and the colouring responses, or return a
labelled order-seven separation.  Neither abstract signature counting nor
contact-only quotient splitting can supply that step.

## Conditional refinements and secondary laboratories

- [The centre-edge common-host theorem](../results/hc7_k7minus_five_centre_common_matching_reduction.md)
  retains the five centre labels, all multi-edge deletion and contraction
  responses, and the co-bagged models, but has separate order-two,
  order-three and dense connectivity rows.
- Its immediate row refinements are the
  [two-shore rooted-`K_4` theorem](../results/hc7_k7minus_five_centre_two_shore_rooted_k4.md),
  [signed four-crossing reduction](../results/hc7_k7minus_four_crossing_signed_boolean_reduction.md),
  [five-crossing omitted-coordinate theorem](../results/hc7_k7minus_five_crossing_omitted_coordinate_linkage.md),
  and [dense response-support theorem](../results/hc7_k7minus_dense_branch_rotation_visibility.md).
- [The five-centre rotation theorem](../results/hc7_k7minus_five_centre_rotation_reduction.md)
  remains available for labelled three-cut geometry; direct palette
  intersection is excluded by the
  [scoped palette barrier](../barriers/hc7_k7minus_five_rotation_palette_intersection_barrier.md).
- The older four-centre cut and fixed-trace programme, including its nearest
  synchronization barriers, is recorded in the
  [technical frontier](hc7_k7minus_seven_exceptional_frontier.md#4-current-global-finishing-obstruction).

## Conditional and frozen routes

- [Seven-connected `4n-2` extremal theorem](hc7_k7minus_density_frontier.md):
  still open and sufficient for Conjecture 21, but non-primary because it
  discards proper-minor colouring responses.
- [Auxiliary five-connected `4n-7` theorem](hc7_k7minus_e5_frontier.md):
  open and stronger than the sufficient extremal theorem; further
  E5-specific enumeration is frozen.
- [Bounded-interface `HC_7` composition frontier](hc7_bounded_interface_synchronization_frontier.md):
  frozen; Conjecture 21 itself would still not prove `HC_7`.

Superseded work and earlier proof spines are preserved in
[`../archive/`](../archive/).
