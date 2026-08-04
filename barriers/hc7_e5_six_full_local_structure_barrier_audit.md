# Internal audit: six-full local-structure barrier

**Verdict:** **GREEN** for the pinned source revision.  This is a separate
internal mathematical audit, not external peer review.

**Audited source:**
`barriers/hc7_e5_six_full_local_structure_barrier.md`

**SHA-256:**
`3de230304dcbe9e9aafcc585200d4eab07db7e2fa0e0bf67c52d2852f41f0a90`

The source hash was independently recomputed and agrees with the value
above.  The construction satisfies every hypothesis of the stated
density-free intermediate claim, is exactly five-connected, and excludes
`K_7^-` by an exhaustive seven-branch-set argument.  No mathematical
correction is required at this revision.

Relative to the previously audited source revision
`53c68ef11f7498fc0a344f006b875067a81c0d7d20ac38b4abc38b0e48db1c2a`,
the source changes only its status text to link this adjacent audit.  Its
theorem statement, construction, proof, scope, and all mathematical
content are unchanged, so the GREEN verdict is retained.

## 1. Construction and labelled adjacencies

The path whose complement defines `B` is

```text
c-d-p-r_3-t-r_2-q-r_1.
```

Its seven consecutive pairs are exactly the nonedges of `B`.  Hence

```text
|V(B)|=8,                           |E(B)|=28-7=21.
```

The path-neighbour and complement-degree data are

```text
vertex    path neighbours    degree in B
c         d                  6
d         c,p                5
p         d,r_3              5
r_3       p,t                5
t         r_3,r_2            5
r_2       t,q                5
q         r_2,r_1            5
r_1       q                  6
```

For

```text
Delta={p,t,q},                       R={r_1,r_2,r_3},
L=Delta union R,
```

no two members of `Delta` and no two members of `R` are consecutive on
the path.  Both induced subgraphs are therefore triangles.

The vertices outside `L` are `c,d`, and `cd` is a path edge, hence a
nonedge of `B`.  Thus `B-L` has the two singleton components `{c},{d}`.
The endpoint `c` has no path neighbour in `L`, so it is adjacent in `B`
to all six vertices of `L`.  The two path neighbours of `d` are `c,p`,
so within `L` the vertex `d` misses exactly `p` and meets the other five
vertices.

Finally, taking complements of the two path incidences at each triangle
vertex gives

```text
N_B(p)-Delta={c,r_2,r_1},
N_B(t)-Delta={c,d,r_1},
N_B(q)-Delta={c,d,r_3}.
```

These sets have order three and are exact.  This checks all labelled
triangle degrees, the six-full singleton, and the singleton missing only
`p`.

## 2. Exact connectivity

Let `X` be a vertex set such that `B-X` is disconnected.  Choose a
nonempty proper union `U` of components of `B-X` and put

```text
W=V(B)-(X union U).
```

Every `U`--`W` pair is a nonedge of `B`, and hence an edge of the defining
path.  The path therefore contains the complete bipartite graph with
parts `U,W`.  Since a path has no `K_{2,2}`, one part has order one.  Its
single vertex has path degree at most two, so the other part has order at
most two.  It follows that every disconnected induced subgraph of `B`
has order at most three.

Deleting at most four vertices from the eight-vertex graph leaves at
least four vertices, and therefore cannot disconnect it.  Thus
`kappa(B)>=5`.

The vertex `d` has degree five.  The vertices outside its open
neighbourhood are `d` and its two nonneighbours `c,p`; the latter pair is
an edge of `B` because `cp` is not a path edge.  Consequently

```text
B-N_B(d) has components {d} and {c,p}.
```

The five-set `N_B(d)` is a cut, proving `kappa(B)<=5`.  Hence

```text
kappa(B)=5.
```

## 3. Exhaustion of seven branch sets

A `K_7^-` model has seven nonempty, pairwise disjoint connected branch
sets.  In an eight-vertex host their union has order seven or eight; these
are the only possibilities.

If the union has order seven, all branch sets are singletons.  The unused
vertex has path degree at most two, so at least `7-2=5` edges of the path
remain among the seven used vertices.  They are five distinct missing
adjacencies between singleton branch sets.  A `K_7^-` model permits at
most one such missing branch-set adjacency.

If the union has order eight, exactly one branch set has order two and
the other six are singletons.  Write the two-vertex set as `{x,y}`.  Its
connectivity forces `xy` to be an edge of `B`, so `xy` is not a path
edge.  Removing `x,y` from the path leaves exactly

\[
                   7-d_P(x)-d_P(y)\ge3
\]

path edges among the six remaining vertices.  These are three distinct
nonadjacencies between singleton branch sets.  Contracting or retaining
the connected set `{x,y}` cannot create an edge between either endpoint
pair of those singleton sets.  Again at least three branch-set pairs are
nonadjacent, whereas `K_7^-` permits only one.

The two union orders exhaust every seven-bag model.  Thus

```text
K_7^- is not a minor of B.
```

## 4. Density-limited scope

At order eight, the `E5` threshold is

```text
4*8-7=25,
```

whereas `B` has only twenty-one edges.  It is also only five-connected,
not seven-connected.  Therefore it is not a counterexample to `(E5)`, to
the seven-connected `4n-2` target, or to any statement which genuinely
uses the minimum-`E5` density accounting or internal density of a
six-full component.

What it refutes is exactly the displayed density-free local implication:
five-connectivity, two boundary triangles, exact three-neighbour capacity
at each triangle vertex, a component complete to all six boundary
vertices, and a second component missing only one triangle vertex do not
alone force `K_7^-`.

There are no unresolved assumptions in this finite construction.  The
barrier must not be cited beyond this density-free scope.
