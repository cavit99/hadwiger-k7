# Challenges to augmentation operations

**Frozen on 14 September 2026.** Retained discovery record; current status is in the research ledger and technical frontier.

**Original status:** unaudited working deductions. These are challenges to specific
operations, not counterexamples to the augmentation target, C19 or HC7.
They are not promoted proof inputs. The research ledger remains the sole
current status authority.

## Connected induced bipartite domination needs more than the numerical host conditions

**Claim refuted.** Every seven-connected seven-chromatic graph of minimum
degree at least eight has a connected induced bipartite dominating set.
The construction below is not proper-minor critical and contains Q7.
Thus proper-minor criticality remains available to repair the selection
claim in the actual hypothetical critical host.

Let X be the eleven-vertex graph on Z_11 with edge differences
`±2, ±3, ±5`, as defined in the
[audited augmentation-operation examples](../barriers/hc7_chromatic_augmentation_operations.md).
It is six-chromatic, six-regular and contains Q7.

Take five disjoint independent sets A_i of order seven, indexed modulo
five. Completely join A_i to A_(i+1), with no other edges between these
sets. Take five disjoint copies X_i of X and completely join X_i to A_i.
There are no other edges. Call the resulting ninety-vertex graph H.

**Verification of the host.** Each vertex of X_i has degree thirteen;
each vertex of A_i has degree twenty-five. Thus the minimum degree is
thirteen. Deleting at most six vertices leaves each A_i nonempty, so the
surviving A_i form a connected cyclic backbone. Every surviving vertex
of every X_i has a neighbour in that backbone. This proves connectivity
at least seven. Deleting A_i separates X_i from the rest, giving equality.

The graph induced by X_i and any one vertex of A_i needs seven colours.
For the upper bound, properly three-colour the five-cycle of sets A_i,
giving every vertex of each A_i its set's colour. Independently six-colour
X_i with the other six colours of a common seven-colour palette. Hence
the chromatic number is exactly seven.

**Failure of the selection claim.** Suppose B is a connected dominating
vertex set. If B avoids A_i, then domination of X_i requires B to meet
X_i. Since every edge leaving X_i ends in A_i, connectedness then forces
B to be contained in X_i. But such a set cannot dominate a different X_j.
Consequently B meets every A_i. One chosen member of B from each A_i
induces a five-cycle. Therefore H[B] is not bipartite.

**First unsupported inference and retained scope.** Seven-connectivity,
the degree bound and seven-chromaticity do not select a connected induced
bipartite dominating set. Every X_i is a proper smaller augmentation host
with a known Q7 model, so the example does not refute a selection-or-minor
dichotomy, nor the selection claim with the actual proper-minor-critical
hypothesis. Disconnected bipartite footprints and simultaneous contraction
responses also remain possible.

## A fixed proper colouring can prohibit all contractions in the critical core

Let H itself be six-vertex-critical, choose z, and put F=L=H-z. Fix a
proper five-colouring f of F. Suppose an allowed contracted bag must be
connected in L and have an f-monochromatic intersection with F. Then
every allowed bag is a singleton: a connected bag of order at least two
contains an edge of F, whose ends receive different colours.

This applies to X under every augmentation hypothesis. X has a direct
Q7 model, so the observation is a limitation of the proposed contraction
invariant, not a counterexample to a contraction-or-terminal theorem.
An operation confined to this invariant must handle the entire H=J
critical-host branch by an independently justified terminal or must change
its retained colouring state.
