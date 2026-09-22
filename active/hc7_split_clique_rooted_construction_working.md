# A four-root obstruction which retains the seventh bag

**Status:** working construction; not separately audited. This does not
close the split-clique neighbourhood case or HC7. It supplies a genuine
`K7` lift for a four-rooted minor test; an ordinary four-root obstruction
in the unequal-cap prism does not have this lift automatically.

Let `G` be seven-connected and `K7`-minor-free. Let
`N(u)=P dotunion D`, where `P` is a triangle, `D` a four-clique and
the two are anticomplete. Label `D={r,q1,q2,q3}`. No chromatic assumption
is needed for the following construction.

## Three paths with prescribed endpoint multiplicities

In `K=G-{u,q1,q2}`, there exist three paths whose initial vertices
exhaust `P`, with two ending at `r` and one ending at `q3`. Their
interiors are pairwise disjoint, and the only shared vertex is `r`
on the first two paths. No member of `P union {r,q3}` is internal
to a path.

Indeed `K` is four-connected. Use the integral vertex-capacity version
of Menger's theorem, with three unit-capacity sources in `P`, endpoint
capacities two at `r` and one at `q3`, and capacity one at every other
vertex. A separating cut of capacity at most two deletes at most two
vertices of `K`, possibly including some source or target vertices.
At least one source and at least one target remain, since deleting all
sources or both targets costs three. Four-connectivity leaves a path
between them, contradicting separation. Thus a flow of value three
exists and uses all the prescribed endpoint capacities. After deleting
cycles, it gives the asserted paths. Unit source capacities and the
total flow value ensure that a different source cannot occur internally.

Relabel `P={p1,p2,p3}` according to the three endpoints. Delete `r`
from the first two paths and call the resulting vertex sets `F1,F2`.
Let `F3` be the entire `p3`--`q3` path. These three sets are nonempty,
connected and pairwise disjoint. Each `Fi`, for `i=1,2`, contains `pi`
and an actual neighbour of `r`. The third contains both `p3,q3`.
None contains `u,q1,q2,r`.

## The four-root test and exact lift

Put `R={r} union (F1-{p1}) union (F2-{p2})`. This is a connected
set (in fact the vertex set of a path through `r`). It is disjoint
from `F3,{u,p1,p2,q1,q2}` and adjacent to each of `p1,p2,q1,q2`.
The first two contacts are the first edges of the two fan legs; the
other two are the actual edges `rq1,rq2`.

The **actual induced graph**

    H0=G-({u} union R union F3)

has no `K4` model rooted at `p1,p2,q1,q2`. For any such model, adjoin
the bags `R,F3,{u}`. The two extra nonsingleton bags are adjacent
through `rq3`. The bag `R` contacts all four rooted bags as just
specified; `F3` contacts the two P-rooted bags through the literal
P edges and the two Q-rooted bags through the literal D edges. The
singleton `u` sees all six bags at their original P or D vertices.
Thus all seven bags form a `K7` model.

This formulation makes no root contraction and hides no parallel
contacts. It retains all root ownership explicitly. The price is the
deletion of the two disjoint reserved paths `R,F3`; controlling their
attachments to `H0` is a remaining construction obligation.

This works for every choice of the four labels on `D` and every
three-path system with the stated endpoint data. No proper minor
inherits contraction-criticality or a chromatic lower bound. There
is no induction.

## A spanning web without an additional cycle premise

