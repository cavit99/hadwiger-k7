# Degree-six cut capacity and exact excess

**Status:** active draft; written proof with a separate hash-pinned internal
audit.  The theorem is an unconditional reduction for the `4n-2` extremal
programme.  It does not prove the lobe-excess inequality isolated in
Corollary 2.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## Theorem 1 (degree-six cut capacity)

Let `H` be a finite simple six-connected graph with no `K_7^-` minor.  Let
`x` be a vertex of degree six, put `T=N_H(x)`, and let `r` be the number of
components of `H-T`.  Then

\[
 2\le r\le3.
\]

Every component of `H-T` is adjacent to every vertex of `T`.  Moreover:

1. if `r=3`, then every four vertices of `T` span at most four edges, and
   hence `|E(H[T])|\le10`;
2. if `r=2`, then every five vertices of `T` span at most eight edges, and
   hence `|E(H[T])|\le12`.

If `r=3` and one of the two components other than `\{x\}` is
non-singleton, then additionally

\[
 \Delta(H[T])\le3,
 \qquad |E(H[T])|\le9.                                \tag{1}
\]

### Proof

The singleton `\{x\}` is a component of `H-T`.  Any component `C` of
`H-T` has `N_H(C)\subseteq T`; six-connectivity and `|T|=6` therefore give

\[
 N_H(C)=T.                                                   \tag{2}
\]

There is at least one component other than `\{x\}`.  Otherwise `H` would
have seven vertices, and six-connectivity would make `H=K_7`, contrary to
the forbidden-minor hypothesis.  Thus `r\ge2`.

We use the following construction.  Choose `k` components
`C_1,\ldots,C_k` of `H-T`.  For `i<k`, choose distinct vertices
`t_i\in T` and take `C_i\cup\{t_i\}` as one branch set.  Take `C_k` as a
branch set by itself, and take every remaining vertex of `T` as a singleton
branch set.  These are seven branch sets: by (2), every branch set
containing a component is adjacent to every other branch set.  Thus the
only possible missing adjacencies are between the

\[
 6-(k-1)=7-k                                             \tag{3}
\]

unabsorbed singleton vertices of `T`.

If `r\ge5`, apply the construction with `k=5`.  Only two singleton
boundary branch sets remain, so there is at most one missing adjacency.
This is a `K_7^-` minor, a contradiction.  Hence `r\le4`.

Suppose `r=4`.  Apply the construction to all four components, choosing
any three vertices of `T` to remain singleton.  Those three vertices must
span at most one edge; otherwise the seven branch sets have at most one
missing adjacency.  This holds for every three-subset of `T`, so no two
edges of `H[T]` share an endpoint.  Thus `H[T]` is a matching.

We now exclude `r=4`.  Suppose first that one component `C` of `H-T` is
non-singleton, and choose any four-set `Q\subseteq T`.  The rooted pair

\[
 (H[C\cup Q],Q)
\]

is internally four-connected.  Indeed, a prohibited rooted separation of
order at most three, after adding the two vertices of `T-Q` to its
separator, would give a cut of `H` of order at most five.  The other three
components of `H-T` provide a nonempty opposite side, contradicting
six-connectivity.  The rooted graph has at least six vertices, so
Jørgensen's rooted-diamond theorem, in the form of Norin--Totschnig,
Lemma 10, gives a `Q`-rooted `K_4^-` model in `H[C\cup Q]`.

There are three other components and two vertices in `T-Q`.  Absorb one
of those vertices into each of two components, and retain the third
component as a bare branch set.  These three branch sets are pairwise
adjacent and each is adjacent to all four rooted bags, by (2).  Together
with the rooted diamond they form a `K_7^-` model, a contradiction.

Thus all four components of `H-T` are singletons.  Every vertex of `T`
then has four neighbours outside `T` and, because `H[T]` is a matching, at
most one neighbour inside `T`.  This contradicts the minimum degree six
implied by six-connectivity.  Hence `r\le3`.

Suppose `r=3`.  The branch-set construction leaves any prescribed
four-subset of `T` singleton.  It cannot span five or six edges, since
again there would be at most one missing adjacency.  Hence every
four-subset spans at most four edges.  Summing over the fifteen
four-subsets of `T`, each edge is counted six times, and therefore

\[
 6|E(H[T])|\le15\cdot4,
\]

which gives `|E(H[T])|\le10`.

