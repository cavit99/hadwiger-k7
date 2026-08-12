# Coordinate responses at a singleton side

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_singleton_coordinate_localisation_audit.md);
and recorded route nonclosure.  This note does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

The full punctured response cube on the eight-edge forest does not remain
available after passage to a singleton response side.  The exact surviving
signatures are determined by a vertex-cover condition.  A second response
coordinate can nevertheless be introduced at the same singleton unless the
mate of the fixed coordinate dominates its whole neighbourhood.

## 1. The vertex-cover criterion

Let `G` be a graph which is not `q`-colourable, let `D` be a nonempty set of
edges, and let `c` be a proper `q`-colouring of `G-D`.  Put

\[
       M_D(c)=\{xy\in D:c(x)=c(y)\}.                 \tag{1.1}
\]

The set in (1.1) is nonempty, since otherwise `c` would colour `G`.

### Theorem 1.1 (exterior-colouring criterion)

Let `Y` be a nonempty vertex set and suppose that `N_G(Y)` is an actual
separator.  The restriction `c|G-Y` is proper if and only if `Y` is a
vertex cover of `M_D(c)`.  Whenever these equivalent conditions hold, the
equality partition induced by `c` on `N_G(Y)` is rejected by the intact
closed `Y`-side.

#### Proof

Every edge on which `c` can fail to be proper in `G` belongs to `M_D(c)`.
The restriction to `G-Y` is therefore proper exactly when `Y` meets every
edge of `M_D(c)`.

Suppose this condition holds.  If the induced boundary partition extended
through `G[Y\cup N_G(Y)]`, permute the colour names of the extension so
that they agree with `c` on the literal boundary blocks.  Gluing that
extension to `c|G-Y` would give a proper `q`-colouring of `G`, a
contradiction.  `\square`

The criterion concerns the monochromatic deleted edges of one fixed
colouring.  Merely deleting further edges does not give their signatures a
trace on `Y`.

## 2. Exact localisation of the eight-coordinate cube

Assume now the forced eight-coordinate setting.  Thus `G` is the
minor-minimal seven-chromatic, `K_7^-`-minor-free critical host, `F_8` is a
componentwise-induced forest of type

\[
                    8K_2\quad\hbox{or}\quad6K_2\mathbin{\dot\cup}P_3,
                                                               \tag{2.1}
\]

and the proper six-colourings of `H=G-F_8` realise exactly the nonempty
signatures on `F_8`.

Let `u` be an endpoint of `e=uv\in F_8`, and suppose that `\{u\}` is an
actual response side.  For each nonempty `J\subseteq F_8`, fix a
signature-`J` colouring `c_J` of `H` and restore every edge of `F_8`.

### Corollary 2.1 (singleton localisation)

The restriction `c_J|G-u` is proper, and hence gives a rejected trace on
the singleton side, if and only if

\[
                         J\subseteq \delta_{F_8}(u). \tag{2.2}
\]

Consequently:

1. if `d_{F_8}(u)=1`, the sole forest signature carried by the singleton
   is `\{e\}`; and
2. if `u` is the central vertex of the induced `P_3` component, with
   incident edges `e,f`, the same singleton carries precisely the three
   signatures `\{e\}`, `\{f\}`, and `\{e,f\}`.

In the second case these three responses live on the common graph
`G-\{e,f\}`.  This graph is seven-connected, the original exact spanning
`K_7^vee` model remains exact in it, and all three boundary responses occur
on the one literal boundary `N_G(u)`.

#### Proof

After all forest edges are restored, the monochromatic-edge set of `c_J`
is exactly `J`.  The singleton `\{u\}` is a vertex cover of `J` exactly
when every edge in `J` is incident with `u`, so Theorem 1.1 proves (2.2)
and the two listed possibilities follow from (2.1).

In the induced-path case, adding the other six forest edges to `H` gives
`G-\{e,f\}`, so seven-connectivity is preserved.  The spanning model in
`H` remains a model after edges are added and is exact already in `G`.
`\square`

