# Four-cut components of the two-triangle complement

**Status:** written proof; a [separate exact-source audit](hc7_four_cut_components_audit.md) is recorded beside it.
These are completed separator subcases, not a closure of the remaining
two-triangle case, Conjecture 19 or HC7.

All graphs are finite and simple. Put `Q=K7-2K2`. A rooted model has
disjoint connected bags containing its prescribed roots separately;
additional contacts are harmless.

**Theorem.** Let G be seven-connected, have minimum degree at least eight
and have no Q minor. Suppose `d(v)=8` and
`N(v)=A dotcup B dotcup {x,y}`, where A and B are literal triangles
and xy is an edge; extra edges are allowed. Put `R={v} union B` and
`F=G-R`. For every four-vertex cut S of F:

1. `F-S` has exactly two components.
2. If `chi(G)=7` and every proper minor of G is six-colourable, S is
   not independent.
3. If a component of `F-S` misses `r in R`, then
   `|N_G(r) intersect S|<=1`.

## Inputs and the side packet

The [complement theorem](hc7_two_triangle_complement_four_connectivity.md),
source SHA-256 `0a75273d2270d5a675e3aa565610d47e375fa89e982b565fbd0ad4f4e5fd3b69`,
gives four-connectivity of F under the stated structural hypotheses.
Its [audit](hc7_two_triangle_complement_four_connectivity_audit.md)
has SHA-256 `d074cc7eb384222f1b68ed53728fd721c7a6e7edbf266c55cec313a5c73b2014`.
The [five-root degree-six theorem](hc7_five_root_degree_six.md),
source SHA-256 `289c5ad015b6c392ea69e8e26e15eba54b4eba7cb155789edd76b3dbb5c9f9a4`,
and its [audit](hc7_five_root_degree_six_audit.md), SHA-256
`6f13ffd37126c78a697b5752574fe06b6fd13b68dabb0d63e4e39d76a8f1d065`,
supply the following packet. Five roots containing a triangle, a nonempty
nonroot set with every subset boundary at least five, and nonroot degree
at least six give a rooted K5-minus-edge. At least two triangle roots
are admissible as the triangle endpoint of its sole possible hole; the
other endpoint is one of the two remaining roots.

Every component C of `F-S` contacts all of S: a missing contact would
give a cut of F of order at most three. Its G-boundary is contained in
`S union R`, and another component survives outside that boundary.
Seven-connectivity therefore makes C contact at least three R vertices.

Suppose C misses `r in R`, and choose distinct `s1,s2 in S`. In the
actual induced graph on `C union (R-{r}) union {s1,s2}`, the roots are
the triangle `R-{r}` and s1,s2. A C vertex loses only the other two S
vertices, so its degree is at least six. For every nonempty `X subseteq C`,
r survives outside `X union N_G(X)`, so `|N_G(X)|>=7`; deleting those
two S vertices leaves at least five neighbours. Thus the packet applies.
All its bags lie in the displayed side, reserving r, the two unused S
vertices and every other component.

## Exactly two components

There is a component meeting `N_F(v)`, since this set has five vertices
and S has four. There are at most two such components: the surviving A
vertices form one connected group, and the surviving x,y form another.
Suppose there are at least three components. Choose a v-free component C
and apply the packet with triangle B and roots s1,s2.

If another v-free component E exists, choose a v-touching component D
and `s3 in S-{s1,s2}`. The bags `E union {s3}` and `D union {v}` are
connected and disjoint from the packet and each other. Both are full to
all five packet bags: E sees B,s1,s2, while D sees s1,s2 and v sees B.
They are adjacent through an s3--D edge. Together with the packet they
give Q, even if its one allowed hole is present.

Otherwise there are two v-touching components D1,D2. Each contacts at
least two B roots. Choose the packet's admissible triangle endpoint
among the B roots contacted by D2; both sets have size at least two.
The bag `D1 union {v}` is full to the packet and contacts D2 through v.
D2 contacts s1,s2 and misses at most one B root, different from the
chosen endpoint. Hence the packet, `D1 union {v}`, and D2 have at most
two missing contacts with disjoint ends, giving Q. This proves (1).

## Independent cuts and proper-minor colourings

Assume the additional hypotheses of (2), suppose S is independent,
and write C,D for the two components. Contract the connected set
`D union S` and six-colour that proper minor. Restrict to the untouched
C-side, expanding S with the merged colour. This properly colours
`G[C union R union S]`, since S is independent. Reversing the roles
gives such a colouring of the D-side. In both responses S is monochromatic
and the four R vertices have distinct colours.

If both responses give S a colour outside the four R colours, permute
their palettes to agree on R and S and glue them. Otherwise, relabel the
sides so a C-side response gives S the colour of `r in R`. In its
quotient the merged set `D union S` is nonadjacent to r. Thus r misses
D and S, and has a neighbour in C, since it has at least five neighbours
in F. The set `C union S union {r}` is connected. Contract it and
six-colour the resulting proper minor. On the untouched D-side expand
`S union {r}` with the merged colour; this set is independent, so the
expansion is proper. Its boundary partition now agrees with the C-side
response. Permute colours to agree on R and glue the two side colourings.

In either case every edge of G lies in one of the two closed sides,
giving a proper six-colouring of G, a contradiction. No colouring is
pulled back through a consumed component. This proves (2).

## A missed root has at most one cut neighbour

Suppose C misses `r in R` but r sees distinct s1,s2 in S. Since r has
at least five neighbours in F, some component D of `F-S` contacts r.
It differs from C. Apply the side packet on C with triangle `R-{r}`
and roots s1,s2. D contacts both helper roots and at least two triangle
roots. Choose an admissible endpoint contacted by D. The singleton r
is full to all five packet bags through their roots and contacts D.
D can miss only one triangle bag, whose root differs from the selected
endpoint. These seven disjoint bags give Q, with independent possible
holes. This proves (3).

The colouring argument is due to the separate independent-cut analysis;
the structural arguments use one fresh packet and actual exterior bags.
The remaining binary cases with non-independent S, including missed
roots with zero or one S-neighbour, are not resolved. No iterable
reduction or completion of C19 or the global objective is asserted.
