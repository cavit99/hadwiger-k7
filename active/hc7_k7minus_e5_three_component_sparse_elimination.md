# Sparse three-component five-cut reduction

**Status:** written computation-free unbounded theorem; separate internal
audit GREEN.  This eliminates every exact-density three-component row in
which all three lobe excesses are at most three, and every row whose
boundary is `K_{1,4}`.  It does not prove `(E5)`.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a minimum `E5`
enemy with

```text
|E(G)|=4|V(G)|-7.
```

Let `S` be a cut of order five, let `L_1,L_2,L_3` be the components of
`G-S`, and put

```text
J=G[S],
delta_i=|E(G[L_i])|+|E_G(L_i,S)|-4|L_i|.
```

Every `L_i` is connected and adjacent to every vertex of `S`, and
`(G[L_i union S],S)` is internally five-connected.  The existing
three-component theorem says that `J` is triangle-free.  Direct edge
accounting gives

```text
delta_1+delta_2+delta_3=13-|E(J)|.                    (1)
```

In a `Z`-rooted `K^*_{4,2}` model, four root bags are each adjacent to two
adjacent helper bags; adjacency between distinct root bags is not required.

## Lemma 1 (two lobe models)

Fix a component `L` of `G-S`, a vertex `t in S`, and put `Z=S-{t}`.  Write

```text
delta=|E(G[L])|+|E_G(L,S)|-4|L|,
p(t)=|E_G({t},L)|.
```

The following statements hold.

1. If

   ```text
   delta+d_J(t)>=5,                                   (2)
   ```

   then `G[L union S]` has a `Z`-rooted `K^*_{4,2}`
   model in which `t` belongs to a helper bag.

2. If

   ```text
   delta+|E(J-t)|>=6,                                 (3)
   ```

   then `G[L union (S-{t})]` has a `Z`-rooted `K_4`
   model.  In particular, this model avoids `t`.

3. If `p(t)<=delta-1`, the model in assertion 1 exists even without
   assuming (2).

### Proof

Let `ell=|L|` and first complete `Z` to a clique by adding only missing
edges with both ends in `Z`.

Suppose that `p(t)<=delta-1`, and omit `t`.  The resulting graph `H_0` has

```text
|V(H_0)|=ell+4,
|E(H_0)|=4ell+delta-p(t)+6>=4|V(H_0)|-9.              (4)
```

The pair `(H_0,Z)` is internally four-connected.  A separation of order at
most three would extend to a separation of `(G[L union S],S)` of order at
most four by putting `t` in its boundary.  Norin--Totschnig Lemma 12 gives
a `Z`-rooted `K^*_{4,2}` model.  The added edges join distinct nominated
roots and are not required root--helper or helper--helper adjacencies, so
they may be deleted.  The fifth-root augmentation lemma then places `t` in
one helper in the original internally five-connected pair.  This proves
assertion 3 and the first case of assertion 1.

It remains for assertion 1 to assume `p(t)>=delta`.  Retain `t` and call
the completed graph `H_1`.  Exact accounting gives

```text
|V(H_1)|=ell+5,
|E(H_1)|=4ell+delta+6+d_J(t)>=4|V(H_1)|-9.            (5)
```

The pair `(H_1,Z)` is internally four-connected.  The only new possible
open side, compared with the internally five-connected pair rooted at
`S`, is the singleton `{t}`.  But

```text
d_{H_1}(t)>=p(t)+d_J(t)>=delta+d_J(t)>=5,
```

so this is impossible for a separation of order at most three.  Lemma 12,
deletion of the virtual root--root edges, and fifth-root augmentation now
give assertion 1.

For assertion 2, omit `t` without completing `Z`.  Put

```text
H=G[L union Z].
```

The pair `(H,Z)` is internally four-connected by the same separation
extension used for `H_0`, and

```text
|E(H)|=4ell+delta-p(t)+|E(J-t)|
      >=3ell+delta+|E(J-t)|.
```

If (3) holds, this is at least `3ell+6`, whereas
Norin--Totschnig Lemma 9 bounds a graph with no `Z`-rooted `K_4` model by

```text
3|V(H)|-7=3ell+5.
```

This contradiction proves assertion 2.  \(\square\)

## Lemma 2 (terminal composition without root overlap)

