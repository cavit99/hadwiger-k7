# Global colouring lifts in the split-clique case

**Status, 7 October 2026:** working deductions, not separately audited.
Neither the exterior six-cut branch nor the whole split-clique case is
closed. The constructions below restore whole-host colourings or give
explicit minors under additional hypotheses. No induction is asserted.

Throughout, G is finite and simple, seven-connected, seven-chromatic and
K7-minor-free, and every proper minor is six-colourable. The neighbourhood
of u is an anticomplete triangle P and four-clique D. Put H=G-u and
C=G-N[u]. The goal is a K7 model or a six-colouring of G, with no bound
on its order. The [technical frontier](hc7_c21_rooted_density_construction.md#next-attack-the-split-clique-neighbourhood)
records the other constructions and barriers.

## The complete boundary-colouring condition

Every six-colouring of H uses exactly six colours on P union D. Thus its
only repeated boundary colour is one P--D pair. Conversely, each of the
twelve pairs occurs: contract the connected set {u,p,d}, six-colour the
proper minor, and give p,d the contracted colour in H. The pullback is
proper because p,d are nonadjacent and every other H-edge survives.

More generally, every proper minor of H obtained while retaining distinct
roots P union D and the two literal clique subgraphs admits a colouring
using at most five colours on those roots. Adjoining u produces a proper
minor of G; its colouring omits u's colour on the roots. This does not
provide a lift through the contracted branch sets. The finite set of
boundary partitions places no bound on the size of the exterior.

## Contracting an independent anti-neighbourhood

Fix v in P, put A=P-{v}={a,b}, I=C-N(v), and suppose I is independent.
Write W=V(G)-({u,v} union I). This section gives terminal constructions
for this conditional case; it does not establish that I is independent
for some choice of v.

First, `chi(G-{u,v})=6`. Otherwise five-colour that graph and choose a
colour t absent from A. Give v colour six; if t occurs at a D vertex,
give that unique vertex colour six too. These two vertices are nonadjacent.
Now u can receive t. The same argument proves the deletion statement
for every v in P union D, with the two cliques interchanged when needed.

Each vertex i of I has a neighbour in C-I: it misses u,v and has at
most six neighbours in A union D, whereas its degree is at least seven.
For each i choose a parent f(i) in W adjacent to it, and contract all
edges i f(i). Their fibres are disjoint stars, each containing just one
W vertex. Let Q_f be the resulting minor of G-{u,v}. Contracting uv as
well gives a proper minor of G whose contracted vertex is universal to
Q_f: u sees the retained roots and v sees C-I. Hence Q_f is five-colourable.
All six roots A union D remain distinct, with their literal clique edges.
The operation removes |I|+1 vertices from G. No quotient inherits
contraction-criticality, and no recursion is used.

**Exact response.** Every five-colouring of every Q_f uses all five
colours on A union D. Otherwise retain its colours on W, colour I union
{v} with six, and give u a colour absent from the six retained roots.
Consequently there is exactly one repeated A--D pair: one A colour lies
outside the four D colours, and the other equals one D colour. The
quantifiers are important: the colouring may depend on the parent map.

**Two disjoint neighbourhoods give a colouring lift.** Suppose distinct
d,e in D satisfy `(N(d) intersect I) intersect (N(e) intersect I)=empty`.
Choose parents d for all I-neighbours of d and e for all I-neighbours
of e; choose other parents arbitrarily. In a five-colouring of Q_f, at
least one of d,e has a colour t absent from A. Call that root d. Restore
the original graph as follows:

- retain the colours on W-{d};
- colour I intersect N(d) with t;
- colour d, v and I-N(d) with six;
- colour u with t.

The three parts of the colour-six class are pairwise anticomplete.
Every W-neighbour other than d of an I vertex assigned t avoids t,
because its edge to the contracted d-fibre survives in Q_f. The other
D roots and both A roots avoid t, so all edges at u are proper. This
is a six-colouring of G. Thus the four sets N(d) intersect I, d in D,
must be pairwise intersecting in any remaining instance. Empty sets
are included in this conclusion.

The following minor construction uses the complementary neighbours.
For every d in D,

`|N(d) intersect (C-I)| >= 2`.

Indeed, write its numbers of I and C-I neighbours as k,l. The k
I-neighbours together with u form an independent subset of N(d), while
`d_G(d)=4+k+l`. The contraction-critical inequality
`alpha(G[N(d)]) <= d_G(d)-5` gives `k+1 <= k+l-1`.
For completeness, that inequality follows by contracting the star on a
vertex s and an independent subset J of N(s), six-colouring the proper
minor, then restoring J in the contracted colour. If `d(s)-|J|<=4`,
at most five colours appear on N(s), allowing s to be restored too.

**A connected cover with at most one C-I vertex gives a minor.** Suppose
L is connected, contains a, meets every D-neighbourhood, and is contained
in `{a} union I union {w}` for some w in C-I (w need not belong to L).
Let R be all vertices outside `{u} union D union L`. Its base consists
of v,b and the remaining C-I vertices, and is connected through v.
Every remaining I vertex has a neighbour in that base: otherwise its
neighbours lie in `{a,w} union D`, at most six vertices. Each d retains
a C-I neighbour in R by the preceding bound. Thus

`{u}, {d} (d in D), L, R`

are seven disjoint connected bags with every required contact. The L--R
edge is ab. In particular, this closes the case in which the I-neighbours
of either a or b collectively contact all four D vertices.

**An I vertex complete to D also gives a minor.** Let x in I see all
of D. If x sees a or b, use the preceding construction. Otherwise put
`F=G-(D union {u,v,x})`. The graph G-D is three-connected. Deleting v
leaves a two-connected graph in which u has exactly the adjacent
neighbours a,b; deleting that simplicial vertex preserves
two-connectivity. Thus F+x is two-connected and F is connected.
Some neighbour z of x is not a cutvertex of F: an end block of F must
have an x-neighbour away from its cutvertex, or that cutvertex would
separate F+x. If F has no cutvertex, any x-neighbour works.

Since x misses P and I is independent, z belongs to C-I and is adjacent
to v. Take bags `{u,v,z}`, `{x}`, `V(F)-{z}`, and the four singleton D
vertices. The third bag is connected and contains a,b. The first two
are adjacent through zx, and each meets the third: use ua for the first
and another C-neighbour of x for the second. Such a neighbour exists
because x has at least three C-neighbours. Every d has at least three
C-neighbours; deleting x,z leaves a contact to the third bag. All other
contacts follow through u or x. This is a K7 model.

After this exclusion, every I vertex has at least two C-I neighbours:
it has at most three D-neighbours and two A-neighbours. The connected
cover construction therefore also permits L to contain both a,b and
at most one C-I vertex. Its complement is connected through v, and
every remaining I vertex retains a C-I neighbour. In particular, if
the I-neighbours of A collectively contact D, take L to be A together
with those neighbours. Thus some D vertex in the remaining instance
has no I-neighbour adjacent to either A root.

These terminal operations in particular exclude `|I|<=2`, for arbitrary
host order. They do not close the independent-I case. In its residue,
each pair of D vertices has a common I-neighbour, no I vertex is complete
to D, and the connected cover just described is absent. A K6 model in
G-{u,v} exists by the six-chromatic deletion statement and HC6. Exactly
one of its bags lies wholly in I, and that bag is a singleton: two such
bags could not be adjacent, while if every bag met W, adjoining {u,v}
would give K7. Enlarging that singleton without losing another bag's
contacts remains unproved. A smaller quotient alone does not resolve it.
For the stated order-two consequence, pairwise intersecting nonempty
subsets of a two-element set have a common element; that element would
be an I vertex complete to D. The empty case is covered by the colouring
lift.

A fan repair remains unproved too. Four disjoint a--D paths avoiding
u,v,b exist. They would form a rooted K2,4 scheme with the length-two
v--D paths if every d had a C-I neighbour outside the fan or on its
own fan path. Minimising total fan length only controls cycles of
foreign contacts: a cyclic reassignment cannot shorten the paths.
An open chain of such contacts can leave a terminal uncovered, so
minimality does not yet provide the required simultaneous choice.

## A whole array from a two-vertex colour class

A different conditional branch assumes `G-{u,p,d}` is five-colourable
for p in P and d in D. Its remaining roots `A=P-{p}`, `B=D-{d}` use
five distinct colours: otherwise restore p,d with six and then colour u.
Restoring just p,d makes the entire sixth class exactly `{p,d}`.

For every pair `a_i in A`, `b_j in B`, their two-colour subgraph contains
an a_i--b_j path, or a Kempe interchange frees a colour at u. There is
also a p--d path of length at most three whose internal vertices have
those two colours. A common neighbour gives a length-two path. If
neither colour occurs at a common neighbour, interchange p with the
b_j-coloured leaves of its star, and d with the a_i-coloured leaves of
its star. These swaps would free a colour at u unless two such leaves
are adjacent; that edge supplies the length-three path.

A sufficient, **unproved** extraction from the full two-by-three array
is a rooted K5 model on A union B satisfying, for every i,j,

`p contacts the b_j bag OR d contacts the a_i bag`.

The clauses force either all three former contacts or both latter
contacts. The corresponding extra root and u would then complete K7.
The ordinary bipartite scheme theorem does not preserve these clauses.
In a deficient projection reduction the orientation may change, and a
vertex carrying an auxiliary contact may enter a different labelled
bag. Its actual contact survives but its required clause need not.
Including every contact vertex also requires proving connectivity of
its projection to the named root. Neither obligation has been met;
this is a construction target, not a new application of contractibility.

## Four-root five-colour extension

**Working lemma.** Let L have four distinct roots X, no X-rooted K4
minor, and at least three nonroots. Suppose every nonempty subset of
V(L)-X has at least four neighbours outside that subset in L. Every
proper precolouring of L[X] from a fixed five-colour palette extends
to L.

Apply Fabila-Monroy--Wood, [Theorem 15 and Section 6](https://arxiv.org/html/1102.3760v1).
L is a spanning subgraph of a member of one of their six obstruction
classes. Every added cell is root-free and attached to at most three
skeleton vertices. The boundary hypothesis therefore makes all cells
empty. Classes A and B have only one and two nonroots, respectively,
and are excluded. It remains to colour the skeleton subgraph.

- **C.** The three nonroots form a triangle v1,v2,v3. The two root pairs
  attach to v1,v2 and v2,v3. The available lists have sizes at least
  3,1,3. Colour v2, then give v1,v3 distinct available colours.
- **D.** The four roots are cofacial in a plane graph. Join consecutive
  roots by arcs in that face. If two consecutive roots have equal
  prescribed colours, identify them along such an arc instead; they
  were nonadjacent in L. Repeat until consecutive colours differ. With
  one remaining root, permute a five-colouring; with two, use the
  precoloured outer-edge theorem below. Otherwise the roots form a
  properly coloured outer triangle or quadrilateral. An existing
  diagonal splits the latter into triangles. Without a diagonal,
  [Diwan, Corollary 1](https://arxiv.org/html/2306.04944v1), with k=5,
  extends its precolouring: the induced cycle has length at most five
  and uses at most four colours. Undo the identifications.
- **E.** The planar core has outer cycle p,q,r,s; p,q are roots, and
  the other two roots attach to r,s. Removing their prescribed colours
  leaves lists of size at least three on r,s. Interior lists have size
  five. If p,q have different colours, retain or add their outer edge
  and extend. If they have the same colour, their actual edge is absent;
  identify them externally and extend with that one precoloured vertex.
- **F.** Each of the four outer core vertices loses at most the two
  colours of its attached root pair. Its list has size at least three;
  every interior list has size five. The outer-face list theorem extends.

The list input in the last three cases is
[Wood--Linusson, Lemma 7, p. 1635](https://users.monash.edu/~davidwo/papers/Thomassen.pdf).
A clique of distinctly precoloured vertices on a minor-class boundary
extends when the other boundary lists have size at least three and
interior lists at least five. Vertices on one face of a planar graph
are such a boundary: adding a new vertex adjacent to them is planar.
The precoloured clique here is empty, one vertex or an outer edge.
Four arbitrary singleton lists are handled separately in class D;
they are not an application of that list theorem.

## A colouring lift across an exterior six-cut

Let T be a six-vertex cut of H contained in C. Then H-T has exactly two
components A,B, containing P,D respectively, and both have neighbourhood
T in H. Indeed every component must contain a neighbour of u; otherwise
T would separate it in G. Each literal clique stays in one component,
and seven-connectivity forces all six boundary contacts.

Let a,b be nonadjacent vertices of T and put X=T-{a,b}. If no such pair
exists, the six singleton T bags and the connected set A already give
K7.

**Working consequence.** G[A union X] has an X-rooted K4. Otherwise G
has the following explicit six-colouring.

For every nonempty W subset A, its neighbours outside G[A union X]
lie in {u,a,b}. Seven-connectivity gives at least four neighbours inside
that graph, since B lies beyond the resulting boundary. Also |A|>=3.
The preceding extension lemma therefore applies if the rooted K4 is
absent.

Contract the connected set A union {u,a,b} to z. Connectivity follows
from the fullness of A and its containing P. This proper minor has
|A|+2 fewer vertices, so it is six-colourable. The vertex z is adjacent
to all of X through A, and to all of D through u. Write gamma for its
colour. Retain the colouring on B union X and give each of u,a,b colour
gamma. These three vertices are independent. Their neighbours in B
avoid gamma because the corresponding quotient edges survive.

Extend the returned precolouring of X over A using the five colours
other than gamma. All restored edges from A to u,a,b are proper; u-D
is proper; there are no A-B edges. This colours the entire original G,
a contradiction. No quotient is assumed to inherit criticality.

The same lift applies to B. In fact its rooted K4 is already structural:
four disjoint paths join X to distinct vertices of D within B union X.
A separator of order at most three, together with u,a,b, would violate
seven-connectivity. The four paths, completed by the literal D edges,
give the rooted model with each bag containing a D vertex.

The lift also has a general form. If a seven-connected graph has all
proper minors six-colourable, A is a full component behind a seven-cut S,
|A|>=3, and I is an independent triple in S, then absence of an
(S-I)-rooted K4 in G[A union (S-I)] makes G six-colourable. Contract
A union I, restore I in its contracted colour, and extend over A with
the other five colours exactly as above.

**Unresolved alternative.** For every nonedge ab of T, both shores can
therefore supply an X-rooted K4. Gluing two arbitrary models along X
produces four clique bags; adjoining u gives at most a fifth. It does
not supply the two remaining bags. The six-path construction with P
multiplicities 222 and D multiplicities 2211 is already recorded in the
technical frontier. Its paths and the rooted models need not coexist
with the required ownership. Choosing a different nonedge, colouring
and model together remains possible; no decreasing exchange has been
proved. Cuts meeting P union D and hosts without this exterior cut are
also outside the present lift.

## What the other global attempts established

For a fixed extendible labelled colouring t of an interface separating P
from D, let F and J be the attainable three-element P palettes and
four-element D palettes. Independent extensions glue, so every f in F
and j in J satisfy |f intersection j|=1. Equivalently, the complement
of j in the six-colour palette lies in every f. If F varies, its
intersection has size two, determining J uniquely. Thus at least one
shore has a fixed terminal palette within each interface colouring.
The fixed shore can change with t. The first missing step is a proper
minor operation preserving a compatible interface colouring on both
sides; fibrewise rigidity alone gives no such operation.

The forest-contraction attempt has a different failure. Contractions
can produce a fresh colouring of the original graph minus the allocated
resource vertices, while fixing the retained roots. Restoring those
vertices is still a list-colouring problem. The
[explicit triangle example](../barriers/bipartite_forest_two_colour_lift.md)
rules out a general repair using only the quotient colour and one spare
colour, even when every projection forest is a tree. It does not refute
the rooted-minor construction or a recolouring that changes the exterior.

Elementary edge responses alone add no contraction-specific colouring
information: in every six-colouring of G-e the two ends of e are equal,
since otherwise G would be six-colourable. These are exactly the
colourings of G/e. A construction using full minor criticality must use
additional contractions and prove their expansion step.

The completed two-triangle structural proof cannot currently be applied
with a distinguished split root. Contracting an edge of D supplies an
ordinary cap-meeting K5, but its bag at that edge need not split while
retaining the other contacts. The existing prism normalisation excludes
all such K5 models; excluding only those that admit the split-root lift
does not justify that normalisation. A new construction must address
this first inference before using its later web descriptions.

## Minimising a shore while retaining the root placements

Starting from an exterior six-cut, allow subsequent six-cuts T of H to
meet P, but require `T intersect D` to be empty and `P-T` to be nonempty.
The two components A,B contain P-T,D, respectively. They are the only
components and both are full, by seven-connectivity and the two literal
cliques. Choose |A| minimum over this enlarged class in the **fixed G**.
Write `k=|T intersect P|`, so k is 0, 1 or 2.

Every nonempty proper subset U of A has at least seven neighbours in H.
For connected U missing P, this follows from seven-connectivity of G,
since u misses U. For connected U meeting P, a boundary of size six
would be a smaller eligible cut: it avoids D, every P vertex outside U
lies on the boundary, and D remains on the other side. A smaller
boundary contradicts seven-connectivity. For disconnected U, apply the
bound to one component, whose neighbours are also outside U.

Consequently, if |A|>=2, every t in T has at least two A-neighbours:
otherwise deleting its sole neighbour v leaves the nonempty proper set
A-v with boundary contained in `{v} union (T-{t})`. Completing T to a
clique makes H[A union T] seven-connected. A cut of order at most six
cannot detach a proper A-subset; deleting all of T leaves A connected.
The completion is auxiliary: its new edges are not minor contacts.

This is a minimum-shore argument, not induction on a smaller critical
graph. A replacement cut strictly decreases |A| and retains the original
G, D and all named P vertices, including those now on T. It does not
justify discarding the k=1 or k=2 endpoints.

## The simultaneous construction still needed

For any four-element X subset T, four disjoint paths in H[B union X]
join X to distinct D vertices. A separator of order at most three there,
together with u and T-X, would separate G with at most six vertices.
These paths give four clique bags, each containing its D endpoint.

Thus, when k=0 or 1, it suffices to find two disjoint connected subsets
L,R of A, each meeting P, with at least four common neighbours in T.
They are adjacent through the literal P clique. Choosing four common
neighbours as X gives the four preceding bags, L,R and {u}: seven
disjoint connected bags with every required contact. Unused A vertices
can be assigned to L or R while preserving connectedness, so a connected
bipartition is an equivalent sufficient target. **Its existence is
unproved**, even under the minimum-shore boundary condition.

There are elementary endpoints. If k=0 and A=P, each P vertex has at
least five T-neighbours, so two share four. If |A|=2, both vertices are
adjacent and complete to T. For k=1 take them as L,R. For k=2 write
`A={p,x}` and choose `q in T intersect P`; take `L={p}`, `R={x,q}` and
`X=T-P`. All four X contacts are actual, and R meets P through q.
These constructions exclude those endpoints without a colouring lift.

The singleton endpoint necessarily has k=2. Write `A={p}`,
`P={p,a,b}` and `Q=T-{a,b}`. Then
`N_G(p)={u,a,b} union Q` and Q is a four-clique: Dirac's degree-seven
neighbourhood bound excludes an independent triple `{u,x,y}` with
nonadjacent x,y in Q. This leaves two adjacent degree-seven centres u,p
with common neighbours a,b and respective four-cliques D,Q. It is not
closed. The named clique and centre adjacencies do not force equal D,Q
palettes in a colouring of G/up: the possible boundary trace
`a=5, b=4, D={1,2,3,4}, Q={1,2,3,5}, up=6` defeats that inference alone.
Recolouring a centre with its omitted clique colour conflicts with a
or b. A compatible linkage or a different whole-host colouring is needed.

The stronger proposal to partition A into three P-rooted connected sets
while splitting every T-neighbourhood is
[false](../barriers/hc7_six_cut_three_part_partition.md). This does not
refute the two-set target. Maximising the number of shared neighbours
also gives no descent yet: moving a connected piece can gain one contact
and lose another, or disconnect the retained P-containing side. The
missing exchange must preserve both connected sides and root ownership,
then increase that number or produce a genuinely smaller eligible shore.

## What transfers from the OpenAI release

At the [reviewed revision](../archive/openai_math_review_2026-10-07/README.md),
the linear list-colouring paper's constrained-colouring lemma requires
lists of size at least `m+6k`, induced k-connected subgraphs to be
m-choosable, and a weighted boundary budget at most `2k^2`. Its separator
accounting is a useful template, but at six colours the numerical slack
is unavailable. Ordinary proper-minor six-colourability is not the
required list-colouring hypothesis.

Lemma 6.9 combines doubled routes, selecting one start from each pair
and unspecified distinct targets. It does not preserve a chosen endpoint
assignment. Here retaining an entire X-rooted K4 on the A side leaves
only T-X, two vertices, for P-to-D routes avoiding that model. This
cannot supply two doubled P sources. Releasing bags permits more routes
but requires rebuilding their contacts simultaneously. Unpaired path
minimisation can change source ownership, so its sparsity bound does not
repair that step. The two-set target above incorporates the needed
contacts in the construction itself; it is not a consequence of the
released lemma. No additional HC7 case or valid induction follows yet.
