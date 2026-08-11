# Internal audit: common five-edge response host

**Verdict:** GREEN for Lemma 2.1, Theorem 2.2, Corollary 2.3,
Lemma 3.1, Theorem 3.2 and Corollary 3.3.  This is a separate internal
audit, not external peer review.

## 1. Exact revision and dependencies

The audited source is
[`hc7_k7minus_five_centre_common_matching_reduction.md`](hc7_k7minus_five_centre_common_matching_reduction.md),
with SHA-256

```text
d0d3aa3574d747a3164f29febff1fa8fd6f37b0899415cd97a515005c5de5f43
```

The following repository inputs were checked at these source revisions:

```text
fc1e88c28b1f4d0dc7a1cbdeefa19fecfd5e969b986c64e11eb1990615f5dfbd  hc7_k7minus_exceptional_neighbourhood_completion.md
1917b5e3d183d44a2d905d2628272d10e4bc6f7ae0768b43cab0e9462b83332a  hc7_k7minus_five_centre_two_cut_reduction.md
1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96  hc7_k7minus_three_component_seven_cut_exclusion.md
4845f5375581971aca7397bbac0e3eb930dd2943c9dca71f6264a24e2fa31c6e  hc7_k7minus_exact_k7vee_separator_dichotomy.md
61fa3c094c34d06590efcef8a6903356f36bc8aadcdec75f834aa7e5cfd82936  hc7_contracted_edge_k6_model_normalization.md
```

Their adjacent audits are GREEN.  The external inputs are Hall's theorem;
Hadwiger's conjecture for parameter six, due to Robertson, Seymour and
Thomas; and Norin--Totschnig Theorem 6 at the `4n-8` threshold.

## 2. Matching and colouring checks

Contracting `\{z\} union I_z` is legitimate because `I_z` is independent
and the displayed star is connected.  After expansion, `I_z` is one colour
and all five vertices of `R_z` avoid it.  If the latter used at most four
colours, one of the six colours would be absent from `N_G(z)` and would
extend the colouring to `G`.  Thus `R_z` has the asserted five singleton
colours.

Hall's condition is immediate but was checked explicitly.  Any subfamily
of `t<=5` sets `R_z` has union of order at least five, hence at least `t`.
The representatives avoid `Z` and are distinct, so the five selected edges
form a matching.

For nonempty `J subseteq M`, a five-colouring of `G-J` plus one fresh
colour on the independent incident centres would colour `G`.  A
five-colouring of `G/J` first expands to `G-J` and gives the same
contradiction.  Proper-minor criticality supplies the upper bounds, proving
both chromatic equalities.

When a six-colouring of `G/J` is expanded to `H=G-M`, every edge of `J`
has equal-coloured ends.  Every edge of `M-J` remains between distinct
contraction bags, even in the presence of arbitrary edges between different
selected pairs, and is bichromatic.  Hence the signature is exactly `J`.
The empty signature would colour `G`.  The specially constructed
centre-deletion colouring has only its selected edge monochromatic.

For the saturation refinement, a centre outside `J` has its displayed
colour absent from its neighbourhood.  If all centres indexed by `J` were
unsaturated, assigning each an independently chosen missing colour would
colour `G`.  Thus the nonempty containment in (2.7) is exact.

The two spanning `K_6` conclusions were kept distinct.  Applying `HC_6` to
`G-J` gives a spanning model there without co-bagging.  Applying it to
`G/J` and expanding the contracted edges, using those edges inside their
bags, gives a spanning model in `G` with the required co-bagging.  No model
in `G-J` is incorrectly claimed to retain a deleted edge inside a bag.

## 3. The five contraction-bag separators

The minimal contraction-bag theorem applies to every selected edge:
`K_7^-`-minor exclusion implies `K_7`-minor exclusion, and the remaining
hypotheses are explicit.  Its lifted root bag splits into two connected
adjacent sets containing opposite ends of the selected edge.  If both sets
retained all five foreign contacts, they and the five external bags would
form a `K_7` model.  Thus a deficient side exists, and the cited theorem
makes its open neighbourhood an actual separator.  Seven-connectivity gives
the order-seven lower bound.

