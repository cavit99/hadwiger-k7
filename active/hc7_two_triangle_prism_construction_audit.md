# Independent audit of the maximal-component construction

**Verdict: GREEN for the stated normalisation, terminal certificates,
zero-contact-path conclusion, conditional switches, straddler bound and
one-contacted-path consequences.**

This separate internal audit does not establish the missing global rerouting,
either exterior chromatic case, C19, C21, HC7 or comparative significance.
The source remains an active construction draft, not a promoted global proof.

**Source:** [the construction](hc7_two_triangle_prism_construction.md).

**Current exact source SHA-256:**
`c8ce1f59cee42fc852153b92e8e53ab936894bb42e20045b9bf945a80b735724`.

**Original normalisation revision:**
`137d12c34cf2f477b80498c254c9a089d2985f7ac4b868800871924d9d70fb31`.

**Reviewer and scope.** On 14 September 2026, `plan_certificate_compute`
independently reconstructed the maximality and residual-cut argument before
reading the written source, then checked the complete pinned revision. The
reviewer did not originate this construction. The only requested clarification
was to specify the two split-network arcs for each undirected edge explicitly;
the original pinned source includes it. On the same date,
`plan_objective_allocation` independently checked the new diagonal certificate,
five-vertex separator, switches, straddler bound and one-contacted-path
consequences at the current hash, after reading the original audit. This
second reviewer did not author those additions.
No finite search is a premise of either review.

## Hypotheses and initial linkage

The source retains the actual critical-host assumptions and the exact identity
`N(v)=A dotcup B dotcup {x,y}`. For these deductions the decisive assumptions
are seven-connectivity, the degree bound, the six distinct triangle terminals,
that identity, and the literal edge xy. Chromatic criticality, the exterior
chromatic split and the absence of neighbourhood four-cycles are not silently
used to obtain a stronger conclusion. This review does not re-audit the
frontier's derivation of the standing assumptions.

Deleting v,x,y leaves a four-connected graph containing both three-sets of
terminals. Any deletion of at most two vertices leaves a terminal of each
set and a path between them. The vertex form of Menger's theorem therefore
supplies three disjoint A--B paths. They use all six terminals as endpoints;
there is no additional terminal available as an internal vertex. The literal
edge xy gives a nonempty complementary component containing both ports.

There are finitely many linkages, so maximising the order of that component
is legitimate. If w in D is avoided by a linkage in H, then the new
complement in F contains the connected set C union {w}. It still contains
both ports and is strictly larger. This proves D vital without a tie-break,
an unproved exchange, or assumptions about other complementary components.
All terminals are vital by definition. Hence a nonvital vertex has no C
neighbour and no v neighbour; the latter conclusion uses the exact N(v).

## Network, terminals and minimum cuts

Vertex arcs have capacity one. An edge uw gives arcs `u+ -> w-` and
`w+ -> u-`; the terminal arcs also have capacity M. Three simple linkage
paths give a flow of value three, and the three A vertex arcs bound the
value above by three. Removing circulating flow leaves the intended
vertex-disjoint paths with free endpoint pairing.

The displayed source side X_A crosses exactly the three A vertex arcs;
X_B crosses exactly the three B vertex arcs. No capacity-M arc crosses
either cut. They are nested minimum cuts, and both are closed under outgoing
residual arcs. In particular no terminal is omitted from the argument by
treating its capacity as infinite. Here S(X) is an A--B vertex separator
that may include terminals: the endpoint cases are S(X_A)=A and S(X_B)=B.
It need not be an ordinary separating cut of H after every terminal on one
side is deleted. The proof requires its cardinality and arc positions,
and does not infer such additional connectivity information.

Contracting residual SCCs gives an acyclic directed graph. The difference
between the nested closed sets can be added one SCC at a time by choosing
a component whose outgoing successors are already present. Each intermediate
source side is residual-closed, contains s and excludes t, so it is a minimum
cut of value three. Since M is greater than three, only three unit vertex
arcs cross it. Every original edge arc has positive forward residual capacity
under the chosen path flow, which justifies each subsequent closure inference.

For a used vertex u, the residual reverse vertex arc is `u+ -> u-`.
If its copies share an SCC, a residual cycle through that reverse arc permits
an integral unit circulation reducing its usage from one to zero while
preserving flow value. Decomposing the resulting flow supplies a linkage
avoiding u. Conversely, subtracting the chosen maximum flow from an avoiding
maximum flow is a residual circulation containing that reverse arc. Its cycle
decomposition puts both copies in one SCC. This checks the equivalence in
the source; an unused vertex is already nonvital.

## Exhausting the nonvital vertices

