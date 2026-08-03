# Audit: dense five-separator reductions

**Verdict:** GREEN.

**Audited source:**
`active/hc7_k7minus_e5_k5minus_cut_elimination.md`

**SHA-256:**
`81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0`

This is a separate internal mathematical audit, not external peer review.
The result is computation-free.

## 1. Fifth-root augmentation

The optimisation in Lemma 1 is legitimate because a finite graph has only
finitely many branch-set models.  The contact-set argument was checked in
the only delicate case.

Let

```text
A_i = {r in R_i : r has a neighbour in U},
B_i = {r in R_i : r has a neighbour in V}.
```

If `A_i union B_i` has at least two vertices, nonempty `A_i,B_i` admit
distinct choices `u in A_i`, `v in B_i`; otherwise both sets would be the
same singleton.  A minimal tree containing `z_i,u,v` has a non-root leaf
among `u,v`.  If this leaf is `u`, moving it into `U` preserves:

- connectivity of both altered bags;
- the `R_i`--`U` adjacency, through the deleted leaf's tree edge;
- the `R_i`--`V` adjacency, through the retained vertex `v`;
- the `U`--`V` adjacency and every other root--helper adjacency.

Thus maximal helper order forces exactly one contact vertex in every root
bag, and that vertex necessarily contacts both helpers.

Absorbing a whole unused component that meets a helper is also valid and
strictly enlarges the helper union.  Hence the external neighbourhood of
the two helpers has order at most four.  If `x` were outside the helpers,
the displayed separation would contain all of `S` on its first side and
have the nonempty helper union as its second open side.  This exactly
contradicts internal five-connectivity.  No assumption that the root bags
are pairwise adjacent is used in this lemma.

## 2. Virtual-edge lift

Lemma 2 was checked independently in its cover-indexed form.  Orient every
virtual edge towards one of its ends in the nominated vertex cover.  A
component assigned to a cover vertex contains one connected subtree
meeting a neighbour of that vertex and neighbours of all opposite ends
assigned to it.  Contracting the subtree into the cover vertex realises all
those edges simultaneously.  Distinct cover vertices use distinct
components, so the enlarged model bags remain disjoint.  The inequality
`|A|<=r-2` leaves a further whole component for the seventh branch set.

This remains valid when a virtual edge is incident with the omitted root
`x`: Lemma 1 first places `x` in a helper bag, and the component subtree is
then absorbed into that helper or into the root bag at the chosen cover
end.  Thus every adjacency of the augmented rooted model lifts literally.

The density conversion is exact:

```text
|E(G[S union C_0]+F)|-(4|S union C_0|-9)
 = |E(G[S])|+delta(C_0)+|F|-11.
```

The lemma states internal four-connectivity explicitly.  The advertised
degree-four sufficient condition correctly handles the only exceptional
separation, whose second open side is the singleton omitted root `x`.
The stronger, unjustified assertion that internal five-connectivity of
`(H,S)` alone implies internal four-connectivity of `(H,S-{x})` is not
used.

## 3. Cap construction and density equality

Every component of `G-S` is full to `S` by five-connectivity.  An
`x`--`y` path through the opposite component realises the sole virtual edge
`xy`; contracting its open interior and deleting surplus material gives
`G[A]+xy` as an actual proper minor, not merely as an abstract completion.

Observation 7(1)--(2) of Norin--Totschnig gives the required
five-connectivity of each completed cap.  Minimum order of the E5 enemy
therefore yields

```text
|E(G[A])| <= 4|A|-9,
|E(G[B])| <= 4|B|-9.
```

Subtracting the nine boundary edges gives the exact global upper bound
`4|V(G)|-7`.  Since the reverse inequality is assumed, both cap bounds and
the global bound are equalities.  The arithmetic was recomputed directly.

## 4. Internal four-connectivity

