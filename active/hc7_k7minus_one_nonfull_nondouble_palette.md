# A shore-localized non-double-critical response in the one-nonfull case

**Status:** active written proof;
[separate internal audit GREEN](hc7_k7minus_one_nonfull_nondouble_palette_audit.md).
The new deductions are computation-free conditional on `|D|<=4`; the host
application inherits the computer-assisted frozen-129/defect-two input which
proves that bound.  This operation-coupled reduction does not eliminate the
one-nonfull case or prove exceptional-centre connectivity.

## 1. Setup

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Let `u` be an exceptional vertex of degree eight, put `X=N_G(u)`, and
suppose that `G-N_G[u]` has exactly two components `E,F`, where `E` misses
`x\in X` and `F` is adjacent to every vertex of `X`.  Put

\[
 S=X-\{x\},\qquad D=N_G(x)\cap S,\qquad R=S-D.        \tag{1.1}
\]

The established one-nonfull reduction gives

\[
                         |S|=7,\qquad |D|\le4.         \tag{1.2}
\]

The exterior components are anticomplete to one another, `u` is
anticomplete to both, and `x` is anticomplete to `E`.

## 2. The missed edge is not double-critical

### Lemma 2.1

\[
                         \chi(G-\{u,x\})=6.            \tag{2.1}
\]

#### Proof

The common neighbours of `u,x` are exactly the vertices of `D`.  Indeed,
every common neighbour of the two ends belongs to `N(u)-\{x\}=S`, and
inside `S` it is common precisely when it is adjacent to `x`.  Thus

\[
                    |N(u)\cap N(x)|=|D|\le4.          \tag{2.2}
\]

Suppose that `G-{u,x}` had a proper five-colouring; a colouring with fewer
colours may be regarded as one with palette `[5]`.  For every colour `i`,
there must be an `i`-coloured common neighbour of `u,x`.  Otherwise recolour
all `i`-coloured neighbours of `u` with one new sixth colour, give `u`
colour `i`, and give `x` the new colour.  The recoloured vertices are
independent, and none is adjacent to `x`, by the assumed absence of an
`i`-coloured common neighbour.  This would be a proper six-colouring of
`G`, a contradiction.  Hence the common neighbourhood has at least five
vertices, contradicting (2.2).

The graph `G-u` is a proper minor and is six-colourable, so its induced
subgraph `G-{u,x}` is at most six-colourable.  This proves (2.1). \(\square\)

## 3. One actual edge response is confined to the joined shore

Delete `ux` and fix a proper six-colouring `c` of `G-ux`.  Necessarily

\[
                         c(u)=c(x)=\alpha,             \tag{3.1}
\]

or the edge could be restored.  Put `H=G-{u,x}` and let `A` be the
`alpha`-colour class in `H`.  Lemma 2.1 implies that `A` is nonempty.
Properness and the literal neighbourhoods give

\[
 A\cap S=\varnothing,
 \qquad
 A\subseteq E\mathbin{\dot\cup}(F-N_G(x)).           \tag{3.2}
\]

Every colour `beta!=alpha` occurs at a neighbour of each of `u,x`.
Otherwise the deficient endpoint could be recoloured `beta` and `ux`
restored.  In particular, all five non-`alpha` colours occur on `S`.

### Theorem 3.1 (shore-localized five-path response)

For every colour `beta!=alpha`, the vertices `u,x` belong to one component
of

\[
 (G[F\cup S\cup\{u,x\}]-ux)
       [c^{-1}(\{\alpha,\beta\})].                   \tag{3.3}
\]

Consequently there are five `u`--`x` paths, one for each
`beta!=alpha`, wholly contained in `F\cup S\cup\{u,x\}`.  Paths belonging
to distinct colours have no common edge, and their common internal
vertices, if any, have colour `alpha`.

If `beta` is absent from `c(D)`, then every corresponding simple path

1. leaves `u` at a `beta`-coloured vertex of `R`;
2. enters `x` from a `beta`-coloured vertex of `F`; and
3. contains an internal `alpha`-coloured vertex of `F`.

In particular, `A\cap F` is nonempty.

#### Proof

