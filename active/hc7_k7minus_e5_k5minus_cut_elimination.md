# Dense five-separator reductions in a minimum `4n-7` enemy

**Status:** written unbounded reduction; separate internal audit.  This
eliminates the nine-edge five-separator case and reduces the eight-edge
case to one exact configuration in the auxiliary statement `(E5)` below.
It does not prove `(E5)`, the `4n-2` seven-connected extremal target, or
the `K_7^-` six-colour conjecture.

Write `K_7^-` for `K_7` with one edge deleted.  Recall the auxiliary
extremal statement

> **(E5).** Every five-connected graph `G` with
> `|E(G)| >= 4|V(G)|-7` contains a `K_7^-` minor.

An **E5 enemy** satisfies the connectivity and density hypotheses of
`(E5)` but has no `K_7^-` minor.  A minimum E5 enemy is chosen first with
minimum order and, subject to that, with minimum size.

The proof uses the following rooted-model augmentation.  In a
`Z`-rooted `K^*_{4,2}` model, the four root bags are each adjacent to two
adjacent helper bags; no adjacency between distinct root bags is part of
the definition.

## Lemma 1 (fifth-root augmentation)

Let `H` be a graph, let `S=Z union {x}`, where `|Z|=4`, and suppose that
`(H,S)` is internally five-connected.  If `H` has a `Z`-rooted
`K^*_{4,2}` model, then it has such a model in which `x` belongs to one of
the two helper bags.

### Proof

Among all `Z`-rooted `K^*_{4,2}` models, choose one whose two helper bags
`U,V` have maximum total order.  Subject to this, minimise the sum of the
orders of the four root bags `R_1,...,R_4`.  Let `z_i` be the member of
`Z` in `R_i`.

For each `i`, put

```text
P_i = {r in R_i : r has a neighbour in U union V}.
```

We first prove that `|P_i|=1`.  Both helpers have a neighbour in `R_i`, so
`P_i` is nonempty.  Suppose that `|P_i|>=2`.  There are distinct vertices
`u,v in R_i` such that `u` has a neighbour in `U` and `v` has a neighbour
in `V`: if no such distinct choice existed, the two nonempty helper-contact
sets would both be the same singleton.

Take a minimal tree in `H[R_i]` containing `z_i,u,v`.  Minimality of the
root bag makes its vertex set all of `R_i`.  One of `u,v`, say `u`, is a
leaf of this tree and is different from `z_i`.  Move `u` from `R_i` into
`U`.  The enlarged helper remains connected because `u` has a neighbour
in `U`.  The reduced root bag remains connected.  It still meets `U`
through the tree edge formerly joining `u` to `R_i-{u}`, and it still
meets `V` through `v`.  Every other required model adjacency is unchanged.
This increases `|U union V|`, contrary to its choice.  Hence `|P_i|=1`.

Next, no component of

```text
H - (R_1 union ... union R_4 union U union V)
```

has a neighbour in `U union V`.  Such a component could be absorbed in a
helper that it meets, again increasing `|U union V|` without losing a
model adjacency.

It follows that every neighbour of `U union V` outside `U union V` belongs
to the set `P_1 union ... union P_4`, which has order four.  If
`x notin U union V`, let

```text
Q = N_H(U union V) - (U union V).
```

Then

```text
(V(H)-(U union V), (U union V) union Q)
```

is a separation of `(H,S)` of order at most four, with nonempty second
open side `U union V`.  Indeed, the four vertices of `Z` lie in the root
bags and `x` was assumed outside the helpers.  This contradicts internal
five-connectivity.  Therefore `x` belongs to one of `U,V`.  \(\square\)

## Lemma 2 (cover-indexed virtual root-edge lifting)

Let `G` be a five-connected graph and let `S` be a vertex cut of order
five.  Let `C_0,...,C_{r-1}` be distinct components of `G-S`, where
`r>=2`.  Choose `x in S`, put `Z=S-{x}`, and let `F` be a set of
nonedges of `G[S]` such that

```text
G[Z]+(F restricted to pairs in Z) is a clique.           (1)
```

Suppose that the graph with edge set `F` has a vertex cover `A subseteq S`
of order `c<=r-2`.

Put `H=G[S union C_0]+F`.  Suppose that `(H,Z)` is internally
four-connected and

```text
|E(H)| >= 4|V(H)|-9.                                  (2)
```

Then `G` contains a `K_7^-` minor.

### Proof

