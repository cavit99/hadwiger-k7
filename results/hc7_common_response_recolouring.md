# Simultaneous recolouring of two matching carriers

**Status:** written proof with a [separate internal audit](hc7_common_response_recolouring_audit.md).
These deductions retain one colouring response. They do not construct the missing Q minor,
where `Q=K7−2K2` has independent missing edges.

All graphs are finite and simple. Let M be a three-edge matching in G,
and let c properly p-colour `G−M`, giving all six endpoints colour α.
Thus the only edges of G with equally coloured ends are those of M.

## 1. Shared vertices need not obstruct repair

Choose distinct colours β,γ different from α, an αβ-component C and
an αγ-component D of `G−M`. Suppose:

- C and D each contain exactly two endpoints of M;
- these endpoint sets are disjoint, neither contains an edge of M,
  and their union meets all three edges of M.

**Lemma 1.** If no edge joins the β-coloured vertices of C to the
γ-coloured vertices of D, G is p-colourable. C and D may intersect.

**Proof.** Their intersection consists of α-coloured vertices and contains
no endpoint of M. Recolour the β vertices of C and the γ vertices of D
with α. Give the α vertices exclusive to C colour β, those exclusive to
D colour γ, and every shared α vertex either β or γ. Leave all other
vertices unchanged.

Every old α-neighbour of a recoloured β vertex belongs to C and receives
β or γ; the corresponding assertion holds for D. The hypothesis excludes
edges between the two newly α-coloured sets. There are no edges inside
either set, by the original colouring. An α vertex assigned β has all
its old β-neighbours in C, now coloured α; the symmetric assertion holds
for γ. These checks include edges leaving C union D. Edges between old
α vertices belong only to M.

Each edge of M has a recoloured endpoint. If both ends change, they lie
in different selected components and receive β and γ. If only one changes,
the other retains α. Every edge of G is therefore proper. QED

Consequently, when G is not p-colourable, every such pair C,D has an
actual β–γ edge. An intersection alone is insufficient to obstruct repair.
The edge is between the specified colour shores, not merely between
connected carriers already adjacent through M.

## 2. Three loopless layers force an eligible pair

For a colour β different from α, contract the αβ-components of `G−M`
only in the following auxiliary multigraph: retain the three edges of M
between their components, including loops. Call this multigraph Γβ.
No minor operation on G is being proposed.

If G is not p-colourable, Γβ is not bipartite: otherwise swapping α,β
on one side of a bipartition properly colours every edge of M. A loopless
Γβ must therefore be a triangle using all three matching edges. Its
three components each contain two matching endpoints, from different
matching edges; their endpoint pairs cover the six endpoints.

**Proposition 2.** Suppose G is not p-colourable and Γβ is loopless for
three distinct colours β. Then Lemma 1 has an eligible pair of components
from two of these layers. Every eligible pair has the asserted β–γ edge.

**Proof.** Name the matching edges R1,R2,R3 cyclically. In each layer
there is one component joining endpoints of R1,R2, one joining R2,R3,
and one joining R3,R1. Fix R2. Among three layers, two use the same
R2 endpoint in their R2,R3 component. Select the R1,R2 component of
the first layer and the R2,R3 component of the second. They use opposite
ends of R2 and one endpoint of each other edge. They therefore satisfy
Lemma 1. Its contrapositive proves the final assertion for every eligible
pair, not just the selected one. QED

## 3. A fixed five-chromatic graph retains all six endpoints

**Proposition 3.** In Proposition 2, suppose p=6. Let H be induced by
the α class and the three chosen β classes, with M retained. Then
`χ(H)=5` and `χ(H−e)=4` for every e in M. Every vertex-critical
five-chromatic induced subgraph of H contains all six endpoints and
all three edges of M.

**Proof.** A four-colouring of H, together with fresh colours on the
two untouched original classes, would six-colour G. Conversely, recolour
one endpoint of each matching edge with a fresh fifth colour. These
three vertices are independent, so this five-colours H.

For e in M, delete e from any one of the three triangle quotients.
The remaining auxiliary graph is bipartite. Swapping its αβ-components
on one side gives a four-colouring of `H−e`. Three colours there would
give four on H by recolouring one endpoint of e, so equality holds.
An induced five-chromatic subgraph omitting either endpoint of e would
be a subgraph of `H−e`, a contradiction. This applies to every e. QED

## Scope of the construction

These are simultaneous deductions from one actual response; no colour
class is identified with a minor bag. The recolouring uses the whole
graph and the chromatic bound retains both complementary classes. There
is no induction, quotient lift or preservation claim for connected bags.

For the critical two-triangle programme, the loopless case now requires
both the actual cross-colour edges and the fixed five-chromatic H. The
β shore of a carrier need not be connected, and different carriers may
share α vertices. Contracting each shore, or lifting a short-path model
through whole carriers, is therefore unjustified. A simultaneous minor
construction using these constraints remains open; loops remain a
separate possibility. No C19 closure or significance comparison follows.
