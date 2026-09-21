# Manuscripts

Read the [research ledger](../RESEARCH_LEDGER.md#manuscript-status) for
authoritative revision and review status. This is the collection map;
the [results map](../results/README.md) covers the larger proof library.
All manuscripts are drafts. Internal audits establish neither external
acceptance nor publication priority.

The collection has one principal paper, two independent specialist papers
and three preserved precursors.

## Principal paper

[Every graph with no K7-minus minor is six-colourable](k7minus-six-colour/main.pdf),
by Cavit Erginsoy, with [source](k7minus-six-colour/main.tex),
[separate manuscript audit](k7minus-six-colour/main_audit.md) and
[build and verification instructions](k7minus-six-colour/README.md).
Its 16 pages contain the complete C21 proof, supporting constructions,
explicit external inputs and the finite nine-vertex lemma. The
[original proof package](../results/hc7_k7minus_bilight_extremal.md)
and its two internal audits remain unchanged.

## Independent specialist papers

| Manuscript | Contents | Review and supporting material |
|---|---|---|
| **1. [A matroid proof of bipartite contractibility](bipartite-contractibility/main.pdf)** · [source](bipartite-contractibility/main.tex) | Universal fully rooted bipartite contractibility; sharp intrinsic radius two for scheme paths of at most three edges; precise flow corollary. | [Manuscript audit](bipartite-contractibility/main_audit.md) · [scope review](bipartite-contractibility/citation_novelty_review.md). The scope review records the earlier revision; the new manuscript audit covers the radius addition. |
| **2. [Paired clique minors from connected regions](paired-clique-regions/main.pdf)** · [source](paired-clique-regions/main.tex) | Arbitrary terminal-set size; one-sided theorem; two-sided linkage equivalence; sharp region requirement and polynomial construction. | [Manuscript audit](paired-clique-regions/main_audit.md) · [focused originality assessment](paired-clique-regions/citation_novelty_review.md). |

These are separate contributions: the new C21 proof neither invokes nor
subsumes them. The bipartite paper supplies an independent proof/repair
and a sharp radius refinement, not the first assertion of the general
existence conclusion. The paired-region paper supplies a sharp criterion
for arbitrary terminal-set size. Neither has a demonstrated NT-level
colouring consequence. The radius refinement does not prove BLR's general
depth assertion, Lemma 3.13. Comparative standing belongs to the ledger.

## Preserved precursors

These drafts retain their sources, PDFs and original audits at their
existing paths. They are not separate current publication candidates.

| Precursor | Preserved value |
|---|---|
| [Degree, defect and separators in critical graphs](k7minus-low-degree/main.pdf) · [source](k7minus-low-degree/main.tex) · [audit](k7minus-low-degree/main_audit.md) | Superseded headline: C21 excludes its critical host, and the new five-connected `4n-2` theorem excludes the broader defect theorem's `r>=6, e>=4n` class. [Independent surviving lemmas](k7minus-low-degree/README.md#surviving-independent-content) remain reusable. |
| [Even subdivisions are contractible](even-subdivision-contractibility/main.pdf) · [source](even-subdivision-contractibility/main.tex) · [provenance](even-subdivision-contractibility/README.md) | Direct even-subdivision proof and the degree-three argument retaining all roots on one shore. |
| [Every K2,n is contractible](k2n-contractibility/main.pdf) · [source](k2n-contractibility/main.tex) · [provenance](k2n-contractibility/README.md) | Short specialised matroid-packing proof. |

An [earlier rooted-web draft](../archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf)
remains in the historical archive.

The original low-degree snapshot with `n_8>=25+tau`, including its source,
bibliography, PDF and audit, remains in Git at revision
`f7b52aff0dfb2578bc30ade68f75df12671cf966` under `paper/k7minus-low-degree/`.
The revised audit distinguishes that historical review from the current
source and finite dependencies.

## Editorial revision

The 21 September revision explains the C21 proof strategy and makes the
NT degree-six and DNR rooted-star attributions explicit. All three current
papers name Cavit Erginsoy in the manuscript and PDF metadata. Their PDFs
were rebuilt and their audit hashes renewed; the precursor PDFs remain
unchanged. No theorem statement or proof was changed by this editorial pass.

The checked comparison versions have 17 pages for
[NT v1](https://arxiv.org/pdf/2507.03244v1), 35 for
[DNR v1](https://arxiv.org/pdf/2609.17760v1), 85 for
[Dvořák's rooted-K5 v1](https://arxiv.org/pdf/2609.13818v1), and nine for
[Liu–Luo v2](https://arxiv.org/pdf/2609.06867v2), including references.
These are arXiv PDFs; journal publication was not verified. Our C21 draft
uses a wider A4 layout than the earlier AMS Letter drafts, so its 16 pages
should not be treated as a measure of brevity relative to those papers.

## Further theorem packages

The [five-root wheel extension](../results/hc7_rooted_wheel_extension.md)
and [four-connected five-chromatic theorem](../results/four_connected_five_chromatic_minor.md)
remain a parked theorem package. Its precise endpoint is that
every four-connected `K_6-2K_2`-minor-free graph other than `K_5` is
four-colourable. It remains a theorem package rather than a manuscript;
a focused originality assessment is still required.

The [attachment and canonical-test counterexamples](../barriers/triangle_free_bipartite_attachment_counterexample.md)
are also parked. No additional manuscript is scheduled for either package.

## Build and review convention

Each current manuscript has a `main.tex` entry point and a checked
`main.pdf`. From its own directory, build into a fresh temporary directory:

```sh
mkdir -p /tmp/manuscript-build
tectonic main.tex --outdir /tmp/manuscript-build --keep-logs
```

Use a different temporary directory for simultaneous builds. Keep logs
and rendered review images outside the collection. After a source change,
rebuild and inspect every PDF page, and update the separate manuscript
audit to identify every TeX input, bibliography and final PDF by hash.
Previous audits are historical evidence only for the revisions they name.
