# Independent audit: the cost of decreasing independence

**Audited source:** [quantitative_alpha_drop_cost.md](quantitative_alpha_drop_cost.md),
SHA-256 `1a31400ce2b7f88bcca1b0eda267ab5d4ec3bc01a952379187d90df17a5328db`.
**Reviewer:** separate internal audit by `marked_core_construction`, 12 September 2026.
**Verdict: GREEN.** The stated unrestricted constant-cost contraction claim
is false. No unresolved mathematical gap was found in the written family.
This is an internal audit, not external peer review or a novelty assessment.

The primary [Janson--Warnke v1 statement, equation (2)](https://arxiv.org/pdf/1406.1248v1)
was independently inspected. Its ground elements are independent, its
dependency sum counts ordered distinct pairs, and its parameter value
`epsilon=1` gives exactly the displayed zero-count inequality. Nonedges
provide the required independent ground elements; growing k is permitted.
Vertex overlap zero or one uses disjoint ground elements, so the source's
sum starts at two and correctly excludes the diagonal overlap k.

The explicit ceiling choice of n gives the stated Stirling constant and
`mu_n=(1+o(1))n^(3/2)`: rounding contributes `1+o(1)` after the kth power,
as does the falling-factorial approximation. The exponent for `mu_m` is
`3/2+2 log_2(.99)>7/5`. The expected number of independent `(k+1)`-sets
is `Theta(k sqrt(n))=o(n^(3/4))`, as needed for the alteration.

The strongest inference is the uniform large-set Janson estimate. The
exact overlap ratio and its substitution `s=k-j` both check algebraically.
On the lower half, convexity of `log A_j` bounds the sum by
`O(k^5/n^2)`; its far endpoint has logarithm `-Theta(k^2)`.
On the upper half, `Q_1=O(k^3/n)` and the far endpoint again decays
exponentially in k squared, giving `O(k^4/(n mu_m))`.
Thus `Delta/mu_m=o(1)` uniformly for fixed-size m-sets. The resulting
failure bound `exp(-mu_m/2)` survives the union over at most `2^n` sets.

The smaller-set argument was checked separately over its entire overlap
range `2<=j<=s0-1`. Here `s0~log_2 m0`, `nu>=m0^3`, and the last
endpoint of `A_j` is `exp(-Omega(s0^2))`. Consequently the zero-count
exponent is `Omega(n/log^5 n)`, which dominates
`log binom(n,m0)=O(sqrt(n) log n)`. Greedy deletion of independent
s0-sets therefore proves `chi(G)=O(n/log n)=o(r)` after alteration too.

The elementary binomial exponential-Markov bound is valid, since
`(1-log 2)/2>1/8`. It proves both the uniform induced-density event and
the pairwise common-neighbour event. The latter survives deleting at most
`n^(3/4)` vertices, proving connectedness of the altered graph.
The clique-minor first moment covers all labelled disjoint bags and an
unused class. For each fixed assignment, the small-bag contact events
use disjoint edge sets. Their failure probabilities are at least
`n^(-1/4)`, and their number is `Omega(t^2)`; this dominates the
`(t+1)^n` assignments. Ignoring bag connectivity is a valid upper bound.

Choosing one vertex from every original independent `(k+1)`-set destroys
all such sets. The simultaneous large-set event gives `alpha(G)=k` and
remains valid after this arbitrary choice of deleted vertices. The proof
of `|H|<=h(H)(2 alpha(H)-1)` is valid for connected and disconnected H:
the grown set dominates, its second added vertices are independent, and
its contraction is adjacent to every bag of a minor in its complement.
Minor monotonicity then verifies the required inequality for every minor
F, including the empty minor, with `r=2t`; also `|G|<=r^(3/2)` eventually.

For every eligible connected B, an independent k-set in G-B would survive
in G/B. Hence B has at least `n/200` vertices. The exact edge-loss formula
includes all internal edges and all duplicated external contacts, so the
uniform density event gives loss `Omega(n^2)=Omega(r^2 log r)`.
This covers arbitrary connected bags, including clique bags and all of G.
There is no finite computation premise or assumption of a minimal bag.

The scope is exact: `r^2 alpha(G)=(128+o(1))n^2`, while `e(G)<=n^2/2`,
so the family itself satisfies the proposed density inequality eventually.
Its `chi(G)=o(r)` misses the critical reduction's high-chromatic premise.
An allowance proportional to the actual independence decrease is also
not refuted. The audit establishes this intermediate counterexample;
it does not establish or refute the critical reduction R, the proposed
improved colouring bound, C19 or HC7, or complete the global research goal.
