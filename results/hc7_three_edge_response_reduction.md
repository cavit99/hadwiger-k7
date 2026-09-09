# Three-edge responses reduce to three-connected cores

**Status:** written proof with a [separate internal audit](hc7_three_edge_response_reduction_audit.md).
The terminal minor construction below is conjectural, not a proof of C19.

## Statement

All graphs are finite and simple. Call `(H,F,c)` a response if H is
five-chromatic, F consists of three distinct edges, and c properly
four-colours `H−F` with colours
`α,β1,β2,β3`, giving every endpoint of F colour α. For each i, form an
auxiliary multigraph whose vertices are the αβi-components of `H−F`
and whose edges are F between those components. Require its nonisolated
part to be a loopless triangle. Parallel edges and loops are retained
when testing this condition.

Write `H+` for H with a new vertex v adjacent precisely to `V(F)`.
The three edges need not form a matching: their possible nonisolated
graphs are `3K2`, `P3 union K2`, `P4` and `C3`, where Pk has k vertices.
Indeed, every F vertex has degree at most two, since all its incident
edges map to edges at one vertex of a quotient triangle.

**Theorem.** Every response has a response `(J,F',c')` such that J is
three-connected and vertex-critical five-chromatic, and `J+` is a minor
of `H+`. The apex v remains a singleton in this minor representation.
Every reduction strictly decreases the core order. The three marked
edges remain distinct, but their endpoint roles may merge or change.

Thus it suffices, for the following stronger conjectural target, to treat
three-connected vertex-critical responses:

> Every response has `Q=K7−2K2` as a minor of H+, with independent
> missing edges in Q.

For the original loopless matching response, H+ is a subgraph of the
actual critical host. Proving this stronger target would close that
response case. It would not by itself close the cases with quotient loops.

## Critical reduction and boundary colourings

Deleting any e in F leaves a path in each quotient triangle. Swapping
α,βi on one side of a bipartition of this auxiliary graph properly
four-colours `H−e`. Consequently every induced five-chromatic subgraph
P contains every F endpoint and all three F edges.

Choose such a P vertex-critical. Restrict c to `P−F`. Components can
split but cannot acquire an F loop. A three-edge loopless quotient which
was not a triangle would be bipartite; its component swaps would
four-colour P. Thus P retains the response, with fresh carrier paths
if necessary. Passing to P is a subgraph operation preserving v and
its neighbours. If P is proper, its order decreases.

We may therefore assume H vertex-critical. It is two-connected: proper
pieces of a disconnected graph or a graph with a cutvertex could be
four-coloured and their palettes aligned. Suppose `{x,y}` is a two-cut.
It is nonadjacent, since colourings of two proper sides could otherwise
be aligned on their differently coloured ports.

Split the components of `H−{x,y}` into two nonempty groups, and let A,B
be the induced sides including x,y. Both sides are four-colourable.
Each admits at least one of the boundary relations E (equal colours at
x,y) and D (different colours). Their relation sets are disjoint,
otherwise palettes could be aligned to four-colour H. They are therefore
the opposite singleton sets `{E}` and `{D}`. This concerns every
four-colouring of each fixed side.

## All marked edges on one side

Suppose A contains all of F; B has no F edge. If `c(x) != c(y)`, B
forces D. Set `J=A+xy`, with the original F. This graph is five-chromatic:
four colours would give the forbidden D colouring of A, while adding
one edge to a four-colourable graph costs at most one new colour.

The added edge is proper in c. If it affects an αβi-component, its port
colours are α,βi. There is an αβi path from x to y in B: otherwise a
component swap in the proper colouring `c|B` would give B an E colouring.
Thus the added edge only joins vertices already in one global component.
It cannot introduce an F loop absent from the old quotient. The new
loopless three-edge quotient must again be a triangle, since J is not
four-colourable.

If `c(x)=c(y)=t`, B forces E. Identify x,y in A, colour the merged vertex
t and call the result J. It is not four-colourable, because that would
give an E colouring of A. It is at most five-colourable: four-colour A
and give the merged vertex a fresh colour.

For every other colour s, B contains a ts path between its ports;
otherwise a component swap gives a D colouring of B. If t=α, the
identification therefore merges vertices already connected in every
old αβi layer. If t=βi, this applies to the only layer containing the
ports. No new F loop can appear. Nor can two F edges become parallel:
this could occur only for α ports with two F edges to the same other
vertex, which would already give parallel edges in every old quotient.
The three F edges remain distinct, the induced colouring of `J−F` is
proper, and non-four-colourability again forces all three quotient
triangles.

