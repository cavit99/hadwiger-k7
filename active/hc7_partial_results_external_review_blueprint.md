# External-review and manuscript blueprint for the bounded-interface results

**Status:** publication-planning document; not a theorem, status authority,
manuscript, novelty claim or external peer review.

**Frozen mathematical revision:** tag `mathematical-freeze-2026-07-27`,
commit `7f3d84e9bcc405f17ef4dea895892c90f6d58c71`.

**Research status:** `HC_7` is not proved.  Intensive autonomous proof search
is paused while the standalone results receive conventional priority,
proof and computational review.  The authoritative mathematical status
remains [`RESEARCH_LEDGER.md`](../RESEARCH_LEDGER.md).

## 1. Purpose and decision

This document defines the smallest useful package to place before external
specialists.  It does not draft the paper.  Its purposes are to:

1. isolate the results that can stand independently of the unfinished proof
   programme;
2. expose their actual dependency and computation boundaries;
3. define four external review tracks and a decision gate for writing a full
   manuscript; and
4. state the remaining completion obstruction as a separate research
   question, without making it part of the proposed paper's claim.

The current operating decision is:

- do not fund another open-ended path, contact-graph or bounded-case
  campaign with the present model;
- use model work for exposition, source checking, reproduction, adversarial
  review and responses to specialist feedback; and
- reopen intensive proof search only under one of the triggers in Section 9.

No theorem or audit file in the frozen revision should change during review.
A mathematical correction creates a new frozen revision and requires renewed
audits and hashes for every affected dependency.

## 2. Candidate paper thesis

**Working title:** *Bounded interfaces in a minimal counterexample to
Hadwiger's conjecture for `t=7`*.

The proposed paper studies necessary structure in a hypothetical
minor-minimal seven-chromatic graph with no `K_7` minor.  Its main theme is
that a low-degree vertex exposes actual full separations of order seven to
nine with unusually complete boundary-colouring responses, and that the
number and packing behaviour of the resulting components are restricted by
explicit upper bounds.

The paper would not claim a proof of `HC_7`, proximity to a proof, or a new
global unlabelled near-`K_7` guarantee.

## 3. Candidate theorem package

Every item below has a written proof and a separate GREEN internal audit.
Those audits are useful preparation, not peer review.

### Core A: bounded full-separation entry

- [Theorem](../results/hc7_low_degree_adjacent_pair_alignment.md)
- [Internal audit](../results/hc7_low_degree_adjacent_pair_alignment_audit.md)
- Frozen theorem SHA-256:
  `263611a40dc7829788967250e031a3f3170e1c7a6c8c9a3fbfbb358231b1f9ca`

There are adjacent vertices `u,z` with `7<=d(u)<=9` and
`chi(G-{u,z})=6`.  For every component `C` of `G-N[u]`, its neighbourhood
`S=N(C)` has order seven to nine and defines an actual full separation.
The boundary is four-colourable, and every nonempty independent subset of
`S` occurs as one exact boundary colour class in a six-colouring of either
closed shore.

The two shore colourings need not induce the same complete partition of
`S`.  The two computer-assisted inputs are the
[degree-nine local completion](../results/hc7_degree9_pole_verifier.md) and
the order-eight/nine
[two-full-shore boundary absorption](../results/hc7_two_full_shore_boundary_absorption.md)
used in the four-colour boundary conclusion.

### Core B: component-uniform responses

- [Theorem](../results/hc7_component_uniform_boundary_alignment.md)
- [Internal audit](../results/hc7_component_uniform_boundary_alignment_audit.md)
- Frozen theorem SHA-256:
  `a6046ab5538b8468bdc211d40b537dec5fca909d47ab9c30acb197d74767410e`

At the same degree-seven-through-nine vertex `u`, every component `D` of
`G-N[u]` has its own vertex `z_D in N(D)` satisfying

```text
chi(G-{u,z_D})=6.
```

This preserves the named response if an actual smaller component is found;
it does not force one to exist.  The exceptional order-nine classification
is computer-assisted.

