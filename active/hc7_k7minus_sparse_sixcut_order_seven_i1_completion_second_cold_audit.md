# Second cold audit: full order-seven `i=1` completion

**Verdict:** **GREEN** at the pinned revisions below.  This is a second
independent internal cold audit, not external peer review.  The first synthesis
audit was not consulted until the proof and the two independent enumerations
described below had been reconstructed.

## Pinned artefacts

```text
7384cdbbd16b0370aa171fad767975f043bddf873eecc235d2d1a552249a911f
  active/hc7_k7minus_sparse_sixcut_order_seven_i1_completion.md
67fb9b60e5272288c534791cf90866236648f6b9d1e6ea2de9b565f7d2315005
  active/experiments/sparse_sixcut_order_seven_i1_classification/verify.py
```

The two imported mathematical revisions were also checked:

```text
a81cb9476890fe0d373ecdc8aecebf5a40996d7d44ba15f16faf076dd5b581d8
  active/hc7_k7minus_ordinary_k5minus_rooting_contraction_gate.md
093c25e97ff5e5d627d12915c551418cd0039f5fb1f745dc03bdeb64148d7d75
  active/hc7_k7minus_sparse_sixcut_order_seven_theta_singleton_completion.md
```

## 1. Hall profile and the two immediate constructions

For an order-one deficient family, the Hall-profile equality chain gives a
single bag `{u}` with

```text
N_S(u)=empty,                 N_C(u)=C-{u}.
```

Writing `W=C-{u}`, relative six-connectivity applied to `{u} union Y` gives

```text
6 <= |N_C({u} union Y)|+|N_S(Y)|
  <= 6-|Y|+|N_S(Y)|
```

for every `Y subseteq W`.  Hence `|N_S(Y)|>=|Y|`, and Hall supplies the
claimed perfect matching from `W` to `S`.  The four branch bags other than
`{u}` partition `W` and retain at least five of their six mutual contacts,
so they are a spanning ordinary `K_4^-` model.  No individual-universality
claim for a deficient family of order greater than one is used.

If a four-bag model in `W` is nonspanning, choose a matched vertex in each
old bag and a vertex `w` outside their union.  The fifth bag
`{s_w,w,u}` is connected, disjoint from the four old bags, and adjacent to
each through `u`; its root is distinct from their four matched roots.  Thus
only the old model's possible missing contact remains.  If `W` instead has
a `K_5^-` minor, adjoining the matched root of one selected vertex in each
branch bag roots that model directly.  These constructions cover all models
regardless of whether a nonsingleton bag has unused matched vertices.

## 2. Independent check of the six-vertex classification

The supplied verifier has the exact search spaces stated in Lemma 2.1:
`65` spanning four-bag partitions, `75` nonspanning four-bag partitions,
and `21` five-bag partitions.  Its connectivity search starts in a nonempty
bag, reaches precisely the vertices of that bag, and its quotient test
accepts exactly when at most one pair of bags has no edge.  The mask loop
covers all `2^15` labelled simple graphs, while the `6!` permutation loop
computes graph-isomorphism classes rather than merely degree-sequence
classes.

I reran the pinned verifier with assertions enabled and obtained

```text
Theta(2,2,3): labelled_survivors=180
Theta(1,2,4): labelled_survivors=360
Theta(1,3,3): labelled_survivors=180
total_labelled_survivors=720 all_have_7_edges
order-seven i=1 core classification: PASS
```

As an independent check, a separately written enumerator used NetworkX's
unlabelled six-vertex graph atlas and restricted-growth surjections for the
branch-set partitions; it imported no masks, partitions, or canonical forms
from the supplied verifier.  It found exactly three unlabelled survivors,
all with seven edges and respectively isomorphic to
`Theta(2,2,3)`, `Theta(1,2,4)`, and `Theta(1,3,3)`.  Direct automorphism counts
gave labelled orbit sizes `180`, `360`, and `180`, summing to `720`.

The supplied program relies on Python assertions and therefore must be run
with the documented ordinary command, not with `python -O`.  This is an
operational qualification, not a mathematical gap.

## 3. Excess threshold and theta completion

Every surviving core has `e(W)=7`.  Since `u` contributes exactly its six
edges to `W` and has no edge to `S`,

```text
e(C)=13,
e(C,S)=e(W,S),
eta_S(C)=13+e(W,S)-4*7=e(W,S)-15.
```

Thus `eta_S(C)>=6` is precisely `e(W,S)>=21`.  These are exactly the
remaining hypotheses of the pinned theta completion theorem: a stable
six-root set, a root-invisible vertex universal to `W`, the perfect matching,
and one of the three theta cores.

I also tested that dependency without using its orbit table.  For each of
the `3*16=48` directed nonedges, a generic branch-set enumerator formed the
minimal graph containing only the theta edges, the six `u`--`W` edges, the
six matching edges, and that one extra incidence.  For each omitted root it
assigned every vertex of `{u} union W` independently to one of the five
labelled root bags or to no bag, then tested bag connectivity and all ten
bag contacts.  It found a punctured rooted `K_5^-` model in every case.
Additional boundary edges cannot destroy such a model.  The pinned theta
verifier independently reproduced its terminal output

```text
checked_models=34560
order-seven theta singleton completion: PASS
```

## 4. Lift to the host and scope

Let the rooted five-bag model omit `s_o`, and let `A,D` be two other
connected `S`-full components.  The two additional bags

```text
A union {s_o},              D
```

are connected and disjoint.  Each contacts all five rooted bags by fullness,
and `D` contacts the first new bag through an edge to `s_o`.  Hence the seven
bags have at most the one missing pair already present in the rooted
`K_5^-`, and they form a `K_7^-` minor.

No counterexample, omitted case, arithmetic defect, or dependency mismatch
was found.  The proved scope is the high-excess order-seven `i=1` Hall return
in the three-full-component setting.  It does not settle the `i>1` profiles,
the weighted local theorem, the whole sparse three-component case, or the
Norin--Totschnig benchmark.