Assign the members of `A` injectively to `C_1,...,C_c`, and assign every
edge of `F` to one of its ends in `A`.  For `a in A`, the component
assigned to `a` contains a connected subgraph meeting a neighbour of `a`
and a neighbour of every other end of an edge assigned to `a`.  Contracting
that subgraph into `a` realises all those virtual edges simultaneously.
The assigned components are distinct, so all of `F` can be realised at
once.  In particular, `H` is a minor of `G` after the other components are
deleted.  More importantly, the original pair
`(G[S union C_0],S)` is internally five-connected, and adding `F`
preserves that property.

By (2) and Norin--Totschnig Lemma 12, `H` has a `Z`-rooted
`K^*_{4,2}` model.  Lemma 1 lets us choose it with `x` in one helper.
The four root bags are pairwise adjacent in `H`, because the edges of `F`
with both ends in `Z` complete `G[Z]` to a clique.

Lift the model back to `G`.  For each `a in A`, enlarge the model bag
containing `a` by the connected subgraph selected in the component assigned
to `a`.  The enlarged bag remains connected, and its edges to the other
ends realise every virtual model adjacency assigned to `a`.  Different
cover vertices use different components, so the six bags remain disjoint.

The six lifted model bags are pairwise adjacent.  Retain `C_{c+1}` as a
seventh branch set.  It meets all four root bags through `Z` and the helper
containing `x` through `x`; it may miss only the other helper.  These are
the branch sets of a `K_7^-` model.  \(\square\)

For density bookkeeping, if

```text
delta(C_0)=|E(G[C_0])|+|E_G(C_0,S)|-4|C_0|
```

and `k=|E(G[S])|`, then (2) is exactly

```text
delta(C_0)+k+|F| >= 11.                              (3)
```

A useful sufficient condition for the connectivity hypothesis is
`d_{G[S union C_0]}(x)>=4`.  Indeed, a separation of `(H,Z)` of order at
most three can be converted to a separation of `(H,S)` of order at most
four unless its second open side is the singleton `{x}`; the degree bound
excludes that last case.  This qualification is necessary: internal
five-connectivity of `(H,S)` alone does not exclude a boundary singleton
of degree three in `H`.

## Theorem 3 (`K_5^-` cut elimination)

Let `G` be a minimum E5 enemy.  No vertex cut `S` of order five induces
`K_5^-`.

### Proof

Suppose that `S` is such a cut.  Write

```text
S = Z union {x},
```

where `xy` is the unique missing edge of `G[S]` and `Z=S-{x}`.  Thus
`G[Z]` is a literal `K_4`.

Every component of `G-S` is adjacent to every vertex of `S`; otherwise
its neighbourhood would be a cut of order at most four.  Let `D` be one
component of `G-S`, let `C` be the union of all the other components, and
put

```text
A = S union C,        B = S union D.
```

The graph `G[A]+xy` is a proper minor of `G`.  To see this, take an
`x`--`y` path whose open interior lies in one component contained in `D`,
contract all but its last edge, and delete the remaining vertices of `D`
and any unwanted edges.  Moreover, `(G[A],S)` is internally
five-connected.  Completing `S` to a clique therefore makes `G[A]+xy`
five-connected.  Since it is target-free and has smaller order than `G`,
minimality gives

```text
|E(G[A]+xy)| <= 4|A|-8,
```

and hence

```text
|E(G[A])| <= 4|A|-9.                                  (1)
```

The same argument gives

```text
|E(G[B])| <= 4|B|-9.                                  (2)
```

As `|E(G[S])|=9` and `|A|+|B|=|V(G)|+5`, (1) and (2)
give

```text
|E(G)| = |E(G[A])|+|E(G[B])|-9
       <= 4|V(G)|-7.
```

The reverse inequality is part of the definition of an E5 enemy.  Thus
equality holds throughout.  In particular,

```text
|E(G[A])| = 4|A|-9.                                   (3)
```

We next check the rooted theorem's connectivity hypothesis.  The pair
`(G[A],Z)` is internally four-connected.  Otherwise let `(L,R)` be a
separation of `(G[A],Z)` of order at most three with `R-L` nonempty.  If
`x` is not in `R-L`, this already contradicts the internal
five-connectivity of `(G[A],S)`.  If `x in R-L` and `R-L` has another
vertex, adding `x` to `L` gives a separation of `(G[A],S)` of order at
most four.  Finally, if `R-L={x}`, then all neighbours of `x` in `G[A]`
belong to `L intersect R`.  This is impossible: `x` has its three
neighbours in `S-{x,y}` and at least one neighbour in `C`.

