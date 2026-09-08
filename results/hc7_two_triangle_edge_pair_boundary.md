# Excluding an exterior four-boundary containing the edge pair

**Status:** written proof; a separate internal audit is recorded beside it. This excludes
one boundary configuration, not the entire two-triangle case or Conjecture 19.

All graphs are finite and simple; set neighbourhoods are external. Write
`Q=K_7-2K_2`, with the two deleted edges independent.

**Theorem.** Suppose `G` is seven-connected, `delta(G)>=8`, has no `Q`
minor, and `d(v)=8`. Suppose

`N(v)=A dotcup B dotcup {x,y}`,

where `A,B` are triangles and `xy` is an edge; additional edges are allowed.
Put `H=G-v-B` and `W=V(G)-N[v]`. There is no nonempty `D subseteq W`
such that `N_H(D)={x,y,p,q}` for distinct `p,q in W`.

## Inputs

The [complement theorem](hc7_two_triangle_complement_four_connectivity.md),
SHA-256 `0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`,
makes `H` four-connected under exactly these hypotheses. Its
[adjacent audit](hc7_two_triangle_complement_four_connectivity_audit.md)
has SHA-256 `d074cc7eb384222f1b68ed53728fd721c7a6e7edbf266c55cec313a5c73b2014`.

The [five-root degree-six theorem](hc7_five_root_degree_six.md),
SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`,
applies to five distinct roots consisting of a triangle and two other roots,
with nonempty nonroot set of minimum degree at least six and every nonempty
nonroot subset having at least five neighbours. At least two triangle roots
are admissible: for either admissible root there is a rooted five-bag model
whose only possible missing contact joins that root to one of the other two
roots. Its [adjacent audit](hc7_five_root_degree_six_audit.md)
has SHA-256 `6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`.
No further literature or colouring input is used.

## Proof

Suppose such a set exists and put `C={x,y,p,q}`. A connected component
`D0` of `H[D]` has boundary in `H` contained in `C`. The triangle `A`
lies outside `D0 union C`; therefore four-connectivity forces
`N_H(D0)=C`. Replace `D` by `D0`. Henceforth `D` is connected and
still has the asserted boundary. This reduction does not presume that
any larger unallocated set is connected.

Let `Z` be the component of `H-(D union C)` containing `A`; the literal
triangle ensures that all three A vertices lie in this one component.
There are no edges from `Z` to `D`, so `N_H(Z) subseteq C`. Since `D`
survives outside `Z` and its boundary, four-connectivity gives

`N_H(Z)=C`.

In the original graph, `N_G(Z) subseteq C union B union {v}`. The vertex
`v` contacts `Z` through `A`. Seven-connectivity, again with `D` surviving
outside this boundary, gives `|N_G(Z)|>=7`. The displayed containing set
has eight vertices, so `Z` contacts at least two vertices of `B`, as well
as both `x,y`.

Form the actual induced graph

`F=G[D union B union {x,y}]`.

Every neighbour of a vertex of `D` lies in `D union C union B`: vertices
of `D subseteq W` miss `v`. Thus passing to `F` deletes only the possible
neighbours `p,q`, and every nonroot degree in `F` is at least six.
For every nonempty `X subseteq D`, the vertex `v` lies outside
`X union N_G(X)`, so seven-connectivity gives `|N_G(X)|>=7`. Therefore

`|N_F(X)|=|N_G(X)-{p,q}|>=5`.

The degree-six theorem applies with roots `B union {x,y}` and nonroots
`D`. Among its at least two admissible B roots, choose `b*` contacted by
`Z`; this is possible because `Z` contacts at least two of the three.
Take the resulting five disjoint connected root bags in `F`. Their only
possible missing contact is `b*--x` or `b*--y`, referring to their bags.

Adjoin the two bags `Z` and `{v}`. They are disjoint from all five core
bags and from each other. The vertex `v` contacts every core bag through
its prescribed root and contacts `Z` through `A`. The bag `Z` contacts
the x- and y-rooted bags and at least two B-rooted bags through their roots.
If it misses a B-rooted bag, that root differs from `b*`. Consequently
the only two possible missing contacts in this seven-bag model have
distinct endpoints: one lies inside the core, and the other joins `Z`
to a different B bag. The model contains `Q`, a contradiction. QED

All seven bags are specified subsets of the original graph. The five
core bags are obtained afresh inside `F`; no earlier root-path interiors
or independently chosen helper bags are retained. Chromatic criticality
is unnecessary for this exclusion, and the remaining two-triangle
configurations are not resolved here.
