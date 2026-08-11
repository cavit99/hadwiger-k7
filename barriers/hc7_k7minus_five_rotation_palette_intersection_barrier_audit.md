# Internal audit: five-row palette-intersection barrier

**Verdict:** GREEN.  This is a separate internal audit, not external peer
review.

## Exact revision

The audited source is
[`hc7_k7minus_five_rotation_palette_intersection_barrier.md`](hc7_k7minus_five_rotation_palette_intersection_barrier.md),
with SHA-256

```text
97602ce40a1f5d7f8816a0b89b71e177fd8f4787331ecb11cb250c72680c9b76
```

## Checks

The row `R` uses all six colours with multiplicities
`1,1,1,1,2,2`, so its singleton colours are exactly `0,1,2,3`.  For each
`c in \{0,1,2,3\}`, the row `P_c` has eight entries and omits exactly
`c`.  Assigning the four non-root centres bijectively to those four colours
therefore makes each centre's displayed colour absent from its neighbour
slots, while only the root is saturated.

The four missing-colour sets are `\{0\},\{1\},\{2\},\{3\}`.  Their
intersection is empty, so condition (1.1) fails for every one of the six
pairs of singleton root colours.  The colour set on the other four centres
is exactly `\{0,1,2,3\}`; every singleton pair meets it, so (1.2) also
fails for all six pairs.  The same construction can be used independently
for each choice of root.

## Scope

The source correctly claims only a palette-row counterexample.  It does not
claim a common graph realization, consistency on overlapping
neighbourhoods, contraction-criticality, seven-connectivity or target
exclusion.  No broader mathematical conclusion was inferred.
