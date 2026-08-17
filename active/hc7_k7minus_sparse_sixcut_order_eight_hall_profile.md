# The exact Hall profile at shore order eight

**Status:** proved analytic reduction with a deterministic finite profile
check; independently cold-audited.  This is not an order-eight completion
theorem: no counterexample was found, but the rooted-model conclusion remains
open in the sixteen profiles listed below.  The excess and packet-number
hypotheses are not used in this reduction.

## 1. Setup

Let `S` be a stable six-set and let `C` be a connected `S`-full shore with
`|C|=8`.  Assume

```text
|N_C(X)|+|N_S(X)|>=6                              (1.1)
```

for every nonempty `X subseteq C`.  Let
`B_1,...,B_5` be a spanning ordinary `K_5^-` model in `C`.  Form the
root--bag incidence graph.  Suppose it has no matching saturating the five
bags, choose an inclusion-minimal deficient family `I`, and put

```text
i=|I|,       U=union_{B in I} B,
R=N_S(U),    W=C-U,    T=S-R.
```

## 2. The order-eight profile theorem

### Theorem 2.1

The following assertions hold.

1. `1<=i<=4`, `|R|=i-1`, and, for every `B in I`, the bags in
   `I-{B}` have a matching onto `R`.
2. Exactly one of the following two types occurs.

   **Singleton type:** `|U|=i`.  Every bag in `I` is a singleton,

   ```text
   |N_C(U)|>=7-i,
   ```

   and the bipartite graph from `W` to `T` has a matching saturating `T`,
   leaving exactly one vertex of `W` unmatched.

   **One-edge-bag type:** `|U|=i+1`.  Exactly one bag in `I` has two
   vertices and every other bag in `I` is a singleton.  Moreover,

   ```text
   N_C(U)=W,
   ```

   and the bipartite graph from `W` to `T` has a perfect matching.

3. In either type all six roots can be matched to six distinct vertices of
   `C`, leaving exactly two shore vertices unmatched.  More precisely:

   * in the singleton type, after fixing a matching from `W` onto `T` and
     writing `z` for its unmatched vertex, every `u in U` can be the other
     unmatched vertex;
   * in the one-edge-bag type, the two vertices of the unique two-vertex bag
     can be left unmatched together; if a singleton `u in U` is left
     unmatched instead, the other unmatched vertex can be chosen in that
     two-vertex bag.

### Proof

Minimal Hall deficiency gives `|R|<=i-1`.  For any `B in I`, every
subfamily of `I-{B}` is a proper subfamily of `I` and hence is
Hall-sufficient.  Hall's theorem matches the `i-1` bags of `I-{B}` into
`R`.  Therefore `|R|>=i-1`, equality holds, and this matching is onto `R`.

Write

```text
s=|U|-i.
```

Every bag is nonempty, so `s>=0`.  Apply (1.1) to `U`:

```text
6 <= |N_C(U)|+|R|
  <= (8-|U|)+(i-1)
   = 7-s.
```

Thus `s` is zero or one.  If `s=0`, all `i` bags are singleton and the same
inequality gives `|N_C(U)|>=7-i`; since `|W|=8-i`, collective domination can
miss at most one vertex of `W`.  If `s=1`, equality holds throughout, so
`N_C(U)=W`; distributing `i+1` vertices among `i` nonempty bags gives exactly
one two-vertex bag and `i-1` singleton bags.

For `Y subseteq W`, apply (1.1) to `U union Y`.  Its internal boundary is
contained in `W-Y`, and its root boundary is contained in
`R union N_T(Y)`.  Hence

```text
6 <= (8-i-s-|Y|)+(i-1)+|N_T(Y)|,
```

or equivalently

```text
|N_T(Y)|>=|Y|+s-1.                                (2.1)
```

When `s=1`, one has `|W|=|T|=7-i`, and (2.1) is Hall's condition for a
perfect matching from `W` to `T`.  When `s=0`, add one dummy root adjacent to
all of `W`.  Inequality (2.1) is Hall's condition from `W` to
`T union {dummy}`.  Both sides have order `8-i`, so deleting the dummy edge
from a perfect matching leaves a matching saturating the `7-i` vertices of
`T` and exactly one unmatched vertex of `W`.