Let `A,B,C` be the three components of `G-S`, fix `t in S`, and put
`Z=S-{t}`.  Suppose that

- `G[A union Z]` has a `Z`-rooted `K_4` model; and
- `G[B union S]` has a `Z`-rooted `K^*_{4,2}` model in which `t` belongs
  to one helper.

Then `G` contains a `K_7^-` minor.

### Proof

Write the rooted `K_4` bags in the `A`-shore as `(Q_z:z in Z)`.  Write the
root bags in the `B`-shore as `(R_z:z in Z)` and its helper bags as `U,V`,
where `t in U`.  For each `z in Z`, put

```text
M_z=Q_z union R_z.
```

The two parts of `M_z` meet at `z`, so `M_z` is connected.  The four
sets `M_z` are disjoint and pairwise adjacent through the rooted `K_4`
model.  They are each adjacent to `U` and `V`, and `U` is adjacent to `V`.

Retain the whole component `C` as the seventh branch set.  It is adjacent
to each `M_z` through `z` and to `U` through `t`; it may miss only `V`.
Thus

```text
{M_z:z in Z}, U, V, C
```

is an explicit `K_7^-` model.  Notice that the rooted `K_4` model avoids
`t`.  This is essential: collapsing a second fifth-root-augmented
six-bag model would put `t` into both a root bag and the retained helper.
\(\square\)

## Theorem 3 (all five- and six-edge no-high-excess rows are impossible)

Suppose that

```text
delta_i<=3 for i=1,2,3.                               (6)
```

Then `|E(J)|=4`, and

```text
delta_1=delta_2=delta_3=3.                            (7)
```

### Proof

Since `J` is triangle-free, `|E(J)|<=6`.  Equations (1) and (6) give
`|E(J)|>=4`.

If `|E(J)|=6`, equality in Mantel's theorem gives `J=K_{2,3}`.  The
excess multiset is either `{3,3,1}` or `{3,2,2}`.  Choose `t` in the
two-vertex part of `J`.  Then

```text
d_J(t)=3,                 |E(J-t)|=3.
```

Use an excess-three component for assertion 2 of Lemma 1.  In the
`{3,3,1}` row use the other excess-three component for assertion 1 and
retain the last component.  In the `{3,2,2}` row use either excess-two
component for assertion 1 and retain the other.  Lemma 2 gives a
`K_7^-` minor in both cases.

Suppose that `|E(J)|=5`.  Equation (1) forces the excess multiset
`{3,3,2}`.  A triangle-free graph on five vertices with five edges is a
five-cycle or a four-cycle with one pendant edge.  In either case it has a
vertex `t` of degree two, and hence `|E(J-t)|=3`.  One excess-three
component supplies the rooted `K_4` in Lemma 1(2), the other supplies the
six-bag model in Lemma 1(1), and Lemma 2 again gives the target.

The only remaining possibility is `|E(J)|=4`.  Equation (1) and (6) then
force (7).  \(\square\)

## Theorem 4 (exact four-edge residue)

Under the hypotheses of Theorem 3, the four-edge boundary `J` is one of

```text
K_{1,4},
or the tree obtained from K_{1,3} by subdividing one edge.              (8)
```

More precisely, put

```text
p_i(s)=|E_G({s},L_i)|,             ell_i=|L_i|.
```

For every lobe `L_i`:

1. if `d_J(s)<=1`, then `p_i(s)>=3`;
2. if `d_J(s)>=2`, then `G[L_i union (S-{s})]` has no
   `(S-{s})`-rooted `K_4` model and

   ```text
   p_i(s)>=ell_i+2-d_J(s).                            (9)
   ```

In the subdivided-claw row, if `u` is its degree-two vertex and `c` its
degree-three vertex, then, for every `i`,

```text
ell_i>=4,
p_i(u)=ell_i,
p_i(c)>=ell_i-1,                                      (10)
```

and `G[L_i union (S-{u})]` is an equality obstruction for the rooted
`K_4` bound:

```text
|E(G[L_i union (S-{u})])|
   =3|L_i union (S-{u})|-7.                           (11)
```

In the `K_{1,4}` row every lobe has order at least three.  If `c` is the
centre and `x` a leaf, then

```text
p_i(c)>=ell_i-2,                 p_i(x)>=3.            (12)
```

