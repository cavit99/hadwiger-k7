# Internal audit: boundary-first donor gate

**Verdict:** **GREEN** for the theorem and the scoped route nonclosure in
the audited source revision.

This is a separate internal mathematical audit, not external peer review.
Two independent cold readings checked the final revision after correction
of the distinction between the fixed-trace core and the smaller geometric
donor.

## Audited revision

- source:
  [`hc7_k7minus_five_centre_minimal_donor_gate.md`](hc7_k7minus_five_centre_minimal_donor_gate.md)
- SHA-256:
  `0b95d7134c96821db1279c905571b03272c3665eca6eaf18fc8fa91f236efba7`

## 1. Donor classes and singletonisation

The distinction between geometric model donors and labelled gate donors is
necessary and correctly maintained.  Proposition 3.6 supplies a donor in a
named model bag with a named anticomplete far bag.  Choosing an incident
edge and a six-colouring after deleting it does not by itself preserve the
original equal/distinct `pq` response; the source now says so explicitly.

Lemma 2.1 is correct.  A spanning tree of `Y`, a spanning tree of `U-Y`,
and one joining edge give a leaf `v in Y` for which `U-v` remains connected.
The named far bag survives deletion of `N_G(v)`, so that neighbourhood is
an actual separator.  The two-clique-sum example correctly shows that
`|N_G(v)|` may exceed `|N_G(Y)|`.  Singletonisation therefore does not
respect a lexicographic order which minimises boundary size first.

## 2. Fixed-trace core inflation

Theorem 3.1 is correct.

1. In every six-colouring `c` of `G-yt`, the ends `y,t` have one colour;
   otherwise `c` would colour `G`.  This is the only violation of the lists
   induced by the colours on `T=N_G(Y)`.
2. The graph `G[Y]` is not colourable from those lists, since such a
   colouring would combine with `c` outside `Y` to colour `G`.  A
   vertex-minimal obstruction `K` is connected and contains `y`.
3. Deleting `K` removes the only possibly monochromatic edge.  Hence `c`
   gives a legal partition on the exterior closed side.  An extension of
   the same partition through the intact `K`-side would colour `K` from
   lists contained in the original lists, a contradiction.
4. If `K` is proper in `Y`, let `W` be the component of `U-K` containing
   `U-Y`.  The construction from `U-W`, or from a component of `Y-K` in the
   equality case, gives a nonempty proper connected `Y' subsetneq Y` with
   connected complement in `U` and the same anticomplete far bag.
5. When the comparison class contains every such donor-eligible subset,
   boundary-first minimality excludes both a smaller boundary and an equal
   boundary with smaller donor.  Thus `|N_G(Y')|>|N_G(Y)|`.

The source correctly keeps `K` and `Y'` distinct.  In the second
construction they may be disjoint, so the smaller donor need not retain the
fixed trace.  No assertion about `|N_G(K)|` is made.  If the labelled class
is not closed under the construction of `Y'`, no lexicographic comparison
is claimed.

## 3. Exact order seven

The order-seven deductions are valid.

- Corollary 2 of the separately audited three-component seven-cut exclusion
  gives exactly two complementary components in the critical host.
- Seven-connectivity makes both components full to the boundary.
- A `K_5` minor in the boundary, together with the two full components,
  would be an explicit `K_7^-` model.  The established `t=5` case of
  Hadwiger's conjecture therefore makes the boundary four-colourable.
- Contracting either full component together with a prescribed nonempty
  independent boundary set makes that set an exact colour block on the
  opposite closed shore.
- The audited split-boundary synchronisation theorem therefore glues a
  split boundary.  Every surviving boundary is nonsplit.

The source does not call this endpoint terminal.  It retains the correct
fork: the list-critical core fills the donor, or a smaller geometric donor
is exposed and either inflates the boundary in a closed comparison class or
falls outside the labelled comparison.

## 4. Broad geometric comparison

The order-eight bound is valid only after enlarging the comparison to all
geometric model donors, exactly as stated.  In every spanning model (3.14),
each ordinary owner bag is `R_i union {z_i}`.  The singleton `{z_i}` has
connected bag complement and an order-eight separating neighbourhood; the
exceptional count leaves a vertex outside `N_G[z_i]`.  Seven-connectivity
therefore restricts the broad minimum boundary order to seven or eight.
If it is eight, the second lexicographic coordinate selects a singleton of
degree eight.

For such a singleton `v`, a six-colouring of `G[N[v]]` uses at most five
colours on `N(v)`, while every six-colouring of `G-v` uses all six there.
A missing colour would extend to `v` and colour `G`.  This proves the stated
block-count incompatibility of the two unmodified shore languages.  It does
not prove that an operated response cannot be transferred, nor that the
broadly selected singleton necessarily loses the model labels; the source
uses the correct “need not retain” formulation.

## 5. Trust boundary

- Theorem 3.1 is a fixed-edge-deletion, fixed-colouring statement.  Strict
  boundary inflation for `Y'` is conditional on closure of the comparison
  class under the constructed donor-eligible subsets.
- No closure of the labelled donor class, upper bound for its boundary, or
  preservation of the original `pq` response is proved.
- Above order seven, the available unique-owner theorem gives an actual
  separator but does not guarantee two full shores.
- The order-eight singleton conclusion belongs only to the broad geometric
  comparison; that comparison need not preserve the model and operation
  labels.
- The cited parity, separator-excess, and Kempe constructions are scoped
  mechanism barriers, not counterexamples to the critical-host theorem.
- This is a decisive nonclosure of the boundary-first one-donor mechanism
  only.  It neither closes `kappa(G-Z)=2` nor proves the `K_7^-` six-colour
  conjecture or `HC_7`.
