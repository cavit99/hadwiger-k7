# A pair path can consume the whole open side

**Status:** written counterexample proof with a
[separate internal audit](relative_six_boundary_pair_and_arm_audit.md).
It does not refute the relative five-root
three--two linkage target or any Hadwiger conjecture.

The false statement asks for a `v1--v2` path and a disjoint `u--P` path
inside an open side X and its six roots `{u,v1,v2} union P`, where
`|P|=3`. The paths may use no other roots internally. Its hypotheses are:
X is connected, every nonempty subset of X has at least six external
neighbours, every X vertex has degree at least six, u has at least two
X-neighbours, and v1,v2 have disjoint X-neighbourhoods.

## Construction and verification

For any `m>=2`, let X be the path `x1--...--xm`. Join every X vertex
to u and to all three vertices of P. Add `v1--x1` and `v2--xm`, and
no other edges. Every X vertex has degree exactly six; u has m
X-neighbours, and the two v-neighbourhoods are disjoint.

Every nonempty `Y subseteq X` has the four neighbours `{u} union P`.
If Y=X, it also has v1,v2. Otherwise, take a path component of Y.
Each of its two ends has a neighbour outside Y: the preceding or following
X vertex, or the appropriate v root at an end of X. These two neighbours
are distinct, so `|N(Y)|>=6`.

A `v1--v2` path avoiding `{u} union P` must contain all of X. Since
u has no neighbour in P, every `u--P` path uses X. The two required
paths therefore cannot be disjoint.

## Unaffected scope

The first failed inference is allocating both v roots within this one
side while reserving a separate u arm. The side can supply disjoint
arms from u and either one v root to different P vertices. Coordinating
such arms through other sides remains possible and is used in the
[three-component construction](../active/relative_five_three_two_five_cut_reduction.md).
The example does not satisfy a requirement that each v root have two
neighbours *in this side*; global root degrees do not imply that requirement.
