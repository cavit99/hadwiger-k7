# Cold self-audit: exact-defect regular elimination

**Verdict:** **GREEN**, subject to the displayed finite trust boundary.
The order-25 elimination, the connected-full hexagonal local conclusion at
`D=25`, the pole-factor propagation, and the exclusion of the
`8^{25}9^2` distribution all follow from the stated hypotheses.  This is a
cold self-audit, not an independent audit or external peer review.

## 1. Audited revision and dependencies

The audited theorem is
[`hc7_k7minus_exact_defect_regular_elimination.md`](hc7_k7minus_exact_defect_regular_elimination.md)
at SHA-256

```text
0750a839063730f515f17868677e8fca546011e540e22180a4d990b7b468e6c0
```

The finite verifier and its reproduction note are:

```text
67fd89db3e97933a950dd1ad256c59141bfab3aec85ba8485014105981f20b95  active/experiments/defect25_regular_elimination/verify.py
e351db441c640b651a24d0966fba32b0f6bcf8802efb3ae0e72e324ee4158b67  active/experiments/defect25_regular_elimination/README.md
```

The pinned local inputs are:

```text
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd  results/hc7_k7minus_exceptional_neighbourhood_completion.md
26be60e5389ec356dfd183d8a39e2a713e6db3695c807674daf7797fa1fcae2b  results/hc7_k7minus_exceptional_neighbourhood_completion_audit.md
421544721b5084fe5dff280cd2299f0e4cb214ba39bc2b2fde5648fc393bcd83  results/hc7_k7minus_two_literal_k5_exclusion.md
4b482d74f6a70c5d00b3f29f261a53a91c48b75750975005fce06f150f69aa24  results/hc7_k7minus_two_literal_k5_exclusion_audit.md
ca51586f29412fc8f861ad8bb22c79cecf2f2c063060bc1d20e5d6b0459c0d71  results/hc7_order8_full_five_colour_reconfiguration.md
b15276f5a11b38dbe05f65f483b2e99223b0d2466eb58896c4367bea48fe1d87  results/hc7_order8_full_five_colour_reconfiguration_audit.md
```

The last core census is only a cross-check: the new verifier independently
checks the narrower order-eight classification used in the proof.

## 2. Distribution and contraction arithmetic

If the critical host has order twenty-five, the inequality

\[
 n_8\geq25+\sum_{i\geq10}(i-9)n_i
\]

forces all twenty-five vertices to have degree eight.  Thus `m=100` and
`D=9n-2m=25`.

For an edge of codegree `c`, contraction leaves twenty-four vertices and
`99-c` edges.  Seven-connectivity descends to six-connectivity.  The order
excludes either Jakobsen base graph, and six-connectivity excludes a
nontrivial four-clique-sum cockade.  Hence

\[
 2(99-c)\leq9\cdot24-25=191,
\]

so `c\geq4`.  For `H=G[N(z)]`, the degree of a neighbour `x` in `H` is
exactly the codegree of `zx`; therefore `\delta(H)\geq4`.  The audited
exceptional-neighbourhood theorem supplies `\alpha(H)=3` and literal
`K_4` exclusion.  No stronger local assumption is imported.

## 3. Finite quotient lemma

NetworkX's atlas contains exactly `1,044` unlabelled graphs of order seven.
Adjoining an eighth vertex with every one of its `128` possible
neighbourhoods is complete for order eight.  It may repeat isomorphism
types but cannot omit a graph or a marked vertex.  The verifier then tests
all eight possible equal misses and all twenty-eight unordered distinct
misses.  The two contracted exterior images are interchangeable, so these
thirty-six profiles are exhaustive when both have boundary order seven.

If either component image is full, delete one of its attachment edges so
that the two chosen misses are distinct.  This gives a tested spanning
subgraph.  A target minor in that subgraph remains a target minor after the
deleted attachment is restored.  Thus the `12,672=352\cdot36` exact-miss
tests cover all attachments of order at least seven.

The minor routine starts with singleton bags and recursively performs only
two operations: merge two touching bags or delete a bag.  Every generated
bag is connected.  Conversely, every family of disjoint connected branch
sets can be obtained by contracting spanning trees inside its bags and
deleting unused vertices.  At seven bags, at least twenty contacts are
equivalent to containing `K_7^-`; at five bags, ten contacts are equivalent
to a `K_5` model.  The positive and negative controls exercise both target
tests.

The rerun ended with

