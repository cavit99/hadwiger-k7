# Audit: exact connectivity of a minimal E5 enemy

**Verdict:** GREEN, conditional only on the two pinned local inputs.

**Audited source:**
`active/hc7_k7minus_e5_exact_connectivity_reduction.md`

**SHA-256:**
`89149f004a35ff639ad061bb6fb9fe5899cb057bd159e0f05222fc7b3b377ac6`

## Pinned dependencies

1. `active/hc7_k7minus_degree6_common_neighbour_bound.md`, SHA-256
   `e157c0e8fa5805cee15888abb9a002d35d51d7e877154e7eee1a37627732493e`.

2. `active/hc7_k7minus_degree7_common_neighbour_exclusion.md`, SHA-256
   `663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0`.

3. Its finite verifier
   `active/hc7_k7minus_degree7_quotient_verify.py`, SHA-256
   `ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445`.

The degree-six input has a written proof.  The degree-seven input has a
written unbounded reduction and an exact finite quotient verification.

## Minimality and small orders

The choice is lexicographic in `(|V(G)|,|E(G)|)`.  Therefore an edge
deletion that remains an enemy contradicts the second coordinate, while a
contraction that remains an enemy contradicts the first.  No stronger claim
that every proper minor preserves connectivity or density is made.

The order check is complete:

- order six cannot meet `4n-7`;
- order seven at the threshold is `K_7`;
- on eight vertices the complement has at most three edges.  Deletion
  handles at most two edges and every nonmatching three-edge graph.  For a
  three-edge matching, contracting an edge whose ends belong to different
  matching pairs absorbs the two incident missing adjacencies and leaves
  exactly the third one.

Thus both local inputs legitimately receive `n>=9`.

## Connectivity under the two operations

The two connectivity transfers are valid.

- If `G-e` had a cut `S` of order at most four, the restored edge could only
  join the components containing its ends.  Removing one endpoint in
  addition to `S` gives a cut of `G` of order at most five.  If that endpoint
  were the whole component, it would have degree at most five, impossible
  in a six-connected graph.
- A cut of order at most four in `G/e` either lifts unchanged or, when it
  contains the contracted vertex, lifts after replacing that vertex by the
  two ends of `e`.  Its lifted order is at most five.

Hence `G-e` and `G/e` are five-connected whenever `G` is six-connected.

## Density and common-neighbour accounting

If `m>=4n-6`, every edge deletion remains above the E5 threshold, so
edge-minimality forces `m=4n-7`.

For `xy in E(G)`, simple contraction removes the edge `xy` and one duplicate
edge for every common neighbour.  Thus

```text
|E(G/xy)|=m-1-|N(x) intersect N(y)|.
```

At `m=4n-7`, a common-neighbour count at most three leaves at least
`4(n-1)-7` edges.  Contraction minimality therefore forces at least four
common neighbours on every edge.

Finally, `2m/n=8-14/n<8`.  Six-connectivity gives minimum degree at least
six, so a minimum-degree vertex has degree six or seven.  The degree-six
bound contradicts `m=4n-7`, and the degree-seven theorem excludes the other
case.

## Scope

The conclusion is only:

> a lexicographically minimal E5 enemy, if one exists, has vertex
> connectivity exactly five.

The source does not claim that (E5), the `4n-2` seven-connected theorem,
Norin--Totschnig Conjecture 21, or `HC_7` is proved.  The remaining case is
an actual order-five separation in the minimal enemy.
