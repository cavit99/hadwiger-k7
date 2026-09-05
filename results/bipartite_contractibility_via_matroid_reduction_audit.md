# Separate internal audit: universal bipartite contractibility

**Status:** separate internal audit.

**Verdict: GREEN.** Audited on 5 September 2026 by a separate agent from
the proof's author. This is an internal mathematical audit, not external
peer review or an assessment of publication priority.

## Exact revision and scope

- [Theorem source](bipartite_contractibility_via_matroid_reduction.md).
- Whole-file SHA-256:
  `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
- Checked: Lemmas 0, 1 and 2, the universal rooted theorem, its scope
  deductions, and the independent-intersection flow corollary.

The conclusion is quantified over every finite simple bipartite target,
every finite host, every injective prescribed-root map, and every scheme
with that map. It preserves every original prescribed root. There is no
bound on target degrees, host order, path lengths or vertex multiplicities.

## Strongest inference: simultaneous component contraction

The audit concentrated on the implication from matroid rank deficiency
to a smaller scheme, especially a label used by several projections and
allocated to a different projection from the path being reconstructed.

The matroid union rank equality holds for any maximizing disjoint
independent family and any minimizing set `X`. For those choices,

`sum_a |I_a-X| <= |E-X|`, and `|I_a cap X| <= r_a(X)` for every `a`.

Equality of the total forces equality in every inequality. In particular,
`I_a cap X` spans each component of `M_a(X)`. No common favorable choice
of independently selected minima is being assumed. Labels absent from a
projection are loops in that projection's matroid and cannot enter its
independent set. Arbitrarily many projections may contain a label.

For each component, its allocated forest lifts to a connected host set
containing its original `A` vertices and only its allocated `B` labels.
The sets are disjoint across all components and colours. No `B` root or
surviving label of `E-X` is absorbed. Different prescribed `A` roots have
different colours and cannot be merged.

Consider an occurrence `u x v` on `P_ab`, where `x in X` is allocated to
an `a'` component with `a' != a`. Its projected edge nevertheless belongs
to `M_a(X)`, so `u,v` belong to one `a` component. That component has its
own allocated connecting tree. After its contraction the occurrence is
replaced by equality of its endpoint images. It never requires ownership
of `x` by both components. This is the decisive valid replacement for the
failed arbitrary split-and-lift argument in the existing frontier.

Reading each original path after these replacements gives a walk of
`a` component vertices, surviving `B` labels of colour `b`, and the
terminal `b` root. Every retained step is an actual quotient edge inherited
from an original `A` vertex and a surviving `B` vertex. Erasing closed
excursions gives a simple path with the same distinct root images.

A path cannot acquire a foreign root: another `A` root has a different
colour, and no `B` root is introduced by a replacement. The endpoint
root images can recur in an intermediate walk, but cannot be internal
vertices of the resulting simple endpoint-to-endpoint path. All paths
meeting at a quotient vertex have its colour as a common target endpoint.
The intermediate walks in the original host need not form a scheme;
only the quotient paths are asserted to do so.

## Normalization, terminal case and descent

Lemma 0 is self-contained. The scheme condition supplies a common
endpoint label for each used nonroot; roots receive their own distinct
labels. Contracting connected monochromatic components merges no two
roots. Every path maps to a walk using only its two endpoint labels;
loop erasure and restriction to the new path union preserve the scheme.
The proof needs neither minimum nonroot degree four nor an edge-disjoint
normalized path system.

In the projections, each nonroot label has distinct endpoint vertices
on its original simple path, so it is a nonloop wherever it occurs.
A target edge and the colour of its label determine its projection
occurrence uniquely. The projected paths share their prescribed `A`
root and cover their colour class, so their graph is connected and has
rank `|W_a|-1`. Trivial projections cause no exception.

Choose the shore with fewer nonroots as `A`. The total required rank is
`N_A` and the ground-set size is `N_B>=N_A`. Full rank gives disjoint
spanning trees and hence the explicit rooted terminal model. If rank
is deficient, the union expression at `X=empty` is `N_B`, strictly
greater than its minimum, so every minimizing `X` is nonempty. Some
projection then has positive rank on `X`; a selected label connects two
distinct `A` vertices through that label. At least one contracted set
therefore has at least three vertices, proving strict decrease of host
order.

As a separate arithmetic check, before removing any additional unused
vertices the reduced nonroot counts are

`N_A' = N_A - sum_a r_a(X)`, and `N_B' = N_B - |X|`.

Thus the number of nonroots decreases by `sum_a r_a(X)+|X|`. The rank
equality in the deficient case also gives `N_A'>N_B'`; reversing the
shore orientation at a later step is legitimate and helps explain why
both original shores may expand in the final lifted model.

The induction hypothesis concerns the same abstract target and a smaller
host. Its final model lifts through disjoint connected preimages of the
fixed quotient vertices. Every required edge lifts to a contact between
these preimages. Root containment and branch-set ownership are preserved
under this composition, independently of the original scheme paths.
Isolated target roots are removed and restored as disjoint singletons;
they occur on no other path. Empty targets and zero-rank terminal cases
are covered.

## Primary statements and the flow corollary

The primary author text of Edmonds, [*Matroid Partition*, Theorem 1 and
the following discussion, pp. 202--203](https://doi.org/10.1007/978-3-540-68279-0_7),
was inspected. Theorem 1 gives the minimum rank expression for an integer
polymatroid function; its application to the sum of the given matroid
ranks, together with the immediately stated partition characterization,
gives precisely the disjoint-independent-set formula used in Lemma 1.
The hypotheses hold for these finite graphic matroids after adjoining
loops for absent labels. No stronger packing theorem is invoked.

Kündgen--Pelsmajer--Ramamurthi's [primary preprint](https://arxiv.org/pdf/1207.6141),
Definitions 1.1 and 2.1, Lemma 3.3, and Section 8 were inspected. The
scheme and rooted-contractibility definitions agree. Lemma 0 supplies
the weaker normalization needed here directly. The universal theorem
answers Questions 2 and 3 affirmatively and rules out the counterexample
requested in Question 4. The claim about bipartite theta graphs follows
from their being included in the universal target class.

Biswal--Lee--Rao's [primary preprint v2](https://arxiv.org/pdf/0808.0148v2),
the independent-edge intersection definition and Lemma 3.2, were
inspected. The corollary supplies its intended minor-existence conclusion
and preserves every terminal. A family of pairwise incident edges in a
bipartite graph is a star. If a nonincident terminal lay inside `P_ab`,
minimum degree two would give an incident edge disjoint from `ab`, whose
path also meets that terminal, contradicting the hypothesis. These are
exactly the two additional checks needed to obtain a scheme. The result
does not use, repair or validate the specific prefix branch sets, and
does not establish any bounded-depth variant or downstream estimate.

## Mathematical reach and the Norin--Totschnig comparison

**Independent internal assessment, not a priority claim.** This is a
terminal universal theorem about rooted minor existence. It settles the
full bipartite contractibility question, includes all complete bipartite
targets, and supplies an independent correct proof of the intended
published flow-minor assertion. Its mathematical reach is substantially
greater than another bounded-degree family, partial-root statement or
finite diagnostic. The proof's central reduction removes the common
ownership obstruction for arbitrary label multiplicity.

Norin--Totschnig's [Theorems 4 and 6](https://arxiv.org/html/2507.03244v1)
give an unrestricted six-colouring conclusion under a near-clique-minor
exclusion and its supporting extremal theorem. The present result gives
a different unrestricted family of rooted-minor conclusions and resolves
explicit published questions; it has no established implication to those
colouring theorems or to Hadwiger's conjecture. Its breadth makes it a
credible candidate for the user's independent-theorem alternative.
Nevertheless, comparative mathematical significance is not certified by
an internal proof audit. In particular, the earlier broad BLR assertion
precludes presenting the underlying unrooted existence statement as first
proved or first formulated here without a separate priority assessment.
The responsible claim is an independent proof with universal rooted
scope, awaiting specialist assessment of originality and significance.

## Unresolved assumptions and limits

No unresolved mathematical gap or additional hypothesis was found in
the audited source revision. The sole external proof input is the stated
finite matroid union theorem. The result is computation-free; this audit
does not turn computational checks into evidence for an unbounded step.

External peer review, publication priority, and the requested comparative
significance standard remain unresolved assessments. `HC_7`, T44 and
Norin--Totschnig Conjecture 21 are not proved by this argument. The
pre-existing barriers remain valid at their stated intermediate scopes.
