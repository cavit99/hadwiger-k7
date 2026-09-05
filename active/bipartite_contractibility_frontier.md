# Universal bipartite contractibility and the remaining global target

**Status:** the universal bipartite theorem has a written proof and a
separate GREEN internal audit. `HC_7` remains conjectural and is the sole
remaining primary target. This technical file records the theorem's exact
application boundary; authoritative current status belongs only to the
[research ledger](../RESEARCH_LEDGER.md).

## Remaining global target

**Conjectural target — Hadwiger's conjecture for `t=7`.** Every finite
graph with no `K_7` minor is six-colourable.

The user's acceptable alternative is an independent theorem of reach and
significance comparable to Norin--Totschnig. The completed theorem below
is universal in its target class and resolves the bipartite scheme
question. Its publication priority and comparative significance require
separate assessment. No implication from it to `HC_7`, T44 or
Norin--Totschnig Conjecture 21 is established. No previously proved
theorem is being invoked here as a direct sufficient reduction of `HC_7`.

The preserved principal conditional refinement is
[T44](hc7_k44_closure_frontier.md): every seven-connected graph containing
a `K_{4,4}` minor contains a `K_7^-` minor. T44 would prove Conjecture 21,
that every `K_7^-`-minor-free graph is six-colourable. Both remain open.
The designated T44 frontier retains its two literal residues, closure
under the proposed induction, and the separate nonliteral branch-set
ownership obligation. Completing only the literal residues would not
prove T44. These are conditional routes, not consequences of bipartite
contractibility.

## Completed universal theorem

**Written proof with a separate internal audit.** For every finite simple
bipartite graph `H`, every `H`-scheme in a finite host `G` contains an
`H`-minor rooted at all prescribed vertices. There is no bound on either
graph's order, degrees, path lengths or intersection multiplicities.

An `H`-scheme has one simple path for each target edge, with its two
prescribed roots as ends and no other prescribed root internally. Every
collection of paths meeting at one vertex has a common target endpoint.
A rooted minor consists of pairwise disjoint connected branch sets, one
containing each prescribed root, with every required target adjacency.

The [full proof](../results/bipartite_contractibility_via_matroid_reduction.md),
[first exact-hash audit](../results/bipartite_contractibility_via_matroid_reduction_audit.md)
and [second independent internal audit](../results/bipartite_contractibility_via_matroid_reduction_second_audit.md)
give the complete unbounded argument. The
[current manuscript](../paper/bipartite-contractibility/main.tex) presents
the theorem independently of the earlier Hadwiger programme.

### The decisive reduction

A direct root-preserving colour normalization makes each path use only
its two endpoint colours. Orient the target bipartition `(A,B)` so that
the number `N_A` of nonroots on the `A` side is at most the number `N_B`
on the `B` side. Project paths onto each `A` colour, using each actual
`B` nonroot as an edge label wherever that vertex occurs. The total
graphic rank is `N_A` and there are `N_B` labels.

Edmonds' matroid union theorem gives either disjoint spanning trees in
all projections, immediately constructing the rooted model, or a
nonempty minimizing label set `X`. Equality in its rank formula forces
a maximizing disjoint forest family to span every component of every
projection restricted to `X`. Contract these connected host sets
simultaneously and delete unused labels of `X`.

Even when an `X` label belongs to several projections, each occurrence
has both endpoints in one component of its own projection. Its endpoints
are therefore already identified in the quotient using that component's
allocated tree. No path must recover the old label from another branch
set. The surviving paths use only their endpoint colours and retain all
roots; at least one contraction is nontrivial, so host order strictly
decreases. Induction and composition of the fixed minor models complete
the proof. Reversing the shore orientation between steps permits expansion
on both original shores.

This construction handles arbitrary label multiplicity. It neither
assumes a singleton root shore nor relies on an arbitrary returned model
being liftable through a previously deleted vertex. The proof is
computation-free; the exact source and its audit, rather than finite
tests, establish the theorem.

## Exact application boundary

**Written corollary.** Let `H` be finite simple bipartite of minimum
degree at least two, with its vertices injected into a finite host. Choose
one path for each target edge. If paths for edges with four distinct
endpoints are vertex-disjoint, the host contains an `H`-minor rooted at
all those terminals. In a bipartite graph, pairwise incident edges form
a star; the minimum-degree condition also excludes a nonincident terminal
inside a chosen path. These facts make the flow paths an `H`-scheme.

