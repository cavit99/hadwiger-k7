# Anchored four-root reduction in the exact singleton residue

**Status:** active computation-free written proof; see the
[adjacent audit](hc7_k7minus_e5_anchored_four_root_reduction_audit.md) for
independent verification.  This note sharpens the remaining two-singleton
branch of `(E5)`.  It does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a minimum
`E5` enemy in the exact surviving three-component configuration.  Thus

```text
|E(G)|=4|V(G)|-7,
G-S has components A,{x},{y},
N_G(x)=N_G(y)=S,
xy is not an edge,
J=G[S]=P_3 disjoint union K_2,
H=G[A union S],
|E(H)|=4|V(H)|-9.
```

Let `T` be the set of degree-one vertices of `J` which have degree five
in `G`.  The audited singleton-contraction theorem proves that
`3<=|T|<=4`.  For `t in T`, let `u_t` be its unique neighbour in `J` and
put

```text
P_t=N_G(t) intersect A.
```

Then `|P_t|=2` and

```text
N_H(t)={u_t} union P_t.                              (1)
```

## Lemma 1 (the four-root graph after deleting a leaf)

Fix `t in T`, and put

```text
K=H-t,                         Z=S-{t}.
```

Then

```text
|E(K)|=4|V(K)|-8,                                      (2)
```

and the rooted pair `(K,Z)` is internally four-connected.

### Proof

Equation (1) gives `d_H(t)=3`.  Deleting `t` from the equality
`|E(H)|=4|V(H)|-9` gives (2).

Suppose that `(U,V)` is a separation of `(K,Z)` of order at most three
with `V-U` nonempty.  Since `Z` is contained in `U`, the set `V-U` lies
in `A`.  In `G`, neither `x` nor `y` has a neighbour in `A`, and deleting
`t` removes every edge from `t` to `A`.  Consequently

```text
(U intersect V) union {t}
```

separates `V-U` from the rest of `G`.  The rest is nonempty: at most
three vertices were deleted from the four-set `Z`, so some member of
`Z-(U intersect V)` survives outside `V-U`.  This is a cut of `G` of
order at most four, contrary to five-connectivity.  Hence `(K,Z)` is
internally four-connected.  \(\square\)

## Corollary 2 (the two existing four-root supplies)

For every `t in T` the graph `K=H-t` has

1. a `Z`-rooted `K_4`-minor model; and
2. a `Z`-rooted `K^*_{4,2}`-minor model.

Moreover, `H` has a `Z`-rooted `K^*_{4,2}`-minor model in which `t`
belongs to one of the two helper bags.

### Proof

The singleton-contraction theorem gives `|A|>=7`, so `|V(K)|>=11`.
By (2),

```text
|E(K)|=4|V(K)|-8>3|V(K)|-7.
```

Norin--Totschnig Lemma 9 and Lemma 1 therefore give the first model.
Similarly,

```text
|E(K)|=4|V(K)|-8>4|V(K)|-10,
```

so Norin--Totschnig Lemma 12 gives the second model.  The pair `(H,S)`
is internally five-connected.  Applying the fifth-root augmentation
lemma to the second model, viewed as a model in `H`, gives such a model
with `t` in a helper bag.  \(\square\)

## Lemma 3 (a helper containing a leaf also meets its dense neighbours)

In the last model of Corollary 2, the helper bag containing `t` contains
at least one member of `P_t`.

### Proof

Let `U` be the helper bag containing `t`.  The four root bags contain
the four distinct vertices of `Z`, and in particular the root bag indexed
by `u_t` contains `u_t`.  Hence `u_t` does not belong to `U`.

The bag `U` cannot be the singleton `{t}`.  Such a bag has neighbours in
at most the three bags containing the three vertices of `N_H(t)`, whereas
a helper of `K^*_{4,2}` is adjacent to all four root bags.  Since `U` is
connected and `u_t` is not in `U`, the first edge of `U` leaving `t` has
its other end in `P_t`.  \(\square\)

Corollary 2 and Lemma 3 therefore supply separately

- four pairwise adjacent bags rooted at `Z`; and
- four possibly different root bags with a universal helper containing
  `t` and a member of `P_t`.

They do not show that one branch-set system has both properties.

