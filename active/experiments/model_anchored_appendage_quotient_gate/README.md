# Static quotient gate for model-anchored appendages

**Status:** deterministic bounded diagnostic and recorded route nonclosure.
This is not a theorem about the critical host, a counterexample to
eight-coordinate terminalisation, or a counterexample to the `K_7^-`
six-colour conjecture.

The verifier is [`probe.py`](probe.py).

## 1. Question tested

Retain the audited terminal form

\[
                 Z=K\mathbin{\dot\cup}A_1
                    \mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}A_t,
                 \qquad t\in\{1,2\},                 \tag{1.1}
\]

inside one universal branch set `R` of an exact `K_7^vee` model.  Put
`R_0=R-Z`.  The quotient has the named connected cells

\[
       K,R_0,A_1,\ldots,A_t,P,B,C,U_2,U_3,U_4.       \tag{1.2}
\]

The core `K` is adjacent to `R_0` and to every appendage.  The appendages
are pairwise anticomplete and anticomplete to `R_0`.  A named far bag `D`
is anticomplete to all of `Z`, so the compulsory old `R-D` contact lies in
`R_0`.

The six foreign bags have the exact `K_7^vee` adjacencies:

- `B,C,U_2,U_3,U_4` form a clique;
- `P` is adjacent to `U_2,U_3,U_4`; and
- `PB,PC` are absent.

For each foreign label, its nonempty portal set in `R` may be any subset of
`{K,R_0,A_1,...,A_t}` consistent with the far-bag condition.  The actual
monopoly set of `A_i` consists of the labels whose portal set is exactly
`{A_i}`.  The verifier requires these monopoly sets to be pairwise
disjoint, to avoid `D`, and to have order at least two.  Thus arbitrary
additional `K`-, `R_0`- and appendage contacts are included rather than
silently suppressed.

The endpoint-support proof supplies `D in {B,C}`.  The other four choices
are checked only as a robustness diagnostic and are not claimed as direct
live provenance.

## 2. Exact target check

The quotient has nine vertices when `t=1` and ten when `t=2`.  The verifier
tests for a `K_7^-` minor by recursively applying every possible edge
contraction and vertex deletion until seven vertices remain, then accepting
exactly when at least twenty of their twenty-one pairs are adjacent.  This
is exhaustive: a seven-branch-set minor model contracts connected branch
sets and deletes unused quotient cells; deletion of quotient edges is never
needed because additional branch-set adjacencies are harmless.

The implementation checks positive and negative controls (`K_7` and the
seven-vertex exact `K_7^vee`) before enumerating the anchored profiles.

## 3. Outcome

For the two live far-twin choices, the exact counts are:

| appendages | far bag | admissible profiles | `K_7^-`-minor-free profiles |
|---:|---|---:|---:|
| 1 | `B` | 2,551 | 1,883 |
| 1 | `C` | 2,551 | 1,883 |
| 2 | `B` | 410 | 368 |
| 2 | `C` | 410 | 368 |

No ownership order is statically terminal.  With one appendage, even the
profile in which it monopolises all five non-far labels has no `K_7^-`
minor.  With two appendages, all twenty profiles having ownership orders
`2+3` survive for either far twin.  In the `2+2` case, 348 of the 390
profiles survive.

One two-appendage survivor with far bag `B` is

\[
 \begin{array}{c|cccccc}
   \text{foreign label}&P&B&C&U_2&U_3&U_4\\ \hline
   \text{whole portal support}&K&R_0&A_1&A_1&A_2&A_2.
 \end{array}                                         \tag{3.1}
\]

Thus

\[
             \Lambda(A_1)=\{C,U_2\},
        \qquad\Lambda(A_2)=\{U_3,U_4\}.              \tag{3.2}
\]

The verifier also checks all six possible far labels.  Their complete
counts are asserted in the source and printed during reproduction.

## 4. Decisive nonclosure

The audited ownership theorem is a genuine unbounded reduction: it leaves
at most two coordinate-free appendages, each owning at least two disjoint
model labels.  This diagnostic shows that its resulting uncoloured contact
data do not construct the target, even when both appendages consume all
five non-far labels.

The missing input must therefore couple operations to the internal
list-critical core.  Each appendage has a fresh response at an attachment
edge into `K`, while `K` retains the original forest-coordinate response.
The quotient encodes neither colouring, their boundary partitions, nor the
Kempe components relating them.  Adding further static ownership cases
cannot perform that operation-provenance exchange.

This is a route nonclosure, not a barrier to a colour-sensitive theorem.
The displayed survivors need not lift to seven-connected, minimum-degree-
eight, minor-critical graphs, and no such lift is claimed.

## 5. Reproduction

From the repository root run

```text
python3 active/experiments/model_anchored_appendage_quotient_gate/probe.py
```

The script uses only the Python standard library, asserts all aggregate
counts and controls, and prints a `GREEN` line.  A typical run takes under
thirty seconds.
