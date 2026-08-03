# Two-component rooted reduction at exact `E5` density

**Status:** written computation-free unbounded reduction; separate internal
audit.  The two terminal theorems below eliminate genuine families of
two-component five-cuts.  The final contraction theorem identifies the exact
remaining low-excess obstruction; it does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a minimum
`E5` enemy, so

```text
|E(G)|=4|V(G)|-7.
```

Let `S` be a cut of order five, let `A,B` be the two components of `G-S`,
and put

```text
J=G[S],
delta_L=|E(G[L])|+|E_G(L,S)|-4|L|       (L in {A,B}).
```

Both components are connected and adjacent to every vertex of `S`, and
`(G[L union S],S)` is internally five-connected.  Exact edge accounting
gives

```text
delta_A+delta_B=13-|E(J)|.                              (1)
```

In a `Z`-rooted `K^*_{4,2}` model, four root bags are each adjacent to
two adjacent helper bags; no adjacency between distinct root bags is part
of the definition.

## Lemma 1 (rooted six-bag supply)

Let `L` be one of `A,B`, let `x in S`, and put `Z=S-{x}`.  If

```text
delta_L+d_J(x)>=5,                                     (2)
```

then `G[L union S]` contains a `Z`-rooted `K^*_{4,2}` model in which
`x` belongs to one helper bag.

### Proof

This is Lemma 1(1) of the
[sparse three-component reduction](hc7_k7minus_e5_three_component_sparse_elimination.md).
Its proof uses only the internally five-connected closed lobe and its
five-vertex boundary, not the number of other components.  It therefore
applies verbatim here.  \(\square\)

## Theorem 2 (two-shore cross-root composition)

Let `x,y` be distinct vertices of `S` and put

```text
T=S-{x,y}.
```

Suppose that `J[T]` is a triangle and, after possibly interchanging
`A,B`,

```text
delta_A+d_J(x)>=5,
delta_B+d_J(y)>=5.                                    (3)
```

Then `G` contains a `K_7^-` minor.

### Proof

Lemma 1 gives an `(S-{x})`-rooted six-bag model in the `A`-shore.  Write
its boundary-bearing bags as

```text
(R_s^A:s in S),
```

where `R_x^A=U_x` is the helper containing `x`, and write its other helper
as `V_A`.  Thus `V_A` and `U_x` are adjacent and both are adjacent to
every `R_s^A` with `s in S-{x}`.

Similarly, the `B`-shore has boundary-bearing bags

```text
(R_s^B:s in S),
```

where `R_y^B=U_y` is the helper containing `y`, and a residual helper
`V_B`.

For every `s in S`, put

```text
M_s=R_s^A union R_s^B.                                (4)
```

The two parts in (4) meet at the boundary vertex `s`, so `M_s` is
connected.  The five sets are pairwise disjoint.  They form a `K_5`
model:

- `M_x` is adjacent to `M_y` and to all three `M_t`, `t in T`, through
  the helper `U_x` in the `A`-shore;
- `M_y` is adjacent to every `M_t`, `t in T`, through `U_y` in the
  `B`-shore; and
- the three bags indexed by `T` are pairwise adjacent through the literal
  triangle `J[T]`.

The helper `V_A` is adjacent to all five `M_s`: it meets `M_x` through
the helper edge `V_A U_x` and the other four through the root--helper
incidences in the `A`-model.  Symmetrically, `V_B` is adjacent to all five
`M_s`.  The two residual helpers lie in different components of `G-S`
and may be nonadjacent.  Therefore

```text
(M_s:s in S), V_A, V_B
```

are seven disjoint connected branch sets with at most the one missing
adjacency `V_A V_B`.  They are an explicit `K_7^-` model.  \(\square\)

The point of Theorem 2 is that no third component is needed.  The literal
triangle supplies the three common-root adjacencies for which the earlier
three-lobe construction used its third component; the two residual helpers
remain as the last two branch sets.

## Theorem 3 (star completion gives strict descent)

Suppose that all nonedges of `J` have one common end `t`, and let `C` be
one of `A,B` with

```text
delta_C>=3.
```

Then `G` has a strictly smaller `E5` enemy, a contradiction.

