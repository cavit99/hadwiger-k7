# Two literal `K_5` subgraphs force a `K_7^-` minor

**Status:** written proof; separate internal audit GREEN for this revision.
This is an unconditional clique-family theorem.  It does not prove that
every `K_7^-`-minor-free graph is six-colourable or prove `HC_7`.

Here `K_t^-` denotes `K_t` with one edge deleted.

## Lemma 1 (two linked cliques)

Let `r>=2`.  If an `(r+1)`-connected graph `H` contains two
vertex-disjoint literal `K_r` subgraphs, then `H` contains a
`K_{r+2}^-` minor.

### Proof

Write the two cliques as

\[
 A=\{a_1,\ldots,a_r\},\qquad B=\{b_1,\ldots,b_r\}.
\]

By Menger's theorem there are `r` pairwise vertex-disjoint `A`--`B`
paths.  Choose them with their open interiors outside `A\cup B`.  Their
ends exhaust both cliques, so relabel them as paths `P_i` from `a_i` to
`b_i`, and put `U=\bigcup_i V(P_i)`.

Call a path `Q` a **usable cross-path** if its ends `x\in P_i` and
`y\in P_j` lie on distinct paths, its open interior avoids `U`, and its
two ends are neither both `A`-ends nor both `B`-ends.  Suppose first that
such a path exists.  An internal vertex of a path `P_i` can be placed on
either side of an edge that splits `P_i` into a nonempty `A`-prefix and a
nonempty `B`-suffix; `a_i` can be placed only in the prefix and `b_i`
only in the suffix.  The definition of usability therefore lets us split
`P_i` and `P_j` so that `x` and `y` lie in opposite kinds of pieces.
Absorb the open interior of `Q` into the piece containing `x`.

The four split pieces are connected and disjoint.  The two `A`-pieces
are adjacent through the clique `A`, the two `B`-pieces are adjacent
through `B`, the two pieces from either original path are adjacent across
its splitting edge, and `Q` supplies one of the two cross-adjacencies.
Thus at most the other cross-adjacency is missing.  Each of the remaining
`r-2` unsplit paths is adjacent to every split piece through its `A`- or
`B`-end, and the unsplit paths are pairwise adjacent.  These `r+2`
connected branch sets form a `K_{r+2}^-`-minor model.

It remains to suppose that no usable cross-path exists.  Let `C` be a
component of `H-U`.  If `C` has neighbours on two distinct paths, a path
through `C` between any two such attachments must be unusable.  Fixing
attachments on two paths shows that all attachments of `C` are either
`A`-ends or all are `B`-ends.  Hence `|N_H(C)|<=r`, contrary to
`(r+1)`-connectivity.  Every component of `H-U` therefore attaches to
only one path `P_i`.

For each `i`, let `W_i` consist of the open interior of `P_i` together
with all components of `H-U` that attach to `P_i`.  A direct edge between
distinct paths is itself a cross-path, so the absence of a usable one
gives

\[
                         N_H(W_i)\subseteq\{a_i,b_i\}.
\]

Since `r>=2`, vertices on another path remain outside this set.  Thus a
nonempty `W_i` would give a vertex cut of order at most two, again a
contradiction.  Every `W_i` is empty.  Consequently `H` consists of the
two cliques `A,B` and the matching edges `a_i b_i`; every other
`A`--`B` edge would be a usable cross-path.  This graph has minimum degree
`r`, contradicting `(r+1)`-connectivity.  The contradiction completes the
proof.  \(\square\)

## Theorem 2 (two literal five-cliques)

Every six-connected graph containing two distinct literal `K_5`
subgraphs contains a `K_7^-` minor.  Equivalently, every six-connected
`K_7^-`-minor-free graph contains at most one literal `K_5`.

### Proof

Let `L_1,L_2` be distinct literal `K_5` subgraphs and put
`s=|L_1\cap L_2|`.

Suppose first that `s<=3`.  Set

\[
 Z=L_1\cap L_2,\qquad
 A=L_1-Z,\qquad B=L_2-Z,\qquad r=5-s.
\]

