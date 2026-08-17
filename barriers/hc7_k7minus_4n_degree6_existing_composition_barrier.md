# The existing degree-six composition inequalities do not close at `4n`

**Status:** explicit barriers to two intermediate inferences, with a
deterministic verifier.  Both graphs contain an explicit `K_7` minor.  They
do not refute the six-connected `4n` target, or either inference after
adding `K_7^-`-minor exclusion as an essential hypothesis.

The verifier is
[`hc7_k7minus_4n_degree6_existing_composition_barrier_verify.py`](hc7_k7minus_4n_degree6_existing_composition_barrier_verify.py).

## 1. The two inferences

Let `H` be six-connected, let `x` have degree six, and put `T=N_H(x)`.
For a component `C` of `H-(T union {x})`, write

```text
delta_C=|E(H[C])|+|E_H(C,T)|-4|C|,
p_C(t)=|E_H(C,{t})|.
```

The exact identity

```text
|E(H)|=4|V(H)|-22+|E(H[T])|+sum_C delta_C
```

shows that the `4n` threshold gives

```text
|E(H[T])|+sum_C delta_C>=22.                         (1.1)
```

Neither of the following conclusions follows from six-connectivity,
fullness and (1.1) alone.

1. In the two-lobe case, some orientation of the lobes and some ordered
   pair `p,q in T` satisfy both numerical hypotheses of the existing
   one-terminal cross-lobe composition lemma.
2. In the one-lobe case, the boundary contains the literal `K_4` required
   by the existing `K_4`-reserve inequality.

The target-free hypothesis could still force a direct minor model when
these numerical conclusions fail.  The examples below show exactly where
such a new target-or-composition argument is needed.

## 2. A two-lobe equality graph defeating every orientation

Let

```text
T={t0,t1,t2,t3,t4,t5}
```

be independent.  Add a vertex `x` adjacent precisely to `T`.  Let

```text
A=a0 a1 ... a9,       B=b0 b1 ... b9
```

be two induced ten-vertex paths, with no edge between `A` and `B` and no
edge from `x` to either path.

For a path vertex, list the members of `T` to which it is **not** adjacent.
Along `A` the lists are

```text
{0}, {0,2}, {0,3}, {1,4}, {1,5},
{2,3}, {2,4}, {3,5}, {4,5}, {1}.                    (2.1)
```

Along `B`, add one modulo six to every entry in (2.1).  All incidences not
excluded by these lists are edges.

Every root has seven neighbours in each path.  Hence

```text
delta_A=delta_B=9+42-40=11,
|E(H[T])|+delta_A+delta_B=22.
```

The graph has order twenty-seven and size 108, exactly `4|V(H)|`.  The
verifier exhausts every deletion of at most five vertices and checks that
its connectivity is exactly six.

For independent `T`, the two hypotheses of the cross-lobe lemma reduce to

```text
delta_C-p_C(p)>=5,             delta_D>=9.            (2.2)
```

The second inequality holds for either lobe, but the first fails for every
root and either lobe:

```text
11-7=4<5.                                             (2.3)
```

Thus none of the 60 choices of an ordered root pair and an ordered pair of
lobes activates the existing composition lemma.

This graph is not target-free.  The seven bags

```text
{x}, {t0,a3}, {t1,a2}, {t2,a0},
     {t3,a1}, {t4,a4}, {t5,a5}
```

form a `K_7` model.

## 3. An independent boundary in the one-lobe equality case

Again take independent `T` and a vertex `x` complete to `T`.  Let

```text
C=c0 c1 ... c6 c0
```

be a seven-cycle with the additional chord `c0c2`, and make every vertex
of `C` adjacent to every vertex of `T`.  There are no other edges.

Then

```text
|V(H)|=14,                 |E(H)|=56=4|V(H)|,
delta_C=8+42-28=22.
```

The graph is six-connected: after deleting at most five vertices, a root
of `T` remains and joins every surviving vertex of `C` to `x` whenever
`x` remains.  The six-set `T` separates `x` from `C`, so the connectivity
is exactly six.

Here (1.1) is tight but `H[T]` contains no edge, and hence no literal
`K_4`.  Thus the current `K_4`-reserve theorem has no application.  Again
the graph itself is harmless: the bags

```text
{x}, {t0,c0}, {t1,c1}, {t2,c2},
     {t3,c3}, {t4,c4}, {t5,c5}
```

form a `K_7` model.

## 4. Exact consequence

Raising the candidate density from `4n-6` to `4n` does not, by arithmetic
alone, close either residual degree-six case with the present theorems.
In the two-lobe case the first unsupported inference is that the two
numerical hypotheses of the cross-lobe lemma can be aligned.  In the
one-lobe case there is no opposite component with which to merge a rooted
`K_4` and a rooted six-bag model, and high excess does not force a literal
boundary clique.

A viable repair must use `K_7^-`-minor exclusion to prove a genuine
dichotomy: either a direct `T`-rooted near-clique model already exists, or
the failed high-attachment pattern can be converted into the numerical
orientation required by the cross-lobe lemma.  Merely strengthening (1.1)
is insufficient.
