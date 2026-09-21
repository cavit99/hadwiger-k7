# Internal manuscript audit

## Current disclosure revision — 21 September 2026

**Verdict: GREEN for the editorial change.** A reviewer separate from
the editor checked the complete source diff against Git revision
`7a1b98ce04a663cc7f01d46752608a0b65c94ecd` and independently verified:

| Current artifact | SHA-256 |
|---|---|
| [Source](main.tex), including bibliography | `02d771ae0973da267cea22be6e2bec6f1d9ac9905222f8c17b22c644e42fe391` |
| [7-page PDF](main.pdf) | `44a9d8daa02da9e93649d976935a1c42e99a30d4327b28ffeae3c5b62d527159` |

The sole source change adds the exact two-sentence AI disclosure approved
by the author before the bibliography. Removing it reproduces the base
source byte for byte. Every mathematical statement, proof and reference
is unchanged; the historical mathematical verdict and its scope remain
unchanged. This is a limited editorial review, not a fresh proof
reconstruction, literature search or external review.

The editor reports a warning-free build, byte-identical renders for pages
1–6 against the previously reviewed PDF, and a clean visual inspection
of the changed page 7. The reviewer independently checked the artifact
hashes; the current rendering check is the editor's report.

The preceding attribution review and its artifact pins are preserved at
the cited Git revision. The historical review below is unchanged; its
revision references and hashes concern the 13 September artifacts.

## Historical mathematical and editorial review — 13 September 2026

**Status:** separate internal mathematical audit; not external peer review.
**Verdict: GREEN.**
**Date:** 13 September 2026.

The auditor is a separate agent from the manuscript editor and did not
write its radius proof. The full mathematical review below preceded the
copyedit. The same auditor then independently reviewed the complete
editorial diff against the saved source, verified the old and new artifact
hashes, and checked that the changes preserve every statement and proof.
No unresolved mathematical gap was found within the stated theorem scopes.

## Exact revision and provenance

| Checked artifact | Whole-file SHA-256 |
|---|---|
| [Manuscript source](main.tex) | `8e531dfa43e072c438d4dd891f841f6171651d67e63d0d39849d6c0652b8b5e2` |
| [Seven-page PDF](main.pdf) | `e6e922f8645389da8ccea0baebb8a361463fca135306babb26a80e8f66d681fc` |
| [Universal theorem](../../results/bipartite_contractibility_via_matroid_reduction.md) | `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272` |
| [Short-scheme radius theorem](../../results/bipartite_short_scheme_radius.md) | `4fd71c1bd710e84f168426d4934e7eb4b1e830ddd9d61ce003d5a8161684202d` |
| [Radius proof audit](../../results/bipartite_short_scheme_radius_audit.md) | `2e53be1480c14ae4331dca2abb113f1a7f05be7904caccc01f42fbde1cf0f249` |

The universal theorem's two existing audit pins were also verified:
`1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`
and `83df07a306bef1a71b50bf5f36020a48b7240187c40d503819eb10baf5348297`.
Hash agreement supplements the present proof review; it is not its basis.

The full review immediately before this copyedit had SHA-256
`5a0718b3662a5c765e6f319eef584376f698a46e7e306ded2e7e614b435548f7`.
It checked manuscript source
`4b1da09fcf141937ed2df87e14238755db7377ab4a4d621fc56a4875918ecbe5`
and PDF `448e474b16ce45eeb1df9ed9557312ca4db2f04c8e64efae0835a29c9288523a`.
That review read the complete source and underlying theorem proofs,
compared the manuscript with Git revision `f7b52aff`, and attacked the
original-host distance invariant. The saved `main.before.tex` and
`main.before.pdf` have exactly those hashes. The current verdict combines
that full review with the editorial-diff checks below.

The previous manuscript audit remains in Git at
`f7b52aff:paper/bipartite-contractibility/main_audit.md`, SHA-256
`a96d5e5df2fc61a9c8f45cce105867b28c257d385aa395eb51f6aff88f4d5397`.
It audited the earlier manuscript source at
`6d804a715f8782ac84679a8a5715105cb28d2a7cf4a594c60aec5b1072b387b9`
and retains the earlier reviewers' precise provenance. Its verdict is
historical, not silently transferred to the added theorem or current PDF.

## Editorial-diff review

The abstract now names the target of the fully rooted model explicitly.
The theorem quantifiers, three-edge length limit, intrinsic radius at the
original prescribed root and sharpness statement are unchanged.

The forest wording correctly says that an independent set of full rank
*restricts* to a spanning tree in each nontrivial component. It does not
assert that the entire forest is one tree. Saying that the projected
paths cover `M_a` retains both vertex and edge coverage. The rewritten
quotient sentence still requires a witnessing original edge for each
remaining step, with the same endpoint colours and surviving label.

“Orient the bipartition” correctly replaces “Choose the shore (A,B)”.
Under the invariant, a current path of length greater than one is exactly
the former “nonliteral” case. The root-preimage invariant, both absorption
cases, opposite-shore reversal and final lift retain their original
meaning. The flow corollary's assignment to distinct terminals is precisely
the original injective terminal map; its minimum-degree hypothesis and
independent-path condition remain intact.

