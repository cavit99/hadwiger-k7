# Verification audit: opposite-shore coordinate-square diagnostic

**Verdict:** GREEN for the fixed finite survivor and the scoped negative
finding stated in the README.  This audit does not promote the diagnostic
to an unbounded theorem and does not refute the critical-host matching
claim, the `K_7^-` six-colour conjecture, or `HC_7`.

## Exact revisions

```text
README.md          cd39d0119565044c69f343c911ff7412e8d99f288d0618aa94d76afebea54442
search_quotient.py 63196c35941a009587a6503517b02471818eb18f00fb461b6b13efe86576da75
verify_survivor.py 999317cdda963a50cedd3f3ffc169044fb9636efbb7359d4ed27cfe0a2b7ea53
```

## Checks performed

Running

```text
python3 active/experiments/opposite_shore_coordinate_square_gate/verify_survivor.py
```

reconstructs the fixed twelve-vertex graph rather than trusting saved
search output.  It verifies:

* two connected, anticomplete two-vertex components, each full to the
  order-eight boundary;
* singleton neighbourhood orders `8,3` on each shore, so no proper
  connected shore subset has boundary order seven;
* the displayed spanning exact `K_7^vee` model in the double deletion;
* one spanning `K_6` model in the same graph which co-bags both selected
  endpoint pairs;
* every connected split of either coordinate bag, with maximum foreign
  double-contact count two;
* all 4,111 canonical boundary partitions into at most six blocks, of
  which exactly 408 are proper, and the exact signature-language sizes
  `PP=361`, `EP=56`, `PE=56`, `EE=14`;
* disjoint `EP` and `PE` boundary-partition languages and an explicit
  shore-confined coloured six-fan in each;
* chromatic numbers `5,6,6,6` for `G,G/e,G/f,G/e/f`;
* vertex connectivity three; and
* absence of a `K_7^-` minor by exhaustive edge-contraction search over
  5,112 memoised labelled states.

The contraction search is exact here.  In a connected graph any unused
vertices can be absorbed into a minor model, so a `K_7^-` minor has a
spanning seven-bag model.  Contracting those bags yields a seven-vertex
graph with at least twenty edges, which is precisely the terminal condition
used by the search.

The fixed verifier imports graph and colouring routines from
`search_quotient.py`; it is independent of the random sample, not an
independent implementation of those routines.  The exploratory search is
therefore retained only for reproducibility of discovery.  The mathematical
scope rests on the explicitly displayed fixed graph and the exhaustive
checks above.

## Scope

The survivor has the forbidden all-proper signature, is five-colourable,
has connectivity three and has degree-three vertices.  It therefore shows
only that the three positive square signatures, exact contraction
chromaticity, two coloured fans, a common co-bagged `K_6` model and blocked
splits do not by themselves force the two singleton boundary languages to
meet.  Any host-level proof must genuinely use absence of the all-proper
signature and the critical connectivity.  The subsequent unbounded
lock-or-separator theorem does exactly the former, but still leaves the
all-lock model-allocation and large-separator problems open.
