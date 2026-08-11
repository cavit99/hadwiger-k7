# Internal audit: paired-donor overlap barrier

**Verdict:** GREEN.  The explicit graph satisfies every stated local
paired-donor condition, its fixed joint trace remains rejected, and the
width-four tree-decomposition certificate excludes a `K_7^-` minor.  The
construction does not satisfy the critical-host hypotheses, exactly as the
source states.

This is a separate internal mathematical and computational audit, not
external peer review.

**Audited source:**
[`hc7_k7minus_paired_donor_overlap_barrier.md`](hc7_k7minus_paired_donor_overlap_barrier.md)

**Source SHA-256:**

```text
342ae58dc8a87ed89b4528d527241c6c844e4c35260a44286fd94accb1f10024
```

**Verifier:**
[`hc7_k7minus_paired_donor_overlap_barrier_verify.py`](hc7_k7minus_paired_donor_overlap_barrier_verify.py)

**Verifier SHA-256:**

```text
a6726cb7443565a833e90ebcca99676b7a65966bf7d0bc6895962eb52405f53b
```

The verifier was run under Python 3 and returned

```text
GREEN paired-donor overlap barrier: {'vertices': 16, 'edges': 38, 'connectivity': 3, 'treewidth_upper_bound': 4}
```

## 1. Independent reconstruction

The graph has 16 vertices and 38 edges.  Its degree multiset is

```text
3^6, 4^6, 8^2, 9^2.
```

The displayed six-colouring is proper on every edge except `a_1a_2`,
whose ends both have colour zero.  For each `i`, the old donor boundary is

\[
 \{a_{3-i},t_1,t_2,t_3,t_4,t_5,w_i\},
\]

of order seven.  Its colours exhaust the palette at `a_i`, so `{a_i}` is
a fixed-trace rejection core.

The replacement `{r_i}` is connected and has connected complement in
`U_i`.  Its boundary has order eight, remains an actual separator, and
contains all five protected vertices `w_i,t_2,t_3,t_4,t_5`.  Its boundary
colours omit colour one, which is the colour assigned to `r_i`; hence the
replacement accepts rather than rejects the fixed trace.

The old boundaries overlap in `t_1,...,t_5`, and the cross-incidence sets
are the two singleton endpoints of the deleted edge.  The joint boundary is

\[
                       \{t_1,t_2,t_3,t_4,t_5,w_1,w_2\}.
\]

Relative to this fixed boundary, both `a_1,a_2` have the singleton list
`{0}`.  Their edge is therefore the claimed minimal joint obstruction.

## 2. Target exclusion and host scope

The explicit twelve-bag tree decomposition is a tree, covers every graph
edge, and has the running-intersection property at every vertex.  Its
largest bag has order five, proving treewidth at most four.  Since
`K_7^-` contains `K_6`, it has treewidth at least five; minor monotonicity
therefore proves target exclusion.

Deletion of any two vertices leaves the graph connected, while deleting
the three neighbours of `b_1` isolates that vertex.  Thus the connectivity
is exactly three.  The source's four-colouring is proper, and either donor
`K_4` gives the reverse lower bound.  Hence the graph is exactly
four-chromatic.

These checks also verify the limitations.  The graph has minimum degree
three, is not seven-connected or contraction-critical, and has none of the
five-centre equal/distinct response or certified owner/helper branch-set
duties.  It refutes the local overlap implication only; it does not refute
a full host-level paired-donor supply theorem.

## 3. Unresolved assumptions

None for the stated finite counterexample.  The audit makes no inference
from this bounded graph to the unbounded critical host.