In the full edge-deleted graph `G-ux`, the two ends belong to one
`alpha`--`beta` component.  Otherwise interchange the two colours on the
component containing `u`; the ends then have different colours and `ux`
can be restored.

Let `J=G[F\cup S\cup\{u,x\}]-ux`, and let `K` be the
`alpha`--`beta` component of `J` containing `u`.  Since `u` has colour
`alpha` and is adjacent to every vertex of `S`, the set `K` contains every
`beta`-coloured vertex of `S`.  Every edge from `E` to `J` has its end in
`S`; if it belongs to the `alpha`--`beta` subgraph, that end has colour
`beta`, because (3.2) says that `S` has no `alpha` vertex.  Thus every such
end already belongs to `K`.  Adding the `alpha`--`beta` vertices and edges
of `E` therefore cannot join `K` to a different component of the
`alpha`--`beta` subgraph of `J`.  Since `x` is in the same full
`alpha`--`beta` component as `u`, it follows that `x\in K`.  This proves
(3.3).

Choose one simple path inside (3.3) for each non-`alpha` colour.  Two paths
with second colours `beta,gamma` can meet away from their common ends only
at a vertex whose colour lies in

\[
       \{\alpha,\beta\}\cap\{\alpha,\gamma\}=\{\alpha\}.
\]

They cannot share an edge, since both ends of a shared edge would then
have colour `alpha`, contrary to properness.

Now suppose `beta` is absent from `c(D)`.  The first vertex after `u` lies
in `S`, has colour `beta`, and therefore belongs to `R`.  The last vertex
before `x` is a `beta`-coloured neighbour of `x`.  It cannot lie in `S`,
because every such neighbour lies in `D`, so it lies in `F`.  Between the
first boundary vertex and this last vertex the alternating path must use an
`alpha` vertex: two `beta` vertices cannot be adjacent.  Such an internal
`alpha` vertex is not in `S` by (3.2), and the path avoids `E`, so it lies
in `F`.  At least one colour is absent from `c(D)` because `|D|\le4`,
which proves the final assertion. \(\square\)

The point of Theorem 3.1 is that the `E` shore is not needed even as a
Kempe detour.  The five paths retain one actual `G-ux` colouring and their
five two-colour labels; they are not ordinary paths selected independently
by Menger's theorem.

### Corollary 3.2 (the simultaneous palette linkage)

Choose one neighbour of each non-`alpha` colour at each of `u,x`.  The
palette-permutation linkage theorem gives five internally vertex-disjoint
`u`--`x` paths in `G`, with the five distinct colours represented at each
pole and paired by a permutation.  At the `u` end all five paths enter
`S`.  At the `x` end, every path whose selected `x`-end colour is absent from
`c(D)` enters `F`; there is at least one such path.

#### Proof

Lemma 2.1 and the colouring `c` give exactly the non-double-critical
palette frame required by that theorem.  The location assertions follow
from `N_H(u)=S`, `N_H(x)=D\mathbin{\dot\cup}N_F(x)`, and `|D|\le4`.
\(\square\)

Theorem 3.1 and Corollary 3.2 retain different information from the same
operation.  The first keeps every two-colour label and confines all paths
to the joined shore, but its paths may meet at `alpha` vertices.  The
second gives simultaneous vertex-disjointness, but its endpoint pairing is
an arbitrary permutation and its paths may use `E`.  No current rerouting
theorem preserves both packages at once.

## 4. The `K_7^-` sharpening of the five-core alternative

Apply the audited adjacent-pair two-colour separation/five-core theorem to
the edge `ux`, using Lemma 2.1.  If its separation alternatives never
occur, then for every `beta!=alpha` the graph

\[
                  Z_\beta=H[A\cup c^{-1}(\beta)]     \tag{4.1}
\]

is connected and dominating after the two poles are restored.  Fix one
`beta`, put

\[
 Q=G-V(Z_\beta),\qquad T=Q-\{u,x\},                 \tag{4.2}
\]

and use the two opposite near-clique models supplied by the five-core
theorem.

### Proposition 4.1 (outside-pole contact bound)

In the model

\[
             \{x\},\ \{u\},\ Z_\beta,\ M_1,\ldots,M_4,          \tag{4.3}
\]

