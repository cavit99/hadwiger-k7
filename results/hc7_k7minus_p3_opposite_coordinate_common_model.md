# The induced-path row has two seven-connected pair hosts and one common model

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_p3_opposite_coordinate_common_model_audit.md).
This note treats only the induced-`P_3` branch of the six-coordinate
forest reduction.  It does not prove the `K_7^-` six-colour conjecture or
`HC_7`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq 6\text{ for every proper minor }J\text{ of }G,
 \qquad \kappa(G)\geq7,
 \qquad K_7^-\npreccurlyeq G,
 \qquad |E(G)|\geq4|V(G)|,
 \qquad |V(G)|\geq25.                               \tag{1.1}
\]

Let

\[
                 F=M_0\mathbin{\dot\cup}\{rx,ry\},             \tag{1.2}
\]

where `M_0` is a matching of order four, disjoint from the induced path
`x-r-y`; in particular `xy` is not an edge.  Put `X=G-F` and assume, as
in the audited six-coordinate forest reduction, that

\[
                  X+rx\quad\text{and}\quad X+ry                \tag{1.3}
\]

are seven-connected.  Let `S` be a cut of order six in `X`.  Orient the
two components of `X-S` as `C,D` so that

\[
                         r\in C,\qquad x,y\in D.                 \tag{1.4}
\]

Let `E_0` be the members of `M_0` with one end in each of `C,D`.  In the
final induced-path rows, `|E_0|` is one or two.  Fix

\[
                    e=uv\in E_0,\qquad u\in C,\quad v\in D.   \tag{1.5}
\]

There is no edge from `u` to either `x` or `y`: any such edge would join
the two components of `X-S`, and it is not a member of the componentwise
disjoint forest `F`.  Consequently

\[
                             \{u,x,y\}\text{ is independent}.   \tag{1.6}
\]

This elementary placement is the source of the common-model conclusion
below.

## 2. Two overlapping seven-connected pair hosts

For `z\in\{x,y\}`, write `z'` for the other leaf and put

\[
       J_z=G-\{e,rz\},\qquad Q_z=G/e/rz.                         \tag{2.1}
\]

Thus the braces in the definition of `J_z` mean edge deletion, while
`Q_z` contracts the two vertex-disjoint edges.

### Theorem 2.1 (opposite-coordinate pair host)

For each `z\in\{x,y\}`:

1. `J_z` is seven-connected and exactly six-chromatic;
2. its six-colour equality signatures on `(e,rz)` are exactly

   \[
       (\mathsf{equal},\mathsf{equal}),\quad
       (\mathsf{equal},\mathsf{proper}),\quad
       (\mathsf{proper},\mathsf{equal});                       \tag{2.2}
   \]

3. `Q_z` is exactly six-chromatic and therefore has a spanning `K_6`
   minor model; lifting this model to `G` gives one model which co-bags
   both pairs `\{u,v\}` and `\{r,z\}`; and
4. `J_z` has a spanning exact `K_7^\vee` model.

#### Proof

The graph `J_z` contains `X+rz'` as a spanning subgraph: compared with
`X+rz'`, it merely restores the three edges of `M_0-\{e\}`.  The graph
`X+rz'` is seven-connected by (1.3), so `J_z` is seven-connected.

Minor-minimality gives `\chi(J_z)\leq6`.  If `J_z` had a proper
five-colouring, recolour `u` and `z` with one new sixth colour.  These two
vertices are nonadjacent by (1.6).  The recolouring restores `e` and `rz`
properly and affects no other edge, giving a six-colouring of `G`.  This
contradiction proves `\chi(J_z)=6`.

Contracting either nonempty subset of the two-edge matching `\{e,rz\}`,
six-colouring the resulting proper minor and expanding gives the three
signatures in (2.2).  A colouring with both pairs proper would remain
proper after restoring the two edges and would six-colour `G`.  Hence
(2.2) is exact.

The graph `Q_z` is a proper minor and is therefore at most
six-chromatic.  If it had a five-colouring, expand its two contraction
images and recolour the independent pair `\{u,z\}` with a fresh sixth
colour.  Again this would restore both edges and six-colour `G`.  Thus
`\chi(Q_z)=6`.  The established case `HC_6` supplies a `K_6` model.  The
graph `Q_z` is connected, so unused vertices can be absorbed to make the
model spanning.  Expanding the two contraction images co-bags the two
specified endpoint pairs.

