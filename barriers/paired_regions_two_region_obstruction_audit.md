# Internal audit of the two-region obstruction

**Verdict: GREEN.** Date: 8 September 2026.

The complete [source](paired_regions_two_region_obstruction.md) is audited
at SHA-256 `b759e5a56e15911dd54bec784e36feaa8edc901558e30b3c05f2ecaf6d618736`.
This covers the original graph, arbitrary paired-bag impossibility,
the family for every `k>=4`, and the final clique-boundary variant with
its two-fan. The proof is elementary; no finite enumeration is a premise.

## Review provenance

The reviewer independently derived the original ownership obstruction
from the exact graph, then compared it with the author's argument.
The full source was read at `08b2c12dab10a15122bd8a2e8dad6ce7faaa321aa510fa63e6509e1eb04e547b`.
The all-k extension was independently checked and its exact text read at
`7789f3968d7a748749ccc3d98affa031f34986638b3799d2f708fdc395614944`;
removing its 22-line insertion exactly recovered the earlier revision.
The strengthened clique-boundary variant was separately checked and read
at `bf64285606ce8a0395f453fde399e4e0bedb195269ff5c0b18a7fb19ac3c451a`.
Reversing only the final status paragraph recovers that mathematical
revision. The final source contains the stronger deletion of `3--10`,
retaining `2--12`; the earlier weaker variant is not the current claim.
These were internal proof reviews with subsequent discussion, not
external peer review or claims of independent discovery of every variant.

## Verified claims

- The original 25-edge graph has the two stated disjoint full regions.
  Every edge of the displayed four-path linkage exists, and its paths
  use all eight terminals with disjoint vertex sets.
- The paired-bag argument permits unused nonterminals. The terminal
  neighbourhoods nevertheless force 10 and 12 into distinct large-R
  bags, and 10 and 14 into distinct large-S bags. Roots 0,1 then force
  8,9; root 5 forces its bag to be the 1/9 bag. Distinct 12 and 14 bags
  would disconnect the 0/8 bag. Their common bag must contain 11 because
  root 4 forces 13 elsewhere. The 10 bag has exactly one neighbour.
- The displayed positive paired model has precisely the claimed triangle
  with a leaf. Thus the barrier concerns the contact requirement, not
  failure of a linkage or of connected paired bags altogether.
- In the all-k family, each large terminal class has exactly `k-2`
  available neighbours. Disjointness forces every Z vertex into its own
  paired large-root bag. These bags are unavailable to 0,1,4,5, so the
  original four-bag forcing remains valid. They are universal through
  terminal edges. The order `3k+3`, full k-linkage and exact contact graph
  `K_k` minus two adjacent edges hold for every `k>=4`.
- In the final clique-boundary variant, added K edges cannot be used
  inside a paired bag: their ends are distinct prescribed R roots.
  Root 3 therefore forces 12, and r forces 10. The regions retain all
  stated properties, while the r bag still has just one contact. The
  two displayed fan paths avoid K and meet only at r; their existence
  does not change the forced ownership of vertex 12 by another bag.

The source correctly identifies the failed depth-three interval argument
without treating an interval supergraph's contacts as actual edges.
The proved k−1-region and one-sided theorems are unaffected. The modified
example is only an abstract boundary-state obstruction; no prequotient
origin or critical-host hypothesis is asserted. No gap was found in
these stated conclusions, and neither C19 nor the global goal is resolved.
