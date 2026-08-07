# Localisation at an order-six cut

**Status:** written proof with a separate hash-pinned internal audit.  This
theorem does not prove the seven-connected `4n-2` extremal target or the
`K_7^-` six-colour conjecture.

Throughout, `K_7^-` denotes the graph obtained from `K_7` by deleting one
edge.  All graphs are finite and simple.

We use two established four-root results in the forms quoted by Norin and
Totschnig.  If `(F,Q)` is internally four-connected, `|Q|=4`, and
`|V(F)|>=6`, then `F` has a `Q`-rooted `K_4^-` model (their Lemma 10,
quoting Jørgensen).  If `(F,Q)` is internally four-connected and has no
`Q`-rooted `K_4` model, then

\[
                         |E(F)|\le3|V(F)|-7.           \tag{1}
\]

This is Norin--Totschnig, Lemma 9.

## Theorem

Let `H` be a six-connected graph with no `K_7^-` minor, let `S` be a
vertex cut of order six, and let `C_1,...,C_r` be the components of
`H-S`.  Then every component is adjacent to every vertex of `S`, and

\[
                              r\in\{2,3\}.             \tag{2}
\]

Moreover:

1. if `r=2`, every five vertices of `S` span at most eight edges, and
   hence `|E(H[S])|<=12`;
2. if `r=3`, every four vertices of `S` span at most four edges, and
   hence `|E(H[S])|<=10`; if one component is non-singleton, then also
   `Delta(H[S])<=3`.

Suppose additionally that

\[
                         |E(H)|\ge4|V(H)|-2.           \tag{3}
\]

Then the alternatives sharpen to

\[
\begin{array}{c|c}
r&\text{boundary conclusion}\\
\hline
2&|E(H[S])|\le11,\\
3&\Delta(H[S])\le3\text{ and }|E(H[S])|\le8.
\end{array}                                             \tag{4}
\]

For later use, define

\[
 \delta_i=|E(H[C_i])|+|E_H(C_i,S)|-4|C_i|,
 \qquad q_H=|E(H)|-(4|V(H)|-2).
\]

Exact accounting gives

\[
                 q_H=|E(H[S])|+\sum_{i=1}^r\delta_i-22. \tag{5}
\]

Consequently, any graph satisfying (3) and avoiding the target lies in
one of the following two exact residual cases:

\[
\begin{array}{c|c|c}
r& H[S]&\text{required component excess}\\
\hline
2&|E(H[S])|\le11&
  \delta_1+\delta_2=q_H+22-|E(H[S])|\ge q_H+11,\\
3&\Delta(H[S])\le3,\ |E(H[S])|\le8&
  \sum_i\delta_i=q_H+22-|E(H[S])|\ge q_H+14.
\end{array}                                             \tag{6}
\]

## Proof

For every component `C_i`, its neighbourhood is contained in `S`.
Six-connectivity therefore gives

\[
                              N_H(C_i)=S.              \tag{7}
\]

We first bound the number of components.  Select `k` full components.
Absorb `k-1` distinct vertices of `S`, one into each of `k-1` components,
retain the last component as a bare branch set, and retain the remaining
boundary vertices as singleton branch sets.  This gives seven disjoint
connected branch sets.  Fullness supplies every adjacency except those
between the unabsorbed boundary singletons.

If `r>=5`, use five components.  Only two boundary singletons remain, so
the construction is a `K_7^-` model.  Thus `r<=4`.

Suppose `r=4`.  Applying the same construction with four components and
any prescribed three boundary singletons shows that every three-set in
`S` spans at most one edge.  Hence `H[S]` is a matching.

If some component, say `C_1`, is non-singleton, choose any four-set
`Q\subseteq S`.  The pair `(H[C_1\cup Q],Q)` is internally
four-connected: a rooted separation of order at most three, together
with the two vertices of `S-Q`, would give a cut of `H` of order at most
five.  Since the rooted graph has at least six vertices, the rooted
diamond theorem supplies a `Q`-rooted `K_4^-` model.  Absorb the two
vertices of `S-Q` into two of the other three components and retain the
third component as a bare branch set.  These three bags and the four
rooted bags form a `K_7^-` model, a contradiction.

Thus all four components would be singletons.  Every boundary vertex then
has exactly four exterior neighbours and at most one boundary neighbour,
so it has degree at most five, contradicting six-connectivity.  This proves
(2).

Assume `r=2`.  Leaving any prescribed five vertices of `S` unabsorbed in
the elementary construction shows that they span at most eight edges.
Each boundary edge belongs to four of the six five-subsets, so

\[
                 4|E(H[S])|\le6\cdot8,
 \qquad |E(H[S])|\le12.                               \tag{8}
\]

Assume `r=3`.  Leaving any prescribed four vertices of `S` unabsorbed
shows that they span at most four edges.  Each boundary edge belongs to
six of the fifteen four-subsets, and hence

\[
                 6|E(H[S])|\le15\cdot4,
 \qquad |E(H[S])|\le10.                               \tag{9}
\]

