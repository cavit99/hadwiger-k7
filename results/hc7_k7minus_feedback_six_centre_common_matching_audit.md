# Internal audit: six centres in the bounded-feedback branch

**Verdict:** GREEN for Theorems 2.1, 3.1 and 5.1, Proposition 4.1, and the
stated scope.  This is a separate internal mathematical audit, not external
peer review.

## 1. Exact revision

The audited source is
[`hc7_k7minus_feedback_six_centre_common_matching.md`](hc7_k7minus_feedback_six_centre_common_matching.md),
with SHA-256

```text
400a3ecedfbff8dbed58fe1ccdb380a443452828753195ca1b08eaf09fd9cc06
```

This revision includes the boundary-crossing matching in Theorem 5.1.

The theorem assumes the audited critical-host conclusions and the
bounded-feedback outcome of the separately audited coordinate-growth
theorem.  In particular, there are at least twenty-five degree-eight
vertices, the host has no literal `K_5`, and deleting a set `T` of at most
fourteen vertices leaves a forest.

## 2. Six independent centres

At least eleven degree-eight vertices lie outside `T`.  Their induced graph
is a subgraph of `G-T`, hence a forest and therefore bipartite.  A larger
bipartition class has order at least six and supplies the independent set
`Z`.

Global `K_5`-exclusion makes every degree-eight vertex exceptional.  The
audited exceptional-neighbourhood theorem therefore supplies an independent
triple in each selected neighbourhood.  Its five-vertex complement is the
candidate set `R_i`.

The Hall calculation is exact.  Every subfamily of at most five candidate
sets has union of order at least five.  A deficient family must consequently
contain all six sets, and their union then has order at most five.  Since
every set has order five, all six are one common set `R`.

In that case the six centres and five common candidates span a `K_{6,5}`
subgraph.  The four paired bags `{z_i,r_i}`, the two singleton centres and
the fifth singleton candidate are connected and mutually adjacent except
for the pair of singleton centres.  This is an explicit seven-bag
`K_7^-` model.  Target exclusion proves Hall's condition.  The resulting
representatives are distinct and avoid `Z`, because `Z` is independent;
the selected centre edges therefore form a matching of order six.

## 3. Chromatic and signature conclusions

For every nonempty matching subset `J`, both `G-J` and `G/J` are proper
minors and hence at most six-chromatic.  If either admitted a five-colouring,
expand contractions when necessary and recolour the independent centres
indexed by `J` with one fresh sixth colour.  This restores every deleted
edge and six-colours `G`.  Thus both chromatic numbers are exactly six.

Expanding a six-colouring of `G/J` onto `H=G-M` makes precisely the edges
of `J` monochromatic.  Matching edges outside `J` remain literal edges
between different contraction bags.  Every nonempty signature is therefore
realised, while an empty signature would six-colour `G` after restoration.

For a singleton signature, contracting the centre together with an
independent neighbourhood triple makes that triple monochromatic.  The five
remaining neighbours avoid its colour and must use all five other colours.
Extending the centre with the selected representative's colour makes the
selected centre edge the unique monochromatic matching edge.

For a colouring expanded from `G/J`, a centre outside `J` is unsaturated
because its own displayed colour is absent from its neighbourhood.  If
every centre indexed by `J` were also unsaturated, those independent
centres could each be assigned a missing neighbourhood colour, producing a
six-colouring of `G`.  This verifies the exact nonempty saturation inclusion.

Seven-connectivity implies seven-edge-connectivity, so deleting at most six
matching edges leaves a connected graph.  Contraction preserves
connectedness.  `HC_6` supplies a `K_6` minor in each exactly
six-chromatic graph, and connectedness allows unused vertices to be
absorbed.  Expanding contracted matching edges inside their bags gives the
claimed spanning co-bagged models, including one model co-bagging all six
pairs when `J=M`.

## 4. Forest placement

Every selected centre lies outside `T`.  If its representative also lies
outside `T`, their selected edge is a tree edge of `G-T` and hence a bridge
there.  The selected edges form a matching, although disjointness is more
than is needed for the component count.  Exactly `6-t` selected edges have
both ends outside `T`, so deleting them increases the number of components
of the forest by exactly `6-t`.  This proves the identity for `c(H-T)`.

## 5. Boundary-crossing matching

Theorem 5.1 makes a separate, stronger placement choice.  For a selected
centre `z outside T`, its neighbours outside `T` are independent: an edge
between two of them would form a triangle in the forest `G-T`.  Their
number is therefore at most three, since the exceptional neighbourhood
has independence number three.  Thus every selected centre has at least
five neighbours in `T`.

Hall's condition for the six sets `N(z_i) cap T` can fail only on the full
six-set family.  In that case their union has order at most five; since
each set has order at least five, they are a common five-set.  The resulting
`K_{6,5}` subgraph gives exactly the seven-bag model already checked in
Section 2.  Hence distinct representatives in `T` exist and their centre
edges form a matching.

The deletion/contraction chromatic argument, exact signature construction,
saturation inclusion and spanning-model lift use only this matching and the
independence of its centre ends.  They therefore apply unchanged.  In
particular, exact singleton signatures and the saturation inclusion survive
the new choice.  Since every selected edge has one end in `T`, deleting
`T` from the matching-deleted graph leaves `G-T` literally unchanged.

The audit also checks the stated loss of information: Hall's representatives
in `T` have not been shown to avoid a chosen independent neighbourhood
triple.  Thus the monochromatic-triple/rainbow-complement construction from
Theorem 3.1 cannot be transferred to the new matching.  The source keeps
the two matchings distinct and makes no such inference.

## 6. Trust boundary

No higher vertex-connectivity follows from deleting either six-edge
matching.  For the original matching, the representatives need not lie on
one prescribed side of `T`.  For the boundary-crossing matching, the
spanning `K_6` model still need not respect the components of `G-T`.
Thus the theorem does not yet couple its complete punctured signature cube
to the feedback decomposition strongly enough to prove `K_7^-`, the
six-colour conjecture, or `HC_7`.
