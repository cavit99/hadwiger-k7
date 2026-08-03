# Exact connectivity of a minimal `4n-7` enemy

**Status:** written unbounded reduction; the degree-seven input is
computer-assisted; separate internal audit.

Consider the following open extremal statement.

> **(E5)** Every five-connected graph `G` with
> `|E(G)|>=4|V(G)|-7` contains a `K_7^-` minor.

An **E5 enemy** is a graph satisfying the connectivity and density
hypotheses of (E5) but containing no `K_7^-` minor.

## Theorem 1 (exact-connectivity reduction)

If an E5 enemy exists, then an enemy chosen first with minimum order and,
subject to that, with the minimum number of edges has connectivity exactly
five.

### Proof

Let `G` be such a lexicographically minimum enemy, and write
`n=|V(G)|`, `m=|E(G)|`.

First, `n>=9`.  Five-connectivity requires `n>=6`.  For `n=6` the density
bound asks for at least 17 edges, more than a simple graph can have.  For
`n=7` it asks for all 21 edges, giving `K_7`.  If `n=8`, the complement has
at most three edges.  With at most two complement edges, delete an endpoint
of one of them (or any vertex if there is none), leaving at most one
non-edge.  With three complement edges that are not a matching, delete a
vertex incident with at least two of them, again leaving at most one
non-edge.  In either case the remaining seven vertices induce `K_7^-` or
`K_7`.  If the three complement edges form a matching, contract an edge
joining ends of two different matching edges; the resulting seven vertices
induce a `K_7^-`.  Thus no enemy has order at most eight.

Suppose for a contradiction that `G` is six-connected.

Deleting one edge from a six-connected graph leaves a five-connected graph.
If `m>4n-7`, then `G-e` is an E5 enemy for every edge `e`, contrary to the
choice of `G`.  Hence

```text
m=4n-7.                                                   (1)
```

Contracting one edge of a six-connected graph leaves a five-connected
graph.  For `xy in E(G)`, put

```text
c(xy)=|N_G(x) intersect N_G(y)|.
```

After contracting `xy` and suppressing parallel edges, the resulting graph
has `n-1` vertices and

```text
m-1-c(xy)
```

edges.  If `c(xy)<=3`, then by (1)

```text
m-1-c(xy) >= 4n-11 = 4(n-1)-7.
```

Thus `G/xy` would be a smaller E5 enemy, again a contradiction.  Therefore

```text
c(xy)>=4 for every edge xy of G.                          (2)
```

Equation (1) gives average degree

```text
2m/n = 8-14/n < 8.
```

Six-connectivity and this strict inequality imply that the minimum degree
of `G` is six or seven.

If `G` has a degree-six vertex, (2) and the
[degree-six common-neighbour bound](hc7_k7minus_degree6_common_neighbour_bound.md)
give

```text
m<=4n-9,
```

contrary to (1).  If its minimum degree is seven, the
[saturated degree-seven exclusion](hc7_k7minus_degree7_common_neighbour_exclusion.md)
contradicts the existence of that vertex.  Both possibilities are
impossible.  Hence `G` is not six-connected.

As every E5 enemy is five-connected by definition, `kappa(G)=5`.  \(\square\)

## Connectivity facts used

For completeness, both minor operations used above lose at most one unit of
vertex connectivity.

- If a set of at most four vertices separated `G-e`, restoring the single
  edge `e` could join at most the components containing its ends.  Removing
  one end as well would give a cut of at most five vertices in `G` (the
  possible singleton-side exception contradicts minimum degree six).
- If a set of at most four vertices separated `G/e`, lift it to `G`; when it
  contains the contracted vertex, replace that vertex by both ends of `e`.
  This gives a cut of at most five vertices in `G`.

Thus six-connectivity of `G` implies five-connectivity of both `G-e` and
`G/e`.

## Scope

The theorem does not prove (E5).  It reduces (E5) to enemies having an
actual five-vertex cut.  In particular, any continuation must use the
structure and density accounting across such a cut rather than assuming a
six-connected minimal counterexample.
