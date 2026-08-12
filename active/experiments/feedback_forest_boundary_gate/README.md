# Bounded feedback forest-boundary diagnostic

**Status:** bounded diagnostic only; not an unbounded theorem and not a
proof of the `K_7^-` six-colour conjecture.

The scripts test the smallest host-level repairs suggested by the audited
[feedback-boundary barrier](../../../barriers/hc7_feedback_boundary_rooted_k5_transversal_barrier.md).
They use every unlabelled graph `Q` of order seven or eight which is not
four-colourable and contains no literal `K_5`.  An exact branch-set
partition search tests each augmented graph for a `K_7^-` minor.

Run from the repository root:

```text
UV_CACHE_DIR=/private/tmp/hc7-uv-cache uv run python \
  active/experiments/feedback_forest_boundary_gate/probe.py
```

Expected output:

```text
eligible_boundaries=27
augmented_cases=2107
GREEN_BOUNDED_SCREEN
```

This shows that every tested natural two-exterior augmentation closes even
though a boundary-only transversal `K_5` model need not exist.  It does not
cover boundary orders nine through fourteen, arbitrary forest bridge
systems, or the full critical-host hypotheses.  Its purpose is to identify
forest-bridge composition as plausible while preventing the finite screen
from being cited as an unbounded reduction.

The seven-connectivity inequality for the two sides of one forest edge gives
only six boundary neighbours on each side.  That threshold is false even in
orders seven and eight:

```text
UV_CACHE_DIR=/private/tmp/hc7-uv-cache uv run python \
  active/experiments/feedback_forest_boundary_gate/probe_adjacent.py 6 6
```

returns

```text
COUNTEREXAMPLE boundary=GCpU}{ left=(0, 1, 2, 3, 4, 6) right=(0, 1, 2, 3, 4, 7)
```

Here `GCpU}{` encodes `(K_2\mathbin{\vee}C_5)\mathbin{\dot\cup}K_1`.
Thus cardinality bounds from a single forest edge do not suffice.  Raising
one of the two thresholds to seven gives

```text
eligible_boundaries=27
augmented_cases=8666
GREEN_BOUNDED_SCREEN
```

Finally, `probe_three_piece_path.py` tests only the displayed obstruction.
It replaces the exterior edge by a three-vertex path, keeps the two terminal
neighbourhoods fixed, and gives the middle vertex each of the 93 boundary
neighbourhoods of order at least five.  All 93 augmentations contain the
target:

```text
boundary=GCpU}{
middle_neighbourhoods=93
GREEN_TARGETED_REPAIR_SCREEN
```

This last outcome is evidence for retaining a middle forest piece; it is not
a screen of all three-piece configurations, even at orders seven and eight.

The full contact-only `7,6,7` quotient claim is false.  Run

```text
python3 -B \
  active/experiments/feedback_forest_boundary_gate/probe_three_piece_terminal.py
```

to reproduce a connected five-chromatic boundary of order eleven whose
three added path vertices have exact contact sequence `7,6,7`, while the
fourteen-vertex augmented graph is `K_5`-subgraph-free and has a certified
tree decomposition of width four.  It therefore has no `K_7^-` minor.  The
exact construction and its scope are recorded in the
[`7,6,7` quotient barrier](../../../barriers/hc7_k7minus_three_piece_767_quotient_barrier.md).