### Proof

Let `D` be the component other than `C`.  Since `D` is connected and full
to `S`, it contains a connected subgraph meeting a neighbour of `t` and a
neighbour of every other end of a missing boundary edge.  Contract this
subgraph into `t` and delete the unused vertices of `D`.  This realises
all missing boundary edges simultaneously.  Hence

```text
H=G[C union S]+E(complement(J))
```

is a proper minor of `G`, and `H[S]` is a clique.

The graph `H` is five-connected.  Indeed, after deleting at most four
vertices, every remaining component meets `S`, since a component contained
in `C` would have at most four neighbours in `G`; the nonempty remainder
of the clique `S` then joins all components.

Writing `c=|C|`, exact counting gives

```text
|E(H)|=4c+delta_C+10
      >=4(c+5)-7.
```

The proper minor `H` is target-free, so it is a smaller `E5` enemy,
contrary to the choice of `G`.  \(\square\)

In particular, a two-component cut with

```text
J=K_4 dotunion K_1
```

is impossible.  Here the four missing edges form a star, (1) gives
`delta_A+delta_B=7`, and one lobe has excess at least four.

## Theorem 4 (low-excess whole-component dichotomy)

Suppose, after interchanging the lobes if necessary, that

```text
delta_B<=1.                                            (5)
```

Then one of the following holds.

1. `B` is a singleton, in which case `delta_B=1`.
2. The lobe `B` is not a singleton, and there is a set
   `T subseteq A union S` with `|T|<=3` such that

   ```text
   G[A union S]-T
   ```

   is disconnected and every one of its components meets `S-T`.

### Proof

Contract the whole connected component `B` to one vertex `b`, suppressing
parallel edges, and call the resulting graph `H`.  If `B` is not a
singleton, `H` is a proper target-free minor.  Equation (1) gives

```text
|V(H)|=|A|+6,
|E(H)|=4|A|+delta_A+|E(J)|+5
      =4|A|+18-delta_B
      >=4|V(H)|-7.                                    (6)
```

Thus `H` cannot be five-connected, since otherwise it would be a smaller
`E5` enemy.  Let `X` be a vertex cut of `H` of order at most four.

The vertex `b` belongs to `X`.  Otherwise `G-X` is connected by
five-connectivity, and contracting `B` leaves `H-X` connected.  Put

```text
T=X-{b}.
```

Then `|T|<=3` and

```text
H-X=G[A union S]-T
```

is disconnected.  Every component of this graph meets `S-T`.  A component
which avoided `S-T` would be contained in `A` and would have all its
neighbours in `T`, contradicting five-connectivity of `G`.  This proves
outcome 2.  If `B` is a singleton, fullness gives precisely its five edges
to `S`, and hence `delta_B=5-4=1`.  \(\square\)

## Exact remaining obstruction

### The two--three linkage route is sharp at lobe excess one

The following observation records exactly what the density form of
two--three linkage can and cannot add.  Suppose that the missing edges of
`J` are

```text
ab, ac, de,
```

and that `C,D` are the two components of `G-S`.  If `delta_D>=2` and
`delta_C>=4`, then this row is terminal.

Indeed, apply Du--Li--Xie--Yu, Theorem 1.2, to the rooted graph

```text
(G[D union S], {a,b,c}, d, e).
```

Every nonempty member of the collection in the theorem would be a subset
of `D` with at most four neighbours in `G[D union S]`.  Since `D` has no
neighbours outside `D union S`, this contradicts five-connectivity of `G`.
The collection is therefore empty.  If the rooted graph were infeasible,
the theorem would give, after adding all root edges except `de`,

```text
|E| <= 4|V|-10.
```

Only `ab,ac` are added, whereas exact lobe accounting gives

```text
|E(G[D union S]+{ab,ac})|
   =4|D|+delta_D+9
   >=4|D union S|-9.
```

Thus the rooted graph is feasible.  There is a `d`--`e` path `P` avoiding
`a,b,c`, and those three vertices lie in one component of the graph after
deleting `P`.  In that component take a shortest path from `a` to
`{b,c}`.  Call its first-hit end `z`.  The path `Q` and `P` are disjoint.
Contract `Q-z` into `a`, and contract `P-e` into `d`.  These disjoint
contractions realise `az` and `de` through `D`.  Deleting the unused part
of `D` leaves the proper minor

