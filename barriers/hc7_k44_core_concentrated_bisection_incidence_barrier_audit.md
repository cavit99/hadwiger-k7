# Independent audit: local core-concentrated bisection incidence barrier

## Verdict

**GREEN** for the exact three-file revision

```text
ac7ce34f53cba653f8ac215ba4f0414ccfbf6de547fd7a32c447129e87978320  barriers/hc7_k44_core_concentrated_bisection_incidence_barrier.md
fe3333a0480d28c8ff3168b6d6980366daa103831912155672d984ae4574e95f  barriers/hc7_k44_core_concentrated_bisection_incidence_barrier_verify.py
29ecbc32a70155be04ee760992cb474aab10244e58bca9fec95b17988c5cdd2a  barriers/hc7_k44_core_concentrated_bisection_incidence_barrier_output.txt
```

The order-three profile is an explicit counterexample to the abstract local
incidence implication stated in the source.  It satisfies every displayed
relative boundary inequality, fullness at all seven boundary resources, the
unique common endpoint-neighbour condition, the joint contact bound, and the
claimed degree-seven compatibility, while every admissible ordered pair of
connected sides has total defect at least two.

The source now states the hypothesis at the correct level: `C_a,C_p` are
given subsets interpreted as rooted-model contact sets.  It does not claim
that the profile itself includes the other component, an actual rooted
model, an ambient seven-connected graph, or target-minor-freeness.

## 1. Exact boundary calculation

Write the vertices of the triangle `R` as `r0,r1,r2`.  The seven boundary
supports are

```text
a:  {r1,r2}       p:  {r0,r2}
t0: {r0}          t1: {r0,r1,r2}
t2: {r1}          t3: {r0,r1,r2}
t4: {r0,r1,r2}.
```

Every support is nonempty.  The endpoint supports meet exactly in `r2`, so
the common neighbour in `R` is unique.  Since `R` is a triangle, a singleton
has two internal boundary vertices, a two-set has one, and all of `R` has
none.  Direct calculation gives

```text
Y                         |N_R(Y)|   |N_E(Y)|   lambda(Y)
{r0}, {r1}, {r2}               2          5          7
{r0,r2}, {r1,r2}                1          6          7
{r0,r1}                         1          7          8
R                               0          7          7.
```

Thus all seven nonempty subsets satisfy the required inequality.  Exactly
six are tight, five of them proper, as stated.

## 2. Exhaustion of endpoint-anchored pairs

Both contact sets equal `{t1,t3,t4}`.  Consequently, for either endpoint
the defect of a side `X` is

\[
              2-\mathbf 1_{r0\in X}-\mathbf 1_{r1\in X}.       \tag{1}
\]

All nonempty subsets of the triangle are connected.  The verifier exhausts
the ordered disjoint pairs `(U,V)` with

\[
 U\cap\{r1,r2\}\ne\varnothing,
 \qquad V\cap\{r0,r2\}\ne\varnothing,                         \tag{2}
\]

which are exactly the conditions that `U,V` are adjacent to `a,p`,
respectively.  There are seven such pairs.  Formula (1) also gives a short
independent proof of the minimum: across two disjoint sets, each of `r0,r1`
can contribute to at most one of the four indicator terms.  Hence the defect
sum is at least `4-2=2`.  The pair

```text
U={r1},       V={r0}
```

attains two.  Therefore the asserted minimum is exact and no admissible pair
satisfies the proposed upper bound one.  No adjacency between `U` and `V`
is imposed by the refuted implication or by the verifier.

## 3. Joint contacts and degree-seven compatibility

The mask `0b11010` has precisely the bits indexed by `t1,t3,t4`, so the
union of the two contact sets has order three.  Each endpoint has the other
endpoint and two neighbours in `R`.  The verifier then assigns four further
neighbours to rooted-bag indices `t1,t3,t4`, using eight pairwise distinct
tokens across the two endpoints.  Thus each endpoint has

\[
                         1+2+4=7                              \tag{3}
\]

neighbours, both have exactly the displayed contact-set indices, and the
additional placements create no second common neighbour.  This verifies
compatibility with the degree-seven singleton identities; it deliberately
does not construct the omitted component or rooted branch sets.

## 4. Verifier and retained output

The verifier is deterministic and uses only the Python standard library.
Its bit masks agree with the seven supports displayed in the source.  Its
connectivity test, internal-boundary calculation, boundary-support union,
defect calculation, and ordered-pair loop all quantify over the full finite
domains rather than sampled cases.

Running

```text
python3 barriers/hc7_k44_core_concentrated_bisection_incidence_barrier_verify.py
```

reproduces the retained output byte for byte.  In particular it reports

```text
minimum_relative_boundary=7
tight_nonempty_sets=6
tight_proper_sets=5
unique_common_R_neighbours=1
joint_contact_rank=3
anchored_disjoint_pairs=7
minimum_total_defect=2
degree_seven_compatible=True
```

## 5. Scope and trust boundary

This is a finite exhaustive check of one three-vertex incidence profile,
with an independent hand calculation above.  It refutes only the claim that
the listed local incidence data force the one-defect bisection.  It does not
refute the proved bisection-or-connected-separator alternative: five proper
sets in the example already have relative boundary exactly seven.

The profile is not asserted to extend to an ambient seven-connected
`K_7^-`-minor-free graph, and it is not a counterexample to the audited
core-concentrated separator theorem, the weighted splitter theorem, the
literal `K_{4,4}` case, T44, Conjecture 21, or `HC_7`.  No unbounded theorem
is inferred from the finite enumeration.
