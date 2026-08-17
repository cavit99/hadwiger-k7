# Dense-boundary elimination for a returned three-component six-cut

**Status:** proved and independently audited, with a deterministic finite
check of the two six-vertex boundary classifications.  It eliminates an
unbounded part of the returned order-six cut in the six-connected `4n`
programme; it does not eliminate the two-component case, the remaining
sparse three-component boundaries, or prove the programme itself.

Write `K_7^-` for the graph obtained from `K_7` by deleting one edge.  For a
component `C` behind a six-cut `S`, put

\[
 \eta(C)=|E(G[C])|+|E_G(C,S)|-4|C|.
\]

## Theorem 1 (three-component dense-boundary bound)

Let `G` be a six-connected graph with no `K_7^-` minor.  Let `S` be a
vertex cut of order six such that `G-S` has exactly three components, each
adjacent to every vertex of `S`.  Put `B=G[S]`, and suppose

\[
 \Delta(B)\le3,
 \qquad |E(B[Q])|\le4\quad\hbox{for every }Q\in{S\choose4}.       \tag{1}
\]

The following statements hold.

1. If `|E(B)|=8`, then every component `C` of `G-S` satisfies
   `\eta(C)\le2`.
2. If `|E(B)|=7` and at least three vertices of `B` have degree three,
   then every component satisfies `\eta(C)\le3`.
3. Of the four seven-edge boundaries with degree sequence
   `3,3,2,2,2,2`, the two types IV and V displayed in Section 4 satisfy
   `\eta(C)\le4` for every component.
4. Type VI displayed in Section 5 satisfies `\eta(C)\le5` for every
   component.

Consequently, if `|E(G)|\ge4|V(G)|`, none of the boundary cases in the
four assertions can occur.  Thus all eight-edge boundaries and six of the
seven seven-edge boundaries allowed by (1) are eliminated.

The component orders are unrestricted.

## 1. The target-sensitive rooted inequality

Fix a component `C`, and write

\[
 c=|C|,\quad e_C=|E(G[C])|,\quad
 a_t=|E_G(C,\{t\})|,\quad P=\sum_{t\in S}a_t.          \tag{2}
\]

Put `Z=S-\{q,p\}` for distinct `p,q\in S`, and suppose that `B[Z]`
contains no four-cycle.  Either of the following two conditions implies

\[
 e_C+P-a_q-a_p+|E(B[Z])|\le3c+4.                     \tag{3}
\]

- `q` has degree three in `B` and `pq` is a nonedge; or
- `pq` is an edge and every vertex of `Z` is adjacent in `B` to at least
  one of `p,q`.

Indeed, `(G[C\cup Z],Z)` is internally four-connected.  A prohibited
rooted separation of order at most three, together with `p,q`, would give
a cut of `G` of order at most five, with either of the other two components
on the opposite side.

Suppose that `G[C\cup Z]` had a `Z`-rooted `K_4` model.  Denote the other
two components by `D,E`.  Under the first condition, its four rooted bags,
together with

\[
                         D\cup\{p\},\qquad E,\qquad\{q\},       \tag{4}
\]

would be seven disjoint connected bags.  Fullness of `D,E` supplies every
adjacency involving either component bag.  Since `qp` is a nonedge and
`d_B(q)=3`, all three boundary neighbours of `q` lie in `Z`; hence `q`
misses at most one rooted bag.  Thus (4) would complete a `K_7^-` model,
a contradiction.

Under the second condition use instead the three bags

\[
                             \{p,q\},\qquad D,\qquad E.          \tag{5}
\]

The first is connected and meets every rooted bag by the neighbourhood
cover hypothesis.  Fullness supplies all adjacencies from `D,E` to the
other five bags and to `\{p,q\}`.  Only the pair `D,E` may be nonadjacent,
so (5) again completes a `K_7^-` model.

Norin--Totschnig Lemma 9, applied to the internally four-connected rooted
pair with no rooted `K_4` model, now gives

\[
 |E(G[C\cup Z])|\le3|C\cup Z|-7=3c+5,
\]

and the inequality is strict here.  Indeed, inspect the proof of that
lemma.  The trisection branches give at most `3|C\cup Z|-8` in the small
case and at most `3|C\cup Z|-9` in the recursive case.  Thus equality at
`3|C\cup Z|-7` forces the planar outcome of the rooted trichotomy, with
all four roots on the outer face.  If the outer facial walk has length
`\lambda`, Euler's formula gives

\[
 |E(G[C\cup Z])|\le3|C\cup Z|-3-\lambda.
\]