The [corollary's written proof](../results/bipartite_contractibility_via_matroid_reduction.md#5-the-intended-bipartite-flow-assertion)
independently proves the intended existence assertion of
Biswal--Lee--Rao [2, Lemma 3.2]. It uses the independent-intersection
convention in arXiv v2. The apparent reversal in the published definition
is a separate issue from the false intermediate statements in its prefix
construction. Lemmas 3.5 and 3.6 of that construction remain refuted by the
[audited explicit examples](../barriers/bipartite_flow_prefix_construction.md).
The new proof supplies the existence conclusion without validating those
branch sets or making an additional claim about spectral, separator or
bounded-depth conclusions.

**Application requirement.** A proposed further use must specify the
finite bipartite target, injective prescribed-root map and all scheme
paths, and verify the common-endpoint condition and exclusion of foreign
roots. Alternatively, it must verify exactly the flow corollary's
minimum-degree and independent-intersection hypotheses. Producing an
ordinary `K_{4,4}` minor alone supplies no additional `K_7^-` adjacency;
that is still the separate T44 obligation. No edge colouring or collection
of Kempe paths is assumed to satisfy the required scheme conditions
without a proof.

The earlier [even-subdivision theorem](../results/even_subdivision_contractibility.md),
[degree-three theorem preserving one shore's roots](../results/degree_three_bipartite_weak_contractibility.md),
and [universal weak-to-rooted equivalence](../results/bipartite_weak_to_rooted.md)
remain audited results at their original revisions. The universal theorem
now supplies full rooted conclusions for every included bipartite target,
including `K_{3,3}`, all `K_{m,n}` and every bipartite theta graph. Its
proof does not need root relocation or pendant root-forcing attachments.

## Literature scope and significance

**Written scope deductions; qualified independent assessment.** The
theorem answers Kündgen--Pelsmajer--Ramamurthi [1, Section 8, Questions 2
and 3] affirmatively, and rules out the bipartite counterexample sought in
Question 4. This is a terminal universal result, not another restriction
on a hypothetical counterexample. Its broad rooted-minor conclusion and
independent proof of the intended flow theorem make it a credible
candidate for the requested independent-theorem alternative.

The [separate internal assessment](../results/bipartite_contractibility_via_matroid_reduction_audit.md#mathematical-reach-and-the-norin--totschnig-comparison)
does not certify equal significance to Norin--Totschnig. Their Theorems 4
and 6 concern six-colouring under a near-clique-minor exclusion and the
supporting extremal bound. The present theorem has a different scope;
its relation to that colouring programme remains unproved. BLR's earlier
broad existence assertion also requires explicit qualification of any
priority claim. Specialist assessment of originality and comparative
significance remains outstanding; an internal audit is not external
peer review.

## Preserved barriers and frozen attempts

The [pre-promotion technical snapshot](../archive/bipartite_contractibility_frontier_2026-09-05_before_universal.md)
preserves the exact hypotheses, first unsupported inferences and possible
repairs of the former local approaches. Their failure does not contradict
the universal theorem. In particular:

- The [singleton-shore barrier](../barriers/bipartite_scheme_singleton_shore_barrier.md)
  still refutes requiring either entire original root shore to remain
  singleton. Iterated contraction permits both shores to expand.
- The [archived split-and-lift attempt](../archive/bipartite_contractibility_frontier_2026-09-05_before_universal.md#two-uniform-cases-and-a-failed-induction)
  still shows that a virtual edge cannot always be expanded through a
  vertex already owned by another returned branch set. The new proof
  contracts all required projection components with disjoint allocated
  labels before invoking induction.
- The [prefix-construction barrier](../barriers/bipartite_flow_prefix_construction.md)
  still refutes the two stated intermediate BLR lemmas. The intended
  main assertion is now independently proved.

Local root relocation beyond degree three, root-suppression attempts on
odd paths, a fixed split of matching paths and a proposed matroid-kernel
application remain archived failed mechanisms. They are not live proof
obligations after the universal theorem. The
[campaign reduction nonclosures](../archive/bipartite_campaign_reduction_nonclosures_2026-09-05.md)
also preserve the failure of a natural degree-preserving gadget lift and
an explicit obstruction to upgrading an arbitrary five-connected `K_6`
model to `K_7` minus a matching. Neither is used by the universal proof.
The
[retained experiments](experiments/bipartite_contractibility/README.md)
are diagnostics with explicitly finite scope.

## References

[1] A. Kündgen, M. J. Pelsmajer and R. Ramamurthi, *Finding minors in graphs
with a given path structure*, Journal of Graph Theory 79 (2015), 30--47,
[primary preprint](https://arxiv.org/pdf/1207.6141),
[DOI](https://doi.org/10.1002/jgt.21812).

[2] P. Biswal, J. R. Lee and S. Rao, *Eigenvalue bounds, spectral
partitioning, and metrical deformations via flows*, Journal of the ACM
57(3) (2010), Article 13, [DOI](https://doi.org/10.1145/1706591.1706593),
[primary preprint v2](https://arxiv.org/pdf/0808.0148v2).

[3] S. Norin and A. Totschnig, *Every graph with no `K_7^vee`-minor is
6-colorable*, [primary preprint](https://arxiv.org/html/2507.03244v1),
Theorems 4 and 6, Conjecture 21.
