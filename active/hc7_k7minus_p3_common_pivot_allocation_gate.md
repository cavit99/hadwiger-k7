# The induced path has one common Kempe pivot, but no proved model-label allocation

**Status:** written unbounded lemmas and a recorded route nonclosure;
[separate internal audit GREEN](hc7_k7minus_p3_common_pivot_allocation_gate_audit.md).
This note does not close the induced-path case,
the six-coordinate terminalisation theorem, the `K_7^-` six-colour
conjecture, or `HC_7`.

The induced path differs from two independent selected edges in one useful
respect.  Contracting the whole path gives one colouring in which both path
edges have monochromatic ends.  Every alternate palette in that one
colouring has to connect the centre to at least one of the two leaves.  Thus
the common-pivot quantifier which is missing in the matching case is
automatic here.

This note proves that assertion in the exact live host.  It also records its
limit.  The palette components still have no canonical relation to the five
foreign branch sets of a fixed `K_6`-minor model.

## 1. The two-edge path host

Let `G` be a minor-minimal seven-chromatic graph satisfying

\[
 \kappa(G)\geq7,\qquad K_7^-\npreccurlyeq G,
 \qquad \chi(J)\leq6\quad\hbox{for every proper minor }J\text{ of }G.
                                                               \tag{1.1}
\]

Let

\[
                              x-r-y                              \tag{1.2}
\]

be an induced path.  Put

\[
                 a=rx,\qquad b=ry,\qquad H=G-\{a,b\}.           \tag{1.3}
\]

Assume that both `G-a` and `G-b` are seven-connected.  These hypotheses
hold for the induced path selected in the audited six-coordinate forest
reduction: restoring the four disjoint matching coordinates only adds
edges to each of the two seven-connected one-restorer hosts.

### Theorem 1.1 (path-only common host)

The following statements hold.

1. `H` is six-connected and exactly six-chromatic, and both `H+a` and
   `H+b` are seven-connected.
2. The equality signatures of the proper six-colourings of `H` on
   `\{a,b\}` are exactly

   \[
                         \{a\},\qquad\{b\},\qquad\{a,b\}.       \tag{1.4}
   \]

3. The contraction `G/a/b` is exactly six-chromatic.  Consequently it has
   a spanning `K_6`-minor model; on expansion, one branch set contains the
   whole path `x-r-y`.
4. If `H` is not seven-connected, there is an actual response boundary of
   order seven or eight carrying all three colourings in (1.4).  More
   precisely, a six-cut `T` of `H` yields either

   \[
       N_G(B)=T\mathbin{\dot\cup}\{r\},\quad |N_G(B)|=7,         \tag{1.5}
   \]

   for a connected side `B` containing `x,y`, or

   \[
       N_G(\{r\})=T\mathbin{\dot\cup}\{x,y\},
       \quad d_G(r)=8.                                          \tag{1.6}
   \]

   In either case the opposite open side is nonempty.  Every colouring in
   (1.4) restricts to a proper colouring after the displayed side is
   deleted, and its boundary partition is rejected by the intact side.

#### Proof

Deleting one edge from a seven-connected graph lowers vertex connectivity
by at most one.  Since `H=(G-a)-b`, the graph `H` is six-connected.  The
identities `H+a=G-b` and `H+b=G-a` give the two seven-connected
restorations.

For each nonempty `I\subseteq\{a,b\}`, contract the edges in `I`,
six-colour the resulting proper minor, expand the contracted vertices and
delete both path edges.  The edges in `I` have monochromatic ends.  Every
edge outside `I` remains an edge after the contraction because (1.2) is
induced, so its ends have different colours.  This gives all three
signatures in (1.4).  A colouring with neither pair monochromatic would
remain proper after restoring both edges and would six-colour `G`.

The preceding colourings show `\chi(H)\leq6`.  If `H` had a proper
five-colouring, recolour the two nonadjacent leaves `x,y` with one fresh
sixth colour.  Leaving `r` unchanged then restores both path edges
properly, contrary to `\chi(G)=7`.  Thus `\chi(H)=6`.

The graph `G/a/b` is a proper minor and hence is at most six-chromatic.
If it had a proper five-colouring, expand the contraction image by retaining
its colour at `r` and giving both nonadjacent leaves one fresh sixth colour.
Every outside neighbour of the path avoided the contraction colour, so
this would be a proper six-colouring of `G`.  Hence `\chi(G/a/b)=6`.
The established case `HC_6` supplies a `K_6` model, and unused vertices may
be absorbed to make it spanning.  Expanding the contraction image gives
item 3.

It remains to prove item 4.  Let `T` be a six-cut of `H`.  Adding either
one of `a,b` produces a seven-connected graph, so each restored edge must
join all components of `H-T`.  It follows that `H-T` has exactly two
components.  Write them as `A,B`, with

\[
                         r\in A,\qquad x,y\in B.                 \tag{1.7}
\]

