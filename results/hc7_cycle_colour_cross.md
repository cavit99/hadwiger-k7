# A five-colour cycle condition forces two crossing paths

**Status:** computation-free written proof; the adjacent audit records a
separate GREEN internal review. The critical application constructs a rooted
subdivision, not the forbidden seven-vertex minor.

All graphs are finite and simple. For a cycle `C`, a **`C`-cross** is a
pair of vertex-disjoint paths whose four distinct endpoints occur in
alternating order on `C`, and whose internal vertices lie outside `C`.
The paths and the four arcs between their endpoints form a subdivision
of `K_4`, with those four actual cycle vertices as branch vertices.

## 1. The five-colour theorem

**Theorem 1.** Let `H` be five-colourable and contain a specified cycle
`C=0,1,2,3,4,0`. If every proper colouring of `H` with a palette of five
colours uses at least four colours on `C`, then `H` contains a `C`-cross.
Extra edges of `H`, including cycle chords, are allowed.

**Proof.** Suppose no `C`-cross exists, and choose a proper five-colouring.
If it already uses three colours on `C`, the claimed hypothesis fails.
Otherwise the cycle uses four or five colours.

First suppose all five cycle colours are distinct. If both pairs `0,2`
and `1,3` are bichromatically connected, their paths have disjoint colour
pairs, avoid the other cycle vertices and give a `C`-cross. Thus one pair
is disconnected in its two-colour graph. Swap the component containing
one endpoint. Only that cycle vertex changes colour, leaving exactly
four cycle colours. Relabel the cycle dihedrally so its repeated pair is
`0,2`.

We now have colours

`0,2: alpha; 1: beta; 3: gamma; 4: delta`,

and a fifth colour `epsilon` unused on `C` (it may be used elsewhere).
The component of `1` in colours `beta,gamma` must contain `3`:
otherwise swapping it makes `1,3` equal and gives three cycle colours.
Similarly there is a `beta,delta` path from `1` to `4`. Choose these
paths and call them `P13,P14`. Their internal vertices avoid `C`.

If `0,2` are connected in colours `alpha,epsilon`, that path together
with `P13` is a `C`-cross, since their colour pairs are disjoint.
Otherwise swap the `alpha,epsilon` component containing `0`. The cycle
is now rainbow with colours `epsilon,beta,alpha,gamma,delta` in order.
Both `P13` and `P14` are unchanged: none of their vertex colours was
swapped.

There cannot now be an `epsilon,gamma` path from `0` to `3`, since
it would cross `P14` with a disjoint colour pair. Likewise there cannot
be an `alpha,delta` path from `2` to `4`, since it would cross `P13`.
In each case the indicated palette has only its two endpoints on `C`,
so the paths would indeed have interiors outside the cycle.

Swap the `epsilon,gamma` component containing `0`, making `0,3` equal.
This leaves the entire `alpha,delta` subgraph unchanged. Its component
containing `2` still avoids `4`, so swap that component too. The cycle
now has pairs `0,3` and `2,4`, with singleton `1`: just three colours,
a contradiction. All swaps are proper Kempe recolourings of the same
host. This proves the theorem. QED

The proof also gives the contrapositive constructively: when there is
no `C`-cross, any proper five-colouring can be changed by at most four
Kempe swaps to one using three colours on `C`. No exhaustive search or
assumption about all Kempe-equivalence classes enters the argument.

## 2. Exact rooted interpretation

The `C`-cross and `C` form an actual `K_4` subdivision. Its four branch
vertices are prescribed vertices of the original cycle; the fifth cycle
vertex lies on one rim arc. To obtain a rooted `K_4` minor, assign the
interior of each subdivided edge to one of its endpoints. These connected
bags are disjoint and preserve the four branch roots and all six contacts.
The fifth cycle vertex must then be owned by one of the ends of its rim
arc. It is not an additional unused root or helper supplied by this proof.

## 3. Consequence of proper-minor six-colourings

Write `Q` for `K_7` with two independent edges deleted. We use the
three-coloured-cycle completion in Section 3 of
[flexible bipartite root families](../results/bipartite_flexible_root_families.md),
SHA-256 `5435c44801978073092cfaef1b685e8b5b52723a52ea28a87e3089d44127ec44`.
It has a separate adjacent internal audit.

**Corollary 2.** Suppose `G` is `Q`-minor-free, `chi(G)=7`, every
proper minor is six-colourable, and a vertex `v` has precisely eight
neighbours consisting of a triangle `A={a0,a1,a2}` and the specified
cycle `C`. Extra neighbourhood edges are allowed. For each `a in A`
there is a proper six-colouring of `G-v` whose colour class `I` at `a`
satisfies `I intersection N(v)={a}`. For every such colouring, the
graph `H=G-v-I` contains a `C`-cross.

**Proof.** Contract the actual edge `va` and properly six-colour this
proper minor. Its merged vertex is adjacent to all seven other neighbours
of `v`. Expand it only to `a`, leaving `v` uncoloured. This is a proper
six-colouring of `G-v`, and the colour of `a` is unique on `N(v)`.

Now fix any colouring with that uniqueness property and let `I` be its
whole colour class at `a`. The graph `H` contains all five cycle roots
and the other two triangle vertices, and is five-colourable. Any proper
five-colouring of `H` extends to a proper six-colouring of `G-v` by
giving the independent set `I` the sixth colour.

If the cycle used only three colours in such a colouring, the other two
triangle vertices would have to use the remaining two colours, each
absent on the cycle: otherwise at most five colours occur on `N(v)`
and `v` could be coloured. Thus all three triangle colours would be
unique on the neighbourhood, while the cycle used three other colours.
A three-colouring of a five-cycle has two nonadjacent pairs and a
singleton, of the form in the cited completion after dihedral relabelling.
That theorem gives `Q`, a contradiction. Consequently every five-colouring
of `H` uses at least four cycle colours. Apply Theorem 1. QED

The two paths in this corollary avoid `v` and the entire colour class
`I`, hence avoid the selected triangle root `a`. They need not avoid the
other two triangle roots. Those roots may be owned by the subdivision
or its resulting minor bags. Crosses obtained from different colourings,
or from different choices of `a`, are not asserted to be disjoint or
simultaneously compatible. A complete `Q` construction using the actual
critical host remains unproved; the corollary is not such a completion.
