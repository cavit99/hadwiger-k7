# Five-root and packet reductions for a sparse returned six-cut

**Status:** proved local reductions.  They apply to components of arbitrary
order.  They do not by themselves bound every component excess or eliminate
the sparse three-component case.

Write `K_7^-` for the graph obtained from `K_7` by deleting one edge.  Let
`G` be a six-connected graph with no `K_7^-` minor, let `S` be a cut of
order six, and suppose that `G-S` has exactly three components `A,C,D`.
Six-connectivity makes every component `S`-full.  Put `B=G[S]`.

For a component `C`, write

```text
c=|C|,  e_C=|E(G[C])|,  a_s=|E_G(C,{s})|,
P=sum_{s in S} a_s,  eta(C)=e_C+P-4c.
```

A connected subgraph of `C` is an **`S`-full packet** if it has a neighbour
at every vertex of `S`.  Let `mu_S(C)` be the maximum number of pairwise
vertex-disjoint `S`-full packets in `C`.

## 1. The five-root terminal object

### Lemma 1 (shore-confined rooted near-clique is terminal)

For every `x in S`, the closed shore `G[C union (S-{x})]` contains no
`(S-{x})`-rooted `K_5^-` model.

### Proof

Suppose that five rooted bags `R_s`, `s in S-{x}`, give such a model in the
displayed closed shore.  Let `A,D` be the other two components of `G-S`.
The seven bags

```text
(R_s : s in S-{x}),  A union {x},  D
```

are connected and disjoint.  Both component bags meet every rooted bag
through its literal root.  The bag `A union {x}` is adjacent to `D`, since
`D` has a neighbour at `x`.  Thus the only possible missing adjacency is
the one already allowed among the five rooted bags.  This is a `K_7^-`
model, a contradiction.  \(\square\)

## 2. A coefficient-four inequality from a boundary path

We use Norin--Totschnig, Lemma 12: if `(F,Z)` is internally
four-connected, `|Z|=4`, and `F` has no `Z`-rooted `K^*_{4,2}` model, then

```text
|E(F)| <= 4|V(F)|-10.                                  (1)
```

In a `Z`-rooted `K^*_{4,2}` model the four root bags are each adjacent to
two adjacent helper bags; no adjacency between distinct root bags is
required.

### Lemma 2 (five-root path inequality)

Let `P_0={x,r}` be a pair of boundary vertices and put `Z=S-P_0`.  Suppose
that some three-set `T subseteq Z` spans at least two edges in `B`.  Then

```text
e_C + sum_{z in Z} a_z + |E(B[Z])| <= 4c+6,             (2)
```

or, equivalently,

```text
a_x+a_r >= eta(C)+|E(B[Z])|-6.                          (3)
```

### Proof

The pair `(G[C union Z],Z)` is internally four-connected.  Indeed, a
rooted separation of order at most three, together with `x,r`, would give
a cut of `G` of order at most five.

Suppose that `G[C union Z]` contains a `Z`-rooted `K^*_{4,2}` model.  The
larger pair

```text
(G[C union Z union {r}], Z union {r})
```

is internally five-connected by the same separator lift, now using only
the omitted vertex `x`.  The fifth-root augmentation lemma therefore
chooses the model so that `r` belongs to one helper, say `U`.

Let `z` be the unique vertex of `Z-T`, let `R_z` be its root bag, and let
`V` be the other helper.  Retain `U` as the bag rooted at `r`, merge
`V` with `R_z`, and retain the three root bags indexed by `T`.  The bag
`U` is adjacent to all four other bags.  The bag `V union R_z` is connected
and is adjacent to all three `T`-bags.  Finally, the at least two literal
edges of `B[T]` leave at most one missing adjacency among those three
bags.  These five bags form an `(S-{x})`-rooted `K_5^-` model, contrary to
Lemma 1.

There is consequently no rooted `K^*_{4,2}` model.  Apply (1) to
`G[C union Z]`.  Since this graph has `c+4` vertices and

```text
|E(G[C union Z])|=e_C+sum_{z in Z}a_z+|E(B[Z])|,
```

inequality (2) follows.  Substitution of
`eta(C)=e_C+P-4c` gives (3).  \(\square\)

The Rolek--Song--Thomas generalised-chain lemma does not supply an
additional shore inequality here: its hypotheses concern the neighbourhood
of a degree-`k+s` vertex in a `k`-contraction-critical graph, whereas an
arbitrary closed shore has neither hypothesis.

## 3. Four packets and a boundary path are terminal

