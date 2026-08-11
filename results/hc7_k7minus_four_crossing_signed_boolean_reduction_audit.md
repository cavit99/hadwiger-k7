# Internal audit: four-crossing signed Boolean reduction

**Verdict:** GREEN for Theorem 2.1, Theorem 3.1 and Corollary 4.1.  This is
a separate internal audit, not external peer review.

## 1. Exact revision

The audited source is
[`hc7_k7minus_four_crossing_signed_boolean_reduction.md`](hc7_k7minus_four_crossing_signed_boolean_reduction.md),
with SHA-256

```text
26bae59cab6b6023207dd5400c093e5a54e4e30b9abff91f3f5ab78bf039c41f
```

The principal input is the audited common-matching theorem at source hash
`d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43`.
Its four-crossing outcome and subsequent order-seven upgrade supply the 16
exact two-full-shore cuts used here.

## 2. Partial transversals and tight connectivity

Fixing endpoints on `E-R` and extending the choice first by all `D`-ends,
then by all `A`-ends of `R`, proves separately that the two residual shores
in (2.1) are connected.  Fullness at `S` follows from those same exact cuts.
For a selected endpoint outside `R`, its matching mate supplies the contact
with the opposite shore, while the relevant full cut supplies its contact
with its home shore.  Deleting `R`, covering every edge of `E-R`, and using
that the fifth selected matching edge is noncrossing prove that no edge
joins the two shores.

The lower-bound argument for `kappa(G-R)` is valid.  Behind a hypothetical
smaller cut, cover every restored `R`-edge leaving one component.  If the
component consists only of crossing ends, choose one opposite end and all
remaining near ends.  This leaves both sides nonempty because
`|V(G)|>=25` and the proposed separator has order at most six.  The result
would be a separator of `G` of order less than seven.  Thus the displayed
separator attains the exact connectivity.

The chromatic and density identities are direct specialisations of the
common-matching theorem.  Contracting any nonempty subset `I subseteq R`
while retaining `R-I` gives exactly signature `I`; the empty signature
would colour `G`.  No independence or one-sided orientation of the centre
ends was used.

## 3. Common coordinate linkage

Both components have order at least six, so the two path anchors can avoid
all eight coordinate ends.  Seven-connectivity supplies seven internally
disjoint paths.  Every one of the 16 exact order-seven cuts meets every path
once.  Comparing the all-`D` transversal with a single flip puts `a_i,d_i`
on one unique path.  The two shore orientations force `a_i` immediately
before `d_i`; an intermediate vertex would lie simultaneously in the
disjoint original components.  Distinct coordinates use distinct paths,
and the assignment persists over the entire signed cube.

## 4. Dense rows and response traces

For `1<=|R|<=3`, exact connectivity is at least four and
`|E(G-R)|>=4|V(G-R)|-3`, so Norin--Totschnig Theorem 6 applies.  The
order hypothesis excludes `K_{2,2,2,2}`.  Target-freeness makes the
spanning `K_7^\vee` model exact in `G-R`; a restored edge filling either
missing adjacency gives `K_7^-`, and otherwise the exact model remains
valid in `G`.  The audited exact `K_7^\vee` dichotomy therefore applies.

If the returned set meets edges in `R_Y`, every signature supported on a
nonempty subset of `R_Y` has all its restored monochromatic edges hit by
that set.  It is proper on the exterior, and an extension of its exact
boundary precolouring would six-colour `G`.  The proof does not count these
as distinct boundary partitions.

## 5. Trust boundary

No proof gap or hidden finite assumption was found.  The result is
computation-free.  It closes the connectivity, separator and linkage
geometry of the four-crossing row, but deliberately does not claim:

- a common boundary partition among its signature colourings;
- that the returned nested set meets a coordinate endpoint;
- that its boundary has order seven;
- anchoring at the old minimum trace-admissible four-centre side; or
- elimination of the fifth, noncrossing selected edge.

Consequently the four-crossing row, Conjecture 21 and `HC_7` remain open.