The four distinct roots give `\lambda\ge4`; equality at `3|C\cup Z|-7`
would force `\lambda=4` and put the four roots consecutively on an outer
four-cycle.  That cycle would lie in `B[Z]`, contrary to the hypothesis.
Integrality proves (3).  This strict rooted estimate is the
target-sensitive step: fullness and the edge count alone do not forbid
the rooted model.

We shall also use

\[
 e_C\ge c-1,
 \qquad 2e_C+P\ge6c,
 \qquad 1\le a_t\le c\quad(t\in S).                  \tag{6}
\]

The first inequality is connectedness.  For the second, sum the degrees
of the vertices of `C`; all their neighbours lie in `C\cup S`, and
six-connectivity gives minimum degree at least six.  The last inequalities
use boundary-fullness and simplicity.

## 2. Eight boundary edges

Under (1), an eight-edge boundary is, up to isomorphism, one of the
following three graphs.  Edges such as `04` denote the pair `\{0,4\}`.

| type | boundary edges | pairs used in (3) | common weight |
|---|---|---|---:|
| I | `03,04,05,13,14,15,24,25` | `01,02,12,34,35,45` | `1/4` |
| II | `02,04,05,13,14,15,24,35` | `01,34,25` | `1/2` |
| III | `02,03,05,13,14,15,24,25` | `01,23,45` | `1/2` |

For completeness, the degree sum is sixteen.  The only possible degree
sequences are `3,3,3,3,2,2` and `3,3,3,3,3,1`; the latter leaves five
edges on four vertices after deleting the degree-one vertex and its
neighbour, contrary to (1).  If `D` is the set of four degree-three
vertices and `L=S-D`, degree summation gives
`|E(B[D])|-|E(B[L])|=4`.  Thus `B[L]` is empty and `B[D]` has four edges.
The latter graph is a four-cycle or a paw.  The two ways of attaching the
two degree-two vertices to the four-cycle, and the unique attachment to
the paw, give the table.

Every displayed pair is a boundary nonedge with a degree-three end, so
(3) applies; each displayed root graph has at most three edges and hence
no four-cycle.  In type I every vertex occurs in two displayed pairs; in
types II and III the pairs partition `S`.  Moreover, the respective sums
of `4-|E(B[Z])|` over the displayed pairs are `8,4,4`.

Adding (3) with the displayed weights gives, in every type,

\[
                 \frac32e_C+P\le\frac92c+2.           \tag{7}
\]

Add one half of `c-e_C\le1`, the connectedness inequality in (6).  We
obtain

\[
                         e_C+P\le4c+\frac52,
\]

and hence `\eta(C)\le2` by integrality, proving assertion 1.

## 3. Seven boundary edges with three cubic vertices

Four degree-three vertices are impossible: if `D` is their four-set and
`L=S-D`, degree summation gives
`|E(B[D])|-|E(B[L])|=5`, contrary to (1).  Hence the hypothesis in
assertion 2 gives degree sequence `3,3,3,2,2,1`.  Up to isomorphism the
three boundaries and the weighted pairs are as follows.

| type | boundary edges | pairs used in (3) | common weight |
|---|---|---|---:|
| I | `01,02,03,12,14,25,34` | `04,15,23` | `1/2` |
| II | `01,02,03,12,14,34,35` | `04,15,32` | `1/2` |
| III | `01,02,03,14,15,24,25` | `04,05,13,23` | `1/2` |

Here is a short classification.  On the three degree-three vertices and
the remaining three vertices, let `h` and `l` be the respective numbers
of internal edges.  Degree summation gives `h-l=2`.  Thus either the
degree-three vertices form a triangle and the only edge on the other side
joins the two degree-two vertices, or they form a path and the degree-one
vertex meets an end or the middle of that path.  These are I, II and III.
The four-set bound in (1) excludes the other placement of the sole edge in
the first case.

Every displayed root graph has at most three edges, so the strict form (3)
applies.  For types I and II, the three displayed pairs partition `S`, and

\[
       \sum\bigl(4-|E(B[S-\{q,p\}])|\bigr)=5.
\]

Half the three instances of (3), plus half of `c-e_C\le1`, yields

\[
                         \eta(C)\le3.
\]

For type III, the corresponding sum over the four displayed pairs is six.
After taking half of these four inequalities, the coefficients of `a_0`
and `a_3` are one and the other four attachment coefficients are
three-halves.  Add half of each of `a_0\le c` and `a_3\le c`, and then add
half of the second inequality in (6), written as

\[
                        -e_C-\frac12P\le-3c.
\]

The result is

\[
                         e_C+P\le4c+3.
\]

