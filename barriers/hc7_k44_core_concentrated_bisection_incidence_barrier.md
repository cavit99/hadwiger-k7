# A local incidence barrier to the core-concentrated bisection

**Status.** Explicit finite counterexample to the local incidence implication
stated below, with an adjacent deterministic verifier.  This is not asserted
to occur in a seven-connected graph and is not a counterexample to the
literal `K_{4,4}` case, T44, or Conjecture 21.

## Refuted implication

Let

```text
E={a,p} dotunion T,                 T={t0,t1,t2,t3,t4},
```

and let `R` be a connected graph carrying neighbourhoods in `E`.  For
`Y subseteq R`, put

```text
lambda(Y)=|N_R(Y)|+|N_E(Y)|.
```

The following proposed local implication is false, even when the endpoint
incidences are compatible with `d(a)=d(p)=7`:

> If every member of `E` has a neighbour in `R`, every nonempty
> `Y subseteq R` satisfies `lambda(Y)>=7`, the vertices `a,p` have a unique
> common neighbour in `R`, and one is additionally given subsets
> `C_a,C_p subseteq T`, interpreted as rooted-model contact sets, with
> `|C_a union C_p|<=3`, then there are disjoint nonempty connected
> `U,V subseteq R`, adjacent to `a,p`, respectively, for which
>
> ```text
> |T-(C_a union N_T(U))| + |T-(C_p union N_T(V))| <= 1.
> ```

The conclusion is the exact sufficient bisection used by the
core-concentrated rooted-`K_5` reduction.

## The order-three profile

Let `R` be the triangle on `r0,r1,r2`, and prescribe the exact supports

```text
N_R(a)  = {r1,r2};                 N_R(p)  = {r0,r2};
N_R(t0) = {r0};                    N_R(t1) = R;
N_R(t2) = {r1};                    N_R(t3) = R;
N_R(t4) = R.
```

Thus `r2` is the unique common `a,p` neighbour.  Take

```text
C_a=C_p={t1,t3,t4}.
```

Every boundary resource is represented.  Direct inspection gives

```text
lambda({ri})=7                                      for i=0,1,2,
lambda({r0,r2})=lambda({r1,r2})=lambda(R)=7,
lambda({r0,r1})=8.
```

Hence all relative boundary inequalities hold, and the profile already
contains proper connected sides with boundary order seven.

Only `t0,t2` contribute to either defect, because `t1,t3,t4` lie in both
contact sets.  A side has defect zero exactly when it contains both `r0,r1`,
and has defect at most one exactly when it contains at least one of them.
If the two disjoint sides had total defect at most one, one would contain
both `r0,r1` and the other would contain at least one of them, a
contradiction.  The minimum total defect is exactly two.

The endpoint degree counts are compatible with the singleton identities.
Each endpoint has the other endpoint and two neighbours in `R`, including
the common neighbour `r2`.  Four further, pairwise distinct neighbours can
be placed in the three rooted bags indexed by `t1,t3,t4`, with the four
neighbours of `a` distinct from the four neighbours of `p`.  This gives
degree seven, exactly the displayed contact sets, and no second common
neighbour.  This is a compatibility check, not a construction of the
components `D,R` inside an ambient seven-connected target-free graph.

## Exact scope

The example proves that relative seven-connectivity, fullness, unique common
endpoint incidence, the degree-seven counts, and the joint contact bound do
not by themselves force the sufficient bisection.  It does not encode the
other component `D`, an actual rooted `K_5` model, all consequences of the
ambient singleton identities, or target-minor-freeness.  In particular, it
does not refute a disjunction in which failure of the bisection returns a
new connected side with boundary exactly seven: six of its seven nonempty
vertex sets, including five proper sets, are tight.

## Verification

Run

```text
python3 barriers/hc7_k44_core_concentrated_bisection_incidence_barrier_verify.py
```

The verifier checks all nonempty subsets of `R`, all ordered disjoint
connected endpoint-anchored pairs, the unique common neighbour, the contact
rank, and an explicit degree-seven-compatible placement of the remaining
endpoint neighbours.  Its pinned output is in
[`hc7_k44_core_concentrated_bisection_incidence_barrier_output.txt`](hc7_k44_core_concentrated_bisection_incidence_barrier_output.txt).
