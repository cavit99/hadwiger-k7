# Scope, provenance and comparison of the bipartite proof

**Status:** primary-source scope review and written elementary deductions,
8 September 2026. The adjacent [audit](citation_novelty_review_audit.md)
checks this revision. Current research standing belongs to the
[ledger](../../RESEARCH_LEDGER.md), not this review.

The [universal proof](../../results/bipartite_contractibility_via_matroid_reduction.md)
is checked at SHA256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`;
the [five-page manuscript](main.tex) at
`6d804a715f8782ac84679a8a5715105cb28d2a7cf4a594c60aec5b1072b387b9`.
The theorem source is unchanged; the manuscript incorporates this review.

## What was already asserted

Biswal--Lee--Rao, [arXiv v2, Lemmas 3.2 and 3.4](https://arxiv.org/pdf/0808.0148v2),
assert the bipartite flow minor and retention of every terminal. The
independent-intersection convention counts intersections of paths for
demand edges with four distinct endpoints. Their prefix construction has
the separately [audited counterexamples](../../barriers/bipartite_flow_prefix_construction.md)
to Lemmas 3.5 and 3.6. These refute its intermediate assertions, not the
intended theorem. The apparent reversal in the published intersection
definition on published page 13:10 is a separate issue. The defective
construction remains on page 13:11 of the journal version.

**The degree restriction supplies no new theorem priority.** The intended
rooted assertion for minimum degree at least two implies contractibility
for every finite bipartite target. Given an arbitrary scheme, attach a
private four-cycle at each target vertex, and the matching literal cycle
at its host root. All three added vertices are prescribed new roots.
The enlarged target is bipartite of minimum degree at least two, and the
old paths together with the added edges form a scheme. Apply the intended
rooted assertion. An original target's bag cannot contain an added vertex,
since that vertex is another prescribed root. Its connectivity and all
contacts to other original bags therefore use only the original host.
Restricting the model proves the claim, including leaves and isolates.

The new contribution is the independently developed simultaneous
graphic-matroid allocation and component contraction proof. Its induction
fixes disjoint connected preimages before recursion and strictly decreases
host order. Root retention, unrestricted degrees and constructive existence
must not be advertised as conclusions absent from the older assertion.

**Equivalent terminology.** Contractibility is property `(*)` in
[Kriesell--Mohr, Definition 1](https://arxiv.org/html/1911.09998v2#S1).
Choose the required bichromatic paths through a transversal of a proper
colouring: every intersection has its colour as a common target endpoint,
and no foreign root can occur internally. Conversely, colour normalisation
turns a scheme into this setting, and the rooted model lifts. Thus the
bipartite theorem also proves property `(*)` for every bipartite target;
this is an equivalent formulation, not an additional independent theorem.

The [flexible root-family result](../../results/bipartite_flexible_root_families.md)
also follows by augmentation. For each family add a centre joined to all
its roots, and a private leaf at each original root. In the target add a
leaf demand for each family member; extend the original demands through
the centres. These paths form a bipartite scheme. A private leaf's model
bag either contains its sole neighbour, the original root, or is singleton
and forces that neighbour into its family's centre bag. Unite the centre
and leaf bags for each family. Removing all artificial vertices leaves
components each containing a correct original root: every edge to a
removed vertex has such a root at its other end. Split each component by
a rooted forest into one bag per original root. Every cross-family model
contact is an original edge and survives between some two resulting bags.
This proves the stated flexible conclusion; it is not a separate stronger
existence theorem.

## Exact later use

Lee's [*Separators in region intersection graphs*, v3, Lemma 3.3](https://arxiv.org/pdf/1608.01612v3)
restates the bipartite flow assertion, citing BLR without a replacement
proof. It is used in Theorem 3.4 and then Corollary 3.6. This establishes
later use of the input; the separator and spectral conclusions are not
new results of this repository.

There is a narrower later bypass. [Kolbe--Spalding-Jamieson, Lemma 3.11
and Proposition 3.4](https://arxiv.org/html/2608.27179v1#S3.SS1), using
[Korhonen--Lokshtanov, Lemmas 4.3--4.4](https://arxiv.org/html/2308.04795v1#S4.SS3),
choose for each `h>=3` a particular demand graph of minimum degree at least
two and maximum degree at most three whose almost-embedding forces an unrooted
`K_h` minor. This bypasses the disputed extraction step for their
clique-flow application; other BLR inputs remain in use. It neither
extracts arbitrary bipartite targets nor retains all prescribed roots.
An arbitrary scheme cannot simply be subdivided into the required input:
newly independent demand segments may still intersect. Our proof should
not be described as necessary for those current clique-flow estimates.

**Scope lemma.** Let `H` be finite simple bipartite with minimum degree at
least two. A Lee `H`-flow of zero crossing congestion in a finite host
has an injective terminal map and yields an `H`-scheme at those terminals.
Consequently the universal theorem proves the full assertion of Lee's
Lemma 3.3, with the additional explicit rooted conclusion.

**Proof.** Each demand pair carries positive total flow. Suppose distinct
target vertices `u,v` have the same image. Choose independent incident
edges `ux,vy`: in the same shore choose distinct neighbours; in opposite
shores choose `x!=v,y!=u`. The degree bound and bipartiteness permit both
choices. Positive-weight paths for these demands meet at the common image,
giving a positive term in the nonnegative crossing sum, a contradiction.
Thus the map is injective.

Choose any positive-weight path for each demand. Zero crossing congestion
makes paths for independent demands disjoint. A foreign terminal on a
path for `ab` has an incident edge independent of `ab`, since at most one
of `a,b` is its neighbour. That edge's chosen path gives a forbidden
intersection. Finally, pairwise incident edges in a bipartite graph share
one endpoint, so all paths meeting at a vertex have a common target end.
This is a scheme. The argument includes fractional flows and endpoint or
length-zero intersections; it needs no rounding theorem. QED

BLR's Lemma 3.13 also asserts a bounded-depth variant. Their Section 1.2.2
uses diameter measured in the ambient host. The universal component proof
does not establish that bound or a bound on intrinsic branch-set radius.
No conclusion about those later estimates follows just from this repair.

## Comparison with Norin--Totschnig

[Norin--Totschnig, Theorem 4](https://arxiv.org/html/2507.03244v1)
proves six-colourability for every graph excluding `K_7` minus two adjacent
edges. Their Theorem 6 gives the sharp threshold `e>=4n-8` for that minor
in four-connected graphs, with exception `K_{2,2,2,2}`. These are new global
conclusions in the HC7 programme, not a proof of HC7 itself.

Our theorem is also uniform over arbitrary host and target order, target
degrees and treewidth, and retains every prescribed root. It answers
[Kündgen--Pelsmajer--Ramamurthi, Section 8, Questions 2--4](https://arxiv.org/pdf/1207.6141):
`K_{2,4}`, `K_{3,3}` and bipartite theta graphs are contractible, and no
bipartite counterexample exists. Those questions do not erase BLR's earlier
assertion. The later use above demonstrates utility, not a new downstream
bound or first-correct-proof priority.

**Assessment:** a substantial specialist contribution, but below the NT
benchmark on demonstrated consequences, even assuming first-valid-proof
credit. The theorem realises a supplied compatible routing; NT force new
minor structure from density and obtain a global colouring conclusion.
The matroid method may have further uses, but those are not yet proved
applications. This is a comparative judgement, not a community consensus.
Historical firstness remains unresolved, and no implication to HC7,
Conjecture 19, Conjecture 21 or T44 follows here. External peer review is
not being imposed as a separate completion gate.

The focused source check covered the BLR v2 statement and construction,
its published construction, KPR's questions, KM's property `(*)`, the NT
theorems, Lee's later use and the KL/KSJ application bypass. No earlier
complete proof of the universal rooted bipartite assertion was located
in these sources. This is not an exhaustive absence claim. The manuscript
presents an independent matroid proof; stronger priority language requires
further evidence. The user's separate AI reviews corroborate the proof
and comparison but supply no exact manuscript hash or external peer review.
