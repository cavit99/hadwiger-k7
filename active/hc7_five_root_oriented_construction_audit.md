# Audit of the prescribed-full-root constructions

**Verdict: GREEN for the written deductions; the orientation target remains
conjectural.** This is a separate internal whole-file review, not external
peer review, a novelty assessment, or a proof of Conjecture 19 or HC7.

## Exact source and provenance

The current audited [source](hc7_five_root_oriented_construction.md) has SHA-256
`167cb695687da0c6702116b1025f3092d743e7c76923d54ef371c4396da4fe5f`.
The complete review below covered the predecessor
`8c66d44544b0b889c215dbdeb46e09cb503da95b617c7db3cce1fa0451b887f3`;
the final addendum separately audits the new Section 6 and revised scope.
The complete mathematical revision was read at SHA-256
`9ce55584cccb71ba421358187a2bfcb1290b3b88ee8619dbee3e18f37b4260d1`.
Replacing only the final audit-status sentence by its pending wording
recovers that draft exactly. The source was not edited by this audit.

The reviewer previously checked several constructions during development
and supplied the corrected three-nonroot endpoint in the anchored-deficit
lemma. Those mathematical exchanges were not a whole-source audit.
This verdict follows a subsequent complete reading, including the new
two-planar-response proof in Section 5 and its original-graph lift.

These input hashes were checked against disk, and the invoked statements
and adjacent audits were reread:

- [Degree-six five-root theorem](../results/hc7_five_root_degree_six.md):
  `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`;
  [audit](../results/hc7_five_root_degree_six_audit.md):
  `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
- [Recorded NT Theorem 8 and port argument](../results/hc7_five_root_almost_clique.md):
  `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`;
  [audit](../results/hc7_five_root_almost_clique_audit.md):
  `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.

This review uses the recorded primary inspection. No fresh literature
inspection or finite-computation premise is claimed.

## Strongest inference checks

1. **Minimum counterexample and five ports.** The outside linkage uses
   every original root and every boundary port once, with trivial paths
   permitted. First-port truncation prevents internal vertices of the
   paths from contacting the smaller side. Added root-triangle edges
   supply only interbag contacts and lift through the original root edges;
   they are not assumed to make the augmented side a minor. Nonroot order
   strictly decreases, and the prescribed full c label is retained.

2. **Unrestricted anchored defects.** Both two-nonroot cases and the
   corrected three-nonroot common-port cases have connected, disjoint bags.
   Thin-root and paired absorptions preserve every surviving degree and
   the adjacency of each degree-five exception to c. With d exceptions,
   the two facial inequalities give `k_c+k_b+k_B1<=d+2`, while the anchor
   and root normalization give at least `d+4`. No bound on d is used.

3. **The complete b-star.** The component containing a surviving c
   neighbour has an actual boundary in the displayed seven-set. Each
   possible missed B root has the stated fixed-preimage repair. In the
   endpoint case `N_D(c)={p,q}`, minimality forces the edge pq and the
   two degree-six endpoints before the simultaneous contraction; old c
   has no surviving nonroot neighbours, so the boundary loses at most one.

4. **Spanning responses and literal contact.** The maximal helper union
   has two actual ports. Its proper old nonroot part would have at most
   five neighbours, whereas the empty case is the excluded common-port
   configuration. Thus the other two root bags really are singleton.
   The rooted-triangle construction checks deletion of every vertex and
   keeps the entire old c helper in its new c bag. Different responses
   are never assumed to share bags or to have compatible ownership.

5. **The two planar responses.** After contracting bp, all degree-five
   exceptions miss Bj and Bk. The trisection cannot have two isolated
   roots of degree at most two. A thin c still has its new cb* edge, and
   Bi has two literal root neighbours; these facts justify actual
   two-connectivity before treating the facial boundary as a cycle.
   Equality forces `k_b*=d` and `k_c=k_Bi=1`. The safe cp contraction
   then forces the edge pq and the degree-six common neighbour q, which
   misses Bj,Bk. With four root edges the required root four-cycle does
   not exist; with three, the sole nonroot on the face would have to be
   q adjacent to Bk. Both contradictions use the same unchanged graph.

6. **The final lift is an actual separator argument.** The lifted helper
   nonroot set explicitly contains p. Its boundary consists of old b,c,
   Bj and at most two individual old port vertices, rather than two large
   bags. It therefore spans all old D. Connectivity of `J-{b,p}` proves
   that contracting bp preserves the two-connectivity needed for the
   last rooted triangle, and the actual pBi edge supplies the extra
   b contact on lifting.

## Scope

The source proves the anchored diamond lemma and the stated necessary
conditions on a minimum counterexample, including that b and all its
nonroot neighbours miss B. It does not prove the prescribed-full-root
target, justify repeated root growth, or close the critical seven-boundary
application. The latter may still have three possible missing pairs,
as the source explicitly records. No unresolved gap was found in the
written deductions at the pinned revision.

## Separate audit of the paired-contraction addition

**Verdict: GREEN.** Removing the new 116-line Section 6, restoring the
former scope wording and renumbering Section 7 recovers `8c66d445...`
exactly. The earlier complete-source review remains the provenance for
all unchanged deductions. A second reviewer read the complete addition;
that reviewer had spot-checked the replacement and supplied the displayed
counterexample, but did not author this section.

The four-root packet checks its universal two-nonroot base, both strict
absorptions, the preserved anchor edge and the impossible one-nonroot
endpoint. Its cofacial inequality gives `K<=delta+2`, while the two
anchor incidences and two other normalized roots give `K>=delta+4`.
The disjoint contractions cannot both lower one nonroot degree; every
four-boundary side contains both anchors. Submodularity excludes overlap
of maximal sides, and losing their cross-ports excludes adjacency.
Their fixed models share only actual ports, whose unions preserve all
labels and outside edges. Adding every incident removed side lifts any
alleged torso four-boundary to a larger old bad set. Newly weak ports
see both anchors; exclusive-b exceptions retain the stated nonadjacency.
The small or empty torso endpoints and the refined terminal class remain
open. The explicit two-nonroot example refutes only the looser class.
No repeated contraction, orientation theorem or global closure follows.