None of the path vertices belongs to `T`, and six-connectivity makes both
components full to `T`.

If `A\ne\{r\}`, then no edge of `G` joins `A-\{r\}` to `B`; the only
edges absent from `H` are `rx,ry`.  Hence (1.5) holds.  The opposite side
`A-\{r\}` is nonempty.  If `A=\{r\}`, then fullness gives
`N_H(r)=T`, proving (1.6).  The component `B` has a vertex other than
`x,y`, because `xy` is not an edge, so the singleton separation is actual.

In (1.5), every nonempty signature in (1.4) has a monochromatic path edge
with its leaf in `B`; in (1.6), every such edge has its centre in `\{r\}`.
Deleting the displayed side therefore removes every monochromatic restored
edge.  The three exterior restrictions are proper.  If any induced boundary
partition extended through the intact side, aligning colour names and
gluing would six-colour `G`.  All three are rejected. `\square`

Thus, once labelled responses of order seven and eight have been
terminalised, the path-only graph `H` itself is seven-connected.  No
opposite matching coordinate is needed for this conclusion.

## 2. The automatic common pivot

Fix a proper six-colouring `phi` of `H` obtained by expanding a colouring
of `G/a/b`.  Write

\[
                       \phi(x)=\phi(r)=\phi(y)=\alpha.           \tag{2.1}
\]

For each colour `beta\ne alpha`, let `C_beta` be the component containing
`r` of the subgraph of `H` induced by the colours `alpha,beta`, and put

\[
             L_\beta=\{z\in\{x,y\}:z\in C_\beta\}.             \tag{2.2}
\]

### Theorem 2.1 (common-pivot palette dichotomy)

For every `beta\ne alpha`, the set `L_beta` is nonempty.  Moreover,
exactly one of the following two alternatives holds.

1. There are distinct colours `beta,gamma\ne alpha` such that

   \[
                         L_\beta=\{x\},\qquad L_\gamma=\{y\}.   \tag{2.3}
   \]

   Switching `C_beta` and `C_gamma` separately gives the two opposite
   singleton signatures from the same literal colouring `phi`.
2. After possibly exchanging `x,y`,

   \[
                             x\in C_\beta
                 \qquad(\beta\ne\alpha).                       \tag{2.4}
   \]

   Thus one fixed centre--leaf pair is joined in all five alternate
   bichromatic graphs of one common colouring.

#### Proof

Fix `beta\ne alpha`.  Suppose that neither leaf lies in `C_beta`.
Interchange `alpha,beta` on the component containing `x` and on the
component containing `y`, counting it only once if those components are
equal.  Neither component contains `r`.  The two leaves change to `beta`
while `r` retains colour `alpha`.  Whole-component interchanges preserve
properness in `H`, and both path edges can now be restored.  This would
six-colour `G`, a contradiction.  Hence `L_beta` is nonempty.

If `L_beta=\{x\}`, switching `C_beta` changes `r,x` together and leaves
`y` unchanged.  The edge `rx` remains monochromatic and `ry` becomes
proper, giving signature `\{a\}`.  The symmetric statement holds for
`L_gamma=\{y\}`.  This proves the last assertion in outcome 1.

Suppose outcome 1 does not hold.  If a singleton set occurs among the
`L_beta`, exchange the leaf names so that it is `\{x\}`.  No `L_gamma`
can then equal `\{y\}`, while every `L_gamma` is nonempty.  Hence every
`L_gamma` contains `x`.  If no singleton occurs, every `L_beta` equals
`\{x,y\}`.  In both cases (2.4) follows. `\square`

The theorem removes the first quantifier problem present for two independent
edges.  One does not have to assume the existence of a shared double-equality
pivot: the common path contraction supplies it.

## 3. What a pivot component returns

### Proposition 3.1 (response or dominating palette component)

For every `beta\ne alpha`, the graph `G[C_beta]` is three-colourable.
If `C_beta` is not dominating, then `N_G(C_beta)` is an actual response
boundary of order at least seven carrying the restriction of `phi`.

If `L_beta` is a singleton, the component switch from Theorem 2.1 agrees
with `phi` outside `C_beta` and supplies the opposite singleton response on
the same exterior boundary partition.  If `C_beta` is dominating, then

\[
       4\leq\chi(G-C_\beta)\leq5,
       \qquad K_6\npreccurlyeq G-C_\beta.                       \tag{3.1}
\]

If `L_beta=\{x,y\}`, the sharper identity

\[
                         \chi(G-C_\beta)=4                       \tag{3.2}
\]

holds.

#### Proof

The graph `H[C_beta]` is bipartite.  The only edges of `G-H` with both
ends in `C_beta` are one or both of `rx,ry`.  Recolouring `r` with a third
colour therefore gives a proper three-colouring of `G[C_beta]`.

