# Degree, defect and separators in critical graphs

**Reclassified 21 September 2026: preserved precursor.** The new
[C21 manuscript](../k7minus-six-colour/main.pdf), if correct, excludes the
hypothetical critical host studied here. Its five-connected `e>=4n-2`
theorem also excludes the broader defect theorem's `r>=6, e>=4n` class.
Those headline conclusions therefore no longer support a separate current
paper. The audited TeX, PDF and reviews are preserved unchanged.

Preserved structural manuscript: [source](main.tex), [PDF](main.pdf),
[separate internal manuscript audit](main_audit.md), and
[citation and originality scope](citation_novelty_review.md).
The status and hashes in the manuscript audit govern the exact revision it
covers; a result audit does not automatically audit its manuscript adaptation.

This is a paper about necessary conditions for a hypothetical counterexample
to Norin–Totschnig Conjecture 21. It does not prove that conjecture, Hadwiger's
conjecture for `t=7`, or a theorem established as comparable in significance
to Norin–Totschnig. Originality and publication priority remain unestablished.

## Surviving independent content

The uniform linked-clique theorem, fifth-root placement and exact boundary
colouring reflection retain their stated hypotheses. The six-connected
`K4`-neighbourhood closure at degree `d` uses `e>=4n+d-13`; for
`6<=d<=10` it reaches sparser graphs than the new `4n-2` theorem.
The degree-eight low-codegree theorem needs no global density or colouring
assumption. The [three-component `3,2,2` seven-cut colouring theorem](../../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
needs no excluded-minor hypothesis and may still apply to HC7.

These remain a library of lemmas, not an automatically justified replacement
paper. Their originality and further applications need separate assessment.
The old critical-host minimum-degree-eight, no-`K5` and defect conclusions
cannot be imported into a `K7`-minor-free host: such a host may contain `K7^-`.

## Contents and proof dependencies

- [main.tex](main.tex): introduction, full theorem statements, linked-clique
  and rooted-helper arguments, and the initial `n8 >= 25 + tau` bound.
- [degree-eight.tex](degree-eight.tex): independent triples, rooted deletion
  models and the computation-free conclusions `n8 >= 26 + tau` and
  an incident edge in at most three triangles at every degree-eight vertex.
- [connectivity-defect.tex](connectivity-defect.tex): an elementary
  eight-vertex lemma, a computer-assisted finite lemma with two parts, the
  six-connected degree-eight theorem, the degree-six disc bound and the
  broader theorem `D(G) >= 20 + r` for every `r`-connected
  `K7^-`-minor-free graph with `r >= 6` and `m >= 4n`.
  Applied to the critical host this gives `n8 >= 27 + tau`.
- [seven-cuts.tex](seven-cuts.tex): a computation-free proof that every
  seven-cut of the critical host has exactly two components. The planar
  `3,2,2` colouring theorem itself needs no minor exclusion.

The computation-free conclusions have their own complete proof chain and
do not depend on the finite lemma. The separator proof uses only the
component-count and boundary-colouring parts of the source results; its
proof does not import their unused connectivity or packing refinements.

The structural proof needs each of the following arguments. The linked
cliques and rooted placement establish minimum degree eight and exclude
`K5` subgraphs. The rooted deletion models give the computation-free
`26 + tau` bound, independently of the stronger finite result. The disc
argument and finite quotients prove the broader defect theorem, which
requires no colouring hypothesis. The separator proof adds a restriction
on seven-cuts that does not follow from either density bound.

The editorial revision consolidates the intermediate density bounds,
Jakobsen's inequality and the contraction identities. The unused edge-cover
count is omitted; the finite profiles below support reproducibility without
interrupting the proof. Font size and margins are unchanged.

The 11 August 2026 compact snapshot, its PDF, bibliography and audits are
preserved at Git revision `f7b52aff0dfb2578bc30ade68f75df12671cf966`, under
this directory. Its source hash was
`461e7433e0b2695ead1d0a3f46724f32989b880389a75ba89bcbecbd219e59fa`.
The current revision strengthens that snapshot; its older audit is not
reused as an audit of the new proofs.

## Finite verification

From the repository root, with dependencies fixed by `pyproject.toml` and
`uv.lock` (including NetworkX 3.6.1), run:

```sh
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 active/hc7_k7minus_degree7_quotient_verify.py
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py
```

Both ran successfully on 13 September 2026 with these outputs:

| Finite input | Coverage | Expected certificate digest (SHA-256) |
|---|---|---|
| Nine-vertex quotient | 29 complement types, 232 attachment cases, 232 checked models | `b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306` |
| Ten-vertex quotient | 424 local classes, 55 local survivors, 2,035 profiles, 2,031 checked positive models and four negatives | `8b9b31cae19b10a9e958a51dd2c8ef12193b655ec7ab2163b67b638dfc646501` |

The first input uses a standard-library-only generator and partition
checker. The second uses NetworkX's complete order-seven graph atlas,
exhaustive vertex extensions, exact isomorphism testing and a recursive
minor engine. Both check disjointness, connectivity and all required
adjacencies of positive certificates and have known positive/negative
calibrations. Its [separate result audit](../../results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md)
additionally records independent partition checks of the negative ten-vertex
quotients and all positive certificates. The independent audit checker was
an audit experiment, not a separately retained executable; the reproducible
executables are the two linked verifiers below.

The nine-vertex models use seven, eight or nine vertices in 67, 102 and
63 cases respectively. In the ten-vertex search, the minimum-degree filter
retains 4,443 extensions before exact isomorphism testing gives 424 classes.
The four negative profiles are as follows. Vertex labels are those encoded
by the graph6 string; `A` is the neighbourhood of the exterior vertex in
the local graph `J`.

| graph6 code for `J` | `V(J) \ A` | Degree sequence of `J` |
|---|---|---|
| `GLNM^_` | 5, 6 | 4, 4, 4, 4, 4, 4, 4, 4 |
| `Gfwhmk` | 0, 1 | 4, 4, 4, 4, 4, 4, 5, 5 |
| `Gfwhm{` | 0, 1 | 4, 4, 4, 4, 4, 5, 5, 6 |
| `GxNg~k` | 0, 1 | 4, 4, 4, 4, 4, 6, 6, 6 |

For each fixed labelled `J` in this table, the missed pair is unique,
adjacent, and has both ends of degree four. The manuscript states precisely
this property, which is the part of the classification used in the proof.

These are exhaustive finite statements about nine- and ten-vertex
quotients. Their applications to arbitrary hosts use written contractions
of whole exterior components. No bound on host order is assumed.

Verifier revisions:

| Executable | SHA-256 |
|---|---|
| [Degree-seven quotient verifier](../../active/hc7_k7minus_degree7_quotient_verify.py) | `ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445` |
| [Degree-eight quotient verifier](../../results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py) | `d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc` |

## Audited mathematical sources

These source hashes were checked against the adjacent audit records on
13 September 2026. They establish provenance, not manuscript audit status.
The source results are unchanged by this manuscript revision.

| Source | Adjacent internal audit | SHA-256 |
|---|---|---|
| [Independent triples](../../results/hc7_k7minus_exceptional_neighbourhood_completion.md) | [Audit](../../results/hc7_k7minus_exceptional_neighbourhood_completion_audit.md) | `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd` |
| [Computation-free complement, deletion and three-triangle lemmas](../../results/hc7_k7minus_degree_eight_triangle_poor_edge_packing.md) | [Audit](../../results/hc7_k7minus_degree_eight_triangle_poor_edge_packing_audit.md) | `2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449` |
| [Degree-six disk bound](../../active/hc7_k7minus_degree6_common_neighbour_bound.md) | [Audit](../../active/hc7_k7minus_degree6_common_neighbour_bound_audit.md) | `e157c0e8fa5805cee15888abb9a002d35d51d7e877154e7eee1a37627732493e` |
| [Degree-seven finite reduction](../../active/hc7_k7minus_degree7_common_neighbour_exclusion.md) | [Audit](../../active/hc7_k7minus_degree7_common_neighbour_exclusion_audit.md) | `663c1b7e0de9b0951de89801d52baf4aae12535d7807547d19d04fc10b00c4b0` |
| [Six-connected degree-eight theorem and defect ladder](../../results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md) | [Audit](../../results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md) | `06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844` |
| [Elementary seven-vertex boundary lemma](../../results/hc7_k7minus_seven_cut_contraction.md) | [Audit](../../results/hc7_k7minus_seven_cut_contraction_audit.md) | `bbb9919b6d04c08836526d017607d318323fe457baa75d4c3364be85a4ad1ff5` |
| [Boundary component models](../../results/hc7_k7minus_seven_boundary_component_descent.md) | [Audit](../../results/hc7_k7minus_seven_boundary_component_descent_audit.md) | `9e2f616c98dd17670f4d15e962f3b36e4fc1f4c4dc9aee4227eabeb51ca33913` |
| [Exact boundary-colouring reflection and capacity](../../results/hc7_k7minus_critical_seven_cut_capacity.md) | [Audit](../../results/hc7_k7minus_critical_seven_cut_capacity_audit.md) | `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34` |
| [Three-component colouring theorem](../../results/hc7_k7minus_three_component_seven_cut_exclusion.md) | [Audit](../../results/hc7_k7minus_three_component_seven_cut_exclusion_audit.md) | `1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96` |

## Build

From the repository root, keep transient TeX files outside Git:

```sh
mkdir -p /tmp/hadwiger-k7-structural-build
tectonic -X compile paper/k7minus-low-degree/main.tex --outdir /tmp/hadwiger-k7-structural-build
cp /tmp/hadwiger-k7-structural-build/main.pdf paper/k7minus-low-degree/main.pdf
```

The PDF is built from all four TeX files and `references.bib`; a manuscript
audit must pin that entire source set and the resulting PDF.

The 13 September 2026 editorial build produced 17 letter-size pages without TeX,
reference, citation, box or PDF-string warnings. Every page was rendered
and visually inspected, with the model tables checked at higher resolution.

A supplementary cross-check of the computation-free degree-eight proofs
also ran successfully:

```sh
UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 results/hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py
```

It checked 42 eligible neighbourhood classes, 336 rooted deletions and 378
almost-full exterior augmentations, together with the negative calibration
`GMs` followed by a backtick and `KK`. The certificate digest was
`6024f1bcececd88038a16700c6c867570524a774f312e5d3acc5a27934e58047`.
This executable is supplementary evidence; it is not a computational
premise of the computation-free proof.