If one component other than `\{x\}` is non-singleton and some
`z\in T` has four neighbours in `T`, choose four such neighbours as `Q`.
The same rooted-connectivity argument gives a `Q`-rooted `K_4^-` model in
that component.  Of the other two components, absorb the one vertex of
`T-(Q\cup\{z\})` into one and retain the other as a bare branch set; keep
`\{z\}` as the seventh bag.  Fullness supplies every adjacency involving
the two component bags, and the four literal `z-Q` edges supply the
adjacencies from `\{z\}` to the rooted bags.  Again only the rooted
diamond's missing edge may be absent.  This contradiction proves (1).

Finally suppose `r=2`.  The branch-set construction leaves any prescribed
five-set of `T` singleton.  It must span at most eight edges.  Summing over
the six five-subsets of `T`, each edge is counted four times, and therefore

\[
 4|E(H[T])|\le6\cdot8,
\]

which gives `|E(H[T])|\le12`.  \(\square\)

## Corollary 2 (exact lobe-excess identity)

Retain the hypotheses of Theorem 1.  Write the components of
`H-T` other than `\{x\}` as `C_1,\ldots,C_s`, so `s=r-1`, and define

\[
 e_i=|E(H[C_i])|+|E_H(C_i,T)|,
 \qquad
 \delta_i=e_i-4|C_i|.
\]

Then

\[
 |E(H)|=4|V(H)|-22+|E(H[T])|+\sum_{i=1}^{s}\delta_i. \tag{4}
\]

Consequently,

\[
 |E(H)|\le4|V(H)|-7
 \quad\Longleftrightarrow\quad
 |E(H[T])|+\sum_{i=1}^{s}\delta_i\le15.              \tag{5}
\]

### Proof

The edges of `H` are partitioned into the edges of `H[T]`, the six edges
from `x` to `T`, and the internal-plus-boundary edges counted by the
`e_i`.  Since

\[
 |V(H)|=7+\sum_{i=1}^{s}|C_i|,
\]

we obtain

\[
\begin{aligned}
 |E(H)|
   &=|E(H[T])|+6+\sum_i(4|C_i|+\delta_i)\\
   &=4|V(H)|-22+|E(H[T])|+\sum_i\delta_i.
\end{aligned}
\]

This is (4), and (5) follows by rearranging.  \(\square\)

## Proposition 3 (the cubic three-component row)

Retain the hypotheses of Theorem 1.  Suppose that `H-T` has three
components, say

\[
 \{x\},A,B,
\]

and that `H[T]` is cubic.  Then

\[
 \delta_A\le3,\qquad \delta_B\le3,
\]

and consequently

\[
 |E(H)|\le4|V(H)|-7.                                  \tag{6}
\]

### Proof

Put `a=|A|`, `e_A=|E(H[A])|`, and

\[
 p_A(t)=|E_H(\{t\},A)|,
 \qquad P_A=\sum_{t\in T}p_A(t)=|E_H(A,T)|.
\]

Let `(q,p)` be an ordered nonedge of `H[T]`, and put
`Z=T-\{q,p\}`.  The pair `(H[A\cup Z],Z)` is internally
four-connected: a rooted separation of order at most three, together with
the two omitted boundary vertices, would give a cut of `H` of order at
most five, with `B` on the opposite side.

The graph `H[A\cup Z]` has no `Z`-rooted `K_4` model.  Otherwise take its
four rooted bags together with

\[
 B\cup\{p\},\qquad \{x\},\qquad \{q\}.               \tag{7}
\]

The seven bags are disjoint and connected.  Fullness of `B` and the six
edges from `x` to `T` supply every adjacency involving the first two bags
in (7).  Since `H[T]` is cubic and `p` is a nonneighbour of `q`, the
vertex `q` is adjacent to three of the four roots in `Z`.  Thus at most one
adjacency, between `\{q\}` and a rooted bag, is absent.  This would be a
`K_7^-` model.

Norin--Totschnig Lemma 9 therefore gives

\[
 e_A+P_A-p_A(q)-p_A(p)+|E(H[Z])|\le3a+5.             \tag{8}
\]

There are twelve ordered nonedges of a cubic graph on six vertices.  On
summing (8) over them, each `p_A(t)` occurs with coefficient eight: there
are twelve positive occurrences and four subtractions.  Each boundary
edge occurs in exactly four of the sets `H[Z]`, since its two ends are
disjoint from exactly two undirected nonedges of `H[T]`.  As
`|E(H[T])|=9`, we obtain

