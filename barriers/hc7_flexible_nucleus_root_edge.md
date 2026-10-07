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

## Maximum flexibility does not force an exchange

**Status:** explicit counterexample to a further intermediate claim;
written proof, not separately audited. This construction is distinct from
the root-edge deletion barrier above. Even a uniquely largest flexible
deleted class, together with all its fixed-boundary five-colourings, need
not supply a bipartite target component or a cardinality augmentation.
This does not refute the full six-colouring-or-`K7` outcome.

Write `G_0` for the preceding frame, with `D={d_1,d_2,d_3,d_4}`.
For each `i in {1,2,3,4}`, add `v_i` adjacent to exactly
`{y} union (D-{d_i})` among existing vertices, and add `r_i` adjacent
to `y,v_i`. Put

`W=(V(G_0)-{u,p}) union {v_1,v_2,v_3,v_4}`.

For every `w in W`, add two private leaves adjacent only to `w`.
There are no other new edges. Call the resulting graph `G^+` and put

`B={p,r_1,r_2,r_3,r_4} union {all new leaves}`.

The set B is independent and meets `N(u)` exactly at p. The graph
`G^+-({u} union B)` is the original K with the four vertices `v_i`.
Every five-colouring fixing `d_i=i` has `y=5` and therefore `v_i=i`.
Consequently both opposite-owner colourings extend, and every such
five-colouring still uses five on exactly one of a,b. Giving B colour
six produces the required whole-graph responses on `G^+-u`.

For any two such responses phi,psi and every `i in {1,2,3,4}`, consider

`F_i=G^+[B union phi^{-1}(5) union psi^{-1}(i)]`.

The `d_i`-component of `F_i` contains the edge `d_i y` and the triangle
`y v_i r_i y`: y always has colour five, `v_i` always has colour i,
and `r_i` belongs to B. Thus every target component is nonbipartite,
for all response choices and all four palette labels.

Moreover B is the unique maximum independent set of `G^+-u`. If S is
independent and `T=S intersect W`, its vertices exclude the `2|T|`
distinct private leaves attached to T. Since every vertex outside W
in `G^+-u` belongs to B,

`|S| <= |B|-2|T|+|T| = |B|-|T|`.

Equality with `|B|` therefore requires `T=empty` and `S=B`. In particular
B is uniquely largest among flexible deleted classes. Neither a larger
independent class nor a different equal-sized flexible class exists,
even when the triangle vertex in the class may change.

The graph still excludes `K7`. Each `v_i` is attached on the existing
four-clique `{y} union (D-{d_i})`, each `r_i` on the edge `y v_i`, and
each leaf on a singleton. These are clique attachments whose added
cliques have order at most five; the clique-separation argument above
preserves `K7` exclusion at each attachment. The displayed six-colouring
of `G_0` extends by setting `v_i=i`, `r_i=6`, and giving each leaf any
colour different from its neighbour.

The original critical-host hypotheses still fail: p retains degree three,
so `G^+` is not seven-connected, and the whole graph is six-colourable,
so it is not the required proper-minor-critical host. The barrier concerns
inferences from maximum B and its full colouring relation alone. A use
of the original host's connectivity or proper-minor constraints remains
possible. No enumeration or computer-assisted conclusion is used here.

## Preserving the quotient can prevent every lift

**Status:** explicit counterexample to a restricted restoration strategy;
written proof, not separately audited. A six-colourable K7-minor-free
split-clique frame need not admit a colouring obtained by restoring its
central four-clique while retaining any colouring of its contraction.
The example also has no literal K6. It is not seven-connected.

Start with `R={u} union P` inducing K4 and `{u} union D` inducing K5,
with no P--D edges. For each p in P add a disjoint private graph
`F_p=K2 join C5`, and join p to all of F_p. There are no other edges.
In particular `N(u)=P dotunion D` exactly. Each F_p is five-chromatic,
and each block `p join F_p=K3 join C5` is six-chromatic with clique
number five. It has no K7 minor: discarding the at most three bags
meeting its K3 would leave a K4 minor in C5, which is impossible.
The whole graph is a clique sum of these blocks, K4 and K5 along
single vertices, so excludes K7 and has no literal K6. Six-colour R
and `{u} union D` consistently; each private F_p can use the five
colours other than p's. This colours the entire graph.

Contract R to q. In every six-colouring of this quotient, normalised
by `q=6,D=1,2,3,4`, each F_p must use all of colours one to five.
Thus every p has an exterior neighbour of every colour in `[5]`.
Keeping this exterior colouring leaves every P vertex only colour six,
so the triangle cannot be restored. This holds for every quotient
colouring, not merely one chosen response or its Kempe class.

The [two-step exterior repair](../active/hc7_split_clique_global_colour_lifts.md#repairing-a-clique-contraction-colouring-in-the-original-host)
does restore the graph, by moving selected private colour classes to
six after q is deleted. The barrier therefore rejects the requirement
that intermediate exterior colourings continue to descend to the
quotient. It does not reject recolouring in the original host. Its
cutvertices and six-colourability exclude the critical-host hypotheses.
