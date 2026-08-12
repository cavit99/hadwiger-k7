# Separate internal audit: model-anchored appendage ownership

**Verdict:** **GREEN.**  The global minimisation class, omission of an
unowned appendage, transfer of a singly owned appendage, exact-model
accounting, fixed response inheritance, the two-appendage bound,
coordinate avoidance and the fresh attachment-edge reduction are correct
at the pinned revision.  The result leaves one or two multiply owned
coordinate-free appendages and does not terminalise the eight-coordinate
branch.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_model_anchored_appendage_ownership.md`](hc7_k7minus_model_anchored_appendage_ownership.md).
The mathematical revision initially checked through Theorem 2.1 had
SHA-256

```text
8a349fb54c1c1475d7eb530d85a130838b347b352c21fe6d440d4988cf428020
```

The source then added Section 4's fresh attachment-edge reduction and
updated its status paragraph.  The current audited source SHA-256 is

```text
aefcb5164c4122bfb142b7cbbbc31f4d4154cb5c632fe454510e358a510843d8
```

Theorem 2.1 is unchanged; Section 4 is separately checked in Section 7 of
this audit.  The proof is computation-free and requires no correction.

## 1. The broadened anchored class

An ordinary minor model is a family of pairwise disjoint nonempty connected
branch sets with the required inter-bag adjacencies; its union need not be
all of `V(G)`.  The definition in Section 1 uses precisely this ordinary
class while requiring the two missing pairs `PB,PC` to be genuinely
anticomplete in `G`.  Allowing unused vertices therefore changes no model
axiom and weakens no exactness assertion.

The class is nonempty.  Endpoint-support capture supplies a spanning exact
model, a connected proper side in one universal bag, a connected branch-bag
complement, a named foreign bag anticomplete to the side, and a singleton
coordinate response.  A spanning model is also a member of the broadened
class.  The graph, its finite set of vertex subsets, its finite family of
labelled branch-set models and its finite set of six-colourings make the
global minimum of `|Z|` well defined.

The boundary response makes `G[Z]` uncolourable from the lists in (1.2): an
`L_Z`-colouring would agree properly with the fixed exterior colouring on
every crossing edge and hence six-colour `G`.  A vertex-minimal obstruction
`K` is connected and retains the required end or ends of the coordinate by
the audited fixed-coordinate core theorem.

At failure of a proper anchored-hull descent, the component of `G[R-K]`
containing the connected set `R-Z` is exactly `R-Z`.  The other components
are consequently exactly the components of `G[Z-K]`; these are the stated
appendages.

## 2. Connectivity after deleting one appendage

Let `A` be an appendage.  Every component of `G[R-K]` has an edge to `K`.
Indeed, a path in the connected graph `G[R]` from that component to `K`
must leave it directly for `K`, since two distinct components of `G[R-K]`
have no edge between them.  Thus

\[
                  R-A=K\cup\!\bigcup_{A'\ne A}A'\cup(R-Z)
\]

is nonempty and connected, and

\[
                        Z-A=K\cup\!\bigcup_{A'\ne A}A'
\]

is nonempty and connected.  Their difference remains the original
connected set `R-Z`.  This verifies (2.2)--(2.3), including the cases of
one appendage and no other appendages.

## 3. Empty ownership and fixed-trace preservation

Every one of the six foreign bags is adjacent to `R` in the labelled exact
model.  Hence its portal set `N_G(Q) cap R` is nonempty.  If
`Lambda(A)=empty`, no such portal set is contained in `A`, so each has a
vertex in `R-A`.  Replacing `R` by `R-A` preserves every required model
adjacency.  The other branch sets are unchanged, the two exact nonedges are
unchanged, and the vertices of `A` may legitimately be left outside the
nonspanning model.

The same coordinate and colouring survive on `Z-A`, because
`K subseteq Z-A` retains the relevant coordinate endpoint set.  The named far branch
set remains outside and anticomplete to `Z-A`, so the new boundary is
actual.  For `x in K`, every old boundary neighbour is still a new boundary
neighbour, while vertices in `A` may add further boundary colours.  Thus

\[
 [6]-c_e(N_G(x)\cap N_G(Z-A))\subseteq L_Z(x).
\]

The old core remains non-list-colourable from the smaller lists.  Directly,
the exterior restriction is proper and any intact extension inducing its
boundary partition would align and glue to a six-colouring of `G`.  Hence
`Z-A` is a strictly smaller anchored response configuration, contradicting
global minimality.  This validates the omission argument without any
spanning-model assumption.

## 4. Single ownership and exact-model accounting

Suppose `Lambda(A)=\{Q\}`.  The monopoly definition supplies an edge
between `A` and `Q`, so `Q'=Q union A` is connected.  The appendage has an
edge to `K subseteq R-A`, restoring the sole required `R-Q` adjacency which
was lost when `A` left `R`.  Every other foreign portal has a vertex in
`R-A`, and enlarging `Q` cannot destroy an adjacency among the other branch
sets.  The seven new branch sets are disjoint, connected and still realise
all required edges of `K_7^vee`.

