# Audit: colourful unions of two triangles

Date: 21 September 2026.

**Verdict: GREEN for the stated conditional reduction.** The reviewed
[source](hc7_two_triangle_colourful_reduction.md) has SHA-256
`f82ab1b68dd04ff2cae5a95628a5ba1d680a81933e49ced1b63ff88f48f79534`.
Sections 1--6 were reviewed at the earlier hash recorded below; the final
section records the separate review of the appended Section 7.
No unresolved inference was found in that reduction. The four-connected
terminal statement is not proved, and neither the exceptional degree-seven
case nor `HC_7` follows without an additional argument.

## Strongest checks

- The preliminary cut reductions never increase the number of marks. If
  six survive, every old mark has a different surviving preimage. A
  triangle with a vertex in a discarded open shore would have its three
  marks represented by at most two ports, so this cannot happen. Thus the
  literal triangles survive every preliminary step with six marks.
- At five marks, their disjoint preimages contain five distinct original
  marks. These necessarily split three-plus-two between the original
  triangles. Restoring their clique edges is a legitimate minor operation
  with the same preimages. It preserves colourability because a colourful
  five-set is rainbow in every proper five-colouring. The Kempe swap
  argument concerns this same fixed colouring; it gives all missing
  routing edges, and their graph is a subgraph of `K_{3,2}`.
- The three port carriers exist even when the opposite triangle meets the
  separator: take the common vertices as trivial paths and apply Menger
  to the remaining terminals. A failed linkage plus those common vertices
  would separate a surviving triangle vertex from the nonempty opposite
  open shore with fewer than three vertices. Each carrier gets a distinct
  opposite triangle mark, and the triangle edges join every carrier pair.
- The symmetric quotient argument for one or two separator colours is
  valid. Merging equal-coloured carriers uses actual triangle edges, and
  all surviving ports form a clique. Permitted quotient colourings expand
  to the original shores with exactly the same separator equality
  partition. Every port colour is old, so a permutation of the four old
  colours aligns them. Their union would be a permitted colouring of the
  original graph. Thus one quotient is colourful; with at most five marks
  it reaches the valid five-mark exit. No simultaneous extension of a
  colouring inside the contracted carriers is asserted or needed.
- For an unmarked shore, the fixed ordinary colouring certifies each
  selected quotient. A permitted colouring extends over that shore by a
  permutation of its original ordinary colouring. Port colours may
  include the special colour when a port is unmarked; using all five
  colours for this permutation is legitimate because the removed
  interior contains no marks.
- The no-rooted-triangle alternative for an arbitrary connected full
  unmarked component is sound. A block median would give three distinct
  attachments in a nontrivial block and hence a rooted triangle. At a
  cutvertex median `z`, every other component contains at most one port.
  Any nonroot there has boundary contained in that port and `z`, a cut of
  order at most two in the original three-connected graph. Consequently
  all nonroots lie in `{z}`. The unmarked component is nonempty, so `z`
  must itself be a nonroot and is its unique vertex. Fullness gives degree
  exactly three. Deleting this unmarked vertex preserves permitted
  colourability in both directions by the elementary extension rule.
- Each replacement removes a nonempty open shore or the unique degree
  three vertex, so vertex order strictly decreases. The marked preimages
  are disjoint connected sets that avoid the retained open shore and
  compose under iteration. No step assumes colourability is minor-closed,
  or that a quotient remains chromatically critical or three-connected.
  The preliminary reduction is reapplied when needed.

## Inputs and scope

The directly reused three-connected marked-minor theorem is in
[colourful_five_wheel.md](colourful_five_wheel.md), SHA-256
`d804335fc68cff69d4eb2de770c246cbb91e0da336eb36a206d93d89378a64a1`.
Its [adjacent audit](colourful_five_wheel_audit.md) matches this
source hash. Its proof was reread, including the colour-dependent transfer
of at most one mark across a two-cut.

