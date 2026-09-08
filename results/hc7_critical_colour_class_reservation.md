# Reserving a whole colour class at a degree-eight critical vertex

**Status:** written deductions with a [separate internal audit](hc7_critical_colour_class_reservation_audit.md).
Neither the rooted K5 extraction nor its seven-bag extension is proved here.

All graphs are finite and simple; `Q=K7-2K2` has two independent edges deleted.
Assume `chi(G)=7`, every proper minor
of G is six-colourable, and `d_G(v)=8`. No minimum-degree, connectivity
or excluded-minor assumption is used below.

This reuses the star contraction and whole-colour-class restoration in
[the earlier cycle-and-triangle construction, Section 1](../active/hc7_degree8_cycle_triangle_construction.md),
source SHA-256 `b3c43b4682c4554c2100d75dd14ea9df07aa898686b1cb6e3a1d9603985f68fe`.
The mechanism is not asserted to be new. Its general form and the
additional reservation are proved explicitly here.

## 1. Five actual roots outside an independent colour class

**Lemma.** For every independent three-element set `T subseteq N_G(v)`,
there is an independent set I with `I intersect N_G(v)=T` such that,
putting `R=N_G(v)-T` and `F=G-v-I`, we have `chi(F)=5` and every
five-colouring of this same graph F makes the five vertices of R rainbow.
Every such colouring supplies a properly endpoint-coloured K5 scheme
rooted at all five actual vertices of R, avoiding `I union {v}`.

**Proof.** Contract the connected star `{v} union T` and six-colour
the resulting proper minor, giving its merged vertex colour alpha.
Expand only T, retaining alpha on its three vertices, and delete v.
This gives a proper six-colouring f of `G-v`: T is independent and
every other edge incident with T was represented in the quotient.
Every vertex of R avoids alpha, because it was adjacent to the merged
vertex through its original edge to v.

The five vertices of R must have five distinct colours. Otherwise
`N_G(v)` would use at most five colours in f, allowing a colour for v
and contradicting `chi(G)=7`. Let I be the entire alpha class of f.
It is independent and meets `N_G(v)` in exactly T.

The restriction of f five-colours F. A four-colouring of F, a fifth
colour on I and a sixth on v would colour G, so `chi(F)=5`.
If any five-colouring of F used at most four colours on R, restore I
in a sixth colour and give v an old colour missed by R. This would
again six-colour G. Thus the universal rainbow assertion holds.

In any five-colouring of F, two roots of colours i,j belong to the
same bichromatic component: swapping a component containing just one
would make those roots equal-coloured. Choose a simple bichromatic
path for each of the ten root pairs. No other prescribed root is
internal, since the roots have distinct colours. Every collection of
paths sharing a vertex has the common target endpoint labelled by
that vertex's colour. These are precisely the coloured scheme conditions.
All five roots remain their original vertices. QED

## 2. Four roots with an additional colour class reserved

**Corollary.** Suppose additionally that `N_G(v)` consists of disjoint
triangles `A={a,a1,a2}`, `B={b,b1,b2}` and the edge xy, with extra edges
allowed, and that `T={a,b,y}` is independent. Choose f and I as above.
Let J be the entire colour class of x in f, and put

`K=G-v-I-J`, and `L={a1,a2,b1,b2}`.

Then `chi(K)=4`; every four-colouring of this fixed K makes L rainbow
and makes `N_K(x)` meet all four colours. Moreover K contains an
L-rooted K4 minor. It avoids both entire classes I,J and v, hence
reserves all four other actual neighbours `a,b,x,y`.

The sole extraction input is
[universal bipartite contractibility](../results/bipartite_contractibility_via_matroid_reduction.md),
source SHA-256 `3faac3d0628f4ea61ceb7e1b2005917371e46b1168ed446492907035efa09272`,
with [adjacent audit](../results/bipartite_contractibility_via_matroid_reduction_audit.md)
SHA-256 `1c8ed74e98829690dc4c1fd6d44631454d330443dd33faea4435d35beb5cca06`.

**Proof.** The inherited colouring gives the four-colour upper bound.
Both I and J are independent, and their neighbourhood intersections
are T and `{x}` respectively. If K were three-colourable, restore I,J
in two new colours and v in a sixth, colouring G. Hence `chi(K)=4`.
If a four-colouring of K made L nonrainbow, restoring I,J in colours
five and six would leave a colour missing from `N_G(v)`, again colouring G.

If x missed a core colour in any four-colouring of K, restore I,J in
colours five and six and give x that missing core colour. No edge at x
is monochromatic. Colour six now disappears from `N_G(v)`, so it can
be assigned to v, a contradiction. This proves the neighbourhood claim.

The universal rainbow condition supplies four bichromatic paths between
`{a1,a2}` and `{b1,b2}`, as in the lemma. They form a K2,2 scheme in K.
Bipartite contractibility gives four disjoint connected rooted bags;
the literal edges `a1a2,b1b2` supply the two remaining contacts.
The triangles are used only for these literal edges. QED

## 3. Exact scope

The five-root scheme exists for every eligible T, independently of the
chromatic branch of the matching quotient. Choices for different T need
not share a colouring or model. A full K5 contractibility theorem would
therefore extract the five actual rooted bags while reserving T in every
branch; that theorem remains unproved. Even such an extraction would
still require a compatible seven-bag extension to Q in the original host.

Deleting whole colour classes is not asserted to preserve minimum degree
or connectivity. The smaller graph F is not asserted contraction-critical.
The star has a fixed connected preimage, but its order decrease is used
only to obtain a colouring, not as a closed induction. Independently
chosen models and helper paths cannot be combined without verifying
their disjointness and all required contacts.
