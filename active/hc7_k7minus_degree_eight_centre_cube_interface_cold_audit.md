# Cold internal audit: degree-eight centre cube interface

**Verdict:** **GREEN.**  The exact order-eight singleton interface and the
order-seven/eight component-localised response family are correct at the
pinned revision.  The result is a bounded, operation-labelled reduction; it
does not eliminate the singleton or identify the operation labels with
branch-set labels.

This audit was carried out by an agent other than the author of the theorem.
It is an internal cold audit, not external peer review.

## Exact revision

The checked source is
[`hc7_k7minus_degree_eight_centre_cube_interface.md`](hc7_k7minus_degree_eight_centre_cube_interface.md),
with SHA-256

```text
7ebbc04ccdac9488088e3620ea949a5f08bdcc659fcffd5316e934cdc99c9292
```

The direct imported statements were checked at the following revisions:

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43  results/hc7_k7minus_five_centre_common_matching_reduction.md
2558204c09967912132cc27d321bf863ecae1878d89e2c4595606917edae76a9  active/hc7_k7minus_five_centre_model_anchored_visibility.md
4ee48c6d71c994b166b29dcd969d64c3526e6b6b75fa8a849fae834cf95eea29  results/hc7_low_degree_exterior_component_bounds.md
7cc1da7567f05e10bb7089c4b6dcd0706e9a0daa406063e7ba986d3d283c9512  results/hc7_k7minus_model_anchored_response_hull.md
```

The common-matching and low-degree results have separate GREEN internal
audits.  The centre-visibility theorem has both a self-audit and a separate
cold GREEN audit at the displayed revision.

## 1. The full singleton boundary

Write `S=N_G(z)`.  Every proper six-colouring of `G-z` uses all six colours
on `S`; otherwise a missing colour extends to `z`.  Every proper colouring
of `G[N_G[z]]` uses at most five colours on `S`, because the colour assigned
to `z` is forbidden at every vertex of `S`.  The two complete boundary
languages therefore have different block counts and are disjoint.

The canonical singleton-signature colouring has only `e_z=zx_z`
monochromatic after restoration of the five matching edges.  Deleting `z`
makes it proper, and the star-contraction construction gives exactly one
triple block and five singleton blocks on `S`.  Thus the claimed
`3+1+1+1+1+1` partition is exact.

## 2. The opposite four-coordinate family

Every other centre lies outside `N_G[z]`, since the five centres are
independent.  In a signature supported on the other four centre edges, each
monochromatic restored edge therefore has an endpoint outside the singleton
closed shore.  Restriction to `G[N_G[z]]` is proper.  If its boundary
partition also extended through `G-z`, a permutation of the six colours
would align the two shore colourings and glue them to a proper six-colouring
of `G`.  This checks all fifteen nonempty signatures; it does not require
their induced boundary partitions to be distinct.

## 3. Localisation on one exterior component

The exterior `G-N_G[z]` is nonempty and has at most two components.  All
four other centres lie there, so some component `C` contains at least two.
Its boundary `T=N_G(C)` is contained in the eight-set `S`, and it separates
`C` from `z`; seven-connectivity gives

\[
                         7\leq |T|\leq8.
\]

Neither endpoint of `e_z` lies in `C`, so the canonical colouring restricts
properly to `G[C\cup T]`.  For every nonempty signature supported on the
centre edges whose centre ends lie in `C`, deleting `C` removes an endpoint
of every monochromatic restored edge, so the corresponding colouring is
proper on `G-C`.  The same gluing argument proves rejection in both
directions.  At least two centre edges lie in `C`, yielding the asserted
punctured response square.

Since `T` is either `S` or `S-{t}`, the three displayed restrictions of the
canonical partition are exhaustive.  In each opposite-shore colouring,
`z` is present and adjacent to every vertex of `T`, so its colour is absent
from `T`; the boundary has at most five blocks.  The stated exceptional
five-block-versus-five-block case is therefore the only case not separated
automatically by block count.

## 4. Provenance and limitation

The proof only restricts fixed colourings and selects a component of the
fixed graph.  It does not alter the exact `K_7^\vee` model, its named far
bag, or any branch set.  The additional coordinates are edges of the
five-centre matching; the source correctly does not identify them with
edges of the separate eight-coordinate forest.

The result also correctly stops before terminalisation.  Operation
signatures need not induce distinct boundary partitions, and no proved
statement assigns them to prescribed model-bag contacts.  No unsupported
minor construction, common-partition conclusion, or closure of the
eight-coordinate branch was found.
