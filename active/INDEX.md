# Current proof work

**Role:** concise navigation only.  The authoritative status is
[`../RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## Closed `K_7^-` theorem

The repository now contains a written proof, with a separate internal GREEN
audit, that every seven-connected graph `G` with

\[
                         |E(G)|\ge4|V(G)|-2
\]

contains a `K_7^-` minor.  Together with the established critical-host
entrance, this proves internally that every `K_7^-`-minor-free graph is
six-colourable.  Internal audit is not external peer review.

Read:

- [exact-six-connectivity closure](../results/hc7_k7minus_exact_six_connectivity_closure.md);
- [independent internal audit](../results/hc7_k7minus_exact_six_connectivity_closure_audit.md);
- [closed density frontier](hc7_k7minus_density_frontier.md).

The dependency-free checker is
`../results/hc7_k7minus_exact_six_connectivity_verify.py`.

## Sole active target

`HC_7` remains open.  The current target is the
[labelled `K_7^-`-to-`K_7` upgrade](hc7_k7minus_to_k7_upgrade_frontier.md):
start from the now-guaranteed spanning near-clique model and repair its one
missing branch-set adjacency, or use the obstruction to obtain a compatible
exact-seven response interface, a strict labelled descent, or a global
`K_5`-minor transversal.

Selected audited inputs:

- [exact-six-connectivity closure and `K_7^-` six-colour theorem](../results/hc7_k7minus_exact_six_connectivity_closure.md)

Immediate barriers:

No individual barrier is promoted as a direct assumption of the active
target.  The target itself records the three methodological warnings that
prevent geometry-only, trace-only, or size-only closure.

## Frozen toolkits

The following remain relevant sources of proved machinery, but are not
parallel active targets:

- [bounded-interface synchronization frontier](hc7_bounded_interface_synchronization_frontier.md);
- [degree-seven model/separator frontier](hc7_degree7_model_separator_frontier.md);
- [historical live case map](hc7_live_case_dag.md).

The E5, strict-surplus separator-shore, exceptional-count, reserve, and
safe-atom programmes are preserved for provenance.  They are no longer
needed for the closed `K_7^-` theorem.

## Review gate

The immediate repository task is external specialist review and manuscript
preparation for the exact-six-connectivity proof.  New local case analysis
should address the active missing-edge upgrade rather than reopen the closed
density programme.
