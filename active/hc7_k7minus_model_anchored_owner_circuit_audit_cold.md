# Cold internal audit: model-anchored owner circuits

**Verdict:** **GREEN.**  At the pinned revision, the multi-owner transfer,
the Rado--Menger certificate, all three operation-sensitive outcomes, the
host-boundary estimate and the coordinate--owner orthogonality statement
are correct.  No spanning-model hypothesis is used where the source allows
unused vertices.  The uncontrolled unused-neighbour term is a genuine
remaining obstruction, not a missing step in a claimed proof.

This was a cold, line-by-line internal mathematical audit by an agent which
did not write the theorem.  It is not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_model_anchored_owner_circuit.md`](hc7_k7minus_model_anchored_owner_circuit.md),
with SHA-256

```text
2be8bf1da6bdaf76727c4f28b5240324d060f5ea0cb45a580b4266a76b11d7e8
```

The proof is computation-free.

The direct dependencies checked at their current revisions are

```text
aefcb5164c4122bfb142b7cbbbc31f4d4154cb5c632fe454510e358a510843d8  results/hc7_k7minus_model_anchored_appendage_ownership.md
d485f6735b11414170bd1eee9d3cb5a84b196e34c501078dd321b8f56f40bef8  results/hc7_k7minus_operation_provenance_exchange.md
4cd27295dc89c172d4246c67a529b87318d9e4343e5185dc5233f37d04f7109b  results/hc7_multi_owner_portal_linkage_transfer.md
```

Each dependency has an adjacent GREEN internal audit.  This audit checked
the deductions made from them afresh and does not elevate those checks to
external review.

## 1. Setting and inherited normal form

The model-ownership theorem supplies exactly the data used in Section 1:
the terminal decomposition, connected sets `K`, `A` and `R-A`, a fixed
forest edge and colouring, a named far bag anticomplete to the whole side,
and pairwise disjoint owner sets of order at least two.  Since all six
foreign bags must meet the universal bag `R`, each owner portal set `A_Q`
is nonempty.  Connectedness of `G[R]` and the nonempty connected proper
split `R=A dotcup (R-A)` make `B_A` nonempty.

The far label is not an owner: every `R-D` contact lies in `R-Z`, whereas
an owner has all its `R`-contacts in `A subseteq Z`.  Thus at most the five
other foreign labels can be owners.  This justifies (1.5) without assuming
that the seven branch sets span `G`.  The set `U_0` is therefore correctly
retained throughout the later boundary count.

## 2. Full owner linkage and branch-set transfer

Pairwise vertex-disjoint paths in Theorem 2.1 have distinct endpoint
vertices, even when different portal sets overlap.  Removing their vertices
from connected `G[A]` leaves components each adjacent to at least one path.
Assigning each whole component to one adjacent path therefore gives a
partition `(L_Q)` of `A` into nonempty connected sets.

For each owner `Q`, the `A_Q` end joins `L_Q` to the old bag `Q`, and the
`B_A` end supplies an edge from `Q union L_Q` to `R-A`.  For a nonowner,
its nonempty `R`-portal set is not contained in `A`, so an old contact with
`R-A` remains.  These observations verify every adjacency incident with
the reduced universal bag.  Enlarging owner bags destroys no internal
connectivity or old inter-bag adjacency, and all branch sets remain
pairwise disjoint.

The only absent pairs in the exact quotient are `PB` and `PC`.  If the
transfer creates either, at most the other remains absent, which is an
explicit `K_7^-` minor model.  Otherwise the new model is still exact.
This conclusion remains valid for an ordinary nonspanning model: vertices
of `U_0` are untouched and need not be assigned.

The fixed response also survives.  The sets `R-A` and `Z-A` are connected,
their difference is the old connected set `R-Z`, and the unchanged far bag
is anticomplete to `Z-A`.  The old list-critical core remains inside the
new side and retains every required end of the fixed coordinate.  At a
core vertex, passing from `Z` to `Z-A` retains every old exterior neighbour
and may add neighbours from `A`; hence its available colour list can only
shrink.  The core stays list-uncolourable, so the same exterior trace is
rejected on the strictly smaller anchored side.  This validates the
minimality contradiction in Theorem 2.1.

## 3. Rado--Menger owner circuit

Take the strict gammoid on the vertices of `A`, rooted at distinct vertices
of `B_A`.  Its rank on `A_I` is exactly `r(I)`: independent endpoint sets
are precisely those linkable to distinct roots by pairwise vertex-disjoint
paths.  Rado's independent-transversal theorem applied to the possibly
overlapping presentation sets `(A_Q)` therefore gives the criterion
`r(J)>=|J|` for every owner subfamily `J`.  A transversal is exactly the
labelled path family required in Theorem 2.1.

Since that full family is excluded, an inclusion-minimal deficient `I`
exists.  No singleton is deficient because `G[A]` is connected and both
endpoint sets are nonempty.  For every `Q in I`, nondeficiency of
`I-{Q}`, rank monotonicity and deficiency of `I` give

```text
|I|-1 <= r(I-{Q}) <= r(I) < |I|.
```

Thus `r(I)=|I|-1`.  Every subset of a proper subfamily is itself a proper
subset of `I`, so all of that subfamily's Rado inequalities hold; this
justifies the full-linkage assertion for every proper subfamily, not merely
for the sets `I-{Q}`.

The set-to-set form of vertex Menger, with endpoint vertices admitted to
the separator, produces `S` of order `r(I)` meeting every `B_A`--`A_I`
path.  It also covers intersections `B_A cap A_I` and the associated
zero-edge paths.  Hence (3.1)--(3.2) are exact.

## 4. Concentrated owner responses

If `A_I subseteq S`, choose one occurrence from every nonempty `A_Q`.
There are `|I|` labelled occurrences on `|S|=|I|-1` vertices, so two
distinct labels share a vertex `s`.  Their bags are disjoint, giving two
distinct outer endpoints and the incident contact edges in (3.4).

The appendage is disjoint from all forest endpoints, so `s` is not an end
of the fixed edge `e`.  Nor can the other end of either fresh contact edge
be an end of `e`: the end of `e` retained in the core lies in `R-A`, and
an `e`-edge from that vertex into an owner bag would be an `R-A` contact,
contradicting monopoly by `A`.  Each fresh edge is consequently disjoint
from `e`.

For either fresh edge `h`, a colouring of `G-e` gives signature `EP`, a
colouring of `G-h` gives `PE`, and a colouring after contracting both
disjoint edges expands to `EE`.  A `PP` colouring would be a proper
six-colouring of `G`.  These are therefore exactly the three signatures
claimed.  A colouring of `G-h` restricts properly to `G-s`; an intact
extension with the same boundary partition would glue to a six-colouring
of `G`.  The unchanged far bag is anticomplete to `s`, so `N_G(s)` is an
actual boundary.  This verifies outcome 1 in full.

## 5. Exposed component and response square

Suppose `A_I` is not contained in `S`, and take a component `C` of `A-S`
meeting `A_I-S`.  It cannot contain a vertex of `B_A-S`, because a path
inside `C` would avoid the Menger transversal.  By the definition of
`B_A`, this makes `C` anticomplete to `R-A`; its remaining neighbours
inside `R` lie in `S`.  It is anticomplete to `D` because `C subseteq Z`.
Connectedness of `A` supplies a `C-S` edge `g=cs`.  The edge `g` is
disjoint from `e` because the entire appendage is coordinate-free.

The fixed singleton-signature colouring of `G-e` gives `EP`, a colouring
of `G-g` gives `PE`, a colouring after contracting both disjoint edges
gives `EE`, and `PP` is impossible.  Thus the common deletion has exactly
the stated response square.

In the `PE` colouring, removing `C` removes an endpoint of the sole
monochromatic edge `g`, so the exterior is proper.  Any intact extension
with the same boundary partition would glue to a colouring of `G`, proving
rejection.  In an `EP` colouring the only monochromatic restored edge is
`e`; since neither endpoint lies in `C`, the closed `C`-side contains that
edge precisely when both endpoints belong to `N_G(C)`.  Condition (3.6)
is therefore necessary and sufficient for the closed-side restriction to
be proper.  Equality of its boundary partition with a `PE` exterior
partition would again align and glue.  These facts verify every response
claim in outcome 2 without assuming that `s` belongs to the list-critical
core.

## 6. Repeated contact and the full host boundary

All vertices of the host lie in `R`, in one of the six foreign bags, or in
`U_0`.  Section 5 gives `N_G(C) cap R subseteq S`, and the far bag `D`
contributes no neighbour.  If one of the other five foreign bags contains
two distinct neighbours `x,y` of `C`, choose a cross-edge at each.  Deleting
either one leaves the companion edge realising the same required
`R`--foreign-bag adjacency.  These external edge deletions do not affect
branch-set connectivity.  For either deletion colouring, removing `C`
removes the sole monochromatic edge, so its exterior trace is rejected by
the intact side.  This proves outcome 3 exactly as stated; joint deletion
persistence is neither needed nor claimed.

If no such repeated named-bag contact exists, the five possible foreign
bags contribute at most one boundary vertex each.  Hence

```text
|N_G(C)| <= |S| + 5 + |N_G(C) cap U_0|
           = |I| + 4 + |N_G(C) cap U_0|
           <= 9 + |N_G(C) cap U_0|.
