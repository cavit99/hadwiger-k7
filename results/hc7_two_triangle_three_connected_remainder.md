# Clean prism webs when the remainder is three-connected

**Status:** written proof, with a [separate internal audit](hc7_two_triangle_three_connected_remainder_audit.md).
In the six-chromatic original-host setting, the extremal remainder cannot be
three-connected. A two-connected remainder with a two-vertex separator,
and remainders with a cutvertex, remain outside this conclusion.

## Precise setting and inputs

Let `J` be the original graph with the exact partition `V(J)=E disjoint
union S`, where `E` is connected and `S` is the induced prism subdivision
with literal caps `P,Q` and nontrivial rails `R1,R2,R3`. A cap vertex has
at least two actual neighbours in `E`; a rail-interior vertex has at least
four. Assume that `J[E]` is three-connected.
Every vertex of `E` has degree at least six in `J`.

For the original critical-host application, assume `chi(J)=6` and all
hypotheses of [the three-web construction](hc7_two_triangle_web_path_cells.md).
Its path-containing-cell theorem excludes that alternative, and its
cross-view disjointness proof applies to whole cell interiors as well as
their actual connected components. These supply inputs 1 and 2 below.
The contradiction proves that this application's `E` is not three-connected.

For each `i`, put `H_i=J-V(R_i)`. The four-root obstruction supplies a
planar web completion of `H_i`: its planar skeleton contains the cycle
formed by the two surviving rails and the two cap edges, and each added
cell has its interior vertices attached only to the three vertices of a
facial triangle. A cell interior may be disconnected in the ACTUAL graph.
All references to a cell below mean its WHOLE completion-cell interior,
not one actual component. Distinct cells of one completion have disjoint
interiors and no edges between their interiors.

The inputs required here are:

1. Every whole cell in all three views is contained in `E` (the clean
   case).
2. Whole cell interiors belonging to different views are disjoint.
   Consequently a cell in one view lies wholly in each other view's
   planar skeleton.
3. The skeleton and its triangular faces are only planar COMPLETION
   objects. Actual cell boundaries are subsets of the corresponding
   facial triples. No added edge is an actual minor edge.

The claim proved below is that every actual `H_i` is planar. The final
edge count then excludes this entire three-connected clean case.

## 1. Every nonempty cell has exactly three actual gates, all in E

Fix a nonempty whole cell `C` of view `i`, and let
`B=N_{H_i}(C)`. We have `|B|<=3`. Write `j,k` for the other indices and
put `h=|E-C|`.

First `h` is not zero or one: each of the four surviving cap vertices
has two distinct E-neighbours, so if `h<=1` each has a neighbour in `C`.
All four would belong to `B`.

If `2<=h<=3`, every interior vertex of both surviving rails has a
neighbour in `C`, because it has at least four E-neighbours. In
particular `B` contains at least two rail-interior vertices, leaving
`|N_E(C)|<=1`. Since there are at least two vertices outside `C`, at
least one lies beyond this boundary. Removing that boundary disconnects
the nonempty `C` from this vertex, contradicting three-connectivity of
`E`. Thus `h>=4`.

Now `N_E(C)` has at least three vertices: if it had at most two, the
at least four vertices of `E-C` include one beyond the boundary, giving
a forbidden cut. As `N_E(C) subseteq B` and `|B|<=3`, we obtain

    B=N_E(C),  |B|=3.

Thus `B` equals the entire facial triple of the completion. There are
no actual C-contacts on either surviving rail, including their roots.
Also `E-(C union B)` is nonempty. This proof does not require `C` to
be connected.

## 2. At most one gate is hidden in each alternate whole cell

Fix a different view `j`. The whole set `C` is visible in its skeleton.
Let `D` be one whole cell of view `j`, and let `A=N_E(D)` be its actual
three-gate facial triple, as established in Section 1.

Suppose `|B intersect D|>=2`. Each such hidden gate has an actual
C-neighbour, because it belongs to `B`. Since `C` is outside `D`, that
neighbour belongs to `A intersect C`; hence this intersection is nonempty.

If `|A intersect C|>=2`, then

    N_E(C union D) subseteq (B-D) union (A-C),
    |N_E(C union D)|<=2.

Neither `C` nor `D` contacts the third rail `R_k`: it survives in both
views, and both cells have only E gates. An interior vertex of `R_k`
therefore has at least four E-neighbours outside `C union D`, including
one beyond the displayed boundary. This contradicts three-connectivity.

Otherwise `A intersect C={a}`. Every vertex of `B intersect D` can
contact `C` only at `a`, so

    N_E(C-{a}) subseteq {a} union (B-D),
    |N_E(C-{a})|<=2.

If `C-{a}` were nonempty, the vertices in `B intersect D` lie outside
it and outside that boundary, again contradicting three-connectivity.
Thus `C={a}`.

For this singleton case the actual graph `J[C union B]` is a subgraph
of `K4` with the three vertices `B` on one face, so the desired
cofacialness is immediate. For every remaining cell `C`, each whole
alternate cell hides at most one vertex of `B`. This is a statement
about whole completion cells and therefore permits at most one inserted
B-star in any facial triangle.

## 3. A full actual exterior component

Assume `|C|>=2`, and choose a connected component `K` of
`E-(C union B)`. Such a component exists by Section 1. Its actual
E-boundary is contained in `B`. Since nonempty `C` lies outside that
boundary, three-connectivity forces

    N_E(K)=B.

