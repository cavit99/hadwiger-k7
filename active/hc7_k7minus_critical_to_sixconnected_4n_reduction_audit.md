# Internal audit: critical host to a six-connected `4n` quotient

**Verdict:** GREEN.  The critical contraction, exact chromaticity, density
calculation and six-colouring trace are valid at the pinned revision.  The
universal six-connected extremal statement is correctly presented only as
an unproved sufficient condition.

**Audited source:**
`active/hc7_k7minus_critical_to_sixconnected_4n_reduction.md`

**SHA-256:**

```text
ac3a9fcf81549c9bb3f7a6e789b240040b1f63bf40cae59b4ac61fbd8981d0a2
```

This is a separate internal mathematical audit, not external peer review.
No finite computation is used in the reduction.

## 1. Critical-host hypotheses and the selected edge

Minor-minimality is used correctly.  Every proper minor of `G` remains
`K_7^-`-minor-free, so it must be six-colourable.  In particular, deleting
one vertex and then restoring it shows `chi(G)<=7`; non-six-colourability
therefore gives `chi(G)=7`.  Mader's theorem gives seven-connectivity, in
the modern form now cited explicitly by the source, and the hypotheses of
the two promoted repository inputs then match exactly.

The checked input revisions are

```text
6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67  results/hc7_k7minus_degree7_rooted_helper_closure.md
06d35e4059848517e65e48b04c592e948bbc8e4407501de75520cfa3e9d22844  results/hc7_k7minus_sixconnected_degree_eight_low_codegree.md
```

Together with Mader's theorem, the first input gives minimum degree eight,
coefficient-four density, and at least one degree-eight vertex.  The host is
seven-connected and hence six-connected, so the second input applies
directly and supplies, at any chosen degree-eight vertex `v`, an incident
edge `vx` with

```text
|N_G(v) intersect N_G(x)| <= 3.
```

There is no neighbourhood-completion, independence-number, or compatibility
assumption in this step.  The selected-edge input is itself GREEN within its
stated finite-computation trust boundary.

## 2. Connectivity and density after contraction

Contracting one edge of a seven-connected graph leaves a six-connected
graph.  Indeed, a cut of order at most five in the quotient either lifts
unchanged, or, if it contains the contracted vertex, lifts after replacing
that vertex by the two ends of the edge, giving a cut of order at most six
in `G`.

Writing `c=|N_G(v) intersect N_G(x)|`, simplification after contraction
removes exactly the edge `vx` and one duplicate edge for each common
neighbour.  Consequently

```text
|V(H)| = |V(G)|-1,
|E(H)| = |E(G)|-1-c >= 4|V(G)|-4 = 4|V(H)|.
```

Target-freeness passes to the quotient because the minor relation is
transitive.  These arguments verify items 1--3 without an exceptional
small-order case.

## 3. Exact chromaticity and the universal palette trace

The quotient `H` is a proper minor, and hence is six-colourable.  If it
were five-colourable, split the contracted vertex into `v,x`, initially
give both the old colour, and give `v` a new sixth colour.  Since
`N_G(v)={x} dot_union T`, this is a proper six-colouring of `G`, a
contradiction.  Therefore `chi(H)=6` exactly.

Now fix any proper colouring of `H` from a six-colour palette and let
`alpha` be the colour of the contracted vertex `w`.  Every vertex of `T`
is adjacent to `w`, so none has colour `alpha`.  If one of the other five
palette colours were absent from `T`, splitting `w`, assigning `alpha` to
both ends, and recolouring `v` with that absent colour would again
six-colour `G`.  Thus all five other colours occur on `T` in every such
colouring.  The source now says explicitly that the intermediate graph is
the edge-deletion graph `G-vx`, so there is no notation ambiguity.

## 4. Conditional implication and scope

Items 2 and 3 immediately show that the universal statement

> every six-connected `J` with `|E(J)|>=4|V(J)|` has a `K_7^-` minor

would exclude the quotient and hence every minor-minimal counterexample to
Conjecture 21.  The source correctly observes that only quotients carrying
the specified split and colour-surjectivity data need be excluded.

This is a new sufficient conditional refinement alongside the older
seven-connected `4n-2` target, not a theorem logically stronger than it.
The universal statements are incomparable: the present condition weakens
seven-connectivity to six-connectivity but raises the density requirement
by two edges.  The source now states this distinction explicitly and does
not claim the six-connected extremal statement, Conjecture 21, or a
`K_7^-` minor has been proved.
