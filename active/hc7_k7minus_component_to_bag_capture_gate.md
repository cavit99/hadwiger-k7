# The exact branch-bag gate for a response component

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_component_to_bag_capture_gate_audit.md).
This is a
conditional reduction inside the eight-coordinate campaign.  It does not
prove the `K_7^-` six-colour conjecture or `HC_7`.

The all-degree dominated-singleton theorem supplies one common graph with a
fixed exact `K_7^vee` model, an operated edge `ux`, and an actual response
component `A` containing `x`.  The component need not lie in one model bag.
The following theorem identifies exactly when its intersection with the bag
containing `x` already yields the required model-anchored response.  The
remaining obstruction is a literal separation of the exterior of the
response component from one named portal set by the vertex `x`; model
persistence by itself does not remove it.

## 1. Setting

Let `G` be a graph which is not six-colourable, let `ux` be an edge, and let
`c` be a proper six-colouring of `G-ux` with

\[
                              c(u)=c(x).                 \tag{1.1}
\]

Let `A` be a connected set containing `x` such that `c|G-A` is proper and
the boundary partition induced by `c` on `N_G(A)` is rejected by the intact
closed `A`-side.

Let

\[
                           J,D_1,\ldots,D_6              \tag{1.2}
\]

be pairwise disjoint nonempty connected branch sets of a fixed labelled
minor model.  They need not cover `V(G)`.  The proof below uses only the
connectedness of `J`; the exact `K_7^vee` application gives the seven sets
in (1.2).  Assume `x in J`.  For a foreign bag `D_i`, put

\[
                 \Pi_i=N_G(D_i)\cap J.                  \tag{1.3}
\]

Thus `Pi_i` is the full set of literal `J-D_i` portal vertices.  It may be
empty when the two model labels are nominally nonadjacent.

## 2. Exact capture criterion

### Theorem 2.1 (portal co-location is equivalent to bag capture)

Fix `i in {1,...,6}`.  The following statements are equivalent.

1. There is a nonempty proper connected set `Y subseteq A cap J` such that
   `x in Y`, `J-Y` is connected, and `D_i` is anticomplete to `Y`.
2. Some component `W` of `G[J-x]` contains

   \[
                         (J-A)\cup\Pi_i.                 \tag{2.1}
   \]

When these conditions hold, one may take

\[
                              Y=J-W.                    \tag{2.2}
\]

This `Y` retains the same operated edge and colouring: `c|G-Y` is proper,
and the partition induced by `c` on `N_G(Y)` is rejected by the intact
closed `Y`-side.  Moreover `N_G(Y)` is an actual separator, with the named
connected bag `D_i` on a far side.  In a seven-connected host,

\[
                              |N_G(Y)|\ge7.              \tag{2.3}
\]

#### Proof

Suppose first that item 1 holds.  The connected set `J-Y` is contained in
`J-x`, and therefore lies in one component `W` of `G[J-x]`.  Since
`Y subseteq A`, every vertex of `J-A` lies outside `Y` and hence in `W`.
Since `D_i` is anticomplete to `Y`, every member of its portal set `Pi_i`
also lies outside `Y`, and hence in `W`.  This proves (2.1).

Conversely, let `W` be a component satisfying (2.1) and put `Y=J-W`.
Every component of `G[J-x]` has a neighbour at `x`, because `G[J]` is
connected.  Consequently `Y`, which consists of `x` together with all
components other than `W`, is connected.  It is nonempty, and it is proper
because `W` is nonempty.  The inclusion `J-A subseteq W` gives
`Y subseteq A`, while `Pi_i subseteq W` says exactly that `D_i` is
anticomplete to `Y`.  Thus item 1 holds.

The only monochromatic edge restored to `G` under `c` is `ux`.  Since
`x in Y`, its restriction to `G-Y` is proper.  If the induced boundary
partition extended through `G[Y union N_G(Y)]`, a permutation of colour
names followed by gluing would give a proper six-colouring of `G`, a
contradiction.  Hence the trace on `Y` is rejected.

Finally, `D_i` is nonempty, connected and anticomplete to `Y`; it lies
outside `Y union N_G(Y)`.  Thus `N_G(Y)` is an actual separator.  The
connectivity bound (2.3) follows immediately. `\square`

### Corollary 2.2 (the non-cutvertex case)

