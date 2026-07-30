# External-review dossier: the computation-free `K_7^-` density spine

**Status:** current specialist-review dossier; not a manuscript, novelty
claim, external peer review, proof of the `K_7^-` six-colour conjecture, or
proof of `HC_7`.

**Mathematical revision:** the exact audited source hashes in Section 2.
Any mathematical change requires renewed audits and replacement hashes.

This dossier is separate from the frozen
[bounded-interface review blueprint](hc7_partial_results_external_review_blueprint.md).
The authoritative project status remains
[`RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## 1. Candidate paper thesis

**Working title:** *Degree-seven rigidity, private-triangle allocation, and
critical seven-cut reflection without a `K_7^-` minor*.

The proposed note studies a hypothetical minor-minimal non-six-colourable
`K_7^-`-minor-free graph.  Its central chain is:

1. Every nonedge in a degree-seven neighbourhood yields a rooted `K_5` on
   the other five neighbours by a direct contraction--Kempe argument.
2. Consequently every degree-seven neighbourhood is exactly

   \[
       K_4\mathbin{\dot\cup}K_3
       \quad\text{or}\quad
       K_1\vee(K_3\mathbin{\dot\cup}K_3).
   \]

3. The graph contains at most two literal `K_5` subgraphs.
4. Degree counting and Jakobsen's theorem give `m>=4n-5`, `n>=19`, and two
   exact degree sequences at the first possible order.
5. Under the temporary critical-host equality assumption, the ten
   degree-seven vertices form two disjoint literal `K_5`s, the order is at
   least twenty-nine, either clique deletion is five-connected, and the
   private triangles satisfy exact overlap, bond, Hall, and edge-critical
   Kempe formulations.
6. A private-triangle Kempe allocation, reconstructed without the equality
   assumption, shows that no literal `K_5` has all five vertices of degree
   seven.  Hence `n_7<=8` and every hypothetical critical host has
   `m>=4n-4`; equality has degree sequence `7^8 8^{n-8}` and the exact
   two-clique structure stated below.
7. Independently, five disjoint connected subgraphs outside a seven-vertex
   boundary, each adjacent to every boundary vertex, already force
   `K_7^-`.  Thus every order-seven cut has at most four components;
   in the four-component case every nonsingleton component is two-connected.
   Exact surplus and connectivity formulas characterize every
   whole-component contraction.  Under the no-proper-descent hypothesis, a
   density-eligible contraction that fails has an explicit deletion
   certificate.
8. In the actual minor-minimal non-six-colourable host, exact boundary-
   colouring reflection improves the maximum packing and component count to
   three, eliminating the four-component case.  With three components the
   boundary is exactly three-chromatic, and every proper three-colouring has
   colour-class sizes `3,2,2`.
9. Combining the density defect with `n_7\le8` forces at least seven
   exceptional degree-eight vertices.  If there are exactly seven, the
   degree sequence, the two literal `K_5`s, parity, and order are rigid.
10. Every exceptional neighbourhood has independence number exactly three.
    For any resulting independent triple, a five-root `K_5` model that
    avoids one exterior component already completes to an explicit
    `K_7^-`-minor model.
11. In the two-component exterior case, common missed attachments are
    impossible.  The remaining nonfull cases reduce to exact order-seven
    cut residues, while the both-full case reduces from 2,076 exceptional
    neighbourhoods to seven boundary types with full-packet vector
    `(1,1,1)`.  These last classifications are computer-assisted and do not
    prove shore allocation.

The note must not claim the global `4n-4` extremal target, a standalone bond
or two-full-transversal theorem, the `K_7^-` six-colour conjecture, or
`HC_7`.  In particular, the equality exclusion uses one permitted missing
branch-set adjacency; it does not prove that two disjoint connected
subgraphs each meet all five private triangles.

## 2. Exact theorem package

### Uniform rooted `K_5` and exact degree-seven neighbourhoods

- [Theorem](../results/hc7_k7minus_degree7_clique_incidence.md)
- [Internal audit](../results/hc7_k7minus_degree7_clique_incidence_audit.md)
- Theorem SHA-256:
  `04e085032a096ef3fd508ca4ee287ef82417a718ae3d95646ae4cbd0b911ed2e`

This theorem replaces the earlier anti-neighbourhood, matching-language,
aligned near-`K_7`, and 129-graph residual chain.  None of those results is
a logical dependency of the present theorem.

### At most two literal `K_5` subgraphs

- [Theorem](../results/hc7_k7minus_three_clique_bound.md)
- [Internal audit](../results/hc7_k7minus_three_clique_bound_audit.md)
- Theorem SHA-256:
  `5b5e399122b996186e861f5075e7808c8e6fe4353082256ee12d5074499d2574`

The overlap-four branch gives `K_7^-`; the remaining branch invokes
Niu--Zhang Theorem 1.10 to obtain `K_7`.

### Density, order, and exceptional degree-eight vertices

- [Theorem](../results/hc7_k7minus_five_exceptional_vertices_reduction.md)
- [Internal audit](../results/hc7_k7minus_five_exceptional_vertices_reduction_audit.md)
- Theorem SHA-256:
  `604d11d4276ce6a3c57a8375d702624a1c364b5123f122b7e9e3dc18d11bf8f4`

The proved conclusions include `m>=4n-5`, `n>=19`, the two order-nineteen
degree sequences, and at least five degree-eight vertices lying in no
literal `K_5`.  The last conclusion is retained as structure, not as the
current main finishing target.

### Equality connectivity, order, and Kempe structure

- [Theorem](../results/hc7_k7minus_equality_connectivity_reduction.md)
- [Internal audit](../results/hc7_k7minus_equality_connectivity_reduction_audit.md)
- Theorem SHA-256:
  `9a3e167b4b5be1d1ff9dbafb16a0e7ed6130fc58ad947603a246fa5022c88307`

The proof gives five-connected clique deletions, a three-connected central
graph, cross-matching order at most three, order at least twenty-nine, the
bond and Hall formulations, and the edge-critical common-spine Kempe fork.
It does not give the stronger, formerly targeted two disjoint connected
transversals.

### Equality exclusion and strict critical-host density

- [Theorem](../results/hc7_k7minus_equality_kempe_exclusion.md)
- [Internal audit](../results/hc7_k7minus_equality_kempe_exclusion_audit.md)
- Theorem SHA-256:
  `127bdbbf35c7048e93ac042c306165d85b348ae0b40c688fe953afd8ab17edc6`

The symmetric `p`- and `q`-component argument excludes both outcomes of the
equality theorem's Hall dichotomy.  It proves that no critical host in the
displayed package has `m=4n-5`, and hence strengthens the critical-host
lower bound to `m>=4n-4`.  Its explicit minor models need only one connected
set to meet all five private triangles; the other may miss one.  Thus it
does not prove a standalone bond theorem or the existence of two disjoint
connected subgraphs each meeting all five private triangles.

### All-degree-seven clique exclusion and the tight layer

- [Theorem](../results/hc7_k7minus_all_degree7_k5_exclusion.md)
- [Internal audit](../results/hc7_k7minus_all_degree7_k5_exclusion_audit.md)
- Theorem SHA-256:
  `e2e5f5dc6c4456413e306c7844771157c5f3d9663553c1170e33a298a8148bf5`

The private-triangle theorem uses no density equality, Hall theorem,
five-connected clique deletion, or finite classification.  It excludes an
all-degree-seven literal `K_5`, proves `n_7<=8`, and gives `m>=4n-4`
directly.  At equality the degree sequence is `7^8 8^{n-8}`; exactly two
literal `K_5`s cover the degree-seven vertices, each contains four of them,
the cliques are disjoint or share their degree-eight vertex, and `n>=21`.

### Seven exceptional vertices and exact equality structure

- [Theorem](../results/hc7_k7minus_seven_exceptional_vertices_corollary.md)
- [Internal audit](../results/hc7_k7minus_seven_exceptional_vertices_corollary_audit.md)
- Theorem SHA-256:
  `5cf181ca631ba0e4f6f5235ca4357faac5bdcce3acde5ba8e83dde0e05e1a388`

If `b` counts exceptional degree-eight vertices and
`tau=sum_{i>=10}(i-9)n_i`, the theorem proves

\[
                         b\ge15-n_7+\tau\ge7+\tau.
\]

The exceptional-vertex subgraph is `K_5`-free.  At `b=7`, the exact degree
sequence is `7^8 8^9 9^{n-17}`, the two literal `K_5`s are disjoint with
degree pattern `7^4 8^1`, `2m=9n-25`, the order is odd, and `n>=21`.

### Exceptional-neighbourhood independent triples and exterior completion

- [Theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
- [Internal audit](../results/hc7_k7minus_exceptional_neighbourhood_completion_audit.md)
- Theorem SHA-256:
  `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd`

Every exceptional degree-eight vertex `u` has
`alpha(G[N(u)])=3`.  The independence-number-at-most-two argument invokes
Rolek--Song--Thomas Lemma 2.1 and then gives an explicit seven-bag
`K_7^-` model for every possible missed exterior attachment.  If
`I\subseteq N(u)` is an independent triple and `R=N(u)-I`, any
`R`-rooted `K_5` model in `G-({u}\cup I)` that avoids a component of
`G-N[u]` likewise completes to `K_7^-`.  A
[retained finite verifier](../results/hc7_k7minus_exceptional_neighbourhood_completion_verify.py),
at SHA-256
`5eb316169563208269c887775376dea9d4b853201a2458f9b604b23ea6017ad0`,
checks the order-eight input and all nine explicit near-full attachment
models; it is an independent cross-check, not a proof dependency.

### Nonfull two-component attachment reduction

- [Theorem](../results/hc7_k7minus_nonfull_attachment_reduction.md)
- [Internal audit](../results/hc7_k7minus_nonfull_attachment_reduction_audit.md)
- Theorem SHA-256:
  `2b269e7ecea09f695991689e2a6db64d928aedb141ea8cfbf85d14f84fc70617`

Two exterior components cannot miss the same neighbour.  With exactly one
nonfull component, the resulting order-seven cut has packing vector
`(1,2)`; its boundary obeys the stated edge, connectivity, clique,
independence and minor restrictions, while the missed vertex has at most
four boundary neighbours and at least two neighbours in the full exterior
component.  A retained exact census leaves 28 unlabelled boundary types.
Distinct misses give two connected-rich `(1,2)` cuts or the exact pair of
overlapping `(1,1)` cuts described in the theorem.

The [retained verifier](../results/hc7_k7minus_nonfull_attachment_reduction_verify.py),
at SHA-256
`d0414ca3171f9a29e78030874eaa61c5c8b7f2e0d0650c0b866654d56e82bee3`,
independently reproduces the 28-code digest and all reported spectra.  The
host reduction is written; the finite census classifies possible literal
boundaries and does not assert their host realisability.

### Both-full shore and packet reduction

- [Theorem](../results/hc7_k7minus_both_full_shore_reduction.md)
- [Internal audit](../results/hc7_k7minus_both_full_shore_reduction_audit.md)
- Theorem SHA-256:
  `8aa99a023ae2247dd24835a158c17677d1e3da218c9a431be36891e54119b758`

The written diamond-deletion lift reduces the exceptional order-eight
boundary to 15 types; the audited three-full-component theorem removes
eight, leaving seven.  Their minimum reserve graphs are `P_5`,
`P_3` disjoint-union `K_2`, or `2K_2` disjoint-union `K_1`.  Actual
star-contraction responses on the six- and seven-demand types must remain
mixed between the shores, and packet completions force each exterior
full-subgraph packing number to equal one.

The [retained verifier](../results/hc7_k7minus_both_full_shore_reduction_verify.py),
at SHA-256
`168c56fdeb52c9835f95796750c82a0c06dfcad7781ca4a9a07affdfab07eb2f`,
reproduces the full census, both certificate digests and every reserve
shape.  The result does not construct a shore-confined rooted `K_5^-`.

The adjacent [scoped barriers](../barriers/hc7_k7minus_shore_allocation_barrier.md)
and [audit](../barriers/hc7_k7minus_shore_allocation_barrier_audit.md), at
source SHA-256
`e6d3bf5c480ad3775de530014aa70f2bb1e32c880e64af45a3087e30d93acee9`,
show that static boundary labels can remain balanced for all 15 types and
that fullness plus minor exclusion alone is insufficient.  Their mechanism
witness lacks seven-connectivity and criticality and therefore does not
refute the host target.

### Seven-boundary connected-subgraph capacity and contraction criteria

- [Theorem](../results/hc7_k7minus_seven_boundary_component_descent.md)
- [Internal audit](../results/hc7_k7minus_seven_boundary_component_descent_audit.md)
- Theorem SHA-256:
  `9e2f616c98dd17670f4d15e962f3b36e4fc1f4c4dc9aee4227eabeb51ca33913`

This theorem strengthens the earlier audited seven-cut result.  It proves
that at most four disjoint connected subgraphs outside the boundary can each
be adjacent to all seven boundary vertices, removes the former
five-component case, proves that four-component interiors are singletons or
two-connected, and gives
the exact density and seven-connectivity criteria for simultaneous whole-
component contraction.  It does not prove that a qualifying contraction
always exists.

Its `p=2,3,4` join constructions use the earlier
[seven-cut theorem](../results/hc7_k7minus_seven_cut_contraction.md) and
[audit](../results/hc7_k7minus_seven_cut_contraction_audit.md), at exact
theorem SHA-256
`bbb9919b6d04c08836526d017607d318323fe457baa75d4c3364be85a4ad1ff5`.

### Critical seven-cut capacity and three-component boundary

- [Theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md)
- [Internal audit](../results/hc7_k7minus_critical_seven_cut_capacity_audit.md)
- Theorem SHA-256:
  `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34`

The theorem gives a self-contained exact boundary-colouring reflection
argument for the critical host.  It improves the maximum boundary-full
connected-subgraph packing number from four to three and consequently
excludes four-component seven-cuts.  If three components remain, each has
packing number one, the boundary is exactly three-chromatic, and every
proper three-colouring has class sizes `3,2,2`.  For two components, one has
boundary-full packing number one, their packing numbers sum to at most three,
and the boundary has an edge.

The capacity-three conclusion and four-component exclusion overlap older
audited exact-seven packing and adaptive reflection results.  The new
deduction from the present `K_7^-` boundary theorem is the exact
three-component chromatic conclusion.  Proper-minor six-colourability is
essential, so this does not exclude four-component cuts in arbitrary
seven-connected graphs or prove the bare extremal theorem.

## 3. Dependency and trust map

```text
criticality + Dirac + Kriesell--Mohr + Mantel
└─ uniform rooted K5 for every neighbourhood nonedge
   └─ exact degree-seven neighbourhoods
      └─ private triangles and degree-seven clique incidence

Niu--Zhang
└─ at most two literal K5s

exact neighbourhoods + two-K5 bound + Jakobsen/Albar
└─ density, order nineteen, and exceptional vertices
   └─ equality bookkeeping and connectivity
      ├─ order at least twenty-nine
      ├─ bond, Hall, and edge-critical Kempe formulations
      └─ symmetric Kempe-component allocation
         ├─ explicit K7-minus models in both Hall branches
         ├─ exclusion of the 4n-5 critical-host equality layer
         └─ critical-host density at least 4n-4

exact neighbourhoods + two-K5 bound + private-triangle Kempe allocation
├─ no all-degree-seven literal K5
├─ at most eight degree-seven vertices
└─ critical-host density at least 4n-4 with exact tight-layer structure

density defect + at most eight degree-seven vertices
└─ at least seven exceptional degree-eight vertices
   └─ exact b=7 degree, clique, parity, and order structure

proper-minor six-colourability + non-six-colourability
└─ every exceptional neighbourhood has independence number at most three

exceptionality + K7-minus exclusion + Rolek--Song--Thomas Lemma 2.1
+ order at least nineteen + seven-connectivity
└─ explicit K7-minus model excludes independence number at most two
   └─ every exceptional neighbourhood has an independent triple
      + seven-connectivity + rooted K5 avoiding an exterior component
      └─ explicit K7-minus exterior-completion model

two exterior components + critical seven-cut capacity
├─ common missed attachment is impossible
├─ every nonfull attachment reduces to exact (1,2) or overlapping (1,1) cuts
└─ one-nonfull boundary census: 28 possible types

two full exterior components + diamond-deletion lift
└─ 15 boundary types
   + three-full-component theorem
   └─ seven exact types
      + dynamic demand and packet completions
      └─ full-packet vector (1,1,1)

seven-connectivity + elementary minor constructions + Mader bounds
└─ capacity of boundary-full connected subgraphs at most four
   ├─ sharpened seven-cut boundary and interior restrictions
   └─ exact whole-component density/connectivity contraction criterion

proper-minor six-colourability
└─ exact boundary-colouring reflection
   + capacity at most four + non-six-colourability
   ├─ critical-host capacity at most three and no four-component cut
   └─ three components: boundary chromatic number three, classes 3,2,2
```

No computer-assisted finite classification is load-bearing in the central
density chain through `m>=4n-4`.  The two-component shore reductions do use
the separately identified order-seven and order-eight finite boundary
classifications.  The audits are internal checks and must not be described
as independent human review or external peer review.  The bond formulation
in the equality theorem is an equivalent target inside the now-excluded
equality host, not a proved standalone bond or two-full-transversal theorem.

## 4. Open statements and ordered next attacks

The strengthened critical-host density makes the following the current
density-only sufficient extremal statement:

> Every seven-connected `n`-vertex graph with at least `4n-4` edges contains
> a `K_7^-` minor.

The equality-host two-transversal problem is no longer a finishing target:
the new Kempe allocation excludes every such critical equality host without
producing two full transversals.  It must not be promoted to the standalone
statement

> Every five-connected graph with five specified disjoint triangles has a
> bond meeting every triangle, or two vertex-disjoint connected subgraphs
> each meeting every triangle.

No theorem of that form is proved here.

The all-degree-seven extraction is complete.  The remaining positive bare-
extremal target is the seven-cut reduction statement:

> If a seven-connected graph `G` has `m>=4n-4` and an order-seven cut, then
> `G` contains a `K_7^-` minor or has a proper seven-connected minor `H` with
> `|E(H)|>=4|V(H)|-4`.

Together with minor minimality and the easy eight-connected case, this would
prove the bare extremal theorem and hence the `K_7^-` six-colour conjecture.
Conversely, the bare theorem immediately supplies the first outcome, so this
dichotomy is headline-equivalent rather than a routine preliminary lemma.

The general attack removed `r=5`, reduced every whole-component descent to
an exact surplus inequality and deletion-connectivity test, and proved that
all nonsingleton components in the `r=4` case are two-connected.  The
critical-host reflection attack now removes `r=4` altogether.  The next
critical-host attack should therefore treat the exact `r=3` form: three
packing-one components and a three-chromatic boundary whose proper
three-colourings all have class sizes `3,2,2`.  Then comes the likely hard
`r=2` case with one component of boundary-full packing number one and a
nonempty `K_5`-minor-free boundary.  Every successful critical-host case must
produce an explicit
minor model or compatible component-side six-colourings, contradicting
seven-chromaticity.

The bare extremal route still contains an `r=4` case because its arbitrary
seven-connected host lacks the proper-minor colouring hypothesis.  That
separate route may seek a threshold-preserving descent but cannot use the
critical theorem's three-component normal form.  No simultaneous
chromatic-critical and density-descent minimality reduction is proved here.
Counterexamples to intermediate lemmas are falsification checks and pivot
signals, not a successful endpoint.  A normalized Norin--Totschnig
near-`K_7` upgrade remains the higher-risk fallback.

The parallel critical-host-specific finishing target is:

> Every graph in the displayed critical package has at most six
> exceptional degree-eight vertices.

This would contradict the proved lower bound of seven and settle the same
six-colour conjecture.  It is not proved.  The current
[technical frontier](hc7_k7minus_seven_exceptional_frontier.md) reduces the
positive route to exterior allocation: at an exceptional centre, construct
a five-root `K_5` model that avoids one exterior component, or leave a
connected residual subgraph adjacent to the independent-triple star and at
least four rooted bags.

The adjacent two-component attack has now completed the proposed split.
The separately audited
[nonfull reduction](../results/hc7_k7minus_nonfull_attachment_reduction.md)
excludes a common missed neighbour and converts every other nonfull
configuration into exact `(1,2)` or overlapping `(1,1)` seven-cut residues.
In the one-nonfull cell it additionally bounds the missed vertex to at most
four boundary neighbours and forces at least two neighbours in the full
exterior component; a retained exact census leaves 28 boundary types.
The separately audited written-and-computer-assisted
[both-full reduction](../results/hc7_k7minus_both_full_shore_reduction.md)
uses a retained verifier and an unbounded diamond-deletion lift to leave
seven boundary types, each with exterior full-packet vector `(1,1)`.
It does not prove a one-shore rooted model.  The exact next input is
compatibility among changing proper-minor colourings or an additional
residual contact inside one packet-one shore; the
[scoped boundary barriers](../barriers/hc7_k7minus_shore_allocation_barrier.md)
rule out static demand counting as a proof.

The alternative seven-root list calculation gives exact list sizes and
anchored minimal uncolourable cores, but a single static colouring is not
enough: the explicit
[seven-root static-list barrier](../barriers/hc7_k7minus_seven_root_list_count_barrier.md)
realises both singleton and full odd-cycle cores without the critical-host
hypotheses.  Any list-based continuation must synchronize the seven
different vertex-deletion responses rather than infer a contradiction from
one core.

These attacks are not prerequisites for external review of the proved
package.  The stronger global `4n-5` statement remains open, but it is no
longer the minimal extremal input required by the critical-host reduction.

## 5. External sources requiring exact checks

1. Mader's seven-connectivity theorem for contraction-critical graphs;
   a modern traceable statement is Rolek--Song, Theorem 1.8.
2. Mader's sharp `K_4`- and `K_5`-minor edge bounds used by the seven-cut
   theorem.
3. Dirac's contraction-critical neighbourhood-independence inequality;
   a modern traceable statement is Rolek--Song, Lemma 1.6(i).
4. Matthias Kriesell and Samuel Mohr,
   [*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
   Theorem 7, including the exact definition and hypotheses of property
   `(*)`.
5. Jianbing Niu and Cun-Quan Zhang, *Cliques, minors and apex graphs*,
   [Theorem 1.10](https://doi.org/10.1016/j.disc.2008.12.009), at `k=5`.
6. Jakobsen's `K_7^-` extremal theorem and cockade exception, in the form
   quoted by Boris Albar,
   [Theorem 2 and Corollary 4](https://arxiv.org/abs/1402.2806).
7. Fournier's cyclability theorem, in the traceable form of Gould Theorem 7
   or Saito--Yamashita Theorem D.
8. Martin Rolek, Zi-Xia Song, and Robin Thomas,
   [Lemma 2.1](https://arxiv.org/abs/2208.07335), for the order-eight
   `K_4`-free, independence-number-two classification.
9. Norin--Totschnig, Theorem 6 and Conjecture 21, for the precise public
   density benchmark and priority context.

## 6. Review questions

1. Does the star contraction really induce the stated colouring of `G-v`,
   and does every Kempe swap leave a colour absent from the whole
   neighbourhood?
2. Does Kriesell--Mohr Theorem 7 apply to the complement demand graph with
   exactly the rooted-branch-set conclusion used here?
3. Are all adjacencies and disjointness conditions in the degree-one and
   degree-two complement contradictions explicit and correct?
4. Does the elementary minimum-degree classification exhaust every
   triangle-free complement on seven vertices?
5. Is Niu--Zhang Theorem 1.10 matched exactly, especially its apex and
   clique-intersection hypotheses?
6. Is the Jakobsen threshold converted correctly to `2m<=9n-25`, including
   exclusion of every cockade exception?
7. Are the equality order cases exhaustive, particularly the block--cut
   argument at central order eighteen and the `k=1` overlap case?
8. In the symmetric `q,c_j` Kempe arguments, do all component-disjointness,
   colour-availability, and restored-edge assertions hold with the displayed
   quantifiers?
9. In the common four-triangle branch, do the selected `p`- and
   `q`-components and the shortest-path extension form two disjoint connected
   branch sets with at most the one stated missing adjacency?
10. In the all-five-triangles branch, does the count `sum n_j<=4` and the
    choice `n_l<=1` ensure that one connected set meets all five triangles,
    the other meets at least four, and the resulting seven bags form an
    explicit `K_7^-` model?
11. Does the private-triangle reconstruction genuinely avoid every equality
    hypothesis, and does seven-connectivity supply its five disjoint private
    triangles for an arbitrary all-degree-seven literal `K_5`?
12. Does the five-subgraph branch model prove capacity at most four, and
    does the cutvertex split in the four-component case give both sides six
    boundary contacts and hence five common contacts?
13. Are the simultaneous-contraction surplus formula and the quantified
    deletion condition exactly equivalent to preservation of
    seven-connectivity?
14. In the boundary-colouring reflection lemma, is the pulled-back colouring
    restricted to the untouched opposite shore, and does the contracted
    clique force the equality partition to be exact?
15. Does `\pi_S(G)=\sum_i\mu_i`, together with the `2+2` and `1+3`
    reflection arguments, exclude every positive composition of four?
16. Does the hand proof cover every four-critical graph on at most seven
    vertices with at most nine edges, and hence justify the exact
    three-component chromatic conclusion without relying on enumeration?
17. Does the defect calculation give
    `b>=15-n_7+tau>=7+tau`, and does equality `b=7` force every asserted
    degree, clique, parity, and order conclusion?
18. In the exceptional-neighbourhood theorem, is Rolek--Song--Thomas
    Lemma 2.1 matched exactly, and do the seven displayed bags give at most
    the one claimed missing adjacency for every exterior miss?
19. In exterior completion, does seven-connectivity force the unused
    component to meet the independent-triple star and at least four of the
    five literal roots?
20. Does the seven-root list barrier refute only a static one-colouring
    inference, without purporting to satisfy the contraction-critical or
    forbidden-minor hypotheses?
21. Is the scope stated sharply enough that no reader can infer a global
    `4n-4` extremal theorem, a bond theorem, or two full connected
    transversals?
22. Are any of the exact neighbourhood, private-triangle, density,
    equality-structure, exceptional-neighbourhood, connected-subgraph-
    capacity, or contraction conclusions already explicit or implicit in
    the literature?

## 7. Review and publication gate

The internal package is ready to send to graph-minor and colouring/Kempe
specialists.  Before submission it still requires:

- independent human proof review of the degree-seven, two-clique,
  private-triangle, density, equality-structure, exceptional-vertex,
  exceptional-neighbourhood, connected-subgraph-capacity, critical
  reflection, and contraction arguments;
- conventional novelty and priority searches, including forward citation
  chains of Niu--Zhang, Rolek--Song, Rolek--Song--Thomas, Albar, and
  Norin--Totschnig;
- an independent rerun of the retained exceptional-neighbourhood verifier;
- correction and renewed hashes for any mathematical change; and
- a separate manuscript pass after the theorem package is stable.

Positive internal audits satisfy the repository promotion standard.  They
do not satisfy this external publication gate.