## Lemma 4 (the anchored model is sufficient)

Fix `t in T` and `p in P_t`.  Suppose that `K=H-t` contains five
pairwise disjoint connected branch sets

```text
(B_z:z in Z),                         R,
```

such that

- `z in B_z` for every `z in Z`;
- the four sets `B_z` are pairwise adjacent;
- `p in R`; and
- `R` is adjacent to every `B_z`.

Then `G` contains a `K_7^-` minor.

### Proof

The seven branch sets

```text
{x,t},          {y},          (B_z:z in Z),          R
```

are pairwise disjoint and connected.  The set `{x,t}` is adjacent to
`R` through the edge `tp`; it is adjacent to every `B_z` through `x`,
and it is adjacent to `{y}` through `ty`.  The singleton `{y}` is
adjacent to every `B_z` through the corresponding root `z`.  The five
sets `(B_z:z in Z),R` are pairwise adjacent by hypothesis.  Thus the only
possibly absent adjacency is `{y}`--`R`, giving an explicit `K_7^-`-minor
model.  \(\square\)

## Theorem 5 (every three--two boundary split has disjoint carriers)

For every partition

```text
S=R disjoint union B,             |R|=3,             |B|=2,
```

the graph `H` contains vertex-disjoint connected subgraphs `C_R,C_B`
such that `R` is contained in `C_R` and `B` is contained in `C_B`.

### Proof

Write `B={b_1,b_2}` and apply Du--Li--Xie--Yu, Theorem 1.2, with
`m=3` to the rooted graph `(H,R,b_1,b_2)`.

Suppose first that the theorem returns an obstruction collection.  Every
nonempty member `X` of that collection is disjoint from the five
terminals, so `X` is a subset of `A`, and the theorem gives

```text
|N_H(X)|<=4.                                             (3)
```

The vertices `x,y` have no neighbours in `A`, and `A` has no neighbours
outside `A union S`.  Hence `N_G(X)=N_H(X)`.  Deleting this set separates
the nonempty set `X` from `x,y`, contrary to five-connectivity of `G`.
Thus the obstruction collection has no nonempty member and its quotient
is just `H`.

Let `epsilon=1` if `b_1b_2` is already an edge of `J`, and let
`epsilon=0` otherwise.  The rooted completion in the theorem adds every
missing edge among the five terminals except `b_1b_2`; it does not delete
that edge when it is already present.  The completed terminal graph
therefore has `9+epsilon` edges.  Since `J` has three edges, the completion
adds `6+epsilon` edges and has

```text
|E(H)|+6+epsilon=4|V(H)|-3+epsilon                     (4)
```

edges.  In the infeasible outcome, Du--Li--Xie--Yu, Theorem 1.2, bounds
the same graph by

```text
4|V(H)|-(3^2)/2-3(3)/2-1=4|V(H)|-10,                  (5)
```

contradicting (4).

The rooted graph is therefore feasible.  There is a `b_1`--`b_2` path
`C_B` such that all three vertices of `R` lie in one component `C_R` of
`H-C_B`.  These are the required disjoint connected subgraphs.  \(\square\)

Theorem 5 is simultaneous only for the two carriers belonging to one
chosen partition.  Applying it to several partitions does not make the
resulting carriers mutually disjoint and does not by itself produce five
pairwise adjacent rooted bags.  The
[octahedral counterexample](../barriers/hc7_three_two_carriers_do_not_force_rooted_k5.md)
shows that even feasibility of every three--two partition, together with
four-connectivity, does not imply a five-rooted `K_5` model without an
additional density-sensitive argument.

## Theorem 6 (boundary contacts force `|A|>=8`)

Label the path and edge of `J` as

```text
s_0-s_1-s_2,                     s_3-s_4,
```

and put

```text
d_i=|N_G(s_i) intersect A|.
```

Then

```text
sum_{i=0}^4 d_i<=|A|+7.                                (6)
```

Consequently `|A|>=8`.

### Proof

For each root `s`, let `C_s,L_s` be the three-cut and root-only low side
given by Theorem 3 of the singleton-contraction theorem.  Thus

```text
|C_s|=3,              s in C_s,              N_H(L_s)=C_s,
1<=|L_s|<=2.                                           (7)
```

