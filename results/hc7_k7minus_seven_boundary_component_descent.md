# Capacity of connected subgraphs adjacent to a seven-vertex boundary and component-contraction accounting

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.  This note strengthens the
component bound in the earlier seven-cut theorem and gives the exact density
and connectivity conditions for a descent obtained by contracting whole cut
components.  It does not prove that such a descent always exists.

## Theorem 1 (capacity for connected subgraphs adjacent to every boundary vertex)

Let `G` be a graph with no `K_7^-` minor, and let `S\subseteq V(G)` have
order seven.  Suppose

\[
                         P_1,\ldots,P_p                 \tag{1}
\]

are pairwise vertex-disjoint connected subgraphs of `G-S`, each adjacent to
every vertex of `S`.  Then

\[
                              p\le4.                    \tag{2}
\]

For `p\ge2`, the following further conclusions hold:

\[
                         \kappa(G[S])\le6-p.            \tag{3}
\]

Moreover:

1. if `p=2`, then `G[S]` has no `K_5` minor;
2. if `p=3`, then `|E(G[S])|\le9`; and
3. if `p=4`, then `G[S]` has maximum degree at most one.

### Proof

Contract each `P_i` to a vertex `c_i`.  The resulting minor contains

\[
                         I_p\vee G[S],                  \tag{4}
\]

where the `c_i` form the independent set `I_p`.

If `p\ge5`, choose five contracted vertices `c_1,\ldots,c_5` and label
`S=\{s_1,\ldots,s_7\}`.  The seven branch sets

\[
 \{c_i,s_i\}\quad(1\le i\le5),
 \qquad \{s_6\},\qquad\{s_7\}                         \tag{5}
\]

are connected and pairwise adjacent except possibly for
`\{s_6\}--\{s_7\}`.  They form a `K_7^-` model, proving (2).

For a seven-vertex graph `R`, direct cut analysis gives

\[
                  \kappa(I_p\vee R)=
                  \min\{7,p+\kappa(R)\}.              \tag{6}
\]

The finite constructions in the audited
[seven-cut component-contraction theorem](hc7_k7minus_seven_cut_contraction.md)
prove that `I_p\vee R` contains a `K_7^-` minor whenever it is
seven-connected for `2\le p\le4`.  Applying (6) to the minor (4) gives
(3).

If `p=2`, a `K_5` model in `G[S]` together with `c_1,c_2` gives seven
branch sets whose only missing adjacency is `c_1c_2`.  This proves part 1.

If `p=3` and `G[S]` has at least ten edges, the elementary seven-vertex
lemma in the same audited theorem supplies, as a not necessarily induced
subgraph, a `K_4^-`, a house, or `K_{2,3}`.  A literal `K_4^-` uses four
boundary vertices; merge the three contracted vertices with the other three
boundary vertices.  For a house or `K_{2,3}`, contract the displayed
five-vertex subgraph to `K_4^-`, retain one contracted vertex as a singleton,
and merge the other two with the two unused boundary vertices.  Each
construction is a `K_7^-` model, proving part 2.

Finally suppose `p=4` and `G[S]` contains a path `x-y-z`.  Choose three
further boundary vertices `u,v,w`.  The seven branch sets

\[
 \{c_1\},\quad \{c_2,u\},\quad \{c_3,v\},\quad \{c_4,w\},
 \quad \{x\},\quad\{y\},\quad\{z\}                    \tag{7}
\]

have every required adjacency except possibly `xz`.  Hence `G[S]` has no
two-edge path, equivalently maximum degree at most one.  This proves part 3.
\(\square\)

## Corollary 2 (sharpened seven-cut theorem)

Let `G` be seven-connected with no `K_7^-` minor, let `S` be a vertex cut
of order seven, and let `C_1,\ldots,C_r` be the components of `G-S`.
Let `\pi_S(G)` denote the maximum number of pairwise vertex-disjoint
connected subgraphs of `G-S` that are each adjacent to every vertex of
`S`.  Then

\[
 N_G(C_i)=S\quad(1\le i\le r),
 \qquad 2\le r\le\pi_S(G)\le4,                       \tag{8}
\]

