# The residual set behind the reserved-core ports is connected

**Status:** written proof; a separate internal audit records the exact reviewed
source revision beside it. This does not close the two-triangle case.
All graphs are finite and simple. Write `Q=K_7-2K_2`, with independent
deleted edges. All contacts below are actual edges between disjoint bags.

**Theorem.** Let `G` satisfy the current two-triangle critical-host
hypotheses: seven-connectivity, minimum degree at least eight, no Q minor,
chromatic number seven and six-colourability of every proper minor. Let
`d(v)=8` and `N(v)=A dotcup B dotcup {x,y}`, where A and B are triangles
and xy is an edge. Choose `a in A,b in B` so `{a,b,x,y}` induces only xy.
For a maximised reserved core as specified below, if both B ports are
nonroots, its residual set D is nonempty and connected.

## Exact input and notation

Use the maximised-reserved-core deduction in
[the critical-host frontier, Section 7](../active/hc7_k44_closure_frontier.md#7-the-critical-host-global-construction),
at the historical revision Git `7bbcacb`,
SHA-256 `a7b7289d3e090414824b6d67b9abd5d456aadb765a2245bff3991c5783d6f5ea`.
Its [scoped audit](../active/hc7_k44_critical_global_construction_audit.md) has SHA-256
`bd435dc374da1b58ba39ee77aa8f0414abf6245f51a2f287dbede3f8558148b8`.
That input uses the whole-class reservation and separately audited boundary
exclusions; no further external theorem is invoked here.

Write `A={a,a1,a2}` and `B={b,B1,B2}`. In
`F=G-{v,a,b,x,y}`, start with a rooted K4 at `a1,a2,B1,B2`, maximise
the union M of its two A-rooted bags, then minimise its B-rooted bags.
Denote the A bags by U,V, interchanging their names so b contacts U.
The input supplies the following exact properties:

* U,V are disjoint and connected, each contains its own A root, and
  they are adjacent. Both contact a and v.
* Each B bag is a path `P_i` from Bi to a common port pi contacting
  both U and V. The two paths and M are pairwise disjoint.
* The ports `p1,p2` lie in `W=V(G)-N[v]` in the present case. Put
  `D=(G-v-B)-(M union {a,x,y,p1,p2})`. This set is nonempty; every
  component C of D contacts all five vertices `a,x,y,p1,p2` and
  at least two of the three actual B roots.

In particular each C misses at most one B root. No connectedness of D
or retained colouring of M is assumed.

## Three components give the forbidden model

**Proposition 1.** The residual set D has at most two components.

**Proof.** Suppose D has distinct components `C1,C2,C3`. The two bags

`X=U union {b,p1}`,     `Y=V union {v,p2}`

are connected and adjacent. Both contact a, B1, B2 and each chosen C:
use the A-triangle and v-edges for a, the B-triangle and v-edges for
B1,B2, and the respective ports for C. All sets used below are disjoint
from these two bags unless expressly replaced in the last case.

If each of B1,B2 is missed by at most one chosen component, take the
five core bags

`C1 union {a}`, `C2 union {x}`, `C3 union {y}`, `{B1}`, `{B2}`.

The first three are connected and pairwise adjacent because every C
contacts a,x,y. The last two are adjacent. The only possible core holes
join a C bag to B1 or B2; they have distinct C ends, since each C misses
at most one B root, and distinct B ends by this case's hypothesis.
X and Y are full to all five core bags. These seven bags contain Q.

Otherwise some `Bi`, with `i in {1,2}`, is missed by at least two
chosen components. Relabel these as C1,C2, and put `{i,j}={1,2}`.
If C3 contacts Bi, keep X,Y and take instead

`C1 union {x}`, `C2 union {y}`, `C3 union {Bi}`, `{Bj}`, `{a}`.

Each union is connected. The first two bags are adjacent and contact
the third through x,y; they contact Bj because C1,C2 miss Bi. The third
contacts Bj through the literal B edge. The a bag contacts all three
C bags. Thus the only possible core hole is a--Bj. Both X,Y are full
to the five core bags, again giving Q.

Finally suppose all three chosen components miss Bi. Every internal
vertex of `P_i` lies in D: the path avoids M, the deleted vertices of F,
the other B root and its port. If there are internal vertices, they form
one connected set in a D component adjacent to Bi. That component is
different from each chosen C, since those miss Bi. Consequently `P_i`
is disjoint from C1,C2,C3, including when it is a single edge.
Replace the two extra bags by

`X'=U union V(P_i)`,     `Y'=V union {v,pj}`.

They are connected and adjacent. Use the core bags
`C1 union {a}`, `C2 union {x}`, `C3 union {y}` and the two singleton
roots in `B-{Bi}`. These five bags form K5: each chosen C contacts both
remaining B roots. X' and Y' contact every C bag through pi,pj and
both B roots through Bi,v. This is a K7 model, hence contains Q.

The cases exhaust every contact pattern of three components. The old
path is used only in the last case, after its disjointness from all
allocated components has been proved. Thus D has at most two components.
The one- and two-component cases and the case of two root ports remain
unresolved by this argument. QED

## A shared omission in the two-component case

**Corollary 2.** Under the theorem's hypotheses and notation, if D has
exactly two components C1,C2, then for each `i in {1,2}` at least one
component contacts Bi. This corollary does not address an omission of b.

We additionally use
[edge-contraction closure, Theorem 1](../active/hc7_companion_contraction_closure.md),
source SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
whose [audit](../active/hc7_companion_contraction_closure_audit.md) has SHA-256
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`;
and [the four-root packet, Lemma 1](hc7_two_triangle_exterior_helpers.md#1-a-four-root-packet),
source SHA-256 `b3fe07ea52e0e553c61edb59cd5b7da3719ae834d8803f21afb9bde90fc410a8`,
whose [audit](hc7_two_triangle_exterior_helpers_audit.md) has SHA-256
`e9bc147d6c0e48bba395dc5fe590ef8a8cc778914804e3c1f5d33c48e2eec628`.
The packet gives a rooted K4 when every nonempty nonroot subset has
at least four neighbours and every nonroot has degree at least six.

**Proof.** Suppose both components miss Bi, and put `{i,j}={1,2}`.
The root Bi also misses M, because its nonroot port is its root bag's
only contact to M. Its only possible neighbours are the eight vertices

`{v,a,b,Bj,x,y,p1,p2}`.

Minimum degree eight forces all eight contacts and `d(Bi)=8`.
No vertex `w in D` can contact all of a,x,y. Otherwise contract the
actual edge va. The five vertices `va,Bi,x,y,w` in the quotient span
K5 with only Bi--w missing: the merged vertex sees all four others,
Bi and w both see x,y, and xy is an edge. This contradicts the
edge-contraction exclusion of a literal K5-minus subgraph.

Take the actual induced graph

`F1=G[C1 union {b,Bj,p1,p2}]`.

Its only deleted neighbours of C1 are a,x,y. Every vertex loses at
most two neighbours by the preceding exclusion, so its degree in F1
is at least six. For every nonempty `T subseteq C1`, v survives outside
T and its G-boundary, giving `|N_G(T)|>=7`. Hence
`|N_F1(T)|=|N_G(T)-{a,x,y}|>=4`. The four-root packet gives a fresh
K4 model in F1 rooted at b,Bj,p1,p2.

Adjoin the three bags `M`, `C2 union {a}`, and `{v,Bi}`. They are
connected, pairwise disjoint and disjoint from the fresh core. They
are pairwise adjacent through the edges from a and v to the A roots
in M, and the edge av. The second bag is full to the core through
C2's four root contacts; the third is full through v's B contacts
and Bi's forced port contacts. M contacts p1,p2,b, so its only possible
core omission is the Bj-rooted bag. The seven bags therefore form
K7 with at most one missing contact, and contain Q. No old root path
is used in this construction. This proves the corollary. QED

## A component cannot miss the omitted B root

We first allow one degree-five exception in the four-root packet used
above. This uses the same pinned four-root alternative and reduction
argument, with the following degree and endpoint checks.

**Lemma 3.** Let Z be four roots of a graph F, with nonempty nonroot
set T. Suppose every nonempty subset of T has at least four external
neighbours, every vertex of T has degree at least five, and at most one
has degree five. Then F has a Z-rooted K4 model.

**Proof.** Choose a counterexample of minimum nonroot order. It has
at least three nonroots: with one nonroot the maximum degree is four;
with two it is five, whereas at least one must have degree at least six.
The boundary of T makes every root adjacent to T.

If a root has only one nonroot neighbour, absorb that neighbour into
the root. As in the pinned packet proof, every surviving nonroot degree
and boundary cardinality is unchanged. The same holds for the paired
root absorption in its order-two trisection: each open root has exactly
the two nonroot separator neighbours, and the two roots absorb different
ports. These operations keep all four root preimages separate, preserve
the single-exception bound, and strictly decrease nonroot order. Their
surviving nonroot sets are nonempty; a surviving set of order one or two
would contradict the same degree count. Thus each root may be assumed
to have at least two nonroot neighbours, and the trisection alternative
is excluded. A small separation with a nonempty root-free side contradicts
the four-neighbour hypothesis, exactly as in the pinned proof.

In the remaining planar alternative, the boundary argument in that proof
makes F two-connected. A facial cycle through the four roots contains
h nonroots, so Euler's bound and the root-incidence count give

`2e(F)<=6|T|+10-2h`,

`2e(F)>=6|T|-1+8+max(0,8-2h)`.

The lower bound exceeds the upper by at least five. The only remaining
four-root alternative is the required rooted K4. QED

**Corollary 4.** Every component of D contacts b.

**Proof.** At most one vertex of D sees all three of a,x,y. Otherwise
contract va. For two such vertices w,w', the five vertices
`va,x,y,w,w'` span K5 with only ww' possibly absent, contradicting the
pinned edge-contraction closure.

Suppose a component C misses b. In the actual induced graph

`F_C=G[C union {B1,B2,p1,p2}]`,

its only deleted neighbours are a,x,y. Every nonroot therefore has
degree at least six except possibly the one vertex just identified,
whose degree is at least five. For every nonempty subset of C, the
original boundary has order at least seven, since v remains outside
both the set and its boundary. Deleting a,x,y leaves at least four
neighbours. Lemma 3 gives a fresh K4 model rooted at B1,B2,p1,p2.

Adjoin the p1-rooted bag to U and the p2-rooted bag to V, retaining
the two fresh B-rooted bags. These four connected bags are disjoint;
the actual edges from each pi to its A bag connect the enlarged bags.
The fresh K4 supplies all their B contacts, and the original U--V edge
retains the A contact. This is an A1,A2,B1,B2-rooted K4 in the same
graph `G-{v,a,b,x,y}`. Its A-bag union contains M and both previously
excluded ports, contradicting the defining maximality of M. The old
B-root paths are discarded, and no colouring of M is retained or used.
Thus every component contacts b. QED

## Opposite omissions in two components

**Corollary 5.** If D has exactly two components, at least one contacts
all three vertices of B.

**Proof.** By Corollaries 2 and 4, the only contrary possibility, after
relabeling, is that C1 misses B2 and C2 misses B1. For `i in {1,2}`,
the actual graph

`F_i=G[Ci union {b,Bi,p1,p2}]`

deletes only a,x,y from the neighbours of Ci. The degree and boundary
counts in Corollary 4 therefore apply: every nonroot has degree at least
six except possibly one of degree five, and every nonempty nonroot set
has at least four neighbours. Lemma 3 gives a K4 model in F_i rooted
at b,Bi,p1,p2.

Discard both b-rooted bags. Unite the two p1-rooted bags, and separately
the two p2-rooted bags; each union is connected through its actual port.
Keep the B1-rooted bag from F1 and the B2-rooted bag from F2. These four
bags are disjoint: the constituent hosts meet only in b,p1,p2, and each
retained bag avoids the other three roots of its model. The constituent
models supply both port contacts of each Bi bag and the contact between
the two port bags. The literal edge B1B2 supplies the remaining contact.
Thus this is a fresh K4 model rooted at B1,B2,p1,p2.

Append its port bags to U,V as in Corollary 4. The four original roots
A1,A2,B1,B2 remain fixed in separate bags, while the A-bag union strictly
contains M. This contradicts the same maximality. Both b-rooted bags
and all old B-root paths are discarded. QED

## Two components are impossible

**Theorem 6.** Under the standing hypotheses, the residual set D in the
two-nonroot-port case is connected, proving the opening theorem.

**Proof.** The input makes D nonempty, and Proposition 1 leaves at most
two components. Suppose there are two, C1,C2.

If one component, say C1, misses a B root, Corollary 4 makes it Bi for some `i in {1,2}`,
and Corollary 5 makes C2 full to B. Put `{i,j}={1,2}`. As in
Corollary 5, Lemma 3 gives a fresh K4 rooted at b,Bj,p1,p2 in
`G[C1 union {b,Bj,p1,p2}]`: only a,x,y were deleted from the component's
neighbourhood. Adjoin the three bags

`X=U`, `Y=V union {v,Bi}`, `Z=C2 union {a}`.

They are connected, disjoint from each other and the fresh core, and
pairwise adjacent through U--V, a's U contact and av. X contacts the
b and both port bags; it can miss only the Bj bag. Y contacts both
port bags through V and both B bags through v. Z contacts all four
core bags through C2, which is full to B and both ports. These seven
bags contain K7 with at most one missing contact, hence Q.

Otherwise both components are full to B. The four bags
`C1 union {p1}`, `C2 union {p2}`, `{B1}`, `{B2}` form a rooted K4:
each port union is connected and meets both B roots, their mutual
contact uses C1--p2, and B1B2 is literal. Append the two port bags to
U,V. This preserves the original four roots in separate connected
bags in `G-{v,a,b,x,y}` and strictly enlarges M, a contradiction.

Neither construction retains an old B-root path. Thus D has exactly
one component. Its allocation and the two-root-port case remain open;
the earlier invalid path-reuse argument is not invoked. QED
