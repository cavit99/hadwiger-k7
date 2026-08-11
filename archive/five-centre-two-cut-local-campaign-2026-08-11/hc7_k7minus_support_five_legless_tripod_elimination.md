# Legless-tripod elimination of the exact support-five residue

**Status:** written proof with a
[separate GREEN internal audit](hc7_k7minus_support_five_legless_tripod_elimination_audit.md).

This theorem eliminates one exact support-five configuration inside a
hypothetical counterexample.  It does not assert that an arbitrary two-cut
has this form, or that the preceding reductions to this form are exhaustive.

## 1. Exact setup

All graphs are finite and simple.  Let `G` be a seven-connected graph with
minimum degree at least eight.  Let

\[
                         Z=\{z_0,z_1,z_2,z_3,z_4\}
\]

be an independent set of degree-eight vertices, and put `F=G-Z`.  Suppose
that the following exact support-five data are present.

1. The vertices `p,q` are nonadjacent, and `F-{p,q}` has exactly two
   components `A,B`.  Both components are full to `{p,q}`: each of `p,q`
   has a neighbour in each of `A,B`.
2. No vertex of `Z` is adjacent to `p` or `q`.
3. There are five vertices

   \[
   R=\{r_0,r_{10},r_{11},r_{20},r_{21}\}\subseteq B
   \]

   such that `G[R]` is the complete tripartite graph with parts

   \[
                  \{r_0\},\qquad
                  \{r_{10},r_{11}\},\qquad
                  \{r_{20},r_{21}\}.
   \]

4. With

   \[
        T_0=\{r_0,r_{10},r_{20}\},\qquad
        T_1=\{r_0,r_{11},r_{21}\},
   \]

   the centre neighbourhoods on the `B`-side are exactly

   \[
   N_B(z_i)=T_0\quad(0\le i\le2),\qquad
   N_B(z_i)=T_1\quad(3\le i\le4).
   \]

5. The graph `Q=B-R` is nonempty and connected, and

   \[
                         N_F(Q)=R\cup\{p,q\}.            \tag{1.1}
   \]

For `0\le i\le4`, put

\[
                         P_i=N_A(z_i).                   \tag{1.2}
\]

The degree and neighbourhood assumptions give

\[
                         |P_i|=5                         \tag{1.3}
\]

for every `i`.  The exact residue from which this setup arises also has
`alpha(G[P_i])=2` and `omega(G[P_i])<=3`; the proof below does not need
those two additional local restrictions.

### Theorem 1.1 (exact support-five elimination)

Under the setup above, `G` contains `K_7^-` as a minor.

The proof first converts seven-connectivity into a relative boundary
inequality on `A`.  It then applies the tripod theorems of Robertson,
Seymour, and Thomas to an augmented graph on `A`.

## 2. The relative-seven inequality

For a nonempty set \(X\subseteq A\), define

\[
 \begin{aligned}
 M(X)&=\{i\in\{0,1,2,3,4\}:X\cap P_i\ne\varnothing\},\\
 L(X)&=\{s\in\{p,q\}:X\cap N_A(s)\ne\varnothing\}.
 \end{aligned}                                             \tag{2.1}
\]

Here \(N_A(X)=N_G(X)\cap A\), which is disjoint from \(X\) under the usual
open-neighbourhood convention.

### Lemma 2.1 (relative-seven inequality)

Every nonempty \(X\subseteq A\) satisfies

\[
             |N_A(X)|+|M(X)|+|L(X)|\ge7.                 \tag{2.2}
\]

#### Proof

There are no edges from `A` to `B`, because `A,B` are distinct components
of `F-{p,q}`.  The exact centre neighbourhoods and the absence of
centre-pole edges therefore give the disjoint decomposition

\[
 N_G(X)=N_A(X)\mathbin{\dot\cup}
        \{z_i:i\in M(X)\}\mathbin{\dot\cup}L(X).         \tag{2.3}
\]

Moreover, \(B\) is disjoint from \(X\cup N_G(X)\).  Hence \(N_G(X)\) separates
the nonempty set `X` from `B`.  Seven-connectivity gives
`|N_G(X)|>=7`, and (2.2) follows from (2.3).  \(\square\)

## 3. The augmented three-foot graph

Let