The passage from `(G[A],S)` internally five-connected to `(G[A],Z)`
internally four-connected is valid.  The only case not handled by simply
moving `x` to the root side is a separation whose second open side is the
singleton `{x}`.  Its separator would contain every neighbour of `x` in
`G[A]`, but `x` has three neighbours in `S-{x,y}` and at least one neighbour
in a component contained in `A-S`.  Thus its order is at least four.

Norin--Totschnig Lemma 12 applies at the strict threshold
`|E(G[A])|=4|A|-9`: absence of the rooted `K^*_{4,2}` model would give the
contradictory upper bound `4|A|-10`.

## 5. Terminal branch sets

The final seven branch sets are:

1. the four rooted bags, containing the four vertices of `Z`;
2. the two adjacent helper bags, one containing `x`;
3. the opposite component `D`.

The first six bags are pairwise adjacent: root--root edges are supplied by
the literal clique `G[Z]`, and all other adjacencies are part of the rooted
model.  Fullness of `D` supplies its four root-bag adjacencies and its
adjacency to the helper containing `x`.  Only its adjacency to the other
helper may be absent.  The bags are disjoint and connected.  This is an
explicit `K_7^-` model.

## 6. The eight-edge boundary reduction

Theorem 4 was audited separately from the earlier `K_5^-` case.

If the two missing boundary edges share an end, one full connected
component contains a connected subgraph meeting all three relevant
boundary vertices.  Absorbing this subgraph into the common-end root bag
simultaneously realises both missing edges.  With at least three exterior
components this gives five clique bags and two further full bags, with only
the last two possibly nonadjacent.  With exactly two components, completing
each closed shore through the opposite component gives two proper
five-connected target-free minors.  Their two minimality inequalities,
after subtracting the eight boundary edges, give the contradictory bound
`|E(G)|<=4|V(G)|-8`.  Thus the two missing edges are independent.

With independent missing edges, four exterior components are immediately
terminal: two realise the two virtual boundary edges through disjoint
components and two are retained as the final branch sets.  Hence at most
three components remain.

For one component `L`, deleting the fifth boundary vertex `t` gives the
four-terminal pair `(H_L,X)`.  Any separation of this pair of order at most
three extends, by putting `t` in its separator, to a separation of the
closed shore relative to all five boundary vertices of order at most four.
Thus the pair is internally four-connected.  Robertson--Seymour--Thomas
Theorem 13 applies to the root order `x,z,y,w`: it gives either the required
disjoint `x`--`y` and `z`--`w` paths, its excluded separation outcome, or a
disc drawing in that cyclic order.  In the disc case a missing outer-face
diagonal may be added, so the planar bound is

```text
|E(H_L)| <= 3|V(H_L)|-7.
```

The four roots induce the cycle `xzywx`, and the identity

```text
|E(H_L)|=4|L|+delta(L)-p_t+4
```

was recomputed from the definition of `delta(L)`.  Since `p_t<=|L|`, a
component without the two paths has `delta(L)<=1`.

The global identity for a boundary with eight edges is

```text
sum_L delta(L)=q+5.
```

It excludes three crossless components; a linked component together with
the other two components gives the explicit seven-bag model.  Thus exactly
two components remain.  One has excess at least three and is linked.
Completing the opposite shore gives `delta(D)<=2`; equality would make
`D` linked and force the first component to have excess at most two,
contrary to the global identity.  Hence `delta(D)<=1`.  If `D` were still
linked, the same opposite-shore completion would again give
`delta(C)<=2`, contradicting `delta(C)+delta(D)>=5`.  Therefore `D` is
crossless and `delta(C)>=q+4`.

Every minor model used here was checked at branch-set level.  A component
realising a virtual boundary edge is split between its two endpoint bags;
different virtual edges use different components.  Every retained whole
component is full to the boundary by five-connectivity.

## 7. Clique caps and global accounting