The reviewer directly inspected Kriesell--Mohr,
[*Kempe Chains and Rooted Minors*, Definition 1 and Theorem 7](https://arxiv.org/html/1911.09998).
Property `(*)` applies to a spanning subgraph of the routing graph, so
the exact missing-edge graph on five rainbow roots is an allowed input.
The resulting certificate keeps every prescribed root in its own bag;
the retained literal root edges supply all remaining adjacencies.

The block-cut argument was also checked against the elementary
[rooted-triangle proof](hc7_c21_rooted_density_low_degree_reduction.md#a-rooted-triangle-lemma),
source SHA-256
`431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2`.
The new source proves the exact degree-three alternative directly and
does not apply that older lemma without its degree hypothesis.

This is a separate whole-source internal review. The reviewer contributed
the unmarked-shore argument during development and checked the assembled
proof separately; this is not a wholly independent discovery or external
peer review. Cross edges between the two triangles are allowed throughout
the reduction. Dropping that invariant would invalidate some torso exits.

No generic statement about four-connected graphs with two triangles and an
unrooted `K5` minor is used. The remaining colourful four-connected
statement is an additional mathematical obligation, not a consequence of
the reduction or this audit.

The promotion from `active/` changed only the status line and relative
navigation links. A byte comparison after reversing those substitutions
confirmed that the mathematical text is unchanged; this audit was repinned
at that stage to the promoted source hash
`dd2e6beeb57b7d2290718ebcd959b703493955d430dd3d4190a2949eb3cc361a`.

## Independent reconstruction

A second reviewer, who did not develop this reduction, reconstructed the
whole argument at source SHA-256
`dd2e6beeb57b7d2290718ebcd959b703493955d430dd3d4190a2949eb3cc361a`.
**Verdict: GREEN for the conditional reduction, with the four-connected
terminal still open.** No additional assumption or mathematical gap was
found. This remains internal review.

The critical checks were the following.

- In the three-port linkage, deleting common port--triangle vertices
  first is legitimate. A separator of the remaining terminal sets has
  order less than their common size; together with the deleted common
  vertices, it separates a surviving triangle vertex from the nonempty
  opposite open shore with at most two vertices. This also checks cuts
  meeting either triangle.
- Opposite-shore quotient colourings need only agree on the equality
  partition of the ports. Their clique ports enforce precisely that
  partition. A permutation of the four old colours then glues permitted
  colourings. The fixed ordinary colouring separately certifies each
  quotient, so colourability is not being inferred from contraction.
- For an unmarked shore with no rooted port triangle, a cutvertex median
  leaves at most one port in each component. Every surviving nonroot
  would then have an actual separator of order at most two in the
  original graph. Thus the sole nonroot is the median itself, and its
  deletion has the asserted extension property. A median belonging to
  the ports would leave no nonroot, contrary to the chosen shore.
- Five surviving preimages have five distinct original representatives,
  necessarily split three-plus-two between the original triangles.
  Their original clique edges can be restored because all five marks
  are rainbow. Kriesell--Mohr's primary Definition 1 and Theorem 7 were
  inspected directly: the missing-edge graph is an allowed spanning
  subgraph of the routing graph and has at most six edges. The resulting
  certificate preserves all five roots.

The reused three-connected reduction was reread at the hash recorded
above. Its operations cannot retain six marks while discarding a vertex
of either literal triangle: three distinct triangle marks cannot survive
in at most two separator preimages. Every later replacement strictly
decreases vertex order, and all marked preimages compose disjointly.

## Appended critical-host application

Section 7 was appended after the preceding reviews. The independent
reviewer separately checked that application at SHA-256
`f82ab1b68dd04ff2cae5a95628a5ba1d680a81933e49ced1b63ff88f48f79534`.
**Verdict: GREEN for the application and the resulting whole source.**
Sections 1--6 are unchanged. No earlier review is represented as having
covered this addition.

The entire colour class `I` containing `r` is independent, and its only
vertex in `N(u)` is `r`, because `r` is adjacent to all six triangle
vertices. Removing `I` from a six-colouring of `G-u` therefore leaves a
five-colourable graph containing both literal triangles. Any five-colouring
of that graph missing a colour on their union extends over `I` in a new
sixth colour and over `u` in the missing colour. This proves universal
colourfulness and also excludes four-colourability of the core.

All marked preimages of the reduction lie in that core, hence avoid
`u,r`. Lifting a marked `K5` model retains an actual triangle vertex in
each bag; the singleton bags `u,r` consequently supply every additional
contact, including `ur`. The argument does not assume a five-colouring of
`G-{u,r}`: it applies whether that graph has chromatic number five or six.
It asserts no inherited host connectivity or chromatic criticality. The
four-connected marked-model theorem is still an unresolved premise, so
neither this neighbourhood case nor HC7 is closed.
