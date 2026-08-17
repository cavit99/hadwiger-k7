# Five visible Lo bags do not suffice

**Status:** explicit target-sensitive barrier with deterministic verifier.
It does not meet the `4n` density threshold.

## Assertion refuted

The following rooted augmentation assertion is false, even when `G-v`
satisfies all the hypotheses of Lo's Theorem 1.3:

> If `G` is six-connected and `G-v` has a `K_6^-` model for which five
> bags meet `N_G(v)`, then `G` has a `K_7^-` minor.

## Construction

Let

```text
G=K_{2,2,2,2}
```

with parts `{0,1}`, `{2,3}`, `{4,5}`, `{6,7}`, and put `v=0`.  The graph
has

```text
|V(G)|=8,       |E(G)|=24=4|V(G)|-8,       kappa(G)=6.
```

It is `K_7^-`-minor-free.  A seven-bag model on eight vertices either
deletes one vertex or has one connected two-vertex bag.  In the first case
the remaining seven singletons contain three nonadjacent twin pairs.  In
the second, the merged bag uses two different parts and the remaining
singletons still contain the two untouched twin pairs.  Either way at least
two branch-bag adjacencies are missing.

Put `H=G-v`.  Then `H` is five-connected, has minimum degree five, and has
eighteen edges on seven vertices, so it is nonplanar.  In particular it is
in the exact regime of Lo's Theorem 1.3; note also that `G` itself already
satisfies `|E(G)|>=4|V(G)|-9`.

The six bags

```text
{1}, {3}, {2,4}, {5}, {6}, {7}
```

form a `K_6^-` model in `H`.  Their only missing adjacency is between
`{6}` and `{7}`.  The neighbourhood of `v` is `{2,3,4,5,6,7}`, so exactly
five bags are visible: `{1}` is the unique invisible bag.  Visibility six
is impossible, since adjoining `{v}` to such a model would give the
forbidden `K_7^-` minor.  Hence the maximum visibility is exactly five.

The two missing edges in the resulting seven-bag quotient are the
independent pair

```text
v--{1},       {6}--{7}.
```

The collision bag `{2,4}` contains two roots, but splitting it produces
three missing pairs among the six visible singletons, namely
`2--3`, `4--5`, and `6--7`.  It is therefore not a safe split.

## Exact scope

This example refutes the claims that five visible bags alone suffice, that
six-connectivity forces visibility six, or that an arbitrary root collision
can be split safely.  It retains target exclusion and all of Lo's local
hypotheses after deleting `v`.  Its density is `4n-8`, not `4n`; it does
not refute a conclusion that genuinely uses the eight additional edges.

The verifier
[`hc7_k7minus_lo_five_visible_bags_barrier_verify.py`](hc7_k7minus_lo_five_visible_bags_barrier_verify.py)
checks the construction, the exact target exclusion, every near-six model
in `H`, and every possible safe split.  Its exhaustive profile is

```text
near_six_models=12,       visibility_profile={(5,1): 12}.
```
