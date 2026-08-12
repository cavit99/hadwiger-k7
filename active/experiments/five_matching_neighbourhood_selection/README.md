# Representative selection in exceptional neighbourhoods

**Status:** bounded diagnostic with two independent exact minor tests.  It
does not prove a host-level selection theorem and is not evidence for a
finite-order reduction of the `K_7^-` six-colour conjecture.

## Question tested

For an eight-vertex graph `L` with

\[
                         K_4\nsubseteq L,
 \qquad                  \alpha(L)=3,
\]

call `x` good when `L-x` contains a `K_5^-` minor.  The omitted-coordinate
linkage theorem becomes terminal at a degree-eight centre if its selected
representative is good.  The experiment asks whether an independent triple
can always be chosen so that a good vertex remains among its five possible
representatives.

## Result

The answer is no.  Among the `2,076` unlabelled eligible graphs of order
eight:

- `756` have no good vertex outside any independent triple;
- `1,836` do not admit an independent triple leaving five good choices;
- the Wagner graph, graph6 code ``GCrb`o``, is a three-connected cubic
  obstruction with no good vertex at all.

The same exhaustive catalogue gives two sharp density thresholds:

\[
 \begin{aligned}
 |E(L)|\ge16&\quad\Longrightarrow\quad
   \text{some selectable representative is good},\\
 |E(L)|\ge19&\quad\Longrightarrow\quad
   \text{some independent triple leaves all five representatives good}.
 \end{aligned}
\]

Failures exist with fifteen edges, so the first threshold is sharp.  No
current host theorem forces an exceptional neighbourhood to have sixteen
edges.  Representative selection is therefore a useful conditional exit,
not a universal closure mechanism.

The later six-coordinate induced-forest reduction supplies a second local
test.  In its singleton-star row, all five star leaves must be bad: deleting
any one of them leaves no `K_5^-` minor.  That condition is still not
locally contradictory.  Exactly

\[
                         719+267+273+225=1,484
\]

eligible neighbourhoods have at most three good vertices, and therefore
have at least five possible bad leaves.  The host-level cut and model
labels, rather than the eight-vertex neighbourhood type alone, are
essential to any closure of that row.

## Verification

The script requires Brendan McKay's `geng` on `PATH`.  Run

```text
python3 active/experiments/five_matching_neighbourhood_selection/representative_probe.py
```

It enumerates all `12,346` unlabelled graphs of order eight, filters the
eligible `2,076`, and tests every deletion both by exact deletion/contraction
recursion and by an independent branch-set partition search.  Expected
final output:

```text
GREEN: representative-selection diagnostic verified
```
