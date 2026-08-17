# Six-connectivity does not force five visible Lo bags

**Status:** explicit target-sensitive barrier with a written proof and a
deterministic certificate checker.  It does not meet the `4n` density
threshold.

## Assertion refuted

The following rooted visibility assertion is false:

> If `G` is six-connected and target-free, and `G-v` is five-connected,
> non-planar and has minimum degree at least five, then some `K_6^-` model
> in `G-v` has at least five bags meeting `N_G(v)`.

## Construction and Lo hypotheses

Let `I` be the icosahedron, let

```text
G=K_1 join I,
```

and denote the universal vertex by `a`.  Choose any `v in V(I)`.  Since
`I` is five-connected, `G` is six-connected.  Moreover

```text
|V(G)|=13,       |E(G)|=42=4|V(G)|-10.
```

The graph `G` has no `K_7^-` minor.  Indeed, remove from a putative model
the branch set containing `a`, if there is one.  The six remaining bags
would give a `K_6` or `K_6^-` minor in the planar graph `I`; if no bag
contains `a`, the entire model already lies in `I`.  Both are impossible.

The graph `G-v` is five-connected, has twelve vertices, thirty-six edges
and minimum degree five.  It is non-planar by the planar edge bound, so it
satisfies the hypotheses of Lo's Theorem 1.3.

## Four is the exact maximum visibility

Consider any near-six model in `G-v`.  One bag `A` must contain `a`, since
otherwise the model would be a non-planar minor of `I-v`.  The bag `A` is
visible from `v`.

Suppose that at least five bags were visible.  At least four of the five
bags other than `A` would then meet `N_I(v)`.  Those five bags, together
with the singleton `{v}`, lie in `I`.  Among the five old bags at most one
adjacency is missing, and `{v}` misses at most one of them.  Their contact
graph therefore has at least thirteen of the fifteen possible edges.  A
simple planar graph on six vertices has at most twelve edges, contradicting
the planarity of `I`.  Thus every near-six model has at most four visible
bags.

The bound is attained.  In the standard NetworkX labelling, take `v=0`,
`a=12`, and the bags

```text
{1}, {2}, {3}, {5,6}, {4,7,8,10}, {12}.
```

Their sole missing adjacency is between `{1}` and `{3}`, and exactly four
bags meet `N_G(0)`.  Hence maximum visibility is exactly four.

## Exact scope

The construction refutes any attempt to derive five visible bags from
six-connectivity, target exclusion and Lo's local hypotheses alone.  Its
density is `4n-10`, so it does not refute an argument that genuinely uses
the ten additional edges available at `4n`.

The checker
[`hc7_k7minus_lo_low_visibility_apex_barrier_verify.py`](hc7_k7minus_lo_low_visibility_apex_barrier_verify.py)
verifies the graph parameters and the displayed four-visible model.  The
upper bound is the computation-free planar argument above.

## Primary source

- O.-H. S. Lo,
  [*A characterization of graphs with no `K_{3,4}` minor*](https://arxiv.org/abs/2603.27973v1),
  Theorem 1.3.