Finally, `J_z` is four-connected and

\[
                         |E(J_z)|\geq4|V(J_z)|-2.                \tag{2.3}
\]

The same Norin--Totschnig density theorem used in the six-coordinate
forest reduction supplies a spanning `K_7^\vee` model.  If either of its
two nominally absent branch-set adjacencies occurred in `G`, the same
seven bags would form a `K_7^-` model.  Target exclusion therefore makes
the model exact even after the two deleted edges are restored. `\square`

The important quantifier is that there are two concrete seven-connected
graphs `J_x,J_y`, not two unrelated operation colourings.  Their
intersection is the graph considered next.

## 3. The common three-coordinate host

Put

\[
             H_e=G-\{e,rx,ry\},\qquad
             Q_e=G/e/rx/ry.                                      \tag{3.1}
\]

The three contracted edges in `Q_e` form the componentwise-induced forest
`K_2\mathbin{\dot\cup}P_3`.

### Theorem 3.1 (one model for the whole induced path)

The following statements hold.

1. `H_e` is six-connected and exactly six-chromatic.  Both
   `H_e+rx=J_y` and `H_e+ry=J_x` are seven-connected.
2. The exact signature language of `H_e` on `\{e,rx,ry\}` is the
   punctured three-cube: every nonempty subset occurs and the empty
   subset does not.
3. `Q_e` is exactly six-chromatic.  It has a spanning `K_6` model which,
   when lifted to `G`, co-bags `u,v` and also co-bags all three vertices
   `r,x,y`.

#### Proof

The graph `H_e` contains `X` as a spanning subgraph, so it is
six-connected.  The identities with the two pair hosts follow directly
from (2.1), and their seven-connectivity is Theorem 2.1.

Minor-minimality gives `\chi(H_e)\leq6`.  If it had a five-colouring,
recolour the independent set `\{u,x,y\}` from (1.6) with one fresh sixth
colour.  This restores all three deleted edges properly and six-colours
`G`, a contradiction.  Hence `\chi(H_e)=6`.

For any nonempty subset of the three-edge forest, contract precisely that
subset, six-colour the proper minor and expand.  No uncontracted forest
edge collapses: the two forest components are disjoint, and `x-r-y` is
induced.  Restricting to `H_e` therefore gives exactly the selected
equality signature.  The empty signature would colour `G` after all three
edges were restored.  This proves item 2.

The graph `Q_e` is at most six-chromatic by minor-minimality.  A
five-colouring could be expanded and repaired by giving the independent
set `\{u,x,y\}` one fresh sixth colour, exactly as above.  Hence it is
six-chromatic.  Apply `HC_6`, make the resulting model spanning, and
expand its two contraction images.  One lifted bag contains `u,v`; one
lifted bag, possibly the same bag, contains the connected path `x-r-y`.
This is item 3. `\square`

### Proposition 3.2 (the exact blocked triple split)

Fix a lifted spanning `K_6` model from Theorem 3.1 and let `B` be the bag
containing `x,r,y`.  There is a partition

\[
                              B=B_x\mathbin{\dot\cup}B_r
                                    \mathbin{\dot\cup}B_y       \tag{3.2}
\]

into three nonempty connected sets containing `x,r,y`, respectively, such
that `B_xB_r` and `B_rB_y` are adjacent.  If four of the five foreign
model bags are adjacent to every one of `B_x,B_r,B_y`, then `G` contains
a `K_7^-` minor.  Consequently, in a target-free host, at most three
foreign bags can have all three contacts.

#### Proof

In the lifted connected bag choose a spanning tree containing the two
edges `rx,ry`; this is possible because those edges form a forest.  Delete
them from the tree and take its three components as the sets in (3.2).
They are connected and have the asserted literal adjacencies.

If four foreign bags meet all three sets, retain those four bags together
with the three sets in (3.2).  These are seven disjoint connected branch
sets.  The foreign bags are pairwise adjacent, each meets all three split
sets, and the only split-set adjacency which might be absent is
`B_xB_y`.  They therefore form a `K_7^-` model. `\square`

This proposition is the exact model-allocation obstruction in the
induced-path row.  Unlike the former one-fan formulation, the model and
both path edges come from one contraction.  What remains is to force a
fourth triple-contacting foreign bag, or to turn the obstruction to doing
so into a smaller response separator.