Thus `\eta(C)\le3` also in type III, proving assertion 2.

## 4. Two further seven-edge boundaries

Two of the four remaining degree-sequence `3,3,2,2,2,2` boundaries are

| type | boundary edges | pairs used in (3) | common weight |
|---|---|---|---:|
| IV | `01,02,03,12,34,35,45` | `04,05,13,23` | `1/2` |
| V | `01,02,03,14,15,24,35` | `04,05,12,13` | `1/2` |

The cubic vertices are `0,3` in IV and `0,1` in V.  Every displayed pair
is a nonedge with a cubic end, and every displayed root graph has two
edges, so (3) applies.  Take half of the four
inequalities.  The attachment coefficients at the two cubic vertices are
one and the other four coefficients are three-halves.  Add half of the two
attachment upper bounds at the cubic vertices, followed by half of the
degree inequality in (6), in the same way as for type III.  In both cases
the four constants `4-|E(B[Z])|` are all two.  The resulting inequality
is

\[
                            e_C+P\le4c+4,              \tag{8}
\]

which proves `\eta(C)\le4`.  The adjacent-cover branch of (3) also applies
to 03 in IV and 01 in V, but is not needed for this bound.  This proves
assertion 3.

## 5. Elimination at coefficient four

The sixth seven-edge boundary is

    VI: 01,02,03,12,14,35,45.

Its cubic vertices are 0 and 1.  Apply (3) to the omitted pairs
\(04,13,15\); each induced root graph has two edges.  Add these three
inequalities, the degree inequality in the form

\[
                         -2e_C-P+6c\le0,
\]

the attachment upper bound \(a_1-c\le0\), and the fullness bound
\(-a_2\le-1\).  The coefficients cancel exactly to give

\[
                           e_C+P-4c\le5.              \tag{9}
\]

This proves assertion 4.  The certificate is sharp for this inequality
system: for every \(c\ge4\), the vector

\[
 e_C=2c-5,\qquad
 (a_0,a_1,a_2,a_3,a_4,a_5)=(c,c,1,3,3,3)
\]

satisfies all four available instances of (3) and (6), with
\(\eta(C)=5\).

If the components of `G-S` are `C_1,C_2,C_3`, exact edge accounting gives

\[
 |E(G)|-4|V(G)|=|E(B)|+\sum_{i=1}^3\eta(C_i)-24.     \tag{10}
\]

With eight boundary edges, the right side is at most
`8+3\cdot2-24=-10`.  In the seven-edge cases from assertion 2 it is at
most `7+3\cdot3-24=-8`; for types IV and V it is at most
`7+3\cdot4-24=-5`; and for type VI it is at most
`7+3\cdot5-24=-2`.  Each contradicts `|E(G)|\ge4|V(G)|`.

This proves the theorem. `\square`

## 6. Residual structure and cross-component tools

Only type VII remains:

    VII: 01,02,03,14,24,35,45.

The strict rooted inequalities (3) still have no order-independent local
bound in this type.  For every integer \(c\ge2\), the numerical vector

\[
 e_C=c-1,\qquad
 (a_0,a_1,a_2,a_3,a_4,a_5)=(c,1,2,c,c,c)             \tag{11}
\]

satisfies every available instance of (3) and all the elementary
inequalities (6), while \(\eta(C)=c+2\).  Thus the local inequality system
is unbounded.  Equation (11) is a recession certificate, not a claim that
a graph realising it exists.

The following two composition lemmas record structural information which
is not captured by that local system.  For a pair \(P\in{S\choose2}\),
write \(Z_P=S-P\), and let \(B^P\) be the graph obtained from \(B\) by
completing \(Z_P\) to a clique.

### Lemma 2 (two rooted-\(K_4\) composition)

Let \(A_1,A_2,A_3\) be the three components of \(G-S\).  Suppose that
\(G[A_1\cup Z_P]\) has a \(Z_P\)-rooted \(K_4\) model and
\(G[A_2\cup Z_Q]\) has a \(Z_Q\)-rooted \(K_4\) model.  If

\[
                         |E(B^P\cup B^Q)|\ge14,       \tag{12}
\]

then \(G\) has a \(K_7^-\) minor.

#### Proof

For every \(s\in S\), merge the two model bags rooted at \(s\) when both
exist, retain the unique such bag when only one exists, and use the
singleton \(\{s\}\) when neither exists.  Bags merged at the same root
are connected through that root, and bags belonging to different roots
remain disjoint.  Two resulting root bags are adjacent whenever their
roots are adjacent in \(B\), or when the two roots both belong to \(Z_P\)
or both belong to \(Z_Q\).  Hence the six root bags contain a \(K_6^-\)
model by (12).  The connected component \(A_3\) is adjacent to each root
bag through its literal root.  Adding it as a seventh bag gives a
\(K_7^-\) model. \(\square\)

