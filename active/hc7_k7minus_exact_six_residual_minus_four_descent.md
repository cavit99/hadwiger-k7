# The exceptional two-root return loses four units of excess

**Status:** proved unbounded descent; independently cold-audited.  The
exceptional two-packet-to-one-packet return has portal charge at most `-4`,
not merely nonpositive.  Consequently a coefficient-five counterexample of
excess at least seven descends to a smaller counterexample.  The only
non-descending row has exact excess data `(10,-4,6)`.

Write `K_7^-` for `K_7` with one edge deleted.  Use the hypotheses and
notation of the audited residual portal-collapse theorem.  Thus `G` is
six-connected and has no `K_7^-` minor, `S` is a six-cut with at least three
connected `S`-full components, and `C` is one of them.  An exact derived
six-cut exchanges two roots:

```text
Z=S intersect T={z_1,z_2,z_3,z_4},
R=T-S={r_1,r_2},
Q=S-T={q_1,q_2}.
```

The remote component `L` contains two disjoint `T`-packets, whilst the
exceptional transfer data are

```text
mu_T(L)=2,        mu_S(C-L)=0,        mu_S(C)=1.     (1)
```

The portal-collapse theorem gives

```text
C-L=R                                                (2)
```

and, after relabelling, the literal matching edges `r_1q_1,r_2q_2`.
At most one of the crossed edges `r_1q_2,r_2q_1` occurs.

## 1. The two-template quotient lemma

Put

```text
e=1 if r_1r_2 is an edge, and 0 otherwise,
c=the number of crossed R--Q edges,
z=|E_G(R,Z)|.                                       (3)
```

Thus `e,c in {0,1}`.

### Lemma 1

```text
e+c+z<=2.                                           (4)
```

### Proof

Suppose instead that `e+c+z>=3`.  Contract each of the two `T`-packets to
vertices `p_1,p_2`, and contract two other `S`-full components to vertices
`a,d`.  Delete every edge not forced below.  Each `p_i` is adjacent to all
of `Z union R`; each of `a,d` is adjacent to all of `S`; and the two matching
edges from `R` to `Q` remain.  It is enough to find a `K_7^-` model in this
quotient.

First suppose `e+c>=1`.  Since `e+c<=2`, the contrary assumption gives
`z>=1`; hence there is an edge `r_i z_0` for some `z_0 in Z`.  Write
`Z-{z_0}={z_1,z_2,z_3}`.  The seven bags

```text
{p_1},            {p_2,z_1},
{a,z_2},          {d,z_3},
{z_0},            {q_1,r_1},        {q_2,r_2}       (5)
```

are connected and pairwise disjoint.  The first four bags contact every
other bag.  The last two portal bags contact because either `r_1r_2` or a
crossed `R`--`Q` edge is present, and `{z_0}` contacts the portal bag
containing `r_i`.  Hence at most the other pair among the final three bags
fails to contact, so (5) is a `K_7^-` model.

Now suppose `e+c=0`.  Then `z>=3`, so one portal, say `r_1`, has two
distinct neighbours `z_1,z_2 in Z`.  Write the other roots as `z_3,z_4`.
The bags

```text
{p_1,r_2},        {p_2,z_3},
{a,q_2},          {d,z_4},
{z_1},            {z_2},             {q_1,r_1}      (6)
```

are connected and pairwise disjoint.  Again the first four are universal:
in particular, `{p_1,r_2}` contacts `{a,q_2}` through the matching edge
`r_2q_2`.  The final portal bag contacts both singleton roots through
`r_1z_1,r_1z_2`.  Thus only the pair `{z_1}{z_2}` may be absent, and (6) is
a `K_7^-` model.  Both cases contradict the hypothesis on `G`, proving
(4).  \(\square\)

The proof is insensitive to additional quotient edges; it uses no finite
bound on `|L|`.

## 2. Exact charge and descent

### Theorem 2 (minus-four portal charge)

```text
eta_S(C-L)=eta_S(R)<=-4,                             (7)
eta_S(C)<=eta_T(L)-4.                               (8)
```

### Proof

There are exactly two forced matching incidences from `R` to `Q`, in
addition to the `c` crossed incidences and the `z` incidences to `Z`.
Using (2)--(4),

```text
eta_S(R)
 =e+|E_G(R,S)|-4|R|
 =e+(2+c+z)-8
 =e+c+z-6
 <=-4.
```

Exact fragment additivity gives

```text
eta_S(C)=eta_T(L)+eta_S(C-L),
```

and (2) and (7) give (8).  \(\square\)

### Corollary 3 (the exact weighted-induction residue)

