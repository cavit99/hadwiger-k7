# OpenAI mathematical releases: review of 7 October 2026

**Frozen literature review.** Current project status belongs to the
[research ledger](../../RESEARCH_LEDGER.md). This directory preserves our
review of external work, not new theorems of this repository.

All sources below refer to `openai/math` revision
[`adc7f1241b42e322a6451854ab7e4b4c146bf78a`](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a).
The three manuscripts are dated 23 September 2026. Our review concerns
this revision; it makes no assertion about subsequent corrections.

## Findings and verification scope

| External manuscript | Main conclusion | Our examination |
|---|---|---|
| [A counterexample to Hadwiger's conjecture](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026) | Theorem 1.1 and Corollary 1.2 give arbitrarily large finite graphs with `chi(G)>h(G)`, indeed `chi_f(G)>h(G)`. | Provisional positive informal proof audit: no fatal gap or unmatched dependency identified. |
| [A linear list-colouring bound in terms of the Hadwiger number](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026) | Theorem 1.1 asserts `chi_list(G)<=C h(G)` for every finite nonempty simple graph, with an absolute integer C. | Primary statement, relevant constructions and input interfaces inspected; no full proof audit here. |
| [A counterexample to the Colin de Verdière chromatic conjecture](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026) | Theorem 1.1 asserts arbitrarily large graphs with `mu(G)+1<chi(G)`. | Statement inspected; no full proof audit here. |

Here `h(G)` is the largest complete-minor order, `chi_f` is fractional
chromatic number and `chi_list` is list chromatic number. The first
paper concerns ordinary minors; it is distinct from the earlier disproof
of the odd Hadwiger conjecture.

The [counterexample review](audit-summary.md) gives the exact theorem,
proof obligations, component reports and limits of verification. The seven
component reports and [source hashes](audit-source-manifest.sha256) are
preserved unchanged from that review. References within them to pending
sibling checks or files outside this repository describe their original
working context; the coordinating summary records the completed assessment.
All 16 section hashes were rechecked when these records were archived.
The hash file lists the filename first and SHA-256 second; it is not in
`shasum -c` format. No third-party manuscript is copied here.

No Lean build was run. The release's [family formalisation note](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/157.md)
covers the linear list-colouring theorem. The inspected
[matching-minor formalisation](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/HadwigerMatching/Main.lean)
contains a conditional counting bound, not the existence construction for
the counterexample. We did not generate or check a manageable explicit
counterexample. Our positive verdict is informal AI-assisted scrutiny,
not independent human review or a formal certificate.

## Consequences for this programme

The counterexample construction has independence number at most two and
enormous order. Such graphs already contain `K7`: the elementary Ramsey
recurrence gives `R(3,7)<=binom(8,2)=28`. Thus these examples refute neither
HC7 nor our stronger-exclusion C21 statement. The paper establishes
failures at unbounded values of t; it does not determine the smallest
failing t. A proof of HC7 remains a separate, substantial objective. If
the general disproof is correct, a proof for every t is no longer a viable
extension of that objective.

The linear list bound, if correct, implies `chi(G)<=C(t-1)` for
`K_t`-minor-free graphs. It supersedes the former asymptotic payoff and
Liu–Luo v2's ordinary `O(t log log log t)` bound. It also makes our old
freely quantified contraction target R vacuous; the
[parked frontier](../../active/quantitative_star_contraction_frontier.md#external-update-7-october-2026)
gives the short implication and distinguishes it from a construction.
Neither external theorem is claimed as our contribution.

The linear paper's Theorem 8.1 simultaneously supplies a rooted complete
minor and prescribed paths in a `Ka`-connected graph with list chromatic
number at least `Qa`. Its proof chooses `K>=100`; those hypotheses are
unavailable in a host with a degree-seven vertex. Wovenness and the
associated rerouting framework already appear in the cited Postle and
Delcourt–Postle work; they are not wholly new to this release. The paper's
Lemma 6.9 allows choices of endpoints, so it cannot silently preserve
fixed colour or root assignments in our setting. These mechanisms suggest
constructions to attempt, not an applicable HC7 closure theorem.

The selected degree-seven split-clique case therefore remains open.
Any proposed reduction still needs the original proper-minor colouring
constraints, disjoint connected preimages and a valid lift. A finite
boundary state space alone does not bound the exterior or justify finite
verification. No additional HC7 case was closed by this literature review.

The release's [workflow account](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/README.md)
describes an unreleased internal model and provides no Hadwiger discovery
trace. It does not support a numerical estimate of our chance of proving
HC7 or establish that copying its compute allocation reproduces its results.
