# Hadwiger's Conjecture for $K_7$-minor-free graphs

> **Research status:** $HC_7$ is not proved in this repository.

This repository is an open research workspace on the first unresolved case
of Hadwiger's Conjecture. It contains written partial results, conjectural
proof targets, computer-assisted finite results, internal audits, and
counterexamples to intermediate claims. Internal audits are not external
peer review.

The notation `$HC_7$` used in historical filenames and internal claim IDs
indexes the excluded clique `K_7`. In Seymour's convention, where `HC(t)`
means that every `K_{t+1}`-minor-free graph is `t`-colourable, this is
`HC(6)`.

## The problem

A $K_t$-minor model in a graph $G$ consists of $t$ pairwise disjoint
connected branch sets, with an edge between every pair. Hadwiger's
Conjecture asserts

$$
K_t\not\preccurlyeq G\quad\Longrightarrow\quad \chi(G)\le t-1.
$$

The conjecture is known for $t\le6$; the $t=6$ case is due to
[Robertson, Seymour, and Thomas](https://doi.org/10.1007/BF01202354),
building on the Four-Colour Theorem. It remains open for every $t\ge7$.
This repository studies

$$
HC_7:\qquad K_7\not\preccurlyeq G\quad\Longrightarrow\quad\chi(G)\le6.
$$

## Current research status

The sole active completion target is the following open statement.

> **T44.** Every seven-connected graph containing a `K_{4,4}` minor
> contains a `K_7^-` minor, where `K_7^-` is `K_7` with one edge deleted.

Kawarabayashi--Toft's `K_7`-or-`K_{4,4}` theorem makes T44 sufficient for
Norin--Totschnig Conjecture 21.  T44 would not by itself prove `HC_7`.
The exact hypotheses, proved inputs and two remaining obligations are in the
[T44 technical frontier](active/hc7_k44_closure_frontier.md).  The
[research ledger](RESEARCH_LEDGER.md) is the sole authority for current
status; [the active index](active/INDEX.md) is the concise navigation map.

The former exceptional-centre, density and direct-`HC_7` programmes are
preserved as frozen or conditional routes, not parallel active targets.
None of their completion statements is proved here.

## Selected completed work

The repository contains many proof notes.  The following are the strongest
reader-facing completed results; the [selected-results map](results/README.md)
links their proofs, audits and exact scopes.

| Result | Status and scope |
|---|---|
| [Every `K_{2,n}` is contractible](results/k2n_contractibility_via_matroid_packing.md) | Computation-free written proof with a [hash-pinned GREEN internal audit](results/k2n_contractibility_via_matroid_packing_audit.md) and a [four-page manuscript](paper/k2n-contractibility/main.pdf).  It answers the `K_{2,4}` half of Kündgen--Pelsmajer--Ramamurthi's Section 8, Question 2. |
| [Five-root partial routing](results/llru_question61_via_km_property_star.md) | Written proof with a [GREEN audit](results/llru_question61_via_km_property_star_audit.md) and a [second GREEN cold audit](results/llru_question61_via_km_property_star_second_cold_audit.md).  It answers Lafferty--Liu--Rolek--Yu Question 6.1 and gives their stated `k>=11` connectivity consequence. |
| [Four prescribed roots in a three-connected graph](results/rooted_k4minus_four_roots.md) | Elementary unbounded proof, with a [GREEN audit](results/rooted_k4minus_four_roots_audit.md), of a rooted `K_4^-` minor at any four distinct roots.  The missing quotient edge is not prescribed. |
| [Degree-eight low-codegree and defect theorem](results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md) | Written unbounded host reduction with one deterministic finite local lemma and [two GREEN internal audits](results/hc7_k7minus_sixconnected_degree_eight_low_codegree_audit.md).  It upgrades the current critical-host count to `n_8>=27+tau`. |
| [Three-component order-seven-cut exclusion](results/hc7_k7minus_three_component_seven_cut_exclusion.md) | Computation-free written proof with a [GREEN audit](results/hc7_k7minus_three_component_seven_cut_exclusion_audit.md).  In the critical `K_7^-` host, every seven-vertex cut therefore leaves exactly two components. |

The preserved critical-host chain now gives

```text
n_7 = 0,  delta(G) >= 8,  |E(G)| >= 4|V(G)|,
G has no K_5 subgraph,  and  n_8 >= 27 + tau,
```

where `tau=sum_{i>=10}(i-9)n_i`.  Every degree-eight neighbourhood is
`K_4`-free.  Thus `n_8<=26` would finish Conjecture 21.  These are necessary
conditions on a hypothetical counterexample, not a proof of Conjecture 21
or `HC_7`.

## Manuscripts

The primary circulation candidate is the clearly marked four-page DRAFT
[Every `K_{2,n}` is contractible](paper/k2n-contractibility/main.pdf), with
[source](paper/k2n-contractibility/main.tex), a
[hash-pinned GREEN internal audit](paper/k2n-contractibility/main_audit.md)
and a
[qualified-GREEN citation and novelty review](paper/k2n-contractibility/citation_novelty_review.md).
It is computation-free and independent of the Hadwiger programme.

The compact `K_7^-` paper is the clearly marked eight-page DRAFT
[Minimum degree eight in `K_7^-`-minor-free contraction-critical
graphs](paper/k7minus-low-degree/main.pdf), with
[source](paper/k7minus-low-degree/main.tex), a
[hash-pinned internal audit](paper/k7minus-low-degree/main_audit.md) and an
[internal citation and novelty review](paper/k7minus-low-degree/citation_novelty_review.md).
It is a frozen, computation-free snapshot: it proves the linked-cliques
theorem, excludes degree seven and obtains the baseline bound
`n_8>=25+tau`.  The later `27+tau` strengthening above is not incorporated
in that draft.

The former rooted-web manuscript is retained as a clearly labelled
[historical DRAFT](archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf).
Neither `K_7^-` manuscript proves Conjecture 21 or `HC_7`.  See the
[manuscript map](paper/README.md) for the exact distinction.

## Repository map

| Location | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Sole authority for current mathematical status |
| [`active/INDEX.md`](active/INDEX.md) | Sole active target and its direct proved inputs and barriers |
| [`results/README.md`](results/README.md) | Selected completed and audited proofs; navigation only |
| [`paper/README.md`](paper/README.md) | Current and historical manuscript map |
| [`barriers/`](barriers/) | Counterexamples to intermediate claims, with exact scope |
| [`archive/`](archive/) | Frozen, superseded and retracted work retained for provenance |
| [`tools/README.md`](tools/README.md) | Search, curated dependency metadata, audit hashes and integrity checks |

Directory placement alone does not establish a claim.  Read a theorem in
[`results/`](results/) together with its adjacent audit, and use the ledger
to determine whether it belongs to the current proof spine.

## Claim labels

- **Written proof:** a proof with explicit hypotheses and conclusion.
- **Separate internal audit:** an independent agent checked that revision;
  this is not peer review.
- **Computer-assisted finite result:** an exact finite reduction with
  retained code and, where practical, checkable certificates.
- **Conjectural target:** an unproved next theorem.
- **Recorded negative finding / route nonclosure:** a failed mechanism or
  unsupported inference, not a counterexample.
- **Barrier:** a counterexample to an intermediate claim, not to Hadwiger's
  Conjecture.

Finite computation is used to test conjectured lemmas and settle explicitly
finite subproblems. It is never substituted for an unbounded proof.

## Research memory and integrity

Every tracked Markdown file, including archived work, is searchable through
a disposable SQLite/FTS index:

```bash
uv run --locked python tools/research_index.py build
uv run --locked python tools/research_index.py search '"bounded interface"'
uv run --locked python tools/research_index.py context hc7.target.k44_sevenconnected_closure
uv run --locked python tools/research_index.py check
uv run --locked python tools/research_index.py report
```

The generated index and reports are retrieval and integrity aids. Markdown
proofs remain authoritative, `RESEARCH_LEDGER.md` is the sole status
authority, and the curated dependency graph is not presumed complete.

## Repository layout

```text
.
├── README.md            # durable public overview
├── RESEARCH_LEDGER.md   # authoritative current research status
├── AGENTS.md            # workflow and proof-integrity rules
├── tools/               # generated index and integrity checks
├── results/             # written claims and adjacent audits
├── active/              # current proof targets and live scripts
├── barriers/            # counterexamples to intermediate claims
└── archive/             # superseded work retained for provenance
```

See [`AGENTS.md`](AGENTS.md) before contributing. Prefer standard
graph-theoretic language, state exact trust boundaries, and do not modify an
audited theorem without renewing its audit.

## Licence

Repository materials are available under the [MIT License](LICENSE). The
licence permits reuse; it does not certify the mathematical claims.
