# Audit: degree-five star allocation

**Source:** [the counterexample](hc7_degree_five_star_allocation.md).

**Exact source SHA-256:**
`7212bf4c1b4f9a97ac09077113a39d3cd4c67fd8256de5ab8a2ad51c3e52dd9e`.

**Verdict:** GREEN — separate internal whole-source audit. No unresolved
gap was found in the stated counterexample or its scope. This is not
external peer review or a completion claim.

The construction is due to `route_assessment`; the parent wrote this
source. The reviewer, `universal_proof`, independently checked the graph,
the proposed exclusion and every line of the frozen source.

## Strongest checks

- The cycle square is four-connected by the cyclic-gap argument. The
  split has neighbour sets {0,2,3} and {0,3,8}, together with the edge
  between its two new vertices. The three deletion cases preserve
  connectedness; in the one-survivor case at most two of its three
  old neighbours were deleted. This proves the claimed connectivity.
- Both root triangles are literal, 7 and 2 are nonadjacent, and the
  complete neighbourhood of y=0 has five vertices. The displayed K4
  bags are disjoint, connected, rooted correctly and avoid {7,0,2}.
- The exact neighbourhoods of roots 4 and 5 contain only other required
  roots. Neither bag can begin an expansion. Moreover no vertex allowed
  in the 7-bag can contact 4, and none allowed in the 2-bag can contact 5.
  Thus the two independent missing pairs are unavoidable for every
  rooted model; all six contacts among the other four bags are required.
- After deleting 4,5, the stated outer cycle, three chords and four
  edges at vertex 1 account for every edge. They give the claimed plane
  embedding. The four remaining roots are cofacial and remain so under
  contractions of disjoint rooted bags. A planar K4 has only triangular
  faces, so no such rooted K4 model exists. This excludes arbitrary
  rooted Q6 models, including reallocations of the displayed witness.
- The supplied four-colouring is proper. Consecutive triangles force
  period three in any proposed three-colouring, and neighbours 0,1,8
  already expose all three colours to vertex 9. The star contraction
  retains the displayed colouring with its merged vertex coloured 3.

## Limits

The graph is exactly four-chromatic, so it has no five-chromatic
subgraph and does not meet the actual colourful-set hypothesis. The
counterexample refutes the stated connectivity-and-degree inference;
it leaves the critical-host construction and chromatic targets open.
Finite checks corroborated the graph and exclusion but are not proof
dependencies. No HC7, C19 or comparative-significance claim follows.
