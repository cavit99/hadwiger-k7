# Internal self-audit: model-anchored owner circuits

**Verdict:** **GREEN as a self-check.**  The multi-owner transfer, the
Rado--Menger circuit, the operation-sensitive circuit outcomes and the
coordinate--owner orthogonality statement are correct at the pinned
revision.  This is not a cold audit by an independent agent and is not
external peer review.  The result ends in a recorded route nonclosure.

## Exact revision

The checked source is
[`hc7_k7minus_model_anchored_owner_circuit.md`](hc7_k7minus_model_anchored_owner_circuit.md),
with SHA-256

```text
2be8bf1da6bdaf76727c4f28b5240324d060f5ea0cb45a580b4266a76b11d7e8
```

The proof is computation-free.

## 1. Full owner linkage and branch-set accounting

For every owner label `Q`, its portal set `A_Q` is nonempty because the old
model contains an `R-Q` edge and ownership places every `R`-end of such an
edge in `A`.  The attachment set `B_A` is nonempty because `G[R]` is
connected and both `A` and `R-A` are nonempty.

The paths in Theorem 2.1 are pairwise vertex-disjoint even when the portal
sets overlap.  Hence they select distinct portal occurrences and distinct
attachment vertices.  Every component left after deleting their vertices
has an edge to at least one path by connectedness of `G[A]`; assigning the
whole component to one such path gives a genuine partition of `A` into
connected sets `L_Q`.

Absorbing `L_Q` into its old owner bag preserves connectivity through its
`A_Q` endpoint.  Its `B_A` endpoint restores the adjacency between that
owner and `R-A`.  Every non-owner already has an `R-A` portal by definition,
and enlarging owner bags cannot destroy any adjacency between other branch
sets.  The argument does not use spanningness: unused vertices stay unused.

The only optional pairs are `PB,PC`.  Creating either leaves at most the
other absent and therefore gives an explicit `K_7^-` model.  Otherwise the
model remains exact.  The far bag is not an owner and is unchanged.

The side `Z-A` and branch set `R-A` are connected by the audited appendage
normal form, with connected difference `R-Z`.  The fixed list-critical core
remains in the side and retains the relevant end or ends of `e`.  Removing
`A` can only add boundary colours at a core vertex, so its permitted list
can only shrink.  The same fixed colouring is therefore still rejected.
This establishes the strict anchored reduction.

## 2. Rado--Menger circuit

The strict gammoid rooted at `B_A` has rank `r(I)` on the union `A_I`.
Rado's independent-transversal criterion is precisely
`r(J)>=|J|` for every owner subfamily `J`; it permits overlapping portal
sets and trivial paths.  Failure of the full transfer gives a deficient
family.  Inclusion-minimality yields

```text
|I|-1 <= r(I-{Q}) <= r(I) < |I|,
```

so `r(I)=|I|-1`.  A singleton cannot be deficient in the connected graph
`G[A]`.  Vertex Menger with endpoints permitted in the transversal supplies
the stated set `S` of the same order.  These arguments are the same
matroidal facts used in the independently audited general multi-owner
portal theorem, but the branch-set transfer to which they are applied here
is the fixed-coordinate exact-`K_7^vee` transfer in Theorem 2.1.

## 3. Concentrated circuit

If `A_I` is contained in `S`, choosing one portal for each owner gives
`|I|` occurrences on `|I|-1` vertices.  Two different labels therefore
share a vertex `s`.  Their contact edges have distinct outer ends because
the owner bags are disjoint.  The far bag is anticomplete to `s`, making
the singleton boundary actual.

Every edge-deleted proper minor is six-colourable and its selected edge is
monochromatic; deleting `s` makes the restriction proper.  The appendage
contains no `F_8` endpoint.  The other end of a fresh owner-contact edge
cannot be an end of `e`: the core end lies in `R-A`, so that forest edge
would itself preserve the corresponding owner contact and contradict
ownership.  Hence each fresh edge is disjoint from `e`.
Single-edge colourings give the two singleton signatures, the double
contraction gives the equality--equality signature, and the all-proper
signature would colour `G`.  The three-corner claim is exact.

## 4. Exposed component and boundary count

If `A_I` is not contained in `S`, the chosen component `C` of `A-S` cannot
meet `B_A-S`: such a meeting would give a path from `B_A` to `A_I` avoiding
`S`.  Thus it has no neighbour in `R-A`; all its neighbours in `R` lie in
`S`.  Connectedness of `A` supplies a `C-S` edge.  The named far bag is
anticomplete to `C`, so the full boundary is actual.

The direct signature argument for the disjoint edges `e,g` is valid even
though the `S`-end of `g` need not lie in the list-critical core.  The
`PE` exterior restriction is proper because `C` contains its unique
monochromatic endpoint.  The `EP` closed-side restriction is proper exactly
when both ends of `e` are not present in that closed side.  Since no end is
in `C`, this is exactly `V(e) not subseteq N(C)`.  Equality of the two
boundary partitions would align and glue the colourings.

Outside `R`, the vertices are partitioned among the six named foreign bags
and the unused set `U_0`.  The far bag contributes nothing.  If another
named bag contributes two vertices, deleting either chosen contact edge
leaves the other to realise the same model adjacency; an external edge
deletion cannot disconnect `R`.  Each deletion separately gives the
claimed response on `C`.

If no named bag contributes twice, the boundary has at most

```text
|S| + 5 + |N(C) cap U_0| = |I| + 4 + |N(C) cap U_0|.
```

Seven-connectivity gives the lower bound.  Since `|I|<=5`, a spanning
model would indeed return order seven, eight or nine.  The term involving
`U_0` is indispensable for an ordinary model.

## 5. Coordinate--owner orthogonality

The fixed core contains an end of `e` and is a subset of `R-A`.  If the
other end were in a named foreign bag, `e` itself would witness an
`(R-A)`--foreign-bag adjacency.  That bag could not be monopolised by `A`.
If the other end lies in `R` or outside all model bags, it supplies no
foreign labelled adjacency.  Thus even adjacency of `A` to both endpoints
of `e` cannot release an owner.  This validates Proposition 4.1 and rules
out the tempting direct composition requested in the proof campaign.

## 6. Trust boundary

The source does not claim that the two boundary-partition languages
intersect, that the exact model can be chosen spanning after the global
anchored minimisation, or that the unused-neighbour term is bounded.  It
also does not claim that the two fresh edges in the repeated-contact outcome
are jointly model-persistent; persistence is correctly stated separately
for each deletion.

There are no unresolved assumptions in the displayed reductions.  The
source does not prove an original-coordinate boundary of bounded order,
eliminate the appendage, terminalise the eight-coordinate branch, prove the
`K_7^-` six-colour conjecture, or prove `HC_7`.
