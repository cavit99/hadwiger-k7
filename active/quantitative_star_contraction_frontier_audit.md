# Audit of the quantitative contraction route

**Verdict: GREEN for the conditional deductions; the target is unproved.**
Date: 9 September 2026. This is separate internal review, not peer review.

Reviewed [source](quantitative_star_contraction_frontier.md) SHA-256:
`6a2d2a1cf714a3d97f007d1e9b70348ce3d943da83eb6a34f5d45835142aea45`.
The parent wrote the original quantitative argument. Literature-repair
and universal-proof independently reviewed it; literature-repair also
rechecked Delcourt–Postle's primary Theorem 1.6. Both reviewers separately
attempted the missing density bound. Reviews of the later additions
are recorded below.

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
literature-repair at revision
`cce103f512dbe626e0a47df0c4e935f7cee86773a5512899710ebb652d6404c3`.
Removing those eleven lines from that revision recovers
`1b80523b745cc0b698f896feaf5f6c99f973adc0468f723226e4a4ccc94f7b2d`.
The [barrier](../barriers/quantitative_bounded_bag_density.md) and
[its audit](../barriers/quantitative_bounded_bag_density_audit.md)
cover all fixed bag-size bounds and the stated small-order regime.
The ledger at `1c849ad8f7628598c4b2d85aa1bcdfb6ba00684d93a50d13b279e0d8ae397545`
adds only the limited scope summary. Neither record refutes the density
inequality or the critical reduction R.

Route-assessment independently reviewed the current source and its
38-line addition; the parent also checked it. The proposed inexpensive
contraction gives a valid connected induction, followed by component
summation. Both displayed contraction identities are exact. In the page
example the two stated edges lower alpha with costs `m+1` and one;
the decomposition has width two and the triangle gives `h=3`.
It excludes an arbitrary minimal choice, not the small-order existential
target. In the prism, pairing each top root with `w3` and each bottom
root with `u3` proves minimality; both opposite-pair paths use `u3w3`.
These checks certify the counterexamples and conditional implication,
not an inexpensive contraction, density bound or improved colouring theorem.

Literature-repair separately checked the added Lin August paragraph against
the primary statements and Section 3. Removing it recovers the preceding
audited source `0776fe609b3ab24807756226fadafa21631d01d36ca78a4bf7c99179a76f9f36`.
The density convention and hypothesis are retained. The smaller colouring
cutoff is reported, not used: its full substitution into Delcourt–Postle
has not been independently audited here. No preservation of independence
number, chromatic number or prescribed attachments follows from the cited
dense-subgraph extraction. Restricting the admissible blocks breaks the
maximality argument: an extension may fail the extra requirement without
violating the edge-loss bound. The conditional theorem and its dependencies
are unchanged.
