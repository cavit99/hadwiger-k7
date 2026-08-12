# Separate internal audit: order-nine crossed-transition projection

**Verdict:** GREEN.  The order-nine projection theorem, both boundary
outcomes, and the stated route nonclosure are correct at the frozen revision
below.  This is a separate internal mathematical audit, not external peer
review.

## Exact revision

The audited source is
[`hc7_k7minus_order9_crossed_transition_projection.md`](hc7_k7minus_order9_crossed_transition_projection.md),
with SHA-256

```text
27b91fc459a81ba2b0d2002b281bb992151f82faafa013c496067bd43778052e
```

The mathematical source was cold-audited at the frozen SHA-256
`bf25bb8945f720b8cdefe9b9a2d19ec82795591787a1218a8628a0053b26553d`.
The only subsequent changes before promotion were status-header updates
linking this audit and recording its GREEN verdict; the displayed promoted
hash includes those non-mathematical changes and the replacement of the
historical word "draft" by "theorem" in one dependency label.  No theorem
statement or proof changed during the audit.

## 1. Crossed components and the selected nondominating component

The forbidden all-proper signature is used correctly.  If the equal ends
`u,p` are in different `i`--`j` components, switching either endpoint
component makes `up` proper.  The other selected edge must then become
monochromatic, so its two original colours are exactly `i,j` and each
endpoint component contains exactly one of its ends.  Thus both omitted
edges cross the same two components and either switch gives the opposite
singleton response.

The two crossed components cannot both dominate.  If they did, their only
cross-edges would be the two omitted independent edges, so domination forces
each component to consist of its two coordinate endpoints.  Connectivity in
the two-colour graph supplies one edge inside each pair, and the four
endpoints induce a four-cycle.  Contracting that cycle gives an exactly
six-chromatic proper minor: a five-colouring would expand by using the
contraction colour on one independent pair and a fresh sixth colour on the
other.  A spanning `K_6` model supplied by `HC_6`, together with the two
dominating crossed components, lifts to a `K_7` model.  This contradicts the
displayed hypothesis.

If neither component dominates, their boundary intersections are disjoint,
so choosing the smaller gives at most `floor(9/2)=4` boundary vertices.  If
one component dominates, every vertex of the other must be incident with one
of the two possible cross-edges; hence the other component consists exactly
of its two coordinate endpoints and meets the boundary in at most two
vertices.  In both cases the selected component `D` is nondominating.

Switching `D` changes the response from `(equal,proper)` to
`(proper,equal)` and leaves the exterior literally unchanged.  Since each
omitted edge loses one endpoint upon deletion of `D`, that exterior
restriction is a proper colouring of `G-D`.  Nondomination makes `N_G(D)`
an actual separator, and seven-connectivity gives order at least seven.  A
closed-side colouring with the same boundary partition can have its colour
names aligned with the exterior colouring and glued, so the displayed
partition is indeed rejected by the intact side.

## 2. Boundary support and sequential switches

Because neither selected edge lies within `T`, the two-colour graph on the
boundary is the same in `G` and `H`.  No boundary two-colour edge can leave
`D cap T`, so

```text
W=D cap T
```

is a union of whole boundary `i`--`j` components.  It is nonempty.  If it
were empty, the two opposite singleton colourings would have the same
labelled trace on `T`; the original colouring is proper on the closed
`B`-shore and the switched colouring is proper on the closed `A`-shore, so
they would glue to a six-colouring of `G`.

Switching the components `K_1,...,K_m` one at a time is legitimate.  A
whole-component interchange preserves boundary properness, and interchanging
the two colour names does not change the underlying component vertex sets.
The cumulative effect is exactly the switch on `W`, while `m<=|W|<=4`.
The initial trace extends through `B` and the final trace through `A`.

