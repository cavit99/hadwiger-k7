# Wagner barrier to one-centre eight-terminal kernel closure

## Status and precise scope

**Status:** barrier/counterexample to an intermediate claim.

The following proposed local lemma is false.

> **False one-centre kernel lemma.** Let `H` be a simple three-connected
> graph, let `T` be eight labelled vertices, and suppose that `H` is
> `T`-irreducible, `alpha(H[T])=3`, and `H[T]` is `K_4`-free.  Then `H`
> contains a `K_6^-` minor.

Here `T`-irreducible has the meaning used by the bounded terminal-kernel
theorem: no contractible edge has fewer than two ends in `T`.

This is the smallest possible obstruction by order.  It does not refute a
multi-centre composition using the contacts of the other degree-eight
centres, nor does it satisfy the global hypotheses of a hypothetical
minor-minimal seven-chromatic counterexample.

## Construction

Let `W` be the Wagner graph on `Z/8Z`.  Its edges are

```text
i(i+1) for i in Z/8Z,
04, 15, 26, 37.
```

Thus `W` is an eight-cycle together with its opposite perfect matching.  Set

```text
H=W,    T=V(W).
```

Because every edge has both ends in `T`, there is no `T`-legal edge at all.
In particular, `W` is `T`-irreducible.

## Verification

### Three-connectivity

Deleting at most one vertex leaves the spanning cycle connected.  After
deleting two vertices, rotate the labels so that one deleted vertex is `0`
and let the shorter cyclic distance to the other be `d`.

If `d=1`, the undeleted part of the eight-cycle is a path.  If `d=2`, the
isolated cycle interval vertex `1` is joined to the other interval by the
opposite edge `15`.  If `d=3`, the opposite edge `15` joins the two remaining
cycle intervals.  If `d=4`, the opposite edges `15`, `26`, and `37` join the
two intervals.  Hence deletion of any two vertices leaves a connected graph,
so `W` is three-connected.

### Neighbourhood constraints

The graph `W` is triangle-free: the endpoints of an opposite edge have no
common cycle neighbour, and the opposite edges form a matching.  It is
therefore `K_4`-free.

An independent four-set in `W` would also be an independent four-set in its
spanning `C_8`.  The only such sets are the two alternating classes.  Each
contains two edges of the opposite matching, so neither is independent in
`W`.  On the other hand, `{0,2,5}` is independent.  Thus

```text
alpha(W)=3.
```

### Missing minor

The Wagner graph has exactly twelve edges.  Edge and vertex deletion cannot
increase the edge count, and contracting an edge in a simple graph loses at
least the contracted edge.  Consequently every minor of `W` has at most
twelve edges.  Since `K_6^-` has fourteen edges, `W` has no `K_6^-` minor.

There is also a literal exceptional-centre version of the obstruction.  Add
a new vertex `z` adjacent to every vertex of `W`.  Then `d(z)=8` and
`G[N(z)]=W`, so the degree-eight neighbourhood has independence number three
and is `K_4`-free.  The cone has nine vertices and

```text
|E(z join W)|=8+12=20=|E(K_7^-)|.
```

Every minor on seven vertices is a proper vertex-reducing minor of this
connected simple graph and therefore has strictly fewer than twenty edges.
Hence the cone itself has no `K_7^-` minor.

## Consequence for the proof route

Applying the audited bounded terminal-kernel theorem to the eight neighbours
of only one degree-eight centre cannot be terminal.  The order-eight base
already retains all the local exceptional-neighbourhood constraints while
missing the required minor.  Any repair must preserve genuinely additional
information, such as contacts from other centres or a global chromatic
obstruction; those data are discarded by the one-centre kernel statement.
