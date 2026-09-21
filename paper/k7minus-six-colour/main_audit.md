# Independent audit of the six-colour manuscript

**Date:** 21 September 2026. **Verdict:** GREEN.

This separate internal audit found no unresolved mathematical gap in the
manuscript's stated density theorem, rooted helper theorem or six-colour
corollary, subject to the cited external results and the finite verification
below. The auditor reconstructed the arguments and checked the conversion
from the research proofs; earlier audit verdicts were not treated as proof.
This is not external peer review, a historical priority assessment or a
proof of HC7.

## Exact revision

The audited manuscript is the following frozen source and its compiled
16-page PDF. SHA-256 values identify the exact files.

| File | SHA-256 |
|---|---|
| [main.tex](main.tex) | `732de540ad860baa937aae51c4fa0aaef2ec07d2a1998504e5a7119159b07349` |
| [preliminaries.tex](preliminaries.tex) | `2c0901be8ce7b215e2975532be13c13e76cff675fe21cb28cacd0abecfbb3013` |
| [rooted.tex](rooted.tex) | `d76f410bfa9ab159daf1fcd585e1796d52c279070df42bbb40168fb35e4adbef` |
| [global.tex](global.tex) | `f46116a341e9415bbfcc9134b473598e69d0da44ca7e33ff4cd06030ea2b6a12` |
| [finite.tex](finite.tex) | `8917dba9aecb046eed6ac3b508837a9cdcc0d6800f012cf48b85837bb377c4f4` |
| [references.bib](references.bib) | `cc2ef60233fb4fc6f7b0f1305d1e77e57a1aca2d392b7b880f8b07907f5ad51c` |
| [main.pdf](main.pdf) | `bd3de99533a4678be71d58fd4acbc21c06a7a80beaceb8d9efeda03d71b9492f` |
| [Finite verifier](../../active/hc7_k7minus_degree7_quotient_verify.py) | `ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445` |

The following underlying proofs were inspected when reconstructing the
manuscript. The manuscript contains its own supporting proofs rather than
requiring the reader to reconstruct them from these notes.

| Source | SHA-256 |
|---|---|
| [Global density and colouring theorem](../../results/hc7_k7minus_bilight_extremal.md) | `4ffbe9fc80a47713173a5f260759959da9397379ff26c2b18754eba5e97a560f` |
| [Two-helper theorem](../../results/five_root_one_missing_contact.md) | `078ba860d4cdde187cdc6e618a4e1842dd623523dbefbe3ead06544c7d8afa18` |
| [Rooted reductions](../../results/hc7_c21_rooted_density_low_degree_reduction.md) | `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2` |
| [Degree-five elimination](../../results/hc7_c21_helper_degree_six.md) | `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee` |
| [Rooted dart](../../results/rooted_dart_nonroot_degree_five.md) | `37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2` |
| [Degree-seven quotient reduction](../../active/hc7_k7minus_degree7_common_neighbour_exclusion.md) | `663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0` |

## Main inferences checked

- **External tools and small root sets.** The labelled target table agrees
  with Dvořák's Theorem 4 and the version reproduced in DNR Theorem 2.6.
  Lightness for `k` roots tests boundaries of order less than `k`, rather
  than always testing order four. The root-forgetting inequality, maximal
  reducible-fragment replacement and extraction hypotheses are retained.
  When an isolator has order equal to the root count, the manuscript now
  explicitly chooses the whole-graph isolator; the total density bound
  then applies. The empty rooted clique covers zero-root isolators.
- **Reordered rooted induction.** Nonroot minimum degree five and internal
  five-connectivity follow from the basic reductions without using the
  later contraction obstruction. Consequently a violating quotient set
  cannot contain a contracted nonroot vertex: its preimage would have
  boundary at most four. A contracted root is excluded by root-freeness.
  This gives a direct, noncircular replacement for the source's compressed
  merged-interior argument. The remaining blocker has the claimed proper
  five-boundary, density one and no shared neighbour of the contracted ends.
- **Root ownership and degree five.** The adjacent degree-five pair's
  rerooted density is exactly its number of missing target edges. The
  labelled density theorem supplies those edges simultaneously. Its two
  eventual helper bags avoid all original roots. The local quasi-five
  contraction lemma was checked by its corner counts; the subsequent
  lightness argument handles both possible singleton sides. All actual
  reductions decrease order or, for edge deletion, lexicographic size,
  and lift through fixed disjoint connected preimages.
