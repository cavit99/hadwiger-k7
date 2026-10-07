# Review of the claimed Hadwiger counterexample

7 October 2026

**Verdict: provisional positive assessment after an informal proof audit.**
No false intermediate statement, fatal inference or unmatched proof dependency
was identified in the reconstruction below. The written argument appears
mathematically sound on this examination. This is an AI-assisted internal
assessment, not independent human review or a formal certificate. Absence of
a detected error does not establish that no error exists.

## Exact source

OpenAI, *A counterexample to Hadwiger's conjecture*, dated 23 September 2026,
in [`openai/math`, revision
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026).
The remote `main` revision was checked again during this audit and matched.
All 16 section files, including the introduction and history, were verified
against their pinned Git blob hashes. Their sorted SHA-256 manifest is
[retained separately](audit-source-manifest.sha256); its SHA-256 is
`e57fbf47bfa648d9cea046514d4cd08daaf7e63808946fe63044e4177eb433c2`.

The audit concerns this manuscript. It does not verify the separate Colin
de Verdiere or linear list-colouring manuscripts.

## What must be established

Theorem 1.1 claims graphs of arbitrarily large order `m` with independence
number at most two and connected-matching number below `m/100`. Here a
connected matching consists of disjoint edges with an edge joining every
pair of their endpoint sets; mere connectivity of their union is insufficient.

The elementary bound

`h(G) <= (m + 4 cm(G) + 2)/3`

then gives

`h(G) < 26m/75 + 2/3 < m/2 <= chi_f(G) <= chi(G)`.

The central existence obligation is Theorem 3.1 (Raw supersaturation):
every law on candidate matching edges with the specified two marginal caps
and joint density cap must produce four cross holes with probability at least
`2^(-100gN)`. Endpoints within an edge may be dependent. Construction
constants and mixers must be chosen before that law, with the conclusion
uniform over all admissible laws for sufficiently large `n`.

## Audit coverage

Six complementary component audits reconstructed the proof; a seventh task
tried to construct counterexamples to Raw supersaturation. The coordinating
review checked the graph transfer, parameter order, final implication and
interfaces between components. One particularly consequential positivity
lemma received an additional separate reconstruction. Agreement between
agents was not used as a mathematical premise.

| Source files | Main checks | Record |
| --- | --- | --- |
| `02-geometry`, `03-frame-laws` | Triangle-free holes, frame sampling, all-rank image estimates, sparse intersections, weighted peeling | [Geometry](audit-geometry.md) |
| `04-moments`, `05-realization` | Boolean label decomposition, mixing forms, preservation of frozen data, annihilator argument, bounded-rank completion through channels | [Algebra](audit-algebra.md) |
| `06-collision`, `07-phases` | Collision probability, independent conditional cells, adaptive marks, rank growth, accepting-family injection, inverse-polynomial compatibility | [Collision and phases](audit-phases.md) |
| `08-preparation`, `09-histograms` | Exactification, preparation alternatives, entropy bounds, finite nets, mixed-law typicality, binary mixing, unary positivity | [Preparation](audit-preparation.md) |
| `10-product-tests`, `11-common-limit` | Product comparison, covariance estimates, compactness, stored conditional laws, truncation and density-product limits | [Analytic limit](audit-common-limit.md) |
| `12-status-span`, `13-rare-overlap` | Dual constraints, short witness lists, rare-case hit estimates, adaptive filters, overlap and uniform supersaturation | [Completion](audit-rare-overlap.md) |
| Main distribution statement | Diagonal couplings, shared frames, fixed subspaces, latent-feature couplings and shared certificates | [Adversarial search](audit-raw-law-adversary.md) |

Each component report states its imported hypotheses. The coordinating review
matched those imports to the corresponding audited statements. No specific
unproved mathematical dependency remained identified after that matching.
The reports' local qualifications should not be read as independent
certifications of the entire paper.

## Checks that matter most

**Dependence and conditioning.** The proof distinguishes the mixed unit law
from separately normalised leaves. Leaf bounds are joint density bounds;
they are not silently treated as marginal bounds. Pair-dependent conditions
are not used to claim that the conditioned units remain independent. In the
collision step, records are fixed at each parameter pair, making the two
remaining cells separate conditions on the two orientations.

**Positivity.** The change of coordinates in the free `Z` variables preserves
a fixed global key cell and the tester data. It does not preserve arbitrary
input filters or the bilinear form `T`. The uses respect this limitation.
The martingale estimate charges the intrinsic bias proportionally to cell
mass, permitting the construction constants to remain fixed as a positive
test cell becomes smaller. This inference survived two reconstructions.

**Rare compatible pairs.** A positive limiting overlap alone would miss
compatibility of order `N^(-4)`. The separate rare-case argument uses a
uniform large-set hit estimate and finite nets chosen on one original leaf
before the independent opposite leaf is sampled. Its exceptional pair mass
is `o(N^(-4))`, preserving a positive fraction of compatible pairs.

**Algebraic completion.** The completion preserves pin and key entries and
solves the two endpoint requirements together. Its residual rank bound is
independent of the later channel size. The available rank
`1000r0 - 2K - 4Blin` exceeds the required
`30r0 + 28J|E| + Dquo` by the stated, satisfiable parameter inequality.

**Parameter order.** Appendix A chooses early density and pin budgets, then
selector and mixer constants, then channels, then `M0`, and finally lets `n`
grow. Later analytic test accuracies change the required onset in `n`, not
the earlier construction constants. The final exponent margin is
`100g - [56(g-1)+.03] = 44g+55.97 > 0`.

**Uniformity and finite graphs.** Failure of a common sufficiently-large-`n`
bound would supply a sequence of violating laws. Preparation and both overlap
branches give the stronger probability bound along a subsequence, a
contradiction. The entropy-controlled container argument then transfers the
statement to a finite sample; its fingerprint log-count is `o(m)`. Repeated
sampled types cause no problem because the graph uses sampled positions.

**Minor counting.** In a clique-minor model, let `s` bags be singletons and
`e` have two vertices. Their adjacencies give a connected matching of size
at least `e + floor(s/2)`. Every other bag uses at least three vertices.
These two counts give the displayed bound on `h(G)` without an additional
structural assumption.

The separate adversarial search found no violating admissible law. That
negative search result is not used to prove supersaturation.

## Limits and decision relevance

No Lean build was run. The released family-level formalisation note covers
the linear list-colouring theorem. The inspected matching-minor formalisation
establishes a conditional bound, not existence of the required graphs. It
therefore supplies no formal certificate for the difficult existence step.
No manageable explicit counterexample was generated or computationally
checked; the manuscript proves asymptotic existence at enormous orders.

The appropriate conclusion from this review is **an apparently sound claimed
disproof with a provisional positive internal audit**, rather than a claim
of established community acceptance. The remaining uncertainty is the
reliability and completeness of informal verification, not a specific gap
discovered in this examination.

The construction does not refute the `t=7` case or the repository's C21
statement. Its graphs have independence number at most two and enormous
order, so they already contain `K7` as a subgraph: the elementary Ramsey
bound `R(3,7) <= 28` suffices. Establishing the first open fixed case remains
a separate mathematical objective even if this general disproof is correct.

No project source or research-status file was changed during this audit.
