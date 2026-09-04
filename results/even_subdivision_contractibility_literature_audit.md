# Separate proof and literature audit: even subdivisions

**Status:** separate internal audit; not external peer review.
**Reviewed source:** [theorem](even_subdivision_contractibility.md).
**Whole-file SHA-256:**
`e7e8499d03f440f81bf558f7d42bc6be09830dd68a4bba50b92e1df4e1332ef7`
**Date:** 4 September 2026.
**Mathematical verdict:** GREEN for Theorem 1.1, Lemma 2.1 and Corollary 1.2.
**Citation verdict:** GREEN. **Novelty verdict:** QUALIFIED GREEN.

## Mathematical check

The proof was checked independently against the primary source definitions.
In each projection, every component away from its distinguished root meets
at least two prescribed paths. Deleting labels outside `X` bounds the total
number of path-component incidences by `m_j+|E_j-X|`, including trivial paths.
Thus the rank deficit is at most `|E_j-X|/2`. Each label occurs in at most
two projections; summing gives precisely the arbitrary-family matroid union
inequality. Equality of the union rank with the sum of the individual ranks
forces pairwise disjoint bases. Adding matroid loops outside `E_j` is valid.

In the application, a nonroot of a degree-two `B` colour lies on both
incident scheme paths and supplies one projected edge at each of its two
distinct `A` neighbours. Every nonroot of an `A` colour lies on at least
two of that projection's paths. Degree-zero and degree-one colours, empty
label sets, parallel projected edges and disconnected targets cause no gap.
Isolated roots are removed before the reduction and restored disjointly.
The lifted trees connect all vertices of each `A` colour, and each literal
`B` root retains its required adjacency through the final scheme-path edge.
Singleton `B` branch sets are asserted only after the coloured reduction;
composing rooted minor models correctly allows larger original branch sets.
The positive-even-path-length corollary follows by alternating parity along
each replacement path. No finite search or unstated preservation is used.

**Unresolved mathematical assumptions or gaps:** none in the stated scope.

## Exact external inputs

- Kündgen--Pelsmajer--Ramamurthi,
  [primary preprint](https://arxiv.org/html/1207.6141): Definitions 1.1,
  2.1 and 3.1; Remark 3.2(1), (2), (6), (7); Lemma 3.3. These give the
  scheme semantics, alternating edge-disjoint paths, minimum path
  multiplicities and the root-preserving coloured reduction used here.
- Edmonds' matroid union rank formula is the only packing input. Besides
  the theorem's 1970 reference, Edmonds' own introduction to the reprint of
  [*Matroid Partition*](https://www.researchgate.net/profile/Jack-Edmonds-2/publication/226200830_Matroid_Partition/links/0deec51d1e5ee4de7b000000/Matroid-Partition.pdf),
  Theorem 1 and the following discussion on pp. 202--203, explicitly give
  `min_{X subseteq E}(|E-X|+f(X))` and identify the independent sets when
  `f=sum_j rho_j` with unions of independent sets of the individual
  matroids. This primary-source text was opened and checked. The original
  *Matroid Partition* appeared in *Mathematics of the Decision Sciences*,
  Part 1 (1968), pp. 335--345.

## Novelty and question scope

The theorem extends the repository's earlier two-projection `K_{2,n}`
proof by allowing arbitrarily many partially shared projections. It answers
the `K_{2,4}` part of KPR Section 8, Question 2 and the part of Question 3
where the three theta paths all have even length. In KPR's
`theta(k,l,m)` notation these are the cases with `k,l,m` all odd. It does
not settle the three odd-length paths case, `K_{3,3}`, or all bipartite
graphs. Their Theorem 7.10 concerns different parity patterns and supplies
no counterexample to this theorem.

Targeted searches through 4 September 2026 located no source proving this
class. The positive classes in [Kriesell--Mohr](https://arxiv.org/html/1911.09998v2)
and the 2025 [Arsenyan thesis](https://dspace.cuni.cz/bitstream/handle/20.500.11956/202604/130435869.pdf?isAllowed=y&sequence=1)
do not state this theorem. This bounded literature review is not a priority
certificate; specialist confirmation remains outstanding.

The family has unbounded treewidth and contains a subdivision of every
finite simple graph. This is a substantive independent theorem, but it
does not close a T44 subcase, Conjecture 21 or `HC_7`, and this audit does
not certify significance comparable to Norin--Totschnig's colouring result.
