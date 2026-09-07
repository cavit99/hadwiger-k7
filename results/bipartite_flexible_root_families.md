# Flexible bipartite endpoints and a three-coloured cycle neighbourhood

**Status:** computation-free written proof; the adjacent audit records a
separate GREEN internal review. The second theorem closes a conditional
colouring state, not Conjecture 19, Conjecture 21 or `HC_7`.

All graphs are finite. Write `Q` for `K_7` with two independent edges
deleted. A minor model below means disjoint connected vertex sets with the
stated contacts. The sole external proof input is graphic
matroid union, in the form of Lemma 1 of
[universal bipartite contractibility](../results/bipartite_contractibility_via_matroid_reduction.md),
SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
The modified component reduction needed here is proved explicitly below.

## 1. A contraction theorem with prescribed root sets

**Theorem 1.** Let `H` be a finite simple bipartite graph. For each
`h in V(H)`, prescribe a nonempty finite set `R_h` of vertices in a host
graph `G`, with all these sets pairwise disjoint. For every `hk in E(H)`
suppose there is one simple path `P_hk` joining a vertex of `R_h` to a
vertex of `R_k`, with no other prescribed root internally.

Let `J` be the union of these paths and all prescribed roots, including
unused roots as isolated vertices. Suppose `J` has a proper colouring
`f:V(J)->V(H)` giving every vertex of `R_h` colour `h`, with `P_hk`
using only colours `h,k`. Then there are pairwise disjoint connected
sets `C_r subseteq V(J)`, one for every prescribed root `r`, such that:

* `r in C_r`;
* for each `hk in E(H)`, some `C_r`, `r in R_h`, has an edge to some
  `C_s`, `s in R_k`.

The contacting family members may depend on the target edge and may differ
from the initially selected path endpoints. Every individual prescribed
root has its own bag. In particular, any original edges between prescribed
roots remain contacts between their bags.

### Projections and full packings

Fix a bipartition `(A,B)` of `H`. Write `N_A,N_B` for the numbers of
nonroots in the corresponding colour shores. For a chosen projected
colour `a in A`, suppress each internal `B` vertex of `P_ab`, inserting
an edge between its two `A` neighbours with that vertex as its label.
Remove the terminal `B` root. The resulting paths begin at members of
`R_a` and cover all vertices of colour `a`; include unused roots too.
Call this actual projection `M_a`.

Identify all vertices of `R_a` only in this auxiliary graph, to obtain
`M_a*`. It is connected: every projected path meets the identified root.
Its graphic rank is the number of nonroots of colour `a`. Use the common
ground `E` of all `B`-coloured nonroots, declaring absent labels to be
matroid loops. A label appears at most once in each projection because
`H` is simple and the path for `ab` is unique. Moreover, every ground
label is a nonloop in some `M_a*`: its two neighbours on a path are
distinct, and they cannot both be prescribed roots, since the path has
no prescribed root internally. The total full rank is `N_A`.

Suppose disjoint label sets give full spanning trees in all `M_a*`.
Lift such a tree by separating its identified root back into `R_a`.
The lifted edges form a forest with exactly `|R_a|` components, each
containing one prescribed root. Indeed, independence after identification
forbids a path between two roots; the edge count gives exactly that many
components. Add to each component the actual `B` vertices labelling its
edges. These are connected sets, pairwise disjoint across all colours and
components. Give every `B` root its singleton bag.

For each demand `ab`, read its original path from the selected `B` root.
Its first neighbour belongs to one of these root-containing `A` bags,
giving the required contact. The selected `A` endpoint may change, which
is allowed. Thus a full packing proves the conclusion. This argument is
symmetric between the two shores.

### The modified component reduction

Fix `X subseteq E`. Suppose disjoint forests `F_a subseteq X` span every
component of every `M_a*(X)`. In a component not containing the identified
root, its allocated tree lifts to a single actual tree. In the component
containing that root, its allocated tree lifts instead to exactly one
tree for each member of `R_a`, by the same independence and edge-count
argument. Isolated roots are retained. In particular, there is no extra
root-free lifted piece inside this component.

For each lifted tree take its actual `A` vertices and its allocated
`B`-label vertices as a connected set `D`. These sets are pairwise disjoint,
contain at most one prescribed root each, and contain no `B` root.
Contract each `D` separately, delete the unallocated labels of `X`, and
retain the vertices of `E-X` and all `B` roots. Give each contracted
vertex its original `A` colour. We do **not** contract a disconnected
preimage of an identified root.

Here is the path lift that makes the reduction valid. Read `P_ab` from
its `B`-root endpoint and stop at its first `A` vertex belonging to a
lifted tree containing a prescribed root. Such a vertex exists, since
the original endpoint lies in such a tree. Before this first visit, an
internal traversal `u x w` with `x in X` lies wholly in a component of
`M_a*(X)` not containing the identified root: its first endpoint is in
a root-free lifted piece, and the edge labelled `x` stays in that same
modified component. Both endpoints therefore lie in the same actual
connected set `D`. Replace this traversal inside `D`, using only its
allocated labels, before contracting it.

