# Audit: four-clique contacts and the nonplanar complement

**Verdict: GREEN.** Separate whole-source internal mathematical audit of
[the construction and contact bounds](hc7_four_clique_complement_contacts.md),
reviewed on 9 September 2026 at SHA-256
`945cfac070104f2b0994fcb6dcfafcc04fa32cbe22cbafb81ab2eac4c0b8d83a`.
No unresolved gap was found in the stated results or their application.
This is not external peer review or a global completion claim.

## Inputs and provenance

The parent authored the source. This reviewer checked the initial
eight-bag construction, supplied the proposed six-pair table and direct
fifth-root strengthening, then separately read every line of the parent's
frozen consolidated proof. This is an exact-source check, not a claim of
independent discovery or another reviewer's approval. The earlier audit
covered source `e9d9f16502e18b9cc0830615dd1887553328fdf96a583ede26a36adab01f011d`.
The invoked statements and audits were reread for that review; the
following whole-file hashes were rechecked and are unchanged:

| Input | Source SHA-256 | Adjacent audit SHA-256 |
| --- | --- | --- |
| [NT Theorem 8 statement](hc7_five_root_almost_clique.md#external-input) | `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd` | `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47` |
| [Five-root wheel](hc7_rooted_wheel_extension.md) | `f72e0b3d4254724a58f55b9445c0c173ea6c96e535416da47b1efc7fd5eb43b3` | `c93612165de23798c63922425fbd8d9e74407d2eb1a85b365853bd1343969178` |
| [Complement four-connectivity](hc7_two_triangle_complement_four_connectivity.md) | `0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69` | `d074cc7eb384222f1b68ed53728fd721c7a6e7edbf266c55cec313a5c73b2014` |
| [Clique-deletion colour bound](hc7_clique_deletion_colour_bound.md) | `dd39ad7bf84d4bf698757e8bc7dbadec987356c4eb53593d41c5478129573a84` | `3ba97a173c20e065665ef49b537cebcc3c0a9033ec752d3f5694bac56f85e742` |
| [Contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md#3-a-contact-restriction-beside-a-literal-four-clique) | `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4` | `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394` |
| [Existing four-root side lemma, Lemma 1](hc7_two_triangle_exterior_helpers.md#1-a-four-root-packet) | `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8` | `e9bc147d6c0e48bba395dc5fe590ef8a8cc778914804e3c1f5d33c48e2eec628` |

The wheel's second audit was also checked at
`677aac154e49ddc1736ba45b8961aa4d9478ec641f4088f83f2d991185bce2d7`,
and the complement's second audit at
`113eddbfd2af4cac9e7196691accb22c74ff6084d984aaaf117bb190bce16d4d`.
The quoted NT alternatives and the existing primary-source audit suffice;
no fresh literature inspection is claimed. The actual-host application
also uses the four-colour theorem in its ordinary planar form.

The revised source adds the existing side lemma to the previously checked
`0365c0939108108aced0fad9d5bc8c7a0df90fc64ad198e80f757192deffae6d`
revision. Its exact lemma and audit were read. This review caught an
incorrect claim that the old-R torso could lose four-connectivity; the
parent corrected it before the present GREEN revision. No added primary
inspection is claimed.

**Separate whole-source review.** Route-assessment independently returned
GREEN on 9 September 2026 for the same final source hash, with no gap or
source edit. That reviewer had participated in the earlier contact-count
and nonapex checks and reconstructed the existing relative-root lemma
before deduplication, but did not supply the six-pair table or direct
fifth-root strengthening. The complete source, relevant four-root lemma
and audit, and all six input source/audit pairs were checked. In particular,
the quarter-turn action on owner indices is `(i,j) -> (j+1,i+1)` modulo
four: its four orbits from the table rows cover all sixteen assignments.
This is a separately attributed internal review, not external peer review.

## Strongest checks

- **Exactly one retained full bag.** Work in the eight-bag contact minor
  and delete one triangle adjacency at every other full wheel vertex.
  This is a legitimate weakening; all originally missing labels remain.
  An absent label makes its triangle vertex and the merger of the other
  two full to the wheel. Otherwise all three labels occur among the four
  nonfull vertices. With full hub, the repeated rim label is either on
  adjacent or opposite vertices; in both cases the stated rim matching
  exists. With full rim, the four displayed equality cases exhaust failure
  of both choices. Each selected merger gives a K4 and leaves only two
  possible cross holes with distinct ends in both cliques.
- **The six-pair table exhausts the assignments.** Connected spanning
  extension of the initial four bags assigns both extra markers, even
  when they were already used, without changing the four prescribed roots.
  The four rotations of the square generate four distinct assignments
  from each row; quarter turns also exchange the two diagonal labels.
  These four sets partition all sixteen assignments. The two adjacent
  rows are not claimed to be different full-dihedral orbits. Directly
  taking the union of each merged pair verifies every listed contact:
  mixed R/core mergers are universal, while the opposite core merger
  is full to R. All listed holes are independent. Additional contacts
  of the six markers or other bag vertices only strengthen the model.
- **Arbitrary five-root extraction.** NT's trisection separates nonempty
  open root sides by two vertices. Its other separation has nonempty
  open sides and order at most three. Four-connectivity excludes both;
  nonplanarity excludes the plane alternative. The wheel theorem then
  applies to any five distinct vertices of F, including when the fifth
  already belongs to the four-root model. No hub or rim order is fixed.
- **Part 1 has no hidden upper contact bound.** The two nonempty parts
  of the literal clique are disjoint, connected and adjacent. Five
  vertices meeting both yield the required two full bags over one wheel.
  For the counting consequence, any chosen pair of R-neighbours is
  separated in two of the three balanced partitions. Vertices with three
  or four R-neighbours are counted in all three, so they cause no exception.
- **The first-hit path preserves ownership.** The path starts at the
  unused fourth clique vertex in G-S and stops on the wheel union.
  Its interior avoids all wheel bags and S. Adding it to the hit bag
  retains every old contact and supplies all three S contacts through
  that fourth vertex. No other bag or root is consumed.
- **The strengthened triangle bound uses a distinct fifth root.** Five
  neighbours in F of the remaining clique vertex supply one outside any
  four proposed S-double vertices. Its wheel bag absorbs that clique
  vertex along their actual edge; the other four rooted bags retain two
  S contacts each. This degree hypothesis also makes G-S connected.
- **Six high-contact vertices force six different pairs.** Each vertex
  with two R-neighbours contributes to two triangle counts; one with
  three or four contributes to all four. Bounds of three on the four
  counts force exactly two neighbours per vertex and equality in every
  count. The resulting pair multigraph has degree three at all four
  vertices. The three opposite-pair multiplicity sums are at least two
  by the balanced cuts and total six, so each is two. Equal degrees
  give equal multiplicities on opposite edges, hence all six are one.
  The six-pair lemma then applies. No extra R-degree assumption is
  silently imposed in this argument.
- **The planar deficit is applied to actual degrees.** A degree-six
  vertex of F has at least two R-neighbours by its degree in G. After
  deleting u, the remaining graph has at least six vertices and minimum
  degree five. Euler's inequality forces at least twelve degree-five
  vertices there. Each has degree exactly six in F, contradicting the
  bound of five. Vertices of degree at least six contribute nonpositively
  to the deficit, so no equality or triangulation assumption is needed.
- **The side replacement retains a four-connected torso.** For a component
  C of F-S, every nonempty subset of C retains its full boundary and every
  C vertex its degree in F[C union S]. The explicit degree-six hypothesis
  permits the existing four-root lemma. Its four disjoint S-rooted bags
  simulate every added S edge while retaining the old R. Completing S on
  the opposite side preserves four-connectivity: any component away from
  surviving S after at most three deletions would already be cut off in F.
  An opposite component is full to all four S vertices, so its contraction
  gives K5 and proves nonplanarity. Part (1) therefore reapplies. Distinct
  R-neighbours can coalesce, degrees at S can fall, and no ordinary
  colouring response is retained; the stronger bounds are not iterable.

In the actual host, all cited structural hypotheses hold for either
triangle choice. The clique-deletion bound gives chi(F)>=5, sufficient
for nonplanarity; chi(F)=6 is allowed. Contraction closure gives at most
two R-neighbours and hence delta(F)>=6. Seven-connectivity gives G-S
connected. No colouring of F or minor retaining its chromatic number is
selected in the construction. Revised Part 3 assumes delta(G)>=8 for
all vertices, including R; this supplies the five F-neighbours required
at each clique vertex and justifies the improved bound of five.

Finite exploration is not a dependency of the hand proof or this audit.
The results bound possible attachments and exclude planar vertex deletions;
they do not force a global compatible model or close C19, HC7, or the
user's comparable-theorem objective.
