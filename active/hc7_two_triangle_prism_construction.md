# A maximal complementary component beside three triangle-to-triangle paths

**Status:** construction draft with written proofs below and a
[separate scoped internal audit](hc7_two_triangle_prism_construction_audit.md).
The global rerouting and the whole two-triangle case remain open.

## Exact host and scope

Let G be finite and simple, seven-connected, of minimum degree at least eight,
with `chi(G)=7` and every proper minor six-colourable. Assume G has no
`Q=K7-2K2` minor. Let v have degree eight, with
`N(v)=A dotcup B dotcup {x,y}`, where A and B are triangles and xy is an edge.
Retain the audited absence of a four-cycle in `G[N(v)]`; other neighbourhood
edges are allowed. The remaining cases have `chi(G-N[v])` equal to five or six.
The exact standing and inputs are in the
[designated frontier](hc7_k44_closure_frontier.md#75-a-neighbourhood-contact-construction).
The deductions below use connectivity, degree and the displayed literal edges;
they do not yet exploit proper-minor colourability.

Put `F=G-v`. A linkage means three vertex-disjoint A--B paths, using all six
distinct terminal vertices and no other A/B vertex internally. End pairings are
free. A vertex is **vital** for this linkage problem if every such linkage
contains it. This term does not prescribe the pairings or uniqueness of paths.

## A terminal certificate

**Claim.** Suppose a linkage `P1,P2,P3` in F has a complementary component C
meeting `{x,y}`. If P1 and P2 each contain two distinct vertices adjacent to C,
and P3 contains at least one, then G contains Q. Path endpoints count as contacts.

**Proof.** Write ai,bi for the A and B ends of Pi. On each of P1,P2, choose
an edge between its first and last C-neighbours, and split there into connected
bags containing its A and B ends. Each of these four bags contacts C.
The A-triangle and B-triangle edges, together with the two split-path edges,
give a four-cycle on the four bags. The whole of P3 is a fifth bag adjacent
to all four through the remaining triangle edges. These five bags form W4.
They all contact C and the singleton v; moreover v contacts C through x or y.
Thus the seven disjoint original-host bags give `K2 join W4=Q`. QED

The same allocation allows a useful weaker contact condition. If an actual
edge adds one missing rim diagonal, the five core bags form `K5-e`. C may then
miss the whole P3 bag: that possible missing pair is disjoint from the remaining
rim hole, so the seven bags still give Q. This does not assert such a diagonal.

## Maximise the component containing both ports

The graph `F-{x,y}` is four-connected. Menger's theorem gives a linkage there:
a cut of at most two cannot separate the surviving A and B terminals.
Consequently at least one linkage avoids x,y, whose literal edge places them
in the same complementary component. Choose such a component C of maximum
order over all linkages avoiding x,y, and put `H=F-C`, `D=N_F(C)`.

**Claim.** Every vertex of D is vital in H.

**Proof.** If a linkage in H avoids w in D, its complement in F has an
x,y-containing component containing `C union {w}`. This contradicts maximality.
All A/B terminals are vital as well. In particular, nonvital vertices of H
belong to `G-N[v]` and have no neighbour in C. QED

## Every vertex of H is vital

**Claim.** With this same maximal C, every linkage in H spans H.

**Proof.** Split every vertex u of H into `u-`, `u+`, with a capacity-one arc
`u- -> u+`. For each edge uw, add `u+ -> w-` and `w+ -> u-` of capacity M; add
`s -> a-` and `b+ -> t` for a in A and b in B, also of capacity M, where
`M>|V(H)|+3`. The maximum flow is three. Fix an integral maximum flow given
by three simple linkage paths, without circulating flow.

Use its residual directed graph. A vertex used by this flow is nonvital
exactly when its two copies lie in one residual strongly connected component
(SCC). Indeed its reverse capacity arc then lies on a residual directed cycle,
which permits a unit circulation reducing its usage. Conversely the difference
from a maximum flow avoiding it decomposes into residual cycles and includes
such a cycle. Vertices unused by the chosen flow are already nonvital.

The source sides `X_A={s} union {a-:a in A}` and
`X_B=V(network)-({t} union {b+:b in B})` are minimum cuts of capacity three.
They are unions of residual SCCs and satisfy `X_A subseteq X_B`.
Pass from X_A to X_B by adding one SCC at a time, always keeping the source
side closed under outgoing residual arcs. Every resulting cut is minimum.
Its three crossing capacity-one arcs correspond to a three-vertex cut
`S(X)={u:u- in X, u+ not in X}` of H.

First exclude a reverse state `u+ in X, u- not in X`. For every H-neighbour
w, the two capacity-M arcs force `w- in X` and `w+ not in X`; hence every
neighbour lies in S(X) and `d_H(u)<=3`. A used vertex cannot be in reverse
state, because its reverse capacity arc is residual. Thus u is nonvital,
misses C and v, and has `d_G(u)=d_H(u)<=3`, contrary to the degree hypothesis.

Every nonvital vertex must therefore have both copies in the same SCC.
Otherwise it is unused by the chosen flow, so its forward capacity arc is
residual: its out-copy must enter the chain before its in-copy, giving the
excluded reverse state. Neither copy is already in X_A or excluded from X_B,
since nonvital vertices are not terminals.

Consider an SCC-addition step, from X to X'. Let Z be the vertices whose
two copies enter at that step. They are nonvital. For a neighbour w outside Z
of some z in Z, the capacity-M arcs imply `w+ not in X` and `w- in X'`.
If `w- in X`, then w belongs to S(X). Otherwise its in-copy enters at this
step; its out-copy does not, since w is outside Z, so w belongs to S(X').
Thus `N_H(Z) subseteq S(X) union S(X')`, of order at most six.
The vertices of Z miss both C and v. A nonempty Z would therefore be separated
from C in G by at most six vertices, contrary to seven-connectivity.
Every SCC step has Z empty, and no nonvital vertex exists. QED

## First missing inference

The normalisation gives one fixed partition `V(F)=C dotcup V(P1) dotcup
V(P2) dotcup V(P3)` for every linkage in H. Six-connectivity of F gives
`|D|>=6`. These facts do not distribute D over the three paths: profiles such
as `(4,1,1)` or `(6,0,0)` do not satisfy the terminal certificate.
Vitality and the minimum-cut chain alone do not imply balanced contacts.

The remaining obligation is a global rerouting, permitted to replace all paths,
the component, the selected marks and the final bags, that either supplies one
Q model or yields a six-colouring of G. A reroute through C must track which
old C vertices it consumes, connect the released path vertices to the same
remaining component, and retain every contact used by its final seven bags.
No improving exchange or closed decreasing reduction is proved here. Both
exterior chromatic cases and the complete C19 implication remain open.