An `X` edge between different pieces of the identified-root component
is never traversed: its first endpoint already triggers stopping. This
is exactly where flexible endpoint choice is used. In particular, a label
owned by another colour's set is never reused to cross between those
pieces. All other traversals use retained vertices of `E-X`. The image
is a two-colour walk from the original `B` root to a prescribed `A` root,
with no other prescribed root internally. Simplify it to a path.

Thus the quotient retains one path for every target edge, with the same
proper endpoint colours and all prescribed roots separate. Each individual
root's connected preimage is specified. If `X` is nonempty, it contains
a nonloop in some projection. The spanning forests then allocate at least
one edge, whose connected preimage contains its two distinct endpoints and
its actual label. At least one contraction therefore strictly decreases
the number of vertices. Keeping only the new path union and all roots
cannot increase that number.

### Induction and rank dichotomy

Induct on `|V(J)|`. Choose the shore with no more nonroots as the projected
shore; call its count `N_A`, so `N_A<=N_B=|E|`. A full packing of rank
`N_A` is terminal as above. Otherwise the union rank `R<N_A<=|E|`.
The matroid-union formula gives a minimizing set `X` and a maximizing
disjoint family with

`R=|E-X|+sum_a r_a*(X)`.

Equality forces its allocated forests to span every `M_a*(X)` component.
The set `X` is nonempty because the value at the empty set is `|E|`.
The modified component reduction gives a strictly smaller instance with
the same root sets represented by distinct connected preimages. Apply
induction there and compose these preimages. Connectivity, disjointness,
every individual root and all required family contacts lift. Isolated
target vertices and unused prescribed roots remain valid singleton-root
components throughout. This proves Theorem 1. QED

## 2. The three-coloured cycle state is terminal

**Theorem 2.** Suppose `G` has nine distinct vertices
`v,a0,a1,a2,0,1,2,3,4`, with a literal `A={a0,a1,a2}` triangle,
the literal cycle `0,1,2,3,4,0`, and `v` adjacent to the other eight.
Suppose their path union in `G-v` has six proper colours with root sets

`{a0}, {a1}, {a2}, {0,2}, {1,3}, {4}`.

For each `ai`, suppose one bichromatic path joins it to some member of
each of the last three root sets. These nine paths contain no other
prescribed root internally. Then `G` contains `Q`. Extra host edges and
all intersections compatible with the stated proper colours are allowed.

Apply Theorem 1 to `K_{3,3}` with these six root sets. Its eight disjoint
root bags retain the literal `A` triangle and rooted five-cycle, avoid
`v`, and each `A` bag contacts the root-`4` bag and at least one bag
from each pair `{0,2}`, `{1,3}`.

Choose one contact in each pair for each `A` bag. Its type is one of

`L=(0,1), R=(2,3), M=(2,1), E=(0,3)`.

Write `l,r,m,e` for the four type counts, whose sum is three. Retain
the root-`4` bag, and split the rooted path `0-1-2-3` at one of its
three edges. Unions over each resulting subpath are connected; the two
unions and the `4` bag form a triangle by the original cycle edges.

For the middle split `{0,1}|{2,3}`, only type L can miss the second
bag and only type R can miss the first. If `l,r<=1`, the at most two
missing cross-contacts have distinct ends. For the left split
`{0}|{1,2,3}`, only types R and M can miss a bag; it is valid if
`r+m<=1`. For the right split `{0,1,2}|{3}`, the analogous condition
is `l+m<=1`.

Some split is valid. If the middle condition fails, either `l>=2`,
giving `r+m<=1`, or `r>=2`, giving `l+m<=1`. The resulting three
cycle bags and three `A` bags therefore have both shore triangles and
at most two missing cross-contacts, which are independent. Add singleton
`{v}`. Each of the other six bags retains a prescribed neighbour of `v`,
so these seven bags form a `Q` model. All unions use disjoint original
preimages. This proves Theorem 2. QED

## 3. Exact critical-colouring application

Suppose additionally that `G` is `Q`-minor-free, `chi(G)=7`, every proper
minor is six-colourable, and `N_G(v)` is exactly the eight displayed
vertices. There is no proper
six-colouring of `G-v` in which the three `A` vertices have distinct
colours used nowhere else on `N(v)`, while the cycle has the three other
colours with pairs `{0,2}`, `{1,3}` and singleton `4`.

Indeed, fix such a colouring. For a colour of `ai` and one cycle colour,
the bichromatic component containing `ai` must meet some neighbourhood
vertex of the cycle colour. Otherwise swap that component: among `N(v)`
only `ai` changes colour, removing its old colour from the neighbourhood
and allowing `v` to be coloured. Choose a path to the first such root.
All nine resulting paths use the same proper colouring and avoid other
prescribed roots internally. Theorem 2 gives `Q`.

Thus this state is impossible in the stated critical host. Reaching it
from the retained two-pair colouring is a separate, unproved global
step. No recolouring is assumed to preserve an earlier selected model.
This conditional case completion is not a completion of the user's
global objective or an asserted significance comparison.