The graph `H=G-Z` is `(6-s)=(r+1)`-connected, while `A` and `B` are
disjoint literal `K_r` subgraphs.  Lemma 1 gives a
`K_{r+2}^-`-minor model in `H`.  Every branch set constructed there
contains a vertex of `A\cup B`.  Each vertex of `Z` is adjacent to every
vertex of `A\cup B`, and `Z` is a clique.  Adding the `s` vertices of `Z`
as singleton branch sets therefore gives a `K_7^-`-minor model in `G`.

If `s=4`, the six-vertex union `X=L_1\cup L_2` contains a literal
`K_6^-`.  A six-connected graph has at least seven vertices, so `G-X` is
nonempty.  Let `C` be any component of `G-X`.  If `N_G(C)` omitted a
vertex of `X`, then `N_G(C)\subseteq X` would be a vertex cut of order at
most five.  Hence `C` is adjacent to all six vertices of `X`.  The six
singleton vertices of `X`, together with `C` as one connected branch set,
form a `K_7^-`-minor model.  \(\square\)

## Corollary 3 (critical-host consequences)

Let `G` be a finite simple graph satisfying

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                              \tag{H}
\]

For each integer `i`, let `n_i` be the number of degree-`i` vertices.  Let
`b` be the number of degree-eight vertices lying in no literal `K_5`, and
put

\[
                  \tau=\sum_{i\ge10}(i-9)n_i.
\]

Then

\[
 n_7\le4,
 \qquad |E(G)|\ge4|V(G)|-2,
 \qquad b\ge20-n_7+\tau\ge16+\tau.                       \tag{1}
\]

### Proof

Theorem 2 permits at most one literal `K_5`.  The audited exact
degree-seven neighbourhood theorem says that every degree-seven vertex
lies in such a clique, and the audited private-triangle theorem says that
no literal `K_5` has five degree-seven vertices.  Hence `n_7<=4`.

Every other vertex has degree at least eight, so

\[
 2|E(G)|\ge7n_7+8\bigl(|V(G)|-n_7\bigr)
              =8|V(G)|-n_7
              \ge8|V(G)|-4.
\]

This proves the edge bound.  Finally, every degree-seven vertex and every
nonexceptional degree-eight vertex lies in the unique possible literal
`K_5`, and therefore

\[
                         n_7+(n_8-b)\le5.                 \tag{2}
\]

The audited Jakobsen defect calculation gives

\[
                         25\le2n_7+n_8-\tau.              \tag{3}
\]

Combining (2) and (3),

\[
 25\le (n_7+n_8-b)+n_7+b-\tau
     \le5+n_7+b-\tau.
\]

Thus `b>=20-n_7+tau`, and `n_7<=4` gives the last inequality in (1).
\(\square\)

## Theorem 4 (amplification when `n_7=4`)

Under (H), if `n_7=4`, then

\[
 2|E(G)|\le9|V(G)|-41,
 \qquad |V(G)|\ge37,
 \qquad n_8\ge33+\tau,
 \qquad b\ge32+\tau.                                    \tag{4}
\]

### Proof

All four degree-seven vertices lie in the unique literal `K_5`; write it
as `A=\{a_1,a_2,a_3,a_4,z\}`.  The exact degree-seven neighbourhood
theorem and Theorem 2 imply

\[
 N(a_i)=(A-\{a_i\})\mathbin{\dot\cup}T_i,
\]

where each `T_i` is a triangle anticomplete to `A-\{a_i\}`.  In
particular, the four triangles are pairwise disjoint and `z` is
anticomplete to all of them.

Put `H=G-A`.  We first show that `H` is four-connected.  If a set
`S\subseteq V(H)` with `|S|<=3` left components
`C_1,\ldots,C_q`, where `q>=2`, seven-connectivity would give

\[
 |N_A(C_j)|\ge7-|S|\qquad(1\le j\le q).                 \tag{5}
\]

Each `a_i` has neighbours in at most one component, because
`T_i-S` is connected whenever it is nonempty.  The vertex `z` can meet at
most all `q` components.  Counting component--`A` incidences in (5) gives

\[
 q(7-|S|)\le4+q,
\]