Both operations have fixed minor lifts through B. For adding xy, contract
all but one edge of an x–y path with interior in B into x. For identifying
the ports, contract the whole path. Such an internal path exists because
every component of the two-cut meets both ports in the two-connected H.
The path interior contains no F endpoint. Port identification may merge
two old endpoint roles, but every new F endpoint has a preimage containing
an old one, hence remains adjacent to v. Delete the other discarded
vertices and unwanted edges. In either case the core order decreases.

## Marked edges on both sides

Suppose both sides contain an F edge. In any αβi layer, a component
meeting both sides must meet the cut. If there is at most one such
component, the two nonempty groups of quotient edges meet in at most
one quotient vertex; their union cannot be a triangle. Choose βi avoiding
every non-α port colour. This shows that both ports must have colour α.
The same argument shows that x,y lie in different global components
in every αβi layer.

Name the equality-forcing side A and the difference-forcing side B.
Set `J=A+xy` and `F'=F[A] union {xy}`. Adding the edge makes J exactly
five-chromatic. The restriction of c properly colours `J−F'` and gives
all F' endpoints colour α. No F' loop can appear: the old edges were
loopless and the ports were in distinct global components.

There are at most three F' edges. Its quotient must be nonbipartite,
otherwise a component swap four-colours J. A loopless nonbipartite
multigraph with at most three edges is a triangle. Thus A contains
exactly two old F edges, B exactly one, and F' has three distinct edges.
This proves that J is a response, even when its marked edges share ports.

It remains to realise both the added xy edge and the new apex contacts
without reusing their preimages. Write pq for the sole F edge in B.
If p,q are outside the cut, they lie in one connected component D of
`H−{x,y}`. There are two disjoint paths from `{x,y}` to `{p,q}` in
`H[D union {x,y}]`, with pairing unrestricted. Otherwise Menger gives
a separator of at most one vertex. Since D meets both ports, deleting
that separator from the whole H would disconnect an outside endpoint
from the remaining port, contradicting two-connectivity.

Stop the paths at p,q and use their vertex sets as the x/y preimages;
use `{v}` for the apex. Edge pq joins the two path bags, and vp,vq give
both apex contacts. If `pq=xq`, instead use `{x}` and a q–y path in
`D union {y}`; the symmetric case is identical. Edge xy itself is
impossible, since the two-cut was nonadjacent. Every other retained
vertex is a singleton. These preimages are disjoint and connected;
they retain all edges of A and every required apex contact, including
those to an old F endpoint at a port. Discard the other vertices and
edges. This represents J+ as a minor of H+ and strictly reduces order.

Repeated critical reductions and two-cut reductions terminate by core
order. The terminal response is vertex-critical and three-connected.
Composing the fixed disjoint preimages lifts any minor it contains,
proving the theorem.

## The path case reduces to the triangle case

**Proposition.** If `F={ab,bc,cd}`, identifying a,d gives a triangle
response J which is a minor of H+. Thus proving the conjectural target
for triangle responses also proves it for path responses.

**Proof.** In each quotient triangle the successive vertices a,b,c,d
belong to component classes A,B,C,A. They are nonadjacent in H, since
both have colour α and ad is not marked. Identify a,d to q. Every
colouring of the resulting graph J pulls back to H, so `χ(J)>=5`.
The colouring c descends to `J−{qb,bc,cq}`. No distinct αβi components
merge, and its three marked edges form a loopless triangle in every
quotient. Deleting one marked edge permits four colours by a component
swap; restoring it costs at most one colour. Hence `χ(J)=5`.

In H+, contract `{v,a,d}` to q. The extra edges from v become qb,qc,
which are already marked edges of J. All other vertices retain singleton
preimages, so this realises J exactly and lowers the core order by one.
For a triangle response, a Q model in J+ also exists in J, by the
simplicial-vertex argument below. Its fixed lift therefore gives Q in H+.
This step consumes v; it does not assert a singleton-apex lift. QED

## Remaining terminal construction

The theorem preserves the stated response class, not seven-connectivity
or seven-chromaticity of an auxiliary graph. It deliberately does not
preserve six distinct original endpoint roles. Neither loss is hidden in
an application of the conjectural target: that target concerns only Q
as an unrooted minor of the explicitly defined H+.

The `F=C3` terminal case requires Q already in H. Here v is simplicial
on a triangle. It cannot be a singleton Q bag, since Q has minimum
degree five. Removing v from any other bag preserves its connectivity
and contacts, using edges within its neighbour triangle where necessary.
Thus adding v cannot create a Q minor. No construction in this terminal
class, nor an induction through three-cuts, is proved here.
