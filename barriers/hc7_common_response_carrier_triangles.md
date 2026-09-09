# Three common-response carrier triangles do not force Q

**Status:** explicit counterexample with a written proof and
[separate internal audit](hc7_common_response_carrier_triangles_audit.md).
No computation is a premise. Put `Q=K7−2K2`, with independent missing edges.

## Refuted sufficient statement

The following data do not force a Q minor: a vertex v whose neighbourhood
is exactly two disjoint triangles A,B and an edge xy; connected
`W=G−N[v]` full to N(v); and one six-colouring of G−M, obtained by expanding
a colouring of the common-star contraction, in which all endpoints of
`M={a1a2,b1b2,xy}` have colour α and three alternative colours supply
loopless carrier triangles using all three named rows. This remains false
when the three two-colour systems intersect only at the six row endpoints.

## Construction and one fixed response

Let `A={a,a1,a2}` and `B={b,b1,b2}`. On the nine vertices
`{v}∪A∪B∪{x,y}`, put the two triangles, edge xy, and all eight edges
from v to the other vertices. For each `j=1,2,3`, add vertices p_j,q_j,r_j
with neighbourhoods, before adding z,

`N(p_j)={a1,b1}`, `N(q_j)={a2,x}`, `N(r_j)={b2,y}`.

Finally add z adjacent to all nine p_j,q_j,r_j and to a,b. There are no
other edges. Thus G has 19 vertices, N(v) induces exactly `2K3∪K2`, and
W is the z-centred star on ten vertices. It is connected and contacts
every vertex of N(v).

Use six distinct colours `α,β1,β2,β3,δ,ε` on G−M as follows:

- a1,a2,b1,b2,x,y receive α;
- p_j,q_j,r_j receive β_j;
- v,z receive δ;
- a,b receive ε.

Every edge of G−M has differently coloured ends. This is an actual
common-star response. Contract the connected set
`D={v,a1,a2,b1,b2,x,y}` to d. Colour d by α and leave every other vertex
as above; this properly six-colours G/D. Expanding D in colour α and
then recolouring v to δ gives precisely the displayed colouring of G−M.

For each j, the subgraph of G−M induced by colours α,β_j consists of
exactly the three vertex-disjoint paths

`a1–p_j–b1`, `a2–q_j–x`, `b2–r_j–y`.

The rows a1a2, b1b2 and xy join these three components cyclically.
Consequently their component quotient is a loopless triangle using all
of M. For different j the systems intersect exactly at the six
α-coloured endpoints. All their internal vertices lie in W, and none
uses v,a,b.

## A tree decomposition of width four

Begin with the path of bags

`T1={a1,a2,x}`, `T2={a1,x,y}`, `T3={a1,y,b2}`, `T4={a1,b2,b1}`.

Attach `{a1,a2,a}` to T1 and `{b1,b2,b}` to T4. Add v to all six bags.
For every j, attach `{a1,b1,p_j,v}` to T4, `{a2,x,q_j,v}` to T1,
and `{b2,y,r_j,v}` to T3. Finally add z to every bag.

These bags cover every vertex and edge of G. Each vertex occurs on a
connected subtree: this is immediate for each p_j,q_j,r_j,a,b; the
occurrences of a1,x,y,b2,b1,a2 follow the displayed base path and its
attached bags; and v,z occur throughout. Every bag has at most five
vertices. This is therefore a tree decomposition of width at most four.

For completeness, such a decomposition excludes a K6 minor. In a clique
minor model, the bags of the decomposition meeting one connected branch
set form a subtree. Adjacent branch sets give intersecting subtrees.
Subtrees of a tree have the Helly property, so six pairwise adjacent
branch sets would all meet one decomposition bag, requiring at least six
distinct vertices there.

Q contains a K6 minor: if its missing edges are rs and tu, contract the
present edge rt. The merged vertex is universal, and the other five
vertices form a clique. Hence this G has no Q minor.

## Unaffected scope

The graph has a proper four-colouring: colour each triangle with colours
1,2,3 so that a,b receive 1; colour x,y by 1,2; give v and every
p_j,q_j,r_j colour 4; and give z colour 2. The literal clique `{v}∪A`
shows `χ(G)=4`. Also every p_j,q_j,r_j has degree three, so `δ(G)=3`
and `κ(G)≤3`.

All proper minors are six-colourable: the displayed decomposition has
width at most four, treewidth does not increase under minors, and a
graph of treewidth at most four is five-colourable. Thus proper-minor
six-colourability alone does not repair this sufficient statement.

The counterexample does not satisfy the actual simultaneous assumptions
`κ(G)≥7`, `δ(G)≥8`, and `χ(G)=7`. In particular its one common response
does not supply universal nonextension of six-colourings. It refutes the
stated response-and-carrier implication, not the actual critical C19
case, HC7, or a construction using those additional hypotheses.