### Proof

Fix `i`.  If `d_J(s)<=1`, then

```text
delta_i+|E(J-s)|=3+4-d_J(s)>=6.
```

Lemma 1(2) supplies a rooted `K_4` avoiding `s` in either of the other
lobes as well.  If `p_i(s)<=2=delta_i-1`, Lemma 1(3) supplies the
six-bag model with `s` in a helper.  Lemma 2, using a different lobe for
the rooted `K_4`, gives the target.  Thus `p_i(s)>=3`.

If `d_J(s)>=2`, Lemma 1(1) supplies the six-bag model in each of the two
lobes other than `L_i`.  A rooted `K_4` avoiding `s` in `L_i` would give
the target by Lemma 2.  Hence no such model exists.  Lemma 9 and exact
edge accounting give

```text
4ell_i+3-p_i(s)+4-d_J(s)<=3ell_i+5,
```

which is (9).

Connectedness of `L_i` gives

```text
sum_{s in S}p_i(s)
 =4ell_i+3-|E(G[L_i])|
 <=3ell_i+4.                                          (13)
```

A triangle-free graph on five vertices with four edges is either
`K_{1,4}`, a subdivided `K_{1,3}`, `P_5`, or `C_4` together with an
isolated vertex.  In the `P_5` row, assertions 1 and 2 lower-bound the
left side of (13) by `3ell_i+6`, a contradiction.  In the
`C_4`-plus-isolated row they lower-bound it by `4ell_i+3`; the isolated
vertex has at least three neighbours in `L_i`, so `ell_i>=3`, and this
again contradicts (13).  This proves (8).

In the subdivided-claw row, (9) makes the degree-two vertex complete to
`L_i` and gives `p_i(c)>=ell_i-1`; the three leaves each have at least
three neighbours in `L_i`.  Combining these bounds with (13) gives
`ell_i>=4` and (10).  Substitution into the edge identity, using the two
edges of `J-u`, gives (11).

For `K_{1,4}`, assertion 1 gives the leaf bounds, (9) gives the centre
bound, and a leaf with three neighbours gives `ell_i>=3`.  This is (12).
\(\square\)

## Theorem 5 (the subdivided claw is impossible)

The second boundary form in (8), the subdivided `K_{1,3}`, does not occur.

### Proof

Let `u` be its degree-two vertex and fix a lobe `L_i`.  Put

```text
Z=S-{u},                    H=G[L_i union Z].
```

Theorem 4 says that `(H,Z)` is internally four-connected, that `H` has no
`Z`-rooted `K_4` model, and that

```text
|E(H)|=3|V(H)|-7.                                      (14)
```

We use the equality case already contained in the proof of
Norin--Totschnig Lemma 9.  Their proof applies the rooted-`K_4`
trichotomy of Robertson, Seymour and Thomas.  Internal four-connectivity
excludes its separation outcome.  In the trisection outcome the induction
in that proof gives the strict bound `|E(H)|<=3|V(H)|-8` (and in its
nontrivial recursive case the stronger bound `3|V(H)|-9`).  Equality in
(14) therefore forces the planar outcome: `H` has a plane drawing in which
all four vertices of `Z` are incident with the outer face.

In any such drawing the outer facial walk has length at least four.  Euler's
formula and the fact that every inner face has length at least three give

```text
|E(H)|<=3|V(H)|-3-lambda,
```

where `lambda` is the length of the outer facial walk.  Equality in (14)
forces `lambda=4`, every inner face to be a triangle, and the outer walk to
contain exactly the four distinct roots.  Hence the four roots induce the
four edges of the outer cycle.

This is impossible.  The graph `J-u` has only the two edges from the
degree-three vertex of the subdivided claw to its two unsubdivided leaves,
and `H[Z]=J-u`.  Thus `H[Z]` cannot contain a four-cycle.  \(\square\)

## Theorem 6 (two excess-three star lobes are terminal)

More generally, suppose that a three-component five-cut in a minimum `E5`
enemy has boundary `K_{1,4}`.  If two of its lobes have excess at least
three, then `G` contains a `K_7^-` minor.  In particular, the first boundary
form in (8), with excesses `(3,3,3)`, does not occur.

For a lobe `L`, continue to write

```text
delta(L)=|E(G[L])|+|E_G(L,S)|-4|L|.
```