which is impossible for `q>=2` and `|S|<=3`.  Hence `H` is
four-connected.

Contract `A` to one vertex and call the resulting graph `J`.  No outside
vertex has two neighbours in `A`: a neighbour of any `a_i` outside `A`
lies in `T_i` and is anticomplete to the rest of `A`.  Thus the contraction
creates no parallel edges and

\[
 |V(J)|=|V(G)|-4,
 \qquad |E(J)|=|E(G)|-10.                               \tag{6}
\]

The graph `J` is five-connected.  A separator of order at most four not
containing the contracted vertex would also separate `G`; one containing
it would, after its removal, leave `H` minus at most three vertices.

The four disjoint triangles show that `|V(J)|>=13`.  Hence `J` is neither
`K_6` nor `K_{2,2,2,2}`.  It is not a nontrivial
`(K_{2,2,2,2},K_6,4)`-cockade either, because every such clique-sum has a
vertex cut of order four.  Since `J` is a minor of `G`, it remains
`K_7^-`-minor-free.  Jakobsen's extremal theorem and integrality therefore
give

\[
 2|E(J)|\le9|V(J)|-25.
\]

Substitution from (6) proves `2|E(G)|<=9|V(G)|-41`.  On the other hand,
Corollary 3 gives `2|E(G)|>=8|V(G)|-4`, so `|V(G)|>=37`.

Finally, the exact degree-defect identity and `n_7=4` give

\[
 41\le9|V(G)|-2|E(G)|=8+n_8-\tau,
\]

and hence `n_8>=33+tau`.  At most one degree-eight vertex is
nonexceptional, by (2), so `b>=n_8-1>=32+tau`.  \(\square\)

## Corollary 5 (sharpened global exceptional count)

Every graph satisfying (H) has

\[
                              b\ge17+\tau.                \tag{7}
\]

More precisely, one of the following holds:

1. `n_7<=3`, `|E(G)|>=4|V(G)|-1`, and `b>=17+tau`;
2. `n_7=4`, `|V(G)|>=37`, and `b>=32+tau`.

### Proof

If `n_7<=3`, Corollary 3 gives `b>=20-n_7+tau>=17+tau`.
The degree sum gives `2|E(G)|>=8|V(G)|-3`; its left side is even, so
`|E(G)|>=4|V(G)|-1`.  If `n_7=4`, Theorem 4 gives the second alternative,
which is stronger than (7).  \(\square\)

## Corollary 6 (exceptional anti-neighbourhoods when `n_7>0`)

Under (H), if `n_7>0`, then `G-N[u]` is connected for every exceptional
degree-eight vertex `u`.

### Proof

A degree-seven vertex lies in a literal `K_5`, so `G` contains such a
clique.  The audited low-degree exterior-component theorem gives at most
two components in `G-N[u]`.  If there were two, the audited two-component
literal-`K_5` exclusion would say that `G` contains no literal `K_5`, a
contradiction.  \(\square\)

## Dependencies and scope

Theorems 1 and 2 use only connectivity, Menger's theorem, and explicit
minor-model branch sets.  They do not use colouring criticality,
computation, or the earlier Niu--Zhang three-clique theorem.

Corollary 3 additionally uses the separately audited exact degree-seven
neighbourhood theorem, all-degree-seven literal-`K_5` exclusion, and
Jakobsen defect calculation.  It gives necessary conditions on a
hypothetical counterexample, not an upper bound on the exceptional
vertices and not a six-colourability theorem.

Theorem 4 uses Jakobsen's extremal theorem, including its exact cockade
alternative.  Its stronger numerical conclusions are conditional on
`n_7=4`; they are not global lower bounds.

Corollary 6 uses the separately audited degree-eight exterior-component
bound and two-component literal-`K_5` exclusion.  It does not settle
exceptional anti-neighbourhood connectivity in the `n_7=0` branch.

The exact density input is Jakobsen's theorem in the form quoted as
Theorem 2 by Boris Albar,
[*Coloration of `K_7^-`-minor free graphs*](https://arxiv.org/abs/1402.2806),
and already checked in the audited critical-host density reduction.
