# Closing the three-contact branch of the split-clique neighbourhood

**Status:** written proof, with a
[separate internal audit](hc7_split_clique_three_contact_audit.md).
This closes the branch specified below, not the whole split-clique
neighbourhood case or Hadwiger's conjecture for seven.

## Statement

Let G be a finite simple graph which is not six-colourable and whose every
proper minor is six-colourable. Suppose a vertex u has neighbourhood
`P dotunion D`, where P induces a triangle, D induces a four-clique, and
P is anticomplete to D. Choose `p in P` and a proper six-colouring of
`G/up`, with the contracted vertex coloured six. Let I be the other
vertices of colour six, put

`K = G - ({u,p} union I)`,

and let X be the component of `K-D` containing the edge `A=P-{p}`.
If X misses a vertex of D, then G contains a K7 minor.

Consequently, in a K7-minor-free graph satisfying these hypotheses, X
contacts all four D vertices for every choice of p and every such colouring.
No maximal choice of X, connectivity hypothesis or induction is required.

The proved input is the repository's [audited bipartite contractibility
theorem](bipartite_contractibility_via_matroid_reduction.md):
every scheme for a finite bipartite target contains its fully rooted minor.

## Proof

The set I is independent, lies outside `N[u]`, and is anticomplete to p.
The quotient colouring restricts to a five-colouring of K. In every
five-colouring of K, the set `A union D` uses all five colours: otherwise
colour p and I with six and give u a colour missing from `A union D`,
obtaining a six-colouring of G.

Fix the original colouring, relabelling colours so that D uses one to
four. The edge A uses colour five and one other colour c. If X missed
two vertices of D, choose the colour j of one of them with `j != c`.
Interchange five and j throughout X. This is proper: all neighbours of X
outside X lie in D, and no such neighbour has colour five or j. The
interchange removes colour five from A, contrary to the preceding
paragraph. Thus X misses exactly one vertex d of D.

Write `Q=D-{d}` and give Q colours one, two and three, and d colour four.
The same interchange of four and five throughout X shows that A must use
exactly colours four and five. Denote its vertices by a and b, respectively.
This conclusion holds in every five-colouring of K with these fixed D
colours.

For each `q_i in Q` of colour i, there is an a--q_i path using only colours
four and i inside `K[X union Q]`. Indeed, if their two-colour components
were distinct, interchange the component containing a. The interchange
extends to K: the whole outside neighbourhood of X is Q, and q_i is the
only Q vertex of either colour, so an affected vertex cannot have a
same-coloured neighbour outside that component. It changes A's colours
to i and five, contradicting the forced pair four and five. The same
argument gives a b--q_i path using only colours five and i. Choose these
six paths simple.

Now lift the original quotient colouring to `G-u` by colouring p six.
For each `q_i in Q`, p and q_i lie in the same component of the subgraph
with colours six and i. Otherwise, interchange the component containing
p. No other vertex of `N(u)` has colour six, and q_i is its only vertex
of colour i: a and d have colour four, and b has colour five. The
interchange would therefore leave colour six absent from `N(u)`, allowing
u to be coloured six. This contradicts the hypotheses. Choose a simple
p--q_i path in this two-colour component. It avoids d, a and b because
none has colour six or i.

The nine paths just chosen lie in `G-{u,d}` and form a K3,3 scheme with
shores P and Q. To check the full scheme condition, all six prescribed
roots have distinct colours. Each path uses only its two endpoint
colours, so no other root is internal to it. At any common vertex of
any nonempty collection of paths, its colour identifies one prescribed
root, and every path in that collection has that root as an endpoint.
Thus the corresponding target edges share that endpoint.

Bipartite contractibility supplies six pairwise disjoint connected bags,
each containing its prescribed root in `P union Q`, with every P--Q
contact. The actual triangle edges of P and Q supply the remaining
contacts between these six bags, giving K6. They all lie in `G-{u,d}`.
The singleton bag `{u}` is adjacent to each through its prescribed root,
so the seven bags form a K7 model. This proves the statement.

## Scope of the construction

All contractions implicit in bipartite contractibility lift through its
fixed disjoint preimages; the six original roots remain in their bags.
The initial contraction up is used only to obtain a colouring, and no
minor is assumed to inherit criticality. The argument is direct, so it
needs no decreasing induction parameter.

The remaining branch has X adjacent to every vertex of D for every p and
quotient colouring. This proof does not supply the two compatible
D-full, P-meeting bags needed to close that branch.
