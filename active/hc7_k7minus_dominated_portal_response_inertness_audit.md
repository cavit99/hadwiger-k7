# Internal audit: dominated-component response inertness

**Verdict:** GREEN for Theorems 1.1 and 2.1 and for the stated route
nonclosure.  The source proves that the original-coordinate colouring is
improper on both closed shores at the dominated response component, and it
gives the exact critical-triangle Kempe alternative.  It does not prove
that portal co-location is false or eliminate any of the three transition
outcomes.

**Audited source:**
[`hc7_k7minus_dominated_portal_response_inertness.md`](hc7_k7minus_dominated_portal_response_inertness.md)

**SHA-256:**

```text
cf1a4c0ab795c89646caf61ba49d8134208a1569f1dadb8be9909fa79e11a732
```

This is a separate internal mathematical audit, not external peer review.
No finite computation is involved.

## 1. Shore properness

The component `A` lies in `Q=N(u)-{v}` and the dominated mate `v` is
complete to `Q`.  Hence every vertex of `A` is adjacent to both `u` and
`v`, while `u,v` lie outside `A`.  Both are therefore in the literal open
neighbourhood `T=N(A)`.  The edge `uv` lies wholly in the boundary, whereas
`ux` crosses the boundary because `x in A`.

For the signature `{ux}`, the only monochromatic restored edge is `ux`.
Its `A`-end is deleted from `G-A`, so the exterior restriction is proper;
both ends occur in the closed side `G[A union T]`, so the same colouring is
improper there.  The proper exterior restriction does induce an equality
partition on `T`.  If that partition were induced by a proper colouring of
the intact closed side, colour permutation and gluing would six-colour `G`.
Thus it is rejected.

For the signature `{uv}`, the only monochromatic restored edge is `uv`.
Both `G-A` and `G[A union T]` contain that boundary edge and its ends.
Accordingly both restrictions are improper.  An improper restriction is
not a shore colouring and induces no admissible boundary partition for a
gluing argument.  This distinction is the central assertion of Theorem
1.1 and is stated correctly.

## 2. Exact signature language

Colourings of `G-uv` and `G-ux` supply the two singleton signatures on the
common deletion.  The all-proper signature would restore both edges and
six-colour `G`.  Equality on both incident edges would give one colour to
`v,u,x`, contradicting the retained triangle edge `vx`.  Therefore the two
exclusive signatures exhaust all proper six-colourings of the common
deletion graph.

## 3. First Kempe transition

If one Kempe component meets both response families, a shortest sequence
contains adjacent colourings of opposite signatures.  The audited
critical-triangle transition theorem applies with centre `u` and outer
ends `v,x`.  It forces the exact placements

```text
u in D, v,x outside D; or v,x in D, u outside D.
```

In either placement, `D` meets both possible monochromatic restored edges:
the first placement meets `uv` and `ux` at `u`, while the second meets them
at `v` and `x`.  Both response colourings consequently restrict properly
to `G-D`.  The Kempe interchange changes only vertices in `D`, so the two
proper exterior restrictions agree literally on `N(D)` and induce one
common equality partition there.  An intact closed-side extension of that
partition would glue to either exterior and six-colour `G`, proving its
rejection.

If `D` is not dominating, a vertex outside `N[D]` makes `N(D)` an actual
separator.  Seven-connectivity gives order at least seven.  If `D` is
dominating, it is connected and bipartite.  A four-colouring of `G-D`,
together with two fresh colours on `D`, would six-colour `G`, so
`chi(G-D)>=5`.  A `K_6` minor in `G-D`, together with the dominating
connected branch set `D`, would give a `K_7` minor and hence a `K_7^-`
minor.  Thus `G-D` is `K_6`-minor-free; the proved `HC_6` gives
`chi(G-D)<=5`.  Equality follows.  Finally, a `K_6^-` model in `G-D`
together with `D` would give precisely a `K_7^-` model, so the sharper
minor exclusion is valid.

The source says that at least one of the three alternatives holds.  It
does not incorrectly claim exclusivity between the non-dominating and
dominating cases beyond their definitions.

## 4. Spanning model and exact trust boundary

The fixed spanning exact `K_7^vee` model survives on the common deletion by
the aligned dominated-singleton hypothesis.  A colouring or Kempe
interchange does not modify its branch sets.  Spanningness nevertheless
only allocates vertices to bags; it does not make the old-coordinate
restriction proper on either shore, contain a bichromatic transition
component in one bag, identify palette colours with bag labels, or put a
full portal set in the transition component.

The branch-bag criterion requires one component of `J-x` to contain both
`J-A` and a whole foreign portal set.  None of the proved colouring
statements implies this uncoloured topological containment.  The source
therefore records only that the response-pair route has not established
portal co-location.  It does not assert a counterexample, the negation of
portal co-location, the eight-coordinate terminalisation theorem,
Conjecture 21, or `HC_7`.

## 5. Remaining exact alternatives

The smallest positive continuations are accurately listed:

1. align a first transition component with a whole named portal set;
2. eliminate the dominating bipartite subgraph with five-chromatic,
   `K_6^-`-minor-free complement; or
3. supply another operation whose colouring is proper on the intact
   `A`-side.

None follows from the two exclusive signatures or spanningness alone.
