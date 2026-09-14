# Bipartite colour-class exchanges for chromatic augmentation

**Status:** unaudited research draft. The elementary statements below have
written proofs; the global augmentation construction remains unproved.
The ledger and designated frontier remain the status authorities. This
draft neither proves HC7 nor establishes an NT-comparable theorem.

The target is that every finite simple five-connected six-chromatic graph
H with minimum degree at least six and order at least seven contains
Q7 = K7 minus two independent edges. Write W4 for a four-cycle with a
universal hub, so Q7 = K2 joined to W4 = K3 joined to C4.

All bags below are connected subsets of the original H. Nothing permits
combining independently selected models or treating a chromatic quotient
as preserving minimum degree or connectivity.

## 1. An exact partition retaining all six colours

**Proposition.** Let H be six-chromatic. There is a partition
V(H) = S disjoint union R such that H[S] is bipartite and chi(H[R]) = 4.
If S is inclusion-minimal among bipartite sets with four-colourable
complement, then S contains an edge and, for every s in S,
chi(H[R union {s}]) = 5. Consequently N_H(s) intersect R is colourful:
it meets every colour class in every proper four-colouring of H[R].

**Proof.** Take two classes of a proper six-colouring for S. The other
four classes colour R. If R were three-colourable, the bipartition of S
would give a five-colouring of H. Minimise S by inclusion while retaining
these properties. If S were independent the same contradiction would
follow. For any s in S, the set S minus {s} is still bipartite, so
minimality says that R union {s} is not four-colourable. It is
five-colourable by giving s a fresh colour. A four-colouring of R missing
one colour on N_H(s) would extend to s. This proves every assertion.

The conclusion does not say that two of these colourful neighbourhoods
root one common model. Nor does the collection of individual neighbourhood
conditions imply that H is six-chromatic: a five-colouring may use all
five colours on R. The full hypothesis chi(H) = 6 remains in force.

## 2. One common rooted model from a bipartition

The next statement uses the full chromatic hypothesis and does not
require S to be connected or inclusion-minimal.

**Proposition.** Let H be six-chromatic, let H[R] be four-colourable,
and let (U,V) be any proper bipartition of H[S], where S = V(H) minus R.
Define

    M(U,V) = {r in R : N_H(r) meets U and meets V}.

Then M(U,V) is colourful in H[R]. Therefore H[R] has one K4 minor model
with a distinct root r_i in M(U,V) in each of its four bags.

**Proof.** The preceding two-plus-three colouring argument gives
chi(H[R]) = 4. Suppose that a class C in a proper four-colouring of R
avoids M(U,V). Each vertex of C has neighbours in at most one of U,V.
Extend the bipartition of S by placing each such vertex opposite the
shore containing its S-neighbours; vertices with no S-neighbour may go
on either side. This is proper because C is independent. Thus S union C
is bipartite. Its two colours and the other three colour classes of R
give a five-colouring of H, a contradiction.

Apply Martinsson--Steiner Theorem 1.3, with its exact set-rooted statement
recorded among the inputs to
[the four-connected five-chromatic theorem](../results/four_connected_five_chromatic_minor.md).
It supplies the asserted single model. Each selected r_i has actual
neighbours in both U and V. These neighbours lie outside all four bags.

In particular this statement holds for every independent choice of the
orientations of the connected components of H[S]. Choosing the orientation
and the rooted model together is permitted. This avoids a separate
connected-footprint existence assumption.

**Exact limitation.** U and V need not be connected. The four roots can
use unrelated vertices in either shore. Furthermore, the first
proposition's colourful neighbourhood of s need not meet these particular
four bags. Replacing the full R by the K4 model can lose the vertices
establishing that colourfulness. The first unsupported step would be to
declare every s adjacent to all four contracted bags, or to contract each
independent shore as though it were connected.

