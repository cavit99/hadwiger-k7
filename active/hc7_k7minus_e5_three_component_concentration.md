# Concentration in a three-component five-cut

**Status:** written computation-free unbounded reduction; separate internal
audit.  This note sharply concentrates every three-component five-cut that
survives the sparse-row and star-boundary eliminations.  It does not prove
`(E5)`.

Let `G` be a minimum `E5` enemy, let `S` be a cut of order five, and let
`L_1,L_2,L_3` be the components of `G-S`.  Put

```text
J=G[S],
delta_i=|E(G[L_i])|+|E_G(L_i,S)|-4|L_i|,
k=|E(J)|.
```

Order the lobes so that `delta_1>=delta_2>=delta_3`.  The existing
three-component theorem gives

```text
J is triangle-free,
delta_1+delta_2+delta_3=13-k.                         (1)
```

## Lemma 1 (sharp rooted-`K_4` obstruction bound)

Fix a lobe `L`, a vertex `t in S`, and put `Z=S-{t}`.  If
`G[L union Z]` has no `Z`-rooted `K_4` model, then

```text
delta(L)<=3                         if |E(J-t)|=0,
delta(L)<=2                         if |E(J-t)|=1,
delta(L)<=1                         if |E(J-t)|>=2.   (2)
```

### Proof

Put `ell=|L|` and `H=G[L union Z]`.  Apply Fabila-Monroy--Wood
Theorem 15 to the four nominated vertices `Z`.  Thus `H` is a spanning
subgraph of an obstruction of class `A`--`F`.

As in the star-boundary elimination, no vertex of `L` lies in a clique
added behind a facial triangle of the planar skeleton.  A component of
such vertices would have external neighbourhood contained in that
triangle together with `t`, contrary to five-connectivity.  Hence every
lobe vertex lies in the skeleton.

Write `r=|E(J-t)|`.  After separating the edges with both ends nominated,
the six obstruction classes give the following bounds:

```text
class A: |E(H)|<=3ell+1+r,       r<=3;
class B: |E(H)|<=3ell+3,         r=0;
class C: |E(H)|<=3ell+2,         r=0;
class D: |E(H)|<=3ell+1+r,       r<=4;
class E: |E(H)|<=3ell+2+r,       r<=1;
class F: |E(H)|<=3ell+1,         r=0.                 (3)
```

These are direct counts from the six skeletons: in class `D` the only
possible nominated--nominated edges are on the outer four-cycle, while in
class `E` the only such edge joins the two nominated outer vertices.
On the other hand, with

```text
p_L(t)=|E_G({t},L)|<=ell,
```

exact lobe accounting gives

```text
|E(H)|=4ell+delta(L)-p_L(t)+r
      >=3ell+delta(L)+r.                            (4)
```

If `r=0`, comparison with (3) gives `delta(L)<=3`.  If `r=1`, classes
`B,C,F` are unavailable and comparison gives `delta(L)<=2`.  If `r>=2`,
only classes `A,D` can occur and comparison gives `delta(L)<=1`.  This is
(2).  \(\square\)

## Theorem 2 (exact concentration)

Every surviving three-component cut satisfies

```text
delta_1>=5.                                           (5)
```

Moreover,

```text
k=0:       delta_2,delta_3<=3,   delta_1>=7;
k=1:       delta_2,delta_3<=2,   delta_1>=8;
k>=2:      delta_2,delta_3<=1,   delta_1>=11-k.       (6)
```

The boundary `K_{1,4}` is already impossible by the separate star-boundary
theorem.

### Proof

The sparse-row theorem shows that `delta_1>=4`.  Suppose first that
`delta_1=4`.  For every nonisolated `t in S`, the rooted six-bag supply
theorem applied to `L_1` gives an `(S-{t})`-rooted `K^*_{4,2}` model with
`t` in a helper, because

```text
delta_1+d_J(t)>=5.
```

Consequently neither other lobe has an `(S-{t})`-rooted `K_4` model
avoiding `t`: such a model, the six-bag model, and the third lobe compose
to an explicit `K_7^-` model.

If `k>=3`, there is a nonisolated vertex `t` with
`|E(J-t)|>=2`.  Indeed, otherwise every nonisolated vertex has degree at
least `k-1`; for `k=3` equality would force a triangle, and for `k>=4`
the degree sum is already impossible on five vertices.  Lemma 1 gives
`delta_2,delta_3<=1`.  This contradicts
(1), since then `delta_2+delta_3=9-k>=3`.  If `k=2`, a nonisolated
vertex can be chosen with `|E(J-t)|=1`, giving
`delta_2,delta_3<=2`, whereas (1) requires their sum to be seven.  If
`k=1`, either end of the unique edge gives
`delta_2,delta_3<=3`, whereas their sum is eight.  Finally `k=0` is
impossible because (1) would make the sum of three excesses at most twelve.
This proves (5).

