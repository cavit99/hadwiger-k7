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

## Every linkage has a path missing C

The normalisation gives the partition `V(F)=C dotcup V(P1) dotcup
V(P2) dotcup V(P3)` for every linkage in H. Each Pi is induced: a chord
would bypass an internal vertex, contrary to vitality. Also `|D|>=6`.
Indeed, if `|D|<=5`, deleting D in the six-connected F leaves both C and
some of the six terminals in H.

**Claim.** If all three paths of a linkage in H meet D, then G contains Q.
Consequently every linkage in H has a path anticomplete to C.

**Proof.** Two paths with at least two contacts give the first terminal
certificate. Otherwise the contact counts are `(h,1,1)`, with `h>=4`.
Orient the heavily contacted path P from A to B; let f,l be its first and
last contacts. Write t1,t2 for the sole contacts on the other paths.

Suppose an edge uw joins a vertex u of P strictly before l to a vertex w
strictly after ti on a lightly contacted path. Split P between the later
of u,f and l, and the light path between ti and w. Their four endpoint bags
form the usual rim. The edge uw adds the diagonal from the A-half of P to
the B-half of the light path. The untouched third path is the hub and meets C.
All five core bags meet C except possibly that light B-half. The sole possible
remaining core hole joins the B-half of P to the light A-half, so it is
independent of the possible C--light-B hole. Together with v the bags give Q.
Reversing both path orientations proves the same conclusion for an edge from
a vertex of P strictly after f to a light-path vertex strictly before ti.

In a Q-free host, the open interval Z=P(f,l) can therefore meet either light
path only at its ti. Since P is induced and every C-neighbour lies in
`Z union {f,l,t1,t2}`, we obtain
`N_G(C union Z) subseteq {v,f,l,t1,t2}`.
Each light path has distinct A and B ends, so at least one end survives
outside that five-set and C union Z. This contradicts seven-connectivity. QED

## Exchanges within H

For this fixed H choose a linkage maximising the number of paths meeting D.
The claim bounds that number by two. A useful exchange retains every vertex:
if two paths have cross-edges pq and p'q', with p before p' and q' before q,
switching their tails along these edges skips both open intervals P(p,p')
and P'(q',q). Vitality forces p,p' and q',q to be consecutive. Thus the switch
preserves all vertices and has a valid inverse. If it divides the D-contacts
of one path between two new paths while the other old path misses D, it
increases the number of contacted paths, contrary to the chosen maximum.
This does not prove that such a switch exists.

**Two simultaneous switches give Q.** Split one path P0 at an edge pq,
with p nearer A. Suppose each other path Pi has an edge a_i b_i, oriented
from A to B, with the cross-edges p b_i and q a_i. The seven bags consisting
of v and the six endpoint halves give Q. Indeed, the two P0 halves and v
form a triangle. They are full to the other four halves: triangle edges
supply the same-end contacts, and the crossed edges supply the opposite-end
contacts. The other four halves form a cycle through the two split edges
and the A- and B-triangle edges. Thus the model is `K3 join C4=Q`, without C.

Consequently at most three vertices of the other two paths have neighbours
on both sides of any edge of P0. Two such vertices on one path must be
consecutive, and the reversed-pair argument forces their crossed edges to
the two ends of that P0 edge. Three on one path are impossible, since its
first and third would have to be consecutive. Two on both paths give the
terminal just proved. If P0 misses C, at most four vertices of G-P0 have
neighbours on both sides of a P0 edge: these three and possibly v.

## If only one path can meet C

Retain the same G,C,H and the maximisation just defined. Suppose its maximum
is one; write P for the contacted path and P2,P3 for the others.

**Claim.** Both ends of P meet C, and every internal vertex w of P has
`d_H(w)<=6` and at least two neighbours in C. For every noncut vertex c of C
other than x,y, its H-neighbours lie within three consecutive vertices of P;
in particular `d_C(c)>=5`.

**Proof.** Use the residual SCC chain from the normalisation. Each cut has
one current vertex on each path. A transition replaces old vertices O_i by
new vertices N_i. No vertex has both copies in one SCC, so O_i,N_i are
consecutive on their path and the SCC consists of the copies O_i+ and N_i-.

If the A end of P missed C, all three A ends would miss C. At the first
transition the nonempty fully processed set consists only of departing A
ends. Its G-boundary lies in the new three-cut together with v, separating
it from C by at most four vertices. This contradicts seven-connectivity.
Reversing the chain proves the assertion about the B end.

Within a transition the residual arcs are O_i+ to N_j- for actual edges
O_i N_j, and N_i- to O_i+ for the used path edges in reverse. Contracting
each matching pair gives a strongly connected directed graph on the changed
path indices. A transition changing P and another path has a directed cycle
through P. Replacing its matching edges by the cross-edges around that cycle
permutes intact suffixes and gives a spanning linkage. P's two pieces lie
on distinct new paths and contain its two C-contacted ends, contradicting
the maximum of one. Thus every transition changing P changes only P.

Fix an internal w of P. Let S_in be the cut just after w becomes current
and S_out the cut just before it ceases to be current. Both contain w.
Vertices processed entirely between these cuts lie on P2 or P3, since P
cannot advance while w is current. They are nonterminals and miss C and v.
Their external neighbours lie in `S_in union S_out`, of size at most five.
If there were any such vertices, this boundary would separate them from C.
Consequently P2 and P3 each advance at most once during this interval.

The cuts immediately before w enters and after it leaves exclude earlier
and later neighbours of w on P2,P3. Those two transitions change only P,
so every such neighbour is among the four positions of P2,P3 in S_in,S_out.
P is induced and supplies exactly two more H-neighbours. Hence `d_H(w)<=6`.
Since w misses v, minimum degree eight gives at least two C-neighbours.

Now let c be a noncut nonport vertex of C. All its H-neighbours lie on P.
If the first and last, p,q, have distance at least three along P, replace
P[p,q] by p-c-q. The other paths remain fixed. This consumes one C-vertex
and releases at least two vertices in the open interval I=P(p,q). Each
released vertex has a C-neighbour other than c. Since C-c is connected and
contains x,y, `(C-c) union I` lies in a new, strictly larger port component.
This contradicts maximality. Thus c has at most three H-neighbours within
a length-two subpath of P. It misses v, so `d_C(c)>=5`. QED

This rules out nonport leaves of C, but not larger endblocks. A path through
several C vertices can consume every C-neighbour of a released interval,
or disconnect its remaining neighbours from the ports.

## The remaining global construction

The remaining profiles are `(h,k,0)` with `h+k>=6`; k may be zero. The
[local shortcut barriers](../barriers/vital_linkage_local_shortcuts.md)
explain why vitality does not supply a separator avoiding the triangle roots,
and why ordered attachments cannot be dismissed by a degree bound. The latter
control fails global maximality of C and proper-minor criticality; both remain
available to the construction.

A reroute through C may replace all paths and final bags. It must either
produce a full Q model or give a six-colouring of G, with the consumed and
surviving pieces specified together. Neither an improving global exchange nor
a closed decreasing reduction is proved here. Both exterior chromatic cases
and the complete C19 implication remain open.