- **The padded atom.** The selected atom minimises over all eligible
  fragments, without any positive-density restriction. Padding excludes
  atoms meeting the roots, and is never used to construct a minor model.
  Mader's precise hypothesis is `S subseteq T minus the opposite fragment`;
  its overbar was checked in the rendered primary statement. The low edge
  meets the atom and has both ends outside its opposite fragment, giving
  exactly the hypotheses and the contradiction in the manuscript.
- **Global compatibility.** The expanded DNR separation argument retains
  the lower-root density and lightness assumptions. The joined models
  assign disjoint path interiors to matching root bags, including trivial
  paths at shared boundary vertices. The degree-five four-cycle cases,
  the low-side rooted-star construction and every corner case of the end
  lemma were reconstructed. Every connectivity invocation has a nonempty
  opposite side. A minimum low eligible fragment is an unrestricted end
  because a smaller heavy fragment would violate orientation consistency.
- **Terminal cases and scope.** Once six-connectivity is established,
  contractions force four common neighbours on each edge. The degree-six
  two-paths argument uses six-connectivity directly; its separation lifts
  to a proper cut of order at most five. The degree-seven reduction uses
  one entire exterior component, with a valid fixed preimage. DNR
  Theorem 1.6 supplies exactly the connectivity and density needed for the
  colouring corollary. No proper minor is assumed to inherit chromatic
  criticality, and neither theorem asserts HC7.

Primary statements and proofs inspected include
[Dvořák, Theorem 4](https://arxiv.org/html/2609.13818v1),
[DNR, Sections 2–5 and Theorem 1.6](https://arxiv.org/html/2609.17760v1),
[Kriesell–Schmidt, Theorem 5, printed page 5](https://arxiv.org/pdf/1610.09093v1),
and the RST two-paths statement reproduced as
[Norin–Totschnig, Theorem 13](https://arxiv.org/html/2507.03244v1).
The dart uses the explicitly identified terminal construction from DNR
Lemma 3.1. The local quasi-five lemma is proved in the manuscript; the
stronger global hypotheses of its cited source are not silently assumed.
The audit does not reprove the full external dependency chains.

## Finite verification

The auditor read the generating and checking code and ran:

```sh
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_k7minus_degree7_quotient_verify.py
```

It returned 29 complement types, 232 attachment cases and model support
counts `{7: 67, 8: 102, 9: 63}`, with certificate digest
`b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306`.
The path-and-cycle classification covers every relevant seven-vertex
complement. The 750 partitions cover every seven-bag model on a subset
of the nine-vertex quotient. Each returned model is checked for disjointness,
nonemptiness, connectivity and at most one missing contact. The positive
and negative sanity checks pass. Search and validation share predicates;
this is not a separately implemented checker. This finite boundary does
not impose an order bound on the original graphs.

All TeX sources were read. Text extracted from the frozen PDF was checked
for the principal statements, author, final deduction, finite appendix and
references. The manuscript records Cavit Erginsoy as author, distinguishes
external inputs from the new construction, discloses AI use and makes no
claim of external review or historical firstness. No unresolved assumptions
beyond the stated external theorems and finite computation were found.

## Editorial revision review

The revision above was compared with Git base
`80ea4d8821e053ce1e0ade60971ee9a6a4f436a8`, which preserves the original
conversion audit and its hashes. This additional review concerns the
editorial diff; it is not a claim that a new mathematical result was proved
or that the entire external literature was reaudited.

The introduction now explains the missing-contact obstruction, separates
the auxiliary atom selection from the actual minor construction, and gives
the proof steps in their dependency order. The degree-six argument is
explicitly attributed to Norin–Totschnig's Section 3. The comparison with
DNR Lemma 4.10 retains the rooted-star lemma's independence assumption;
it does not claim an unconditional strengthening of that published lemma.
These attributions agree with the primary statements and arguments inspected
in the original review. All theorem statements, hypotheses and proofs,
including root ownership, induction parameters and lifts, are unchanged.
The finite verifier and appendix are unchanged, so their recorded check was
not repeated.

All 16 pages of the rebuilt PDF were visually inspected. Equations, labels,
tables, author details, page headers and the now left-aligned bibliography
render correctly, with no clipping, overlapping text or missing glyphs found.
The refreshed hashes were checked directly. The GREEN verdict and its
original mathematical scope are unchanged.
