# Operation-labelled descent for distinct adjacent misses

**Status:** active written reduction; [separate internal audit](hc7_k7minus_adjacent_miss_operation_descent_audit.md)
GREEN.  This is an unbounded
normalization of the distinct-adjacent-miss case.  It proves that the missed
edge is non-double-critical, obtains a coupled four-path packing and two
full prescribed shore fans from one edge-deletion response, and exposes a
four-connected nonplanar residual.  It also gives either a clean
colour-indexed path packing on each side or a strict actual order-seven
separation carrying that response.  It does not by itself exclude distinct
adjacent misses.

## 1. Setting

Assume

\[
 \kappa(G)\ge7,\qquad \chi(G)=7,\qquad
 \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                            \tag{1}
\]

Let `u` be an exceptional degree-eight vertex, put `X=N_G(u)`, and suppose
that `G-N_G[u]` has components `E,F` with distinct adjacent missed
neighbours

\[
 N_X(E)=X-\{x\},\qquad N_X(F)=X-\{y\},
 \qquad xy\in E(G).                                     \tag{2}
\]

Write `Z=X-{x,y}` and

\[
 S_x=Z\cup\{y\},\qquad C_x=F\cup\{u,x\}.               \tag{3}
\]

Then `S_x` is an order-seven separator and `C_x` is one component of
`G-S_x`; the other component is `E`.  The symmetric definitions are

\[
 S_y=Z\cup\{x\},\qquad C_y=E\cup\{u,y\}.               \tag{4}
\]

Fix a proper six-colouring `phi` of `G-xy`.  Necessarily

\[
 \phi(x)=\phi(y)=\alpha.                                \tag{5}
\]

Put `beta=phi(u)`.  Since `u` is adjacent to every member of `X`, colour
`beta` is absent from `X`.  For every colour
`gamma notin {alpha,beta}`, the usual critical-edge Kempe argument gives
an `alpha`--`gamma` path from `x` to `y` in `G-xy`.  The fifth path is the
literal two-edge path

\[
                         xuy,                            \tag{6}
\]

in colours `alpha,beta`.

## 2. Four distinct operated shore spokes

The four noncentral Kempe paths can be made disjoint inside either named
shore without losing their operation-specific first edges.  Their boundary
ends are not colour-labelled: the construction below is free to permute
the four paths among the selected roots.

### Lemma 1 (four distinct operated shore spokes)

For every `gamma notin {alpha,beta}`, orient an
`alpha`--`gamma` path in the fixed colouring `phi` from `x` towards `y`,
and let `xs_gamma` be its first edge.  If `s_gamma` belongs to `Z`, put
`r_gamma=s_gamma`.  Otherwise `s_gamma` belongs to `F`.

Let

\[
 I_x=\{s_\gamma:s_\gamma\in Z\}.
\]

For every four-set `T subseteq Z` containing `I_x`, there are four paths
from `x` to the four distinct vertices of `T` such that

1. the paths are pairwise vertex-disjoint outside `x`;
2. the path indexed by `gamma` begins with the prescribed edge
   `xs_gamma`; and
3. every nontrivial open path interior belongs to `F`.

The symmetric conclusion holds for the four first edges at `y`, with
`E` in place of `F`.

#### Proof

The first hit of `Z union {y}` on the chosen
`alpha`--`gamma` path belongs to `Z`: the edge `xy` is absent, `F` has no
neighbour at `y`, and a path cannot enter `E` before meeting `Z`.  Before
that first hit the path avoids `u`, whose colour is `beta`.  Consequently
every `s_gamma` lies in `Z` or in `F`.  The four vertices `s_gamma` are
distinct because they have the four distinct colours outside
`{alpha,beta}`.  In particular, the members of `I_x` are distinct.

Put `r=|I_x|`.  Retain the `r` literal paths `xs_gamma` whose second
vertices lie in `I_x`.  Let `A` be the set of the other `4-r` prescribed
second vertices, all of which lie in `F`, and put `B=T-I_x`.  Thus

\[
                         |A|=|B|=4-r.
\]

If `r=4`, the four retained edges already prove the assertion.  Assume
therefore that `r<4`.

We claim that `G[F union B]` contains `4-r` pairwise vertex-disjoint
`A`--`B` paths using every vertex of `A` and every vertex of `B`.  If not,
the set form of Menger's theorem gives an `A`--`B` separator `W`, allowed
to meet the two terminal sets, with

\[
                         |W|\le 3-r.
\]

Some member of `A-W` survives.  Let `Q` be its component in
`G[F union B]-W`.  Since `W` separates `A` from `B`, the set `Q` contains
no member of `B-W`; hence `Q subseteq F-W`.  All exits from `F` lie in
`Z union {x}`, because `F` is anticomplete to `E union {u,y}`.  Moreover
`Q` has no neighbour in `B-W`.  Therefore

