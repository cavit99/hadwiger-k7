# Independent computational audit: finite \(K_7^-\) layer

**Status:** archived external computational-reproducibility dossier.  
This is **not** part of the live proof spine and does **not** advance the mathematical frontier.

## Scope

Independent reproduction and encoding audit of the eight principal finite
\(K_7^-\) verifiers at commit

```text
f4705983bd5de40661236943f80be80a5a2c961a
```

Covered: exceptional-neighbourhood enumeration; one-nonfull 28-type census;
overlap-trace common-six census; both-full \(2076\to15\to7\); distinct-miss
fan-tree completion (principal and independent checkers); two scoped
barrier verifiers; assertion hardening under `python3 -O`.

Explicitly **out of scope:** written host reductions and lifts; external
theorem applications; exceptional-centre connectivity; Conjecture 21 /
\(HC_7\); the frozen 129-boundary / defect-two reflection computation; the
older degree-eight exterior-component bound.

## Files

| File | Role |
|---|---|
| [`AUDIT_REPORT.md`](AUDIT_REPORT.md) | Full auditor report (environment, run table, encoding review, trust boundary, verdicts) |
| [`cross_check.py`](cross_check.py) | Independent scratch cross-check suite (stdlib + `geng`; not imported by project verifiers) |
| [`cross_check.stdout`](cross_check.stdout) | Captured successful run of `cross_check.py` |
| [`independent_cross_check_report.txt`](independent_cross_check_report.txt) | Line log from the independent suite |
| [`ENVIRONMENT_AND_HASHES.txt`](ENVIRONMENT_AND_HASHES.txt) | Host environment and artifact SHA-256 anchors |

## Artifact hashes (as archived)

```text
7d58b8b6130b708901597f10d1252209773091308e47f10be2a55dd0b13695f6  AUDIT_REPORT.md
800b9c76f36c3f9e106c7339204220c9653c20ef6e9674c66bbff02cc6ddf275  cross_check.py
```

## How to re-run the independent checker

From a checkout with nauty’s `geng` on `PATH`:

```bash
python3 archive/k7minus_finite_computational_audit_f4705983/cross_check.py
```

Expected terminal outcome: `ALL INDEPENDENT CROSS-CHECKS PASSED` (exit 0).

## Applicability to later `main`

At preservation, none of the eight audited verifier programs differed
between `f4705983` and `main` tip `5948401`. Reconfirm with

```bash
git diff f4705983..HEAD -- \
  results/hc7_k7minus_exceptional_neighbourhood_completion_verify.py \
  results/hc7_k7minus_nonfull_attachment_reduction_verify.py \
  barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier_verify.py \
  results/hc7_k7minus_overlap_trace_synchronization_verify.py \
  results/hc7_k7minus_distinct_miss_fan_tree_completion_verify.py \
  results/hc7_k7minus_distinct_miss_fan_tree_completion_independent_verify.py \
  results/hc7_k7minus_both_full_shore_reduction_verify.py \
  barriers/hc7_k7minus_shore_allocation_barrier_verify.py
```

before citing this dossier against a newer tip.

## Verdict summary

- Computational credibility of the audited finite layer: **materially improved**.
- Publication readiness of the computational appendix: **materially improved**.
- Mathematical frontier / conjecture status: **unchanged**.

A clean finite reproduction does not prove the unbounded theorem.
