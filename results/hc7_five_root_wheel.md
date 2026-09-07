# A rooted wheel from a prescribed triangle

**Status:** written proof; the adjacent audit records its separate internal
verdict at the exact source hash. Conjecture 19 and HC7 remain open.
All graphs are finite and simple. A wheel `W_4` has a four-cycle and a
fifth vertex adjacent to its four vertices.

**Theorem 1.** Let `S={b,c,r,s,t}` be five distinct vertices of a graph
`F`, with `rst` a triangle and `B=V(F)-S` nonempty. Suppose

- every nonempty `X subseteq B` has `|N_F(X)|>=5`; and
- every vertex of `B` has degree at least six in `F`.

Then `F` has an `S`-rooted `W_4` minor whose centre is one of `r,s,t`.
More explicitly, there are five disjoint connected rooted bags such that
the three triangle bags are pairwise adjacent, the `b,c` bags are adjacent,
and each of the latter contacts at least two triangle bags, with their
combined contacts covering all three. No edge `bc` is assumed.

Here `N_F(X)` is the neighbourhood outside `X`. The first hypothesis is
exactly internal five-connectivity relative to `S`: a prohibited separation
with all roots on one side has a nonempty root-free other side with at
most four external neighbours, and conversely.

## 1. An elementary ordering fact

**Lemma 2.** If `J+bc` is two-connected, there is an ordering of `V(J)`
beginning at `b` and ending at `c` such that every nonempty proper prefix
and suffix induces a connected subgraph of `J`.

**Proof.** Write `H=J+bc`. Start with a cycle of `H` containing `bc`,
and order the vertices along its other `b`-to-`c` path. While vertices
remain outside the current subgraph, an outside component has two
distinct neighbours in it, by two-connectivity. Add a path between these
neighbours whose internal vertices are in that component. If its ends
occur as `u` before `w` in the current order, insert its internal vertices
in path order immediately after `u`.

Every vertex other than `b` has an earlier neighbour, and every vertex
other than `c` has a later neighbour. These properties are preserved by
each insertion and imply connected prefixes and suffixes. The number of
ordered vertices strictly increases until all vertices are ordered. No
proper prefix or suffix contains both `b,c`, so its connectivity never
uses the possibly added edge `bc`. QED

## 2. The root-preserving reduction

**Proof of Theorem 1.** Put `R={r,s,t}` and `J=F-R`.
If a triangle root `p` has at most one neighbour in `J`, it has exactly
one, say `q`, and `q` is a nonroot. Indeed the boundary condition applied
to all of `B` implies that every root has a neighbour in `B`.

Contract `pq`, keeping the label `p`. All five prescribed roots remain
distinct and the triangle remains literal in the quotient. For every
nonempty `X subseteq B-{q}`, the old vertex `p` was not in `N_F(X)`:
its only nonroot neighbour was `q`. The new neighbourhood of `X` is
therefore exactly the old one with `q` relabelled as the new `p`, if
present. Its cardinality is unchanged. Thus internal five-connectivity
is preserved.

Every remaining nonroot degree is also unchanged: no remaining nonroot
was adjacent to both `p,q`. The new nonroot set has one fewer vertex.
It cannot become empty or a singleton: with five roots a sole nonroot
has degree at most five, contrary to the invariant degree bound. Repeat
until each triangle root has at least two neighbours in `J`.

In the resulting graph, `J+bc` is two-connected. Otherwise, after deleting
at most one vertex `z`, some component avoids the surviving vertices of
`{b,c}`, which are joined by `bc` when neither is deleted. That component
is a nonempty subset of `B` whose external neighbourhood in `F` lies in
`R union {z}`, of order at most four. This contradicts the boundary
condition. The same argument with no deletion proves connectivity.
There are at least four vertices in `J`.

Use Lemma 2. Let `P` be the first prefix which contacts at least two
vertices of `R`. Its complementary suffix `Q` is nonempty: if that first
prefix ended at `c`, two triangle roots would have no neighbour except
`c` in `J`. Suppose that `Q` contacts at most one triangle root. At least
two triangle roots then have every `J` neighbour in `P`. The prefix
before its last vertex contacted at most one triangle root. Consequently
one of those two roots has its sole `J` neighbour at that last vertex,
contrary to the termination condition.

Thus both `P,Q` contact at least two triangle roots. Their union is `J`,
so their combined contacts cover `R`. They are connected, contain `b,c`
respectively, and have an edge between them: `J` is connected, since
deleting the edge `bc` from a two-connected graph leaves it connected.
Together with the singleton triangle roots, they give the asserted model.
Choose a triangle root contacted by both parts as the wheel centre;
the other two triangle roots can be assigned to different parts which
contact them. Their literal edge, the part-part edge and these two
contacts give the rim cycle.

Finally lift through the contractions in reverse order. The fixed preimage
of each merged root is connected, contains its original prescribed root,
and is disjoint from every other preimage. Expanding a model bag through
these preimages preserves every required contact and all five roots.
The decreasing parameter throughout the reduction is `|B|`. QED

## 3. Application across an actual seven-vertex cut

Put `Q_7=K_7^=`, where the two deleted edges are independent.

**Corollary 3.** Let `G` be seven-connected, with minimum degree at least
eight and no `Q_7` minor. Let `R_0` be a literal four-clique and `v in R_0`.
No three-vertex cut `T` of `G-R_0` contains two neighbours of `v`.

**Proof.** Suppose `b,c` are such neighbours in `T`, put `T={a,b,c}`
and `R_0={v,r,s,t}`, and choose distinct components `B,D` of
`G-(R_0 union T)`. Each component is adjacent to every vertex of the
seven-set `R_0 union T`, since a missing contact would give an actual
cut of at most six vertices.

Let `F=G[B union {b,c,r,s,t}]`, with these five vertices as its roots.
Every nonroot loses at most the two neighbours `v,a`, so has degree at
least six. For nonempty `X subseteq B`, a neighbourhood of order at most
four in `F`, together with `v,a`, would separate `X` from `D` in `G`
using at most six actual vertices. Thus Theorem 1 applies.

Its five rooted wheel bags are disjoint from `{v}` and `D`. Both extra
bags contact all five through their prescribed roots, and they contact
each other. The resulting minor is `K_2 join W_4=Q_7`. This contradicts
the exclusion. No boundary edge or foreign branch-set vertex is reused.
QED

**Corollary 4.** Under Corollary 3, if the neighbours of `v` outside `R_0`
span a two-connected subgraph, then `G-R_0` is four-connected. In
particular this holds in the degree-eight five-cycle-and-triangle case.

**Proof.** The graph `G-R_0` is three-connected. If it had a three-cut
`T`, each component after deletion would contain a neighbour of `v`,
by fullness of the corresponding seven-cut. If `T` met that neighbour
set in at most one vertex, its spanning two-connected subgraph would
keep all remaining neighbours in one component. Thus `T` contains at
least two neighbours of `v`, contradicting Corollary 3. QED

These constructions settle that separator case. They do not provide the
remaining compatible helper in a four-connected exterior, a global
density induction, or a proof of Conjecture 19, Conjecture 21 or HC7.