\[
 N_G(Q)\subseteq (Z-T)\mathbin{\dot\cup}I_x
                         \mathbin{\dot\cup}\{x\}
                         \mathbin{\dot\cup}W.
\]

The set on the right has order at most

\[
                         2+r+1+(3-r)=6.
\]

It is a genuine separator: `Q` is nonempty, while at least one member of
`B-W` survives and lies outside `Q union N_G(Q)`.  This contradicts
seven-connectivity.  The claimed linkage therefore exists.

Truncate the linkage paths at their first and last terminals, prepend the
prescribed edges `xs_gamma`, and restore the `r` retained literal paths.
The result has four distinct ends, preserves all four named first edges,
and otherwise lies in `F`.  Interchanging `(x,F)` with `(y,E)` proves the
symmetric assertion.  \(\square\)

The freedom in `T` concerns only the four terminal roots.  It does not
preserve which colour reaches which root, does not make the two shore
linkages simultaneous, and does not imply any adjacency between their
terminal-respecting tree contractions.

## 3. The missed edge is non-double-critical

### Lemma 2 (non-double-criticality of the missed edge)

Under (1)--(6),

\[
                         \chi(G-\{x,y\})=6.             \tag{12}
\]

#### Proof

The upper bound follows by restricting a six-colouring of the proper minor
`G-x`.  Suppose that `G-{x,y}` had a proper five-colouring.  The standard
double-critical-edge recolouring says that every one of the five colours
occurs on a common neighbour of `x,y`: if one colour did not, recolour the
neighbours of `x` in that colour with a fresh sixth colour, give `x` the
old colour and `y` the fresh colour.  This would six-colour `G`.

Every common neighbour of `x,y` belongs to `\{u\}\cup Z`.  Indeed, `E`
misses `x` and `F` misses `y`.  At least four of the five distinct common
neighbours therefore belong to `Z`.  Any two of those four vertices are
nonadjacent: together with the edge `xy`, an adjacent pair would form a
literal `K_4` in `G[X]`.  They consequently form an independent four-set
in `G[X]`, contrary to the established equality
`\alpha(G[X])=3` for an exceptional degree-eight vertex.  Thus no
five-colouring exists, proving (12).  \(\square\)

## 4. One operation gives four disjoint two-sided paths

### Theorem 3 (coupled prescribed-path packing)

Fix the colouring `phi` in (5).  For each
`gamma notin {alpha,beta}`, choose an `alpha`--`gamma` path from `x` to
`y` in `G-xy`, and denote its first and last edges by

\[
                         xs_\gamma,\qquad t_\gamma y.   \tag{13}
\]

There are five internally vertex-disjoint `x`--`y` paths, one of which is
`xuy`, such that the other four collectively use every edge `xs_gamma`
and every edge `t_gamma y` in (13).  Pairing of the four first edges with
the four last edges may be permuted.

In particular, the four noncentral path interiors are pairwise disjoint,
avoid `u`, and each meets `Z`.

#### Proof

Put `H=G-{x,y}`.  Lemma 2 gives `chi(H)=6`, while seven-connectivity of
`G` makes `H` five-connected.  The sets

\[
 A=\{u\}\cup\{s_\gamma:\gamma\notin\{\alpha,\beta\}\},
 \qquad
 B=\{u\}\cup\{t_\gamma:\gamma\notin\{\alpha,\beta\}\}
                                                               \tag{14}
\]

have order five: their vertices have the five distinct colours other than
`alpha`.  Apply the audited palette-permutation linkage theorem to `A,B`
in `H`.  Its proof retains every member of `A\cap B` as a trivial path;
in particular, `u` is the trivial path for colour `beta`.  The remaining
four disjoint paths use all four selected first neighbours and all four
selected last neighbours.  Prepending and appending the edges in (13),
and adding `xuy`, proves the packing assertion.

A noncentral path begins in `F\cup Z` and ends in `E\cup Z`; it cannot use
`u`, since the five paths are disjoint outside `x,y`.  As `E,F` are
anticomplete, it must meet `Z`.  Disjointness makes these four boundary
hits distinct.  \(\square\)

### Corollary 4 (full shore fans retaining the operated edges)

There is a full six-fan from `x` to the literal six-set `Z` in
`G[F\cup Z\cup\{x\}]` which retains the four prescribed first edges
`xs_gamma`.  Symmetrically there is such a full six-fan from `y` through
`E`, retaining the four edges `yt_gamma`.

#### Proof

First, an ordinary full `x`--`Z` fan exists.  Otherwise the fan form of
Menger gives a set `C` of order at most five and an `x`-side component `A`
in `G[F\cup Z\cup\{x\}]-C` that contains no member of `Z-C`.  It then has

