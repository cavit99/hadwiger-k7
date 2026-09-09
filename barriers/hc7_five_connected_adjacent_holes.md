# Five-connectivity does not upgrade adjacent missing edges

**Status:** written counterexample, with a
[separate internal audit](hc7_five_connected_adjacent_holes_audit.md).
No finite computation is a premise. All graphs are finite and simple.
Write `K7^vee` for K7 with two adjacent edges deleted and
`Q7=K7-2K2` for K7 with two independent edges deleted.

**Refuted assertion.** Every five-connected graph with a `K7^vee` minor
contains a Q7 minor.

## Construction

Let P be the cycle `0,1,2,3,4,5,0` with the additional edge `02`.
Let A be the independent triple `{a,b,c}`, and put `G=A join P`.
Thus G has nine vertices and 25 edges. Its minimum degree is five:
the vertices `1,3,4,5` have degree five and all others have degree six.
The triangle `012` and the cyclic colour sequence `0,1,2,0,1,2`
give `chi(P)=3`, so
`chi(G)=4`.

The graph P is two-connected. After at most four deletions from G,
either both shores survive, in which case the join connects them, or
all of A was deleted and at most one vertex of P was deleted. The latter
graph is connected too. Deleting `{a,b,c,0,3}` leaves the two edges
`12,45`, so `kappa(G)=5`.

The seven connected, disjoint bags

```text
{a,3}, {b,4}, {c}, {0}, {1}, {2}, {5}
```

give a `K7^vee` minor. The first six bags form a clique; the last bag contacts
the first four and misses exactly `{1}` and `{2}`.

## Exclusion of every Q7 model

The following two elementary properties of P will be used.

1. P has no four-cycle: its three internally disjoint `0`--`2` paths
   have lengths `1,2,4`, so its cycles have lengths `3,5,6`.
2. For every edge e of P and every vertex s outside its ends,
   `e(P/e-s)<=4`. A triangle edge has one common neighbour, so its
   quotient has five edges; deleting s removes at least one, since that
   quotient is connected. Contracting any of the four other edges gives
   a five-cycle with a chord, with six edges and minimum degree two.

Any Q7 model in the connected graph G can be extended to a spanning
model: assign each unused component to one bag it contacts. The resulting
partition of nine vertices into seven bags has either two double bags
or one triple bag. In Q7 every vertex misses at most one other vertex,
and the total missing pairs are at most two and are independent.
Consequently three singleton A bags are impossible.

With **two double bags**, there are only two remaining possibilities.
Two mixed A--P bags leave four singleton P bags. Their required graph
contains a four-cycle, contradicting property 1. Alternatively there is
one mixed bag and one P-edge bag. The two remaining singleton A bags
already use one missing pair. The four P bags therefore need at least
five contacts; their contact graph is `P/e-s`, contradicting property 2.
Two P-edge bags leave all three A vertices singleton, and an A--A double
bag is disconnected.

With **one triple bag**, it must contain one or two A vertices. With
one, the two singleton A vertices again use one missing pair, forcing
at least five edges among the four singleton P bags. Every four-vertex
graph with at least five edges contains a four-cycle, contradicting
property 1. With two A vertices, five singleton P bags remain. Any five
vertices of Q7 span at least eight edges, whereas P has only seven.
A triple bag with no A vertex leaves all three A vertices singleton;
one consisting of A is disconnected. These cases exhaust arbitrary
connected branch sets, proving that G has no Q7 minor.

## Scope

The counterexample has connectivity and minimum degree five and chromatic
number four. It does not refute the retained seven-connected adjacent-hole
upgrade, the five-connected six-chromatic target, or the actual
seven-connected, minimum-degree-eight critical host. Conjecture 19,
HC7 and the stated completion criterion remain unresolved.
