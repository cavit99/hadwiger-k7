# Audit: three-connected remainder in the clean prism webs

Date: 22 September 2026.

**Verdict: GREEN for the stated three-connected remainder exclusion.**
The reviewed [source](hc7_two_triangle_three_connected_remainder.md) has SHA-256
`bf1ca479698259b2aa9752060afd7bc9e8c0f66f21e14ee2ef9b68e672a83980`.
No unresolved gap was found in its whole-cell cofacialness construction,
the simultaneous insertion or the resulting Euler contradiction. This
is a separate internal reconstruction by a reviewer who did not write
the source, not external peer review. It excludes this entire structural
subcase, not the whole selected six-chromatic case or HC7.

**Promotion provenance:** the independent reconstruction originally
reviewed the pre-promotion draft at SHA-256
`6fa555fefb19fb46483e4f890304219b0d8c6be7a403d2aff923bbe019ad4364`.
On 22 September 2026 the source and this audit were moved to `results/`.
The reviewer compared the promotion against the frozen original:
only proof-status wording, a heading and relative links changed.
The mathematical statement and argument are unchanged; the verdict
applies to the promoted hash above.

## Hypotheses and dependency check

The structural argument assumes finite simple graphs, the exact induced
prism subdivision with six literal cap roots and nonempty rail interiors,
and three-connectivity of `J[E]`. It retains the actual contact bounds
of two `E` neighbours per root and four per internal rail vertex.
The degree hypothesis used in the final count is `d_J(v)>=6` for every
`v in E`; no minimum degree six inside `J[E]` is assumed or needed.

The two clean-web inputs are substantive hypotheses of this structural
argument. They follow in the stated original-host application from
`chi(J)=6` and the hypotheses of the
[three-web argument](hc7_two_triangle_web_path_cells.md), whose
promoted source hash is
`21d22e189e0cb1e0f5a536aec3267577645bc8c37af94a888dbb3f3098ae4e50`.
The reviewer previously reconstructed its path-cell exclusion and
cross-view disjointness in the
[adjacent audit](hc7_two_triangle_web_path_cells_audit.md).
The disjointness proof applies to arbitrary nonempty `E` subsets with
the displayed actual boundary bounds, so it applies to whole completion
cells even when their actual induced graphs are disconnected. Thus a
whole cell in one view lies in both other skeletons. The present proof
does not infer those clean-web inputs from the local degree bounds alone.

## Gates and three-connectivity

For a whole cell `C`, the proof correctly eliminates `|E-C|<=1` using
the four surviving cap roots. When `2<=|E-C|<=3`, each of the two
surviving nonempty rail interiors supplies a distinct non-`E` boundary
vertex. At most one `E` gate remains, leaving a vertex of `E-C` beyond
that gate and contradicting three-connectivity. With `|E-C|>=4`, a
boundary of at most two `E` vertices would again have vertices of `E`
on both sides. Consequently all three actual gates lie in `E` and
equal the whole facial triple. These arguments are valid for disconnected
`C`, and they prove absence of contacts with both surviving rails.

Suppose an alternate whole cell `D` hides at least two gates of `C`.
Actual edges across `D` force a gate of `D` into `C`. If there are at
least two such gates, the union has at most two external `E` neighbours.
The third rail has at least four `E` neighbours outside this union,
so the putative cut has a nonempty exterior. If there is exactly one
such gate `a`, removing `a` from `C` leaves at most two possible
boundary vertices, while a hidden `C` gate lies beyond that boundary.
Three-connectivity forces `C={a}`. This singleton patch is a subgraph
of `K4` with its three gates cofacial. Hence every remaining whole
cell has at most one hidden gate in each alternate whole cell; splitting
one whole cell into actual components is neither used nor permitted.

Every component `K` of `E-(C union B)` has actual boundary exactly
`B`: it is nonempty, its boundary is contained in `B`, and nonempty
`C` remains outside that boundary. The proof also handles the possible
loss of all of `K` inside one alternate cell. With no hidden `B` gate,
that cell's facial triple is `B`, already witnessing cofacialness in
the alternate skeleton. With one hidden gate `b`, its other gates
must be the two remaining `B` vertices and one vertex of `C`.
Every exterior component is full to `b`; none contains a gate through
which it could leave this alternate cell. They therefore all lie in
it, leaving at most two possible `E` neighbours for the third rail.
The four-contact hypothesis excludes this case. Thus the unresolved
case has a nonempty visible part of `K` available for projection.

## The strongest step: an exterior through the alternate web

For each component `L` of `K intersect D`, connectedness of `K` and
the fact that `K` is not contained in `D` force an exit through a
facial gate belonging to `K`. Projecting passages through `L` uses
only edges between those `K` gates. The projected graph is nonempty
and connected, has only vertices of `K`, and uses only skeleton edges.
In particular, no vertex of `C` or `B` is consumed as an internal
connection. This remains true if different components of `K intersect D`
use different subsets of the same facial triple.

All actual edges of the whole patch `J[C union B]` are retained.
Edges with visible endpoints are skeleton edges. Each hidden `B`
vertex occupies a different alternate cell face and can be joined by
one star to that cell's three gates. Every actual neighbour of that
vertex outside its cell is such a gate, and two vertices hidden in
different cells have no actual edge between them. These stars cause
no collision with the projected exterior, which uses only face-boundary
edges. Added star edges are auxiliary planar edges, not asserted
actual contacts of `J`.

Each actual contact from `B` to `K` yields a direct edge to the
projected exterior: it is retained when both endpoints are visible,
replaced by a face-boundary edge when only the `K` endpoint is hidden,
or supplied by the inserted star when the `B` endpoint is hidden.
The relevant component inside the face has a `K` gate in every case.
The resulting connected exterior avoids the entire actual cell patch,
so its drawing lies in one face of that patch. Its three incident
edges put every vertex of `B` on that same face. This establishes
cofacialness of the whole patch, not merely of its separate components.

## Insertion, counting and exact limit

A planar graph with three specified vertices incident with one face
can be drawn in a disk with those vertices at the three boundary
corners. There is no ordering obstruction for three corners: rotation
and reflection match the original facial triple. Each whole cell is
inserted in its own original skeleton face. The different interiors
are disjoint, no actual edges join them, and actual gate edges remain
on the skeleton. This simultaneously includes every actual edge of
`H_i`. In particular the proof has repaired, rather than assumed, the
cofacialness needed for insertion.

For each resulting planar `H_i`, connected `E` lies on one side of
the surviving-rail cycle. The induced prism has no chords of that
cycle, so the other side is empty and can be made the outer face.
The disk bound and the fact that every prism vertex and every
`E`--prism edge occurs in two views give `3a+2d<=9e+2s-9`.
The actual bounds `2a+d>=6e` and `d>=4s-12` give the incompatible
lower bound `3a+2d>=9e+2s-6`. All constants and multiplicities are
correct.

The conclusion is an unbounded exclusion of a three-connected
remainder under the stated clean-web inputs, and hence of that
remainder in the stated six-chromatic original-host application.
There is no induction, finite computation or transfer of chromatic
criticality to another graph. Remainders with a cutvertex or a
two-vertex separator remain outside this proof; no closure of their
attachment and colouring obligations is established by this audit.
