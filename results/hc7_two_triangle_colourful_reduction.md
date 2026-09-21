# Colourful unions of two triangles: reduction to four-connectivity

**Status:** written conditional reduction, with a [separate internal audit](hc7_two_triangle_colourful_reduction_audit.md). This is a
conditional reduction in the [degree-seven laboratory](../active/hc7_c21_rooted_density_construction.md#4-what-remains-towards-hc7).
It does not prove the remaining four-connected statement, either exceptional
degree-seven case, or `HC_7`.

All graphs are finite and simple. A set is **colourful** if it meets every
colour class of every proper five-colouring. A marked minor has fixed,
pairwise disjoint connected preimages, with an original marked vertex in
each marked preimage. A model meeting the new marks therefore lifts to a
model meeting the original marks.

## 1. Statement and invariant

Let `H` be five-colourable, and let `T=P dotunion Q`, where `P,Q` are
disjoint literal triangles and `T` is colourful. Edges between the two
triangles are allowed. Then at least one of the following holds:

1. `H` has a `K5` model with all five bags meeting `T`;
2. `H` has a four-connected marked minor `H'`, with two disjoint literal
   triangles `P',Q'`, such that `H'` is five-colourable and
   `T'=P' union Q'` is colourful. Every vertex of `T'` has a different
   connected preimage containing an original vertex of `T`.

Every nonterminal replacement below strictly reduces vertex order. The
invariant consists of ordinary five-colourability, colourfulness, the two
literal triangles when six marks remain, and fixed disjoint marked
preimages. Chromatic criticality is neither assumed nor inherited.

Use the palette `{0,1,2,3,4}`. A **permitted** colouring gives all marked
vertices colours in `{1,2,3,4}`. Colourfulness is equivalent to the absence
of a permitted colouring. In particular, a five-colourable colourful pair
has chromatic number five, and it cannot have fewer than five marks.

## 2. The five-mark exit and preliminary reduction

The existing [three-connected marked-minor theorem](colourful_five_wheel.md#a-three-connected-marked-minor)
reduces an arbitrary colourful pair to a three-connected one. Its proof
retains ordinary five-colourability, absence of permitted colourings,
disjoint marked preimages and strict decrease. It never increases the
number of marks.

If all six marks survive a cut of order at most two in that proof, both
triangles survive as literal triangles. Indeed, a triangle cannot meet
both open shores of a separation. A triangle meeting the discarded open
shore lies wholly in that closed shore, and all three of its original
marks would then have to survive in at most two separator preimages.
That would reduce the total number of marks. Thus neither triangle has a
vertex in the discarded open shore when six marks survive. Identification
of two marked separator vertices would likewise reduce the number of
marks; the remaining operations retain the literal triangle edges.

Here and in subsequent reductions, five surviving marks are terminal.
Choose one original `T` representative from each of their five disjoint
preimages. They form a three-plus-two distribution between `P,Q`. The
edges of the original three-set and the edge of the original two-set can
be retained between the corresponding preimages. If a reduction deleted
one of these edges, restore it in the marked minor: this is a valid minor
with the same preimages, and preserves five-colourability because all five
marks have distinct colours in every proper five-colouring.

Fix a five-colouring. Every missing pair of marked vertices lies in one
bichromatic component; otherwise a component interchange makes two marks
equal and omits a colour from the marked set. The missing-edge graph on
the marks is a subgraph of `K_{3,2}`, so it has at most six edges.
Kriesell--Mohr, [*Kempe Chains and Rooted Minors*, Theorem 7](https://arxiv.org/abs/1911.09998),
says that every five-vertex graph with at most six edges has property `(*)`.
Its precise rooted-certificate application is already used in
[the matching-bridge theorem, Theorem 3.5](hc7_degree7_matching_bridge_bundle.md).
Apply it to these missing pairs in the one fixed colouring. The resulting
five rooted bags, together with the retained literal edges, form a `K5`
model. Its fixed preimages lift it to the original graph.

Thus after every reduction we may stop with this model, or assume that
exactly six marks remain as two disjoint literal triangles and that the
graph is three-connected.

## 3. Rooted triangle carriers across a three-cut

Let `S` be a three-vertex cut of the current three-connected graph `H`.
Take proper closed shores `A,B` with `A intersect B=S`. Each component
of `H-S` is adjacent to every vertex of `S`.

Suppose a literal triangle `Q` lies in `B`. There are three disjoint
`S`--`Q` paths inside `B`, including the trivial paths at `S intersect Q`.
For completeness, delete the common vertices first. Failure of the
remaining linkage would, by vertex Menger, give a set of fewer than
`3-|S intersect Q|` vertices separating the remaining ports from the
remaining triangle vertices in that shore. Together with the common
vertices it would be a cut of `H` of order at most two: a surviving
triangle vertex could not reach the nonempty opposite open shore without
passing through a surviving port. This contradicts three-connectivity.

The paths end at distinct triangle vertices. Their vertex sets are three
disjoint connected port carriers, pairwise adjacent through the literal
triangle edges, and each containing a different original triangle mark.
Delete other vertices of the opposite open shore and contract the
carriers. This realises the clique completion on `S`, with all three
ports marked, while keeping the retained open shore unchanged.

For any partition `pi` of `S`, carriers belonging to the same block can
be merged: their triangle edges make their union connected. Distinct
block carriers remain adjacent. Thus this same construction realises the
quotient whose ports are the blocks of `pi`, with a clique on those
ports, and supplies an original opposite-triangle mark to every port.
These preimages avoid the retained open shore and remain pairwise
disjoint. If an ordinary five-colouring `f` induces `pi` on `S`, its
restriction to the retained shore colours the quotient properly. Edges
added between different blocks join different colours; edges within a
merged block become loops and are discarded. No colouring is expanded
through a contracted carrier.

## 4. A three-cut with the triangles on opposite shores

Suppose neither closed shore contains all of `T`. Since a triangle cannot
meet both open shores, orient the separation so `P subseteq A` and
`Q subseteq B`, with each triangle meeting its designated open shore.
Fix an ordinary five-colouring `f` of `H`, and let `r` be the number of
colours on `S`, where `1<=r<=3`.

Construct one quotient from each retained shore by the carriers of
Section 3, merging precisely the ports equal in `f`. Mark every quotient
port and every remaining vertex of the retained triangle. Each quotient
is five-colourable by `f` and has at most `3+r` marks.

Both quotients cannot have permitted colourings. Such colourings expand
only their separator blocks back to `S`, giving proper colourings of the
two original closed shores with the same equality partition on `S`.
Every port colour is old. A permutation of the four old colours aligns
these colours; glue the two shore colourings. Every original marked
vertex is old, contradicting the colourfulness of `T`.

Consequently at least one quotient is colourful. If `r=1`, both quotients
have at most four marks, an impossibility. If `r=2`, the colourful quotient
has exactly five marks and Section 2 gives the terminal `T`-meeting `K5`.
When there are five marks, its retained triangle and its two adjacent
ports are disjoint, so the required three-plus-two root edges are literal.

If `r=3`, the selected colourful quotient has the retained triangle and
the separator triangle as its marked set. If these triangles overlap,
there are at most five marks and Section 2 applies. Otherwise it is a
smaller pair in the same two-triangle class. Cross edges between the
triangles are harmless and are retained. This covers cuts meeting `T` as
well as cuts disjoint from `T`.

## 5. A three-cut with all marks on one closed shore

It remains that all marks lie in one closed shore. Choose an unmarked
component `D` of `H-S`, and put `B=H[D union S]` and `A=H-D`.
The component is nonempty and full at `S`. Fix an ordinary five-colouring
`f` of `H`.

If `f(S)` has one colour, contract the connected set `D union S` to one
port. If it has two colours, contract `D` together with the equal-coloured
pair of ports, retaining the third port. Fullness makes the two quotient
ports adjacent. In either case retain exactly the images of the old
marks; there are no marks in `D`. The restriction of `f` colours this
proper minor. A permitted colouring of it expands on `A`, and an ordinary
colour permutation of `f|B` aligns the selected separator partition and
extends over `D`. There is no condition on colours of vertices in `D`.
This would be a permitted colouring of `H`. Thus the minor remains
colourful. If two marks merged, Section 2 applies; otherwise the two
literal triangles survive. No two vertices of the same triangle can have
been identified, since they had different colours in `f`.

Suppose now that the three colours on `S` are distinct. If `B` has an
`S`-rooted triangle minor, use its carriers to realise `A+K_S`, retaining
the old marks. The restriction of `f` is a proper five-colouring. Every
permitted colouring would extend over `D` by permuting `f|B` to match the
three distinct port colours. Hence this smaller marked minor is colourful
and retains the two literal triangles.

If `B` has no `S`-rooted triangle, then `D` is a single vertex of degree
three in `H`. This is the degree-three alternative in the block-cut-tree
proof of the existing [rooted triangle lemma](hc7_c21_rooted_density_low_degree_reduction.md#a-rooted-triangle-lemma).
Here is the relevant argument without its unnecessary degree-four
assumption. The median of the three root locations in the block-cut tree
cannot be a block: three distinct attachment vertices in that block have
a rooted triangle, which lifts along disjoint root arms. The median is
therefore a cutvertex `z`, and every component of `B-z` contains at most
one port. Any nonroot in such a component, after removing its possible
port, would be separated in `H` by that port and `z`, contradicting
three-connectivity. All nonroots therefore lie in `{z}`; since `D` is
nonempty, `D={z}`. Fullness gives `N_H(z)=S`.

Delete `z`. Every five-colouring of `H-z`, permitted or otherwise,
extends over this unmarked degree-three vertex. Thus `H-z` is still
five-colourable and colourful on the same two literal triangles. This
again strictly decreases order.

## 6. Termination, lifts and remaining obligation

In each three-cut step a nonempty opposite open shore disappears. The
retained graph has at most three quotient ports and fewer vertices than
the original graph. Deleting the unmarked degree-three vertex is also
strict. Apply the three-connected marked-minor reduction again if needed;
it cannot increase order. Stop at five marks as in Section 2, or continue
with six marks and the two literal triangles. Vertex order is a
well-founded parameter, so the process terminates at a four-connected
pair unless it has already produced the desired model.

All contractions have explicit disjoint connected preimages. At a port
replacement the preimage lies in the deleted shore together with its
assigned old separator vertices; it avoids the retained open shore.
Composing preimages preserves connectedness, disjointness and one
original mark in each marked preimage. Every eventual marked model
therefore lifts. Ordinary five-colourability is checked anew at each
operation and is never inferred from minor closure of colourability.

The remaining statement is that every four-connected five-colourable
graph with a colourful union of two disjoint literal triangles has a
`K5` model meeting that union. It is not proved here. In particular, an
ordinary `K5` minor or a model rooted at just one triangle does not yet
settle the marked model requirement.

## 7. Application to the exceptional critical host

Let `G` be seven-chromatic, with every proper minor six-colourable and
no `K7` minor. Suppose `N_G(u)=P dotunion Q dotunion {r}`, where `P,Q`
are triangles and `r` is adjacent to every vertex of `P union Q`.
Choose any six-colouring of `G-u`, and let `I` be the entire colour class
containing `r`. Put `K=G-u-I` and `T=P union Q`.

The graph `K` is five-colourable, and `T` is colourful in every
five-colouring of `K`. Indeed, if some such colouring used at most four
colours on `T`, give the independent set `I` a sixth colour and give `u`
a colour missing from `T`. Since `I intersect N(u)={r}`, this would
six-colour `G`. The same argument rules out a four-colouring of `K`.

A `T`-meeting `K5` model in `K` extends to `K7` by the singleton bags
`{u},{r}`: each singleton sees every old bag at an actual vertex of `T`,
and `ur` is an edge. The first outcome of Section 1 is therefore
impossible. The second gives a four-connected, five-colourable marked
minor of `K`, with a colourful union of two disjoint literal triangles
and disjoint preimages at the original six roots. Any marked `K5` model
in that minor would lift and give the same contradiction.

This application covers both possible values five and six of
`chi(G-{u,r})`. It does not assert that `K` or the marked minor retains
the connectivity or criticality of `G`. The unproved four-connected
statement would close this entire neighbourhood case; the present
reduction does not.
