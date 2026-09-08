# Internal audit of the two-triangle exterior helpers

**Verdict: GREEN.**

The complete [source](hc7_two_triangle_exterior_helpers.md) was checked at
SHA-256 `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8`.
No gap was found in its stated theorem, corollary or lifts. This is an
internal audit, not external peer review or completion of Conjecture 19.

## Provenance and inputs

The reviewer co-developed the four-root induction and all-A cut repair,
and discussed the linkage and uncrossing arguments before this full-file
audit. Those prior discussions are disclosed rather than presented as a
wholly uninformed review. The complete frozen draft was independently
read at `77bf9868d9fe98010f58cff740a1dbd986eb99a86ecdefe86c606145d54b1416`;
only its pending-status sentence changed before the first audited revision.
Promotion changes only relative input links; reversing them exactly recovers
the audited source `243f6958ac632fc3ab38a370847f1ee9f00f857e8734da3c30f5408e460a91d6`.
All four input sources and all four adjacent audits match their exact
hashes printed in the source; their invoked statements were reread.
The NT8 alternative is taken from the previously audited repository
statement. No fresh primary-source inspection or finite computation is
claimed or used as a proof premise.

## Strongest inference checks

**Four-root induction.** The nonempty interior has at least three vertices
under degree six. Single-root absorption and simultaneous two-root transfer
preserve each surviving nonroot degree and boundary cardinality exactly,
keep four distinct connected root preimages, and strictly decrease interior
order. Normalization makes both ports in the trisection nonroots. The
small rooted separation has a nonempty root-free open side. In the planar
case, two-connectivity follows from the actual component boundary count;
the facial cycle and the two separate kinds of root incidences give the
displayed lower bound exceeding the planar upper bound by at least six.

**All-A boundary.** Connectedness and fullness of the exterior exclude
`q=x,y`. Seven-connectivity makes the actual boundary exactly `A+B+q`
and forces at least two vertices in the side. The opposite component
contains both `x,y`, misses at most one of the eight possible boundary
vertices, and contacts `v`. Contracting an edge in the triangle containing
its possible missed root is a joint choice made before the wheel theorem
is applied. Deleting `q` and that root merger lose at most two neighbours
of every interior subset. The other literal triangle and at least two
nonroots remain, so the degree-free wheel applies. The opposite component
and singleton `v` are disjoint, adjacent, full apices; every root merger
has its fixed actual two-vertex preimage. Their seven bags give `Q`.

**Two-connectivity and two-A boundary.** Any cutvertex of `K` in the
exterior produces precisely the forbidden all-A boundary; the endpoints
are not cutvertices because the exterior is connected and full to both.
In Lemma 4 the closed side retains all nonroot degrees and boundaries.
Two-connectivity supplies the two set-linkage paths, including trivial
paths for shared terminals. First-port truncation prevents either path
from entering the packet interior; they avoid the other A roots and meet
different packet bags only at their respective ports. Thus the two new
root labels and all rooted clique contacts lift without reuse.

**Three compatible deletions.** An A-neighbour in the exterior has at
most one B contact, so it retains degree six after that A root is deleted;
the other exterior vertices lose nothing. The four roots retain degree
five. The bound `2e>=6n-4` excludes planarity. Three-connectivity excludes
the trisection, leaving a root-free set with an actual four-boundary
containing the deleted A root and with all B contacts. Closed-neighbourhood
coverage minus vertex cardinality gives the stated submodularity. An
overlap keeps both deleted roots outside the union and in its boundary,
so Lemma 4 applies. Otherwise the three disjoint enlarged sides, B roots
and `v` give the displayed seven-clique model. No independent minor models
are combined during this argument.

**Spanning form and scope.** Literal `st` permits both port transfers;
maximization then puts the entire external boundary of the two helpers
at two actual ports. Three-connectivity makes those ports exactly the
singleton roots `s,t`. The helpers therefore partition all of `K` with
`x,y` separately retained, and the degree of `r` gives its contact with
at least one helper. The only possible missing pair is between `r` and
the other helper. Contacts with the separate B triangle and a compatible
third helper remain unproved; the two-triangle case and global objective
are explicitly still open.
