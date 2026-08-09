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
- [every exceptional neighbourhood contains an independent triple](../results/hc7_k7minus_exceptional_neighbourhood_completion.md#theorem-2-every-exceptional-neighbourhood-has-an-independent-triple)
- [a degree-eight centre has at most two exterior components](../results/hc7_low_degree_exterior_component_bounds.md#theorem-1-sharp-current-component-bounds)
- [every order-seven cut in the critical host has exactly two components](../results/hc7_k7minus_three_component_seven_cut_exclusion.md#corollary-2-two-component-normal-form-in-the-critical-host)

Immediate barriers:

- [fullness and local root contacts alone do not force one-shore allocation](../barriers/hc7_k7minus_shore_allocation_barrier.md#theorem-2-two-full-shore-mechanism-barrier)
- [the exact support-allocation and cut-family nonclosure](hc7_k7minus_seven_exceptional_frontier.md#4-current-global-finishing-obstruction)

## Active finishing route

[Critical-host exceptional-centre frontier](hc7_k7minus_seven_exceptional_frontier.md)

A hypothetical counterexample has no degree-seven vertices, no literal
`K_5`, and at least 25 degree-eight vertices.  Thus proving that such a host
has at most 24 degree-eight vertices settles Conjecture 21.  The current
global attack selects four independent centres, retains their proper-minor
colouring data through an exact two-shore order-seven separation, and seeks
to turn unavoidable branch-set use of the opposite shore into a second cut.
The final theorem must eliminate the resulting cut family globally; another
isolated boundary census is not an accepted endpoint.

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
