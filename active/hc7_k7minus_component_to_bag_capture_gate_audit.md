# Internal audit: response-component branch-bag gate

**Verdict:** GREEN for Theorem 2.1, Corollary 2.2 and Propositions
3.1--3.3.  The source proves an exact portal co-location criterion, closes
the easy co-connected placements, records the use of the common adjacency
to `u,v`, and exhausts every one-component branch-set reassignment.  It
does not prove the remaining portal co-location statement.

**Audited source:**
`active/hc7_k7minus_component_to_bag_capture_gate.md`

**SHA-256:**

```text
d898309beab77fd6fea9a62459f933e9a3974cfe1486bfecd039957e43ccf8a4
```

This is a separate internal mathematical audit, not external peer review.
No finite computation is involved.

## 1. Exact capture equivalence

Let `Y` satisfy item 1 of Theorem 2.1.  Because `x in Y`, the connected
complement `J-Y` lies in one component `W` of `J-x`.  Containment
`Y subseteq A` forces `J-A subseteq W`, and anticompleteness of `D_i` to
`Y` forces the whole portal set `Pi_i` into `W`.  This verifies necessity,
including the fact that the full portal set, rather than one selected
portal, is required.

Conversely, if one component `W` contains both sets, then `J-W` consists of
`x` and all other components of `J-x`.  Every such component has an edge to
`x` because `J` is connected.  Hence `Y=J-W` is connected, nonempty and
proper; the two containments give `Y subseteq A` and `Y` anticomplete to
`D_i`.  This proves sufficiency.

Deleting `Y` removes `x`, the end of the unique monochromatic restored edge
`ux`, so the fixed colouring is proper on the exterior.  Any matching
closed-side boundary partition would glue to a six-colouring of `G`.
The nonempty anticomplete bag `D_i` is outside `Y union N(Y)`, making the
boundary actual.  Seven-connectivity therefore gives the stated lower
bound.

## 2. Co-connected model placements

When `J-x` is connected, the component criterion reduces to the existence
of a named bag missed by `x`.

- For `J=P`, meeting all six clique bags makes `{x}` universal to a fixed
  `K_6` model and gives `K_7`.
- For `J=B` or `C`, exactness makes `P` anticomplete to the whole bag.
- For `J=U_i`, a missed foreign bag gives capture.  If no bag is missed,
  split `U_i` into `{x}` and `U_i-x` and retain the other five clique bags.
  The singleton meets all five.  The residual bag misses exactly those
  clique adjacencies monopolised by `x`; hence zero or one such monopoly
  gives `K_7` or `K_7^-`, respectively.

Thus the claimed lower bound of two monopolised clique labels is exact.
The proof does not claim that two monopolies themselves give the target.

## 3. Common-neighbour incidence

In Proposition 3.2 the seven proposed branch sets are disjoint by
hypothesis.  The four old bags are a clique model.  The dominated-singleton
condition gives both `u-K_j` and `v-K_j` edges through the chosen vertices
of `A cap K_j`; the separate hypothesis gives `x-K_j`.  Finally
`uv,ux,vx` are all edges.  Every one of the twenty-one branch-set
adjacencies is therefore present.

The proposition is only conditional on four bags avoiding `u,v,x`.  It
does not infer that four such bags exist or are met by `A`, and the source
states this limitation.

## 4. Exhausting one-component transfers

For every component `C` of `H[J-x]`, the complement `J-C` is connected
through `x`.  Empty monopoly permits omission of `C`, because every
required portal survives in `J-C`.  A singleton monopoly `{L}` supplies a
literal `C-L` edge; moving `C` to `L` connects the enlarged target, and the
cut edge to `J-C` restores the donor-target adjacency.  All other required
donor adjacencies survive.  A newly created nominally missing edge gives at
least `K_7^-`; otherwise the exact model survives with smaller `J`.

Distinct components cannot own the same nonempty portal set.  Dividing the
required label degree by two gives the component bounds `2,2,2,3` for
`P,B,C,U_i`, respectively.  The source correctly warns that preserving
the original placement of `u` and its named anticomplete bag can forbid
some of these transfers.

## 5. Exact unresolved assumption

None of the proved statements places `J-A` and one full foreign portal set
in the same component of `J-x`.  The common adjacency
`A subseteq N(u) cap N(v)` rules out the four-bag incidence of Proposition
3.2, but a named bag disjoint from `A` may still have edges to every
candidate subside.  Nor do the arguments eliminate a singleton universal
bag or a co-connected universal bag with at least two clique monopolies.

The quoted response-sensitive portal co-location statement is therefore a
conjectural repair, not a proved conclusion.  The source does not claim
component-to-bag capture, the eight-coordinate terminalisation theorem,
Conjecture 21, or `HC_7`.
