# Independent cold audit: the order-eight Hall profile

**Verdict:** **GREEN** at the exact revisions below.  This is an independent
internal audit, not external peer review.

## Pinned source, verifier and imported lemma

```text
92f868fc8547fbba58037587ad3c65e2894905011d0c2c71ea9d8e0de6bc1ba5
  active/hc7_k7minus_sparse_sixcut_order_eight_hall_profile.md
4f6f4bbcbec7b82b79de02454419429538b90e996ef161e49cac65d98686923c
  active/experiments/sparse_sixcut_order_eight_hall_profile/verify.py
e5ad8fef32d6581234d5873317c77592757b1cd809c2a95c6bbbc2b710fec78c
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion.md
3993f9989bb6fdc6258c54d81793f56d670ef9589f844076bc592035e34ed1f8
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion_cold_audit.md
```

All four hashes match the files inspected.

The final source differs from the audited draft at SHA-256
`0fca63a9b9e8a1e573ce8eed43265cd67916832eb7f4b3d51538b5b1161c6516`
only by the status-only promotion to independently cold-audited and
paragraph reflow.  The theorem, proof, scope and verifier are mathematically
unchanged.

## 1. Minimal Hall deficiency

Let `I` be an inclusion-minimal deficient family of model bags and let
`R` be the set of roots adjacent to their union.  Every proper subfamily of
`I` satisfies Hall's condition.  Therefore, after deleting any one bag,
the remaining `i-1` bags match into `R`.  Their neighbourhood is contained
in `R`, so this gives `|R|>=i-1`; deficiency gives the reverse inequality.
Consequently

```text
|R|=i-1,
```

and the displayed matching is onto `R`.  This remains valid for `i=1`,
when both sets are empty.

Writing `s=|U|-i`, relative six-connectivity applied to `U` gives

```text
6 <= |N_C(U)|+|R| <= 8-|U|+i-1=7-s.
```

Thus `s` is zero or one.  When it is zero all selected bags are
singletons.  When it is one, equality forces `N_C(U)=C-U`, and distributing
`i+1` vertices among `i` nonempty bags gives exactly one two-vertex bag.
No bag-size case is omitted.

## 2. The complementary matching

For every `Y subseteq W`, the internal boundary of `U union Y` is contained
in `W-Y`, and its root boundary is contained in `R union N_T(Y)`.  The
relative-connectivity inequality therefore yields exactly

```text
|N_T(Y)|>=|Y|+s-1.
```

For `s=1`, the two bipartition classes `W,T` have the same order, so this is
Hall's condition for a perfect matching.  For `s=0`, adding one dummy root
adjacent to all of `W` converts the inequality into Hall's condition between
two sets of order `8-i`; deleting the dummy edge leaves a matching onto all
of `T` and one unmatched vertex of `W`.  The empty-set instance causes no
exception.

The matching of `I-{B}` into `R` chooses one adjacent vertex from each
matched bag.  Bag disjointness makes these choices distinct, and they are
disjoint from the complementary choices in `W`.  This verifies all three
claims about the two unmatched shore vertices, including the case in which
a singleton is omitted and one chosen vertex comes from the unique
two-vertex bag.  If `i=5`, spanning of the five model bags would give
`|U|=8`, contradicting `|U|<=i+1=6`; hence `1<=i<=4`.

## 3. Profile census and rerun

The positive five-part partitions of eight are exactly

```text
(4,1,1,1,1), (3,2,1,1,1), (2,2,2,1,1).
```

Selecting only singleton bags, or one two-vertex bag together with
singletons, gives respectively `4+3+2` and `4+3` rows, for sixteen in all.
The verifier independently enumerates the partitions and every nonempty
selected subfamily, filters by `|U|-i<=1`, and compares the resulting set
with the sixteen stated profiles.  It also checks that the two Hall
matchings select six vertices and leave two.  A fresh run produced

```text
profiles=16 matched_vertices=6 unmatched_vertices=2
order-eight Hall profile classification: PASS
```

The script uses only the Python standard library and is deterministic.

## 4. Rooted-model corollary

For a fixed six-root matching, the two unmatched vertices are exactly the
deleted set `Z`.  If `C-Z` had an ordinary `K_5^-` model, choosing one
vertex in each of its five branch sets and adjoining that vertex's distinct
matched root would preserve connectedness, disjointness and every old
branch-set adjacency.  The unused sixth root is omitted, so this is exactly
the excluded punctured rooted model.  The imported audited six-vertex
extremal lemma then gives `e(C-Z)<=11`, with equality only for
`K_2 join 2K_2`.

## 5. Scope

The result is an exact analytic Hall reduction plus a finite arithmetic
profile check.  It does not claim that any of the sixteen profiles is
realisable, eliminate them, or use the excess-six or packing-one
hypotheses.  The source states this limitation accurately.  No defect was
found within its stated scope.
