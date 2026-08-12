# Cold internal audit: centre-anchored lobe normal form

**Verdict:** **GREEN.**  The bounded centre-side bypass, the centre-lobe
decomposition, the pairwise disjoint owner sets, and the owner-circuit
conclusion are valid at the pinned revision.  No gap was found.  The source
correctly records that the result does not eliminate the bounded
model-allocation residue.

This audit was performed independently of the proof's author within the
project.  It is internal review, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_centre_anchored_lobe_normal_form.md`](hc7_k7minus_centre_anchored_lobe_normal_form.md),
with SHA-256

```text
4188e79d174aeaaad67bfa763883f01cfb8bd3af45807eac6c87af66373be609
```

The direct dependencies were checked at the revisions recorded in the
adjacent self-audit.  This cold audit concentrates on the two points most
liable to a quantifier or ownership error.

## 1. Localisation of the other centre edges

The common-matching theorem supplies one matching `M` and one colouring for
each nonempty equality signature.  If
`J subseteq M-{e_z}`, every monochromatic restored edge has its centre end
in `Z_0-{z}`.  Centre independence puts all four of those ends outside
`N_G[z]`; hence no defect survives in the induced singleton shore.  This
checks all fifteen signatures simultaneously and does not assume that their
boundary partitions are distinct.

The far branch set proves that `G-N_G[z]` is nonempty.  Its at-most-two
component bound and the presence of the other four centres put at least two
in one component `Q`.  For every signature supported on centre edges whose
centre ends lie in `Q`, deleting `Q` removes every monochromatic edge, so the
restriction to `G-Q` is proper.  The canonical `e_z` defect is absent from
`G[Q union N(Q)]`, because `z` is outside that shore and its mate lies in
`N(z)`.  Seven-connectivity gives the claimed boundary order seven or eight.
Thus the component localisation is literal; it does not exchange the
matching coordinates or colourings.

## 2. Minimal centre-bearing hull

Let `W` be the component of `R-z` containing the connected nonempty set
`R-Y`.  Every other component of `R-z` lies inside `Y-z` and meets `z`, as
`R` is connected.  Therefore `R-W` is a connected centre-bearing side with
connected complement `W`, is contained in `Y`, remains anticomplete to the
named far bag, and carries the same rejected centre response.  Global
minimality forces `Y=R-W`.

One `z`-neighbour from each component of `R-z` is an independent set inside
`N(z)`.  The exact exceptional-neighbourhood identity `alpha(N(z))=3`
therefore leaves the component `W` and at most two additional lobes.  The
maximum-independent-set assertion in the two-lobe case follows directly.

## 3. Owner sets really are pairwise disjoint

For a foreign label `L`, put

```text
C_L = N_G(L) cap R.
```

Because `R` is a universal branch set of the exact model, `C_L` is nonempty
for each of the six foreign labels.  By definition,

```text
L in Lambda(A_i)  if and only if  C_L subseteq A_i.
```

Distinct lobes are distinct components of `R-z` and hence are disjoint.  If
one label belonged to both `Lambda(A_i)` and `Lambda(A_j)`, the same nonempty
set `C_L` would be contained in the empty intersection `A_i cap A_j`, a
contradiction.  This proves pairwise disjointness without an unstated
uniqueness choice.

The named far label `D` is not an owner: its required contact with the
universal bag `R` is nonempty, while anticompleteness to `Y` puts every such
contact in `R-Y subseteq W`, not in a lobe.

If a lobe owns no label, deleting it from `R` preserves every required
foreign contact.  If it owns exactly one label `L`, moving the whole lobe to
the `L`-bag preserves connectedness, and an edge from the lobe to `z`
restores the `L`--`R` model adjacency.  All other required contacts survive.
Any newly created nominally missing `PB` or `PC` adjacency yields the target;
otherwise the model remains exact and the centre-bearing side is strictly
smaller.  Thus every lobe owns at least two labels.  These transfers use
ordinary, not necessarily spanning, minor models exactly as stated.

A second centre in a lobe would make that lobe a smaller configuration for
its own singleton-signature response: deleting the lobe removes the centre
end of the sole defect, while the same far bag and connected split remain.
Thus centre-freeness is also justified.

## 4. Owner circuit

A full family of disjoint `B_A`--`A_L` paths, one for each owner label and
with distinct starts, can be extended to a connected partition of the
connected lobe, rooted at those paths.  Moving the parts to their respective
owner bags preserves their connectivity, attaches each part to its owner,
and uses its `B_A` endpoint to restore adjacency to `R-A` through `z`.
This again gives either the target or a smaller configuration, so the full
labelled linkage is impossible.

Apply the independent-transversal theorem to the strict gammoid on the
vertices of `A` reachable by vertex-disjoint paths from `B_A`, with the
owner contact sets `A_L` as the family of possible representatives.  An
inclusion-minimal deficient owner family `I` has rank exactly `|I|-1`, since
each proper subfamily is independent.  Vertex Menger then supplies a set of
that order meeting every path from `B_A` to the union of its owner contact
sets.  A singleton cannot be deficient because `A` is connected and both
endpoint sets are nonempty.  Since the far label is excluded, the bounds
`2<=|I|<=5` are correct.

## 5. Scope

The minimisation class excludes other centres from lobes but does not exclude
noncentre matching mates.  The source does not silently promote that weaker
fact to coordinate-freeness.  Nor does it identify operation signatures with
model labels.  Those are precisely the recorded residual quantifier and
allocation problems.

No unresolved assumption was found in the proved normal form.  It remains a
conditional internal theorem and does not prove the `K_7^-` six-colour
conjecture or `HC_7`.
