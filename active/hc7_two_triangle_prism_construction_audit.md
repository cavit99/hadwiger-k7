# Independent audit of the maximal-component construction

**Verdict: GREEN for the stated normalisation and conditional terminal certificates.**

This separate internal audit does not establish the missing global rerouting,
either exterior chromatic case, C19, C21, HC7 or comparative significance.
The source remains an active construction draft, not a promoted global proof.

**Source:** [the construction](hc7_two_triangle_prism_construction.md).

**Exact source SHA-256:**
`137d12c34cf2f477b80498c254c9a089d2985f7ac4b868800871924d9d70fb31`.

**Reviewer and scope.** On 14 September 2026, `plan_certificate_compute`
independently reconstructed the maximality and residual-cut argument before
reading the written source, then checked the complete pinned revision. The
reviewer did not originate this construction. The only requested clarification
was to specify the two split-network arcs for each undirected edge explicitly;
the pinned source includes it. No finite search is a premise of this audit.

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
considering the possibility H=D. Its total size does not supply the
required distribution among paths. The source leaves contact balance,
rerouting through C, and any decreasing reduction explicitly unproved.
No unresolved gap was found in the pinned normalisation or either
conditional certificate; the global construction remains open.
