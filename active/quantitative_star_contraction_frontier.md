# Quantitative star contractions

**Status:** reserved construction route. Reduction R remains unproved;
its auxiliary uniform-cost independence reduction is refuted. Its former
global colouring target is superseded by Liu–Luo v2. No new colouring
bound is established by this repository. Current priorities are in the
[research ledger](../RESEARCH_LEDGER.md).

## Target and existing input

**Literature correction, 14 September 2026.**
[Liu–Luo, v2, 9 September 2026](https://arxiv.org/html/2609.06867v2),
Theorem 1.1, gives `chi(G)<=C t log log log t` for every finite
`K_t`-minor-free graph and integer `t>=16`, with an absolute constant C.
The former target `O(t(1+log log t)^(1/3))` is asymptotically weaker:
putting `x=log log t`, `log x=o(x^(1/3))`. Thus proving that global
bound would no longer improve the published preprint's bound. This
supersedes the proposed payoff, not the unproved contraction R or its
conditional deduction below.

Version 2 combines contraction to low degeneracy (Lemma 3.2) with
fractional-colouring rounding (Lemma 4.3). The latter's concentration
condition is `R0^2>=64 k m^2 log n`, where `R0=2r`,
`m=ceil(n/r)` and `k=ceil(R0 log(2 max{1,d/R0}))` for a d-degenerate
n-vertex graph with fractional chromatic number at most r. Sections 3–6
were inspected for scope and mechanism; this is not a separate full
proof audit. Neither a six-colouring for t=7 nor prescribed branch-set
attachments follow from these estimates. Reopen this route only for a
stronger quantitative consequence or a specified application of R;
the old exponent alone is no longer a reason to pursue it.

**Combination limit; no counterexample to R or the density target.** For
fixed positive a,b and large integer r, take
`r<=n<=min{r^(3/2),a r log^b r}` and put `lambda=1+log(n/r)`.
Assume the stronger density target with a fixed `D>=1` and the all-minor
independence hypothesis. Choose an integer `r<=d<=n`. A core A of minimum
degree d then supplies
`ceil(|A|d/(2D r^2))<=r` independent centres. Capped packing removes at
least `|A|d^2/(2 exp(1) D r^3)` vertices per paid colour. Liu–Luo's core
iteration would then cost `O(r^3 lambda/d^2)` colours to reach degeneracy
below d. With `x=d/r`, their rounding yields
`O(r lambda/x^2+r(1+log^+ x))`; choosing `x` of order `sqrt(lambda)`
still gives `O(r(1+log lambda))`, the same asymptotic order as v2.
R alone does not even supply this core reduction: it applies only to
chromatic-critical graphs. A stronger packing with this polynomial gain
therefore does not by itself justify an improved bound through that
combination. The chromatic-preserving rule below remains a possible
different mechanism, with global availability and total progress unproved.

**Retained input provenance.** [Liu–Luo, v1, 6 September 2026](https://arxiv.org/html/2609.06867v1),
Lemmas 3.1–3.2, contract disjoint stars with independent centres and
independent leaf sets, losing at most one colour and removing
`Omega(n q/r^2)` vertices when `n<=r^2`, `q>=8r`, `delta>=q-1` and every induced
subgraph has independence number at least its order divided by r.
[Lin, v1, 8 September 2026](https://arxiv.org/html/2609.08713v1),
Lemmas 2.4–2.7, gives a related star packing and an iteration through
critical minors. Both papers report `O(t sqrt(log log t))` colouring.
Their primary statements and core proofs were inspected. The Liu–Luo
square-root comparison is historical and superseded above. These are fresh
preprints; no claim of external verification or relative priority is made.

[Lin, v3, 6 August 2026](https://arxiv.org/html/2607.21222v3),
Theorems 1.4–1.5, gives an asymptotically sharp `O(t log t)` order bound
for a k-connected subgraph when `k>=t>=3` and `e(G)/|G|>=Ck` in a
`K_t`-minor-free graph. Section 3 maximises disjoint contractions with
edge loss bounded by their degree sum; failure to extend them supplies
a dense neighbourhood. This suggests testing unrestricted contractions
against the density obligation below. It supplies neither independence
decrease nor a chromatic-loss bound. Restricting blocks to require either
breaks this inference: an extension can fail the extra condition without
losing many edges. Its density premise is unavailable
in the degree-eight C19 host. The paper also reports replacing the
Delcourt–Postle order cutoff by `O(t log^2 t)`; the conditional proof
below retains the original cutoff. That replacement alone would not
improve its double-logarithmic exponent.

The [archived two-centre argument](../archive/hadwiger_simultaneous_star_adversarial_audit.md)
already uses simultaneous contractions for exact recolouring. It supplies
no quantitative global packing. Our
[bipartite theorem](../results/bipartite_contractibility_via_matroid_reduction.md)
retains prescribed roots, but supplies no bound on chromatic loss.
The [product audit](../archive/hadwiger_product_amplification_barrier_and_bramble_lift.md)
already excludes the proposed amplification through standard products.

Uniform extensions cannot assume odd Hadwiger: [Kühn–Sauermann–Steiner–Wigderson,
v1, 23 December 2025](https://arxiv.org/html/2512.20392v1), Theorem 1.3,
construct, for every fixed epsilon>0 and sufficiently large t, graphs
with no odd K_t minor and chromatic number at least `(3/2-epsilon)t`.
This refutes the universal odd variant. It does not refute ordinary
Hadwiger or settle odd t=7. The present reduction uses only ordinary minors.

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

Allowing several centres in each connected bag gives no asymptotic gain
within this lifting rule. Let I be independent in the original graph;
delete only vertices of I and contract disjoint connected bags B with
B-I independent in that same graph. If L counts the non-I vertices in
nontrivial bags, the order loss is at most `L+|I|`. Assign each such vertex
to an adjacent I-vertex in its bag. The resulting disjoint stars remove
exactly L vertices and have the preceding one-colour lift. Deleting I
alone removes `|I|` vertices with the same colour bound. One of these
two operations therefore recovers at least half the proposed loss.
Thus this lifting rule gives no stronger asymptotic reduction than stars
or deletion of an independent set. A new packing argument could still help.

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
at the required scale has been proved.

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

## The uniform-cost independence reduction is refuted

The proposed alternative required, for an absolute D, a connected set B
in every connected noncomplete graph of the small-order, all-minor class,
with `alpha(G/B)<alpha(G)` and `e(G)-e(G/B)<=Dr^2`.
The [counterexample](../barriers/quantitative_alpha_drop_cost.md) refutes
this even when B is unrestricted: there are such graphs for which every
independence-decreasing contraction costs `Omega(r^2 log r)`.
Deleting a sublinear set from a suitable random graph leaves its maximum
independence number unchanged under every further small deletion. Every
eligible B is therefore linear in the host order and contains quadratically
many edges. The construction retains the order cap and independence bound
on every minor. The graphs themselves satisfy `e(G)<=r^2 alpha(G)`.

The old conditional induction was valid: a complete base has order at
most r, and contraction preserves the class and lifts through connected
preimages. Its universally bounded-cost premise is false. The density
inequality, critical reduction R and desired colouring bound remain open;
the construction does not establish R's additional chromatic and critical
hypotheses. Further attempts must use the density surplus or R directly.

Allowing cost `Dr^2 (alpha(G)-alpha(G/B))` avoids this counterexample but
merely restates the density obligation up to constants. Such reductions
telescope to the density bound. Conversely, under that bound, contracting
the whole connected noncomplete graph costs at most
`2Dr^2 (alpha(G)-1)`, since `alpha(G)>=2`. This supplies no new proof.

The following older local checks remain valid but do not restore the
refuted universal premise.

For a nonempty connected B, the exact identities are
`alpha(G/B)=max(alpha(G-B),1+alpha(G-N[B]))` and
`e(G)-e(G/B)=e(G[B])+sum_(z outside B) max(0,|N(z) intersect B|-1)`.
The first separates independent sets by use of the contracted vertex;
the second counts deleted internal edges and coalesced parallel edges.
Minimality of B alone does not bound this edge loss in terms of `h(G)^2`.
For `m>=1`, take the cycle `u-v-a-b-u`, and add vertices `w_i,l_i`
with exactly the extra edges `uw_i,vw_i,w_i l_i`, for `1<=i<=m`.
Then `alpha(G)=m+2`, while B=`{u,v}` gives `alpha(G/B)=m+1`
and edge loss `m+1`; its only proper nonempty subsets are singletons.
Tree-decomposition bags `{u,v,a}`, `{u,a,b}`, `{u,v,w_i}`, `{w_i,l_i}`,
with the second and all page bags attached to the first and each leaf
bag attached to its page bag, give width two; the literal triangle
`u,v,w_1` gives `h(G)=3`. Thus arbitrary minimal choices can be costly.
This does not refute the existential statement: B=`{a,b}` drops alpha
at cost one. The example neither violates the density inequality nor
satisfies the small-order premise with `r=3`.

Pairwise paths also need not form a scheme, even when each vertex of B
is its sole vertex in some maximum independent set. In the triangular
prism with triangles `u1u2u3`, `w1w2w3` and matching `u_i w_i`, take the
minimal alpha-dropping set B=`{u1,u2,w1,w2}`. Paths for its two opposite
pairs, with interiors outside B, must both use the edge `u3w3`.
This also blocks using separately chosen paths as a scheme. A construction
using the full density-surplus hypotheses remains possible.

Testing must respect the hypotheses. The all-minor independence bound
implies `h(G)<=r`, by applying it to a clique minor. Thus a graph in the
unbounded `q/r` regime would already contradict ordinary Hadwiger;
familiar high-degree examples do not test that regime merely by having
large minimum degree. This observation neither proves nor refutes R.
Successive independent sets in different quotients also need not have
independent original preimages, so their colour losses cannot simply be
charged once. Independent leaf sets are not a matroid.

## Criticalisation after a star packing

**Written deductions; global reduction still unproved.** The following
uses the [rooted bipartite theorem](../results/bipartite_contractibility_via_matroid_reduction.md),
source SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`,
and its [separate audit](../results/bipartite_contractibility_via_matroid_reduction_audit.md),
SHA-256 `1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`.
Those pins audit the input theorem, not this application.

**Degree bound.** If G is minor-minimal of chromatic number p and
`h(G)<=r`, where `r>=2`, then `delta(G)>=2p-2r+1`.
Fix v and a `(p-1)`-colouring of `G-v`. Every colour appears on `N(v)`;
at least `2(p-1)-d(v)` colours appear there exactly once. The unique
neighbours of any two such colours lie in the same bichromatic component:
otherwise a Kempe swap removes one colour from `N(v)`, colouring v too.
If `d(v)<=2p-2r`, select `2r-2` such roots and simple bichromatic paths
between every pair across an equal bipartition. Their colour projection
gives a scheme: intersecting paths share an endpoint label, fibres are
independent, and no selected root is internal on another path.
The theorem gives a rooted `K_(r-1,r-1)` model in `G-v`.
Contract `r-2` disjoint cross-pairs of its bags, retaining the two
unpaired bags, to obtain a `K_r` model. Every bag contains a neighbour
of v, so adjoining singleton v gives `K_(r+1)`, a contradiction.

**Order accounting.** Let G satisfy R's hypotheses. Choose independent
centres `I={v1,...,vk}` and, successively, maximal independent sets
`Li` in `N(vi)` outside earlier leaves. Put `L=union_i Li`, `ell=|L|`,
and contract the disjoint stars `Bi={vi} union Li`, with `ell>0`, to H.
Their fixed preimages give `|H|=n-ell` and `chi(H)=q-1`: expanding
independent leaves and giving I one fresh colour proves the lower bound;
minor-minimality gives the upper bound. For every untouched vertex
`u outside I union L`, maximality supplies a neighbour in Li whenever
`uvi` is an edge. Therefore

```text
d_H(u) <= d_G(u)-|N_G(u) intersect I|,
U = {u outside I union L : d_H(u)<2q-2r-1}.
```

Choose a `(q-1)`-chromatic minor J of H of minimum order, then minimum
edge count. It is fully minor-minimal and has `delta(J)>=2q-2r-1`.
No vertex of U survives as a singleton bag: contracting or deleting
elsewhere cannot increase its degree. A deleted vertex costs one;
a bag of size `b>=2` contains at most b members of U and costs
`b-1>=b/2`. Consequently

```text
|G|-|J| >= ell+ceil(|U|/2),       chi(J)=q-1.
```

Composition of the two models preserves disjoint connected preimages.
Also `e(G)-e(H)>=sum_(v in I) d(v)-binom(k,2)`: centre edges inside
their own stars disappear; each centre edge to an untouched vertex
coalesces with a leaf edge; between any pair of star bags at most one
centre-incident edge survives. These cases account for every centre edge.

The weighted external input [Reed--Seymour, (1.4), p. 148](https://cgm.cs.mcgill.ca/~breed/SummerNSERC04/frachad.pdf)
gives `chi_f(G)<=2h(G)<=2r`. Its primary statement was inspected.
**Capped-centre repair, 14 September 2026.** In R's order range, put
`m=ceil(n/r)<=r`. Split every class of a fractional 2r-colouring into
independent pieces of size at most m, retaining its weight on each piece.
Unit vertex coverage is preserved and the total weight is at most
`2r+n/m<=3r`. Weighted degree summation is `2e(G)`, so some piece I has
`|I|<=r` and `sum_(v in I) d(v)>=2e(G)/(3r)`. The earlier packing recurrence
then removes at least `2e(G)/(3 exp(1) r^2)` vertices at one-colour cost.
This combines the already recorded fractional splitting with capped
packing; it is also the mechanism of Liu–Luo v2, Lemma 4.1. It closes the
previous cardinality gap, but gives only the baseline `nq/r^2` scale
using our critical-degree bound. The extra factor `q/r` required by R
remains unproved; no improvement over Liu–Luo v2 follows.

It remains unproved that a choice forces
`ell+ceil(|U|/2)>=c n q^2/r^3`. The
[order and edge potential obstruction](../barriers/quantitative_order_edge_potential.md)
shows why the displayed numerical bounds alone do not yield the cubic
improvement; it is an arithmetic obstruction, not a graph counterexample
to R. No improved global colouring theorem follows from this subsection.

## Density surplus and a retained contraction history

**Retained construction; unproved.** Seek an absolute `D>=1` such that,
for every integer `r>=2` and finite graph G with

```text
|G|<=r^(3/2),       e(G)>D r^2 alpha(G),
```

there is a minor F with `|F|>r alpha(F)`. This is exactly the
contrapositive of the sufficient density inequality above. Test inputs
need not satisfy the all-minor independence bound: the output witnesses
its failure. No chromatic criticality or prescribed roots are required.

Generate a history by contracting an edge of minimum codegree in the
active quotient, or retiring a current bag of degree at most r. Record
each merged pair as the children of its new bag; a retired bag becomes a
forest root and is never merged again. Every operation decreases active
order by one; continue until it is zero. Select pairwise incomparable
forest nodes as the final bags, allowing retired roots and nodes from
different stages. Use **all original contacts**, including those lost
from the active quotient on retirement. The original preimages are
connected and disjoint, so this contact graph is a minor after deleting
unused vertices. The existential target permits choosing retirements,
ties and final nodes; success for every choice is not assumed.

This admits every induced subgraph of every intermediate quotient and
avoids permanently losing useful bags through a later contraction.
Merely inspecting full quotients misses a clique diluted by isolates.
The [sharp order barrier](../barriers/quantitative_density_contraction_order.md)
also forces a long interval before independence first decreases, despite
arbitrarily large surplus. Its explicit batch crosses that interval.
The global density construction remains unproved.

**Private neighbours; written deduction.** Suppose the candidate forest
has no selectable minor of independence ratio greater than r. At a
minimum-codegree merge uv in its current quotient H, put

```text
c=|N_H(u) intersect N_H(v)|,
p_u=|N_H(u)-N_H[v]|,       p_v=|N_H(v)-N_H[u]|.
```

Then `c+1<=r+(r-1)min(p_u,p_v)`. Indeed every vertex in `H[N(u)]`
has degree at least c there. An independent set in that neighbourhood
has at most `d_H(u)-c=p_u+1` vertices. Its induced ratio is at most r,
so `d_H(u)<=r(p_u+1)`, giving the inequality; exchange u,v as well.
In particular, merging a universal vertex costs at most r edges.
An expensive merge therefore has private neighbours on both sides.

**Exact remaining charge.** Each merge loses precisely `c+1` active
edges; retirement loses the bag's current degree. These losses sum to
`e(G)`, and the total number of operations is `|G|`. All retirements
and merges costing at most r therefore contribute at most
`r|G|<=r^2 alpha(G)`, since the original leaf selection also has ratio
at most r. It would suffice to bound the expensive merges' cost by
`C r^2 alpha(G)` for one permissible history without a successful
selection. This bound is unproved. Private-neighbour counts alone do not
supply it: the same original vertices can occur in many such counts.
Any charge must retain actual preimages or provide a justified exchange.

**Uniform allocation is refuted under the no-success hypothesis alone.**
Set `b=r^2 alpha(G)/|G|>=r`. Paying at most b per operation costs at
most `r^2 alpha(G)`; assigning the remaining merge losses to original
vertices with capacity b would give the desired total bound. But the
[connected padding construction](../barriers/quantitative_uniform_allocation.md)
has no successful minor and a permissible history in which demand
`Omega(N^2)` is supported on N original vertices of total capacity
`o(N^2)`. This still fails when child preimages are eligible, capacities
are computed per original connected component, or b is multiplied by
any fixed constant. The first false step is inferring a minor from this
allocation deficit. The examples satisfy `e(G)<r^2 alpha(G)`; they do not
refute extraction under density surplus, or an existential history choice.

**A tested repair still lacks a decreasing step.** Let I be a maximum
independent set in G. For every vertex set W,
`alpha(G[W])<=|I intersect N_G[W]|`: an independent set in W can replace
the I vertices in its closed neighbourhood. Give each I vertex capacity
`Dr^2`. For each merge or retirement, retain distinct original edge
representatives of the active edges lost at that operation. For merge
losses, retain one representative of each coalesced pair as the surviving
edge and charge the other. Let W_t contain the complete preimages of
every bag meeting a charged edge, and allow the operation's loss to use
`I intersect N_G[W_t]`.

A capacitated Hall deficit for operations X gives, with
`W=union_(t in X) W_t`,

```text
e(G[W]) >= sum_(t in X) loss_t
         > Dr^2 |I intersect N_G[W]| >= Dr^2 alpha(G[W]).
```

If W is proper, induction for the density target applies to G[W]: r and
the order cap are retained, order strictly decreases, and every minor
lifts by inclusion with the same connected disjoint bags. There are no
root or colouring constraints in this target. If W is the entire host,
the inequality only repeats the original surplus. Neither a minimal
deficient collection nor maximising `e(H)/alpha(H)` over induced H proves
that W is proper. This repair therefore supplies no complete induction;
the spanning case still needs an actual minor construction. The allocation
is not a new target or a necessary form of every successful construction.

On an interval of constant independence number, a maximum independent
set in its last quotient has representatives in distinct anticomplete
bags throughout the interval. This witness need not extend through an
independence decrease: in `K4-ab`, contracting the minimum-codegree edge
ac gives K3, whose singleton maximum set at the fourth vertex cannot
extend to the earlier unique maximum set `{a,b}`. No nested choice or
exchange across intervals is proved. Nor does adding two apex vertices
justify changing an all-minor ratio bound r to `r-2`.

**Finite laboratory only.** The deterministic
[probe](quantitative_density_contraction_probe.py) checks eight cases:
five genuine `D=1` surplus inputs, one positive control and two negative
controls. It returns six verified models; three surplus inputs are
handled by deletion alone. This implementation inspects minimum-degree
deletion prefixes and may prune to an r-core before contracting, which
fits the degree-restricted retirement rule. Higher-degree deletion
prefixes are inspected as possible outputs, not performed in the history.
The probe does
not enumerate all forest-node selections or prove their existence.
Every output includes the original graph and model hashes and explicit
bags, checked for connectivity, disjointness and exact contacts. Run
`uv run python3 active/quantitative_density_contraction_probe.py`; expected
final line: `PASS: 8 finite cases; 6 verified models; 2 negative controls.`
The negative controls are forests and K3,3, whose minors have ratio at
most two and four respectively. No improved global theorem follows from
the experiment or these deductions.

## Simultaneous connected components

**Written deductions and finite laboratory; universal extraction unproved.**
The proposed unequal-clique test has a shortcut. In a complete join of
cluster parts, let r be the sum of their largest clique orders. Retain
one such clique per part, giving K_r. If two parts have further cliques,
one spare vertex from each forms an edge whose contraction gives a full
extra bag, hence K_(r+1). Otherwise, writing s for the repeated part's
largest clique and R=r-s, its order M is at most `alpha(G)s`, and
`e(G)<=M((s-1)/2+R)+R(R-1)/2<=alpha(G)r(r-1)/2`.
Thus every genuine surplus input in this family has a one-edge solution.
It cannot validate the missing simultaneous construction.

The new laboratory assigns q independent uniform labels to all original
vertices and contracts each maximal connected monochromatic component.
Select any subcollection of these components using all original contacts.
The bags are disjoint and connected without a size bound; labels are
auxiliary, not a proper colouring of G. This is a direct model construction,
not a decreasing induction. No success probability is proved.

Every resulting quotient is q-colourable. Conversely, every minor model
whose full contact graph is `(q-1)`-colourable can be represented: properly
label that contact graph and give every unused vertex one reserved label.
Bags of the same label are anticomplete, so each remains a maximal
monochromatic component. Colourability of a target obtained by deleting
contact edges is insufficient.
Consequently existential labelling alone largely reformulates the minor
problem; fixing q also imposes an additional output-colouring restriction.
A density-based choice or probability bound, with valid component
selection, is the missing theorem.

**Exact event and failed estimate.** For fixed nonempty, connected,
pairwise anticomplete sets `C_1,...,C_k`, put `U=union C_i`. The probability
that all C_i are whole monochromatic components is

```text
q^(-|U|) sum_(sigma in [q]^k)
  product_(x in N(U)-U)
    (1-|{sigma_i : x has a neighbour in C_i}|/q).
```

For each assignment sigma, all vertices of each C_i must take its label;
each outside neighbour must avoid the distinct adjacent labels. Outside
choices are independent conditional on sigma. Different C_i may share
a label, so their boundary exclusions cannot be multiplied independently.

Choosing an induced graph minimal for density surplus does not close this
estimate. For every such U, minimality gives
`e(G)-e(G-N[U])>Dr^2 alpha(G[U])`: the residual has independence at most
`alpha(G)-alpha(G[U])`, and satisfies the density bound if nonempty.
The first unsupported inference is replacing this incident-edge cost by
distinct forbidden-label events. Edges from N(U)-U to farther vertices
contribute to the cost but no additional factor in the displayed product.
Their endpoints' components and the total component count must be handled
jointly. This inequality supplies no new induction or extraction theorem.

**Three fixed tests.** The [component probe](quantitative_component_label_probe.py)
checks explicit r-colourings, so neither surplus input admits a
deletion-only solution. For the planted graph, 36 independent six-vertex
classes have cross-edges sampled with probability 0.6 and seed zero;
complement-clique enumeration gives its exact independence number.
For `Q4[K32]`, one vertex from each fibre over a cube shore gives an
independent eight-set; a perfect matching of the cube partitions the host
into eight cliques, proving independence eight. The one-sum control has treewidth three,
so every minor is four-colourable and has independence ratio at most four.

| Host | Order | Edges | Independence | r | Labels q; seed | Verified clique minor |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| Planted graph | 216 | 13,630 | 9 | 36 | 54; 0 | K47 |
| Q4[K32] | 512 | 40,704 | 8 | 64 | 96; 1 | K65 |
| Two K4s joined at one vertex | 7 | 12 | 2 | 4 | 6; 3 | K4 |

Both positive inputs satisfy the order cap and `D=1` surplus. For the
cube input, selecting from all components gives clique number 65; allowing
every tie choice among largest components of each label gives only 52.
The successful model includes singleton bags and has maximum bag size
thirteen. This comparison concerns clique numbers, not all attainable
independence ratios. It justifies retaining small components in this test,
not a universal selection rule.

Run `uv run python3 active/quantitative_component_label_probe.py`; the final
line is `PASS: 3 finite cases; 2 verified surplus models; 1 negative control;
10 clique-search cross-checks.` The script emits explicit bags and graph/model
hashes, checks every contact in the original host, and cross-checks its exact
clique search on ten small graphs. These finite certificates prove neither
the density target nor its colouring consequence.

## Direct critical reduction: neighbourhood constraint and failed repairs

**Written deduction; no case of R is closed.** Let G be minor-minimal
q-chromatic, with `h(G)<=r` and integers `q>=2r>=4`. Then, for every v,

```text
d(v)-alpha(G[N(v)]) >= T := 2q-2r-1.
```

Choose a maximum independent set S in N(v) and contract the star
`{v} union S`. This is a proper minor; give it a `(q-1)`-colouring in
which the merged vertex has colour zero. Expanding S with colour zero
gives a proper colouring of G-v: every outside neighbour of S avoids
zero. On N(v), precisely S has colour zero, since every other neighbour
of v sees the merged vertex. Criticality forces each of the other q-2
colours to occur on N(v)-S. At least `2(q-2)-(d(v)-|S|)` occur once.
If `d(v)-|S|<=T-1`, select 2r-2 such singleton roots. The Kempe argument
from the earlier degree proof gives paths between every pair across an
equal bipartition. These paths avoid S and v; their colour projection
is a scheme with all selected roots retained. Bipartite contractibility
gives a rooted `K_(r-1,r-1)`, and r-2 cross-pair contractions give K_r.
Adding the original singleton v gives K_(r+1), a contradiction. All bags
are disjoint in the original host; no induction or quotient-class closure
is asserted by this deduction.

**Correction to the proposed low-degree case.** In R, the induced
independence bound gives `alpha(G[N(v)])>=d(v)/r`. Consequently

```text
d(v) >= rT/(r-1),       d(v)-T >= d(v)/r > q/(6r).
```

The last inequality follows already from `d(v)>=q-1`. Thus the proposed
band `d(v)<=T+q/(6r)` is empty. Splitting a fractional 2r-colouring into
independent sets of size at most `ceil(n/r)` does give total weight at
most `2r+n/ceil(n/r)<=3r`: first trim to unit vertex coverage, then split
each class into pieces, preserving that coverage. The ensuing conditional
band calculation was arithmetically valid, but was incorrectly interpreted
as a substantive case closure. It is not promoted as a result.

More generally, for every independent centre set I,
`|N(u) intersect I|<=alpha(N(u))<=d(u)-T`. Hence the earlier centre-incidence
bound alone can never certify an untouched vertex's degree below T.
Actual extra coalescence remains possible. Using a stronger threshold for
the next critical minor requires a fresh estimate; it is not ruled out.

**Attempted joint degree accounting; global gain unproved.** For the
nontrivial maximal-star bags B_i, put `W=union B_i`, `A=V(G)-W`, and let
H be their simultaneous quotient. Define

```text
D_* = sum_i d_H([B_i]),
C_A = sum_(i,u in A) (e_G(B_i,{u})-1)_+,
C_B = 2 sum_(i<j) (e_G(B_i,B_j)-1)_+.
```

Counting edges incident with W gives the exact identity
`sum_(x in W) d_G(x)=D_*+C_A+C_B+2 sum_i e(G[B_i])`.
Here C_A is the total degree loss at untouched vertices. Small coalescence
therefore leaves degree on the merged vertices. But these vertices need
not stay independent or survive the subsequent critical minor. Deleting
one costs one further quotient vertex while discarding many edges; its
original bag size has already been paid for in the star order loss.
No sufficient charge for such deletions, or critical-minor choice retaining
the vertices, is proved. At the baseline star order loss `nq/r^2`, an
edge contribution of scale `nq^2/r^2` gives only the old order scale when
divided by q. Division by r would assume the missing gain.

Replacing degree by `d(u)-alpha(N(u))` also lacks a valid monotonicity
step: contractions elsewhere can lower neighbourhood independence while
u survives as a singleton. Retaining particular independent neighbours
instead creates shared ownership costs, with no disjoint charge proved.
These failed repairs refute no graph theorem; R and its consequence remain
open. Multiple rounds must pay their actual colour losses.

For a batch consisting only of star contractions with independent leaves,
let E contain every original preimage of a selected centre. Each final
bag B has B-E independent: when an original edge first becomes internal,
at least one end lies in that round's centre preimage. Thus
`chi(G)<=chi(H)+chi(G[E])`. If `chi(G[E])<=s` for an integer `s>=1`, assign each non-E vertex
in a nontrivial bag to an adjacent E vertex in that bag. The s independent
classes of E partition these original independent-leaf stars. Writing L
for their total leaf count and D for the batch's order loss, `D<=L+|E|`.
One class supplies at least L/s leaves, or deleting a class removes at
least `|E|/s` vertices. One original one-colour operation therefore removes
at least `D/(2s)`. This may discover a better packing, but low-colour
accounting alone does not prove its size. No bound on `chi(G[E])` is
proved; arbitrary intervening critical-minor deletions are not covered.

The component-label experiment remains a control, not a leading proof
mechanism. Its cube input already has a K128 minor: in a Q3 face with
binary labels 0,...,7, the pairs 01,26,37,45 form a K4 model. Taking each
pair separately at each of the 32 clone indices gives 128 disjoint
two-vertex bags with every contact. The recorded K65 is a valid certificate,
but supplies little evidence for universal extraction.

## Construction selection: preserving chromatic number

**Written deduction; R remains unproved.** Let r>=2 and p>=2r be integers,
let `chi(H)=p`, `h(H)<=r`, and let u be nonisolated. Put
`tau_H(u)=d_H(u)-alpha(H[N_H(u)])`. If
`tau_H(u)<=2p-2r-2`, then contracting the star B consisting of u and a
maximum independent set S in its neighbourhood retains at least p colours.
Indeed, a `(p-1)`-colouring of H/B would give at least 2r-2 singleton
neighbour colours by the preceding neighbourhood argument. Its rooted
bipartite scheme and the original u would give K_(r+1), a contradiction.
The star is nontrivial because S is nonempty. Isolated vertices can first
be deleted without changing p.

Start with G as in R with `q>=2r+1`, delete a nonempty independent set I,
and put p=q-1.
Then `chi(G-I)=p`: fewer colours would extend to G with one fresh colour,
and proper-minor colourability supplies the upper bound. While the displayed
low-tau condition holds at a nonisolated vertex, its star contraction
retains exactly p colours, since every minor of G-I is p-colourable.
Delete isolated vertices as necessary. Every operation strictly decreases
order; the independence hypothesis persists and fixed connected preimages
lift all further minors. This is a valid reduction to a state with no such
vertex, not a lower bound on the accumulated order loss required by R.

**Exact local changes and failed charge.** Induced vertex deletion cannot
increase tau at a surviving vertex. For a connected bag B avoiding u, put
`k=|N_H(u) intersect B|`. If k is positive, contraction lowers its degree
by k-1 and can lower neighbourhood independence by at most k, so tau rises
by at most one; if k=0 it is unchanged. If `H[N_H(u) intersect B]` has an
edge, a maximum independent witness loses at most k-1 vertices, so tau
cannot rise. For a star with maximal independent leaves S, every untouched
neighbour of its centre sees both the centre and a leaf. Therefore positive
changes occur only at neighbours of S outside the centre's closed
neighbourhood.

The [explicit maximum-star counterexample](../barriers/quantitative_neighbourhood_cover_charge.md)
shows that this restriction does not bound the total change by a constant
times r times the order loss, even with the order cap and all-minor
independence bound. The example has a much better star at another centre
and lacks the required chromatic gap. It refutes a uniform charge for
arbitrary maximum-leaf stars, not an existential favourable choice in R.

Under R's inherited independence bound, choosing S globally largest gives
only a quadratic bound: every neighbourhood has independence number at most
`M=|S|`, hence degree at most rM. At most `r M^2` untouched vertices can
increase tau. That star need
not have a low-tau centre or preserve p colours. Neither a stronger charge
nor an exchange selecting a chromatic-preserving large star is proved.

**Other tested operations; no quantitative gain.** Contracting a connected
induced bipartite bag loses at most one colour, but deleting its larger
independent shore retains q-1 colours and achieves at least half its order
loss. An induced odd cycle of length 2k+1 likewise has an independent
k-set, compared with contraction loss 2k. If its quotient is only
`(q-2)`-colourable, every cycle vertex must meet every nonmerged colour:
otherwise use a missed colour there, and colour the remaining path with
the merged colour and one fresh colour to `(q-1)`-colour G. This saturation
does not supply connected exterior bags or a larger deletion. Neither
proposal, nor the low-tau iteration, has qualified for a renewed R campaign.
