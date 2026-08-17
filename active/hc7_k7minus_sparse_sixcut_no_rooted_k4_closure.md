# Closure of the all-no-rooted-`K_4` sparse six-cut branch

**Status:** written proof with a deterministic exact finite lemma, pending
separate audit.  In every returned three-component six-cut, at least one
closed lobe contains a four-rooted `K_4` model.  The result closes the
entire branch in which all such models are absent.  It does not compose an
arbitrary surviving rooted model across the other lobes and therefore does
not eliminate the whole sparse three-component row.

Write `K_7^-` for `K_7` with one edge deleted.  Let `G` be a
six-connected `K_7^-`-minor-free graph, let `S` be a six-vertex cut, and
suppose that `G-S` has exactly three components.  Put

```text
B=G[S],   b=|E(B)|.
```

For a component `C`, write

```text
c=|C|,
e_C=|E(G[C])|,
a_s=|E_G(C,{s})|  for s in S,
P=sum_{s in S}a_s,
eta(C)=e_C+P-4c.
```

Assume the returned-cut density identity

```text
b+sum_C eta(C)=24+sigma,   sigma>=0.                 (1)
```

This is the exact identity supplied by the audited returned-cut gate in
the minimum-enemy `4n` programme.

## Theorem 1 (some four-rooted clique exists)

There are a component `C` of `G-S` and a four-set `Z subseteq S` such
that the closed shore `G[C union Z]` contains a `Z`-rooted `K_4` model.

### Proof

Suppose otherwise.  Fix a component `C` and a pair
`{p,q} subseteq S`, and put `Z=S-{p,q}`.  The pair
`(G[C union Z],Z)` is internally four-connected: a prohibited rooted
separation of order at most three, together with `p,q`, would give a cut
of `G` of order at most five, with either of the other two components on
the opposite side.

By assumption the pair has no `Z`-rooted `K_4` model.  Norin--Totschnig
Lemma 9 therefore gives

```text
e_C+P-a_p-a_q+|E(B[Z])| <= 3c+5.                    (2)
```

Sum (2) over the fifteen pairs `{p,q}`.  Each attachment count `a_s`
occurs in ten of the complementary four-sets, whilst each boundary edge
occurs in six of them.  Hence

```text
15e_C+10P+6b <= 45c+75.                              (3)
```

Since `C` is connected, `e_C>=c-1`.  Rewriting (3) in terms of the excess
and then using connectedness gives

```text
10eta(C)+5e_C+6b <= 5c+75,
10eta(C)+6b <= 80.                                   (4)
```

Apply (4) to all three components.  If `b>0`, then

```text
b+sum_C eta(C) <= b+3(8-3b/5)=24-4b/5<24,
```

contrary to (1).  It remains that `b=0`.  Equations (1) and (4) now force

```text
sigma=0,   eta(C)=8                                  (5)
```

for each of the three components.

Fix one component.  Equality in (4), together with connectedness, gives

```text
e_C=c-1,   P=3c+9.                                   (6)
```

Thus `C` is a tree.  Since `B` is independent, (2) and (6) say

```text
a_p+a_q>=c+3                                         (7)
```

for every pair.  The sum of the fifteen left sides is `5P=15c+45`,
which is exactly the sum of the fifteen lower bounds in (7).  Every
instance is consequently an equality.  All six attachment counts are
equal, and

```text
a_s=(c+3)/2  for every s in S.                       (8)
```

In particular, `c` is odd.  Six-connectivity gives minimum degree at
least six, so summing the degrees of vertices in `C` yields

```text
6c <= 2e_C+P = 5c+7.
```

Therefore `c<=7`.  The case `c=1` contradicts (8), since a boundary
vertex cannot have two neighbours in a singleton component.  If `c=3`,
then every boundary root is adjacent to all three vertices of `C`.
For any four-set `Z`, those three vertices are three disjoint singleton
`Z`-carriers, contrary to the audited bound `mu_Z(C)<=2`.

It remains that `c` is five or seven.  Lemma 2 below proves that every
four-set `Z subseteq S` then has a `Z`-rooted `K_4` model in
`G[C union Z]`, again contradicting the supposition.  \(\square\)