The later-use paragraph only changes syntax and tense. It preserves the
restricted demand-graph extraction claim and the qualifications concerning
arbitrary targets and bounded depth. No new mathematical or literature
claim is introduced. This review did not repeat the earlier finite or
primary-literature checks.

## Universal proof and root ownership

The normalisation contracts disjoint monochromatic components, each with
at most one prescribed root. Endpoint-coloured path images can be made
simple without introducing a foreign root. Every projection is connected;
the label is unique within each projection. Matroid-union equality forces
all component-spanning forests simultaneously, with disjoint labels.

The strongest quotient step is valid when an omitted label is allocated
to another root. Its two original base neighbours belong to the same
projection component; its omission therefore gives a well-defined quotient
walk. The retained edges have actual base-vertex witnesses. Loop erasure
preserves both endpoint colours, all roots and the scheme intersection
condition. The allocated connected preimages are fixed before recursion.
The count `|X|+sum_a r_a(X)` gives strict descent for nonempty `X`.
The full-rank case directly supplies all target contacts; the deficient
case recurs on the same target with a smaller host. Isolated roots and
reversal of the bipartition introduce no ownership exception.

The property `(*)` equivalence, flow corollary and private-four-cycle
augmentation remain unchanged. Their deductions were checked in the
current source: all additional cycle vertices are prescribed roots, so
restriction of a rooted model keeps the original bags inside the original
host. The eight-vertex prefix example refutes the indicated construction
and has the displayed replacement model.

## Radius theorem: strongest checks

Theorem 5.1 quantifies over every finite simple bipartite target and every
scheme with path length at most three. The distances are inside the final
branch sets and start at their original prescribed roots.

The normalisation assertion is sufficient for that stronger conclusion.
On a path of at most three edges, each endpoint of a monochromatic edge
has a monochromatic route of at most two edges to the root of that colour.
Consequently every vertex of a nontrivial monochromatic component has its
own such route, and that component contains its unique prescribed root.
A reduced nonliteral path must have odd length three; if an internal
vertex had merged into a root component, loop erasure would shorten it.
Its surviving interiors are therefore original singletons.

Every subsequent projection is a root-centred star. For a three-edge
demand `r_a x y r_b`, its selected label `x` has an actual edge to the
original `r_a`, and the base vertex `y` reaches that root through its
allocated label in two original edges. A spanning forest of a star chooses
one label for each absorbed leaf. These witnesses lie in the same fixed
preimage as the vertices they connect. Old witnesses remain available;
only root preimages grow. Thus repeated contraction, including shore
reversal, does not accumulate a radius factor.

If the old path label is omitted, the retained last edge gives a
root--root contact even when that label belongs to another root's forest
or is deleted. The same contact works when only its base vertex is
absorbed. Otherwise the two internal vertices remain singleton and the
original path persists. Existing literal root contacts survive. This
checks closure of all parts of the invariant and the final full-packing
step, not just the radius of one contraction.

In the six-vertex sharpness example, the two leaf roots share their sole
neighbour. At least one radius-one leaf bag must be singleton, forcing
that neighbour into the central bag, where it is not adjacent to the
central root. This excludes every radius-one model; the displayed
radius-two model has both required contacts. No finite computation is
a premise of the theorem or sharpness proof.

## Literature scope and remaining limits

The new qualification was checked directly against
[BLR v2, Section 1.2.2 and Lemma 3.13](https://arxiv.org/pdf/0808.0148v2).
Their depth uses diameter measured by distances in the ambient graph.
The manuscript's length-at-most-three theorem gives an intrinsic radius
bound at the roots, and does not establish the general depth assertion.
The longer proof-method obstruction is correctly omitted from this paper.

The unchanged literature discussion was compared with the existing
[scope review](citation_novelty_review.md), SHA-256
`dda2925dbb76d623369ca997048ac1a3df8299de5e764ebcc1fe53a662ffb178`,
and its [audit](citation_novelty_review_audit.md), SHA-256
`1f5d50ecf88eed6301dde9bb33207225b7aedc573f77c638da0bb540ae0fcb73`.
Those records describe their own earlier manuscript revision and primary
checks; this audit does not claim a fresh exhaustive literature search.

The external mathematical input remains the stated matroid-union formula.
No further unproved assumption was found. Publication priority, longer-path
radius bounds, significance comparable to Norin--Totschnig, HC7 and the
related unresolved conjectures remain outside this verdict.

## Compilation and rendering

For the full review before this copyedit, the auditor independently rebuilt
the source pinned above, compared its extracted text with the stored PDF,
and inspected all seven pages. That build had no warnings or unresolved
references, and those pages had no clipping or overlap.

For the current revision, the manuscript editor reports a warning-free
Tectonic build and visual inspection of all seven final pages. The present
auditor verified the final source and PDF hashes in the table and read the
editor's build record. The current rendering check is the editor's report,
not a second independent inspection by this auditor.