Thus the quantifier supplied by the punctured eight-cube is

\[
 \forall\varnothing\ne J\subseteq F_8\ \exists c_J,
\]

but at a degree-one forest endpoint the exterior-colouring condition
retains only `J=\{e\}`.  Comparing `\{e\}`, `\{f\}`, and `\{e,f\}` on
`N_G[u]` for a forest edge `f` disjoint from `u` would be invalid: the
monochromatic edge `f` remains in `G-u`.

## 3. A fresh incident coordinate or a dominated edge

The following fork replaces the unavailable disjoint forest coordinate by
an edge incident with the singleton.  It is stated separately because its
near-clique models need not agree with the original eight-coordinate
model.

### Theorem 3.1 (singleton two-edge fork)

Retain the critical-host hypotheses and let `e=uv` be an edge for which a
fixed proper six-colouring `c_e` of `G-e` makes `e` monochromatic.  Suppose
that `\{u\}` is an actual response side.  Then at least one of the
following alternatives holds.

1. There is a neighbour `w\in N_G(u)-\{v\}` with `vw\notin E(G)`.  Put

   \[
                          f=uw,\qquad Q=G-\{e,f\}.   \tag{3.1}
   \]

   Then:

   - `Q` is exactly six-chromatic and its edge-equality signatures on
     `\{e,f\}` are precisely

     \[
                         \{e\},\qquad\{f\},\qquad\{e,f\}; \tag{3.2}
     \]

   - the `\{e\}` corner in (3.2) may be chosen to be the original
     colouring `c_e`;
   - every colouring in (3.2), restricted to `G-u`, gives a rejected
     exterior trace on the same singleton boundary `N_G(u)`;
   - each of `G/e`, `G/f`, and `G/\{e,f\}` is exactly six-chromatic, and
     `G/\{e,f\}` has a spanning `K_6`-minor model whose lift co-bags the
     induced path `v-u-w`; and
   - `Q` is at least five-connected and has a spanning exact
     `K_7^vee`-minor model.

2. The mate `v` is adjacent to every other neighbour of `u`.  Hence

   \[
        N_G(u)-\{v\}\subseteq N_G(v),\qquad
        |N_G(u)\cap N_G(v)|\ge d_G(u)-1\ge7.         \tag{3.3}
   \]

   In the target-free critical host, the graph

   \[
                            G[N_G(u)-\{v\}]          \tag{3.4}
   \]

   is triangle-free and has no `K_5^-` minor.  Under `c_e` it uses all
   five colours other than the common colour of `u,v`.

   If those common neighbours meet five branch sets of any `K_5` submodel
   avoiding `u,v`, then `G` contains a `K_7` minor.  In particular this
   applies to five pairwise adjacent branch sets of the original exact
   `K_7^vee` model, provided they avoid `u,v`.

#### Proof

If the second alternative fails, choose `w` as in the first.  The three
vertices `v,u,w` induce a path.  The graph `Q` is a proper minor and is
therefore at most six-chromatic.  If it were five-colourable, recolouring
`u` with one fresh sixth colour would permit both deleted incident edges to
be restored and would six-colour `G`.  Thus `chi(Q)=6`.

The original colouring `c_e` is proper on `Q`, makes `e` monochromatic,
and makes `f` proper because `f` is present in `G-e`.  Contracting `f` and
expanding its ends gives the signature `\{f\}`.  Contracting the induced
path `v-u-w` to one vertex and expanding it gives the signature
`\{e,f\}`.  The empty signature would colour `G`, so (3.2) is the exact
signature language.  The singleton meets every monochromatic deleted edge
in all three cases, and Theorem 1.1 attaches the asserted traces.

