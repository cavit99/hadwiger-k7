# Changing the deleted edge at a model-anchored response side

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_operation_provenance_exchange_audit.md);
and recorded route nonclosure.  This note does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

Allowing the deleted edge to change collapses every model-anchored response
side to a singleton.  The resulting singleton supports a complete
three-corner response square on an induced path.  What need not survive is
the labelled exact minor model which supplied the original side.

If instead the original eight-forest coordinate is retained and compared
with a fresh appendage edge, the common deletion has one of three exact
signature languages.  The comparison gives either a boundary partition
which six-colours the host or a rigid obstruction: the appendage sees both
ends of the old coordinate, or two nonempty boundary-partition languages on
the same separator are disjoint.  A third equality corner, when it exists,
does not itself exchange the operation provenance.

## 1. Setting

Let `G` be a minor-minimal seven-chromatic graph with no `K_7^-` minor.
Use the standard critical-host consequences

\[
  \kappa(G)\ge7,\qquad \delta(G)\ge8,\qquad
  |E(G)|\ge4|V(G)|,
\]

and the fact that `G` contains no `K_5` subgraph.

Let

\[
                         P,B,C,U_1,U_2,U_3,U_4        \tag{1.1}
\]

be a labelled exact `K_7^vee`-minor model in `G`.  Let `R` be one universal
branch set, let `D` be a foreign branch set, and suppose that
`empty != Z subsetneq R` is connected, `R-Z` is connected, and `D` is
anticomplete to `Z`.  These are the geometric parts of a model-anchored
response configuration.

For this note, an **operation-changing model-anchored response side** means
the same geometric data, together with an arbitrary selected edge meeting
the side and a proper six-colouring of its deletion whose induced boundary
partition is rejected by the intact side.  Thus the selected edge need not
belong to `F_8`.  Statements which retain an `F_8` coordinate say so
explicitly.

## 2. Operation-changing singleton normalisation

### Theorem 2.1

There is a vertex `u in Z` such that `R-u` is connected.  For every edge
`uv`, a proper six-colouring of `G-uv`, together with the same exact model,
the same universal branch set `R` and the same far branch set `D`, makes
`{u}` an operation-changing model-anchored response side.

Moreover, `u` has two nonadjacent neighbours `v,w`.  For

\[
             e=uv,\qquad f=uw,\qquad Q=G-\{e,f\},     \tag{2.1}
\]

the three vertices `v,u,w` induce a path and all of the following hold.

1. `Q` is exactly six-chromatic and its equality signatures on
   `\{e,f\}` are precisely

   \[
                       \{e\},\qquad\{f\},\qquad\{e,f\}.             \tag{2.2}
   \]

2. Every colouring in (2.2) gives a rejected exterior trace on the one
   actual boundary `N_G(u)`.
3. The three contractions `G/e`, `G/f` and `G/\{e,f\}` are exactly
   six-chromatic.  A spanning `K_6` model lifted from the last contraction
   co-bags the path `v-u-w`.
4. The graph `Q` is at least five-connected and has a spanning exact
   `K_7^vee` model.

#### Proof

If `Z={u}`, then `R-u=R-Z` is connected.  Otherwise choose a spanning tree
of `G[Z]`, rooted at a vertex which has an edge to `R-Z`, and take a leaf
`u` different from the root.  Joining that tree to a spanning tree of
`G[R-Z]` shows directly that `R-u` is connected.

Let `uv` be any incident edge and let `c` be a proper six-colouring of the
proper minor `G-uv`.  Its ends have the same colour, since otherwise `c`
would colour `G`.  Removing `u` removes the sole improper edge, so `c|G-u`
is proper.  Its boundary partition cannot extend through `G[N_G[u]]`, or
the two colourings would align and six-colour `G`.  The boundary is actual
because the nonempty branch set `D` is anticomplete to `u`.  The connectivity
of `R-u` and the unchanged labelled model prove the first assertion.

