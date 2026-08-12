# A common double-contraction state at the order-nine matching row

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_matching_square_common_state_audit.md).
This note
sharpens the matching case of the final order-nine six-cut residue.  It does
not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J,
 \qquad \kappa(G)\geq7.                              \tag{1.1}
\]

Suppose

\[
 V(G)=A\mathbin{\dot\cup}T\mathbin{\dot\cup}B,
 \qquad A,B\ne\varnothing,
 \qquad E_G(A,B)=\varnothing,                         \tag{1.2}
\]

and choose vertex-disjoint edges

\[
                  e=up,\qquad f=vq,                  \tag{1.3}
\]

where `u in A`, `v in B`, and `p,q in T`.  Assume that
`G-{e,f}` contains a spanning six-connected subgraph `X`.

In the live application, `|T|=9`, `X=G-F` for the six-edge matching
`F`, and `e,f` are the two distinguished matching coordinates entering
opposite full components.  The hypothesis on `X` follows from the
six-coordinate forest reduction.  The arguments below are stated without
assuming that the components are full until fullness is needed for the
final application.

Put

\[
                         H=G-\{e,f\}.                 \tag{1.4}
\]

For a six-colouring `c` of `H`, its **edge signature** records, for each
of `e,f`, whether its two ends have equal or distinct colours.

## 2. One common six-chromatic graph and one common model

### Theorem 2.1 (opposite-coordinate common state)

The following statements hold.

1. `H` is six-connected and exactly six-chromatic.
2. Among their edge signatures, its six-colourings realise precisely

   \[
        (=,\ne),\qquad(\ne,=),\qquad(=,=),             \tag{2.1}
   \]

   and never `(\ne,\ne)`.
3. The double contraction is exactly six-chromatic:

   \[
                              \chi(G/e/f)=6.            \tag{2.2}
   \]

4. Consequently `G/e/f` has a spanning `K_6`-minor model.  On lifting
   this model to `G`, both endpoint pairs `{u,p}` and `{v,q}` are
   contained in branch bags of this one model.  The two pairs may lie in
   the same bag.
5. The graph `H` has a `K_4`-minor model rooted at `u,p,v,q`.

#### Proof

The inclusion `X subseteq H` makes `H` six-connected.  It is a proper
minor of `G`, so it is six-colourable.  If it had a colouring with at most
five colours, recolour `u` and `v` with one new sixth colour.  The vertices
`u,v` are nonadjacent by (1.2).  The new colour occurred nowhere else,
and the recolouring repairs both omitted edges.  This would six-colour
`G`.  Hence `chi(H)=6`.

Contracting `e`, contracting `f`, or contracting both independent edges
and then expanding the contraction classes gives respectively the three
signatures in (2.1).  A colouring with both pairs distinct would remain
proper after restoring `e,f`, contrary to `chi(G)=7`.  This proves items
1--2.

The proper minor `G/e/f` is six-colourable.  Suppose that it had a
colouring with at most five colours.  Expand both contraction vertices,
so that the ends of each of `e,f` have one colour.  Recolour `u,v` with
one fresh sixth colour.  Again `uv` is not an edge, and every other
neighbour of either vertex retains one of the original five colours.
The resulting assignment is a proper six-colouring of `G`, a
contradiction.  This proves (2.2).

The established case `HC_6` gives a `K_6` minor in `G/e/f`.  Since that
graph is connected, unused components may be absorbed into adjacent bags
to make the model spanning.  Expanding the two contraction vertices
inside their bags gives item 4.

Finally, every six-connected graph is two-linked.  Applying the standard
rooted-`K_4` characterisation to the four nominated vertices in `H`
gives item 5. `\square`

Item 4 is local to the opposite-shore pair.  It does not claim that one
model co-bags all six edges of the original forest.

### Theorem 2.2 (double-contraction connectivity fork)

Put `K=G/e/f`, and denote its two contraction vertices by `r_e,r_f`.
Then

\[
                              \kappa(K)\geq5.           \tag{2.3}
\]

Moreover, either `K` is six-connected, or `G` has an actual order-seven
separation carrying a generic proper-minor colouring response.

More precisely, if `Q` is an order-five cut of `K`, then

\[
              r_e,r_f\in Q,\qquad
              S=(Q-\{r_e,r_f\})\cup\{u,p,v,q\}        \tag{2.4}
\]

