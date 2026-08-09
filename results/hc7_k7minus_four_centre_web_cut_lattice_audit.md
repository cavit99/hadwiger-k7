# Internal audit: four-centre rooted web and exact-cut lattice

Audited file:
`results/hc7_k7minus_four_centre_web_cut_lattice.md`.

Audited mathematical revision SHA-256:

```text
e5245aaea640f663c126e97ef462ed7c4fbccfba4bcb3f6c3a347ca2087a3ea3
```

Promoted source SHA-256:

```text
e7fcf00c9bdbd2fcbab78bb13d4244a659f4f7db0ae45a97cfbd9a8d599a0ee3
```

The promoted revision changes only the status paragraph, source path, and
one trailing space in display (5.1); its theorem statements and proofs are
identical to the audited mathematical revision.

**Verdict:** **GREEN** for the exact revision above.

This is a separate internal mathematical audit, not external peer review.
The proof was reconstructed theorem by theorem, including the rooted-minor
source, the lift-order identities, the Kempe argument, and the two-universal-
vertex quotient.  No computation is used in the audited theorem.

## 1. Critical-host arithmetic and the common deleted graph

The cited critical-host closure supplies at least 25 degree-eight vertices
and excludes a literal `K_5`.  McKay--Radziszowski's exact equality
`R(4,5)=25`, together with Ramsey-number symmetry, therefore supplies an
independent four-set `U` of degree-eight vertices.

Because `U` is independent, deleting it removes exactly 32 edges.  Thus,
with `H=G-U`,

\[
 |E(H)|\ge4|V(H)|-16>3|V(H)|-6,
\]

where `|V(H)|>=21`.  This correctly proves nonplanarity.  Deleting four
vertices lowers connectivity by at most four, so `H` is three-connected,
and it is four-connected when `G` is eight-connected.  Conversely the
eight neighbours of any member of `U` separate that vertex from the other
three members, so `kappa(G)<=8`.

The minor-minimal hypothesis makes `H` six-colourable.  A five-colouring of
`H` would extend by assigning one new colour to the independent set `U`, so
`chi(H)=6`.  These deductions use no unstated order or simplicity exception.

## 2. Rooted-web dichotomy and the exact cut

In a six-colouring of `G-r`, every colour occurs on the eight neighbours of
`r`; otherwise the colouring extends to `r`.  Six positive colour
multiplicities summing to eight have at least four singleton classes.  Their
representatives all lie in `H`, since `U` is independent.

Fabila-Monroy--Wood, Theorem 8, was checked in the cited primary source.  For
four distinct nominated vertices in a three-connected graph it says exactly
that a rooted `K_4` model exists if and only if the graph is not a spanning
subgraph of a web rooted at those vertices.  Thus the two outcomes in
Theorem 2.1 are exhaustive and exclusive.  In the model outcome, adjoining
the singleton `{r}` is valid because `r` meets each rooted bag at its
nominated vertex.

In the web outcome, nonplanarity of `H` forces at least one added cell
`X_T` to be nonempty; otherwise `H` would be a subgraph of the planar
skeleton.  For a component `C` of `H[X_T]`, web containment gives
`N_H(C) subseteq T`.  An outer nominated vertex lies outside the three-set
`T`, so there is a genuine opposite side.  Three-connectivity forces
`N_H(C)=T`.  In `G`, the only additional possible neighbours are the four
deleted centres.  Seven-connectivity then forces

\[
                         N_G(C)=T\mathbin{\dot\cup}U.
\]

The separately audited order-seven-cut theorem applies and leaves exactly
one other component `D`; seven-connectivity makes both components full at
the literal boundary.  The nominated roots belong to the web skeleton and
avoid `C`; at least one avoids the three-set `T` as well and hence lies in
`D`.  No web-completion edge on `T` is treated as an edge of `G`.

For Lemma 2.3, the selected vertex in `D` is the unique neighbour of `r` in
its colour.  That colour is absent from the closed `C`-shore neighbourhood
of `r`, so it can be assigned to `r`.  The same uniqueness argument excludes
all four selected colours from `N_G(r) cap C`, leaving only the other two
colours there.

## 3. Minimum lifted order and submodularity

For a separation `p` of `H`, every trace-preserving lift contains the trace
separator and every centre having neighbours in both open shores.  Conversely,
put exactly those crossing centres in the lifted separator and put each
remaining centre on a side containing all its open-shore neighbours.
Independence of `U` prevents an added centre-to-centre crossing edge.  This
proves the exact minimum-lift formula for `lambda_U`.

