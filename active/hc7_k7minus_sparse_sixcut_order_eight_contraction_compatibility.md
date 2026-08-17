# Contraction compatibility in the sixteen order-eight Hall profiles

**Status:** proved analytic reduction; independently cold-audited.  This
is not an order-eight completion theorem.  It reduces every internal
branch-bag edge to a high-codegree edge or a coefficient-neutral exact
six-fragment, and gives a sharper four-row table for the deficient
two-vertex bag.

## 1. Setup

Use the hypotheses and notation of the audited order-eight Hall-profile
theorem.  Thus `S` is stable of order six, `C` is a connected `S`-full shore
of order eight satisfying relative six-connectivity, and

```text
eta_S(C)>=6.
```

Fix a spanning ordinary `K_5^-` model in `C` and suppose the closed shore has
no punctured `S`-rooted `K_5^-` model.  For an internal edge `uv` of one of
the five branch bags, put

```text
lambda(uv)=|N_C(u) intersect N_C(v)|
           +|N_S(u) intersect N_S(v)|.              (1)
```

## 2. The exact contraction fork

### Theorem 2.1

For every branch-bag edge `uv`, at least one of the following holds.

1. There is a nonempty connected set

   ```text
   X subseteq C-{u,v}
   ```

   with exact boundary

   ```text
   |N_C(X)|+|N_S(X)|=6,       u,v in N_C(X).        (2)
   ```

2. The edge has the codegree lower bound

   ```text
   lambda(uv)>=eta_S(C)-2.                          (3)
   ```

### Proof

Contract `uv` inside its branch bag.  The ordinary `K_5^-` model survives,
and every punctured rooted model after contraction lifts by replacing the
contracted vertex with the connected pair `{u,v}`.

If relative six-connectivity fails after contraction, the audited exact
contraction gate gives precisely a connected set `X` satisfying (2).
Suppose it does not fail.  The contracted shore has order seven, remains
connected and `S`-full, and satisfies every hypothesis of the audited
order-seven ordinary-minor theorem except possibly its excess threshold.
The contraction formula is

```text
eta_S(C/uv)=eta_S(C)+3-lambda(uv).                  (4)
```

If the right side were at least six, the order-seven theorem would return a
punctured rooted model, and the lift would contradict the hypothesis on the
original shore.  Hence `eta_S(C/uv)<=5`.  Rearranging (4) gives (3).
`\square`

The two outcomes are not asserted to be exclusive: a high-codegree edge may
also be blocked by an exact fragment.

## 3. The deficient two-vertex bag

In a one-edge-bag Hall profile, let `{u,v}` be the unique two-vertex bag in
the minimal deficient family `I`, and let `i=|I|`.  The Hall theorem gives

```text
N_S(U)=R,                 |R|=i-1.                  (5)
```

In particular both `u` and `v` have all their root neighbours in `R`, so

```text
|N_S(u) intersect N_S(v)|<=i-1.                    (6)
```

### Corollary 3.1

If the deficient-bag edge `uv` is not blocked by a set in (2), then

```text
|N_C(u) intersect N_C(v)|>=eta_S(C)-i-1.           (7)
```

At the threshold `eta_S(C)>=6`, the four profiles therefore require

| `i` | common neighbours of `u,v` in `C` |
|---:|---:|
| 1 | at least 4 |
| 2 | at least 3 |
| 3 | at least 2 |
| 4 | at least 1 |

Moreover, `C-{u,v}` has only six vertices.  Consequently the deficient edge
must be blocked by an exact fragment whenever

```text
eta_S(C)>=i+8;                                     (8)
```

that is, at excess at least `9,10,11,12` for `i=1,2,3,4`, respectively.

### Proof

Subtract (6) from Theorem 2.1(3) to obtain (7).  Substitution of excess six
gives the table.  The left side of (7) is at most six, so (7) is impossible
when `eta_S(C)-i-1>=7`, which is exactly (8).  `\square`

## 4. Exact scope and next obligation

The theorem applies to every internal edge of every nonsingleton branch bag
in all sixteen Hall profiles.  The sharper table applies only when the
nonsingleton bag itself belongs to the deficient family.  Neither outcome
alone constructs a rooted model: high codegree does not specify a compatible
five-bag allocation, while an exact fragment still requires the packet and
portal descent.

The packet-number-one hypothesis is not used.  Thus the order-eight status
remains open.  The next compatibility step is finite at low excess: combine
the table in Corollary 3.1 with the six-vertex minor-free deletion supplied
by the Hall profile.  At higher excess, (8) routes the deficient edge directly
into the exact-six fragment programme.

## Pinned dependencies

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