\[
                         J=G[A\cup\{z_0,z_1,z_2\}].      \tag{3.1}
\]

Obtain `hat J` from `J` by adjoining three new, pairwise nonadjacent
vertices `rho,sigma,tau` with

\[
 \begin{aligned}
 N_{\widehat J}(\rho)&=\{z_0,z_1,z_2\},\\
 N_{\widehat J}(\sigma)&=P_3,\\
 N_{\widehat J}(\tau)&=P_4.
 \end{aligned}                                             \tag{3.2}
\]

Thus `sigma` and `tau` replace, only for this auxiliary argument, the
incidences from `A` to `z_3` and `z_4`.

### Lemma 3.1

The graph `hat J` is three-connected.

#### Proof

Suppose that \(K\subseteq V(\widehat J)\) has order at most two and that
`hat J-K` has two distinct components `C,D`.  Every component of
`hat J-K` meets `A`.  Indeed, each of `z_0,z_1,z_2,sigma,tau` has five
neighbours in `A`, and `rho` has three neighbours among `z_0,z_1,z_2`.
After deleting at most two vertices, every surviving special vertex is
therefore connected to a surviving vertex of `A`.

Put

\[
                 X=C\cap A,\qquad Y=D\cap A,
                 \qquad k=|K\cap A|.                    \tag{3.3}
\]

Both `X` and `Y` are nonempty.  Since `C,D` are components of `hat J-K`,

\[
                         N_A(X),N_A(Y)\subseteq K\cap A. \tag{3.4}
\]

Lemma 2.1 and `|L(X)|,|L(Y)|<=2` give

\[
                         |M(X)|,|M(Y)|\ge5-k.            \tag{3.5}
\]

Associate with the five indices the five distinct vertices

\[
       s_0=z_0,\quad s_1=z_1,\quad s_2=z_2,\quad
       s_3=\sigma,\quad s_4=\tau.                      \tag{3.6}
\]

If `i in M(X) cap M(Y)`, then `s_i` has a neighbour in each of the
distinct components `C,D`.  Consequently `s_i in K`, and hence

\[
                         |M(X)\cap M(Y)|\le2-k.           \tag{3.7}
\]

On the other hand, both type sets lie in a five-element set, so (3.5)
gives

\[
                         |M(X)\cap M(Y)|\ge5-2k.          \tag{3.8}
\]

Inequalities (3.7)-(3.8) imply `k>=3`, contrary to `|K|<=2`.  Thus
deleting at most two vertices cannot disconnect `hat J`.  \(\square\)

### Lemma 3.2

The graph `hat J` is nonplanar.

#### Proof

For every `a in A`, all neighbours of `a` outside `A union Z` belong to
`{p,q}`.  In `hat J`, the edges from `a` to `z_3,z_4` are replaced
one-for-one by edges to `sigma,tau`.  Therefore

\[
                         d_{\widehat J}(a)\ge d_G(a)-2\ge6. \tag{3.9}
\]

The vertices `z_0,z_1,z_2` have degree six in `hat J`, the vertices
`sigma,tau` have degree five, and `rho` has degree three.  Consequently

\[
 \sum_{v\in V(\widehat J)}d_{\widehat J}(v)
       \ge6|A|+3\cdot6+2\cdot5+3
       =6|A|+31.                                          \tag{3.10}
\]

But `hat J` has `|A|+6` vertices, so a planar `hat J` would have degree
sum at most

\[
                         6(|A|+6)-12=6|A|+24,             \tag{3.11}
\]

a contradiction.  \(\square\)

## 4. A legless tripod

