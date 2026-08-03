# At most three components behind a seven-vertex cut

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.

## Theorem

Let `G` be a seven-connected graph with no `K_7^-` minor, and let
`S\subseteq V(G)` be a vertex cut of order seven.  Then `G-S` has at most
three components.  If `G-S` has exactly three components, then

\[
                         \Delta(G[S])\le3.
\]

## Proof

Let `C_1,\ldots,C_r` be the components of `G-S`.  The audited
[seven-boundary capacity theorem](hc7_k7minus_seven_boundary_component_descent.md)
gives

\[
                         2\le r\le4,                  \tag{1}
\]

and every `C_i` is adjacent to every vertex of `S`.  If `r=4`, it also
gives

\[
                         \Delta(G[S])\le1.            \tag{2}
\]

Suppose that `r=4` and some component, say `C_1`, has at least two
vertices.  Choose a four-set

\[
                         Q=\{q_1,q_2,q_3,q_4\}\subseteq S.
\]

Apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
with `A=C_1` and with `R` equal to the union of the other three
components.  The rooted pair `(G[C_1\cup Q],Q)` is internally
four-connected.  It has at least six vertices, so Jørgensen's rooted
diamond theorem gives four pairwise disjoint connected branch sets

\[
                         B_1,B_2,B_3,B_4
\]

with `q_i\in B_i`, all but at most one of the six mutual adjacencies being
present.

Write `S-Q=\{s_2,s_3,s_4\}`.  For `j=2,3,4`, put

\[
                         P_j=V(C_j)\cup\{s_j\}.
\]

Each `P_j` is connected because `C_j` is adjacent to `s_j`.  The seven
sets

\[
                         B_1,B_2,B_3,B_4,P_2,P_3,P_4 \tag{3}
\]

are pairwise disjoint.  For distinct `j,k`, fullness of `C_j` at `S`
supplies an edge from `C_j` to `s_k`, so `P_j` and `P_k` are adjacent.
The same fullness supplies an edge from `C_j` to each literal root `q_i`,
so every `P_j` is adjacent to every `B_i`.  Hence the sets in (3) form a
`K_7^-`-minor model, a contradiction.

It follows that, if `r=4`, every component of `G-S` is a singleton.  By
fullness, each vertex of `S` is adjacent to all four of these singleton
components.  Equation (2) then gives

\[
                         d_G(s)\le4+1=5
                         \qquad(s\in S),
\]

contrary to seven-connectivity.  Thus `r\ne4`, and (1) proves `r\le3`.

It remains to prove the stated boundary-degree conclusion.  Suppose that
`r=3`.  At least one component, say `C_1`, is non-singleton.  Indeed, if
all three components were singletons, then every vertex of `S` would have
three neighbours outside `S`.  Seven-connectivity would therefore give
minimum degree at least seven and hence

\[
                         d_{G[S]}(s)\ge4
                         \qquad(s\in S).
\]

It would follow that `|E(G[S])|\ge14`, whereas the seven-boundary capacity
theorem gives `|E(G[S])|\le9` when `r=3`.

Suppose now that some `z\in S` has at least four neighbours in `G[S]`,
and choose

\[
                         Q=\{q_1,q_2,q_3,q_4\}
                         \subseteq N_{G[S]}(z).
\]

Apply the closed-shore rooted-connectivity lemma with `A=C_1` and with
the union of the other two components as the nonempty opposite side.
As above, Jørgensen's theorem gives a `Q`-rooted `K_4^-`-minor model
`B_1,B_2,B_3,B_4` in `G[C_1\cup Q]`, with `q_i\in B_i`.

Write `S-Q=\{z,a,b\}`, and let `C_2,C_3` be the other two components.
Then the seven sets

\[
 B_1,B_2,B_3,B_4,
 \quad V(C_2)\cup\{a\},
 \quad V(C_3)\cup\{b\},
 \quad \{z\}                                           \tag{4}
\]

are pairwise disjoint and connected.  Fullness makes both
component-derived bags adjacent to every rooted bag, to one another, and
to `\{z\}`.  The literal edges `zq_i` make `\{z\}` adjacent to every
`B_i`.  Thus the only possible missing adjacency among the sets in (4)
is the one already allowed inside the rooted `K_4^-` model.  They form a
`K_7^-`-minor model, a contradiction.  Consequently
`\Delta(G[S])\le3` when `r=3`.
\(\square\)

## Scope and inputs

The theorem uses neither a density hypothesis nor proper-minor
six-colourability.  It combines:

- the capacity-four and boundary-degree conclusions for a seven-vertex
  cut;
- rooted internal four-connectivity of a closed shore; and
- Jørgensen's rooted `K_4^-` theorem, in the form quoted as Lemma 10 by
  Norin and Totschnig.

The argument does not eliminate the two- or three-component cases.  In
the three-component case it proves only that the seven-vertex boundary is
subcubic; the remaining problem is to obtain the required seventh
branch-set adjacencies without a boundary vertex having four prescribed
boundary neighbours.
