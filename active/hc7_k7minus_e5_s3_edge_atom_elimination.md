# Elimination of the three-separator edge atom

**Status:** active computation-free written reduction; separately audited in
the [adjacent audit](hc7_k7minus_e5_s3_edge_atom_elimination_audit.md).
This note reduces the edge atom in the `s=3` singleton-`q` row to the
singleton atom.  It does not prove `(E5)`.

Use the notation and hypotheses of the
[atomic six-boundary reduction](hc7_k7minus_e5_six_boundary_atomic_reduction.md).
Use also the refined choice from the
[companion-cut elimination](hc7_k7minus_e5_s3_companion_cut_elimination.md):
among minimum-order high-excess lobes choose `(S,A)` with maximum excess.
Thus `delta_S(A)=8`.
Thus `G` is a minimum `E5` enemy in the exact two-singleton configuration,

```text
G-S has components A,{x},{y},
N_G(x)=N_G(y)=S,                    xy is not an edge,
G[S]=P_3 disjoint union K_2,
```

and, for a degree-five leaf root `t`,

```text
N_G(q)={b,p,t} union R_0,           |R_0|=2,
F=G-{x,y,t,q},                      Z=S-{t}.
```

Suppose that the order-three alternative in Theorem 6 of the atomic
reduction has the edge atom

```text
C={p,b},                            pb is an edge,
N_G(C)=U union {t,q},               |U|=3.
```

The theorem says that `b` is complete to `U`, while `p` has two or three
neighbours in `U`.  Put

```text
U_p=N_G(p) intersect U,             k=|U_p| in {2,3}.
```

The exact individual neighbourhoods are

```text
N_G(b)={p,q} union U,
N_G(p)={b,t,q} union U_p.                                (1)
```

Direct counting gives

```text
delta_{U union {t,q}}({p,b})=k-1.                        (2)
```

## Theorem

The edge atom with `k=3` produces an explicit `K_7^-` minor and hence is
impossible.  If `k=2`, then

```text
U'={b} union U_p
```

is a three-set and `U' union {t,q}=N_G(p)` is an exact five-cut whose two
components are `{p}` and its connected exterior.  Thus the excess-one
edge atom is exactly a singleton order-three atom after changing its
three-vertex adhesion.

### Proof

Suppose first that `k=2`.  Equation (1) says that `N_G(p)` has order five,
so deleting it isolates `p`.  We check that the rest is connected.  In
`F`, the open neighbourhood of `p` is the three-set `U'`.  Every component
of `F-U'` other than `{p}` meets `Z`.  Otherwise such a component lies in
the dense side, avoids `p,b`, and has no neighbour among `x,y,t,q`; its
neighbourhood in `G` would be contained in `U'`, contrary to
five-connectivity.

At least two vertices of the four-set `Z` survive the deletion of `U'`.
The vertices `x,y` are also not deleted and join every component which
meets a surviving root.  Hence all components other than `{p}` belong to
one component of `G-N_G(p)`.  This proves the singleton-atom conclusion.
Moreover, since `|E(F)|=4|V(F)|-8` and `d_F(p)=3`,

```text
|E(F-p)|=4|V(F-p)|-7.                                  (3)
```

It remains to exclude `k=3`.

The edge `bq` is density-safe.  Indeed, by (1) and the displayed
neighbourhood of `q`,

```text
N_G(b) intersect N_G(q)={p} union (U intersect R_0),
```

which has order at most three.  Contracting `bq` therefore loses at most
four edges and leaves a proper target-free minor at the `E5` density
threshold.  Minimality says that this minor is not five-connected.  It is
four-connected: a cut of order at most three either lifts unchanged, or
lifts after replacing the contracted vertex by `b,q` to a cut of `G` of
order at most four.  Every four-cut contains the contracted vertex, since
one avoiding it would also lift unchanged.
Lifting such a cut gives an exact five-cut

```text
Q'={b,q} union D,                  |D|=3.               (4)
```

Every component of `G-Q'` is adjacent to all five vertices of `Q'`.

We classify the placement of the twins `x,y` in `D`.  The set `D` cannot
contain exactly one of them.  If, say, `x in D` and `y notin D`, fullness
at `x` makes every component contain a surviving root, while `y` joins
all those roots into one component.

Suppose next that `D` contains neither twin.  The vertices `x,y` and all
surviving roots lie in one component `K` of `G-Q'`.  Any other component
must meet `q`; all surviving root-neighbours of `q` lie in `K`, so the
only available `q`-neighbour is `p`.  Consequently there is exactly one
other component `P`, and it contains `p`.

The universal five-cut excess lemma supplies a component of order at
least `|A|`.  There are `|A|+2` vertices outside `Q'`, while `K` contains
`x,y` and at least two surviving roots.  Hence `K` is the high component
and

```text
|P|<=2.                                                   (5)
```

The edge `pt` forces `t in D`.  In `F`, the component `P` has the
three-vertex neighbourhood

```text
N_F(P)={b} union (D-{t})                                (6)
```

and contains no member of `Z`.  If `P` had a second vertex, that vertex
would lie in `X` and would have at most one neighbour in `P` and the three
neighbours in (6), contrary to minimum degree five.  Thus `P={p}`.
Fullness now gives `N_G(p)=Q'`, so `d_G(p)=5`, contradicting `k=3` in
(1).

We may therefore write

```text
D={x,y,v}.                                                (7)
```

If `v` is not `p`, all neighbours of `b` outside `Q'` lie in the connected
star

```text
{p} union (U-{v}),
```

