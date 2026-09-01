# Independent internal audit: blocker-repair barriers

**Verdict: GREEN at the stated profile-level scope.**  Both exact abstract
incidence constructions satisfy every listed reduced local minimum-blocker
condition.  The first has no witness to the component-local claim.  The
second has no witness either to that claim or to the proposed cross-component
mode which unnecessarily required the first side to see `b`.  This is a
separate internal audit, not external peer review and not an ambient-host
realization.

**Audited source:**
[`hc7_k44_intra_component_transversal_barrier.md`](hc7_k44_intra_component_transversal_barrier.md)

**Audited source SHA-256:**
`66e1502d0132a89d22439aa464e0dc48a0e79aa9f16b0fe9390d37e6d8688237`

**Verifier SHA-256:**
`7e075b20d71793fcb6c35bc43b2326a3199a4daf2b276a363b288d74d4cc11ee`

**Pinned-output SHA-256:**
`f03cba5d3817806c7dbebc2245316684cab63bbc5107bdb9d0f3fda72724243b`

## 1. Common graph and local hypotheses

An independent named-set enumerator checked all 511 nonempty subsets of

```text
X=K_3[Q] join (K_2[W_1] dotcup K_2[W_2] dotcup K_2[W_3]).
```

The degree sequence is `4,4,4,4,4,4,8,8,8`; the graph is
three-connected; and deleting `Q={t_0,t_1,t_2}` gives exactly the three
components `W_1,W_2,W_3`.  In both profiles the minimum of
`|N_X(Y)|+|N_D(Y)|` over nonempty `Y` is exactly seven, and its minimum
over proper connected sets seeing both `a,b` is exactly eight.  Thus all
relative inequalities and every strict smaller-blocker inequality hold.
The five `K`-resources are multiply attached.  In each profile the two
common resources meet all three components and the three exclusive
resources have support exactly `W_i`.  The sole boundary edge `ab` is
compatible with the required proper boundary bipartition of orders three
and four.

These checks establish only the reduced-data hypotheses.  They do not show
that either profile occurs in a seven-connected graph or that `ab` is an
actual three-contractible edge in such a graph.

## 2. First profile

For the first support assignment, the five `K`-resource support sizes are
`3,3,2,2,2`.  The special vertex `p=t_0` sees `a` and no
`K`-resource, while `X-p` is `H`-full.

For `V subseteq W_i` to see `b,c_1`, it must contain `l_i`; to see
`c_2`, it must contain `r_i`.  Thus `V=W_i`, after which `X-V`
misses `e_i`.  Hence the component-local transversal claim has no witness.

The full two-helper bisection remains positive.  For

```text
U={t_0,l_1,l_2},    V=X-U,    h_0=c_2,
```

both sides are connected and adjacent.  The first defect is `{e_3}` and
the second is empty.  Exhaustion finds 231 spanning two-helper witnesses.

## 3. Second profile and the corrected cross mode

For the second support assignment the independently recomputed minima are
again seven and eight.  Every vertex of a component `W_i` is eligible for
the special-vertex conclusion; for example `p=l_1` sees `a`, sees exactly
`c_1,e_1` in `K`, and `X-p` is `H`-full.

No component `W_i` sees `b`, so there is no component-local witness.  The
original cross mode also has no witness: a first side seeing `b` must
contain its unique support vertex `t_2`, whereas an `H`-full complement
must contain `t_2` as well.  Exhaustion gives zero witnesses for each of
these two modes.

For

```text
U={t_0,l_1,l_2},    V=X-U,    h_0=c_2,
```

the first side sees `a,c_1,e_1,e_2` but not `b`, the complement is
`H`-full, and the two defects are `{e_3}` and the empty set.  Exhaustion
finds 54 such `b`-free cross-mode witnesses.

Fix any spanning connected bipartition `U,V=X-U` with `V` `H`-full.
The second defect in the two-helper criterion is zero.  Because `b` is
adjoined for free to the first helper, the first defect is

```text
|K-(N_D(U) union {h_0})|.
```

Some `h_0 in H` makes this at most one if and only if `U` misses at most
two of the five `K`-resources, equivalently if and only if `U` sees at
least three of them.  Thus the corrected `b`-free condition is exactly
equivalent to the spanning `H`-full-complement subcase of the two-helper
criterion, not merely sufficient within that subcase.

## 4. Exact scope

The constructions refute two inferences from the audited reduced local
data: a purely component-local transversal, and the disjunction of that
mode with a cross-component mode that requires the first side to see `b`.
They do not refute the corrected `b`-free `H`-full-complement mode, the
full two-helper bisection lemma, ambient realization, the weighted splitter
theorem, the literal `K_{4,4}` case, T44, Conjecture 21, or `HC_7`.
The exact remaining nonsingleton issue is the support-transfer case in
which the complement is not `H`-full.
