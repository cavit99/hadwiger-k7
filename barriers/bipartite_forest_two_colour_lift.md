# Forest contractions need not admit a two-colour expansion

**Status:** explicit counterexample to an intermediate colouring claim;
checked directly below, not separately audited. It does not refute
bipartite contractibility or HC7.

## Statement refuted

In a properly coloured bipartite scheme, disjoint spanning forests in
one shore's graphic projections need not yield host branch sets which
can be restored using two colours. A forest in a projection is not a
forest in the actual induced host graph.

## Construction

Take target K2,3 with roots a,b,q1,q2,q3. Add six distinct nonroots
s,t,w,x,y,z. Use the paths

| Target edge | Path |
| --- | --- |
| a q1 | a-x-s-q1 |
| a q2 | a-y-s-q2 |
| a q3 | a-z-t-q3 |
| b q1 | b-x-w-q1 |
| b q2 | b-y-w-q2 |
| b q3 | b-z-w-q3 |

The host consists of their edges and the additional edges zx,zy.
Give a,s,t colour a; b,w colour b; x colour q1; y colour q2; and z
colour q3. Roots have their own target colours. This is a proper
colouring, including on the two additional edges.

This is a scheme. The paths meeting at s have common endpoint a;
those meeting at w have common endpoint b. At x,y,z the common
endpoints are q1,q2,q3 respectively. All other intersections are at
their incident roots, or on the single a-q3 path at t. No prescribed
root is internal to a path. Additional host edges do not change this
path-membership condition.

In the a projection, x,y label parallel a-s edges, and z labels a-t.
In the b projection, x,y,z label parallel b-w edges. A disjoint pair
of spanning trees must therefore allocate z and exactly one of x,y
to the a tree, and the remaining label to the b tree.

If a receives x, its actual branch set {a,s,t,z,x} contains the
triangle a-z-x-a. If it receives y, {a,s,t,z,y} contains a-z-y-a.
Every full-rank allocation in this orientation thus has a branch set
which is not two-colourable. This fails independently of which
six-colouring a later quotient returns.

## Unaffected scope

The allocated branch sets are still disjoint and connected and still
give the prescribed rooted minor. The graph itself has the displayed
five-colouring. The example is not a seven-connected critical host.
It leaves open a different orientation, a repair using more colours,
or a simultaneous change of allocation and exterior colouring. Any
such repair must prove its own colouring lift and strict progress.
