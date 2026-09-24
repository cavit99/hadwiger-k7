# Independent audit of the six-colour manuscript

**Updated:** 24 September 2026. **Verdict:** GREEN.

This separate internal audit found no unresolved mathematical gap in the
manuscript's stated density theorem, rooted helper theorem or six-colour
corollary, subject to the cited external results. The original auditor
reconstructed the arguments and checked the conversion
from the research proofs; earlier audit verdicts were not treated as proof.
This is not external peer review, a historical priority assessment or a
proof of HC7.

The current revision is editorial. It retains the
[elementary proof with a separate focused audit](../../results/hc7_k7minus_degree7_quotient_hand_proof_audit.md)
that replaced the former computational premise. The reviews below
distinguish these revisions from the original full reconstruction.

## Exact revision

The audited manuscript is the following frozen source and its compiled
16-page PDF. SHA-256 values identify the exact files.

| File | SHA-256 |
|---|---|
| [main.tex](main.tex) | `9a01d50b276ad4698a17f830b1b8a8cb1f72df6aa5e027570ceb2b23217601cf` |
| [preliminaries.tex](preliminaries.tex) | `154216056703898d0fe7efe8c66f1fdc3ec6765a57523a9b116fbf042ed8f1e5` |
| [rooted.tex](rooted.tex) | `850470da79df0157db15e85d3be402c60ac67bfcddd3b9b99d73028d6c0f183c` |
| [global.tex](global.tex) | `0e95903cae23f4b7474c7fb8936871d6e5d337904955fc001eece62724c6210f` |
| [finite.tex](finite.tex) | `8ed1f5f2b8cdc0dd328045d5c57e4c267ccf779ffff28f360092fbe28205be44` |
| [references.bib](references.bib) | `ded089d41254ede7b13c9dee176b7a9d032f1ee95e88ae9e48524c40381f3336` |
| [main.pdf](main.pdf) | `4284ef08ed93affecba2988ac49e65a66a29526d9cebf220aafa8f854536c2d9` |

The following underlying proofs were inspected in the original
reconstruction or the focused revision review. The manuscript contains
its own supporting proofs rather than requiring the reader to reconstruct
them from these notes.

| Source | SHA-256 |
|---|---|
| [Global density and colouring theorem](../../results/hc7_k7minus_bilight_extremal.md) | `4c48b60d4de77de2afc357ba81b47d8f2107656b5684005f743d247f894620d3` |
| [Two-helper theorem](../../results/five_root_one_missing_contact.md) | `078ba860d4cdde187cdc6e618a4e1842dd623523dbefbe3ead06544c7d8afa18` |
| [Rooted reductions](../../results/hc7_c21_rooted_density_low_degree_reduction.md) | `431bd7d7d2b5bcb59e385781234c6d7ed6824f62ee50eb8ddf49e69da792cef2` |
| [Degree-five elimination](../../results/hc7_c21_helper_degree_six.md) | `85927a0f7d1af6229930fd67f7144eac35b934c54ad504539a34d39e209020ee` |
| [Rooted dart](../../results/rooted_dart_nonroot_degree_five.md) | `37dcf256f64fca7c49a1bd4ec66021371fba9a7863bf9523597ba4b898ecfad2` |
| [Elementary nine-vertex lemma](../../results/hc7_k7minus_degree7_quotient_hand_proof.md) | `34b881c8b29ca1abfd3d322ee1aa63d7cbc5b7f132aecca7edeb682844af3bd6` |

## Editorial revision, 24 September 2026

**Verdict: GREEN for mathematical equivalence.** A reviewer separate from
the editors compared all five LaTeX sources with Git revision
`66c9cabcee92a809be95e8e3dbc2e2dc700cf656` and checked the source hashes above.
The [preceding audit](https://github.com/cavit99/hadwiger-k7/blob/66c9cabcee92a809be95e8e3dbc2e2dc700cf656/paper/k7minus-six-colour/main_audit.md)
preserves the earlier artifact hashes.

The revision standardises branch-set terminology, clarifies the proof
outline and tightens the prose. The review checked that hypotheses,
quantifiers, root ownership, density and separation conditions, induction
and lifting are unchanged. In particular, adjacency to the branch sets
at a boundary does not require adjacency to every vertex in them, and
atom minimisation remains unrestricted by density. The introduction now
explicitly attributes the exact edge count to minimality. No theorem or
proof dependency changed; this was not a fresh reconstruction of the proof
or a new review of the external literature.

The editor rebuilt the 16-page PDF without warnings, inspected every
rendered page and recorded its hash above. The author, AI-use statement,
bibliography and computation-free proof are unchanged.

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

## Elementary quotient revision

**Verdict: GREEN for the replacement.** A reviewer separate from the editor
reconstructed the complement-maximalisation argument, checked all nine
marked cases by hand and compared them with the exact Appendix A pinned
above. Edge deletion has the correct monotonicity; the five maximal forms
and nine vertex orbits are exhaustive. All displayed bags are connected
and disjoint, with exactly twenty contacts. The unchanged global reduction
contracts a whole exterior component and lifts through its fixed connected
preimage. No new hypothesis or computational premise is needed.

This replaces the earlier appendix, SHA-256
`8917dba9aecb046eed6ac3b508837a9cdcc0d6800f012cf48b85837bb377c4f4`.
The [prior review record](https://github.com/cavit99/hadwiger-k7/blob/cb8a9db56144ba8151448095e0eda82213f1ec56/paper/k7minus-six-colour/main_audit.md)
preserves the original 232-case verification, its coverage and shared-predicate
trust boundary. The original note and verifier are unchanged. The editor
reran the verifier as an optional cross-check; its certificate digest is
unchanged. It is no longer an input to the manuscript's proof.

The editor rebuilt the 16-page PDF without warnings, rendered all pages
and visually inspected pages 1 and 16. The other fourteen page renders
are byte-identical to the previous PDF. The introduction now describes
the elementary proof; the author, AI-use statement and theorem scopes
are unchanged. These build and rendering checks are the editor's report.
The separate replacement audit covers the exact proof sources.

## Prior attribution revision

**Verdict: GREEN for the editorial change.** A reviewer separate from the
editor compared the frozen sources with Git base
`373ec9d9272223063bb9df401aea80c9efb50890`. The introduction and an
immutable historical citation now recognise the repository's independent
critical-graph density reduction. The reviewer inspected the dated July
and August proofs: vertex deletion gives chromatic number seven, Mader
gives seven-connectivity, and Corollary 3 at revision `2f78c8b` gives
the density required by DNR Theorem 1.6. These Git records do not establish
the other authors' discovery dates or historical firstness.

The final colouring proof retains DNR Theorem 1.6 as its cited formulation.
The distinct rooted-density and separation inputs remain attributed to
DNR. In that revision, no theorem, mathematical argument, finite input or
verification code changed. The reviewer checked its source and PDF hashes;
the editor reported a warning-free 16-page build and visual inspection.
The linked prior review record preserves those artifact pins. The current
elementary-proof replacement and its rendering checks are recorded above.
