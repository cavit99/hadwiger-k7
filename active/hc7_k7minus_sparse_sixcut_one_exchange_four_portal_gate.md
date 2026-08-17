# The one-exchanged-root return reduces to four internal portals

**Status:** written unbounded reduction; adjacent independent cold audit
GREEN.  This note does not prove that two connected subgraphs full to a
derived boundary return as two connected subgraphs full to the original
boundary.  It isolates one maximal four-portal augmentation statement which
remains open.

Use the setup of the
[exact-six rerooting theorem](hc7_k7minus_six_boundary_fragment_rerooting.md).
Thus `G` is six-connected, `S` is a six-set, `C` is a component of `G-S`
adjacent to every vertex of `S`, and

```text
F=G[C union S]+E(K_S).
```

Let `T` be an order-six cut of `F`, and let `L` be a component of `F-T`
not containing `S-T`.  Then `L subseteq C` and `N_F(L)=T`.  This note treats
the one-exchanged-root case

```text
Z=T intersect S,       T-S={r},       S-T={q}.        (1)
```

In particular,

```text
|Z|=5,                 T=Z union {r}, S=Z union {q}.  (2)
```

All edges incident with `L` are actual edges of `G`, since the only edges
added in the definition of `F` have both ends in `S`.

Assume throughout that every punctured original shore is rooted-model-free:

```text
G[C union (S-{s})] has no (S-{s})-rooted K_5^- model
for every s in S.                                    (3)
```

## Theorem 1 (one-exchange four-portal reduction)

Suppose `L` contains two vertex-disjoint connected subgraphs, each adjacent
to every vertex of `T`.  Then there are vertex-disjoint connected subgraphs
`A,B,W` of `G[C]` with the following properties.

1. `A,B subseteq L` are adjacent, and each is adjacent to every vertex of
   `Z union {r}`.
2. `W` is the component of `G[C-(A union B)]` containing `C-L`; in
   particular, `r in W`, `W` has a neighbour at `q`, and `W` is adjacent to
   both `A` and `B`.
3. Writing

   ```text
   d=|N_G(W) intersect Z|,
   p=|N_G(W) intersect (A union B)|,
   ```

   we have

   ```text
   d<=1,                    p>=5-d>=4.                (4)
   ```

The pair `A,B` may moreover be chosen so that `|W|` is maximum among all
pairs satisfying item 1, with `W` defined as in item 2.

### Proof

Let `P_1,P_2` be the two given connected subgraphs.  Choose a shortest
`P_1`--`P_2` path in `G[L]`.  Its internal vertices avoid both `P_1` and
`P_2`.  Absorb those internal vertices into `P_1`, and call the resulting
subgraph `A`; put `B=P_2`.  The subgraphs `A,B` are connected, disjoint and
adjacent, and both retain all their contacts with `T`.

Put `D=C-L`.  We first check that `D` is connected.  We have

```text
N_G(L) intersect C={r},                              (5)
```

because `N_F(L)=T` and `T-S={r}`.  If `G[D]` had a component not containing
`r`, connectivity of `G[C]` would give an edge from that component to `L`.
Its end outside `L` would contradict (5).  Hence `D` is connected.  Also
`D` has a neighbour at `q`: the component `C` is adjacent to `q`, while `L`
is not, since `q notin T=N_F(L)`.  In particular, `D` is nonempty and
contains `r`.

Let `W` be the component of `G[C-(A union B)]` containing `D`.  It is well
defined because `D` is connected and disjoint from `A union B`.  Each of
`A,B` has a neighbour at `r`, so `W` is adjacent to both of them, and the
preceding paragraph gives a neighbour from `W` to `q`.

We use the following explicit minor-model construction.  Suppose that `W`
has neighbours at two distinct vertices `x,y in Z`.  Choose distinct
`a,b in Z-{x,y}`, and let `z` be the remaining member of
`Z-{x,y,a,b}`.  The five sets

```text
A union {a},   B union {b},   W union {q},   {x},   {y}       (6)
```

are pairwise disjoint and connected.  The first two are adjacent to each
other and to `W union {q}`.  They are also adjacent to both singleton sets,
because `A` and `B` are `Z`-full.  The third set is adjacent to both
singletons by the choice of `x,y`.  Thus the only pair in (6) which may be
nonadjacent is `{x},{y}`.  The sets in (6) form an
`(S-{z})`-rooted `K_5^-` model contained in
`G[C union (S-{z})]`, contrary to (3).  Therefore

```text
d=|N_G(W) intersect Z|<=1.                            (7)
```

The rooted pair `(G[C union S],S)` is internally six-connected.  Indeed, all
neighbours of a nonempty `X subseteq C` lie in `C union S`.  If its external
neighbourhood had order at most five, some vertex of the six-set `S` would
survive its deletion; that deletion would then separate `X` from this
surviving vertex, contrary to six-connectivity of `G`.  Apply this to `W`.
Since `W` is a component after deleting `A union B`, all its neighbours in
`C-W` lie in `A union B`.  Its boundary in the closed shore is consequently
the disjoint union of its `p` neighbours in `A union B`, its `d` neighbours
in `Z`, and `{q}`.  Hence

```text
6<=p+d+1,
```

which proves (4).

There are finitely many admissible pairs `A,B`, so one may choose a pair
maximising the order of the corresponding component `W`.  All conclusions
above remain valid for that choice.  `\square`

## Open statement (maximal four-portal augmentation)

The following statement is not proved here.

> In the setup of Theorem 1, let `A,B` maximise `|W|`.  If
> `|N_G(W) intersect Z|+|N_G(W) intersect (A union B)|>=5`, then either the
> closed original shore contains a punctured `S`-rooted `K_5^-` model, or
> there are disjoint adjacent connected subgraphs `A',B' subseteq L`, each
> adjacent to every vertex of `Z union {r}`, such that the component `W'` of
> `G[C-(A' union B')]` containing `C-L` strictly contains `W`.

This statement would close the one-exchanged-root return.  Theorem 1 gives
the displayed lower bound, while (3) excludes its first outcome and the
maximal choice of `W` excludes its second.  No such conclusion is presently
justified merely from the number of portal vertices: a proof must use their
placement inside the two connected `Z`-full subgraphs, or an equivalent
linkage theorem.

## Why the single opposite-side linkage does not finish the proof

For (1), the saturated opposite-side linkage is one `r`--`q` path outside
`L union Z`.  After contracting `A` and `B`, adjoining their two contacts at
`r` to the common `r`--`q` suffix gives a rooted `K_{2,1}` scheme.  The
[contractibility of `K_{2,n}`](../results/k2n_contractibility_via_matroid_packing.md)
therefore supplies a rooted `K_{2,1}` model.  Its `q`-rooted branch set may
contain `r` and the common suffix.  It need not acquire two contacts in `Z`;
the subgraph `W` in Theorem 1 records exactly this possible outcome.  Thus
contractibility alone does not prove the open augmentation statement.

## Dependency

The notation and the saturated opposite-side linkage are imported from
[the exact-six rerooting theorem](hc7_k7minus_six_boundary_fragment_rerooting.md),
source SHA-256
`53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15`.