```text
GREEN defect25 regular elimination finite inputs: bases=1044 extensions=133632 eligible=352 exact_miss_profiles=12672 k5_minor_free=2 hexagonal=2; D26_static_survivor=GMs`KK misses=3,5
```

Thus two exterior components contradict target exclusion.  Contracting an
entire component preserves all of its literal boundary contacts, so the
host-to-quotient lift in Lemma 3.1 is valid.

## 4. Fullness and the unique neighbourhood

Once the exterior `C` is connected, seven-connectivity allows it to miss
at most one boundary vertex `r`.  In the regular layer, a miss forces `r`
to be adjacent to `z` and all seven other boundary vertices.  Deleting `r`
from `H` leaves a seven-vertex graph of minimum degree at least three.
It is triangle-free, since a triangle together with the universal `r`
would be a literal `K_4` in `H`.

If that seven-vertex graph has a vertex of degree at least four, its
triangle-free neighbourhood is an independent four-set.  Otherwise it is
cubic, contradicting parity of the degree sum.  Both alternatives conflict
with `\alpha(H)=3`, so the exterior is full.

A `K_5` model in `H`, together with `{z}` and the connected full exterior,
would give seven bags with only the `zC` contact absent.  Hence `H` is
`K_5`-minor-free.  The verifier finds only two eligible atlas-extension
representations without a `K_5` minor and checks both are isomorphic to
`C_6\vee\overline{K_2}`.  This proves the claimed unlabelled uniqueness.

## 5. Pole-factor propagation

In a hexagonal-bipyramid neighbourhood, the two poles have local degree
six and the six rim vertices have local degree four.  Codegree is symmetric,
so the codegree-six edges form a spanning two-factor `P` in the regular
graph.  The two pole neighbours at one vertex are nonadjacent, excluding a
triangle component of `P`.

For a pole edge `xy`, its common neighbours are precisely the six rim
vertices at either end.  Thus `x` and `y` have the same rim-neighbourhood,
which induces `C_6`.  Constancy propagates around a component of `P`.
It also proves:

1. no rim edge has both ends in one pole component; and
2. one rim edge between two pole components makes the two components
   completely adjacent.

Every pole component has order at least four, while a vertex has six rim
neighbours.  Hence it has a unique rim-adjacent pole component of order six;
symmetry makes its own order six.  Connectedness leaves one joined pair,
so the graph is `C_6\vee C_6`, of order twelve.  This contradicts the
assumed order twenty-five.  The propagation uses regularity exactly when
it applies the two-pole/six-rim decomposition at the other endpoint.

## 6. The mixed `8/9` layer

When `\tau=0` and `n_8=25`, one still has `D=25`.  At a degree-eight
centre, the preceding local proof remains valid.  A boundary vertex missed
by the exterior cannot have degree nine because all of its possible
neighbours lie in an eight-vertex closed-neighbourhood remainder; if it has
degree eight, the parity argument above applies.  Thus every degree-eight
centre has the connected-full hexagonal structure.

Let `P_B` retain pole edges with both ends in `B`.  A four-vertex path in
`P_B` has a common rim cycle.  For path vertices `a_0a_1a_2a_3` and cyclic
rim vertices `b_0,\ldots,b_5`, the seven bags

\[
 \{a_3\},\{a_0,b_0\},\{a_1,b_1\},\{a_2,b_2\},
 \{b_3\},\{b_4\},\{b_5\}
\]

are pairwise adjacent except for `{b_3},{b_5}`.  This directly verifies the
`K_7^-` certificate.  Therefore `P_B` consists of paths of order at most
three.  Each path sends exactly two pole edges out of `B`, so twenty-five
vertices require at least eighteen such edges.

If there were exactly two degree-nine vertices, their total degree eighteen
would be exhausted by these pole edges.  Equality gives nine pole paths and
no rim edge incident with either degree-nine vertex.  The possible path-order
multisets are `3^8,1` and `3^7,2^2`.  Rim adjacency between pole paths is
complete or empty, and the adjacent path orders at each path sum to six.
For `3^8,1`, the singleton must see two order-three paths; either such path
then needs five further neighbours as a sum of threes, impossible.  For
`3^7,2^2`, the equation `3u+2v=6` and the existence of only two order-two
paths prevent any order-three path from meeting an order-two path.  The two
order-two paths can then supply only two, rather than six, rim neighbours to
one another.  Degree-sum parity makes `n_9` even, so `n_9\geq4`.

No argument in the source excludes arrangements with four or more
degree-nine vertices.  The theorem therefore correctly stops short of
eliminating `\tau=0`.

## 7. Exact nonclosure and significance

At `D=26`, the contraction calculation gives only codegree at least three.
The verifier's cubic graph `GMs`KK`, with two contracted component images
missing vertices `3` and `5`, satisfies the corresponding local
neighbourhood conditions and has no `K_7^-` minor.  It is not asserted to
be a critical host; it shows only that the finite two-exterior inference
cannot be extended by lowering `\delta(H)` from four to three.

The work eliminates a complete order and degree-distribution layer and the
first mixed distribution above it.  That is broader than a response cube,
but it is not a colouring theorem, does not eliminate all `D=25` or
`\tau=0` hosts, and is not comparable in scope to Norin--Totschnig's main
theorem.
