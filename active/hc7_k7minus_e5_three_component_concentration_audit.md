# Internal audit: three-component concentration

**Verdict:** GREEN for the pinned source revision.  This is an internal
mathematical audit, not external peer review.

**Audited source:**
`active/hc7_k7minus_e5_three_component_concentration.md`

**SHA-256:**
`40391662ea90f75e36732776b67c9cac22c6ecaee1e056e0498b45d034620580`

## Rooted-obstruction count

The class `A`--`F` counts were checked directly against
Fabila-Monroy--Wood Theorem 15.  After added facial cliques are excluded by
five-connectivity, the possible nominated--nominated edges and remaining
edge counts are exactly those displayed in (3).  Comparing with

```text
|E(G[L union (S-{t})])|
  >=3|L|+delta(L)+|E(J-t)|
```

gives the three bounds in Lemma 1.  No finite enumeration is used.

## Terminal composition and concentration

The proof uses only the already audited composition with three distinct
lobes: a rooted `K_4` avoiding `t`, a rooted `K^*_{4,2}` with `t` in a
helper, and the remaining full lobe.  When `delta_1=4`, that six-bag model
exists at each nonisolated `t`; the three numerical cases `k>=3`, `k=2`,
and `k=1` then contradict the exact excess sum.  When `delta_1>=5`, it
exists for every `t`, and the same obstruction count gives (6).

For a triangle-free graph on five vertices with at least two edges, a
vertex incident with at most `k-2` edges exists, so some `t` has
`|E(J-t)|>=2`.  This elementary selection was checked in the only tight
case `k=2`, where an isolated vertex works.

## Contraction and scope

Contracting a low lobe of excess at most one changes the excess above
`4n-7` by `1-delta(B)`.  If the lobe is nontrivial, the contraction is a
proper minor and therefore cannot remain five-connected.  Every small cut
contains the contracted vertex; deleting it leaves the asserted set of at
most three vertices.  This is a separator conclusion, not a strict
high-excess descent.

If both low lobes are singletons, their excesses are one and the high
closed shore has exactly `4|H|-9` edges.  The source correctly does not
turn the resulting ordinary `K_6` minor into a five-rooted model.

The Xie discussion is a recorded negative finding, not a counterexample to
Xie's theorem.  The theorem's connected subgraphs contain the boundary
terminals and need not remain connected after those terminals are removed.
Thus it does not prove the two disjoint interior carriers required by the
virtual-edge lift.  Failure of the completed linkage likewise has no proved
excess-preserving lift.  The source stops at the first unsupported inference.
