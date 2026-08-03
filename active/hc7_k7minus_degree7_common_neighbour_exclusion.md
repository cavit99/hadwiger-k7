# Saturated degree-seven vertices force a `K_7^-` minor

**Status:** written unbounded reduction with a computer-assisted finite
lemma; separate internal audit.

## Lemma 1 (nine-vertex quotient)

Let `R` be a graph on seven vertices with minimum degree at least four, and
let `A subseteq V(R)` have order at least six.  Form `Q` from `R` by adding
two vertices `v,c` such that

- `v` is adjacent to every vertex of `R`;
- `c` is adjacent to every vertex of `A`; and
- `vc` is not an edge.

Then `Q` contains a `K_7^-` minor.

### Finite verification

The complement `F` of `R` has maximum degree at most two.  Hence every
component of `F` is a path or a cycle.  There are 29 multisets of path and
cycle components having total order seven.

The verifier
[`hc7_k7minus_degree7_quotient_verify.py`](hc7_k7minus_degree7_quotient_verify.py)
generates these 29 types directly, without graph-isomorphism software.  For
each type it checks the full attachment set and each of the seven possible
single missed vertices.  For every one of the resulting `29*8=232` cases,
it constructs seven disjoint connected branch sets and verifies that at
most one pair of branch sets is nonadjacent.

The search is exact.  Since `Q` has nine vertices, every seven-bag minor
model is represented by a partition of a subset of seven, eight, or nine
vertices into seven nonempty sets.  The verifier enumerates all 750 such
partitions, checks connectivity inside each bag, and checks every required
interbag adjacency.  It also tests the model checker on `K_7^-` as a known
positive instance and on `K_6` and `K_{2,2,2,2}` as known negative
instances.

Run:

```bash
python3 active/hc7_k7minus_degree7_quotient_verify.py
```

Expected output:

```text
complement types: 29
full-or-one-missed attachment cases: 232
model support orders: {7: 67, 8: 102, 9: 63}
certificate digest: b98ac56930aa7044c3a6a7c029b75cd85feb39f4dabd8476a0ba7f08ccdb7306
GREEN: every quotient contains a certified K_7^- minor
```

This proves Lemma 1 within the stated computational trust boundary.

## Theorem 2 (degree-seven exclusion)

Let `H` be a six-connected graph with at least nine vertices.  Suppose that

1. `H` has no `K_7^-` minor; and
2. every edge of `H` has at least four common neighbours.

Then `H` has no vertex of degree seven.

### Proof

Suppose that `d_H(v)=7` and put `S=N_H(v)`.  For every `s in S`, each common
neighbour of `v,s` belongs to `S`.  The four-common-neighbour hypothesis
therefore gives

```text
delta(H[S]) >= 4.
```

Since `|V(H)|>=9`, the graph `H-N_H[v]` is nonempty.  Let `C` be one of its
components.  Its external neighbourhood is contained in `S`, because `v`
has no neighbours outside `N_H[v]`.  Six-connectivity gives

```text
|N_H(C)| >= 6.
```

Contract the connected subgraph `C` to one vertex `c`, and delete every
other vertex outside `N_H[v]`.  The resulting minor contains the graph `Q`
of Lemma 1 with

```text
R=H[S]  and  A=N_H(C).
```

Lemma 1 supplies a `K_7^-` minor in `Q`, and hence in `H`, contrary to
hypothesis 1.  Therefore no degree-seven vertex exists.  \(\square\)

## Scope

The finite calculation is confined to a literal nine-vertex quotient.  The
reduction from an arbitrary host is written and uses a whole exterior
component, so the theorem is unbounded and is not an inference from testing
hosts of bounded order.

The theorem closes the degree-seven half of the saturated six-connected
enemy reduction.  It does not itself prove that every edge of such an enemy
has four common neighbours.
