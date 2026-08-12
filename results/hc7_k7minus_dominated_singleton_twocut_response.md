# A dominated singleton exposes a two-cut in its common neighbourhood

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_dominated_singleton_twocut_response_audit.md).
This is a conditional reduction inside the eight-coordinate campaign.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The dominated alternative in the singleton-coordinate theorem is not an
unstructured palette obstruction.  Its common-neighbour graph has a cut of
order at most two.  The two sides of that cut support opposite incident-edge
responses, while the original coordinate participates in an exact
two-colouring switch with every fresh incident edge.

## 1. Setting

Let `G` be seven-connected and seven-chromatic, suppose every proper minor
of `G` is six-colourable, and suppose that `G` has no `K_7^-` minor and no
`K_5` subgraph.  Let

\[
                              e=uv\in E(G),
\]

and assume that `v` is adjacent to every member of `N_G(u)-{v}`.  Put

\[
                     Q=G[N_G(u)-\{v\}],\qquad
                     O=G-N_G[u].                         \tag{1.1}
\]

As proved in the
[singleton-coordinate theorem](hc7_k7minus_singleton_coordinate_localisation.md),

\[
 |V(Q)|\ge7,qquad Q\text{ is triangle-free},\qquad
                         K_5^-\npreccurlyeq Q.            \tag{1.2}
\]

## 2. The common-neighbour cut

### Theorem 2.1 (two-cut and external attachment)

There is a set `S subseteq V(Q)` with `|S|<=2` such that `Q-S` has at
least two components.  If `A` and `B` are distinct components of `Q-S`,
then

\[
 \begin{aligned}
   &N_G(A)=N_{G-\{u,v\}}(A)\mathbin{\dot\cup}\{u,v\},\\
   &|N_{G-\{u,v\}}(A)|\ge5,\\
   &|N_G(A)\cap V(O)|\ge5-|S|,\\
   &|N_G(A)|\ge7.                                      \tag{2.1}
 \end{aligned}
\]

The same assertions hold with `B` in place of `A`.  In particular,
`N_G(A)` and `N_G(B)` are actual separators: each has its named component
on one side and the other named component on the far side.

#### Proof

Wood and Woodall prove that every three-connected `K_5^-`-minor-free graph
is a wheel, the triangular prism, or `K_{3,3}`.  A wheel and the triangular
prism contain triangles, while `K_{3,3}` has six vertices.  Therefore
(1.2) implies that `Q` is not three-connected.  This gives `S,A,B` as
stated (with `S` empty if `Q` is disconnected).

Put `R=G-{u,v}`.  Since `G` is seven-connected, `R` is five-connected.
There is no edge from `A` to `B`, and every neighbour in `Q` of `A` lies
in `S`.  Hence `N_R(A)` separates the nonempty sets `A` and `B` in `R`, so

\[
                             |N_R(A)|\ge5.               \tag{2.2}
\]

Moreover `N_R(A) cap V(Q) subseteq S`, and
`V(R)-V(Q)=V(O)`.  Thus (2.2) gives at least `5-|S|` neighbours of `A`
in `O`.

Every vertex of `A` is adjacent to `u` by the definition of `Q`, and to
`v` by the dominated-edge hypothesis.  Consequently

\[
                         N_G(A)=N_R(A)\mathbin{\dot\cup}\{u,v\},
\]

which proves the remaining assertions.  The proof for `B` is identical.
`\square`

The external-attachment conclusion is essential: the cut of `Q` does not
by itself give a cut of order four in `G`.  Five-connectivity of
`G-{u,v}` forces at least three neighbours outside `N_G[u]` even when
`|S|=2`.

## 3. Exact incident-edge responses on the two sides

### Theorem 3.1 (opposite side responses)

Retain `S,A,B` from Theorem 2.1 and choose `x in A`, `y in B`.  Put

\[
                         f=ux,\qquad g=uy,
             \qquad     L=G-\{f,g\}.                    \tag{3.1}
\]