\[
 12e_A+8P_A+4\cdot9\le12(3a+5),
\]

or equivalently

\[
 3e_A+2P_A\le9a+6.                                   \tag{9}
\]

Connectedness of `A` gives `e_A\ge a-1`.  Hence

\[
\begin{aligned}
 2\delta_A
   &=2e_A+2P_A-8a\\
   &=(3e_A+2P_A)-e_A-8a\\
   &\le7.
\end{aligned}
\]

The excess is integral, so `\delta_A\le3`.  The same argument gives
`\delta_B\le3`.  Therefore

\[
 |E(H[T])|+\delta_A+\delta_B\le9+3+3=15,
\]

and (6) follows from Corollary 2.  \(\square\)

## Proposition 4 (the eight-edge three-component row)

Retain the hypotheses of Theorem 1.  Suppose that `H-T` has three
components `\{x\},A,B` and

\[
 |E(H[T])|=8.
\]

Then

\[
 |E(H)|\le4|V(H)|-7.                                  \tag{10}
\]

### Proof

At least one of `A,B` is non-singleton unless (10) follows immediately:
if both are singletons, then `\delta_A=\delta_B=2`, and Corollary 2 is
strict.  Hence Theorem 1 gives `\Delta(H[T])\le3`.

#### The three boundary graphs

The degree sum of `H[T]` is sixteen.  A subcubic six-vertex graph with
this degree sum has degree sequence `3,3,3,3,2,2` or
`3,3,3,3,3,1`.  The latter is impossible: after deleting the degree-one
vertex and its neighbour, the other four vertices span five edges,
contrary to Theorem 1.

Let `D` be the four degree-three vertices and `L` the two degree-two
vertices.  The vertices of `L` are nonadjacent; otherwise `H[D]` would
have five edges.  Thus `H[D]` has four edges.  It is either a four-cycle or
a paw.  The boundary is consequently one of the following three labelled
graphs:

```text
I:   D={0,1,4,5}, E(D)={04,05,14,15},
     N(2)={4,5}, N(3)={0,1};

II:  D={0,1,4,5}, E(D)={04,05,14,15},
     N(2)={0,4}, N(3)={1,5};

III: D={0,1,2,5}, E(D)={02,05,15,25},
     N(3)={0,1}, N(4)={1,2}.
```

There are no further boundary edges.  For a four-cycle, the two
degree-two neighbourhoods partition its vertices, in either the opposite
or adjacent way, giving I and II.  For a paw, its cross-degrees determine
III uniquely.

#### A weighted rooted bound

Let `C` be either `A` or `B`, put `c=|C|`,
`e_C=|E(H[C])|`, and set

\[
 p_C(t)=|E_H(\{t\},C)|,
 \qquad P_C=\sum_{t\in T}p_C(t).
\]

Whenever `q` has boundary degree three and `p` is a boundary nonneighbour
of `q`, put `Z=T-\{q,p\}`.  Exactly as in Proposition 3, the pair
`(H[C\cup Z],Z)` is internally four-connected and has no `Z`-rooted
`K_4` model.  Hence

\[
 e_C+P_C-p_C(q)-p_C(p)+|E(H[Z])|\le3c+5.             \tag{11}
\]

Use the following inequalities (11), with the displayed common weight:

| boundary | omitted pairs | weight | sum of `5-|E(H[Z])|` |
|---|---|---:|---:|
| I | `01,02,12,34,35,45` | `1/4` | `14` |
| II | `01,34,25` | `1/2` | `7` |
| III | `01,23,45` | `1/2` | `7` |

In row I every boundary vertex occurs in two omitted pairs.  In rows II
and III the three pairs partition `T`.  Adding the weighted inequalities
to one half of the connectedness inequality

\[
 c-e_C\le1

\]

gives in every row

\[
 e_C+P_C-4c\le4.
\]

Thus

\[
 \delta_A\le4,
 \qquad \delta_B\le4.                                \tag{12}
\]

By Corollary 2, only equality in both inequalities of (12) could violate
(10).  We show that equality produces a `K_7` minor.

#### Equality structure

Let `\delta_C=4`.  Equality in the weighted proof gives

\[
 e_C=c-1,
 \qquad P_C=3c+5.                                    \tag{13}
\]

