# Elimination of the `K_{2,3}` three-component equality row

**Status:** written computation-free unbounded theorem; separate internal
audit.  This eliminates one exact three-component row in a minimum
`E5` enemy.  It does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Recall that a minimum
`E5` enemy is a five-connected, `K_7^-`-minor-free graph `G` with

```text
|E(G)| >= 4|V(G)|-7,
```

chosen first with minimum order and then with minimum size.  Let `S` be a
cut of order five, let `A,B,C` be the components of `G-S`, and put

```text
delta(L)=|E(G[L])|+|E_G(L,S)|-4|L|.
```

Every component of `G-S` is connected and full to `S`, and the pair
`(G[S union L],S)` is internally five-connected.

## Theorem

There is no cut `S` in a minimum `E5` enemy for which

```text
G[S] is K_{2,3},
|E(G)|=4|V(G)|-7,
and {delta(A),delta(B),delta(C)}={3,3,1}.
```

### Proof

Write the bipartition of `J=G[S]` as

```text
X={u,v},                 Y={a,b,c}.
```

We use the two excess-three components `A` and `B` for different rooted
models.

#### 1. An excess-three component supplies an avoidant rooted `K_4`

We first prove that, for some `x in Y`,

```text
G[(S-{x}) union B]
```

contains a `K_4` minor rooted at the four vertices of `S-{x}`.

For `s in S`, let `p(s)=|E_G({s},B)|`, and write `b_0=|B|`.  Suppose to
the contrary that no such `x` exists.  Fix `x in Y`, put `Z=S-{x}`, and
let

```text
H_x=G[Z union B].
```

Fabila-Monroy and Wood's rooted-`K_4` obstruction theorem places `H_x`
in a spanning rooted obstruction obtained from a planar skeleton by adding
cliques complete to facial triangles.  No vertex of `B` can belong to an
added clique.  Indeed, for a nonempty component `Q` of the vertices of
`B` in one such clique, every neighbour of `Q` outside `Q` lies in the
corresponding facial triangle, with the possible additional boundary
vertex `x`.  Thus

```text
|N_G(Q)| <= 4,
```

contrary to five-connectivity of `G`.  Hence `H_x` is planar.

The graph `J-x` is a four-cycle.  Since

```text
|E(H_x)|=4b_0+delta(B)-p(x)+4,
```

the planar bound gives

```text
4b_0+delta(B)-p(x)+4 <= 3(b_0+4)-6,
```

and therefore

```text
p(x) >= b_0+delta(B)-2.                              (1)
```

Summing (1) over the three vertices of `Y`, and using fullness at `u` and
`v`, gives

```text
|E_G(B,S)| >= 3b_0+3delta(B)-4.                      (2)
```

On the other hand, connectedness of `B` gives

```text
|E_G(B,S)|
 =4b_0+delta(B)-|E(G[B])|
 <=3b_0+delta(B)+1.                                  (3)
```

For `delta(B)=3`, inequalities (2) and (3) read respectively
`|E_G(B,S)|>=3b_0+5` and `|E_G(B,S)|<=3b_0+4`, a
contradiction.  Choose `x in Y` for which the required rooted `K_4`
exists, and put `Z=S-{x}`.

#### 2. The other excess-three component supplies the six-bag model

Let `F` be the two missing edges which complete the four-cycle `J[Z]` to
a clique.  We show that `G[S union A]` has an actual `Z`-rooted
`K^*_{4,2}` model.  Here the four root bags are each adjacent to two
adjacent helper bags; adjacency between different root bags is not part of
the definition.

Put `p_A(x)=|E_G({x},A)|`.  If `p_A(x)=1`, consider

```text
G[Z union A]+F.
```

The pair with root set `Z` is internally four-connected, and its order and
size are

```text
|A|+4,                 4|A|+delta(A)+5.
```

Indeed, a separation of this pair of order at most three would become a
separation of `(G[S union A],S)` of order at most four after putting `x`
in its separator.

If `p_A(x)>=2`, instead consider

```text
G[S union A]+F.
```

The omitted vertex `x` has at least two neighbours in `A` and two in
`J`, so the pair with root set `Z` is again internally four-connected.
Its order and size are

```text
|A|+5,                 4|A|+delta(A)+8.
```

For otherwise a separation of order at most three extends to an internal
separation with boundary `S`; the only possible exception has open side
`{x}`, which the displayed degree bound excludes.

As `delta(A)=3`, both graphs meet the threshold

```text
|E(H)| >= 4|V(H)|-9.
```

Norin--Totschnig Lemma 12 therefore gives a `Z`-rooted
`K^*_{4,2}` model.  The two edges of `F` join distinct roots.  They cannot
lie inside a branch set, and no root--root adjacency is required, so
deleting them leaves the same rooted model in the original graph.

Apply the fifth-root augmentation lemma to `(G[S union A],S)`.  We may
choose the rooted model with `x` in one helper bag, say `U`; call the other
helper `V` and the root bag containing `z in Z` by `R_z`.

#### 3. Terminal composition

Let `Q_z`, for `z in Z`, be the four branch sets of the rooted `K_4`
model in `G[Z union B]` obtained in Step 1.  Define

```text
M_z=R_z union Q_z             for z in Z.
```

Each `M_z` is connected because its two parts meet at `z`.  The four sets
`M_z` are pairwise adjacent through the rooted `K_4` model in the
`B`-shore.  Each is adjacent to both `U` and `V` through the
`K^*_{4,2}` model in the `A`-shore, and `U` is adjacent to `V`.

The sets are disjoint: distinct roots belong to distinct bags in each
rooted model, the two shores meet only in `S`, and the `B`-shore model
contains neither `x` nor a second member of `Z` in any root bag.

Finally retain the whole component `C` as the seventh branch set.  It is
adjacent to every `M_z` through the root `z`, and it is adjacent to `U`
through `x`.  It may miss only `V`.  The seven disjoint connected sets

```text
{M_z : z in Z}, U, V, C
```

therefore form a `K_7^-` minor model in `G`, a contradiction.  Notice that
the rooted `K_4` model lies in `G[Z union B]` and hence avoids `x`; this is
exactly what prevents the helper--root overlap in the earlier incomplete
composition.  \(\square\)

## Dependencies

- The fifth-root augmentation lemma in
  `active/hc7_k7minus_e5_k5minus_cut_elimination.md`.
- Sergey Norin and Agnes Totschnig, *Every graph with no
  `K_7^vee`-minor is 6-colourable*, Lemma 12,
  <https://arxiv.org/abs/2507.03244>.
- Ruy Fabila-Monroy and David R. Wood, *Rooted `K_4`-Minors*, Electronic
  Journal of Combinatorics 20(2) (2013), P64, Theorem 15,
  <https://doi.org/10.37236/3476>.

## Scope

The theorem eliminates only the displayed exact equality row.  It does
not eliminate every triangle-free three-component boundary or prove
`(E5)`.
