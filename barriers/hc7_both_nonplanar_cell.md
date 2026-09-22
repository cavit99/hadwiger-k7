# Both sides of a seven-boundary cell can be nonplanar

**Status:** explicit counterexample with computer-checked finite hypotheses;
not separately audited. It shows that joint nonplanarity
of the gate side and port side does not finish the cell construction.
The [deterministic verifier](hc7_both_nonplanar_cell_verify.py) checks the
finite hypotheses and explicit witnesses below. No minor-exclusion search
is used.

## Construction

Let `a,b` be cycles of length five and `c,d,e,f` cycles of length seven,
with vertices indexed from zero. Add two vertices `p,z`.

For cycles `A,B` and a list of positive integers `r_i` summing to `|B|`,
make an annulus as follows. Set `j_0=0` and `j_(i+1)=j_i+r_i`, and add

    A_i B_j  for j_i <= j <= j_(i+1), with B indices modulo |B|.

Use precisely the following five annuli, retaining every cycle edge:

| Cycles | Runs |
| --- | --- |
| `a,b` | `1,1,1,1,1` |
| `a,c` | `2,2,1,1,1` |
| `b,d` | `2,2,1,1,1` |
| `c,e` | `1,1,1,1,1,1,1` |
| `d,f` | `1,1,1,1,1,1,1` |

Join `p` to every vertex of `e`, and `z` to every vertex of `f`.
Call this 40-vertex graph `H`. It is a planar triangulation: draw the
rings successively as `e,c,a,b,d,f`, triangulate each displayed annulus,
and cap the two ends with `p,z`. It has 114 edges.

Add `h1` adjacent to every other vertex. Add `h0` adjacent to `h1` and
every vertex of `H` except

    O={a0,a1,b0,b1}.

The resulting graph `G` has 42 vertices and 191 edges. Set

    X=b union d union f union {z},
    T={h1,a3,a4},
    F=a0-a1-a2-h0,
    K={h0,h1,p,e0,e1}.

Here cycle letters denote their full vertex sets. The exact boundary is
`N_G(X)=T union V(F)`, of order seven. The path `F` is induced and meets
the literal clique `K` only at `h0`. Its extremes have no common neighbour
in `X`: the only X-neighbours of `a0` are `b0,b1`, and both miss `h0`.
Also `p in K` has no neighbour in `X`.

## Connectivity and neighbourhood inequalities

The verifier checks all 102,091 deletions of at most four vertices from
`H`, each leaving a connected graph. It also checks

    |N_H(Y)|>=6  for every nonempty Y subseteq O.

These two finite facts imply seven-connectivity of `G`. After deleting
at most six vertices, a surviving `h1` connects everything. If both
added vertices were deleted, at most four H vertices were deleted.
Otherwise only `h0` remains and at most five H vertices were deleted.
Any remaining H component with no h0-neighbour would be contained in
`O`; its H boundary would have been deleted, contradicting the second
check. The minimum degree is seven, so connectivity is exactly seven.

For every `v in V(G)` the verifier checks

    alpha(G[N_G(v)]) <= d_G(v)-5.

At vertices of `H` it excludes every independent set of the first
forbidden size. At either added vertex, the seven disjoint edges
`c_i e_i` in its neighbourhood give the required upper bound.

The gates already induce a triangle. The verifier checks that
`G[X union T]` is four-connected; deleting `h1,b0,b3,b4` separates
`{a3,a4}` from the remaining vertices, so its connectivity is exactly four.

## Both sides are nonplanar, but G has no K7 minor

For either `h=h1` or `h=h0`, the following five disjoint connected sets
are pairwise adjacent:

    {h}, {z}, {f0}, {f1}, {f2,f3,f4,f5,f6}.

They give a `K5` minor in `G[X union T]` when `h=h1`, and in
`G[X union V(F)]` when `h=h0`. Both sides are therefore nonplanar.

Nevertheless `G` has no `K7` minor. Deleting `h0,h1` leaves the planar
graph `H`. Any seven pairwise adjacent branch sets would have five
avoiding those two vertices, giving a `K5` minor in `H`.
The verifier also checks an explicit six-colouring.

## Scope and reproducibility

This refutes the proposed inference from seven-connectivity, the local
Dirac bounds, an exact seven-boundary cell, an outside literal five-clique,
the stated induced-path data and four-connected gate torso, even with
**both** sides nonplanar, to a `K7` minor.

It does not refute a colouring-or-minor theorem. The graph is explicitly
six-colourable. Neither seven-contraction-criticality nor the original
`N(u)=K3 dotunion K4` frame and its minimum reserved sets is realised by
this construction. Those additional premises must enter any repair.

Run:

    UV_CACHE_DIR=/tmp/hadwiger-k7-uv-cache uv run python3 barriers/hc7_both_nonplanar_cell_verify.py

Expected output records the 42-vertex graph, the cut-check count, both
explicit five-clique models and the six-colouring. The script uses only
the Python standard library and is run through `uv`.
