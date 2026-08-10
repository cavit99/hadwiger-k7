# Five independent centres at a two-cut: the unconditional shore reduction

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_two_cut_reduction_audit.md`](hc7_k7minus_five_centre_two_cut_reduction_audit.md).

This note treats the two-cut branch of the five-centre finishing route.  It
does not assume the support-five normal form.  It proves that an arbitrary
two-cut has exactly two full sides with opposite colouring responses, and
it turns the equality side into a rooted-linkage obstruction satisfying a
sharp Du--Li--Xie--Yu edge bound.  The five-vertex equality case is closed
by an explicit `K_7^-` model.  Components of order at least six remain.

Throughout, `K_7^-` is `K_7` with one edge deleted.

## 1. Setting and statement

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
 \tag{1.1}
\]

and suppose

\[
 \kappa(G)\ge7,\qquad \delta(G)\ge8,
 \qquad K_5\not\subseteq G.                           \tag{1.2}
\]

Let

\[
                         Z=\{z_1,z_2,z_3,z_4,z_5\}     \tag{1.3}
\]

be an independent set, put `F=G-Z`, and suppose `{p,q}` is a two-cut of
`F`.  Set

\[
                         S=Z\mathbin{\dot\cup}\{p,q\}. \tag{1.4}
\]

For a component `L` of `G-S`, define its full-packing number `mu_S(L)` to
be the maximum number of pairwise vertex-disjoint connected subgraphs of
`G[L]` that are each adjacent to every literal vertex of `S`.

For a closed side `G[L union S]`, consider only proper six-colourings in
which all five vertices of `Z` have one colour and `p,q` avoid that colour.
Its **response set** records which of the two types `equal` and `distinct`
can occur on `p,q`.

### Theorem 1.1 (unconditional two-cut reduction)

Under (1.1)--(1.4), all of the following hold.

1. The graph `G-S` has exactly two components `C,D`, both adjacent to every
   vertex of `S`.  Moreover,

   \[
                              pq\notin E(G),            \tag{1.5}
   \]

   while `G[S]` has a centre--pole edge.

2. The response sets of the two closed sides are nonempty opposite
   singletons.  Orient the notation so that `C` has the equal response and
   `D` has the distinct response.  Then

   \[
                         \chi(G[C])\ge4,
             \qquad     \chi(G[D])\ge5.               \tag{1.6}
   \]

   In every permitted colouring of the `D`-side, there is a bichromatic
   `p`--`q` path whose internal vertices lie in `D`.

3. Contracting the connected set `D union Z` to a vertex `x` gives a
   proper minor `M_C` in which every proper six-colouring has `p,q` equal.
   Consequently

   \[
                              M_C+pq                    \tag{1.7}
   \]

   is exactly seven-chromatic and `pq` is a critical edge.  In any proper
   six-colouring of `M_C`, four colour-distinguished bichromatic `p`--`q`
   paths avoid `x` and have all internal vertices in `C`.  Paths belonging
   to distinct colours are edge-disjoint and can meet only at vertices
   having the common colour of `p,q`.

4. The rooted graph

   \[
                    (G[C\cup S],Z,p,q)                 \tag{1.8}
   \]

   is not feasible: there is no `p`--`q` path `P` for which all five roots
   in `Z` lie in one component of `G[C union S]-P`.  In addition,

   \[
                              \mu_S(C)=1.               \tag{1.9}
   \]

5. Writing `c=|C|`, one has

   \[
       |E(G[C])|+|E_G(C,S)|\le6c+1,
       \qquad |E(G[C])|\ge2c-1,                        \tag{1.10}
   \]

   and

   \[
                              c\ge6.                   \tag{1.11}
   \]

All conclusions are invariant under interchanging the original two
components; the labels `C,D` are fixed only by the response orientation.

## 2. The exact seven-boundary geometry

The components of `F-{p,q}` are exactly the components of `G-S`.  By
seven-connectivity, every such component has neighbourhood exactly `S`.

The audited
[critical seven-cut capacity theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md),
Theorem 3, gives at most three components.  If there were three, the same
theorem would say that every proper three-colouring of `G[S]` has class
sizes `3,2,2`.  But

\[
                              Z\mid\{p\}\mid\{q\}       \tag{2.1}
\]

is a proper three-colouring with class sizes `5,1,1`, because `Z` is
independent.  Hence there are exactly two components; call them temporarily
`A,B`.

Suppose `pq` were an edge.  Apply the exact boundary-colouring reflection
lemma in the same audited source to the partition (2.1).  On either side,
assign the block `Z` to the opposite full component and retain the two
singleton blocks `{p},{q}`, which form a clique.  This produces proper
six-colourings of both closed sides with the exact partition (2.1).  After
permuting colour names, they agree on `S` and glue to a six-colouring of
`G`, contrary to (1.1).  Thus (1.5) holds.

The two-component conclusion of the capacity theorem also says that
`G[S]` has an edge.  Since `Z` is independent and `pq` is absent, every
boundary edge is a centre--pole edge.  This proves assertion 1.

## 3. Opposite response types

Fix one component `L` and let `R` be the other.  The set `R union Z` is
connected: `R` is connected and has a neighbour at every vertex of `Z`.
Contract a spanning tree of this set to one vertex.  It is adjacent to both
`p,q`, because `R` is full at `S`.  A proper six-colouring of the resulting
proper minor pulls back on `G[L union S]` to a colouring in which `Z` is one
monochromatic block and `p,q` avoid its colour.  Thus each response set is
nonempty.

If the two response sets had a common type, choose a colouring of each
closed side having that type.  Their exact boundary partitions would both
be either

\[
                         Z\mid\{p,q\}                   \tag{3.1}
\]

or

\[
                         Z\mid\{p\}\mid\{q\}.          \tag{3.2}
\]

Aligning the block colours and gluing would six-colour `G`.  Hence the two
nonempty response sets are disjoint opposite singletons.  Orient them so
that `C` has (3.1) and `D` has (3.2).

If `G[C]` were three-colourable, use three fresh colours on `C` and three
distinct boundary colours on the blocks in (3.2).  This would give the
forbidden distinct response on `C`.  Therefore `chi(G[C])>=4`.  If `G[D]`
were four-colourable, use four fresh colours on `D` and two distinct
boundary colours on the blocks in (3.1).  This would give the forbidden
equal response on `D`.  Thus `chi(G[D])>=5`, proving (1.6).

Take any permitted colouring of the `D`-side and let `beta,gamma` be the
distinct colours on `p,q`.  If `p,q` lay in different components of the
subgraph induced by those two colours, interchange `beta,gamma` on the
component containing `p`.  The colour on `Z` is different and is not
changed.  The result would be a permitted equal response, a contradiction.
Thus a bichromatic `p`--`q` path exists.  Its internal vertices avoid `Z`
and hence lie in `D`.

## 4. The critical-edge packet on the equality side

Contract `D union Z` to `x` and retain `C,p,q`; call the resulting proper
minor `M_C`.  The contraction vertex is adjacent to both poles.  Every
proper six-colouring of `M_C` pulls back to a permitted response on the
closed `C`-side, so it makes `p,q` equal.

It follows that `M_C+pq` is not six-colourable.  Conversely, a proper
six-colouring of `M_C` becomes a seven-colouring after assigning one new
colour to one pole.  Hence (1.7) is exactly seven-chromatic.

In particular, `M_C` is exactly six-chromatic, and every proper
six-colouring of it uses all six colours: otherwise assigning a new colour
to one pole would six-colour `M_C+pq`.

Fix a proper six-colouring of `M_C`, let `alpha` be the common colour of
`p,q`, and let `delta` be the colour of `x`.  For every colour
`beta != alpha`, the vertices `p,q` lie in one `alpha`--`beta` component;
otherwise a Kempe interchange on the component containing `p` would extend
to a proper six-colouring after restoring `pq`.  For each of the four
colours outside `{alpha,delta}`, a corresponding path avoids `x` and has
all internal vertices in `C`.  Two paths for distinct colours can meet only
at `alpha`-coloured vertices, and cannot share an edge.  This proves
assertion 3.

## 5. Rooted infeasibility and packing number one

Suppose (1.8) were feasible.  Let `P` be its `p`--`q` path and let `K` be
the component of `G[C union S]-P` containing all of `Z`.  The sets `K` and
`P` are disjoint and connected.  They are adjacent because the
centre--pole boundary edge proved in Section 2 joins a vertex of `Z subseteq
K` to `p` or `q` in `P`.

Contract spanning trees of `K` and `P`, delete the unused vertices on the
`C`-side, and six-colour the resulting proper minor.  Restrict to the
untouched `D`-side and expand the literal boundary vertices: all of `Z`
receive the colour of the first contraction image, while `p,q` receive the
common, different colour of the second.  This is a permitted equal response
on `D`, contradicting its response singleton.  Therefore (1.8) is not
feasible.

The component `C` itself is connected and full at `S`, so `mu_S(C)>=1`.
If `P_1,P_2` were two disjoint connected `S`-full subgraphs in `C`, then

\[
                         P_1\cup Z,
              \qquad    P_2\cup\{p,q\}                 \tag{5.1}
\]

would be disjoint connected adjacent sets.  Contracting them and repeating
the preceding restriction would again produce a permitted equal response
on `D`.  Hence `mu_S(C)=1`, proving assertion 4.

## 6. The Du--Li--Xie--Yu bound

Put `H=G[C union S]` and apply Theorem 1.2 of Du, Li, Xie, and Yu,
[*Linkages and removable paths avoiding vertices*](https://arxiv.org/abs/2303.12146),
to the five-rooted graph `(H,Z,p,q)`.  The rooted graph is infeasible by
Section 5.  The theorem therefore gives a terminal-avoiding collection
`mathcal X` such that every member has neighbourhood of order at most six,
and the completed quotient satisfies

\[
 e(\mathcal H/\mathcal X)
 \le 6v(H/\mathcal X)-\frac{5^2}{2}-\frac{3\cdot5}{2}-1
 =6v(H/\mathcal X)-21.                                \tag{6.1}
\]

Any nonempty member `X` of the collection lies in `C`.  Since `C` is
anticomplete to `D`,

\[
                              N_G(X)=N_H(X).            \tag{6.2}
\]

A neighbourhood of order at most six would separate `X` from `D`, contrary
to seven-connectivity.  Thus the collection has no nonempty member, and its
quotient is just `H`.

The rooted completion makes the seven terminals complete except for `pq`,
and therefore contributes exactly 20 terminal edges.  Since `v(H)=c+7`,
(6.1) becomes

\[
 |E(G[C])|+|E_G(C,S)|+20\le6(c+7)-21,
\]

which is the first inequality in (1.10).

Every vertex of `C` has all its neighbours in `C union S`.  Summing the
minimum-degree bound over `C` gives

\[
                    2|E(G[C])|+|E_G(C,S)|\ge8c.       \tag{6.3}
\]

Combining (6.3) with the first inequality in (1.10) yields

\[
                         |E(G[C])|\ge2c-1,             \tag{6.4}
\]

as required.

For `c<=4`, (6.4) exceeds the complete-graph edge count.  Thus `c>=5`.
If `c=5`, then literal-`K_5` exclusion and (6.4) force

\[
                         G[C]\cong K_5^-.              \tag{6.5}
\]

The separately audited
[order-seven `K_5^-` component elimination theorem](../results/hc7_k7minus_order_seven_k5minus_component_elimination.md)
then gives an explicit `K_7^-` minor in `G`, contrary to (1.1).  Therefore
`c>=6`, completing the proof of Theorem 1.1.  \(\square\)

## 7. Exact remaining gap

The arbitrary two-cut branch is now confined to an equality-response
component `C` of order at least six satisfying all of

\[
 \chi(G[C])\ge4,\qquad
 \mu_S(C)=1,\qquad
 (G[C\cup S],Z,p,q)\text{ is rooted-infeasible},
 \qquad e(C)+e(C,S)\le6|C|+1.                         \tag{7.1}
\]

The opposite component has chromatic number at least five and contains a
literal bichromatic `p`--`q` path, while the equality side contains the
four-path critical-edge packet of Section 4.  A terminal continuation must
use those two coupled structures to produce an explicit `K_7^-` model or a
common boundary partition.  Merely assuming the support-five normal form,
or obtaining another unlabelled separator, does not close the arbitrary
two-cut branch.

## Dependencies and claim status

The component count, boundary edge, and reflection step use the separately
audited critical seven-cut capacity theorem.  The five-vertex terminal step
uses the separately audited order-seven `K_5^-` component theorem.  The
edge bound uses Du--Li--Xie--Yu, Theorem 1.2, specialized to five roots.

All other deductions in this note are proved here and covered by the
adjacent separate internal audit.
