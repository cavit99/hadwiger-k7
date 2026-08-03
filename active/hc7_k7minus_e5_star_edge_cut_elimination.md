# Elimination of the disjoint star-and-edge five-cut row

**Status:** written computation-free unbounded theorem; separate internal
audit.  This eliminates the exact surviving row of Theorem 3 in
[`hc7_k7minus_e5_seven_edge_cut_reduction.md`](hc7_k7minus_e5_seven_edge_cut_reduction.md).
It does not by itself prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted and `K^*_{4,2}` for the
six-bag rooted model in which four root bags are each adjacent to two
adjacent helper bags.  No adjacency between distinct root bags is required
in a `K^*_{4,2}` model.

## Lemma 1 (an excess-two lobe supplies the rooted six-bag model)

Let `Q=Z union {t}`, where `|Z|=4`, and let `L` be a component behind the
five-cut `Q` in a five-connected graph `G`.  Suppose that

```text
delta_Q(L)=|E(G[L])|+|E_G(L,Q)|-4|L| >= 2
```

and that `t` has at least three neighbours in `Z`.  Then
`G[L union Q]` has a `Z`-rooted `K^*_{4,2}` model in which `t` belongs to
one helper bag.

### Proof

Put `H=G[L union Q]`, and add the missing edges of `G[Z]` to make `Z` a
clique.  Call the resulting graph `H^+`.  The pair `(H^+,Z)` is internally
four-connected.  Indeed, a separation of order at most three would extend
to an internal separation of `(H,Q)` of order at most four unless its
non-root open side were the singleton `{t}`.  The latter case is impossible
because `t` has at least three neighbours in `Z` and, by fullness of `L` to
`Q`, at least one neighbour in `L`.

Writing `ell=|L|` and `gamma=delta_Q(L)`, exact edge accounting gives

```text
|E(H^+)|
 = 4ell+gamma+|E(G[Q])|+6-|E(G[Z])|
 = 4ell+gamma+6+d_{G[Q]}(t)
 >= 4ell+11
 = 4|V(H^+)|-9.
```

Norin--Totschnig Lemma 12 therefore gives a `Z`-rooted
`K^*_{4,2}` model in `H^+`.  Every added edge joins two nominated roots.
Its ends consequently belong to distinct root bags; such an edge is
neither internal to a branch set nor one of the root--helper or
helper--helper adjacencies required by `K^*_{4,2}`.  Deleting all the added
edges leaves the same rooted model in `H`.

The pair `(H,Q)` is internally five-connected.  The fifth-root augmentation
lemma now lets us choose the model so that `t` belongs to one of its two
helper bags.  \(\square\)

## Theorem 2 (terminal composition)

Let `G` be a minimum `E5` enemy and let

```text
S={a,b,c,d,e}
```

be a five-cut for which `G-S` has exactly two components `C,D` and the
missing edges of `G[S]` are

```text
ab, ac, de.
```

Assume that the reduction in Theorem 3 of the seven-edge five-cut theorem
has produced `p in C` and the two components `A,B` of `C-p` satisfying

```text
N_G(A)={p,a,b,c,d},       N_G(B)={p,a,b,c,e},
```

and put

```text
Q_d={p,a,b,c,d},          Q_e={p,a,b,c,e},
alpha=delta_{Q_d}(A),     beta=delta_{Q_e}(B).
```

If `alpha,beta>=2`, then `G` contains a `K_7^-` minor.  In particular,
every numerical row left by that reduction is impossible.

### Proof

Put

```text
Z={p,a,b,c}.
```

In `G[Q_d]`, the vertex `d` is adjacent to `a,b,c`; in `G[Q_e]`, the
vertex `e` is adjacent to `a,b,c`.  Lemma 1 applied first to `A` and then
to `B` gives two actual `Z`-rooted `K^*_{4,2}` models.  Write the model in
the `A`-shore as

```text
(R_z^A : z in Z), U_A, V_A,
```

where `d in U_A`.  Write the model in the `B`-shore as

```text
(R_z^B : z in Z), U_B, V_B,
```

where `e in U_B`.

Collapse the latter six-bag model to four rooted bags by putting

```text
Q_p=R_p^B union U_B,       Q_a=R_a^B union V_B,
Q_b=R_b^B,                 Q_c=R_c^B.
```

These four sets are connected and pairwise adjacent.  The helper edge
gives the `Q_p`--`Q_a` adjacency; the universal root--helper incidences
give all adjacencies from `Q_p` and `Q_a` to `Q_b,Q_c`; and the literal
edge `bc` gives the last adjacency.  Thus they are a `Z`-rooted `K_4`
model.  Moreover,

```text
e in Q_p.                                                   (1)
```

For each `z in Z`, define

```text
M_z=R_z^A union Q_z.
```

The two parts meet at the root `z`, so `M_z` is connected.  The four
sets `M_z` are pairwise disjoint and pairwise adjacent through the rooted
`K_4` model in the `B`-shore.  Each is adjacent to both `U_A` and `V_A`,
and `U_A` is adjacent to `V_A`.

Retain the whole low-excess component `D` as the seventh branch set.
Five-connectivity makes `D` full to `S`.  It is therefore adjacent to
`M_a,M_b,M_c` through `a,b,c`, to `M_p` through (1), and to `U_A` through
`d`.  It may miss only `V_A`.  Consequently

```text
M_p, M_a, M_b, M_c, U_A, V_A, D
```

are seven pairwise disjoint connected branch sets with at most one missing
pair of adjacencies.  They form a `K_7^-` minor model in `G`, a
contradiction.  \(\square\)

## Consequence and scope

The exact rows in the preceding seven-edge reduction have

```text
(alpha,beta) in {(3,3),(2,3),(3,2)}.
```

Theorem 2 eliminates all of them.  Together with Theorems 1 and 2 of that
reduction, this closes every complement type for a seven-edge boundary of
a component chosen minimum among those with excess at least `q+4`.

The proof does **not** infer the star-and-path support inside `D` from
ordinary two--three linkage.  Instead, it uses the second high-side lobe
to turn one rooted six-bag model into a rooted `K_4`, placing `e` in the
bag rooted at `p`.  That single transfer supplies the contact with `D`
which the direct support argument lacked.

## Dependencies

- The fifth-root augmentation lemma and its internal-connectivity
  convention in
  [`hc7_k7minus_e5_k5minus_cut_elimination.md`](hc7_k7minus_e5_k5minus_cut_elimination.md).
- Sergey Norin and Agnes Totschnig, *Every graph with no
  `K_7^vee`-minor is 6-colourable*, Lemma 12,
  <https://arxiv.org/abs/2507.03244>.
- The exact disjoint star-and-edge reduction in
  [`hc7_k7minus_e5_seven_edge_cut_reduction.md`](hc7_k7minus_e5_seven_edge_cut_reduction.md).
