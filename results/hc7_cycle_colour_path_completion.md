# Two ways to complete the cycle-and-triangle colour configuration

**Status:** computation-free written proofs; the adjacent audit records
two separate internal reviews at the exact source hash. These are conditional critical-colouring
constructions, not proofs of Conjecture 19, Conjecture 21 or `HC_7`.

All graphs are finite and simple. Write `Q` for `K_7` with two independent
edges deleted. Inputs are graphic-matroid union and the explicit
component reduction in
[universal bipartite contractibility](bipartite_contractibility_via_matroid_reduction.md),
SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`,
and the elementary bag constructions in
[marked scheme completion](hc7_marked_k33_scheme_completion.md),
SHA-256 `fb55cc00b52e0f3fb6f6e547f08b29ed6aae37cb25c4176a7c7fb96ada05dc2f`.
We do not contract an abstract identification of the marked vertices.

## 1. The two statements and their common decorations

Fix nine distinct vertices `v,a0,a1,a2,0,1,2,3,4` in a graph `G`.
Assume a literal triangle `a0,a1,a2`, a literal cycle `0,1,2,3,4,0`,
and all eight edges from `v` to the other named vertices. Put
`A={a0,a1,a2}`, `B={1,3,4}`. Extra host edges are allowed.
All paths below avoid `v`. A proper endpoint-colouring fixes the six
root labels, uses only endpoint colours on each scheme path, and gives
each used marker `0,2` colour `a0`.

**Theorem 1 (any two connections).** If there is a properly
endpoint-coloured scheme for

`H_j=K_{3,3}-a0-j`, for any `j in {1,3,4}`,

with the six prescribed roots `A union B`, then `G` contains `Q`.
In particular, the omitted edge may be `a0-1`.

**Theorem 2 (crossed paths).** Suppose there are six properly
endpoint-coloured paths `P_ij` from `ai` to `j`, for `i=1,2` and
`j=1,3,4`, containing no other prescribed root internally. Suppose
also there are simple paths `L3` from `a0` to `0` using colours
`a0,3`, and `L4` from `a0` to `2` using colours `a0,4`, under one
proper six-colouring of their union. Then `G` contains `Q`.
No `a0-1` path is assumed. Intersections are unrestricted beyond these
proper colour constraints.

Throughout the proofs, the literal cycle, triangle and `v` edges are
auxiliary edges, retained separately from the coloured path union.
Every minor has specified disjoint connected preimages in the original
host. Root preimages contain their prescribed roots. The vertex `v`
stays its original singleton; every other preimage avoids it.

We use the following elementary terminal construction from the marked
input. A rooted `K_{2,3}` model at `a1,a2` and `1,3,4`, avoiding both
markers, together with a disjoint connected set `D` containing `a0`
and at least one marker, gives `Q`. If `D` contains one marker, add
the other to its natural cycle-root bag; the possible missing pairs
are independent. If it contains both, take a minimal tree spanning
`a0,0,2`, transfer a pendant segment at one marked leaf into `X4`
or `X3`, and retain the root and the other marker. The retained tree
contacts all three `X` bags through the other marker and the cut edge.
It retains its two `Y` contacts through `a0`. All these operations use
disjoint actual preimages. We call this the **root-and-marker terminal**.

## 2. Auxiliary inductions with one marked vertex

These auxiliaries are established at all finite orders before either
main theorem uses them. Their statements are about actual host minors
with the preimages just specified. All auxiliary markers are distinct
from `v` and the six roots.

**Auxiliary L.** Let a properly coloured `H_j` scheme have the literal
`A` triangle, literal edges `14,34`, and one marker `m` of colour
`a0` adjacent to `1,3`. The vertex `v` is outside the scheme and
adjacent to its six roots. Then `Q` exists, for every `j`.

An unused `m` can be added to `X1`, completing the `B` triangle;
the six root bags miss only possibly `a0-j`, so `{v}` gives `K_7^-`.
A connected preimage `D` containing `a0,m`, disjoint from the other
five rooted bags, is also terminal: those five bags miss only possibly
`X1-X3`; `D` meets both ends through `m`, and both `Y` bags through
`a0`. Its only possible missing core contact is `X4`. The two
possible missing pairs are therefore independent, irrespective of `j`.

Induct on scheme-union order. Dispose first of an unused marker.
Let `N_A,N_B` count its nonroots in the two colour shores. When
`N_A<=N_B`, use the ordinary `A` projections of the universal input.
Full packing puts `a0,m` in one bag and is terminal. Otherwise the
rank minimizer is nonempty and its component reduction strictly
decreases order. A root-marker collision is terminal: delete the
`a0` colour from the quotient and extract the disjoint `K_{2,3}`
core. With no collision, retain the marker and all auxiliary edges.
When `N_A>N_B`, restrict the `B` ground to `E'=E-{m}`. Full rank
`N_B` gives a model avoiding `m`. If its rank is smaller, then
`R'<N_B<=N_A-1=|E'|`, so a nonempty minimizer reduces while
protecting `m`. After path cleanup check again for an unused marker.
Every recursive step strictly decreases order and has a literal
root-preserving lift. This proves Auxiliary L for every omitted edge.