Every monochromatic omitted edge under `phi` has an end in `C_beta`, since
`r\in C_beta`.  Hence `phi` restricts to a proper colouring of
`G-C_beta`.  If the component is not dominating, its neighbourhood is an
actual separator, of order at least seven by (1.1).  The usual
alignment-and-gluing argument shows that its exterior boundary partition
is rejected by the intact component side.  For a singleton `L_beta`, the
switch in Theorem 2.1 changes no vertex outside `C_beta`, proving the
additional response assertion.

Now suppose that `C_beta` dominates.  A three-colouring of `G-C_beta`,
together with the proved three-colouring of `G[C_beta]` on a disjoint
palette, would six-colour `G`.  Thus `\chi(G-C_beta)\geq4`.  The colouring
`phi` uses at most five colours outside `C_beta`: a vertex outside the
component coloured `alpha` or `beta` can be adjacent to it only through
the one omitted path edge whose leaf is outside.  This proves the upper
bound in (3.1).

A `K_6` model in `G-C_beta`, completed by the connected dominating set
`C_beta`, would give a `K_7` model in `G`.  This proves the minor exclusion
in (3.1).  Finally, if both leaves belong to `C_beta`, neither omitted edge
leaves the component.  Domination then forbids every outside vertex of
colour `alpha` or `beta`, since its edge into `C_beta` would belong to `H`
and join the bichromatic component.  Thus `phi` uses at most the other four
colours outside, proving (3.2). `\square`

The target-free terminal obstruction is consequently very rigid.  Either
an actual response separator is returned, or one common double-contraction
colouring gives two opposite dominating response components, or gives one
leaf joined to the centre in all five palettes.  A palette component which
contains both leaves is a connected dominating three-colourable subgraph
with an exactly four-chromatic `K_6`-minor-free complement.

## 4. Exact model-allocation nonclosure

Lift a spanning `K_6` model of `G/a/b`, let `R` be its branch set containing
`x,r,y`, and split it into connected pieces

\[
                         R_x\mathbin{\dot\cup}R_r
                              \mathbin{\dot\cup}R_y              \tag{4.1}
\]

containing the three path vertices and retaining the two path adjacencies.
Four foreign bags adjacent to all three pieces would give an explicit
`K_7^-` model.  Theorems 1.1--2.1 do not force that allocation.

The obstruction is now exact.

* The full response square does not imply that one common pivot has both
  singleton orientations in (2.3).  Singleton signatures may be realised
  by colourings in unrelated Kempe components.  Outcome 2 of Theorem 2.1
  is compatible with all presently proved colouring data.
* Even in outcome 1, `C_beta` and `C_gamma` are colour-defined connected
  subgraphs, not branch bags.  They may traverse the same foreign bags,
  meet only bags which already contact the relevant split pieces, or have
  all useful interaction inside `R`.  Their common vertex `r` does not
  assign either component to a deficient foreign label.
* A non-dominating pivot component gives an actual separator, but the proof
  supplies only the lower bound `|N_G(C_beta)|\geq7`.  It gives no upper
  bound of eight.  A dominating pivot component gives (3.1)--(3.2), not a
  model-label incidence.

Thus the first unsupported implication is

\[
 \begin{gathered}
 H\text{ seven-connected},\quad
 \Sigma_{\{a,b\}}(\operatorname{Col}_6H)
       =\{\{a\},\{b\},\{a,b\}\},\\
 \text{one common pivot satisfying Theorem 2.1},\quad
 \text{one co-bagged spanning }K_6\text{ model}
 \end{gathered}
 \quad\Longrightarrow\quad
 \begin{gathered}
 \text{four foreign bags meet all three pieces, or}\\
 \text{a common boundary partition, or an order-seven/eight response.}
 \end{gathered}                                                \tag{4.2}
\]

No result in the repository proves (4.2).  This is a route nonclosure, not
a counterexample to a response-sensitive path theorem.

The smallest repair is a **deficiency-aware common-pivot exchange theorem**:
for a fixed co-bagged model maximising the number of triple-contacting
foreign bags, a pivot component from Theorem 2.1 must either support a legal
branch-set reassignment which increases that number, have an actual boundary
of order seven or eight retaining its singleton response, or induce a
partition accepted by both relevant closed sides.  If every pivot component
is dominating, the repair must instead turn the exact four-chromatic
complements in (3.2), or the two opposite dominating components in outcome
1, into the same branch-set reassignment.  Static contact profiles and the
existence of further unlabelled paths do not supply this conclusion.

## Dependencies and scope

The live application comes from the audited
[six-coordinate forest reduction](../results/hc7_k7minus_six_coordinate_forest_reduction.md)
and complements the audited
[opposite-coordinate common-model theorem](../results/hc7_k7minus_p3_opposite_coordinate_common_model.md).
The proof uses the established case `HC_6`, due to Robertson, Seymour and
Thomas.  It is unbounded and computation-free.