Combine this complementary matching with a matching of `I-{B}` onto `R`,
choosing in each matched bag a vertex adjacent to its matched root.  The bags
are disjoint, so the chosen vertices are distinct.  In the singleton type,
choose `B={u}`; this leaves `u` and the unmatched complementary vertex.  In
the one-edge-bag type, omitting the two-vertex bag leaves both of its vertices.
If a singleton bag is omitted, the matched root of the two-vertex bag is
adjacent to at least one of its vertices; choose that vertex and leave the
other one together with the omitted singleton.  In every case the two root
sets `R,T` are disjoint and all six roots are used.

Finally, `i=5` would put every one of the five spanning model bags in `I`,
so `U=C` would have eight vertices, contradicting `|U|<=i+1=6`.  Therefore
`1<=i<=4`.  □

## 3. The sixteen bag-size profiles

The five positive bag sizes partition eight, so their unordered shape is one
of

```text
(4,1,1,1,1),    (3,2,1,1,1),    (2,2,2,1,1).
```

In the singleton type, `I` selects only singleton bags.  In the one-edge-bag
type, it selects one two-vertex bag and otherwise only singleton bags.  Up to
equal-size bag permutations this gives exactly the following sixteen rows.

| spanning bag sizes | type | possible `i` |
|---|---|---|
| `(4,1,1,1,1)` | singleton | `1,2,3,4` |
| `(3,2,1,1,1)` | singleton | `1,2,3` |
| `(3,2,1,1,1)` | one-edge-bag | `1,2,3,4` |
| `(2,2,2,1,1)` | singleton | `1,2` |
| `(2,2,2,1,1)` | one-edge-bag | `1,2,3` |

The accompanying standard-library verifier enumerates every positive
five-part partition of eight and every nonempty selected subfamily, applies
`|U|<=i+1`, and reconstructs exactly these sixteen profiles.

## 4. Consequence under rooted-model exclusion

### Corollary 4.1

Fix any six-root matching supplied by Theorem 2.1 and let `Z` be its two
unmatched shore vertices.  If `G[C union S]` has no punctured rooted
`K_5^-` model, then `C-Z` has no ordinary `K_5^-` minor.  Consequently

```text
e(C-Z)<=11,
```

and equality can occur only when `C-Z` is isomorphic to
`K_2 join 2K_2`.

### Proof

If `C-Z` had an ordinary `K_5^-` model, select one vertex from each of its
five branch bags and adjoin that vertex's distinct matched root.  The five
enlarged bags form the excluded punctured rooted model.  The edge bound and
equality graph are the audited six-vertex extremal lemma in the order-seven
`i=4` completion theorem.  □

That theorem is pinned at

```text
e5ad8fef32d6581234d5873317c77592757b1cd809c2a95c6bbbc2b710fec78c
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion.md
3993f9989bb6fdc6258c54d81793f56d670ef9589f844076bc592035e34ed1f8
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion_cold_audit.md
```

## 5. Exact scope and remaining status

This theorem is an exact reduction of every deficient Hall outcome at shore
order eight.  It does not prove that the sixteen profiles contain a rooted
model, and it does not use `eta_S(C)>=6` or `mu_S(C)=1`.  Exact lazy searches
on several representative profile supports found no counterexample even
without the packet hypothesis, but those searches do not cover all support
orbits and are not part of the proof.

Thus the exact order-eight ordinary-minor status under the excess-six and
packet-one hypotheses remains open.  The next finite obligation is to combine
the two-unmatched-vertex matching with the overlapping six-vertex
minor-free deletions in Corollary 4.1, profile by profile, while retaining
unrestricted multi-vertex rooted branch bags.

## 6. Reproduction

Run

```text
python3 \
  active/experiments/sparse_sixcut_order_eight_hall_profile/verify.py
```

The expected terminal line is

```text
order-eight Hall profile classification: PASS
```
