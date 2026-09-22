# Audit: a common graph in three facial-triangle web views

Date: 22 September 2026.

**Verdict: GREEN for the stated planarity theorem.** The reviewed
[source](three_web_remainder_planarity.md) has SHA-256
`d58c33ff25efd8b9e08e8186516c5170db90814a4ea4ee3a5714165d4afdd65e`.
The theorem proves that the common graph is planar under its four
stated web hypotheses, without a connectivity assumption. No unresolved
mathematical gap was found. This is a separate internal reconstruction
by a reviewer who did not write the construction, not external peer
review. Planarity of the actual prism graphs `H_i` and cofacialness of
their cell gates are not conclusions of this theorem.

## Reviewed revision and promotion

The review began with the pre-promotion draft
at SHA-256
`ef749e935d271dbee5b6c0a44c7c0f971c60942c48312bd1320bb5ceee05c913`.
One sentence incorrectly said that four incident edge paths shared no
endpoints. Two share `x` and two share `y`, both inside the cell.
The reviewer corrected that sentence to the precise fact used by the
proof: their portions outside the cell are pairwise vertex-disjoint,
so their first exit gates are distinct. This follows directly from
the definition of a subdivision and introduces no new hypothesis.
The corrected active revision had SHA-256
`97a329262a2b958bab9fa0644d23f3097d16e152e810932976c63aaaf61bf3df`.
The subsequent move to `results/` changed only the status line and
relative links. The verdict covers the corrected, promoted hash above.

## Exact assumptions and external input

The proof needs the four hypotheses for the same finite simple graph
`F`, with each skeleton embedded in the plane, each whole cell attached
only to its assigned facial triple, and at most one cell per face.
Whole cell interiors are disjoint both within a view and across views.
They need not be connected. Skeletons may contain auxiliary vertices
and edges: the construction uses those edges only to build planar
drawings, not as actual edges of `F` or as minor contacts.

The external input is the classical Kuratowski theorem: a finite graph
is nonplanar exactly when it contains a subdivision of `K5` or `K3,3`.
The rest of the argument was reconstructed directly. In such a fixed
subdivision, every cycle traverses at least three branch vertices for
`K5` and at least four for `K3,3`. Indeed a simple cycle must traverse
an entire subdivided edge whenever it enters an internal degree-two
vertex, and hence corresponds to a cycle of the unsubdivided graph.

## Suppression and repeated boundary edges

In a branch-free whole cell, every nonempty component of the fixed
subdivision restricted to that cell is a path, possibly one vertex.
A cycle component would violate the preceding branch-vertex count.
Each path has two exit incidences. Equal exit vertices would create a
cycle with at most one branch vertex; two different path components
with the same exit pair would create a cycle with at most two.
Both possibilities are excluded. Thus replacing those paths by edges
of their facial triangle is actual suppression of internal degree-two
vertices of the subdivision.

The same check excludes the strongest possible simultaneous failure.
If paths in different cells projected onto the same skeleton edge,
their original interiors would be disjoint and their union would be
a cycle with at most two branch vertices. The same contradiction
applies if a projected edge coincided with a retained actual edge of
the subdivision. Thus suppression does not merge parallel routes or
discard an edge of the Kuratowski subdivision. Different replacement
edges lie on the already embedded facial boundaries. Shared gate
vertices preserve their original degrees in the subdivision; no
unrelated vertices are identified.

## Branch-containing cells

For `K5`, a cell containing exactly one branch vertex would force its
four incident edge paths through four distinct first gates. Those
paths have distinct other branch endpoints outside the cell and meet
only at their common branch vertex inside it. The triple cannot
supply four gates. If no cell contained two branch vertices, all cells
would therefore be branch-free, and the preceding simultaneous
suppression would put a `K5` subdivision in the planar skeleton.
Consequently every view has a cell containing at least two of the
five branch vertices.

For `K3,3`, assume no cell contains a same-shore branch pair. A cell
then contains at most two branch vertices. If it contained two of
opposite shores, the four edge paths from them to the other four
branch vertices would have pairwise disjoint portions outside the
cell. The corrected first-gate count rules this out. Hence every
cell contains at most one branch vertex.

The component containing a single branch vertex `x` is precisely the
three initial legs leading to three distinct first gates. Every
additional component would be a branch-free path between two of
those gates. Together with the two corresponding legs through `x`,
it would make a cycle with at most three branch vertices. Re-entry
of an incident edge path would also produce such an additional
component. Both are impossible. This check uses the entire whole
cell, not merely the component containing `x`.

Replacing its three legs by one three-legged star in the assigned
open face suppresses only degree-two vertices and preserves `x` as
a branch vertex. There is at most one star per face. Stars in distinct
faces are disjoint, and branch-free replacements occupy only the
facial boundaries. The previous repeated-edge argument applies to
all of those boundary replacements. Thus the simultaneous operation
really draws a subdivision of `K3,3`, rather than a quotient with
lost paths, in the plane. This contradiction establishes a same-shore
branch pair in some cell of every view.

## The three-view contradiction and application boundary

The proof keeps one fixed Kuratowski subdivision throughout. In the
`K5` case the three selected cells would contain at least six distinct
branch vertices, because their interiors are pairwise disjoint across
views. There are only five. In the `K3,3` case, two of the three
selected same-shore pairs belong to the same shore; disjointness
would require four branch vertices in that shore, which has only
three. These counts use neither connectivity of `F` nor compatibility
between the three skeleton embeddings.

For the stated prism application, the clean-web inputs and whole-cell
cross-view disjointness establish the four hypotheses for `F=J[E]`.
The [path-cell theorem](hc7_two_triangle_web_path_cells.md) supplies
those inputs in its original-host application; this proof does not
derive them from degree conditions alone. The conclusion removes a
connectivity premise from planarity of the remainder itself. It does
not permit an arbitrary three-gate patch to be inserted into a
skeleton face: a specified gate triple can fail to be cofacial in a
planar graph. That remaining obligation, the whole selected critical-host
case and HC7 are not resolved here. No finite computation or transfer
of criticality is used.
