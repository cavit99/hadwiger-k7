# The full order-seven `i=1` Hall return is terminal

**Status:** proved, conditional only on the pinned finite six-vertex
classification and the independently audited theta completion theorem.

Write `K_5^-` for `K_5` with one edge deleted.  A punctured `S`-rooted
model uses five distinct roots of the stable six-set `S`, one in each of five
disjoint connected bags, with at most one missing pair of bag contacts.

## 1. Direct theorem

### Theorem 1.1

Let `C={u} union W`, where `|W|=6`, and let `S` be a disjoint stable
six-set.  Suppose that

1. `u` is adjacent to every vertex of `W` and to no vertex of `S`;
2. the bipartite graph between `W` and `S` has a perfect matching;
3. `W` has a spanning ordinary `K_4^-` model; and
4. `eta_S(C)=e(C)+e(C,S)-4|C|>=6`.

Then `G[C union S]` has a punctured `S`-rooted `K_5^-` model.

### Proof

Fix the perfect matching and use it to give each vertex `w` of `W` a
distinct root `s_w`.

First suppose that `W` has a `K_4^-` model whose four branch bags do not
span `W`.  Choose one vertex from each branch bag and attach its distinct
matched root.  Choose `w` outside the four bags.  The fifth bag

```text
{s_w,w,u}
```

is connected and, through `u`, contacts all four old bags.  The four old
bags have at most one missing contact, so these five rooted bags give the
conclusion.

Next suppose that `W` has a `K_5^-` minor.  Choose one vertex from each of
its five disjoint branch bags and attach the five distinct matched roots.
This roots the old model directly and again proves the conclusion.

It remains to consider a six-vertex graph `W` which has a spanning
`K_4^-` model, no nonspanning `K_4^-` model, and no `K_5^-` minor.  The
finite classification in Lemma 2.1 below says that `e(W)=7` and that `W` is
one of

```text
Theta(2,2,3),  Theta(1,2,4),  Theta(1,3,3).
```

Because `u` is universal to `W` and root-invisible,

```text
e(C)=6+e(W)=13,
e(C,S)=e(W,S),
eta_S(C)=e(W,S)-15.
```

The excess hypothesis therefore gives `e(W,S)>=21`.  The pinned theta
singleton completion theorem now supplies a punctured rooted `K_5^-`
model.  This proves the theorem.  \(\square\)

## 2. The finite core classification

### Lemma 2.1

Let `W` be a simple graph on six vertices.  If `W` has a spanning
`K_4^-` model, no nonspanning `K_4^-` model, and no `K_5^-` minor, then
`W` has seven edges and is isomorphic to exactly one of the three theta
graphs in Theorem 1.1.

### Finite proof

There are `2^15=32768` labelled simple graphs on six vertices.  A spanning
four-bag model is an unlabelled partition of the six vertices into four
nonempty connected bags; there are `S(6,4)=65` such partitions.  A
nonspanning four-bag model uses four or five vertices, giving

```text
C(6,4) S(4,4) + C(6,5) S(5,4) = 15+60 = 75
```

partitions.  A five-bag model uses five or six vertices, giving

```text
C(6,5) S(5,5) + S(6,5) = 6+15 = 21
```

partitions.  For each partition it is enough to test bag connectivity and
whether at least all but one pair of bags contact.

The accompanying standard-library verifier enumerates exactly these masks
and partitions.  Precisely `720` labelled graphs survive.  Every survivor
has seven edges, and canonicalisation under all `6!` vertex permutations
gives three classes:

```text
Theta(2,2,3): 180 labelled graphs,
Theta(1,2,4): 360 labelled graphs,
Theta(1,3,3): 180 labelled graphs.
```

The counts sum to `720`, so the three classes are exhaustive.  This proves
the finite lemma.  \(\square\)

## 3. Order-seven Hall consequence

Take a spanning ordinary `K_5^-` model in a seven-vertex shore and suppose
an inclusion-minimal Hall-deficient family of its root--bag incidence graph
has order `i=1`.  The audited order-seven Hall profile gives a singleton bag
`{u}` with

```text
N_S(u)=empty,          N_C(u)=C-{u},
```

and gives a perfect matching from `W=C-{u}` to `S`.  The other four model
bags partition `W` and retain all but at most one of their six mutual
contacts, so they form a spanning ordinary `K_4^-` model in `W`.  Therefore
Theorem 1.1 applies whenever `eta_S(C)>=6`.

In the three-full-lobe setting, absorb the omitted root into either of the
two other full components and use the remaining component as the seventh
bag.  The result is a `K_7^-` minor.  Hence the complete order-seven `i=1`
Hall return is terminal; it is not merely reduced to three unchecked theta
rows.

## 4. Pinned dependencies and reproduction

The order-seven Hall profile is in
`hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md`, SHA-256

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8.
```

The theta completion theorem is
`hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion.md`,
SHA-256

```text
093c25e97ff5e5d627d12915c551418cd0039f5fb1f745dc03bdeb64148d7d75,
```

with cold audit SHA-256

```text
b8dc456fb995e382478884bc3bc55531ae1797d59f3c8d7eee739adb0de335ae.
```

Run the new finite classifier with

```text
python active/experiments/sparse_sixcut_order_seven_i1_classification/verify.py
```

Its terminal line is

```text
order-seven i=1 core classification: PASS
```
