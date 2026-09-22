# A six-clique model with two singleton triangle roots

**Status:** preserved working proof, not separately audited. This earlier
sufficient construction is superseded in the critical-host application by
the [audited whole-case theorem](../results/hc7_two_triangle_case_closure.md).
Its more general statement below remains a separate unaudited claim.

## Statement

Let J be a five-connected graph, and let P={p1,p2,p3} and
Q={q1,q2,q3} be vertex-disjoint literal triangles. Edges between P and Q
are allowed. Suppose J has a K6 model with {p1} and {p2} as branch sets.
Then J has a K5 model whose five branch sets all meet T=P union Q.

In the original critical host, such a model extends to a K7 model by
adding {u} and {r}: these vertices are adjacent to each other and to
every vertex of T. The statement also applies with P and Q interchanged.

All graphs and paths below are finite. A linkage between two vertex sets
consists of pairwise vertex-disjoint paths with distinct ends in each
set; a shared source and target may give a one-vertex path. We use the
vertex form of Menger's theorem, allowing a separator to contain source
or target vertices.

## A spanning four-bag partition

Put R=J-{p1,p2} and p=p3. The graph R is three-connected. The other
four branch sets of the K6 model are connected, pairwise adjacent, and
each has a neighbour at both p1 and p2. Absorb every component of the
unused vertices of R into one adjacent branch set. Such a neighbour
exists because R is connected. The four enlarged bags partition R;
they retain all their adjacencies and both singleton contacts. Name the
bag containing p by D and the other bags by A,B,C.

If Q meets at least two of A,B,C, use those two bags and D together
with {p1},{p2}. Thus we may assume that Q either lies wholly in D,
lies wholly in one helper A, or meets both D and A and no other helper.

In the next two sections contract B and C to vertices b and c, leaving
every other vertex of R intact. Seek a three-path linkage from
{b,c,p} to Q. Whenever it exists, lift its b-path by including all of B,
its c-path by including all of C, and retain the p-path as the third
bag. These three connected bags are disjoint, each meets Q, and they
are pairwise adjacent through the literal Q edges. The first two keep
their p1,p2 contacts; the third has them through p. Together with the
two singleton bags this gives the required model.

If the linkage does not exist, let S be a source--target separator of
order at most two. If S avoids b and c, it lifts unchanged to a cut of
R of order at most two: a source and a target survive, and the two
contracted bags are connected. This contradicts three-connectivity.
Deleting both b and c does not separate p from Q, since D and A are
connected and adjacent. Deleting just b or just c also fails, by the
same observation. Consequently every failed linkage has a separator

    S={b,z} or S={c,z}.

We may exchange B and C and use the first form. Here z is an actual
vertex outside B and C; no whole branch set is being counted as one
actual separator vertex.

## Q meets both D and A

A p--Q path inside D avoids b, so z must belong to D. A path from C
to Q using an edge from C to A and then only A avoids b and D, so z
must belong to A. This is impossible. Therefore the three-path linkage
exists and the preceding construction finishes this case.

## Q is contained in A

The path from C to Q through A shows that z belongs to A. In the
contracted graph with b and z deleted, let F be the component containing
Q-{z}. This component is well defined because Q-{z} contains at least
two adjacent vertices. The connected bags C,D, and p, lie outside F:
they survive the separator and C,D are adjacent. The boundary of F in
the contracted graph is contained in {b,z}.

Consider the graph induced by F union {b,z}. It has two disjoint paths
from {b,z} to distinct vertices of Q. Here are the separator details.
The vertex z has a path to Q in this graph: use a path in A from z to
Q, or the one-vertex path if z belongs to Q. The vertex b has a
neighbour in F; otherwise F would have actual R-boundary contained in
{z}, contradicting three-connectivity. As F is connected, b therefore
has a path to Q-{z} avoiding z. Thus neither b nor z is a one-vertex
source--target separator. Any other such separator w would leave a
component containing a surviving Q vertex and avoiding both b and z.
Since F has no outside neighbours except b,z, that component would have
actual R-boundary contained in {w}, again impossible. Menger gives the
claimed two paths.

Choose a C--Q path consisting of an initial vertex of C followed by
vertices of A. It meets z. Its prefix up to z avoids D, and all its
vertices before z lie on the C-side of the separator, outside F.
Enlarge C by this prefix and the z--Q path just obtained. Enlarge B
by the lifted b--Q path. Keep all of D intact. The two paths on the
F-side are disjoint, and the C-prefix meets that side only at z, so
these three bags are disjoint and connected. B and C now meet distinct
Q vertices, while D contains p. Their old pairwise contacts and their
p1,p2 contacts all survive. They give the required five bags.