**The same argument in the actual critical host.** More generally, if
`chi(G)=k+r`, S has a proper k-colouring and R=G-S is r-colourable,
then the vertices of R seeing every S-colour class are colourful in R.
A missed R-class could be inserted vertex by vertex into missing
S-colours, giving k+r-1 colours on G. No roots or edges are changed.

Apply this to a six-colouring of G-v in the actual seven-chromatic C19
host. Choose two whole classes U,V whose representatives in N(v) are
singletons, and put `S={v} union U union V`. Give v a third S-colour;
the other four classes colour R. One rooted K4 in R then has four
actual neighbours of v, each also contacting both U and V. The same
conclusion holds after every component flip that keeps v's S-class
singleton. This is one compatible model, but its contacts to U,V need
not lie in the component containing their prescribed neighbours of v.
It therefore does not supply the two further connected bags.

## 3. A complete edge-footprint subcase

**Proposition.** Suppose H satisfies the augmentation hypotheses. Suppose
uv is an edge and H minus {u,v} is four-colourable. If u and v have at
least five common neighbours, H contains Q7.

**Proof.** Put R = V(H) minus {u,v}. The second proposition applies
with U = {u}, V = {v}, so the common-neighbour set M is colourful in
the four-chromatic graph H[R]. It gives a K4 model in H[R] with four
distinct roots in M. Choose a fifth member of M. Five-connectivity of H
implies three-connectivity of H[R]: deleting at most two additional
vertices deletes at most four vertices from H.

Apply the existing
[five-root wheel extension](../results/hc7_rooted_wheel_extension.md)
in H[R]. It returns five disjoint W4 bags, each retaining a different
member of M; the fifth root may have belonged to the initial model.
Both singleton bags {u} and {v} contact every wheel bag and contact
each other. These seven original sets give K2 joined to W4, hence Q7.

This argument uses no contraction preserving the augmentation class.
The terminal certificate replaces the need for such a preservation claim.

**Exact remaining edge-footprint case.** If the common-neighbour set has
four members and induces K4, then uv and those four vertices form a
literal K6. A component outside that K6 has at least five distinct
neighbours in it, by five-connectivity and the order hypothesis, and
gives Q7 together with the six singleton bags. Consequently the unresolved
edge-footprint case has exactly four common neighbours, they are rainbow
in every four-colouring of R, and they do not induce K4. Each pole has at
least one additional exclusive neighbour in R, by minimum degree six.

It is not enough to choose the two exclusive neighbours separately as a
fifth wheel root. A fifth wheel bag would have to retain both contacts in
one connected set disjoint from the other four bags. No such simultaneous
extension is proved here.

## 4. A simultaneous exchange with a proved colour invariant

**Proposition.** Retain a bipartition (U,V) of S and a proper
four-colouring of R. Let C be one entire colour class and put

    I = U intersect N_H(C),
    S' = (S minus I) union C,
    R' = (R minus C) union I.

Then H[S'] is bipartite and chi(H[R']) = 4.

**Proof.** A bipartition of S' is

    V,   (U minus I) union C.

The second shore is independent: U and C are individually independent,
and every U-neighbour of C was put in I. In R', keep the other three
old R colours and give I the vacated fourth colour. Since I is
independent this is proper. A three-colouring of R' together with the
bipartition of S' would five-colour H, so its chromatic number is four.

This can transfer arbitrarily many vertices simultaneously. It changes
the partition of the fixed original graph, not the graph itself. Component
orientations and the chosen four-colouring may change before another
exchange. The exchange can join old S-components through C, but deleting
I can also split them. Thus neither a component-count decrease nor
minimum-degree preservation has been inferred. The mixed-root proposition
applies anew to every resulting state.

A more flexible version keeps one compatible six-colouring throughout.
Choose any collection of connected components of H[U union C], let K
be their union, and interchange the U-colour and C-colour on K. There
are no edges of H[U union C] from K to its complement. The new colouring
is therefore proper. With

    I = U intersect K,   J = C intersect K,
    S' = (S minus I) union J,
    R' = (R minus J) union I,