The same is true of every component of `E-(C union B)`.

Consider first the possibility that all of `K` lies inside one whole
cell `D` of the alternate view.

* If `D` hides no vertex of `B`, fullness of `K` forces all three B
  vertices to be D-gates. Hence its facial triple is exactly `B`.
  All of `C union B` is visible in the planar skeleton, and the empty
  facial triangle of D witnesses a face incident with all three B
  vertices in the actual subgraph `J[C union B]`. This case is finished.

* If `D` hides one vertex `b` of `B`, the other two B vertices must be
  D-gates. An actual neighbour of `b` in `C` consumes the third gate,
  say `a`. Thus D's whole boundary is `{a} union (B-{b})`.
  Every other component `K'` of `E-(C union B)` is also full to `b`.
  It must meet D, since b is inside D and none of D's gates belongs to
  K'. Once K' meets D, its connectedness and the same gate exclusion
  imply `K' subseteq D`. Consequently

      E subseteq C union D union (B-{b}).

  Neither C nor D contacts the third rail `R_k`, so an internal vertex
  of that rail would have at most the two E-neighbours `B-{b}`. This
  contradicts the four-neighbour bound.

The case of two hidden B vertices was excluded in Section 2. Therefore,
unless cofacialness is already proved, `K` is not wholly contained in
any alternate cell and has at least one vertex in that planar skeleton.

## 4. Project the exterior without consuming C or B

Keep every skeleton vertex of `K`, and its actual edges to other such
vertices. For each alternate whole cell `D`, consider each actual
connected component `L` of the induced graph on `K intersect D`.
Because `K` is connected and not wholly contained in D, L has a
neighbour in a D-gate that lies in `K`. Let `Q_L` be the nonempty set
of these K-gates. Replace the portion L by edges joining `Q_L` inside
the clique on D's facial triple. These are boundary edges of the face.

The resulting plane subgraph `K*` is nonempty and connected: every
path in K projects to a walk after each maximal segment inside a cell
is replaced by the corresponding gate edge or a constant walk. Every
vertex of `K*` belongs to `K`, so `K*` avoids `C union B` completely.
No C- or B-gate is used to connect the projected pieces.

Preserve the actual graph `J[C union B]` as follows. C is already in
the skeleton. Each hidden B vertex `b` is alone among B in its whole
cell D, by Section 2. Put b inside D's triangular face and draw one
star from b to D's three gates. All actual b-neighbours in C or in
visible B are among these gates. There are no actual edges between
vertices hidden in different cells. Thus the stars preserve every
actual edge of `J[C union B]`. There is at most one star per face;
K* uses only the boundary edges of these faces, so no insertion
collision occurs.

Finally retain an edge from each b in B to K*. Such an edge exists
in the constructed plane supergraph, using `N_E(K)=B`:

* If b and an actual K-neighbour are both visible, keep their edge.
* If b is visible and a K-neighbour lies in a cell D, b is a D-gate.
  Connect b by the facial triangle edge to a K-gate of the relevant
  component L of `K intersect D`.
* If b is hidden in D, an actual K-neighbour either is a K-gate of D
  or lies in a component L inside D having a K-gate. The inserted
  b-star therefore has an edge to a vertex of K*.

These edges have B and K* endpoints and consume no C vertex. We now
have a plane supergraph containing the actual `J[C union B]` and a
connected graph K* outside it, adjacent to every B vertex. The drawing
of K* lies in one face of `J[C union B]`; its three incident edges
show that this face contains all three gates. This proves the required
cofacialness of the WHOLE cell patch, even when C is disconnected.

All added face edges and stars in this argument are solely auxiliary
objects proving existence of a planar embedding. They are not asserted
to be edges or minor-model contacts of J.

## 5. Reinsert whole cells and apply the disk count

Each whole cell patch has now been proved planar with its actual gate
triple on one face. Insert that whole patch inside its own triangular
face of the original web skeleton, preserving any actual gate edges.
Different whole cells occupy different faces. This gives a planar
embedding of the actual H_i for each i. We never insert several
three-legged stars in the same face by treating actual components of
one whole cell separately.

Let `e=|E|`, `s=|S|`, let `a` be the number of actual edges inside E,
and let `d` be the number of E--S edges. In H_i the two surviving
rails and their two cap edges form a cycle `C_i`; all remaining vertices
are the connected E. Hence this cycle can be taken as the outer face.
Writing `s_i=|V(C_i)|` and `d_i=e(E,V(C_i))`, the disk edge bound gives

    a+d_i+s_i <= 3(e+s_i)-3-s_i,
    a+d_i <= 3e+s_i-3.

Each S vertex and each E--S edge occurs in exactly two views, so summing
yields

    3a+2d <= 9e+2s-9.

Every E vertex has J-degree at least six, giving `2a+d>=6e`.
The six roots contribute at least twelve E--S edges and each of the
`s-6` rail-interior vertices contributes at least four, so
`d>=4s-12`. Consequently

    3a+2d = (3/2)(2a+d)+(1/2)d
           >=9e+2s-6,

a contradiction. Subject to the two stated clean-web inputs, the
three-connected remainder case is therefore excluded.

## Exact boundary of this proof

For merely two-connected E, an exterior component need only meet two
of a cell's three E gates, and two B gates can remain hidden in one
alternate cell behind a genuine two-vertex separator. The proof above
does not remove those cases. Neither the full six-chromatic case nor
HC7 is asserted here.
