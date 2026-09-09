# Audit of the quantitative contraction route

**Verdict: GREEN for the conditional deductions; the target is unproved.**
Date: 9 September 2026. This is separate internal review, not peer review.

Reviewed [source](quantitative_star_contraction_frontier.md) SHA-256:
`cce103f512dbe626e0a47df0c4e935f7cee86773a5512899710ebb652d6404c3`.
The parent wrote the frontier. Literature-repair independently read the
whole final source and rechecked Delcourt–Postle's primary Theorem 1.6.
Universal-proof independently checked the preceding mathematical text;
the final changes make the packing choice, parameter range and rounding
explicit. Both reviewers separately attempted the missing density bound.

Lexicographic `(n,e)` minimality supplies chromatic criticality for every
proper minor. The independence hypothesis and order cap are minor-closed.
The proposed reduction strictly decreases order; `n'>=q-1>Kr` activates
both logarithms. The stated constants make the potential loss exceed
`q^3-(q-1)^3`. The small-graph range in Delcourt–Postle eventually lies
below `r^(3/2)`, uniformly in its specified parameter interval.

The weighted packing recurrence selects a largest independent set in each
remaining neighbourhood. Its stars are disjoint, with original independent
centres; expanding their leaves and using one fresh colour gives the
claimed lift. The density implication uses an independent subset of size
`ceil(n delta/(2Dr^2))<=r`; its degree sum has the stated lower bound.

Neither stronger packing nor the density inequality is established.
Quotient independence does not permit charging successive rounds once.
The all-minor hypothesis cannot be replaced by independence information
about the original graph alone. No new colouring theorem, priority claim,
HC7 proof or NT-level significance is certified by this audit.

The bounded-bag obstruction insertion was separately checked by
literature-repair. Removing its eleven lines recovers the preceding
source `1b80523b745cc0b698f896feaf5f6c99f973adc0468f723226e4a4ccc94f7b2d`.
The [barrier](../barriers/quantitative_bounded_bag_density.md) and
[its audit](../barriers/quantitative_bounded_bag_density_audit.md)
cover all fixed bag-size bounds and the stated small-order regime.
The ledger at `1c849ad8f7628598c4b2d85aa1bcdfb6ba00684d93a50d13b279e0d8ae397545`
adds only the limited scope summary. Neither record refutes the density
inequality or the critical reduction R.
