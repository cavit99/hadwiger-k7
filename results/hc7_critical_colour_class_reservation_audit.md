# Separate internal audit: critical colour-class reservation

**Verdict: GREEN.** This is an exact-source internal mathematical audit,
not external peer review or an assessment of priority or significance.

Audited source: [critical colour-class reservation](hc7_critical_colour_class_reservation.md).
Whole-file SHA-256:
`6c40aab52c5e5c8dc822640ce3c801f6cc46e04b161fd49f108dfd6835116eb3`.

The reviewer is separate from the current source's author. The whole
frozen source and its invoked inputs were read. Earlier discussion of
the star-colouring mechanism and earlier reviews of the bipartite input
are disclosed; this is not a claim of external or historically uninformed
review. The initial full read was at `0e9df05e33abd4c864f7fee026309d3022922fefb188f6d8c6e4aeb435d72d79`;
the reviewed draft `289570f7e353c8a6bd0ebd6faf26620710cd27446bd8479e945a0cf4cb93fe8a`
only clarifies the definition of Q and the status wording. Reversing the
promoted source's subsequent status and relative-link edits recovers that
reviewed draft hash exactly. Its mathematics is unchanged.

## Strongest quantifiers and colouring extensions

The order of quantifiers is valid: for each eligible independent triple T,
one star-contraction colouring selects I; every subsequent five-colouring
is of that same fixed graph F. The contracted star is connected and gives
a proper minor. Expanding T is proper because T is independent, and all
five other neighbours of v avoid its colour. Failure of their distinctness
would extend the colouring to v.

The entire colour class I is independent and meets the neighbourhood of v
in exactly T. A four-colouring of F would extend using separate colours
for I and v. A five-colouring using at most four colours on R would extend
using a sixth colour for I and a missing old colour for v. These arguments
prove the stated chromatic equality and universal rainbow condition without
preserving any connectivity or criticality after deletion.

In each fixed five-colouring, a two-colour component swap containing just
one of its two roots violates the same rainbow condition. All ten paths
can therefore be chosen in one colouring. Their endpoint colours exclude
foreign roots and certify the full collection-intersection condition.

The corollary fixes J from the original colouring, with
`J intersect N(v)={x}` and `I intersect J=empty`. Restoring these two
independent classes in distinct new colours proves both `chi(K)=4` and
the universal rainbow assertion for L. For the neighbourhood assertion,
recolouring x with a missing core colour is proper: its K-neighbours avoid
that colour, I has another colour, and J is independent. The old J colour
then disappears from the entire neighbourhood of v and can colour v.
This verifies the universal assertion over all four-colourings of K.

## Extraction, inputs and scope

The four cross-pair paths form one K2,2 scheme in K. Its rooted minor has
four disjoint bags containing the four original roots. Hence the two
literal triangle edges remain edges between distinct bags and complete
the rooted K4. All bags avoid both deleted classes and v.

All three source/input hashes printed in the proof were checked exactly.
The earlier [cycle construction, Section 1](../active/hc7_degree8_cycle_triangle_construction.md)
was reread for provenance; its additional structural assumptions and its
later conclusions are not imported. The
[bipartite theorem](bipartite_contractibility_via_matroid_reduction.md)
and its [pinned audit](bipartite_contractibility_via_matroid_reduction_audit.md)
were reread at their recorded hashes, including preservation of every root.

No gap remains in these stated deductions. The K5 scheme is available for
every eligible T, independently of a matching quotient's chromatic branch.
Neither K5 extraction nor a compatible seven-bag extension is established.
Different choices of T need not share colourings, classes or models. No
finite computation is a mathematical premise of this source.
