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
seven-boundary contraction criteria without a `K_7^-` minor*.

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

seven-connectivity + elementary minor constructions + Mader bounds
└─ capacity of boundary-full connected subgraphs at most four
   ├─ sharpened seven-cut boundary and interior restrictions
   └─ exact whole-component density/connectivity contraction criterion
```

No computer-assisted finite classification is load-bearing in this chain.
The audits are internal checks and must not be described as independent
human review or external peer review.  The bond formulation in the equality theorem is an
equivalent target inside the now-excluded equality host, not a proved
standalone bond or two-full-transversal theorem.

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

The all-degree-seven extraction is complete.  The remaining positive target
is the seven-cut reduction statement:

> If a seven-connected graph `G` has `m>=4n-4` and an order-seven cut, then
> `G` contains a `K_7^-` minor or has a proper seven-connected minor `H` with
> `|E(H)|>=4|V(H)|-4`.

Together with minor minimality and the easy eight-connected case, this would
prove the bare extremal theorem and hence the `K_7^-` six-colour conjecture.
Conversely, the bare theorem immediately supplies the first outcome, so this
dichotomy is headline-equivalent rather than a routine preliminary lemma.

The first attack has removed `r=5` and reduced every whole-component descent
to an exact surplus inequality and an exact deletion-connectivity test.  It
has also proved that all nonsingleton components in the `r=4` case are
two-connected.  The next attack should therefore treat `r=4`, combining the
deletion certificate of any density-eligible contraction with the other
three components, each adjacent to every boundary vertex.  Then come `r=3`
and the likely hard
`r=2` `K_5`-minor-free boundary.  Every successful case must produce an
explicit minor model or threshold-preserving descent.
Counterexamples to intermediate lemmas are falsification checks and pivot
signals, not a successful endpoint.  A normalized Norin--Totschnig
near-`K_7` upgrade remains the higher-risk fallback.

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
8. Norin--Totschnig, Theorem 6 and Conjecture 21, for the precise public
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
14. Is the scope stated sharply enough that no reader can infer a global
    `4n-4` extremal theorem, a bond theorem, or two full connected
    transversals?
15. Are any of the exact neighbourhood, private-triangle, density,
    equality-structure, connected-subgraph-capacity, or contraction conclusions already
    explicit or implicit in the literature?

## 7. Review and publication gate

The internal package is ready to send to graph-minor and colouring/Kempe
specialists.  Before submission it still requires:

- independent human proof review of the degree-seven, two-clique,
  private-triangle, density, equality-structure, connected-subgraph capacity, and
  contraction arguments;
- conventional novelty and priority searches, including forward citation
  chains of Niu--Zhang, Rolek--Song, Albar, and Norin--Totschnig;
- correction and renewed hashes for any mathematical change; and
- a separate manuscript pass after the theorem package is stable.

Positive internal audits satisfy the repository promotion standard.  They
do not satisfy this external publication gate.