## Q is contained in D

For each of the three pairs of helpers chosen from {A,B,C}, contract
only that pair and seek three disjoint paths from its two images and
p to Q. A successful linkage finishes exactly as above. Suppose all
three choices fail.

For a failed pair the separator classification again gives {h,z},
where h is the image of one selected helper H and z is an actual
vertex. The p--Q path inside D forces z to belong to D; z=p is
allowed. The other selected helper is a surviving source, and it is
adjacent to the unselected helper. Thus neither of these two connected
helpers meets the component containing Q-{z} after the separator is
deleted. Since D,A,B,C partition R, that component is exactly the
component F_z of R[D]-z containing Q-{z}. In particular,

    p is not in F_z,
    N_R(F_z) is contained in H union {z}.

The Q-sides F_z arising from different failures are nested. To see this
directly for two distinct gates z,w, choose q in Q-{z,w} and a p--q
path in D. Both gates lie on that path, because each separates p from
q in D, with a gate equal to p regarded as the first vertex. Suppose
z occurs before w. Then z lies on the p-side of D-w. The connected
set F_w therefore avoids z and contains q, so F_w is contained in F_z.
Equal gates give equal Q-sides.

If two failures have different exceptional helpers H and H', take
their smaller nested Q-side F_z. Its helper neighbours must lie both
in H and in H', because it is contained in the other Q-side and all
helpers are outside D. There are therefore no helper neighbours at
all, and

    N_R(F_z) is contained in {z}.

The set F_z is nonempty and the helpers lie outside it, contradicting
three-connectivity of R. Hence every failed pair would have to use
the same exceptional helper. This is impossible for all three pairs
{A,B}, {A,C}, {B,C}, whose intersection is empty. At least one
three-path linkage exists, finishing the last case and the proof.

## A four-colour deletion application

Suppose additionally that chi(J)=6. If deleting the ends a,b of any edge
of P or Q leaves a four-colourable graph L, the theorem applies.
Indeed chi(L)=4, since colouring a,b with two new colours shows that
chi(L)>=4. Put C=N_J(a) intersect N_J(b). In every four-colouring of L,
C meets all four colours. Otherwise choose a colour i missing C,
recolour the colour-i neighbours of a with colour 5, give a colour i,
and give b colour 5. The recoloured set is independent and avoids
N_J(b), so this would five-colour J.