and all conclusions of Theorem 1 hold with `p=\pi_S(G)`.  In particular,
they hold with `p=r` and `P_i=G[C_i]`.

### Proof

Seven-connectivity implies `N_G(C_i)=S`: a proper subset of `S` containing
the neighbourhood of `C_i` would be a cut of order at most six.  Thus the
components are connected subgraphs adjacent to every vertex of `S`, so
`r\le\pi_S(G)`.
Apply Theorem 1 to a maximum such family and also to the component family.
\(\square\)

## Corollary 3 (four-component interiors)

Under the hypotheses of Corollary 2, if `r=4`, then every component of
`G-S` either has order one or is two-connected.

### Proof

Suppose a component `C` has order at least two and is not two-connected.
We first find a partition

\[
                         V(C)=X\mathbin{\dot\cup}Y             \tag{9}
\]

such that `G[X]` and `G[Y]` are connected and adjacent, and each of `X,Y`
has at least six neighbours in `S`.

If `|V(C)|=2`, take its two vertices as `X,Y`.  Each has its partner and,
by seven-connectivity, at least six neighbours in `S`.

Otherwise let `v` be a cutvertex of `C`.  Choose a component `X` of `C-v`
and a different component `D`, and put `Y=V(C)-X`.  Both `G[X]` and
`G[Y]` are connected and they are adjacent through `v`.  Moreover,

\[
 N_G(X)=N_G(X)\cap S\;\mathbin{\dot\cup}\;\{v\},
 \qquad
 N_G(D)=N_G(D)\cap S\;\mathbin{\dot\cup}\;\{v\}.       \tag{10}
\]

Each displayed neighbourhood separates its set from the other three
components of `G-S`.  Seven-connectivity therefore gives at least six
`S`-neighbours to both `X` and `D`.  Since `D\subseteq Y`, the set `Y` also
has at least six `S`-neighbours.

In either case, `X` and `Y` have at least five common neighbours in the
seven-set `S`; call five of them `s_1,\ldots,s_5`.  Let `D_1,D_2,D_3` be
the other three components of `G-S`.  The seven branch sets

\[
 X,\quad Y,\quad
 V(D_1)\cup\{s_1\},\quad
 V(D_2)\cup\{s_2\},\quad
 V(D_3)\cup\{s_3\},\quad
 \{s_4\},\quad\{s_5\}                                  \tag{11}
\]

are connected, disjoint, and pairwise adjacent except possibly for the
last pair.  They form a `K_7^-` model, a contradiction.  \(\square\)

## Theorem 4 (exact whole-component contraction criterion)

Retain the hypotheses and notation of Corollary 2.  Put

\[
 n_i=|V(C_i)|,
 \qquad
 e_i=|E(G[C_i])|+|E_G(C_i,S)|,
 \qquad
 \delta_i=e_i-4n_i,                                   \tag{12}
\]

and define the global surplus

\[
 q=|E(G)|-(4|V(G)|-4),
 \qquad e_S=|E(G[S])|.                                \tag{13}
\]

Then

\[
                         q=e_S+\sum_{i=1}^r\delta_i-24. \tag{14}
\]

Let `X` be a nonempty subset of `\{1,\ldots,r\}` and let `H_X` be obtained
by contracting each `C_i`, `i\in X`, to one vertex.  Then

\[
 |E(H_X)|-(4|V(H_X)|-4)
       =q+\sum_{i\in X}(3-\delta_i).                  \tag{15}
\]

The graph `H_X` is seven-connected if and only if the following condition
holds:

> For every nonempty `D\subseteq X` and every
> `Z\subseteq V(G)-\bigcup_{i\in X}V(C_i)` satisfying
> `|D|+|Z|\le6`, the graph
>
> \[
>              G-\bigcup_{i\in D}V(C_i)-Z             \tag{16}
> \]
>
> is connected.

Consequently, the proposed seven-cut descent exists by whole-component
contraction whenever some `X` satisfies

\[
 \sum_{i\in X}\delta_i\le3|X|+q,                     \tag{17}
\]

condition (16), and `X` contains a component of order at least two.

### Proof

Since `|S|=7`, summing the component and boundary edges gives

