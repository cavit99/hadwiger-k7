# Audit: two-connected remainders have no clean web cells

Date: 22 September 2026.

**Verdict: GREEN for the entire stated two-connected cell exclusion and
its final Euler contradiction.** The reviewed
[source](hc7_prism_two_connected_cell_exclusion.md) has SHA-256
`b765f99f798f0251bf2c152011cc637ede2d6bd091b125b0064f969e7ec7c84c`.
No unresolved mathematical inference was found. This is a separate
internal reconstruction by a reviewer who did not author the proof,
not external peer review. It proves an unbounded structural conditional
case; it does not by itself establish HC7.

## Review and promotion provenance

The original reviewed source was
the pre-promotion draft, SHA-256
`992c31e7deb7f7e0dd9bc4a137ca2228ff6fa47c64b6a42320b2591ace17ac83`.
On 22 September 2026 the source and this audit were promoted together
into `results/`. The reviewer checked the complete promotion diff:
only status wording and relative/navigation links changed. Every
mathematical statement, case and argument is unchanged. The verdict
applies to the promoted source hash above.

## Scope and pinned inputs

The audit retains all five source assumptions in the finite simple graph
setting: the whole induced prism with three nonempty rail interiors,
two-connectivity of the nonempty remainder, the six-neighbour bound for
every nonempty root-free set, two actual remainder neighbours at every
root and four at every rail-interior vertex, no T-meeting K5 model,
and three fixed clean ordered web completions. Neighbours of a set mean
vertices outside that set. No chromatic number is assumed.

The web structure and cross-view disjointness are taken from the
[path-cell proof](hc7_two_triangle_web_path_cells.md), SHA-256
`21d22e189e0cb1e0f5a536aec3267577645bc8c37af94a888dbb3f3098ae4e50`.
Its originating [extremal prism proof](hc7_two_triangle_extremal_prism.md)
has SHA-256
`8d617e35d5bc6fac0f25b5f418c6f35e976d282d883401199084e15c6d258222`.
The latter derivation is not needed once the displayed prism partition
is assumed. The whole-chain review independently reconstructed these
inputs, including the cross-view assertion for arbitrary, possibly
disconnected E-only shores.

