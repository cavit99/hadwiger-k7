# Audit of the intrinsic-radius theorem

**Status:** separate internal proof audit, 8 September 2026; not external
peer review.

**Verdict: GREEN.**

**Exact source:** [bipartite_short_scheme_radius.md](bipartite_short_scheme_radius.md),
whole-file SHA256
`4fd71c1bd710e84f168426d4934e7eb4b1e830ddd9d61ce003d5a8161684202d`.
The independent reviewer checked the complete draft at
`21dfbf0b82883205ff6787928c9e9459900c358391b53087b9231ed2d2004bb5`.
Promotion changes only its status sentence and three relative links;
reversing those changes recovers that exact draft hash. The parent also
read the whole proof and checked the arguments below. All three input
proof/audit pins match their unchanged files.

The statement quantifies over every finite simple bipartite target and
every scheme with path length at most three. The promised distances are
inside each final bag and measured from its original prescribed root.
There is no target-degree or host-order bound.

In raw colour normalization, every monochromatic edge has a monochromatic
route of length at most two to its colour's root. Thus each nontrivial
component contains that root and has the asserted intrinsic radius.
A remaining nonliteral path must be its unchanged original three-edge
path, with singleton interiors; a shorter properly bichromatic path
between opposite-shore roots is an edge.

Every projection is consequently a root-centred star. A component forest
allocates one original root neighbour to each absorbed base vertex, with
an actual two-edge route inside the same preimage. No nonroot preimage
grows. For every affected demand, the retained last edge gives the new
root contact even if its discarded label has another owner. Unaffected
paths keep their original singleton interiors. These assertions hold on
either shore, so reversal does not accumulate a distance factor.

The universal rank split supplies either the full star packing or a
nonempty tight set and strict host-order descent. Connectivity, root
labels, proper endpoint colouring and disjoint preimages survive. Lifting
uses the invariant's original paths inside those fixed preimages; it
does not multiply radii of successive quotient models.

The `K_{1,2}` example excludes every radius-one rooted model: one leaf
bag is singleton and forces its sole neighbour into the central bag,
where it is not adjacent to the central root. The stated radius-two
model has both required contacts.

For the length-five example, all paths have the required colours and
membership and exclude foreign roots. The displayed disjoint forests
attain the proposed union expression, proving that `X` really minimizes
it. Its first projection has a root-free doubled path; every spanning
forest lifts to an induced path of intrinsic diameter `2n`. This refutes
the root-only invariant for that valid reduction, not the existence of
some bounded-radius model obtained differently.

**Unresolved:** intrinsic-radius bounds for longer schemes, publication
priority, comparative significance and the main HC7-related objective.
No finite computation is used in either the theorem or method obstruction.
