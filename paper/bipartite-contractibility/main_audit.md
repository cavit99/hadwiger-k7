# Internal manuscript audit

**Status:** internal manuscript audit; not external peer review.
**Verdict: GREEN.**
**Date:** 5 September 2026.

**Exact manuscript source checked:** [main.tex](main.tex), whole-file SHA256
`8cea0ca4838a7090b5fb4798c2c9ec670efe60017a6f7df1e79dc0d668c0b701`.
**Rendered PDF checked:** [main.pdf](main.pdf), whole-file SHA256
`138e3da77020b7900641c8a2d0663afd9d6515297d04504387fc749c76627c87`.

The root agent read the complete manuscript independently of its
transcription agent, checked its mathematical content against the
[theorem source](../../results/bipartite_contractibility_via_matroid_reduction.md),
whole-file SHA256
`3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`,
and inspected all five rendered pages. This is a manuscript and
transcription check, not an additional cold audit of the originating
research. The separate theorem audits are linked beside that source.

Theorem 1.1 matches the universal rooted statement. Lemma 1.2 proves the
needed colour normalization directly. Lemma 2.1 correctly extracts
simultaneous component-spanning forests from equality in the finite
matroid union rank formula. In Lemma 3.1, discarded-label traversals are
replaced inside the specifically allocated component preimages; no label
is restored through a different component's owner. The quotient paths
retain their endpoint colours and all roots, and the final model lifts
through fixed disjoint connected preimages. Nonempty minimizing sets
give a strict decrease in host order, with shore orientation allowed to
change at the next step.

Corollary 5.1 verifies both the common-endpoint intersection condition and
the exclusion of foreign internal terminals under the minimum-degree-two
hypothesis. The manuscript distinguishes the intended BLR intersection
convention from the apparent reversal in the published display. Its
eight-vertex example agrees with the separately audited prefix-construction
barrier, and the new proof does not rely on that construction. The KPR
question scope is stated without asserting publication priority.

Tectonic compiled the final source without warnings. All five pages have
legible equations, references and page numbering, with no clipped or
overlapping content. The original even-subdivision, degree-three and
earlier manuscripts were not edited.

**Unresolved mathematical gaps in the checked transcription:** none found.
External specialist review, publication priority and comparison with
Norin--Totschnig remain outstanding. No implication to `HC_7`, T44 or
Conjecture 21 is claimed.
