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

## Scope and headline progress

The sole active target is Norin--Totschnig Conjecture 21: every
`K_7^-`-minor-free graph is six-colourable, where `K_7^-` is `K_7` with one
edge deleted.  This would follow already from the conditional extremal
statement that every seven-connected `n`-vertex graph with at least `4n`
edges contains a `K_7^-` minor.  The older universal `4n-2` statement and
the five-connected `4n-7` laboratory remain stronger conditional routes,
not primary targets.  None of these statements is proved here.

The project works from a hypothetical minor-minimal non-six-colourable
`K_7^-`-minor-free graph `G`.  The audited computation-free chain now gives

```text
n_7 = 0,  delta(G) >= 8,  |E(G)| >= 4|V(G)|,
G has no K_5 subgraph,  and  n_8 >= 25 + tau,
```

where `tau` is the degree excess above nine.  Every degree-eight
neighbourhood is `K_4`-free, and every seven-vertex separator leaves exactly
two components.  Thus the remaining target for the critical graph is to
prove `n_8 <= 24`.  These are necessary structural conditions on a
hypothetical counterexample; they do not prove Conjecture 21 or `HC_7`.

The direct `HC_7` programme is frozen.  Its audited bounded-separation,
colouring-response and labelled near-clique results leave an unresolved
branch-set and colouring synchronisation problem.  The
[bounded-interface frontier](active/hc7_bounded_interface_synchronization_frontier.md)
records that exhaustive direct-`HC_7` obligation; it is not a parallel
active target.

The exact live theorem changes as new reductions are proved. Its
authoritative status is maintained in the research ledger, and its full
hypotheses and trust boundary are stated in the technical frontier rather
than duplicated here.

### Partial-results manuscript status

The current manuscript is the eight-page, computation-free draft
[Minimum degree eight in `K_7^-`-minor-free contraction-critical
graphs](paper/k7minus-low-degree/main.pdf),
with [LaTeX source](paper/k7minus-low-degree/main.tex), a
[hash-pinned internal audit](paper/k7minus-low-degree/main_audit.md),
and a separate
[internal citation and novelty review](paper/k7minus-low-degree/citation_novelty_review.md).
Both reviews are internal checks, not external peer review or a priority
certificate.  The manuscript proves the linked-cliques theorem, excludes
degree seven, and derives the current low-degree and density package.  The
former rooted-web manuscript is retained as a clearly labelled
[historical draft](archive/manuscripts/k7minus-rooted-web-2026-08-09/main.pdf).
The broader
[external-review blueprint](active/hc7_partial_results_external_review_blueprint.md)
is frozen.  This manuscript proves neither the `K_7^-` six-colour conjecture
nor `HC_7`.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Sole authority for current research status |
| [`active/INDEX.md`](active/INDEX.md) | Concise navigation to live proof work |
| [Degree-eight finishing frontier](active/hc7_k7minus_seven_exceptional_frontier.md) | Sole active route, finishing reduction, and current support-allocation obstruction |
| [`K_7^-` strict-density frontier](active/hc7_k7minus_density_frontier.md) | Stronger conditional `4n-2` route, minimal-enemy reductions, and exact nonclosures |
| [External-review and manuscript blueprint](active/hc7_partial_results_external_review_blueprint.md) | Frozen theorem package, review questions, reproduction plan, and restart criteria |
| [Live case verification map](active/hc7_live_case_dag.md) | Exhaustive global chain, conditional refinements, and every missing descent arrow |
| [Bounded-interface technical frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Frozen all-degree target, direct inputs, and trust boundary |
| [Degree-seven technical frontier](active/hc7_degree7_model_separator_frontier.md) | Conditional exact-seven refinement and residual cases |
| [`K_7^-` specialist-review dossier](active/hc7_k7minus_external_review_dossier.md) | Frozen hash-pinned review provenance predating the rooted `K^*_{4,2}` closure |
| [`K_7^-` minimum-degree-eight draft](paper/k7minus-low-degree/main.pdf) | Eight-page computation-free paper containing the linked-cliques theorem, degree-seven exclusion and the low-degree critical-host package |
| [Order-seven separator component bound](results/hc7_k7minus_critical_seven_cut_capacity.md) | Excludes four-component seven-vertex separators in the critical graph and normalises the three-component boundary |
| [Low-degree bounded-interface entry](results/hc7_low_degree_adjacent_pair_alignment.md) | Uniform entry from a hypothetical counterexample |
| [Component-uniform boundary alignment](results/hc7_component_uniform_boundary_alignment.md) | A named edge-deletion response for every exterior component at one low-degree vertex |
| [Exterior-component upper bounds](results/hc7_low_degree_exterior_component_bounds.md) | At most one, two and three components at degrees seven, eight and nine |
| [Exact order-seven packing restrictions](results/hc7_exact_seven_packet_packing.md) | Limits disjoint connected subgraphs adjacent to every vertex of an order-seven boundary |
| [Component-deletion Kempe exchange](results/hc7_component_deletion_kempe_exchange.md) | Simultaneous component-supported augmentation and rejection-map dichotomy |
| [Full-component common-root exchange](results/hc7_full_exterior_component_common_root_exchange.md) | Exact two-component rooted residue in the full unique-rejector case |
| [Degree-seven boundary-labelled near-clique model](results/hc7_degree7_aligned_near_k7_model.md) | Principal degree-seven structural compression |
| [Research integrity tools](tools/README.md) | Search, curated dependency metadata, audit hashes, and CI checks |

Read a theorem in [`results/`](results/) together with its adjacent
`_audit.md` file. Refuted intermediate principles and their exact scope are
kept in [`barriers/`](barriers/). Superseded work remains in
[`archive/`](archive/) for provenance.

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
python3 tools/research_index.py build
python3 tools/research_index.py search '"bounded interface"'
python3 tools/research_index.py context hc7.target.k7minus_six_colour_conjecture
python3 tools/research_index.py check
python3 tools/research_index.py report
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