Every vertex of `C` has degree at least six, and hence

\[
 6c\le2e_C+P_C=5c+3.
\]

Therefore `c\le3`.  The case `c=1` is impossible because (13) would give
`P_C=8>6`.  If `c=3`, then `C` is a three-vertex path; equality in the
degree sum makes its two ends miss one boundary vertex each and its middle
vertex miss two.

Put `h_t=c-p_C(t)`.  Equality in the selected instances of (11), together
with the remaining instances, gives the following complete list:

| boundary | `c` | `(h_0,h_1,h_2,h_3,h_4,h_5)` |
|---|---:|---|
| I or II | `3` | `(1,1,0,0,1,1)` |
| III | `2` | `(0,1,0,0,0,0)` |
| III | `3` | `(1,1,1,0,0,1)` or `(0,2,0,1,1,0)` |

For example, in row I the equalities for `01,02,12` force
`h_0=h_1=1,h_2=0`, and the other three pairs give the symmetric
conclusion.  In row II, the equalities for the three displayed pairs and
the inequalities for `03,12,45` give the same vector.  Row III follows
from the displayed pairs and `04,12,35`.  The same equations exclude
`c=2` in rows I and II and force the sole missed incidence at vertex `1`
when `c=2` in row III.

#### Decoding equality into a rooted `K_6`

In rows I and II, let `A=a_0a_1a_2` and `B=b_0b_1b_2` be the two paths.
Every path vertex is adjacent to both `2` and `3`, and each of
`0,1,4,5` is missed by exactly one vertex of each path.  In `A`, choose a
vertex seeing both `0,1` and assign it to the root bag at `0`.  In `B`,
choose a vertex seeing both `4,5` and assign it to the root bag at `4`.
Each choice exists because only two of the three path vertices can miss an
end of the prescribed pair.

Four path vertices remain.  At least two of them see `1`, and at least two
see `5`, because each path has two neighbours of each degree-three root.
Choose distinct representatives seeing `1` and `5` and assign them to
those root bags.  Assign the last two path vertices to roots `2` and `3`.

The six resulting bags are pairwise adjacent.  The missing pairs `01` and
`45` are repaired by the vertices chosen to see both ends; the
four degree-three roots induce the four-cycle; and every path vertex sees
both degree-two roots, repairing all remaining boundary nonedges.  This is
a `T`-rooted `K_6` model.

It remains to treat III.  If both components have order two, orient their
edges so the first vertex is the one missing root `1`.  Assign the two
vertices of `A` to roots `0,1`, the two vertices of `B` to roots `3,4`,
and retain `2,5` as singleton bags.  Directly from the edge list of III,
these six rooted bags form a `K_6` model.

Otherwise choose a three-vertex path `C=c_0c_1c_2` and absorb the other
component into a root bag at a boundary vertex.  Up to reversing the path
and applying the boundary automorphism `(0 2)(3 4)`, its possible ordered
miss sets and a valid assignment of `c_0,c_1,c_2` to three root bags are:

| misses along `C` | assigned roots |
|---|---|
| `3 ; 1,4 ; 1` | `1,3,4` |
| `5 ; 0,2 ; 1` | `1,4,3` |
| `0 ; 1,2 ; 5` | `1,5,3` |
| `2 ; 0,5 ; 1` | `3,2,4` |
| `0 ; 1,5 ; 2` | `1,3,5` |
| `1 ; 3,4 ; 1` | `3,1,4` |

In each row, absorb the other component into the image of root `0` under
the same boundary automorphism.  This bag is adjacent to all five others
because that component is full to `T`.  The path edges, its displayed
attachments, and the edge list of III show directly that the other five
rooted bags are pairwise adjacent.  The table covers the two deficiency
vectors above: rows two to five and their symmetric images cover
`(1,1,1,0,0,1)`, while the first and last rows and their images cover
`(0,2,0,1,1,0)`.

Thus equality always gives a `T`-rooted `K_6` model.  Adding the singleton
bag `\{x\}` gives a `K_7` model, since `x` is adjacent to every root in
`T`.  This contradiction proves (10).  \(\square\)

## Lemma 5 (one-terminal cross-lobe composition)

Retain the hypotheses of Theorem 1, and suppose that

\[
 H-T=\{x\}\mathbin{\dot\cup}A\mathbin{\dot\cup}B.
\]

Choose distinct `p,q in T`, and put `Z=T-{p,q}`.  For a lobe `C` in
`{A,B}`, write

