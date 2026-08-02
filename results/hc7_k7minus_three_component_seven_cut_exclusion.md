# Three-component `3,2,2` seven-cut colouring theorem

**Status:** written proof; separate internal audit GREEN for this revision.

Here a component of `G-S` is **full at `S`** if it is adjacent to every
literal vertex of `S`.

## Theorem 1 (three-component `3,2,2` cut)

Let `G` be a finite simple seven-connected graph such that every proper
minor of `G` is six-colourable.  Let `S` be a seven-vertex cut for which

\[
                 G-S=D_1\mathbin{\dot\cup}D_2\mathbin{\dot\cup}D_3
\]

is the decomposition into components.  If `G[S]` has a proper
three-colouring with colour-class sizes `3,2,2`, then `G` is
six-colourable.

### Proof

Fix a proper boundary partition

\[
                 S=T\mathbin{\dot\cup}A\mathbin{\dot\cup}B,
       \qquad |T|=3,\quad |A|=|B|=2.                    \tag{1}
\]

Seven-connectivity gives `N_G(D_i)=S` for each `i`; otherwise fewer than
seven vertices would separate `D_i` from another component.

Say that `D_i` **realises** `(A,B)` if it contains disjoint connected
subgraphs `X_A,X_B` such that `X_A` is adjacent to both vertices of `A`
and `X_B` is adjacent to both vertices of `B`.  The two subgraphs may be
taken adjacent: join them by a shortest path in `D_i`, split the path at
one edge, and absorb its two halves into the corresponding subgraphs.

At most one component realises `(A,B)`.  Indeed, suppose two do.  For any
fixed component `D_i`, choose a realising component `R` different from
`D_i`, and let `F` be the third component.  Contract the three pairwise
disjoint connected sets

\[
                 X_A\cup A,\qquad X_B\cup B,\qquad F\cup T.              \tag{2}
\]

Their images form a triangle: the first two are adjacent by construction,
and fullness of `F` supplies the other two adjacencies.  A six-colouring
of this proper minor pulls back on `G[D_i\cup S]` to a colouring whose
equality partition on the literal boundary is exactly `T|A|B`.  Doing
this for all three components and permuting colour names makes the three
colourings agree on `S`; they then glue to a six-colouring of `G`.

Consequently, after relabelling, `D_1` and `D_2` do not realise `(A,B)`.
Fix one of them, say `D_i`.  In an auxiliary graph, add four distinct
terminals `a_1^*,b_1^*,a_2^*,b_2^*`, where `a_j^*` is adjacent precisely
to the vertices of `D_i` adjacent in `G` to `a_j\in A`, and similarly for
`b_j^*` and `b_j\in B`.  The ordered tuple

\[
                         (a_1^*,b_1^*,a_2^*,b_2^*)                       \tag{3}
\]

is crossless: a crossing gives the two disjoint connected subgraphs that
realise `(A,B)`.  First add the four consecutive frame edges; none can
create such a crossing because it joins consecutive terminals belonging to
the two different prescribed pairs.  Then add edges, without adding
vertices, until the graph is maximal subject to remaining crossless.  The
generalised Two Paths
Theorem of Humeau--Pous
([arXiv:2505.16431v2, Theorem 1.3](https://arxiv.org/abs/2505.16431))
identifies the resulting graph as a web with the four terminals as its
frame.

No cell inserted behind a facial triangle of this web contains an original
vertex of `D_i`.  Otherwise, take all original vertices in such a cell.
In the auxiliary graph their external neighbourhood is represented by at
most the three vertices of the facial triangle.  Replace every artificial
terminal among those vertices by its corresponding literal root in
`A\cup B`, and add the three vertices of `T`, whose incidences were not
represented in the auxiliary graph.  At most six actual vertices of `G`
then separate a nonempty subset of `D_i` from either other component,
contrary to seven-connectivity.

It follows, after replacing the artificial terminals by their literal
roots, that

\[
                  H_i^+=G[D_i\cup A\cup B]+E(K_{A,B})                    \tag{4}
\]

is planar, with the added `K_{2,2}` as an induced facial four-cycle.
The cycle is induced because `A` and `B` are independent.  This conclusion
holds for both `i=1,2`.  The web-completion edges in (4) are auxiliary
edges; none is asserted to be an edge of `G`.

Now contract in `G` the two disjoint connected sets

\[
                         Q_0=D_1\cup T,
                 \qquad Q_1=D_2\cup A.                                  \tag{5}
\]

Their images are adjacent, and each is adjacent to both retained vertices
of `B`, by fullness.  Six-colour this proper minor and pull the colouring
back only to the retained vertices and the literal boundary.  On
`G[D_3\cup S]` this gives a proper colouring `c` in which `T` has one
colour, say `0`, `A` has a different colour, say `1`, and neither vertex
of `B` has colour `0` or `1`.

For `i=1,2`, precolour the induced frame of `H_i^+` by `c|_{A\cup B}`.
This proper precolouring uses at most three colours from the five-colour
palette excluding colour `0`.  Diwan's planar precolouring theorem
([arXiv:2306.04944, Corollary 1](https://arxiv.org/abs/2306.04944)) says
that a properly precoloured induced cycle of length at most `2k-5` using
at most `k-1` colours extends to a `k`-colouring of every planar supergraph
containing it.  With `k=5`, it extends over each `H_i^+`.

Use these extensions on `D_1,D_2` and use `c` on `D_3\cup S`.  The
colourings agree on `A\cup B`; the first two use no colour `0`, so their
edges to `T` are proper; and distinct components of `G-S` are anticomplete.
They therefore combine into a six-colouring of `G`.  \(\square\)

## Corollary 2 (two-component normal form in the critical host)

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \text{every proper minor of `G` is six-colourable},\qquad
 \kappa(G)\ge7,\qquad
 K_7^-\npreccurlyeq G.
\]

Deleting any seven-vertex cut from `G` leaves exactly two components.
If their boundary-full connected-subgraph packing numbers are
`\mu_1,\mu_2`, then

\[
                 \min\{\mu_1,\mu_2\}=1,
             \qquad \mu_1+\mu_2\le3,
\]

and the boundary contains an edge.

### Proof

The audited critical seven-cut capacity theorem gives two or three
components.  In the three-component case it gives `\chi(G[S])=3` and says
that every proper three-colouring of `G[S]` has class sizes `3,2,2`.
Theorem 1 excludes that case.  Its two-component conclusions are exactly
the remaining conclusions stated above.  \(\square\)

## Scope

Theorem 1 is computation-free and does not use `K_7^-`-minor exclusion.
The corollary uses that exclusion only through the separately audited
critical seven-cut capacity theorem.  These results do not prove
Norin--Totschnig Conjecture 21, the bare seven-connected `4n-4` extremal
theorem, or Hadwiger's conjecture for `t=7`.
