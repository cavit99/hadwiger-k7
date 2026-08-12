# Internal self-audit: degree-eight centre cube interface

**Verdict:** **GREEN as a self-check.**  The block-count separation at the
singleton boundary, the fifteen opposite centre-edge responses, and the
order-seven/eight component localisation are correct at the pinned
revision.  The result is a labelled bounded reduction, not an elimination
of the singleton or of the eight-coordinate branch.

This audit was written by the same agent as the theorem.  It is not a cold
independent audit and is not external peer review.

## Exact revision

The checked source is
[`hc7_k7minus_degree_eight_centre_cube_interface.md`](hc7_k7minus_degree_eight_centre_cube_interface.md),
with SHA-256

```text
7ebbc04ccdac9488088e3620ea949a5f08bdcc659fcffd5316e934cdc99c9292
```

The proof is computation-free.  Its direct imported statements were checked
at these revisions:

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  results/hc7_k7minus_five_centre_common_matching_reduction.md
2558204c09967912132cc27d321bf863ecae1878d89e2c4595606917edae76a9  active/hc7_k7minus_five_centre_model_anchored_visibility.md
4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29  results/hc7_low_degree_exterior_component_bounds.md
7cc1da7567f05e10bb7089c4b6dcd0706e9a0daa406063e7ba986d3d283c9512  results/hc7_k7minus_model_anchored_response_hull.md
```

The first, third and fourth dependencies have separate GREEN internal
audits.  The active visibility theorem has a GREEN self-audit and a separate
cold audit at its current revision.

## 1. Singleton block counts

Let `S=N_G(z)`.  In any proper six-colouring of `G-z`, failure to use one
of the six colours on `S` would allow that colour to be assigned to `z`.
Thus every exterior partition has exactly six blocks.  In a proper
six-colouring of `G[N_G[z]]`, the colour on `z` is absent from `S`, so the
boundary has at most five blocks.  Equality partitions with different block
counts cannot agree.  Lemma 2.1 therefore separates the complete shore
languages, not merely the canonical pair of colourings.

The gluing steps use only equality partitions.  If two six-colourings induce
the same partition on a common boundary, the bijection between the colours
used on that boundary extends to a permutation of the six-colour palette.
After that permutation the colourings agree vertexwise on the boundary and
glue.  No unproved identification of named colours is used.

## 2. The opposite four-coordinate family

The common-matching theorem gives one literal matching `M` and, for every
nonempty `J subseteq M`, a colouring of `G-M` whose monochromatic restored
matching edges are exactly `J`.  For `J subseteq M-{e_z}`, every such edge
has its centre end in `Z-{z}`.  Independence of the five centres puts all
four of those centre ends outside `N_G[z]`.  Hence restriction to
`G[N_G[z]]` deletes at least one end of every defect; the restriction is
proper.  The selected edge `e_z` is not a defect in these colourings.

Conversely, the canonical singleton-signature colouring has only `e_z`
monochromatic after restoring `M`, and deleting `z` makes it proper on
`G-z`.  The imported star-contraction construction gives precisely one
triple block `I_z` and five singleton blocks on `S`.  These checks establish
Theorem 3.1 and its exact `3+1+1+1+1+1` assertion.

The theorem correctly does not claim that the fifteen boundary partitions
are distinct.  Their labels are operation signatures on matching edges, not
visible boundary colours.

## 3. Component localisation

Since `d_G(z)=8` and the host has at least 25 vertices,
`O=G-N_G[z]` is nonempty.  The imported degree-eight theorem gives at most
two components.  All four other independent centres lie in `O`, so one
component `C` contains at least two.  Its full neighbourhood `T` is contained
in `S`; it separates `C` from `z`, and seven-connectivity gives
`7<=|T|<=8`.

The sole defect of the canonical colouring is `e_z=zx_z`.  Neither end lies
in `C`, and `z` is absent from `G[C union T]`, so that restriction is proper.
For a nonempty signature supported on centre edges whose centre ends lie in
`C`, deleting `C` removes every monochromatic restored edge, so the opposite
restriction to `G-C` is proper.  Extension of either displayed partition
through the other shore would glue to a six-colouring of `G`; the rejection
claims in Theorem 4.1 follow.

Because `T` is a subset of the eight-set `S` and has order at least seven,
it is either `S` or `S-{t}`.  Restricting the canonical partition gives the
three shapes recorded in (4.5).  In each opposite colouring, `z` remains in
`G-C`, is adjacent to every vertex of `T`, and its colour is absent from
`T`; hence those partitions have at most five blocks.  This checks the last
block-count assertion.

## 4. Model provenance and trust boundary

The construction only restricts already fixed colourings and selects a
component of `G-N_G[z]`.  It neither changes nor reselects the exact
`K_7^vee` model, its named far branch set, or the complement inside the
containing branch set.  Corollary 4.2 therefore preserves the stated model
provenance literally.

The two or four additional coordinates are the original five-centre matching
edges.  They are not asserted to be further edges of the induced
eight-coordinate forest, and their boundary partitions need not differ.
Nothing proved here converts an operation signature into a foreign
branch-set contact.  The source records this as the first unsupported
inference and does not claim a forbidden minor, a common partition at the
full singleton boundary, Conjecture 21, or `HC_7`.

No material gap was found in the stated conditional reduction.  Promotion
would require an independent cold audit.
