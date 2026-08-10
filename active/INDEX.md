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
- [boundary replacement and anchored uncrossing give trace-preserving strict descent](../results/hc7_k7minus_four_centre_trace_descent.md)
- [the generalized-wheel outcome reduces to one canonical leaf with no two disjoint connected subgraphs adjacent to the whole boundary](../results/hc7_k7minus_four_centre_wheel_leaf_descent.md)
- [exact boundary colourings reduce the minimum side to one support and at most eight centre-bearing components](../results/hc7_k7minus_four_centre_exact_u_bridge_reduction.md)
- [a paired exact trace forces a clean `2+1` fan](../results/hc7_k7minus_four_centre_paired_trace_fan.md)
- [a common colouring bounds the minimal opposite-side cut family by four and forces at least sixteen cuts in the equality case](../results/hc7_k7minus_common_colouring_centre_change.md)
- [replacement edges are common linkage coordinates whose one-edge and two-edge deletions expose exact order-six and order-five separations](../results/hc7_k7minus_boolean_replacement_edge_coupling.md)
- [a rooted-triangle construction eliminates the `C_4` four-region interaction and confines every surviving `P_4` replacement square to an internal region](../results/hc7_k7minus_cyclic_four_region_elimination.md)
- [every opposite-region coordinate has a centre-fixed linkage to the minimum cut, while one normalized edge-deletion colouring yields an exact endpoint language and two-sided Kempe lock](../results/hc7_k7minus_boolean_minimum_separator_linkage.md)
- [completing the boundary of a minimum exact-cut side gives a four-connected graph and an exact six-terminal rooted-minor criterion](../results/hc7_k7minus_four_centre_completed_side.md)
- [a partition-specific family of connected subgraphs reflects the fixed boundary colouring through an exact seven-cut](../results/hc7_exact7_selected_response_preservation.md)

Immediate barriers:

- [fullness and local root contacts alone do not force one-shore allocation](../barriers/hc7_k7minus_shore_allocation_barrier.md#theorem-2-two-full-shore-mechanism-barrier)
- [tri-inseparability and local degree conditions alone do not force two connected subgraphs adjacent to the whole boundary](../barriers/hc7_k7minus_tri_inseparable_full_subgraph_barrier.md)
- [internal six-connectivity, a boundary edge and a rooted `K_4` do not force the prescribed `K_6^-` minor](../barriers/hc7_k7minus_internal_six_rooted_k6minus_barrier.md)
- [an exact lower cut, adjacent lifted cuts, endpoint locks and a literal linkage coordinate do not alone synchronize a lifted boundary partition](../barriers/hc7_k7minus_local_coordinate_synchronization_barrier.md)

## Active finishing route

[Critical-host exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)

A hypothetical counterexample has no degree-seven vertices, no literal
`K_5`, and at least 25 degree-eight vertices.  Four independent centres give
either a colour-anchored rooted `K_5` or a nontriangular exact order-seven
cut with a retained colouring trace.  On a minimum selected side `C`, exact
boundary colourings leave one connected support and at most eight components
that meet a centre.  In the paired case, the three Kempe connections sharpen
to one `p`--`p'` path and two `p`--`q` paths with disjoint interiors.

Changing the deleted centre now gives at most four inclusion-minimal regions
inside the opposite component `D`.  Their interaction graph has maximum
degree at most three and independence number at most two.  Four regions
initially force one of `2K_2,P_4,C_4` and at least sixteen distinct exact
order-seven cuts through simultaneous centre replacement.  A terminal
rooted-triangle construction now eliminates `C_4`.  In a surviving `P_4`,
every Boolean square is based at an internal region, and those two regions
carry at least five unique-centre incidences between them.  For each exact
component the replacement cuts form a Boolean sublattice, and one
closed-side six-colouring induces a coherent boundary partition at each
cut.

The replacement edges are fixed, disjoint coordinates of one common
seven-path linkage.  Deleting one gives an exact order-six separation;
deleting two gives an exact order-five separation with a spanning `K_6`
model.  Every opposite-region coordinate now has a centre-fixed linkage to
the old minimum separator: its literal replacement edge ends at its named
centre, and the remaining suffix lies in `C` and can be stopped on the clean
fan.  A normalized colouring of the one-edge deletion aligns the two shores
on the six-vertex boundary and forces one bichromatic lock on each shore,
with the first beginning at the literal replacement edge.  Rejection at the
replacement-vertex cut already implies rejection at the centre cut, so the
two rejections are one endpoint-language condition, not independent data.

The unresolved task is fixed-trace synchronization in the remaining
`2K_2` case and the internal-region squares of `P_4`.  A direct audit shows
why one coordinate is insufficient: after fixing the old `C`-shore trace,
rejection becomes a list obstruction in `D`, and a minimal obstruction can
avoid the replacement vertex entirely.  The coordinate then disappears and
the resulting separators stay nested on the wrong side of `C`.  The next
accepted theorem must localize the two marked list changes of a whole square
and return a fixed-trace colouring, an explicit `K_7^-` model, or an exact
separator entering and strictly splitting `C`.  Another unlabelled cut or
attachment census is not an accepted endpoint.

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
