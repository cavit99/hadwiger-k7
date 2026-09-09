# Quantitative star contractions

**Status:** conditional route. The improved reduction below is unproved;
no improved colouring bound is established. The primary exact campaign
remains Conjecture 19 in the [research ledger](../RESEARCH_LEDGER.md).

## Target and existing input

The proposed global target is an absolute-constant bound
`chi(G) <= C t (1+log log t)^(1/3)` for every finite `K_t`-minor-free
graph and every integer `t>=3`. This would improve the exponent, rather
than only the constant, in the newly reported square-root bound.

[Liu–Luo, v1, 6 September 2026](https://arxiv.org/html/2609.06867v1),
Lemmas 3.1–3.2, contract disjoint stars with independent centres and
independent leaf sets, losing at most one colour and removing
`Omega(n q/r^2)` vertices when `n<=r^2`, `q>=8r`, `delta>=q-1` and every induced
subgraph has independence number at least its order divided by r.
[Lin, v1, 8 September 2026](https://arxiv.org/html/2609.08713v1),
Lemmas 2.4–2.7, gives a related star packing and an iteration through
critical minors. Both papers report `O(t sqrt(log log t))` colouring.
Their primary statements and core proofs were inspected. These are fresh
preprints; no claim of external verification or relative priority is made.

The [archived two-centre argument](../archive/hadwiger_simultaneous_star_adversarial_audit.md)
already uses simultaneous contractions for exact recolouring. It supplies
no quantitative global packing. Our
[bipartite theorem](../results/bipartite_contractibility_via_matroid_reduction.md)
retains prescribed roots, but supplies no bound on chromatic loss.
The [product audit](../archive/hadwiger_product_amplification_barrier_and_bramble_lift.md)
already excludes the proposed amplification through standard products.

## A sufficient reduction, with its global implication

**Unproved reduction R.** There are absolute constants `K>=2` and
`0<c<=1/2` such that the following holds for every integer `r>=2`.
Suppose G has `n<=r^(3/2)` vertices, every minor F satisfies
`alpha(F)>=|F|/r`, and G is minor-minimal of chromatic number `q>=Kr`.
Then G has a minor J with

```text
chi(J) >= q-1,       |J| <= n(1-c q^2/r^3).
```

Minor-minimal means that every proper minor is `(q-1)`-colourable.
No prescribed roots or connectivity are required here. A construction
must specify disjoint connected contraction preimages; a quotient with
the right vertex count alone does not establish R.

**Conditional deduction.** R implies, for every nonempty graph in this minor class
with `n<=r^(3/2)`,

```text
chi(G)^3 <= (Kr+1)^3 + (3/c) r^3 log^+(n/(Kr)).
```

Here `log^+(x)=max(0,log x)`. To prove the implication, minimise `(n,e(G))`
lexicographically among counterexamples and put `q=chi(G)`. Every proper
minor has smaller `(n,e)` and a no-larger right side, so its chromatic
number is at most `q-1`. Also `q>Kr+1`. Apply R. The quotient has
`n'<n`, and its minors retain the independence hypothesis. Since
`n'>=q-1>Kr`, both logarithms are active. Writing the right side as
Phi(n), we obtain

```text
(q-1)^3 <= chi(J)^3 <= Phi(n')
 <= Phi(n)+(3/c)r^3 log(1-cq^2/r^3)
 <= Phi(n)-3q^2 < q^3-3q^2 < (q-1)^3.
```

The logarithm is defined because `q<=n<=r^(3/2)` and `c<=1/2`.
This is a contradiction. The decreasing parameter, minor-class closure
and complete chromatic conclusion are explicit; R itself remains open.

For the global implication use `r=2(a-1)` and the Duchet–Meyniel bound
on every `K_a`-minor-free minor, as stated in Liu–Luo, Theorem 2.2.
[Delcourt–Postle, v5, Theorem 1.6](https://arxiv.org/html/2108.01633v5)
reduces colouring to subgraphs of order at most `C0 a log^4 a`, with
`t/sqrt(log t)<=a<=t`. For sufficiently large a this order is at most
`(2(a-1))^(3/2)`. The displayed conditional bound then gives
`chi(H)/a=O((1+log log t)^(1/3))`; the bounded remaining a-range is
absorbed into the absolute constant. Thus R would prove the stated
global target. This is not a finite verification or an HC7 implication.

## The missing quantitative gain

The elementary star argument admits the following useful formulation.
Let `I={v1,...,vk}` be independent, `k<=r`, and suppose every induced
subgraph has independence number at least its order divided by r.
Greedily choose a largest independent `Li` in `N(vi)` outside the earlier leaves.
If `s_i` is the total number of leaves selected, then

```text
s_i >= (1-1/r)s_(i-1) + d(vi)/r,
s_k >= (1/(er)) sum_i d(vi).
```

The first inequality follows by applying the independence bound to the
remaining neighbourhood, which has at least `d(vi)-s_(i-1)` vertices.
Iterate it and use `(1-1/r)^(r-1)>=1/e`. The leaf sets are disjoint and
avoid I. Contracting the stars gives fixed disjoint connected preimages
and removes exactly `s_k` vertices; empty leaf sets can be skipped.
A colouring of the quotient colours
the original graph outside I by expanding each independent leaf set;
one fresh colour suffices for I. This is a refinement of the cited
elementary packing argument, not a new global colouring theorem.

Consequently it would suffice to prove

```text
max { sum_(v in I) d(v) : I independent, |I|<=r }
    >= c0 n q^2/r^2
```

in the critical graphs of R. Present inputs give only order `nq/r`.
They do supply the desired gain when `delta(G)>=q^2/r`, up to absolute
constants. The unresolved case therefore includes critical graphs with
`q-1<=delta(G)<q^2/r`. Further vertex losses when passing to a critical
minor might replace the stronger packing, but no bound on those losses
has been proved.

A distinct sufficient approach is the unproved density inequality
`e(G)<=D r^2 alpha(G)` for an absolute `D>=1` in the same minor class.
It would give an independent set of size at least `n delta/(2Dr^2)`.
Take `ceil(n delta/(2Dr^2))` of its vertices. This is at most r because
`n delta<=n^2<=r^3`. Their degree sum is at least
`n delta^2/(2Dr^2)>=nq^2/(8Dr^2)` for `delta>=q-1` and `q>=2`.
The first unsupported step is
this density inequality, not the star contraction or its cubic potential.

The attempted intermediate statement that a minor with uniformly bounded
branch-set size can have independence ratio
`Omega(sqrt(e(G)/alpha(G)))` is
[refuted for every fixed size bound](../barriers/quantitative_bounded_bag_density.md),
even when `|G|<=t log t` for `t=sqrt(e(G)/alpha(G))`. The audited
construction uses high-girth graphs and clique blow-ups and covers every
choice of the bounded bags. Matching contractions are a special case.
Thus the small-order hypothesis alone does not justify this extraction.
Larger bags or use of the full density-surplus hypotheses remain possible;
neither the density inequality nor R is refuted.

Testing must respect the hypotheses. The all-minor independence bound
implies `h(G)<=r`, by applying it to a clique minor. Thus a graph in the
unbounded `q/r` regime would already contradict ordinary Hadwiger;
familiar high-degree examples do not test that regime merely by having
large minimum degree. This observation neither proves nor refutes R.
Successive independent sets in different quotients also need not have
independent original preimages, so their colour losses cannot simply be
charged once. Independent leaf sets are not a matroid.