Fabila-Monroy--Wood,
[*Rooted K4-Minors*, Theorem 15 and Section 6](https://arxiv.org/html/1102.3760v1),
apply to every graph, without a connectivity assumption. In the
absence of the rooted minor, the graph is a spanning subgraph of
one of their six obstruction classes. The nominated-root subgraphs
in classes A,B,C,E,F have matching number at most one: respectively
a star, an independent set, an independent set, one edge, and an
independent set. Adding their triangular cells does not add edges
between the original nominated roots.

Our roots have the two disjoint actual edges `p1p2,q1q2`. Thus only
class D remains: `H0` has a spanning web completion. Its skeleton is
plane with the four roots on the outer face; each additional cell
is attached to the three vertices of a triangular face. The two
actual root edges cannot both be diagonals of the outer quadrilateral,
so they are consecutive pairs in its outer order. No artificial
completion edge has been used as a contact in the `K7` lift.

For every nonempty actual cell set `X`, its actual `H0` boundary has
order at most three. It is disjoint from all seven original neighbours
of `u`, so `u` has no neighbour in `X`. Seven-connectivity therefore
gives the concrete attachment condition

    |N_G(X) intersection (R union F3)| >= 4.

Otherwise its complete actual `G` boundary would have order at most
six and separate `X` from `u`.

## A larger state class and a genuine minimum

Allow `R` to be any connected set containing `r`, avoiding all other
P and D vertices, and adjacent to `p1,p2`. Keep `F` a `p3`--`q3`
path, disjoint from `R` and the other named roots. The same seven-bag
lift and web conclusion hold. Choose a state minimising
`|R union F|`, over all labellings of P,D and all such sets and paths.
Existence follows from the three-path construction above.

The path `F` is induced: shortcutting a chord strictly reduces the
minimum while leaving the other bag and every root contact intact.
The set `R` is an inclusion-minimal induced connector for `r` and
chosen contacts with `p1,p2`. It has the shape of a tree with at most
three terminal stems, or a triangle with one terminal stem at each
corner. To see this, remove nonterminal leaves from its block tree.
Every cyclic block must have all its vertices either marked terminals
or gates leading to a terminal: any other vertex can be removed while
preserving connectivity. There are only three terminal directions,
so such a block is a triangle; there can be at most one branching
block. These are descriptions of the actual induced graph, not merely
a chosen spanning tree.

In the tree case let `b` be the meeting vertex of the three paths to
`r,p1,p2`, adding one chosen contact edge to each P vertex. The
`b`--`r` path may have length zero. In the triangle case let
`c1,c2,cr` be its corners owning those three stems. A zero terminal
stem is allowed; the P vertices themselves remain outside `R`.

### Swapping a P endpoint and the two D labels

Suppose `x` lies on the open `p1`--`b` stem in the tree case and
`xy` is an actual edge with `y in F-{p3}`. Switch the roles of
`r,q3`, and put

    new F = the old p2--r tree path,
    new R = (F-{p3}) union (old p1--x prefix minus p1).

The edge `xy` connects the displayed parts of the new R bag. Its
new D root is the old `q3`; it sees the remaining P roots `p1,p3`.
The new F contains the old `p2,r`, now the remaining P--D pair.
The bags are disjoint. The old `p2` enters the reserved union and
the old `p3` leaves it, cancelling in the count. Every internal vertex
of the old `x`--`b` segment is freed and no vertex is added. Hence
an F contact of this kind is possible only at the stem vertex next
to `b`.

For a triangle core use the old `p2`--`r` path through the edge
`c2cr`, avoiding `c1`. If `x` lies strictly between `p1` and `c1`,
the same swap frees `c1` as well as any remaining stem segment.
Consequently no such vertex contacts `F-{p3}`. The corner `c1`
itself may do so. The analogous conclusions hold on the other P stem.

### Two contacts of a P-side vertex

For the permitted vertex `x` just considered (including a P-owned
triangle corner), suppose `y,z` are distinct F neighbours, ordered
from `p3` to `q3`. A second valid swap uses the same new F, and

    new R = (p1--x prefix minus p1)
            union (F[p3,y] minus p3) union F[z,q3].

The edges `xy,xz` connect these sets and retain both P contacts.
If `y=p3`, the first F prefix is empty and `xp3` supplies that contact
directly. This swap frees every vertex of the open F interval `(y,z)`.
Thus all F neighbours of such an `x` lie in at most two consecutive
vertices of `F`.

### Reversed contacts on the r stem

Let the r stem be oriented from the core to `r`, and `F` from
`p3` to `q3`. Suppose there are distinct stem vertices `x',x` and
distinct F vertices `y,y'`, in those respective orders, with edges
`x'y',xy`. Switch `r,q3`; let the new R consist of the old core
and P stems, followed by the r-stem prefix ending at `x'`, the edge
`x'y'` and `F[y',q3]`. Let the new F be

    F[p3,y] + yx + old r-stem segment x--r.

These are disjoint admissible bags with exactly the same remaining
P roots. Both open intervals `(x',x)` and `(y,y')` are released.
Minimality therefore permits this reversal only when both intervals
are empty. The argument retains an entire triangle core if one is
present. Contacts sharing an endpoint are not covered by this rule.

## The remaining global construction

The explicit swaps above strictly reduce a finite parameter whenever
their stated forbidden intervals are nonempty. They do not eliminate
all web cells. In particular, none yet handles a cell whose reserved
neighbours all lie on F: three H gates and four F neighbours give an
actual boundary of order seven, consistent with seven-connectivity.
A path through that cell between two F contacts need not be shorter
than the F segment it replaces. No valid reduction of this remaining
configuration, preserving the two root bags or the colouring data,
has been proved.

Even an actual planar `H0` would leave the induced graph on the two
reserved paths to be coloured compatibly with `u`. Their union is
not asserted bipartite, and the vertices `r,p3,q3` need not have one
colour. Thus planarity of the remainder alone is not a six-colouring
of `G`. No whole-case closure or induction is asserted.

In the original contraction-critical host, a sufficient terminal is
the weaker statement `chi(G-{u,r})<=5`. Indeed the only common
neighbours of `u,r` are the three vertices of `D-{r}`. In a proposed
five-colouring choose a colour absent from those three vertices.
Recolour the independent set of u-neighbours having that colour with
a fresh sixth colour; give u the freed colour and r colour six. The
recoloured set has no r-neighbour, so this colours G properly. This is
the [existing selected-edge reduction](hc7_degree7_exceptional_construction_working.md#4-scope-of-the-negative-findings),
not a new theorem. An apex description of `G-{u,r}` would suffice,
but has not been constructed.
