# Two-exterior completion at a dominated degree-eight singleton

**Status:** computer-assisted finite result.  This is a conditional finite
lemma in the model-anchored eight-coordinate campaign, not a proof of the
`K_7^-` six-colour conjecture or `HC_7`.

The verifier is [`verify.py`](verify.py).  It reuses the exact graph6,
independence, cut and deletion/contraction minor routines from the adjacent
[`dominated_singleton_low_degree_completion`](../dominated_singleton_low_degree_completion/verify.py)
verifier.

## Finite statement

Let `Q` have order seven, be triangle-free, satisfy `alpha(Q)<=3`, have no
`K_5^-` minor, and have a vertex cut of order at most two.  Add adjacent
vertices `u,v` complete to `Q`.  Add two further nonadjacent vertices
`c_1,c_2`, each nonadjacent to `u` and each adjacent to at least seven
vertices of `\{v\} union V(Q)`.

Every resulting graph contains a `K_7^-` minor.

The verifier enumerates the nine eligible unlabelled graphs `Q` with
`geng -t`.  Each component vertex may miss no interface vertex or one of
the eight interface vertices.  It therefore checks exactly

\[
                         9\cdot9^2=729
\]

labelled attachment profiles.  Its exact deletion-and-contraction routine
finds a `K_7^-` minor in every profile.

## Hostile one-component screen

The same verifier also contracts only one exterior component and checks its
nine possible near-complete attachment profiles.  Of the resulting 81
quotients, exactly 46, arising from six of the nine eligible graphs `Q`, do
not contain a `K_7^-` minor.  Five of those six graphs retain all nine
profiles; the sixth retains one.

This is a negative diagnostic, not a counterexample to the critical-host
theorem.  The contracted quotients need not be seven-connected,
seven-chromatic, or carry the exact-model and response-cube data of the live
host.  It proves only that connectedness together with a single
near-complete attachment to `\{v\} union V(Q)` cannot finish the remaining
case by static quotient geometry.

The live connected-exterior geometry permits only two of those nine
profiles: the component sees the whole interface, or it misses exactly
`v`.  Exactly five graphs survive both profiles.  In standard descriptions
they are

1. `C_5 dotunion K_2`;
2. `C_5` with a pendant path of length two attached at one cycle vertex;
3. the theta graph with path lengths `2,3,3`;
4. `C_7`; and
5. `C_7` with a chord whose two resulting cycles have orders four and five.

Their graph6 strings are, in the same order,

```text
FCQ`_
FCQb_
FCR`o
FCp`_
FCpb_
```

This is an exact quotient classification.  It still does not classify the
unbounded connected exterior component attached to the seven-vertex graph.

## Reproduction

From the repository root run

```text
python3 active/experiments/dominated_singleton_two_exterior_completion/verify.py
```

The script uses the Python standard library and `geng` from nauty.  It
asserts the eligible graph count and every minor conclusion before printing
its `GREEN` line.  The expected output is

```text
GREEN dominated degree-eight singleton two-exterior completion eligible_Q=9 profiles=729 one_component_survivors=46 survivor_graphs=6 live_profile_survivors=10 live_graphs=5
```
