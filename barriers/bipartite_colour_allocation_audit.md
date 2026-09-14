# Independent audit of the bipartite allocation counterexamples

**Verdict: GREEN for both stated counterexamples.** These are barriers to
the specified selection rules, not counterexamples to chromatic
augmentation, Conjecture 19 or HC7. This is separate internal review,
not external peer review or a significance assessment.

**Source reviewed:** [bipartite_colour_allocation.md](bipartite_colour_allocation.md),
SHA-256 `4121d35e1e91a505d5840486fac8beb0d7d075b4db65ddf95de095dbe3300ee9`.
The reviewer did not construct either example. The arguments, numerical
claims and exact scope below were reconstructed independently.

## 1. Connected partitions of the three-vertex set

The reused eleven-vertex graph is specified in
[the augmentation operation counterexamples](hc7_chromatic_augmentation_operations.md),
SHA-256 `8b0fdc2a94bc4fb55464990dca7657b768131429f5211f0fd31102b365d9eea5`.
Its adjacent audit covers that exact source hash. Its written arguments
establish six-connectivity, degree six, chromatic number six,
independence number two and an explicit Q7 model.

The edge differences make the induced graph on `{0,2,4}` exactly a
three-vertex path. The four displayed independent pairs partition its
eight-vertex complement. The complement is exactly four-chromatic:
three colours there and two on the path would five-colour X.

Every proper subset of S has a complement with at least nine vertices.
Independence number two therefore makes that complement at least
five-chromatic. This checks inclusion-minimality for every proper subset,
not merely one endpoint deletion.

A connected partition of a three-vertex path must cut one of its two
edges. Direct calculation gives precisely the two mixed-neighbour sets
in the table. The same proper four-colouring misses `{3,7}` in the first
case and `{1,5}` in the second. Thus neither connected partition has the
asserted universal colourfulness; the counterexample does not depend on
choosing incompatible witness colourings for different partitions.

The independent shores `{0,4}` and `{2}` give `{5,7,8,10}`. Its universal
colourfulness can be checked without relying on the evolving draft:
if a four-colour class avoided that mixed set, each of its vertices
would meet at most one shore. Place it in the opposite shore. That
class is independent, so this extends the bipartition of S. The resulting
two colours and the other three complement classes would five-colour X.

**First unsupported inference refuted:** replacing the two independent
shores by a connected partition of the same S while retaining a
colourful common-neighbour set. The example does not rule out choosing
another S, changing all branch sets, or finding an unrestricted minor.
It already contains Q7.

## 2. The connected bipartite dominating-set claim

There are 35 backbone vertices and 30 private clique vertices. A clique
vertex has five clique neighbours and seven backbone neighbours; a
backbone vertex has fourteen cyclic neighbours and six clique neighbours.
The degrees are therefore twelve and twenty.

After at most six vertex deletions, each seven-vertex backbone set
survives. The surviving cyclic complete joins are connected, and every
surviving private-clique vertex still has a neighbour in its own
backbone set. Conversely, deleting one whole backbone set separates its
private K6 from the remaining graph. This proves connectivity exactly
seven, including the upper bound.

A private K6 together with one vertex of its backbone set is K7. To
check the matching upper bound, colour the five backbone sets with
colours `0,1,0,1,2` cyclically. In each private clique use each of the
six other colours from `{0,...,6}` once. All edges are properly coloured,
so the chromatic number is exactly seven.

If a connected dominating set B missed a backbone set A_i, domination
would force B to meet its private clique X_i. Since all edges leaving
X_i end in A_i, connectedness would then confine B to X_i. Such a set
cannot dominate any other private clique. Therefore B meets all five
backbone sets. One selected vertex from each induces C5, contradicting
the bipartiteness of the induced graph on B.

**First unsupported inference refuted:** selecting a connected induced
bipartite dominating set from connectivity, minimum degree and chromatic
number alone. The example contains a proper K7 subgraph, so it fails
both the actual critical host's proper-minor colourability and its Q7
exclusion. It does not refute a construction retaining those hypotheses
or allowing a terminal-model alternative.

## 3. Verification and limits

An independent auxiliary reconstruction through
`UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3` enumerated the two
connected partitions of the first S, checked their footprints and
missed classes, and checked the independent-shore footprint. A separately
constructed 65-vertex graph reproduced both degrees, vertex connectivity
seven, the explicit seven-colouring and the literal K7. These checks
agree with the written arguments above; neither counterexample depends
on a finite search for absent minor models or dominating sets.

No mathematical gap was found in the pinned source. Its two negative
conclusions have different hypothesis classes and must not be combined
into a nonexistence assertion for the actual critical host. The global
augmentation and critical-host constructions remain unresolved.