**Auxiliary C.** Instead retain a single vertex `m` of colour `a0`
whose connected original preimage contains both original markers
`0,2`, disjoint from all six root preimages. Suppose there is an
`H_j` scheme, and retain the original cycle/triangle edges as preimage
contacts. Then the original decorated host contains `Q`, for every `j`.

If a rooted model avoids `m`, its lift avoids both original markers;
add them separately to `X4,X3` to complete the `B` triangle. There
is at most the one cross-hole `a0-j`. If a component preimage contains
`a0,m`, it contains all three original terminals and the root-and-marker
construction applies to the other five bags. Otherwise use the same
one-marker induction as for L: ordinary `A` full packing or a nonempty
reduction when `N_A<=N_B`, and a full packing on `E-{m}` or its
nonempty deficient reduction when `N_A>N_B`. The marked preimage
is never split or allocated to a `B` component in a nonterminal step.
No full reverse packing that uses `m` is assumed terminal. This proves C.

**Auxiliary H (one crossed path).** Retain the one-marker decorations
of L: the `A` triangle, `14,34`, and `m` of colour `a0` adjacent
to `1,3`, with `v` outside and adjacent to the six roots. Suppose
there are the six old `K_{2,3}` paths, an actual proper `a0-3`
path, and a path `L` from `a0` to `m` using colours `a0,4`.
Then `Q` exists.

If `L` hits the root `4`, its prefix together with the `a0-3`
path gives an `H_1` scheme, so Auxiliary L applies, whether or not
its selected paths use `m`. If `L` misses the old six-path union,
it is itself the connected helper in L's root-marker terminal. In
every other case it avoids `4` and meets that union in colour `4`.

The ordinary `A` and `B` projections are then connected. On the
`A` side the actual `a0-3` path and `L` project to paths beginning
at `a0`; on the `B` side the colour-`4` projection of `L` meets
the root-connected old projection. Its endpoint `m` is not counted
as an edge of that projection. Induct on the full path-union order.
When `N_A<=N_B`, ordinary `A` full packing or a root-marker
component is terminal by L's helper construction; otherwise use a
nonempty ordinary component reduction. When `N_A>N_B`, restrict
the `B` ground to `E-{m}`. Full rank gives entire `B` colour
fibres as bags. The first edges of the actual path and `L` give
`a0` contacts to `3,4`. The unused `m` completes the `B` triangle,
leaving only possibly `a0-1` missing. Deficient rank is strictly
below `N_B<=N_A-1`, so a nonempty reduction protects `m`.

The component reduction translates internal traversals of `L` just
as it translates scheme paths; both its endpoints survive unless a
root-marker collision is already terminal. After every simplification
dispatch a new root-`4` hit to L, or loss of all old intersections to
the helper terminal. Otherwise the smaller instance retains the
hybrid hypotheses. All labels in a reverse minimizing set are genuine
internal vertices, since `m` is excluded. Thus every recursive step
strictly contracts a connected set. This proves H independently of
both main theorems.

## 3. Two-projection packing and the rank-one terminal

In either main path system a nonroot of colour `a1,a2` belonging
to only one of its three old paths belongs to no other path in the
system. Its two neighbours have the same `B` colour `j`. Contract
the connected triple consisting of it and those neighbours to colour
`j`. This contains at most the prescribed root `j`, no marker,
no other root and no `v`. Paths map to proper two-colour walks and
then simplify. This strictly reduces path-union order. Each main
proof checks its terminal cases after cleanup and recomputes all
counts and ranks; normalization is not claimed to preserve them.

After all such reductions, every nonroot of colours `a1,a2` belongs
to at least two of its three old paths. Their two projections have
full simultaneous spanning rank. Indeed, for `X` in the `B`-label
ground, let `c_i(X)` count the components of `M_i(X)`. Its root
component meets all three projected paths; every other component meets
at least two. Counting visits gives