By (3) and Norin--Totschnig Lemma 12, `G[A]` has a `Z`-rooted
`K^*_{4,2}` model.  Lemma 1 supplies such a model with `x` in one helper
bag.  Its four root bags are pairwise adjacent because they contain the
four vertices of the clique `G[Z]`.  Together with the two adjacent
helpers, they therefore form a `K_6` model.

Use the connected subgraph `D` as a seventh branch set.  It is adjacent to
all four root bags through the vertices of `Z`, and to the helper
containing `x` through `x`.  It may fail to meet only the other helper.
The resulting seven branch sets form a `K_7^-` model in `G`, a
contradiction.  \(\square\)

## Exact density consequence

The equality argument also records the structure that would have preceded
the contradiction.  If the components of `G-S` are `C_1,...,C_r` and

```text
delta_i = |E(G[C_i])|+|E_G(C_i,S)|-4|C_i|,
```

then applying the cap argument to every nonempty proper subfamily gives
`sum_{i in I} delta_i=2`.  Hence every `delta_i=2`, while the global
equality gives `sum_i delta_i=4`; consequently `r=2`.  The rooted
augmentation above eliminates this entire exact two-cap configuration.

## Theorem 4 (eight boundary edges)

Let `G` be a minimum E5 enemy and let `S` be a vertex cut of order five
with `|E(G[S])|=8`.

1. The two nonedges of `G[S]` are independent.
2. The graph `G-S` has exactly two components.
3. Label the missing edges `xy` and `zw`, and let `t` be the fifth
   boundary vertex.  After naming the two components `C,D` suitably,
   there are disjoint `x`--`y` and `z`--`w` paths with open interiors in
   `C`, there are no such two paths through `D`, and, with

   ```text
   delta(L)=|E(G[L])|+|E_G(L,S)|-4|L|,
   q=|E(G)|-(4|V(G)|-7),
   ```

   one has

   ```text
   delta(C) >= q+4,             delta(D) <= 1.          (4)
   ```

### Proof

First suppose that the two missing edges have a common end `x`, say they
are `xy,xz`.  A connected component of `G-S`, being full to `S`, contains
a connected subgraph meeting `x,y,z`.  Absorb that subgraph into the
singleton bag `{x}`.  This realises both missing edges simultaneously and
therefore completes `S` to a clique in a minor.

If `G-S` has at least three components, use one component for this
completion and retain two others.  The five completed boundary bags and
the two retained full components form a `K_7^-` model; only the two
retained components may be nonadjacent.

It remains that `G-S` has two components.  For either closed shore, the
opposite component realises both virtual edges.  The completed shore is a
proper target-free five-connected minor of `G`.  Minimality gives

```text
|E(G[S union C])| <= 4|S union C|-10
```

and the analogous inequality for the other component.  Subtracting the
eight boundary edges gives

```text
|E(G)| <= 4|V(G)|-8,
```

contrary to the E5 density.  This proves assertion 1.

We now assume that the missing edges are the independent edges `xy,zw`.
If `G-S` has at least four components, use one component to realise `xy`
and a second to realise `zw`, by paths with open interiors in their
respective components.  Retain two further components.  Splitting each
path at one edge between the two corresponding boundary bags completes
the five boundary bags to a clique.  The two retained full components are
the sixth and seventh bags and have the unique possible missing adjacency.
Thus `G-S` has at most three components.

We record the exact obstruction to using one component for both missing
edges.  Let `L` be a component of `G-S`, and put

```text
H_L=G[L union S]-t,             X={x,z,y,w}.
```

The pair `(H_L,X)` is internally four-connected.  Indeed, a separation of
this pair of order at most three becomes a separation of
`(G[L union S],S)` of order at most four by putting `t` in the separator.

Apply the Robertson--Seymour--Thomas Two Paths Theorem to the cyclically
ordered roots `x,z,y,w`.  Either `H_L` contains disjoint `x`--`y` and
`z`--`w` paths, or it has a disc drawing with these four roots on the
boundary in that order.  The theorem's separation outcome is excluded by
the preceding internal connectivity.  In the disc outcome the outer face
has length at least four, and hence

```text
|E(H_L)| <= 3|V(H_L)|-7.                              (5)
```

Let `p_t=|E_G({t},L)|`.  Since the four roots induce a four-cycle,

```text
|E(H_L)|=4|L|+delta(L)-p_t+4.
```

Combining this identity with (5), and using `p_t<=|L|`, gives

```text
delta(L) <= 1                                         (6)
```

whenever the two prescribed paths do not exist.

If `G-S` had three components and none supplied the two paths, (6) would
give `sum_L delta(L)<=3`.  On the other hand, direct edge accounting gives

```text
sum_L delta(L)=q+5>=5.                                (7)
```