is an order-seven cut of `G`.  Every component of `G-S` is full to `S`.
For every such component `Y` and every edge `yz` from `Y` to `S`, a
six-colouring of `G-yz` restricts to a proper colouring of `G-Y` whose
partition on `S` is rejected by the intact `Y`-side.

#### Proof

Let `Q` be a cut of `K`.  Replace every contraction vertex belonging to
`Q` by the two ends of its contracted edge.  The resulting set `Q^+`
separates in `G` the literal preimages of any two components of `K-Q`, and

\[
                              |Q^+|\leq |Q|+2.          \tag{2.5}
\]

If `|Q|<=4`, then (2.5) contradicts seven-connectivity.  This proves
(2.3).

Suppose `|Q|=5`.  If either `r_e` or `r_f` were absent from `Q`, then
`|Q^+|<=6`, again impossible.  Thus both belong to `Q`, and `Q^+` is
exactly the seven-set `S` in (2.4).  It is an actual separator.  In a
seven-connected graph, every component behind an order-seven cut is
adjacent to every literal cut vertex, proving fullness.

Fix `Y` and `yz`.  In every six-colouring of `G-yz`, the ends `y,z` have
one colour; otherwise the deleted edge could be restored.  Deleting `Y`
removes the sole possible monochromatic edge, so the restriction to
`G-Y` is proper.  If its equality partition on `S` extended through the
intact closed `Y`-side, align colour names on the boundary blocks and
glue.  This would six-colour `G`.  Hence the partition is rejected, as
claimed. `\square`

Thus the genuinely model-allocation case may additionally assume that the
common double contraction itself is six-connected.  The order-five case
returns an exact order-seven separator with a rejected proper-minor
partition.  This separator need not be nested in either original shore, so
the theorem does not by itself turn it into an anchored minimum-side
descent.

### Lemma 2.3 (the literal connector cycle and its limitation)

Suppose that `A` and `B` are connected and full to `T`, as in the live
residue.  There are an `u`--`q` path `P_A` in `G[A\cup\{q\}]` with
interior in `A` and a `v`--`p` path `P_B` in `G[B\cup\{p\}]` with
interior in `B`.  The paths are internally disjoint, and

\[
                         P_A\cup P_B\cup\{e,f\}       \tag{2.6}
\]

contains a cycle through both selected coordinate edges.

#### Proof

Fullness gives a neighbour of `q` in `A`; connectedness of `A` joins it
to `u`.  This gives `P_A`, and the proof for `P_B` is symmetric.  Their
interiors lie in the disjoint anticomplete open shores.  Adding
`up` and `vq` closes their union into the asserted cycle. `\square`

This does not yield a common four-endpoint contraction model.  Fullness
does not say that `uq` or `vp` is an edge.  Even after choosing shortest
connectors, the cycle in (2.6) may have odd length or chords.  Contracting
it to one vertex therefore does not justify expanding a five-colouring by
two-colouring the contracted subgraph with the old colour and one fresh
sixth colour.  Its unbounded order also destroys the useful cut-lifting
bound.  Thus Theorem 2.1(4), rather than a four-cycle contraction, is the
strongest common `K_6` model presently proved.

### Theorem 2.4 (two restorers make the common deletion seven-connected or return an order-at-most-eight response)

Assume additionally that both one-edge restorations

\[
                            H+e=G-f,\qquad H+f=G-e     \tag{2.7}
\]

are seven-connected.  Then either `H` is seven-connected, or there is a
nonempty connected set `Y` such that

\[
                       7\leq |N_G(Y)|\leq8,           \tag{2.8}
\]

and `N_G(Y)` is an actual separator carrying a rejected proper-minor
colouring partition.

More precisely, if `S` is an order-six cut of `H`, then `H-S` has exactly
two components `C,D`, and both `e,f` cross between them.  Write

\[
                       e=u_Cu_D,\qquad f=v_Cv_D
\]

according to their sides.  Each of

\[
                    S\cup\{u_C,v_D\},\qquad
                    S\cup\{v_C,u_D\}                 \tag{2.9}
\]

is the boundary of an actual order-eight separation of `G` with nonempty
residual vertices on both sides.  Every component behind either boundary
has the response in (2.8).

#### Proof