`2(c_i(X)-1) <= |(E-X) intersection E_i|`.

Here `E_i` contains the labels actually used by that projection;
its three path label sets are disjoint. Summing for `i=1,2` yields
`c_1(X)+c_2(X)<=|E-X|+2`, since a label occurs in at most two
of these projections. The graphic rank identities and union formula
give their full total rank. No `B`-vertex membership hypothesis is
needed; labels used only by extra paths are loops in this pair.

We isolate the remaining allocation argument. Suppose the three
ordinary `A` projections are connected, their total full rank is
`N_A`, their common ground has `N_B` labels, and the pair `M_1,M_2`
has full simultaneous spanning rank as above. The projection `M_0`
contains the distinct vertices `a0,0,2`. Identify `0,2` only in
this abstract graph to form a graphic matroid `M_0*`. Independence
means an ordinary forest separating `0,2`; its full rank is one
below that of `M_0`. Let `R,R*` be the ordinary and modified
three-matroid union ranks. Always `R*<=R<=R*+1`, since an ordinary
forest can be made independent after identification by removing at
most one edge on its marked connecting path.

**Rank-one terminal.** If

`N_A=N_B+1`, `R=N_B`, and `R*=N_B-1`,

then the actual decorated host contains `Q`.

Choose an ordinary maximizing allocation `I_0,I_1,I_2`. It allocates
every label and has exactly one total forest-rank deficit. In every
such allocation `I_0` connects the two markers: otherwise the same
allocation would be modified-independent of size `N_B`.

Move the deficit into `M_0` if necessary. When it is in `M_1` or
`M_2`, their current union has size one below their full union rank.
The augmentation axiom for that union matroid supplies one new label
`e`, retaining all old labels with a possible repartition into two
forests. Every label is allocated globally, so `e` belongs to `I_0`.
Remove it there and repartition the enlarged pair into full spanning
trees. This is another ordinary maximum allocation, whose markers
therefore remain connected. Its sole deficient projection is now `M_0`.

Lift allocated forest components to their sets of `A` vertices and
allocated actual `B` labels. They are connected and pairwise disjoint,
avoid `v`, and contain at most one prescribed root. The full sets
`Y1,Y2` each contact the three singleton `B` roots through their
old path endpoints. If the `a0` component contains both markers, it
is the root-and-marker terminal helper for this core.

Otherwise the two `M_0` components are `U` containing `a0`, and
`K` containing both markers. A crossing edge of the connected
projection `M_0` has its label allocated to `Y1` or `Y2`; allocation
to `I_0` would connect the components. Thus an actual vertex `k`
inside `K` is adjacent to one of those full bags. Retain `k`, not
the foreign-owned edge label. Merge `U` into `Y1` through `a0a1`.
Inside `K`, take a minimal tree spanning `0,2,k`. Transfer a
pendant segment at a marked leaf into `X4` through `04`, or into
`X3` through `23`, retaining `k` and the other marker. If `k` is
a marker, transfer the other one.

The retained tree contacts all three `B` bags through the other
marker's two literal neighbours and its old cut edge; it retains its
contact to a `Y` bag. The transferred marker and `34` provide two
`B`-shore contacts. Consequently the seven bags consisting of `{v}`,
the two `Y` bags, the retained tree and the three `B` bags have
all nine cross-contacts, at least two contacts in each shore, and all
six contacts to `v`. The retained tree meets `v` through its marker;
the other bags retain prescribed roots. At most one pair in each
shore is missing, and these pairs are independent. This proves the
rank-one terminal using actual disjoint connected preimages.

## 4. Proof of Theorem 1

Induct on scheme-union order. An unused `0` may be contracted into
root `4` through `04`, giving literal `14`; Auxiliary L with
marker `2` applies. An unused `2` is handled by reflection.
Normalize the `a1,a2` single-membership vertices as in Section 3.
After every simplification check again for an unused marker; compute
all ranks and counts only when both remain in the scheme union.

All three ordinary projections in either orientation are connected,
because their incident projected paths start at the prescribed root
and cover the colour class. The full rank totals are `N_A,N_B`.

If `N_A<=N_B`, full ordinary `A` packing is the root-and-marker
terminal. Otherwise its minimizing set is nonempty and the universal
input's connected-component reduction applies. A root-marker collision
gives the terminal helper after deleting the `a0` colour and extracting
the old `K_{2,3}` core. A collision of `0,2` without `a0` gives
Auxiliary C. With no collision, induct on the smaller marked instance.

