# Cold audit: order-eight contraction compatibility

**Verdict:** **GREEN** at the exact source revision below.  This is an
independent internal audit, not external peer review.

## Pinned source and dependencies

```text
34365fec6f9bb1fd77596255b2443239e63af3d5a60af74cfc0985d641f08f62
  active/hc7_k7minus_sparse_sixcut_order_eight_contraction_compatibility.md
```

Relative to the audited source
`e2478dded0e291e82600dcb6de5d19c6f4f61524369c51153eaed7d008990360`,
the final source changes only its status from audit-pending to independently
cold-audited.  The theorem, proof and scope are unchanged.

The pinned dependencies, all of which match the files checked, are:

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md
23db844015f8f38619e164453b1049b9c16468fe6677d3337d5b5bf63d33a0d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate_cold_audit.md
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3
  active/hc7_k7minus_six_boundary_fragment_rerooting_cold_audit.md
6005366ee90407ec9207fc3d07cc52dd84b28b9cfec254d2f583ed5c1e818a20
  active/hc7_k7minus_sparse_sixcut_order_seven_ordinary_minor_completion.md
1dc4f8019a42fa4fa75ca69857000ecccb1af1be1dec2a008f5d4a26882bd907
  active/hc7_k7minus_sparse_sixcut_order_seven_ordinary_minor_completion_cold_audit.md
92f868fc8547fbba58037587ad3c65e2894905011d0c2c71ea9d8e0de6bc1ba5
  active/hc7_k7minus_sparse_sixcut_order_eight_hall_profile.md
9428c5d22c9ff5a433949865aa1946f62f0d2823894a966f6b3159741847ab05
  active/hc7_k7minus_sparse_sixcut_order_eight_hall_profile_cold_audit.md
```

## 1. Exact contraction fork

Contracting an edge `uv` within one ordinary branch bag preserves that
ordinary `K_5^-` model.  A rooted model in the contracted shore lifts by
replacing the contracted vertex, when used, by the connected edge `uv`.
Thus punctured-rooted-model exclusion is inherited by the contraction.

After simplifying parallel edges, the contraction removes the edge `uv`,
one internal edge for every common neighbour in `C`, and one boundary
incidence for every common neighbour in `S`; it removes one shore vertex.
Consequently

```text
eta_S(C/uv)-eta_S(C)
  =-1-lambda(uv)+4
  =3-lambda(uv),
```

which verifies the displayed contraction formula.

If relative six-connectivity fails, the pinned contraction gate gives a
nonempty connected `X subseteq C-{u,v}` whose old boundary has order six
and contains both `u,v`.  Since the internal and root boundary parts are
disjoint, this is exactly

```text
|N_C(X)|+|N_S(X)|=6,       u,v in N_C(X).
```

If connectivity survives, the contracted shore has order seven, is still
connected and `S`-full, retains the ordinary minor, and satisfies the same
stable-boundary and relative-connectivity hypotheses.  Were its excess at
least six, the pinned complete order-seven theorem would give a punctured
rooted model, which would lift.  Hence its excess is at most five, and the
contraction identity gives

```text
lambda(uv)>=eta_S(C)-2.
```

This proves the exhaustive, nonexclusive fork for every internal edge of
every branch bag.

## 2. The deficient two-vertex bag

In a one-edge-bag Hall profile, the unique two-vertex bag in the minimal
deficient family is connected, so its vertices `u,v` are joined by the
edge to which Theorem 2.1 applies.  The Hall profile gives

```text
N_S(U)=R,                 |R|=i-1.
```

Every root neighbour of either `u` or `v` lies in `R`; therefore their
common root-neighbour set has order at most `i-1`.  In the nonfragment
outcome, subtracting this bound from the total-codegree inequality yields

```text
|N_C(u) intersect N_C(v)|
  >= eta_S(C)-2-(i-1)
  = eta_S(C)-i-1.
```

At excess six this gives, for `i=1,2,3,4`, the exact lower bounds
`4,3,2,1` stated in the table.  No individual root-neighbour information
beyond the collective Hall neighbourhood is assumed.

There are six possible common internal neighbours outside `{u,v}`.  Thus
the displayed lower bound becomes impossible once

```text
eta_S(C)-i-1>=7,
```

equivalently `eta_S(C)>=i+8`.  The thresholds `9,10,11,12` follow in the
four rows, and the exact-fragment outcome is then forced.

## 3. Hypotheses and scope

The stable six-root set, order-eight shore, relative six-connectivity,
spanning ordinary model, rooted-model exclusion and excess threshold are
all used with their stated quantifiers.  The general contraction fork does
not require Hall deficiency; the sharper codegree table requires that the
two-vertex bag itself belong to the chosen minimal deficient family.

The theorem neither produces a compatible rooted allocation from high
codegree nor eliminates the returned exact fragment.  It does not use or
infer packet number one, and it does not complete any of the sixteen
order-eight profiles.  Its stated next steps and nonterminal scope are
therefore accurate.  No defect was found.
