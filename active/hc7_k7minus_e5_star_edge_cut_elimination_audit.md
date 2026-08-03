# Audit: disjoint star-and-edge five-cut elimination

**Verdict:** GREEN for the theorem as stated.

**Audited source:**
`active/hc7_k7minus_e5_star_edge_cut_elimination.md`

**SHA-256:**
`3963035bb15be4599dfa8e785d5ef0543a5a153b66a907f0b28008ca98a6f488`

This is an internal mathematical audit, not external peer review.  The
source eliminates one complete row of the auxiliary `(E5)` programme; it
does not prove `(E5)`, the seven-connected `4n-2` theorem, Conjecture 21,
or `HC_7`.

## 1. Pinned dependencies

The two internal dependencies were checked at:

```text
fifth-root augmentation and dense five-cut conventions
81306114489449f1bd2d8521c4aefc216411f81bf6721c7763412d4a7a87c6c0

seven-edge five-cut reduction
a0f26f2c57a00f7e4d238bf68a4f2d824e3c90f100f47ebe2697e6be42f73461
```

Norin--Totschnig Lemma 12 is used in exactly its rooted form: an internally
four-connected graph `H` with four nominated roots and

```text
|E(H)| >= 4|V(H)|-9
```

contains a rooted `K^*_{4,2}` model.

## 2. Rooted six-bag lemma

Let `Q=Z union {t}` and write `gamma=delta_Q(L)`.  The edge identity is
exact:

```text
|E(G[L union Q])|=4|L|+gamma+|E(G[Q])|.
```

Completing only `G[Z]` adds `6-|E(G[Z])|` edges, while

```text
|E(G[Q])|=|E(G[Z])|+d_{G[Q]}(t).
```

Thus the completed graph has

```text
4|L|+gamma+6+d_{G[Q]}(t)
```

edges.  The hypotheses `gamma>=2` and `d_{G[Q]}(t)>=3` give exactly the
required lower bound `4|L|+11` on `|L|+5` vertices.

The internal-connectivity reduction has no omitted singleton case.  A
separation of the pair rooted at `Z` of order at most three either becomes
an internal separation of the pair rooted at `Q` after adding `t` to the
root side, or has open side `{t}`.  In the latter case `t` has its three
displayed neighbours in `Z` and at least one neighbour in the full lobe
`L`, so its degree is at least four.

The virtual edges added within `Z` can be deleted after applying the rooted
theorem.  Distinct nominated roots belong to distinct root bags.  Hence an
added root--root edge cannot be internal to a bag, and root--root adjacency
is not required in a `K^*_{4,2}` model.  No lifting through another
component is being assumed here.

After deleting the virtual edges, the fifth-root augmentation lemma applies
to the original internally five-connected pair `(G[L union Q],Q)`.  It
places `t` in a helper without changing the four root bags or the model
type.

## 3. Application to both high-side lobes

The preceding seven-edge reduction gives

```text
N(A)={p,a,b,c,d},        N(B)={p,a,b,c,e}
```

and every surviving numerical row has `alpha,beta>=2`.  In the first
boundary, `d` sees `a,b,c`; in the second, `e` sees `a,b,c`.  Lemma 1
therefore applies to both lobes with the same four-root set

```text
Z={p,a,b,c}.
```

No assumption on the edges from `p` to `a,b,c,d,e` is used.

## 4. The branch-set transfer

In the `B`-shore model, absorb the helper containing `e` into the root bag
at `p` and the other helper into the root bag at `a`.  The resulting four
bags form a rooted `K_4`:

- the helper--helper edge supplies the `p`--`a` bag adjacency;
- the two absorbed helpers supply all contacts from those bags to the
  bags rooted at `b,c`; and
- the literal boundary edge `bc` supplies the remaining contact.

The bag rooted at `p` contains `e`.  This last fact is the operation which
repairs the old two--three-linkage nonclosure.

The two shore models intersect only in the four literal roots.  Uniting
corresponding root bags is therefore legitimate: each union is connected
through its common root, different unions are disjoint, and all four
pairwise adjacencies come from the collapsed `B`-shore model.  The two
unabsorbed `A`-shore helpers are disjoint from these bags and from each
other, and have every required adjacency to the four roots and to one
another.

Finally, the component `D` is disjoint from all six bags and is connected.
Fullness to the original five-cut gives contacts

```text
D--M_a, D--M_b, D--M_c,
D--M_p through e, and D--U_A through d.
```

Only `D--V_A` is unforced.  The displayed seven sets consequently have at
most one missing pair, exactly the definition of a `K_7^-` minor model.

## 5. Scope and antecedent check

The proof does not assert that `D` contains disjoint connected supports for
the triple `{a,b,c}` and pair `{d,e}`.  It therefore avoids the invalid
ordinary two--three-linkage inference recorded in the audited predecessor.
It uses the two excess-at-least-two lobes simultaneously, so it is not an
isolated finite boundary elimination.

Together with the audited star, triangle, and four-edge-path cases in the
predecessor, this theorem eliminates the complete seven-edge complement
list for the selected minimum high-excess component.  Further boundary
sizes and the global existence of such a selected component remain separate
obligations in `(E5)`.