In a reverse state, `u+ in X` and `u- not in X`, closure along both arcs of
every incident edge puts every neighbour's in-copy inside X and out-copy
outside X. Thus all H-neighbours of u lie in the same three-set S(X).
A used vertex cannot have this state because its reverse vertex arc would
cross the residual cut. Therefore u is nonvital, has no C or v neighbour,
and has degree at most three in G, contradicting the retained degree bound.

An unused vertex with copies in different SCCs has its forward vertex arc
residual. Its out-copy must consequently enter the chain before its in-copy,
creating the excluded reverse state. Nonvital vertices are nonterminals,
so both copies lie in the portion traversed by the chain. Hence every
nonvital vertex enters with both copies in one SCC step.

For such a step, include in Z all vertices whose two copies enter together.
For an outside neighbour w, the edge arcs force `w+ not in X` and
`w- in X'`. Either w is in S(X), or its in-copy enters at the step while
its out-copy remains outside X', putting it in S(X'). Thus the external
boundary of Z has at most six vertices. These separators are disjoint
from Z. Every Z vertex is nonvital, so there are no additional edges to C
or v. If Z were nonempty, deleting that boundary would leave both Z and
the nonempty C surviving without a path between them. Seven-connectivity
rules this out. The two possibilities exhaust the nonvital vertices.

This proves that every linkage in this fixed H spans H. It does not assert
a unique linkage, fixed pairings, or a bound on individual root degrees.

## Terminal ownership and the remaining obligation

On each of the first two paths, two distinct contacts permit an edge split
leaving a C-contact in each endpoint bag. The four bags have the four rim
edges from the two triangles and the two split edges. The third path is
a disjoint connected hub meeting all four bags through triangle edges.
Its one C-contact completes the five C-contacts. Every core bag contains
a triangle terminal adjacent to v, and v contacts C through a port.
These are seven connected disjoint original-host bags with all required
contacts of K2 joined to W4. No virtual edge or independently owned root
is substituted for an actual contact.

If an actual rim diagonal is additionally present, the core has at most
one missing rim edge. The possible C--hub omission has disjoint ends
from that edge, so the stated weaker certificate also gives Q.

Finally, H contains the six terminals. If D had size at most five,
deleting D in the six-connected F would leave both C and a vertex of
H-D, a contradiction. Thus the boundary lower bound is valid even when
considering the possibility H=D.

## New diagonal certificate and the five-vertex separator

The new conclusion quantifies over every linkage in the same H. Vitality
makes each path induced: a chord would give another linkage omitting an
internal vertex. Since the linkage spans H, its contact counts sum to
`|D|>=6`. If all three counts are positive and the original terminal
certificate does not apply, they therefore have the form `(h,1,1)` with
`h>=4`.

For a cross-edge from u before the last heavy contact l to w after the sole
light contact t_i, an edge split after the later of u and f and before l
exists. Both heavy halves retain C-contacts. A split between t_i and w
leaves the light A-half contacted, and its B-half contains w. This remains
valid when u or a chosen contact is a path endpoint.

The seven bags are v, C, the four endpoint halves and the untouched third
path. Triangle edges and split edges supply the rim and its hub contacts;
the cross-edge adds the heavy-A to light-B diagonal. Every core bag meets
v, C meets v, and the hub meets C. The only possible omissions are
heavy-B to light-A and C to light-B. Their endpoints are disjoint, giving
the required Q model without combining different allocations. Reversing
both path orientations proves the symmetric exclusion.

Consequently each vertex in the open heavy interval `Z=P(f,l)` can meet
either light path only at its sole contact. Inducedness excludes further
exits along the heavy path. Every C-neighbour lies in Z or among
f,l,t_1,t_2, and the spanning conclusion leaves no other H vertices.
Thus the full G-boundary of `C union Z` is contained in
`{v,f,l,t_1,t_2}`. All five lie outside `C union Z`. Each light
path has distinct A and B endpoints, at most one of which equals its
sole contact; a light endpoint therefore survives outside both the boundary
and `C union Z`. Seven-connectivity gives the claimed contradiction.
Every linkage in H must have a path anticomplete to C.

## Tail-switch ownership and remaining scope

Orient both paths from A to B. The proposed crossed edges produce the paths
`P[A,p] + pq + P'[q,B]` and
`P'[A,q'] + q'p' + P[p',B]`, with the third path unchanged.
They have distinct terminal endpoints and disjoint vertex sets. The only
omitted vertices are the two stated open intervals. Vitality forces those
intervals to be empty, so both old endpoint pairs are consecutive. The
old path edges then give the inverse switch, and no root, vertex or contact
with C is silently lost.

If one old path misses D while the other's contacts occur on both new paths,
the number of contacted paths increases by one. This contradicts the chosen
maximum. The source does not infer that an appropriate crossed pair exists,
or that a path contact can be moved across it without this condition.

