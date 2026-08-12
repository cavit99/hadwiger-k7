# Internal self-audit: centre-anchored lobe normal form

**Verdict:** **GREEN as a self-check.**  The direct degree-eight bypass,
the opposite four-coordinate singleton responses, the order-seven/eight
component localisation, and the cutvertex-lobe normal form are correct at
the pinned revision.  The note correctly stops before model-label
allocation and does not claim closure of the eight-coordinate branch.

This audit was written by the same agent as the theorem.  It is not a cold
independent audit and is not external peer review.

## Exact revision

The checked source is
[`hc7_k7minus_centre_anchored_lobe_normal_form.md`](hc7_k7minus_centre_anchored_lobe_normal_form.md),
with SHA-256

```text
4188e79d174aeaaad67bfa763883f01cfb8bd3af45807eac6c87af66373be609
```

The direct dependencies were checked at these revisions:

```text
2558204c09967912132cc27d321bf863ecae1878d89e2c4595606917edae76a9  active/hc7_k7minus_five_centre_model_anchored_visibility.md
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  results/hc7_k7minus_five_centre_common_matching_reduction.md
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd  results/hc7_k7minus_exceptional_neighbourhood_completion.md
4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29  results/hc7_low_degree_exterior_component_bounds.md
aefcb5164c4122bfb142b7cbbbc31f4d4154cb5c632fe454510e358a510843d8  results/hc7_k7minus_model_anchored_appendage_ownership.md
```

The visibility source has a separate cold GREEN audit.  Each promoted
dependency in `results/` has a separate GREEN internal audit.

## 1. Direct singleton response

The canonical common-matching colouring `c_z` is a proper colouring of
`G-e_z`: after all five matching edges are restored, `e_z` is its only
monochromatic edge.  Deleting `z` therefore leaves a proper colouring.

The named far branch set is disjoint from the containing branch set and
anticomplete to the original side, hence in particular anticomplete to
`z`.  It lies outside `N[z]`.  Thus `N(z)` is an actual separator, and it
has order eight because `z` is a degree-eight centre.  An extension of the
same equality partition through the singleton closed shore would align and
glue to `c_z|G-z`, contradicting `chi(G)=7`.

The star-contraction construction uses one colour on the independent
triple `I_z` and five distinct further colours on its complement.  The
six-block shape `3+1+1+1+1+1` is therefore exact.  No connectedness of the
containing bag after deleting `z` is used in this argument.  The original
model remains literally unchanged; the theorem does not assert that the
singleton is itself a valid two-piece split of that bag.

## 2. The opposite four-coordinate family

Every other centre is outside `N[z]`, since the five centres are
independent.  For a nonempty signature supported on their four matching
edges, every monochromatic restored edge has such an exterior centre as an
end.  No monochromatic edge is therefore wholly contained in `N[z]`, and
the signature colouring restricts properly to the singleton closed shore.

If its boundary partition also extended through `G-z`, the two closed
shore colourings would glue.  This verifies the orientation and rejection
claim for all fifteen nonempty signatures.  The block-count check is also
exact: every colouring of `G-z` uses all six colours on `N(z)`, while the
colour of `z` is unavailable on `N(z)` in every colouring of the singleton
closed shore.  The two complete boundary languages are disjoint.

## 3. Component localisation

The far bag makes `G-N[z]` nonempty.  The audited degree-eight component
bound gives at most two components, and all four other centres lie in
their union.  Pigeonhole therefore places at least two centres in one
component `Q`.

Its full neighbourhood `T` is contained in `N(z)` and separates `Q` from
`z`.  Seven-connectivity gives `|T|>=7`; degree eight gives `|T|<=8`.
The fixed edge `e_z` has ends `z` and `x_z in N(z)`, so neither lies in
`Q`; consequently its canonical colouring is proper on `Q union T`.
For a signature supported on centres in `Q`, deleting `Q` removes one end
of every monochromatic edge, so the colouring is proper on the opposite
shore.  Gluing proves the two rejection assertions.  This verifies the
claimed response square without asserting that the component respects the
branch-set partition.

## 4. The cutvertex hull

Let `W` be the component of `R-z` containing the connected set `R-Y`.
Every other component lies wholly in `Y-z`.  Because `R` is connected,
each component of `R-z` has a neighbour at `z`.  Hence `R-W` is connected,
contains `z`, has connected complement `W`, remains anticomplete to the far
bag, and carries the same centre-edge response.  Global side-order
minimality forces `Y=R-W`.

Choosing one `z`-neighbour in each component of `R-z` gives an independent
set in `N(z)`.  The audited identity `alpha(G[N(z)])=3` permits at most
three components: one exterior component `W` and at most two lobes.  With
two lobes, the three representatives are a maximum independent triple, so
every further neighbour of `z` meets at least one representative.

## 5. Model ownership and the owner circuit

Removing a lobe leaves both the branch set and the centre-bearing side
connected.  A lobe which monopolises no foreign model adjacency can be
omitted.  A lobe which monopolises one label can be moved into that branch
set; its edge to `z` restores the lost adjacency to the reduced containing
bag.  Enlarging the owner bag preserves all its other contacts.  If a
nominally missing `PB` or `PC` adjacency appears, the seven bags give the
target; otherwise the result is a smaller exact model-anchored
centre-bearing configuration.  Thus every lobe owns at least two labels.

Different lobes cannot own the same nonempty `R`-contact set.  The far bag
is owned by neither lobe because all its `R` contacts lie outside the side.
If a lobe contained another centre, that centre's singleton-signature
colouring would make the lobe itself a smaller centre-bearing configuration.
These observations verify items 1 and 2 of the normal form.

For the final circuit assertion, a full system of disjoint paths from the
owner contact sets to distinct `z`-neighbours partitions the lobe into
connected pieces which can be transferred to the respective owner bags.
This again yields the target or a smaller configuration.  Its failure is
exactly a Rado independent-transversal deficiency in the strict gammoid
rooted at those `z`-neighbours.  An inclusion-minimal deficient family has
rank one less than its order, and Menger gives the separator of that order.
A singleton family cannot be deficient in a connected lobe.  The circuit
statement is therefore correct.

## 6. Trust boundary

The minimum is taken only among sides containing the centre corresponding
to their operation.  It consequently excludes centres from lobes, but it
does not exclude a noncentre matching mate.  Using that mate's response
would give a smaller side outside the restricted class.  Conversely,
minimising over all endpoint-bearing sides loses the assertion that the
minimum retains a degree-eight centre.  The quantifier table in the source
records this distinction correctly.

The bounded bypass is a real gain but is not a terminal theorem.  At the
full singleton boundary the two shore languages cannot share a partition,
and on the component boundary no proved theorem assigns an operation label
to a prescribed exact-model branch-set contact.  The source therefore
correctly records model allocation or strict component descent as the
first unsupported inference.  No gap was found in the proved reduction.