Every displayed contraction is a proper minor and hence at most
six-chromatic.  A five-colouring after contracting one edge could be
expanded by retaining the contracted colour at one end and assigning a
fresh sixth colour to the other.  A five-colouring after contracting the
whole induced path could be expanded by giving `v,w` the contracted colour
and `u` a fresh sixth colour.  Either construction would six-colour `G`.
Thus all three contraction graphs are exactly six-chromatic.  Hadwiger's
conjecture for parameter six gives a `K_6` model in the double contraction;
connectedness permits it to be made spanning, and expansion co-bags the
whole path.

Deleting one edge lowers vertex-connectivity by at most one.  Since `G` is
seven-connected, `Q` is at least five-connected.  Also

\[
                         |E(Q)|\ge4|V(G)|-2.         \tag{3.5}
\]

The Norin--Totschnig density theorem therefore gives a `K_7^vee` model in
`Q`; its small exceptional graph is excluded by `|V(G)|\ge25`.  Make the
model spanning.  If either nominally missing branch-set pair became
adjacent when `e,f` were restored, the same branch sets would give a
`K_7^-` model in `G`.  Target exclusion therefore makes the model exact.

It remains that no such `w` exists.  Then (3.3) is immediate from
`delta(G)\ge8`.  A triangle in (3.4), together with the adjacent universal
vertices `u,v`, would be a literal `K_5`, which the critical host excludes.
A `K_5^-` model in (3.4), together with the singleton branch sets
`\{u\},\{v\}`, would be a `K_7^-` model.  This proves the two structural
exclusions.

Finally `c_e(u)=c_e(v)`.  Every other neighbour of `u` avoids that colour.
All six colours must occur on `N_G(u)`, since otherwise the missing colour
could be assigned to `u` in `c_e|G-u`.  Hence (3.4) uses every one of the
other five colours.

For the final assertion, let `A_1,\ldots,A_5` be five pairwise adjacent
connected branch sets, disjoint from `u,v`, each meeting
`N_G(u)-\{v\}`.  The dominated-edge hypothesis makes each `A_i` adjacent
to both `u` and `v`, while `uv` is an edge.  Thus

\[
                     \{u\},\{v\},A_1,\ldots,A_5
\]

are seven pairwise adjacent connected branch sets, giving a `K_7` minor.
`\square`

## 4. Exact consequence and nonclosure

Theorem 3.1 gives a genuine common two-edge operation at every singleton
except the dominated-edge residue (3.3).  It does not yet terminalise the
eight-coordinate branch:

- unless `u` is the centre of the original induced `P_3`, the second edge
  is not an `F_8` coordinate;
- the new exact `K_7^vee` model and the co-bagged `K_6` model are separately
  existential and need not agree with one another or with the original
  eight-coordinate model; and
- in alternative 2, the fixed colouring supplies five common-neighbour
  colours, but no theorem presently aligns them with five pairwise adjacent
  branch sets of the exact model.  The exact statement available is only

  \[
   \forall\alpha\ne c_e(u)\ \exists x_\alpha\in N(u)\cap N(v)
        \text{ of colour }\alpha,
  \]

  whereas the model composition needs five different `K_5`-model bags to
  meet that common neighbourhood.  A single large branch set may contain
  several or all of the five colour witnesses.

Accordingly the proposed inference

\[
 \text{full eight-coordinate cube}
 \quad\Longrightarrow\quad
 \text{a second forest-coordinate response on every singleton side}
\]

is false at the level of its quantifiers.  The smallest positive repair is
now the following disjunction: terminalise the common induced-path state in
Theorem 3.1(1), or eliminate the triangle-free, `K_5^-`-minor-free dominated
common-neighbour residue in Theorem 3.1(2) using the original exact-model
provenance.

## Dependencies

- [forced eight-coordinate growth](../results/hc7_k7minus_bounded_feedback_degree_elimination.md#corollary-2-forced-eight-coordinate-growth)
- [endpoint visibility](../results/hc7_k7minus_eight_coordinate_endpoint_visibility.md)
- [fixed-coordinate side reduction](../results/hc7_k7minus_fixed_coordinate_response_core_reduction.md)
- Norin--Totschnig, Theorem 6, for the density-to-`K_7^vee` implication
