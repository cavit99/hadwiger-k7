# A degree-five star does not split a rooted four-clique

**Status:** explicit counterexample to an intermediate construction;
[separate internal audit](hc7_degree_five_star_allocation_audit.md).
The five-chromatic, colourful-set hypothesis is not satisfied.

Write `Q6=K6-2K2`, with independent deleted edges. The following claim
is false: in a four-connected graph with disjoint root triangles A,B,
a nonroot y of degree five adjacent to nonadjacent roots a in A and b
in B, and a K4 rooted at the other four roots avoiding a,y,b, the six
roots necessarily admit a rooted Q6 minor.

## Construction

Start with the square of the cycle on 0,...,8: cyclic distance one or
two defines adjacency. Delete edge 18 and add vertex 9 with neighbours
0,1,3,8. Put

    A={5,6,7}, B={2,3,4}, a=7, b=2, y=0.

Then `N(y)={1,2,7,8,9}`, and ab is absent. The four bags

    {3,9,8}, {4}, {5}, {6}

are connected, pairwise adjacent and avoid a,y,b. Their triangle roots
remain distinct; edge 86 supplies the only contact not already literal
between these four roots.

The graph is four-connected. The original cycle square remains connected
after deleting at most three vertices: two breaks in the surviving cyclic
order would require two disjoint pairs of consecutive deleted vertices.
The modification splits its vertex 1 into adjacent vertices 1,9, each
retaining three original neighbours, with union {0,2,3,8}. A deletion of
at most three vertices leaving both split vertices contracts to a connected
original graph. If exactly one is deleted, the original graph minus 1 and
at most two other vertices is connected, and the surviving split vertex
retains a neighbour there. Deleting both leaves the original graph minus
1 and at most one further vertex, also connected.

## No rooted Q6

Every neighbour of root 4 or 5 is another root. Their bags must therefore
be singleton in any model rooted at all six prescribed vertices. The
pairs 7–4 and 2–5 are necessarily absent. They exhaust the two possible
missing contacts, so the other four bags must form a K4 rooted at
7,2,6,3 in the graph with 4,5 deleted.

That graph has a plane drawing with outer cycle

    0–2–3–9–8–6–7–0.

Draw chords 09,08,78 inside it, and put vertex 1 inside the quadrilateral
0,2,3,9, adjacent to all four corners. This accounts for every edge.
The four prescribed roots are cofacial. They remain cofacial under a
root-preserving minor, whereas K4 has no plane embedding with all four
vertices on one face. The required rooted K4, and hence rooted Q6, is
impossible. This excludes arbitrary connected bags, not merely a chosen
allocation of the displayed witness.

## What remains possible

A proper four-colouring, in vertex order 0,...,9, is

    (0,2,3,0,1,2,0,3,2,1).

No three-colouring exists: the consecutive triangles through 0,...,8
force a period-three colouring, in which vertex 9 sees all three colours.
Thus the graph is exactly four-chromatic. In the displayed colouring,
a,b are precisely the y-neighbours of their colour, so the colouring also
descends after contracting the whole star {a,y,b}.

The first invalid inference is that a fifth actual neighbour of y repairs
the split while preserving the four core bags' contacts. Four-connectivity
and the degree condition do not supply that allocation. A construction
using universal colourfulness in a five-chromatic subgraph remains open;
the counterexample has no such subgraph. Neither the critical-host case
nor the chromatic augmentation target is refuted.
