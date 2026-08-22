# Independent audit wrapper: four-root `K_4^-`

**Verdict: GREEN.**  At the exact revision below, every three-connected
finite simple graph has a `K_4^-` minor rooted at any four prescribed
distinct vertices, with the missing quotient edge not prescribed.

**Audited source:**
[`rooted_k4minus_four_roots.md`](rooted_k4minus_four_roots.md)

**Source SHA-256:**
`c848504c758371545c27e60f577c06d096f5fd61714bfcab37f4cd80402af598`

This adjacent note is only a wrapper around the already completed
[independent internal cold audit](hc7_k44_closure_local_normal_forms_audit.md).
It records that audit beside the promoted theorem; it is not a fresh audit or
a new proof claim.

## Exact scope

The GREEN verdict covers the unbounded written proof of the rooted
`K_4^-` theorem.  The finite computation below is an independent
falsification screen through order seven, not the basis for extrapolating the
theorem to arbitrary order.

From the repository root, run

```bash
cc -O3 results/rooted_k4minus_four_roots_verify.c -o /tmp/t44-root
/tmp/t44-root
```

The expected output is

```text
n=4 three_connected_labelled=1 assignment_upper_bound=1 all_green
n=5 three_connected_labelled=26 assignment_upper_bound=130 all_green
n=6 three_connected_labelled=1768 assignment_upper_bound=44200 all_green
n=7 three_connected_labelled=225096 assignment_upper_bound=28137000 all_green
```

The theorem does not prescribe which quotient edge may be absent, make the
four bags span the graph, or control their contacts with a literal
`K_{4,4}` core.  It therefore does not prove the open literal-core capstone,
T44, Conjecture 21, or `HC_7`.
