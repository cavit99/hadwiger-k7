# Internal audit: four-colour extension through a forest shore

**Verdict:** GREEN for Lemma 1, Corollary 2, Theorems 3 and 4, and the
stated application to the full order-seven outcome of the bounded-feedback
forest reduction.  This is a separate internal mathematical audit, not
external peer review.

## 1. Exact revision and imported results

The audited source is
[`hc7_k7minus_forest_shore_four_colour_extension.md`](hc7_k7minus_forest_shore_four_colour_extension.md),
with SHA-256

```text
bf0dfec2649c6c7fb6e3db784586e71ca38fc02523238129ecad56bde5e8ecec
```

Theorem 4 has exactly the hypotheses required by the separately audited
[`critical seven-cut capacity theorem`](../results/hc7_k7minus_critical_seven_cut_capacity.md),
whose audited revision is

```text
d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34
```

That theorem gives `pi_S(G)<=3` in this critical host.  Its cited general
seven-boundary theorem also gives `|E(G[S])|<=9` whenever `pi_S(G)=3`,
including when `G-S` has two rather than three components.  Corollary 2
uses the separately audited three-component exclusion at revision

```text
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96
```

together with the capacity theorem's exclusion of four or more components.
Thus an order-seven cut in the target-free critical host has exactly two
components.

Promotion changed only the status paragraph and audit link.  A mechanical
diff check found no mathematical change.

## 2. Forest extension and the proper-minor trace

A boundary colouring using at most four of a six-colour palette leaves two
unused colours.  Since every forest is bipartite, these two colours properly
colour `G[Y]`; neither can conflict across an edge from `Y` to `S`.  The
absence of `Y`--`D` edges then makes the gluing statement in Lemma 1 exact.
No equality merely up to a palette permutation is being assumed there: the
literal colouring on `S` is retained.

For Theorem 3, the sets `K_i union P_i` are connected, pairwise disjoint,
and each contains an edge, because `K_i` meets every vertex of the nonempty
set `P_i`.  Contracting their spanning trees therefore produces a proper
minor.  Pulling its six-colouring back only on `D union S` is legitimate:

- every `P_i` is independent, so assigning its vertices one colour creates
  no internal conflict;
- every edge from `P_i` to an untouched vertex is represented by an edge
  from the corresponding contracted image; and
- an edge between two different boundary blocks is represented between
  their two contracted images and hence forces distinct colours.

Vertices of `Y` are deliberately not pulled back.  They are recoloured by
Lemma 1 after the boundary trace has been obtained.  The trace uses at most
one colour for each contracted block and at most one for each remaining
literal boundary vertex, so (3.3) is exactly the required four-colour
bound.  This verifies both the contraction operation and the subsequent
bipartite extension without an unproved colouring synchronisation.

## 3. Full leaves, packing capacity and the boundary edge bound

Let `Y` be a tree component of `G-S`.  Seven-connectivity makes every
component of `G-S` full at the literal boundary `S`: otherwise its open
neighbourhood would be a cut of order at most six.  The tree is not a
singleton because such a vertex would have all its neighbours in the
seven-set `S`, contrary to `delta(G)>=8`.

Choose distinct leaves `u,v`.  Each has exactly one neighbour in `Y`, no
neighbour in another component of `G-S`, and degree at least eight.  It
must therefore be adjacent to all seven vertices of `S`.  The two singleton
subgraphs `{u},{v}` and any other component `D` of `G-S` are three disjoint
connected subgraphs full at `S`.  Hence `pi_S(G)>=3`; critical seven-cut
capacity gives equality and then the imported boundary estimate gives

```text
pi_S(G)=3,             |E(G[S])|<=9.
```

No assumption that `u` and `v` are adjacent, or that `D` is unique, is used
in this packing count.

## 4. The independent-triple alternatives

Suppose `I` is an independent triple in `S`.

If `G[S-I]` is a `K_4`, use its vertices as four singleton branch sets and
attach the three vertices of `I` bijectively to `{u}`, `{v}` and `D`.
Each enlarged set is connected because its exterior part is full at `S`.
Two such enlarged sets are adjacent because either exterior part meets the
boundary vertex assigned to the other.  They are also adjacent to all four
clique singletons.  The result is an explicit seven-bag `K_7` model.

If `G[S-I]` is not `K_4`, that four-vertex graph is three-colourable and
has an independent colour class `P` of order at least two.  The full
singletons `{u},{v}` are disjoint carriers for `I,P`.  The boundary-colour
count in Theorem 3 is

```text
2 + |S-(I union P)| <= 2 + (7-3-2) = 4,
```

so the resulting proper-minor trace extends through the forest and
six-colours `G`.  Both cases contradict the hypotheses.  Therefore
`alpha(G[S])<=2`.

## 5. Complement and Mantel equality

The last inequality makes the complement of `G[S]` triangle-free.  Mantel's
bound on seven vertices gives at most twelve complementary edges.  The
nine-edge boundary estimate gives at least `21-9=12`, so equality holds in
both bounds.  The equality case is `K_{3,4}`; consequently

```text
G[S] = K_3 disjoint union K_4.
```

Use the literal `K_4` as four singleton branch sets and attach the other
three boundary vertices to `{u}`, `{v}`, and `D`.  The same fullness check
as in Section 4 supplies every adjacency among the three enlarged sets and
between them and the clique.  This is again an explicit `K_7` model, which
is stronger than the forbidden `K_7^-` conclusion.  The final contradiction
is therefore valid.

## 6. Transfer to the bounded-feedback outcome and trust boundary

In outcome 1 of the audited forest-component reduction, the displayed set
is connected inside the induced forest `G-T`, and equality in its boundary
inequality makes it a component after deleting its seven-vertex open
neighbourhood.  Its induced graph is consequently a tree.  All hypotheses
of Theorem 4 come from the same critical host, so that entire full
order-seven outcome is eliminated.

The result does not eliminate the three-piece or six-component alternatives
of the forest reduction.  It also does not infer that a matching-signature
colouring is proper on an opposite shore: the source correctly records that
deleted monochromatic edges and five-/six-colour boundary traces remain an
obstruction in other settings.  No unresolved assumption or proof gap was
found in the audited statements.
