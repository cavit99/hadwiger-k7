# Audit of the quantitative contraction route

**Verdict: GREEN for the conditional deductions; the target is unproved.**
Initial review: 9 September 2026; latest scoped review: 13 September 2026.
This is separate internal review, not peer review.

Reviewed [source](quantitative_star_contraction_frontier.md) SHA-256:
`86926710366d20ac3564195c5e11b126d8cb569f0cc565c0ae08c0b528741424`.
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

Literature-repair checked the seven-line odd-Hadwiger addition against
[Kühn–Sauermann–Steiner–Wigderson, v1, Theorem 1.3](https://arxiv.org/html/2512.20392v1).
GREEN for the date, quantifiers and stated scope: the asymptotic disproof
neither refutes ordinary Hadwiger nor settles odd t=7. This is a primary
statement check, not an independent audit of that paper's proof. Removing
the addition byte-recovers the preceding audited source
`6a2d2a1cf714a3d97f007d1e9b70348ce3d943da83eb6a34f5d45835142aea45`.
The conditional mathematics and ordinary-minor dependencies are unchanged.


## Refutation of the auxiliary uniform-cost reduction

**GREEN; separate internal integration audit, 12 September 2026.**
The preceding conditional deductions are preserved from source
`627bbd53c83f4fdc0f69e7c54fb1298cbc74151d5a561fee35878fd70d5e69f6`.
The revised source is
`0759a4ff5bada8eafe50e5ce1d0206027a30ab1f70549f21143f77119e756e9a`.
The [new barrier](../barriers/quantitative_alpha_drop_cost.md), source
`1a31400ce2b7f88bcca1b0eda267ab5d4ec3bc01a952379187d90df17a5328db`,
with its [separate proof audit](../barriers/quantitative_alpha_drop_cost_audit.md),
refutes the uniform-cost premise under both its order and all-minor
hypotheses. Its examples satisfy the density bound and have `chi=o(r)`;
they refute neither that bound nor the high-chromatic critical reduction R.
The original induction remains valid as a conditional implication.

The stated proportional-cost repair is equivalent to the density bound
up to constants. For D at least one, the terminal clique contributes at
most `r^2/2`, and the independence losses telescope. Conversely the whole
connected noncomplete graph has `alpha>=2`, so its contraction costs at
most `2Dr^2(alpha-1)` under the density bound. No new construction follows.

The separately reviewed ledger at
`a19e3ad6d981b4f11ed4e6a7a350f7a139157f3423f489eff251c0e96e7f8d2d`
and index at
`6385f25e328a905a622f57c8e049598b2f7e7752c155733c981420f7d696cce9`
retire only the false auxiliary step. R, the density inequality, the
improved colouring bound and the full HC7/comparable-theorem objective
remain unproved. No previous audited proof was modified.

## Several centres under the same one-colour lift

**GREEN; separate scoped internal audit, 12 September 2026.**
The added paragraph takes source
`0759a4ff5bada8eafe50e5ce1d0206027a30ab1f70549f21143f77119e756e9a`
to `65a0a62ca3c72fb26697465e09e1bd6b65f986b2cdd5abdceaddd6d7a1df3d9f`.
Both I and each B-I must be independent in the original host. For deleted
D subseteq I and b nontrivial bags, the exact order loss is
`L+|D|+sum_B |B intersect I|-b<=L+|I|`. Connectivity gives each non-I
bag vertex an adjacent I-centre. Assigning one produces disjoint stars
removing exactly L vertices; their independent leaves inherit quotient
colours, and all of I receives one fresh colour. Inter-star edges remain
in the quotient. Singleton bags and unused I-vertices cause no exception.
Deleting all I instead removes |I| vertices with the same colour bound,
so one operation recovers at least half the original reduction.
This excludes an asymptotic advantage of the enlarged operation class,
not a new packing proof within that class. It does not establish R,
the density inequality, an improved colouring bound or the global goal.

## Criticalisation after a star packing

**GREEN; separate scoped internal audit, 13 September 2026.**
The comparison-adversary agent independently checked the appended
70-line subsection and one earlier status-wording correction at source hash
`86926710366d20ac3564195c5e11b126d8cb569f0cc565c0ae08c0b528741424`.
The subsection is unchanged from the initially checked source
`c070665c4b21fd762c0b33b541d426fd2ab9ae6e8817a54df3efd0c5ba43b9cc`.
The preceding source, SHA-256
`65a0a62ca3c72fb26697465e09e1bd6b65f986b2cdd5abdceaddd6d7a1df3d9f`,
is byte-recovered by removing the appendix and restoring the earlier
phrase "has been proved" from "at the required scale has been proved".
The correction properly distinguishes the new conditional loss bound
from the unresolved scale required by R. The historical audits above
remain scoped to their stated revisions. Both new bipartite-input hash
pins match the files and the existing input audit's recorded theorem hash.

The strongest structural inference is valid. A singleton neighbour colour
can be eliminated by a Kempe swap unless its root shares a bichromatic
component with every other singleton root. Simple paths between opposite
shores give a simultaneous scheme: every common vertex has one colour,
so all paths there have that same target endpoint. A selected root cannot
occur internally on a foreign path. Rooted bipartite extraction retains
every neighbour of v; the matching contractions and singleton v then give
the forbidden complete minor. This proves the stated integer degree bound.

The star lift retains all edges between distinct bags. Every untouched
neighbour u of a centre was eligible when its leaf set was chosen;
maximality therefore supplies the second u-neighbour in that same bag.
Different star bags give distinct coalescences. Moreover every minor of H
is a proper minor of G and has chromatic number at most q-1. Thus minimum
order and then minimum edge count among (q-1)-chromatic minors really does
give full minor-minimality, not merely induced or vertex criticality.

A singleton preimage's degree cannot increase under operations elsewhere.
Consequently every U vertex is deleted or belongs to a bag of size at
least two. Charging a size-b bag at most b vertices against its b-1 order
loss proves the ceiling bound for arbitrary connected minor preimages.
Composing those bags with the original stars preserves disjointness and
all retained contacts; no roots or connectivity assumptions are imported.

For the edge inequality, independence of I means its degree sum counts
each centre-incident edge once. Internal edges vanish; a centre edge to
an untouched vertex has a distinct leaf-edge witness that coalesces with
it. Between two star bags, at most one of their centre-incident edges can
survive simplification. Subtracting binom(k,2) therefore suffices, even
when some bags are singletons or some pairs have no such edge.

Reed--Seymour's primary page 148 was checked: (1.3) gives fractional
2r-colourability under K_(r+1)-minor exclusion, and (1.4) gives the weighted
independent-set statement directly. Degree weights yield e(G)/r with no
cardinality guarantee. The source explicitly retains that missing cap.

No bound forcing enough leaves or U vertices is established. The linked
potential obstruction is identified as numerical, not an example meeting
R's graph hypotheses. Neither this audit nor the new degree and charging
deductions prove R, an improved colouring bound, or the HC7/comparable-
theorem objective. No novelty or significance assessment is certified.
