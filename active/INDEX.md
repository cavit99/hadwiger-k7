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
- [a six-coordinate induced forest supplies the complete punctured
  signature cube, two seven-connected restorations, an exact spanning
  `K_7^vee` model and a common coordinate cycle](../results/hc7_k7minus_six_coordinate_forest_reduction.md)
- [degree counting eliminates bounded feedback and forces the
  eight-coordinate seven-connected exact-model host](../results/hc7_k7minus_bounded_feedback_degree_elimination.md)
- [maximal endpoint visibility reduces that host to `K_7^-` or a bounded
  response interface, while identifying the exact coordinate-label loss](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md)
- [model-anchored minimisation leaves a boundary-list-critical core and at
  most two coordinate-free appendages, each monopolising at least two
  disjoint model adjacencies](../results/hc7_k7minus_model_anchored_appendage_ownership.md)
- [a singleton response has either one common induced-path operation or a
  dominated coordinate edge](../results/hc7_k7minus_singleton_coordinate_localisation.md)
- [the dominated case is model-aligned in every degree; the only finite
  low-degree placements are eliminated by exact minor verification](../results/hc7_k7minus_dominated_singleton_low_degree_terminal.md)
- [centre-preserving visibility bypasses the unbounded side and exposes an
  exact order-eight boundary carrying the other four centre operations](hc7_k7minus_degree_eight_centre_cube_interface.md)

Immediate barriers:

- [a singleton coordinate response can have arbitrarily large boundary even
  under stronger connectivity and degree bounds](../barriers/hc7_k7minus_anchored_coordinate_compression_barrier.md).
  The construction contains a literal `K_7`, so it isolates the need to use
  target exclusion rather than refuting the desired disjunction.

## Immediate finishing route

[Critical-host exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)

Let `G` be a minor-minimal counterexample.  The direct campaign supplies a
six-edge componentwise-induced forest

\[
 F\cong6K_2\quad\hbox{or}\quad4K_2\mathbin{\dot\cup}P_3,
 \qquad X=G-F.
\]

Its two connectivity cases are exhaustive.

If `kappa(X)>=7`, the forest grows to eight coordinates: `H=G-F_8` is
seven-connected, realises all `255` nonempty signatures, and has an exact
spanning `K_7^vee` model.  Maximising coordinate-endpoint visibility in
that model gives `K_7^-` or an actual separator retaining one singleton
`F_8` response.

The response side can now be minimised without discarding its exact-model
geometry.  If it is nonsingleton, it consists of one boundary-list-critical
core and at most two coordinate-free appendages.  Each appendage monopolises
at least two disjoint foreign model adjacencies.  Deleting an attachment
edge supplies a fresh response, but comparison with the retained forest
coordinate does not exchange their model provenance; both exhaustive
[static quotient diagnostics](experiments/model_anchored_appendage_quotient_gate/README.md)
leave target-free contact profiles.

If the minimum side is a singleton, its forest response localises exactly.
A fresh nonadjacent neighbour gives one induced-path deletion host with all
three nonempty signatures.  Every failure of seven-connectivity returns an
actual order-seven or order-eight response retaining that whole square; the
seven-connected outcome is the existing induced-path triple-split
allocation problem.  Otherwise the forest edge is dominated.  That case is
now aligned in every degree: one common deletion preserves the original
exact model, original coordinate colouring, a fresh exclusive response and
an actual response component.  What is not implied is that this component
lies in one branch bag or has a named anticomplete bag.

Centre-preserving visibility gives more at a dominated degree-eight
singleton.  Its exterior is connected, its exact boundary is
`N(u)=Q\dot\cup\{v\}`, and `Q` is one of three seven-vertex graphs.  In
`H=G-\{u,v\}`, protect `Q` and two of the four other exceptional centres.
One common terminal-legal contraction then leaves a rooted kernel of order
nine or ten: the complete order-eleven branch is eliminated.  The order-ten
catalogue has 1,153 rooted occurrences and an independent checker confirms
that one usable centre-to-`Q`-bag coordinate contact closes every one.  At
order nine, two usable contacts close every survivor; a single contact
closes all but 75 asymmetric placements.

The immediate target is therefore an **operation-labelled contact-or-split
theorem for two protected centres**.  For a selected centre edge, either its
mate lies in a usable `Q`-rooted bag, or the singleton-signature colouring
produces a movable split of its centre-rooted bag or an actual labelled
separation.  This is the missing host input.  Ordinary rooted-bag
minimisation and exact two-owner suffix transfer leave `256`, `1022`, and
`256` order-nine placements, so static ownership is decisively exhausted.
The nonsingleton model-anchored outcome still has the parallel operation-
transfer obligation across at most two appendages.

If `kappa(X)=6`, the matching and induced-`P_3` cases remain deferred.  In
the matching case the full `EP,PE,EE` comparison proves a literal
Kempe-component interaction only when one common `EE` pivot is supplied.
Neither the response square nor static branch-set deficiency profiles force
that pivot to repair a missing model contact.  In the path case, four
foreign bags must still meet all three pieces of one co-bagged path, or a
labelled response must be returned.

The separate exact-model route retains one further conditional problem: a
portal edge and all six original coordinates lie on at most two disjoint
cycles.  Merging them still requires the critical colouring data or a
labelled order-seven separation.

## Conditional refinements and secondary laboratories

- [The cross-signature matching gate](hc7_k7minus_cross_signature_pivot_gate.md)
  records the shared-pivot theorem and exact route nonclosure.  The
  [static two-split profile barrier](../barriers/hc7_k7minus_static_two_split_profile_barrier.md)
  proves that uncoloured model contacts cannot supply the missing exchange.
- [The centre-edge common-host theorem](../results/hc7_k7minus_five_centre_common_matching_reduction.md)
  retains all five exceptional-centre labels and every nonempty signature,
  but its low-connectivity and dense rows remain conditional refinements.
- The older four-centre and five-centre separators, their proved inputs and
  their nearest synchronisation barriers are catalogued in the
  [technical frontier](hc7_k7minus_seven_exceptional_frontier.md#4-current-global-finishing-obstruction).

## Conditional and frozen routes

- [Seven-connected `4n-2` extremal theorem](hc7_k7minus_density_frontier.md):
  open and sufficient for Conjecture 21, but non-primary because it discards
  proper-minor colouring responses.
- [Auxiliary five-connected `4n-7` theorem](hc7_k7minus_e5_frontier.md):
  open and stronger than the sufficient extremal theorem; further
  E5-specific enumeration is frozen.
- [Bounded-interface `HC_7` composition frontier](hc7_bounded_interface_synchronization_frontier.md):
  frozen; Conjecture 21 itself would still not prove `HC_7`.

Superseded work and earlier proof spines are preserved in
[`../archive/`](../archive/).
