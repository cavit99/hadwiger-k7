# Internal audit of the global five-root palette alternative

Audited file:
`active/hc7_k7minus_five_centre_t5_global_palette.md`

Audited SHA-256:

```text
b26f9f0d12822f93af55e3aa566fc75b985dcb5a17daa4ea2b329c8efea274c3
```

**Verdict:** **GREEN** for every stated theorem, lemma, exact chromatic
completion, and limitation of this revision.

This is a hash-pinned internal mathematical audit, not external peer review.
The result is an unbounded reduction of the minimally infeasible five-root
row.  It does not close that row or construct a `K_7^-` minor.

## 1. Dependencies and hypothesis match

The audit checked the following exact local revisions.

| input | source SHA-256 | audit SHA-256 |
|---|---|---|
| five-centre two-cut reduction | `1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a` | `d01183c936d79ea2e07f956c2e89f7291df9cc28a5dab3dda6b093c8a69c4ea3` |
| exceptional-neighbourhood theorem | `fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd` | `26be60e5389ec356dfd183d8a39e2a713e6db3695c807674daf7797fa1fcae2b` |
| four-root palette transfer | `1f91f4396e090497a576fd63c1462762b5ab5f95151a06632a8f63584caee1a9` | `b366bbd22bd3b37db844db80d14c80b909a49e4ee2c3681767ac0b1c916ce668` |
| exact boundary matching theorem | `e8c53c8255f7e6fe62b014e6909f4d12501e7994691d99e6b749ad9b2b9a3fd6` | `bb913b8a6af2aa830567c87d6350246885743195514fb6fcc1db4af49025d3ee` |

The two-cut reduction supplies the two full components, opposite exact
boundary responses, the nonedge `pq`, minor-minimal six-colourability and
the degree-eight centres.  The exceptional-neighbourhood theorem supplies
both `K_4`-freeness and independence number three at every centre.  These
are exactly the extra hypotheses used by the four-root transfer to infer

\[
 c_z\ge4,\qquad N_D(z)\text{ is a clique of order at most three}.
\]

The draft was amended before this audit to state those neighbourhood facts
explicitly; previously they were only implicit in the phrase
"equality-side transfer".  Feasibility after deleting each individual root
also implies feasibility for every smaller root set, so it matches the
minimal-infeasibility hypothesis in the transfer corollaries.

## 2. Universal equality-side palette

For `A=Z-\{z\}`, the equal-response transfer gives a closed `D`-side
colouring with `A` monochromatic, the poles monochromatic in a different
colour, and `z` avoiding the pole colour.  After aligning the two boundary
colours with an arbitrary permitted `C`-side colouring, the only unchecked
edges are the edges from `z` to `C`.

If `z` receives the root colour, those edges are proper because the fixed
`C`-side colouring originally assigns that colour to `z`.  Otherwise its
colour belongs to the four colours whose names may be permuted while the
two boundary colours remain fixed.  Any missing free colour on `N_C(z)`
would therefore permit a gluing.  This verifies that all four free colours
occur on every `N_C(z)` in the same fixed colouring.  No synchronization of
five different transferred colourings is asserted or needed.

Together with `d_z\in\{2,3\}` and `rho_z\in\{0,1\}`, the exact identity
`c_z+d_z+rho_z=8` gives precisely the four displayed profiles.  The
boundary matching theorem has matching number two; since each centre has
at most one pole edge, it gives `2\le b\le5`, both pole labels, and exactly
the stated `b=2` and `b\ge3` alternatives.

## 3. Transfer minor and seven-chromatic completions

The distinct-response transfer supplies three pairwise adjacent connected
sets: the component containing `Z-\{z\}` and the two halves of a `p`--`q`
path.  Contracting them produces the triangle `k_z a_z b_z`.  The minor is
proper because the opposite nonempty shore remains literal while vertices
on the witness shore are contracted or deleted.  Pullback assigns three
distinct colours to `Z-\{z\}`, `p`, and `q`.

In any six-colouring of `M_z`, align the triangle colours with the fixed
distinct response on `D`.  The root colour is absent from `N_D(z)`.  If the
three free colours do not all occur on `N_D(z)`, an arbitrary permutation
of those free colour names sends the colour of `z` to a missing contact
colour and glues the shores.  Hence failure of the rainbow outcome forces
`z` to copy one of the two pole bags in every six-colouring of `M_z`.

When `rho_z=1`, the actual centre--pole edge excludes the incident pole
bag's colour.  Thus `z` always copies the opposite bag, the corresponding
edge is absent, and adding it excludes every six-colouring.  Recolouring
`z` with a fresh seventh colour proves the upper bound seven.  Therefore
the augmented graph is exactly seven-chromatic.

When `rho_z=0`, adding every missing edge from `z` to the two pole bags
similarly excludes every six-colouring.  At least one edge is missing,
since otherwise the known six-colouring of `M_z` could not make `z` copy a
pole bag.  Again a fresh colour on `z` proves exact seven-chromaticity.

For the one-edge completion, the standard critical-edge Kempe argument
joins its equal-coloured endpoints in the bichromatic subgraph for each of
the other five colours.  For a free colour, neither of the other two
triangle vertices has an allowed path colour, so every internal vertex of
the resulting path lies in `C`.  A pre-audit wording slip naming the second
excluded triangle colour always `beta` was corrected: it is the colour of
the pole bag different from `v_z`, which can be either pole colour.

## 4. One-colouring rainbow connections

If a rainbow contact vertex of colour `gamma` were outside the
`epsilon`--`gamma` component containing the pole of colour `epsilon`, a
Kempe interchange on the component containing that contact would leave all
seven boundary vertices fixed and remove `gamma` from the contact triangle.
The other contact vertices originally have the other two free colours, so
none is changed to `gamma` by this interchange.

In every six-colouring of `M_z`, the centre cannot have the root colour or
either pole colour, since each is absent from the original rainbow triangle
and would permit gluing.  It therefore has a free colour, whose name can be
sent to `gamma` while the triangle boundary colours remain fixed.  Gluing
to the altered `D`-colouring is then proper, a contradiction.  This proves
all six pole--triangle connections for each centre in one fixed colouring,
and hence the thirty simultaneous incidences claimed in Theorem 5.2.

## 5. Fan core and exact scope

If `b\ge3`, two centres share a pole neighbour.  Since deleting one vertex
from a seven-connected graph leaves a six-connected graph, the fan lemma
gives three internally disjoint paths from the second centre to the first
centre's contact triangle.  Deleting the common fan origin from the arms
makes three disjoint connected sets.  Their triangle endpoints make the
three sets pairwise adjacent; both centre singletons meet every arm, and
only the centre--centre adjacency is absent.  Thus the five displayed bags
are exactly a `K_5^-` minor core, and the shared pole sees both centre bags.

The proof correctly does not use that pole as a sixth branch set: an
unrestricted fan arm may contain it.  Nor does it produce two disjoint
connected sets meeting all three arms.  In the completion alternative, the
added edge is not asserted to be realized by a path in the original graph.
These are the two explicit unresolved geometric steps.  No terminal
`K_7^-` conclusion, colouring of `G`, or closure of the order-at-least-eight
two-cut branch follows from this theorem alone.

No unresolved assumption or proof gap remains inside the theorem as now
stated.