The graph `H` is six-connected by Theorem 2.1.  Suppose that `S` is an
order-six cut.  Since `H+e-S` is connected, adding the one edge `e` must
join all components of `H-S`.  Hence there are exactly two components,
both ends of `e` lie outside `S`, and `e` crosses between them.  Applying
the same argument to `H+f` proves the assertion for `f`.

The two selected edges are vertex-disjoint.  Deleting `S\cup\{u_C,v_D\}`
therefore leaves `v_C` on the `C` side and `u_D` on the `D` side.  It also
meets both edges omitted from `H`.  The remaining vertices inherited from
`C,D` are nonempty and anticomplete in `G`.  Thus the first set in (2.9)
is an actual order-eight boundary.  The other choice is symmetric.

Let `Y` be any component behind one of these boundaries, chosen on either
side.  A component on the opposite side is nonempty, so `N_G(Y)` is an
actual separator contained in the eight-set (2.9).  Seven-connectivity
gives (2.8).  Choose an edge `yz` with `y in Y` and `z in N_G(Y)` and
six-colour the proper minor `G-yz`.  Its two ends have the same colour,
since otherwise the deleted edge could be restored.  Deleting `Y` removes
that sole conflict.  If the induced partition on `N_G(Y)` extended through
the intact `Y`-side, the two colourings would align and glue to a
six-colouring of `G`.  It is therefore rejected. `\square`

In the live `6K_2`, `q=3` row, take `e,f` to be the two distinguished
forest edges and orient them into opposite lifted shores.  The
six-coordinate theorem gives seven-connectivity of `X+e` and `X+f`.
Since these are spanning subgraphs of `G-f` and `G-e`, respectively,
(2.7) holds.

### Corollary 2.5 (one seven-connected host carries the square and the exact near-clique model)

Assume the critical-host density and target-exclusion hypotheses

\[
 |E(G)|\geq4|V(G)|,\qquad |V(G)|\geq25,qquad
                         K_7^-\npreccurlyeq G.         \tag{2.10}
\]

If the response outcome (2.8) has been excluded, then `H` is
seven-connected and contains a spanning exact `K_7^vee`-minor model.
This one graph simultaneously carries that exact model, all three
signatures in (2.1), no all-proper signature, and the rooted `K_4` from
Theorem 2.1.

#### Proof

Theorem 2.4 gives seven-connectivity.  Moreover

\[
                         |E(H)|\geq4|V(H)|-2.
\]

The Norin--Totschnig density theorem supplies a `K_7^vee` minor; its small
exception is excluded by the order hypothesis.  Absorb unused components
into adjacent branch sets to make the model spanning.  If either of its
two nominal missing adjacencies occurred in `G`, the same seven branch
sets would form a `K_7^-` model.  Target exclusion therefore makes both
pairs anticomplete even after `e,f` are restored. `\square`

### Theorem 2.6 (an unlocked singleton response returns a separator)

Assume that `G` has no `K_7` minor.  Let `phi` be a six-colouring of `H`
with

\[
       \phi(u)=\phi(p)=i,\qquad \phi(v)\ne\phi(q).    \tag{2.11}
\]

If `u,p` lie in different components of the `i`--`j` subgraph of `H` for
some `j != i`, then there is a nonempty connected set `D` such that
`N_G(D)` is an actual separator of order at least seven.  Moreover, one
six-colouring of `G-D` is the common restriction of the two opposite
singleton responses, and its partition on `N_G(D)` is rejected by the
intact `D`-side.

Consequently, if no such response-bearing separator exists, then in every
singleton response the equal endpoint pair is bichromatically joined for
all five alternate colours.

#### Proof

Switch the colours `i,j` on the bichromatic component `D_u` containing
`u`.  This makes `e` proper.  Since an all-proper colouring of `H` would
six-colour `G`, the switch must make `f` monochromatic.  It follows that
the two original colours on `v,q` are exactly `i,j` and that `D_u`
contains exactly one of `v,q`.  Applying the same argument to the
component `D_p` containing `p` shows that it contains the other endpoint
of `f`.  Thus `D_u,D_p` are distinct connected bichromatic components,
both omitted edges cross between them, and switching either component
changes (2.11) directly into the opposite singleton response.

