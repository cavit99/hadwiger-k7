# Internal audit: at most three components behind a seven-vertex cut

**Audited source:**
[`hc7_k7minus_seven_cut_three_component_bound.md`](hc7_k7minus_seven_cut_three_component_bound.md)

**Audited source SHA-256:**
`cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8`

**Verdict:** **GREEN.**  The theorem is computation-free.  This is a
separate internal mathematical audit, not external peer review.

## Dependency revisions

- [`hc7_k7minus_seven_boundary_component_descent.md`](hc7_k7minus_seven_boundary_component_descent.md),
  SHA-256
  `9e2f616c98dd17670f4d15e962f3b36e4fc1f4c4dc9aee4227eabeb51ca33913`;
- [`hc7_closed_shore_rooted_connectivity.md`](hc7_closed_shore_rooted_connectivity.md),
  SHA-256
  `ba6dbfe1ca9e89041b1a77174844c24598984cbe76349a55c41f15b2e997cc03`;
- Jørgensen's rooted-diamond theorem, as quoted in Lemma 10 of Norin and
  Totschnig.

## Audit

The capacity theorem gives exactly the facts used at the entrance: every
component of `G-S` is connected and adjacent to every vertex of `S`, there
are at most four components, and four components force
`Delta(G[S])<=1`.

Assume there are four components and one, `C_1`, is non-singleton.  For any
four-set `Q\subseteq S`, the remaining three components form a nonempty
opposite side, so the closed-shore lemma applies to `G[C_1\cup Q]`.  The
pair is internally four-connected and has at least six vertices.  Thus the
rooted-diamond input is applicable and returns four disjoint rooted bags
with at most one missing mutual adjacency.

There are exactly three unused boundary vertices and exactly three other
components.  Enlarging each component by a different unused boundary
vertex gives three connected and mutually disjoint bags.  For two such
bags, one component has a literal edge to the boundary vertex in the other
bag.  For a component bag and a rooted-diamond bag, the component has a
literal edge to that bag's named boundary root.  Therefore all cross
adjacencies and all three adjacencies among the component bags are present;
the sole possible missing adjacency is the one already allowed in the
rooted diamond.  This is a valid `K_7^-` model.

Consequently all four components would have to be singletons.  Fullness
then gives each boundary vertex four neighbours outside `S`, while
`Delta(G[S])<=1` gives at most one inside.  This contradicts the minimum
degree at least seven implied by seven-connectivity.  This excludes four
components.

For the strengthened three-component conclusion, the proof first correctly
shows that some component is non-singleton.  If all three were singletons,
each boundary vertex would have three neighbours outside `S`; minimum
degree at least seven would give minimum boundary degree at least four and
therefore at least fourteen boundary edges.  This contradicts the audited
capacity bound `|E(G[S])|<=9` for three full components.

If a boundary vertex `z` had four boundary neighbours, those four
neighbours could be used as the roots on a non-singleton component.  The
other two components form the required nonempty opposite side for the
closed-shore lemma.  The resulting rooted `K_4^-` model is disjoint from
`z` and the two unused boundary vertices.  Pairing those unused vertices
with the two other components gives two connected bags.  Fullness supplies
all adjacencies involving either component-derived bag, while the four
literal edges from `z` to the chosen roots supply every adjacency from
`\{z\}` to the rooted bags.  Thus the sole possible missing adjacency is
inside the rooted diamond, and the seven bags form a valid `K_7^-` model.
This proves `Delta(G[S])<=3`.

The proof makes no claim that the remaining two- or three-component cases
are impossible.  In particular, in the three-component case it establishes
only that the boundary is subcubic.
