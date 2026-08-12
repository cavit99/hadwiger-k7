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
- [fixed-coordinate list-core reduction preserves one forest edge and its
  colouring under strict side-order descent](../results/hc7_k7minus_fixed_coordinate_response_core_reduction.md)

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
`F_8` response.  Generic density descent bounds the latter interface by
nine, but can replace the forest edge by an unrelated singleton operation.
The immediate target is therefore a **one-coordinate anchored compression
theorem**: preserve one `F_8` edge and its exterior colouring while reducing
the boundary to order seven or eight, or produce `K_7^-` or one boundary
partition extending through both shores.  Coordinate-preserving
list-critical minimisation now provably lowers side order until a connected
boundary-list-critical or singleton side remains, but may increase the
boundary.  Generic density descent lowers the boundary but may lose the
coordinate.  A target-free proof must therefore use `K_7^-`-minor exclusion
at that terminal side.

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