If `J-x` is nonempty and connected, then the required capture exists
whenever `x` is anticomplete to one named foreign bag `D_i`.

#### Proof

Take `W=J-x`.  Then `J-A subseteq W`, and anticompleteness of `x` to
`D_i` gives `Pi_i subseteq W`.  Theorem 2.1 returns `Y={x}`. `\square`

## 3. What target exclusion supplies, and what it does not

Retain an exact `K_7^vee` model

\[
                    P,B,C,U_1,U_2,U_3,U_4,              \tag{3.1}
\]

where `B,C,U_1,...,U_4` form a `K_6` model and `P` is anticomplete to
`B,C`.

### Proposition 3.1 (co-connected vertex: exact far-bag residue)

Suppose `G` has no `K_7^-` minor, `x in J`, and `J-x` is nonempty and
connected.

1. If `J=P`, then `x` is anticomplete to at least one of
   `B,C,U_1,...,U_4`, and Theorem 2.1 captures `{x}`.
2. If `J` is `B` or `C`, then the nominally missing bag `P` is
   anticomplete to `x`, and Theorem 2.1 captures `{x}`.
3. Suppose `J=U_i`.  Then Theorem 2.1 captures `{x}` unless `x` has a
   neighbour in every one of the six foreign bags.  In that exceptional
   placement, let `Omega_x` be the set of required foreign labels whose
   whole `J`-portal set is the singleton `{x}`.  Target exclusion forces

   \[
     |\Omega_x\cap\{B,C,U_j:j\ne i\}|\ge2.              \tag{3.2}
   \]

#### Proof

If `J=P` and `x` met all six members of the displayed `K_6` model, then
`{x}` together with those six bags would be seven pairwise adjacent
connected branch sets, giving a `K_7` minor.

If `J` is `B` or `C`, exactness says that `P` is anticomplete to all of
`J`, so in particular to `x`.

Now let `J=U_i`.  A foreign bag missed by `x` gives the conclusion by
Corollary 2.2, so suppose that `x` meets all six.  Split `J` into `{x}` and
`J-x`, and retain the other five members of the `K_6` model.  Those five
bags are pairwise adjacent, and `{x}` meets all of them.  The residual bag
`J-x` misses exactly the clique labels in the intersection displayed in
(3.2).  If that intersection had order at most one, these seven sets would
form a `K_7^-` model.  This proves (3.2). `\square`

The proposition deliberately requires a nonempty connected complement.
If `J-x` is disconnected, target exclusion does not by itself put
`J-A` and the portal set of one missed label in the same component of
`J-x`.  If `J={x}=U_i` is a singleton universal bag, the model itself makes
`x` adjacent to all six foreign labels and there is neither a proper bag
subside nor a missed named bag.  Even when `J-x` is connected, the sole
far-bag failure is now exact: `x` is in a universal bag, meets all six
foreign bags, and monopolises at least two of its five clique adjacencies.

### Proposition 3.2 (what the common adjacency to `u,v` buys)

Assume in addition that every vertex of `A` is adjacent to both `u` and
`v`, and that `uv` is an edge.  Let `K_1,...,K_4` be four bags of the
displayed `K_6` model which avoid `u,v,x`.  If

\[
             A\cap K_j\ne\varnothing
       \quad\hbox{and}\quad
             N_G(x)\cap K_j\ne\varnothing
       \qquad(1\le j\le4),                             \tag{3.3}
\]

then `G` contains a `K_7` minor.

#### Proof

The seven sets

\[
                     \{u\},\{v\},\{x\},K_1,K_2,K_3,K_4 \tag{3.4}
\]

are disjoint and connected.  The four model bags are pairwise adjacent.
The vertices `u,v,x` form a triangle, each of `u,v` meets every `K_j`
through a vertex of `A cap K_j`, and `x` meets every `K_j` by (3.3).
Thus (3.4) is a `K_7` model. `\square`

In the dominated-singleton application one has

\[
                         A\subseteq N_G(u)\cap N_G(v).  \tag{3.5}
\]

Moreover the fixed bag which is anticomplete to `u` is disjoint from `A`.
Proposition 3.2 therefore rules out any placement in which four available
clique bags are simultaneously met by `A` and by `x`.  It does not force a
far bag to be anticomplete to an arbitrary subset of `A`: a bag disjoint
from `A` may still have edges to every candidate subset.  Nor does it apply
when the labels containing `u` and `v` leave fewer than four disjoint
clique bags.  Thus the common adjacency sharpens, but does not remove, the
portal co-location obstruction.

