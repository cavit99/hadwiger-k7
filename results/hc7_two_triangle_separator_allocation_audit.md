# Independent audit of the two-triangle separator allocation

**Verdict: GREEN.** Separate internal mathematical audit of the complete
[source](hc7_two_triangle_separator_allocation.md), at whole-source SHA-256
`283444e901f18ec60f461eca91e158806a45e2b42394d6a87e5b54134c7b4b2b`.
This is a cold read of the complete promoted source, including the stronger
full-packet theorem and final normalized-packet assertion. An earlier review
covered draft `7ba3e125ee31624ed1aa83d4c7a6ad4e1ebc7e51ca2f7662e2214e0a0b7cfb8a`;
that historical verdict alone did not cover the substantive new proof.
This audit is not external peer review or a completion claim.

## Inputs and exact scope

All five displayed input source hashes were checked against the files and
their adjacent GREEN audits: contraction closure `ab7ce8ad…987ccb4`,
five-root wheel `f0fbab79…33f62a`, degree-free wheel in the two-triangle
exterior source `e51564c9…a745776`, bounded-deficit almost-clique
`de183e35…7bba9cd`, and helper source `0c1ac805…b6d1f375`.
The separately pinned helper audit also matches `73b9e61a…05e5601`.
The relevant wheel, deficit and port arguments were reread. No fresh
primary-source inspection or finite enumeration is a premise.

The conclusions use seven-connectivity, minimum degree eight, exclusion
of `Q`, and the displayed spanning neighbourhood. Additional edges are
allowed. Proper-minor colourability is needed only for the explicitly
conditional independent-cut paragraph.

## Strongest inference checks

Every component of `H-T` has the actual seven-set boundary stated in the
source and must meet `N(v)`. The cut restriction and the surviving triangle
and edge therefore give exactly the two named components. The degree
bound gives at least four vertices on each side.

For a cutvertex `z` of the A-side, all surviving A roots stay in one
component. The two-terminal linkage in `K-z`, or the single path in
`K-{z,a*}`, has the required distinct ends even when `z` is an A root.
Stopping at the first cut vertex makes every retained path edge an actual
edge of `H`; no added torso edge is lifted. The prefixes stay in the
A-component and avoid the wheel's nonroots. Every nonempty wheel-side set
loses at most the two actual boundary vertices `z,t3`, and that side has
at least three vertices. The two root extensions remain disjoint. The
opposite component with `t3` and the singleton `v` are adjacent and full
to all five extended wheel bags through retained original roots.

For the minimal A-side, a three-cut of its torso leaves a component inside
`L` separated by the same actual vertices in `H`. The surviving `xy`
vertices stay on the original opposite side. The new component is thus
an A-side, strictly smaller than `L`; equality would make the cut exactly
`T`, whose deletion leaves `L` connected. This proves four-connectivity
without transferring a model through unspecified torso edges.

Both five-root sides lose only `v,t3`. Their degree-six nonroots must be
original neighbours of `v`, so there are at most three. Every nonempty
nonroot boundary loses at most those same two actual vertices. The
bounded-deficit theorem therefore applies with the triangle root designated
before selecting the opposite-side model.

The full-packet and allowed-one-hole normalizations are distinct valid
optimizations. Literal B-root edges survive all contact-leaf transfers.
Minimal root bags become root-to-port paths, and no unassigned component
contacts the T union. In the allowed class, transferring a nonroot designated
port retains at least one contact and loses at most the other allowed contact;
secondary minimality also removes an unnecessary path when the root itself
is a port. Thus the designated bag is singleton. No assumption of actual
five-connectivity or singletonness of the other bags enters this argument.

A nonempty T interior missing `v` has at most six actual boundary vertices.
An empty T interior on the minimal side cannot have at most two ports in
`L`: deleting those ports and `t3` separates nonempty `L` minus the ports
from the surviving opposite side. Three-connectivity and Theorem 1 then
give a strictly smaller A-side. Consequently an empty full packet has
three nonempty disjoint path interiors in `L`. Any actual T-to-B-root edge
would contradict its bag's unique port. This argument precedes, and does
not invoke, the common-B-neighbour corollary.

After contracting the three path interiors, a minimal tree spanning their
images and an A-root image has a marked leaf different from the A-root
image. Removing it leaves a connected lift containing both other entire
path interiors and the A root. The resulting component `D` of `L-P_k^o`
also contacts `P_k^o`, since `L` is connected. No disconnected virtual
root preimage is contracted or reused in this selection.

In the opposite normalized packet, its singleton designated B root has
no actual contact with either singleton T root. The required contact to
at least one T bag therefore forces a nonempty T interior, and the
six-vertex boundary argument forces a `v` contact. Appending the old
`P_k^o` only to the designated bag preserves connectivity and supplies both
T contacts through its old port. The retained `D` contacts the other B
roots through its two old paths, the enlarged bag through `P_k^o`, both
T bags through their original roots, and `v` through its A root. These
seven disjoint bags have at most one missing contact and give `Q`.

The shared-neighbour corollary now follows from the full-packet theorem.
In any surviving allowed packet its one missing core edge and the sole
missing `v` contact must share the uncontacted T bag; the other configurations
are explicitly terminal. With both selected T roots outside `N(v)`, the
contacted bag contains an A root. Another A root outside it must be the
port of a non-designated B bag. Moving that nonroot terminal port to the
other T bag retains its old path contact, loses at most the first T bag's
contact with that B root, and makes both T bags meet `N(v)`. This new loss
and the old designated hole have distinct ends on both sides, giving the
claimed wheel and terminal construction. All moves preserve actual roots
and disjoint ownership; no universal transfer beyond this case is asserted.

The independent-cut colouring expansion retains each untouched side and
aligns the four clique colours and the single independent T colour.
None of these arguments excludes every remaining three-cut, establishes
the required simultaneous allocation, or proves Conjecture 19 or HC7.
