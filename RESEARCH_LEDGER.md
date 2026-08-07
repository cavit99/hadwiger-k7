# Hadwiger `K_7` research ledger

**Last updated:** 7 August 2026  
**Authoritative status:** the repository now contains a written proof, with a
separate internal **GREEN** audit, of the `K_7^-` six-colour conjecture and of
the seven-connected `4n-2` extremal theorem.  Internal audit is not external
peer review.  `HC_7` itself is **not** proved.

The preceding live ledger is preserved at
[`archive/RESEARCH_LEDGER_2026-08-06_before_exact6_closure.md`](archive/RESEARCH_LEDGER_2026-08-06_before_exact6_closure.md).
This file is the sole authority for the current research status.

## 1. Headline theorem

The former sole active target is now closed by
[`results/hc7_k7minus_exact_six_connectivity_closure.md`](results/hc7_k7minus_exact_six_connectivity_closure.md):

> **Seven-connected `4n-2` theorem.** Every seven-connected graph `G` with
> \[
>                         |E(G)|\ge4|V(G)|-2
> \]
> contains a `K_7^-` minor.

The proof is computation-free except for an exhaustive six-vertex boundary
checker which independently verifies the finite arithmetic.  The theorem file
has SHA-256

```text
c17ea01e3d4f1aad159ca66a75c2b1f0ab7bc589b3473d302dba0c31d4712be0
```

and the adjacent audit is
[`results/hc7_k7minus_exact_six_connectivity_closure_audit.md`](results/hc7_k7minus_exact_six_connectivity_closure_audit.md).

## 2. Decisive mechanism

The proof bypasses the proposed global labelled-shore rank.

### Exact connectivity six

First prove the stronger intermediate theorem:

> If
> \[
>                         \kappa(H)=6,
> \qquad |E(H)|\ge4|V(H)|-2,
> \]
> then `K_7^-\preccurlyeq H`.

For a six-cut `S`, every component of `H-S` is full to `S`.  Explicit
branch-set templates show that there are only two or three components.

- With two components, `H[S]` must be `K_6-3K_2`.  Applying the sharp
  internally-four-connected rooted-`K_4` edge bound to each of the three
  complementary four-cycles forces each component excess to be at most two,
  whereas exact density requires total excess at least ten.
- With three components, `H[S]` must be cubic.  Summing the same rooted bound
  over all twelve ordered boundary nonedges forces each component excess to
  be at most three, whereas exact density requires total excess at least
  thirteen.

Both cases are impossible.

### Safe contraction closes connectivity seven

In a minimum seven-connected counterexample, the audited
[degree-seven safe-contraction theorem](results/hc7_k7minus_degree7_safe_contraction.md)
supplies an edge `vs` at a degree-seven vertex with at most three common
neighbours.  The quotient `G/vs` still meets the `4n-2` density threshold.
Every cut of order at most five in the quotient lifts to a cut of order at
most six in `G`, so the quotient is at least six-connected.

- If it remains seven-connected, it is a smaller counterexample.
- Otherwise its connectivity is exactly six, and the theorem above applies.

This contradiction proves the headline result.

## 3. Six-colour consequence

The headline theorem settles the Norin--Totschnig `K_7^-` six-colour
conjecture:

> **Corollary.** Every `K_7^-`-minor-free graph is six-colourable.

Indeed, a minor-minimal non-six-colourable graph is seven-contraction-critical
and hence seven-connected.  The audited critical-host chain proves that:

1. every degree-seven vertex lies in a literal `K_5`;
2. there is at most one literal `K_5`;
3. that clique cannot have all five vertices of degree seven.

Thus at most four vertices have degree seven and every other vertex has
degree at least eight.  Consequently

\[
                         2|E(G)|\ge8|V(G)|-4,
\]

so `|E(G)|\ge4|V(G)|-2`; the headline theorem gives the forbidden minor.

The exact audited inputs are:

- [`results/hc7_k7minus_degree7_clique_incidence.md`](results/hc7_k7minus_degree7_clique_incidence.md);
- [`results/hc7_k7minus_two_literal_k5_exclusion.md`](results/hc7_k7minus_two_literal_k5_exclusion.md);
- [`results/hc7_k7minus_all_degree7_k5_exclusion.md`](results/hc7_k7minus_all_degree7_k5_exclusion.md).

## 4. Verification

The dependency-free verifier is
[`results/hc7_k7minus_exact_six_connectivity_verify.py`](results/hc7_k7minus_exact_six_connectivity_verify.py).
It exhausts all `2^15=32768` labelled graphs on the six-vertex cut boundary.
Expected output:

```text
six_vertex_graphs=32768
four_component_survivors=0
two_component_boundaries=15
two_component_edge_counts=[12]
three_component_cubic_boundaries=70
ordered_nonedge_checks=PASS
summary_sha256=2282b0fa6a51fd9318bd67126defec4a41e27957e32cdc0381a53c571945280c
ALL CHECKS PASSED
```

The verifier checks only the finite boundary classification and incidence
coefficients.  The unbounded rooted-minor and connectivity arguments are
proved in the theorem and audited line by line in the adjacent audit.

## 5. Trust boundary

The result is internally proof-complete for the pinned revision, but it has
not undergone external expert review or publication.  In particular:

- an internal GREEN audit is not a priority claim or peer review;
- the theorem depends on the cited rooted results of
  Robertson--Seymour--Thomas and Jørgensen in the forms recorded by
  Norin--Totschnig;
- the six-colour corollary depends on Mader's seven-connectivity theorem for
  contraction-critical graphs and on the three audited critical-host files
  listed above;
- no finite computation substitutes for an unbounded step.

The exact review target is now the short proof chain in the theorem and audit,
not the historical E5 or labelled-shore laboratories.

## 6. What remains open

`HC_7` remains open:

\[
                         K_7\npreccurlyeq G
 \quad\Longrightarrow\quad \chi(G)\le6.
\]

The new theorem guarantees a `K_7^-` minor in every hypothetical
minor-minimal `HC_7` counterexample, but one missing adjacency still has to
be repaired.  The sole active target is the
[labelled `K_7^-`-to-`K_7` upgrade](active/hc7_k7minus_to_k7_upgrade_frontier.md).
The frozen bounded-interface, exact-seven, and labelled near-clique
programmes remain sources of tools for that final upgrade.  They should not
be represented as part of the now-closed `K_7^-` proof.

The immediate repository task is external mathematical review and manuscript
consolidation of the exact-six-connectivity proof.  New local case analysis
should not resume unless review finds a concrete gap or supplies a route from
the guaranteed `K_7^-` model to `K_7`.

## 7. Superseded frontiers

The prior strict-surplus labelled-separator-shore attack, E5 laboratory,
exceptional-count programme, and reserve-aggregation campaign are preserved
for provenance.  They are no longer needed for the `K_7^-` six-colour
conjecture.

The former detailed density frontier remains available in the immutable
pre-closure revision
[`93079280`](https://github.com/cavit99/hadwiger-k7/blob/93079280ceedd5754105446e27bb76985ad8ffc0/active/hc7_k7minus_density_frontier.md).
The former curated claim manifest is preserved verbatim at
[`archive/research_manifest_2026-08-06_before_exact6_closure.toml`](archive/research_manifest_2026-08-06_before_exact6_closure.toml).
