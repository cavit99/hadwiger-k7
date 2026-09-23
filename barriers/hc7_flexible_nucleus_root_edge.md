# A flexible minimal list obstruction need not become colourable when its root edge is deleted

**Status:** explicit counterexample to an intermediate claim; written proof,
not separately audited. This is a local barrier for the
[split-clique construction](../active/hc7_c21_rooted_density_construction.md#next-attack-the-split-clique-neighbourhood),
not a counterexample to HC7 or to a statement using all the original
seven-connected critical-host hypotheses.

## Statement refuted

Even in a `K7`-minor-free literal split-clique frame, the following
properties do **not** imply that deleting the root edge `ab` makes the
list instance colourable:

1. `D` is a four-clique fixed in colours `1,2,3,4`, and `A={a,b}` is an
   edge anticomplete to `D`.
2. `X=Z` is a connected component of `K-D`, contacts every vertex of `D`,
   and is an inclusion-minimal induced uncolourable graph for the lists
   `L(v)=[5] minus c(N_D(v))`, additionally forbidding five at both
   vertices of `A`.
3. The whole `K` has two five-colourings fixing `D`, with opposite
   owners of colour five on `A`. Every five-colouring fixing `D` uses
   five on `A`.

Here `X=Z`, so there are no outside vertices or edges to restore. The
frame is six-colourable and is not seven-connected.

## A planar vertex-critical graph with a redundant edge

Let `J` have vertices `0,...,6` and edges

\[
 03,04,05,06,12,14,15,23,24,34,36,56.
\]

Put `a=0,b=4`. The graph `J-ab` is not three-colourable. Its diamonds
on `{0,3,5,6}` and `{1,2,3,4}` force, respectively, `3=5` and `1=3`
in any three-colouring. This contradicts the edge `15`. Here a diamond
is `K4` minus one edge; its nonadjacent vertices receive the same colour
in every three-colouring.

The following table gives three-colourings of every vertex deletion.
Columns are vertices; a dash denotes the deleted vertex.

| Deleted | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | — | 2 | 3 | 2 | 1 | 3 | 1 |
| 1 | 2 | — | 2 | 1 | 3 | 1 | 3 |
| 2 | 1 | 1 | — | 3 | 2 | 3 | 2 |
| 3 | 2 | 2 | 3 | — | 1 | 1 | 3 |
| 4 | 3 | 3 | 1 | 2 | — | 2 | 1 |
| 5 | 3 | 2 | 3 | 2 | 1 | — | 1 |
| 6 | 3 | 2 | 3 | 2 | 1 | 1 | — |

Adding the deleted vertex in a fourth colour proves that `J` is
vertex-critical four-chromatic. The preceding diamond argument shows
that `J-ab` is still four-chromatic.

A planar embedding has the following cyclic clockwise neighbour orders:

\[
\begin{array}{c|l}
0&3,4,5,6\\
1&4,2,5\\
2&3,1,4\\
3&0,6,2,4\\
4&2,1,0,3\\
5&1,6,0\\
6&5,3,0.
\end{array}
\]

Its face walks are `063`, `056`, `0415`, `034`, `324`, `36512`,
and `421`. The rotation system is orientable and connected, with
`7-12+7=2`, so it is a sphere embedding. These finite tables are
checkable certificates; no search bound is a premise of the argument.

## The minimal list obstruction and both colourings

Let `H=r join J`, where `r` is universal in `H`. Thus `H` is
vertex-critical five-chromatic, and `H-ab` is still five-chromatic.
Add `y` adjacent to exactly `V(H)-A`, obtaining `Z`. Add a four-clique
`D`, join it completely to `y`, and leave it anticomplete to `H`.
This is `K`, with `X=Z`. Fixing the colours of `D` gives exactly

\[
 L(a)=L(b)=[4],\qquad L(v)=[5]\ (v\in V(H)-A),
 \qquad L(y)=\{5\}.
\]

An `L`-colouring of `Z` would colour `y` five and therefore put every
vertex of `H` in `[4]`, which is impossible. For `v` in `H`, a
four-colouring of `H-v` together with `y=5` colours `Z-v` from its lists.
For `Z-y`, colour `r` five and four-colour `J`. Thus `Z` is
inclusion-minimal induced uncolourable.

For either `s` in `A`, four-colour `H-s` and colour both `s,y` five.
They are nonadjacent, so this five-colours all of `K` while fixing `D`.
Conversely, every such colouring has `y=5`; hence `H-A` avoids five,
and the five-chromatic graph `H` forces five onto `A`. Exactly one root
has colour five because `ab` is an edge. All four `D` contacts occur
at `y` inside `Z`.

Nevertheless `Z-ab` remains `L`-uncolourable: its forced colour `y=5`
would otherwise give a four-colouring of the five-chromatic `H-ab`.

## A `K7`-minor-free split-clique frame

Add `p,u`, join `p` to `a,b`, and give `u` exactly the neighbours
`D union {p,a,b}`. Then `N(u)=K3 dotunion K4`, and
`K=G-({u} union B)` for `B={p}`. Each preceding colouring of `K`, with
`p=6`, colours `G-u` with the same entire sixth colour class `B` and
also colours `G/up`.

To see that `G` has no `K7` minor, add the edge `uy`. The two sides of
the resulting clique separation have intersection `{u,y}`. One is the
six-clique `D union {u,y}`. The other, after deleting `r,y`, is the
planar graph obtained by gluing a `K4` on `{a,b,u,p}` to `J` along its
edge `ab`. Thus the second side is two-apex planar. It has no `K7`
minor: deleting its two apex vertices from any proposed seven-bag
model would leave at least five pairwise adjacent bags in a planar
graph. A clique sum along at most two vertices preserves exclusion
of `K7`: all model bags avoiding the separator must lie on one side,
and the separator clique allows the remaining bags to be restricted
to that same side. Both completed sides exclude `K7`, and therefore
so does their subgraph `G`.

The frame is six-colourable. Give `D` its fixed colours, put `u=y=5`
and `r=6`, use the four-colouring `(3,4,3,2,1,2,1)` of `J`, and put
`p=2`. Every edge is proper. Moreover `p` has degree three, so `G` is
not seven-connected and is not the hypothetical critical host.

This refutes root-edge deletion colourability inferred from the stated
local data, even together with `K7` exclusion. The original host's
seven-connectivity and proper-minor colouring constraints remain
available and are not refuted.