### Lemma 3 (connector--anchor packet completion)

Suppose that one component, say `C`, contains two disjoint `S`-full
packets.  If some three-set of `S` spans at least two boundary edges, then
`G` contains a `K_7^-` minor.

### Proof

Let `C_1,C_2` be two disjoint packets in `C`.  Take a shortest
`C_1`--`C_2` path in `G[C]`.  Its internal vertices avoid both packets.
Absorb its internal vertices into `C_1`; the resulting connected bag and
`C_2` are disjoint and adjacent.

Let `A_1,D_1` be one `S`-full packet in each of the other two components.
Choose a three-set `T subseteq S` spanning at least two edges.  From the
three vertices of `S-T`, choose distinct `p,q`, and enlarge `A_1` by `p`
and `D_1` by `q`.  These enlarged bags are connected.

The four packet bags form a clique.  The two bags in `C` are adjacent by
the chosen connector.  Every other pair is adjacent through one of the
anchors `p,q`, because each unanchored packet is `S`-full; in particular,
the two anchored packets are adjacent since the packet containing `q`
has a neighbour at `p`.

Retain the three vertices of `T` as singleton bags.  Every packet bag is
adjacent to every singleton, and at most one adjacency is missing among
the three singletons.  The four packet bags and three singleton bags are a
`K_7^-` model.  \(\square\)

### Corollary 4 (packet-one regime)

If `Delta(B)>=2`, then

```text
mu_S(A)=mu_S(C)=mu_S(D)=1.                              (4)
```

### Proof

A vertex of boundary degree at least two and two of its neighbours give a
three-set spanning at least two edges.  Every component is itself an
`S`-full packet, so each packing number is at least one.  Lemma 3 excludes
packing number at least two in any component.  \(\square\)

This also verifies the aggregate packet count directly: if the total
packet number is four, its vector is `(2,1,1)` up to order, and Lemma 3 is
terminal whenever `Delta(B)>=2`.

## 4. Sharpness and the remaining unbounded target

The constant five is the best possible value in a prospective theorem
bounding `eta(C)` under five-rooted near-clique avoidance.  Let `B` be
independent and let `C=uv` be an edge with both `u,v` adjacent to every
vertex of `S`.  Then `(G[C union S],S)` is internally six-connected and

```text
eta(C)=1+12-8=5.                                       (5)
```

Every model on five boundary roots has at least three root bags containing
neither `u` nor `v`; those three bags are pairwise nonadjacent.  Hence no
five-rooted `K_5^-` model exists.

Packing number one alone gives no excess bound.  For any `t>=4`, let
`C=K_t`, let one vertex be adjacent to all six roots, and let each of the
other `t-1` vertices be adjacent to the same five roots.  The pair is
internally six-connected: a proper nonempty subset of `C` has at least five
boundary neighbours and at least one neighbour in `C`, while all of `C`
has neighbourhood `S`.  Every `S`-full connected subgraph must contain the
unique vertex adjacent to the sixth root, and thus `mu_S(C)=1`, while

```text
eta(C)=binom(t,2)+(5t+1)-4t=binom(t,2)+t+1,             (6)
```

which is unbounded.  This family is correctly excluded by Lemma 1: the five
common roots have a rooted `K_5` model, obtained by assigning four clique
vertices to four root bags and leaving the fifth root as a singleton.

Thus the sharp packet-one target is the target-sensitive dichotomy

```text
eta(C)>=6  =>  a five-rooted K_5^- model or mu_S(C)>=2. (7)
```

Lemma 3 turns this into the target when `Delta(B)>=2`, because every lobe
then has `mu=1`.  For a matching boundary, however, (7) leaves a possible
`mu=2` lobe with uncontrolled excess.  Closing the full sparse row requires
the stronger packet-weighted alternative `eta(C)<=5 mu_S(C)` under
rooted-model exclusion, equivalently `eta(C)>=5 mu_S(C)+1` forces the rooted
model.  Neither statement is proved here.  The examples (5)--(6) show
respectively that the packet-one threshold would be sharp and that the
rooted exception cannot be omitted.

## References

- Sergey Norin and Agnès Totschnig, *Every graph with no
  `K_7^vee`-minor is `6`-colorable*, Lemma 12,
  [arXiv:2507.03244](https://arxiv.org/abs/2507.03244).
- The fifth-root augmentation lemma is Lemma 1 of
  [`hc7_k7minus_e5_k5minus_cut_elimination.md`](hc7_k7minus_e5_k5minus_cut_elimination.md).