The neighbourhood `G[N_G(u)]` contains no `K_4`, since such a subgraph
together with `u` would be a literal `K_5`.  In particular it is not
complete, so choose nonadjacent neighbours `v,w`.  The remaining assertions
are exactly the singleton two-edge fork applied to the actual response side
`{u}`.  \(\square\)

Theorem 2.1 shows that minimising model-anchored sides over all edge
operations always stops at a singleton.  The non-singleton appendage form is
possible only because its minimisation retains a member of the fixed
eight-edge forest.  Here the unchanged exact model is a model in `G`
anchoring the singleton response.  No claim has yet been made that it
survives either selected edge deletion; that separate question is exact in
the next proposition.

### Proposition 2.2 (exact persistence of the old model)

Retain the notation of Theorem 2.1.  The labelled model (1.1) itself remains
a model in the common deletion `Q` if and only if both of the following
conditions hold.

1. The set `Q[R]` is connected.  Since `R-u` is connected, this is
   equivalent to

   \[
       \bigl(N_G(u)\cap(R-u)\bigr)-\{v,w\}\ne\varnothing.          \tag{2.3}
   \]

2. For every foreign branch set `S` required to be adjacent to `R` in
   (1.1),

   \[
                    E_G(R,S)-\{uv,uw\}\ne\varnothing.             \tag{2.4}
   \]

If either condition fails, the exact model supplied by item 4 of Theorem
2.1 is a separately existential model: there is no justified identification
of its universal branch sets or far branch set with the labels in (1.1).

#### Proof

Both deleted edges are incident with `u in R`.  Thus no branch set other
than `R` can lose an internal edge, and no required adjacency not incident
with `R` can be lost.  The set `R-u` remains connected, so `u` is joined to
it in `Q[R]` exactly under (2.3).  A required adjacency from `R` to a
foreign branch set survives exactly under (2.4).  Edge deletion creates no
new optional adjacency, proving necessity and sufficiency.

The density model in `Q` is obtained after the old labels have been
discarded.  Existence of that model therefore supplies no relabelling or
branch-set equality with (1.1).  \(\square\)

The obstruction in Proposition 2.2 is exact rather than numerical.  The
two selected edges may contain every internal attachment of `u` to `R-u`,
or an edge may be the sole contact realising one required model adjacency.
Neither seven-connectivity nor the response square by itself rules this
out.

## 3. Comparing an old forest coordinate with an appendage edge

Now use the terminal form from the model-ownership theorem.  Thus

\[
              Z=K\mathbin{\dot\cup}A_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}A_t,\qquad 1\le t\le2,       \tag{3.1}
\]

where `K` is connected and boundary-list-critical, every appendage is
connected and contains no endpoint of the eight-edge forest `F_8`, and
`K` contains the end or ends of the fixed coordinate needed by its
singleton-signature colouring.

Fix one appendage `A`, choose an attachment edge

\[
                   g=ak,\qquad a\in A,\quad k\in K,                 \tag{3.2}
\]

and let `e in F_8` be the fixed coordinate.  Put

\[
                              Q=G-\{e,g\}.                          \tag{3.3}
\]

Write `E` when the ends of a selected edge have equal colours and `P` when
they have different colours; signatures below are ordered as `(e,g)`.

### Theorem 3.1 (exact signature classification)

Exactly one of the following geometries and signature languages occurs.

1. If `e` and `g` are disjoint, the realised signatures are exactly

   \[
                              EP,\quad PE,\quad EE.                 \tag{3.4}
   \]

2. If they share an endpoint and their two outer endpoints are nonadjacent,
   they form an induced `P_3`, and the realised signatures are again
   exactly (3.4).  In this case `Q` and the contraction of the whole path
   are exactly six-chromatic.
3. If they share an endpoint and their outer endpoints are adjacent, the
   three vertices form a triangle, and the realised signatures are exactly

   \[
                                   EP,\quad PE.                     \tag{3.5}
   \]

   The `EE` corner is impossible.

