# Audit of the rooted-wheel extension limits

**Verdict:** GREEN for the [source](rooted_wheel_extension_limits.md),
SHA-256 `bcfbc442f33f18fe4198f0d9dcffae282ca31eea47d1251e72bfad2fecb01a39`.
No unresolved mathematical gap was found in the stated counterexamples.
The first two examples retain Bacon's separate complete review at source
`be41868a1502979528f8548a35216e6d23028986b590d4ce925c9df4bd19e711`;
that reviewer did not develop them. Removing Section 3 and reversing only
the title and “None refutes” wording byte-recovers that earlier hash.
Route-assessment independently checked the new Section 3 and its frontier
integration; the parent and literature-repair developed that example.
The checks below are internal reviews, not external peer review.

## Cuboctahedral example

The two root triples are disjoint because the chosen cube vertices have
distance two. A separation of the line graph after at most three vertex
deletions would give two edge-containing components after deleting the
corresponding cube edges. A smaller component has two, three or four
vertices; cubic degree and bipartiteness give edge boundaries at least
four, five and four. Thus the asserted connectivity is exactly four.
The standard line-graph embedding around the cube vertices is planar.

For a common neighbour c, the roots ac and bc each have exactly four
neighbours: two roots of their own triangle, each other, and the same
nonroot cw. Any expansion must first take cw. If one expands, the other
has at most three distinct bag contacts. If neither expands, their
required second opposite-triangle contacts assign cw to different root
triples. This excludes every six-root octahedral model, without fixing
which opposite-triangle pairs form its missing matching.

## Apex-prism example

The prism remains connected after deleting any two vertices: an intact
layer connects everything, or the two surviving layer paths are joined
by remaining spokes. Its cone consequently has connectivity four.
Planarity of the cone would put every prism vertex on one face after
deleting h, contradicting the elementary degree-two property of
outerplanar graphs.

A rooted K5 model avoiding h is excluded by planarity. If one bag uses
h, the other four bags lie in the prism and would give a rooted K4 at
four cofacial outer roots. Equivalently, its contacts would supply two
vertex-disjoint paths joining opposite pairs of those four roots, which
is impossible in the disc. This checks the obstruction even when the
h-owning bag consumes additional prism vertices.

The five displayed bags are disjoint and connected. Their rim contacts
are r1-r2, r2-r3, r3-r4 and r4-s4; precisely the two stated rim diagonals
are absent. Both displayed diagonal paths are simple, mutually disjoint
and internally root-free. One nevertheless traverses the hub bag, so
the paths cannot simply be added to the wheel model as independent
branch-set contacts.

## Preserved scope of the first two examples

The two negative conclusions use only the elementary connectivity and
planarity facts checked above. No finite search is a proof dependency.
The source does not claim labelled wheel contractibility, a K5-scheme
counterexample, or a counterexample to the five-connected nonplanar
two-triangle target. Neither construction refutes the audited five-root
wheel theorem or closes the remaining C19/HC7 programme.

## Entire hub colour class and frontier integration

The canonical paths alternate their endpoint colours, contain no foreign
roots and meet only at vertices whose colour is a common target endpoint.
Every host edge is used; nonroots lie on three or four demands and have
degree six or eight. The asserted strong normalisation therefore holds.
A connected bag containing h,u must use a rim clone, which rotation makes
A. Then the only possible nonroot neighbour of b or d outside that bag
is C. Either singleton would have at most one rim-bag contact; both must
therefore absorb C, contradicting disjointness. This checks containment of
the hub colour class even when further expansion is allowed.

The positive model has all four hub contacts and the four rim contacts
through BC, CD, DA, AB; its bags are connected and correctly labelled.
It leaves u unused and h singleton. Thus neither labelled W4
contractibility nor a singleton-hub theorem is refuted. The two-line
addition to the [K5 frontier](../active/k5_contractibility_frontier.md),
SHA-256 `0b55dd9f3657dee1fadd7e759555af92743a4b104da29ad44412044729833fa2`,
accurately records only the failed whole-class containment requirement.
No computation is a proof premise, and no C19 or HC7 closure is claimed.
