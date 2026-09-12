# Audit of the four-root linkage criteria

**Verdict:** GREEN for the two stated theorems and their exact hypotheses.
Reviewed 12 September 2026 against
[the source](four_root_linkage_with_ports.md), SHA-256
`f41f60cb657d39c9de1e19457c86d65b228607a9115e711b8c48a4d0dc92a8c1`.
This is a separate internal audit by `literature_repair`, not external peer
review. The reviewer previously checked the Section 2 scratch proof;
the general degree-sum argument received a separate reconstruction. After
the final source review, only its status line was changed to link this audit.

- **Simultaneous lift.** A clique on at most three boundary vertices cannot
  supply a new edge to each of two disjoint paths. Replacing the affected
  path segment through the connected deleted port set preserves its roots
  and disjointness. Reversing successive eliminations handles virtual edges
  without assigning one deleted vertex to both paths.
- **Degree-sum criterion.** Only removed port-to-X and port-to-root edges
  decrease the counted sum, by at most three per removed port. Original
  non-port neighbours of an X-subset remain literal neighbours. This gives
  relative boundary four; termination handles port-only subsets. The lower
  bound `2e>=6|X|+7m+3` contradicts `2e<=6|X|+6m+2` for every remaining m.
- **External input and edge count.** The inspected input is Norin--Totschnig,
  arXiv:2507.03244v1, Theorem 13. Relative boundary four excludes its
  root-free separation alternative. The Euler bound counts the graph after
  deleting root--root edges, as both proofs explicitly do; adding an outer
  four-cycle does not require an originally simple facial boundary.
- **Relaxed arm theorem.** The suppression incidence count, all four m cases,
  and the pendant-root contraction check. The pendant bridge retains the
  common face; disjoint V-neighbourhoods leave at most one new root--root
  edge, giving the required bound of twelve. The two-vertex endpoint has
  the asserted opposite V owners and exact disjoint carriers.

No unresolved inference was found within these statements. The V path may
use other ports; the arm endpoint is existential. No outer allocation,
colouring-preserving reduction, full three--two linkage theorem, or C19/HC7
closure follows merely from this audit.
