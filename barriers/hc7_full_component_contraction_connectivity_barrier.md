# Contracting a full component need not preserve six-connectivity

**Status:** explicit counterexample to an intermediate claim, with a
deterministic exhaustive verifier.  The graph contains a `K_7` subgraph, so
the example does not address a version with `K_7^-`-minor exclusion.

The verifier is
[`hc7_full_component_contraction_connectivity_barrier_verify.py`](hc7_full_component_contraction_connectivity_barrier_verify.py).
Its SHA-256 is

```text
bf736e6aeec3dbed5ebadb540811f7548249262e4cca57f92e36937b0177829a.
```

## The false assertion

The following natural strengthening of the full-component property is
false.

> If `G` is six-connected, `S` is an order-six separator and `D` is a
> component of `G-S` with `N_G(D)=S`, then contracting all of `D` to one
> vertex preserves six-connectivity.

Consequently, this contraction cannot be used without an additional
hypothesis in the returned-cut analysis of a minimal `4n` enemy.

## Construction

Let

```text
S={s_0,...,s_5},
A=A_0 dot_union ... dot_union A_5,       |A_i|=2,
B=B_0 dot_union ... dot_union B_5,       |B_i|=4.
```

Make `A` a clique of order twelve and `B` a clique of order twenty-four.
There are no edges inside `S` or between `A` and `B`.  For each `i`, join
`s_i` to every vertex of `A_i union B_i`, and add no other edges incident
with `S`.  Call the resulting graph `G`.

Then `G-S` has precisely the two components `A` and `B`, and both are full
to `S`.

## Verification of six-connectivity

Let `X` contain at most five vertices.  Both `A-X` and `B-X` are nonempty
cliques.  To destroy the path through index `i` from `A-X` to `B-X`, the
set `X` must contain `s_i`, all of `A_i`, or all of `B_i`.  These six
index blocks are disjoint, and destroying the path for one index costs at
least one vertex.  Thus some index supplies a surviving path

```text
(A-X)-s_i-(B-X).
```

Moreover, every surviving `s_j` retains a neighbour in `A_j union B_j`,
since that union has six vertices.  Hence `G-X` is connected.  Deleting
`S` separates `A` from `B`, so `G` is exactly six-connected.

## The failed contraction

Contract the full component `A` to a vertex `a`.  In the quotient,

```text
N(s_i)={a} union B_i.
```

Deleting the five vertices `{a} union B_i` isolates `s_i`.  The quotient
therefore has connectivity at most five and is not six-connected.

This is deliberately a target-rich warning: the clique `B` contains a
`K_7` subgraph.  The example refutes only the bare inference from
six-connectivity and fullness.  It does not refute the possibility that
`K_7^-`-minor exclusion, the special split origin of the quotient, or some
additional boundary condition makes such a contraction safe.

## Reproduction

From the repository root run

```text
python3 -B barriers/hc7_full_component_contraction_connectivity_barrier_verify.py
```

The checker uses only the Python standard library.  It constructs the
graph, exhausts all deletions of at most five vertices, checks the two full
components behind `S`, checks the displayed five-cut after contraction,
and confirms a `K_7` subgraph in `B`.
