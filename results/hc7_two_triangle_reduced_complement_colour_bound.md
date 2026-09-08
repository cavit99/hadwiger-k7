# A five-chromatic remainder after reserving three neighbours

**Status:** written proof; separate exact-source internal audit recorded beside it.
This is a chromatic lower bound, not a closure of the two-triangle case.
All graphs are finite and simple. Write Q for K7 with two independent
edges deleted.

**Theorem.** Let G be seven-connected, have minimum degree at least eight,
be Q-minor-free, and satisfy chi(G)>=7. Suppose d(v)=8 and

`N(v)=A dotcup B dotcup {x,y}`,

where A and B are triangles and xy is an edge; extra edges are allowed.
For every a in A adjacent to neither x nor y, put

`M=G-({v} union B union {a,x,y})=G[W union (A-{a})]`,

where `W=V(G)-N[v]`. Then `chi(M)>=5`. At least two choices of a are
eligible. No proper-minor colouring hypothesis or previously selected
minor model is required.

## Input

We use [contraction closure](../active/hc7_companion_contraction_closure.md),
SHA-256 `ab7ce8adc265c0e2300fb2d0c3367b972f6fc828163ee8c4ffb5d950c987ccb4`,
and its [separate internal audit](../active/hc7_companion_contraction_closure_audit.md),
SHA-256 `26b2f5ad7226c7bb3f194cac8523f043d7ae6ca955036249f04ddc9fb6d94394`.
Theorem 1 excludes a literal K5-minus-edge after any edge contraction.
Corollary 6 gives the same exclusion after contracting any connected
set of at most three vertices under the present seven-connectivity.
Corollary 3 says that outside a literal four-clique R every vertex has
at most two R neighbours; if w has two, every outside neighbour z of w
has its R-neighbour set contained in that of w.
No additional external theorem is invoked.

## 1. One B label near each reserved vertex

Put `R={v} union B`. For each `z in {a,x,y}`, define

`S_z=(N_G(z) intersect B) union
     union_{w in N_G(z) intersect V(M)} (N_G(w) intersect B)`.

Then `|S_z|<=1`. Otherwise choose a connected set C consisting of z
and at most two of its M neighbours which together contact two distinct
B vertices. The set C lies outside R and also contacts v through z.
Contract C. The four original R vertices remain distinct and retain
their clique, while the merged vertex has at least three R neighbours.
These five vertices contain a literal K5-minus-edge, contrary to the
input for connected sets of order at most three. All preimages are fixed;
no excluded clique vertex was contracted.

Also each of a,x,y has at most one B neighbour, since it already sees v
in the four-clique R. At least two vertices a in A miss both x and y:
if the union of the A-neighbours of x and y had size at least two,
contracting xy would give three contacts to the untouched four-clique
`{v} union A`, again contradicting Theorem 1.

## 2. Recolour one class of a hypothetical four-colouring

Suppose M has a proper four-colouring, allowing empty classes. Write
`A-{a}={A1,A2}`. Their literal edge gives distinct colours. Choose a
colour class I containing neither root, and give the other three classes
the colours 1,2,3. In particular every vertex of I lies in W and misses v.

Colour the three B vertices with a disjoint palette Omega={4,5,6}.
For `w in I union {a,x,y}`, let L(w) be Omega minus the colours on its
B neighbours. We will colour this induced graph from these lists using
only two Omega colours on a,x,y. Its only edge outside I is xy, and I
is independent. The lists of a,x,y each have size at least two.

Every I vertex has at most two B neighbours. If it has two, it is
anticomplete to {a,x,y}: an edge to any of these vertices would violate
Corollary 3 at R, since that vertex sees v and the I vertex does not.
Thus an I vertex with a one-element list causes no conflict. A vertex
with no B neighbour has three available colours, so retains a colour
after at most two colours are assigned to a,x,y.

Choose `Bi in B-(S_x union S_y)` and let P be the two Omega colours
other than Bi's colour. First suppose x,y can receive distinct colours
in P from their lists. Give a any colour in `P intersect L(a)`, which
is nonempty. An I vertex with exactly one B neighbour could now have
its two-element list exhausted only if that list equals P and it sees
both assigned colours. Its B neighbour would then be Bi. Since a alone
cannot supply two colours, the vertex would meet x or y, contradicting
the choice of Bi. Hence all I lists can be coloured independently.

It remains to handle failure of that assignment to x,y. Two nonempty
subsets of a two-set have no distinct representatives exactly when both
are the same singleton. Here this says that x and y both have the same
literal B neighbour Bk, whose colour lies in P. We handle this case with
the new pair `P'=Omega-{colour(Bk)}` instead.

The vertices `R'={v,Bk,x,y}` form a literal four-clique. Give x and y the
two colours in P' distinctly, and give a any allowed colour in P'. Consider an
I vertex w whose sole B neighbour is Bk. It cannot meet both x and y,
which would give three R' neighbours and a literal K5-minus-edge.
Nor can it meet a and x: it would have exactly the two R' neighbours
Bk,x, whereas its outside neighbour a sees v, contrary to Corollary 3
at R'. The case a,y is symmetric. Thus w meets at most one of a,x,y
and retains an available colour. An I vertex with a different sole
B neighbour misses both x and y, since S_x and S_y already contain Bk
and each has size at most one. It too sees at most one assigned colour.
The zero- and two-B-neighbour cases were settled above. This colours I
in the exceptional case as well.

In either case, the lists prevent conflicts with B, and the disjoint
palettes prevent conflicts with the other three M classes. We have a
proper six-colouring of G-v. Among colours 1,2,3, at least one is absent
from A1,A2; every other neighbour of v has an Omega colour. Give v that
absent colour, contradicting chi(G)>=7. Therefore chi(M)>=5. QED

The proof applies before any helper normalization, including when no
zero-port model has been chosen. It neither produces a rooted five-clique
in M nor preserves connectivity or minimum degree after the displayed
deletion. The remaining simultaneous Q construction is unproved.