Then `xy` is not an edge, `chi(L)=6`, and the equality signatures of the
proper six-colourings of `L` on `{f,g}` are exactly

\[
                           \{f\},\qquad\{g\},\qquad\{f,g\}.
                                                               \tag{3.2}
\]

All three colourings give rejected exterior traces on the singleton
`{u}`.  In addition:

1. a signature-`{f}` colouring gives a rejected exterior trace on the
   actual side `A`; and
2. a signature-`{g}` colouring gives a rejected exterior trace on the
   actual side `B`.

Thus the two components behind the common-neighbour cut carry opposite
responses of one common induced two-edge star.

#### Proof

The vertices `x,y` lie in different components of `Q-S`, so `xy` is not
an edge.  The graph `L` is a proper subgraph of `G` and hence is at most
six-colourable.  If it were five-colourable, recolouring `u` with one new
sixth colour and restoring `f,g` would six-colour `G`.  Therefore
`chi(L)=6`.

An empty equality signature would colour `G`.  A proper six-colouring of
`G-f` makes the ends of `f` equal, since otherwise it too would colour
`G`; the present edge `g` has differently coloured ends.  Its restriction
to `L` therefore has signature `{f}`.  Interchanging `f,g` gives
signature `{g}`.  Finally, contract the induced path `x-u-y`, six-colour
the proper minor, and expand its contracted vertex with one colour.  This
gives signature `{f,g}`.  Hence (3.2) is exact.

The singleton `{u}` meets every monochromatic deleted edge in each of the
three signatures.  Restriction outside `{u}` is therefore proper, and any
extension of the induced boundary partition through the closed singleton
side would glue to a six-colouring of `G`.

For a signature-`{f}` colouring, deletion of `A` removes the endpoint
`x` of the sole monochromatic restored edge, while `g` is already proper.
The restriction to `G-A` is consequently proper.  Since `N_G(A)` is an
actual separator, the same gluing argument proves that its boundary
partition is rejected by the closed `A`-side.  The assertion for `B` and
`g` is symmetric. `\square`

## 4. The original coordinate is not lost completely

### Proposition 4.1 (triangle switch with the original edge)

For every `x in V(Q)`, put

\[
                         L_x=G-\{uv,ux\}.               \tag{4.1}
\]

Then `chi(L_x)=6`, and its equality-signature language on
`{uv,ux}` is exactly

\[
                              \{uv\},\qquad\{ux\}.       \tag{4.2}
\]

In particular, if `uv` is the original member of the eight-coordinate
forest, its singleton-signature colouring is one literal corner of this
common two-edge operation.

#### Proof

The same fresh-colour argument as in Theorem 3.1 proves `chi(L_x)=6`.
The empty signature would six-colour `G`.  The signature containing both
edges is impossible because `vx` is present: equality on both deleted
edges would give the same colour to the adjacent vertices `v,x`.
Colourings of `G-uv` and `G-ux` supply the two singleton signatures, as in
the proof of Theorem 3.1. `\square`

### Theorem 4.2 (one model-persistent triangle switch)

Assume in addition that `uv` is the retained forest coordinate and that
`G-uv` contains a spanning labelled exact `K_7^vee` model.  Let `R` be the
branch set containing `u`.  Suppose that

\[
        R=\{u\}\quad\hbox{or}\quad R-u\text{ is connected}.     \tag{4.3}
\]

and that one named foreign branch set `D` is anticomplete to `u`.  Then
some `x in V(Q)` has the following property: deleting `ux` leaves the same
labelled branch sets as an exact `K_7^vee` model in

\[
                            G-\{uv,ux\}.                          \tag{4.4}
\]

Consequently (4.4) simultaneously carries the original exact model, the
original coordinate colouring, and the exact exclusive signature pair
`{uv},{ux}` from Proposition 4.1.

#### Proof