Suppose that `C_1` is non-singleton and some `z\in S` has at least four
boundary neighbours.  Choose four such neighbours as `Q`.  As above,
`(H[C_1\cup Q],Q)` has a rooted `K_4^-` model.  If `w` is the remaining
vertex of `S-(Q\cup\{z\})`, then the four rooted bags together with

\[
                  C_2\cup\{w\},\qquad C_3,
                  \qquad\{z\}
\]

form a `K_7^-` model.  Fullness supplies every adjacency involving the
component bags, while the four literal edges from `z` to `Q` join
`\{z\}` to the rooted bags.  Therefore `Delta(H[S])<=3`.

It remains to prove the sharpenings under (3).  Equation (5) follows by
partitioning the edges into the boundary edges and the internal-plus-
boundary edges of the components, and using
`|V(H)|=6+sum_i|C_i|`.

### Two components at twelve boundary edges

Suppose `r=2` and `|E(H[S])|=12`.  For every `s\in S`, the five-set
`S-\{s\}` has at most eight edges, so

\[
                    12-d_{H[S]}(s)\le8.
\]

The boundary degree sum is twenty-four.  Hence every boundary vertex has
degree four and

\[
                         H[S]\cong K_6-3K_2.          \tag{10}
\]

Fix a component `C`, and put

\[
 c=|C|,\quad e_C=|E(H[C])|,\quad
 p(s)=|E_H(C,\{s\})|,\quad P=\sum_{s\in S}p(s),
 \quad\delta=e_C+P-4c.
\]

Let `pq` be one of the three boundary nonedges and put
`Q=S-\{p,q\}`.  The graph `H[Q]` is a four-cycle.  The pair
`(H[C\cup Q],Q)` is internally four-connected by the same separator
lift used above.  It has no `Q`-rooted `K_4` model: such a model, the
other full component and the singleton bags `\{p\},\{q\}` would form a
`K_7^-` model, with `pq` as the only possible missing adjacency.

Applying (1) gives

\[
 e_C+P-p(p)-p(q)+4\le3(c+4)-7,
\]

or equivalently

\[
                         p(p)+p(q)\ge c+\delta-1.      \tag{11}
\]

The three nonedges partition `S`, so summing (11) gives

\[
                         P\ge3c+3\delta-3.             \tag{12}
\]

Connectedness gives `e_C>=c-1`, and therefore

\[
                         P=4c+\delta-e_C
                           \le3c+\delta+1.             \tag{13}
\]

Thus `delta<=2`.  Applying this to both components gives
`delta_1+delta_2<=4`, whereas (5) requires

\[
                         \delta_1+\delta_2=q_H+10\ge10.
\]

This contradiction proves the first line of (4).

### Three components at nine boundary edges

Suppose `r=3`.  The three components cannot all be singletons under (3):
then `|V(H)|=9`, and the eighteen component--boundary edges together with
(9) would give at most twenty-eight edges, below the required thirty-four.
Thus one component is non-singleton, so `Delta(H[S])<=3`.  In particular,
`|E(H[S])|<=9`.

Suppose equality holds.  Then `H[S]` is cubic.  Fix a component `C` and
retain the notation `c,e_C,p(s),P,delta` above.  For every ordered boundary
nonedge `(q,p)`, put `Q=S-\{q,p\}`.  The rooted pair
`(H[C\cup Q],Q)` is internally four-connected and has no `Q`-rooted
`K_4` model.  Indeed, if `D,E` are the other two components, such a model
would combine with

\[
                         D\cup\{p\},\qquad E,
                         \qquad\{q\}
\]

to give seven bags.  Since `q` has three boundary neighbours and `p` is
one of its two nonneighbours, `q` meets three of the four rooted bags and
can miss only one; fullness supplies every other required adjacency.

The rooted bound (1) gives

\[
 e_C+P-p(q)-p(p)+|E(H[S-\{q,p\}])|\le3c+5.            \tag{14}
\]

A cubic graph on six vertices has twelve ordered nonedges.  On summing
(14), every attachment count is subtracted four times and every boundary
edge belongs to four of the four-root sets.  Since the boundary has nine
edges,

\[
                    12e_C+8P+36\le36c+60,
\]

and hence

\[
                         3e_C+2P\le9c+6.               \tag{15}
\]

Using `e_C>=c-1`,

\[
 \begin{aligned}
  2\delta
     &=2e_C+2P-8c\\
     &\le(9c+6)-e_C-8c\\
     &\le7.
 \end{aligned}
\]

Thus `delta<=3`.  This applies to all three components, while (5) requires

\[
                         \sum_{i=1}^3\delta_i=q_H+13\ge13,
\]

a contradiction.  Therefore `|E(H[S])|<=8`, proving the second line of
(4).  Equation (6) is now just (5) rearranged. `\square`

## Scope

The theorem leaves two genuine component-excess problems: the
two-component case with at most eleven boundary edges, and the
three-component case with a subcubic boundary of at most eight edges.
Closing either case requires information about the component interiors and
their attachments; fullness and minimum degree do not supply a lower bound
on boundary degree.

## External source

Sergey Norin and Agnès Totschnig,
[*Every graph with no `K_7^\vee`-minor is 6-colourable*](https://arxiv.org/abs/2507.03244),
Lemmas 9 and 10.
