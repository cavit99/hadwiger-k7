# Audit of the three-edge response reduction

**Verdict: GREEN.** Independent whole-source internal review of
[the proof](hc7_three_edge_response_reduction.md), SHA-256
`2c6175160901c664f47c145c94ff9e0a56176a5938bc28dc0c7302a51d7b6c40`.
No gap was found within the stated response class. The parent authored
the proof; literature-repair independently read it and checked the
reductions and lifts, without participating in this proof's development.
This is internal review, not external peer review or a C19 proof.

The original reduction was reviewed at draft SHA-256
`8672c40ecf6da047698c03b762e767390db6922a38cab3071978b5c2846d5629`.
The finite-simple clarification and added P4 proposition were then checked
at `f6b26229a5935ccd1450fddd2f2cbe255af24495757a4d0925b94b10606183ae`.
Only the status/link and introductory line wrapping changed in promotion;
reversing those edits recovers that final draft exactly.

Deleting a marked edge makes each auxiliary triangle bipartite, so its
component swaps four-colour the edge-deleted core. Every induced
five-chromatic subgraph must therefore retain every marked endpoint and
edge. Restriction can split components but cannot create a loop; with
three edges, looplessness and nonbipartiteness force a triangle again.
Thus vertex-critical reduction preserves the full response and apex.
Vertex-criticality also justifies two-connectivity, the nonadjacency of
two-cut ports, and the opposite singleton equality/difference relations
on the two proper sides. No favourable boundary colouring is assumed.

In the one-sided case, the fixed colouring is proper on the side with
no marked edge. Its forced port relation supplies the requisite
bichromatic port paths there. Consequently the added edge or port
identification cannot merge previously distinct global layer components
at marked endpoints. Identifying alpha ports cannot merge two marked
edges: a shared other endpoint would already make parallel edges in an
old quotient triangle. All three edges remain distinct and the residual
colouring stays proper. The discarded path interior has no marked
endpoint; its contractions lift the edge or identification while
preserving the singleton apex and all required apex contacts.

When both sides contain marked edges, a triangle's two nonempty edge
groups share two quotient vertices. Both must be represented at the cut.
A colour avoiding the non-alpha port colours therefore forces both
ports to be alpha; in every layer they must belong to different global
components. Adding the marked port edge on the equality side is loopless.
Non-four-colourability forces exactly three marked edges, hence exactly
two old ones on that side and one on the discarded side.

For that discarded edge pq, the two disjoint port-to-endpoint paths are
valid in its component plus the ports. A separating vertex inside the
component would also separate a surviving endpoint from both exits in
the original graph, contradicting two-connectivity. A port cannot be
such a separator, since the connected component meets the other port.
This also covers an endpoint separator. When one endpoint is a port,
the remaining endpoint reaches the other port inside the component.
The resulting two bags avoid the retained side internally and each
other. Edge pq supplies the new port edge, and vp,vq supply the new
apex contacts simultaneously; no preimage is used twice.

Every proper induced-core step and every two-cut step decreases core
order. Applying critical reduction again after a two-cut step preserves
the enlarged response class. Composing these fixed preimages keeps v
a singleton, although original endpoint roles may merge. For F=C3,
v is simplicial of degree three: it cannot be a singleton Q bag, and
deleting it from any larger bag preserves that bag's connectivity and
contacts through its neighbour clique. Thus Q must already occur in H.

For F=P4, the consecutive marked edges traverse each quotient triangle
as A,B,C,A. Thus a,d already lie in one component in every layer, and
identifying them preserves the three distinct marked edges and all three
loopless quotient triangles. A colouring of J pulls back to H, giving
the lower chromatic bound; deleting one marked edge and then restoring
it with a fresh colour gives the matching upper bound. The connected
preimage {v,a,d} realises the identification in H+ and adds only qb,qc,
which are already present. This constructs J, not J+, and consumes v.
The simplicial-apex argument for the resulting triangle response is
therefore essential: it moves any Q model in J+ into J before lifting.
The separate proposition correctly makes no singleton-apex claim.

The theorem does not prove that remaining terminal construction, retain
six distinct matching endpoints, or close the loopless C19 case or HC7.
No computation or external literature application is a proof premise.
