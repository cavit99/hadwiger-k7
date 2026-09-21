# Extremal prism normalisation for two anticomplete triangles

**Status:** written proof, with a [separate internal audit](hc7_two_triangle_extremal_prism_audit.md).
This is an unbounded structural reduction, not a closure of the critical-host
case or HC7. All graphs are finite and simple. No computation is used.
Its application belongs to the [original-host construction](../active/hc7_degree7_exceptional_construction_working.md).

## Statement

Let J be a four-connected graph containing an ordinary K5 minor. Let
P={p1,p2,p3} and Q be two vertex-disjoint literal triangles, with no edge
between P and Q. Put T=P union Q. Suppose J has no K5 model all five of
whose branch sets meet T.

Then Q can be labelled {q1,q2,q3}, and there exist a nonempty connected
set E disjoint from T and three nonempty pairwise disjoint sets C1,C2,C3,
such that:

1. V(J) is the disjoint union of E, P, Q, C1, C2, C3.
2. J-E is an induced subdivision of the triangular prism. Its two
   triangles are the literal P and Q, and its three vertical paths are
   Ri=J[{pi,qi} union Ci]. Each Ri is an induced pi--qi path, with interior
   exactly Ci. Thus each vertical path has length at least two.
3. E is adjacent to every vertex of P. If D=Q union C1 union C2 union C3,
   then D is connected and adjacent to every vertex of P. Among all
   partitions V(J)-P=D' disjoint union E' with both parts nonempty,
   connected, and adjacent to every vertex of P, and with Q contained in
   D', the displayed E has maximum cardinality.
4. Every vertex t of T has exactly three neighbours outside E, and every
   vertex x of C1 union C2 union C3 has exactly two neighbours outside E.
   Consequently d_E(t)=d_J(t)-3 and d_E(x)=d_J(x)-2.

In particular, for the original critical-host J, five-connectivity and
the six-neighbour boundary condition give at least two distinct actual
E-neighbours at every t in T and at least four at every internal vertical
vertex. The general theorem itself requires neither five-connectivity
nor that boundary condition.

## Source dependency and the initial partition