### Core C: exterior-component upper bounds

- [Theorem](../results/hc7_low_degree_exterior_component_bounds.md)
- [Internal audit](../results/hc7_low_degree_exterior_component_bounds_audit.md)
- Frozen theorem SHA-256:
  `4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29`

The numbers of components of `G-N[u]` are at most one, two and three when
`d(u)` is seven, eight and nine, respectively.  The direct order-eight and
order-nine bounds use retained finite classifications.  The degree-seven
bound comes from the separate
[anti-neighbourhood connectivity theorem](../results/hc7_degree7_anti_neighbourhood_connectivity.md),
whose dependency closure includes the exact-seven results below.  This
nonlinear dependency must be visible in any paper.

### Core D: exact order-seven full-connected-subgraph packing

- [Theorem](../results/hc7_exact_seven_packet_packing.md)
- [Internal audit](../results/hc7_exact_seven_packet_packing_audit.md)
- Frozen theorem SHA-256:
  `501f581d764607ef9cd13b854150dae95ea251efde0fdd28c77bb9632415fc57`

For an actual order-seven separation, let `nu_i` be the maximum number of
pairwise vertex-disjoint connected subgraphs in open shore `i` that are
adjacent to every boundary vertex.  Then

\[
 \nu_1+\nu_2\le4,\qquad
 \min\{\nu_1,\nu_2\}=1,\qquad
 \omega(G[S])\le6-(\nu_1+\nu_2).
\]

This is the cleanest standalone theorem in the package and has a written
proof independent of computation.  A small exhaustive program is retained
only as a regression check.  Packing number one does not imply a small
vertex transversal, planarity or compatible boundary colourings.

### Core E: multi-component colouring response

- [Theorem](../results/hc7_component_deletion_kempe_exchange.md)
- [Internal audit](../results/hc7_component_deletion_kempe_exchange_audit.md)
- Frozen theorem SHA-256:
  `e659b2765053c34415cad0c6e9dcec78a250e751dd80d79f8e077d064d24835f`

When at least two exterior components occur, every component has a private
rejected boundary colouring and supported nonedge.  All selected nonedges
may be retained simultaneously in a `K_6`-minor-free neighbourhood
augmentation.  Either one boundary trace is rejected by several components,
or one Kempe interchange transfers the unique rejection between two
components.

Neither outcome is terminal for `HC_7`.  One finite equality classification
is computer-assisted.  This is the preferred fifth main theorem because it
continues the bounded-interface narrative without overlapping the public
unlabelled near-clique theorem.

### Optional application: a localized degree-seven near-clique model

- [Theorem](../results/hc7_degree7_aligned_near_k7_model.md)
- [Internal audit](../results/hc7_degree7_aligned_near_k7_model_audit.md)
- Frozen theorem SHA-256:
  `51bd2cf191f848a398a1a4aee711ef0c4d36c747468ce9613b9514cbc56cd060`

Conditional on a degree-seven vertex, the theorem gives a boundary-labelled
model of `K_7^-` or `K_7^vee`, with every possibly missing adjacency
incident with one literal boundary singleton.  It should appear only as a
secondary application unless the priority review confirms that the retained
roots and localization add publishable content beyond the known global
`K_7^vee` theorem.  Here `K_7^vee` denotes `K_7` with two adjacent edges
deleted.

## 4. Dependency and trust map

The results form a branching package, not one linear proof.  The following
is the reader-facing composition map; the adjacent audits remain the
authority for the complete formal dependency closure.

```text
hypothetical-counterexample hypotheses
├─ bounded entry
├─ component-uniform response
│  └─ reuses the bounded-entry local-completion lemma
├─ degree-8/9 component upper bounds
├─ component-deletion exchange, when at least two components occur
└─ exact-seven package
   ├─ exact-seven packing
   ├─ adaptive (1,3) and (1,2) closures
   └─ singleton/Moser two-component closures
      └─ degree-7 anti-neighbourhood connectivity
         └─ optional degree-7 labelled application
```