where `\{u\},M_1,...,M_4` form a `K_5` model in `Q-x`, the vertex `x`
is adjacent to at most two of `M_1,...,M_4`.  Symmetrically, in the
oppositely rooted model, `u` is adjacent to at most two of the four
non-pole branch sets.

#### Proof

All pairs in (4.3) are adjacent except possibly `\{x\}M_i`: the first
five sets after `\{x\}` contain the singleton-rooted `K_5` model,
`Z_\beta` dominates `Q`, and both poles meet `Z_\beta`.  If `x` met at
least three of the four sets `M_i`, the seven displayed sets would have at
most one missing adjacency.  They would therefore be an explicit
`K_7^-`-minor model, contrary to (H).  The opposite orientation has the
same proof. \(\square\)

This improves the corresponding `K_7`-free statement, which needs contact
with all four non-pole branch sets.  Equivalently, in the four-chromatic
graph `T`, a terminal `K_7^-` construction would follow from a `K_4` model
all four of whose bags meet one pole neighbourhood and at least three of
whose bags meet the other.

### Corollary 4.2 (two rooted bags are forced into `F`)

Choose `beta` absent from `c(D)` and suppose the five-core alternative
holds.  In the opposite near-clique model, write

\[
                     \{x\},L_1,L_2,L_3,L_4           \tag{4.4}
\]

for the singleton-rooted `K_5` model in `Q-u`.  At least two of the four
sets `L_i` are wholly contained in `F` and are anticomplete to `u`.  They
are disjoint, connected, and adjacent to one another.

#### Proof

The seven sets

\[
                   \{x\},\ \{u\},\ Z_\beta,
                   L_1,L_2,L_3,L_4                  \tag{4.5}
\]

have every adjacency except possibly those between `u` and the `L_i`.
Thus `u` meets at most two of the four bags by the same `K_7^-` argument as
Proposition 4.1.  Let `L_i` be one of the at least two missed bags.  Since
`u` is adjacent to every vertex of `S`, the bag `L_i` contains no vertex of
`S`.  It is adjacent to the singleton branch set `\{x\}` in the rooted
`K_5` model.  That adjacency cannot be witnessed in `E`, because `x`
misses `E`.  A connected set in
`H-S=E\mathbin{\dot\cup}F` which meets `F` lies wholly in `F`.  The two
selected bags retain their mutual adjacency from the `K_4` model.
\(\square\)

Corollary 4.2 is a literal shore allocation, but the two bags need not be
adjacent to every vertex of `S`.  It therefore does not supply the two
boundary-full connected subgraphs required by the existing exact-seven
reflection theorem.

## 5. Exact stopping point

The new input does not close the clean non-tight fan outcome of the
one-nonfull reduction.

The two-colour analysis has the following exhaustive obstruction types.

1. A diffuse pole-support component, a one-pole component, or an inactive
   component gives an actual operation-labelled separator.  Components
   with no boundary vertex lie in one literal exterior shore.  Seven-
   connectivity supplies only a lower bound of seven on the separator;
   it does not give the upper bound needed to make the separator an exact
   order-seven descent.
2. If all five two-colour graphs avoid those separator outcomes, the
   connected-dominating five-core alternative applies.  Strong Hadwiger
   for four colours roots a `K_4` model at either pole neighbourhood
   separately.  What is still missing is one model rooted at one
   neighbourhood and meeting the other in at least three bags, or a
   compatible exact order-seven separation.  Proposition 4.1 records the
   precise failure forced by `K_7^-` exclusion: both opposite rooted
   models have at least two branch sets missed by the outside pole.
   Corollary 4.2 places two such bags literally in `F`, but gives no
   boundary-fullness or response-compatible way to enlarge them.

Neither the shore-localized paths nor the contact bound aligns palette
colours with the four named minor branch sets.  Thus promoting this note to
an elimination of the one-nonfull case would require exactly the
label-preserving operation that remains open.

## Inputs

- [one-nonfull attachment reduction](../results/hc7_k7minus_nonfull_attachment_reduction.md)
- [palette-permutation linkage](../results/hc7_adjacent_pair_palette_linkage.md)
- [two-colour separation or five-core](../results/hc7_adjacent_pair_separator_or_five_core.md)
- [five-core compression](../results/hc7_star_kempe_five_core_compression.md)
