# Internal manuscript audit

**Status:** separate internal mathematical audit; not external peer review.
**Verdict: GREEN.**
**Date:** 8 September 2026.

**Exact source checked:** [main.tex](main.tex), whole-file SHA256
`6d804a715f8782ac84679a8a5715105cb28d2a7cf4a594c60aec5b1072b387b9`.

The auditor, a separate agent from the manuscript editor, read the whole
revised source and its diff against the previous manuscript. The auditor
had previously reviewed the underlying argument and supplied pre-edit
spot checks of the quotient sequence and vertex count; this was not a
blinded review or an independent discovery of the proof. The full reading
covered hash `ad42f119b9df851718e631ac3f3b5976a33e61032e12ad0d52cb5cb7910c698b`.
Reversing only the final clarification to "nonempty collection" and the
proof-mark command exactly recovers those bytes, so the verdict applies
to the final source above.

The [underlying theorem](../../results/bipartite_contractibility_via_matroid_reduction.md)
was reread and its source hash checked:
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`.
Its two adjacent audits retain their separate provenance. The previous
manuscript audit is preserved at Git revision `80ebbd2`, at this same
path; it checked manuscript hash
`8cea0ca4838a7090b5fb4798c2c9ec670efe60017a6f7df1e79dc0d668c0b701`
and PDF hash
`138e3da77020b7900641c8a2d0663afd9d6515297d04504387fc749c76627c87`.
Those historical checks are not silently transferred to the new PDF.

## Mathematical checks

Normalisation retains every root and turns each original path into a
path using its endpoint colours. Matroid-union equality holds for any
maximising disjoint forest family and any minimising set, forcing all
the required component-spanning forests simultaneously.

The decisive quotient sequence is valid even when a label belongs to
several projections and is allocated elsewhere. Its original occurrence
is omitted, while its two adjacent A vertices have the same component
image. Only edges from original A vertices to surviving B vertices are
retained. The allocated trees provide fixed disjoint connected preimages;
no foreign owner's label is traversed or reused. Loop erasure introduces
no foreign root and preserves the scheme intersection condition.

The exact count
`|V(G)|-|V(Q)|=|X|+sum_a r_a(X)` applies to Q as defined, before any
additional vertex deletion. It gives strict descent for nonempty X.
The full-rank case supplies the required rooted model directly; otherwise
the same target recurs on a smaller host. Isolated roots, zero-rank cases,
reversal of the bipartition and composition of the fixed preimages are
all covered.

Property `(*)` was checked against
[Kriesell--Mohr, Definition 1, v2](https://arxiv.org/pdf/1911.09998v2).
Selected bichromatic paths form a scheme, and normalisation proves the
converse implication, including isolated target vertices. The stated
equivalence and its bipartite consequence therefore hold.

The flow corollary correctly excludes foreign internal terminals using
minimum degree two and bipartiteness. The private-four-cycle construction
also checks: every added vertex is another prescribed root, so the old
bags and their contacts lie entirely in the original host. It removes
the degree restriction from the earlier intended rooted assertion.

In the eight-vertex example the BLR right sets overlap, whereas the four
displayed replacement bags are disjoint, connected, contain their named
roots and have all four required cross-contacts. The negative claim
concerns the prefix construction, not minor existence.

## Historical scope and limits

The BLR and Lee discussion is consistent with the separately audited
[scope review](citation_novelty_review.md). The auditor also inspected
[Kolbe--Spalding-Jamieson, Lemma 3.11 and Proposition 3.4](https://arxiv.org/html/2608.27179v1)
and [Korhonen--Lokshtanov, Lemmas 4.3--4.4](https://arxiv.org/pdf/2308.04795v1).
These support the manuscript's specific bounded-degree demand-graph
route to unrooted clique minors; that route is not stated as universal
rooted bipartite contractibility. No new downstream estimate is claimed.

No unresolved proof hypothesis or mathematical gap was found beyond the
stated external matroid-union input. This audit does not establish first
correct-proof priority, exhaustive absence of other proofs, significance
comparable to Norin--Totschnig, or an implication to HC7. External peer
review has not occurred.

## Compilation and rendering

The manuscript editor (the parent agent), separately from the mathematical
auditor, reports that Tectonic compiled the final source without warnings,
overfull or underfull boxes, or undefined references. The editor inspected
all five final pages: mathematics and citations are legible, with no
clipped or overlapping text.

The mathematical auditor independently checked the copied
[PDF](main.pdf) file's SHA256:
`1e8d07ee6aedf7dbbf5d5c3c874957a1cffcbcf6e029407f676af0e0051001d8`.
The visual-inspection verdict above is the editor's, not a second claimed
render review.
