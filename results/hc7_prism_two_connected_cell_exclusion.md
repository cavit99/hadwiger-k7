# Clean prism webs with a two-connected remainder

**Status:** written proof, with a [separate internal audit](hc7_prism_two_connected_cell_exclusion_audit.md).
This is a structural argument with no chromatic-number premise, under
the stated prism and clean-web inputs. It is an input to the
[whole two-triangle case closure](hc7_two_triangle_case_closure.md).
No closure of HC7 is asserted.

## Statement and inputs

Let `J` have the partition `V(J)=E disjoint union S`, where `S` induces
a prism subdivision with literal end triangles
`P={p_1,p_2,p_3}`, `Q={q_1,q_2,q_3}` and three disjoint rails
`R_i=p_i...q_i`, each with nonempty interior. Put `T=P union Q`.
Assume:

1. `J[E]` is two-connected.
2. Every nonempty subset of `V(J)-T` has at least six actual neighbours.
3. Each root has at least two actual E-neighbours, and each rail-interior
   vertex has at least four actual E-neighbours.
4. `J` has no T-meeting K5 model.
5. Each of the three fixed ordered web completions of
   `H_i=J-V(R_i)` has every whole cell interior contained in `E`.

The web descriptions and the following cross-view statement are the
inputs proved in the [path-cell theorem](hc7_two_triangle_web_path_cells.md):

- Each web has a planar skeleton. Each whole cell attaches only to the
  three vertices of one triangular inner face. Different cell interiors
  in one view are disjoint and have no edges between them. Actual cell
  boundaries are subsets of their facial triples.
- If nonempty `U,V subseteq E` have
  `|N_{H_i}(U)|<=3` and `|N_{H_j}(V)|<=3`, with `i!=j`, then
  `U intersection V` is empty. This applies to arbitrary such shores,
  including disconnected whole cells.

Both rails surviving in a view lie in its skeleton under input 5.
The cycle consisting of its two rails and their two cap edges is an
actual cycle. A rooted K4 on the four surviving cap vertices would,
with the deleted rail as fifth bag, contradict input 4.

**Theorem.** These five assumptions are inconsistent. In fact every
actual cell component in every view is empty. The three actual graphs
`H_i` are consequently planar, and their disk edge bounds contradict
the actual degree and rail-contact bounds.

Throughout, projections inside facial triangles are auxiliary planar
objects only. No completion edge is used as an actual minor edge.

## 1. A connected one-rail shore with connected complement is impossible

**Pocket lemma.** Suppose `W` is a nonempty connected proper subset of
`E`, its complement `A=E-W` is connected, and

    B=N_E(W),  |B|<=3,  N_S(W) subseteq V(R_i).

Then there is a nonempty root-free set with at most five actual
J-neighbours, contrary to input 2.

### Visibility and projection of the complement

The boundary of W in `H_i` is exactly B. Cross-view disjointness with
each whole cell of either alternate view shows that W lies wholly in
both alternate planar skeletons. Fix one, say `H_j`, retaining rails
`R_i,R_k`.

The set A has a visible skeleton vertex. Otherwise, since A is
connected and there are no edges between different cell interiors, A
lies in one whole cell D. This D is disjoint from W, so D=A. Every
vertex of R_k has an E-neighbour, and all these neighbours lie in A,
because W has no R_k contact. Hence all vertices of R_k are gates of
D. There are at least three such vertices. Connectivity of E also
gives an edge from A to W, requiring an additional gate in W. This
exceeds the three available gates.

For each whole cell D, consider a connected component L of the actual
induced graph `J[A intersection D]`. It has at least one A-gate of D:
otherwise L would be a component of connected A entirely inside D,
although A has a visible vertex. Let `Q_L` be its nonempty set of
actual neighbouring A-gates. Replace passages through L by edges of
D's facial triangle joining the relevant members of Q_L. Retain all
visible vertices of A and all actual edges between them. This gives a
nonempty connected plane graph `A*` with vertices only in A, disjoint
from W and the rails. Connectedness follows by projecting each actual
A-path and replacing each maximal cell passage by an edge or a
constant walk between its A-gates.

