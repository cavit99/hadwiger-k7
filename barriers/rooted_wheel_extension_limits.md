# Limits of proposed rooted wheel extensions

**Status:** written counterexamples; the adjacent internal audit records
its verdict and exact source hash. All graphs are finite and simple.
None refutes the audited five-root wheel theorem or HC7.

## 1. Two triangles in a four-connected planar graph

**False assertion:** two disjoint triangles in every four-connected planar
graph root an octahedron, with each root retaining its own bag.

Let C be the cube, choose vertices a,b at distance two, and put H=L(C).
Take as A,B the triples of edge-vertices incident with a,b. The
cuboctahedral embedding is planar. Deleting at most three cube edges
cannot produce two components containing edges: a smaller such component
has s=2,3,4 vertices, with edge boundary at least 4,5,4 respectively,
by cubic degree and bipartiteness. Thus H is four-connected; its degree
four gives the matching upper bound.

Choose a common neighbour c of a,b, and let w be c's third neighbour.
The adjacent roots ac,bc share their sole nonroot neighbour cw.
Every rooted octahedron bag needs at least four contacts, hence at least
two opposite-triangle contacts. If either root bag expands, it must
contain cw, leaving the other singleton with only one opposite-triangle
contact. If both stay singleton, ac needs cw in another B bag and bc
needs it in another A bag. These requirements are incompatible.

The first false step was asserting this planar rooted model before
augmenting it through a nonplanar attachment. The proposed five-connected
nonplanar two-triangle theorem remains unproved and is not refuted here.

## 2. A wheel and two disjoint missing-diagonal paths

**False assertion:** in a four-connected nonplanar graph, a five-root
wheel and disjoint paths for its two missing rim diagonals give a rooted
K5, provided neither path contains a foreign root internally.

Take the pentagonal prism P with cycles r0,...,r4 and s0,...,s4 and
edges ri-si, with subscripts modulo five. Add a universal vertex h.
The prism is three-connected, so the host is four-connected. A planar
drawing of the cone would make all prism vertices cofacial, impossible
since every outerplanar graph has a vertex of degree at most two.
The prescribed roots are r0,...,r4.

There is no rooted K5. If h is unused, planarity of P excludes one.
If h belongs to one bag, the other four would give a rooted K4 in P at
four vertices of its outer face. Deletion and contraction preserving
these distinct roots retain their cofaciality, which excludes K4.

Nevertheless, the bags

    {r0,h}, {r1,s1,s0,s4}, {r2}, {r3}, {r4}

give a wheel with hub r0 and rim r1,r2,r3,r4. Its missing-diagonal paths

    r1-h-r3,    r2-s2-s3-s4-r4

are disjoint and have no foreign root internally. The first path uses
the existing hub bag; assigning it to a rim bag is not a valid lift.
The full scheme intersection constraints remain available and are not
satisfied merely by these two paths. This is not a K5-scheme counterexample.

## 3. The hub cannot always own its entire colour class

**False assertion:** every strongly normalised coloured W4 scheme has a
labelled rooted model whose hub bag contains every hub-coloured vertex.

Let W4 have hub h and rim a,b,c,d. Add one clone of each root, named
u,A,B,C,D respectively. For each target edge ij use the path
`i-clone(j)-clone(i)-j`; take exactly their union. Each nonroot lies on
at least three demands, so this is a strongly normalised coloured scheme.

A connected hub bag containing h,u must contain a rim clone, say A by
rotation. The only available nonroot neighbour of either b or d is then C.
Each must absorb C: a singleton could contact at most one rim bag, whereas
its required rim degree is two. Disjointness makes this impossible.

Nevertheless `{h}, {a,B}, {b,C}, {c,D}, {d,A}` is a correctly labelled
rooted W4 model. The first unsupported step is prescribing the entire
hub colour class before allocating the rim. A successful construction
must permit its vertices to be omitted or assigned elsewhere; neither
arbitrary hub expansion nor W4 contractibility is refuted.

## 4. Six-connectivity does not reserve a connected complementary triple

**False assertion:** if F is six-connected, T is an independent triple,
and F-T has a wheel rooted at a disjoint five-set R, some such wheel
leaves T in one connected component of its complement. This fails even
when F-T has an R-rooted K5 subdivision.

Let P be the hexagonal antiprism with cycles a0,...,a5 and b0,...,b5,
and edges a_i b_i, a_i b_{i-1}, with indices modulo six, augmented by
the inner-face diagonals b1b5, b2b4, b2b5. Its outer face remains the
a-cycle. The underlying antiprism is C12 squared in interleaved order.
Deleting at most three vertices leaves it connected: two separating gaps
in that cyclic order would each require two consecutive deletions.
Put F=K2 join P, with apex vertices h1,h2. It is six-connected, since a
surviving apex connects everything and deleting both leaves at most three
further deletions from P. Set R={h1,h2,a0,a2,a4} and T={a1,a3,a5}.
The triple T is independent. The seven edges of F[R] and the disjoint paths

    a0-b0-b1-a2,    a2-b2-b3-a4,    a4-b4-b5-a0

give the claimed rooted K5 subdivision in F-T.

The counterexample also retains a five-chromatic core K=F-T in which R
is rainbow in every five-colouring, and chi(K+T)=chi(F)=6. Indeed the
inner triangulation has faces b0b1b5, b1b2b5, b2b4b5, b2b3b4. Every
three-colouring has, up to permutation, the b-colours (2,0,2,1,0,1),
forcing colours (0,1,2) on a0,a2,a4 in P-T. Hence P-T is three-chromatic
with these roots universally rainbow; the two joined apices give the
claimed property of K. A three-colouring of P would also force a1 to
have colour 1, equal to adjacent a2. Thus chi(P)=4: a fourth colour on
the independent T extends the displayed colouring of P-T.

Suppose a rooted R-wheel and a disjoint connected T-containing set existed.
Remove the two bags rooted at h1,h2. W4 remains connected after deleting
any two vertices, so the union of the other three bags is a connected
subset of P containing a0,a2,a4. The T-containing set also lies in P.
These disjoint connected sets would join alternating triples on one face,
contradicting the planar separation of alternating cofacial terminals.
Thus no choice of the rooted wheel leaves the required complementary set.

This is not an actual critical-host counterexample. Here delta(F)=6,
and F already contains Q: use h1,h2 and the wheel with hub
{b0,...,b5} and rim bags {a0,a1},{a2,a3},{a4},{a5}. Adding a vertex v with
neighbourhood R union T would give N(v)=K2 join C6, which contains a
four-cycle and violates the actual C19 neighbourhood restrictions.