If either component, say `D_u`, is not dominating, its open neighbourhood
is an actual separator and has order at least seven by seven-connectivity.
The two response colourings agree literally outside `D_u`; after deleting
`D_u`, their common restriction is proper on `G-D_u` because both omitted
edges lose one endpoint.  An extension of its boundary partition through
the intact `D_u`-side would align and glue to a six-colouring of `G`.
This gives the asserted response.

It remains to exclude the possibility that both components dominate.
There is no edge of `H` between two distinct `i`--`j` components.  The
only `G`-edges between `D_u,D_p` are therefore the vertex-disjoint edges
`e,f`.  Domination by `D_u` says that every vertex of `D_p` is incident
with one of these two edges.  Their two ends already lie in `D_p`, so
`D_p` consists of exactly those vertices.  Symmetrically `D_u` also has
order two.  Connectedness supplies one `H`-edge inside each component,
and the four endpoints consequently induce a four-cycle whose opposite
edges are `e,f`.

Contract that four-cycle to a vertex `w`, obtaining a proper minor `L`.
If `L` were five-colourable, expand `w` by giving one independent pair of
the cycle its old colour and the other independent pair one fresh sixth
colour.  Every outside neighbour avoids the old colour, and the fresh
colour occurs nowhere outside the cycle.  This would six-colour `G`.
Hence `chi(L)=6`.

By `HC_6`, choose a spanning `K_6` model in `L` and lift the bag containing
`w`.  The other five bags remain pairwise adjacent and disjoint from
`D_u,D_p`.  Since both components dominate, each is adjacent to every one
of those five bags; they are adjacent to one another through `e,f`.
Therefore

\[
                  D_u,D_p,B_1,\ldots,B_5
\]

are seven pairwise adjacent connected branch sets, an explicit `K_7`
minor.  This contradiction proves that one component is nondominating and
finishes the theorem. `\square`

The theorem spends the missing fourth signature at a literal Kempe switch.
It is stronger than the earlier four-lock count, but its returned separator
has no proved upper bound.  A response of order seven or eight is terminal
for the present row; a larger boundary still requires an anchored descent
or a further model allocation theorem.

## 3. The double state either repairs a shore or supplies its response fan

Fix a six-colouring `c` of `G/e/f` and lift it to `H`.  Put

\[
              c(u)=c(p)=\alpha,\qquad
              c(v)=c(q)=\gamma,\qquad
              \pi=\Pi_T(c).                           \tag{3.1}
\]

Say that the `A`-shore is **repairable with trace `pi`** if
`G[A union T]` has a proper six-colouring inducing `pi` on `T`.
Define repairability of the `B`-shore symmetrically.

### Theorem 3.1 (common-state repair or prescribed fan)

The two shores are not both repairable with trace `pi`.

If the `A`-shore is not repairable, then `G[A union T]` contains six
paths from `u` to six distinct vertices of `T`, pairwise vertex-disjoint
outside `u` and meeting `T` only at their ends, with the following extra
properties:

1. one path is the edge `up`;
2. for each colour `beta != alpha`, one of the other five paths starts
   with an edge from `u` to a `beta`-coloured vertex in the fixed lifted
   colouring `c`.

The symmetric conclusion holds at `v` when the `B`-shore is not
repairable.  Consequently exactly one of the following applies to the
fixed common state `c`:

1. one shore is repairable with `pi`, while the other shore has the
   displayed common-state six-fan; or
2. neither shore is repairable, and both shores have such six-fans.

#### Proof

If both shores were repairable, permute colour names so that their
colourings agree literally with `c` on `T`.  They would glue across
(1.2) to a proper six-colouring of `G`.  Thus at least one repair fails.

Suppose the `A`-shore is not repairable.  Fix `beta != alpha` and consider
the component `K_beta` containing `u` in the subgraph of
`G[A union T]-e` induced by colours `{alpha,beta}` under `c`.  If
`K_beta` avoided `T`, interchanging `alpha,beta` on that component would
fix every boundary colour and make `up` proper.  This would repair the
`A`-shore with trace `pi`, contrary to the assumption.  Hence
`K_beta` meets `T`.  A shortest path from `u` to `T`, stopped at its first
boundary vertex, has all internal vertices in `A`.  Its first neighbour
of `u` has colour `beta`.  The five alternate colours therefore give five
distinct prescribed first edges.

It remains to make the paths disjoint while preserving those first edges.
Let `D` be the set of prescribed first neighbours which already belong to
`T`, put `h=|D|`, and retain those `h` one-edge paths.  The other
`ell=5-h` first neighbours form a set `R subseteq A-{u}`.  In

