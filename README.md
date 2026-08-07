# Hadwiger's Conjecture for `K_7`-minor-free graphs

> **Research status:** this repository now contains a written, internally
> audited proof that every `K_7^-`-minor-free graph is six-colourable.
> `HC_7` is not proved and remains open.  Internal audits are not external peer review.

This repository is an open research workspace on the first unresolved case
of Hadwiger's Conjecture.  It contains written theorems, conjectural proof
targets, computer-assisted finite results, internal audits, and explicit
counterexamples to intermediate claims.

Here `K_7^-` means `K_7` with one edge deleted.  The notation `HC_7` in
historical filenames refers to the excluded clique `K_7`; in Seymour's
indexing convention this is `HC(6)`.

## The two statements

Hadwiger's Conjecture at `t=7` is

\[
                         K_7\npreccurlyeq G
 \quad\Longrightarrow\quad \chi(G)\le6.
\]

That remains unproved.

The adjacent near-clique statement is now proved in the repository:

\[
                         K_7^-\npreccurlyeq G
 \quad\Longrightarrow\quad \chi(G)\le6.
\]

The key extremal theorem is stronger and purely structural:

\[
 \boxed{
 \kappa(G)\ge7,
 \qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G.}
\]

## Decisive proof

The proof is in
[`results/hc7_k7minus_exact_six_connectivity_closure.md`](results/hc7_k7minus_exact_six_connectivity_closure.md),
with an adjacent hostile internal audit in
[`results/hc7_k7minus_exact_six_connectivity_closure_audit.md`](results/hc7_k7minus_exact_six_connectivity_closure_audit.md).

Its central intermediate theorem is:

> Every graph `H` with
> \[
>                         \kappa(H)=6,
> \qquad |E(H)|\ge4|V(H)|-2
> \]
> contains a `K_7^-` minor.

For a six-cut, every complementary component is full to the boundary.
Explicit branch-set templates leave only two or three components.

- In the two-component case, the boundary is forced to be `K_6-3K_2`.
  Three sharp rooted-`K_4` inequalities make the available component excess
  far too small for the global density.
- In the three-component case, the boundary is forced to be cubic.  Summing
  the same rooted inequality over its twelve ordered nonedges gives the same
  contradiction.

A minimum seven-connected enemy has a degree-seven vertex with a
coefficient-four density-safe incident contraction.  The quotient remains at
least six-connected.  If it is seven-connected it is a smaller enemy; if its
connectivity is exactly six, the theorem above applies.

The six-colour consequence then uses the audited critical-host facts that all
degree-seven vertices lie in the unique possible literal `K_5`, while that
clique cannot contain five degree-seven vertices.  Hence a hypothetical
minor-minimal non-six-colourable target-free graph has at least `4n-2` edges
and is covered by the extremal theorem.

## Verification and trust boundary

The dependency-free verifier
[`results/hc7_k7minus_exact_six_connectivity_verify.py`](results/hc7_k7minus_exact_six_connectivity_verify.py)
exhausts all `2^15` labelled graphs on the six-vertex boundary and checks the
finite classification and incidence coefficients:

```bash
python3 results/hc7_k7minus_exact_six_connectivity_verify.py
```

Expected final line:

```text
ALL CHECKS PASSED
```

The finite verifier does not establish the unbounded theorem.  The rooted
minor and connectivity arguments are written out in the theorem and checked
line by line in the audit.

The current claims have not yet been externally peer reviewed or published.
No novelty or priority claim should be inferred from repository timestamps or
internal GREEN labels.

## What remains

A hypothetical minor-minimal `HC_7` counterexample now has a guaranteed
`K_7^-` minor.  The remaining problem is to repair the model's single missing
adjacency—or use its labelled branch-set structure and proper-minor colouring
responses to derive a contradiction.

The historical bounded-interface, exact-seven, degree-seven, and labelled
near-clique programmes remain available as toolkits for that upgrade.  The
former E5 and strict-surplus density laboratories are preserved for
provenance but are no longer required for the `K_7^-` theorem.

## Start here

| Document | Purpose |
|---|---|
| [`RESEARCH_LEDGER.md`](RESEARCH_LEDGER.md) | Sole authority for current status and trust boundary |
| [`active/INDEX.md`](active/INDEX.md) | Concise navigation to current work |
| [Exact-six-connectivity theorem](results/hc7_k7minus_exact_six_connectivity_closure.md) | Proof of the `4n-2` extremal theorem and six-colour corollary |
| [Adjacent internal audit](results/hc7_k7minus_exact_six_connectivity_closure_audit.md) | Pinned hostile verification of every proof step |
| [Finite boundary verifier](results/hc7_k7minus_exact_six_connectivity_verify.py) | Deterministic check of the six-vertex arithmetic |
| [Closed density frontier](active/hc7_k7minus_density_frontier.md) | Short record of the completed proof spine |
| [Bounded-interface frontier](active/hc7_bounded_interface_synchronization_frontier.md) | Frozen toolkit for the remaining `K_7^-` to `K_7` upgrade |
| [Degree-seven frontier](active/hc7_degree7_model_separator_frontier.md) | Labelled exact-seven and model/separator tools |
| [Research integrity tools](tools/README.md) | Search, audit hashes, dependency metadata, and CI checks |

Read a theorem in [`results/`](results/) together with its adjacent
`_audit.md` file.  Refuted intermediate principles are retained in
[`barriers/`](barriers/), and superseded work in [`archive/`](archive/).

## Claim labels

- **Written proof:** explicit hypotheses, statement, and proof.
- **Separate internal audit:** an independent hostile check of a pinned
  revision; not external peer review.
- **Computer-assisted finite result:** an exact finite reduction with
  retained code and reproducible output.
- **Conjectural target:** an unproved next theorem.
- **Barrier:** a counterexample to an intermediate claim, not to Hadwiger's
  Conjecture.

## Repository layout

```text
.
├── README.md            # public overview
├── RESEARCH_LEDGER.md   # authoritative current status
├── AGENTS.md            # workflow and proof-integrity rules
├── tools/               # research index and integrity checks
├── results/             # written claims and adjacent audits
├── active/              # current frontiers and live scripts
├── barriers/            # counterexamples to intermediate claims
└── archive/             # superseded work retained for provenance
```

See [`AGENTS.md`](AGENTS.md) before contributing.

## Licence

Repository materials are available under the [MIT License](LICENSE).  The
licence permits reuse; it does not certify the mathematical claims.
