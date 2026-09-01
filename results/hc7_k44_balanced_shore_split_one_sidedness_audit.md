# Audit: one-sidedness in the balanced adjacent-singleton shore split

**Verdict: GREEN.**  The exact written unbounded theorem revision identified
below follows from its stated hypotheses.  This is a separate internal
mathematical audit, not external peer review.  No finite computation is used.

**Audited source:**
[`hc7_k44_balanced_shore_split_one_sidedness.md`](hc7_k44_balanced_shore_split_one_sidedness.md)

**Audited source SHA-256:**
`5d89f80b93bb185fc7176cf5098a96b506fd8e518c5b7bbc9718867a4d0db664`

## 1. The two endpoint-specific misses

In the `D`-side `T`-rooted model, trimming the `x`--`S_1` path at its first
vertex of `D cap S_1` leaves exactly three unused opposite-shore core
vertices.  Assigning them arbitrarily to three distinct `S_0` bags gives all
ten `K_5` contacts.  If the second miss `u` of an `a`-component lies in
`S_0`, the `F` vertex assigned to the `u` bag makes
`W_a union {p}` universal; `W_p union {a}` has defect at most one.  The
seven bags are disjoint and have at least `10+5+4+1=20` contacts.  Symmetry
forces every two endpoint-specific misses to be `{a,x}` and `{p,x}`.

## 2. Anticompleteness of `x` and `F`

If `xf` is an edge, the `x` bag containing `f` and one `D`-side `S_1`
representative, with the other two available opposite-shore representatives
attached to distinct `S_0` bags, is a `T`-rooted `K_5^-` model.  Both helpers
are universal through `f`, so the contact count is `9+5+5+1=20`.  Thus the
displayed anticompleteness conclusion is valid.

## 3. Exact component counts

Fullness of `R` to `x` produces an `{a,p}`-missing component `W_0` with exact
boundary `T union F`.  Deleting `T union F` leaves exactly `k` such
components plus one connected remainder.  Deleting
`{p} union S_0 union F`, and symmetrically `{a} union S_0 union F`, leaves
exactly the respective endpoint-specific components plus one connected
remainder.  The seven-cut component theorem gives each count at most two.
Equality would give exactly three complementary components while a vertex
of `F` has four boundary neighbours in `S_0`, contradicting the theorem's
subcubic-boundary conclusion.  Hence `R-F` consists exactly of
`W_0,W_a,W_p`.

## 4. Final minor model

The final bags

```text
B_x=W_0 union {x} union J,
B_a=W_p union {a},
B_p=W_a union {p}
```

are connected, pairwise disjoint, and form a triangle.  They are universal
to the four disjoint core bags

```text
{q_1,f_1}, {q_2,f_2}, {q_3}, {q_4},
```

whose quotient has at least five contacts.  The final count
`3+12+5=20` is correct, with no hidden branch-set overlap.

## 5. Dependencies and exact scope

The audit treats as inputs the audited adjacent-singleton shore-split
profile theorem at SHA-256
`9234ff2c545608e7dcb3572dff3875137cbd2978a209826196dc111153d555ae`
and the audited seven-cut component theorem at SHA-256
`cbd3ecb73bea0530797ad58080ae6db6052bfbf69f90af558283e3f250772ef8`
(audit SHA-256
`8cd2f3adb52c8cfedd8fc3a11d47c67444dc9df62d6b5e79a78bfe914e533294`).
Apart from these inputs, the proof uses only seven-connectivity fullness,
connected paths and trees, literal `K_{4,4}` edges, and elementary
minor-model counting.

The theorem closes exactly the mixed endpoint-miss subcase.  It does not
close the remaining one-sided balanced, core-concentrated, or unbalanced
profiles, the literal T44 branch, T44, Conjecture 21, or `HC_7`.
