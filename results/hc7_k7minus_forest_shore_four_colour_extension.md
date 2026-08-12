# Four boundary colours always extend through a forest shore

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_forest_shore_four_colour_extension_audit.md).
This is an unbounded colouring lemma and a terminal elimination of the
full order-seven forest-shore outcome in the bounded-feedback branch.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## Lemma 1 (forest-shore extension)

Let

\[
 V(G)=Y\mathbin{\dot\cup}S\mathbin{\dot\cup}D,
 \qquad E_G(Y,D)=\varnothing,                              \tag{1.1}
\]

where `G[Y]` is a forest.  Every proper colouring of `G[S]` which uses at
most four colours extends to a proper six-colouring of `G[Y union S]`.

Consequently, if the same boundary colouring extends to a six-colouring
of `G[D union S]`, then `G` is six-colourable.

### Proof

Choose two colours from the six-colour palette which do not occur on `S`.
Every forest is bipartite, so colour `G[Y]` with those two colours.  No
edge from `Y` to `S` is monochromatic because neither new colour occurs
on `S`.  This proves the first assertion.  The two closed-shore
colourings agree on `S` and glue across (1.1), proving the second.
`\square`

The same proof works with `q` colours whenever the boundary uses at most
`q-2` colours.

## Corollary 2 (exact residue at a full forest seven-cut)

Assume that `G` is seven-connected, is not six-colourable, and every
proper minor of `G` is six-colourable.  Let `S` be a seven-vertex cut and
let `Y` be a component of `G-S` such that `G[Y]` is a tree.  Then every
proper six-colouring of `G-Y` uses at least five colours on `S`.

If, in addition, `G` has no `K_7^-` minor, then `G-S` has exactly two
components.  Thus this statement applies directly to the exact
order-seven separation returned by the forest-component reduction: its
forest side accepts every proper boundary partition with at most four
blocks, while every colouring of the unique opposite closed shore has a
five- or six-block boundary partition.

### Proof

The graph `G-Y` is a proper subgraph and hence has a proper six-colouring.
If one such colouring used at most four colours on `S`, Lemma 1 would
extend its literal boundary colouring through `Y`, and the two colourings
would glue to a six-colouring of `G`, a contradiction.

The assertion that an order-seven cut leaves exactly two components is
the separately audited three-component seven-cut exclusion for the
critical `K_7^-`-minor-free host. `\square`

## Theorem 3 (disjoint boundary-block carriers close the cut)

Retain (1.1), assume that `G[Y]` is connected, and suppose every proper
minor of `G` is six-colourable.  Let

\[
                         P_1,\ldots,P_r\subseteq S             \tag{3.1}
\]

be pairwise disjoint nonempty independent sets.  Suppose there are
pairwise vertex-disjoint nonempty connected sets

\[
                         K_1,\ldots,K_r\subseteq Y              \tag{3.2}
\]

such that `K_i` is adjacent to every literal vertex of `P_i`.  If

\[
              r+\left|S-\bigcup_{i=1}^rP_i\right|\le4,         \tag{3.3}
\]

then `G` is six-colourable.

### Proof

For each `i`, the set `K_i union P_i` is connected.  Contract a spanning
tree of each of these pairwise disjoint sets.  At least one edge is
contracted, so the resulting graph is a proper minor and has a proper
six-colouring.

Keep that colouring on `D` and on the boundary vertices outside the sets
`P_i`.  Give every vertex of `P_i` the colour of the contracted image of
`K_i union P_i`.  This gives a proper colouring of `G[D union S]`:
`P_i` is independent, and every edge from `P_i` to a retained vertex is
represented by an edge incident with the corresponding contracted image.

Its restriction to `S` uses at most the number in (3.3): one colour for
each contracted block and at most one further colour for every untouched
boundary vertex.  Lemma 1 extends this same literal boundary colouring
through the forest side.  The two closed-shore colourings then glue to a
six-colouring of `G`. `\square`

For an order-seven boundary, condition (3.3) is equivalently

\[
                         \sum_{i=1}^r(|P_i|-1)\ge3.             \tag{3.4}
\]

