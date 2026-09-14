# Bipartite colour sets need a global connected allocation

**Status:** explicit counterexamples to intermediate selection claims;
separate internal audit recorded [beside this file](bipartite_colour_allocation_audit.md).
Neither example refutes the augmentation target, Conjecture 19 or HC7.

## A connected bipartition cannot always retain colourfulness

**Claim refuted.** Suppose H is five-connected, six-chromatic, has
minimum degree at least six, and S is an inclusion-minimal bipartite set
whose complement R is four-colourable. If H[S] is connected, some
partition `S=A disjoint union B` into two nonempty connected sets has

`M(A,B)={r in R : r has neighbours in both A and B}`

meeting every class in every four-colouring of H[R].

Use the graph X on `Z_11` with edge differences `±2, ±3, ±5` from the
[audited augmentation examples](hc7_chromatic_augmentation_operations.md).
It is six-connected, six-regular and six-chromatic, and has a Q7 minor.
Set `S={0,2,4}`; it induces the path 0–2–4. Its complement has the
proper four-colouring

`{3,7}, {1,5}, {6,10}, {8,9}`.

The possible connected partitions, up to reversal, are exactly:

| A | B | M(A,B) | A missed colour class |
|---|---|---|---|
| `{0}` | `{2,4}` | `{5,6,8,9}` | `{3,7}` |
| `{4}` | `{0,2}` | `{6,7,9,10}` | `{1,5}` |

Every row follows directly from the edge differences. S is
inclusion-minimal: deleting either endpoint from S would leave an edge
and nine vertices. Since `alpha(X)=2`, recorded in the same audited
source, those nine vertices need at least five colours. Deleting its
middle vertex would leave an independent set, whose four-colourable
complement would five-colour X. No proper subset of S is therefore
eligible.

The independent shores `{0,4}` and `{2}` instead give the mixed set
`{5,7,8,10}`, colourful by the
[mixed-root lemma](../active/hc7_augmentation_batch_draft.md#2-one-common-rooted-model-from-a-bipartition).
Its vertices contact both independent shores, but those shores cannot
be treated as connected bags. The same displayed colouring defeats
both connected choices, so synchronising their colourings is insufficient.
Reselecting S or constructing a minor with different bags remains possible.

## Connectivity and chromatic number do not select a bipartite dominating set

**Claim refuted.** Every seven-connected seven-chromatic graph of
minimum degree at least eight has a connected induced bipartite
dominating set.

Take independent sets `A_0,...,A_4`, each of order seven, and completely
join cyclically consecutive sets. For each i add a disjoint clique
`X_i=K6`, completely joined to A_i and to no other set. Call the
resulting 65-vertex graph H.

Every X_i vertex has degree twelve and every A_i vertex has degree
twenty. Deleting at most six vertices leaves all A_i nonempty and their
cyclic backbone connected; every surviving X_i vertex contacts that
backbone. Deleting A_i separates X_i, so connectivity is exactly seven.
Each X_i together with one A_i vertex is K7. Conversely, three-colour
the backbone and give X_i the six other colours from a seven-colour
palette. Thus `chi(H)=7` and `delta(H)=12`.

Suppose B is connected and dominating. If it misses A_i, it must meet
X_i to dominate that clique. Since every edge leaving X_i ends in A_i,
connectedness confines B to X_i, preventing domination of other cliques.
Hence B meets every A_i. One representative from each intersection
induces a five-cycle in H[B], so B cannot be bipartite.

This graph contains a proper K7 subgraph. It does not satisfy the actual
critical host's proper-minor colourability or Q7 exclusion. Those
hypotheses, and a smaller-instance or terminal-model alternative, remain
available. The unsupported inference is selecting B from connectivity,
minimum degree and chromatic number alone.