In addition, preserve every actual contact of A with either retained
rail. If a rail vertex v has a visible A-neighbour, keep that edge.
If it has a neighbour in a component L inside D, then v is a D-gate;
join v to any member of Q_L along an edge of the facial triangle.
These contact edges have one endpoint in A* and the other on the same
rail vertex v. They use no W vertex. All the projected edges are
skeleton edges, so they can be retained simultaneously in its drawing.

This projection need not preserve hidden vertices of B or the W--A
edges. Neither is needed: A* is used only as a connected witness for
the positions of the actual A--rail contacts.

### A common side of the actual cycle

Separately project all of connected E into this skeleton, using only
E-gates of each cell component. W is visible and nonempty, so E has a
visible vertex. Each actual component inside a cell has an E-gate by
connectivity. Retain all visible E vertices and actual edges between
them, and all facial edges needed for these projections, including
those already used in A*. The resulting plane graph `E*` is connected,
is disjoint from the actual cycle

    Z=R_i union R_k union {p_i p_k,q_i q_k},

and contains both the actual graph on W and the E-only graph A*.
Thus W and A* lie on the same side of Z. Regard that side as a closed
disk. Every retained contact edge from W or A* to Z also lies on this
side: its interior cannot cross Z. This E* is only a side witness;
no disjointness of E* from W or A* is asserted or required.

### The actual small boundary

Input 2 applied to W implies at least `6-|B|>=3` distinct R_i
contacts. Let a,b be their first and last vertices in the order from
p_i. Connectedness of W gives a simple actual a--b arc with all
internal vertices in W. It lies in the disk just specified. Together
with the subpath `R_i[a,b]`, it bounds the pocket adjacent to that
boundary subpath. The pocket contains no vertex of R_k.

A* is connected and disjoint from this arc and from the cycle. It
has a contact with R_k, so it lies outside the pocket. An edge from
A* to a vertex of the open interval `R_i(a,b)` would have to approach
that vertex from the pocket side of the boundary. This is impossible
in the plane drawing. Since the projection preserved every actual
A--R_i contact at its original rail vertex, A has no actual neighbour
in `R_i(a,b)`.

Now put `X=W union V(R_i(a,b))`. This set is nonempty and root-free.
The prism is induced, W has no contacts with the other rails, and the
open interval has no A-neighbour. Therefore

    N_J(X) subseteq B union {a,b},  |N_J(X)|<=5.

This proves the pocket lemma.

## 2. The diagonal obstruction with one surviving-rail contact

The following elementary construction uses actual edges only. Let
W,A be disjoint connected subsets of E. Suppose W contacts two
vertices a,b on R_i with a preceding b, and contacts t on R_j.
Suppose A contacts a vertex v strictly between a,b on R_i, and a
vertex d of R_j different from t.

If d precedes t, there are vertex-disjoint paths

    p_i R_i a -- W -- t R_j q_j,
    p_j R_j d -- A -- v R_i q_i.

If d follows t, there are vertex-disjoint paths

    p_i R_i v -- A -- d R_j q_j,
    p_j R_j t -- W -- b R_i q_i.