Call `ux`, for `x in V(Q)`, essential if deleting it from `G-uv` destroys
the displayed model with its branch sets fixed.  Only two kinds of failure
are possible.

First suppose `x in R-u`.  By (4.3), deleting `ux` disconnects `R` only
when `ux` is the sole edge from `u` to `R-u`.  There is at most one such
essential edge.

Otherwise `x` belongs to a foreign branch set `J`.  The edge `ux` is
essential only when it is the sole edge between `R` and `J` and the two
labels are required to be adjacent in `K_7^vee`.  There is at most one
such edge for each label adjacent to the label of `R`.

Every label of `K_7^vee` has degree at most six.  If the label of `R` has
degree at most five, the internal possibility and all foreign possibilities
together account for at most six essential edges.  If it has degree six,
all six foreign labels are required, but the named branch set `D` supplies
no edge incident with `u`; again there are at most five essential foreign
edges and at most one essential internal edge.  Thus in every case at most
six of the edges

\[
                              ux\quad(x\in V(Q))
\]

are essential.  Since `|V(Q)|>=7`, one is not.  For that choice of `x`,
the fixed branch sets remain a model after both deletions.  Edge deletion
cannot create either nominally missing adjacency, so the model remains
exact.  Proposition 4.1 supplies the asserted signature pair. `\square`

The theorem is deliberately a one-edge assertion.  It does not guarantee
two jointly persistent edges with nonadjacent outer endpoints, nor that its
chosen endpoint avoids the two-vertex cut `S` from Theorem 2.1.

### Corollary 4.3 (high-degree component alignment)

Under the hypotheses of Theorem 4.2, if `d_G(u)>=10`, then the endpoint
`x` may be chosen outside `S`.  Let `A` be the component of `Q-S`
containing it.  The common graph `G-{uv,ux}` then retains the original
labelled exact model, while its signature-`{ux}` colouring induces a
rejected exterior trace on the actual boundary `N_G(A)`, of order at least
seven.

#### Proof

The proof of Theorem 4.2 bounds the number of essential edges `ux` by six.
Now

\[
                   |V(Q)|=d_G(u)-1\ge9,
\]

so at least three choices of `x` are nonessential.  Since `|S|<=2`, one
lies in a component of `Q-S`.  The model conclusion is Theorem 4.2 and the
response conclusion is the proof of Theorem 3.1. `\square`

## 5. Exact gain and remaining obstruction

The dominated alternative is therefore reduced to the following literal
configuration:

\[
 \boxed{
 \begin{gathered}
 Q\text{ has a cut of order at most two};\\
 \text{each of two components has an actual boundary of order at least seven};\\
 \text{the components carry opposite responses of one common induced }P_3;\\
 \text{and the original edge has an exact exclusive switch with every fresh edge.}
 \end{gathered}}
\]

Theorem 4.2 preserves the original exact model for one triangle switch.
It does not yet preserve that model for the two opposite component edges
in Theorem 3.1: deleting `ux` or `uy` may destroy the connectivity of the
branch set containing `u`, or its unique contact with another named branch
set.  Nor does (2.1) upper-bound either returned boundary.  The smallest
remaining repair is therefore a **two-sided model-persistent choice
theorem**: choose `x in A` and `y in B` so that deleting `ux,uy` preserves
one common labelled exact model, or turn failure of that choice into
`K_7^-` or a smaller model-anchored response side.  The present theorem
supplies the two sides, all colouring responses, and one model-aligned
original-coordinate switch; it does not assert the two-sided choice.

## Primary source

R. G. Wood and D. R. Woodall,
[*Defective Choosability of Graphs without Small Minors*](https://doi.org/10.37236/181),
*Electronic Journal of Combinatorics* **16** (2009), R92,
Lemma 4.2.1.  The cited lemma states exactly that every three-connected
`K_5^-`-minor-free graph is a wheel, the triangular prism, or `K_{3,3}`.
