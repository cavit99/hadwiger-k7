# Pairwise-touching Kempe components do not force paired roots or descent

**Status:** barrier/counterexample to an intermediate claim; written proof;
separate internal audit GREEN at the revision recorded in the adjacent audit.
This is not a counterexample to `HC_7` and is not a model of the full
five-centre configuration.

Throughout, a set is *colourful* if it uses every colour in every proper
colouring with the specified number of colours.

## 1. Claim refuted

The following proposed local implication is false.

> Let `C` be a connected graph with two four-vertex sets `S,T` and a proper
> five-colouring using colours `r,0,1,2,3`.  Suppose that `S` and `T` each
> contain one vertex of every colour `0,1,2,3`, and that, for each `i`, the
> `r`--`i` component containing the `i`-coloured member of `S` also contains
> the `i`-coloured member of `T`.  Suppose these four components pairwise
> touch.  Let `L` be a seven-vertex boundary and put
> `Lambda(X)=N_L(X)`.  If
>
> \[
>       |N_C(X)|+|\Lambda(X)|\ge 7
>              \qquad(\varnothing\ne X\subseteq V(C)),       \tag{1.1}
> \]
>
> then either `C` has a `K_4`-minor model every branch set of which meets
> both `S` and `T`, or some nonempty proper `X subsetneq V(C)` has equality
> in (1.1).

The counterexample below satisfies the stronger inequality eight for every
nonempty proper `X`, has one of `S,T` colourful in every four-colouring of
the four-chromatic graph obtained by deleting the `r`-coloured vertex, and
has all four two-colour components meeting in one vertex.

## 2. Construction

Let `R` be the graph on `0,...,8` with edge set

```text
03 04 06 07   13 15 16 18   24 25 27 28
35 36 37      46 47 48      57 58 68.
```

This is the graph of the separately audited
[paired-colourful planar-core barrier](hc7_paired_colourful_planar_core_barrier.md).
It is four-connected and four-chromatic, and

\[
                        S=\{0,3,5,7\}                         \tag{2.1}
\]

is colourful in every proper four-colouring of `R`.  One proper
four-colouring has colour classes

\[
                     012,\quad 34,\quad 56,\quad 78.          \tag{2.2}
\]

Add four new vertices `9,10,11,12` and the edges

\[
                         93,\quad 10\,0,\quad 11\,0,\quad 12\,0.
                                                                    \tag{2.3}
\]

Put

\[
                         T=\{9,10,11,12\}.                       \tag{2.4}
\]

Finally add a vertex `h` adjacent to every member of \(S\cup T\).  Call
the resulting graph `C`.  Extend (2.2) by colouring `9,10,11,12` with
colours `0,1,2,3`, respectively, and give `h` the fresh colour `r`.
This is a proper five-colouring.  Both `S` and `T` contain one vertex of
each ordinary colour.

For each ordinary colour `i`, the `r`--`i` component containing the two
corresponding contacts contains `h`, because `h` is adjacent to both of
them.  Hence all four components meet at `h`; in particular, they pairwise
touch.  Moreover, `C-h` contains `R`, is four-colourable by the displayed
extension, and is therefore exactly four-chromatic.  Its set `S` remains
colourful in every proper four-colouring, because restriction to `R`
preserves colourfulness.

Take an independent seven-set

\[
                   L=\{z_S,z_T,u_1,u_2,u_3,u_4,u_5\}.           \tag{2.5}
\]

Join `z_S` precisely to `S`, join `z_T` precisely to `T`, and join every
`u_j` to every vertex of `C`.  These adjacencies define `Lambda(X)` in
(1.1).

## 3. No paired-rooted `K_4` model

### Proposition 3.1

There are no four pairwise disjoint connected vertex sets in `C` each of
which meets both `S` and `T`.  In particular, there is no paired-rooted
`K_4`-minor model.

#### Proof

If four such connected sets existed, the orders of `S` and `T` would force
each set to contain exactly one member of `S` and exactly one member of
`T`.

The vertex `9` has only `3,h` as neighbours in `C`.  Thus a connected set
containing `9` but not `h` must also contain `3` before it can reach its
member of `S`.  Similarly, each of `10,11,12` has only `0,h` as neighbours,
so a connected set containing one of these vertices but not `h` must also
contain `0`.  Disjointness permits at most one of the latter three sets to
contain `0`, and at most one set contains `3`.  Consequently at least two
of the four connected sets must contain `h`, contradicting disjointness.
\(\square\)

## 4. Strict relative inequality

### Proposition 4.1

For every nonempty proper `X subsetneq V(C)`,

\[
                         |N_C(X)|+|\Lambda(X)|\ge8.              \tag{4.1}
\]

For `X=V(C)`, the left side of (1.1) is exactly seven.

#### Proof

Every nonempty `X` meets all five universal boundary neighbourhoods, so

\[
 |N_C(X)|+|\Lambda(X)|
 =|N_C(X)|+5+mathbf 1_{X\cap S\ne\varnothing}
                 +\mathbf 1_{X\cap T\ne\varnothing}.           \tag{4.2}
\]

The graph `C` is two-connected.  Indeed, deleting `h` leaves `R` with each
new vertex attached to its neighbour in (2.3); deleting any other vertex
leaves the four-connected graph `R` minus at most one vertex connected,
while `h` supplies an alternative attachment for every new vertex and
still has a neighbour in the remaining copy of `R`.

If a proper `X` meets both `S` and `T`, connectedness gives
`|N_C(X)| at least 1`, and (4.2) gives eight.  If it meets exactly one of
the two sets, then `|N_C(X)| at least 2`: otherwise its unique external
neighbour would be a cutvertex, since at least three vertices of the
missed four-set remain beyond it.  Again (4.2) gives eight.

Suppose finally that `X` meets neither set.  If `h in X`, all eight
vertices of \(S\cup T\) lie in `N_C(X)`.  If `h notin X`, then `X` is a
nonempty subset of `V(R)-S`.  Four-connectivity of `R` gives
`|N_R(X)| at least 4`: if this neighbourhood had order at most three,
some member of the four-set `S` would lie beyond it, making
`N_R(X)` a separator of order at most three.  Thus (4.2) is at least nine
in the first subcase and at least nine in the second.

For `X=V(C)`, its internal neighbourhood is empty and it meets both contact
sets, so (4.2) equals seven. \(\square\)

The graph `C` itself has no `K_5` subgraph.  A clique avoiding `h` lies in
the planar graph `R`, apart from vertices of degree one in `C-h`; a clique
containing `h` would require a `K_4` inside \(S\cup T\), but each member of
`T` has only one neighbour in \(S\cup T\) and `S` is not a clique.

## 5. Exact scope and repair

The construction refutes the inference

\[
 \text{pairwise-touching common-hole components}
 +\text{relative seven-connectivity}
 \Longrightarrow
 \text{paired-rooted `K_4` or strict order-seven descent}.       \tag{5.1}
\]

It does not realize the full five-centre host.  In particular, the five
universal boundary vertices do not have the pole and degree-eight centre
profiles of the `b=2` configuration, and the augmented graph is not claimed
to be seven-connected, seven-chromatic, minor-critical, or `K_5`-subgraph
free.  It also has none of the proper-minor colouring responses of the
hypothetical counterexample.

Thus (5.1) cannot be repaired by the relative boundary inequality alone.
A positive continuation must use at least one omitted host-specific input:
the exact pole/centre contact budgets, the proper-minor response colourings,
or a model interaction stronger than pairwise touching.
