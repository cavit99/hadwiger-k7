# Internal audit: six-boundary quotient barrier

**Verdict:** GREEN for the pinned source and verifier revisions.  This is
a separate internal mathematical and computational audit, not external
peer review.

**Audited source:**
`barriers/hc7_e5_six_boundary_quotient_barrier.md`

**Source SHA-256:**
`d7a7b3bd8ea57498d6005e8c0ed9bbf1f6dc418467c1c2ae1423320e7d1243ce`

**Audited verifier:**
`barriers/hc7_e5_six_boundary_quotient_barrier_verify.py`

**Verifier SHA-256:**
`86bfb088112389651e3f81bd71dc4a406a337fb3cb2a8e2f932c4ea1273fc0eb`

No mathematical or computational correction is required at these
revisions.

## 1. Corrected construction and contact hypotheses

The verifier reconstructs exactly the graph in the written source.  The
five roots induce

```text
s0-s1-s2                 and                 s3-s4,
```

so `Q[S]=P_3` disjoint union `K_2`.  The nominated vertices are
`t=s3` and `z=s1`; they are distinct, and `t` has degree one in `Q[S]`.
The remaining contacts are exactly

```text
N(p) intersect S = {s0,s2,s3,s4},
N(x)=N(y)=S,
N(q)={p,s0,s2,s3,s4},
N(c)={s0,s1,s2,s4,p}=W-{t}.
```

There is no edge among `x,y,q,c`.  Thus `pt` is present, `q` sees
precisely `p` and `S-{z}`, and `c` sees precisely `W-{t}`.  In particular,
the corrected graph satisfies the missing-`ct` contact forced by
`N_A(t)={p,q}` while retaining the required `cp` and `cz` edges.

The edge classes are disjoint and have orders

```text
3 + 4 + 10 + 5 + 5 = 27.
```

Hence the stated ten vertices and 27 edges are correct.  The verifier
checks every displayed neighbourhood, the degree-one condition on `t`,
the `pt,cz` contacts, the missing `ct` contact and exterior independence
before searching.

## 2. Completeness of the model enumeration

A `K_7^-` minor is equivalent to seven pairwise disjoint, nonempty,
connected branch sets with at most one nonadjacent pair.  Their union in
this graph can have any order from seven to ten, with every remaining
vertex unused.

The outer `combinations` loop selects every possible used set of each
order.  For a fixed sorted tuple, `seven_partitions` places the least
vertex in the first block and each subsequent vertex either in an existing
block or in one newly appended block.  Blocks are therefore ordered by
their least elements, the restricted-growth normal form for an unlabelled
set partition.  Every seven-part partition occurs once.  The pruning test
discards only prefixes unable to reach seven nonempty blocks.

The resulting totals are

```text
binom(10,7) S(7,7)  =  120,
binom(10,8) S(8,7)  = 1260,
binom(10,9) S(9,7)  = 4620,
binom(10,10)S(10,7) = 5880,
```

for 11,880 candidates.  Enumeration over proper used subsets explicitly
includes models with one, two or three unused vertices.

The connectivity search is exact for each induced branch set.  For every
connected partition, all 21 pairs of bags are tested for at least one
joining edge.  A missing-pair count at most one would be exactly a
`K_7^-`-minor model; the count is independent of labels on the seven bags.

## 3. Execution, digest and independent reproduction

Running

```text
python3 barriers/hc7_e5_six_boundary_quotient_barrier_verify.py
```

at the pinned revision gives exactly

```text
vertices 10 edges 27
partitions_by_used_order {7: 120, 8: 1260, 9: 4620, 10: 5880}
connected_branch_partitions 4873
minimum_missing_branch_pairs 2
closest_partition {s0,x} | {s2,y} | {s3} | {s4} | {p} | {q} | {c}
search_digest 3f94261a42cdadf57a2b55576d9cd2ce9bd3a173eceebe5fef0d553cf294ff67
VERIFIED: the quotient has no K_7^- minor
```

The stronger per-order connected totals checked by the program are

```text
{7: 120, 8: 756, 9: 1988, 10: 2009},
```

which sum to 4,873.  The digest includes every disconnected candidate
with missing-count marker `-1`; subset, block and within-block orders are
canonical and independent of set iteration.

The audit also used a structurally independent bitmask enumerator.  It
chose the block containing the least remaining vertex and recursed on the
complement, rather than using the verifier's restricted-growth generator.
It returned the same four total counts, the same four connected counts,
minimum defect two, and zero candidates with defect zero or one.

## 4. Closest partition

Every displayed part in

```text
{s0,x}, {s2,y}, {s3}, {s4}, {p}, {q}, {c}
```

is connected.  Direct inspection confirms every branch-set adjacency
except `{s3}`--`{c}` and `{q}`--`{c}`.  The corrected `ps4` edge repairs
the missing pair from the previous graph, while the corrected missing
`cs3` edge replaces it.  Thus this partition has exactly two missing
pairs and attains the computed minimum without being a `K_7^-` model.

## 5. Trust boundary and exact scope

The verifier is deterministic and dependency-free beyond the Python
standard library.  The finite conclusion relies on the explicit graph,
the standard branch-set characterisation of minors, exhaustive integer
and set operations, and correct execution of the pinned Python source.
The SHA-256 digest locks the canonical search record but is not treated as
a substitute for reviewing and independently reproducing the enumeration.

The barrier refutes only the corrected contact-only quotient inference.
It omits the internal structure and high excess of the component represented
by `c`, which are precisely what the host-level boundary-collapse theorem
uses to eliminate `s=4`.  The example is not asserted to be an `E5` enemy
or a realisable full quotient and does not encode the simultaneous exact
cuts, host connectivity or colouring-critical data.  It therefore does
not refute `(E5)`, `HC_7`, the primary theorem, or the host-level `s=4`
collapse.
