# Internal audit: six-boundary quotient barrier

**Verdict:** GREEN for the pinned source and verifier revisions.  This is
a separate internal mathematical and computational audit, not external
peer review.

**Audited source:**
`barriers/hc7_e5_six_boundary_quotient_barrier.md`

**Source SHA-256:**
`980b0190866dde07591ecc04115268fc9c10778ff0ea479e19cc0a9060487797`

**Audited verifier:**
`barriers/hc7_e5_six_boundary_quotient_barrier_verify.py`

**Verifier SHA-256:**
`d63881647a019b47dc62adac8d5f461c4dafb421f16368158d8bdb6e1131bd84`

No mathematical or computational correction is required at these
revisions.

## 1. Construction and contact hypotheses

The verifier reconstructs exactly the graph in the written source.  The
five roots induce the three edges

```text
s0-s1,             s1-s2,             s3-s4,
```

so `Q[S]=P_3` disjoint union `K_2`.  With `z=s1`, its remaining contacts
are exactly

```text
N(p) intersect S = {s0,s2,s3},
N(x)=N(y)=S,
N(q)={p,s0,s2,s3,s4},
N(c)=S union {p}.
```

There is no edge among `x,y,q,c`.  Thus `x,y` are complete to `S` and
miss `p`; `q` sees `p` and every root other than `z`; and `c` sees all six
vertices of `W`, including `p,z`.  Every hypothesis of the refuted
intermediate claim is met.

The edge classes are disjoint and have orders

```text
3 + 3 + 5 + 5 + 5 + 6 = 27,
```

where the two terms of order five after the `p` contacts belong to `x,y`,
followed by the five `q` contacts and six `c` contacts.  Hence the stated
ten vertices and 27 edges are correct.  The verifier explicitly checks
all of these neighbourhood and independence assertions before searching.

## 2. Completeness of the model enumeration

A `K_7^-` minor is equivalent to seven pairwise disjoint, nonempty,
connected branch sets with at most one nonadjacent pair.  In this
ten-vertex graph their union can have any order from seven to ten; all
other vertices may be unused.

The outer `combinations` loop selects every possible used vertex set of
each such order.  For a fixed ordered tuple, `seven_partitions` starts its
least vertex in the first block.  Each later vertex is placed either in
one existing block or in one newly appended block.  Consequently blocks
are ordered by their least elements, which is the restricted-growth
normal form for an unlabelled set partition.  Every partition into seven
nonempty parts occurs once, and the pruning condition discards only
prefixes that cannot reach seven parts.

The resulting totals are

```text
binom(10,7) S(7,7)  =  120,
binom(10,8) S(8,7)  = 1260,
binom(10,9) S(9,7)  = 4620,
binom(10,10)S(10,7) = 5880.
```

Here `S(7,7)=1`, `S(8,7)=28`, `S(9,7)=462`, and
`S(10,7)=5880`.  Their sum is 11,880.  In particular, enumeration over
proper used subsets explicitly covers models with one, two or three
unused vertices.

The connectivity test explores the subgraph induced by each part.  This
is equivalent to the existence of a connected branch set on that vertex
set.  For every connected partition, the verifier checks all 21 pairs of
parts and counts a pair as missing exactly when no graph edge joins the
two sets.  Therefore a count of zero or one would be precisely a
`K_7^-`-minor certificate; no labelling of the seven bags is omitted.

## 3. Execution, digest and independent reproduction

Running

```text
python3 barriers/hc7_e5_six_boundary_quotient_barrier_verify.py
```

at the pinned revision gives exactly

```text
vertices 10 edges 27
partitions_by_used_order {7: 120, 8: 1260, 9: 4620, 10: 5880}
connected_branch_partitions 4912
minimum_missing_branch_pairs 2
closest_partition {s0,x} | {s2,y} | {s3} | {s4} | {p} | {q} | {c}
search_digest e6f4284228d49e3143df81b07c311cb5a23a77014ac86124a3a2e3d8bb653ded
VERIFIED: the quotient has no K_7^- minor
```

The verifier also checks the stronger per-order connected totals

```text
{7: 120, 8: 756, 9: 2002, 10: 2034},
```

which sum to 4,912.  The digest record contains every candidate,
including a disconnected candidate with missing-count marker `-1`.
Vertex subsets are lexicographic, and the restricted-growth block order
and within-block vertex order are canonical.  Set iteration affects
neither this record nor any boolean adjacency result.

As an independent cross-check, the audit used a second bitmask enumerator
which chooses the block containing the least remaining vertex and then
recurses on its complement.  It independently returned the same four
partition totals, the same four connected totals, 4,912 connected models,
minimum missing-pair count two, and no candidate of count zero or one.
This second implementation did not reuse the verifier's partition
generator or connectivity routine.

## 4. Closest partition

Every displayed part in

```text
{s0,x}, {s2,y}, {s3}, {s4}, {p}, {q}, {c}
```

is connected.  Direct inspection confirms all branch-set adjacencies
except `{s4}`--`{p}` and `{q}`--`{c}`.  These are two distinct missing
pairs, so this witness attains the computed minimum but is not a
`K_7^-` model.

## 5. Trust boundary and exact scope

The verifier is deterministic and uses only the Python standard library.
The finite conclusion relies on the explicit ten-vertex graph, the
standard branch-set characterisation of graph minors, exhaustive integer
and set operations, and correct execution of the pinned Python source.
The SHA-256 search digest locks the canonical enumeration record; it is
not by itself a mathematical proof, which is why the generator,
connectivity test, adjacency test and counts were also reviewed and
independently reproduced.

The result excludes `K_7^-` only in this explicit quotient graph.  It
does not assert that the graph is an `E5` enemy or that it lifts to the
full singleton-residue configuration.  Internal component structure,
simultaneous exact cuts, host connectivity and colouring-critical data
are absent.  The barrier therefore refutes only the contact-only quotient
inference and does not refute `(E5)`, `HC_7`, or the primary theorem.
