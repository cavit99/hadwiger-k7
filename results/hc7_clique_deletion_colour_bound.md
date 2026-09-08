# Deleting a four-clique leaves chromatic number at least five

**Status:** written proof; a separate internal audit is recorded beside it.
No global six-colouring or case-completion conclusion is asserted.
All graphs are finite and simple. Write `Q` for `K_7` with two independent
edges deleted.

**Theorem.** Let `G` be six-connected, `delta(G)>=8`,
`Q`-minor-free, and `chi(G)>=7`. For every four-vertex clique `R`,

`chi(G-R)>=5`.

In particular this holds in the current critical host, where every proper
minor is six-colourable. That additional criticality is not needed here.

## The four-list recolouring lemma

**Lemma.** Let `F` be bipartite with specified shores `I,J`. Give every
vertex `w` a list `L(w) subseteq {1,2,3,4}` of size at least two.
Suppose that for every edge `wz`, whenever `|L(w)|=2`,

`L(w) subseteq L(z)`.

Then `F` has a proper colouring from these lists.

**Proof.** Put `P={1,2}` and `Q'={3,4}`. Call a vertex of `I` bad if
its list is `Q'`, and a vertex of `J` bad if its list is `P`.
The hypothesis excludes an edge between two bad vertices.

Give every bad vertex of `I` colour `3`, and all its neighbours colour `4`.
Give every bad vertex of `J` colour `1`, and all its neighbours colour `2`.
Each forced colour belongs to the corresponding list by the inclusion
hypothesis. The two neighbourhoods lie in different shores, and no bad
vertex receives a conflicting forced colour.

Give each remaining vertex of `I` any available colour in `P`, and each
remaining vertex of `J` any available colour in `Q'`. These choices exist:
a list of size at least two missing `P` or `Q'` was exactly a bad list.
An edge incident with a bad vertex has colours `3,4` or `1,2`.
Every other edge has its `I` colour in `P` and its `J` colour in `Q'`.
Thus every edge is properly coloured. QED

## Application to the actual host

We use [contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md),
source SHA-256
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.
Its [separate internal audit](../active/hc7_companion_contraction_closure_audit.md)
is pinned to that source. This input says that every vertex outside `R`
has at most two neighbours in `R`; if `wz` is an edge outside `R` and
`w` has two neighbours in `R`, then `N_G(z) intersect R` is contained in
`N_G(w) intersect R`. No new external theorem is invoked.

**Proof of the theorem.** Suppose `H=G-R` has a proper four-colouring,
allowing empty colour classes. Choose two classes as shores `I,J`.
Colour the four vertices of `R` with `1,2,3,4`, and give the other two
classes of `H` the fresh colours `5,6`.

For `w in I union J`, let `L(w)` be the colours on its nonneighbours
in `R`. The input gives `|L(w)|>=2`. If `|L(w)|=2` and `wz` is an edge
of `H[I union J]`, the same input gives `L(w) subseteq L(z)`.
The lemma therefore recolours `I union J` using the four clique colours.
The lists prevent conflicts with `R`; the fresh colours prevent conflicts
with the other two classes. This is a proper six-colouring of `G`,
contrary to `chi(G)>=7`. QED

The argument uses two classes of one fixed colouring. It does not assert
that three classes can be recoloured with the four clique colours, or
that a minor model in `G-R` preserves any prescribed clique contacts.
