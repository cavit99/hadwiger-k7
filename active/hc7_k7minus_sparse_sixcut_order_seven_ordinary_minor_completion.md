# Ordinary `K_5^-` minors root in every order-seven six-boundary shore of excess at least six

**Status:** proved by the complete order-seven Hall split, with each of its
four deficient-family cases and this synthesis independently cold-audited.

## 1. The local theorem

Write `K_5^-` for `K_5` with one edge deleted.  Let `S` be a stable set of
six vertices and let `C` be a connected `S`-full shore of order seven.
Assume

```text
|N_C(X)|+|N_S(X)|>=6                              (1.1)
```

for every nonempty `X subseteq C`, and put

```text
eta_S(C)=e(C)+e(C,S)-4|C|.
```

### Theorem 1.1

If `eta_S(C)>=6` and `C` has an ordinary `K_5^-` minor, then
`G[C union S]` has a punctured `S`-rooted `K_5^-` model: five pairwise
disjoint connected bags, rooted at five distinct vertices of `S`, with at
most one missing pair of bag contacts.  The sixth root is absent.

### Proof

Choose an ordinary five-bag `K_5^-` model in `C`.  Make it spanning as
follows.  Every component of the vertices outside its bags meets a bag,
because `C` is connected.  Absorb each such component into one bag that it
meets.  Connectivity and every old quotient contact are preserved, and the
five enlarged bags now partition `C`.

Form the bipartite incidence graph between these five bags and the six roots:
a root is incident with a bag when it has a neighbour in that bag.  If this
graph has a matching saturating the five bags, adjoin the five matched roots
to their bags.  This is already the required punctured rooted model.

Otherwise choose an inclusion-minimal Hall-deficient family `I` of model
bags and put `i=|I|` and `U=union I`.  The audited order-seven Hall profile
gives

```text
|U|=i,        |N_S(U)|=i-1,        N_C(U)=C-U,     (1.2)
```

so every bag in `I` is a singleton.  It also gives a perfect matching from
`C-U` to `S-N_S(U)` and, for every `u in U`, a perfect matching from
`U-{u}` to `N_S(U)`.  Since the five model bags partition seven vertices,
not all five can be singleton; hence

```text
1<=i<=4.                                             (1.3)
```

The four values in (1.3) are exactly the four pinned terminal theorems.

* If `i=1`, the unmatched singleton is universal in `C`, root-invisible,
  and the other six vertices have a perfect matching to `S`.  The pinned
  `i=1` theorem applies; this is the sole case that uses
  `eta_S(C)>=6`.
* If `i=2`, the direct pole-and-tree theorem produces the rooted model from
  (1.1), without using excess or packets.
* If `i=3`, the finite internal-support theorem leaves one possible core,
  whose two Hall leaves have total degree at most five.  Condition (1.1)
  excludes it.
* If `i=4`, the fourteen-row incidence theorem produces the rooted model
  directly; it needs neither (1.1) nor the excess bound after the Hall
  return.

Every possible Hall outcome therefore gives a punctured rooted model.  This
proves the theorem.  \(\square\)

## 2. Returned-six-cut consequence

### Corollary 2.1

Let `G` be six-connected and have no `K_7^-` minor.  Let `S` be an order-six
cut for which `G-S` has at least three connected `S`-full components.  After
deleting edges inside `S`, let `C` be one such component with `|C|=7`.  If
`C` has an ordinary `K_5^-` minor, then

```text
eta_S(C)<=5.
```

### Proof

Six-connectivity gives (1.1), and deleting edges within `S` does not change
it, the excess, or the ordinary minor.  Suppose instead that
`eta_S(C)>=6`.  Theorem 1.1 gives five rooted bags using `S-{x}` for some
`x in S`.

Choose two other connected `S`-full components `A,D` of `G-S`.  Add the two
bags

```text
A union {x},        D.
```

The first is connected.  Each new bag contacts every old rooted bag through
the root contained in that bag, and they contact each other through an edge
from `x` to `D`.  Thus the two new bags are universal to the five old bags
and to one another.  Since the old five-bag quotient misses at most one
pair, the seven bags form a `K_7^-` minor, a contradiction.  Hence the
integer `eta_S(C)` is at most five.  \(\square\)

## 3. Exact pinned dependencies

The Hall profile used in (1.2) is pinned at

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md
23db844015f8f38619e164453b1049b9c16468fe6677d3337d5b5bf63d33a0d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate_cold_audit.md
```

The four terminal cases and their reproducible checks are pinned at

```text
7384cdbbd16b0370aa171fad767975f043bddf873eecc235d2d1a552249a911f
  active/hc7_k7minus_sparse_sixcut_order_seven_i1_completion.md
67fb9b60e5272288c534791cf90866236648f6b9d1e6ea2de9b565f7d2315005
  active/experiments/sparse_sixcut_order_seven_i1_classification/verify.py
9c37daecebe2bf17e9ef7fafd9aae8845f01e989d7797afb208369b235cfb825
  active/hc7_k7minus_sparse_sixcut_order_seven_i1_completion_cold_audit.md
e3972b14008f022475682e4f802ffa17a02267010b42e41b98fa8deacbaccca2
  active/hc7_k7minus_sparse_sixcut_order_seven_i1_completion_second_cold_audit.md

c31da46f7cdd1f45c849ddc40e03372f2c2a240143d3020ef4978ca56456a9a3
  active/hc7_k7minus_sparse_sixcut_order_seven_i2_completion.md
0f70f992c3f348781bff753605c74b19f41058e5cdb60306d47168434ddfcd78
  active/experiments/sparse_sixcut_order_seven_i2_completion/verify.py
ae31d153d923989ba92c5007cf9f434b4257bbb09c009ebb75fbd066c67cb8b8
  active/hc7_k7minus_sparse_sixcut_order_seven_i2_completion_cold_audit.md

d37a3defb6a1344c151b43c92829fb420611fa2ef7e1c56dcc3e69ce38410b72
  active/hc7_k7minus_sparse_sixcut_order_seven_i3_completion.md
ac42bdfc2957b732484570ddb513f20e95d386d57a79d4265f2cfb804b7957af
  active/experiments/sparse_sixcut_order_seven_i3_classification/verify.c
7bf2163157aff5be99a0e7d0376547dc398dc795368cf9fc1265d7d8e16616be
  active/hc7_k7minus_sparse_sixcut_order_seven_i3_completion_cold_audit.md

e5ad8fef32d6581234d5873317c77592757b1cd809c2a95c6bbbc2b710fec78c
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion.md
08d284ea78a8a1d97ce3506166f005815507dbdcd852f6a73896f3148eca58e7
  active/experiments/sparse_sixcut_order_seven_i4_completion/verify.py
3993f9989bb6fdc6258c54d81793f56d670ef9589f844076bc592035e34ed1f8
  active/hc7_k7minus_sparse_sixcut_order_seven_i4_completion_cold_audit.md
```

## 4. Scope and benchmark

Theorem 1.1 is a complete local theorem at the first unresolved shore order:
it eliminates every order-seven ordinary-`K_5^-`-minor lobe of excess at
least six, rather than one Hall subcase or one finite configuration.  It is
a direct advance in the returned-six-cut route to `HC_7`.

It is not Conjecture 21, `HC_7`, or the unbounded coefficient-four theorem.
It does not treat shores of order at least eight, nor order-seven shores with
no ordinary `K_5^-` minor.  Its present significance is therefore below the
principal Norin--Totschnig machinery and below the campaign's stated primary
benchmark, despite closing a genuine complete base-order frontier.
