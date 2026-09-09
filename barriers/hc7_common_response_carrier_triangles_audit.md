# Internal audit of the common-response carrier barrier

**Verdict: GREEN.** Separate internal proof review, 9 September 2026.
The complete [source](hc7_common_response_carrier_triangles.md) reviewed has
SHA-256
`584a0bd9daec9b27b0f7c2f6795f97dab60867f51a0108c59f6a12fe0020c9e5`.
No mathematical gap was found at its stated scope. This is not external
peer review or a proof of the critical C19 case.

## Revision and review provenance

Sartre developed the construction and proof; the parent finalised its
status and adjacent link. Route-assessment independently read the entire
source and attacked the colouring, decomposition and minor exclusion.
Reversing only that status/link change exactly recovers the reviewed
temporary draft, SHA-256
`74b790f008d9c1bf8c11b3e4759bff6931e470a93db86426fdbf7c8b3d7ad8a1`.
The comparison was performed on the actual bytes.

## Strongest-inference checks

The construction has precisely nineteen vertices and the claimed induced
neighbourhood at v. Its ten-vertex exterior is a connected star touching
all eight neighbours. The displayed colouring is proper after deleting
the three matching edges. The common-star contraction is connected and
its colouring really expands to this same response; no separately chosen
colourings are combined. Each of the three induced two-colour graphs has
exactly the stated three path components. The three matching rows join
their components in a loopless triangle, with different systems sharing
only the six endpoints.

Every edge is covered by the given tree decomposition. In particular the
base path covers xy and both matching rows, the two leaf bags cover the
rest of the triangles, and each carrier bag covers its two endpoint
edges. Adding z covers its carrier and a,b edges. Running intersection
holds for all vertices; every final bag has at most five vertices.
The Helly argument applies to the connected subtrees meeting disjoint
minor bags, so a K6 model would require six distinct vertices in one
decomposition bag. Contracting rt in Q with missing pairs rs,tu does give
K6. This proves the Q exclusion without enumeration.

The four-colouring is valid, including z of colour 2 and all carriers of
colour 4; the literal v+A clique gives the matching lower bound. Every
carrier has degree three. Treewidth is minor-monotone and width four
implies five-colourability, so all proper minors are indeed six-colourable.
These facts do not supply seven-connectivity, minimum degree eight,
seven-chromaticity or universal nonextension of actual critical responses.

## Scoped frontier integration

The two insertions in the [critical frontier](../active/hc7_k44_closure_frontier.md),
SHA-256 `06398531aadda59fa4ab761a05f042d5153b38bc47e2af028e8b85577e6523ea`,
were separately read. Removing just those insertions byte-recovers Git
`430655bc4348977699471e6f33e85c3bc0bfb1df`; inherited sections are unchanged.
The barrier summary has the correct limited scope. The alternative
six-connected K6-to-Q augmentation is explicitly unproved: the existing
critical connectivity and HC6 inputs would apply to G-v, without a rooted
lift. A literal K6 has an exterior full component by six-connectivity.
The five-connected complement-of-C8 and the planar-apex example without
a K6 minor do not refute the new candidate. The parent's primary-source
check of Robertson--Seymour--Thomas is reported as such; this audit does
not claim a fresh independent literature verification. Neither a general
augmentation nor the remaining C19 case is established.
