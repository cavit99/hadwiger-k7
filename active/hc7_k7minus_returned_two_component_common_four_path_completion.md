# Common four-portal paths are terminal in a returned two-component six-cut

**Status:** proved unbounded target theorem.  It eliminates the aligned-path
recession family from the returned two-component row.  It does not eliminate
all two-component six-cuts or prove the Hadwiger-7 frontier.

Write `K_7^-` for `K_7` with one edge deleted.  Let `S` be a six-set in a
graph `G`, and let `A,B` be distinct components of `G-S`.  Assume that `A`
is connected and `S`-full.  These conditions hold on either shore of the
returned six-cut in a six-connected graph.

For a four-set `T subseteq S`, a **`T`-carrier** in `B` is a connected
subgraph of `B` having a neighbour at every vertex of `T`.  A family of
carriers is disjoint when their vertex sets are pairwise disjoint.  Its
**contact graph** joins two carriers when an edge of `G` has one end in
each.

For the singleton consequences, put

```text
U_T(B)={v in B : v is adjacent to every vertex of T}.
```

## Theorem 1 (common four-portal carrier completion)

Suppose that `G[T]` contains an edge.  If `B` contains four disjoint
`T`-carriers `Q_0,Q_1,Q_2,Q_3` such that the contact graph on
`Q_1,Q_2,Q_3` has at least two edges, then `G` contains a `K_7^-` minor.

### Proof

Write

```text
T={t_1,t_2,t_3,t_4},   with t_1t_2 in E(G),
S-T={x,y}.
```

Consider the seven branch sets

```text
A union {x,y,t_3},
{t_1}, {t_2}, {t_4} union Q_0, Q_1, Q_2, Q_3.          (1)
```

They are pairwise disjoint.  The first is connected because the connected
set `A` has a neighbour at each of `x,y,t_3`; the fourth is connected
because `Q_0` is a `T`-carrier and therefore has a neighbour at `t_4`.

The first bag is adjacent to every other bag.  It meets the three
boundary-bearing bags through fullness of `A`, and it meets each
`Q_i`, `1<=i<=3`, through the vertex `t_3`.

The other three boundary-bearing bags form a clique: `t_1t_2` is a
literal edge, while `Q_0` has a neighbour at both `t_1` and `t_2`.  Each
of these three bags is adjacent to each of `Q_1,Q_2,Q_3`, because all four
selected carriers are `T`-full.  Finally, at least two of the three pairs
among the last three carrier bags are adjacent.
Thus at most one pair among the seven bags in (1) is nonadjacent.  They
form a `K_7^-` minor model.  \(\square\)

The construction uses no edge between the open shores and no unspecified
virtual boundary edge.  In particular, it is insensitive to how the four
portal contacts are distributed elsewhere in either component.

## Lemma 2 (connecting disjoint carriers)

Let `H` be connected and let `Q_1,...,Q_k` be pairwise disjoint connected
subgraphs.  They can be enlarged, without losing connectivity or
disjointness, so that their contact graph is connected.

### Proof

Start with the given bags.  While their contact graph is disconnected,
choose a shortest path in `H` between bags in two different contact
components.  Its internal vertices avoid every current bag: if it first
met another bag, the corresponding initial or final subpath would be a
shorter path between two contact components.  Absorb all internal vertices
into the bag at one end.  That bag remains connected and disjoint from all
others, and the last edge of the path joins two former contact components.
The number of contact components strictly decreases, so the process
terminates.  \(\square\)

Enlarging a `T`-carrier preserves the carrier property.

## Corollary 3 (four-portal packet bound)

If `G` has no `K_7^-` minor and `G[T]` contains an edge, then `B` contains
at most three pairwise disjoint `T`-carriers.

### Proof

If four existed, apply Lemma 2 inside the connected component `B`.  Their
enlarged contact graph is connected, so one of its four vertices has at
least two neighbours.  Use that carrier and two of its neighbours as
`Q_1,Q_2,Q_3`, and use the remaining carrier as `Q_0` in Theorem 1.  This
gives the forbidden target.  \(\square\)

This is a packing restriction on arbitrary connected portal bags, not an
attachment-sum inequality.