The only non-elementary external input needed for this statement is
Costalonga--Zhou, *Triangle-roundedness in matroids*, Theorem 4, in
[arXiv:1711.01618v3](https://arxiv.org/html/1711.01618v3): in a
three-connected graph with a specified triangle and an ordinary K5 minor,
there is a K5 minor retaining the three literal triangle edges as the
edge set of a triangle. Its primary statement was inspected. Applied to
P, the three P vertices therefore lie in distinct branch sets.

Here is the elementary normalisation of that model used in the working
frontier. Let A1,A2,A3 be its three P-rooted bags, and let D,E be the other
two bags. Among such models maximise W=D union E. If a root bag Ai has
two distinct actual neighbours of W, choose distinct vertices d,e of Ai
contacting D,E respectively. Such a choice exists unless the union of
the two contact sets is a singleton. Replace Ai by a minimal tree joining
pi,d,e. At least one of d,e is a leaf different from pi; move that leaf
into the helper it contacts. The remaining tree retains pi and its
contact with the other helper; its edge to the moved leaf retains the
first helper contact. Literal P edges preserve contacts between root
bags. This increases W, a contradiction.

Thus each Ai has exactly one actual vertex vi adjacent to W. An unused
component adjacent to W could also be absorbed into a helper, so there is
none. It follows that N_J(W) is contained in {v1,v2,v3}. Four-connectivity
forces V(J)=W union {v1,v2,v3}: otherwise these at most three vertices
separate the nonempty W from a vertex outside. Therefore pi=vi and each
Ai={pi}. The two helpers partition J-P, are connected and P-full, and
are adjacent.

If both helpers meet Q, the model already meets T in all five bags.
Otherwise orient them so Q is contained in D. Such a partition exists.
Now choose it to maximise |E| over all partitions in item 3. This is a
maximum over a finite nonempty set. No induction or quotient criticality
is asserted.

Throughout the remaining proof, both parts of a new connected partition
of J-P are automatically adjacent: J-P is connected, by four-connectivity.

## Shadows of vertices contacting E

For v in D define M(v) as the component of J[D]-v containing Q-{v}.
This component is well defined, because Q-{v} contains at least two
vertices and induces a clique. Set S(v)=D-M(v). Thus S(v) contains v and
every other component of J[D]-v. It is connected: each such component has
a neighbour at v because J[D] is connected.

Claim 1. If v in D has a neighbour in E, then there exists i such that
the nonempty set N_D(pi) is contained in S(v).

Proof. If M(v) were P-full, E union S(v) and M(v) would be connected
P-full parts. If v is not in Q, the second part contains all of Q, and
the first is strictly larger than E, contradicting maximality. If v is
in Q, the first part contains v and the second contains Q-{v}; together
with singleton P these parts form a T-meeting K5 model, a contradiction.
Therefore M(v) misses some pi, which is exactly the claimed containment.
Nonemptiness follows from the P-fullness of D. QED

## The block containing Q is exactly Q

Let B be the unique block of the connected graph J[D] containing the
literal triangle Q. For w in D define its projection pi_B(w) onto B as
w itself if w lies in B, and otherwise as the unique vertex of B through
which the component of J[D]-V(B) containing w attaches to B. Existence
and uniqueness are the elementary block-cut-tree property; a component
attached to two vertices of B would belong to the same block as B.

For every v in D, all vertices of S(v) have a common projection g(v).
Indeed, if v lies in B, B-v is connected and contains Q-{v}, so S(v)
consists of v and components hanging from v, and its projection is v.
If v is outside B, B is contained in M(v), and S(v) lies wholly in the
single branch of the block-cut tree containing v, so its projection is
the attachment of that branch to B.

Call index i localised if the projections of the nonempty set N_D(pi)
form a singleton {gi}. Let L be the set of localised indices and let
Gamma={gi:i in L}. Claim 1 implies that every neighbour v of E in D has
projection in Gamma: its assigned index is localised because S(v) has
only the projection g(v), and then g(v)=gi.

Suppose B-Gamma is nonempty, and put

    Z={w in D: pi_B(w) is not in Gamma}.

Then Z is nonempty. No vertex of Z has a neighbour in E. A P vertex
neighbouring Z must have an unlocalised index. Finally N_D(Z) is contained
in Gamma: the full hanging branch at a vertex of B is included together
with that vertex, so only edges of B can leave the chosen projection
region. Consequently

    N_J(Z) subseteq Gamma union {pi:i not in L},
    |N_J(Z)| <= |L|+(3-|L|)=3.

The nonempty E lies outside Z and this boundary, contradicting
four-connectivity of J. Therefore B is contained in Gamma. Since B
contains the three vertices of Q, while |Gamma|<=|L|<=3, all indices are
localised, the gates gi are distinct, and B=Gamma=Q. Relabel Q so gi=qi.

This argument does not require three disjoint E--Q arms, nor any lower
bound on |E|. In particular it applies unchanged after deleting one
root-free vertex from a five-connected J, provided an ordinary K5 minor
remains.

## Exactly one component at each triangle vertex

Every component C of J[D]-Q attaches to exactly one vertex qi of Q.
If C contains no neighbour of pi, it contains no P-neighbour at all,
by the established projection ownership. It then has no E-neighbour:
for v in C, S(v) is contained in C, so Claim 1 would force all neighbours
of some P vertex into C. Its entire J-boundary would thus be {qi},
contradicting four-connectivity.

Thus every component attached at qi contains a neighbour of pi. Such a
component must have an E-neighbour, since otherwise its J-boundary is
contained in {pi,qi}. At an E-neighbour v in C, Claim 1 and the distinct
projections imply N_D(pi) is contained in S(v), which is contained in C.
Therefore all D-neighbours of pi lie in this component, and there can be
no second component at qi (which would also have to contain a neighbour
of pi). Denote the unique component by Ci.

The Ci are nonempty: N_D(pi) is nonempty and cannot contain qi because
P and Q are anticomplete. There are no edges between distinct Ci, no
edges from Ci to pj or qj for j different from i, and Ci attaches to qi.

## Each component is an induced path

Let Ki=J[Ci union {pi,qi}]. This graph is connected. Each vertex v in Ci
having a neighbour in E separates pi from qi in Ki: Claim 1 gives
N_D(pi) subseteq S(v), while qi lies in M(v), so a pi--qi path avoiding v
is impossible. Hence all E-contact vertices in Ci are cutvertices on the
pi--qi spine of the block-cut tree of Ki.

There is no branch of that block-cut tree off the pi--qi spine. Its
vertices other than its attachment contain neither pi nor qi and none
of the cutvertices separating those endpoints. They therefore have no
E-contact. By the component ownership just proved they have no other
external contacts, so their actual J-boundary is their one attachment
vertex, contradicting four-connectivity.

Consider a block on the remaining spine. Its two spine ends are its
entry and exit vertices, with pi or qi serving as the end at an extremal
block. If the block has any further vertex, the set of all its vertices
other than those two ends has no E-contact: those vertices do not
separate pi from qi. There are no off-spine branches, and all other
possible external contacts have already been excluded. This nonempty
set therefore has actual J-boundary contained in the two spine ends,
again impossible. Thus every block on the spine is an edge. Ki is an
induced pi--qi path with interior exactly Ci.

All claimed graph identities and degree counts now follow. The complete
vertex partition means no omitted vertices or unrecorded attachments
are being discarded. E remains the same extremal helper throughout.

## Consequences in the original critical graph

Assume now that G is seven-connected, has chromatic number seven, and
every proper minor is six-colourable. Let N_G(u)=P union Q union {r},
where P,Q are anticomplete triangles and r is adjacent to every vertex
of P union Q. Suppose G has no K7 minor, and put J=G-{u,r}.
Then J is five-connected and has chromatic number at least five:
a four-colouring of J together with new colours on u,r would colour G
with six colours. Hadwiger's theorem for K5 supplies an ordinary K5
minor. A T-meeting K5 in J would extend with singleton bags {u},{r},
so the normalisation applies.

Every nonempty X contained in J-T has at least six neighbours in J.
Otherwise N_G(X) is contained in N_J(X) union {r}, since u has no
neighbour in X. These at most six vertices separate X from u, contrary
to seven-connectivity. In particular every internal vertex of a vertical
path has at least four E-neighbours; every triangle vertex has at least
two by five-connectivity of J. These are actual distinct neighbours.

### Colouring the connected remainder

Let F=G[E union {r}]. Then chi(F)>=4. Indeed, the induced prism
subdivision J-E is three-colourable: colour each triangle and extend
over each vertical path, all of which have length at least two. If F
were three-colourable, use a disjoint palette on the prism and give u
any F colour different from the colour of r. This is a six-colouring
of G because u has no neighbour in E or in the path interiors.
Consequently E is not bipartite. In contrast, G/E is five-colourable:
use three colours on the prism, one on both u and the contracted E
vertex, and one on r. This quotient colouring is not asserted to lift.

### A simultaneous exchange

Write I_i=V(R_i)-{p_i,q_i}. Suppose x is a vertex of E such that
E-{x} is connected and x has a neighbour in I_i. Then every neighbour
of x in J-E lies on R_i.

To prove this, suppose first that x has a neighbour in
D-V(R_i). Removing q_i from D leaves exactly two components: I_i,
and the connected union of the other two vertical interiors and the
edge on Q-{q_i}. Thus

    H1=(E-{x}) union {q_i},   H2=(D-{q_i}) union {x}

are disjoint connected sets. The first is connected because q_i has
at least two E-neighbours. It remains adjacent to all of P because
each p_j also has at least two E-neighbours. The second contains every
I_j and is therefore adjacent to all of P. They are adjacent through
an edge of Q, and both meet Q. With the three singleton P bags they
give a T-meeting K5, a contradiction.

If the outside neighbour instead belongs to P-{p_i}, interchange
P and Q in this construction. The remainder E-{x} is also Q-full,
by the same degree bounds. These cases cover every prism vertex
outside R_i. No connectivity or root contact is inferred from a
contracted helper.

More generally the first exchange works with a connected set X in E
in place of {x}, provided E-X is nonempty and connected, remains
P-full, and still contacts q_i, while X meets both components of D-q_i
by edges. These conditions suffice for the same two displayed bags.
They are not consequences of connectedness of X alone.

### Locality forced by maximality

For any vertex x of E with E-{x} connected, any two neighbours on a vertical
path have distance at most two along that path. Otherwise choose
neighbours y,z at distance at least three, replace y R_i z by y-x-z,
and move its at least two internal vertices into E-{x}. Each moved
vertex has at least four E-neighbours, at most one of which is x, so
the enlarged helper is connected. Every P vertex retains an E
neighbour. The other helper consists of Q and the modified paths;
it is connected and P-full. These are disjoint parts covering J-P,
and the new E is larger, contrary to its defining maximum. Extra
edges in the modified paths do not matter: this comparison requires
a connected partition, not an induced prism.

Together with the exchange, every non-cut vertex of E that contacts
a path interior has all its prism neighbours in a segment of at most
two edges of that one path.

### Vertices contacting only triangle roots

A non-cut vertex x of E cannot be adjacent to both p_i and q_j with
i different from j. Relabel these indices as 1 and 3 and set A=E-{x}.
The following five bags would give a T-meeting K5:

    A union {p3};
    {p1} union I1;
    V(R2);
    {q1};
    {x,q3}.

The first bag is connected and adjacent to every other bag: every prism
vertex retains an A-neighbour, and x has an A-neighbour since E is
connected and has more than one vertex. The other four bags are connected.
Among the middle three, the required contacts are supplied respectively
by the P edge, the last edge of R1, and the Q edge q2q1. The last bag
contacts them through xp1, q3q2 and q3q1. Disjointness follows from the
three disjoint vertical paths and x outside A.

Consequently the prism neighbours of every non-cut vertex of E lie
either in P, in Q, or in a segment of at most two edges of one vertical
path. For a vertex contacting only roots, a matched pair {p_i,q_i}
also satisfies the segment bound by locality. In all cases it has at
most three prism neighbours. Its degree in J is at least six, so its
degree inside E is at least three. This does not control a connected
set of such vertices or supply a rooted model inside E.

## Exact remaining construction obligation

This theorem does not show that the induced-prism configuration contains
a T-meeting K5. In particular, contracting E erases the multiplicity and
placement of its actual contacts and leaves only a cone over a prism,
which does not supply the required rooted model. A completion must use
the original E, all column contacts and, where needed, the critical-host
colourings or the additional vertices u,r. For J-x the normalisation is
available independently; no compatibility between its E and the old E
has yet been established. The connected-set exchange must retain the
complement's connectivity and root contacts through vertices with no
path-interior contact and through separations of E. The locality result
does not supply that step or a decreasing induction. Neither the
two-triangle case, the whole degree-seven case, nor HC7 is proved here.
