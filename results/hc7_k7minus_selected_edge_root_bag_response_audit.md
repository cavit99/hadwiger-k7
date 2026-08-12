# Separate internal audit: selected-edge root-bag response

## Verdict and exact revision

**Verdict: GREEN, with the label-loss limitation stated in the source.**

This audit checks the complete source file
[`hc7_k7minus_selected_edge_root_bag_response.md`](hc7_k7minus_selected_edge_root_bag_response.md)
at SHA-256

```text
403070aaa16845f167e1111e77fdf8dfbe72d08434d6c1246c732906cbfd083b
```

The mathematical content was cold-audited at

```text
228c916bf33e03cddd27218a5f828e9e4e807c20fe0c83021841740625dc26f5
```

and promotion changed only the status wording and the relative paths of
three dependency links.

The branch-set split, the actual-separation conclusion, the rejected
boundary partition and the bounded unlabelled endpoint are correct at this
revision.  Section 4 accurately records a route nonclosure; it does not
claim an order-at-most-eight separator carrying the original labels.  This
is a separate internal mathematical audit, not external peer review.

The direct dependencies have the following current source hashes, each
matching its adjacent GREEN audit:

```text
ca291c23674c11832159301af0c9d1bd7bfd5302495359bbfe81b4f8a5f55e14  results/hc7_k7minus_matching_square_common_state.md
61fa3c094c34d06590efcef8a6903356f36bc8aadcdec75f834aa7e5cfd82936  results/hc7_contracted_edge_k6_model_normalization.md
d95c459737f7d94e8c212e8f3d90e2b5fbf762f46567d70e6e6d9dfb386dd244  results/hc7_k7minus_matching_lock_boundary_reduction.md
```

## 1. The model lift and selected-edge split

The spanning `K_6` model in `G/e` is an explicit hypothesis of Theorem
2.1, not a consequence silently inferred from six-colourability.  In the
opposite-coordinate application, the audited common-state theorem gives a
spanning `K_6` model in `G/e/f`.  Expanding the contraction class of `f`
inside its branch bag preserves connectedness and every branch-set
adjacency, so it gives exactly the required spanning model in `G/e`.  This
remains true whether the two contraction images originally lie in the same
bag or in different bags.

Expanding the contraction image of `e` makes the root bag connected because
the two preimages are joined by `e`.  Any edge of a connected graph belongs
to some spanning tree.  Choosing such a tree and deleting `e` therefore
partitions the lifted root bag into two nonempty, disjoint connected sets
`R_u,R_p`, containing the respective endpoints.  The restored edge makes
the two sets adjacent.

Every foreign bag is adjacent to `R_u union R_p`, and the five foreign bags
are pairwise adjacent.  If four foreign bags meet both split sets, the seven
displayed branch sets have at most one missing adjacency: only the fifth
foreign bag can miss one of the split sets.  Extra adjacencies are harmless,
so this is a valid `K_7^-`-minor model.

If at most three bags meet both sides, at least one foreign bag meets only
one side and is therefore anticomplete to the other side.  Taking the latter
as `Y` gives a nonempty connected set and a foreign bag disjoint from
`N_G[Y]`.  Thus `N_G(Y)` is an actual vertex cut.  Seven-connectivity gives
its asserted lower bound of seven.  The source correctly attributes
disjointness here to the branch-set axioms; spanningness is not needed for
that step.

## 2. The original colouring response

The colouring `phi` is proper on `G-e`, and the sole edge which can be
monochromatic after restoring `e` is `e` itself.  Exactly one endpoint of
`e` lies in `Y`.  Hence deleting `Y` removes that possible conflict and
`phi|G-Y` is a proper six-colouring of the intact complementary closed
shore.  The other endpoint lies in `N_G(Y)`, so the selected edge crosses
the actual boundary literally.

If the equality partition induced by `phi` on `S=N_G(Y)` extended through
the intact closed `Y`-shore, the two boundary colourings would use the same
blocks.  The resulting bijection between their used boundary colours
extends to a permutation of the six colour names.  After that permutation
the two colourings agree on `S` and glue to a proper six-colouring of all of
`G`, contradicting `chi(G)=7`.  This verifies both the rejection assertion
and the fact that the initial separator retains the original selected edge,
colouring and equality partition.

The theorem is stated under target exclusion while retaining the explicit
target as its first alternative.  This is logically redundant but harmless:
under the complete setting the second outcome must occur, while the first
branch records the terminal model construction used in applications.

## 3. Numerical descent and loss of labels

The large actual-boundary singleton descent is invoked at exactly its
audited strength.  Starting from any actual boundary of order at least ten,
it produces the neighbourhood of a singleton with order at least seven and
strictly smaller than the old order.  Repetition must therefore terminate
at order seven, eight or nine.  Every produced boundary carries a rejected
proper-minor colouring response.

That descent chooses a new low-degree vertex, an incident edge and a
six-colouring of the newly edge-deleted graph.  It does not preserve the
original edge `e`, the common-model branch labels, the original shore or the
partition induced by `phi`.  Corollary 2.2 states precisely this loss.  It
retains all original labels only when the boundary supplied directly by
Theorem 2.1 already has order at most nine.  No labelled order-at-most-eight
conclusion is inferred.

## 4. Comparative machinery and exact trust boundary

The summaries in Section 3 agree with the cited audited results.  Minimal
contraction-bag normalisation and the standard branch-set splits return
actual separators without an upper bound; the colour-matched and
first-hit transfer theorems require named model contacts absent from a bare
palette lock; and the paired-source theorem assumes the special
order-eight labelled configuration.  The adjacent-pair and double-critical
fan constructions occur in a different deletion host and do not identify
their branch sets with the fixed model in `G/e`.  These observations are
comparisons of hypotheses, not additional positive lemmas used in the proof
of Theorem 2.1.

Five bichromatic lock paths can overlap and can first meet the boundary or
the common model in repeated, unprescribed locations.  They consequently
do not imply five distinct boundary vertices, four prescribed foreign-bag
contacts, or an upper bound on the original boundary.  The unsupported
implication displayed in (4.1) is therefore correctly withheld.

There are no unresolved mathematical assumptions in Theorem 2.1 or
Corollary 2.2 beyond their stated hypotheses and the audited dependencies.
The note does not prove the matching row, the six-cut branch, the
`K_7^-` six-colour conjecture or `HC_7`.
