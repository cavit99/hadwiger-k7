# Four-root carrier packing in a full degree-eight exterior

**Status:** computation-free unbounded theorem with an adjacent author-side
audit.  It gives a constant attachment core in the connected full exterior;
it does not bound vertices having at most three boundary neighbours.

Write `K_7^-` for `K_7` with one edge deleted.

## Theorem 1 (four common roots are terminal)

Let `G` have no `K_7^-` minor.  Let `v` be a vertex with an eight-set
`J=N_G(v)`, and let `C` be a connected subgraph disjoint from `N_G[v]`.
Fix a four-set `T subseteq J` for which `G[T]` contains an edge.  Then `C`
has at most three pairwise vertex-disjoint connected subgraphs which each
have a neighbour at every vertex of `T`.

### Proof

Suppose that `Q_0,Q_1,Q_2,Q_3` are four such carriers.  They may be
enlarged inside `C`, without losing disjointness or any root contact, so
that their contact graph is connected.  Indeed, repeatedly take a shortest
path in `C` between two current contact components and absorb its internal
vertices into the carrier at one end.  The internal vertices avoid every
current carrier, and the last path edge merges two contact components.

A connected graph on four vertices has a vertex with two neighbours.
Relabel so that the contact graph on `Q_1,Q_2,Q_3` has at least two edges,
and retain the fourth carrier as `Q_0`.  Write

```text
T={t_1,t_2,t_3,t_4}, with t_1t_2 an edge,
```

and choose distinct `x,y in J-T`.  The seven sets

```text
{v,x,y,t_3}, {t_1}, {t_2}, {t_4} union Q_0,
Q_1, Q_2, Q_3                                      (1)
```

are disjoint and connected.  The first bag is adjacent to all the others:
`v` sees the three boundary-bearing bags, while `t_3` sees the three last
carriers.  The next three bags form a clique, using `t_1t_2` and the
contacts of `Q_0` at `t_1,t_2`.  Each is adjacent to every one of
`Q_1,Q_2,Q_3` through its root in `T`.  Finally, at least two of the three
pairs among the last three bags are adjacent.  Thus at most one of the
twenty-one bag pairs is nonadjacent, so (1) is a `K_7^-` model, a
contradiction. `\square`

## Corollary 2 (the `210` attachment bound)

In the setting of Theorem 1, suppose `alpha(G[J])<=3`.  For `c in C` put

```text
a(c)=|N_G(c) cap J|.
```

Then

```text
sum_{c in C} binom(a(c),4) <= 210.                    (2)
```

Consequently the numbers of vertices of `C` having at least four, five,
six, seven and eight neighbours in `J` are at most, respectively,

```text
210, 42, 14, 6, 3.                                   (3)
```

### Proof

Every four-set `T subseteq J` contains an edge, since `alpha(G[J])<=3`.
The vertices adjacent to all of `T` are pairwise disjoint singleton
`T`-carriers.  Theorem 1 bounds their number by three.  Sum that bound over
the `binom(8,4)=70` choices of `T` and reverse the incidence count to get
(2).  A vertex with boundary degree at least `k` contributes at least
`binom(k,4)`; division of `210` by `1,5,15,35,70` gives (3). `\square`

## Critical-host application and scope

The connected full exterior at a critical degree-eight centre meets the
hypotheses with `J=N_G(v)` and `C=G-N_G[v]`.  The exceptional-neighbourhood
condition `alpha(J)=3` therefore gives (2) without any bound on `|C|`.

The construction is the boundary-eight extension of the frozen common
four-portal carrier theorem at SHA-256
`49f2056d05c2c9550dbfdbc3429fc09ed55da0e5acbba2209ecc153b7b8a851f`.
Two extra boundary vertices are simply unused; no virtual edge or
between-shore edge is introduced.

The result does not control vertices with at most three neighbours in `J`,
bound the order or internal edge count of `C`, or by itself eliminate the
connected full-exterior case.
