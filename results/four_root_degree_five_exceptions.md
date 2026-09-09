# Four rooted bags with five degree-five exceptions

**Status:** written proof; a [separate exact-source audit](four_root_degree_five_exceptions_audit.md) is recorded beside it.
This strengthens a local rooted-model input. No closure of the
two-triangle case, C19 or HC7 is asserted.

All graphs are finite and simple. Neighbourhoods of sets are external.
A rooted model has pairwise disjoint connected bags containing the four
prescribed roots separately; additional contacts are allowed.

**Theorem.** Let Z be four vertices of a graph F and put D=V(F)-Z.
Suppose |D|>=3, every nonempty X contained in D has at least four
neighbours, every vertex of D has degree at least five, and at most
five vertices of D have degree five. Then F has a Z-rooted K4 model.

The order restriction is necessary: with two nonroots of degree at least
five, the only obstruction is K2 join I4 with its four independent
vertices prescribed as roots.

## Input and the small endpoint

We use the exact Norin--Totschnig Theorem 8 alternative recorded in
[the five-root almost-clique source](../results/hc7_five_root_almost_clique.md),
SHA-256 `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`;
its [audit](../results/hc7_five_root_almost_clique_audit.md) has SHA-256
`dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.
For four roots the alternatives are a rooted K4; an order-two trisection
with two specified open parts each containing exactly one root; a
separation of order at most three with all roots on one closed side and
at least two nonroots on the other open side; or a plane drawing with
all four roots on one face. In the trisection all pairwise intersections
are the same two-set, with no edges between distinct open parts.

The reductions are those of the
[existing four-root packet](../results/hc7_two_triangle_exterior_helpers.md#1-a-four-root-packet)
and its [one-exception extension](../results/hc7_reserved_core_component_bound.md#a-component-cannot-miss-the-omitted-b-root).
The endpoint checks below permit five exceptions. No fresh primary-source
inspection is claimed; the invoked alternative is the pinned input above.

**Two-nonroot classification.** If D={p,q} and both degrees are at least
five, p and q are universal in this six-vertex graph. If roots a,b are
adjacent and c,d are the other roots, the bags {a},{b},{c,p},{d,q}
give a rooted K4. If the roots are independent, every four-root model
has at least two singleton root bags, since only two nonroots are
available. Those singleton bags are nonadjacent. Thus precisely
K2 join I4 fails. A one-nonroot graph cannot satisfy degree at least five.

## Reductions and their lifts

**Proof of the theorem.** Choose a counterexample minimizing |D| within
the stated class. Applying the boundary hypothesis to D shows that
every root has a neighbour in D.

If a root a has only one D-neighbour p, contract ap and retain the
label a. No surviving nonroot was adjacent to old a. Thus every surviving
nonroot degree and every nonroot-set boundary cardinality is unchanged:
the vertex p, when present in such a boundary, is replaced by the new
root. The number of degree-five nonroots cannot increase. All four
root preimages remain disjoint and connected, and models lift.
If at least three nonroots remain, this contradicts minimality. The
only smaller endpoint has two nonroots. Its merged root has degree at
least d_F(p)-1>=4, whereas all roots in the exceptional K2 join I4
have degree two. The classification therefore gives a rooted K4 there
as well. Consequently every root has at least two D-neighbours.

Apply the pinned four-root alternative. Its small separation contradicts
the four-neighbour bound on its nonempty root-free open side.

In a trisection, each of the two specified open parts is its sole root,
say a,b: its nonroot subset would otherwise have at most three neighbours.
Let P be the common two-set. All nonroots lie in the third closed part.
If P contained a root, D-P would be nonempty since |D|>=3, and its
boundary would lie in P and the other two roots apart from a,b, giving
at most three neighbours. Hence P={p,q} consists of nonroots.
Normalization makes a and b adjacent to both p and q, and to no
surviving nonroot. Contract the disjoint edges ap,bq, retaining their
respective root labels. Every surviving nonroot degree and boundary
cardinality remains unchanged, and the root preimages are separate.
The cross edges aq and bp create an edge between the two new roots.
With at least three remaining nonroots, minimality applies. One remaining
nonroot is impossible by degree five; with two, the new root edge
excludes the exceptional graph. All possibilities contradict the absence
of a rooted K4. Thus the trisection is also excluded.

## The planar alternative

Only the cofacial planar outcome remains. The graph is two-connected.
Indeed, after deleting at most one vertex, every component contains a
nonroot, because each retained root had two nonroot neighbours. If X
is the nonroot set of a component after one deletion, its boundary in F
lies among that component's roots and the deleted vertex. The boundary
bound forces at least three roots in every component, so there cannot
be two components. Without a deletion the same argument forces all
four roots into every component and proves connectivity.

The distinguished facial boundary is therefore a cycle containing the
four roots and h nonroots. Writing d=|D|, Euler's inequality gives

`2e(F) <= 6d+10-2h`.

The nonroot degree sum is at least 6d-5. The four roots have at least
eight incidences with nonroots. Their eight facial-cycle incidences
include at most 2h incidences with nonroots, so their degree sum is at
least `8+max(0,8-2h)`. Consequently

`2e(F) >= 6d-5+8+max(0,8-2h)`.

For h<=4 this exceeds the upper bound by one; for h>=4 it exceeds
that bound by at least one. This contradiction excludes the last
alternative and proves the theorem. Every reduction strictly decreased
nonroot order and had fixed disjoint connected root preimages. QED

The theorem supplies one rooted K4 under its stated degree and boundary
hypotheses. It does not reserve another connected set, preserve degrees
at a retained cut after a side replacement, or establish an iterable
critical-host reduction.
