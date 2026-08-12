# Finite completion of the low-degree dominated singleton

**Status:** computer-assisted finite result.  It is a conditional completion
inside the model-anchored eight-coordinate campaign, not a proof of the
`K_7^-` six-colour conjecture or of `HC_7`.

The verifier is [`verify.py`](verify.py).

## Question

In the dominated-singleton alternative, put

\[
 Q=G[N(u)-\{v\}].
\]

The proved host reductions give that `Q` is triangle-free,
`K_5^-`-minor-free and has a vertex cut of order at most two.  If `d(u)=8`,
then the exceptional-neighbourhood theorem gives `|Q|=7` and `alpha(Q)=3`.
If `d(u)=9`, contraction-criticality gives `|Q|=8` and `alpha(Q)<=4`.

At most six edges `ux`, with `x in V(Q)`, are essential to the fixed exact
`K_7^vee` model.  Thus at least one endpoint is model-persistent when
`|Q|=7`, and at least two are model-persistent when `|Q|=8`.  The finite
question is whether every cut of order at most two can contain all of those
marked persistent endpoints.

## Exact screen

Using `geng -t`, the verifier enumerates every unlabelled triangle-free
graph of the relevant order.  It independently checks the independence
bound and excludes a `K_5^-` minor by exhaustive deletion and contraction.
It then tests every marked vertex or marked pair.

The exact outcome is:

| `|Q|` | eligible graphs | marked instances | surviving marked instances |
|---:|---:|---:|---:|
| 7 | 9 | 63 | 2 |
| 8 | 158 | 4,424 | 1 |

The order-seven survivors are the two automorphic choices `0` and `5` in
the graph6 graph `FCxv?`.  The sole order-eight survivor is the pair
`{6,7}` in `G?rF\`w`.

## Exterior-component completion

Let `C` be a component of `G-N[u]` and contract it to a vertex `c`.
Seven-connectivity makes `c` adjacent to at least seven vertices of the
interface `\{v\} union V(Q)`.  The vertices `u,v` are adjacent and complete
to `Q`, while `c` is nonadjacent to `u`.

For each surviving marked graph, the verifier tests every possible miss set
consistent with that lower bound: nine profiles at order seven and 46 at
order eight.  Every augmented graph contains a `K_7^-` minor, again by an
exact deletion-and-contraction search.  Hence neither finite survivor can
occur in a target-free critical host.

The computation is a finite completion of hypotheses already reduced to
orders seven and eight.  It does not infer an unbounded statement from a
search bound.

## Reproduction

From the repository root run

```text
python3 active/experiments/dominated_singleton_low_degree_completion/verify.py
```

The script uses only the Python standard library and `geng` from nauty.  It
checks positive and negative controls for its exact minor routine, asserts
all counts and survivors, asserts every exterior profile, and prints a
`GREEN` line.