If `N_A>=N_B+2`, restrict the `B` ground to `E-{0,2}`. Full
rank `N_B` gives a rooted `H_j` model avoiding both markers; adding
them to `X4,X3` completes the `B` triangle and leaves only one
cross-hole. Otherwise the rank is below `N_B<=N_A-2`, so a
nonempty minimizing set reduces while protecting both markers.
Check unused markers after cleanup, or induct on the smaller instance.

When `N_A=N_B+1`, use the modified `A` system of Section 3. Full
rank `R*=N_B` gives two full forests for `a1,a2` and an ordinary
`a0` forest with exactly two components separating `0,2`. Its
component containing `a0` contains one marker; the other is unused
by that component and the two full bags. The root-and-marker terminal
applies. If `R*<N_B`, then `R<=R*+1<=N_B`. For `R<N_B`
an ordinary nonempty minimizer gives a genuine connected-component
reduction as above. Otherwise the rank-one terminal applies.

Every recursive invocation strictly decreases scheme order and keeps
all roots, marked colours and auxiliary edges. The auxiliaries were
proved independently at all orders. This proves Theorem 1. QED

## 5. Root-hit dispatch for the crossed paths

We now prove Theorem 2 by induction on the union of its eight paths.
First dispatch root or crossed-marker hits, including after every
normalization or later path simplification.

If `L3` hits root `3`, take its prefix to that root. If it hits
marker `2`, take its prefix to `2` followed by `23`, stopping at
an earlier `3` if necessary. Either way this gives an actual proper
path `P3` from `a0` to `3`, avoiding `0`: the latter is the end
of the original simple `L3`. If `L4` hits `4` or `0`, it likewise
supplies a proper `a0-4` path. Together these and the old six paths
give an `H_1` scheme, and Theorem 1 applies.

Otherwise `L4` avoids both `4,0`. Keep only `P3,L4` and the six
old paths. None uses `0`. Contract its auxiliary edge `04` into
root `4`, gaining literal `14`. With marker `m=2`, this is precisely
Auxiliary H: an actual `a0-3` path and a colour-`4` path ending at
`2`, with literal `14,34` and the two marker edges `21,23`.
This step discards paths before contracting their unused marker, so
it neither assigns a scheme vertex to a foreign root nor presupposes
the endpoint remains in a path. Reflect this argument for a hit of
root `4` or marker `0` on `L4`.

We may henceforth assume `L3` avoids `3,2` and `L4` avoids `4,0`.
If either extra path misses the six-path `K_{2,3}` union, it is
itself the connected helper in the root-and-marker terminal. Thus
each extra path meets that union, necessarily in its `B` colour.
These terminal checks use no connection from `a0` to `1`.

## 6. Projection induction for the crossed paths

Normalize the `a1,a2` single-membership vertices as in Section 3,
checking Section 5 after each simplification, then compute fresh
counts and ranks. The `a0` projection consists of the two projected
paths from `a0` to `0,2`; it is connected. The other two `A`
projections are the old root-connected ones. Their total rank is
`N_A`, and every `B` nonroot is an internal, nonloop label.

The `B` projections are connected as well. For colours `3,4`,
project the old root-starting paths and the corresponding extra path;
the latter's internal `B` vertices form a possibly one-vertex path
meeting the old projection by Section 5. Its two `A` endpoints are
omitted. Colour `1` has only its old paths. In particular, neither
endpoint marker gives a `B`-projection edge: each is absent from
the opposite extra path, and no `a0-1` path exists in this system.
Every other `A` nonroot is internal on a path and gives a nonloop.

The ordinary connected-component reduction of the universal input
translates the extra paths as well as the old paths: each removed
internal traversal is replaced inside its specifically allocated
component before contraction. In the `B` orientation we exclude both
endpoint markers from the ground. In the `A` orientation a collision
between `a0` and a marker is the root-and-marker terminal after
extracting the old five-root core without the `a0` colour.

For a collision between `0,2` without `a0`, call the new colour-`a0`
vertex `m`. It has auxiliary edges to roots `3,4` through original
`23,04`. Append these to the two reduced extra paths, stopping at
the first visit to the matching root if necessary. This gives an
`H_1` scheme. Its single marked object has a connected preimage
containing both original markers, so Auxiliary C applies; if a chosen
prefix leaves it unused, use C's unused-object terminal case.

