# Second internal audit: exterior colouring bound

**Verdict: GREEN.** This is an independent internal mathematical audit,
not external peer review. No gap was found in the stated theorem.

**Audited source:** [neighbourhood colouring and exterior bound](hc7_two_triangle_exterior_colour_bound.md).
**Whole-source SHA-256:**
`4c3732c09aa157014c0ba417d3e1c0bda5ee16537ff253333cb0bf891caa1610`.

The mathematical argument was independently checked at draft hash
`408cc0325ebfaa23eb7392a8d958c18596a8b24cfc70bd5cf88a179e58fe894e`.
Restoring only its status paragraph and two relative input links in the
promoted source recovers that exact hash. The mathematics is unchanged.

## Inputs and strongest construction

The pinned [contraction-closure source](../active/hc7_companion_contraction_closure.md)
and its [audit](../active/hc7_companion_contraction_closure_audit.md) were read;
their hashes match those quoted in the source. Corollaries 3 and 6 have
the required connectivity, degree and excluded-minor hypotheses here.
Their inherited external input was not freshly audited.

The support contraction uses one neighbourhood vertex and at most two
exterior witnesses. This connected set is disjoint from the retained
four-clique and contacts three distinct clique vertices. Thus Corollary 6
excludes precisely the proposed quotient; no repeated contraction is used.
The symmetric support restrictions give a matching between the triangles.
Every large contact set contains a port, so the two listed alternatives
are exhaustive, including repeated contact sets and additional literal edges.

## Simultaneous colouring and extension

In the first alternative, a triangle vertex has only one attainable colour
exactly when both port edges force colour 3, or its mark and one port edge
force the other colour in {1,2}. All other attainable sets have at least two
colours. Equal singleton sets at the cross-edge endpoints yield the stated
four-cycle or a large set meeting a literal triangle twice. Otherwise the
independent triangle colourings realize distinct endpoint colours together.

In the second alternative each triangle has at most one port edge. For
the cross-edge a0b0, one of the two indexed pairs therefore has at most
one port edge. Its vertices can receive opposite colours 1,2 while avoiding
that edge; the other pair receives colour 3. The remaining triangle colours
at a0,b0 are opposite. The other cross-edge constructions also respect all
permitted edges and make both large contact types use at most two colours.

One fixed neighbourhood colouring consequently works for every exterior
vertex. Removing a whole class of a k-colouring, k>=2, leaves k-1 old
colours; its independent vertices can each take a missed fresh colour.
The disjoint palettes prevent conflicts with the remaining exterior, and
v receives an old colour because it sees only the neighbourhood. The
k<=1 case correctly uses four colours, including when the exterior is empty.

## Scope

The proof has no finite-check premise, host-order bound, induction, or
unresolved branch-set lift. No unresolved assumption beyond the stated
hypotheses and pinned input was found. It gives the asserted chromatic
bound and the four-chromatic exterior closure; it establishes no novelty
claim and does not complete Conjecture 19 or HC7.
