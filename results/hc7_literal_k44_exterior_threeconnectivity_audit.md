# Independent audit wrapper: literal `K_{4,4}` exterior

**Verdict: GREEN.**  At the exact revision below, the adjacent-portal
quotient classification and the deduction that a target-free literal
`K_{4,4}` exterior is three-connected are valid.

**Audited source:**
[`hc7_literal_k44_exterior_threeconnectivity.md`](hc7_literal_k44_exterior_threeconnectivity.md)

**Source SHA-256:**
`4b863b62699f62131e874d22bda0af127fb29c73de7da82da46c1f3d3e34811a`

This adjacent note is only a wrapper around the already completed
[independent internal cold audit](hc7_k44_closure_local_normal_forms_audit.md).
It records that audit beside the result and makes no fresh proof claim.

## Exact scope

The verdict covers Lemmas 2.1--2.3 and Theorem 3.1.  In particular, for a
seven-connected `K_7^-`-minor-free graph with a specified literal
`K_{4,4}` core `S`, the exterior `G-S` is connected and has no cut of order
at most two.  The final two-cut argument uses both assignments of the cut
vertices, the exact five-portal exception, and seven-connectivity across a
literal six-vertex deletion.

The independent adjacent-pair verifier is reproduced by

```bash
cc -O3 results/hc7_literal_k44_adjacent_portal_census_verify.c \
  -o /tmp/t44-adj
/tmp/t44-adj >/tmp/t44-adj-profiles.txt
```

Its expected terminal output is

```text
partitions=11880
total=26569 negative=5428
hist 4 4 4900
hist 4 5 240
hist 5 4 240
hist 5 5 48
special_five=48 crossing_edge_positive=192
```

The verifier certifies only the finite adjacent-portal Lemmas 2.2--2.3;
Lemma 2.1 and the host-level three-connectivity deduction have written
proofs.  The portal-triangle and portal-`K_4` summaries in Section 4 are
audited in their own adjacent notes.

The core-sensitive trichotomy in Section 5 remains explicitly open.
Three-connectivity alone supplies neither a portal-rich exterior model nor a
lift from an arbitrary nonliteral `K_{4,4}` model.  Consequently this result
does not prove the literal closure theorem, T44, Conjecture 21, or `HC_7`.
