# Independent audit of the two-triangle exterior theorem

**Verdict: GREEN.** Separate internal mathematical audit of the complete
[source](hc7_degree8_two_triangle_exterior.md), including its degree-free
wheel lemma, at whole-source SHA-256
`e51564c9ffd857d15eb3d1de9c5cfa4ce9b9bfac514ac3188ac5379e2a745776`.
This is not external peer review or completion of Conjecture 19 or HC7.
Reversing exactly three promotion link changes recovers the audited draft
SHA-256 `7157308341ece1a0f60a04cf4b961e157edc39874f1161efddc787bd861a4329`.

## Inputs and scope

The three input files were read, and their hashes checked against their
adjacent GREEN audits: contraction closure `ab7ce8ad…987ccb4`, five-root
almost-clique `de183e35…7bba9cd`, and rooted wheel `f0fbab79…33f62a`.
The full hashes are pinned in the source. No external primary statement
was freshly inspected and no finite computation establishes this verdict.
The hypotheses allow every additional edge in the displayed neighbourhood;
no induced or disconnected-neighbourhood assumption enters the proof.

## Strongest inference checks

- **Degree-free wheel.** Thin triangle-root absorption replaces one
  nonroot by a root without identifying two boundary vertices of any
  surviving nonroot set. Root preimages stay connected and disjoint, and
  nonroot order strictly decreases. Stopping at two avoids the excluded
  one-nonroot case. There each nonroot misses at most one root when they
  are adjacent, and their union misses none. The two attachment assignments
  cannot both fail. The resulting two bags have the required distinct
  triangle contacts. Above order two, the original ordering proof uses
  only the boundary hypothesis and the triangle-root stopping condition.
- **Full component contacts.** The root degree estimates remain valid with
  extra edges. Contracting the two root pairs when a triangle root is
  missed loses at most one neighbour per nonroot, by the four-clique contact
  restriction; contracting the other triangle when an edge root is missed
  also loses at most one. Every nonroot-set boundary loses at most two.
  The exterior helper meets both nontriangle roots and misses at most one
  triangle root. Designating a different triangle root makes its possible
  omission independent of the almost-clique omission. All choices precede
  application of that theorem, and the fixed contraction preimages lift.
- **Simultaneous ports.** A separator `C` of size less than `p` leaves
  every port outside `C` in the reachable set `Y`, which avoids `M-C`.
  Thus every actual exit from `X union Y` lies in `Z union C`; the nonempty
  set `X` and vertex `v` survive, contradicting seven-connectivity.
  Disjoint paths use every port as a start and distinct missing roots as
  ends. Stopping at the first missing root excludes every other root from
  their interiors. Any interior vertex contacting `X` would itself be a
  port, impossible. Hence port replacement preserves the boundary size of
  **every** subset of `X`, not merely the boundary of `X` itself.
- **Terminal lift.** Seven distinct neighbour roots contain a whole
  prescribed triangle. Deleting two root preimages loses at most two
  boundary vertices; boundary seven and original minimum degree eight
  exclude singleton `X`. The eighth neighbour `h` is absent from every
  path preimage. Therefore `O+h` and `v` are disjoint adjacent full helpers
  for the lifted wheel. For the final side, the strengthened boundary
  loses only `b2,x,y`. A singleton full component is independently excluded
  by the literal `K_5^-` on it, `v` and `A`; minimum degree alone would
  not justify that step. The same two-helper construction then applies.

**Remaining obligations.** No gap was found in these claims. They prove
that the exterior is nonempty, connected and full to the eight roots.
They do not provide a compatible global allocation inside that remaining
component, close the complete two-triangle critical case, or settle any
global colouring conjecture. No quotient criticality is assumed.