\[
 p_C(t)=|E_H(\{t\},C)|,
 \qquad
 \delta_C=|E(H[C])|+|E_H(C,T)|-4|C|.
\]

The following statements hold.

1. If

   \[
   \delta_C-p_C(p)+d_{H[T-p]}(q)\ge5,                \tag{14}
   \]

   then `H[C union (T-{p})]` has a `Z`-rooted
   `K^*_{4,2}` model in which `q` belongs to one of the two helper bags.

2. If

   \[
   \delta_C+|E(H[T-q])|\ge9,                         \tag{15}
   \]

   then `H[C union (T-{q})]` has a `Z`-rooted `K_4`
   model.

Consequently, if (14) holds for one lobe and (15) holds for the other,
then `H` contains a `K_7^-` minor.

### Proof

Let `C` be one lobe and put `c=|C|`.  The pair

\[
 (H[C\cup(T-\{p\})],T-\{p\})
\]

is internally five-connected.  Indeed, a rooted separation of order at
most four, after adding `p` to its separator, would give a cut of `H` of
order at most five, with the other lobe on the opposite side.

Put

\[
 \delta'=\delta_C-p_C(p),
 \qquad d'=d_{H[T-p]}(q).
\]

First suppose that `p_C(q)<=delta'-1`.  Omit `q` and complete `Z` to a
clique.  The resulting graph has `c+4` vertices and at least

\[
 4c+\delta'-p_C(q)+6\ge4c+7=4(c+4)-9
\]

edges.  Its rooted pair at `Z` is internally four-connected, so
Norin--Totschnig Lemma 12 gives a `Z`-rooted `K^*_{4,2}` model.

Otherwise `p_C(q)>=delta'`.  Retain `q` and again complete `Z` to a
clique.  Exact counting and (14) give

\[
 4c+\delta'+6+d'\ge4c+11=4(c+5)-9.
\]

The rooted pair is internally four-connected.  The only additional
possible open side is the singleton `{q}`, but its degree in the completed
graph is at least

\[
 p_C(q)+d'\ge\delta'+d'\ge5.
\]

Lemma 12 again supplies the rooted six-bag model.  In both cases the added
edges join nominated roots and are not required by the
`K^*_{4,2}` model, so they may be deleted.  The fifth-root augmentation
lemma, applied in the internally five-connected closed lobe, places `q` in
one helper.  This proves assertion 1.

For assertion 2, consider `F=H[C union (T-{q})]`, rooted at `Z`.  Since
`p_C(q)<=c`,

\[
\begin{aligned}
 |E(F)|
  &=4c+\delta_C-p_C(q)+|E(H[T-q])|\\
  &\ge3c+\delta_C+|E(H[T-q])|\\
  &\ge3c+9=3|V(F)|-6.
\end{aligned}
\]

The pair `(F,Z)` is internally four-connected unless its only prohibited
open side is the singleton `{p}`.  Indeed, every other separation of order
at most three lifts after adding `p,q` to a cut of `H` of order at most
five.  If the singleton exception does not occur, Lemma 9 gives a rooted
`K_4` model immediately from the displayed strict edge bound.

If the singleton exception does occur, then `d_F(p)<=3`.  Delete `p`.
The pair `(F-p,Z)` is internally four-connected by the same lift, and

\[
 |E(F-p)|\ge |E(F)|-3\ge3c+6
              =3|V(F-p)|-6.
\]

Lemma 9 now gives a `Z`-rooted `K_4` model in `F-p`, again a subgraph of
`F`.  This proves assertion 2 in all cases.

Finally suppose that assertion 1 holds in `A` and assertion 2 in `B`.
Write the four rooted bags in the `B`-lobe as `(Q_z:z in Z)`, and the
rooted bags and helpers in the `A`-lobe as

\[
 (R_z:z\in Z),\qquad U,V,
\]

where `q in U`.  For each `z in Z`, let `M_z=Q_z union R_z`.  These four
bags are connected and pairwise adjacent through the rooted `K_4` model;
each meets both `U` and `V`, and `U` meets `V`.  The singleton `{x}` is
adjacent to every `M_z` through `z` and to `U` through `q`; it may miss
only `V`.  Thus

\[
 \{M_z:z\in Z\},\quad U,\quad V,\quad\{x\}
\]

