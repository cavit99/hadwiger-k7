# Internal audit: the contraction-boundary exclusion

**Verdict: GREEN.**

**Audited source:** [the boundary exclusion](hc7_reserved_core_contraction_boundary.md).

**Whole-source SHA-256:**
`da0e3fd73fb52815d01bdfd7d9e56a0fd9d1bca4c93bb2d332fc0f4fe67de571`.

This is a separate internal mathematical review, not external peer review.
The source was written by another agent. This reviewer has co-developed
related reserved-core results and checked the proposal before reading the
complete source independently. The parent separately reported a conceptual
check; that is not represented as another exact-source audit.

## Revision and input checks

The complete mathematical draft was read at SHA-256
`e7d6430fdca618b20409be5a8e74215ca6c1516ed1b96120c10ee12b6a76de76`.
The status-only active revision had SHA-256
`71e2eb582fc00f8f3773b337531c9bb36f9380208c0396a7b0c3ccad2de5e660`.
Reversing its final status sentence recovers the draft exactly. Promotion
changed only four source links to sibling links; reversing those links
recovers the active revision. Both reconstructions were checked. The
promoted source was inspected and its mathematics is unchanged.

Both source/audit pairs were checked against disk, and the exact invoked
statements were reread:

- Five-root degree-six theorem:
  `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`;
  audit `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
- Tight-boundary exclusion, Lemma 1:
  `f190c8e63df3d12b301440280babeee611db897a5542216f2d074314fb5a6b18`;
  audit `e6d22369b0e860fde909aefe9e48491497769e72edfa8ff37eaa5024abb48e54`.

This checks their use here, without claiming a fresh external-literature
review or re-auditing their full proofs.

## Outside components and fixed preimages

Deleting the five named vertices from a seven-connected G makes L
two-connected. The exact X-boundary in L is B1,s,t. In the first case,
connected C and its B2 contact give a path towards X whose prefix ends
at s or t and avoids both X and M. The stopped B2-to-M path lies wholly
in Z. Their union is connected through B2, misses M and all other core
roots, and has an actual edge to M. It need not be a path, which is harmless.

In the second case, connected L-B1 forces every outside component to
contain s or t; hence there are exactly two, with one port in each.
Neither port belongs to M. The component E of Z-t containing M has
L-boundary contained in t,B1. Since another component and X survive
outside it, two-connectivity forces both contacts, including B1.
The chosen B2-to-s path in the other component is disjoint from E.

The root preimages b,B1,P,a,xy are connected and pairwise disjoint,
and preserve the literal B triangle. Deleting all X--t edges before
contraction covers both possibilities for t's membership in P. Only
s supplies an X contact to that preimage. Thus each X vertex loses at
most the t neighbour and one neighbour from merging x,y; every nonempty
X subset loses at most the corresponding two boundary vertices. The
surviving outside vertex v licenses the original seven-boundary bound.
The degree-six and internal-five hypotheses therefore hold exactly.

The five lifted bags avoid E and v. The singleton v is full to them
through their retained original roots and meets E through M. E is full
to three core roots and to B2 in the first case or B1 in the second.
Selecting an admissible triangle centre different from its sole possible
B omission makes the two possible holes independent. This gives seven
disjoint connected bags containing Q, without using an old B-root path.

## Boundary corollary and scope

Any offending nonroot subset in the quotient has boundary exactly three:
the deletion and contraction lose at most four original neighbours.
Each of its connected components has boundary at most that same three-set,
so equality and all five forced old boundary vertices hold componentwise.
The two other old boundary vertices are distinct. If one is B2, removing
B leaves the forbidden H four-boundary containing a,x,y; otherwise both
are in W and the proved terminal applies. This establishes the asserted
four-neighbour condition for every nonempty nonroot subset.

No colouring assumption, maximum-core property or unstated minor degree
inheritance is used. The corollary proves only the boundary condition.
The merged-root bag still owns both b and B1; deleting b from that bag
is not justified. The remaining allocation and the full two-triangle
case are explicitly unresolved. No mathematical gap was found within
the stated conclusions.
