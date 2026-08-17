# Independent cold audit: prescribed separator order barrier

**Audited source:**
[`hc7_degree_eight_prescribed_separator_order_barrier.md`](hc7_degree_eight_prescribed_separator_order_barrier.md)

**Source SHA-256:**
`2abfb09d7b288355a4a5de3ebab48e26fdff8f9d80083e1118d36ef5e26f8a79`

**Verdict:** **GREEN.**  This is an independent, computation-free cold
audit.  The connectivity, prescribed degree, exact minimum boundary order,
fullness and target-rich scope all check for every `n>=8`.

## 1. Connectivity and the nominated degree

Let `G_n=K_{8,n}` with parts `A,B`, where `|A|=8`, `|B|=n>=8`, and
`v in B`.  Removing at most seven vertices leaves a vertex in each part,
so the remaining complete bipartite graph is connected.  Removing all of
`A` leaves at least two isolated vertices in `B`.  Hence

```text
kappa(G_n)=8.
```

Every vertex of `B`, including the nominated vertex `v`, has neighbourhood
exactly `A` and therefore degree eight.

## 2. Exact value of the prescribed separator parameter

Let `R` be admissible in the definition of `lambda_G_n(v)`.  Since
`v in N(R)`, the set `R` contains a neighbour `a of v`, and every such
neighbour lies in `A`.  If `R` also contained `b in B`, then `a` would be
adjacent to every vertex of `B-R`, whilst `b` would be adjacent to every
vertex of `A-R`.  Thus every vertex outside `R` would lie in `N(R)`, making
the required far side empty.  This is forbidden.

It follows that `R subseteq A`.  The part `A` is independent, so the
requirements that `R` be nonempty and `G[R]` connected force `R={a}`.
Its external neighbourhood is exactly `B`, of order `n`.  Conversely,
every such singleton is admissible: its boundary `B` contains `v`, and
the far side `A-{a}` has seven vertices.  Therefore

```text
lambda_G_n(v)=n
```

exactly, not merely for the displayed choice of separator side.

## 3. Fullness and exact scope

Deleting the boundary `B` leaves the eight singleton components indexed by
`A`; each has neighbourhood exactly `B`.  Hence every component behind the
minimum prescribed boundary is full to all `n` boundary vertices.  Side
minimality and fullness therefore do not lower the unbounded value.

The source correctly excludes any target-free or critical-host conclusion.
For `n>=8`, choose distinct `a_1,...,a_7 in A` and
`b_1,...,b_7 in B`.  The seven two-vertex sets `{a_i,b_i}` are connected,
disjoint and pairwise adjacent, since for `i ne j` the cross-edge
`a_i b_j` exists.  They form a `K_7` minor and hence also a `K_7^-` minor.
Moreover `G_n` is bipartite.  Finally, `A` itself is an unprescribed
separator of order eight; the unbounded conclusion concerns only
separators whose boundary must contain the fixed vertex `v in B`.

Thus the example refutes a bound derived solely from connectivity,
`d(v)=8`, connected-side minimisation and fullness, while leaving open any
bound that genuinely uses target exclusion or colouring-criticality.
