# Descent from an eight-edge five-cut

**Status:** written computation-free unbounded theorem; separate internal
audit.  This theorem transfers the high excess forced by an eight-edge
five-cut to a strictly smaller component behind a five-cut with at most
seven boundary edges.  It does not eliminate all eight-edge cuts or prove
`(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Recall that a minimum
`E5` enemy is a five-connected, `K_7^-`-minor-free graph `G` with

```text
|E(G)| >= 4|V(G)|-7,
```

chosen first with minimum order and then with minimum size.  Put

```text
q=|E(G)|-(4|V(G)|-7).
```

If `S` is a cut of order five and `C` is a component of `G-S`, define

```text
delta_S(C)=|E(G[C])|+|E_G(C,S)|-4|C|.
```

Every component of `G-S` is adjacent to every vertex of `S`.

## Lemma 1 (the two one-vertex obstructions)

Let `S={x,y,z,w,t}` induce all edges except the independent edges `xy`
and `zw`.  Suppose that `G-S` has exactly two components `C,D`, that `C`
contains disjoint `x`--`y` and `z`--`w` paths, and that

```text
delta_S(C)>=q+4.
```

Then there are distinct vertices `p,q in C` such that

```text
N_C(w)={p},             N_C(y)={q},
```

after interchanging the ends within each missing pair if necessary.
Moreover, `C-p` and `C-q` are connected.

### Proof

First add only the edge `xy` to the closed side `G[C union S]`.  This
augmented graph is an actual proper minor of `G`: a path from `x` to `y`
through the full connected component `D` realises the added edge, after
which the unused vertices and edges can be deleted.  It is target-free and
has

```text
4|C|+delta_S(C)+9 >= 4(|C|+5)-7
```

edges.  It cannot be five-connected, since otherwise it would be a
smaller `E5` enemy.

Every component after deleting a separator of order at most four contains
a boundary vertex.  Otherwise a nonempty set contained in `C` would have
at most four neighbours in `G`, contrary to five-connectivity.  The
boundary now induces `K_5-zw`, so all surviving boundary vertices lie in
one component unless the only two survivors are `z,w`.  Consequently any
separator of order at most four contains `{x,y,t}` and leaves `z,w` on
opposite sides.  It cannot have order three: connectedness of `C` and
fullness to `z,w` give a `z`--`w` path through `C`.  Thus it is

```text
{x,y,t,p}
```

for some `p in C`, and every `z`--`w` path through `C` contains `p`.

Adding only `zw` instead gives, symmetrically, a vertex `q in C` such that
every `x`--`y` path through `C` contains `q`.  The two disjoint paths
assumed in the statement show that `p` and `q` are distinct.

Consider a component `L` of `C-p`.  Its neighbours lie in
`S union {p}`, and it cannot meet both `z` and `w`.  Five-connectivity
therefore forces

```text
N_G(L)={p,x,y,t,z}       or       N_G(L)={p,x,y,t,w}.       (1)
```

If a component of `C-p` did not contain `q`, (1) would give an
`x`--`y` path through that component avoiding `q`, a contradiction.
Hence `C-p` is connected.  Similarly `C-q` is connected.

Interchange `z,w` so that `C-p` meets `z` and not `w`; then
`N_C(w)={p}`.  Interchange `x,y` so that `C-q` meets `x` and not `y`;
then `N_C(y)={q}`.  \(\square\)

## Theorem 2 (strict high-excess descent)

Under the hypotheses of Lemma 1, there is a cut `Q` of order five and a
component `R` of `G-Q` such that

```text
0<|R|<|C|,
|E(G[Q])|<=7,
delta_Q(R)>=delta_S(C)+1>=q+5.
```

In particular, `R` is a strictly smaller component satisfying the same
weaker high-excess inequality `delta_Q(R)>=q+4`.

### Proof

Take `p,q` from Lemma 1 and put

```text
R=C-{p,q},                 Q={p,q,x,z,t}.
```

The set `R` is nonempty.  If `C={p,q}`, then

```text
|E(G[C])|+|E_G(C,S)| <= 1+10,
```

so `delta_S(C)<=3`, contrary to `delta_S(C)>=q+4>=4`.

Let `L` be a component of `G[R]`.  No vertex of `L` is adjacent to `y`
or `w`, because `N_C(y)={q}` and `N_C(w)={p}`.  Thus
`N_G(L) subseteq Q`; five-connectivity gives `N_G(L)=Q`.  It follows that
every component of `G[R]` is an actual component of `G-Q`.

All vertices outside `Q union R` lie in one component of `G-Q`: the
component `D` is connected and full to `S`, so it joins `y` and `w` and
contains every vertex outside `Q union R`.  Therefore

```text
number of components of G-Q = number of components of G[R] + 1.       (2)
```

The graph `G[R]` is connected.  Indeed, if it had two components, then
`G-Q` would have three components by (2), while `G[Q]` contains the
triangle `xzt`; this contradicts the proved three-component five-cut
theorem.  Three components of `G[R]` would give four components of
`G-Q`, which have already been eliminated.  Four components would give
five components of `G-Q`, also already eliminated.  If `G[R]` had at
least five components, choose six components of `G-Q`, say
`U_1,...,U_6`, and write `Q={s_1,...,s_5}`.  The seven sets

```text
{s_1} union U_1, ..., {s_4} union U_4, {s_5}, U_5, U_6
```

are connected and pairwise adjacent except possibly for `U_5,U_6`.
They form a `K_7^-` model, a contradiction.  Hence `R` itself is one
component of `G-Q`.

Put `k=|E(G[Q])|`.  We have `k<=8`: a complete `G[Q]`, together with
the two full components of `G-Q`, immediately gives a `K_7^-` model.
The case `k=9`, namely `G[Q]=K_5^-`, has also been eliminated.  Hence

```text
k<=8.                                                        (3)
```

Exact edge accounting improves (3).  The old closed side has

```text
|E(G[C union S])|=4|C|+delta_S(C)+8
                    =4|R|+delta_S(C)+16.