where `p` is adjacent to every surviving member of `U` because `k=3`.
Every component behind `Q'` must contain a neighbour of `b`, so they would
all coincide.  Hence the sole remaining possibility is

```text
v=p,                   Sigma={b,p,q,x,y}.               (8)
```

The graph induced by `Sigma` is the triangle `bpq` together with the two
isolated vertices `x,y`.  We next determine the components behind this
cut.  Every component contains a root because it is adjacent to `x`.
The universal five-cut excess lemma and the minimum choice of `|A|` give
one component of order at least `|A|`; all other components together have
order at most two.  A low component cannot be a singleton, since all five
roots survive `Sigma` and every root has a neighbour in
`G[S]=P_3` disjoint union `K_2`.  Thus `G-Sigma` has exactly two
components: a high component `K` and a two-vertex component `L`.

Both vertices of `L` are roots.  If one lay in `A`, it would have at most
one neighbour in `L`, at most the three possible neighbours `b,p,q` in
`Sigma`, and no neighbour in `{x,y}`, contradicting minimum degree five.
Since no root belongs to `Sigma`, the two roots form the whole `K_2`
component of `G[S]`; write

```text
L={ell_1,ell_2},                   ell_1 ell_2 is an edge.
```

There are two cases.

If `t` does not belong to `L`, each `ell_i` has only its mate and `x,y`
as three guaranteed neighbours.  If it did not belong to `U`, then (1)
would exclude both `b ell_i` and `p ell_i`, leaving at most the additional
edge to `q` and hence degree at most four.  Therefore both members of `L`
belong to `U`.  They are adjacent to each of `b,p,x,y`, and fullness at
`q` makes at least one adjacent to `q`.  With

```text
r=|N_G(q) intersect L| in {1,2},
```

exact accounting gives

```text
delta_Sigma(L)=1+r in {2,3},
delta_Sigma(K)=9-r in {7,8}.                            (9)
```

Suppose instead that `L={t,u_t}`.  The vertex `t` is adjacent in `Sigma`
to `p,q,x,y` and not to `b`.  The same minimum-degree argument puts
`u_t` in `U`, so `u_t` is adjacent to `b,p,x,y`; write

```text
epsilon=1 if q u_t is an edge, and epsilon=0 otherwise.
```

Exact accounting gives

```text
delta_Sigma(L)=1+epsilon,
delta_Sigma(K)=9-epsilon.                              (10)
```

If `epsilon=0`, then `K` has order `|A|` and excess nine, contradicting
the maximum-excess tie-break against `delta_S(A)=8`.  Thus it remains only
to treat `epsilon=1`, when `delta_Sigma(K)=8`.

The closed shore `G[K union Sigma]` with boundary `Sigma` is internally
five-connected.  Apply Lemma 1 of the
[two-component rooted reduction](hc7_k7minus_e5_two_component_rooted_reduction.md)
to this lobe with the nominated boundary vertex `y`.  Here

```text
delta_Sigma(K)+d_{G[Sigma]}(y)>=7>=5,
```

so there is a `(Sigma-{y})`-rooted `K^*_{4,2}` model in which `y` belongs
to one helper bag.  Denote the four root bags by

```text
B_b, B_p, B_q, B_x
```

and the helper bags by `U_y,V`, with `y in U_y`.  Both helpers are
adjacent to every root bag and to one another.

Absorb `V` into the root bag `B_x`.  The four bags

```text
B_b,                  B_p,                  B_q,
B_x union V
```

are pairwise adjacent: the first three meet through the literal triangle
`bpq`, and `V` supplies all three adjacencies from the fourth bag.  The
seven branch sets

```text
B_b, B_p, B_q, B_x union V, U_y, {ell_1}, {ell_2}       (11)
```

are disjoint and connected.  The helper `U_y` is adjacent to the four
root bags by the model and to both low singletons through `y`, and the two
low singletons are adjacent to each other.

If `t` is not in `L`, each low singleton is adjacent to
`B_b,B_p,B_x union V`, and at least one is adjacent to `B_q`; the other
may fail only that one adjacency.  If `L={t,u_t}`, then `epsilon=1`:
the vertex `t` is adjacent to `B_p,B_q,B_x union V`, while `u_t` is
adjacent to all four root bags.  Only `t B_b` may be absent.  In either
case (11) is an explicit `K_7^-`-minor model, a contradiction.

This excludes `k=3` and completes the proof.  \(\square\)

## Consequence and scope

The order-three edge atom is no longer a terminal outcome.  Its
excess-one form is precisely a singleton atom under a different
three-vertex adhesion, and its excess-two form is impossible.  The sole
remaining order-three obstruction in the `s=3` singleton-`q` row is
therefore the singleton atom `{p}`.

This note does not eliminate that singleton atom.  Contracting `pt`
preserves more than the `E5` density, but the image of `N_G(q)` is already
a four-cut in the quotient, so the contraction alone supplies no new
connectivity contradiction.

## Dependencies

- [Atomic six-boundary reduction](hc7_k7minus_e5_six_boundary_atomic_reduction.md),
  especially Theorem 6 and its exact edge-atom classification.
- [Companion-cut elimination](hc7_k7minus_e5_s3_companion_cut_elimination.md),
  for the maximum-excess tie-break among minimum-order lobes.
- [Singleton-contraction uncrossing](hc7_k7minus_e5_singleton_contraction_uncrossing.md),
  Lemma 1 for the universal high-excess component behind every five-cut.
- [Two-component rooted reduction](hc7_k7minus_e5_two_component_rooted_reduction.md),
  Lemma 1 for the rooted six-bag model in the high shore.
