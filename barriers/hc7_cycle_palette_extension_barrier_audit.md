# Independent audit of the cycle-palette counterexamples

**Verdict: GREEN.**

Date: 7 September 2026. This is a separate internal mathematical audit,
not external peer review.

Audited source: [cycle-palette barrier](hc7_cycle_palette_extension_barrier.md).
Whole-file SHA-256:
`257805e4f1c4771b57fdcb7980af77a53b94f45853920287593221166f2ef294`.
The audit covers both constructions and their stated scope. No computation
or uninspected literature theorem is a proof premise.

The strongest conclusion holds: the 42-vertex graph is five-colourable,
has neither a \(P=K_7-3K_2\) nor a \(Q=K_7-2K_2\) minor, and its seven
roots induce exactly \(C_5\mathbin{\dot\cup}K_2\). Every five-colouring
uses all five colours on the roots and at least four on the cycle.

## Hostile checks

- **Exact forcing and independent extension.** Each private four-clique
  forces its two full neighbours \(x,z\) to share the fifth colour;
  the edge \(zy\) therefore forces \(x\ne y\) in colour. Conversely,
  every distinct endpoint assignment extends. Private gadget interiors
  allow all seven extensions simultaneously, with no extra root edges.
  The virtual root graph contains precisely the required five-clique.
  The displayed colouring proves existence, so the universal condition
  is not vacuous. The counts are \(7+7\cdot5=42\) vertices and
  \(6+7\cdot15=111\) edges.
- **Arbitrary minor models across the separators.** After adding the
  virtual edges, each gadget meets the rest in its actual two-root clique.
  At most two model bags meet that clique. A three-connected target cannot
  have remaining bags on both sides. On the retained side every bag stays
  nonempty; excursions within a bag can be replaced by the clique edge,
  and the same edge restores any lost contact between two separator bags.
  These replacements respect disjoint ownership. Iterating localizes a
  \(P\) or \(Q\) model in one torso. Each torso has seven vertices and
  at most sixteen edges, so seven nonempty disjoint bags must all be
  singletons and cannot realize either target. Passing to the subgraph
  without the virtual edges preserves this exclusion.
- **Planar example.** The eleven triangles have exactly the stated disk
  boundary; the interior edges occur in two faces and vertex links are
  circles or boundary intervals. The three forcing rows and both permitted
  singleton extensions check directly. Rotation by two gives disjoint
  permitted singleton sets. The displayed four-colouring respects both
  disks, verifying the order, size and chromatic claims. The apex colour
  is unavailable everywhere in the planar remainder in every five-colouring.
- **Different target exclusions.** Apex closure under minors and the
  six-vertex planar edge bound exclude \(Q\). The six displayed bags in
  the planar remainder are connected and disjoint, with precisely the
  three stated independent missing contacts. Adding the apex gives \(P\);
  the source correctly reserves simultaneous \(P,Q\) exclusion for the
  gadget example.

## Remaining obligations

No gap was found in either counterexample. They refute the stated
unrestricted palette extensions, including the version with induced root
graph \(C_5\mathbin{\dot\cup}K_2\) and both target exclusions. They do
not supply the original host's critical colouring responses, connectivity
or degree hypotheses. Both contain a literal \(K_5^-\), already excluded
in that host. A construction using those stronger hypotheses remains
possible; neither a companion conjecture nor HC7 is completed here.