### Proposition 3.3 (exhausting unprotected component transfers)

Let `H` be the common edge-deleted graph in which the exact model is fixed,
and retain one label `J` containing `x`.  Among all labelled exact models in
`H` with `x` in the `J`-bag, choose one with `|J|` minimum.  For a component
`C` of `H[J-x]`, let `Omega_J(C)` be the set of required foreign labels
whose entire `J`-portal set in `H` lies in `C`.  If `G` has no `K_7^-`
minor, then

\[
                           |\Omega_J(C)|\ge2             \tag{3.6}
\]

for every such component.  The sets `Omega_J(C)` are pairwise disjoint.
Consequently `H[J-x]` has at most two components when `J=P,B`, or `C`, and
at most three components when `J=U_i`.

#### Proof

The set `J-C` is connected: it consists of `x` and every other component
of `H[J-x]`, each of which has an edge to `x`.  If `Omega_J(C)` is empty,
omit `C` from the model.  Every required adjacency at `J-C` survives, so
this gives a smaller `J`-bag, contrary to the choice of the model.

Suppose `Omega_J(C)={L}`.  The required `J-L` adjacency has an edge from
`C` to `L`, because its whole nonempty portal set lies in `C`.  Move `C`
from `J` into `L`.  The enlarged `L`-bag is connected, the cut edge between
`C` and `J-C` restores the `J-L` adjacency, and every other required
adjacency at `J-C` survives.  If the move creates either nominally missing
adjacency of the exact `K_7^vee` model, the resulting seven branch sets
miss at most one edge and give `K_7^-`.  Otherwise they remain an exact
model with a smaller `J`-bag.  Both outcomes contradict the standing
hypotheses.  This proves (3.6).

A nonempty portal set cannot be wholly contained in two disjoint
components, so the monopoly sets are pairwise disjoint.  The label `P` has
four required neighbours, `B,C` have five, and each `U_i` has six.  The
component bounds follow. `\square`

This exhausts every one-component omission or transfer and leaves precisely
multi-owner components.  If the reselected model is required also to keep
`u` in its
original bag and to keep the original `u`-anticomplete bag unchanged, the
component containing `u` and a component whose sole admissible target is
that anticomplete bag must instead be protected.  Thus adding provenance
requirements weakens, rather than strengthens, the component-transfer
normal form.

## 4. The first unsupported inference and smallest repair

Apply the theorem to the aligned dominated-singleton state, with `J` the
fixed-model bag containing the persistent endpoint `x`.  The response and
the fixed model alone do **not** imply item 2 of Theorem 2.1.  After
Proposition 3.1, the first unsupported inference is whether

\[
                            J-A                         \tag{4.1}
\]

and a full foreign portal set `Pi_i` occupy one component of `J-x`.
Likewise, model persistence does not exclude `J={x}=U_i`, or a
co-connected universal bag in which `x` monopolises at least two clique
labels.

Thus the smallest sufficient repair is the following branch-bag statement.

> **Response-sensitive portal co-location.**  In the aligned dominated
> singleton state, either `G` contains a `K_7^-` minor, one boundary
> partition extends through both shores, or the bag `J` containing `x` is
> nonsingleton and there are a foreign label `D_i` and a component `W` of
> `J-x` containing `(J-A) union Pi_i`.

Theorem 2.1 turns its third outcome immediately into the desired
component-to-bag capture, with no further minimisation.  A proof of the
quoted statement must use the second equality response or a branch-set
exchange to co-locate the two sets in (2.1).  An argument using only the
fixed uncoloured model and persistence of `ux` cannot infer that
co-location.

## Dependencies and scope

The aligned response component is supplied by the audited
[`dominated-singleton low-degree completion`](../results/hc7_k7minus_dominated_singleton_low_degree_terminal.md)
together with its high-degree input.  The exact model and its named missing
pair come from the audited
[`eight-coordinate endpoint-visibility theorem`](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md).

The theorem above is computation-free.  It proves an exact bag-topological
criterion and its co-connected special case.  It does not prove portal
co-location in the two residual placements, terminalise the dominated
singleton, prove Conjecture 21, or prove `HC_7`.
