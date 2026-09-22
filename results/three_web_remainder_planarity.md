# Planarity of a common graph in three facial-triangle web views

**Status:** written proof, with a [separate internal audit](three_web_remainder_planarity_audit.md).
This proves planarity of the remainder
`J[E]` under the clean-web and cross-view-disjointness inputs. It does not
prove that the actual path-deleted graphs `H_i` are planar: the three gates
of a cell patch need not be cofacial merely because `J[E]` is planar.

## Exact statement

Let `F` be a finite simple graph. For each `i in {1,2,3}`, suppose there is
an embedded planar graph `P_i` and a family of pairwise disjoint sets
`C_{i,f}` indexed by some triangular faces `f` of `P_i`, such that:

1. Every vertex of `F` is either a vertex of `P_i` or belongs to exactly
   one `C_{i,f}`.
2. Every edge of `F` whose endpoints are both in `P_i` is an edge of
   `P_i`.
3. Every edge of `F` from `C_{i,f}` to its complement ends at one of the
   three vertices of `f`. In particular there are no edges between
   distinct cell interiors of this view.
4. The sets `C_{i,f}` and `C_{j,g}` are disjoint whenever `i != j`.

Skeletons may contain auxiliary vertices or edges absent from `F`.
There is at most one whole cell interior assigned to any face; a whole
cell interior may induce a disconnected graph in `F`.

**Claim.** The graph `F` is planar.

The clean prism webs satisfy these conditions with `F=J[E]`. All cells
are contained in `E`, all actual edges between skeleton vertices are
present in the completion, and whole cell interiors from different views
are disjoint by the six-neighbour argument in the
[three-web theorem](hc7_two_triangle_web_path_cells.md).
No connectivity assumption on `F` is needed in the claim.

## Localizing a Kuratowski subdivision in one web

Suppose `T` is a subdivision of `K5` or `K3,3` contained in `F`. Its
**branch vertices** are the five or six vertices corresponding to those
of the unsubdivided graph. For `K3,3`, retain their two three-vertex shores.
Every cycle of `T` contains at least three branch vertices in the `K5`
case, and at least four in the `K3,3` case.

Fix one view and write `C` for any of its whole cell interiors and `B`
for the three vertices of its facial triangle. The only exits from `C`
used by `T` are in `B`.

### Branch-free cell interiors

If `C` contains no branch vertex of `T`, every nonempty component of
`T[C]` is a path, possibly a single vertex, with two exit incidences at
`B`. There cannot be a component that is a cycle: such a cycle would
contain no branch vertex. The two exits of any one path have distinct
endpoints, since equal endpoints would give a cycle with at most one
branch vertex. No two paths have the same unordered pair of exit
endpoints, since their union would give a cycle with at most two branch
vertices.

Suppress each such path, replacing it with the corresponding edge of
B's triangle. The local replacement is a subgraph of the triangle and
is drawable on its boundary. It is exactly suppression of degree-two
vertices of `T`, not identification of unrelated vertices.

These replacements remain valid simultaneously over all branch-free
cells. A repeated projected edge from distinct cells, or repetition of
an actual retained edge, would again give a cycle of `T` with at most
two branch vertices. Thus no projected edge collision identifies two
edges of the resulting subdivision. Different facial boundaries already
belong to the same planar skeleton.

### Cells in a `K5` subdivision

If `C` contains exactly one branch vertex `x`, the four edge paths of
`T` incident with `x` all reach a gate of `B` before reaching another
branch vertex. They reach distinct gates: two reaching the same gate
would give two routes from `x` to a single other branch vertex, or would
meet at a degree-two vertex, contrary to the definition of a subdivision
of the simple graph `K5`. Four distinct gates are unavailable.

Consequently, if no cell contains at least two branch vertices, every
cell is branch-free. The simultaneous suppression above puts a
subdivision of `K5` inside the planar skeleton, a contradiction.

**Conclusion for one view:** some whole cell contains at least two of
the five branch vertices of every fixed `K5` subdivision in `F`.

### Cells in a `K3,3` subdivision

Suppose no cell contains two branch vertices of the same shore. Then a
cell contains at most two branch vertices. It cannot contain two of
opposite shores, say `x` and `y`: the two edge paths from `x` to the
other shore vertices and the two from `y` to the other shore vertices
must leave `C` through four distinct gates. Their portions outside `C`
are pairwise vertex-disjoint: distinct edge paths of the subdivision
can meet only at common branch endpoints, and their only shared
endpoints here are `x` and `y` inside `C`. Thus their first gates are
distinct. The path corresponding to the edge `xy` is irrelevant to
this count.

Thus each cell contains at most one branch vertex. A cell containing a
single branch vertex `x` has exactly three distinct gates on the three
incident edge paths of `T`. Their portions from `x` to first exit form
a three-legged star. There can be no further component of `T[C]`:
such a component would be a branch-free path between two of these same
three gates, and together with two legs of the star would give a cycle
with at most three branch vertices. That is impossible in a subdivision
of `K3,3`. The same argument excludes an incident edge path leaving and
then returning to `C` before reaching its next branch vertex.

Replace this entire local star by a fresh copy of `x` in the triangular
face and three edges from it to the face vertices. This only suppresses
the degree-two vertices of the three legs. There is one star at most in
any whole cell, hence one at most in any face. The other, branch-free
cells are replaced on their facial boundaries as above. Stars occupy
pairwise disjoint open faces and do not cross those boundary edges.
The resulting graph is a subdivision of `K3,3` drawn in the plane,
a contradiction.

**Conclusion for one view:** some whole cell contains two branch vertices
of the same shore of every fixed `K3,3` subdivision in `F`.

## Use all three views

If `F` were nonplanar, Kuratowski's theorem would give one fixed
subdivision `T` of `K5` or `K3,3`.

In the `K5` case each of the three views supplies a whole cell containing
at least two branch vertices. These three cells have pairwise disjoint
interiors, so they would contain at least six distinct branch vertices,
whereas `T` has only five.

In the `K3,3` case each view supplies a whole cell containing a same-shore
pair of branch vertices. Two of the three pairs belong to the same shore.
Their cells are disjoint, so that shore would contain at least four
branch vertices, whereas each shore has only three.

Both alternatives are impossible. Therefore `F` is planar.

## Remaining obstruction in the prism application

The proof supplies an embedding of `J[E]`, without a specified outer
face or cyclic order at its separators. For a cell `C` of `H_i`, it does
not yet embed the actual patch `H_i[C union N_{H_i}(C)]` with all its
gates on one face. In particular, adding a triangle on three vertices
of a planar remainder can destroy planarity. That cofacialness obligation,
with all actual rail contacts retained, remains necessary to reconstruct
all three actual `H_i` and invoke the established degree/Euler contradiction.
