# Cold audit: the codegree-three or excess-eighteen dichotomy

**Verdict:** **GREEN** for the theorem source at SHA-256

```text
891f937237eff6eb3dd1a111ea6a68611c4b5d3ee7b4c2b4ef0465ff684b0b3e
```

This is an independent cold audit of the finite census, its lift to every
degree-eight centre, the ordered-incidence calculation, the use of the
Jakobsen-defect bound, the four-root residue and the low-endpoint
pair-deletion statement.  It is not an audit of any later use of the
trichotomy.

## 1. Frozen files and reruns

The principal experiment was audited and rerun at

```text
993278e07663ee5cd10df67917037ff784a743e4b3806813b6ddd8ad0c1e46a3
  active/experiments/sevenconnected_full_exterior_profiles/verify.py
247dc2357acf42f76a443c05f670f148cec9f347f31585e4aa5d110db2def55a
  active/experiments/sevenconnected_full_exterior_profiles/README.md
```

with NetworkX `3.6.1` from the repository lockfile.  The exact command

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  active/experiments/sevenconnected_full_exterior_profiles/verify.py
```

returned

```text
GREEN full-exterior degree-eight profile classification
minimum_degree_three_extensions=27529 isomorphism_classes=2590 critical_local=542
full_profiles=542 positive=486 target_free=56
cubic_vertex_distribution=[(4, 8), (5, 13), (6, 25), (7, 6), (8, 4)]
positive_certificate_digest=e2e65a34a35d8467054ab5c7b9db2df3bc2f4a2bb4345be1f900cb98d87fb500
target_free_profile_digest=a1bf6e4c242e984c46d89ce5a0f642c1ed2ae0811cb6aa0c7938a77f5ffa6bd0
rooted_completion_distribution=[(0, 29), (1, 8), (2, 4), (3, 7), (4, 3), (5, 3), (6, 1), (15, 1)]
canonical_completion_digest=e6efa5015a79c25f2a20757325b70ce86a52575ece804ded026cf706317269cc
```

The separate static-obstruction experiment was also inspected and rerun:

```text
2421f7b00b263ad3ee5f4f747252d7bee23f6ff7bdfd73247033ff2012f2fb76
  active/experiments/pair_deletion_low_endpoint_interface/verify.py
1d559d1efcf6ed90f24e417a12f67ce3d555cb8707405674ab02f3b3f171dd18
  active/experiments/pair_deletion_low_endpoint_interface/README.md
```

It reproduced graph6 code `HN~~zpx`, connectivity four, target exclusion,
the common four bag contacts and the arithmetic degree/codegree allocations
`(8,8,3)` and `(8,9,3)`.

## 2. Completeness of the eight-vertex census

Every unlabelled graph on eight vertices occurs in the generator: delete
one vertex, identify the resulting seven-vertex graph with one of the
`1,044` complete NetworkX atlas representatives, and restore the deleted
vertex with each of its `2^7` possible neighbourhoods.  Filtering before
isomorphism reduction therefore loses no eligible class.  The
Weisfeiler--Lehman hash and degree sequence are used only to make buckets;
the code performs an exact isomorphism test inside each bucket.  Isomorphic
graphs have the same bucket invariants, while nonisomorphic graphs in a
common bucket are not merged.

The four retained conditions are exactly those in Lemma 1:

```text
minimum degree at least three;
no K_6^- minor;
clique number at most three;
independence number exactly three.
```

The imported minor engine starts from singleton bags and recursively tries
every deletion and every merge of two touching bags.  Every connected
branch set can be built by such merges along a spanning tree, and all
unused vertices can be deleted, so the search is exhaustive.  Every
positive answer is separately checked for nonempty connected bags,
pairwise disjointness and at most one missing bag adjacency.  The engine's
frozen revision is

```text
d721c181a8388feb7901e8ab04f704c19679cfb56551752756a45733f28d6fdc
  results/hc7_k7minus_sixconnected_degree_eight_low_codegree_verify.py
```

For each local graph `J`, `augmented_graph(J, ())` adds two distinct
nonadjacent vertices, both complete to `J`.  Thus the program tests exactly
the graph `Q(J)` in Lemma 1, not a one-pole surrogate.  The `56` exhaustive
negative instances have the displayed distribution and hence each has at
least four degree-three vertices.  This proves the finite lemma over its
whole stated domain.

The README's abbreviated phrase about adding a centre should be read in
the full-exterior context: the implementation adds both the original
centre and the contracted exterior pole.  The source statement and tested
construction are unambiguous, so this shorthand does not affect the
result.

## 3. Lift to every degree-eight centre

Assume outcomes 1 and 2 of Theorem 2 both fail and fix a degree-eight
vertex `v`.  For `x in N(v)`,

```text
c(vx)=d_{G[N(v)]}(x),
```

so failure of outcome 1 gives minimum local degree three.  Literal
`K_5`-exclusion makes the local graph `K_4`-free.  The frozen exceptional
neighbourhood result gives independence number three.  A local `K_6^-`
model, together with singleton `{v}`, would be a `K_7^-` model, so the
fourth census condition also holds.

The exact defect improvement used here is Corollary 8 of the frozen source

```text
2ffeb857f4c999abc14bc28cd4650332d9397a140c601929117376f38f637449
  results/hc7_k7minus_degree_eight_triangle_poor_edge_packing.md
