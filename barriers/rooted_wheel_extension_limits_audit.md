# Audit of the two rooted-extension obstructions

**Verdict:** GREEN; separate internal review of the complete
[source](rooted_wheel_extension_limits.md), SHA-256
`be41868a1502979528f8548a35216e6d23028986b590d4ce925c9df4bd19e711`.
No unresolved mathematical gap was found in either stated counterexample.
This reviewer did not develop the examples. The review checks the frozen
written arguments independently; it is not external peer review.

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

## Scope and dependencies

The two negative conclusions use only the elementary connectivity and
planarity facts checked above. No finite search is a proof dependency.
The source does not claim labelled wheel contractibility, a K5-scheme
counterexample, or a counterexample to the five-connected nonplanar
two-triangle target. Neither construction refutes the audited five-root
wheel theorem or closes the remaining C19/HC7 programme.