```text
G[C union S]+{de, one of ab,ac},
```

whose boundary is `K_5^-` and which has at least

```text
4|C|+delta_C+9 >= 4|C union S|-7
```

edges.  This minor is five-connected.  To see this, delete at most four
vertices.  Every remaining component meets the surviving boundary, since
a component contained in `C` would have at most four neighbours in `G`.
The surviving part of `K_5^-` is connected except when precisely the two
ends of its missing edge remain.  In that exceptional case, a component
on one end contains a neighbour in `C`; after deleting that boundary end,
a component inside `C` has at most the other three deleted boundary
vertices and that end as neighbours, again contradicting
five-connectivity of `G`.  The displayed proper minor would consequently
be a smaller `E5` enemy, a contradiction.

The hypothesis `delta_D>=2` is exact for this mechanism.  The sharp
example in Du--Li--Xie--Yu has `D` a path from the `d`-side to the
`e`-side, every vertex of `D` adjacent to `a,b,c`, and no further lobe
edges.  It has `delta_D=1`, satisfies the local five-neighbour condition,
and has no disjoint connected subgraphs in `D` respectively adjacent to
`{a,b,c}` and `{d,e}`: removing a triple-support vertex separates the
unique `d`--`e` route.  This is diagnostic, not an `E5` enemy, because the
opposite high-excess lobe has not been supplied.

Consequently ordinary two--three linkage cannot eliminate the concentrated
`delta_D=1` equality row.  The missing statement must use the opposite
high-excess lobe to absorb this path interface, or prove an equality
classification which yields a different explicit minor or strict descent.
Asking merely for the triple branch set to have a leafified tripod is not a
known consequence of Xie's theorem; the corresponding strengthening is
explicitly conjectural even in the six-connected non-apex setting.

Theorem 2 closes a two-lobe row once two operation-independent rooted
six-bag models can be assigned to complementary vertices of a boundary
triangle.  Theorem 3 closes the complete star of missing boundary edges.
Theorem 4 shows that a lobe of excess at most one is terminal unless it is
a singleton or contracting it exposes a separation of order at most three
inside the opposite closed shore.

That returned separation does not yet give the required strict descent.
Its components contain boundary vertices, and removing those boundary
vertices can split their interiors.  Even when one obtains a smaller
component behind a new five-cut, the current identities do not force that
component to retain excess at least four.  This is the first unsupported
inference in the whole-component contraction route.

Equivalently, the missing positive statement is a **five-root reserve
lemma**: in a lobe at the concentrated excess forced by (1), produce a
`K_6` model with five distinct bags meeting `S`, or return a smaller
component behind a five-cut which still has excess at least four.  The
opposite whole lobe would then be the seventh branch set, adjacent to the
five boundary-meeting bags and allowed to miss only the sixth.  An
unrooted `K_6` model, an arbitrary smaller side, or a rooted `K_4` using
the whole lobe does not supply this reserve.

## Dependencies and antecedents

- The rooted six-bag supply and fifth-root augmentation are in
  [`hc7_k7minus_e5_three_component_sparse_elimination.md`](hc7_k7minus_e5_three_component_sparse_elimination.md)
  and
  [`hc7_k7minus_e5_k5minus_cut_elimination.md`](hc7_k7minus_e5_k5minus_cut_elimination.md).
- The one-terminal rooted-`K_4`/six-bag composition in
  [`hc7_k7minus_degree6_cut_capacity_excess.md`](hc7_k7minus_degree6_cut_capacity_excess.md)
  is an antecedent for cross-lobe composition, but it uses a third,
  singleton component as its seventh bag.  Theorem 2 instead retains the
  two residual helpers.
- The exact three-packet quotient results elsewhere in the repository use
  three full components.  They do not create the missing reserve in a
  two-component five-cut.
- X. Du, Y. Li, S. Xie and X. Yu, *Linkages and removable paths avoiding
  vertices*, Theorem 1.2, gives the sharp density alternative used above.