We use statements (3.4) and (3.5) of N. Robertson, P. D. Seymour, and
R. Thomas, [*Hadwiger's conjecture for `K_6`-free graphs*](https://thomas.math.gatech.edu/PAP/hadwiger.pdf),
Combinatorica **13** (1993), 279-361.

In their terminology, a triad is a tree with three prescribed leaves.  A
tripod on three prescribed feet consists of two triads, initially allowed
to reach those feet through three common legs.  Statement (3.5) says that,
in the absence of an order-at-most-two separation putting the three feet
on one side and at least two vertices on the other, either a tripod exists
or the graph has a disc drawing with the three feet on the boundary.
Statement (3.4) says that an existing tripod can be chosen legless if
there is no order-three separation `(L,R')` such that all three feet lie
in `L`, `|L|>=4`, and `|R'-L|>=2`.

Lemma 3.1 excludes the separation in (3.5), while Lemma 3.2 excludes its
disc-drawing alternative.  Thus `hat J` contains a tripod on
`rho,sigma,tau`.  It remains to verify the order-three hypothesis needed
to make that tripod legless.

### Lemma 4.1

There is no order-three separation `(L,R')` of `hat J` satisfying

\[
 \rho,\sigma,\tau\in L,\qquad |L|\ge4,
 \qquad |R'-L|\ge2.                                      \tag{4.1}
\]

#### Proof

Suppose otherwise, put `K=L cap R'`, and choose a component `C` of
`hat J-K` contained in `R'-L`.  The component `C` meets `A`.  Indeed,
`rho` lies in `L`, while every other special vertex has five neighbours
in `A`, at least two of which survive the deletion of `K`.

Set

\[
                         X=C\cap A,\qquad k=|K\cap A|. \tag{4.2}
\]

Then `X` is nonempty and `N_A(X) subseteq K cap A`.  Lemma 2.1 gives

\[
                         |M(X)|\ge5-k.                   \tag{4.3}
\]

First suppose `rho notin K`.  Then `rho in L-R'`.  If
`i in M(X)` for `i<=2`, the vertex `z_i` must belong to `K`: otherwise
the edge from `X` to `z_i` puts `z_i` in `C`, and `z_i rho` is an edge
between `R'-L` and `L-R'`.  If `3 in M(X)`, then `sigma in K`, since
`sigma` is a foot in `L`; similarly, `4 in M(X)` forces `tau in K`.
The five types have distinct representative vertices, so

\[
                         |M(X)|\le |K-A|=3-k,             \tag{4.4}
\]

contrary to (4.3).  Hence `rho in K`.

Let

\[
                         e=|K\cap\{\sigma,\tau\}|.       \tag{4.5}
\]

At most the three root types `0,1,2` can be met without placing their
representative vertex in the separator.  Each endpoint type `3,4` met by
`X` forces its foot into `K`.  Thus

\[
             5-k\le |M(X)|\le3+e\le3+(2-k)=5-k.          \tag{4.6}
\]

Equality holds throughout.  In particular,

* `e=2-k`;
* the vertices of `K-{rho}-(K cap A)` are endpoint feet, not any of
  `z_0,z_1,z_2`; and
* `X` meets all of `P_0,P_1,P_2`.

It follows that `z_0,z_1,z_2` all belong to `C`.

Now put

\[
                         Y=(L-R')\cap A.                 \tag{4.7}
\]

If `Y` were nonempty, then `N_A(Y) subseteq K cap A`.  Moreover, `Y`
could meet none of `P_0,P_1,P_2`, because the corresponding centre lies
in `C subseteq R'-L` and an edge to `Y` would cross the separation.
Applying Lemma 2.1 to `Y` gives

\[
 7\le |N_A(Y)|+|M(Y)|+|L(Y)|
   \le k+2+2\le6,                                        \tag{4.8}
\]

a contradiction.  Therefore `Y` is empty.

There are now three cases.  If `k=0`, equality in (4.6) gives
`K={rho,sigma,tau}`.  All three original roots lie in `C`, and there is
no vertex of `A` in `L-R'`; hence `L=K`, contrary to `|L|>=4`.

If `k=1`, exactly one of `sigma,tau` lies outside `K`; if `k=2`, both do.
Any such foot lies in `L-R'`.  Its five neighbours all belong to `A`.
None lies in `L-R'`, because `Y` is empty, and none lies in `R'-L`,
because the separation has no edge between its open sides.  All five
would therefore have to lie in `K cap A`, whose order is at most two.
This is impossible.  The three possible values of `k` are exhausted, and
the assumed separation does not exist.  \(\square\)

By Robertson-Seymour-Thomas (3.4), `hat J` therefore contains a legless
tripod on `rho,sigma,tau`.  Let its two triads be `T_1,T_2`, and define

\[
              C_j=V(T_j)-\{\rho,\sigma,\tau\}
              \qquad(j=1,2).                            \tag{4.9}
\]

The sets `C_1,C_2` are nonempty, disjoint, and connected in the original
graph `J`.  For each `j`, the neighbour in `T_j` of

* `rho` is one of `z_0,z_1,z_2`;
* `sigma` belongs to `P_3`; and
* `tau` belongs to `P_4`.

Consequently each `C_j` contains at least one of `z_0,z_1,z_2` and meets
both `P_3` and `P_4`.  Since the interiors are disjoint, their selected
neighbours of `rho` are distinct.  No artificial edge remains inside
either `C_j`, so their connectivity is genuine connectivity in `G`.

## 5. The explicit `K_7^-` model

The following four disjoint connected branch sets form a `K_4` model:

\[
 \begin{aligned}
 K_0&=\{r_0\},&
 K_1&=\{r_{10},r_{20}\},&
 K_2&=\{r_{11}\},&
 K_3&=\{r_{21}\}.
 \end{aligned}                                           \tag{5.1}
\]

Indeed, `r_{10}r_{20}` makes `K_1` connected.  Adjacency from `K_0` to
the other three bags follows from the edges
`r_0r_{10},r_0r_{11},r_0r_{21}`.  The remaining three adjacencies are
witnessed by

\[
                  r_{20}r_{11},\qquad
                  r_{10}r_{21},\qquad
                  r_{11}r_{21}.                          \tag{5.2}
\]

Define two more branch sets by

\[
                         D_1=C_1\cup\{z_3\},\qquad
                         D_2=C_2\cup\{z_4\}.             \tag{5.3}
\]

They are disjoint and connected: `C_1` meets `P_3`, and `C_2` meets
`P_4`.  They are adjacent to one another in both available directions.
A vertex of `C_1 cap P_4` is adjacent to `z_4 in D_2`, and a vertex of
`C_2 cap P_3` is adjacent to `z_3 in D_1`.

Each `D_j` is adjacent to all four bags in (5.1).  A vertex of
`C_j cap {z_0,z_1,z_2}` has neighbours `r_0,r_{10},r_{20}`, giving
adjacency to `K_0,K_1`.  The added vertex `z_3` or `z_4` has neighbours
`r_0,r_{11},r_{21}`, giving adjacency to `K_0,K_2,K_3`.

It remains to construct the seventh branch set.  Each `C_j` meets `A`,
and `G[A union {p}]` is connected.  Choose a first-hit path `W` in this
graph from `p` to `C_1 union C_2`: its last vertex `c` belongs to exactly
one of `C_1,C_2`, and no earlier vertex of `W` belongs to either.  Put

\[
                         D_3=Q\cup(V(W)-\{c\}).           \tag{5.4}
\]

The set `D_3` is connected.  The path segment `W-c` is connected and
contains `p`, while (1.1) gives an edge from `p` to the connected graph
`Q`.  It is disjoint from the six earlier bags: `Q subseteq B-R`, and the
first-hit choice makes `W-c` disjoint from `C_1 union C_2`; the path was
chosen inside `A union {p}`, so it also avoids `R union {z_3,z_4}`.

Equation (1.1) gives a `Q-r` edge for every `r in R`.  Hence `D_3` is
adjacent to each of `K_0,K_1,K_2,K_3`.  The last edge of `W` makes `D_3`
adjacent to the one of `D_1,D_2` containing `c`.

Thus the seven disjoint connected branch sets

\[
                         K_0,K_1,K_2,K_3,D_1,D_2,D_3     \tag{5.5}
\]

have every pairwise adjacency except possibly the adjacency from `D_3`
to the other one of `D_1,D_2`.  Equivalently, their quotient contains
`K_4` joined to a three-vertex path, which is `K_7^-`.  This proves
Theorem 1.1.  \(\square\)

## 6. Scope

The proof is unbounded and uses no finite enumeration.  It closes the
exact support-five residue in Section 1.  Its only external mathematical
input is the primary Robertson-Seymour-Thomas tripod pair (3.4)-(3.5),
used after the required separation hypotheses are proved directly.

The theorem does **not** prove that every two-cut of `G-Z` supplies the
five-vertex graph `R`, the two exact centre-neighbourhood triples, or the
connected full remainder `Q`.  Any global use of Theorem 1.1 still depends
on an independently proved exhaustive reduction to precisely those data.
