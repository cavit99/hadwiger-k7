# Universal rainbow roots do not force a prescribed singleton bag

**Status:** explicit counterexample with a written proof and a
[separate internal audit](critical_colour_singleton_root_audit.md).

The failed inference is: if `chi(F)=5`, every five-colouring makes five
prescribed vertices `L union {x}` rainbow, and deleting the entire colour
class of x leaves a four-chromatic graph, then F has a rooted K5 model
at those five vertices with the x bag equal to `{x}`. This inference is
false, even when L induces a K4.

## Construction

Take disjoint four-vertex cliques L and Q and two further vertices x,y.
Add every edge from x to Q and every edge from y to `L union Q`.
There are no other edges: in particular x,y are nonadjacent and there
are no L--Q edges. The prescribed roots are the four vertices of L and x.
Write `J={x,y}` and `K=F-J`.

## Colouring and minor claims

**Claim.** The graph F has chromatic number five, every five-colouring
makes `L union {x}` rainbow, and J is an entire colour class in every
five-colouring. Moreover `chi(K)=4`, and both L and `N_K(x)=Q` use all
four colours in every four-colouring of K. Nevertheless no rooted K5
model at `L union {x}` has singleton x bag.

**Proof.** Colour both cliques with the same four colours and give x,y
a fifth colour. Conversely `Q union {x}` is a K5, so `chi(F)=5`.
In any five-colouring, Q uses four colours. Both x and y see every Q
vertex, so both receive the unique remaining colour. Every L vertex
sees y; the four vertices of L therefore use the other four colours.
Thus the five prescribed roots are rainbow and J is exactly the
colour class of x. Deleting J leaves two disjoint K4s, proving
the assertions about K, L and `N_K(x)`.

If the x bag were singleton, each of the other four bags would contain
its prescribed L root and a neighbour of x, hence a Q vertex. Every
L--Q path in `F-x` passes through y. Each such connected bag must
therefore contain y, contrary to their pairwise disjointness. QED

There is, however, a full rooted K5 model: take the four singleton L
bags and the fifth bag `{x,y} union Q`. The fifth bag is connected
through Q and sees every L bag through y; the six L--L contacts are
literal edges. Thus allowing the x bag to expand repairs the obstruction.

## Scope

This refutes the prescribed-singleton inference even with the universal
five-colouring quantifier, a fixed independent class J, and four
pairwise adjacent remaining roots. It does not refute fully rooted K5
contractibility or an extension whose x bag may expand. The example
does not retain the connectivity, degree or excluded-minor hypotheses
of the actual seven-contraction-critical two-triangle case, and is not
asserted to be a minimum counterexample to a scheme theorem. A proof
for that case must retain those hypotheses or control the expanded
x bag's use of reserved vertices.
