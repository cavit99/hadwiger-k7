# Independent internal audit: even subdivisions are contractible

**Status:** separate internal mathematical audit; 4 September 2026.
**Verdict:** GREEN for Lemma 2.1, Theorem 1.1 and Corollary 1.2.
This is an internal agent audit, not external peer review.

## Exact revision

Audited source: [even subdivisions are contractible](even_subdivision_contractibility.md).
SHA256 of the complete source file:

```text
e7e8499d03f440f81bf558f7d42bc6be09830dd68a4bba50b92e1df4e1332ef7
```

The earlier draft was independently checked before promotion. The promoted
revision changes its status, a relative link and the isolated-root handling;
the latter now explicitly removes those roots before the coloured reduction
and restores their singleton branch sets. These changes preserve the proof.

## Cold mathematical checks

1. **External reduction.** Checked Definitions 1.1 and 2.1, Lemma 3.3 and
   Remark 3.2(1), (2), (6), (7) in the
   [Kündgen--Pelsmajer--Ramamurthi primary preprint](https://arxiv.org/pdf/1207.6141).
   They supply exactly the rooted reduction, proper colouring, alternating
   paths, unique edge ownership and two-path membership used here.
2. **Projection construction.** Every nonroot of a degree-two `B` colour
   lies on both incident paths, producing one edge in each corresponding
   projection. Simple scheme paths exclude auxiliary loops. Parallel edges
   remain legitimate graphic-matroid elements with distinct labels.
3. **Coverage.** The projected paths cover every `A_a` vertex and contain
   `a`. Removing terminal `b` removes no `A_a` vertex. Each nonroot in
   `A_a` belongs to at least two distinct projected paths, including when
   it is an endpoint of a projected path.
4. **Component inequality.** For every `X`, the root component meets all
   prescribed paths, and each other component meets at least two. A path
   meets at most one more component than its deleted-edge count. Summing
   these counts counts each deleted label once in a given projection.
   Thus (2.1)--(2.2) hold with isolated components included.
5. **Simultaneous packing.** Matroid loops outside `E_j` give the stated
   ranks on the common ground set. Every deleted label contributes to at
   most two projections, establishing (2.3) for all `X`. The matroid union
   rank formula yields the full sum of ranks. Equality forces disjoint
   bases simultaneously; no independent existential choices are combined.
6. **Rooted lift.** A tree label lifts to an actual two-edge path. Distinct
   bases use disjoint nonroot `B`-colour vertices. Colour classes and roots
   are disjoint, and each required adjacency is witnessed by the last edge
   of its scheme path. Composing the rooted minor models preserves all four
   requirements: connectivity, disjointness, root containment and adjacency.
7. **Small cases and corollary.** Empty ground sets, an empty index family,
   trivial projected paths, isolated roots and degree-one roots are valid.
   For a positive even-length replacement path, the alternating partition
   places every odd-position vertex in `B` with degree two. Disjoint new
   interiors make parallel original edges harmless and the target simple.

## Assumptions, reach and unresolved issues

No unresolved mathematical gap was found. The external inputs are the
stated coloured-scheme reduction and the standard finite matroid union rank
formula; neither is re-proved here. No finite computation is used as proof.

The theorem extends the two common-label projections for `K_{2,n}` to an
arbitrary number of partially overlapping projections. Once-subdivisions
of arbitrary cliques establish unbounded treewidth of the target family.
Contractibility of the unsubdivided graph does not follow. The proof does
not cover all bipartite graphs or all bipartite theta graphs, and proves
neither T44, Conjecture 21 nor `HC_7`. Novelty, publication priority and
comparability with Norin--Totschnig are outside this audit's verdict.