The degree-seven arm therefore depends on more than Core D.  Its promoted
closure package consists of the
[adaptive `(1,3)` theorem](../results/hc7_exact7_adaptive_packet_reflection.md),
[adaptive `(1,2)` theorem](../results/hc7_exact7_adaptive_12_boundary_closure.md),
[singleton-component closure](../results/hc7_exact7_two_component_singleton_closure.md)
and the audited
[pure-Moser two-component closure](../results/hc7_exact7_moser_two_component_closure.md),
in addition to exact-seven packing.
The bounded entry, component-uniform response, component bounds and
component-deletion exchange then compose into the proposed paper narrative;
that narrative order should not be mistaken for a chain of theorem
dependencies.

The main external inputs to verify against primary sources are:

| Input | Role | Primary or traceable source |
|---|---|---|
| `HC_5` and `HC_6` | supplies `K_5`/`K_6` minor models from chromatic lower bounds | Robertson, Seymour and Thomas, [Hadwiger's conjecture for `K_6`-free graphs](https://doi.org/10.1007/BF01202354) |
| Mader's exact `K_7` density bound | closes dense bounded-neighbourhood quotients | Mader, [*Homomorphiesätze für Graphen*](https://eudml.org/doc/161741); modern statement in [Rolek--Song](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf), Theorem 2.1 |
| Seven-connectivity of contraction-critical graphs | makes the displayed boundaries actual and full | Mader; modern statement in [Rolek--Song](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf), Theorem 1.8 |
| Dirac's neighbourhood independence bound | controls low-degree neighbourhoods | Dirac; modern statement in [Rolek--Song](https://sciences.ucf.edu/math/zxsong/wp-content/uploads/sites/13/2018/04/Coloring-graphs-with-forbidden-minors.pdf), Lemma 1.6(i) |
| Kempe connectivity of colourings of a degenerate graph | connects component-private responses | Las Vergnas--Meyniel, Proposition 2.1 |
| Rooted `K_5` packaging | used only in the optional degree-seven application | Kriesell--Mohr, Theorem 7 |

The graph-minor reviewer should also trace the internal dependencies named
in each adjacent audit, rather than treating this table as complete.

## 5. Preliminary public-frontier and priority map

This is an initial comparison, not novelty clearance.

| Candidate contribution | Closest identified public result | Present assessment |
|---|---|---|
| Same-vertex order-seven-to-nine full separations with component-specific double-deletion responses | Classical connectivity, Dirac and Kempe-path machinery; no exact published match identified | Plausibly new; highest priority-search value |
| Exterior-component upper bounds `1/2/3` | Rolek--Song--Thomas, [Theorem 1.2](https://doi.org/10.1016/j.ejc.2023.103711), treats a different eight-contraction-critical regime and degree distribution | Plausibly new; database and citation-chain check required |
| Exact order-seven packing inequalities | No close published statement identified | Plausibly new and cleanest standalone claim |
| Multi-component rejection/Kempe dichotomy | Generic Kempe and contraction-critical methods | Plausibly new formulation; check for equivalent separator-language results |
| Boundary-labelled degree-seven near-clique model | Norin--Totschnig, [Theorem 4](https://arxiv.org/html/2507.03244v1), already guarantees an unlabelled `K_7^vee` minor globally | Only the localization and retained labels may be new |

Norin and Totschnig's Theorem 6 is also the current nearby density theorem,
and their Conjecture 21 identifies the global `K_7^-` guarantee as a natural
next problem.  None of the proposed paper claims should be described as a
stronger global guaranteed minor.

A conventional priority review must search MathSciNet, zbMATH, arXiv and
the forward citation chains of Rolek--Song--Thomas and Norin--Totschnig.
Search terms should include anti-neighbourhood components of
contraction-critical graphs, precolouring extension across order-seven
separators, and packing connected subgraphs full to a minimum separator.

## 6. Reproducibility inventory

The following commands were rerun locally against the frozen revision on
27 July 2026.  A local rerun is not independent external reproduction.

| Claim | Command | Frozen local outcome |
|---|---|---|
| Degree-nine local completion | `python3 results/hc7_degree9_pole_verifier.py` | PASS; 4,608 rooted instances |
| Component-uniform alignment | `python3 results/hc7_component_uniform_alignment_verifier.py` | PASS; 5,913 marked pairs and two stated exceptions |
| Order-eight component bound | `python3 archive/degree8_three_shore_verify.py` | PASS; three certificate families with 141, 183 and 98 model templates |
| Order-nine component bound | `python3 archive/degree9_four_shore_verify.py` | PASS; all `23` miss types, `423` model templates |
| Two-full-shore boundary absorption | `geng -q -c -d4 8 | python3 active/hc7_boundary_join_probe.py`<br>`geng -q -c -d4 9 | python3 active/hc7_boundary_join_probe.py` | Expected output reproduced: `0` order-eight and `1` order-nine survivor |
| Component-deletion equality case | `python3 results/hc7_component_exchange_five_core_verifier.py` | PASS; 1,449 marked quotients |
| Exact-seven partition regression check | `c++ -O2 -std=c++17 results/hc7_exact_seven_partition_probe.cpp -o /tmp/hc7_exact_seven_partition_probe`<br>`/tmp/hc7_exact_seven_partition_probe` | PASS; `GREEN labelled_triangle_free_graphs=133501 candidates=546 nonbip_no_singleton=0 nonbip_no_balanced_singleton=0` |
| Adaptive `(1,2)` boundary census | `uv run --with networkx==3.6.1 python results/hc7_exact7_adaptive_12_boundary_verify.py` | PASS; `685` boundaries, `876` partitions, `446` robust-block closures, `10` absolute hard residuals |
| Exact-seven packet quotient | `uv run --with networkx==3.6.1 python results/hc7_exact7_adaptive_12_packet_quotient_probe.py`<br>`uv run --with networkx==3.6.1 python results/hc7_exact7_adaptive_12_boundary_probe.py` | PASS; `446` robust-block and `246` two-anchor closures, overlap `136`, residual `129` |
| Exact-seven residual identity | `uv run --with networkx==3.6.1 python results/hc7_exact7_adaptive_12_residue_probe.py` | PASS; unique independence-two residuals at `11` and `12` edges |
| Moser singleton-closure subcases | `uv run --with networkx==3.6.1 python archive/moser_global_cutvertex_verify.py`<br>`uv run --with networkx==3.6.1 python archive/moser_global_2cut_verify.py` | PASS; `57` cutvertex pairs and `260` two-cut quotients with the stated two residuals |

The local environment was CPython 3.14.6, NetworkX 3.6.1, Z3 4.16.0,
nauty `geng` on `PATH`, and Apple clang 21.0.0.  The sequential order-nine
command is a long run; independent reproducers may invoke its indices
`0,...,22` as separate parallel processes.  The exterior-component
certificate files contain model templates rather than proof-producing UNSAT
traces.  An
external reproducer should therefore regenerate the finite universes and
check the certificates with an independent catalogue and checker wherever
feasible, rather than merely rerunning these programs.

## 7. External review tracks

### A. Novelty and priority

1. Is the same-vertex combination of degree seven to nine, actual full
   separations, four-colourable boundary and exact independent-block shore
   responses already known?
2. Is the component-specific choice of `z_D` with
   `chi(G-{u,z_D})=6` new?
3. Are the exterior-component upper bounds known or immediate from existing
   contraction-critical results?
4. Are the exact-seven packing inequalities known or folklore?
5. Does the retained degree-seven boundary labelling add content beyond
   Norin--Totschnig's global theorem?
6. Which claims should be main theorems, corollaries, credited as known, or
   omitted?

### B. Graph-minor proof audit

1. Check every contraction, branch-set lift and disjointness assertion in
   Cores A--E.
2. Check each use of seven-connectivity and Mader's bound against its exact
   hypotheses.
3. Check the two exceptional marked order-nine quotients in Core B.
4. Check that the finite alternatives in Core C exhaust the stated
   unbounded host configurations and lift back to the host.
5. Check the full-connected-subgraph-plus-clique construction in Core D
   without assuming adjacency between the connected subgraphs.

### C. Colouring and Kempe audit

1. Check the exact independent-block realization on both closed shores.
2. Check the component-uniform double-deletion and recolouring argument.
3. Check every colour permutation and boundary-partition gluing step.
4. Check the full-connected-subgraph-funded synchronization in Core D.
5. Check that no labelled-colour normalization error of the kind corrected
   in exact-block Corollary 2.2 enters this package.

### D. Independent computation

1. Regenerate each finite universe and marked instance set.
2. Check graph canonicalization and catalogue completeness independently.
3. Validate every branch-set certificate directly.
4. Reproduce the exact counts and hashes under a documented environment.
5. Where practical, replace solver-trusted UNSAT with proof-producing or
   formally checked certificates.

## 8. Blueprint for a later manuscript

Only after the review gate passes, a full manuscript should use this
structure:

1. public context, exact claims and explicit non-claim of `HC_7`;
2. minimal-counterexample setup and external inputs;
3. bounded full-separation entry;
4. component-uniform responses;
5. exterior-component upper bounds;
6. exact order-seven full-connected-subgraph packing;
7. multi-component colouring response;
8. optional degree-seven localized application, if priority review supports
   it;
9. limitations and the unresolved synchronization problem; and
10. a computational appendix separated from the written arguments.

The order-eight/order-nine live case tree, conflict graph, height-six route,
PR history, token expenditure and probability estimates should not appear
in the main narrative.

The gate for drafting the full manuscript is:

- all core theorems survive line-by-line human review;
- the primary-literature overlap matrix is complete;
- the finite classifications are independently reproduced;
- every correction is resolved at a new frozen revision; and
- external reviewers agree that a coherent novel theorem package remains.

## 9. Separate specialist challenge and restart criteria

The unfinished proof campaign should be described separately from the paper.
The exhaustive open theorem remains the
[pole-free bridge-composition theorem](hc7_bounded_interface_synchronization_frontier.md#4-primary-open-theorem):
operation-specific failed-lift paths must yield an explicit `K_7`-minor
model, one common complete boundary partition, or a response on a strictly
smaller literal anti-neighbourhood component in the same host.

A clean major intermediate question is also available.  The
[dominating-model regeneration theorem](../results/hc7_dominating_k5_regeneration.md)
gives an unlabelled dominating `K_5` model after deleting any two vertices.
For an adjacent deleted pair, a model whose five bags have root-contact
profile `5/4` would give a `K_7^-` minor, while profile `5/5` gives a `K_7`
minor.  No present theorem aligns the bags with the roots.  This is a useful
question for specialists, not a current autonomous proof campaign.  The
external source is Girão et al.,
[*The Dominating 4-Colour Theorem*](https://arxiv.org/abs/2605.10112).

Intensive proof search should restart only if at least one of the following
occurs:

1. a specialist identifies a concrete applicable theorem or missing lemma
   whose hypotheses already match the host;
2. a new external theorem materially strengthens rooted or colourful minor
   theory at the required connectivity and separator orders; or
3. a future model independently closes one exhaustive branch with only the
   three permitted outputs and survives cold reconstruction against the
   barrier corpus.

A new path description, colouring response, unbounded separator, finite
boundary census or reversible normalization is not a restart trigger.

## 10. Human review record template

```text
Reviewer and area:
Frozen tag and commit:
Files reviewed:
Review type: novelty / graph-minor proof / colouring proof / computation
Verdict: verified / correction required / unresolved
Exact theorem, line or computation affected:
Reason and proposed correction:
Known-source overlap, with theorem number:
Independent computation environment and output, if applicable:
Remaining dependencies not checked:
```

Completed human reviews should be retained as ordinary review records and
must not be labelled as repository-internal GREEN audits.
