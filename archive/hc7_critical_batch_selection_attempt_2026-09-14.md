# Critical-host batch selection: attempted global constructions

**Frozen on 14 September 2026.** Retained discovery record; current status is in the research ledger and technical frontier.

**Original status:** unaudited working draft; recorded route nonclosure. This is a
bounded attempt at the actual C19 host, not another current ledger or a
promoted theorem. No global batch-selection theorem, C19 closure, HC7 proof,
or independently substantiated comparable theorem is established here.

Assume throughout that G is seven-contraction-critical in the strong
sense `chi(G)=7` and every proper minor is six-colourable. For the actual
C19 application also retain seven-connectivity, minimum degree eight,
Q-minor exclusion, and the degree-eight vertex with the recorded
two-triangle-and-edge neighbourhood, where `Q=K7-2K2`.

The existing [matching construction](../active/hc7_two_triangle_matching_colour_host.md)
already contracts three neighbourhood edges with an independent
transversal, and obtains complementary actual-root schemes from a shared
colouring in its five-chromatic branch. Neither that colour-preservation
argument nor its unclosed rooted allocation is counted as new progress.

## 1. One simultaneous response for arbitrary independent star assignments

**Written deduction; unaudited.** Let I be any nonempty independent set
of G. For every assignment choosing `r_w in N_G(w)` for each `w in I`,
there is one proper six-colouring c of `G-I` such that

`c(r_w) notin c(N_G(w)-{r_w})` for every w simultaneously.

Indeed all selected roots lie outside I. For each distinct root r,
contract the connected star consisting of r and the vertices assigned
to r. These stars are disjoint even when several vertices select the
same root. The resulting proper minor has vertex set `V(G)-I` and adds
exactly the edges from each selected root to the other neighbours of
its assigned vertices, apart from repetitions. Its six-colouring is
precisely the asserted common response. The star sets are fixed connected
preimages for every subsequent model lift.

For a six-colouring c of `G-I`, define

`S_c(w)={r in N_G(w): c(r) notin c(N_G(w)-{r})}`.

The response statement is equivalently the exact Cartesian cover

`union_c product_{w in I} S_c(w) = product_{w in I} N_G(w)`.

Every such c saturates at least one w, meaning that its neighbours use
all six colours. Otherwise each vertex of I could independently receive
a missing colour and c would extend to G.

**Attempt and first unsupported inference.** Choosing roots diagonally
outside the singleton-neighbour sets of saturated responses need not
produce an uncovered assignment. Already on the literal neighbourhood
`K3 disjoint-union K3 disjoint-union K2`, every prescribed vertex can be
singleton-coloured in a proper partition using all six colours. Pair
two disjoint nonedges avoiding that vertex and leave the other four
vertices singleton. For a triangle vertex a0 one can pair a1 with b1
and a2 with x; for x one can pair a0 with b0 and a1 with b1. Symmetry
handles the other vertices. Thus saturated local responses cover all
eight root choices. Independent products reproduce this phenomenon in
arbitrarily many abstract coordinates.

This is a nonimplication for the proposed response argument, not a
counterexample to the actual host. A successful use must prove additional
compatibility between responses from the same exterior. Bounding each
individual singleton set, or merely taking more simultaneous choices,
does not supply that inference.

## 2. A global contraction that would make the terminal theorem applicable

**Written sufficient construction; unaudited.** Suppose G contains a
connected induced bipartite set B with at least two vertices, B dominates
`G-B`, and `G-B` is four-connected with at least six vertices. Then G
contains Q.

To prove the assertion, contract B to p. If its quotient had a
five-colouring, expand one shore in the colour of p and the other shore
in one fresh sixth colour. This would six-colour G. Proper-minor
criticality therefore makes the quotient exactly six-chromatic. Since
p is universal, `chi(G-B)=5`. The audited
[four-connected colouring theorem](../results/four_connected_five_chromatic_minor.md)
supplies `Q6=K6-2K2` in `G-B`, which is not K5 by its order. Adding p
gives Q. Replacing p by the fixed connected set B lifts this model.

This operation permits a large batch and expands the completing bag
globally. It does not prescribe the original triangle roots or require
their later restoration. Its missing part is selection of B.

**First attempted selection.** An inclusion-maximal connected induced
bipartite set need not dominate: outside vertices with no neighbour in
the set cannot be added while retaining connectedness, and vertices
meeting both shores can block access to them.

**Explicit obstruction to structural selection alone.** Take independent
sets `A_0,...,A_4`, each of order seven, and put in all edges between
cyclically consecutive sets. For each i add a disjoint clique `X_i=K6`
joined completely to A_i and to no other vertices. This 65-vertex graph
is seven-connected, has minimum degree twelve, and has chromatic number
seven. Deleting at most six vertices leaves every A_i nonempty and the
cyclic backbone connected, with every surviving X_i vertex attached.
Deleting A_i separates X_i, so connectivity is exactly seven. Each
`X_i` together with one A_i vertex is K7; conversely colour the backbone
with three colours and each X_i with the six colours avoiding its A_i
colour.

There is no connected induced bipartite dominating set B in this graph.
If B misses A_i, domination of X_i forces B to meet X_i. Connectivity
then confines B to X_i, which cannot dominate distant modules. Hence B
must meet every A_i. One representative from each intersection induces
a five-cycle inside B, a contradiction.

The example contains a proper K7 subgraph and violates both proper-minor
criticality and Q exclusion. It refutes the selection statement under
connectivity, minimum degree and chromatic number alone. The precise
remaining obligation is to use those actual-host hypotheses to select B,
including four-connectivity of its entire exterior; neither is inferred.

**Second attempted selection.** Drop connectedness and choose a maximal
induced bipartite set B containing an edge. Its connected components can
all be contracted in the same batch: choose one shore in each component;
their union is independent because distinct components have no edges.
The quotient is again six-chromatic, and its component poles form an
independent dominating set. Maximality gives domination, since an outside
vertex with no B-neighbour could otherwise be added as an isolated vertex.
The exterior has chromatic number five or six.

This repair retains the colouring and disjoint preimages but loses the
universal completing bag. Connecting the poles through exterior vertices
can create an odd cycle in a preimage, invalidating the one-fresh-colour
expansion, and can consume contacts needed by the exterior minor. No
selection or exchange preserving both requirements was proved.

## 3. Actual-neighbourhood initialization did not remove the selection gap

Start with the induced star on v and an independent triple in N(v), as
in [whole-class reservation](../results/hc7_critical_colour_class_reservation.md).
Its proper-minor response gives a six-colouring of `G-v` with that triple
in one entire class I and the remaining five neighbours in five distinct
classes. For one such remaining neighbour r with class J, the induced
graph on `I union (J-{r}) union {v}` is bipartite. Its component through
v contains the three chosen marks, and is an admissible single bag.

However other components of those two classes can remain outside that
bag. They need not be dominated by it; deleting the v-component need not
leave a five-chromatic or four-connected graph. Restoring, moving or
connecting the detached components changes the same colouring responses
and ownership needed in the exterior construction. This initialization
therefore does not yet select the global bag in Section 2.

No decreasing induction class or terminal alternative was obtained from
these three attempts. The Cartesian response and the dominating-bag exit
make the desired operation precise; they do not close the batch-selection
obligation. Further work should attack an actual selection inference,
not reprove the matching or independent-shore colour-preservation step.