In every case `Q` is at least five-connected and has a spanning exact
`K_7^vee` model.  Each of `G/e` and `G/g` is exactly six-chromatic.

#### Proof

The singleton-signature colouring of `G-e` remains proper on `g`, so it
gives `EP`.  A proper six-colouring of `G-g` must make the ends of `g`
equal and remains proper on `e`, so it gives `PE`.  The signature `PP`
would be a proper six-colouring of `G` and is impossible.

For disjoint edges, expand a six-colouring after contracting both edges.
For an induced path, expand a six-colouring after contracting the whole
path.  These give `EE`.  In the triangle case, an `EE` colouring would give
the same colour to the adjacent outer endpoints, so it is impossible.
This proves the exact lists (3.4)--(3.5).

If the two edges are incident and `Q` were five-colourable, assigning one
fresh sixth colour to their common endpoint would restore both edges and
six-colour `G`.  Thus `Q` is exactly six-chromatic in both incident
geometries.  In the induced-path case, a five-colouring after contracting
the path expands by giving the common endpoint a fresh sixth colour, so
that contraction is also exactly six-chromatic.  The same fresh-colour
argument for one contracted edge proves that `G/e` and `G/g` are exactly
six-chromatic in all three geometries.

Deleting two edges from a seven-connected graph leaves a five-connected
graph.  Also `|E(Q)|>=4|V(G)|-2`.  The Norin--Totschnig density theorem,
with its small exception excluded by `|V(G)|>=25`, gives a `K_7^vee` model
in `Q`.  Make it spanning.  Target exclusion makes it exact, since either
additional nominally missing adjacency would give `K_7^-`.  \(\square\)

The proof deliberately makes no exact-six claim for the double contraction
in the disjoint case.  A five-colouring of two co-bagged disjoint pairs need
not expand with only one fresh colour.

## 4. Exact localisation and the boundary-partition alternative

Let

\[
                                S=N_G(A).                            \tag{4.1}
\]

This is an actual boundary: the far branch set `D` is anticomplete to
`A subseteq Z`.  The response chambers from Theorem 3.1 localise as follows.

### Theorem 4.1

1. On the exterior `G-A`, precisely the `PE` chamber is proper.  It gives
   the fresh attachment-edge response on `A`.
2. Every realised chamber is proper on each exterior `G-K` and `G-Z`, and
   hence gives a rejected response on those connected sets.
3. An `EP` colouring is proper on the closed side `G[N_G[A]]` if and only
   if

   \[
                               V(e)\not\subseteq S.                 \tag{4.2}
   \]

   Neither a `PE` nor an `EE` colouring is proper on that closed side.
4. Consequently, either

   \[
                               V(e)\subseteq N_G(A),                \tag{4.3}
   \]

   or the following two nonempty languages of equality partitions of the
   same boundary `S` are disjoint:

   - partitions induced by `EP` colourings on the intact closed `A`-side;
   - partitions induced by `PE` colourings on the exterior `G-A`.

   If the two languages intersect, `G` is six-colourable.

In the second alternative, `Q` is exactly six-chromatic and the triangle
geometry cannot occur.  In the first alternative, the triangle geometry
always satisfies (4.3).

#### Proof

The appendage contains neither end of any member of `F_8`.  Therefore an
`EP` or `EE` colouring leaves the monochromatic edge `e` wholly in `G-A`
and is not proper there.  A `PE` colouring has only `g` monochromatic, and
deleting `A` removes its endpoint `a`.  This proves item 1.

The set `K` meets `e` and contains `k`, so it meets every monochromatic
edge in each realised chamber.  The same holds for `Z`.  The exterior
restrictions are proper and their boundary partitions are rejected, since
an extension through the corresponding intact closed side would glue to a
six-colouring of `G`.  Their boundaries are actual because `D` is
anticomplete to `Z`, and hence to `K`.  This proves item 2.