Only the pairs `PB,PC` were absent in the original exact model.  If the
transfer supplies either pair, the seven branch sets have at most the other
pair missing and therefore form an explicit `K_7^-` model.  If it supplies
neither, both pairs remain anticomplete and the model remains exact.  No
third missing adjacency can be created by enlarging `Q` and replacing the
lost `RQ` contact by the literal `A-K` edge.

The far label cannot equal `Q`: `D` is anticomplete to `A subseteq Z`,
whereas membership of `Q` in `Lambda(A)` requires an `A-Q` edge.  Therefore
`D` remains unchanged and anticomplete to `Z-A`.  The same connectivity,
list-containment and fixed-trace argument as in Section 3 produces a smaller
anchored configuration unless the target model has occurred.  This proves
`|Lambda(A)|>=2` in the target-free case.

## 5. Disjoint ownership and the number of appendages

If one foreign label belonged to the monopoly sets of two distinct
appendages, its nonempty portal set in `R` would be contained in two
disjoint components, which is impossible.  Thus the monopoly sets are
pairwise disjoint.

The exact model has an `R-D` edge.  Since `D` is anticomplete to `Z`, every
`R`-end of such an edge lies in `R-Z`; consequently `D` belongs to no
appendage monopoly set.  The pairwise disjoint monopoly sets therefore have
order at least two inside the five labels other than `D`.  There can be at
most two appendages.  This count does not require the model to be spanning.

## 6. Coordinate avoidance by global minimisation

Suppose an appendage `A` contains an endpoint of `f in F_8`.  The
singleton-signature colouring `c_f` is proper on `G-f` and has `f` as its
only monochromatic edge after restoration.  Deleting `A` removes one end,
so the exterior restriction is proper.  Any intact extension with the same
boundary partition would glue to a six-colouring of `G`; hence `A` carries
the fixed response at `f`.

This is an anchored response configuration in the globally minimised class:

* `A` is nonempty and connected;
* `R-A` is nonempty and connected by Section 2;
* the same exact model is retained without alteration;
* the same named far branch set is anticomplete to `A subseteq Z`; and
* its boundary is actual because that nonempty far bag lies outside
  `N_G[A]`.

The nonempty core `K` is disjoint from `A`, so `|A|<|Z|`.  Global
minimality was deliberately taken over **all** coordinates,
singleton-signature colourings, exact models and labels; changing from
`e,c_e` to `f,c_f` is therefore legitimate and gives the contradiction.
Every appendage is consequently disjoint from `V(F_8)`.

## 7. The fresh attachment-edge response

Let `A` be an appendage.  Its attachment to `K` supplies an edge
`g=ak` with `a in A` and `k in K`.  Minor-criticality gives a proper
six-colouring of `G-g`; its ends must be equal, since otherwise it would
six-colour `G`.  Deleting `A` removes `a`, so the restriction to `G-A` is
proper.  If its boundary partition extended through the intact closed
`A`-side, alignment and gluing would again six-colour `G`.  This is a
genuine fresh fixed-edge response on `A`.

The same anchored model data survive literally.  The appendage `A` is
connected, `R-A` is connected by Section 2, and the same named far branch
set `D` is nonempty and anticomplete to `A subseteq Z`.  Thus its boundary
is actual and the existing exact model need not be altered.  Since the
nonempty core `K` is disjoint from `A`, one has `|A|<|Z|`.

This does not contradict the global choice in Section 1.  That minimum
ranges over the eight named edges `F_8` and their singleton-signature
colourings, whereas the attachment edge `g` need not lie in `F_8`.
Theorem 2.1 has already proved `A cap V(F_8)=empty`, so no nonempty forest
signature is covered by `A`; the punctured cube supplies no exterior-proper
forest response on that side.  The source therefore identifies the exact
coordinate-loss quantifier rather than silently enlarging the minimisation
class.

## 8. Scope

The corollary follows: the terminal side is its list-critical core together
with at most two pairwise anticomplete, coordinate-free appendages, each
owning at least two disjoint foreign labels and none owning the far label.
All coordinate endpoints in the side therefore lie in the core.

There are no unresolved assumptions in these conclusions.  The theorem
does not eliminate either remaining multiply owned appendage, bound the
response boundary, give a compatible two-shore partition, prove
eight-coordinate terminalisation, Conjecture 21 or `HC_7`.