\[
       G[(A-\{u\})\cup(T-(D\cup\{p\}))]               \tag{3.2}
\]

seek `ell` pairwise vertex-disjoint paths from `R` to distinct members of
`T-(D union {p})`.  If no such linkage exists, Menger's theorem gives a
set `Z` of order at most `ell-1` meeting every such path.  A surviving
source lies in a component `K` whose neighbourhood in `G` is contained in

\[
                         \{u,p\}\cup D\cup Z.          \tag{3.3}
\]

The right side has order at most

\[
                    2+h+(\ell-1)=6.                   \tag{3.4}
\]

The nonempty opposite shore lies outside `K` and its neighbourhood, so
(3.3) contradicts seven-connectivity.  The linkage exists.  Prepending
the prescribed first edges, retaining the `h` direct paths, and adding
`up` gives the required six-fan.  The proof for `B` is identical.  The
final alternatives merely record whether one or both repairs fail.
`\square`

Thus the two singleton responses need not be aligned with one another.
Instead, the double-contraction colouring itself supplies every first-edge
colour used by whichever shore rejects its boundary trace.

### Theorem 3.2 (common-state lock allocation)

In the same lifted colouring `c`, the following additional statement
holds.

1. If `alpha=gamma`, then one of `up,vq` is joined between its ends in
   `H` by bichromatic paths for at least three of the five alternate
   colours.
2. If `alpha != gamma`, then one of `up,vq` has such paths for at least
   four alternate colours.

Every one of these paths can be stopped at its first visit to `T`; before
that visit it lies in the appropriate open shore and starts with an edge
whose other end has the stated alternate colour.

#### Proof

Fix two colours and consider all components of their induced subgraph in
`H`.  Interchanging the two colours on an arbitrary union of components
preserves properness.  For either equal-coloured endpoint pair, whether a
chosen family of components separates its two colours after the switches
is a linear form over `F_2` in the component choices.

If `alpha=gamma`, fix an alternate colour `delta`.  The two forms for
`up` and `vq` cannot both be nonzero: if they were, elementary linear
algebra over `F_2` would give a component choice making both pairs
distinct.  Restoring `e,f` would then six-colour `G`.  Hence at least one
pair is locked in the `alpha`--`delta` subgraph for each of the five
choices of `delta`.  One pair receives at least three locks.

Suppose instead that `alpha != gamma`.  Let `J` be the set of the four
colours other than `alpha,gamma`.  Let `U` be the colours `delta in J`
for which `up` is not `alpha`--`delta` locked, and define `V`
symmetrically for `vq` and `gamma`.  If `delta in U` and `eta in V` are distinct, the palettes
`{alpha,delta}` and `{gamma,eta}` are disjoint.  The two component
switches therefore commute and make both pairs distinct, again colouring
`G`.  Thus either one of `U,V` is empty, or both are the same singleton.
In the `alpha`--`gamma` subgraph at least one pair is locked by the same
two-form argument.  If one of `U,V` is empty, its pair has the four locks
indexed by `J`; if both are the same singleton, both pairs have the three
locks indexed by the other members of `J`, and one receives the
`alpha`--`gamma` lock.  In every case one pair is locked for at least four
alternate colours.

A lock is a path between the two ends in the corresponding bichromatic
subgraph.  Starting at the open-shore end and stopping at the first member
of `T` gives the final assertion, by (1.2). `\square`

The paths in Theorem 3.2 need not be mutually internally disjoint.  Its
gain is instead that all of them, both endpoint pairs, and the forbidden
all-proper signature belong to one literal colouring of one graph.

## 4. Exact split obstruction in the common model

Lift a spanning `K_6` model from Theorem 2.1(4), and let `R_e` be the bag
containing `e`.  Choose a spanning tree of `G[R_e]` which contains `e`.
Deleting `e` from that tree divides `R_e` into two nonempty connected sets
`R_u,R_p`, containing `u,p`, respectively.

### Proposition 4.1 (four foreign double contacts are terminal)

If at least four of the five foreign `K_6` bags are adjacent to both
`R_u` and `R_p`, then `G` contains a `K_7^-` minor.

Consequently, in a target-free host, every such split of either co-bagged
coordinate has at most three foreign bags adjacent to both sides.

