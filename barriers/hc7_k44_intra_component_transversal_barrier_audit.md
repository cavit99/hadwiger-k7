# Independent internal audit: component-local transversal barrier

**Verdict: GREEN at the stated profile-level scope.**  The exact abstract
incidence construction below satisfies every listed reduced local
minimum-blocker condition and has no witness to the refuted
component-local claim.  This is a separate internal audit, not external peer
review and not an ambient-host realization.

**Audited source:**
[`hc7_k44_intra_component_transversal_barrier.md`](hc7_k44_intra_component_transversal_barrier.md)

**Audited source SHA-256:**
`05301322bae9cfa8d7f12913ccea6aa3fec30f1500bffe20c684c54253bc94d8`

**Verifier SHA-256:**
`436791d1043f59d59d707bd03d89bc85b8f765db3a655202519c97c52d3efe5a`

**Pinned-output SHA-256:**
`6e08e040500e1f3c506f0e3af51beba1455b8bc183b63853c0e223188dd403de`

## 1. Independent reconstruction

An independent named-set enumerator checked all 511 nonempty subsets of
`X=K_3 join (3K_2)`.  The degree sequence is

```text
4,4,4,4,4,4,8,8,8,
```

the graph is three-connected, and its only three-cut is
`Q={t_0,t_1,t_2}`.  The minimum of
`|N_X(Y)|+|N_D(Y)|` is exactly seven.  Among proper connected sets seeing
both `a,b`, the minimum is exactly eight.  Thus all relative inequalities
and every strict smaller-blocker inequality hold.

The five `K`-resource support sizes are `3,3,2,2,2`.  The special vertex
`p=t_0` sees `a` and no `K`-resource, while `X-p` is `H`-full.  Deleting `Q`
gives exactly `W_1,W_2,W_3`; the resources `c_1,c_2` meet all three and each
`e_i` is supported exactly on `W_i`.  The boundary edge `ab` by itself is
compatible with a proper bipartition of orders three and four.

## 2. Refutation and surviving witness

For `V subseteq W_i` to see `b,c_1`, it must contain `l_i`; to see `c_2`,
it must contain `r_i`.  Thus `V=W_i`, after which `X-V` misses `e_i`.
There is no component-local transversal witness.

The full two-helper bisection remains positive.  For

```text
U={t_0,l_1,l_2},    V=X-U,    h_0=c_2,
```

both sides are connected and adjacent.  The first defect is `{e_3}` and the
second is empty.  Exhaustion finds 231 spanning two-helper witnesses.

The proposed corrected condition is valid only as a sufficient open target:
if `U` and `X-U` are connected, `U` sees `a,b` and at least three
`K`-resources, and `X-U` is `H`-full, then choosing `h_0` among at most two
missed `K`-resources leaves total defect at most one.  The audit does not
assert that every first-profile blocker has this form.

## 3. Exact scope

The construction refutes an inference from the audited reduced local data to
a purely component-local transversal.  It is not shown to occur inside a
seven-connected literal-core host.  It does not refute the full
boundary-bisection lemma, weighted splitter theorem, literal T44 branch,
T44, Conjecture 21, or `HC_7`.
