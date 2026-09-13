# Citation provenance and originality scope: structural manuscript

**Status:** bibliography and primary-statement checks for the expanded
13 September 2026 draft; focused originality assessment incomplete.
This note is not a separate mathematical audit or a publication-priority
certificate. The exact source and PDF revision is pinned in
[main_audit.md](main_audit.md).

The previous compact draft's citation review and qualified novelty verdict
remain preserved at Git revision
`f7b52aff0dfb2578bc30ade68f75df12671cf966` in this directory. That review
covered source hash
`461e7433e0b2695ead1d0a3f46724f32989b880389a75ba89bcbecbd219e59fa`
and a literature cutoff of 9 August 2026. Its verdict does not extend to
the new connectivity and defect or separator theorems.

## Citation checks for this revision

The fourteen bibliography entries are used, all citation keys resolve, and
the rebuilt PDF has no citation or reference warning. The original ten
references retain their earlier roles: Hadwiger and Robertson–Seymour–Thomas
for context; Albar and Norin–Totschnig for the colouring problem;
Mader and Dirac for contraction-critical hypotheses; Kriesell–Mohr and
Norin–Totschnig for the rooted inputs; Rolek–Song and Mayer for precedent;
and Jakobsen for the extremal threshold and cockade exception.

The expanded arguments make the following additional dependencies explicit:

- [Rolek–Song–Thomas, Lemma 2.1](https://arxiv.org/html/2208.07335v2):
  an eight-vertex graph with independence number two contains a `K4` or
  their spanning square-antiprism graph `H8`. The manuscript invokes this
  unrestricted local statement, not the ambient hypotheses of their main
  theorem. Independence number one already contradicts `K4`-freeness.
- [Wood–Woodall, Lemma 4.2.1](https://doi.org/10.37236/181):
  the classification of three-connected graphs with no `K5^-` minor as
  wheels, the triangular prism and `K3,3`. The exact input is also checked
  in the retained [triangle-poor-edge audit](../../results/hc7_k7minus_degree_eight_triangle_poor_edge_packing_audit.md).
- [Norin–Totschnig, Theorem 13 and Claims 3.12–3.15](https://arxiv.org/abs/2507.03244):
  the degree-six two-paths argument is adapted with an explicit audit of
  its forbidden-minor and connectivity hypotheses. This does not assert
  that their whole theorem holds after replacing the forbidden graph.
- [Humeau–Pous, Theorem 1.3 in PDF version 2](https://arxiv.org/pdf/2505.16431v2):
  a graph with a frame cycle is a web precisely when it is maximally
  crossless at that frame. The manuscript first adds the safe frame edges,
  takes a completion on the same vertex set, and excludes nonplanar cells
  by an actual cut of order at most six.
- [Diwan, Corollary 1](https://arxiv.org/html/2306.04944v1):
  extension of a proper induced-cycle precolouring of length at most
  `2k-5` using at most `k-1` colours. The application uses `k=5`, a
  four-cycle and at most three colours from the five-colour palette.

Rolek–Song–Thomas's statement, Humeau–Pous's web statement and Diwan's
precolouring statement were inspected in their primary versions for this
revision. The other previously checked inputs retain their pinned source
and audit provenance in [README.md](README.md). The mathematical manuscript
audit separately examines the application of these statements.

## Originality and significance

The candidate contributions for a focused originality assessment are the
combined necessary conditions for a critical host, the broad
`D(G) >= 20 + r` connectivity and defect theorem and its finite quotient
reduction, and the computation-free seven-cut closure. The all-`r`
linked-cliques theorem and the fifth-root placement lemma are retained
from the earlier package, with their documented precedents.

The new numerical bound is presented with its full proof chain and finite
trust boundary. It is not, by itself, a colouring theorem. Neither the
manuscript adaptation nor the existing internal audits establish that the
expanded package is original in the literature or comparable in reach to
Norin–Totschnig's global colouring theorem. Those assessments need a
focused literature comparison and independent specialist review.
