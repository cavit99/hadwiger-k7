# Independent audit wrapper: branch models and the double cone

**Verdict: GREEN.**  At the exact revision below, the double-cone theorem,
the two-near-full-bridge lemma, the minimal-counterexample exact-cut normal
form, and the carefully limited separator-trace lemma are valid in the scope
stated in the source.

**Audited source:**
[`hc7_k44_branch_model_and_double_cone.md`](hc7_k44_branch_model_and_double_cone.md)

**Source SHA-256:**
`9385a53db73abc8c7a35a78bbe243bfc6fa18fba8b367ef0d0f9248e9961a87a`

This adjacent note is only a wrapper around the already completed
[independent internal cold audit](hc7_k44_closure_local_normal_forms_audit.md).
It adds no proof claim and does not enlarge that audit's scope.

## Exact scope

The inherited audit covers the following deductions.

- Two vertices universal to a five-connected graph force a `K_7^-` minor,
  whether or not the two vertices are adjacent.  Hence the boundary of an
  exact seven-cut in a seven-connected target-free graph has no
  five-connected minor.
- Two anticomplete connected sets meeting at least seven displayed
  `K_{4,4}` branch sets force the target.
- In a vertex-minimal T44 counterexample, each internal edge of every
  nontrivial displayed branch bag lies in an exact seven-cut.
- If such a cut meets at least seven model bags, at most one complementary
  component can be disjoint from the entire model.  This gives no bound on
  the number of branch bags traced by the cut.

The rooted theorem used in the double-cone proof has the independent exact
screen

```bash
cc -O3 results/rooted_k4minus_four_roots_verify.c -o /tmp/t44-root
/tmp/t44-root
```

whose expected final line is

```text
n=7 three_connected_labelled=225096 assignment_upper_bound=28137000 all_green
```

The unbounded double-cone and branch-model deductions are proved
deductively; the bounded screen does not prove them.  The Section 5 shortcut
families have separate exhaustive RED verifiers documented in
[`hc7_k44_shortcut_certificate_barriers.md`](../barriers/hc7_k44_shortcut_certificate_barriers.md);
their expected aggregate is

```text
fat_profiles=15 unexpected_status=0 max_quotient_edges=18
split_profiles=18 unexpected_status=0 max_quotient_edges=15
```

The stronger minimum-degree conclusion in Corollary 1.4 is covered by its
own [adjacent cold audit](hc7_k44_fourconnected_seven_boundary_double_cone_audit.md),
not newly audited here.

No exact cut is proved to lie inside one branch bag, to be laminar with
other cuts, or to preserve ownership of all eight model labels.  Thus no
peel/reconstruction theorem, T44, Conjecture 21, or `HC_7` follows from this
source alone.