Apply (7) first with `s=s_0`.  The only neighbour `s_1` of `s_0` in `J`
must belong to `L_{s_0}`.  If `s_2` does not also belong to this low side,
then both `s_0,s_2` belong to its three-vertex neighbourhood, so `d_1<=1`.
If `s_2` does belong to the low side, its external root neighbourhood
contains `s_0`; all dense-component neighbours of `s_1,s_2` lie in the
other at most two members of `C_{s_0}`, so

```text
d_1<=2,                         d_2<=2.                (8)
```

The symmetric argument at `s_2` says either `d_1<=1`, or

```text
d_1<=2,                         d_0<=2.                (9)
```

It follows that `d_1<=2`, and if `d_1=2` then
`d_0,d_2<=2`.

At `s_3`, the root `s_4` belongs to `L_{s_3}`.  The cut `C_{s_3}` already
contains `s_3`, and every neighbour of `s_4` in `A` belongs to that
three-set.  Hence `d_4<=2`; symmetrically, `d_3<=2`.

Finally apply (7) at the centre `s_1`.  Its low side contains `s_0` or
`s_2`.  All dense-component neighbours of that root lie in `C_{s_1}`,
which already contains `s_1`.  Therefore

```text
min(d_0,d_2)<=2.                                      (10)
```

If `d_1=2`, equations (8)--(10) give `sum_i d_i<=10`.
If `d_1<=1`, one of `d_0,d_2` is at most two, the other is at most
`|A|`, and `d_3,d_4<=2`; hence `sum_i d_i<=|A|+7`.
Since `|A|>=3`, the same bound also covers the first case.  This proves
(6).

Exact accounting at the original five-cut gives

```text
|E(G[A])|+sum_i d_i=4|A|+8.
```

Together with (6) and `|E(G[A])|<=binom(|A|,2)`, this yields

```text
4|A|+8<=binom(|A|,2)+|A|+7,
```

or `|A|^2-7|A|-2>=0`.  Thus the positive integer `|A|` is at least
eight.  \(\square\)

## Exact remaining synchronization statement

For a five-cut `Q` and a component `D` of `G-Q`, write

```text
delta_Q(D)=|E(G[D])|+|E_G(D,Q)|-4|D|.
```

The exact two-singleton branch would be closed by the following statement.

> **Anchored four-root `K_5`-or-descent target.**  In the setup above,
> there are `t in T` and `p in P_t` such that either
>
> 1. the five branch sets in Lemma 4 exist in `H-t`; or
> 2. there are a five-cut `Q` and a component `D` of `G-Q` such that
>    `|D|<|A|` and `delta_Q(D)>=4`.

The first outcome closes the branch by Lemma 4.  The second contradicts
the minimum-order choice of the high-excess component `A`.

This target is strictly narrower than an arbitrary `S`-rooted `K_5`
theorem.  The first outcome is precisely a `K_5`-minor model rooted at
the five-set `Z union {p}` in `H-t`, where the bag containing `p` is
disjoint from all four boundary-root bags.  Its unresolved content is
the synchronization of the two model supplies in Corollary 2 while
retaining the selected anchor `p`, or a well-founded high-excess descent.

An unrooted `K_6` or `K_7^vee` model, a smaller component without the
displayed excess, or independently chosen rooted models does not prove
the target.

## Dependencies

- The [singleton-contraction uncrossing theorem](hc7_k7minus_e5_singleton_contraction_uncrossing.md).
- The [sparse three-component reduction](hc7_k7minus_e5_three_component_sparse_elimination.md),
  whose Lemma 1 contains an equivalent rooted-`K_4` application.
- The [fifth-root augmentation lemma](hc7_k7minus_e5_k5minus_cut_elimination.md).
- Sergey Norin and Agnes Totschnig, *Every graph with no
  `K_7^vee`-minor is 6-colorable*, Lemmas 9 and 12, arXiv:2507.03244v1.
- Xiying Du, Yanjia Li, Shijie Xie and Xingxing Yu, *Linkages and
  removable paths avoiding vertices*, Journal of Combinatorial Theory,
  Series B 169 (2024), 211--232, Theorem 1.2,
  DOI `10.1016/j.jctb.2024.06.006`.
