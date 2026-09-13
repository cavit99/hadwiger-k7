# Audit of the uniform-capacity obstruction

**Verdict: GREEN; separate internal audit, 13 September 2026.** This is not external
peer review. The allocation-construction agent independently reviewed the
proof written by allocation-adversary and revised by the parent.

Reviewed [source](quantitative_uniform_allocation.md) SHA-256:
`681581bc9364a715dc8690739c7e0c26dae1a1cb14b2caa3139838a52c4c4a55`.
The mathematical review covered revision
`5458774bad90c66522dad00159fc4d74e0680afa1fdd9b6ce52e8d74461ed34c`;
the only subsequent change replaces the pending-audit status sentence.

The integer slack argument proves hereditary independence-ratio closure
under a one-vertex sum. For minors, a bag meeting several pieces must
contain the shared vertex, and its intersection with each piece is
connected. All other bags belong to individual pieces. This proves the
required all-minor conclusion, including deleted contacts and unused
shared vertices.

The random-graph properties hold simultaneously. The clique-minor upper
bound counts arbitrary disjoint bags, with pairwise independent contact
events on the small bags and an upper bound of `(t+1)^N` assignments.
Ignoring connectivity increases the event being bounded. The elementary
bound `|F|<=h(F)(2alpha(F)-1)` was independently reconstructed from the
proof in [the independence-cost barrier](quantitative_alpha_drop_cost.md),
SHA-256 `1a31400ce2b7f88bcca1b0eda267ab5d4ec3bc01a952379187d90df17a5328db`.

The clique retirements are permissible. Through the first `floor(N/100)`
core mergers, the untouched-singleton edge comparison excludes every
edge incident with the apex, regardless of minimum-codegree ties. The
degree lower bound excludes retirement. At most j original common
neighbours enter the two endpoint bags, and at most j more are lost by
identifications, giving the stated common-neighbour lower bound.

All eligible preimages remain inside H, including when endpoint bags
are allowed. Demands total `Omega(N^2)` whereas capacities total
`bN=o(N^2)`. This also holds for any fixed multiplier. The order cap,
`b~r=o(N)`, and `e(G)/(r^2 alpha(G))->1/2` are correct.

The example refutes the uniform allocation for a permissible history,
even with connected inputs and no successful minor. It does not have
density surplus, refute the density target, or exclude an existential
choice of history under that surplus. Adaptive and nonuniform allocations
remain possible. No global colouring theorem, HC7 result or significance
comparison is certified here.
