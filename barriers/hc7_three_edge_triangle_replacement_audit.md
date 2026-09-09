# Audit of the triangle-replacement counterexample

**Verdict: GREEN.** Separate whole-source internal review of
[the construction](hc7_three_edge_triangle_replacement.md), SHA-256
`a9b6abedad1cee5f40b1fdb43f9e173009e1391829a3472c31c945e84fac0cf5`.
Route-assessment constructed and wrote the example; the parent separately
checked its complete edge rules, colouring argument and minor model.
The only change from the reviewed draft at `d9c04b529b617e80182ef9b41b792dbb34c7ef146066683cfb558ff3ae799972`
is its status and audit link. This is internal review, not external review.

There are 17 vertices. The three marked groups and the stated location
of t follow from the displayed neighbourhoods. Replacing de by ac leaves
exactly the same coloured graph after deleting the new marked triangle,
so every quotient remains a triangle. The supplied J-colouring makes
every displayed edge proper, and recolouring d gives five colours on H.

The four-colour exclusion is exhaustive. The triangle x3,y2,z3 forces
c=e, and disjoint Z and X∪Y palettes leave at most two colours on Z.
When Z uses two, connectedness forces one colour per opposite shore.
When Z uses one and the other palettes are disjoint, only one shore can
use two. The t constraint or the shared y0 then gives a=d, while ab,bc
forces a=c. If the palettes overlap, the sole missing cross-edge confines
their common colour to x0,y1. Each remaining shore is monochromatic:
two colours on one would leave none for the other. The forced values
of c,d,e then contradict de. These cases prove χ(H)=5 and χ(J)=4.

For the connectivity claim, at most three deletions leave both a Z vertex
and at least four X∪Y vertices. Every surviving α vertex either retains
a core neighbour or reaches one through a surviving marked edge. The
only problematic vertices have exactly three core neighbours, so losing
all of them exhausts the deletion set; their asserted alternate neighbour
indeed survives. Vertex a has degree four, proving κ(H)=4.

The seven displayed bags are disjoint and connected. The two mixed bags
are full to each other and to all five singleton bags. The latter induce
parts of sizes 1,2,2, giving exactly the two independent missing contacts.
Thus the example contains Q even without its apex. Only unconditional
chromatic retention is refuted; the global response target and the
audited two-cut and P4 reductions are unaffected. No computation is a
premise, and vertex-criticality is not asserted.
