# A local exchange between two degree-two scheme vertices

**Status:** written proofs with a separate internal audit beside this source. This is a
local reduction in the K5 construction, not a proof of K5 contractibility
or of the remaining Hadwiger target. No novelty claim is made.

All graphs are finite and simple. An H-scheme consists of one simple path
for each edge of H, joining its two prescribed roots and containing no
other root. Every nonempty collection of paths meeting at a vertex has
a common target endpoint. A properly coloured scheme has a proper colouring by V(H),
each root having its own colour and each path using only its two endpoint
colours. Work in the union of these paths and all prescribed roots R.
Assume every nonroot lies on at least two scheme paths.

## The exchange

**Lemma.** Let x,y be adjacent nonroots, each of degree two in G−R.
Write z for the other nonroot neighbour of x and w for that of y.
If z,w have the same colour, G has a root-preserving minor with at
least two fewer vertices containing a properly coloured H-scheme.
The vertices z,w may coincide. In particular, the lemma applies when
x,y lie in a nonroot triangle and have no other nonroot neighbours.

**Proof.** Write α,β for the colours of x,y and γ for the common colour
of z,w. These three colours are distinct by properness. Distinct scheme
paths cannot share an edge: the colours of its ends specify its unique
target edge. Each path through a nonroot uses at least one nonroot
neighbour, since its two neighbours have the same opposite colour and
only one prescribed root has that colour. Consequently x and y each
lie on exactly two paths, using one root and one nonroot neighbour on
each path.

It follows that x lies only on P(αβ),P(αγ), and y only on
P(αβ),P(βγ). If r_η denotes the root of colour η, then

`P(αβ) = r_β–x–y–r_α`,

and r_γ is adjacent to both x and y. Absorb y into the α root bag and
x into the β root bag, using the actual edges r_αy and r_βx.
These bags are disjoint and connected and contain only their own
prescribed roots. The edge xy gives their mutual contact; r_γy and
r_γx give their respective contacts with the γ root.

Replace P(αβ),P(αγ),P(βγ) by those three literal quotient edges.
Every other demand path avoids x,y, so it survives unchanged apart
from its root images. Give each new root vertex its root's colour,
retain just these paths and the other prescribed roots, and delete
unused material. The resulting paths remain properly coloured and
contain no foreign root. Any paths meeting at a vertex share that
vertex's colour as a target endpoint, so they form an H-scheme.

The two contractions reduce the host order by two, before any further
deletion. Their fixed preimages are {r_α,y} and {r_β,x}; all other
retained vertices have singleton preimages. Every rooted model of the
new scheme therefore lifts with the original roots, disjointness and
all required contacts preserved. QED

This exchange deliberately changes ownership across colours. In the
[ten-vertex example](../barriers/k5_scheme_full_colour_class_obstruction.md),
apply it to B,C and then D,E. The resulting model is precisely
`{a}, {b,C}, {c,B}, {d,E}, {e,D}`; the remaining vertex u is unused.

**Short consequence.** If every cyclic block of G−R is a triangle,
every H-scheme in G has a fully rooted H minor. Use the strong
root-preserving normalization recorded in
[Section 3 of the independent-set reduction](../results/general_scheme_independent_set_reduction.md)
to make every nonroot lie on at least two paths. This host class is
minor-closed: every block is an edge or a triangle, and deleting or
contracting an edge preserves that property. The normalized nonroot
graph has minimum degree at least two. A leaf block of any nonempty
component is therefore a triangle with two degree-two vertices (a
component consisting of a triangle also qualifies). Apply the lemma
and repeat normalization and reduction. Host order strictly decreases,
and the process ends with all demands literal. This observation is
only a consequence of the local exchange, not a separate research
direction.

The normalization input above is pinned to source SHA-256
`07fa0fc58284dba6f5ab180a64e92dd86f3829fd31494b8529f00fcaf7751e9f`
and its [adjacent audit](../results/general_scheme_independent_set_reduction_audit.md)
SHA-256 `f3b8137aec93dbf618a3c19a6f97b17fbb46a386a16cc7e6c9581927e271b76f`.
The local lemma itself needs no external theorem.

