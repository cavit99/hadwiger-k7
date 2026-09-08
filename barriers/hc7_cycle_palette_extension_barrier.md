# Counterexamples to unrestricted cycle-palette extensions

Status: explicit counterexamples; written proof. See the adjacent audit for
the exact independently reviewed revision and scope.

Write \(Q=K_7-2K_2\), with the two deleted edges independent. The following
claim is false: every five-colourable, \(Q\)-minor-free graph containing an
induced five-cycle has a five-colouring using only three colours on that cycle.
The first example is apex. The second also excludes \(P=K_7-3K_2\), with
three independent deleted edges, and has root-induced graph exactly
\(C_5\mathbin{\dot\cup}K_2\). Both satisfy the quantified seven-root palette
condition described below. No computation is a premise of either proof.

## The planar disk

Let \(D\) have boundary \(C=c_0c_1c_2c_3c_4c_0\) and four interior vertices
\(u,v,w,z\). Its interior edges are \(uv,uw,uz,vw,vz\). The remaining edges are

\[
u\{c_0,c_1,c_2\},\qquad v\{c_3,c_4\},\qquad
w\{c_2,c_3\},\qquad z\{c_0,c_4\}.
\]

Here \(xT\) denotes all edges from \(x\) to \(T\). There are no other edges.
This is a triangulated disk: its eleven inner faces are

\[
uc_0c_1, uc_1c_2, uc_2w, wc_2c_3, wc_3v, vc_3c_4,
vc_4z, zc_4c_0, zc_0u, uvw, uvz.
\]

For example, place \(u,v\) above and below a common interior edge, \(w,z\)
to its left and right, and the boundary vertices in their displayed cyclic
order. The faces form a disk with precisely the stated outer boundary.

**Disk claim.** In a proper four-colouring of \(D\) for which \(C\) uses
three colours, the colour appearing only once on \(C\) occurs at \(c_3\)
or \(c_4\); both possibilities extend.

Indeed, a three-coloured five-cycle has colour multiplicities \(2,2,1\).
If the singleton occurs at \(c_0,c_1,c_2\), respectively, the boundary colours
can be named as follows:

| Singleton | \((c_0,c_1,c_2,c_3,c_4)\) | Forced \(u,v\) | Impossible vertex |
|---|---|---|---|
| \(c_0\) | \((C,A,B,A,B)\) | \(D,C\) | \(w\) |
| \(c_1\) | \((A,C,B,A,B)\) | \(D,C\) | \(w\) |
| \(c_2\) | \((A,B,C,A,B)\) | \(D,C\) | \(z\) |

In each row the last vertex has neighbours of all four colours. For singleton
\(c_3\), boundary \((A,B,A,C,B)\) extends by
\((u,v,w,z)=(D,A,B,C)\); for singleton \(c_4\), boundary
\((A,B,A,B,C)\) extends by \((D,A,C,B)\). This proves the claim.

## Gluing two disks and adding an apex

Glue two copies of \(D\) along their boundary cycles, one on each side. In the
second copy send its boundary vertex \(c_i\) to the common vertex \(c_{i+2}\),
with indices modulo five. Denote the resulting planar graph by \(J\).
Its two sets of four interior vertices are disjoint. Thus \(J\) has thirteen
vertices and thirty-three edges, and the common cycle is induced.

The first disk allows only singleton positions \(\{3,4\}\) in a three-coloured
boundary; the second allows only \(\{0,1\}\). These sets are disjoint, so no
four-colouring of \(J\) uses three colours on \(C\). A four-colouring does
exist: colour the common boundary \((A,B,A,C,D)\), the first disk's
\((u,v,w,z)\) by \((C,A,B,B)\), and the second disk's own
\((u,v,w,z)\) by \((B,D,C,C)\). Every listed edge has distinct endpoint colours.
Consequently \(\chi(J)=4\).

Let \(H\) be obtained from \(J\) by adding a universal vertex \(p\). Then
\(|V(H)|=14\), \(|E(H)|=46\), and \(\chi(H)=5\). In every proper five-colouring,
the colour on \(p\) is absent from \(J\), so \(C\) uses exactly four colours.

The graph \(H\) has no \(Q\) minor. Every minor of an apex graph is apex:
if a model uses the apex, deleting its branch set leaves a minor of the planar
remainder; if it does not, the whole model is planar. But \(Q\) is not apex.
It has nineteen edges and maximum degree six, so deleting any one vertex
leaves at least thirteen edges on six vertices, exceeding the planar bound
twelve. The graph \(Q\) itself is also nonplanar.

