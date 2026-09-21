# Every graph with no K7-minus minor is six-colourable

**Author:** Cavit Erginsoy. **Draft:** 21 September 2026.

[PDF](main.pdf) · [LaTeX entry point](main.tex) ·
[separate internal audit](main_audit.md).

The manuscript proves that every finite simple `K7^-`-minor-free graph
is six-colourable, through a stronger extremal theorem for 4-bilight
graphs with at least `4n-2` edges. It includes the new supporting
constructions and states its external inputs explicitly. The proof is
computation-free. It does not prove HC7 or
claim external peer review or historical priority.

## Source map and provenance

| File | Contents |
|---|---|
| [main.tex](main.tex) | Main statements, context, attribution and AI-use disclosure. |
| [preliminaries.tex](preliminaries.tex) | Definitions and exact external tools. |
| [rooted.tex](rooted.tex) | Local constructions, rooted reductions and the two-helper theorem. |
| [global.tex](global.tex) | Separation consistency, degree-five and five-cut elimination, terminal cases and colouring. |
| [finite.tex](finite.tex) | The nine-vertex lemma: five complement types and explicit minor models. |
| [references.bib](references.bib) | Primary sources with version-specific theorem numbering. |

The draft consolidates the proof package at Git revision
`320ea3275197f3b5124b38fb26af24bb05754d57`, principally the
[global theorem](../../results/hc7_k7minus_bilight_extremal.md) and
[rooted helper theorem](../../results/five_root_one_missing_contact.md),
including their cited supporting proofs. The manuscript proves internal five-connectivity before
analysing contraction obstructions, simplifying that step; its separate
audit checks this reordering as well as the full conversion. The revised
degree-seven step uses an [elementary proof](../../results/hc7_k7minus_degree7_quotient_hand_proof.md)
with a [separate internal audit](../../results/hc7_k7minus_degree7_quotient_hand_proof_audit.md).
Its five maximal complement types give nine marked cases, covered by seven
rows of explicit models. The global proof uses the same replacement;
the earlier computer-assisted note and its audit remain unchanged.

The critical-graph density reduction was also obtained independently in
earlier repository work: the [29 July neighbourhood classification](https://github.com/cavit99/hadwiger-k7/blob/c3acf6216ce59a397721ffdc89d11e9c20031ba5/results/hc7_k7minus_degree7_clique_incidence.md)
and [1 August clique-uniqueness and density theorems](https://github.com/cavit99/hadwiger-k7/blob/2f78c8b46afc4ace5e7148f1e1d1f61314573689/results/hc7_k7minus_two_literal_k5_exclusion.md).
Together with Mader's seven-connectivity theorem, these give the conclusion
of Dvořák–Norin–Rahman Theorem 1.6, which the manuscript cites. The distinct
rooted-density and separation tools from their Sections 2–5 remain external
inputs. The Git dates do not establish those authors' discovery dates.

## Optional computational cross-check

The original exhaustive verification is retained for reproducibility;
it is no longer a proof dependency. Appendix A now proves the same lemma
directly, including the completeness of its classification and the models.

From the repository root:

```sh
uv run python3 active/hc7_k7minus_degree7_quotient_verify.py
```

If needed, prefix the command with
`UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache`. The program uses only the
Python standard library. Expected output:

```text
complement types: 29
full-or-one-missed attachment cases: 232
model support orders: {7: 67, 8: 102, 9: 63}
certificate digest: b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306
GREEN: every quotient contains a certified K_7^- minor
```

Verifier SHA-256:
`ac0c37438d802930a0aa80bfd1d6491101da3df9a55fac1e1cf3db5ae1b7e445`.
The [original source](https://github.com/cavit99/hadwiger-k7/blob/320ea3275197f3b5124b38fb26af24bb05754d57/active/hc7_k7minus_degree7_quotient_verify.py)
is unchanged. Its certificate validation shares predicates with the search;
the elementary proof removes this computational trust requirement.

## Build

From this directory:

```sh
mkdir -p /tmp/hc7-c21-manuscript-build
tectonic main.tex --outdir /tmp/hc7-c21-manuscript-build --keep-logs
```

After a source edit, rebuild, inspect every rendered PDF page and renew
the audit's hashes before replacing `main.pdf`. Keep intermediate build
files outside the repository. Current status and the boundary with HC7
remain in the [research ledger](../../RESEARCH_LEDGER.md).
