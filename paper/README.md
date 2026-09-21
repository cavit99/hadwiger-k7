# Manuscripts

Read the [research ledger](../RESEARCH_LEDGER.md#manuscript-status) for
authoritative revision and review status. This is the collection map;
the [results map](../results/README.md) covers the larger proof library.
All manuscripts are drafts. Internal audits establish neither external
acceptance nor publication priority.

The immediate editorial priority is the new
[complete C21 proof package](../results/hc7_k7minus_bilight_extremal.md),
with [two](../results/hc7_k7minus_bilight_extremal_audit.md)
[internal audits](../results/hc7_k7minus_bilight_extremal_second_audit.md).
It has not yet been assembled into a manuscript PDF. The existing papers
below retain their original scopes.

## Existing manuscript collection

| Manuscript | Contents | Review and supporting material |
|---|---|---|
| **1. [A matroid proof of bipartite contractibility](bipartite-contractibility/main.pdf)** · [source](bipartite-contractibility/main.tex) | Universal fully rooted bipartite contractibility; sharp intrinsic radius two for scheme paths of at most three edges; precise flow corollary. | [Manuscript audit](bipartite-contractibility/main_audit.md) · [scope review](bipartite-contractibility/citation_novelty_review.md). The scope review records the earlier revision; the new manuscript audit covers the radius addition. |
| **2. [Paired clique minors from connected regions](paired-clique-regions/main.pdf)** · [source](paired-clique-regions/main.tex) | Arbitrary terminal-set size; one-sided theorem; two-sided linkage equivalence; sharp region requirement and polynomial construction. Selected as the next standalone package. | [Manuscript audit](paired-clique-regions/main_audit.md) · [focused originality assessment](paired-clique-regions/citation_novelty_review.md). |
| **3. [Degree, defect and separators in K7-minus-minor-free critical graphs](k7minus-low-degree/main.pdf)** · [source](k7minus-low-degree/main.tex) | Necessary critical-host conditions: computation-free 26+tau, broader connectivity–defect theorem giving 27+tau with explicit finite inputs, and computation-free two-component seven-cut closure. | [Manuscript audit](k7minus-low-degree/main_audit.md) · [dependencies and finite verification](k7minus-low-degree/README.md) · [citation review](k7minus-low-degree/citation_novelty_review.md). |

Here `tau=sum_{i>=10}(i-9)n_i` and `n_i` counts degree-i vertices; the
bounds are on `n_8`. The radius refinement does not prove BLR's general
depth assertion, Lemma 3.13. The structural paper does not prove
Norin–Totschnig Conjecture 21. None of these manuscripts establishes
`HC_7`; the ledger's new benchmark assessment concerns the separate C21
proof package, not these earlier manuscripts.

## Preserved precursors

These simpler proofs retain their sources, PDFs and original audits at
their existing paths. Their bipartite conclusions are subsumed by the
universal theorem, so they are not separate current publication candidates.

| Precursor | Preserved value |
|---|---|
| [Even subdivisions are contractible](even-subdivision-contractibility/main.pdf) · [source](even-subdivision-contractibility/main.tex) · [provenance](even-subdivision-contractibility/README.md) | Direct even-subdivision proof and the degree-three argument retaining all roots on one shore. |
| [Every K2,n is contractible](k2n-contractibility/main.pdf) · [source](k2n-contractibility/main.tex) · [provenance](k2n-contractibility/README.md) | Short specialised matroid-packing proof. |
| [Earlier rooted-web manuscript](../archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf) | Historical structural architecture and proof provenance. |

The original low-degree snapshot with `n_8>=25+tau`, including its source,
bibliography, PDF and audit, remains in Git at revision
`f7b52aff0dfb2578bc30ade68f75df12671cf966` under `paper/k7minus-low-degree/`.
The revised audit distinguishes that historical review from the current
source and finite dependencies.

## Further theorem packages

The [five-root wheel extension](../results/hc7_rooted_wheel_extension.md)
and [four-connected five-chromatic theorem](../results/four_connected_five_chromatic_minor.md)
form the next colouring-focused candidate. Its precise endpoint is that
every four-connected `K_6-2K_2`-minor-free graph other than `K_5` is
four-colourable. It remains a theorem package rather than a manuscript;
a focused originality assessment is still required.

The [attachment and canonical-test counterexamples](../barriers/triangle_free_bipartite_attachment_counterexample.md)
are reserved for a possible separate note. Their longer proof is kept
outside the concise bipartite paper.

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
