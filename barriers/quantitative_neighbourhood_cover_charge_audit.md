# Audit of the maximum-star cover-charge counterexample

**Verdict: GREEN for the stated counterexample and its limited scope.**
Separate internal review by operation-challenger, 13 September 2026;
this is not external peer review.

Reviewed [source](quantitative_neighbourhood_cover_charge.md) SHA-256:
`05eef613fd99c198426e8d76195d3de6911e7273f1941e8c2c50d7895cb97ea8`.

The construction has order `2m+3`. Its displayed width-two decomposition
covers every edge; the bags containing each of a, b and x_i form connected
subtrees. Edge contraction joins two intersecting bag subtrees and cannot
increase bag size. The leaf-bag argument therefore gives a three-colouring
of every minor, proving the all-minor independence bound. The displayed
five-cycle proves that H itself needs three colours. With
`r=ceil((2m+3)^(2/3))`, both `r>=3` and the order cap hold.

The leaves a,b are the entire independent neighbourhood of u, so the
contracted star is maximum, not merely maximal. Its quotient consists of
the m stated triangles with their common vertex w. Every original
neighbourhood is independent. Each surviving x_i,y_i has tau one, while
the matching in the neighbourhood of w gives tau m. The order loss is
two, the positive singleton change is `2m`, and the net change in the sum
over all quotient vertices is `3m`. These include the new merged vertex
and omit the three removed vertices, whose original contributions were
zero. Since `m/r` tends to infinity, no absolute constant gives either
proposed charge uniformly over this family.

The alternative star at a has exactly the independent leaves
`{u,x_1,...,x_m}`. Its quotient is the claimed collection of triangles
through the edge wb, so its order loss is `m+1` and its chromatic number
remains three. Thus the counterexample does not exclude a favourable
choice of centre or a globally selected sequence.

The graph is three-chromatic with `r>=3`; it satisfies neither the required
high-chromatic gap nor the low-tau operation's positive-threshold regime.
The proof therefore refutes the stated arbitrary-choice charge, not R,
its critical-host application, or its proposed colouring consequence.
No computation, novelty claim or significance comparison is certified.
