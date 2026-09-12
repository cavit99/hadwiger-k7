# A neighbourhood colouring that extends across one exterior class

**Status:** written proof; two separate internal audits accompany this source.
This closes the stated four-chromatic exterior branch, not Conjecture 19 or HC7.
No finite computation is a premise of the proof.

All graphs are finite and simple. Write `Q=K7-2K2`, with the deleted
edges independent, and write `K5^-` for K5 with one edge deleted.

**Theorem.** Let G be seven-connected, have minimum degree at least eight,
and have no Q minor. Suppose v has degree eight and

`N(v)=A dotcup B dotcup {x,y}`,

where A and B are triangles, xy is an edge, and `G[N(v)]` has no
four-cycle. Extra neighbourhood edges are allowed. Put `W=V(G)-N[v]`.
Then `G[N(v)]` has a proper three-colouring in which every vertex of W
sees at most two colours. Consequently

`chi(G) <= max{4, chi(G[W])+2}`.

In particular, under these structural hypotheses, `chi(G)>=7` implies
`chi(G[W])>=5`. Proper-minor colourability is not needed for this deduction.

## Pinned input and contact restrictions

We use [contraction closure](../active/hc7_companion_contraction_closure.md),
source SHA-256
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
with its [separate GREEN internal audit](../active/hc7_companion_contraction_closure_audit.md),
SHA-256 `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
Corollary 6 excludes a literal K5^- after contracting any nonempty
connected set of at most three vertices, including a singleton.
Corollary 3 says that outside any literal four-clique R, every vertex
has at most two R-neighbours; if an outside vertex w has two, every
outside neighbour u of w satisfies `N(u) intersect R subseteq N(w) intersect R`.
The hypotheses of both corollaries hold in G.

For w in W put `S(w)=N(w) intersect N(v)`. Call S(w) large if its size
is at least three. For every triangle T in `G[N(v)]`, a large S(w) meets
T in at most one vertex. Indeed `R={v} union T` is a four-clique and
w misses v. Three T-neighbours are forbidden by Corollary 3. If w has
exactly two T-neighbours, largeness supplies a neighbour u in `N(v)-T`.
This u lies outside R and sees v, contradicting the same corollary.

For every `z in N(v)-A`, define its A-support to comprise its literal
A-neighbours and all A-vertices sharing a W-neighbour with z. This
support has size at most one. Otherwise choose two distinct supported
A-vertices and at most two witnessing W-neighbours. Together with z
these witnesses form a connected set C of order at most three, disjoint
from `R={v} union A`. The set C sees v and both supported vertices.
Contracting C therefore leaves R intact and creates a fifth vertex with
three R-neighbours, a literal K5^-, contradicting Corollary 6. Literal
contacts require no witness; the same argument includes those cases.
The symmetric assertion holds for B-support.

It follows that the relation between A and B consisting of literal edges
and pairs sharing a W-neighbour is a matching: each endpoint has at most
one partner by its support bound. In particular, whenever a large S(w)
contains an A-vertex and a B-vertex, they form one pair of this matching.

Four-cycle freeness gives two further elementary restrictions. There is
at most one literal A--B edge: two with a common endpoint form a
four-cycle using the third vertex of the opposite triangle; two with
distinct endpoints form one using an edge of each triangle. All edges
between `{x,y}` and either triangle meet at most one triangle vertex.
Two neighbours of one port give a four-cycle through the third triangle
vertex; neighbours at distinct vertices of the two ports give one using xy.

## The complete contact classification

A large contact set contains at most one vertex of A and at most one of
B. Thus its possible forms, for `a in A,b in B`, are

`{a,b,x}, {a,b,y}, {a,x,y}, {b,x,y}, {a,b,x,y}`.

Let F_A and F_B be the triangle vertices occurring in any large contact
set. There are exactly the following alternatives:

1. Each of F_A and F_B has size at most one.
2. The distinct large contact sets are exactly `{a1,b1,x}` and
   `{a2,b2,y}`, where `a1!=a2` and `b1!=b2`.

To verify exhaustiveness, suppose a large set contains both x and y.
If it contains a in A, both ports' A-supports equal `{a}`, so no large
set uses another A-vertex. All large sets also using B have the same
B-vertex: sets containing a use its unique matching partner, whereas a
set of the form `{b,x,y}` fixes both ports' B-supports. If there is no
set using both A and B, the latter form itself fixes the sole possible
B-vertex. The argument is symmetric when the starting set uses B only.
This proves alternative 1. Otherwise only the first two displayed types
remain. Each occurs with at most one pair, by the port support bounds.
If both occur, the matching makes their pairs either identical or disjoint,
giving alternative 1 or 2 respectively. Empty families are in alternative 1.

## Colouring the neighbourhood

Set `x=1,y=2`. In alternative 1, call each member of F_A or F_B marked
and forbid colour 3 at marked vertices. Consider either triangle. Its
port edges meet at most one vertex p. If p sees both ports, it cannot be
marked: a large contact set containing p contains a port and hence meets
the literal triangle `{p,x,y}` twice. Thus the triangle can be coloured
respecting the port edges and its at-most-one marked vertex.

More precisely, a specified triangle vertex has a singleton set of
attainable colours only in two cases: it sees both ports, forcing 3;
or it is marked and sees exactly one port, forcing the other colour in
`{1,2}`. To check this, with no port edges every vertex has at least two
choices. With only a colour-1 port edge at p, p has choices `{2,3}`,
or just `{2}` if marked. In the latter case the other vertices each
have `{1,3}`; otherwise a marked vertex different from p has `{1,2}`
and the third vertex has all three choices. A colour-2 port edge is
symmetric. With both port edges, p has `{3}` and the others `{1,2}`.

The two triangle colourings are independent except for the possible
single A--B edge ab. Its endpoints can receive distinct attainable
colours unless both attainable sets are the same singleton. If both
are forced 3, their double port adjacencies give the four-cycle
`a-x-b-y-a`. Otherwise a and b are marked and see the same port z,
so `{a,b,z}` is a literal triangle. A large contact set containing a
contains either b or both ports, because b is the only possible B-mark.
It therefore meets that triangle twice, a contradiction. Distinct
endpoint colours can consequently be chosen and extended within the
triangles. Every large set now avoids colour 3.

In alternative 2, write `A={a0,a1,a2}`, `B={b0,b1,b2}`. The matching
restriction permits only `a0b0,a1b1,a2b2` as the possible cross-edge.
Port support permits only `xa1,xb1,ya2,yb2` as literal port edges.
At most one of `xa1,ya2` exists, and similarly for B, by the restriction
on attachment vertices. Use the following complete list of constructions.

- With no cross-edge, give `a0,b0` colour 3, `a1,b1` colour 2, and
  `a2,b2` colour 1.
- With cross-edge a1b1, give `a2,b2` colour 3 and `a1,b1` opposite
  colours 1,2, avoiding their possible x-edge. They cannot both see x:
  their large contact set would contain the literal triangle `{a1,b1,x}`.
  Complete each triangle with its remaining colour. The case a2b2 is
  symmetric, exchanging x,y and indices 1,2.
- With cross-edge a0b0, at least one of the pairs `{a1,b1}`, `{a2,b2}`
  has at most one edge to its corresponding port, since there are at
  most two port edges altogether. Give that pair opposite colours 1,2,
  avoiding its possible port edge, and the other pair colour 3 on both
  vertices. Complete the triangles. The colours of a0,b0 are opposite,
  so their edge is proper.

Every construction respects all neighbourhood edges, and each large
contact type sees at most two colours. Sets of size at most two do so
automatically. This proves the asserted neighbourhood colouring.

## Extending the colouring

Put `k=chi(G[W])`. If `k<=1`, colour N(v) as above and give W and v
a fourth colour; W is independent and v has no W-neighbour. If `k>=2`,
choose a whole class I of a proper k-colouring of W. Colour `W-I` using
`k-1` old colours and N(v) using three disjoint fresh colours. Each
vertex of I receives a fresh colour absent from its neighbourhood in
N(v); these independent choices are compatible because I is independent.
They cannot conflict with W-I, whose palette is disjoint. Give v any
old colour, since all its neighbours use fresh colours. This is a proper
`k+2`-colouring of G, proving the theorem. QED
