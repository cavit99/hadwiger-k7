# Independent audit of the degree-six five-root theorem

**Verdict: GREEN — separate internal audit of the complete written proof.**
This is internal review, not external peer review or a claim of global
Hadwiger closure. No mathematical gap or correction was found.

## Exact revision and inputs

The audited source is [the degree-six five-root theorem](hc7_five_root_degree_six.md),
SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`.
The complete draft was independently read at SHA-256
`50e27563671a7efbbbfd0e99df2ea932c09b4fed6e3c1e240a3eac5985024d97`.
Promotion changed only its draft-status line and two relative input links.
Reversing those exact text substitutions reproduces the audited draft hash;
the mathematics is byte-identical. No source edits were made by this audit.

Both pinned input hashes were checked against disk:

- [The recorded exact Norin--Totschnig Theorem 8 statement](hc7_five_root_almost_clique.md):
  `de183e350c412739c05a744e811304454ba90856efee9e097813c70617bba9cd`.
- [Its separate audit](hc7_five_root_almost_clique_audit.md):
  `dc7db3d391ef2701516d64dd32e7546d40e2e4171406193f17d8feadcc4abb47`.

The four alternatives and the trisection definition were compared with
the pinned statement. This audit relies on that recorded primary
inspection; it does not claim a fresh literature inspection or a finite
verification premise.

## Strongest checks

1. **Fixed counterexample class.** Fixing two inadmissible triangle labels
   before minimizing nonroot order is legitimate. An admissible model
   after either reduction lifts with the same labels and all required
   contacts. Thus both fixed bad labels remain bad in any smaller
   counterexample. The two-nonroot base is a rooted `K_5`: both nonroots
   are universal in the seven-vertex graph.

2. **Both reductions preserve the full hypotheses.** A root with one
   nonroot neighbour can be absorbed without changing any surviving
   nonroot degree or boundary cardinality. In the simultaneous `bp,cq`
   transfer, no surviving nonroot sees old `b` or `c`, and `p,q` become
   distinct root preimages. The root triangle survives, nonroot order
   strictly decreases, and a one-nonroot endpoint is excluded by the
   retained degree-six bound itself.

3. **Rooted-four and trisection cases.** For a bad centre, either helper
   contacting that centre would give exactly the asserted admissible
   model. The maximal-helper argument therefore has an actual boundary
   of at most two ports; deleting the two helper roots gives a nonroot
   boundary of at most four in the original graph. The resulting empty
   helper interiors force the excluded common-two-neighbour transfer.
   In a trisection, the boundary hypothesis makes the two open parts
   singleton roots. The common separator is nonroot, and the literal
   edge between the two retained triangle roots forces the isolated
   roots to be `b,c`. No extra contact or shared contraction preimage
   is assumed.

4. **Actual facial cycles.** Each retained root has two nonroot
   neighbours. After deleting at most one vertex, every component
   therefore contains a nonroot; the internal-four boundary bound forces
   at least three roots into each component. This proves actual
   two-connectivity of each planar response, so its distinguished face
   has a simple cycle of length `4+h`.

5. **The comparison uses one unchanged host.** Euler gives
   `e(J)<=3|D|+5-h`. The facial cycle contains at least `4-h` distinct
   root-root edges, which may be subtracted from this bound. The
   inequality remains valid when `h>4`. Hence each bad centre satisfies
   `e_D+K-k_u<=3|D|+1`. Together with `2e_D+K>=6|D|`, this gives
   `2k_u>=K-2`. Applying it to the two fixed bad centres in the same
   graph forces the other three root-to-nonroot degrees to sum to at
   most two, whereas normalization makes their sum at least six.
   No alignment of drawings or independently returned models is needed.

## Scope

The proof establishes at least two admissible triangle roots, with a
possibly different model for each. It permits arbitrarily many
degree-six nonroots and needs only the stated nonroot boundary condition.
It does not retain an arbitrary preassigned centre, provide a disjoint
sixth helper, or complete the two-triangle case, Conjecture 19, or HC7.