## Lemma 2 (the two finite equality rows)

Let `C` be a tree, let `S` be an independent six-set, and suppose that
every vertex of `C` has total degree at least six in `G[C union S]`.

1. If `|C|=5` and every root has four neighbours in `C`, then every
   four-set `Z subseteq S` has a `Z`-rooted `K_4` model.
2. If `|C|=7` and every root has five neighbours in `C`, then the same
   conclusion holds.

Moreover, in every case the four bags can be chosen as

```text
{z_i,v_i},   i=1,2,3,4,
```

for four distinct vertices `v_i in C`.

### Exact finite verification

The verifier
[`active/experiments/sparse_sixcut_no_rooted_k4/verify.py`](experiments/sparse_sixcut_no_rooted_k4/verify.py)
uses only the Python standard library.

For order five, each root misses exactly one tree vertex.  If `h(v)` is
the number of roots missing `v`, minimum degree says

```text
h(v)<=d_C(v).
```

The verifier generates the three unlabelled trees and all `36` possible
missing-count profiles satisfying these inequalities.  Root permutations
need not be repeated because the conclusion is required for every
four-subset and is invariant under relabelling the roots.

For order seven, each root misses a pair of tree vertices.  The six missed
pairs form a loopless multigraph `M` on `C`.  If `h(v)=d_M(v)`, minimum
degree again gives `h(v)<=d_C(v)`.  Both sides have total sum twelve, so

```text
d_M(v)=d_C(v)  for every v.                          (9)
```

The verifier generates the eleven unlabelled order-seven trees and all
`1,149` loopless edge multisets with degree sequence (9).

For each profile and each of the fifteen four-sets of roots, the verifier
tests every injection of the four roots into the tree.  It accepts only
after directly checking that each two-vertex bag is connected and every
pair of bags has an edge between it.  The exact census is

```text
order     tree shapes   profiles   four-sets verified
  5            3           36               540
  7           11        1,149            17,235
```

Every test accepts.  The first-witness transcript digests are

```text
order 5: c78743f57d3a36bf6ca87f1a9e339e1f2f09cd53832ad6805f73e9f606ecacf7
order 7: a5d70b88bfb125047b3cb2d3b3a9f0acfdfd5d7741c5aaac11ec66390c76ae1d
```

The generation is exhaustive: Prüfer sequences generate every labelled
tree and canonical centre codes retain one representative of each
unlabelled shape; bounded compositions give every order-five profile;
and recursive pairing of degree stubs gives every loopless order-seven
edge multiset, with duplicates removed.  The script asserts every census
and digest above.  This proves the lemma within the stated finite trust
boundary.  \(\square\)

## Consequence and remaining obstruction

The all-no-rooted-model branch is empty for every boundary with
`0<=b<=8`, including the independent boundary equality case.  Hence any
surviving sparse returned three-component cut necessarily contains at
least one four-rooted `K_4` model in one lobe.  The unresolved step is a
valid cross-lobe composition theorem.  Two four-root carriers in another
lobe do not by themselves suffice: the omitted boundary roots need not
attach separately to the two carriers.

## Dependencies

- The returned-cut identity (1) is Corollary 5 of
  [`hc7_k7minus_sixconnected_degree_eight_low_codegree.md`](../results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md),
  source SHA-256
  `06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844`.
- Norin--Totschnig Lemma 9 is used in the same checked form as in the
  audited exact six-cut localisation theorem, source SHA-256
  `f2a4480d27556996620117a68a8a7924dd61cf37bf5ec9e8cce4c953dfcc88af`
  and audit SHA-256
  `28ce72f1ea1f7db44b6f8c4bd14b3c51c863c0b4f2478acf37952daff10fa00b`.
- The four-root carrier packing bound used at `c=3` has source SHA-256
  `adfcc70aca8543e15bcf7e94e1fb310492535f8155f02cb5a5430adba4ce8372`
  and adjacent GREEN cold-audit SHA-256
  `4a185697d20ed73c358703eb7d433c3555bca6474497a011630d3805dc493e97`.