## Corollary 4 (common-neighbour bound)

If `G` has no `K_7^-` minor and `G[T]` contains an edge, then

```text
|U_T(B)| <= 3.                                        (2)
```

### Proof

Four distinct common neighbours, used as singleton carriers, would
contradict Corollary 3.  \(\square\)

Thus four fixed portals with one literal boundary edge have at most three
common neighbours in either open shore of a target-free returned cut.

## Corollary 5 (portal-incidence census)

Let `mathcal T` be the family of four-sets `T subseteq S` for which
`G[T]` contains an edge.  In a target-free host,

```text
sum_{T in mathcal T}|U_T(B)| <= 3|mathcal T|.          (3)
```

Equivalently, if `a(v)=|N_G(v) cap S|`, then the left side counts, over
`v in B`, the edge-containing four-subsets of `N_G(v) cap S`.

In particular, if `alpha(G[S])<=3`, then every four-set belongs to
`mathcal T` and

```text
sum_{v in B} binom(a(v),4) <= 45.                     (4)
```

Hence at most `45` vertices of either lobe have four or more boundary
neighbours, at most `9` have five or more, and at most `3` see all six.

### Proof

Sum the bound `|U_T(B)|<=3` from Corollary 4 over `mathcal T` and reverse
the order of counting.  When `alpha(G[S])<=3`, all fifteen four-sets are
counted.  The three numerical consequences use contributions at least
`1,5,15`, respectively, in (4).  \(\square\)

Thus the carrier theorem gives a constant portal-incidence core even when
the open lobe has arbitrary order.  This census is a consequence of the
target model, not an attachment-excess hypothesis.

## Corollary 6 (target or aligned path)

Suppose that `G[T]` contains an edge.  If `B` contains a connected subgraph
`P` of order at least four every vertex of which is adjacent to every
member of `T`, then `G` contains a `K_7^-` minor.

### Proof

Four vertices of `P` are distinct members of `U_T(B)`, contrary to (2) in
a target-free graph.  \(\square\)

In particular, in a target-free returned two-component cut, a whole
connected lobe all of whose vertices see the same four-set `T` has order at
most three whenever `G[T]` contains an edge.

## 4. Elimination of the equality recession profile

The aligned recession profile in
[`hc7_k7minus_returned_two_component_contraction_descent.md`](hc7_k7minus_returned_two_component_contraction_descent.md)
has a path lobe whose every vertex sees the four common roots
`T={2,3,4,5}`.  Its displayed boundary contains the edge `34`.  Every path
of order at least four is therefore terminal by Corollary 6.

For the deterministic order-seventeen equality witness, an explicit model
is especially short.  Let its order-five path be `6,7,8,9,10` and its
order-six path be `11,12,13,14,15,16`.  The seven bags

```text
{0,1,2,6,7,8,9,10},
{3}, {4}, {5,11}, {14}, {15}, {16}                    (5)
```

form `K_7^-`; the sole missing pair is `{14},{16}`.  The first bag is the
full opposite path together with `0,1,2`.  Formula (5) also shows directly
why aligned low-root supply edges do not obstruct the actual target model:
one common root is absorbed into the opposite full component, while a
second common root turns an unused common neighbour into the third
boundary-bearing clique bag.

The standard-library
[`experiments/returned_two_component_common_four_path_verify.py`](experiments/returned_two_component_common_four_path_verify.py)
checks every branch-set condition in (5), in addition to the arithmetic and
six-connectivity checks already made for the equality witness.

## Exact scope

Theorem 1 is unbounded in both component orders and converts a concrete
four-portal carrier arrangement into the target itself.  Lemma 2 turns it
into the packing bound `nu_T(B)<=3` for every four-set containing a
boundary edge.  In particular, such a four-set has at most three literal
common neighbours in either open shore.  This removes the whole aligned
path recession family.

It does not show that an arbitrary dense lobe contains four vertices with
the same four portals, couple the general pole partitions of the two
contracted `K_7^vee` models, control the nested-separator excess, or
eliminate every returned two-component six-cut.  It is therefore a genuine
target-sensitive advance within that row, but not completion of the
Norin--Totschnig significance benchmark.