\[
 |V(G)|=7+\sum_i n_i,
 \qquad
 |E(G)|=e_S+\sum_i(4n_i+\delta_i),                    \tag{18}
\]

which is (14).

Contracting `C_i` removes `n_i-1` vertices.  Because `C_i` is connected and
has neighbourhood exactly `S`, it replaces its `e_i` incident or internal
edges by exactly seven edges from the contracted vertex to `S`.  Thus it
removes `e_i-7=4n_i+\delta_i-7` edges.  Substitution into (13) proves (15).

Let `c_i` denote the vertex replacing `C_i`, `i\in X`.  Consider a set
`Y\subseteq V(H_X)` with `|Y|\le6`, put

\[
 D=\{i\in X:c_i\in Y\},
 \qquad Z=Y-\{c_i:i\in D\}.                           \tag{19}
\]

If `D` is empty, seven-connectivity makes `G-Z` connected, and contracting
the surviving `C_i` preserves connectedness.  If `D` is nonempty, then
`H_X-Y` is obtained from the graph in (16) by contracting the surviving
components `C_i`, `i\in X-D`.  Each such component lies wholly in one
connected component of (16), so these contractions neither join nor split
connected components.  Hence `H_X-Y` is connected exactly when (16) is
connected.  This proves the criterion.

Equation (15) shows that (17) is exactly the condition

\[
                         |E(H_X)|\ge4|V(H_X)|-4.        \tag{20}
\]

Condition (16) supplies seven-connectivity.  If some selected component has
order at least two, the contraction is a proper minor.  This proves the final
assertion.  \(\square\)

## Corollary 5 (exact failure certificate in a descent-minimal graph)

In addition to the hypotheses of Corollary 2, suppose `q\ge0` and no proper
minor `H` of `G` is both seven-connected and satisfies

\[
                         |E(H)|\ge4|V(H)|-4.            \tag{21}
\]

If a nonempty set `X\subseteq\{1,\ldots,r\}` contains a component of order
at least two and satisfies (17), then there are a nonempty `D\subseteq X`
and a set

\[
 Z\subseteq V(G)-\bigcup_{i\in X}V(C_i),
 \qquad |D|+|Z|\le6,                                  \tag{22}
\]

such that

\[
              G-\bigcup_{i\in D}V(C_i)-Z              \tag{23}
\]

is disconnected.  In particular, if `|V(C_i)|\ge2` and
`\delta_i\le3+q`, then some

\[
                 Z\subseteq V(G)-V(C_i),
                 \qquad |Z|\le5,                       \tag{24}
\]

makes `G-V(C_i)-Z` disconnected.

### Proof

If condition (16) held for `X`, Theorem 4 would make `H_X` a proper
seven-connected minor satisfying (21), contrary to the hypothesis.  Its
failure gives (22)--(23).  For `X=\{i\}`, the only nonempty choice of `D`
is `\{i\}`, which gives (24).  \(\square\)

## Exact residue of the whole-component method

Theorem 4 separates the two independent requirements that the earlier
fragment target combined informally: the excess inequality (17) and the
deletion-connectivity condition (16).  Neither follows from the boundary
restrictions alone.

At exact global surplus `q=0`, the permitted boundary values admit the
following arithmetic patterns:

\[
\begin{array}{c|c|c}
r&e_S&(\delta_1,\ldots,\delta_r)\\ \hline
4&0&(6,6,6,6)\\
3&9&(5,5,5)\\
2&15&(4,5).
\end{array}                                             \tag{25}
\]

Each row satisfies (14), but every nonempty subset violates (17).  These
are arithmetic obstructions, not asserted graph examples.  They show that
density counting and the contracted boundary quotient alone cannot prove
the desired descent.  A proof of the full seven-cut target must use internal
component structure to obtain a different minor, rule out these excess
distributions, or construct the `K_7^-` model directly.

## Scope

The connected-subgraph capacity and accounting theorems are unbounded and
computation-free.  They improve the former component bound from five to four
and identify an exact sufficient descent criterion.  They do not prove that
criterion for any of the remaining `r=2,3,4` cases, the bare `4n-4`
extremal theorem, the `K_7^-` six-colour conjecture, or `HC_7`.
