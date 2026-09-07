# Independent audit of the degree-eight neighbourhood triangle theorem

**Date:** 7 September 2026.

**Verdict:** GREEN for the exact written statements. This is a separate
internal mathematical audit, not external peer review.

**Audited source:** [the neighbourhood triangle theorem](hc7_degree8_neighbourhood_triangle.md),
SHA-256
`907384c665975c47f7850ee49da2d7f389802b077837c4285a3f00a81f5ef824`.
I read the complete source and independently checked its strongest
contraction and lifting inferences. No finite enumeration was used.

## 1. The elementary eight-vertex argument

The contradiction hypothesis excludes a `K_{2,3}` subgraph because
contracting one of its edges gives a four-vertex diamond. Triangle-freeness
makes every neighbourhood independent, so the maximum degree is at most
three. The elementary independent-three-set argument on six vertices
also correctly excludes degrees zero and one in the eight-vertex host.

For a degree-two vertex `t`, its five nonneighbours induce a triangle-free
graph of independence number at most two. The source proves, rather than
assumes, that this graph is `C_5`: its degrees are all two. The two
neighbours `a,b` of `t` are independent. Their common nonneighbours in
the five-cycle must consequently form a clique and have order at most
two. If there are two, they are consecutive. In every case the covered
cycle vertices contain a three-vertex path. Contracting the actual
connected triple `{a,t,b}` therefore supplies the apex of a diamond
on that path. The contracted triple is disjoint from its three vertices.

In the cubic case, the radius-two count is valid: without a triangle or
a four-cycle, a vertex, its three neighbours and their six other
neighbours would be ten distinct vertices. For the resulting four-cycle,
the four outside neighbours are distinct. Adjacent repetitions would
make a triangle, and opposite repetitions would give the already excluded
`K_{2,3}`. Thus the independent-set test on `{a,c,B,D}` forces `BD`.
The set `{a,b,B}` is connected, and the five listed original edges
give exactly the required diamond contacts on `w,c,d,D`. These are four
distinct quotient vertices. Extra edges would not invalidate the subgraph
conclusion.

This checks all degree cases and the exact existential conclusion:
some connected set of order at most three has a quotient containing a
diamond. It is not a claim about an arbitrary chosen contraction.

## 2. Connected-triple input and the critical-host lift

The source pins Corollary 6 of
[the connected-set contraction closure](hc7_companion_contraction_closure.md)
at SHA-256
`ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`.
I independently checked the part used here, including its underlying
charge identity. For a connected set `C`, the contribution of
`C` together with two unmerged universal vertices of a proposed
quotient `K_5^-` is at least `2q+4+b-D`. The condition `D<=b+3`
therefore gives a strict contradiction to total degree excess `2q`.

For a connected triple, three common outside neighbours would contain
`K_{1,2,3}` with it; an edge contraction between the parts of orders two
and three yields `K_5^-`. The one-edge exclusion forbids this, so
`D-b=n_3-n_1<=2`. A cut of at most four in the triple quotient lifts
to at most six original vertices, establishing five-connectivity from
the original seven-connectivity. These facts verify every hypothesis
of the connected-set charge result; no quotient criticality is needed.

The application contracts `C` wholly inside `N_G(v)`, so `v` survives
as a distinct vertex. Every selected vertex of the quotient neighbourhood
is adjacent to `v`, including the merged vertex. A diamond on those
four vertices, together with the singleton `v`, is a literal `K_5^-`
in the same quotient. This directly contradicts the pinned exclusion.
There is no lifting of an arbitrarily rooted model and no reuse of an
owned vertex. Host order strictly decreases whenever a nontrivial
contraction is used; the proof makes no inductive claim on the quotient
class.

## 3. Scope and corrections

No substantive correction was needed after the cold mathematical check.
The final revision adds the precise dependency hash and final audit-status
wording. The conclusion that every applicable degree-eight vertex belongs
to a literal `K_4` is proved, including the critical-host specialization
using the previously established minimum degree and independent-four-set
star-contraction argument.

No unresolved gap remains in these stated implications. They do not give
the further construction from that four-clique to `K_7^=` or `K_7^-`,
preserve chromatic criticality after contraction, prove a universal
six-colouring theorem, or establish completion or comparable significance
for the user's global objective.
