# Dominated degree-eight rooted-carrier diagnostic

This deterministic finite check composes the nine eligible seven-vertex
common-neighbour graphs `Q` with rooted carriers available in the
five-connected remainder.

It verifies four claims used by the adjacent written reduction.

1. Every labelled `K_{3,4}` on `Q` completes `Q` to a `K_5^-` minor.
2. A labelled seven-cycle does not always do so: there are 456 surviving
   placements, in 125 fixed-`Q` automorphism orbits.  In the five graph
   types surviving the connected-exterior reduction, the figures are 402
   placements and 99 orbits.
3. A rooted `F_5=K_1\vee P_4` on a suitable five-subset closes every
   possible fan labelling for the theta graph and for the seven-cycle with
   a chord making cycles of orders four and five.  No such five-subset
   exists for `C_5\dot\cup K_2`, the pendant-path extension of `C_5`, or
   `C_7`.
4. Several tempting static augmentations remain insufficient.  One
   connected set meeting at least five cycle bags has 666 failures under
   all possible absorptions, including 14 failures even when it meets all
   seven.  Adding an aligned clique on four cycle bags has 701 failures.

The script also tests every proper partition of `Q` into five nonempty
independent blocks.  The residual three graph types have no robust
five-subset at all, so choosing one vertex from every colour block cannot
repair the rooted-fan implication there.

Run from the repository root:

```text
python3 active/experiments/dominated_singleton_rooted_seven_carrier/verify.py
```

The principal pinned totals are:

```text
eligible_Q=9 rooted-seven pairs=3555 survivors=456
K3,4 survivors=0
C7 survivor orbits=125
live C7 placements=402 live C7 orbits=99
post-F5 C7 placements=326 post-F5 C7 orbits=64
C7 minimum-added-edge histogram=[(1,381),(2,61),(3,13),(4,1)]
live histogram=[(1,334),(2,54),(3,13),(4,1)]
connected-owner tests=11658 failures=666
aligned-rooted-K4 tests=14070 failures=701
rooted-F5 tests=11340
independent five-block partitions=438 rainbow-robust failures=322
```

## Trust boundary

The nine graphs and exact deletion/contraction minor routine are imported
from the audited dominated-degree-eight verifier.  This script independently
generates all 360 labelled undirected seven-cycles, all 35 labelled
`K_{3,4}` graphs and all 60 labelled fans on each five-subset.  It does not
infer an unbounded theorem from a search bound.  The host lifts use the
fixed order-seven set `Q` and are proved separately.

The augmentation failures are quotient barriers only.  They need not be
five-connected, contraction-critical, or compatible with the four
operation-labelled colourings in the live host.
