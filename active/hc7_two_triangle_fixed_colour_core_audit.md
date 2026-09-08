# Internal audit of the fixed colour core

**Verdict: GREEN.** Complete mathematical audit of the
[source](hc7_two_triangle_fixed_colour_core.md), SHA-256
`8596aab3da33d0169f7f8cc5b4805365bcb3a18bd32d6293809744e2a97d1100`.
This is a separate internal audit, not external peer review. No unresolved
inference was found in the stated deductions; the global minor construction
remains open.

The source was first read at SHA-256
`7f910dfca0aaf166fa57d25ca1856fd53a0f680384250729172cc0eb51d7bb70`.
The only audit edit to it changes the pending-audit status sentence;
all mathematics is unchanged. This reviewer had previously discussed the
colouring route and its ownership limitations with the author, but checked
the complete written argument and its strongest lift independently.

## Exact inputs

The following source and adjacent-audit hashes were checked against disk.
The invoked statements were reread; no new external literature inspection
or finite computation is a proof premise.

- [Connected-set contraction closure](hc7_companion_contraction_closure.md),
  Corollary 6: source
  `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`;
  [GREEN audit](hc7_companion_contraction_closure_audit.md)
  `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
- [Universal bipartite contractibility](../results/bipartite_contractibility_via_matroid_reduction.md):
  source `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`;
  [GREEN audit](../results/bipartite_contractibility_via_matroid_reduction_audit.md)
  `1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`.

## Strongest inference checks

Contracting either triangle preserves the other literal four-clique with
`v`. Two distinct neighbours in that other triangle, together with the
merged vertex's `v` contact, would give nine contacts on five vertices.
The symmetric argument handles cross-edges sharing one endpoint.
Contracting `xy` gives the same restriction on its combined triangle
neighbours. Thus the independent choices of `a,b` exist as claimed.

The five-vertex set `{v,a,b,x,y}` is connected. Expanding its single
contracted vertex represents every edge incident with the four surviving
vertices except their sole internal edge `xy`, which is deleted.
The four remaining neighbours of `v` use at most four colours distinct
from colour 1, so a fifth other colour can indeed be reserved for `v`.
The contraction is used only for proper-minor colourability; no minimum
degree or connectivity assertion is made about its quotient.

The graphs `K,J` and the sets `C0,C1` stay fixed in Proposition 2.
Restoring these sets with fresh colours verifies each chromatic lower
bound for arbitrary colourings of the remaining graph. The only edge
inside the fixed class `C1` in `G` is `xy`. Consequently recolouring
either endpoint to a missing core colour repairs the only defect, and
the universal colourful-neighbourhood conclusion follows. No original
colouring of `K` is silently substituted for an arbitrary one.

In the rainbow alternative, a disconnected bichromatic pair of T roots
could be made equal by a component interchange. The four resulting
cross paths therefore form a properly coloured `K_{2,2}` scheme with
the four prescribed roots. The universal theorem retains those roots;
the two literal triangle edges survive and complete the rooted `K_4`.
The entire model lies in `K`, so both deleted colour classes are avoided.

In the other alternative, the four core-colour `x-y` paths avoid `v`.
The missing colour on `T` can be assigned to `v` because its other four
neighbours all have colour 1. The resulting `1,0` path also avoids `v`.
Only `v` was changed between these two colourings; hence all five paths
are simultaneously bichromatic in one proper colouring of `G-v-xy`.
The argument does not transfer old paths between differently coloured
vertices of that fixed host.

For the forest lift, the projected vertex set consists of all colour-1
vertices on the five paths. Their common endpoints make its union
connected. A non-1 label occurs on exactly one projected edge: its colour
chooses one simple path. There are no projected loops, though parallel
edges are permitted. Removing an edge of a spanning tree's `x-y` path
leaves exactly two components, containing the two prescribed roots
separately. Their actual lifts use only their own tree-edge labels, so
the bags are disjoint and connected. Every projected `x-y` path crosses
this partition; a crossing edge cannot belong to the retained forest.
Its unused actual label has a neighbour in each lifted bag. Selecting
one crossing label from each differently coloured path gives five
distinct singleton leaves, all disjoint from the two root bags.
The original `xy` edge supplies their additional mutual contact in
`G-v`. No virtual edge or unowned label is used in a lift.

## Scope

The alternative is exhaustive but is not asserted to be exclusive. The
rooted `K_4` need not meet both endpoint neighbourhoods in each bag.
In the other outcome, the five leaves need not be the four named T roots
or retain either literal triangle, and the root bags can absorb named
neighbours. Thus the source establishes fixed-graph colouring constraints
and its two stated rooted minors, not a `Q` minor, Conjecture 19, or the
user's global completion criterion.