Thus a proper four-colouring of `G[S]` closes the separation as soon as
the non-singleton colour classes admit pairwise disjoint connected
carriers in the tree side.  For example, three disjoint carriers for the
three pairs in a `2,2,2,1` partition are terminal.

## Theorem 4 (a full order-seven cut has no forest component)

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\le6\text{ for every proper minor }J,
 \qquad \kappa(G)\ge7,\qquad \delta(G)\ge8,
 \qquad K_7^-\npreccurlyeq G.                              \tag{4.1}
\]

Then no seven-vertex cut `S` has a component `Y` of `G-S` for which
`G[Y]` is a tree.

### Proof

Suppose such `S,Y` exist.  Seven-connectivity makes every component of
`G-S` adjacent to every literal vertex of `S`.

The tree `G[Y]` is not a singleton: a singleton component would have
degree at most seven, contrary to `delta(G)>=8`.  Let `u,v` be two
distinct leaves.  Every neighbour of a leaf outside its unique tree
neighbour lies in `S`.  Hence minimum degree eight and `|S|=7` force

\[
                         N_G(u)\cap S=N_G(v)\cap S=S.           \tag{4.2}
\]

Thus the singleton connected subgraphs `{u},{v}` are both full at `S`.
Any component `D ne Y` of `G-S` is a third disjoint connected subgraph
full at `S`.  Consequently the full-connected-subgraph packing number
satisfies `pi_S(G)>=3`.  The audited critical seven-cut capacity theorem
gives `pi_S(G)<=3`; hence

\[
                         \pi_S(G)=3,
                         \qquad |E(G[S])|\le9.                 \tag{4.3}
\]

We next show that `alpha(G[S])<=2`.  Suppose instead that `I subseteq S`
is an independent triple.  If `G[S-I]=K_4`, use the four clique vertices
as singleton branch sets.  Assign the three vertices of `I` bijectively
to `{u},{v},D` and enlarge each full connected subgraph by its assigned
boundary vertex.  The resulting seven connected sets are pairwise
adjacent and form a `K_7`-minor model.

Otherwise `G[S-I]` is three-colourable, since it has four vertices and is
not `K_4`.  Some colour class `P subseteq S-I` has order at least two.
Use `{u}` and `{v}` as the two disjoint carriers in Theorem 3 for the
independent blocks `I,P`.  Since

\[
                 2+|S-(I\cup P)|\le2+(7-3-2)=4,               \tag{4.4}
\]

that theorem six-colours `G`, a contradiction.  Both alternatives are
impossible, proving `alpha(G[S])<=2`.

The complement of `G[S]` is therefore triangle-free.  Mantel's theorem
and (4.3) give

\[
 |E(\overline{G[S]})|\le12,
 \qquad
 |E(\overline{G[S]})|=21-|E(G[S])|\ge12.                      \tag{4.5}
\]

Equality holds.  The equality case of Mantel's theorem on seven vertices
is `K_{3,4}`.  Hence

\[
                             G[S]=K_3\mathbin{\dot\cup}K_4.    \tag{4.6}
\]

The literal `K_4` in (4.6), together with the other three boundary
vertices assigned to `{u},{v},D` exactly as above, gives a `K_7` minor.
This final contradiction proves the theorem. `\square`

### Consequence for the bounded-feedback branch

The exact order-seven-separation outcome of the forest-component
reduction is impossible: its displayed side is a connected subgraph of
the feedback forest and is a component after deleting its seven-vertex
boundary.  Thus that entire outcome is terminally eliminated, with no
colour-partition synchronisation assumption.

## Scope

Theorem 4 closes the full order-seven forest-shore case completely.  The
intermediate extension and carrier lemmas are retained because their two
leaf carriers are the mechanism that turns a large independent boundary
set into the contradiction.

The six matching-edge signature colourings do not automatically close
this residue.  A signature colouring restricts properly to the opposite
shore only when all of its monochromatic deleted edges avoid that shore;
even then its boundary trace may use five or six colours.  A terminal use
of the common response cube must force one legal opposite-shore trace with
at most four boundary blocks, or use a five-/six-block trace to construct
the forbidden minor.