Choose \(q\) to be any one of the eight interior vertices of \(J\). The seven
roots \(V(C)\cup\{p,q\}\) are distinct and \(pq\) is an edge. In every
five-colouring of \(H\), these seven roots use all five colours, while \(C\)
uses at least four. Thus the full quantified palette condition alone, even
together with \(Q\)-minor exclusion, does not force a \(Q\) minor inside \(H\).

## Colour-forcing gadgets also exclude \(P\)

For two existing distinct vertices \(x,y\), an inequality gadget consists of
a private four-clique \(L\), a private vertex \(z\), all eight edges from
\(\{x,z\}\) to \(L\), and the edge \(zy\). The edge \(xy\) is absent.
In every proper five-colouring, the four colours on \(L\) force \(x,z\)
to have the same fifth colour, so \(x,y\) have different colours. Conversely,
every assignment of distinct colours to \(x,y\) extends: give \(z\) the
colour of \(x\) and give \(L\) the other four colours.

Start with seven roots \(c_0,\ldots,c_4,p,q\), inducing exactly \(C\) and
\(pq\). Add seven pairwise internally disjoint inequality gadgets for
\[
c_1c_3,\ c_1c_4,\ c_2c_4,\ pc_1,\ pc_2,\ pc_3,\ pc_4.
\]
Call this graph \(H_*\). It has forty-two vertices and 111 edges. The
five-colourings restricted to its roots are exactly the five-colourings of
the virtual root graph obtained by adding the seven displayed edges.
In that virtual graph, \(\{c_1,c_2,c_3,c_4,p\}\) is a five-clique. Thus
every five-colouring of \(H_*\) uses all five colours on the seven roots,
and at least four on the induced cycle \(C\). Such a colouring exists:
give \((c_1,c_2,c_3,c_4,p)\) five distinct colours, give \(c_0\) the colour
of \(c_2\), and give \(q\) the colour of \(c_1\); extend each gadget as
above. Each gadget contains a five-clique, so \(\chi(H_*)=5\).

Nevertheless \(H_*\) has neither a \(P\) nor a \(Q\) minor. Add the seven
virtual edges, forming a supergraph \(H_*^+\). It is the union, along
two-vertex cliques, of its seven-vertex virtual root graph (thirteen edges)
and seven seven-vertex gadget torsos (sixteen edges each). None of these
pieces has a \(P\) or \(Q\) minor: a seven-vertex target model on seven
vertices has only singleton bags, whereas the targets have eighteen and
nineteen edges, respectively.

For completeness, a three-connected target minor in a union along a clique
\(S\) of size at most two lies in one of its pieces. At most two model bags
meet \(S\). If bags avoiding \(S\) occur on both sides, the target vertices
corresponding to the bags meeting \(S\) form a separator of order at most
two, a contradiction. Restrict the model to the side containing all bags
avoiding \(S\). Its remaining bags stay connected: any excursion through
the other side has both ends in the clique \(S\). Any lost contact between
two bags meeting \(S\) is restored by the clique edge. Iteration proves
localization in one piece. Both \(P,Q\) are at least three-connected, so
this applies to \(H_*^+\) and hence to its subgraph \(H_*\).

## Scope

The apex example does contain \(P=K_7-3K_2\), where the three deleted edges are
independent. Write \(U,V,W,Z\) for the second disk's interior vertices. In
\(J\), the six connected disjoint bags
\[
\{c_0,c_1,z,u,v\},\quad \{c_2,c_3,c_4,w\},\quad
\{U\},\quad\{V\},\quad\{W\},\quad\{Z\}
\]
have all contacts except the first bag with \(U\), the second with \(V\),
and \(W\) with \(Z\). They form an octahedral minor; adding the singleton
apex \(p\) gives \(P\). Thus this example does not refute the analogous
cycle-colouring assertion under \(P\)-minor exclusion.

The apex example alone does not refute the \(P\)-free version; the gadget
example does. Neither realizes the original seven-contraction-critical host
or preserves its seven-connectivity, minimum degree eight, independent-class restoration,
or all proper-minor colouring responses. In particular, the apex example
contains a literal \(K_5\) minus an edge (the apex and an interior diamond),
and every inequality gadget contains a literal \(K_5\). Both violate the
literal \(K_5\)-minus exclusion already available in the actual critical host.
These examples do not refute a suitable rooted near-clique conclusion from
the quantified palette condition. The global
Hadwiger and companion-minor objectives remain unresolved.
