# Audit of the bounded-bag density obstruction

**Verdict: GREEN.** Date: 9 September 2026. Separate internal review,
not external peer review or a novelty assessment.

Reviewed [source](quantitative_bounded_bag_density.md) SHA-256:
`0818c1c78b098140c215f8e542033276c16460efb193380b9f1efae2b8ff0cd3`.
Universal-proof wrote the proof; literature-repair independently
reconstructed the argument, then read the complete draft and promoted
revision. The parent separately checked both. Relevant archives already
contain clique-blow-up projection arguments; no priority claim is made.

The independent-set conditioning has exactly `1+2^Z` extensions.
Summing the normalised neighbourhood expectation proves the stated
triangle-free bound. The independent-set first moment, size-biased degree
tail and short-cycle estimates hold simultaneously for sufficiently
large d. Deletions preserve the independence upper bound and retain the
claimed edge count. Thus the lexicographically first finite base exists.

Every disjoint model projects to connected supports of size at most b,
with multiplicity at most s at each base vertex. The conflict colouring
uses at most bs colours, including bags contained in one fibre. A triangle
in any class lifts to a cycle of length at most 3b. The maximum-degree
and independence estimates therefore cover every model, including minors
with deleted contact edges. The exponential blow-up gives `n<=t ln t`
without changing the vanishing ratio for fixed b.

The argument refutes the proposed bounded-bag extraction, including
matching contractions. It establishes no violation of the density
inequality and supplies no chromatic criticality or density-surplus
instance. Unbounded bags and the full target remain open. No computation
or external theorem is a premise; there is no finite verification claim.
