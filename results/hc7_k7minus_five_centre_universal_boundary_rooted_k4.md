# A rooted `K_4` on every four boundary vertices of the distinct-response shore

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_universal_boundary_rooted_k4_audit.md`](hc7_k7minus_five_centre_universal_boundary_rooted_k4_audit.md).

This is an unbounded consequence of the five-centre two-cut reduction.  It
applies, in particular, throughout the surviving order-at-least-eight branch.

## Theorem

Assume the hypotheses and notation of the audited
[five-centre two-cut reduction](hc7_k7minus_five_centre_two_cut_reduction.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

the graph `G-S` has exactly two connected components `C,D`, both are
adjacent to every vertex of `S`, and the notation is oriented so that `D`
is the distinct-response component.  For every four-set `Q subseteq S`,
the graph

\[
                         J_Q=G[D\cup Q]
\tag{1}
\]

contains a `K_4` minor rooted at the four literal vertices of `Q`.

## Proof

The two-cut reduction gives

\[
                         \chi(G[D])\ge5.              \tag{2}
\]

The sets `C,D` are nonempty, there is no `C-D` edge, and `G` is
seven-connected.  Apply the audited
[closed-shore rooted-connectivity lemma](hc7_closed_shore_rooted_connectivity.md)
with `A=D`, `R=C`, and the chosen set `Q`.  It follows that `(J_Q,Q)` is
internally four-connected: there is no separation `(X,Y)` of `J_Q` with

\[
 Q\subseteq X,\qquad Y-X\ne\varnothing,
 \qquad |X\cap Y|\le3.                                \tag{3}
\]

Suppose for a contradiction that `J_Q` has no `Q`-rooted `K_4` minor.
Fabila-Monroy and Wood's rooted-`K_4` obstruction theorem, Theorem 15,
says that `J_Q` is a spanning subgraph of a graph `H^+` in one of their
six classes `A`--`F`.  In every class the four nominated vertices belong
to the base graph `H`.  The graph `H^+` is obtained from `H` by assigning
to each triangle `T` of `H` a possibly empty clique `X_T`, disjoint from
`H` and from the other assigned cliques, whose only neighbours outside
`X_T` are the three vertices of `T`.

We first show that every `X_T` is empty.  Otherwise, since `J_Q` is a
*spanning* subgraph of `H^+`, all vertices of `X_T` are vertices of
`J_Q`.  Let `W` be a nonempty component of `J_Q[X_T]`.  No edge of `J_Q`
joins `W` to another vertex of `X_T`, and the definition of `H^+` gives

\[
                              N_{J_Q}(W)\subseteq T.  \tag{4}
\]

Put

\[
 X=V(J_Q)-W,\qquad Y=W\cup N_{J_Q}(W).
\]

These vertex sets define a separation of `J_Q`.  All four roots lie in
`H`, so `Q subseteq X`; its non-root side is `Y-X=W`, and

\[
                         |X\cap Y|=|N_{J_Q}(W)|\le3.
\]

This contradicts (3).  Hence all cliques added to `H` are empty.

Consequently `J_Q` is a spanning subgraph of the base graph `H` itself.
Every base graph in classes `A`--`F` is planar: this is immediate for the
three finite bases `A`--`C`, and is part of the plane construction in
classes `D`--`F` (the nominated degree-two vertices in `E,F` are attached
along edges of the outer face).  Therefore `J_Q` is planar.  Its induced
subgraph `G[D]` is planar as well, so the Four Colour Theorem gives
`chi(G[D])<=4`, contradicting (2).  Thus `J_Q` contains the required
`Q`-rooted `K_4` minor.  \(\square\)

## External input

Ruy Fabila-Monroy and David R. Wood,
[*Rooted `K_4`-Minors*](https://doi.org/10.37236/3476), *Electronic Journal
of Combinatorics* **20** (2013), Paper P64, Theorem 15; see also the
definition of `H^+` and the six obstruction classes preceding the theorem.

## Scope

The theorem is simultaneous only at the level of existence: every choice
of four boundary roots has a rooted model, but the models for different
four-sets need not have compatible branch sets.  No such compatibility is
claimed here.
