# Six-full local structure does not force `K_7^-` without density

**Status:** barrier/counterexample to an intermediate density-free local-host
claim; computation-free written proof with a
[separate internal audit](hc7_e5_six_full_local_structure_barrier_audit.md).
This is not a counterexample to `(E5)` or to the primary seven-connected
theorem.

## Refuted intermediate claim

The following local implication is false.

> Let `Delta={p,t,q}` and `R={r_1,r_2,r_3}` be disjoint triangles in a
> five-connected graph, and put `L=Delta union R`.  Suppose that `G-L` has
> two singleton components, one complete to `L` and the other adjacent to
> every member of `L` except `p`.  Suppose also that every vertex of
> `Delta` has exactly three neighbours outside `Delta`.  Then `G` contains
> a `K_7^-` minor.

The counterexample below satisfies every displayed condition.  It has no
corresponding density hypothesis.

## Construction

Let `P` be the eight-vertex path in the displayed order

```text
c-d-p-r_3-t-r_2-q-r_1
```

and let

```text
B=complement(P).
```

Thus the seven consecutive pairs in the display are precisely the
nonedges of `B`; every other pair is an edge.

## Theorem

The graph `B` has order eight and size twenty-one, is exactly
five-connected, and has no `K_7^-` minor.  Moreover, with

```text
Delta={p,t,q},                 R={r_1,r_2,r_3},
L=Delta union R,
```

both `B[Delta]` and `B[R]` are triangles, the components of `B-L` are
`{c}` and `{d}`, the vertex `c` is complete to `L`, and `d` is adjacent
to exactly `L-{p}` in `L`.  Each vertex of `Delta` has exactly three
neighbours outside `Delta`.

### Proof

The path `P` has seven edges, so complementation gives

```text
|V(B)|=8,                         |E(B)|=binom(8,2)-7=21.
```

We first check connectivity.  Suppose that deleting a set `X` leaves
`B-X` disconnected.  Take a nonempty union `U` of components and put
`W=V(B)-(X union U)`.  Every pair with one end in `U` and the other in
`W` is a nonedge of `B`, and hence is an edge of the path `P`.  Thus `P`
contains the complete bipartite graph with parts `U,W`.  A path contains
no `K_{2,2}`, so one of `U,W` is a singleton.  A vertex of a path has
degree at most two, so the other part then has order at most two.
Consequently `B-X` has at most three vertices.  If `|X|<=4`, however,
at least four vertices survive.  Therefore no set of at most four
vertices disconnects `B`.

The vertex `d` has degree five in `B`: its only nonneighbours are its two
path neighbours `c,p`.  Deleting `N_B(d)` leaves the isolated vertex `d`
and the adjacent pair `c,p`.  Hence `N_B(d)` is a five-cut, and

```text
kappa(B)=5.
```

We next exclude a `K_7^-` minor.  Seven nonempty, pairwise disjoint branch
sets in an eight-vertex graph use either seven or eight vertices.

If they use seven vertices, every branch set is a singleton.  Deleting
one vertex from `P` leaves at least five path edges, so the corresponding
seven vertices of `B` have at least five missing pairs.  They cannot
contain the twenty-edge graph `K_7^-` as a subgraph.

If all eight vertices are used, exactly one branch set has order two and
the other six are singletons.  Write the two-vertex branch set as
`{x,y}`.  It is connected, so `xy` is an edge of `B` and therefore not an
edge of `P`.  Among the other six vertices, the number of path edges is

```text
7-d_P(x)-d_P(y)>=3,
```

because every path degree is at most two and `xy` is not a path edge.
These path edges are at least three distinct nonadjacencies between
singleton branch sets.  Contracting `{x,y}` cannot create an edge between
two such singleton sets.  A `K_7^-` model permits only one missing pair,
so this case is also impossible.  Thus `K_7^-` is not a minor of `B`.

It remains to verify the labelled local structure.  No pair within
`Delta` or within `R` is consecutive on `P`, so both sets induce
triangles.  Deleting their union leaves `c,d`, which are consecutive on
`P` and therefore nonadjacent in `B`; hence they are two singleton
components.  The only path neighbour of `c` in the remaining graph is
`d`, so `c` is complete to `L`.  The path neighbours of `d` are `c,p`,
so its only missed vertex of `L` is `p`.

Finally, direct inspection gives the exact exterior neighbourhoods

```text
N_B(p)-Delta={c,r_2,r_1},
N_B(t)-Delta={c,d,r_1},
N_B(q)-Delta={c,d,r_3}.
```

Each triangle vertex therefore has exactly three exterior neighbours,
as claimed.  \(\square\)

## Exact scope

The graph has

```text
|E(B)|=21<25=4|V(B)|-7.
```

It consequently does not refute `(E5)`, does not arise as a verified
minimum `E5` enemy, and says nothing against the primary seven-connected
`4n-2` target.  It refutes only the density-free implication that the
displayed five-connected local host structure -- including a six-full
component, a second component missing just one triangle vertex, both
boundary triangles, and the exact three-neighbour capacities -- already
forces a `K_7^-` minor.  Any successful use of this local pattern must
also exploit the density or internal structure of the complementary
components.
