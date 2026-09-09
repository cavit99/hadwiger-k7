# Audit of simultaneous recolouring of two matching carriers

**Verdict: GREEN.** Whole-source independent internal proof review of
[the source](hc7_common_response_recolouring.md), SHA-256
`0c90ba957d42eee66d8b082096a5528b54fef72e47e2f64785ac4a229a809e81`.
No mathematical correction or unresolved assumption was found within its
stated hypotheses. This is not external peer review.

The parent wrote the source. Route-assessment supplied earlier checks of
the recolouring and a longer endpoint-selection argument, then separately
read the entire frozen source and attacked its shorter proof and stronger
chromatic equality. This audit discloses that preliminary contribution;
it is not a claim of review without prior involvement.

Lemma 1 explicitly excludes a whole matching edge from either endpoint
trace. Shared vertices are therefore nonterminal α vertices. Component
closure checks every edge to an unchanged vertex; the only possible new
conflicts between the two recoloured non-α shores are exactly the excluded
β–γ edges. Shared α vertices may choose either new colour independently.
Each restored matching edge has either one changed end or ends assigned
different new colours. No vertex-disjointness assumption is used.

A bipartite auxiliary quotient permits whole-component swaps. With only
three matching edges, its loopless nonbipartite alternative is exactly a
triangle. In Proposition 2 the pigeonhole choice fixes the endpoint used
by the R2,R3 component in two distinct layers; the complementary R1,R2
component uses the other R2 endpoint. This gives the required four
distinct endpoints and covers all three matching edges. The forced
cross-shore edge follows for every eligible pair, not only this choice.

For Proposition 3 the two untouched whole colour classes justify the
lower bound on χ(H). Choosing one endpoint per matching edge gives an
independent set and hence the five-colouring. Deleting any matching edge
leaves a bipartite quotient and a four-colouring; a three-colouring would
four-colour H after giving one endpoint a fresh colour. Thus the asserted
equality is valid. Every five-chromatic induced subgraph must retain all
six endpoints and all three matching edges.

The proof uses no computation or external theorem. Its scope paragraph
correctly retains the unresolved simultaneous branch-set allocation:
colour shores need not be connected, carriers may overlap, and neither
Q nor a closure of C19 follows from these deductions alone.
