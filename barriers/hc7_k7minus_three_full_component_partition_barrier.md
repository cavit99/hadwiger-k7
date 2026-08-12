# Three full components do not force the adjacent-pair partition

**Status:** barrier/counterexample to the boundary-allocation claim stated
below;
[separate internal audit GREEN](hc7_k7minus_three_full_component_partition_barrier_audit.md).
This graph is not a counterexample to the `K_7^-` six-colour conjecture
or to `HC_7`.

## 1. Construction

Let

\[
                         T=2K_3\mathbin{\dot\cup}2K_1              \tag{1.1}
\]

and let `A={a_1,a_2,a_3}` be an independent set.  Form

\[
                              Q=\overline K_3\vee T.                \tag{1.2}
\]

Thus the three singleton sets `{a_i}` are pairwise anticomplete connected
components of `Q-T`, each full to the literal eight-vertex boundary `T`.

### Proposition 1.1

The graph has the following properties.

1. `T` is nonsplit, three-colourable and `K_5`-minor-free.
2. `Q` has no `K_7^-` minor.
3. For every edge `uv` of `T`, the graph `T-{u,v}` is not bipartite.

Consequently the following proposed allocation lemma is false:

> Three anticomplete connected boundary-full components, a nonsplit
> `K_5`-minor-free boundary, and exclusion of `K_7^-` force a boundary edge
> `uv` whose deletion leaves a bipartite graph.

Such an edge would let two of the full components carry the two bipartition
classes while `u,v` remain as adjacent singleton colour classes.  The
construction shows that this natural four-block synchronization need not
exist.

#### Proof

The two triangles give chromatic number three.  They also contain an
induced `2K_2`, so `T` is nonsplit.  A connected minor model lies in one
component of a disconnected graph; no component of `T` has five vertices,
so `T` has no `K_5` minor.

Consider any putative `K_7^-` model in `Q`.  At most three branch sets can
contain a vertex of `A`, so at least four branch sets avoid `A`.  Every
connected branch set avoiding `A` lies wholly in one component of `T`.
If `p` such branch sets lie in one component and `q` in another, all `pq`
pairs are nonadjacent.  A `K_7^-` model permits at most one nonadjacent
pair.  Hence branch sets avoiding `A` can either all lie in one component,
or consist of exactly one branch set in each of two components.  The first
case has at most three such branch sets, and the second has exactly two.
Both contradict the required lower bound four.  This proves item 2.

Finally every edge `uv` lies in one of the two triangles.  Deleting its
ends leaves the other triangle intact, so `T-{u,v}` is not bipartite.
`\square`

## 2. Scope

The graph `Q` is four-colourable and is not seven-connected: either
isolated boundary vertex has neighbourhood exactly `A`.  It is not asserted
to be minor-minimal non-six-colourable and carries none of the six forest
coordinates or their singleton-signature colourings.  It therefore does
not refute a theorem using criticality, the two seven-connected edge
restorations, or the exact coordinate responses.  It isolates the first
invalid inference after the full-component reduction: contact geometry and
ordinary boundary colouring alone do not close the three-component case.
