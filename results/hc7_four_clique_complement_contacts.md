# Contacts with a four-clique and its nonplanar complement

**Status:** written proof; separate internal audit beside this file.
These are construction and exclusion lemmas. They do not close the
two-triangle case, Conjecture 19 or HC7.

All graphs are finite and simple. Put `Q=K7-2K2` and `W4=K1 join C4`.
Contacts are actual edges between disjoint connected bags.

## An eight-bag construction

**Lemma.** Suppose three bags form a triangle and five other bags form
a W4. Each wheel bag contacts at least two triangle bags, and at least
one contacts all three. Then their union contains a Q minor.

**Proof.** Retain one full wheel bag. For every other full bag, discard
one triangle contact; now each other wheel bag has one missing triangle
label. Extra host edges may always be ignored.

If a triangle label never occurs as a missing label, merge the other
two triangle bags. Both remaining triangle bags contact every wheel bag,
giving `K2 join W4=Q`. Otherwise all three labels occur.

If the hub is full, the four rim labels include all three labels.
There is a perfect matching of the rim cycle whose two edges both have
different endpoint labels: the repeated label occurs twice, and pairing
those two occurrences to the other two vertices is possible along the
cycle. Contract one matching edge. Its bag is full to the triangle;
the wheel becomes a K4, and the other matching edge's two vertices have
different missing labels. The only two missing contacts are independent.

If a rim bag is full, call it `w0`. Write `c` for the hub's missing
label and `a,b,d` for the labels of `w1,w2,w3` in cyclic order.
At least one of

```text
a != b and c != d;       b != d and c != a
```

holds. Indeed, failure of both forces one of `a=b=d`, `a=b=c`,
`b=c=d`, or `a=c=d`, leaving at most two labels, a contradiction.
Contract `w1w2` in the first case and `w2w3` in the second. The merged
bag is full to the triangle. The resulting four wheel bags form a K4;
the two nonfull bags have different missing labels. Again there are
at most two independent missing contacts. Every merger uses an actual
edge and fixed disjoint preimages, proving the lemma. QED

## Six pair contacts

**Lemma.** Let R be a literal four-clique and let F be a connected
graph disjoint from R in which any four vertices root a K4. If six
distinct vertices of F contact the six different pairs of R, then F
together with R contains a Q minor.

**Proof.** Label R by `0,1,2,3`. Root a K4 at the vertices contacting
`01,12,23,03`, respectively, and extend its bags `C0,C1,C2,C3` to a
connected partition of F by assigning unused vertices along a forest.
The vertices contacting `02` and `13` now have definite owners, even
if they already belonged to the initial model. Their contacts are added
to those of their owning bags.

The following table gives a single merger and the only possible missing
contacts afterwards. Here `Ri` denotes the singleton clique vertex i.

| Owner of 02 | Owner of 13 | Merge | Possible missing contacts |
| --- | --- | --- | --- |
| C0 | C0 | R0 with C3 | C1–R3, C2–R1 |
| C0 | C2 | C1 with C3 | C0–R3, C2–R0 |
| C0 | C1 | R0 with C3 | C0–R3, C2–R1 |
| C1 | C0 | R2 with C2 | C1–R3, C3–R1 |

Square symmetries give four assignments from each row, exhausting all
sixteen: the owners coincide, are opposite, or are adjacent in either
of the two orientations. In every row the merged bags are adjacent,
and the two listed omissions have distinct ends. The seven resulting
bags therefore give Q, with disjoint fixed preimages. QED

## Contact bounds

**Theorem.** Let G have no Q minor, let R be a literal four-clique, and
let `F=G-R` be four-connected and nonplanar.

1. For every partition of R into two nonempty sets, at most four vertices
   of F have a neighbour in each set. Consequently at most six vertices
   of F have at least two neighbours in R.
2. If S is a triangle in R and `G-S` is connected, at most four vertices
   of F have at least two neighbours in S.
   The bound is three if the remaining clique vertex has at least five
   neighbours in F. If every clique vertex has at least five neighbours
   in F, at most five vertices of F have at least two neighbours in R.
3. If `delta(F)>=6` and `delta(G)>=8`, at most five vertices of F
   have degree six, all others have degree at
   least seven, and `F-u` is nonplanar for every vertex u of F.