## A terminal with different outside colours

**Lemma.** In a properly coloured K5-scheme under the same normalization,
let adjacent degree-two nonroots x,y have colours α,β and other nonroot
neighbours z,w of different colours γ,δ. Assume these four colours are
distinct, and let ε be the fifth colour. Let Q be the z-to-r_α tail
of P(αγ), obtained by removing its initial segment
r_γ–x. Suppose Q meets P(βγ), and let t be its first such contact
when followed from r_α. If P(βγ)[t,r_γ] is disjoint from P(βε),
the host has a fully rooted K5 minor. When P(βε) is literal this
avoidance is automatic.

**Proof.** The degree-two argument above gives the edges
`r_βx, xy, yr_α, r_γx, r_δy`. Thus

`B_β={r_β,x,y}`

is connected and has literal contacts with r_α,r_γ,r_δ.

Starting at r_α, follow Q to its first vertex t on P(βγ), then follow
P(βγ) from t to r_γ. The contact t has colour γ and is not a root.
The resulting path is simple by the first-contact choice, avoids r_β,
and is disjoint from B_β. Retain it as the αγ demand on the remaining
four roots, together with their five other original demand paths.
All these paths avoid B_β, since x,y occur only on αβ,αγ,βδ.

These six paths form a raw K4-scheme, although the replacement path
need not be properly two-coloured. Its Q part inherits the original
intersection condition. Its P(βγ) part is disjoint from P(αδ),
P(αε),P(δε), whose target edges are independent of βγ. It can meet
P(γδ),P(γε) only at γ-coloured vertices. Hence every collection of
retained paths meeting the replacement path has a common K4 endpoint,
including collections of three or more paths. No foreign root occurs.

Set E=V(P(βε))−{r_β}. This is connected, contains r_ε, and is
disjoint from B_β. The new αγ path avoids E: its Q part is independent
of the original βε demand, and its other part avoids P(βε) by
hypothesis. The αδ and γδ paths also avoid E by independence.
Contract E to the ε root, and truncate each original αε,γε,δε path
at its first entry into E from its other root. Such an entry has the
old colour ε, so the truncations retain their two endpoint colours.
The six quotient paths still form a raw K4-scheme: their only new
shared vertex is the ε root, and the three paths not demanding ε
avoid it. The contraction has the fixed connected preimage E and
does not consume any other prescribed root.

The known contractibility of K4 gives four disjoint connected rooted
clique bags in this quotient. Lift them using E, and add B_β. It is
disjoint from those bags, contacts the α,γ,δ bags through their original
roots, and contacts the ε bag through the first edge of P(βε). These
are the five required K5 bags. QED

The external K4 input follows, for example, from Kriesell--Mohr,
*Kempe Chains and Rooted Minors*, arXiv:1911.09998v2, Theorem 7:
normalize the raw scheme root-preservingly, add a fresh isolated root,
and apply property (*) to K4 plus that isolated vertex, a five-vertex
graph with six edges. The exact primary statement is recorded in
[Section 2 of the source review](../results/llru_question61_via_km_property_star.md),
SHA-256 `8cac1bbffdc41825c6934921b4f778eea60a593615e4ae5e1ce5fe2606cf3797`,
with [audit](../results/llru_question61_via_km_property_star_audit.md)
SHA-256 `9281458846054d8e1a4002a8d54b96a03866e08dd97397e79fe72be6a6a9c467`.

## Remaining exchange

If z,w instead have different colours γ,δ, the same two absorptions
replace the required αγ,βδ contacts by βγ,αδ. Even for K5, where all
six of these target pairs exist, this does not supply the two lost
contacts. The old αγ and βδ paths pass through the vertices whose
ownership changed. No retained path yet repairs both lost contacts
without using a foreign root or another bag's vertices.
The terminal above handles its exact additional hypotheses. Its E
contraction is valid because the repaired αγ path avoids E; without
that condition it could consume vertices needed by this fourth demand.
The unrestricted different-colour case and degree-three nonroots remain
open here.
