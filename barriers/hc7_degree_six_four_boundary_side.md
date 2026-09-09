# Degree six and a four-vertex boundary do not give the five-root packet

**Status:** written counterexample; a [separate exact-source audit](hc7_degree_six_four_boundary_side_audit.md) is recorded beside it.
No finite computation or external structural theorem is a premise.

Put `Q=K7-2K2`, with the two missing edges independent. The following
proposed side statement is false: five roots `{b,c,r,s,t}` containing
the triangle rst, nonempty nonroots all of degree at least six, and
boundary at least four for every nonempty nonroot subset force either
a Q minor or a rooted K5 with at most one hole, incident with a triangle
root and one of b,c. Additional global hypotheses of the actual
seven-connected critical host are not refuted.

## Construction

Start with the seven-vertex graph G0 whose edges are exactly the
triangle rst, the clique on `K={b,c,p,q}`, and `ps,pt,qr,qt`.
Thus p misses r, q misses s, and neither b nor c sees r,s,t.

Define a planar graph P on twelve vertices
`c,l,u0,...,u4,w0,...,w4`, with indices modulo five. Its edges are

```text
u_i u_(i+1),  w_i w_(i+1),  u_i w_i,  u_i w_(i-1),
c u_i,       l w_i                         (0<=i<5).
```

This is the icosahedron graph: its two pentagons bound a triangulated
annulus, and c,l cap the two boundary pentagons. This describes a
plane embedding with `c u0 u1` a facial triangle. Every vertex has
degree five. Identify `u0=p,u1=q`, and let H be the cone over P with
apex b. Finally take `G=G0 union H`, identifying exactly the clique K;
there are no other identifications or edges.

The five prescribed roots are `S={b,c,r,s,t}`. The nonroot set is
`D=V(P)-{c}`, of order eleven. The nine new vertices form
`E=V(P)-{c,p,q}`. The graph G has sixteen vertices and forty-nine edges.

## Degrees and boundaries

The vertices p,q each have degree eight: their five P neighbours,
b, and their two neighbours in rst. Every vertex of E has degree six,
consisting of its five P neighbours and b. Thus every nonroot has
degree at least six. The root degrees are respectively `12,6,3,3,4`
for b,c,r,s,t. In particular this is not a seven-connected host.

For completeness, P is three-connected. If at most two deleted
vertices leave both poles c,l, every surviving pentagon vertex meets
its pole, and some cross-edge between the pentagons remains. If one
pole is deleted, at most one other vertex is deleted; every surviving
vertex of its pentagon retains a neighbour in the other pentagon,
whose surviving pole connects it. If both poles are deleted, the two
intact pentagons and their cross-edges are connected. This proves
connectivity after every deletion of at most two vertices. Consequently
H is four-connected: either b survives and connects everything, or
deleting b leaves at most two further deletions from P.

Let `X subseteq D` be nonempty. If X meets `{p,q}`, its boundary
already contains the at least five G0-neighbours of
`X intersect {p,q}` outside that intersection. Those vertices lie
outside X because the only nonroots of G0 are p,q. Otherwise `X subseteq E`.
All four vertices of K are outside X. A boundary of size at most three
in H would leave a K vertex outside `X union N_H(X)`, contradicting
four-connectivity of H. Thus `|N_G(X)|>=4` in all cases. Equality
occurs for E itself: `N_G(E)=K`. Also `N_G(D)=S`, so every root
contacts the nonroot side.

## No admissible rooted model

First consider G0. In an admissible model each helper bag must contact
at least two triangle bags. A singleton helper can do this only if
p,q occupy two distinct triangle bags, since it has no triangle-root
neighbour. Both helpers would then be singleton and both would miss
the third triangle bag, giving two holes. Hence neither helper can
be singleton. The only two nonroots must therefore be assigned one
to each helper. The resulting bags miss r and s respectively, again
giving two holes. This also covers models leaving vertices unused
or assigning both nonroots to one bag. G0 has no admissible model.

Every S-rooted model in G projects to G0. Delete E from each bag.
The remainder contains its original root. Any portions previously
connected through E each contain a port in K; the literal clique K
connects these portions within the same bag. If an interbag contact
used E, both participating bags own distinct K ports, and their
clique edge restores that contact. The restricted bags are disjoint,
connected and retain all five roots and all required contacts. An
admissible model in G would therefore give one in G0, a contradiction.

## No Q minor

The graph Q is five-connected: after deleting at most four vertices,
at least three remain, and a complete graph minus a matching on at
least three vertices is connected. It is nonapex: deleting any vertex
leaves six vertices with thirteen or fourteen edges, exceeding the
planar bound twelve. Therefore the apex-planar graph H has no Q
minor. Indeed, deleting the bag containing b from any minor model
leaves a minor of P; if b is unused, the entire model lies in P.
The graph G0 also has no Q minor: it has seven vertices and only
thirteen edges, whereas Q has nineteen.

Here is the projection argument for their four-clique sum. In a
hypothetical Q model in G, at most four bags meet K. Deleting their
vertices from Q leaves a nonempty connected graph. Each remaining
bag lies entirely in one of `G0-K` and `H-K`, and there are no edges
between these two sides. Thus all remaining bags lie on the same
side. Restrict every K-meeting bag to that side together with K.
Its pieces are connected by the clique edges on its own K ports;
contacts lost through the other side are replaced by edges between
distinct owned ports. All contacts involving a bag disjoint from K
are already on the retained side. This gives a Q model wholly in
G0 or wholly in H, both impossible.

The example rules out repairing the five-root side packet merely by
combining relative boundary four, nonroot minimum degree six and
Q-freeness. It does not supply a seven-connected, minimum-degree-eight,
seven-chromatic critical graph, and does not settle C19 or HC7. A valid
application must use additional information from the full host.
