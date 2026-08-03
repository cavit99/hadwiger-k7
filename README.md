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
building on the Four-Colour Theorem. This repository studies

$$
HC_7:\qquad K_7\not\preccurlyeq G\quad\Longrightarrow\quad\chi(G)\le6.
$$

## Scope and headline progress

The current research focus is the unconditional statement that every
seven-connected `n`-vertex graph with at least `4n-2` edges contains a
`K_7^-` minor.  This would settle the Norin--Totschnig `K_7^-` six-colour
conjecture, but not `HC_7`.

The project works from a hypothetical minor-minimal counterexample. Such a
graph is seven-connected, is seven-chromatic, has no $K_7$ minor, and every
proper minor is six-colourable.

The frozen direct `HC_7` programme contains audited bounded-separation,
colouring-response, exterior-component and labelled near-clique theorems.
Its unresolved task is to synchronise branch-set labels and proper-minor
colourings into an explicit `K_7` model, a common boundary partition, or a
strict same-host descent.  The [bounded-interface frontier](active/hc7_bounded_interface_synchronization_frontier.md)
records that conditional programme; it is not a parallel active target.

Separately, a computation-free, internally audited route towards the adjacent
`K_7^-` problem, where `K_7^-` is `K_7` with one edge deleted, proves that
every six-connected `K_7^-`-minor-free graph has at most one literal `K_5`.
Consequently, every hypothetical minor-minimal non-six-colourable host has
at most four degree-seven vertices, at least `4n-2` edges, and at least
`17+tau` exceptional degree-eight vertices, where `tau` is the excess
degree above nine.  If all four possible degree-seven vertices occur, the
host has order at least 37 and at least `32+tau` exceptional vertices.  The
anti-neighbourhood of every exceptional vertex is connected whenever a
degree-seven vertex exists.  The route also gives exact degree-seven
neighbourhoods and proves that outside
every order-seven cut there are at most four disjoint connected subgraphs
each adjacent to every boundary vertex, with exact whole-component
contraction criteria; the number of complementary components is at most
three, and a three-component boundary is subcubic.  In the
minor-minimal non-six-colourable host, exact boundary-colouring reflection
first restricts a possible three-component cut to colour classes of sizes
`3,2,2`; the audited three-shore planar-extension theorem then six-colours
that configuration.  Thus every order-seven cut in the critical host has
exactly two complementary components.  These are structural theorems about
a hypothetical critical graph and about seven-connected
`K_7^-`-minor-free graphs; they are not the bare extremal `4n-2` theorem, the
`K_7^-` six-colour conjecture, or `HC_7`.

The unproved critical-host target of at most sixteen exceptional
degree-eight vertices and the stronger `4n-4` extremal statement remain
frozen conditional refinements.

The exact live theorem changes as new reductions are proved. Its
authoritative status is maintained in the research ledger, and its full
hypotheses and trust boundary are stated in the technical frontier rather
than duplicated here.

### Partial-results manuscript status

The adjacent `K_7^-` chain has been distilled into a concise,
computation-free [paper](paper/k7minus-low-degree/main.pdf), with
[LaTeX source](paper/k7minus-low-degree/main.tex).  It has separate
mathematical and citation audits, but these are internal checks rather than
peer review or a priority certificate.  The broader
[external-review blueprint](active/hc7_partial_results_external_review_blueprint.md)
is frozen.  Neither manuscript proves the `K_7^-` six-colour conjecture or
`HC_7`.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Sole authority for current research status |
| [`active/INDEX.md`](active/INDEX.md) | Concise navigation to live proof work |
| [`K_7^-` strict-density frontier](active/hc7_k7minus_density_frontier.md) | Sole active target, minimal-enemy reductions, and exact nonclosures |
| [External-review and manuscript blueprint](active/hc7_partial_results_external_review_blueprint.md) | Frozen theorem package, review questions, reproduction plan, and restart criteria |
| [Live case verification map](active/hc7_live_case_dag.md) | Exhaustive global chain, conditional refinements, and every missing descent arrow |
| [Bounded-interface technical frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Frozen all-degree target, direct inputs, and trust boundary |
| [Degree-seven technical frontier](active/hc7_degree7_model_separator_frontier.md) | Conditional exact-seven refinement and residual cases |
| [`K_7^-` specialist-review dossier](active/hc7_k7minus_external_review_dossier.md) | Current theorem hashes, dependency map, review questions, and publication gate |
| [`K_7^-` degree-seven rigidity paper](paper/k7minus-low-degree/main.pdf) | Concise computation-free manuscript containing the low-degree structural theorem chain |
| [Critical seven-cut capacity](results/hc7_k7minus_critical_seven_cut_capacity.md) | Excludes four-component seven-cuts in the critical host and normalises the three-component boundary |
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
python3 tools/research_index.py context hc7.target.k7minus_extremal_4n_minus_2
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
