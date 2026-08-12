# Separate internal audit: anchored coordinate-compression barrier

**Verdict:** **GREEN.**  The family `G_m=K_4 join (K_{m,m}+uv)` has all the
claimed chromatic, connectivity, minimum-degree and fixed-response
properties.  Its singleton side refutes exactly the displayed local rooted
compression assertion.  The construction contains a literal `K_7`, so its
scope is correctly restricted and it is not a counterexample to the
`K_7^-` six-colour conjecture or to a target-free compression theorem.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The mathematical source audited was
[`hc7_k7minus_anchored_coordinate_compression_barrier.md`](hc7_k7minus_anchored_coordinate_compression_barrier.md),
with SHA-256

```text
eb4c35854827a504c06ecb54656d3059ca691c6224c14df616d89d06e5c68238
```

After this audit, its status line was updated to link this audit and trailing
whitespace in one quoted blank line was removed.  The current source SHA-256
is

```text
2e09b181eb0afc95cee6c68ef7ebfb7ede99c39f0337f0f77675d6599a4c2a17
```

No mathematical statement or construction changed.

The construction and its verification are computation-free.

## 1. Chromatic number and edge-deletion response

The graph `Q_m=K_{m,m}+uv` is three-chromatic.  The edge `uv` together
with any vertex of the opposite bipartition class forms a triangle, while
the displayed three-class colouring supplies the matching upper bound.
Chromatic numbers add under a join, so

\[
                         \chi(G_m)=4+3=7.
\]

Deleting `uv` makes `Q_m` bipartite.  Colouring its two parts with two
colours and the joined `K_4` with four further colours gives a proper
six-colouring of `G_m-uv`.  On restoring `uv`, its two ends have the same
colour and every other edge remains proper, so `uv` is the unique
monochromatic edge.

## 2. Connectivity and minimum degree

Deleting fewer than `m+4` vertices leaves either a vertex of the joined
`K_4`, which is adjacent to every other survivor, or deletes all four of
those vertices and fewer than `m` vertices of `Q_m`.  In the latter case
both bipartition classes survive and the remaining complete bipartite
edges keep the graph connected.  Conversely, deleting the four clique
vertices and all `m` vertices of `B` leaves the vertices of `A`, among
which only `uv` is an edge; for `m>=4` this graph is disconnected.  Hence
`kappa(G_m)=m+4`.

Every ordinary vertex of either bipartition class has degree `m+4`; the
ends `u,v` and the clique vertices have larger degree.  Thus
`delta(G_m)=m+4`, as claimed.

## 3. The singleton response side

For `Y={u}`,

\[
 N_{G_m}(u)=V(K_4)\mathbin{\dot\cup}B
                         \mathbin{\dot\cup}\{v\},
 \qquad |N_{G_m}(u)|=m+5.
\]

After deleting this neighbourhood, `u` and the `m-2` vertices of
`A-{u,v}` remain as distinct components.  The neighbourhood is therefore
an actual separator.

In the fixed six-colouring, its equality partition has six colour blocks:
four singleton blocks on the `K_4`, one block on `B`, and the block
containing `v` (and externally the deleted vertex `u`).  Since `u` is
adjacent to every boundary vertex, no proper six-colouring of the closed
singleton side can induce that same six-block partition.  Equivalently,
the exterior trace is rejected.  The side nevertheless has no nonempty
proper subset containing `u`, while its boundary order `m+5` is unbounded.
This refutes the assertion in Section 1 without relying merely on a failed
proof method.

## 4. Scope

The four joined clique vertices, `u`, `v`, and any vertex of `B` induce a
literal `K_7`.  The family therefore contains a `K_7^-` minor and is not a
hypothetical target-free critical host.  It does not obstruct a theorem
which spends target exclusion, nor does it refute `HC_7`.  It establishes
only that a fixed edge-deletion trace, arbitrarily high connectivity and
arbitrarily high minimum degree do not by themselves force a proper rooted
subset with smaller boundary.

There are no unresolved assumptions in the stated barrier.
