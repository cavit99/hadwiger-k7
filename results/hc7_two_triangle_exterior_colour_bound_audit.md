# Internal audit: the two-triangle exterior colour bound

**Verdict: GREEN.** This is an independent internal mathematical audit,
not external peer review or a completion of Conjecture 19 or HC7.

**Audited source:** [exterior colour bound](hc7_two_triangle_exterior_colour_bound.md).
Whole-source SHA-256:
`4c3732c09aa157014c0ba417d3e1c0bda5ee16537ff253333cb0bf891caa1610`.
The [second audit](hc7_two_triangle_exterior_colour_bound_second_audit.md)
records a separate review.

The proof was independently checked at draft hash
`408cc0325ebfaa23eb7392a8d958c18596a8b24cfc70bd5cf88a179e58fe894e`.
Reversing only the final status change and two relative-link changes
reproduces that hash exactly; the promoted mathematics is unchanged.

## Input and strongest inference

The [contraction-closure source](../active/hc7_companion_contraction_closure.md)
has SHA-256
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`;
its [audit](../active/hc7_companion_contraction_closure_audit.md) has SHA-256
`26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
Both hashes match. Corollaries 3 and 6 apply under the stated hypotheses;
their inherited external input was not freshly reviewed here.

Two supported A-vertices require at most two W-witnesses. Together with
their common neighbourhood vertex these form one connected set of at
most three vertices, disjoint from the retained four-clique. Its quotient
vertex has three distinct clique contacts, giving the forbidden K5^-.
Literal contacts need no witness. The symmetric restriction yields the
matching between A and B. Corollary 3 also correctly excludes two contacts
with any literal neighbourhood triangle from a large contact set.

## Classification and simultaneous colouring

Every large set contains a port. If two A-vertices occur, their sets use
different ports exclusively, forcing the two displayed triples; the
matching makes their B-vertices distinct. The symmetric argument covers
two B-vertices. This independently verifies the complete classification.

In Case I the per-triangle attainable sets have exactly the stated
singleton cases. The triangles can be completed independently after
choosing distinct cross-edge endpoint colours. Equal forced 3s give a
four-cycle; equal forced 1s or 2s give a literal triangle met twice by a
large set. Both obstructions are excluded with the same contact family.

In Case II all four cross-edge possibilities are covered. The a1b1 and
a2b2 constructions respect their corresponding port restrictions. For
a0b0 either selected pair works: one port edge fixes its endpoint's
opposite colour, and the remaining triangle colours make a0,b0 opposite.
Each large triple sees at most two colours in every displayed construction.

## Extension and scope

For k=0 or 1, W and v can share the fourth colour. For every k>=2,
including k=2, W-I leaves a nonempty old palette for v. Recolouring I
uses available neighbourhood colours independently because I is independent;
the disjoint palettes prevent conflicts with W-I. No finite computation
is a proof premise. No gap was found. The four-chromatic exterior branch is closed; the global targets remain open.