Lemma 5 is valid with a vertex cover rather than one component per missing
edge.  All missing boundary edges oriented to one cover vertex are realised
inside one opposite full component and contracted into that boundary
vertex.  Completing the five-set therefore gives an actual proper minor.
Internal five-connectivity of the closed shore and the clique completion
give five-connectivity.  Minimality yields

```text
4|C_i|+delta(C_i)+10 <= 4(|C_i|+5)-8,
```

so every capped component has `delta(C_i)<=2`.

The global identity was recomputed as follows:

```text
|E(G)|
 = |E(J)| + sum_i (4|C_i|+delta(C_i))
 = 4|V(G)|-20+|E(J)|+sum_i delta(C_i).
```

Subtracting `4|V(G)|-7` gives
`sum_i delta(C_i)=q+13-|E(J)|`.

## 8. Four-, five-, and three-component quotients

For five components, any boundary edge gives the seven displayed bags;
the only possible missing adjacency is between the last two whole
components.  Thus the boundary is edgeless.  Its complement has vertex
cover number four, so the cap bound gives total excess at most ten whereas
the global identity requires at least thirteen.

For four components, a boundary triangle gives the displayed seven-bag
model.  Hence a nonempty surviving boundary is triangle-free and has at
most six edges.  Any boundary edge leaves three other vertices covering
the complement, so all four component excesses are at most two.  The
global identity forces five or six boundary edges and a component of
excess two.  The elementary classification is complete:

- six edges gives `K_{2,3}` by equality in Mantel's theorem;
- five edges gives `C_5` when the minimum degree is two, and `C_4` with a
  pendant edge when there is a leaf.

For each of these three graphs, the stated set `F` was checked to consist
of missing boundary edges, to make the four roots a clique, and to have a
two-vertex cover.  Its size is respectively three, four, and four, so the
rooted density expression is exactly eleven.  The omitted vertex has
degree at least four after the stated augmentation.  Lemma 2 therefore
applies with two components realising `F` and a third retained component.

For three components, a boundary triangle leaves two vertices covering all
missing edges, so the cap and global bounds force at least seven boundary
edges.  A boundary with at most one missing edge is terminal after using at
most one component to realise that edge.  With two missing edges, a common
end is terminal by one-component absorption; the independent matching is
closed by one virtual edge.  With three missing edges, a star is terminal
by the same absorption.  The remaining three isomorphism types are exactly
`K_3`, `P_4`, and `P_3` disjoint from `K_2`.  In the three displayed rows,
the virtual set has size two and a one-vertex cover, completes the four
roots, and makes the density expression eleven.  The omitted-root degree
check is correct in every row.  Thus every three-component boundary is
triangle-free.

All quotient constructions were checked directly from fullness: a whole
component is connected and adjacent to every boundary singleton or bag,
and two retained whole components account for the unique permitted missing
adjacency.

## 9. Scope and dependencies

The audit checked the following external statement against the current
primary source:

- Norin--Totschnig, Lemma 12: an internally four-connected pair `(H,Z)`
  with `|Z|=4` and no `Z`-rooted `K^*_{4,2}` model satisfies
  `|E(H)|<=4|V(H)|-10`.
- Robertson--Seymour--Thomas, in the form quoted as Norin--Totschnig
  Theorem 13: for cyclically ordered terminals, either the alternating
  two-path linkage exists, there is a root-side separation of order at most
  three with nonempty far side, or the graph has the corresponding disc
  drawing.

Theorem 3 eliminates the `|E(G[S])|=9` five-cut case.  Theorem 4 eliminates
all `|E(G[S])|=8` cases except the exact two-component independent-miss
configuration stated there.  Theorem 6 excludes five components and forces
an edgeless boundary for four components.  Theorem 7 forces a triangle-free
boundary for three components.  It does not eliminate the empty
four-component boundary, the remaining triangle-free three-component
boundaries, or the two-component residues, and does not prove E5 or the
primary seven-connected extremal target.

No unresolved mathematical assumption was found in the stated result.
