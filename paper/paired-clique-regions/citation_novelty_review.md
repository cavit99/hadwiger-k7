# Focused originality and citation assessment

**Date:** 13 September 2026.
**Verdict:** the stated literature positioning is supported; originality
and publication priority remain unresolved. This is a focused internal
assessment, not external peer review or an exhaustive literature search.

## Exact package assessed

The [manuscript](main.tex), SHA-256
`3b799e0e2a02a223a41943a18f9cc2cc092057e3dbbd7b639c6faa79cbe735b5`,
combines the arbitrary-k one-sided region
theorem, its symmetric linkage equivalence, sharpness for k−1 symmetric
regions, and a polynomial construction for supplied regions. Its
[manuscript audit](main_audit.md) identifies the exact final source and PDF.
The editorial revision preserves the statements and literature claims of
the assessed source (`141cf321eb94afc108f0b4f03e7834d484dd764a8f2ceb624dccbe4c7aa0455a`).
The originating sources were checked at SHA-256:

- [Two-sided theorem](../../results/paired_clique_full_regions.md):
  `78121803cfc368cf0ff2e367d87dfc6747fbe888b0f3f5e994abdfe83ac5b8da`.
- [One-sided theorem](../../results/paired_clique_one_sided_regions.md):
  `d39271926d1cce2287de2369061b9c236a6355536bbd81b736661fbc4e6bed69`.

The mathematical content is a sufficient region criterion, with an
unspecified pairing. It does not require a proper colouring or promise
preservation of the given regions as additional bags.

## Closest inspected primary statements

[Protopapas, Thilikos and Wiederrecht, *Colorful Minors*, v3](https://arxiv.org/html/2507.10467v3#S1.SS1)
provides the appropriate terminology. Give R colour 1, S colour 2 and
all other vertices no colour. A rainbow Kk-minor then has exactly the
required terminal ownership: its k disjoint bags exhaust each k-set.
Thus the conclusion itself fits an existing framework.

Their [Theorem 3.1 and Lemma 3.5](https://arxiv.org/html/2507.10467v3#S3.SS1)
require a K4k-minor when there are two colours and the requested rainbow
clique has order k; a separator outcome is also permitted. Lemma 3.2
supplies linkages, not clique contacts. These same statements were checked
in v2; the published [ICALP 2026 Theorem 2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.149/LIPIcs.ICALP.2026.149.html)
states the broader structural dichotomy.

**Comparison deduction.** Our hypotheses permit a matching of size k
with k−1 added vertices full to all terminals. It has only 3k−1 vertices,
so cannot supply a K4k-minor. Moreover deleting R leaves no vertex of
colour 1. The stated theorem therefore cannot be invoked directly to
obtain our conclusion. This does not rule out another proof or a more
elaborate reduction from the literature.

[Böhme, Harant, Kriesell, Mohr and Schmidt, *Rooted Minors and Locally
Spanning Subgraphs*, Theorem 3](https://arxiv.org/html/2003.04011v3#S2)
produces a j-connected X-minor from local connectivity of X, for
`1<=j<=4`. Taking X to be both terminal sets retains their vertices
separately; taking X=R does not require one S terminal in every bag.
The stated conclusion therefore does not directly provide the paired
clique theorem for arbitrary k.

[Kriesell and Mohr, *Kempe Chains and Rooted Minors*, Definition 1](https://arxiv.org/html/1911.09998v2#S1)
concerns a transversal of a proper colouring and paths using two colour
classes. Our arbitrary regions and terminal linkage do not assert those
colouring hypotheses. This is relevant rooted-minor context, not an
input used by the manuscript's proof.

## Search scope and editorial conclusion

The search used combinations of “paired clique”, “rooted clique minor”,
“two terminal sets”, “linkage”, “full components”, “connected regions”
and “colorful minors”. Primary statements were read before comparing
their hypotheses. A second agent independently compared the v2
rainbow-clique lemmas and the locally spanning theorem; the manuscript
editor and parent also checked the final v3 statement used in the paper.
These checks are not independent discoveries of the region proof.

This supports developing the self-contained manuscript, with its claim
centred on the region criterion, sharpness and construction. It does not
support calling rainbow clique minors a new concept, claiming first
proof priority, or asserting a first polynomial algorithm for the
general problem. A specialist comparison with earlier rooted-clique
and linkage results, including the Robertson–Seymour antecedents cited
by the inspected papers, remains appropriate before submission.

The wheel/colouring package has not undergone this focused assessment.
No originality verdict for it follows from this review, and no
NT-comparable significance or HC7 implication is established.