```

Within this side, `y` has precisely the neighbours `z,w,t,q`, while `w`
has precisely the neighbours `x,y,t,p`.  Deleting `y,w` therefore removes
seven edges and gives

```text
|E(G[R union Q])|=4|R|+delta_S(C)+9.
```

On the other hand,

```text
|E(G[R union Q])|=4|R|+delta_Q(R)+k.
```

Thus

```text
delta_Q(R)=delta_S(C)+9-k.                              (4)
```

If `k=8`, Theorem 4 for eight-edge five-cuts applies to the component
`R`, because (4) gives `delta_Q(R)>=q+5`: it says that the other component
has excess at most one and hence that `R` supplies the two disjoint paths
for the independent missing edges of `G[Q]`.  Lemma 1 can therefore be
applied again, with `R` in place of `C`, and yields a further component
of order `|R|-2`.  Repeating this step while the new boundary has eight
edges is impossible indefinitely.  At the first step with boundary size
at most seven, equation (4) at each preceding step shows that the excess
has increased by at least one.

Equivalently, take the last component in this finite descent and rename it
`R`, with its boundary renamed `Q`.  Then

```text
0<|R|<|C|,             |E(G[Q])|<=7,
delta_Q(R)>=delta_S(C)+1>=q+5.
```

This is the claimed descent.  \(\square\)

## Corollary 3 (the minimum high-excess component has sparse boundary)

Suppose that at least one pair `(S,C)`, consisting of an order-five cut
and a component of `G-S`, satisfies

```text
delta_S(C)>=q+4.
```

Choose such a pair with `|C|` minimum.  Then

```text
|E(G[S])|<=7.
```

### Proof

The complete and `K_5^-` boundary cases have already been eliminated.  If
`|E(G[S])|=8`, Theorem 4 forces exactly the hypotheses of Lemma 1 for
this high-excess component.  Theorem 2 then produces a strictly smaller
component behind an order-five cut with excess at least `q+4`, contrary
to the choice of `C`.  \(\square\)

## Scope

This result closes the eight-edge row only for a component chosen minimum
among all high-excess components.  It does **not** prove that a minimum
`E5` enemy has no eight-edge five-cut: an arbitrary eight-edge cut may
descend to a smaller high-excess component whose new boundary has at most
seven edges.  The next exact obligation is therefore the minimum
high-excess component behind a five-cut inducing at most seven edges.
