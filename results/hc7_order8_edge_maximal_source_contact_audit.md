# Independent audit of the edge-maximal source-contact theorem

## Verdict

**GREEN** at the exact corrected mathematical source and verifier revisions

```text
ca5fb07a55951f6d6817bc44d410042db1426a549c221880147f1627c7d6f126  results/hc7_order8_edge_maximal_source_contact.md
108d79e76cf029707e29df51e0b35258fb1b4bae84b52fbea1780a1f16906da4  results/hc7_order8_edge_maximal_source_contact_verify.py
```

The final theorem-source hash is

```text
d5ada64351dab70919e7800ada3b9869830df197ab523bbdf380d8bbcbd1ddd1  results/hc7_order8_edge_maximal_source_contact.md
```

The only subsequent source change was replacing the pending-audit status
with the link to this audit; no theorem or proof content changed.  This is a
separate internal audit, not external peer review.

## 1. Exhaustive encoding

There are `21-5=16` variable edges, so the `65,536`-graph universe is exact.
The verifier's `266` possible `K_5` branch-set systems are precisely

\[
 \binom75 S(5,5)+\binom76 S(6,5)+\binom77 S(7,5)
 =21+105+140.
\]

The `65` spanning `K_4` candidates are exactly the `S(6,4)` partitions of
`J-c_0`.  The connectivity and pairwise-contact predicates are direct, and
every missing edge is tested for creation of a `K_5` minor.  Canonicalization
checks all `7!` ordinary vertex permutations.

Running the verifier reproduces

```text
labelled_graphs 65536
edge_maximal_survivors 562
unlabelled_types 6
type_counts 007fff:10 00efff:192 01d7ff:120 01deff:84 05cdff:144 05defb:12
spanning_k4_failures 0
PASS order8_edge_maximal_source_contact
```

All survivors have fifteen edges and `d(c_0)=3`.

## 2. Host consequence

The four spanning bags and one original universal root form a genuine
`K_5`-minor model.  Taking the low-degree source column and the other
original root as the two roots matches the one-defect two-root theorem:
the original root meets all five model bags, while the source column meets
the first root and exactly three of the four remaining bags, hence four in
total.  The `K_7`-minor-or-separation conclusion is valid.

The abstract one-edge maximality hypothesis is not implied by maximality
among host-realizable decorated column systems.  The result is correctly
classified as a conditional finite endpoint, not a dirty-path exchange or
an unbounded closure theorem.
