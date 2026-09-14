# Audit of the augmentation operation counterexamples

**Verdict: GREEN for the stated counterexamples and finite checks.**
The augmentation theorem, a universal exchange or contraction-selection
rule, C19 and HC7 remain unproved. This is internal review, not external
peer review or a novelty assessment.

**Revisions reviewed:**

- Source SHA-256:
  `8b0fdc2a94bc4fb55464990dca7657b768131429f5211f0fd31102b365d9eea5`.
- `active/hc7_chromatic_exchange_probe.py` SHA-256:
  `c5f57b28431d0dd3c9b2ce38a2a13562b73a495d94ec04c49d05321170e087fd`.

**Independence.** The reviewer who developed the eleven-vertex construction
independently reconstructed Section 2 and the finite probe. The reviewer
who developed the seventy-seven-vertex construction independently
reconstructed Section 1 at the pinned source. Thus neither section relies
on its originator's check alone. Sections 1 and 2 have written proofs;
finite computation is not a premise of either counterexample.

**Section 1.** The complement is triangle-free; the six colour classes,
common-neighbour counts and exclusion of K2,4 and K3,3 establish the
claimed chromatic number and connectivity. The three edge orbits cover
every edge, and each displayed quotient colouring checks directly.
The untouched nine-vertex subgraph gives the matching lower bound.
Common-neighbour degrees and lifted cuts give minimum degree and
connectivity five. Expanding the quotient colourings and translating the
vertex-deletion colouring justify edge- and vertex-criticality.

The two contracted edges are disjoint and connected; their bags become
universal, while the residual seven-vertex graph is four-chromatic. This
recovers six colours only for the specified batch. The explicit seven
original bags are disjoint and connected, with exactly the two stated
independent omissions. There are no prescribed roots to preserve.

**Section 2.** The modular edge-colouring gives distinct ports, and the
copy-colour shifts properly colour every cross-edge. Four deletions leave
all copies connected and remove at most four cross-edges; the displayed
cut bound for B proves five-connectivity. Splitting a copy gives exactly
nineteen contacts, and every legal merger leaves at most eighteen.
The other two objective coordinates already attain absolute minima.
The port transfer is a valid connected split-and-merge: it preserves the
contact graph and increases the squared-order sum by two. The proper
full-hypothesis core inside each copy remains an available induction exit;
the construction does not refute a rule that detects such a core.

**Finite reconstruction.** The pinned probe was rerun through `uv run
python3`. A separate implementation generated connected subsets using
NetworkX and partitions by recursive exact covers, then independently
tested the local-minimum conditions.
It reproduced connected-state counts 16,093 and 16,082; Q7-model counts
792 and 681; K7-model counts zero and three; two-coordinate local-minimum
counts zero and 24; and no three-coordinate local minima on either host.
The displayed 103-successor obstruction and shortest two-move escape
were independently checked in the original graph. Those positive balance
results concern exactly two eleven-vertex hosts; Section 2 refutes their
extension to a universal strict-descent theorem.
