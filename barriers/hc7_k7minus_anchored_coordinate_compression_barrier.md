# A coordinate response need not admit rooted boundary compression

**Status:** explicit infinite barrier;
[separate internal audit GREEN](hc7_k7minus_anchored_coordinate_compression_barrier_audit.md).
This is not a counterexample to the `K_7^-` six-colour conjecture or to a
target-free anchored-compression theorem.

## 1. Assertion refuted

The following local implication is false, even with connectivity and
minimum degree stronger than those available in the critical host.

> Let `G` be seven-chromatic and at least seven-connected, with minimum
> degree at least eight.  Suppose `e=uv` is an edge and `G-e` has a proper
> six-colouring in which `e` is the unique monochromatic edge after it is
> restored.  If a connected actual response side `Y` contains `u`, then
> there is a nonempty proper connected set `Y' subsetneq Y` containing
> `u`, carrying the same edge-deletion colouring and rejected trace, and
> satisfying
>
> \[
>                     7\le |N_G(Y')|<|N_G(Y)|.
> \]

The construction shows more narrowly that a response side may already be
a singleton with arbitrarily large boundary.  It therefore has no
nonempty proper rooted subset at all.

## 2. Construction

Fix an integer `m>=4`.  Let `A,B` be disjoint sets of order `m`, choose
distinct vertices `u,v in A`, and let

\[
              Q_m=K_{m,m}+uv,
              \qquad G_m=K_4\vee Q_m.                \tag{2.1}
\]

Thus every vertex of the displayed `K_4` is adjacent to every vertex of
`Q_m`, every `A`--`B` edge is present, and `uv` is the only edge inside
either bipartition class.

## 3. Chromatic and connectivity properties

The graph `Q_m` is three-chromatic: the edge `uv` and any vertex of `B`
form a triangle, while colouring `A-{v}`, `{v}`, and `B` with three
colours is proper.  Hence

\[
                         \chi(G_m)=4+3=7.             \tag{3.1}
\]

After deleting `uv`, the graph `Q_m-uv=K_{m,m}` is bipartite.  Give the
two bipartition classes two colours and the four vertices of the joined
`K_4` four further colours.  This is a proper six-colouring of
`G_m-uv`.  Restoring `uv` makes it the unique monochromatic edge.

We also have

\[
                         \kappa(G_m)=m+4,
                  \qquad \delta(G_m)=m+4.             \tag{3.2}
\]

For the connectivity equality, deleting fewer than `m+4` vertices leaves
either a vertex of the `K_4`, which joins all remaining vertices, or all
four clique vertices have been deleted and fewer than `m` further vertices
have been removed from `Q_m`.  In the latter case both `A` and `B` retain
a vertex and the surviving complete bipartite graph is connected.  On the
other hand, deleting the four clique vertices together with all of `B`
disconnects the surviving vertices of `A`.  This proves the first equality
in (3.2).  A vertex in `A-{u,v}` or in `B` has degree `m+4`, while all
other vertices have at least that degree, proving the second.

## 4. The uncompressible rooted response

Put

\[
                              Y=\{u\}.                \tag{4.1}
\]

Its open neighbourhood is

\[
                N_{G_m}(u)=V(K_4)\mathbin{\dot\cup}B
                                  \mathbin{\dot\cup}\{v\},
       \qquad |N_{G_m}(u)|=m+5.                       \tag{4.2}
\]

This is an actual separator.  After it is deleted, the vertex `u` and the
`m-2` vertices of `A-{u,v}` are distinct isolated components.

In the six-colouring from Section 3, the boundary (4.2) uses all six
colours: the four clique vertices use four singleton colours, `B` uses its
bipartition colour, and `v` has the colour of `u`.  The restriction to
`G_m-u` is proper.  No colouring of the intact singleton side can induce
the same boundary equality partition, because all six colours already
occur on neighbours of `u`.  Thus `Y` carries the rejected trace from the
literal edge-deletion response at `uv`.

But `Y={u}` has no nonempty proper subset.  Its boundary has order `m+5`,
which is unbounded as `m` grows.  Consequently neither the fixed response,
nor connectivity, nor minimum degree can force the proposed rooted
boundary reduction.

## 5. Exact scope

The graph `G_m` contains a literal `K_7`: take the four vertices of the
joined `K_4` together with `u,v` and any vertex of `B`.  Accordingly this
family does **not** refute a theorem whose alternatives include a
`K_7^-` minor, and it is not a hypothetical critical host.

The barrier identifies the first hypothesis that a positive proof must
spend.  At a shore-filling or singleton coordinate response, the colouring
trace and high connectivity alone give no compression.  A target-free
anchored-compression theorem must use `K_7^-`-minor exclusion at that exact
point, or permit replacement of the original coordinate operation.