## 4. Six-cuts of the three-coordinate host

### Theorem 4.1 (six-cut placement)

Let `R` be a cut of order six in `H_e`.  Then `H_e-R` has exactly two
components, say `A,B`, and the names can be chosen so that

\[
                         r\in A,\qquad x,y\in B.                \tag{4.1}
\]

Moreover exactly one of the following holds.

1. `A=\{r\}`.  Then

   \[
                   N_G(r)=R\mathbin{\dot\cup}\{x,y\},
                   \qquad d_G(r)=8.                              \tag{4.2}
   \]

2. `A-\{r\}` is nonempty and `e` does not cross between `A` and `B`.
   Then `R\cup\{r\}` is the boundary of an actual order-seven
   separation of `G`.
3. `A-\{r\}` is nonempty and `e` crosses between `A` and `B`.  If `w`
   denotes its end in `B`, then `R\cup\{r,w\}` is the boundary of an
   actual order-eight separation of `G`.

Every actual separator in items 2--3 contains the actual neighbourhood of
each connected open component.  That neighbourhood has order seven or
eight and carries a proper-minor colouring response: choose an edge from
the component to its neighbourhood and restrict a six-colouring of its
deletion to the opposite closed shore.  The response boundary is
`N_G(K)`, which need not be the whole displayed seven- or eight-set.

#### Proof

Both `H_e+rx` and `H_e+ry` are seven-connected.  Adding either one edge
to `H_e-R` must therefore join all its components.  It follows that there
are exactly two components, none of `r,x,y` lies in `R`, and the two
incident edges have their ends in opposite components.  Since they share
`r`, (4.1) follows.

If `A=\{r\}`, then `N_{H_e}(r)\subseteq R`.  Six-connectivity of `H_e`
gives equality and `d_{H_e}(r)=6`.  The only deleted edges incident with
`r` are `rx,ry`, proving (4.2).

Assume `A-\{r\}` is nonempty.  Restoring `rx,ry` creates no edge between
`A-\{r\}` and `B`, because their common end `r` has been added to the
boundary.  If `e` does not cross the two components, no other restored
edge joins the residual sides, proving item 2.

If `e` crosses, put its `B`-end `w` in the boundary as well.  The set
`B-\{w\}` remains nonempty because it contains the two distinct vertices
`x,y`, neither of which is incident with `e`.  The other side contains
`A-\{r\}`.  This proves item 3.

For the final assertion, let `K` be a connected component on one open
side and choose an edge `ab` with `a\in K` and `b\in N_G(K)`; such an edge
exists by connectedness of `G`.  A six-colouring of `G-ab` restricts to a
proper colouring after `K` is deleted.  Its boundary partition cannot
extend through the intact `K`-side, since aligning and gluing the two
colourings would six-colour `G`. `\square`

### Corollary 4.2 (the order-nine path row becomes seven-connected)

Suppose the lifted induced-path boundary has order nine and **every**
proper-minor response separator of order seven or eight has been excluded,
including fresh or unanchored responses not carrying an inherited
coordinate label.  Then `H_e` is seven-connected for each of the two
edges `e\in E_0`.

#### Proof

The graph `H_e` is already six-connected.  If it had a six-cut, item 2 or
3 of Theorem 4.1 would give a response separator of order at most eight.
In item 1, (4.2) itself is an order-eight singleton response separator:
the graph has other vertices because it is seven-connected and has order
at least twenty-five.  Every case contradicts the hypothesis. `\square`

Thus the order-nine row is not another instance of the old bounded
fan/model mismatch.  Its common triple-deletion graph is seven-connected,
six-chromatic and carries the complete three-coordinate response cube.
By the density argument in Theorem 2.1 it also has a spanning exact
`K_7^\vee` model.

### Corollary 4.3 (exact order-eight normal form)

Suppose `|E_0|=1`, so the lifted boundary has order eight.  Then `S` is a
six-cut of `H_e`, `H_e-S` has exactly the original components `C,D`, and
all three edges `e,rx,ry` cross between them.  The graph therefore has,
on one literal common host:

* a six-connected, exactly six-chromatic graph with a specified six-cut;
* two seven-connected one-edge restorations;
* the full punctured three-coordinate response cube; and
* the common co-bagged `K_6` model and blocked triple split of
  Proposition 3.2.

#### Proof

