# Independent internal audit: three-component trace elimination

**Verdict: GREEN.**  Under the explicitly retained adjacent-singleton
label-disjointness hypothesis, the theorem gives a valid explicit
`K_7^-` minor model for every possible distribution of the opposite
literal shore.  The proof is unbounded and computation-free.  This is a
separate internal audit, not external peer review.

**Audited source:**
[`hc7_k44_three_component_trace_elimination.md`](hc7_k44_three_component_trace_elimination.md)

**Audited source SHA-256:**
`3a0231bf451aa1ae577b8cc9c59e2900f6f311582984b572e992dc2f8fddf6d3`

**Frozen adjacent-singleton contraction trace:**
`174baaa7a01d75048575760387f568bbf2ace15cef61e10a2dd5ed35372ca2ef`

## 1. Distribution and component pieces

The distributions of the four `S_1` vertices among three components,
subject to meeting at least two, are exactly `3+1+0`, `2+2+0`, and
`2+1+1`.  Selecting component sizes `(3,1)`, `(2,2)`, and `(2,1)`,
respectively, ensures that at most one selected component has only one
core vertex.

The proof correctly retains the hypothesis

```text
L(a) cap L(p) = emptyset.
```

It is needed to show that a selected one-core component is not the
singleton consisting of that core vertex: fullness would otherwise make
the vertex adjacent to both `a,p`.  This fact is not supplied by the bare
contraction-trace theorem for arbitrary adjacent vertices, but it is an
audited conclusion in the singleton application and appears explicitly in
the theorem statement.

After removing a selected core vertex `s_i`, a chosen component `W_i`
satisfies

```text
N_G(W_i) subseteq E union {s_i}.
```

If `m_i=|E-N_E(W_i)|` and `delta_i` records whether `W_i` sees `s_i`,
then

```text
7 <= |N_G(W_i)| = 7-m_i+delta_i.
```

Thus `m_i<=1`, and `m_i=1` forces the `W_i`--`s_i` contact.  In a
multi-core selected component, choosing `W_i` to contain another member
of `S_1` makes it universal to `S_0`.  At the unique possible one-core
index, attaching `s_i` to the sole missed root repairs that contact.
Attaching the two removed core vertices to distinct roots therefore gives
four core branch sets with at least five mutual contacts.

## 2. The outside triangle

For

```text
A_i=N_E(W_i) cap {a,p,x},
```

one has `|A_i|>=2`.  The representative lemma is correct.  Two subsets
of a three-set, each of order at least two, have nonempty intersection.
If the intersection has at least two members, choose two distinct common
representatives.  If it has one member, choose it for one side and a
different member of the other set for the second.  In both cases the
representatives are distinct and there is a cross-incidence.

With `r_2` the unused member of `{a,p,x}`, the sets

```text
B_0=W_0 union {r_0},
B_1=W_1 union {r_1},
B_2=C_2 union {r_2}
```

are connected and pairwise disjoint.  The cross-incidence supplies
`B_0B_1`; fullness of the untouched component `C_2` supplies the other
two contacts.  Each of the three sets is universal to all four core sets.
Consequently the quotient has `3+12+5=20` contacts.

## 3. Scope

The audit checked every branch-set allocation, including the `2+1+1`
case, for connectivity, disjointness, and all twenty contacts.  The proof
does not use the common neighbour `b` or the subcubic conclusion for
`G[E]`.  There are no unresolved assumptions within the stated scope.

The result eliminates the complete three-component contraction response.
It does not eliminate the two-component core-concentrated rooted-contact
profile, a nonsingleton blocker, the literal `K_{4,4}` case, T44,
Conjecture 21, or `HC_7`.
