# Barrier to lowering the exterior-neighbourhood threshold to three

**Status:** barrier/counterexample to an intermediate claim; exact
computer-assisted minor exclusion with positive and negative calibration.

## Refuted claim

> Let `J` be an eight-vertex, literal-`K_4`-free graph with
> `alpha(J)=3` and `delta(J)>=3`.  Add two nonadjacent vertices both complete
> to `J`.  The resulting graph contains `K_7^-` as a minor.

## Counterexample

On vertices `0,...,7`, let `J` have edge set

\[
\begin{aligned}
\{&03,04,07,12,13,14,25,26,34,56,57,67\}.
\end{aligned}
\]

Its graph6 code is ``GMs`KK``.  The graph is cubic and literal-`K_4`-free,
has independent triples, and has no independent four-set.  Thus

\[
                 \delta(J)=3,\qquad \alpha(J)=3.
\]

Let `Q` be obtained by adding nonadjacent vertices `z,c`, each adjacent to
all eight vertices of `J`.  The exact deletion-and-contraction recursion in

[`hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py`](../results/hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py)

certifies that `Q` has no `K_7^-` minor.  The recursion starts with singleton
branch sets and exhausts every deletion and every merge of two adjacent
connected branch sets until seven sets remain; it accepts exactly when at
most one pair of sets is nonadjacent.  The same run first accepts literal
`K_7^-` and literal `K_5^-`, rejects undersized and cyclic negative controls,
and then verifies all 42 eligible minimum-degree-four neighbourhood types.

The retained command is

```text
UV_CACHE_DIR=/tmp/uv-cache uv run python \
  results/hc7_k7minus_degree_eight_triangle_poor_edge_packing_verify.py
```

and its expected final negative-calibration line is

```text
negative_calibration=GMs`KK full exterior augmentation is target-free
```

## Scope not refuted

This ten-vertex quotient is not asserted to be seven-connected, nor to lift
to a full critical host.  It refutes only the local quotient inference at
minimum neighbourhood degree three.  Additional uncontracted exterior
structure or colouring-critical information could still force an incident
edge in at most two triangles.
