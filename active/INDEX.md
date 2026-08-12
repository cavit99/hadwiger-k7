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
- [two opposite matching coordinates have one exact response square, one
  common co-bagged `K_6` model and, after bounded responses are excluded,
  one seven-connected exact-model host](../results/hc7_k7minus_matching_square_common_state.md)
- [splitting the co-bagged root along the selected equality edge gives
  `K_7^-` or an actual separator retaining that edge and its rejected
  boundary partition](../results/hc7_k7minus_selected_edge_root_bag_response.md)
- [large actual response boundaries descend numerically to orders seven
  through nine via fresh singleton responses, while an all-lock response
  has five dominating three-chromatic components or a bounded response
  endpoint](../results/hc7_k7minus_matching_lock_boundary_reduction.md)
- [an unlocked order-nine transition is supported on at most four original
  boundary vertices and returns either a doubly rejected trace or one
  opposite-shore boundary interchange](../results/hc7_k7minus_order9_crossed_transition_projection.md)
- [the induced-path row has two seven-connected response hosts, one common
  three-coordinate model and an exact triple-split obstruction](../results/hc7_k7minus_p3_opposite_coordinate_common_model.md)
- [the seven-connected row either grows to eight coordinates or has a
  feedback vertex set of order at most fourteen](../results/hc7_k7minus_six_coordinate_growth_or_feedback.md)
- [degree counting eliminates every feedback set of order at most fourteen
  whose induced graph is at least five-chromatic](../results/hc7_k7minus_bounded_feedback_degree_elimination.md)
- [a portal edge and all six coordinates reduce to two cycles or an
  order-seven separation](../results/hc7_k7minus_portal_edge_cycle_threshold.md)

Immediate barriers:

The first item is a recorded route nonclosure, not a counterexample.

- [one fixed all-lock colouring cannot convert a blocked branch-set
  transfer into the required labelled response](hc7_k7minus_all_lock_branch_transfer_gate.md)
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
strict responses leaves only boundary order eight or nine.  In the
order-nine matching row, two opposite distinguished coordinates now share
the complete nonempty response square, a co-bagged `K_6` model and, after
bounded responses are excluded, a seven-connected exact `K_7^vee` host.
Splitting the selected equality edge in that common root bag already gives
`K_7^-` or an actual response separator retaining the edge, model split and
rejected boundary partition; only the numerical descent to orders seven
through nine loses those labels.
The missing all-proper signature forces either a projected boundary
transition, a response of order at most nine, or five dominating
three-chromatic lock components.  The immediate gap is to allocate one of
those objects to four foreign model bags while preserving its labels.  In
particular, the audited fixed-lock transfer gate shows that minimising and
absorbing pieces of one lock component cannot supply the colouring labels:
a proper lock prefix is not switchable, while the whole-component switch
leaves the selected edge monochromatic.  A matching-row continuation must
therefore compare different realised signatures or use target exclusion,
not repeat fixed-colouring branch-set transfer.  In
the induced-`P_3` row, one common model co-bags the crossing coordinate and
the entire path; the exact gap is to make four foreign bags meet all three
split pieces, or return a labelled order-seven response.

If `kappa(X)>=7`, either an eight-coordinate exact-model host exists or a
feedback set `T` of order at most fourteen does.  The new degree-elimination
theorem rules out the latter alternative directly from the critical-host
degree defect and the forest identity.  Thus this row now consists only of
the eight-coordinate seven-connected deletion host with its complete
punctured response cube and exact spanning `K_7^vee` model.  The former
full-shore, `7,6,7` and six-component cases are no longer live obligations.

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