```

It applies because the critical-host inputs give minimum degree eight, no
literal `K_5`, and independence number three in every degree-eight
neighbourhood.  It yields, unconditionally within this critical-host
setting,

```text
n_8 >= 26+tau.
```

In particular the host has at least twenty-six vertices, whereas `N[v]`
has nine, so the exterior is nonempty.  The full-exterior theorem at

```text
c7cb794dd0298b1cbe98ac4ee1bdbbf04f1e5c546ae26f195fcbb034602b0c0d
  active/hc7_k7minus_critical_degree_eight_full_exterior_reduction.md
```

makes that exterior connected and full to `N(v)`.  Contracting it creates
the second universal pole, and it remains nonadjacent to `v` because it
lies outside `N[v]`.  The quotient is therefore exactly `Q(J)`.  Lemma 1
applies separately at every degree-eight centre.

## 4. Ordered-incidence inequality

Each degree-eight centre supplies at least four neighbours `x` with local
degree, and hence edge codegree, exactly three.  Failure of outcome 2
forces every such `x` to have degree at least ten.  Counting ordered pairs
with the degree-eight centre first gives

```text
4n_8 <= I.
```

A vertex of degree `i>=10` can be the second entry of at most `i` pairs.
With `h=sum_{i>=10} n_i`, the upper bound is exactly

```text
I <= sum_{i>=10} i n_i = 9h+tau.
```

Every term in `tau=sum_{i>=10}(i-9)n_i` contributes at least one per
high-degree vertex, so `h<=tau` and `I<=10tau`.  There is no division by
two: the orientation of the pair is fixed, and an edge between two
degree-eight vertices cannot enter because the second endpoint is required
to have degree at least ten.  Combining this with the defect bound gives

```text
4(26+tau) <= 10tau,
```

and hence `tau>=104/6`; integrality gives `tau>=18`.  The constant eighteen
and all quantifiers in Theorem 2 are therefore correct.

## 5. Four-root residue

For every one of the `56` negative profiles, the verifier checks all
`binom(8,4)=70` four-sets.  A local `K_4` is excluded, so every four-set has
at least one local nonedge.  The code tests every such nonedge as the sole
pair possibly absent from a rooted `K_4^-` model and declares a four-set
closing only when every one of those tests contains a certified
`K_7^-` model.

If the nominally missed rooted pair is already an edge of `J[T]`, that
edge joins the two rooted branch sets and there is no miss after the lift;
so omitting local edges from the list of tested misses is correct.  After
contracting the four rooted bags, the tested completed graph is a subgraph
of a minor of the host.  Thus every finite certificate lifts.  The exact
`27/29` split and the list of `29` graph6 residues in Corollary 3 match the
rerun.

## 6. Low-endpoint branch and exact scope

In outcome 2, minimum degree eight makes the low endpoint have degree
eight or nine.  For `H=G-{v,x}`, deletion of the present edge `vx` gives

```text
|E(H)|=|E(G)|-8-d(x)+1 >= 4|V(H)|-8.
```

Deleting two vertices from a seven-connected graph leaves a
five-connected graph.  The primary statement of Norin--Totschnig,
Theorem 6, is exactly that every four-connected graph at this density has
a `K_7^vee` minor unless it is `K_{2,2,2,2}`.  The defect bound gives
`|V(H)|>=24`, excluding that eight-vertex exception.  The seven model bags
can be enlarged to span `H`; target exclusion ensures that neither of the
two nominal missing adjacencies appears.  Each of the three stated root
contact restrictions then follows from the indicated seven-bag completion
or absorption, with the edge `vx` used in the final restriction.

The graph `HN~~zpx` only proves a static quotient nonclosure.  Its
connectivity is four and the multiplicity rows are arithmetic data, not a
critical host.  The source accurately refrains from treating it as a
counterexample or as closure of the low-endpoint branch.

No proof defect was found.  The result is an unbounded global trichotomy,
but it expressly leaves outcome 1, the low-endpoint codegree-three branch,
and the `tau>=18` branch unresolved.  It does not prove Conjecture 21 or
Hadwiger's conjecture for `t=7`.
