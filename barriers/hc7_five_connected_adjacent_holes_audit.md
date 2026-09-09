# Audit: five-connectivity and adjacent missing edges

**Source:** [the counterexample](hc7_five_connected_adjacent_holes.md).

**Exact source SHA-256:**
`83df13a4eeedf8c7a27d5eba314d758e0e002ab40a9b9f80536b6d90c15a7861`.

**Verdict:** GREEN — separate internal whole-source audit. No unresolved
gap was found. This is not external peer review or a completion claim.

The construction and source are due to `literature_repair`. The reviewer,
`universal_proof`, independently checked the original proposed argument,
the corrected contraction count and every line of this frozen source.

## Strongest checks

- The join has nine vertices and 25 edges. The stated four-colouring
  and the clique consisting of one pole and triangle 012 give chromatic
  number four. The deletion argument proves connectivity at least five;
  the displayed five-cut proves equality. All degree counts check.
- The seven displayed bags are connected and disjoint. Their only
  absent contacts are the two specified pairs incident with the last
  bag, so they give exactly the required adjacent-hole minor.
- P is the theta graph with path lengths 1,2,4. Its cycle lengths are
  therefore 3,5,6. Contracting a triangle edge leaves five edges and a
  connected graph; every other edge gives a five-cycle with one chord.
  The bound on P/e-s follows without assuming every quotient is
  two-connected. In particular contraction of 02 may create a leaf.
- Extending a model to span the connected host preserves every old
  contact. The two-double-bag and one-triple-bag cases exhaust partitions
  of nine vertices into seven nonempty bags. Three singleton poles would
  already create three missing pairs, and two poles alone cannot form
  a connected double bag.
- Two mixed doubles force a C4 among four P singletons. A mixed double
  and a P-edge double leave two singleton poles, so the four P bags
  require at least five contacts, contradicted by P/e-s. A triple with
  one pole similarly requires five edges on four P vertices; a triple
  with two poles requires at least eight on five P vertices. The other
  triple types are disconnected or leave three singleton poles. These
  arguments apply to all connected bags, not just a chosen minor model.

## Limits

This is an unrooted Q7 exclusion and refutes the proposed five-connected
upgrade from an adjacent-hole minor. Its chromatic number is four and
its connectivity and minimum degree are five. It does not refute the
six-chromatic target, the retained seven-connected upgrade, the actual
critical host, or the colourful-marked construction. Finite checks were
corroborative only; no computation is a premise of this audit or proof.
Conjecture 19, HC7 and the requested completion criterion remain open.