Consider the fragment-closed local assertion

```text
eta_U(X)<=5 mu_U(X)                                 (9)
```

under relative six-connectivity and punctured five-rooted-`K_5^-`
exclusion.  Let `(C,S)` be a minimum-order counterexample, and suppose an
exact two-root return is in the exceptional row (1).  Then

```text
eta_S(C)=6,
eta_T(L)=10,
eta_S(C-L)=-4,
e+c+z=2.                                            (10)
```

In particular, a residual counterexample with `eta_S(C)>=7` descends to the
strictly smaller counterexample `(L,T)`.

### Proof

Hereditary rerooting excludes the punctured rooted model in `(L,T)`, and
the exact fragment is relatively six-connected.  Since `mu_T(L)=2`,
minimality gives

```text
eta_T(L)<=10.                                       (11)
```

The counterexample has `mu_S(C)=1`, hence integer excess at least six.
Theorem 2 and (11) give

```text
6<=eta_S(C)<=eta_T(L)-4<=6.
```

Equality holds throughout, yielding the first three identities in (10).
The charge formula in the proof of Theorem 2 then gives `e+c+z=2`.

Without invoking minimality, if `eta_S(C)>=7`, Theorem 2 gives
`eta_T(L)>=11>5 mu_T(L)`.  Thus `(L,T)` is itself a smaller counterexample,
which proves the last assertion.  \(\square\)

## 3. Consequence for the ordinary-minor route

The audited branch-bag contraction gate returns proper exact six-fragments.
Whenever such a fragment has the two-root exchange and enters the residual
row (1), Theorem 2 removes every positive return charge, and Corollary 3
shows that the two-copy packing loss costs only one unresolved unit: the sole
non-descending numerical row is `(10,-4,6)`.

There remains one genuine heredity issue.  An ordinary `K_5^-` minor in `C`
need not lie in `L`.  Hence minimum-order induction restricted to the
ordinary-minor branch cannot use the last paragraph of Corollary 3 when the
smaller counterexample is ordinary-minor-free.  A fragment-closed proof of
(9), or a sharp theorem for the ordinary-minor-free fragment, is still
needed.  This is now a precise class-transfer obstruction rather than an
uncontrolled packet linkage or an uncontrolled main-side excess.

The order-seven ordinary-minor theorem supplies the first base order, but it
does not eliminate the equality row (10) at arbitrary order.  This result is
therefore an unbounded structural advance, not a proof of Conjecture 21 or
`HC_7`, and remains below the Norin--Totschnig benchmark.

## Reproducible adversarial check

The computation-free proof above is accompanied by

```text
active/experiments/exact_six_residual_portal_minus_four/verify.py
```

Its SHA-256 is
`a3246b99e012beb808d0006b8801af5d876913fcc5a600a5be2f0f0d138599cd`.
The standard-library verifier enumerates all `1,536` labelled portal
profiles with at most one crossed edge and checks all `1,470` profiles at
or above the theorem's three-optional-edge threshold.  It recovers `156`
minimal profiles in twelve symmetry orbits and verifies explicit seven-bag
certificates in every orbit.  It also checks the seven two-edge orbits as a
guardrail for the equality boundary.  The proof does not depend on this
finite check.

## Pinned dependencies

```text
9e1742e20e89f1df3cdb02f944873cc48dbc61bb6830e8e1a8be16b50b214eb1
  active/hc7_k7minus_exact_six_residual_portal_collapse.md
3df2585010cd685c346a1149b36bf89fe9ec95c1dfab0b0a7222e54dd765dd1d
  active/hc7_k7minus_exact_six_residual_portal_collapse_cold_audit.md
53c91cee74ae8b1f5251e13c14095f8abc65f05625eedb401d3d53173996da15
  active/hc7_k7minus_six_boundary_fragment_rerooting.md
c30aa69b6919edd2cfba80d6df1f02e2c75d38d9544bd87e4332ba4d823526a3
  active/hc7_k7minus_six_boundary_fragment_rerooting_cold_audit.md
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md
23db844015f8f38619e164453b1049b9c16468fe6677d3337d5b5bf63d33a0d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate_cold_audit.md
6005366ee90407ec9207fc3d07cc52dd84b28b9cfec254d2f583ed5c1e818a20
  active/hc7_k7minus_sparse_sixcut_order_seven_ordinary_minor_completion.md
1dc4f8019a42fa4fa75ca69857000ecccb1af1be1dec2a008f5d4a26882bd907
  active/hc7_k7minus_sparse_sixcut_order_seven_ordinary_minor_completion_cold_audit.md
```