\[
                         N_G(A)\subseteq C\cup\{u,y\}.
\]

Seven-connectivity forces equality and `|C|=5`.  If `A-{x}` were
nonempty, a component `Q` of it would lie in `F` and satisfy
`N_G(Q)\subseteq C\cup\{x\}`, contradicting seven-connectivity.  Hence
`A={x}`, which gives `d_G(x)=7`, contrary to the established
`delta(G)>=8` in the two-component exceptional-centre branch.

Now make `Z` sinks in the strict gammoid on
`G[(F\cup Z\cup\{x\})-x]` and restrict its ground set to the neighbours of
`x` in `F\cup Z`.  Lemma 1 says that the four distinct first neighbours
`s_gamma` form an independent set of this restricted gammoid.  The ordinary
six-fan says that its rank is six.  Matroid augmentation extends the four
prescribed elements to a basis of order six within the restricted ground
set.  Prepending the six corresponding edges at `x` gives the required full
fan; because `Z` consists of sinks, its open interiors lie in `F`.  The
argument at `y` is symmetric.
\(\square\)

## 5. The nonplanar four-root opportunity and its exact limit

### Lemma 5 (four-connected nonplanar residual)

The graph

\[
                         R=G-\{u,x,y\}                  \tag{15}
\]

is four-connected and nonplanar.

#### Proof

Four-connectivity follows by deleting three vertices from a
seven-connected graph.  The established two-component literal-`K_5`
exclusion gives `delta(G)>=8`.  Each vertex of `E\cup F` loses at most one
neighbour in (15), so it has degree at least seven in `R`; each of the six
vertices of `Z` loses at most three neighbours, so it has degree at least
five.  Moreover `|E|,|F|>=2`, since a singleton nonfull exterior component
would have degree seven in `G`.

Consequently

\[
 \sum_{v\in V(R)}(6-d_R(v))
       \le 6-|E|-|F|\le2.                              \tag{16}
\]

A simple planar graph of order at least three satisfies
`sum_v(6-d(v))>=12`, by Euler's inequality.  Equation (16) is impossible,
so `R` is nonplanar.  \(\square\)

Choose one boundary vertex `z_i` on each of the four noncentral paths in
Theorem 3.  They are distinct.  The rooted-`K_4` theorem of
Fabila-Monroy and Wood therefore gives a `\{z_1,z_2,z_3,z_4\}`-rooted
`K_4` model in `R`: its planar alternative is excluded by Lemma 5.

This is not yet a terminal model.  Its four bags contain the nominated
vertices and hence all meet `N(u)`, but the theorem does not make the bag
rooted at `z_i` contain, or avoid, the operated path through `z_i`.
If the four rooted bags could be chosen so that no bag met a foreign
operated path, absorbing each whole path interior into its own bag would
make all four bags adjacent to `x,y,u`; together with the triangle
`\{x\},\{y\},\{u\}` they would give a `K_7` model.  Thus a surviving
host forces a foreign bag--path intersection in every such rooted model.
Neither the point-rooted theorem nor seven-connectivity bounds the full
neighbourhood exposed by that intersection by seven.  The missing step is
precisely a label-preserving, **set-rooted** absorption theorem, or an
operation-labelled exact-seven separation produced when absorption fails.

## 6. The exact alternative on one side

### Theorem 6 (colour-indexed packing or strict order-seven descent)

Under (1)--(6), one of the following holds on the `x,F` side.

1. **Clean path packing.**  There is a five-set `T_x subseteq S_x`, with
   `y in T_x`, and five paths from `x` to `T_x`, indexed by the five
   colours other than `alpha`, such that:

   - the paths are pairwise vertex-disjoint outside `\{x\}\cup T_x`;
   - the `beta`-path begins with the edge `xu`;
   - for every `gamma notin {alpha,beta}`, the `gamma`-path begins with
     the first edge of an actual `alpha`--`gamma` path from `x` to `y` in
     the fixed colouring `phi`; and
   - the four latter paths avoid `u`, have their open interiors in `F`,
     and end in `T_x cap Z`.

2. **Strict operation-labelled separation.**  There is a nonempty
   connected proper subset `A_x` of `F` and a four-set
   `D_x subseteq C_x-{x}` such that

   \[
   N_G(A_x)=(S_x-T_x)\mathbin{\dot\cup}\{x\}
                    \mathbin{\dot\cup}D_x,              \tag{7}
   \]

   where `T_x` is a five-set containing `y`.  In particular,

   \[
                         |N_G(A_x)|=7.                   \tag{8}
   \]

   The restriction of `phi` to
   `G[A_x union N_G(A_x)]` is proper in the original graph `G`, and its
   exact `alpha`-coloured boundary class contains `x` and at least one
   other vertex.  Thus (7) is an actual order-seven separation carrying
   the named `G-xy` response, and its selected open side has order strictly
   smaller than `F`.