#### Proof

The sets `R_u,R_p` are adjacent through the restored edge `e`.  The five
foreign bags are pairwise adjacent.  Four of them are adjacent to both
split sets by hypothesis.  The fifth is adjacent to their union, because
it was adjacent to the original bag `R_e`, and hence can miss at most one
of `R_u,R_p`.  These seven connected branch sets therefore have at most
one nonadjacent pair and form a `K_7^-` model.  The final assertion is the
contrapositive. `\square`

## 5. What this resolves and what remains

The matching-row response square now has one literal common state:

* `G/e/f` is exactly six-chromatic;
* one spanning `K_6` model co-bags both opposite coordinate pairs;
* for the two distinguished restorers, excluding generic responses of
  order at most eight makes their common deletion seven-connected and
  puts the full response square on the same graph as an exact spanning
  `K_7^vee` model;
* the same double-contraction colouring either repairs one shore or gives
  its five prescribed first edges; and
* in that colouring one coordinate has three or four literal
  bichromatic lock paths; and
* Menger's theorem upgrades the five prescribed first edges on every
  nonrepairable shore to a shore-confined six-fan; and
* an unlocked palette in either singleton response gives a
  response-bearing separator: its alternative dominating endpoint
  four-cycle would give an explicit `K_7` minor.

This removes two proposed quantifier exchanges: no comparison of unrelated
singleton colourings is needed, and no comparison of two independently
chosen edge-rooted `K_6` models is needed.

A bounded hostile diagnostic in
[`opposite_shore_coordinate_square_gate/`](../active/experiments/opposite_shore_coordinate_square_gate/)
shows that these positive objects still do not imply the exchange.  Its
`K_7^-`-minor-free quotient has the three displayed signatures, exact
single and double contractions, two coloured six-fans, one common
co-bagged spanning `K_6` model and blocked splits, while the two singleton
boundary languages remain disjoint.  The quotient is only
three-connected and is five-colourable: crucially, it also has the fourth
all-proper signature.  It is therefore a scoped barrier to a positive-data
argument, not to the critical-host theorem.  Theorem 2.4 shows that its
low connectivity is not available after all order-at-most-eight responses
are excluded; its all-proper signature remains the decisive missing
critical-host input.

It does **not** complete the fan-to-model exchange.  The paths in Theorem
3.1 may use internal vertices of the foreign branch bags and may first meet
several vertices carrying the same model label.  Proposition 4.1 requires
four foreign bags to retain contacts with both split sides.  Neither
vertex-disjointness of the fan nor the three edge signatures assigns those
contacts.  After all response separators are excluded, Theorem 2.6 makes
the equal pair in each singleton response locked in all five alternate
palettes, but those five paths still need not be disjoint or respect the
five model labels.

The exact remaining implication in the matching row is therefore:

> Starting with the common double-contraction colouring, its nonrepairable
> shore fan, the common co-bagged `K_6` model, and the exact spanning
> `K_7^vee` model in the seven-connected common deletion, use the universal
> absence of the all-proper signature at a blocked coordinate split
> to do one of the following: reassign fan prefixes so that four foreign
> bags meet both sides; produce one partition extending through both
> shores; or return a connected proper shore subset whose actual
> neighbourhood has order seven or eight.

The quoted two-restorer formulation cannot assume that both shores supply
fans: one shore may already be repairable with the common trace.  When both
are nonrepairable, Theorem 3.1 does supply two fans in the same colouring,
but it still supplies no model-label assignment.  This is the first
unsupported inference after the common response square has been fully
spent.  The finite diagnostic shows that merely retaining the three
positive square vertices at that inference is insufficient; the proof must
convert the missing fourth vertex into literal model contact or a boundary
extension.

## Dependencies and scope

The proof uses seven-connectivity, proper-minor six-colourability, the
six-connected common deletion host, Menger's theorem, the established case
`HC_6`, the standard theorem that every six-connected graph is two-linked,
and the rooted-`K_4` characterisation.  In the live application the
six-connected host and the opposite coordinate placement come from the
audited six-coordinate forest and six-cut localisation theorems.

No finite enumeration is used in the proofs.  The theorem is unbounded in
the orders of the two open shores.  The cited finite diagnostic is only a
scoped proof gate.  The final paragraph is a route nonclosure, not a
counterexample to the remaining exchange theorem.
