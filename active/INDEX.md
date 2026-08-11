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
- [the independence-four branch is impossible, so five degree-eight centres can be chosen independently](../results/hc7_k7minus_alpha4_regular_ramsey_elimination.md)
- [an arbitrary two-cut after deleting five independent centres has opposite singleton shore responses and a sharp rooted-linkage bound](../results/hc7_k7minus_five_centre_two_cut_reduction.md)
- [the order-six equality-response component is terminal by a ten-orbit DRAT-certified incidence theorem](../results/hc7_k7minus_order_six_equality_shore_elimination.md)
- [the order-seven equality-response component is terminal by a cold-rerun 149-orbit allocation theorem](../results/hc7_k7minus_order_seven_equality_shore_elimination.md)
- [every four boundary vertices root a `K_4` on the distinct-response shore](../results/hc7_k7minus_five_centre_universal_boundary_rooted_k4.md)
- [five distinct centre edges can be deleted to put all 31 nonempty equality signatures on one six-chromatic host, whose cuts have an exact connectivity trichotomy](../results/hc7_k7minus_five_centre_common_matching_reduction.md)
- [in the two-cut row the distinct-response shore always has universal four-boundary rooted `K_4` models, and one equality-shore singleton gives the same property on both shores](../results/hc7_k7minus_five_centre_two_shore_rooted_k4.md)
- [four crossing response edges form a tight signed Boolean cube with exact connectivity, all punctured signatures and one common seven-path coordinate linkage](../results/hc7_k7minus_four_crossing_signed_boolean_reduction.md)
- [in the five-crossing row each omitted coordinate gives an exact centre-edge response or a seven-connected complete linkage packet with a rooted neighbourhood-join minor](../results/hc7_k7minus_five_crossing_omitted_coordinate_linkage.md)
- [two response-support portals in one universal near-clique bag force the target or a trace-bearing separator; every invisible dense residue has at least three unsupported portals](../results/hc7_k7minus_dense_branch_rotation_visibility.md)
- [the five centre-deletion colourings give singleton saturation witnesses on one common core; every fixed-root packet in the three-connected branch has a rooted model or a common literal extension colour, while the rigid alternative returns a labelled two-cut](../results/hc7_k7minus_five_centre_rotation_reduction.md)
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

