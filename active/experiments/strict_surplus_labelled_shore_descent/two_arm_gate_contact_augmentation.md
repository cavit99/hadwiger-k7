# The two-arm singleton gate is impossible

**Status:** experimental computation-free proof; independent audit pending.

Use the notation and conclusions of
[`singleton_gate_arm_classification.md`](singleton_gate_arm_classification.md).
Thus

\[
D-y=A_0\mathbin{\dot\cup}A_1\mathbin{\dot\cup}A_2,
\]

where `A_0` contains every root of `D` other than `y`, the two root-free
arms are joined to `y`, and, after relabelling,

\[
\Omega(A_1)=\{Q_1,Q_2\},
\qquad
\Omega(A_2)=\{Q_3,Q_4\}.                              \tag{1.1}
\]

The fifth foreign bag `U` is uncontacted, every `D-U` edge ends in `A_0`,
and the five foreign bags form a clique model.

## Theorem 1

The two-arm state (1.1) contradicts contact maximality of the original
`K_6` model.

### Proof

Put

\[
C=A_1\cup\{y\}\cup A_2,
\qquad
R=A_0\cup U.                                          \tag{1.2}
\]

Both sets are connected.  The set `C` is connected through the gate `y`.
The set `R` is connected because the model duty `D-U` has an edge from
`A_0` to `U`.

The six sets

\[
                         C,\ R,\ Q_1,Q_2,Q_3,Q_4       \tag{1.3}
\]

are pairwise disjoint, connected and pairwise adjacent.

- The edge `C-R` is supplied by any `y-A_0` edge.
- The set `C` is adjacent to `Q_1,Q_2` through `A_1` and to `Q_3,Q_4`
  through `A_2`.
- The set `R` is adjacent to all four `Q_i` through the old clique edges
  from `U`.
- The four retained foreign bags remain pairwise adjacent.

Thus (1.3) is a `K_6` model.

Originally the donor `D` contributed one contacted bag and `U` was
uncontacted.  In the new model, `C` is contacted by the root `y`, while
`R` is contacted by the other root or roots in `A_0`.  Every contacted
status among `Q_1,...,Q_4` is unchanged.  Hence the new model has exactly
one more contacted bag than the original contact-maximal model, a
contradiction.  `\square`

## Consequence

A minimum singleton/root blocker has at most one root-free arm.  The exact
remaining gates are therefore:

1. the clean singleton `C={y}`, with `D-y` connected; or
2. one root-free arm `A`, where `D-y=A_0 dotcup A`, the arm owns at least
   two accessible foreign duties and has at least six literal portals.

The second row is the genuine terminal-arm lock.  A detachable piece of an
owned foreign bag repairs the split and increases the contact count; the
surviving obstruction is a locked foreign carrier, not a second arm or an
unbounded family of duty assignments.
