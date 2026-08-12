# Independent cold audit: full-boundary fans at the final six-cut residue

**Verdict:** **GREEN** for Theorems 2.1 and 3.1 at the exact revision
below.  Section 4 correctly records a route nonclosure, not a theorem or
counterexample.  This is a separate internal mathematical audit, not
external peer review.

## Exact revision and dependencies

The audited source is
[`hc7_k7minus_six_cut_fan_model_alignment.md`](hc7_k7minus_six_cut_fan_model_alignment.md),
with SHA-256

```text
f50587a8d481379da4b0d7851878555500ba75b51d3e3cfa818cc3d09297f56c
```

The mathematical proof was checked at
`56fa06d7445aac3f12343e7ddcca518a3b1e4f9d1d4d769024310000a7492a23`.
The final promoted source differs only by status text linking this cold
audit; a mechanical comparison found no mathematical change.

The direct repository inputs were checked at their separately audited
revisions:

- the [six-cut coordinate-localisation theorem](../results/hc7_k7minus_six_cut_coordinate_localisation.md),
  `b2803d6cabf6684aaa0af8487be66ab7ac738909719028fd304f29b1b9682555`;
  and
- the [six-coordinate induced-forest reduction](../results/hc7_k7minus_six_coordinate_forest_reduction.md),
  `cc2b56362d52a3ef23559a4a0e5cbf5eded5abbe7d54b57e73f66f74f1dd3405`.

The first gives the stated residual geometry after strict responses are
excluded: `|T|` is eight or nine, `G-T` has exactly two or three components,
and every component is full to `T`.  The second supplies the exact singleton
signature colourings and the spanning exact `K_7^vee` model used in the
application and route analysis.  The source makes its additional no-response
hypothesis explicit rather than importing it from either theorem.

## 1. Completed-shore connectivity and the full fan

For a separator `Z` of order less than `t` in the completed torso `H_C`, the
clique `T-Z` lies in one component.  Every other component has a nonempty
connected vertex set `A subseteq C`, and the added edges have both ends in
`T`, so

```text
N_G(A) = N_{H_C}(A) subseteq Z.
```

Another component of `G-T` is a genuine far side.  Seven-connectivity gives
`|N_G(A)|>=7`, while `|Z|<t` makes `A` a forbidden strict response.  Thus
`H_C` is `t`-connected.

The cold audit first found a gap in an earlier draft which attempted to use
Menger directly in the uncompleted closed shore: the stated separator did
not ensure that the source component avoided all other boundary vertices.
The audited revision repairs this by fixing `x in P` and applying the Fan
Lemma in the already proved `t`-connected torso.  It gives `t` paths from
`x` to distinct vertices of `T`, disjoint outside `x`.  Truncation at the
first visit to `T` removes every possible use of an added clique edge, so the
paths lie in `G[C union T]`, have internal vertices in `C`, and are disjoint
outside `P`.

For each prescribed edge from a vertex of `P` to a distinct terminal, replace
the fan path ending at that terminal by the edge.  The replacement has no
internal vertex outside `P`, its terminal is not used by another path, and
intersections inside `P` are allowed.  This verifies all three assertions of
Theorem 2.1, including simultaneous prescribed-edge replacement.

## 2. The operation-specific six-fan

In a proper six-colouring of `G-pv`, the vertices `p` and `v` must receive
the same colour; otherwise restoring `pv` would six-colour `G`.  For every
other colour `beta`, the `alpha`--`beta` component containing `v` must contain
`p`, since otherwise a Kempe interchange on that component makes `pv`
proper.  A path to `p`, stopped at its first visit to `T`, stays in `C`
internally.  Its first neighbour has colour `beta`, so the five choices of
`beta` give five distinct first vertices and edges.

Let `D` be the `h` first neighbours already in `T`, and let the other
`ell=5-h` first neighbours be `S subseteq C-{v}`.  If the required
`S`-to-`T-(D union {p})` linkage in (3.2) does not exist, set-to-set Menger
gives a separator `Z` of order at most `ell-1`.  At least one source survives.
Its component contains no surviving target, lies in `C`, and can leave in
`G` only through `v`, `p`, `D`, or `Z`.  Hence

```text
|N_G(A)| <= 2 + h + (ell - 1) = 6,
```

contradicting seven-connectivity because a different component of `G-T` is
a far side.  The linkage is therefore present.  Its paths are mutually
vertex-disjoint; prepending the distinct prescribed first edges, retaining
the direct edges to `D`, and adding `vp` produces six distinct boundary ends
and no common vertex outside `v`.  Truncation preserves both properties.
The case `ell=0` is vacuous and consistent with the same construction.

For a singleton forest signature, restoring the forest leaves exactly the
selected coordinate edge monochromatic.  The colouring is consequently a
proper colouring of `G-e` with equal-coloured ends, exactly as required by
Theorem 3.1.

## 3. Model alignment and route nonclosure

The selected-terminal obstruction in Section 4 is correctly scoped.  In
the displayed five-nondirect-source case the potential neighbourhood bound
is `1+1+(t-6)+4=t`; with `h` retained direct terminals the same accounting is
`1+1+h+(t-6)+(4-h)=t`.  Seven-connectivity excludes neither value, and a
prescribed first edge that already ends at an unselected boundary vertex
cannot be retargeted while retaining that edge and the first-hit condition.

The source also correctly separates two different models.  The exact
spanning `K_7^vee` model lives in `G-F`, where the coordinate edge is absent,
so its endpoints need not be in one bag.  On the other hand `G/e` is exactly
six-chromatic: it is a proper minor and hence at most six-colourable, while a
five-colouring could be lifted and one endpoint recoloured with a fresh sixth
colour to six-colour `G`.  The established case `HC_6` supplies a `K_6`
model.  Absorbing components outside that model makes it spanning, so the
bag containing the contraction image may be designated as the root bag.
None of this identifies its five foreign bags with the six foreign bags of
the exact `K_7^vee` model.

After lifting the root bag, a spanning tree can be chosen to contain `e`.
Deleting `e` from that tree gives two disjoint connected sides.  If four of
the five foreign bags contact both sides, the sides and the five foreign bags
are seven pairwise disjoint connected branch sets: `e` joins the two sides,
the foreign bags are pairwise adjacent, and only the fifth bag can miss one
side.  This is an explicit `K_7^-` model.  Thus a target-free split has at
most three doubly contacting foreign bags.

The response fan is disjoint from itself, not from those foreign bags.  Its
paths may consume or disconnect vertices needed by the model, so fan
existence does not prove the required reassignment.  Section 4 identifies
that first unsupported inference and does not claim a counterexample.  The
exchange statement in Section 5 remains explicitly conjectural.

## Trust boundary

No unresolved assumption remains in Theorems 2.1 or 3.1 beyond their stated
hypotheses and the classical Fan Lemma and Menger theorem.  The model
discussion additionally uses the established `HC_6`.  The note does not
synchronise boundary partitions with model labels, prove the proposed
fan-to-model exchange, eliminate the order-eight/order-nine residue, or
prove the `K_7^-` six-colour conjecture or `HC_7`.  No computer-assisted
claim is made.