The symmetric alternative holds on the `y,E` side for the same colouring
`phi`.

### Proof

Apply the audited
[critical-edge fan/descent theorem](../results/hc7_exact7_critical_edge_fan_descent.md),
Theorem 3.1, with

\[
 Y=S_x,\qquad C=C_x,\qquad v_{\rm base}=x,
 \qquad x_{\rm boundary}=y.                             \tag{9}
\]

The deleted edge in that theorem is precisely `xy`.  Orient the five
bichromatic paths from `x` towards `y` and stop each at its first vertex of
`S_x`.  The `beta`-path (6) first meets `S_x` at `y`.  Every other path
first meets `S_x` in `Z`: it cannot reach `y` directly because `xy` was
deleted, `F` is anticomplete to `y`, and its two colours exclude the
`beta`-coloured vertex `u`.  Hence the five first-hit vertices, together
with the boundary end `y` required in the cited theorem, occupy at most

\[
                         1+4=5                           \tag{10}
\]

vertices.  Its target-retaining hypothesis is therefore automatic.  Take
any five-set `T_x subseteq S_x` containing those vertices.

The packing conclusion of the cited theorem preserves the five first
edges.  Its four non-`beta` paths avoid `u`, which is used by the preserved
edge `xu`; after leaving `x` they remain in
`C_x-{u,x}=F` until reaching the boundary.  Since `F` has no neighbour
`y`, their ends belong to `T_x cap Z`.  This is outcome 1.

In the other conclusion the cited theorem gives a connected set `A_x`, a
four-set `D_x subseteq C_x-{x}`, and equality (7), together with (8), the
proper inherited colouring, and an exact boundary `alpha`-class containing
`x` and another vertex.  It remains only to locate the new open side.

The vertex `u` does not belong to `A_x`.  Indeed `u` is adjacent to all
seven vertices of `S_x`, whereas (7) says that no member of the nonempty
five-set `T_x` is adjacent to `A_x`.  Since the cited construction also
excludes `x` from `A_x`, it follows from (3) that

\[
                         A_x\subseteq F.                 \tag{11}
\]

This containment is strict.  If `A_x=F`, then the four vertices of
`D_x`, which lie in `C_x-{x}=F\cup\{u\}` and are disjoint from `A_x`,
would all have to lie in the singleton `\{u\}`.  This is impossible.
Thus `|A_x|<|F|`, and outcome 2 has every asserted property.

Interchanging `(x,F,S_x,C_x)` with `(y,E,S_y,C_y)` proves the symmetric
statement without changing `phi`.  \(\square\)

## 7. Consequence and exact limit

### Corollary 7 (two-sided normalization)

For the one fixed colouring `phi` of `G-xy`, either the clean path packing
in Theorem 6 exists on both sides, or at least one of `F,E` contains a
strictly smaller connected open side behind an actual order-seven
separation carrying the inherited `G-xy` colouring and a nontrivial exact
`alpha`-coloured boundary class.

#### Proof

Apply Theorem 6 first to `(x,F)` and then to `(y,E)`.  If neither
application returns its strict-separation outcome, both return their clean
path packing.  \(\square\)

This is a genuine operation-specific normalization: the four noncentral
first edges come from the same `G-xy` colouring, while each strict
alternative retains that colouring on a smaller literal open side.  The
returned side is an exact-seven critical-edge instance, but need not itself
be another exceptional-neighbourhood instance, so no recurrence or
minimality claim is made here.

The path packing alone does not supply the missing branch-set contacts in
the remaining `P_4` or `3K_2` quotient patterns.  Lemma 1 preserves the
four first-edge colour labels but is allowed to permute their four ends,
and a subsequent terminal-respecting tree contraction retains no colour
label on its tree edges.  In particular, the graph
`K_3\vee P_4` admits a six-colouring after deleting one edge of its
triangle in which the two ends have one colour, the third triangle vertex
has a second colour, and four internally disjoint two-edge paths use four
further colours.  Nevertheless its four nontriangle vertices still induce
only `P_4`.  Thus first and last shore contacts cannot be promoted directly
to the absent quotient adjacencies; a completion must spend either the
strict operation-labelled separation in outcome 2 or additional
proper-minor responses at the returned separator.

No finite boundary classification is used in this note.

## Inputs

- [palette-permutation linkage at a non-double-critical adjacent pair](../results/hc7_adjacent_pair_palette_linkage.md)
- [critical-edge fan/descent](../results/hc7_exact7_critical_edge_fan_descent.md)
- [exceptional-neighbourhood structure](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
- [two-component literal-`K_5` exclusion](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
- R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electronic
  Journal of Combinatorics **20** (2013), P64, Theorem 6.
