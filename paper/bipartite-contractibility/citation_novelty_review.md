# Scope, provenance and comparison of the bipartite proof

**Status:** primary-source scope review and written elementary deductions,
8 September 2026. The adjacent [audit](citation_novelty_review_audit.md)
checks this revision. Current research standing belongs to the
[ledger](../../RESEARCH_LEDGER.md), not this review.

The [universal proof](../../results/bipartite_contractibility_via_matroid_reduction.md)
is checked at SHA256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`;
the [five-page manuscript](main.tex) at
`8cea0ca4838a7090b5fb4798c2c9ec670efe60017a6f7df1e79dc0d668c0b701`.
Neither source is changed by this review.

## What was already asserted

Biswal--Lee--Rao, [arXiv v2, Lemmas 3.2 and 3.4](https://arxiv.org/pdf/0808.0148v2),
assert the bipartite flow minor and retention of every terminal. The
independent-intersection convention counts intersections of paths for
demand edges with four distinct endpoints. Their prefix construction has
the separately [audited counterexamples](../../barriers/bipartite_flow_prefix_construction.md)
to Lemmas 3.5 and 3.6. These refute its intermediate assertions, not the
intended theorem. The apparent reversal in the published intersection
definition is a separate issue.

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

**Assessment:** a complete independent proof with substantial universal
scope and a concrete repair of an earlier construction. An original proof
of an old assertion can be important research. The present evidence does
not establish that this repair advances mathematics as far as the two new
NT conclusions, nor that it is the first correct proof. Comparable
significance is therefore not substantiated; no implication to HC7,
Conjecture 19, Conjecture 21 or T44 is established by this theorem.
External peer review is not being imposed as a separate completion gate.

The focused source check covered the BLR v2 statement and construction,
its version record, KPR's questions, the stated NT theorems, and Lee's
later use. No replacement proof was located in the checked sources. This
is not an exhaustive absence claim. Manuscript positioning should be
"an independent proof of the intended rooted bipartite flow assertion";
stronger priority language needs further evidence.