Each path through a connected E-set can be chosen simple. The two
paths are disjoint because their E-parts are disjoint and their used
rail intervals are disjoint. They join the opposite cap-root pairs
on the actual cycle formed by R_i,R_j and their cap edges.
Fabila-Monroy--Wood,
[Lemma 7](https://arxiv.org/html/1102.3760v1), therefore supplies a K4
minor rooted at those four cap vertices. Its hypothesis is a cycle
in the specified root order and this disjoint opposite-pair linkage;
no connectivity assumption on the path-deleted graph is needed.
The unused rail R_k is a fifth connected bag adjacent to all four root
bags. This is a T-meeting K5, contrary to input 4.

Consequently, whenever A has an R_j contact different from t, A cannot
contact the open R_i interval between two W contacts.

## 3. Exhaust all actual cell components under two-connectivity

Fix a view H_i and a nonempty actual connected component C of one
whole cell. Its boundary lies in the facial triple. Write

    B=N_E(C),  L=N_{S-V(R_i)}(C),  h=|E-C|.

Thus `|B|+|L|<=3`. We first establish the exact possibilities.

If `h<=1`, every one of the four surviving roots has a C-neighbour,
because each has at least two E-neighbours. Then `|L|>=4`, impossible.
Hence `h>=2`. If `|B|<=1`, there is a vertex of E-C beyond B, and
removing B separates it from nonempty C, contrary to two-connectivity.
Therefore `|B|>=2` and `|L|<=1`. Choose the surviving rail not
containing the possible vertex of L. An interior vertex of that rail
has at least four E-neighbours, all outside C. Hence `h>=4`.

Every component of E-C meets B, by connectivity of E. If such a
component K contains exactly one B vertex b, then K={b}: otherwise
removing b separates `K-{b}` from C, making b an E-cutvertex.

### Two E gates

Suppose `B={x,y}`. If E-C were disconnected, its two components would
each contain one gate and so be the two gate singletons, contradicting
`h>=4`. Hence `A=E-C` is connected.

If L is empty, C satisfies the pocket lemma and is impossible.
Otherwise `L={t}`, say on surviving rail R_j. The six-neighbour
condition gives at least three distinct C contacts on R_i. Let a,b
be their extremes. Every vertex d of R_j other than t has an
A-neighbour, since it has an E-neighbour and no C-neighbour. Choose
one such d. Section 2, with W=C, shows that A has no neighbour in
`R_i(a,b)`. The nonempty root-free set

    X=C union V(R_i(a,b))

then has actual boundary contained in `{x,y,t,a,b}`, a contradiction.

### Three E gates, connected complement

Suppose `|B|=3`. Then L is empty. If E-C is connected, C satisfies
the pocket lemma and is impossible.

### Three E gates, disconnected complement

If E-C is disconnected, the component classification above and
`h>=4` give exactly

    E-C=A disjoint union {z},  B={x,y,z},

where A is connected and contains x,y, while `N_E(z) subseteq C`.
Indeed any single-gate component must be that gate singleton; three
singleton components would give h=3. The only other gate distribution
among at least two components is two plus one.

The set `W=C union {z}` is connected, because z is a gate of C.
Its complement A is connected and `N_E(W) subseteq {x,y}`.
If z has no contact with a surviving rail, W is a one-rail shore,
so the pocket lemma again gives a contradiction.

Otherwise z contacts a vertex t of a surviving rail R_j. Every
vertex of R_j has an A-neighbour: C has no contacts on this rail,
z is the only E vertex outside C and A, and even a root has at least
two E-neighbours. Choose any vertex d of R_j different from t.
The six-neighbour condition gives at least three C contacts on R_i;
let a,b be their extremes. Apply Section 2 to the connected disjoint
sets W and A. It follows that A has no R_i contact strictly between
a,b. Consequently

    X=C union V(R_i(a,b)),
    N_J(X) subseteq {x,y,z,a,b}.

Again X is nonempty and root-free with at most five actual neighbours.
All possible contacts of z with R_i are already accounted for by the
boundary vertex z. No locality or Dirac inequality is needed.

This exhausts every actual connected component C. Thus every whole
cell in all three views is empty. In particular each actual H_i is a
subgraph of its planar skeleton and is planar. No insertion of a
three-gate cell, and no assumption that its gates are cofacial, occurs.

## 4. The simultaneous disk edge count

Put `e=|E|`, `r_i=|R_i|`, `s=r_1+r_2+r_3`,
`a=|E(J[E])|`, `d_i=|E_J(E,R_i)|`, and `d=d_1+d_2+d_3`.
In planar H_i, its two-rail cycle has the connected set E on just one
side. Since S is induced, the other side has no graph edges or
vertices. Take it as the outside face. The disk edge inequality gives

    a+d_j+d_k <= 3e+r_j+r_k-3.

Summing over the three views gives

    3a+2d <= 9e+2s-9.

Input 2 applied to each singleton in E gives `2a+d>=6e`.
The root and rail-interior contact bounds give

    d>=2*6+4*(s-6)=4s-12.

It follows that

    3a+2d = (3/2)(2a+d)+(1/2)d >= 9e+2s-6,

a contradiction. This proves the structural theorem without a
chromatic-number assumption or any transferred criticality.