The compatibility check in (12) is finite.  Up to interchanging \(P,Q\),
there are eleven compatible pair-pairs in VI and ten in VII:

    VI:
    01/23, 01/24, 02/13, 04/12, 04/13, 04/15,
    05/13, 05/23, 05/34, 15/24, 15/34.

    VII:
    04/12, 04/13, 04/15, 04/23, 04/25,
    05/13, 05/23, 05/34, 15/34, 25/34.

### Lemma 3 (rooted-\(K_4\)/helper composition)

Fix \(P=\{p,q\}\), put \(Z=S-P\), and let \(A,D,E\) be the three
components of \(G-S\).  Suppose \(G[A\cup Z]\) has a \(Z\)-rooted
\(K_4\) model.  If

\[
                         a_p(D)+a_q(D)\le\eta(D)-1,   \tag{13}
\]

then \(G\) has a \(K_7^-\) minor.

#### Proof

Complete \(Z\) to a clique in \(G[D\cup Z]\).  The resulting graph has
\[
 4|D|+\eta(D)-a_p(D)-a_q(D)+6
 \ \ge\ 4(|D|+4)-9
\]
edges.  Its pair rooted at \(Z\) is internally four-connected by the
separator lift in Section 1.  Norin--Totschnig Lemma 12 therefore supplies
a \(Z\)-rooted \(K^*_{4,2}\) model.  The added root edges are not required
by such a model, so it exists in the original graph.

The larger pair
\[
             (G[D\cup Z\cup\{p\}],\,Z\cup\{p\})
\]
is internally five-connected: a prohibited rooted separation of order at
most four, together with \(q\), would lift to a cut of \(G\) of order at
most five.  The fifth-root augmentation lemma therefore chooses the
rooted \(K^*_{4,2}\) model with \(p\) in one helper bag.

Merge corresponding root bags of this model and the rooted \(K_4\) model
in \(A\).  The four merged bags are pairwise adjacent through the latter
model and each is adjacent to both helper bags; the helpers are adjacent
to each other.  Component \(E\) sees all four merged bags through \(Z\)
and sees the helper containing \(p\).  It may miss only the other helper.
These seven bags form a \(K_7^-\) model. \(\square\)

## Verification and exact scope

The deterministic script
[`hc7_k7minus_returned_three_component_dense_boundary_elimination_verify.py`](hc7_k7minus_returned_three_component_dense_boundary_elimination_verify.py)
enumerates all labelled graphs on the six boundary vertices, checks (1),
reduces them under all 720 relabellings, and verifies the displayed weighted
certificates with exact rational arithmetic.  It also confirms that the
seven-edge degree sequence `3,3,2,2,2,2` has four isomorphism classes and
that IV--VII are exactly those four classes.  Finally, it checks every
strict-root hypothesis, the adjacent-cover inputs, the two finite
cross-component compatibility lists, and the numerical vectors which show
the limits of the inequality system used here.

The theorem eliminates all three eight-edge boundary classes and six of
the seven seven-edge classes, for arbitrary component orders.  The sole
remaining seven-edge boundary has canonical edge set

```text
01,02,03,14,24,35,45.
```

It also leaves every boundary with at most six edges and the two-component
returned case.  No assertion is made that the rooted inequalities used
here alone close those cases.

For type VI, the exact linear certificate in Section 5 has value five and
is attained numerically, for example at $c=10$, by

    e_C=15, (a_0,...,a_5)=(10,10,1,3,3,3), eta=5.

For the remaining type VII, the recession vector (11) gives at $c=10$

    e_C=9, (a_0,...,a_5)=(10,1,2,10,10,10), eta=12.

These are certificates about the linear inequality system, not claims that
graphs realising the vectors exist.  They show why the final seven-edge
type requires the cross-component structural inputs above.

## External source

Sergey Norin and Agnès Totschnig,
*Every graph with no `K_7^\vee`-minor is 6-colorable*, Theorem 8 and
Lemmas 9 and 12,
[arXiv:2507.03244](https://arxiv.org/abs/2507.03244).

The fifth-root augmentation used in Lemma 3 is
[Lemma 1 of the five-separator reduction](../active/hc7_k7minus_e5_k5minus_cut_elimination.md#lemma-1-fifth-root-augmentation),
which has a separate internal audit in this repository.
