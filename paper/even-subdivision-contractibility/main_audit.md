# Internal manuscript audit

**Status:** separate internal audit; not external peer review.
**Reviewed source:** [main.tex](main.tex).
**Whole-file SHA-256:** `abdc8dc0e1cae250eb300cabdebc7f046adab230e9c0610bdbaf95b4e341a68f`.
**PDF SHA-256:** `92352b99c66baa15cc44212066d793d5a8423313f998dda9c025b2e614ebb8a0`.
**Date:** 5 September 2026. **Verdict: GREEN.**

This replaces the manuscript audit for the four-page revision with source
hash `ffbe81816284caafaffe039f6a61533e958b25db55c792c75ae282055b8e97f9`,
preserved in Git at `bec6d3f`. The original packing and degree-two proof
text is unchanged. The new material is the degree-three extension and a
qualified literature discussion.

The reviewing root agent read the complete manuscript independently of the
agent that transcribed it. The theorem, auxiliary packing lemma and even
subdivision corollary agree with the
[audited proof](../../results/even_subdivision_contractibility.md), hash
`e7e8499d03f440f81bf558f7d42bc6be09830dd68a4bba50b92e1df4e1332ef7`.
The component count includes isolated components and trivial paths;
matroid union gives disjoint bases on the common ground set. Actual vertex
labels occur in exactly two projections, trees lift to disjoint connected
branch sets, and the rooted reduction composes without asserting singleton
branch sets in the original host. Isolated target vertices are restored.
The positive-even-path corollary permits parallel original edges.

The new Lemma 4.1 and Theorem 4.2 agree with the independently audited
[degree-three proof](../../results/degree_three_bipartite_weak_contractibility.md),
hash `72e52cdcb734bd5620e4c3d6cc3bdd29d7861563bc9ba2507ff39d1c6c2d609d`.
Projection labels are defined by actual path occurrence. The relocation
changes only a root in the degree-bounded shore, deletes the previous
root from every path, and strictly lowers host order after normalization.
It preserves all roots in the opposite shore. No lift is claimed to
preserve relocated roots.

The eight-vertex BLR example and the intended-versus-printed intersection
qualification agree with the [audited construction note](../../barriers/bipartite_flow_prefix_construction.md).
The manuscript refutes the supplied prefix construction, not the intended
main existence statement or any spectral conclusion. Publication priority
remains expressly qualified.

The manuscript retains the exact external inputs and makes no claim of
full rooted `K_{3,3}`, universal bipartite contractibility, Hadwiger's
conjecture, publication priority or comparable significance. The
transcription agent compiled all five pages with cached Tectonic and
visually inspected them; compilation had no layout or reference warnings.
The root auditor separately checked the added proof and final two pages.
This is a layout check, not proof evidence.

**Unresolved mathematical assumptions or gaps:** none within the stated
scope. Novelty and significance remain subject to specialist assessment.