With no terminal collision all nine named vertices remain distinct.
After each reduction check Section 5. Otherwise the smaller path
system retains its proper colours, endpoints and auxiliary edges.
Every nonempty minimizing set used below contains a nonloop; in the
reverse orientation its only possible endpoint-only labels were
excluded. Thus at least one allocated connected set has three or
more vertices, and order strictly decreases.

For `N_A<=N_B`, ordinary `A` full packing is terminal because its
`a0` bag contains both markers. Deficient rank is below the ground
size `N_B`, so a nonempty ordinary minimizing set gives the genuine
reduction just checked.

For `N_A>=N_B+2`, restrict the `B` ground to `E-{0,2}`, whose
size is at least `N_B`. A full packing gives entire `B` colour
fibres as bags and singleton `A` roots. The first edges of `L3,L4`
give `a0` contacts to roots `3,4`; the old paths give all six
other cross-contacts. Both markers are unused and complete the `B`
triangle. Together with the literal `A` triangle, these six bags
miss at most `a0-1`; adding `{v}` is terminal. Deficient restricted
rank is below the ground size and gives a nonempty marker-protecting
reduction.

For `N_A=N_B+1`, full modified `A` rank gives the two-component
forest terminal of Section 4. If the modified rank is deficient,
`R<=R*+1<=N_B`. When `R<N_B`, use a genuine ordinary nonempty
component reduction. The remaining case is exactly the rank-one
terminal of Section 3, whose two-projection rank hypothesis follows
from the normalization and component count there.

All self-recursion strictly decreases the current path-union order;
the discarded paths in the root-hit dispatch instead invoke the
already established auxiliaries or Theorem 1. All contractions and
terminal transfers have fixed disjoint connected preimages and retain
the original-root contacts to `v`. This completes Theorem 2. QED

## 7. Exact critical-colouring consequence

**Corollary.** Suppose additionally that `G` is seven-connected,
`Q`-minor-free, `chi(G)=7`, every proper minor is six-colourable,
`N_G(v)={a0,a1,a2,0,1,2,3,4}`, and `{a0,0,2}` is independent.
For every proper six-colouring `f` of `G-v` giving `a0,0,2` one
colour `alpha`, one Kempe swap gives a colouring whose repeated pairs
on this neighbourhood are `{a0,x}` and `{y,z}`,
where `y,z` are nonadjacent cycle vertices and `x` is not their common
cycle neighbour. After a dihedral relabelling of the cycle, the pairs
are `{a0,3}` and `{0,2}`.

Such a colouring exists by the reserved-star contraction in
[the cycle-and-triangle construction](../active/hc7_degree8_cycle_triangle_construction.md),
SHA-256 `b3c43b4682c4554c2100d75dd14ea9df07aa898686b1cb6e3a1d9603985f68fe`.
In every such colouring the five other neighbours have distinct
colours; otherwise one could colour `v`. The same input's proof shows
that every five-colouring after deleting the whole `alpha` class
makes those five roots distinct. Hence the six old bichromatic paths
exist for every `f` under consideration.

**Proof.** Let `K3,K4` be the components containing `a0` in colours
`alpha,f(3)` and `alpha,f(4)`. Theorem 1 implies that at most one
contains its corresponding root `3` or `4`. A component `K3` missing
`3` also misses `2`, since `23` is a literal bichromatic edge; a
component `K4` missing `4` also misses `0` through `04`.

If either failed component avoids both markers, swap its two colours.
Among the eight neighbours this changes only `a0`, producing pairs
`{0,2}` and `{a0,3}` or `{a0,4}`. Each is of the required type.

Otherwise every failed component contains the opposite marker. Both
cannot fail: that would give an `a0-0` path in the first colour pair
and an `a0-2` path in the second, contrary to Theorem 2. Suppose
`K3` contains `3` and `K4` misses `4`; the other case is symmetric.
Then `K4` contains `2`. Theorem 2 forces `K3` to miss `0`.
It contains `a0,2,3`, the latter two joined by `23`, and contains
no other vertex of the displayed neighbourhood. Swapping its colours
therefore gives pairs `{0,3}` and `{a0,2}`. Relabel the cycle by

`(new0,new1,new2,new3,new4)=(0,4,3,2,1)`.

These become `{new0,new2}` and `{a0,new3}`, as claimed. All paths
used to apply the two theorems came from the same original colouring
`f`. The final swap is a proper recolouring of the unchanged host.
No earlier selected path system or model is claimed to survive it. QED

The remaining global obligation is a minor construction or a colouring
contradiction from the resulting two-pair state using the actual
critical host and its proper-minor responses. No finite computation
or significance-completion claim is a premise of these results.