## Simultaneous switches and straddlers

The seven bags are v and the two endpoint halves of each path. The P0
halves and v form a triangle. Each P0 half contacts the other same-end
halves through the corresponding terminal triangle, and the opposite-end
halves through the stated crossed edges. Every half contacts v through
its terminal. The four halves on P1,P2 form a cycle using their two split
edges and the A- and B-triangle edges. All bags are connected and disjoint,
and their contacts therefore contain `K3 join C4=Q`. C is unused.

For the subsequent bound, the two sides of an edge pq are the disjoint
path portions ending at p and starting at q, including those endpoints.
Suppose two vertices w,w' occur in that order on another path and each
contacts both sides. Choose a left-side neighbour l of w' and a right-side
neighbour r of w. These two edges form a reversed pair. The earlier switch
argument forces l,r and w,w' to be consecutive. Since `l<=p<q<=r`, this
means l=p and r=q, giving exactly the required inversion cell.

Three straddlers on one path would force its first and third to be
consecutive, which is impossible. Two on each of the other paths give the
simultaneous-switch terminal above. Thus at most three straddle in total.
When P0 misses C, spanning H leaves only the other paths, C and v outside
P0. C contributes no straddlers, so the full G bound is at most four.
This is an upper bound, not a claim that an inversion or separator exists.

## One contacted path: transition cycles, degrees and ears

This section assumes the maximum contacted-path count is one. It does not
apply its stronger degree conclusions to a linkage in the two-contacted-path
case. Every vertex is used by the fixed flow and is vital, so no SCC contains
both copies of a vertex. Each minimum cut meets each of the three fixed paths
once. Consequently a transition replaces one current vertex by its immediate
successor on each changed path; skipping a vertex would put both its copies
in that SCC. The SCC therefore consists exactly of the departing out-copies
and arriving in-copies.

If the A end of the contacted path missed C, all three A roots would miss C.
The first transition fully processes a nonempty set consisting only of A
roots. Residual closure confines their H-boundary to the new three-cut, while
v covers their only other possible G-neighbour outside H. The nonempty C
survives outside this boundary of size at most four. The last-transition
argument is dual: its wholly unprocessed set is a nonempty subset of B,
with boundary in the old three-cut and v. Thus both ends of P contact C.

The stated internal residual arcs are exhaustive. A used matching edge has
both its forward residual arc and its reverse residual arc, so contracting
each matching pair preserves strong connectivity on the changed path indices.
If another path changes with P, a directed cycle of length at least two
through P exists. Its cross-edges permute the fixed, disjoint suffixes after
the cut, preserving all vertices and a permitted free endpoint pairing.
The two pieces of P retain its two contacted ends on distinct new paths.
This contradicts the one-contact maximum. Every transition changing P
therefore changes only P.

For an internal vertex w, consider the set of vertices with both copies
processed between the cut just after its entry and the cut just before
its exit. P is stationary, so those vertices lie on the two uncontacted
paths. They cannot be terminals: A in-copies were already present initially,
and B out-copies never enter the chain. They consequently miss C and v.
For an outside neighbour, residual closure places its in-copy in the later
cut and its out-copy outside the earlier cut. Unless it belongs to the
processed set, it lies in one of the two boundary three-cuts. Their union
has at most five vertices because both contain w, and is disjoint from the
processed set. Seven-connectivity forces that set to be empty. Either other
path can therefore advance at most once during w's lifetime.

The neighbour bound additionally uses the cut immediately before w's entry
and immediately after its exit. An already processed neighbour at the former
cut, or a still unprocessed neighbour at the latter, would violate residual
closure along its edge with w. Those singleton transitions leave both other
path positions unchanged. Thus w has at most two neighbours on each other
path, plus its two neighbours on the induced P. It misses v, so degree at
least eight implies at least two distinct C-neighbours.

Finally take a noncut c of C different from both ports. Its H-neighbours all
lie on P. If their extreme positions have distance at least three, replacing
that interval by the two-edge path through c releases at least two internal
P vertices. Each has a C-neighbour different from c. The connected set C-c
still contains both ports, so adjoining the released interval gives a larger
port component. This is a valid linkage avoiding x,y and contradicts the
original maximisation. Empty or singleton neighbour sets satisfy the span
bound trivially. Hence there are at most three H-neighbours in three consecutive
P vertices. Since c also misses v, its C-degree is at least five.

No gap was found in the current scoped claims. The ear proof specifically
uses a noncut nonport vertex; it does not license consuming a port, deleting
a separating vertex, or a multi-vertex ear whose surviving attachments may
be lost. A zero-contact path and the larger-block allocation remain. The
global reroute through C, both exterior chromatic cases, and the complete
two-triangle construction remain open.