That deficient side contains exactly one end of the selected edge.  The
singleton-signature colouring's sole restored defect is therefore removed
when the side is deleted.  An extension of the resulting exact boundary
precolouring would glue to a six-colouring of `G`.  Corollary 2.3 follows.

## 4. Connectivity and separator checks

For a cut `S` of order `k<=3`, the graph `G-S` is
`(7-k)`-connected and hence `(7-k)`-edge-connected.  Every cut of the
component multigraph `Q_S` is literally the set of restored matching edges
across the corresponding union of components.  This proves
`lambda(Q_S)>=7-k` and also excludes cuts of order zero or one in `H`.

For `k=2,3`, the degree sum in a multigraph with at most five edges forces
exactly two component vertices.  It forces five crossing edges when `k=2`,
and four or five when `k=3`.  Minimum-cut fullness and restoration of the
matching give the two exact neighbourhood identities (3.3).

Since `delta(H)>=7`, every component of `H-S` has order at least `8-k`.
The only tight endpoint-choice issue is `k=3` and a component of order five;
then the component would be a literal `K_5`, contrary to the hypotheses.
Thus every stated endpoint transversal leaves both sides nonempty.

In the two-cut row, all five matching edges cross, the cut avoids `Z`, and
deleting `Z` leaves a proper two-cut of the two-connected graph `F`.  The
audited five-centre theorem gives the two open shores.  Each centre has its
selected representative as its sole neighbour in one open shore and its
other seven neighbours in the opposite closed shore.  Every one of the 32
transversal cuts has order seven, so the audited order-seven theorem gives
exactly two full components.

For a three-cut, the same reasoning gives four or five crossings and makes
`S-Z` a cut of `F`.  At most one centre can lie in `S`; this gives either a
two-cut of `F` or, when `S` avoids `Z`, a three-cut.  The four-crossing row
has 16 exact order-seven cuts.  In the five-crossing row all 32 order-eight
cuts are proper.  For a mixed transversal, every residual component has
boundary seven or eight.  Boundary seven is the asserted exact descent.  If
all are full at the order-eight boundary, a selected endpoint on either
side has only its matching mate across the original component separation;
it can see only the component containing that mate.  Mixedness applies this
argument on both sides and forces exactly two full components.

## 5. The four-connected row

Here `|E(H)|>=4|V(H)|-5`, so Norin--Totschnig Theorem 6 applies.  The
exception `K_{2,2,2,2}` is excluded by the order hypothesis, and the model
can be enlarged to span.  If a restored matching edge supplied either
nominal missing adjacency, the seven bags would contain `K_7^-`.
Target-freeness therefore keeps the spanning `K_7^\vee` model exact in
`G`, and the cited separator dichotomy applies.

Let `M_Y` be the matching edges met by the returned set.  For every
nonempty `J subseteq M_Y`, a signature-`J` colouring has precisely those
edges as its restored defects, and the returned set meets every one.  The
colouring is therefore proper outside the returned set.  Extending its
exact boundary precolouring inside would colour `G`.  This proves the full
`2^{|M_Y|}-1` family in Corollary 3.3; no distinctness of the induced
boundary partitions is inferred.

## 6. Trust boundary

No proof gap or unstated finite-search assumption was found.  The theorem
is computation-free.  The following are deliberate nonclaims:

- the five Corollary 2.3 separators need not be distinct, minimal, of order
  seven, or compatible on their boundaries;
- the 31 common-host colourings need not induce one boundary partition;
- the two unmixed order-eight endpoint choices may split one side;
- the dense-branch separator may avoid every matching endpoint or have
  boundary larger than seven; and
- a rejected boundary precolouring is not yet a six-colouring, forbidden
  minor or strict descent.

Consequently neither the `K_7^-` six-colour conjecture nor `HC_7` follows
from the audited theorem.