Thus one component supplies the two paths.  They complete the boundary
clique, while the other two components supply the last two branch sets,
again giving a `K_7^-` model.  This proves assertion 2.

Let the two components now be `C,D`.  Equation (7) shows that at least one
has excess at least three, so (6) makes it a linked component; call it
`C`.  Use its two disjoint paths to complete the opposite closed shore
`G[S union D]` to a clique.  The completed shore is a proper target-free
five-connected minor.  Minimality gives

```text
|E(G[S union D])|+2 <= 4|S union D|-8,
```

which is exactly `delta(D)<=2`.  If equality `delta(D)=2` held, (6) would
make `D` linked as well.  Completing the other shore through `D` would
then give `delta(C)<=2`, contrary to (7).  Hence `delta(D)<=1`.  Moreover,
`D` is not linked: if it were, completing the other shore through `D`
would give `delta(C)<=2`, and then `delta(C)+delta(D)<=3`, again
contradicting (7).  Finally, (7) gives `delta(C)>=q+4`.  This proves
assertion 3.
\(\square\)

## Lemma 5 (clique-cap bound)

Let `G` be a minimum E5 enemy, let `S` be a cut of order five, and let
`C_1,...,C_r` be the components of `G-S`.  Put `J=G[S]`, and suppose that
the complement of `J` has a vertex cover of order at most `r-1`.  Then,
for every `i`,

```text
delta(C_i)<=2.                                         (8)
```

### Proof

Fix `i` and assign distinct components other than `C_i` to the vertices of
a cover of the missing edges of `J`.  Assign every missing edge to one of
its ends in that cover.  In the component assigned to a cover vertex `a`,
take a connected subgraph meeting a neighbour of `a` and a neighbour of
every other end assigned to `a`, and contract it into `a`.  This shows that

```text
G[S union C_i]+E(complement(J))
```

is a proper minor of `G`.  The pair `(G[S union C_i],S)` is internally
five-connected, and completing `S` to a clique therefore makes this minor
five-connected.  It is target-free.  Minimality of `G` gives

```text
4|C_i|+delta(C_i)+10
   <= 4(|C_i|+5)-8,
```

which is (8).  \(\square\)

For later use, direct edge accounting gives

```text
sum_i delta(C_i)=q+13-|E(J)|.                          (9)
```

## Theorem 6 (four or five components)

Let `G` be a minimum E5 enemy and let `S` be a cut of order five.  Then
`G-S` does not have five components.  If it has four components, then
`G[S]` is edgeless.

### Proof

Suppose first that `G-S` has five components.  If `ab` were an edge of
`J=G[S]`, let `c,d,e` be the other boundary vertices and let
`U_1,...,U_5` be the five components.  The seven sets

```text
{a}, {b}, U_1 union {c}, U_2 union {d}, U_3 union {e}, U_4, U_5
```

are connected and pairwise adjacent except possibly for `U_4,U_5`.
They form a `K_7^-` model.  Hence `J` is edgeless.  The complement of `J`
has a vertex cover of order four, so Lemma 5 gives
`delta(C_i)<=2` for all five components.  This contradicts (9), whose
right side is at least thirteen.

Now suppose that `G-S` has four components and `J` is nonempty.  The graph
`J` is triangle-free.  Indeed, if `a,b,c` formed a triangle and `d,e` were
the other boundary vertices, the seven sets

```text
{a}, {b}, {c}, U_1 union {d}, U_2 union {e}, U_3, U_4
```

would again be a `K_7^-` model, with only `U_3,U_4` possibly nonadjacent.
Thus Mantel's theorem gives `|E(J)|<=6`.

As `J` contains an edge, the complement of `J` has a vertex cover of order
at most three: take the three vertices outside the ends of that edge.
Lemma 5 and (9) now give

```text
q+13-|E(J)| <= 8,
```

so `5<=|E(J)|<=6`.  In either case some component `C_0` has
`delta(C_0)=2`.

If `|E(J)|=6`, equality in Mantel's theorem gives `J=K_{2,3}`.  Write its
parts as `{x,a}` and `{b,c,d}`, and put `Z=S-{x}`.  Then `J[Z]` is the
star with centre `a`.  Set

```text
F={bc,bd,cd}.
```

The set `{b,c}` covers `F`, the graph `J[Z]+F` is complete, and

```text
delta(C_0)+|E(J)|+|F|=2+6+3=11.
```

The omitted vertex `x` has its three boundary neighbours and a neighbour
in `C_0`; hence its degree in the closed shore is at least four.  Lemma 2
gives a `K_7^-` minor, a contradiction.