### Proof

Write the centre of the star as `t` and its leaves as `x,y,r,s`.  Name two
lobes of excess at least three `A,B`, and call the third `C`.

We first construct an `(S-{x})`-rooted `K^*_{4,2}` model in the `A`-shore
with `x` in a helper.  Complete the four roots

```text
S-{x}={t,y,r,s}
```

to a clique and also add the one virtual edge `xr`.  If
`p_A(x)=|E_G({x},A)|>=2`, the augmented graph on `A union S` has

```text
4|A|+delta(A)+4+4>=4|A|+11=4|A union S|-9         (15)
```

edges.  Its pair rooted at `S-{x}` is internally four-connected.  Indeed,
the only possible additional open side is the singleton `{x}`, and `x`
has its edge to `t`, the virtual edge to `r`, and at least two neighbours
in `A`.

If `p_A(x)=1`, omit `x` first.  Completing the four roots gives

```text
4|A|+delta(A)-1+6>=4|A|+8
   >=4|A union (S-{x})|-9.                           (16)
```

The rooted pair is internally four-connected by putting `x` into the
boundary of any putative separation.  In either case
Norin--Totschnig Lemma 12 applies.  Delete the virtual edges having both
ends among the four roots; no root--root adjacency is required by the
model.  In the second case restore `x` and the edge `xr`.  The fifth-root
augmentation lemma, applied in the graph with the one remaining virtual
edge `xr`, gives a model

```text
(R_z^A:z in S-{x}),       U_x, V_A,
```

where `x in U_x`.  The only nonliteral edge which this model may use is
`xr`.

The same construction in the `B`-shore, with roots `S-{y}` and the one
virtual edge `yr`, gives

```text
(R_z^B:z in S-{y}),       U_y, V_B,
```

where `y in U_y`.  Again, only `yr` may be a nonliteral model edge.

Cross-merge the two models according to their boundary vertices:

```text
M_x=U_x union R_x^B,
M_y=R_y^A union U_y,
M_t=R_t^A union R_t^B,
M_r=R_r^A union R_r^B union C,
M_s=R_s^A union R_s^B.
```

Each union is connected: the `A`- and `B`-parts of every `M`-bag meet at
its displayed boundary vertex, and the connected full lobe `C` has an edge
to `r`.
The five sets are mutually disjoint.  They form a `K_5` model.  Indeed,
`M_x` is adjacent to the other four through the first six-bag model, and
`M_y` is adjacent to the other four through the second.  The bag `M_r` is
adjacent to `M_t,M_s` through the full lobe `C`, while `ts` is a literal
edge of the boundary star.  The edges from `C` to `x` and `y` also realise
the two possible virtual adjacencies `xr` and `yr` after `C` is absorbed
into `M_r`.

Finally retain `V_A` and `V_B` as two further branch sets.  The first is
adjacent to all five `M`-bags through the roots and the helper `U_x`; the
second is adjacent to all five through the roots and `U_y`.  They may miss
only each other.  Thus

```text
M_x,M_y,M_t,M_r,M_s,V_A,V_B
```

are the branch sets of a `K_7^-` minor, a contradiction.  \(\square\)

At exact density, a surviving three-component star cut would satisfy

```text
delta_1+delta_2+delta_3=9.
```

After ordering the excesses, Theorem 6 therefore forces

```text
delta_1>=5,                 delta_2,delta_3<=2.        (17)
```

## Theorem 7 (the star boundary is impossible)

No three-component five-cut in a minimum `E5` enemy has boundary
`K_{1,4}`.

### Proof

Write the centre of the star as `t`, put `Z=S-{t}`, and fix a lobe `L`.
The graph

```text
H=G[L union Z]
```

has no `Z`-rooted `K_4` model.  Otherwise, let its four rooted bags be
`Q_z` for `z in Z`, and let `A,B` be the other two lobes.  Then

```text
{Q_z:z in Z}, {t}, A, B
```

are seven disjoint connected branch sets.  The first four are pairwise
adjacent; the singleton `{t}` is adjacent to all four through the four
edges of the boundary star; and each of `A,B` is adjacent to all five of
those bags because it is full to `S`.  Only `AB` may be absent.  This is a
`K_7^-` model.

