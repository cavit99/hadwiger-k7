# Forest-component reduction in the bounded-feedback branch

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_feedback_forest_component_reduction_audit.md).
This is a conditional structural reduction inside a hypothetical critical
host.  It does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` be a minor-minimal non-six-colourable graph satisfying

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor `J` of `G`},
 \qquad \kappa(G)\geq7,\qquad K_7^-\npreccurlyeq G,
 \qquad K_5\nsubseteq G,
\]

and suppose that `T` is a feedback vertex set with

\[
             |T|\leq14,\qquad \chi(G[T])\geq5.       \tag{1.1}
\]

Put `R=G-T`, so `R` is a forest.  Use Theorem 5.1 of the audited
[six-centre feedback theorem](../results/hc7_k7minus_feedback_six_centre_common_matching.md)
to fix six independent degree-eight vertices

\[
 Z=\{z_1,\ldots,z_6\}\subseteq V(R)
\]

and distinct vertices `y_i in T cap N_G(z_i)`.  Thus

\[
                       M_T=\{z_iy_i:1\leq i\leq6\}   \tag{1.2}
\]

is a matching.  The same theorem supplies the complete punctured
six-signature family and a spanning `K_6`-minor model co-bagging all six
pairs in (1.2).

For `Y subseteq V(R)`, write

\[
 \partial_R Y=N_R(Y),\qquad \partial_TY=N_G(Y)\cap T. \tag{1.3}
\]

The two sets in (1.3) are disjoint and their union is `N_G(Y)`.

## 2. The basic forest inequality

### Lemma 2.1 (connected-piece boundary)

Let `Y` be a nonempty connected vertex set in `R`.  If

\[
                  V(G)-(Y\cup N_G(Y))\ne\varnothing, \tag{2.1}
\]

then

\[
              |\partial_TY|+|\partial_RY|\geq7.      \tag{2.2}
\]

If equality holds, `N_G(Y)` is an order-seven separator, `Y` is a
component of `G-N_G(Y)`, and every component of `G-N_G(Y)` is adjacent to
every vertex of `N_G(Y)`.

#### Proof

The set `N_G(Y)` separates the connected set `Y` from the nonempty set in
(2.1).  Seven-connectivity gives (2.2).  In the equality case, `Y` is a
component after its entire open neighbourhood is deleted.  If another
component `D` of `G-N_G(Y)` missed a vertex `s` of `N_G(Y)`, then
`N_G(D)` would be contained in the other six separator vertices.  This
would contradict seven-connectivity. `\square`

The equality case has two further consequences which will be useful in a
future colouring composition.  Its seven-vertex boundary has no `K_5`
minor: such a five-bag model, together with `Y` and any other full
component, would be a `K_7^-` model.  Moreover the boundary partitions
induced by six-colourings of `G[Y\cup N_G(Y)]` and `G-Y` are disjoint.
Indeed, a common partition can be aligned by a permutation of the six
colours and the two colourings can then be glued to six-colour `G`.

## 3. Exact forest alternatives forced by the six centres

Call three pairwise disjoint connected sets `A,B,C` in one component of
`R` a **three-piece forest path** when the only edges of `R` between them
are at least one `A`--`B` edge and at least one `B`--`C` edge; in the
construction below there is exactly one of each and no `A`--`C` edge.

### Theorem 3.1 (order-seven separation, three pieces, or six components)

At least one of the following holds.

1. `G` has an order-seven separator of the exact kind in Lemma 2.1.
2. One component of `R` has a partition into a three-piece forest path
   `(A,B,C)` satisfying

   \[
       |\partial_TA|\geq7,\qquad
       |\partial_TB|\geq6,\qquad
       |\partial_TC|\geq7.                            \tag{3.1}
   \]

   Either `B` contains one of the selected exceptional centres, or `A`
   and `C` are singleton selected exceptional centres.
3. There are six distinct components `C_1,...,C_6` of `R`, with

   \[
       z_i\in C_i,qquad |N_G(C_i)\cap T|\geq8
                       \quad(1\leq i\leq6).           \tag{3.2}
   \]

#### Proof

For a selected centre `z`, neighbours of `z` in `R` are independent:
two adjacent such neighbours would form a triangle in the forest `R`.
The exceptional-neighbourhood theorem gives
`alpha(G[N_G(z)])=3`, and hence

\[
       d_R(z)\leq3,\qquad |N_G(z)\cap T|=8-d_R(z)\geq5. \tag{3.3}
\]

Suppose first that some selected centre `z` has `d_R(z)>=2`.  In its tree
component choose two components `A,C` of `R-z` which contain two distinct
neighbours of `z`, and put all the remaining vertices of that tree
component into `B`.  Thus `B` contains `z` and is connected; precisely one
forest edge joins `A` to `B`, precisely one joins `B` to `C`, and there is
no `A`--`C` edge.  We have

\[
        |\partial_RA|=|\partial_RC|=1,qquad
        |\partial_RB|=2.                               \tag{3.4}
\]

Lemma 2.1 applies to `A` and `C`, and gives the two outer lower bounds
`6,6`.  If equality holds in either application, outcome 1 holds;
otherwise both bounds strengthen to seven.  If
`V(G)-(B\cup N_G(B))` is nonempty, the lemma also applies to `B` and
gives the middle lower bound five.  Equality again gives outcome 1, and
otherwise the bound strengthens to six.  If instead
`B\cup N_G(B)=V(G)`, then there is no other component of `R` and
`T=\partial_TB`.  By (1.1), `G[T]` is at least five-chromatic.  Since
`G` has no `K_5` subgraph, this forces `|T|>=6`.  Thus (3.1) holds in
this case as well, with `z in B`.

We may therefore assume that every selected centre has forest degree at
most one.  If two selected centres `z_i,z_j` lie in one tree component,
they are distinct nonadjacent leaves.  Put `A={z_i}`, `C={z_j}`, and let
`B` be the tree left after deleting those two leaves.  The set `B` is
nonempty and connected, and `(A,B,C)` is a three-piece forest path.  Since
the centres have degree eight,

\[
                  |\partial_TA|=|\partial_TC|=7.       \tag{3.5}
\]

If `V(G)-(B\cup N_G(B))` is nonempty, Lemma 2.1 applied to `B`, whose
forest boundary has order two, gives `|\partial_T B|>=5`.  Equality gives
outcome 1; otherwise (3.1) holds.  If instead
`B\cup N_G(B)=V(G)`, the other four selected centres lie in `B`: they
lie neither in `T` nor in `A\cup C`, and there is no other component
of `R`.  Each has forest degree at most one and degree eight, so each has
at least seven neighbours in `T`.  All of those neighbours belong to
`\partial_TB`; in particular `|\partial_TB|>=7`, and again (3.1)
holds.

It remains that the six selected centres lie in six distinct components
`C_i` of `R`.  The open neighbourhood of each `C_i` is contained in `T`,
and deleting it separates `C_i` from the other five components.  Thus
seven-connectivity gives

\[
                         |N_G(C_i)\cap T|\geq7.        \tag{3.6}
\]

Equality gives outcome 1 by Lemma 2.1.  If equality never occurs, the six
integer bounds in (3.6) strengthen to (3.2). `\square`

The thresholds in (3.1) are stronger than the first `6,5,6` suggested by
the three-vertex diagnostic.  The strengthening costs exactly one clear
alternative: an actual full order-seven separation.

## 4. Simultaneous cycle and common-model obstruction

### Theorem 4.1 (one cycle through the boundary-crossing matching)

One cycle of `G` contains all six edges of `M_T`.  For every prescribed
vertex `v` of `G`, a cycle can be chosen which contains `v` and all six
edges of `M_T`.

#### Proof

The six edges of `M_T` are independent, and `G` is seven-connected.  The
theorem of Haggkvist and Thomassen on cycles through prescribed independent
edges gives the first assertion.  For the second, start with such a cycle
`C`.  If `v` is outside `C`, the Fan Lemma gives seven internally disjoint
paths from `v` to seven distinct vertices of `C`.  The seven endpoints cut
`C` into seven intervals, at most six of which contain a selected edge.
Replace an interval containing none of them by the two corresponding fan
paths. `\square`

This puts all six forest-boundary coordinates on one literal cycle.  It is
simultaneous information; it does not exchange six separately existential
linkages.

There is also an exact obstruction to splitting the common co-bagged
model.  Fix a spanning `K_6` model

\[
                              Q_1,\ldots,Q_6          \tag{4.1}
\]

which co-bags every edge of `M_T`.  Assign each selected edge to one bag
which contains both its ends.  In each `Q_j`, the assigned matching edges
form a forest and hence extend to a spanning tree `S_j` of `G[Q_j]`.

### Proposition 4.2 (blocked split certificate)

Let `e` be assigned to `Q_j`, and let `A_e,D_e` be the two components of
`S_j-e`.  At most three of the five other model bags have a neighbour in
both `A_e` and `D_e`.

#### Proof

Suppose four other bags contact both sides.  The fifth other bag contacts
at least one side because it is adjacent to `Q_j`.  The seven connected
sets

\[
              A_e,\ D_e,\ (Q_k:k\ne j)               \tag{4.2}
\]

are pairwise adjacent except possibly for the fifth bag and the one side
which it does not contact.  The two split sets are adjacent through `e`.
Thus (4.2) is a `K_7^-` model, contrary to the setting. `\square`

The spanning trees `S_j` are chosen once, so Proposition 4.2 holds for all
six selected edges on one common model.  It records the exact obstruction
left by the contact-only split: every selected crossing edge has at most
three foreign branch bags represented on both sides of its tree cut.

## 5. Exact remaining composition statements

The feedback branch has therefore been reduced to the following three
host-level tasks.

1. **Full order-seven separation.**  Use the selected centre edge when it
   is incident with the returned shore, or the common signature family,
   to rule out the two disjoint boundary-partition families described
   after Lemma 2.1.
2. **Three-piece composition.**  For the path `(A,B,C)` in (3.1), combine
   the two forest edges, its `7,6,7` contacts in `T`, and the six-centre
   response/model data.  A `K_4` model in `T` whose every branch set meets
   all three boundary-neighbour sets would already be terminal: together
   with `A,B,C` it gives seven bags with only `A,C` nonadjacent.  The
   boundary-only existence of that rooted model is not asserted here.
3. **Six-component composition.**  Combine six pairwise anticomplete tree
   components satisfying (3.2) with the six selected centre edges.  The
   previous two-set-transversal barrier does not address this six-piece,
   contact-eight configuration.

Proposition 4.2 says exactly what a proof using the common `K_6` model must
overcome in any of these rows.  The common cycle in Theorem 4.1 is the
additional graph-level structure not present in a contact quotient.

There is one further boundary input which postdates the earlier
`K_5`-minor formulation.  Theorem 1.1 of Girão, Illingworth, Mohar,
Norin, Steiner, Tamitegama, Tan, Wood and Yip, *The Dominating 4-Colour
Theorem* (arXiv:2605.10112v1), says that every non-four-colourable graph
has a dominating `K_5` model.  Thus (1.1) supplies such a model in
`G[T]`, and it may be chosen with two adjacent singleton branch sets and
a third path bag whose union with them induces a cycle.  This is stronger
than an arbitrary `K_5` model, but the published theorem does not
prescribe which of the contact sets in outcomes 2--3 meet its branch bags.
It therefore sharpens the available model normal form without closing
either composition.

No finite diagnostic is used in the proof above.  In particular, the
order-seven/eight screens in
[`feedback_forest_boundary_gate`](../active/experiments/feedback_forest_boundary_gate/README.md)
remain evidence only and are not cited as an unbounded implication.

## Dependencies

The critical-host and six-centre inputs are listed in the audited
[six-centre feedback theorem](../results/hc7_k7minus_feedback_six_centre_common_matching.md).
The cycle input is Roland Haggkvist and Carsten Thomassen, *Circuits through
specified edges*, Discrete Mathematics **41** (1982), 29--34, in the form
already used and audited in the six-coordinate induced-forest reduction.
The dominating-model input is António Girão, Freddie Illingworth, Bojan
Mohar, Sergey Norin, Raphael Steiner, Youri Tamitegama, Jane Tan, David R.
Wood and Jung Hon Yip, *The Dominating 4-Colour Theorem*,
arXiv:2605.10112v1, Theorem 1.1 and the structural remarks immediately
following it.