The graph `H_e` is obtained from `X` by restoring the three members of
`M_0-\{e\}`.  Since `e` is the sole member of `M_0` crossing `C,D`, none
of those restored edges joins the two components of `X-S`.  Hence they
remain exactly the two components of `H_e-S`.  The placement of the three
deleted edges is (1.4)--(1.5).  All other assertions have already been
proved. `\square`

### Theorem 4.4 (two exact linkages with one common shore fan)

In the order-eight normal form, `H_e` contains:

1. six internally vertex-disjoint `r`--`x` paths; and
2. six internally vertex-disjoint `r`--`y` paths,

such that every path in either family contains exactly one vertex of `S`
and the six paths use the six vertices of `S` bijectively.  The paths are
pairwise internally vertex-disjoint within each family; they share both
nominated ends, `r,x` or `r,y`, and no other vertices.
The two families may be chosen with exactly the same six `r`--`S`
subpaths in `C\cup S`; only their subpaths in `D\cup S` need differ.

Moreover, if `P` is any connected subgraph of `H_e[D]` containing `x,y`,
there are six paths from `P` to the six vertices of `S`, pairwise
vertex-disjoint outside `P` and meeting `S` only at their ends.
Concatenating them with the same fixed `r`--`S` fan gives six `r`--`P`
paths which are pairwise vertex-disjoint outside `r` and `P`.

#### Proof

Complete `S` to a clique in each of the two closed shores
`H_e[C\cup S]` and `H_e[D\cup S]`.  Each resulting torso is
six-connected.  Indeed, a separator of order at most five would leave all
surviving vertices of the completed clique in one component; any other
component would have, in the original graph `H_e`, a neighbourhood of
order at most five separating it from the opposite shore.  This
contradicts six-connectivity of `H_e`.

The Fan Lemma in the `C`-torso gives a fixed six-fan from `r` to the six
vertices of `S`.  Stop its paths at their first boundary visits, so all
their internal vertices lie in `C`.  Apply the Fan Lemma in the `D`-torso
first at `x` and then at `y`, again stopping at first boundary visits.
Concatenating at the equally labelled vertices of `S` produces the two
asserted linkage families with their common `C`-side fan.

For the final assertion, choose any vertex of `P` and apply the Fan Lemma
there in the `D`-torso.  Stop each path at its first boundary visit, and
trim its initial segment through `P` up to its last vertex in `P`.  The
six residual paths have distinct boundary ends and are pairwise disjoint
outside `P`.  Concatenate them with the already fixed `C`-side fan.
`\square`

Thus the order-eight row already has both complete **geometric** linkages
in one graph.  The paths are not asserted to preserve bichromatic response
palettes.  The remaining quantifier issue is only between the two
`D`-side families: Theorem 4.4 does not give a simultaneous twelve-path
system or assign the six boundary vertices to the five foreign bags of
Proposition 3.2.

## 5. Exact gain and remaining obstruction

The common-model mismatch identified in the earlier single-fan note is
genuinely removed in the induced-path row.  For each leaf there is one
seven-connected graph carrying the opposite two-edge response, an exact
near-clique model and a co-bagged `K_6` model; contracting the whole
three-edge forest gives one model containing both the opposite coordinate
and the entire path.

This still does not finish the row.  The first unsupported inference would
be to turn the two response systems into four foreign bags meeting all
three pieces in (3.2).  The complete response cube fixes edge equalities,
not branch-set labels, and the two one-edge Kempe fans may use different
colourings.  Proposition 3.2 records the precise obstruction rather than
assuming that allocation.

The next positive statement can now be narrower than the proposed generic
two-restorer theorem:

> **Induced-path triple-split exchange target.**  In the exact order-eight
> normal form of Corollary 4.3, optimize the single co-bagged model from
> Theorem 3.1.  Either four foreign bags meet all three split pieces,
> giving `K_7^-`; or the obstruction returns an order-seven
> response-bearing separator.  In the order-nine row the same obstruction
> must be resolved inside the seven-connected common host of Corollary
> 4.2.

The accepted outputs are now literal and host-measured.  No comparison of
two separately chosen `K_6` models is required.

## Dependencies and scope

The proof uses only the audited six-coordinate forest reduction, the
established `HC_6`, the Norin--Totschnig density theorem already used in
that reduction, and elementary colouring, connectivity and branch-set
arguments.  No finite enumeration is used.
