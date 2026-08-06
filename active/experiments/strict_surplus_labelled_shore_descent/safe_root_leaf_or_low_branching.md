# Safe blocked root or a low-branching root carrier

**Status:** experimental written reduction; independent audit pending.

Use the strict-surplus canonical setting at a reserve-blind degree-seven
vertex `x`.  Put

\[
N=N_G(x),\qquad H=G[N],\qquad
q=q(G)\ge1.
\]

Let

\[
\mathcal M=(D,Q_1,\ldots,Q_5)
\]

be a spanning contact-maximal `K_6` model in `G-x`, and suppose that `D`
contains at least two vertices of `N`.  Call a foreign bag uncontacted when
it contains no member of `N`.

A root `s in N` is **safe at `x`** when

\[
d_H(s)\le q+3.
\]

Equivalently, the edge `xs` is density-safe.

## 1. At least five safe roots

### Lemma 1.1

The graph `H` has at most thirteen edges and at most two vertices of degree
at least five.  Consequently at least five roots are safe at `x`.

### Proof

For each `s in N`, the six-vertex graph `H-s` is the canonical boundary
`G[T_s]`.  It contains neither a literal `K_4` nor a `K_5^-` minor, and
therefore has at most ten edges.  Summing over the seven choices gives

\[
5|E(H)|=\sum_{s in N}|E(H-s)|\le70,
\]

so `|E(H)|<=14`.

Equality is impossible.  If `|E(H)|=14`, every `H-s` has ten edges and
`H` is four-regular.  Its complement is a two-regular graph, hence `C_7`
or `C_3 dotcup C_4`.

- If the complement is `C_7`, delete one cycle vertex.  In the resulting
  complementary path `1-2-3-4-5-6`, contract the edge `25` of `H`.
  The ends have no common neighbour in `H`, so contraction changes a
  ten-edge graph on six vertices into a nine-edge graph on five vertices.
- If the complement is `C_3 dotcup C_4`, delete one vertex of the
  four-cycle.  Write the remaining complement as the triangle `abc` and
  the path `d-e-f`.  Contract the edge `ae` of `H`; again its ends have no
  common neighbour.

Either contraction gives a `K_5^-` minor in some `H-s`, a contradiction.
Thus `|E(H)|<=13`.

Suppose that three vertices `a,b,c` have degree at least five.  They cannot
span a triangle: each would then have at least three neighbours in the
remaining four-set, giving at least nine incidences into a set whose
vertices can each see at most two members of the triangle in a `K_4`-free
graph.  They cannot span at most one edge either, because an isolated one
would need five neighbours in a four-set.  Hence they induce the path

\[
                         a-b-c.
\]

Put `W=V(H)-{a,b,c}`.  The ends `a,c` are complete to `W`, and the middle
vertex `b` has either three or four neighbours in `W`.

If `b` is complete to `W`, then `W` is independent: an edge of `W`
together with `a,b` would form a `K_4`.  The graph therefore has fourteen
edges, while every member of `W` has degree three; deleting any such vertex
leaves eleven edges, contrary to the six-vertex bound.

Otherwise let `w_0` be the unique member of `W` missed by `b`, and put
`B=W-{w_0}`.  The set `B` is independent, for the same `K_4` reason.  Every
edge in `H[W]` is consequently incident with `w_0`.  If

\[
t=d_{H[W]}(w_0),
\]

then

\[
|E(H)|=13+t.
\]

For `t=0`, the vertex `w_0` has degree two and its deletion leaves eleven
edges.  For `t=1,2`, choose a member of `B` not adjacent to `w_0`; it has
degree three and its deletion leaves at least eleven edges.  For `t=3`,
every member of `B` has degree four and deleting one leaves twelve edges.
All cases contradict `|E(H-s)|<=10`.  Thus at most two vertices have degree
at least five.

For `q>=2`, every root of boundary degree at most five is safe; for `q=1`,
every root of degree at most four is safe.  The preceding conclusion gives
at least five safe roots in all cases.  `\square`

## 2. Leaf-root blockers

Choose a spanning tree of `G[D]`, and inside it the minimal subtree `R`
containing all roots `D cap N`.  Every leaf of `R` is a root.  For a leaf
root `r`, delete the first tree edge on its route into `R` and let `C_r` be
the leaf-side tree component.  Then

\[
C_r cap N=\{r\},
\qquad D-C_r\text{ is connected},                     \tag{2.1}
\]

and the sets `C_r` for distinct leaf roots are disjoint.

Call a leaf root **open** when `C_r` is adjacent to every uncontacted
foreign bag.  Otherwise it is **blocked**.

### Lemma 2.1

At most one leaf root is open.

### Proof

If distinct leaf roots `r,s` were both open, use the connected split

\[
D=C_r\mathbin{\dot\cup}(D-C_r).
\]

The second side contains `C_s`.  Hence every uncontacted foreign bag meets
both sides.  The completion-after-a-connected-split lemma from the promoted
labelled-shore theorem then gives a `K_7^-` model.  `\square`

### Theorem 2.2 (safe blocked leaf or low branching)

At least one of the following holds.

1. A safe leaf root `r` is blocked.  Its one-root component `C_r` is a
   strict labelled separator shore carrying the density-safe endpoint
   edge `xr`.
2. The minimal root subtree `R` has at most three leaves.  At most one leaf
   is safe, and every other leaf is one of the at most two unsafe roots of
   `H`.

In the three-leaf residue there is exactly one safe open leaf and two
unsafe blocked leaves.  In the two-leaf residue all safe roots of `D`
except possibly one lie internally on the root subtree.

### Proof

Assume outcome 1 fails.  Every safe leaf is then open, so Lemma 2.1 gives
at most one safe leaf.  Lemma 1.1 gives at most two unsafe roots in all of
`N`, and every other leaf is unsafe.  Therefore `R` has at most three
leaves and the stated refinements follow.  `\square`

### Corollary 2.3 (surplus at least three always has a safe blocked leaf)

If `q>=3`, outcome 1 of Theorem 2.2 always holds.

### Proof

Every root is safe because `d_H(s)<=6<=q+3`.  The root subtree has at least
two leaves, while Lemma 2.1 permits at most one open leaf.  Hence some leaf
is both safe and blocked.  `\square`

## 3. Scope

Outcome 1 links the static branch-set split directly to one of the at
least five density-safe edges at `x`; it is the preferred entrance to the
eligible-shore recursion and exact-cut family.

Outcome 2 is the exact model-theoretic singleton residue.  The multiply
rooted carrier is no longer arbitrary: after suppressing nonroot corridors,
its root skeleton is a path or a three-arm tree, with the two exceptional
unsafe roots occupying all but possibly one leaf.  Static support masks do
not orient the resulting path/three-arm rotations.  Closing this residue
requires the failed contractions of the internal safe roots, or a literal
model reroute using the named uncontacted bags.