# Two exterior components do not force codegree two in the five-connected case

**Status:** explicit `K_7^-`-minor-free counterexample, with a deterministic
exhaustive verifier.

The verifier is
[`hc7_k7minus_fiveconnected_degree_eight_two_component_barrier_verify.py`](hc7_k7minus_fiveconnected_degree_eight_two_component_barrier_verify.py).
Its SHA-256 is

```text
a48b585a02c2cad65a5121707fcd2f4c1f783382bff092208e2b5b84a89bd7da.
```

## The false assertion

The following proposed extension of the six-connected degree-eight theorem
is false.

> If `G` is five-connected and `K_7^-`-minor-free, `v` has degree eight,
> and `G-N[v]` has at least two components, then some edge incident with
> `v` has codegree at most two.

The obstruction already occurs with two singleton exterior components and
with every edge at `v` having codegree exactly three.

## Construction

Let `J` be the cube on vertices `{0,...,7}`, with edges

```text
01 05 06 12 17 23 26 34 37 45 46 57.
```

Add three pairwise nonadjacent vertices `v,x,y`.  Join `v` to all eight
vertices of `J`, and put

```text
N(x)={3,4,5,6,7},       N(y)={0,1,2,6,7}.
```

There are no further edges.  Thus

```text
|V(G)|=11,       |E(G)|=30,       degree(v)=8,
G-N[v] = {x} dot_union {y}.
```

For each `u in V(J)`, the common neighbours of `u` and `v` are precisely
the three neighbours of `u` in the cube.  Hence every edge `uv` has
codegree three.

## Exact checks

The verifier exhausts all vertex deletions of order at most four and finds
the remaining graph connected.  Deleting `N(x)`, which has order five,
isolates `x`; consequently `G` is exactly five-connected.

It then performs an exact minor search.  Starting with singleton branch
sets, the search recursively deletes a branch set or merges two touching
branch sets.  At seven remaining branch sets it tests whether at most one
pair is nonadjacent.  These operations enumerate every possible minor
model, and none is a `K_7^-` model.

## Scope

This example closes the bare five-connected, two-exterior-component route.
The six-connected theorem is unaffected: its proof uses attachments of
size at least six, whereas `x` and `y` each have five attachments here.

The graph is not a counterexample to the dense extremal conjecture:
`30<4(11)`.  More importantly, density in the original graph does not by
itself remove the local profile, because contracting two internally dense
exterior components can produce this sparse quotient.  Any repair must use
the component excess, the special split origin of the five-connected
quotient, or another global condition; five-connectivity, target exclusion
and the mere presence of several exterior components are insufficient.

## Reproduction

From the repository root run

```text
python3 -B barriers/hc7_k7minus_fiveconnected_degree_eight_two_component_barrier_verify.py
```

The checker uses only the Python standard library.  It verifies the edge
set, exact five-connectivity, the two exterior components, all eight
codegrees and exhaustive absence of a `K_7^-` minor.
