# Four-root carrier packing in a three-component six-cut

**Status:** written unbounded proof, pending separate audit.  The theorem
gives a target-sensitive packing bound and a constant boundary-incidence
core in every component of a returned three-component six-cut.  It does
not prove the remaining excess-five dichotomy or eliminate every sparse
boundary.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a
six-connected graph with no `K_7^-` minor, let `S` be a six-vertex cut,
and suppose that `G-S` has at least three components.  Every component is
adjacent to every vertex of `S`, since otherwise its neighbourhood would
be a cut of order at most five.

Fix a component `C` of `G-S`.  For `T subseteq S`, a **`T`-carrier** in
`C` is a connected subgraph of `C` having a neighbour at every vertex of
`T`.  Let `mu_T(C)` be the maximum number of pairwise vertex-disjoint
`T`-carriers in `C`.

## Lemma 1 (putting an omitted root into one carrier)

Let `T` be a proper subset of `S`, let `x in S-T`, and let
`Q_1,...,Q_k` be disjoint `T`-carriers in `C`.  One carrier can be
enlarged, without meeting the others, so that it has a neighbour at `x`.

### Proof

Choose `z in N_G(x) cap C`.  If `z` already lies in a selected carrier,
there is nothing to prove.  Otherwise, take a shortest path in `C` from
`z` to the union of the carriers.  Its last vertex lies in one carrier and
all its other vertices avoid every carrier.  Absorb those other vertices
into the carrier at the last vertex.  The enlarged carrier is connected,
remains disjoint from the others, retains all its contacts with `T`, and
contains the neighbour `z` of `x`.  \(\square\)

## Lemma 2 (three four-root carriers are terminal)

For every four-set `T subseteq S`,

```text
mu_T(C) <= 2.                                         (1)
```

### Proof

Suppose that `C` contains three disjoint `T`-carriers.  Write

```text
T={t_1,t_2,t_3,t_4}
```

and choose `x in S-T`.  By Lemma 1, after relabelling and enlargement the
carriers may be denoted `Q_0,Q_1,Q_2`, where `Q_0` has a neighbour at
`x`.  The five sets

```text
{x} union Q_0,  {t_1} union Q_1,  {t_2} union Q_2,
{t_3},  {t_4}                                      (2)
```

are disjoint and connected.  Every pair in (2) is adjacent except
possibly the last pair.  Indeed, a bag containing `Q_i` is adjacent to a
singleton `t_j` because `Q_i` is a `T`-carrier; two different carrier
bags are adjacent because the root in either one has a neighbour in the
other carrier.  Thus (2) is a `(T union {x})`-rooted `K_5^-` model in the
closed `C`-shore.

Let `y` be the sixth boundary vertex and choose two components `A,D` of
`G-S` different from `C`.  Add to (2) the bags

```text
A union {y},  D.
```

They are disjoint and connected.  Fullness makes each new bag adjacent
to all five rooted bags; `A union {y}` is adjacent to `D` through a
`y-D` edge.  The seven bags therefore form a `K_7^-` model, a
contradiction.  This proves (1).  \(\square\)

## Lemma 3 (a boundary two-edge triple lowers the packing to one)

Let `U subseteq S` have order three and suppose that `G[U]` has at least
two edges.  Then, for every `r in S-U`,

```text
mu_{U union {r}}(C)=1.                                (3)
```

### Proof

The whole connected component `C` is a carrier, so the left side of (3)
is at least one.  Suppose that `Q_0,Q_1` are two disjoint carriers for
`T=U union {r}`.  Choose `x in S-T` and use Lemma 1 so that `Q_0` has a
neighbour at `x`.  Then

```text
{x} union Q_0,  {r} union Q_1,  ({u}:u in U)          (4)
```

are five disjoint connected rooted bags.  The first two bags are adjacent
to each other and to every singleton in `U`, using the carrier property.
At least two of the three singleton pairs are literal boundary edges.
Consequently (4) is a rooted `K_5^-` model.  The two unused full
components complete it to `K_7^-` exactly as in Lemma 2, a contradiction.
Thus the packing number is one.  \(\square\)

## Corollary 4 (constant boundary-incidence core)

For `v in C`, put

```text
a(v)=|N_G(v) cap S|.
```

Then

```text
sum_{v in C} binom(a(v),4) <= 30.                     (5)
```

If `G[S]` contains a three-set spanning at least two edges, then the
stronger bound

```text
sum_{v in C} binom(a(v),4) <= 27                      (6)
```

holds.  Under the latter hypothesis, at most `27` vertices of `C` have
four or more boundary neighbours, at most `5` have five or more, and at
most one is adjacent to all six vertices of `S`.

### Proof

For a four-set `T subseteq S`, every vertex adjacent to all of `T` is a
singleton `T`-carrier.  Lemma 2 therefore gives

```text
|{v in C:T subseteq N_G(v)}| <= 2.                    (7)
```

Sum (7) over the fifteen four-sets and reverse the order of counting to
obtain (5).

Now fix a three-set `U` spanning at least two boundary edges.  For each of
the three vertices `r in S-U`, Lemma 3 improves (7) to one for the
four-set `U union {r}`.  The other twelve four-sets retain the bound two,
giving `3+2*12=27` and hence (6).  A vertex of boundary degree at least
four, five, or six contributes at least `1`, `5`, or `15`, respectively,
to its left side.  The three asserted numerical bounds follow.  \(\square\)

## Consequence for the sparse three-component row

Whenever `Delta(G[S])>=2`, a vertex of degree at least two together with
two of its neighbours gives the three-set required in Lemma 3 and
Corollary 4.  Thus every lobe has three simultaneous four-root carrier
packing numbers equal to one and has only a constant-size set of vertices
with four or more boundary neighbours.  In particular, an unbounded
arithmetic ray cannot be realised by repeating a fixed four-root
attachment mask.

This does not yet bound the coefficient-four excess: arbitrarily many
vertices may have at most three boundary neighbours, and their internal
edges still contribute to the excess.  The remaining unbounded task is to
turn the three packing-one statements in Lemma 3, together with internal
six-connectivity and five-rooted-model avoidance, into an excess bound or
a second carrier.

## Dependency

The completion of a shore-confined five-root `K_5^-` model by two other
full components is also recorded, with a separate GREEN audit, in
[`hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md`](hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md).
