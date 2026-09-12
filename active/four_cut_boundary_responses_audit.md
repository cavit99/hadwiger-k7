# Audit of the chosen four-cut boundary responses

**Current verdict: GREEN.** The reviewed
[source](four_cut_boundary_responses.md) has SHA-256
`39e21ddc123d8d55fb2daf4760b39bddf5e1c4d08d8dec86d02af1a21bc50d95`.
The missed-root and full-contact response restrictions are accepted at
their stated scopes. No full separator case or global target is closed.

## Prior missed-root revision

**Verdict: GREEN — separate internal exact-source audit.**
The reviewed [source](four_cut_boundary_responses.md) has SHA-256
`1e2e95d605f04a51adbc727a58a3d5792b5a4afc9961b2f0822ed9fe909e89aa`.
This proves the stated restrictions on minimum responses, not four-cut
exclusion, C19, HC7 or an independently assessed NT-comparable theorem.

The reviewer participated in the minimum-partition discussion, but did
not author this source. This was a separate cold reading of its complete
argument and applications. It is internal review, not external peer
review; no finite computation or fresh literature inspection is a premise.
The final spelling, input citations and audited-status changes were checked;
reversing them recovers the earlier reviewed mathematical source exactly.

## Inputs and strongest checks

The source and audit hashes printed for the four-cut theorem, contraction
closure and four-root exception theorem were checked against the files.
Their stated hypotheses suffice here. The final application also uses
the [relative five-root wheel theorem](../results/five_root_relative_degree_six_wheel.md),
SHA-256 `46a2211c03938afb9fd5fc3e8e309f31ab7d102c3211a51f7a1c6e1adcb5ed6d`,
and its [audit](../results/five_root_relative_degree_six_wheel_audit.md),
SHA-256 `1c67692b6ce69ae068e9d1b14cc4b4f2884cc4d9c888373c76e5698c88f7163e`.

- **Actual open sides.** The bound of two R-neighbours gives at least
  three vertices in each original component. The missed root r contacts
  D, so C and E=D+r are connected and anticomplete. Their opposite side
  witnesses every required seven-neighbour bound, including subsets
  containing r. After deleting T, C and D vertices have degree at least
  six; only r can have degree five. Both S-rooted K4 applications are
  therefore valid and reserve T.
- **Reflection.** Connected realisations are on the side supporting the
  chosen proper response. They identify only independent boundary blocks.
  The quotient colouring expands only on the untouched closed side;
  its trace coarsens the old one. Minimum block count over both original
  languages forces equality, permitting a palette permutation and glue.
  Every use deletes or contracts a vertex of a nonempty open side, so
  proper-minor colourability applies. No consumed interior is recoloured.
- **The two-pair case.** Deleting the other three roots preserves relative
  boundary four and degree five. If those roots span an edge, at most two
  nonroots can lose three neighbours and reach degree five: three common
  neighbours would create a literal K5-minus in the displayed edge
  quotient. The four-root model then realises either prescribed pairing
  with disjoint preimages, irrespective of which shores its roots occupy.
- **Independent omitted roots.** Contracting their union with one whole
  open side makes their image full to the other four boundary roots.
  Expansion on the opposite side is proper. Minimum five forces exactly
  the one-triple trace, which reflection excludes. The analogous argument
  for an independent four-set is valid when the minimum is four.
- **Remaining patterns.** The integer partitions listed for three and
  four blocks are exhaustive after excluding a sole nonsingleton block.
  Deleting two singleton roots leaves relative boundary five, nonroot
  degree six and at least three nonroots. In W4, an adjacent pair and its
  complementary triple are both connected; merging their respective
  bags realises the 3+2 partition. An opposite rim pair remains unresolved.

No simultaneous three-pair realisation, preservation of S-injectivity
under arbitrary reflection, or root-clean carrier from bichromatic
component membership is proved or used. The minimum-three and remaining
minimum-four responses remain open.

## Both components contact all four clique roots

**Scoped verdict: GREEN.** Date: 12 September 2026. This review covers
the final section at current source hash
`39e21ddc123d8d55fb2daf4760b39bddf5e1c4d08d8dec86d02af1a21bc50d95`.
Removing that section and restoring the former title recovers exactly
the prior source `1e2e95d605f04a51adbc727a58a3d5792b5a4afc9961b2f0822ed9fe909e89aa`.
The earlier audit and its provenance above remain historical.

- **Strict whole-side contraction.** Each cut component has at least
  three vertices: a component of order at most two would give one of its
  vertices degree at most `1+4+2=7`, using the actual R-contact bound.
  Thus contracting D strictly reduces order. Its image is adjacent to
  every vertex of the eight-vertex boundary, so restriction of a proper
  six-colouring gives at most five boundary colours on the untouched
  original side. The R clique supplies the lower bound four. Nonemptiness
  alone would not justify this strict contraction; the stated size bound
  resolves that issue.
- **Reflection and independent four-set.** The old reflection argument
  uses independence of boundary blocks, fixed connected preimages and
  minimality over both original colouring languages, independently of
  boundary order seven. A sole nonsingleton block is still realisable
  with the whole connected coloured side. Contracting `D union I` for
  independent I of size four is connected and proper, and its image is
  full to the other four boundary vertices. Expansion only on the
  untouched side is proper. Under minimum five it forces precisely the
  excluded `4,1,1,1,1` response. The two remaining five-block patterns
  exhaust the integer partitions after that exclusion.
- **Four independent boundary traces.** Every proposed bag contains a
  distinct R root, so the literal R edges survive between all four bags.
  Their quotient colours are distinct. Independence of the traces makes
  boundary expansion proper on the untouched side, yielding exactly four
  blocks. Unused open-side vertices are deleted; any used vertex is
  contracted into a root-containing bag, so order strictly decreases.
  No pre-existing colouring on the consumed side is required, and none
  is reconstructed through its interior.

The reviewer participated in deriving these deductions and supplied an
earlier audit-ready formulation; the parent wrote the appended source.
This is a separate exact-source internal check, not independent discovery
or external peer review. The four bags themselves, a common response at
minimum four, full four-cut exclusion, C19, HC7 and independently assessed
NT-comparable significance remain unproved.