```

The nonempty far bag lies outside `N_G[C]`, so `N_G(C)` separates the
nonempty set `C` from a nonempty remainder.  Seven-connectivity gives the
lower bound seven.  This verifies (3.7).  When the model spans, `U_0` is
empty and the returned boundary has order seven, eight or nine.  For the
ordinary anchored model, no proof in the source bounds the unused-neighbour
term, and the source correctly withholds that conclusion.

## 7. Coordinate--owner orthogonality

At least one end of `e` lies in `K subseteq R-A`.  If its other end lay in
an owner bag `Q`, the edge `e` itself would witness an `R-A`--`Q` contact,
contradicting `N_G(Q) cap R subseteq A`.  If the other end lies in `R` or
in `U_0`, it supplies no foreign labelled adjacency.  Thus no endpoint of
the fixed coordinate outside `R` belongs to an owner bag, and even
`V(e) subseteq N_G(A)` does not replace any adjacency monopolised by `A`.
Proposition 4.1 follows.

## 8. Trust boundary and unresolved work

No material gap or unstated assumption was found in the proved reductions.
In particular, the proof does **not** infer that:

- the two boundary-partition languages in outcome 2 intersect;
- the globally minimal anchored model can be required to span;
- the term `|N_G(C) cap U_0|` is bounded;
- a repeated contact preserves both fresh deletions simultaneously;
- the owner circuit is eliminated; or
- the eight-coordinate branch, Conjecture 21 or `HC_7` is proved.

The first unsupported inference remains exactly the terminal implication
recorded in (5.1).  The theorem is therefore suitable for promotion as a
conditional reduction, with its route nonclosure retained explicitly.