It remains that `|E(J)|=5`.  A triangle-free graph of order five and size
five is connected.  If it has minimum degree at least two, it is `C_5`;
if it has a leaf, deleting that leaf leaves the four-edge triangle-free
graph `C_4`.  Thus `J` is either `C_5` or a four-cycle with one pendant
edge.

In the first case write the cycle as

```text
x a b c d x
```

and put `Z={a,b,c,d}` and

```text
F={ac,ad,bd,xb}.
```

The set `{a,b}` covers `F`, and `J[Z]+F` is complete.  In the second case
write the four-cycle as `a b c d a`, let `x` be the pendant vertex joined
to `a`, put `Z={a,b,c,d}`, and set

```text
F={ac,bd,xb,xc}.
```

Now `{b,c}` covers `F`, and again `J[Z]+F` is complete.  In both cases

```text
delta(C_0)+|E(J)|+|F|=2+5+4=11.
```

The extra virtual edge or edges incident with `x`, together with its
literal boundary neighbours and a neighbour in `C_0`, give `x` degree at
least four in the augmented closed shore.  Lemma 2 again gives a
`K_7^-` minor.  This contradiction proves the theorem.  \(\square\)

## Theorem 7 (three components force a triangle-free boundary)

If `G-S` has three components, then `G[S]` is triangle-free.

### Proof

Suppose that `J=G[S]` contains a triangle.  The two vertices outside that
triangle cover every missing boundary edge.  Lemma 5 gives
`delta(C_i)<=2` for all three components.  Equation (9) then gives

```text
q+13-|E(J)|<=6,
```

so `|E(J)|>=7`.

On the other hand, `|E(J)|<=8`.  If `J` had one missing edge, one component
would realise it through a path and the other two components would be the
last two bags; if `J` were complete, only the last two components would be
needed.  Either construction is a `K_7^-` model.  Hence `|E(J)|` is seven
or eight, and some component `C_0` has `delta(C_0)=2`.

If `|E(J)|=8`, the two missing edges must be independent.  If they shared
an end, absorb a connected subgraph of one component meeting their three
ends into their common-end singleton bag; the resulting five boundary
bags and the other two components form a `K_7^-` model.  Label the missing
edges `ab,cd`, choose `x=a`, put `Z=S-{a}`, and take

```text
F={cd}.
```

This set has a one-vertex cover, `J[Z]+F` is complete, and
`delta(C_0)+8+1=11`.  The omitted vertex has three boundary neighbours and
a neighbour in `C_0`.  Lemma 2 gives a contradiction.

It remains that `|E(J)|=7`.  The three missing edges cannot form a star:
one component absorbed into its centre would complete the boundary and
leave the other two components as the final bags.  Up to isomorphism, a
three-edge graph on five vertices which is not a star is a triangle, a
four-vertex path, or the disjoint union of a three-vertex path and an edge.
In each row below, the displayed edges are precisely the missing edges of
`J`.

```text
missing graph                 x       F inside or incident with Z
triangle ab,bc,ca             a       {ab,bc}
path ab,bc,cd                 a       {bc,cd}
path ab,bc plus edge de       d       {ab,bc}
```

In every row `Z=S-{x}`, the set `F` is covered by one vertex, and
`J[Z]+F` is complete.  Moreover `|F|=2`, so

```text
delta(C_0)+7+2=11.
```

The degree of `x` in the augmented closed shore is at least four: in the
first row it has two literal boundary neighbours, one added neighbour and
a neighbour in `C_0`; in the other rows it already has three boundary
neighbours and a neighbour in `C_0`.  Lemma 2 gives the final
contradiction.  Thus `J` is triangle-free.  \(\square\)

## Scope and next case

Together with the immediate `K_5` case, Theorem 3 shows that every
five-separator in a minimum E5 enemy induces at most eight edges.  Theorem
4 eliminates the adjacent-miss eight-edge case and leaves one exact
independent-miss configuration.  Theorems 6 and 7 also show that four
components require an edgeless boundary, five components are impossible,
and three components require a triangle-free boundary.

Closing the two-component eight-edge configuration requires a new
path-residual theorem: the linked high-excess component must either leave
a connected subgraph full to `S` after the two paths are allocated, or
yield a different explicit seven-bag model.  Merely completing the boundary
consumes that component and leaves only six bags.  The empty
four-component boundary and triangle-free three-component boundaries are
the other surviving high-component cases.

## External input

Sergey Norin and Agnes Totschnig, *Every graph with no
`K_7^vee`-minor is 6-colorable*, Lemma 12,
<https://arxiv.org/abs/2507.03244>.
