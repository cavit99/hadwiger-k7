# Deleting the exceptional centre and lifting every six-separation at the connected remote interface

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_connected_full_remote_pole_core_audit.md).
The
theorem replaces the connected-full order-eight case by one six-connected
common host carrying the whole labelled deletion cube, and classifies every
possible loss of seven-connectivity in that host.  The final seven-connected
core, the overlapping order-eight separations and the boundary-contained
exact-seven case
are not claimed terminal.  In particular, this note does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

Throughout, `K_7^\vee` denotes `K_7` with two incident edges deleted.

## 1. Connected-full setting

Let `G` satisfy

\[
 \begin{gathered}
  \chi(G)=7,
  \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,\\
  \kappa(G)\ge7,
  \qquad \delta(G)\ge8,
  \qquad |E(G)|\ge4|V(G)|,
  \qquad |V(G)|\ge25,\\
  K_7^-\npreccurlyeq G.
 \end{gathered}                                      \tag{1.1}
\]

Fix a degree-eight vertex `z`, put

\[
                         X=N_G(z),\qquad |X|=8,       \tag{1.2}
\]

and fix an independent triple

\[
                         I=\{x_1,x_2,x_3\}\subseteq X.           \tag{1.3}
\]

Assume that the connected-full case of the audited
[remote-interface topological reduction](../results/hc7_k7minus_remote_interface_topological_reduction.md)
holds.  Thus

\[
                 C=G-N_G[z]\text{ is connected},
                 \qquad N_G(C)=X.                    \tag{1.4}
\]

Let `f=uv\in E(C)` be the named remote edge from the audited
[remote-edge operation cube](../results/hc7_k7minus_remote_removable_edge_operation_cube.md),
so that `G-f` is seven-connected.  Put

\[
 T=\{zx_1,zx_2,zx_3,f\},
 \qquad H=G-T.                                      \tag{1.5}
\]

For every nonempty `J\subseteq T`, fix a proper six-colouring `c_J` of
`H` whose exact equality signature on `T` is `J`.  Thus, after all four
edges are restored, precisely the edges in `J` are monochromatic.  The
original theorem also supplies all eighty nontrivial keep/delete/contract
patterns and a fixed spanning exact `K_7^\vee` model in `H`.

## 2. Why the existing order-eight routes do not compose directly

Before changing the host, there are three precise obstructions to simply
feeding (1.1)--(1.5) into the existing order-eight machinery.

1. The audited
   [operation-coupled order-eight response theorem](../results/hc7_operation_coupled_order8_response.md)
   applies to a selected edge crossing from `X` into one of the two full
   open components.  The named remote edge `f`, however, is internal to
   `C`, and the theorem's Hall obstruction does not retain its equality
   bit.  Splitting `C` into two full subgraphs does not create a third open
   component to which the componentwise proof can be applied: the explicit
   [common-portal barrier](../barriers/hc7_order8_connected_shore_common_portal_barrier.md)
   shows that this particular substitution, which simply treats an
   internal split as a surrogate for a separate full component, loses the
   intact-shore colouring conclusion.  It does not rule out every possible
   use of a split of `C`.