Martinsson--Steiner, [Theorem 1.3](https://arxiv.org/html/2209.00594v1#S1),
gives a C-rooted K4 in the four-chromatic graph L: its four disjoint
connected bags each meet C. The primary statement and its definition
of a rooted minor were inspected. Adjoining {a},{b} gives precisely
the K6 model required above. Thus an unclosed six-chromatic instance
has chi(J-{a,b})>=5 for every edge within either triangle. No such
four-colouring is assumed to exist in the general instance.

## A joint cap-edge colouring response

The following working deductions use the original critical graph `G`:
it is seven-connected, seven-chromatic, every proper minor is six-colourable,
and `N(u)=P union Q union {r}`, with anticomplete triangles `P,Q` and
`r` adjacent to every vertex of `T=P union Q`. Put `J=G-{u,r}` and
assume there is no `T`-meeting K5 in J. These deductions hold in both
chromatic branches; they do not themselves exploit `chi(J)=6`.

**The common-neighbour exit.** For an edge `ab` of P, there are at most
two common neighbours of a,b in J. Otherwise choose three of them.
Three-connectivity of `J-{a,b}` gives three disjoint paths from that
three-set to Q. The paths are pairwise adjacent through Q, and each
touches a and b. Together with `{a},{b}` they give a T-meeting K5.
The same assertion holds for every edge of Q. Thus every cap edge has
at most four common neighbours in G, including u,r and its third cap
vertex p. In the prism representation its ends have at most one common
neighbour in E.

Consequently `chi(G-{a,b})=6`. Indeed, in any five-colouring of that
graph a colour i misses the common neighbourhood. Recolour the colour-i
neighbours of a with a new sixth colour, give a colour i and b colour
six. The recoloured set is independent and avoids b, so this six-colours
G, a contradiction. The upper bound follows from proper-minor criticality.

**Simultaneous expansion.** Fix any six-colouring of `G/ab`, with the
contracted vertex coloured 0. Expand it to a colouring of `G-ab`, where
only ab is monochromatic. Let D be the other colour-0 vertices. They
are independent and anticomplete to `{a,b}`. For each colour i other
than 0, choose a shortest a-b path in the subgraph on colours 0,i,
with ab omitted. Such a path exists: otherwise interchanging the colours
on the component of a repairs ab and six-colours G.

If i occurs on a common neighbour, choose the length-two path through
one such vertex. In particular choose u,r,p for their three distinct
colours. For each path let `w_i` be its last vertex before b, and let
`A_i` be its prefix ending immediately before `w_i`. Put `A=union A_i`.
Then:

- A is connected and contains a, while b is outside A;
- the five vertices `w_i` are distinct, outside A, and adjacent to both
  A and b; they include u,r,p;
- `A-{a}` is anticomplete to b.

Here every prefix contains a. Different paths intersect internally only
at vertices of D, since their other colours differ; each `w_i` has its
own nonzero colour and was omitted from its sole path prefix. This proves
disjointness from A. Shortestness excludes a b-neighbour earlier on a
path, proving the last assertion. This direct prefix union is the
singleton-end case of the two-tree allocation used in earlier work; no
new matroid theorem is needed.

There are one or two colours absent from the original common neighbourhood.
Only their paths enlarge A beyond a. With one absent colour, A is an
induced bipartite path; with two, it is the union of two alternating
path prefixes and is at most three-colourable. In either case u,r,p are
preserved, and at least three of the new common neighbours lie in J.
Vertices of Q, however, may belong to A.

**A chromatic consequence, not an induction.** In the one-absent-colour
case, `chi((G-b)/A)=6`. More generally, this holds with b replaced by
any vertex z outside A whose neighbours in A lie in one bipartition
class. A five-colouring of `(G-z)/A` would lift by giving that class
the contracted vertex's colour, and the other class and z a new sixth
colour. All neighbours outside A avoid the contracted colour, and z
misses the new-colour class. This would six-colour G. The proper-minor
upper bound gives equality. If A avoids Q, then u also contacts A only
at a, so `chi((G-u)/A)=6` as well. Neither quotient inherits the original
seven-critical hypothesis.

## Why the joint response has not closed the case

The new common neighbours would finish by three disjoint paths to Q in
`J-(A union {b})`. The expansion and those paths have not been selected
jointly. If Q survives but the linkage fails, Menger gives a separator
of order at most two in this residual graph. Its lifted boundary can
also contain the whole of A and b; it is not a small cut of J.

The original host does give three-connectivity of `J-P` and `J-Q`.
For example, after deleting at most two vertices from `J-P`, the surviving
Q vertices lie in one component. Any other component X is root-free and
has `N_J(X)` contained in P and those two deleted vertices, contrary
to the six-neighbour bound. But this does not preserve connectivity
after the prescribed expansion is deleted. A topological bypass may use
other colours and cease to be an eligible colouring response.

Shortest path length also fails to orient the natural cap switch. If a
Q edge e on the alternating a-b path separates a from b in the entire
two-colour graph with ab omitted, flip one component after deleting e.
This repairs ab and makes e monochromatic, giving a colouring of G/e.
The cycle consisting of the old path and ab supplies the new bridge
after e is removed. Its length is unchanged, and reversing the switch
recovers the original response. Without the separator condition even
this transfer is unjustified. With two absent colours, the prefixes
can also intersect in D; their valid union supplies no additional lift.

An earlier proposed separator exchange was withdrawn before use: full
components on either side of a separator inside four bags can themselves
contain parts of retained bags. Taking the whole components therefore
does not establish disjointness. Similarly, deleting the contracted
vertex's whole colour class does not make the common neighbourhood
five-colourful: a proposed recolouring can conflict with other vertices
of that deleted class. Neither assertion is a proved terminal case.

## Remaining global obligation

In the selected critical-host branch, chi(J)=6 supplies an ordinary K6
minor. The proof above does not make two vertices of P or Q singleton
in such a model. A root-bag part can carry the only contacts to two
helpers, so moving that part can destroy the retained model; neither
a simultaneous transfer nor a colouring repair has been proved for
general models. This is still an unresolved global construction, and
no closure of the six-chromatic branch or of HC7 is claimed here.
