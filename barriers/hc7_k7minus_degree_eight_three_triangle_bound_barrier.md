# Barrier to a three-triangle bound at a degree-eight vertex

**Status:** barrier/counterexample to an intermediate claim; computation-free.

## Refuted claim

> If `G` is `K_7^-`-minor-free and `v` has degree eight, then some edge
> incident with `v` lies in at most three triangles.

## Counterexample

Let `J=C_8^2`: its vertices are `Z_8`, and two vertices are adjacent when
their cyclic distance is one or two.  This is the planar square-antiprism
graph.  Let

\[
                         G=K_1\vee J
\]

and denote the apex by `v`.  The graph `J` is four-regular, so `v` has degree
eight and every edge `vx` lies in exactly four triangles, one for each
neighbour of `x` in `J`.

The graph `G` is `K_7^-`-minor-free.  A target model which avoids `v` would
lie in the planar graph `J`, which is impossible.  If `v` belongs to one
branch set, deleting that branch set from the model leaves either a `K_6`
or a `K_6^-` minor in `J`.  Both are nonplanar: `K_6^-` has fourteen edges,
more than the planar maximum twelve on six vertices.  This again contradicts
the planarity of `J`.

Thus the degree-eight conclusion cannot be improved from four triangles to
three for arbitrary target-free graphs.

## Scope not refuted

The example has connectivity five: the square-antiprism graph is
four-connected, and adjoining one universal vertex raises its connectivity
by one.  It therefore does not refute a stronger three-triangle conclusion
under seven-connectivity, critical colourability, or another global
hypothesis.