is an explicit `K_7^-` model.  The argument with the lobes interchanged is
identical.  \(\square\)

## Proposition 6 (the three-cubic-vertex seven-edge row)

Retain the hypotheses of Theorem 1.  Suppose that

\[
 H-T=\{x\}\mathbin{\dot\cup}A\mathbin{\dot\cup}B,
 \qquad |E(H[T])|=7,
\]

and that `H[T]` has three vertices of degree three.  Then

\[
 |E(H)|\le4|V(H)|-7.                                  \tag{16}
\]

### Proof

The degree sequence of `H[T]` is `3,3,3,2,2,1`.  Up to isomorphism and
with vertex set `{0,1,2,3,4,5}`, the boundary is one of

```text
I:   01,02,03,12,14,25,34;
II:  01,02,03,12,14,34,35;
III: 01,02,03,14,15,24,25.
```

Here is a short classification proof.  Let `D` be the three degree-three
vertices and `L=T-D`.  If `h=|E(H[D])|` and
`ell=|E(H[L])|`, degree summation gives `h-ell=2`.  If `ell=1`, the
four-set bound in Theorem 1 forces the edge of `H[L]` to join its two
degree-two vertices, giving I.  If `ell=0`, `H[D]` is a path and the
degree-one vertex of `L` meets either its middle or an end, giving III or
II.  These exhaust the possibilities.  The same degree count also shows
that four degree-three vertices would force five edges on a four-set, so
there is no omitted degree sequence.

Fix a lobe `C`, put `c=|C|`, `e_C=|E(H[C])|`, and use the attachment
notation of Lemma 5.  For I use the rooted inequalities (11) obtained by
omitting

\[
 04,\quad15,\quad23,
\]

each with weight `1/2`.  For II use `04,15,32` with the same weights.
In either case the pairs partition `T`, the values of
`5-|E(H[T-{p,q}])|` sum to eight, and adding half of
`c-e_C<=1` gives

\[
 \delta_C\le\frac92.
\]

Thus `delta_C<=4`, and applying this to `A,B` proves (16) in I and II.

For III use the four rooted inequalities obtained by omitting

\[
 04,\quad05,\quad13,\quad23,
\]

each with weight `1/2`.  Add half of each of

\[
 p_C(0)\le c,\qquad p_C(3)\le c,
\]

and half of the minimum-degree inequality

\[
 6c\le2e_C+\sum_{t\in T}p_C(t).
\]

The left side is exactly `delta_C`, while the right side is five.  Hence

\[
 \delta_C\le5.                                      \tag{17}
\]

If equality holds, every inequality used above is tight.  Substitution in
the four rooted inequalities gives

\[
 p_C(0)=p_C(3)=c,qquad
 p_C(1)=p_C(2)=3,qquad
 p_C(4)=p_C(5)=2.                                  \tag{18}
\]

Suppose that (16) fails.  By (17), after interchanging `A,B` if necessary,
we have `delta_A=5` and `delta_B>=4`.  In boundary III, vertex `4` has
degree two, `45` is a nonedge, and (18) gives `p_A(5)=2`.  Therefore

\[
 \delta_A-p_A(5)+d_{H[T-5]}(4)=5-2+2=5,
\]

so Lemma 5(1), with `(q,p)=(4,5)`, supplies the rooted six-bag model in
the `A`-lobe.  Also

\[
 \delta_B+|E(H[T-4])|\ge4+5=9,
\]

so Lemma 5(2) supplies the opposite rooted `K_4`.  Lemma 5 then gives a
`K_7^-` minor, a contradiction.  This proves (16).  \(\square\)

## Scope

If `J` is the rooted graph in the low-endpoint safe-atom reduction, adding
a new vertex adjacent precisely to its six terminals produces a graph `H`
of the form treated here.  The desired rooted bound

\[
 |E(J)|\le4|V(J)|-9
\]

is equivalent to `|E(H)|\le4|V(H)|-7`, and hence, by Corollary 2, to (5).
Theorem 1 bounds the boundary contribution but does not in general bound
the lobe excesses `\delta_i`.  Propositions 3, 4 and 6 close the
three-component rows with nine or eight boundary edges and the seven-edge
row whose boundary has three degree-three vertices.  The remaining
problem is a rooted-minor theorem controlling the two-component case, the
four seven-edge boundaries of degree sequence `3,3,2,2,2,2`, and the
three-component rows with at most six boundary edges.