The extension languages are disjoint: one labelled trace extending both
closed shores would glue across the anticomplete open sides.  Therefore, if
no trace in the finite switch sequence is rejected by both shores, the first
trace which extends through `A` is preceded by one which extends through
`B`.  The two adjacent traces differ on the one literal component switched
at that step.  This proves the stated rejected-trace versus single-boundary-
interchange dichotomy without assuming Kempe connectivity of either shore.

## 3. First-hit components in the two shores

For two adjacent traces extending through opposite shores, consider in one
closed-shore extension the full two-colour component containing the switched
boundary component.  If it met the boundary only there, switching the full
component would produce the opposite trace and glue to the other shore.
Hence it reaches a different boundary two-colour component.  A shortest
set-to-set path, stopped at its first new boundary vertex, has nonempty
interior wholly in that open shore.  Reversing the roles of the traces and
shores gives the second path.  The two interiors lie in distinct components
of `G-T`, because the open shores are anticomplete.

Each such component `Q` has neighbourhood contained in `T`; the nonempty
opposite shore witnesses that this neighbourhood is an actual separator.
Thus seven-connectivity and `|T|=9` give

```text
7 <= |N_G(Q)| <= 9.
```

For order seven or eight, a six-colouring of the proper minor `G-Q`
realises a boundary partition which cannot extend through the intact
`Q`-side, since such an extension would glue and colour `G`.  At order nine
the neighbourhood is all of `T`, exactly as claimed.  No upper bound on the
earlier separator `N_G(D)` is inferred.

## 4. Rejected traces, list-critical kernels, and maximum palette

For a boundary trace `theta`, extension through an open shore is equivalent
to colouring that shore from the lists

```text
L(x)=[6]-theta(N_G(x) cap T).
```

If `theta` is rejected by both shores, each shore therefore contains a
vertex-minimal induced non-list-colourable subgraph.  Such a subgraph is
connected: otherwise each component could be coloured independently unless
one component were already a smaller obstruction.  The two kernels use the
same literal boundary trace, so the paired conclusion is valid.

The maximum-palette argument is also correct without an exact-root
assumption.  At least one trace extends through a shore, so the maximum `p`
is defined.  If an extending trace uses `p<6` colours on nine vertices, a
colour class is repeated.  Recolouring one member with a globally unused
boundary colour preserves properness and raises the palette size by one.
The operation can be repeated until all six colours occur.  Every new trace
uses more than `p` colours and hence extends through neither shore by the
definition of `p`.  Consequently, unless a full-six-colour trace is rejected
by both shores, `p=6`; and in that case every full-six-colour trace extends
through exactly one shore, because the two extension languages are disjoint.
The source does not claim that these recolourings extend through either
shore.

Finally, let `K` be one selected kernel inside an original component `C` of
an open shore.  If `K` is proper in `C`, then `G-K` is a proper minor and is
six-colourable.  Its trace on `N_G(K)` cannot extend through
`G[K union N_G(K)]`, or colour-name alignment and gluing would six-colour
`G`.  Thus `K` is a connected rejected response side with `|K|<|C|`.
The nonempty opposite open shore also ensures that this is an actual
separation.  If no proper selected kernel occurs, the selected kernel fills
its named component.  The source correctly declines to control the new
boundary order or preserve the original model labels.

## 5. Trust boundary

The proof uses the established `HC_6` only in excluding simultaneous
domination of the two crossed components.  Its Kempe input is the audited
forbidden-signature coupling theorem; the first-hit argument agrees with
the independently audited opposite-shore single-transition theorem.  The
list-critical and palette arguments are reproved in the source rather than
silently importing stronger hypotheses from the earlier order-nine notes.

The theorem does not bound `|N_G(D)|`, eliminate the paired shore-filling
list-critical endpoint, align either transition path with a prescribed
minor-model branch bag, or settle the maximum-palette ownership residue.
Section 4 states these as route nonclosures and does not claim the
`K_7^-` six-colour conjecture or `HC_7`.