2. Applying the audited
   [arbitrary-edge response star](../results/hc7_order8_arbitrary_edge_response_star.md)
   to an edge inside a connected operated shore preserves the first
   neighbours of five Kempe paths, but not their intermediate column
   labels.  The
   [dirty-path uncrossing barrier](../barriers/hc7_degree8_dirty_path_local_uncrossing_barrier.md)
   and the
   [coupled Hall-tableau barrier](../barriers/hc7_order8_coupled_response_hall_tableau_barrier.md)
   rule out the two generic local repairs.  The exact remaining obligation
   is recorded in the
   [low-degree response-column frontier](../active/hc7_order8_low_degree_response_column_frontier.md#6-exact-open-theorem).
3. The finite order-eight boundary classifications with three full
   components do not apply to the two-component case (1.4).  Neither the
   colours of a response nor the bags of the fixed exact model come with a
   canonical label matching, so no such matching is assumed below.

The next theorem avoids all three inferences.  It deletes the centre and the
remote edge, so every signature becomes a proper colouring of one common
host.  The colour formerly assigned to the deleted centre is retained only
as a label.

## 3. The common centre-deletion graph

Define

\[
                           K=G-z-f.                  \tag{3.1}
\]

### Theorem 3.1 (six-connected exact core and pointed cube)

The graph `K` has all of the following properties.

1. **Exact common host.**

   \[
    \kappa(K)\ge6,
    \qquad \delta(K)\ge7,
    \qquad \chi(K)=6,
    \qquad K_7^-\npreccurlyeq K,                     \tag{3.2}
   \]

   and, writing `N=|V(K)|=|V(G)|-1`,

   \[
                       |E(K)|\ge4N-5.                \tag{3.3}
   \]

   The literal boundary is nevertheless four-colourable:

   \[
                              \chi(K[X])\le4.         \tag{3.3A}
   \]

2. **A second exact near-clique model.**  The common host `K` has a
   spanning exact `K_7^\vee` model.  That model remains exact after `f` is
   restored in `G-z`.  This model need not have the same branch sets as
   the fixed model in `H`.

3. **Full pointed signature cube.**  For nonempty `J\subseteq T`, let

   \[
        \varphi_J=c_J|_K,
        \qquad \gamma_J=c_J(z),
        \qquad A_J=\{x\in X:\varphi_J(x)=\gamma_J\},
        \qquad \varepsilon_J=[\varphi_J(u)=\varphi_J(v)].        \tag{3.4}
   \]

   Each `\varphi_J` is a proper six-colouring of the **same** graph `K`,
   and

   \[
      (A_J,\varepsilon_J)
       =\bigl(\{x_i:zx_i\in J\},[f\in J]\bigr).       \tag{3.5}
   \]

   Consequently these pointed colourings realise exactly the fifteen
   signatures

   \[
          \{(A,\varepsilon):A\subseteq I,
                    \ \varepsilon\in\{0,1\}\}
                    -\{(\varnothing,0)\}.            \tag{3.6}
   \]

   In particular, for every nonempty `A\subseteq I`, the same exact
   deleted-centre colour
   trace `A` occurs with both statuses of the remote edge.

4. **Universal palette/equality constraint.**  Every proper six-colouring
   `\varphi` of `K` satisfies

   \[
        \varphi(u)\ne\varphi(v)
        \quad\Longrightarrow\quad
        |\varphi(X)|=6.                              \tag{3.7}
   \]

   Equivalently, if a colour is absent from `X`, then `u` and `v` have the
   same colour.  The pointed cube exhibits two distinct patterns covered
   by this implication: every pure nonempty star signature has `u,v`
   different and uses all six colours on `X`, while the `f`-only signature
   has `u,v` equal and uses at most five colours on `X`.  Thus an
   intrinsically four-colourable
   boundary is forced to use all six colours in every `f`-proper extension
   through `K`.

5. **Numerical separation of the original response languages.**  Let
   `\pi_A` be the partition of `X` induced by the pure star signature
   `A`, and let `\rho` be that induced by the `f`-only signature.  Then
   every `\pi_A`
   has exactly six blocks, whereas `\rho` has at most five.  More
   precisely,

   \[
   \begin{array}{c|c}
   |A|&\text{block shape of }\pi_A\\
   \hline
   3&3+1+1+1+1+1,\\
   2&2+2+1+1+1+1,\\
   1&3+1+1+1+1+1\text{ or }2+2+1+1+1+1.
   \end{array}                                      \tag{3.8}
   \]

   The block `A` in each line is the exact deleted-centre-colour block.
   Thus the
   centre-star and remote-edge response families are disjoint for the
   stronger reason `6` blocks versus at most `5`, not merely by an
   abstract gluing contradiction.

### Proof

Put `L=G-f`.  By choice of `f`, the graph `L` is seven-connected, and
`K=L-z`; hence `K` is six-connected.  A vertex of `K` loses at most one
incident edge from `G`: vertices of `X` lose their edge to `z`, the
vertices `u,v` lose `f`, and these two classes are disjoint because
`f\subseteq C`.  Therefore `\delta(K)\ge7`.

The graph `K` is a proper minor of `G`, so `\chi(K)\le6`.  Suppose it had
a proper five-colouring.  If `u,v` had different colours, restore `f` and
give `z` a fresh sixth colour.  If they had the same colour, recolour `u`
and `z` with that same fresh sixth colour and restore `f`.  The vertices
`u,z` are nonadjacent because `u\in C`, and no other vertex initially has
the fresh colour.  Either case gives a proper six-colouring of `G`, a
contradiction.  Thus `\chi(K)=6`.  Target exclusion descends to the minor
`K`.

Deleting `z` and the remote edge removes exactly nine edges, so

\[
 |E(K)|=|E(G)|-9
       \ge4|V(G)|-9
       =4|V(K)|-5,                                  \tag{3.9}
\]

which proves (3.3).

If `K[X]=G[X]` had a `K_5` model, its five branch sets together with the
connected `X`-full set `C` and the singleton `{z}` would form a
`K_7^-` model in `G`; the only possibly missing contact is `Cz`.  Hence
`K[X]` is `K_5`-minor-free, and the established case `HC_5` proves
(3.3A).

The graph `K` is four-connected, has order at least twenty-four, and its
density in (3.3) is above `4N-8`.  Norin--Totschnig, Theorem 6, therefore
supplies a `K_7^\vee` model; its eight-vertex exception
`K_{2,2,2,2}` is impossible.  Enlarge the model to span `K`.  If either
nominally missing bag pair had a contact in `K`, the bags would give a
`K_7^-` model.  The same argument after restoring `f` proves exactness in
`G-z`.

Since

\[
                              H-z=G-z-f=K,             \tag{3.10}
\]

each `c_J` restricts properly to `K`.  The edges from `z` to `X-I` are
kept in `H`, while the equality signature on the three deleted star edges
and on `f` is exact.  This proves (3.5), and the nonempty subsets of the
four-edge set `T` give precisely (3.6).

For (3.7), let `\varphi` be a proper six-colouring of `K` with
`\varphi(u)\ne\varphi(v)`.  If some palette colour were absent from `X`,
give that colour to `z` and restore `f`.  This would be a proper
six-colouring of `G`, a contradiction.  Thus all six colours occur on
`X`.  In the pure star signatures `f` is proper, so (3.7) applies.  In the
`f`-only signature the deleted-centre colour `\gamma_{\{f\}}` is absent
from `X` by
(3.5), so at most five colours occur there.

Finally, in a pure star signature the deleted-centre-colour block on `X`
is exactly
`A`, and the preceding paragraph gives six blocks on eight vertices.
Distributing the remaining excess `8-6=2` outside that prescribed block
gives exactly the three lines in (3.8).  The `f`-only block count was just
proved.  This completes the theorem. `\square`

## 4. Every six-cut lifts with its operation label

Theorem 3.1 leaves only the possible drop from seven- to six-connectivity.
The following theorem classifies that drop without choosing a model bag or
a palette-to-boundary alignment.

### Theorem 4.1 (operation-labelled six-cut lift)

Either `K` is seven-connected, or let `S` be any six-vertex cut of `K`
and let

\[
                      D_1,\ldots,D_r                 \tag{4.1}
\]

be the components of `K-S`.  Then:

\[
 r\in\{2,3\},
 \qquad N_K(D_i)=S,
 \qquad |D_i|\ge2,
 \qquad D_i\cap(X-S)\ne\varnothing                 \tag{4.2}
\]

for every `i`.  In particular,

\[
                         |S\cap X|\le8-r.            \tag{4.2A}
\]

Moreover

\[
 \begin{array}{c|c}
 r&\text{boundary sparsity in }K[S]\\
 \hline
 2&\text{every five vertices span at most eight edges and }
      |E(K[S])|\le12,\\
 3&\text{every four vertices span at most four edges, }
      \Delta(K[S])\le3,\ |E(K[S])|\le10.
 \end{array}                                        \tag{4.3}
\]

If `|E(G)|\ge4|V(G)|+3`, the last bounds improve to `11` and `8`,
respectively.

For this fixed `S`, exactly one of the following three lift types occurs.

1. **Operation-labelled exact-seven response.**  The set

   \[
                              Q=S\cup\{z\}            \tag{4.4}
   \]

   is an order-seven cut of `G`, and `G-Q` has exactly two components,
   both full at `Q`.  There is a named edge `e\in T` and one of the two
   open components `A` such that `e` has an end in `A` and is absent from
   the opposite closed shore.  The singleton-signature colouring
   `c_{\{e\}}` restricts properly to that opposite closed shore, and its
   equality partition on `Q` is rejected by the intact `A`-shore.

   This lift always occurs when `r=3`; then `f` joins two of the three
   components in (4.1), the joined union is `A`, and one may take `e=f`.
   It also occurs when `r=2`, `f` does not join `D_1` to `D_2`, and the
   four operation edges are not all contained in `G[Q]`.

2. **Two overlapping remote-edge order-eight separations.**  Here `r=2`
   and, after
   relabelling,

   \[
                         u\in D_1,\qquad v\in D_2.    \tag{4.5}
   \]

   The two selected shores have exact order-eight neighbourhoods

   \[
      Q_1=N_G(D_1)=S\cup\{z,v\},
      \qquad
      Q_2=N_G(D_2)=S\cup\{z,u\}.                    \tag{4.6}
   \]

   Both are actual cuts, each selected component is full at its displayed
   boundary, and

   \[
                    Q_1\cap Q_2=S\cup\{z\}.          \tag{4.7}
   \]

   The one fixed `f`-only colouring gives both orientations at once:
   `c_{\{f\}}|_{G-D_i}` is proper, and its partition on `Q_i` is rejected
   by the intact `D_i`-shore, for `i=1,2`.

3. **Boundary-contained exact-seven cut.**  Here `r=2`, the edge `f` does
   not
   join `D_1` to `D_2`, and

   \[
             S=I\mathbin{\dot\cup}\{u,v\}
                    \mathbin{\dot\cup}\{s\}        \tag{4.8}
   \]

   for one vertex `s\notin I\cup\{u,v\}`.  The set `Q=S\cup\{z\}` is an
   order-seven cut with exactly two full complementary components, but
   all four named operation edges lie inside `G[Q]`.  Consequently every
   nonempty signature has a monochromatic restored edge already on the
   common boundary: none of the fifteen fixed signature colourings
   restricts properly to either intact closed shore after `T` is restored.

   Necessarily `s\in X\cup C`, so this residue has

   \[
       (|S\cap X|,|X-S|)\in\{(3,5),(4,4)\}.          \tag{4.8A}
   \]

   This is the unique way in which a six-cut of `K` can return an
   order-seven cut while trapping every original operation label.

### Proof

Apply the audited
[six-cut localisation theorem](../results/hc7_k7minus_exact_six_cut_localisation.md)
to `K`.  Theorem 3.1 supplies six-connectivity and target exclusion, so it
gives `r\in\{2,3\}`, fullness and (4.3).  A singleton component would
have precisely its six neighbours in `S`, contrary to `\delta(K)\ge7`;
hence `|D_i|\ge2`.

The graph `G-f` is obtained from `K` by adding `z` with neighbourhood
`X`.  It is seven-connected.  If some `D_i` missed `X-S`, that component
would remain separated after deleting the six vertices of `S` from
`G-f`.  Therefore every `D_i` meets `X-S`, proving (4.2).  The
intersections are disjoint for distinct components, so
`r\le|X-S|=8-|S\cap X|`, which is (4.2A).  If the surplus
of `G` over `4|V(G)|` is at least three, (3.9) gives
`|E(K)|\ge4|V(K)|-2`, and the sharpened conclusion of the same localisation
theorem gives the last assertion of (4.3).

Delete `Q=S\cup\{z\}` from `G`.  The resulting graph is obtained from
`K-S` by restoring the single edge `f`.  If `r=3`, the set `Q` is
certainly a cut.  The audited
[three-component seven-cut exclusion](../results/hc7_k7minus_three_component_seven_cut_exclusion.md#corollary-2-two-component-normal-form-in-the-critical-host)
says that `G-Q` has exactly two components.  Hence both ends of `f` lie
outside `S` and in two distinct members, say `D_1,D_2`, of (4.1); `f`
merges those two and leaves `D_3` as the other component.  Seven-
connectivity makes both resulting components full at `Q`.

Restore `T` in the colouring `c_{\{f\}}`.  Its sole monochromatic edge is
`f`, which lies in the merged open component.  The restriction to
`G[D_3\cup Q]` is therefore proper.  If its equality partition on `Q`
extended through the intact merged shore, align colour names on the
boundary and glue.  This would six-colour `G`.  Thus the partition is
rejected, proving outcome 1 when `r=3`.

Now let `r=2`.  If `f` has one end in each of `D_1,D_2`, restoring it
makes `G-Q` connected.  For `D_1`, fullness in `K`, the fact that
`D_1\cap X\ne\varnothing`, and the edge `uv` give

\[
                         N_G(D_1)=S\cup\{z,v\},       \tag{4.9}
\]

and symmetrically for `D_2`.  The components are nonsingleton, so deleting
the opposite endpoint does not exhaust the opposite open shore; both
sets in (4.6) are actual cuts.  Restoring `T` in `c_{\{f\}}` creates only
the conflict `uv`.  Deleting either `D_i` removes one end of that conflict,
so `c_{\{f\}}|_{G-D_i}` is proper.  An extension through the intact
selected shore would again glue to a six-colouring of `G`.  This proves
(4.6)--(4.7) and the two labelled nonextension statements.

This proves outcome 2.

It remains that `r=2` and `f` does not join the two components.  Then `Q`
is an order-seven cut, and the critical seven-cut theorem gives exactly
the two full components `D_1,D_2`.  If `V(f)\nsubseteq S`, the edge `f`
has an end in one open component and is absent from the opposite closed
shore; take `e=f`.  If `V(f)\subseteq S` but `I\nsubseteq S`, choose
`x_i\in I-S` and take `e=zx_i`.  In either case, restoring `T` in the
singleton-signature colouring `c_{\{e\}}` creates only the conflict `e`,
and that edge is absent from the opposite closed shore.  The restriction
is proper and the usual gluing argument proves rejection by the intact
selected shore.  This is outcome 1.

The only remaining possibility is

\[
                          I\cup\{u,v\}\subseteq S.    \tag{4.10}
\]

The five displayed vertices are distinct because `I\subseteq X` and
`u,v\in C`; since `|S|=6`, (4.8) follows.  Since the connected-full case
has `V(K)=X\mathbin{\dot\cup}C`, the last vertex `s` lies in one of those
two sets, proving (4.8A).  All endpoints of every edge of
`T` now belong to `Q`.  Every nonempty signature colouring has at least
one monochromatic restored edge in the common boundary of both closed
shores, so none restricts properly to either one.  Conversely, if (4.10)
fails, one of the two choices in the preceding paragraph supplies a
labelled response.  Thus outcome 3 is exact and the three outcomes are
exhaustive.

This completes the proof. `\square`

## 5. Exact gain and surviving configurations

Theorem 3.1 is not a reformulation of the original shore response.  It
puts all fifteen labelled signatures on one six-connected, exactly
six-chromatic, dense host with its own spanning exact near-clique model.
The universal implication (3.7) couples an arbitrary colouring of that
host to the named remote edge, and (3.8) turns the former abstract
partition-disjointness into a numerical six-block/five-block gap.

Theorem 4.1 then shows exactly where a proof may continue.

- In outcome 1, the loss of seven-connectivity has already returned an
  exact-seven separation with an original operation label, not a generic
  restart edge.
- Outcome 2 is a rigid bilateral residue: the same remote-edge colouring
  rejects both overlapping order-eight selected shores, and the overlap
  is the literal seven-set `S\cup\{z\}`.  The result does not identify
  either response partition with a bag contact of either exact model.
- Outcome 3 is the exact first label obstruction.  Its six-cut consists
  of the five non-centre operation endpoints and one further vertex.  All
  fifteen conflicts are contained in the common order-seven boundary, so a
  closed-shore response cannot be extracted from the existing cube.
- If `K` is seven-connected, the survivor is a seven-connected,
  minimum-degree-seven, exactly six-chromatic graph at density `4N-5`
  with a spanning exact `K_7^\vee` model, the full pointed cube and the
  palette/equality constraint.  None of the audited model theorems assigns
  its two missing contacts to `f` or to a deleted-centre colour trace.

Thus the next terminal theorem need address only the seven-connected
constrained core, the two overlapping order-eight separations, or the
boundary-contained five-endpoint cut.  A generic first-hit path, common
portal, unlabelled exact-seven
restart or palette/model identification does not resolve any of these
three cases.

## 6. Dependency map

1. The
   [remote-edge operation cube](../results/hc7_k7minus_remote_removable_edge_operation_cube.md)
   supplies `f,T`, seven-connectivity of `G-f`, all fifteen exact deletion
   signatures, all eighty exact operation patterns and the original fixed
   exact model.
2. The
   [remote-interface topological reduction](../results/hc7_k7minus_remote_interface_topological_reduction.md)
   supplies the connected-full order-eight case (1.4) and `|C|\ge16`.
3. The
   [six-cut localisation theorem](../results/hc7_k7minus_exact_six_cut_localisation.md)
   supplies `r\in\{2,3\}`, `N_K(D_i)=S`, and (4.3).  The lower bound on
   `|D_i|` and the intersections with `X-S` are proved here from
   `\delta(K)\ge7` and the seven-connectivity of `G-f`.
4. The
   [three-component seven-cut exclusion](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
   supplies the exact two-component conclusion after deleting any
   seven-cut of `G`.
5. The established case `HC_5` turns the literal `K_5`-minor exclusion
   of `K[X]` into the four-colour bound (3.3A).
6. Norin--Totschnig,
   [Theorem 6](https://arxiv.org/html/2507.03244#S1.Thmtheorem6), supplies
   the `K_7^\vee` model at density `4N-8`.

The barrier audit in Section 2 limits which earlier results may be
composed; none of those barrier files is a positive dependency of the two
theorems.