Now `delta_1>=5`, so the `L_1`-shore supplies the rooted six-bag model for
every `t in S`, including an isolated boundary vertex.  The same terminal
composition therefore shows that neither `L_2` nor `L_3` contains a rooted
`K_4` after any one boundary vertex is omitted.

If `k>=2`, some vertex `t` satisfies `|E(J-t)|>=2`, and Lemma 1 gives
`delta_2,delta_3<=1`.  For `k=1`, choose `t` outside the unique edge and
obtain the bound two.  For `k=0`, Lemma 1 gives the bound three.  Substitution
in (1) gives the lower bounds on `delta_1` in (6).  \(\square\)

## Proposition 3 (what a low-lobe contraction actually returns)

Suppose `k>=2` and let `B` be either low lobe.  If `B` is not a singleton,
then contracting `B` to one vertex produces a proper target-free graph at
or above the `E5` density threshold which is not five-connected.  Hence
there is a set

```text
T subseteq (S union L_1 union L_j),       |T|<=3,
```

where `L_j` is the other low lobe, such that deleting `T` disconnects the
uncontracted remainder and every resulting component meets `S-T`.

If both low lobes are singletons, then both have excess one.  Writing `A`
for the high lobe, its closed shore satisfies the exact identity

```text
|E(G[A union S])|=4|G[A union S]|-9.                  (7)
```

### Proof

Theorem 2 gives `delta(B)<=1`.  Contracting `B` replaces its internal and
boundary edges by five edges and changes the excess above the `E5`
threshold by `1-delta(B)`.  If `B` is not a singleton, minimality therefore
forces a cut of order at most four in the contraction.  The contracted
vertex belongs to every such cut, since otherwise it would lift to a cut
of order at most four in `G`.  Removing it leaves the asserted set `T`.
A component avoiding `S-T` would lie inside one original lobe and have at
most three external neighbours, contrary to five-connectivity.

A singleton full to `S` has excess one.  If both low lobes are singletons,
(1) gives `delta(A)+k=11`, which is exactly (7).  \(\square\)

## Exact nonclosure of the two--three-linkage lift

For nonempty triangle-free `J`, the missing-edge graph on `S` has vertex
cover number three.  Thus the cover-indexed virtual-edge completion of `S`
through the two low lobes requires three boundary-star realisations.  One connected full
lobe supplies one such realisation, but obtaining two from the other lobe
requires two vertex-disjoint connected **interior** subgraphs with prescribed
boundary-neighbour sets.

Xie's two--three linkage theorem does not supply this assertion.  It gives
two disjoint connected subgraphs containing two prescribed groups of
terminals when a specified completion is six-connected.  Here the terminals
are boundary vertices.  A returned tree may use one boundary terminal as an
internal vertex, so deleting the boundary does not leave the required
interior carrier.  This is not a harmless choice of a minimal tree.  In the
singleton residue of Proposition 3, two disjoint interior carriers are
literally impossible.

Nor does failure of the Xie completion presently give the required descent.
It returns a separator of order at most five in the completed lobe graph;
after the virtual edges and boundary terminals are restored, its lift need
not be a five-cut of `G`, and no proved inequality places excess at least
four on a strictly smaller component.

Thus the first unsupported inference is:

> a low lobe supplies two disjoint boundary-star carriers, or failure yields
> a genuinely smaller component behind a five-cut which retains excess at
> least four.

The narrow repair is an **interior-carrier-or-excess-descent lemma** for an
internally five-connected five-rooted lobe.  In the exact singleton residue,
the equivalent repair is a five-root reserve theorem for the high shore in
(7): it must produce five pairwise adjacent branch sets meeting the five
vertices of `S`, or a strict same-graph high-excess descent.  An ordinary
`K_6` minor at the Mader threshold does not retain those five root contacts.

## Dependencies

- The rooted six-bag supply and root-overlap-free composition in
  [`hc7_k7minus_e5_three_component_sparse_elimination.md`](hc7_k7minus_e5_three_component_sparse_elimination.md).
- The low-lobe contraction argument in
  [`hc7_k7minus_e5_two_component_rooted_reduction.md`](hc7_k7minus_e5_two_component_rooted_reduction.md).
- Ruy Fabila-Monroy and David R. Wood, *Rooted `K_4`-Minors*, Theorem 15.
- Shijie Xie, *6-Connected Graphs Are Two-Three Linked*, Theorem 1.2.1,
  used only to delimit the unsupported carrier inference above.