- [five singleton-saturation palettes alone do not force a common missing colour or the common-partition fallback](../barriers/hc7_k7minus_five_rotation_palette_intersection_barrier.md)
- [fullness and local root contacts alone do not force one-shore allocation](../barriers/hc7_k7minus_shore_allocation_barrier.md#theorem-2-two-full-shore-mechanism-barrier)
- [tri-inseparability and local degree conditions alone do not force two connected subgraphs adjacent to the whole boundary](../barriers/hc7_k7minus_tri_inseparable_full_subgraph_barrier.md)
- [internal six-connectivity, a boundary edge and a rooted `K_4` do not force the prescribed `K_6^-` minor](../barriers/hc7_k7minus_internal_six_rooted_k6minus_barrier.md)
- [an exact lower cut, adjacent lifted cuts, endpoint locks and a literal linkage coordinate do not alone synchronize a lifted boundary partition](../barriers/hc7_k7minus_local_coordinate_synchronization_barrier.md)

## Active finishing route

[Critical-host exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)

A hypothetical counterexample has no degree-seven vertices, no literal
`K_5`, and at least 25 degree-eight vertices.  The complete
independence-four branch is now eliminated, so five of those vertices can
be chosen independently.  Any four of the five give either a
colour-anchored rooted `K_5` or a nontriangular exact order-seven cut with a
retained colouring trace.  On a minimum selected side `C`, exact boundary
colourings leave one connected support and at most eight components that
meet a centre.  In the paired case, the three Kempe connections sharpen to
one `p`--`p'` path and two `p`--`q` paths with disjoint interiors.

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

Fixed-trace synchronization remains unresolved in the `2K_2` case and the
internal-region squares of `P_4`; a minimal list obstruction can avoid a
marked replacement vertex and stay nested on the wrong side of `C`.

The five-centre attack now gives an independent global reduction.  Put
`F=G-Z`.  If `F` has a two-cut `{p,q}`, its exact seven-vertex boundary has
two full components with opposite singleton colouring responses.  The
equality-response component is rooted-`(2,5)`-infeasible, has full-packing
number one, contains four colour-distinguished critical-edge paths, satisfies
`e(C)+e(C,S)<=6|C|+1`, and has order at least eight.  The order-five row is
terminal by an explicit `K_7^-` model, and the order-six row is terminal by
an independently checked ten-orbit DRAT certificate.  The order-seven row
is terminal by an exact 149-orbit allocation search with a separate cold
full rerun.

For the unbounded row, every four boundary vertices root a `K_4` on the
distinct-response shore.  In the completion obtained by contracting
`D union Z` and adding `pq`, all distinct-pole models lift and the sole
survivor has five bijectively owned bags and one owner--owner nonedge.  The
audited
[unique-owner reduction](hc7_k7minus_five_centre_owner_nonedge_connector.md)
now eliminates every quotient pattern: it gives an explicit `K_7^-` minor
or a genuine nested separator.  In a target-free host that separator may
have order greater than seven, may miss four centres, and carries no known
boundary partition.  The
[boundary-first donor gate](hc7_k7minus_five_centre_minimal_donor_gate.md)
is now a recorded decisive route nonclosure: a proper fixed-trace core
either fills the selected donor or exposes a smaller geometric donor which
inflates the boundary when the comparison class is closed and may lose the
trace.  Enlarging the donor class instead is not proved to retain the model
and response labels at a degree-eight singleton.  The one-donor minimisation
is therefore frozen.  The
[single-edge paired-donor gate](hc7_k7minus_five_centre_paired_donor_gate.md)
aligns two traces only across the deleted edge and conditionally returns a
`K_7^-` model or a joint response-bearing separator.  The unique-owner
reduction does not supply the required compatible pair, joint minimisation
permits private same-bag inflation, and an explicit target-free local
barrier rules out boundary overlap as the missing mechanism.  This variant
is also frozen.  The audited
[two-edge response reduction](hc7_k7minus_five_centre_two_edge_response_reduction.md)
shows that a common double deletion can retain the literal five-centre
boundary and reverse the pole response after both singleton contractions
remain stable.  Otherwise a singleton already flips, or the three stable
completions contain `K_7^-` models with the prescribed co-bagging.  No
current theorem supplies the required induced cross-edge pair or lifts all
stable same-pole-bag models.  Three simultaneous disjoint donor traces are
impossible for one fixed deletion colouring, so this bounded operation is
not being enlarged.  The exact-seven backup still needs the new boundary to
contain all five centres with the equality orientation.  The singleton
six-arm, order-four, all-rainbow, and `b=2` rows remain open.

The new immediate laboratory is the audited
[common five-edge response host](../results/hc7_k7minus_five_centre_common_matching_reduction.md).
For each centre, a star-contraction colouring supplies five
singleton-colour neighbours.  Hall's theorem selects distinct neighbours,
giving a matching `M` of five centre edges.  On `H=G-M`, every nonempty
subset of `M` is the exact monochromatic-edge set of a six-colouring; the
empty signature would colour `G`.  Each singleton coordinate also yields an
actual separator carrying that literal rejected boundary precolouring.

The connectivity of `H` is exhaustive.  A two-cut is crossed by all five
matching edges and gives 32 exact order-seven cuts; it is also a two-cut of
`F=G-Z`, with all five centres having simultaneous singleton shore
contacts.  A three-cut is crossed by four or five matching edges.  The
four-crossing row gives 16 exact order-seven cuts; in the five-crossing row,
each of 30 mixed order-eight cuts gives exact-seven descent or two full
sides.  If `H` is four-connected, Norin--Totschnig supplies a spanning
`K_7^vee`; the exact near-clique theorem returns the target or a nested
model-bag separator.  A returned set meeting `r` matching edges carries all
`2^r-1` nonempty rejected traces supported there, although their boundary
partitions may repeat.

The four-crossing three-cut row is now geometrically exact.  Deleting any
nonempty set `R` of its four crossing edges gives connectivity and a
two-full-shore separator of order `7-|R|`, realizes every nonempty signature
on `R`, and retains the four edges as distinct coordinates of one common
seven-path linkage.  The dense deletion rows return a `K_7^vee` model and
hence the target or a nested response-bearing separator.  This does not yet
force that nested piece to meet a coordinate end or synchronize its boundary
partitions.

The other rows have sharper endpoints as well.  In the two-cut row, the
distinct shore always has a rooted `K_4` on every four boundary vertices;
if one selected singleton lies on the equality shore, both shores have that
universal property, leaving an exact `3`-by-`3` cross-bag allocation.  In
the five-crossing row, omitting any coordinate gives an exact centre-edge
response or a seven-connected complete linkage packet; if all five packets
occur, their simultaneous composition is the unsupported step.  In the
dense row, two response-support portals in one universal bag force the
target or a trace-bearing separator.  The invisible residue has at most one
such portal per universal bag and at least three portals outside the full
five-centre response support.

The immediate target is to terminalize this trichotomy: eliminate the five
simultaneous-singleton two-cut row through its cross-bag allocation, or
handle the all-five-on-one-shore orientation; compose the five complete
omitted-coordinate packets or terminalize the signed four-crossing
separator; or eliminate the response-support-sparse near-clique model.  The
audited
[rotation theorem](../results/hc7_k7minus_five_centre_rotation_reduction.md)
remains available for labelled three-cut geometry.  Direct palette
intersection is frozen by the scoped barrier above.

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