Apply Fabila-Monroy--Wood Theorem 15 to `H`, nominated at the four members
of `Z`.  It says that `H` is a spanning subgraph of one of six rooted
obstructions.  Such an obstruction is obtained from a planar skeleton by
adding, at each of some facial triangles `T`, a clique `X_T` complete to
`T`.

No vertex of `L` can belong to an added clique.  If it did, take a
component `Y` of the graph induced by the vertices of `L` in one `X_T`.
The four nominated vertices belong to the skeleton, distinct lobes have no
edge between them, and the only vertex of `S` absent from `H` is `t`.
Consequently

```text
N_G(Y) subseteq T union {t},
```

contrary to five-connectivity.  Hence every vertex of `H` belongs to the
planar skeleton.

Put `ell=|L|`.  Since the four roots are independent in `H`, the six
obstruction classes give the following exact upper bounds.

- In class `A`, the skeleton has five vertices and seven edges, three of
  which join nominated vertices.  Thus `ell=1` and `|E(H)|<=4`.
- In class `B`, the skeleton has two non-root vertices and nine edges, so
  `ell=2` and `|E(H)|<=9=3ell+3`.
- In class `C`, the skeleton has three non-root vertices and eleven edges,
  so `ell=3` and `|E(H)|<=11=3ell+2`.
- In class `D`, the planar skeleton has the four roots on its outer
  four-cycle and therefore has `3(ell+4)-7` edges.  The four outer-cycle
  edges are absent from `H`, so `|E(H)|<=3ell+1`.
- In class `E`, before the two nominated degree-two vertices are added,
  the planar skeleton has an outer four-cycle and all internal faces
  triangular.  The full obstruction has at most `3(ell+4)-9` edges, and
  one edge joins its other two nominated vertices.  That edge is absent
  from `H`, so `|E(H)|<=3ell+2`.
- In class `F`, deleting the four nominated degree-two vertices leaves a
  plane graph with outer face of length four and all internal faces
  triangular.  Hence `|E(H)|<=3(ell+4)-11=3ell+1`.

In all six cases,

```text
|E(H)|<=3ell+3.                                      (18)
```

On the other hand, if `p_L(t)=|E_G({t},L)|`, exact lobe accounting and
the fact that `Z` is independent give

```text
|E(H)|=4ell+delta(L)-p_L(t)>=3ell+delta(L).           (19)
```

Equations (18) and (19) imply `delta(L)<=3`.  This holds for every lobe.
Their excesses sum to nine, so all three equal three.  Theorem 6 then gives
an explicit `K_7^-` model, a contradiction.  \(\square\)

## Scope and exact survivor

The argument eliminates every exact-density three-component row in which
all lobe excesses are at most three, and every excess row over the star
boundary.  The subdivided-claw row first forces
a boundary vertex complete to every lobe and equality in the rooted-`K_4`
obstruction theorem; the equality case eliminates it.  The final star row
requires two differently rooted six-bag models and uses the third lobe to
realise their two virtual edges simultaneously.  The same construction
first reduces every remaining exact-density star row to the concentrated
high-excess form (17).  The full rooted-`K_4` obstruction classification
then excludes even that form.

The tempting stronger composition using two fifth-root-augmented models
with the same omitted vertex is not valid: both models contain that vertex
in a helper.  Collapsing one model into root bags therefore overlaps the
helper retained from the other.  The cross-root construction in Theorem 6
avoids that overlap rather than collapsing either augmented model.

## Dependencies

- The fifth-root augmentation lemma in
  [`hc7_k7minus_e5_k5minus_cut_elimination.md`](hc7_k7minus_e5_k5minus_cut_elimination.md).
- Sergey Norin and Agnes Totschnig, *Every graph with no
  `K_7^vee`-minor is 6-colourable*, Lemmas 9 and 12,
  <https://arxiv.org/abs/2507.03244>.
- The exact-density and triangle-free-boundary conclusions in
  [`hc7_k7minus_e5_k5minus_cut_elimination.md`](hc7_k7minus_e5_k5minus_cut_elimination.md).
- Ruy Fabila-Monroy and David R. Wood, *Rooted `K_4`-Minors*, Electronic
  Journal of Combinatorics 20(2) (2013), P64, Theorem 15,
  <https://doi.org/10.37236/3476>.
