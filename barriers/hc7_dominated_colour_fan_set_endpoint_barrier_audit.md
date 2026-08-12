# Internal self-audit: set-endpoint colour-fan barrier

**Verdict:** **GREEN as an internal self-check.**  The displayed graph has
the asserted proper five-block partition, rooted `F_5` and two disjoint
set-rooted connectors, and it has no `K_5^-` minor.  This is not an
independent cold audit or external peer review.

## Exact revisions

```text
e85e92cf34aa200edae119019f9f83511914dcb7c6bb607f249c14748008362d  barriers/hc7_dominated_colour_fan_set_endpoint_barrier.md
cebbb319586feec1dc128efbf54441c2f6deb410d7e6827f46f745ed5688fc37  barriers/hc7_dominated_colour_fan_set_endpoint_barrier_verify.py
```

## Structural check

The six edges on `Q` are the five-cycle

```text
0-3-6-2-5-0
```

and the disjoint edge `1-4`.  The only non-singleton colour block is
`{0,1,2}`, which is independent.  The seven fan edges have hub `3` and
path `0-5-4-6`, so they form exactly `K_1\vee P_4` on one representative
of each block.  The two new paths are disjoint and meet the block pairs
`A,C` and `D,E`; the first uses `1` rather than selected root `0`.

## Minor check

Every five-branch-set minor model on nine vertices is represented by a
choice of a used vertex subset of order at least five and a partition of
that subset into five nonempty blocks.  The verifier enumerates all such
objects once.  It rejects a partition unless every block is connected and
then counts the ten possible inter-block adjacencies.  A count of at least
nine is equivalent to a `K_5^-` minor (extra quotient edges may be ignored).

The asserted total

```text
22827
```

agrees with

\[
 \sum_{j=5}^9 {9\choose j}S(j,5),
\]

where `S(j,5)` is a Stirling number of the second kind.  Exactly 3,058 of
these partitions have five connected blocks, and none has nine quotient
adjacencies.  As a second implementation check, the repository's audited
deletion-and-contraction dense-minor routine also returned false on the
same nine-vertex edge set.

## Scope

The barrier refutes only the local composition from set contacts.  It has
none of the full critical-host hypotheses and does not refute a theorem
which coordinates the rooted model with the connectors or uses
`K_7^-`-minor exclusion, contraction-criticality or the exact two-shore
response.
