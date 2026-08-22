# Dense seven-vertex boundaries close the double cone

## Stronger structural lemma

Every seven-vertex graph `S` with minimum degree at least four either has a
`K_5` minor or is the pentagonal bipyramid.

Indeed, degree counting first gives `kappa(S)>=3`.  If a set `X` of order at
most two separated two components, then every such component `D` would have

`|D|-1+|X| >= 4`,

so `|D|>=5-|X|`; two components do not fit among the `7-|X|` remaining
vertices.

If `kappa(S)=3`, let `T={t_1,t_2,t_3}` be a three-cut.  The four remaining
vertices must form exactly two components

`A={a_1,a_2}` and `B={b_1,b_2}`.

The same degree bound forces each component to be an edge and every member
of `A union B` to be adjacent to all of `T`.  Then

`{a_1,t_1}, {a_2,t_2}, {b_1}, {b_2}, {t_3}`

are five disjoint connected pairwise adjacent branch sets.  Thus `S` has a
`K_5` minor.  In the remaining case `S` is four-connected.  If it has no
`K_5` minor, the planar analysis in the proof below identifies it as the
pentagonal bipyramid.  This proves the lemma.

## Theorem

Let `S` be a four-connected graph on seven vertices.  Add two new
nonadjacent vertices `x,y`, each adjacent to every vertex of `S`.  The
resulting graph contains a `K_7^-` minor.

## Proof

If `S` has a `K_5` minor, take its five branch sets together with the
singletons `{x},{y}`.  Their sole possible missing contact is `xy`.

Suppose, then, that `S` has no `K_5` minor.  We use the standard consequence
of Wagner's structure theorem that every four-connected nonplanar graph has
a `K_5` minor.  Hence `S` is planar.  Four-connectivity gives minimum degree
at least four, while Euler's formula gives

`14 <= |E(S)| <= 15`.

First assume `|E(S)|=15`.  A planar embedding is a triangulation.  Every
triangle is facial, since a nonfacial triangle would be a vertex cut of
order three.  The degree sum is 30, so the degree sequence is either

`(6,4,4,4,4,4,4)` or `(5,5,4,4,4,4,4)`.

The first sequence is impossible.  Around the degree-six vertex its six
neighbours occur on a cycle.  The graph has nine edges among those six
vertices, hence three chords of that cycle.  Each chord and the degree-six
vertex form a nonfacial, separating triangle.

In the second sequence, let `p,q` be the degree-five vertices.  They cannot
be adjacent: if they were, each would have four neighbours among the other
five vertices, and hence they would have at least three common neighbours.
But the edge `pq` in a four-connected plane triangulation has only its two
facial common neighbours.  Thus `p,q` are nonadjacent.  Each is consequently
adjacent to all other five vertices.  Those five vertices each have two
remaining neighbours, and so they induce a five-cycle.  Therefore `S` is
the pentagonal bipyramid: two nonadjacent apices complete to a `C_5`.

There is no fourteen-edge case.  Such a graph would be four-regular.  Its
plane embedding has exactly one quadrilateral face and all other faces
triangular.  At least one diagonal of that quadrilateral is absent; add it
inside the face.  The resulting graph is still planar and four-connected,
has fifteen edges, and has degree sequence `(5,5,4,4,4,4,4)`.  The preceding
paragraph says its two degree-five vertices are nonadjacent, but they are
the endpoints of the newly added diagonal, a contradiction.

It remains to close the pentagonal bipyramid.  Name its cycle
`c_0 c_1 c_2 c_3 c_4 c_0` and its two old apices `p,q`.  In the double cone
use the seven branch sets

`{c_0,p}, {c_1,x}, {c_2}, {c_3}, {c_4}, {q}, {y}`.

They are nonempty, disjoint and connected.  Every pair is adjacent except
possibly `{c_2},{c_4}`.  They form a `K_7^-` minor.  QED

## Consequence for an exact seven-cut

In a seven-connected graph, every component behind an exact seven-cut `S`
has neighbourhood all of `S`.  Contracting any two such components and
deleting the others produces the double cone over `G[S]`.  Therefore, in a
`K_7^-`-minor-free seven-connected graph, every exact seven-cut satisfies

`delta(G[S]) <= 3`,

and hence also `kappa(G[S])<=3`.

The exact atlas census and the independently checked positive witnesses
retained beside this file provide a separate finite audit of the theorem.

The structural lemma also proves the stronger standalone statement that
the double cone closes whenever `delta(S)>=4`, even without assuming that
`S` is four-connected: use the `K_5` model together with `{x},{y}`, or use
the displayed pentagonal-bipyramid model.  The atlas census contains 29 such
graphs and independently finds all 29 positive.