the same two-plus-four partition is retained. This is an ordinary Kempe
exchange with the whole bipartite footprint and the remaining four
classes tracked explicitly. The preceding canonical move is the choice
of every component meeting C, leaving isolated U-vertices in place.

If S has minimum cardinality over all such partitions, every individual
component K of H[U union C] satisfies |U intersect K| <= |C intersect K|.
Otherwise that component exchange produces a smaller admissible S.
This is only a necessary balance condition. It neither supplies a
matching nor bounds how deleting U intersect K fragments H[S]. A proof
based on fewer components must control those fragments and the newly
joined components in the same move; a bare colour-class size comparison
cannot establish the missing global improvement.

## 5. Rejected allocations and the remaining global choice

Full domination of R by two adjacent edge bags is unavailable in every
triangle-free six-chromatic host. If adjacent endpoints dominate the
complement of a four-vertex set, that complement is bipartite: partition
it according to which endpoint is a neighbour, using the independence of
each endpoint's neighbourhood. The four-vertex set is also bipartite in
a triangle-free graph. The resulting four-colouring is a contradiction.
Arbitrarily large bags and contacts to selected model bags remain allowed.

A fixed allocation of two S-bags and five R-bags can fail even for a
connected inclusion-minimal S. Take H = K4 joined to C4, let S be the
C4 and R the K4. H has chromatic number six, connectivity six and
minimum degree six. Adding any S-vertex back to R gives a K5, so S is
inclusion-minimal. There cannot be five nonempty R-bags. A terminal model
instead uses three R-singletons joined to the four S-cycle bags. This is
Q7 itself; alternatively three consecutive S-vertices and all four
R-vertices give K7 minus one edge.

The surviving construction therefore permits all seven bags and their
roles to change. The mixed-root proposition supplies one common K4 with
four simultaneous two-shore attachments. It does not yet provide a way
to distribute S and the unused part of R among seven connected bags
while preserving the required contacts. A valid advance must either
construct that terminal allocation, find a smaller instance satisfying
every required hypothesis with a decreasing parameter and fixed lift,
or obtain a five-colouring of the entire original H.

No such exhaustive global alternative is proved. In particular the
exchange proposition supplies valid successor partitions, but no
well-founded induction or guaranteed terminal selection.

The [audited connected-allocation counterexample](../barriers/bipartite_colour_allocation.md)
refutes replacing the independent shores by connected bags within a fixed
S. One four-colouring defeats both possible connected partitions in the
specified eleven-vertex host. Reselection of S remains possible, and a
wheel bag may use different vertices for its two external contacts.

### A checked exchange changes an initially selected root

In X the connected bags

    {2}, {0,1,3}, {4}, {7}, {5,6,8}, {9}, {10}

give K7 with only the pairs {2}--{9} and {9}--{10} absent. The quotient
is six-chromatic, but its degree-four vertex does not belong to the
augmentation class. Split {0,1,3} into {1} and {0,3}, then merge {0,3}
with the old singleton {2}. The seven bags become

    {1}, {0,2,3}, {4}, {7}, {5,6,8}, {9}, {10}.

They give K7 minus the sole pair {9}--{10}. The new singleton {1}
contacts all six other bags, while {0,2,3} is connected through 02 and
03 and retains the contacts to {4}, {7}, {10} through 2. The other
nonsingleton bag is connected through 58 and 68. Direct checking of all
21 pairs confirms the one omission. The existing original-host
`check_model` verifier independently checks these connectivity and contact
assertions; no universal inference is drawn from this finite check.

This terminal exchange does not preserve the original bipartite footprint:
the new three singletons {1}, {7}, {9} form a triangle. Allowing that
change is essential to the purpose of the operation. Neither a literal
colour-class swap nor a fixed-root extension describes this move.