On the closed `A`-side, the edge `g` is present between `a in A` and
`k in S`.  Hence every `PE` or `EE` colouring is improper there.  In an
`EP` colouring the edge `g` is proper, and its only improper edge is `e`.
Since neither end of `e` lies in `A`, this edge belongs to the closed side
exactly when both its ends belong to `S`.  This proves item 3.

Assume (4.2).  Both displayed partition languages are nonempty by Theorem
3.1.  If an `EP` closed-side colouring and a `PE` exterior colouring induced
the same equality partition on `S`, permute the names of the colours on one
side and glue them.  This would give a proper six-colouring of `G`.
Therefore the languages are disjoint unless that terminal conclusion holds.

It remains to prove the chromatic assertion.  For incident edges it was
proved in Theorem 3.1.  Suppose that the edges are disjoint and that `Q` has
a five-colouring.  Its signature cannot be `EP` or `PE`, since recolouring
one endpoint of the sole equal pair with a fresh sixth colour would
six-colour `G`.  It is therefore `EE`.  If some endpoint of `e` were
nonadjacent to some endpoint of `g`, recolouring those two vertices with the
same fresh sixth colour would again six-colour `G`.  Thus all four cross
edges are present.  In particular `a` is adjacent to both ends of `e`,
which gives (4.3), contrary to (4.2).  Hence `chi(Q)=6` in the second
alternative.

Finally, in the triangle geometry the end of `e` shared with `g` is
adjacent to `a` through `g`, and its other end is adjacent to `a` through
the third triangle edge.  Both ends of `e` lie in `N_G(A)`, proving the
last assertion.  \(\square\)

The `EE` chamber does not bridge the two languages in Theorem 4.1.  It is
improper on `G-A` because `e` survives there and improper on the closed
`A`-side because `g` survives there.  Its existence is a common colouring
of the deletion graph, not a colouring of either shore required for gluing.

## 5. Model provenance and exact nonclosure

The density model in the common deletion `Q` is a genuine common model for
all realised signatures.  It need not be the old labelled model.  For that
old model the only possible changes occur at its branch set `R`: it survives
in `Q` exactly when `Q[R]` is connected and every required adjacency from
`R` to another named branch set retains an edge after `e` and `g` are
deleted.  The fresh edge `g` is internal to `R`; the old coordinate `e`
may be internal to `R` or may realise an external model contact.

Thus the strongest operation-provenance exchange currently justified is

\[
\begin{array}{c}
  \text{a six-colouring of }G,\quad\text{or}\quad
  V(e)\subseteq N_G(A),\quad\text{or}\quad
  \mathcal P^{\rm in}_{EP}(S)\cap
       \mathcal P^{\rm out}_{PE}(S)=\varnothing.                 \tag{5.1}
\end{array}
\]

Meanwhile `K` carries every realised response but is not an anchored side
for the fixed model, because `R-K` has both `A` and `R-Z` as distinct
components.  The appendage `A` is an anchored side for `g` but carries no
forest-coordinate response.  This is the exact quantifier mismatch:

\[
\begin{array}{c}
  \text{fixed forest coordinate and disconnected branch complement at }K,\\
  \text{connected branch complement and fresh-edge response at }A.
\end{array}                                                       \tag{5.2}
\]

The three-corner response square does not repair (5.2), and the triangle
case has only two corners.  A positive continuation must use the physical
interaction of the two partition languages with the appendage's two
monopolised model labels.  Merely selecting the `EE` colouring, a new
density model, or another minimum response side does not retain both the
forest coordinate and the original branch labels.

This is a recorded route nonclosure, not a counterexample to an
operation-sensitive model-transfer theorem.

## 6. Dependencies

- [model ownership and coordinate avoidance](hc7_k7minus_model_anchored_appendage_ownership.md);
- [coordinate responses at a singleton side](hc7_k7minus_singleton_coordinate_localisation.md);
- [model-anchored response hull](hc7_k7minus_model_anchored_response_hull.md); and
- [eight-coordinate endpoint visibility](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md).