The ordinary separator contribution is modular under the displayed meet and
join.  For each fixed centre, the crossing indicator is submodular: crossing
both corners forces crossing both inputs, while crossing only one corner
forces crossing at least one input.  Hence the summed inequality is valid.
Because the ordinary contribution has zero slack and every rootwise slack is
nonnegative, equality of the total forces equality centre by centre.

A proper trace has two nonempty open shores in every lift, so connectivity
gives the asserted lower bound.  With fixed opposite anchors both lattice
corners remain proper; their two lower bounds and submodularity force exact
order in both corners.  Repeated meet therefore gives a canonical minimum
anchored shore.  In the seven-connected case a proper three-separation of
`H` must be crossed by all four centres.  Conversely, every vertex of an
order-seven boundary sees both open shores, since otherwise the other six
boundary vertices would disconnect `G`.

If the minimum anchored open shore were disconnected, its anchor component
would have neighbourhood contained in the same seven-vertex boundary.
Seven-connectivity makes that neighbourhood equal to the boundary, producing
a strictly smaller anchored four-centre shore.  This proves connectedness.

For Corollary 3.4, orienting all cuts between vertices in antipodal nonempty
sign regions permits repeated meet.  Its open shore is exactly the selected
sign region, so every centre has a neighbour there.  Distinct regions are
disjoint, and every centre has degree eight.  The eight-region saturation
and four-cut impossibility conclusions therefore follow exactly as stated.

## 4. Centre-supported Kempe linkage

If two selected neighbours `x_i,x_j` were in different bichromatic
components, swapping their two colours on the component of `x_i` would
remove colour `c_i` from `N_G(r)`: `x_i` was its unique representative, and
the unique `c_j`-representative `x_j` is not swapped.  Assigning `c_i` to
`r` would then six-colour `G`.  Thus every selected pair is joined in its
bichromatic component.

The two alternating pairs use disjoint colour sets, so their components are
vertex-disjoint.  If both avoided `U-{r}`, paths within them would give the
crossing linkage in `H` excluded by the ordered web.  Hence another named
centre lies in one of the two components.

For the final assertion, negate (4.2).  Each other centre then has an
available colour in `Delta` absent from its `H`-neighbourhood.  Simultaneous
recolouring is proper because `U` is independent, and it does not change the
colours on `N_G(r)`.  All other centres now use colours outside the four
crossing-path colours.  Repeating the Kempe argument would put both crossing
paths wholly in `H`, the same web contradiction.  Therefore some named
centre sees both colours in `Delta`, as claimed.

## 5. Universal-pair quotient and triangle terminality

Lemma 5.1 was checked by branch-set cases.  A `K_5` model in `F`, together
with the two independent universal vertices, gives the right-to-left construction.
A `K_5^-` model in `F-x`, together with `{c,x}` and `{d}`, gives the other
construction.

Conversely, if a `K_7^-` model uses at most one universal vertex, at least
six model bags lie in `F`; omitting an endpoint of the possible missing pair
leaves five pairwise adjacent bags.  If both universal vertices are singleton
bags, their nonedge is the unique possible missing pair and the other five
bags form a `K_5` model.  In every remaining case, discard the one or two
bags containing the universal vertices and choose an `F`-vertex `x` in one
of them.  At least five remaining bags lie in `F-x` and have at most one
missing adjacency, giving a `K_5^-` model.

If `G[T]` were a triangle, the boundary partition

\[
                         U\mid\{t_1\}\mid\{t_2\}\mid\{t_3\}
\]

is reflected through one full component in each direction.  The contracted
representative of `U` and the three retained singleton vertices form a
clique, so the returned equality partition is exact.  Palette alignment then
glues the two closed-shore colourings, contradicting `chi(G)=7`.

Contracting `C` and `D` gives two nonadjacent vertices universal to `G[S]`.
The contraction is proper because `|V(G)|>=25` while `|S|=7`.  Minor
exclusion and Lemma 5.1 therefore give both boundary exclusions in
Corollary 5.2.

## 6. Dependency integrity and scope

The local theorem dependencies were checked at their audited revisions:

- critical-host degree and density closure:
  `6ffee04cf9ff66275f9674c24bc2b9c669b1e108b76e5b1d2a18ec7d0106fe67`;
- two-component normal form for order-seven cuts:
  `1041988a33b749bef5802dd21d3cd9419b5afc754735a20174bf5a13c0a56c96`;
- exact boundary-colouring reflection:
  `d4d650fee168fc2ff0e00a3b7b0faed6ff674ba8cd3c06c263f63c4170656f34`.

No unresolved assumption or proof gap was found.  The result gives a genuine
unbounded structural reduction and a labelled Kempe constraint.  It does not
eliminate the nontriangular exact-cut outcome, preserve colouring labels under
uncrossing, prove the `K_7^-` six-colour conjecture, or settle `HC_7`.
