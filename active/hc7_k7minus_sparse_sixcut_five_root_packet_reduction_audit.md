# Cold audit: sparse six-cut five-root and packet reductions

**Verdict:** GREEN.

**Audited source:**
[`hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md`](hc7_k7minus_sparse_sixcut_five_root_packet_reduction.md)

**Source SHA-256:**
`32c45ee41ee349e2499c82c49bd7a0af7cfd636620bbc7873edea4ca061e1100`

This is an independent internal mathematical audit, not external peer
review.  The results are unbounded local reductions.  The proposed
excess-five dichotomy (7) is explicitly left open.

## 1. Dependencies and hypotheses

The only imported extremal result is Norin--Totschnig, Lemma 12.  Its
primary-source statement was checked: an internally four-connected pair
`(F,Z)` with four roots and no `Z`-rooted `K^*_{4,2}` model satisfies

```text
|E(F)| <= 4|V(F)|-10.
```

The fifth-root augmentation used in Lemma 2 is Lemma 1 of
[`hc7_k7minus_e5_k5minus_cut_elimination.md`](hc7_k7minus_e5_k5minus_cut_elimination.md),
at audited SHA-256
`81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0`.
It requires an internally five-connected pair on the four old roots and
the fifth nominated vertex, exactly as used here.

Six-connectivity makes every component of `G-S` full to `S`: otherwise
its boundary would be a cut of order at most five.  No minimum-order or
minimum-degree assumption beyond six-connectivity is hidden in the source.

## 2. The shore-confined five-root terminal

Lemma 1 was reconstructed bag by bag.  A rooted `K_5^-` model in the
`C`-shore avoiding `x`, together with

```text
A union {x},  D,
```

gives seven disjoint connected bags.  Fullness makes each of the two new
bags adjacent to every rooted bag.  The first new bag is connected because
`A` has a neighbour at `x`, and it is adjacent to `D` through an
`x`--`D` edge.  Thus the only possible missing adjacency is the one
already permitted inside the rooted `K_5^-`.  This is an explicit
`K_7^-` model.

## 3. Internal connectivity and fifth-root augmentation

For `Z=S-{x,r}`, a forbidden rooted separation of
`G[C union Z]` of order at most three has a nonempty open side in `C`.
Putting `x,r` into its separator and all other components on its root side
produces a cut of `G` of order at most five.  Hence `(G[C union Z],Z)` is
internally four-connected.

Likewise, a forbidden rooted separation of

```text
(G[C union Z union {r}], Z union {r})
```

of order at most four becomes a cut of `G` of order at most five after
adding only `x`.  The pair is therefore internally five-connected, so the
audited augmentation lemma may place `r` in one helper of any existing
`Z`-rooted `K^*_{4,2}` model.

The subsequent `K_5^-` completion is exact.  If `U` is the helper
containing `r`, `V` the other helper, and `z` the root outside the chosen
three-set `T`, the five bags are

```text
U,  V union R_z,  (R_t : t in T).
```

The merge is connected because `V` meets `R_z`.  Helper--helper and
root--helper incidences make `U` universal and make `V union R_z`
adjacent to all three `T`-bags.  The two literal edges in `B[T]` leave at
most one missing pair among those three bags.  The five literal roots are
in distinct bags, so this is precisely the rooted model excluded by
Lemma 1.

Consequently Lemma 12 applies.  The edge count

```text
|E(G[C union Z])| = e_C + sum_{z in Z} a_z + |E(B[Z])|
```

and `|C union Z|=c+4` give (2).  Substituting
`eta(C)=e_C+sum_{s in S}a_s-4c` gives (3) with no rounding loss.

## 4. Connector--anchor packet composition

The shortest path between two disjoint packets in `C` has no internal
vertex in either packet.  Absorbing its internal vertices into the first
packet therefore preserves disjointness and connectivity and makes the two
packet bags adjacent.

Choose full packets in `A,D`, anchor them at distinct
`p,q in S-T`, and retain the two connected packet bags in `C`.  These four
bags form a clique:

- the two `C`-bags use the connector;
- the `A`-bag uses its anchor `p` to meet both `C`-packets and the
  `D`-packet; and
- the `D`-bag uses its anchor `q` to meet both `C`-packets.

Fullness makes all four bags adjacent to the three singleton bags in `T`.
At least two edges in `B[T]` leave at most one missing adjacency among the
singletons.  These are seven legal branch sets for `K_7^-`.  Corollary 4
then follows because a boundary vertex of degree at least two and two of
its neighbours span a three-set with two boundary edges, while every whole
component is itself one full packet.

## 5. Sharpness examples

For the universal edge `C=K_2` over an independent six-set, every proper
nonempty part of `C` has all six roots in its neighbourhood, so the rooted
pair is internally six-connected.  In any model on five roots only two
root bags can contain an internal vertex.  A remaining bag cannot use the
omitted boundary vertex without also using an internal vertex, because the
boundary is independent.  Hence at least three bags are singleton roots
and are pairwise nonadjacent.  This verifies rooted `K_5^-` avoidance and
the sharp value `eta(C)=5`.

The repaired unbounded family is also correct.  For `C=K_t`, one clique
vertex sees all six roots and every other clique vertex sees the same five.
Every proper nonempty subset of `C` has at least five boundary neighbours
and at least one neighbour in `C`; all of `C` has the six roots as its
neighbourhood.  Thus the pair is internally six-connected.  Every full
packet contains the unique neighbour of the sixth root, so two disjoint
full packets are impossible.  Finally,

```text
eta(C)=binom(t,2)+(5t+1)-4t=binom(t,2)+t+1,
```

which is unbounded.  For `t>=4`, four clique vertices assigned to four of
the five common-root bags, with the last root singleton, give the stated
rooted `K_5`; hence this family does not evade Lemma 1.

## 6. Scope verdict

The source proves a target-sensitive coefficient-four inequality and an
unbounded packet-composition terminal for arbitrary component order.  It
does not prove dichotomy (7), eliminate all sparse three-component
boundaries, prove the returned six-cut programme, or prove the Hadwiger-7
frontier.  Its status paragraph and final section state those limitations
accurately.

## Primary source

- Sergey Norin and Agnès Totschnig, *Every graph with no
  `K_7^vee`-minor is `6`-colorable*, Lemma 12,
  [arXiv:2507.03244](https://arxiv.org/abs/2507.03244).
