# Audit: clean response bypass at a six-vertex topological `K_5`

**Verdict:** GREEN.

**Audited source SHA-256:**
`66d9ef5f6195eacc2d5dc8cf459388f48a41b905d240c5548cc03ec555b79ff0`.

## 1. Hypothesis matching

Every hypothesis of Theorem 1.1 in
[`hc7_shared_interface_bichromatic_bypass.md`](hc7_shared_interface_bichromatic_bypass.md)
matches the application in Theorem 3.1:

- `chi(G)=7` makes `G` non-six-colourable;
- `aw,wb` are distinct incident edges;
- `ab` is the required outer nonedge; and
- contracting the two-edge path gives a proper six-colourable minor.

## 2. Response table and exact chromaticity

The three positive signatures follow by expanding colourings of `G/aw`,
`G/wb`, and `G/aw/wb`.  A `(ne,ne)` colouring would permit both deleted
edges to be restored and would six-colour `G`.

The double contraction is exactly six-chromatic.  A hypothetical
five-colouring would expand with `a,b` retaining the contracted colour and
`w` receiving a fresh sixth colour.  The nonedge `ab` makes that assignment
proper.

## 3. Exterior cleanliness

The three remaining branch vertices form a triangle, are adjacent to both
`a` and `b`, and therefore use three distinct nonzero colours.  For each
such colour, the corresponding two-edge path through the branch vertex
places `a,b` in one bichromatic component.  The dependency's per-colour
cover law then places `w` in that component, so both half-edges are linked
for all three core colours.

If neither half-edge is universally linked, its two failures therefore use
the other two colours.  The components selected by the dependency exclude
`w` and the opposite outer endpoint; their palettes exclude the three
remaining branch vertices.  Hence the returned path has no selected-support
vertex internally.  The two opposite one-edge response colourings have the
orientation stated in the theorem.

## 4. Trust boundary

No gap remains in Lemma 2.1 or Theorem 3.1.  The unresolved global step is
correctly excluded: the theorem does not align several supports, produce a
two-vertex transversal of the complete family, or increase the global pair
height.
