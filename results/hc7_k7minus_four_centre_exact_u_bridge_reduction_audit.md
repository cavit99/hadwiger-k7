# Internal audit: exact boundary traces and bounded shore reduction

**Verdict:** **GREEN**.

**Audited source:**
[`hc7_k7minus_four_centre_exact_u_bridge_reduction.md`](hc7_k7minus_four_centre_exact_u_bridge_reduction.md)

**Audited source SHA-256:**

```text
eca904897e1d32126be1399034966d3304d724ae746fcb83a7b1c56e1b561b0a
```

This pin includes the final terminology edit which states the
response-reflection hypothesis directly instead of using project-specific
shorthand.  A separate final audit confirmed that no hypothesis, conclusion,
notation or proof step changed.

This is a separate internal mathematical audit, not external peer review.
Every partition case, connected-subgraph construction, attachment
inequality and component count was reconstructed from the cited inputs.  No
unresolved assumption or gap was found within the stated scope.

## Exact boundary partitions and Kempe paths

The wheel-leaf theorem gives an edge in `G[T]`, while the web-cut theorem
excludes a triangle and gives the required `K_5`-minor exclusion in `G[S]`.
Thus `G[T]` is a three-vertex path or an edge plus an isolated vertex.
Every exact-`U` equality partition is therefore either all-distinct on `T`
or pairs one nonadjacent pair of `T`.

The exact-block anchor theorem applies because `C,D` are connected and full
to `S`, `U` is independent, and `G[S]` has no `K_5` minor.  The shore
languages are nonempty.  They cannot contain the same literal equality
partition: a palette permutation would make the two shore colourings agree
on `S`, and the colourings would glue.

If the selected shore rejects the all-distinct partition, its anchor has a
paired block `{p,p'}`.  Exactly three palette colours are absent from the
boundary.  For any such colour, separating `p,p'` in the corresponding
two-colour graph permits a Kempe interchange producing the rejected
all-distinct partition.  Hence a bichromatic `p`--`p'` path exists.  No
other boundary vertex has either path colour, so the path interior lies in
`C`; paths with different secondary colours meet only at vertices of their
common colour.

If the selected shore accepts the all-distinct partition, the opposite
shore accepts a paired partition which the selected shore rejects.  The
audited singleton-block exchange then forces the stated path.  In the edge
plus isolated-vertex case, the proof correctly enlarges the path interior
to reach the other endpoint of the boundary edge.  This extra step is
necessary and preserves connectedness.

## Response-reflection obstruction and attachment bounds

In each of the three cases, `Y` is nonempty and connected, the vertices of
`Q` form a clique of singleton boundary blocks, and `Y` supports the one
remaining non-`U` block.  For a component `K` of `C-Y`, connectedness of
`C` supplies an edge from `K` to `Y`.

Distinct components of `C-Y` are anticomplete, and `C,D` are anticomplete.
Consequently

```text
N_G(K)=A_K dotunion B_K.
```

The set `D` lies outside `K union N_G(K)`.  Seven-connectivity therefore
gives

```text
a_K >= d_K+e_K.
```

If `K` saw `U union Q`, then `K` would support the `U` block and `Y` would
support the other nonsingleton or non-clique block.  The `K-Y` edge and the
defined contacts with `Q` give all required adjacencies.  These are exactly
the connected open-side subgraphs required by exact response reflection for
the same partition accepted on the `C`-shore.  Exact response reflection
would six-colour `G`.  Thus the exclusion
`U union Q not subseteq B_K` is correctly oriented and uses no colouring
from the opposite shore.

When `d_K=0`, that exclusion leaves a vertex of `T-B_K`.  In the audited
four-connected graph

```text
F=H[C union T]+binom(T,2),
```

the set `A_K union (B_K cap T)` separates `K` from the missing boundary
vertex.  Its order is `a_K+3-e_K`, so four-connectivity gives
`a_K>=e_K+1`.  No trace transfer or virtual-edge lift is used.

## Bounded centre-bearing remainder

For `u in U`, choose a neighbour of `u` in `D`.  It is anticomplete to
`N_C(u)`.  Since `alpha(G[N(u)])=3`, an independent triple in `N_C(u)`
would form an independent four-set with that `D`-neighbour.  Hence

```text
alpha(G[N_C(u)]) <= 2.
```

Neighbours of `u` chosen from distinct components of `C-Y` are independent,
so each centre meets at most two components.  There are at most eight
centre-component incidences.  Absorbing all centre-free components into
`Y` preserves connectedness and the boundary contacts; old components are
pairwise anticomplete, so no surviving components merge.  This proves the
eight-component bound and the bound of two components adjacent to all four
centres.

If `a_K=1`, the attachment inequality and response-reflection exclusion give
`d_K+e_K=1`.  The strengthened all-centre inequality rules out
`(d_K,e_K)=(0,1)`, leaving `(1,0)`.  Thus `B_K=S-{u}` for one centre `u`.
Each such component meets three centres, so the incidence bound permits at
most two.  The final path-colour contact bound also follows: each colour
class is independent, and therefore contributes at most two neighbours of
any centre inside `C`.

The result does not construct the prescribed rooted `K_6^-` model, bound
the orders of the remaining components, or prove the `K_7^-` six-colour
conjecture.

## Pinned dependencies

```text
four-centre rooted-web cut and exact static residue
e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3

generalized-wheel leaf descent
c04236752495ec7ff6e57b54cc498423be1b621c5ba3547739cec72b045db176

exact-block anchors across two full shores
b9b1c08af789a08c3259f899cd821058d78bfd023e161ee5597a6eabaf127feb

exact singleton-block Kempe exchange
d0157bc10b6f588a7e7fd714b1e5be02faee3da35f2d35ce43cf03f5237c91e2

exact response reflection
94c154ce0d8d9bebaaff2ff97df66beb3e2381bb242378df38d9620ed8ec36e0

four-connectivity of the completed minimum side
ae424dc24a95ab8afe9b6ea93dd850b727dcd4bf8f00ee72a8fd11eaf312e846

degree-eight neighbourhood structure
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd
```