**Proof.** Every five vertices of F root a W4. To see this, apply
[Norin–Totschnig, Theorem 8](https://arxiv.org/html/2507.03244v1#S2)
to any four of them. Four-connectivity excludes both separation
alternatives and nonplanarity excludes the plane alternative, leaving
a rooted K4. The [five-root extension](hc7_rooted_wheel_extension.md)
gives the wheel on all five roots; its fifth root may already lie in
the initial model.

For (1), five common-contact vertices would give five wheel bags each
adjacent to both parts of R. Those parts are connected and adjacent,
so the seven bags give `K2 join W4=Q`. There are three balanced
two-by-two partitions of R. Any vertex with at least two R-neighbours
is counted in at least two of them, since each chosen neighbour pair
is separated twice. Their total count is at most twelve, proving the
bound of six. No bound on an individual vertex's R-degree is needed.

For (2), root a wheel at five alleged vertices. Let r be the sole vertex
of `R-S`. In the connected graph `G-S`, take a path from r to the wheel
union, stopped at its first wheel vertex. Absorb the path into the bag
it meets. Its interior avoids every other wheel bag and S, so all five
bags stay disjoint and retain their contacts. The enlarged bag is full
to S through the literal r–S edges. Every other wheel bag retains its
two S contacts. The eight-bag lemma gives Q, a contradiction.

For the stronger bound, suppose four vertices have two S contacts.
Choose a neighbour of r in F different from those four. Root a wheel
at these five vertices and absorb r into the bag containing the fifth
root, using their actual edge. That bag is full to S; the other four
retain their two S contacts. The eight-bag lemma again gives Q.

If six vertices had at least two R-neighbours, sum their contributions
to the four triangle counts, now at most three each. Each contributes
at least two; three or more R-neighbours would contribute four. Thus
each has exactly two R-neighbours and every triangle count is three.
Write `m_ij` for the multiplicity of pair ij. The four weighted vertex
degrees are three. By (1), every balanced cut has at most four crossing
pairs, so the multiplicities on each pair of opposite edges sum to at
least two. These three sums total six, hence all equal two. Equal
weighted vertex degrees also give equal multiplicities on opposite
edges. Consequently every `m_ij=1`, contradicting the six-pair lemma.

For (3), a degree-six vertex of F has at least two R-neighbours. Each
clique vertex has at least five neighbours in F, so (2) bounds the number
of degree-six vertices by five. Suppose `P=F-u` were planar. It has minimum
degree at least five and at least six vertices. Euler's inequality gives
`sum_(w in V(P)) (6-d_P(w))>=12`. Vertices of degree five contribute
one and all others contribute at most zero, so P has at least twelve
degree-five vertices. Each has degree six in F, contrary to the bound
just proved. QED

## An existing side replacement and its limit

The [four-root lemma](hc7_two_triangle_exterior_helpers.md#1-a-four-root-packet)
already proves that four prescribed roots have a rooted K4 if every
nonempty nonroot set has at least four external neighbours and every
nonroot has degree at least six. Consequently, if `delta(F)>=6`, every
component C beyond a four-cut S supplies an S-rooted K4 in `F[C union S]`: its
nonroot degrees and boundaries are inherited from F. A clique completion
of S on the opposite side lifts through these actual disjoint bags.
This uses an existing audited theorem, not a new four-root result.

Retaining the old R gives a minor whose complement contains
`F'=(F-C)+K_S`. This torso is four-connected: after at most three
deletions the surviving S vertices lie in one component, and any other
component would already violate four-connectivity of F. It is nonplanar:
an opposite component is full to the literal K4 S, giving a K5 minor.
Thus the basic contact bound in part (1) still applies.

## Application and limit

In the actual two-triangle critical host, take `R={v} union B`, or
exchange the triangles. The [complement theorem](hc7_two_triangle_complement_four_connectivity.md)
gives four-connectivity of F, and the
[clique-deletion bound](hc7_clique_deletion_colour_bound.md) gives
`chi(F)>=5`, hence nonplanarity by the four-colour theorem. The host has minimum degree
eight; [contraction closure, Corollary 3](../active/hc7_companion_contraction_closure.md)
gives at most two R-neighbours per outside vertex, hence `delta(F)>=6`.
Seven-connectivity gives connectedness of `G-S`. All three conclusions
therefore apply, without assuming `chi(F)=5` rather than six.

The side replacement need not preserve the five outside neighbours at
each R vertex, the degree bound at S, or the colouring responses. Therefore
the stronger contact bounds and another side replacement do not yet form
a closed induction. These constructions do not close the remaining host.
