# Internal audit: the chromatic bound after deleting a four-clique

**Verdict: GREEN.** The theorem and four-list lemma hold at the exact
revision below. This is a separate internal mathematical audit, not
external peer review or a global case-completion claim.

**Audited source:** [four-clique deletion bound](hc7_clique_deletion_colour_bound.md).

**Whole-source SHA-256:**
`dd39ad7bf84d4bf698757e8bc7dbadec987356c4eb53593d41c5478129573a84`.

Promotion changed only status and relative links; reversing those substitutions
recovers frozen source SHA-256
`d991a2a9afa5011db6c1d56359522b9190cf22d7a49ab9eb7527ad2aa87e6ce3` exactly, so the mathematics is unchanged.

## Inputs and provenance

The reviewer did not author this proof and cold-read the complete frozen
source. The invoked [contraction-closure source](../active/hc7_companion_contraction_closure.md),
SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
and its [adjacent audit](../active/hc7_companion_contraction_closure_audit.md),
SHA-256 `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`,
were read and their hashes checked. No fresh primary-source inspection
or finite computation is used.

## Strongest checks

The graph lies in the exact class required by Corollary 3: six-connectivity,
minimum degree eight and Q-minor exclusion suffice. Its clique has four
actual vertices. Every outside vertex therefore has at least two available
clique colours; the neighbour-set containment at a vertex with exactly
two clique neighbours reverses correctly to the asserted list inclusion.

In the list lemma, bad vertices in opposite shores cannot be adjacent:
their disjoint two-element lists violate inclusion. Every neighbour of a
bad vertex contains its entire list and can take the forced alternate
colour. A vertex cannot be both bad and forced by an opposite bad vertex.
All remaining I colours lie in {1,2}, including forced colour 2; all
remaining J colours lie in {3,4}, including forced colour 4. Edges incident
with bad vertices and all other edges are thus checked separately. Lists
of size three or four, isolated vertices and empty shores cause no exception.

Any colouring with at most four colours can be represented by four
classes, including empty ones. Recolouring exactly two classes leaves
the other two independent classes in fresh colours 5 and 6; there is no
conflict with either the clique or the recoloured bipartite graph. Hence
the assumed colouring of G-R gives an actual six-colouring of G,
contradicting chi(G)>=7 for every permitted G and every four-clique R.

**Scope and gaps.** No gap was found. Proper-minor six-colourability is
not used. The result is a chromatic lower bound, and supplies neither a
compatible rooted minor nor the remaining two-triangle construction.
