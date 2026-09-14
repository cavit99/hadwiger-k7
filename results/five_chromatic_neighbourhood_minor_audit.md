# Independent audit: five-chromatic neighbourhoods and joins

**Verdict: GREEN.**

No unresolved gap was found in either theorem or the
stated necessary restriction on augmentation counterexamples. This is a
separate internal audit, not external peer review or a novelty assessment.
It does not establish the general augmentation target, C19, C21, HC7 or
NT-comparable significance.

**Source:** [the two theorems](five_chromatic_neighbourhood_minor.md).

**Exact source SHA-256:**
`80c19491f50feb698f10857c19e1269107acfb0566de742d96ba8019e9f2e92a`.

**Reviewer and scope.** On 14 September 2026, the reviewer
`plan_certificate_compute`, who did not originate either proof,
independently reconstructed both arguments and checked the complete pinned
source. The review accepts the following established inputs at their stated
hypotheses; it does not constitute a new audit of their internal proofs.
No finite experiment is a premise of either theorem or this verdict.

## Inputs and exact hypotheses

- [Five-root wheel theorem](hc7_rooted_wheel_extension.md), SHA-256
  `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3`;
  [its audit](hc7_rooted_wheel_extension_audit.md), SHA-256
  `c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178`.
  Its ambient graph is three-connected and its terminal set has five
  distinct vertices. A K4 rooted at four of those terminals extends to a
  W4 rooted at all five. The fifth terminal may already occupy an initial
  K4 bag, and the hub is not prescribed.
- Martinsson--Steiner, [Theorem 1.3 and the preceding set-rooted
  definition](https://arxiv.org/html/2209.00594v1#S1), freshly inspected in
  the primary text. The graph must be exactly four-chromatic, and the
  marked set must meet every class in every proper four-colouring. The
  conclusion has four disjoint connected clique bags, each meeting the
  marked set. It selects representatives; it does not require specified
  representatives or connectivity of the four-chromatic graph.
- Brooks' theorem at maximum degree four: a graph with no K5 component
  is four-colourable. The original statement on p. 194 was inspected in
  the [lower-order theorem's audit](four_connected_five_chromatic_minor_audit.md),
  SHA-256
  `901d9d32e466fd18bd29db254a04374667cd3066af844e42023c4773589f88af`.
  This review reuses that recorded primary-source verification and checks
  the specialization needed here. The corresponding
  [lower-order source](four_connected_five_chromatic_minor.md), SHA-256
  `92627c08e88c8e067c34d6865afa939f349545f694f8691c1b4d2e682bc9cfd7`,
  supplies provenance and comparison, rather than an additional theorem
  invoked between these inputs and the present conclusion.

All local input hashes were checked against the files.

## The neighbourhood theorem

**Critical selection and Brooks.** An induced vertex-minimal graph J that
is not four-colourable is connected: otherwise a non-four-colourable
component is a smaller induced choice. Deleting any vertex leaves a
four-colourable graph, so restoring that vertex with a fresh colour gives
`chi(J)=5`. Every J-a is exactly four-chromatic, since a three-colouring
would extend to a four-colouring of J. If J is not K5 and had maximum
degree at most four, the stated Brooks specialization would contradict
`chi(J)=5`. Thus the selected vertex a has at least five J-neighbours.
No minimum degree or connectivity of J-a is inferred.

**Root selection and ownership.** Every four-colouring of J-a uses all
four colours on N_J(a), or it extends to J. The primary rooted theorem
therefore applies. Disjointness of its four bags permits choosing four
distinct actual neighbours of a. The degree bound supplies a fifth
distinct neighbour. The wheel input expressly covers the possibility
that this fifth vertex already lies in one of those four bags.

**Ambient connectivity and contacts.** The graph H-{z,a} has at least
five vertices. Removing at most two more vertices removes at most four
vertices from H and therefore leaves a connected graph. Consequently the
ambient graph for the wheel theorem is three-connected. The initial K4
model and all five selected terminals lie there. Every returned wheel bag
contains a vertex of J adjacent to both a and z. The bags avoid both
singletons; moreover az is an actual edge because a belongs to N_H(z).
Their contact graph consequently contains K2 joined to W4, namely Q7.
Expansion outside J cannot erase the two required terminal contacts.

**Literal K6 exit.** If J=K5, then J together with z is a literal K6.
The order assumption supplies a component D outside it. All neighbours
of D outside D lie in that clique. A boundary of size at most four leaves
a surviving clique vertex separated from D, contradicting
five-connectivity. Hence D contacts at least five singleton clique bags.
Their seven-bag contact graph omits at most one edge and contains Q7;
extra contacts are allowed. No minor model is being mistaken for a
literal clique in this case.

## The join theorem

A disconnected complement gives two nonempty join factors. Their palettes
must be disjoint, so their chromatic numbers add. Relabel the factors to
have `1<=a<=b`; the hypothesis gives a+b>=6.

For a=1, a vertex of that factor sees a graph of chromatic number at least
five. For a=2, the factor contains an edge, and an endpoint sees the other
endpoint joined to a graph of chromatic number at least four. Both cases
meet Theorem 1. If a>=3 and either factor contains a triangle, a triangle
vertex sees an edge joined to the other factor, again giving at least
five colours in its neighbourhood.

In the remaining case both factors are triangle-free and nonbipartite.
Each therefore contains an odd cycle of length at least five. Three
nonempty consecutive arcs partition one cycle into connected K3 bags;
four such arcs partition the other into connected C4 bags. The two sets
of bags lie in disjoint factors, and every cross pair has an original
join edge. This gives K3 joined to C4, namely Q7. Chords or unused vertices
do not affect the model. These cases exhaust all positive a,b and do not
require either factor separately to be connected.

## Limits

Both arguments are nonrecursive and require no decreasing-parameter or
induction-class claim. Neither uses a minimum-degree assumption. Taking
their contrapositives under the augmentation hypotheses correctly forces
a Q7-free counterexample to have connected complement and four-colourable
neighbourhoods. These restrictions leave the general compatibility problem
open. No additional unresolved assumption was found beyond the named,
previously established inputs.
