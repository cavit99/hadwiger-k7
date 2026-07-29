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

The project works from a hypothetical minor-minimal counterexample. Such a
graph is seven-connected, is seven-chromatic, has no $K_7$ minor, and every
proper minor is six-colourable.

The main internally audited reductions currently establish that:

- every hypothetical counterexample has a vertex `u` of degree seven,
  eight, or nine and an actual separation of order between seven and
  `d(u)`, with each open side containing a connected subgraph adjacent to
  every boundary vertex; at the same `u`, every component outside `N[u]`
  has its own boundary vertex `z_D` with `chi(G-{u,z_D})=6`, and the numbers
  of such exterior components are at most one, two and three in degrees
  seven, eight and nine, respectively;
- whenever at least two exterior components occur, their private colouring
  obstructions lie in one connected Kempe reconfiguration space and all
  component-supported nonedges can be retained simultaneously in a
  `K_6`-minor-free neighbourhood augmentation; in the full unique-rejector
  case exactly two components remain and their failed lifts share one root;
- in the degree-seven case the exterior of the closed neighbourhood is
  connected, and its boundary-colouring constraints admit an exact
  matching description;
- those constraints produce five-rooted minor models and a boundary-labelled
  model of $K_7$ with either one missing edge or two adjacent missing edges;
- several unbounded boundary families, including split boundaries and the
  induced-cycle completion family, are closed by explicit minor-model or
  planarity arguments; and
- failed branch-set reroutings and colouring transfers can often be converted
  into actual full-neighbourhood separations or smaller list-critical
  subgraphs.

Separately, a computation-free, internally audited route toward the adjacent
`K_7^-` problem, where `K_7^-` is `K_7` with one edge deleted, proves that
every minor-minimal non-six-colourable `K_7^-`-minor-free graph has at least
`4n-4` edges and at most eight degree-seven vertices.  At equality it gives
the exact degree sequence and two-clique structure.  It also gives exact
degree-seven neighbourhoods and proves that outside every order-seven cut
there are at most four disjoint connected subgraphs each adjacent to every
boundary vertex, with exact whole-component contraction criteria.  In the
minor-minimal non-six-colourable host, exact boundary-colouring reflection
improves that bound to three and excludes four-component seven-cuts.  A
three-component cut has a three-chromatic boundary, and every proper
three-colouring has class sizes `3,2,2`.  These are structural theorems about
a hypothetical critical graph and about seven-connected
`K_7^-`-minor-free graphs; they are not the bare extremal `4n-4` theorem, the
`K_7^-` six-colour conjecture, or `HC_7`.

On the primary `HC_7` route, the remaining work is to synchronize branch-set
labels and boundary colourings: proper-minor colouring responses must yield
an explicit $K_7$-minor model, a common complete boundary partition on the
order-seven, -eight, or -nine separation, or a genuine same-host descent.
On the adjacent `K_7^-` route, the separate remaining target is the bare
`4n-4` extremal theorem, equivalently the full seven-cut dichotomy described
in the technical frontier.  The new contraction criteria do not force that
dichotomy by themselves.

The exact live theorem changes as new reductions are proved. Its
authoritative status is maintained in the research ledger, and its full
hypotheses and trust boundary are stated in the technical frontier rather
than duplicated here.

### Partial-results manuscript status

The internally audited corpus now supports a credible specialist
partial-results manuscript candidate about the structure of a hypothetical
minor-minimal counterexample.  A coherent core consists of the bounded full
separations of order seven to nine, component-uniform colouring responses,
the proved one/two/three exterior-component upper bounds, exact order-seven
packing restrictions for connected subgraphs adjacent to the whole boundary,
and the multi-component colouring-response theorem.  The boundary-labelled
degree-seven result is a possible secondary application, subject to a careful
overlap review against the public unlabelled near-clique theorem.

The adjacent `K_7^-` chain is a second, narrower manuscript candidate with no
load-bearing finite classification.  Its current specialist-review dossier
records the exact theorem revisions and the limits of the `4n-4` conclusion.

This is not a proof of $HC_7$, evidence that completion is near, or a
confirmed novelty claim.  In particular, Norin and Totschnig already prove
the global unlabelled result that every non-six-colourable graph contains a
minor isomorphic to
[$K_7^\vee$](https://arxiv.org/abs/2507.03244), obtained from $K_7$ by
deleting two adjacent edges.  The repository's possible contribution is the
bounded-interface localization, component-uniform responses, component
bounds, packing restrictions, and retained boundary labels.  Submission
should wait for a conventional literature and priority review, independent
human audits by graph-minor and colouring specialists, and independent
reproduction of the load-bearing finite classifications.  See the
[external-review and manuscript blueprint](active/hc7_partial_results_external_review_blueprint.md)
and the
[verification-gate assessment](active/hc7_verification_gate_report.md#partial-results-paper-blueprint-only-until-the-external-review-gates-pass).
Intensive autonomous proof search on the primary `HC_7` programme is paused
pending the external review gate described there; the adjacent `K_7^-`
density programme remains live.  Both open targets remain mathematically
current.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Sole authority for current research status |
| [`active/INDEX.md`](active/INDEX.md) | Concise navigation to live proof work |
| [External-review and manuscript blueprint](active/hc7_partial_results_external_review_blueprint.md) | Frozen theorem package, review questions, reproduction plan, and restart criteria |
| [Live case verification map](active/hc7_live_case_dag.md) | Exhaustive global chain, conditional refinements, and every missing descent arrow |
| [Bounded-interface technical frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Primary all-degree theorem, direct inputs, and trust boundary |
| [Degree-seven technical frontier](active/hc7_degree7_model_separator_frontier.md) | Conditional exact-seven refinement and residual cases |
| [`K_7^-` strict-density frontier](active/hc7_k7minus_density_frontier.md) | Live adjacent route, exact proved entrance, and positive finishing targets |
| [`K_7^-` specialist-review dossier](active/hc7_k7minus_external_review_dossier.md) | Current theorem hashes, dependency map, review questions, and publication gate |
| [Critical seven-cut capacity](results/hc7_k7minus_critical_seven_cut_capacity.md) | Excludes four-component seven-cuts in the critical host and normalizes the three-component boundary |
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
python3 tools/research_index.py context hc7.target.bounded_interface_bridge
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
