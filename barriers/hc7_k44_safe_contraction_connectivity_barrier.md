# Labelled safety alone does not preserve ambient seven-connectivity

**Status:** barrier/counterexample to the unconditional claim below, with a
written proof and an [internal audit](hc7_k44_safe_contraction_connectivity_barrier_audit.md).
The example is target-rich. It does not refute T44 or preservation under
target-free or labelled-terminal-free hypotheses.

## Claim refuted

> Let a seven-connected graph `G` contain a specified literal `K_{4,4}`
> on `S`, with three-connected exterior `C=G-S`. If an exterior edge
> contraction preserves three-connectivity and every inequality
> `lambda(W)=|N_C(W)|+|N_G(W) cap S|>=7` under union labelling, then the
> whole quotient is seven-connected.

## Construction and proof

Let `C=K_7` on `c0,...,c6`; take an induced core `K_{4,4}` and a
distinguished core vertex `s`. Join the other seven core vertices to all
of `C`, and join `s` precisely to `c0,c1,c2`.

The graph is seven-connected. After at most six deletions, at least one
exterior vertex and at least one of the seven fully attached core vertices
survive. All surviving vertices other than `s` are in one component.
If `s` survives, at least one of its seven neighbours survives and joins it
to that component. Its degree seven gives the matching upper bound on
connectivity.

Contract `c0c1`. The new exterior is `K_6`, hence is three-connected.
Every nonempty exterior set before or after contraction has `lambda>=8`:
a set meeting a neighbour of `s` uses eight labels, while a set missing
all such neighbours has at least two exterior boundary vertices and uses
the other seven labels. The edge is therefore safe.

Nevertheless `s` now has degree six. Its six neighbours form a cut, so the
quotient is not seven-connected. Contraction lowers connectivity by at
most one, so its connectivity is exactly six.

The exterior contains `K_7`, and also contains all three labelled terminal
configurations. Thus target-free and terminal-free hypotheses both fail.
The example does not refute the
[new preservation theorem](../results/hc7_k44_safe_contraction_preservation.md):
the original degree of `s` is seven, below its required core-degree bound.
