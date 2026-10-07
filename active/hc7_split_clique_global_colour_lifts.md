# Global colouring lifts in the split-clique case

**Status, 7 October 2026:** working deductions, not separately audited.
Neither the exterior six-cut branch nor the whole split-clique case is
closed. The strongest construction below restores a colouring of the
original host in one rooted-minor alternative. No induction is asserted.

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
