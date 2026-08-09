# External-review packet: clique incidence under `K_7^-` exclusion

**Status:** compact review blueprint; not a manuscript, external peer review,
proof of the `K_7^-` six-colour conjecture, or proof of `HC_7`.

**Historical note:** the statements and hashes below are frozen at tag
`k7minus-global-count-review-2026-07-28`.  The linked density result has
since been superseded by the audited
[rooted-helper closure](../results/hc7_k7minus_degree7_rooted_helper_closure.md),
which gives `n_7=0`, no literal `K_5`, `m>=4n`, and `n_8>=25+tau` in the
critical host.  Use the
[critical-host frontier](hc7_k7minus_seven_exceptional_frontier.md) and the
[revised manuscript](../paper/k7minus-low-degree/main.pdf) for live status.

**Review branch:** `experiment/k7minus-global-count-gate`

**Frozen review tag:** `k7minus-global-count-review-2026-07-28`

This packet is separate from the
[bounded-interface review blueprint](hc7_partial_results_external_review_blueprint.md)
and does not alter the authoritative `HC_7` proof spine.

## 1. Proposed note

**Working title:** *Clique incidence in a hypothetical counterexample to the
`K_7^-` six-colour conjecture*.

The note should contain only the following chain.

1. A minor-minimal non-six-colourable `K_7^-`-minor-free graph is
   seven-connected, seven-chromatic, and has every proper minor
   six-colourable.
2. Every degree-seven vertex lies in a literal `K_5`.
3. The whole graph contains at most two literal `K_5` subgraphs.
4. Jakobsen's density theorem then forces at least five degree-eight
   vertices whose neighbourhoods are `K_4`-free.
5. The exact finishing conjecture is that five such vertices cannot coexist.
6. A paired-rooted `K_5` model for one nonadjacent pair is recorded only as
   a stronger possible route.
7. The 11-vertex barrier shows that the two local neighbourhoods and seven
   internally disjoint paths alone do not supply that model.

The note should omit the bounded-interface case tree, campaign history,
compute use and speculative proof architectures.

## 2. Results for review

### Degree-seven clique incidence

- [Theorem](../results/hc7_k7minus_degree7_clique_incidence.md)
- [Internal audit](../results/hc7_k7minus_degree7_clique_incidence_audit.md)
- Theorem SHA-256:
  `8378b1920987284abf3ff33d476d28efee5c9a13659afe7a192febaacb3d501f`

The dependency audit must include the full promoted proof of degree-seven
anti-neighbourhood connectivity and Theorem 3.5 of the matching-language
rooted-model result.  The optional finite census is not a dependency.

### At most two literal `K_5` subgraphs

- [Theorem](../results/hc7_k7minus_three_clique_bound.md)
- [Internal audit](../results/hc7_k7minus_three_clique_bound_audit.md)
- Theorem SHA-256:
  `5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574`

The overlap-four branch yields `K_7^-`, not necessarily `K_7`.  When all
pairwise intersections have order at most three, Theorem 1.10 of Niu and
Zhang yields `K_7`.

### Five exceptional degree-eight vertices

- [Theorem and exact finishing conjecture](../results/hc7_k7minus_five_exceptional_vertices_reduction.md)
- [Internal audit](../results/hc7_k7minus_five_exceptional_vertices_reduction_audit.md)
- Theorem SHA-256:
  `3ebcbaf595b16d616dcd01efdc2e8dd23f0ed6079a3294e8299f7b365787483b`

The proved conclusion is that every hypothetical counterexample has at
least five degree-eight vertices lying in no literal `K_5`, and two of them
are nonadjacent.

### Seven-path barrier

- [Barrier](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier.md)
- [Internal audit](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier_audit.md)
- [Deterministic verifier](../barriers/hc7_k7minus_bad_pair_seven_paths_barrier_verify.py)

The barrier is not seven-connected or contraction-critical.  It refutes
only the inference from two local neighbourhood types and seven disjoint
paths to a `K_7^-` minor.

## 3. Exact open statement

> **Five-exceptional-vertices conjecture.** A seven-connected graph `G` with
> `chi(G)=7`, every proper minor six-colourable, and no `K_7^-` minor has at
> most four degree-eight vertices whose neighbourhoods are `K_4`-free.

This is exactly sufficient after the proved density count.  It is weaker
than excluding every nonadjacent exceptional pair and weaker still than
demanding a five-bag clique-minor model meeting both neighbourhoods of such
a pair.

## 4. External sources requiring exact checks

- Mader's seven-connectivity theorem for contraction-critical graphs;
- Dirac's contraction-critical neighbourhood-independence inequality;
- Jakobsen's `K_7^-` extremal theorem and cockade exception, as quoted in
  Albar, Theorem 2 and Corollary 4;
- Niu--Zhang, *Cliques, minors and apex graphs*, Theorem 1.10;
- Norin--Totschnig's `K_7^vee` theorem and its proposed `K_7^-`
  strengthening;
- Albar's treatment of the specific `C_8^{1,2}` degree-eight
  neighbourhood; and
- the closest multi-degree-eight results of Rolek, Song and Thomas.

## 5. Review questions

1. Is every dependency and branch-set adjacency in the degree-seven theorem
   valid under exactly the displayed hypotheses?
2. Does Niu--Zhang Theorem 1.10 apply exactly as stated, including the
   meaning of non-two-apex and without an omitted disjointness or union-size
   condition?
3. Is the Jakobsen threshold and exclusion of every cockade exception used
   correctly in the degree count?
4. Is the at-most-two-`K_5` theorem already explicit or implicit in the
   literature, especially in Norin--Totschnig or Albar?
5. Can known colourful-minor or contraction-critical methods exploit all
   five exceptional vertices simultaneously?

## 6. Decision gate

Do not merge these claims into a publication-grade theorem package or
restart autonomous proof search until independent specialists validate the
two `K_5` lemmas and the source matching.  A correction creates a new frozen
tag and requires renewed audits and hashes.