The primary statements of Fabila-Monroy--Wood,
[*Rooted K4-Minors*, Lemmas 2 and 7](https://arxiv.org/html/1102.3760v1),
were checked in a separate dependency reconstruction during this review.
Lemma 7 requires the specified cyclic root order and a vertex-disjoint
opposite-pair linkage, with no additional connectivity assumption.
Lemma 2 gives the ordered spanning web in the absence of that linkage.
These are external theorem inputs, not results reproved by this audit.

## The complement projection and the pocket

For the pocket lemma, W is a nonempty connected proper subset of E,
A=E-W is connected, its E-boundary B has size at most three, and W
contacts only R_i. Hence its H_i-boundary is B. Cross-view disjointness
against every whole cell of an alternate view puts all vertices of W
in that view's skeleton, including all actual edges inside W.

A has a visible vertex. Otherwise connectedness places all of A in
one whole cell D: distinct whole cell interiors have no edges between
them. Since W is visible and E=A union W, this also forces D=A.
Every vertex of the other retained rail R_k then supplies a distinct
gate of D, because each has an E-neighbour and none has a W-neighbour.
There are at least three such gates. An actual edge between A and W,
which exists by connectedness of E, requires a fourth gate in W.
This contradicts the facial triple. This reasoning does not assume
that an arbitrary whole cell is connected in the actual graph.

Every connected component L of J[A intersection D] has an actual
A-gate: an A-path to a visible A vertex must first leave D through
one. Replacing cell passages by facial edges between their A-gates
therefore gives a connected auxiliary graph A* on visible A vertices.
It is disjoint from W and both rails. If a rail vertex v has a hidden
A-neighbour in L, v itself is a gate of that same cell. A facial edge
from v to any A-gate of L represents this contact at the original
rail vertex v. Such an A-gate differs from v. Thus every actual A--rail
contact is represented, including contacts whose original endpoint in
E was hidden. All these edges are skeleton edges and can be retained
simultaneously in its one planar drawing. They use no W vertex.

Separately projecting all of connected E using only E-gates gives a
connected auxiliary graph E*. Every hidden actual E component has an
E-gate because visible W is nonempty. E* contains the actual W graph
and the E-only A* graph; the previously selected A*-edges are E-gate
edges and may be retained. It is disjoint from the actual two-rail
cycle. Consequently W and A* lie on the same side of that cycle.
No disjointness between E*, W and A* is needed. A represented contact
edge also lies on this side, since its non-rail endpoint does and
its interior cannot cross the cycle.

W has at least three distinct R_i contacts by the six-neighbour
bound. An actual path through connected W between its first and last
contacts a,b is a simple arc with no other point on the cycle. The
arc and R_i[a,b] bound the pocket adjoining this boundary interval.
The other rail lies outside it. Connected A* avoids the arc and has a
represented contact with the other rail, so it lies outside the pocket.
At an open-interval vertex, the only side available within the cycle's
disk is the pocket side. An A* contact there would therefore enter the
pocket or cross the arc. This proves the absence of all actual
A-neighbours in R_i(a,b), by the contact-preserving projection above.

The actual set W union R_i(a,b) is nonempty and root-free, even when
a or b is a cap root. Extremality of the contacts accounts for every
W--rail edge; inducedness of the prism accounts for every rail exit.
Its actual boundary is contained in B union {a,b}, of size at most
five. Hidden vertices of B need not survive either auxiliary drawing:
they are retained in this actual boundary count. The contradiction is
therefore valid without a visibility assumption on B.

## Actual diagonals and exhaustive cell cases

The two displayed diagonal constructions use only actual edges.
Connected disjoint E-sets W,A supply internally disjoint passages.
The strict inequalities a<v<b on R_i and d<t or t<d on R_j separate
their rail portions. They join opposite pairs on the actual cycle,
so Lemma 7 supplies a rooted K4 in the graph avoiding the third rail.
That third rail is a disjoint connected fifth bag. Its two cap roots
are adjacent to all four nominated roots through literal cap edges,
which proves the claimed T-meeting K5 lift. No completion edge enters
this model.

For a nonempty actual connected cell component C, all neighbours
outside its whole cell lie among its facial triple, and there are no
edges to another actual component of the same cell. Thus, with the
source notation, |B|+|L|<=3. The complement cases are exhaustive:

- If |E-C|<=1, every surviving root has a C-neighbour by its two
  distinct E contacts. Four surviving roots would be four gates.
  With |E-C|>=2, two-connectivity excludes |B|<=1, since a vertex
  outside C and B survives removal of B. Hence |B|>=2 and |L|<=1.
  A rail-interior vertex on the untouched surviving rail has four
  distinct neighbours outside C, giving |E-C|>=4.
- Every component of E-C contains a B-vertex. A component containing
  only one such vertex b is the singleton {b}: otherwise b separates
  its other vertices from C in E. For |B|=2, a disconnected complement
  would therefore consist of just two singleton gates, already excluded.
- With two E-gates and no surviving-rail gate, the pocket lemma applies
  directly. With L={t}, C has at least three R_i contacts. The connected
  complement A contacts every vertex of the rail containing t except
  possibly t, so it has a contact d different from t. The diagonal
  obstruction rules out any A contact strictly between C's extreme
  R_i contacts. Adjoining that interval to C leaves exactly the
  possible boundary {x,y,t,a,b}, of size at most five.
- With three E-gates, L is empty. A connected complement again gives
  the pocket lemma. A disconnected complement must have gate counts
  two plus one: three one-gate components would all be singletons and
  give |E-C|=3. Thus E-C=A disjoint union {z}, where A is connected
  and contains x,y, and z has no E-neighbour outside C.
- In this last case W=C union {z} is connected, has connected
  complement A and E-boundary contained in {x,y}. If z misses both
  surviving rails, the pocket lemma applies to W. Otherwise choose
  a surviving contact t of z. Every vertex of that rail has an
  A-neighbour, since C misses the rail and the singleton z cannot
  provide even the two required distinct root contacts. Choose d!=t.
  The diagonal obstruction applies using any two C contacts a,b on
  R_i around a proposed A contact. It therefore excludes A contacts
  in the open interval between C's extremes. The final set includes
  C and that interval, but not z: all contacts of z, wherever they
  lie, are covered by the one boundary vertex z. Its boundary is
  contained in {x,y,z,a,b}. Multiple surviving-rail contacts of z
  do not affect this conclusion.

Every nonempty whole cell has an actual connected component, so these
cases exclude every whole cell. Planarity of the actual H_i follows
by taking a subgraph of its skeleton, with no insertion or cofacial-gate
assertion.

## Edge count and limits

The connected off-cycle graph E lies on a single side of the surviving
two-rail cycle in each actual planar H_i. The induced prism has no
additional cycle chord. The other side is empty and can be the outer
face. With boundary length r_j+r_k, the simple planar disk inequality
gives a+d_j+d_k<=3e+r_j+r_k-3. Summing yields
3a+2d<=9e+2s-9. Singleton root-free degree bounds give 2a+d>=6e;
the six roots and s-6 rail-interior vertices give d>=4s-12. Their
combination yields 3a+2d>=9e+2s-6, a contradiction by three.

There is no induction, inherited criticality, finite computation,
cell insertion, or transfer of auxiliary edges into a minor. The only
external assumptions are the stated graph-theoretic inputs above.
No unresolved gap remains within this exact scope. The separate
[whole-case audit](hc7_two_triangle_case_closure_audit.md) checks how
these inputs arise in the structural theorem and original graph.
