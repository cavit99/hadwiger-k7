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

**Working title:** *Degree-seven rigidity and density in a hypothetical
critical graph with no `K_7^-` minor*.

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
5. At equality, the ten degree-seven vertices form two disjoint literal
   `K_5`s, the order is at least twenty-nine, either clique deletion is
   five-connected, and the remaining two-transversal problem has exact
   overlap, bond, Hall, and edge-critical Kempe formulations.
6. Independently, every order-seven cut has the exact component and boundary
   restrictions recorded in the seven-cut theorem.

The note must not claim the `4n-5` extremal target, the two-transversal
target, the `K_7^-` six-colour conjecture, or `HC_7`.

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
  `451fd13b2fbd688cafb6f8005aefab92cc90eb7a1b92614ca10bdb7bdc9cc128`

The proof gives five-connected clique deletions, a three-connected central
graph, cross-matching order at most three, order at least twenty-nine, the
bond and Hall formulations, and the edge-critical common-spine Kempe fork.
It does not give the required two disjoint connected transversals.

### Seven-cut component contraction

- [Theorem](../results/hc7_k7minus_seven_cut_contraction.md)
- [Internal audit](../results/hc7_k7minus_seven_cut_contraction_audit.md)
- Theorem SHA-256:
  `3a746698ba61603ccbdc236d79afd5a4ba1f860c84a987b168f25cd962a00586`

The written proof is computation-free.  The finite scan recorded in its
audit only corroborates one elementary seven-vertex lemma.

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
      └─ bond, Hall, and edge-critical Kempe formulations

seven-connectivity + elementary minor constructions + Mader bounds
└─ seven-cut component and boundary restrictions
```

No computer-assisted finite classification is load-bearing in this chain.
The audits are internal checks and must not be described as independent or
external review.

## 4. Open statements and proposed next attack

The full sufficient extremal statement remains open:

> Every seven-connected `n`-vertex graph with at least `4n-5` edges contains
> a `K_7^-` minor.

The next bounded positive target is the equality-host specialization:

> In the five-connected graph obtained by deleting one equality `K_5`, the
> five private triangles have two vertex-disjoint connected transversals.

Equivalently, the deletion graph has a bond meeting every private triangle.
The immediate attack should use the edge-critical common four-triangle
Kempe spine and the exact overlap restrictions.  It should be time-bounded
and should not be treated as a prerequisite for external review of the
proved package.

If this attack stalls, the second research route is the fragment/descent
problem isolated by the seven-cut theorem.  A direct attack on the full
`4n-5` theorem is not recommended at this stage.

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
8. Are any of the exact neighbourhood, density, or equality conclusions
   already explicit or implicit in the literature?

## 7. Review and publication gate

The internal package is ready to send to graph-minor and colouring/Kempe
specialists.  Before submission it still requires:

- independent human proof review of the degree-seven, two-clique, density,
  and equality arguments;
- conventional novelty and priority searches, including forward citation
  chains of Niu--Zhang, Rolek--Song, Albar, and Norin--Totschnig;
- correction and renewed hashes for any mathematical change; and
- a separate manuscript pass after the theorem package is stable.

Positive internal audits satisfy the repository promotion standard.  They
do not satisfy this external publication gate.
