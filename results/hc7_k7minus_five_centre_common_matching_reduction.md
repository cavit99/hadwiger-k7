# A common five-edge response host for five exceptional centres

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_common_matching_reduction_audit.md`](hc7_k7minus_five_centre_common_matching_reduction_audit.md).
This is an unbounded, computation-free reduction.  It does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,                       \tag{1.1}
\]

and suppose

\[
 \kappa(G)\geq7,\qquad |E(G)|\geq4|V(G)|,
 \qquad \delta(G)\geq8,\qquad K_5\not\subseteq G,
 \qquad |V(G)|\geq25.                              \tag{1.2}
\]

Fix five independent degree-eight vertices

\[
                         Z=\{z_1,\ldots,z_5\},       \tag{1.3}
\]

and assume, as supplied in the critical host by the audited
[exceptional-neighbourhood theorem](hc7_k7minus_exceptional_neighbourhood_completion.md),
that

\[
                         \alpha(G[N_G(z)])=3
                         \qquad(z\in Z).             \tag{1.4}
\]

Put `F=G-Z`.

## 2. Five chosen responses on one deleted matching

### Lemma 2.1 (five singleton-colour neighbours)

For every `z in Z`, there are an independent triple
`I_z subseteq N_G(z)` and a proper six-colouring `phi_z` of `G-z` such
that the five vertices in

\[
                         R_z=N_G(z)-I_z              \tag{2.1}
\]

receive five distinct colours, none equal to the common colour on `I_z`.

#### Proof

Choose an independent triple `I_z` using (1.4), contract the connected star
`G[\{z\} union I_z]`, and six-colour the resulting proper minor.  Expanding
the contracted vertex gives a proper colouring of `G-z` in which `I_z` is
monochromatic.  Every vertex of `R_z` avoids that colour because it is
adjacent to the contracted star.

If the five vertices of `R_z` used at most four further colours, at most
five colours would occur on `N_G(z)`.  A missing sixth colour could then be
assigned to `z`, contrary to `chi(G)=7`.  Thus the colours on `R_z` are
pairwise distinct. `\square`

The five sets `R_z` have a system of distinct representatives: every
nonempty subfamily has union of order at least five, which is at least the
number of its members.  Choose

\[
                         x_z\in R_z\qquad(z\in Z)     \tag{2.2}
\]

with all five `x_z` distinct, and set

\[
 M=\{e_z:z\in Z\},\qquad e_z=zx_z,\qquad H=G-M.     \tag{2.3}
\]

Because `Z` is independent, none of the representatives lies in `Z`.
Hence `M` is a matching.

For a proper six-colouring `psi` of `H`, define its matching signature by

\[
 \Sigma_M(\psi)=\{e_z\in M:\psi(z)=\psi(x_z)\}.     \tag{2.4}
\]

### Theorem 2.2 (the punctured Boolean response cube)

For every nonempty `J subseteq M`,

\[
                         \chi(G-J)=\chi(G/J)=6.       \tag{2.5}
\]

Moreover, the matching signatures of the proper six-colourings of `H` are
exactly

\[
                         2^M-\{\varnothing\}.         \tag{2.6}
\]

For each `z`, the colouring `phi_z` from Lemma 2.1, extended to `z` with
the colour of `x_z`, is a colouring of `H` with signature exactly
`\{e_z\}`.

For every nonempty `J subseteq M`, one may choose a signature-`J`
colouring `psi_J` such that its restriction `theta_J` to `F` satisfies

\[
 \varnothing\ne\operatorname{Sat}(\theta_J)
 \subseteq\{z:e_z\in J\},                           \tag{2.7}
\]

where a centre is saturated when all six colours occur on its
neighbourhood.  In addition, `G-J` has a spanning `K_6`-minor model, and
`G` has a spanning `K_6`-minor model in which the ends of every edge of
`J` lie in the same branch set.

#### Proof

Both `G-J` and `G/J` are proper minors, so they are at most six-chromatic.
Suppose that `G-J` had a five-colouring.  Recolour every centre incident
with an edge of `J` with one new sixth colour.  Those centres are
independent, and the new colour occurs nowhere else.  This restores every
edge of `J` and gives a six-colouring of `G`, a contradiction.

A five-colouring of `G/J` expands to a five-colouring of `G-J`, because
the edges in `J` are pairwise vertex-disjoint.  The same recolouring gives
the same contradiction.  This proves (2.5).

Now six-colour `G/J` and expand each contracted edge.  On the common
subgraph `H`, precisely the edges in `J` have equal-coloured ends.  Every
edge of `M-J` remains an edge between two distinct contraction bags, so its
ends receive distinct colours.  Thus every nonempty subset of `M` occurs
as a signature.  The empty signature would be a proper six-colouring of
`G`, so it cannot occur.

Finally, all six colours occur on `N_G(z)` under `phi_z`, and every colour
except the colour on `I_z` occurs there exactly once.  Giving `z` the
colour of `x_z` therefore makes `e_z` the unique monochromatic edge incident
with `z`; all other matching edges are already proper edges of `G-z`.
This gives the asserted singleton signature.

For (2.7), take `psi_J` by expanding a six-colouring of `G/J`.  If `e_z`
is not in `J`, all edges incident with `z` are proper under `psi_J`, so the
displayed colour of `z` is absent from `theta_J(N_G(z))`; hence `z` is not
saturated.  If no centre indexed by `J` were saturated, assign to each of
those independent centres a colour missing from its neighbourhood.  This
would six-colour `G`.

Finally, `G-J` and `G/J` are connected and exactly six-chromatic, so
`HC_6` gives a `K_6` minor in each.  Absorb unused components into the
branch sets to make both models spanning.  The first is the asserted model
in `G-J`.  Expanding the contracted matching edges in the second, using
the edges of `J` inside their bags, gives the co-bagged spanning model in
`G`. `\square`

In particular,

\[
 \chi(H)=6,\qquad |E(H)|\geq4|V(H)|-5.              \tag{2.8}
\]

Theorem 2.2 is stronger than five unrelated centre-deletion colourings:
all 31 nonempty endpoint-equality patterns occur on one literal graph.

### Corollary 2.3 (five literal response-bearing separators)

For every `e=zx_z in M`, there is a nonempty connected set `Y_e` which
contains exactly one end of `e` and whose open neighbourhood is an actual
separator of `G` of order at least seven.  A singleton-signature colouring
of `H` is proper on `G-Y_e`, and its exact precolouring of `N_G(Y_e)` does
not extend over `G[Y_e union N_G(Y_e)]`.

#### Proof

Apply the audited
[minimal contraction-bag theorem](hc7_contracted_edge_k6_model_normalization.md)
to `G/e`.  Lifting its root bag separates the two ends of `e` into
connected adjacent sets.  If both retained all five external model
contacts, the five external bags and those two sets would form a `K_7` minor,
and hence a `K_7^-` minor.  Thus one of the two sets, call it `Y_e`, has an
actual open-neighbourhood separator.  It contains exactly one end of `e`,
and seven-connectivity gives `|N_G(Y_e)|>=7`.

Take a six-colouring of `H` with signature exactly `\{e\}`.  Its only
monochromatic edge after restoring `M` is `e`, and deleting `Y_e` removes
that edge.  The colouring is therefore proper on `G-Y_e`.  An extension of
its boundary precolouring through `Y_e` would glue to a six-colouring of
`G`, which is impossible. `\square`

## 3. Cuts of the common host

For a vertex cut `S` of `H`, let `Q_S` be the multigraph whose vertices are
the components of `H-S`.  Each edge of `M` with ends in different
components gives one edge of `Q_S`; edges of `M` incident with `S`, or with
both ends in one component, are omitted.

### Lemma 3.1 (matching edges lift component cuts)

If `|S|=k<=3`, then

\[
                         \lambda(Q_S)\geq7-k,         \tag{3.1}
\]

where `lambda` is edge-connectivity.  Consequently `H` is at least
two-connected.

#### Proof

The graph `G-S` is `(7-k)`-connected and therefore `(7-k)`-edge-connected.
Partition the components of `H-S` into two nonempty classes.  The only
edges of `G-S` between the corresponding unions are precisely the edges of
`M` represented in that cut of `Q_S`.  Hence every edge cut of `Q_S` has
order at least `7-k`, proving (3.1).

Deleting at most five edges cannot disconnect the at least
six-edge-connected graph `G-S` when `k<=1`.  Thus `H` is connected and has
no cut of order at most one. `\square`

### Theorem 3.2 (the connectivity trichotomy)

Exactly one of the following holds.

1. **A two-cut.**  If `kappa(H)=2`, then for every two-cut `S` the graph
   `H-S` has exactly two components and all five edges of `M` run between
   them.  All `32` endpoint transversals of those matching edges, together
   with `S`, are exact order-seven cuts with two full complementary
   components.  The set `S` is a two-cut of `F`.  Applying the audited
   [five-centre two-cut theorem](hc7_k7minus_five_centre_two_cut_reduction.md)
   gives exactly two components `C,D` of `F-S`.  For each `z in Z`, the
   selected neighbour `x_z` is the unique neighbour of `z` in one of
   `C,D`; if

   \[
                            \rho_z=|N_G(z)\cap S|,
   \]

   then `z` has `7-rho_z` neighbours in the other component.  Equivalently,
   the other seven neighbours of `z` all lie in the opposite closed shore,
   consisting of that component together with `S`.  Hence every one of the
   five centres has a singleton open-shore contact, with at least three
   singleton contacts on the same shore.

2. **A three-cut.**  If `kappa(H)=3`, then for every three-cut `S` the graph
   `H-S` has exactly two components, and exactly four or five edges of `M`
   run between them.  If four run between them, choosing one end of each
   gives `16` proper order-seven separators of `G`; choosing the four
   centre ends gives a separator consisting of `S` and four exceptional
   centres.  If all five run between them, the `32` endpoint choices give
   proper order-eight separators of `G`, including `S union Z`.  Every one
   of the `30` mixed choices either exposes an exact order-seven cut or is
   itself an order-eight cut with exactly two full complementary
   components.  In either case `S-Z` separates `F`.  If `S` contains a
   centre, `S-Z` is a two-cut of `F`; otherwise `S` is a three-cut of `F`.
   Hence, in the branch `kappa(F)>=3`, the set `S` avoids `Z` and is a
   three-cut of `F` crossed by four or five selected centre edges.

3. **A four-connected common host.**  If `kappa(H)>=4`, then `H` has a
   spanning `K_7^\vee` model, where `K_7^\vee` is obtained from `K_7` by
   deleting two incident edges.  In a target-free `G`, the audited
   [exact `K_7^\vee` dichotomy](hc7_k7minus_exact_k7vee_separator_dichotomy.md)
   then supplies a nonempty proper connected subset of one of the six
   mutually adjacent model bags whose connected complement in that bag has
   an actual open neighbourhood separator in `G`, of order at least seven.

#### Proof

Let `S` be a cut of order `k in \{2,3\}`.  By Lemma 3.1, every vertex of
`Q_S` has degree at least `7-k`.  Since `Q_S` has at most five edges,

\[
                         (7-k)|V(Q_S)|\leq2|E(Q_S)|\leq10. \tag{3.2}
\]

As `Q_S` has at least two vertices, it follows that it has exactly two.
For `k=2`, the five edges of `M` all cross between them.  For `k=3`, four
or five do.

Write the two components as `A,D`, and let `P_A,P_D` be the respective
sets of ends of the crossing matching edges.  Minimum-cut fullness in `H`
and the definition of `H` give the literal identities

\[
 N_G(A)=S\mathbin{\dot\cup}P_D,
 \qquad N_G(D)=S\mathbin{\dot\cup}P_A.               \tag{3.3}
\]

Thus both displayed component boundaries have order `k+|P_A|`, and the
component is adjacent to every vertex of its boundary.

Every component `A` of `H-S` has order at least `8-k`, since
`delta(H)>=7` and every neighbour in `H` of a vertex in `A` lies in
`A union S`.  When `k=3`, equality would give `|A|=5` and force `H[A]` to
be a literal `K_5`, contrary to (1.2).  Thus every component has order at
least six in both cases.  Removing at most five selected matching ends
therefore leaves both components nonempty.  Consequently every endpoint
choice described in outcomes 1 and 2 is a proper separator of `G`.

Suppose first that `k=2`.  Deleting the centres removes every restored
cross-edge, so `S` separates `F`.  Both shores remain nonempty: a component
of `H-S` retains a vertex after the at most five centres are deleted.  Since
deleting five vertices from a seven-connected graph leaves `F`
two-connected, `S` is a two-cut.  The cited theorem now gives the two
connected components `C,D` of `F-S`.

For each centre, its selected edge crosses the two components of `H-S`.
Every other edge incident with that centre belongs to `H`, so its other end
lies in the centre's component or in `S`.  This proves the asserted
`1+(7-rho_z)` profile.  The last statement follows by pigeonhole.

For `k=3`, choose one end from each crossing matching edge.  No restored
edge then joins the two surviving parts, and the preceding size bound makes
both parts nonempty.  Its order is seven when four edges cross and eight
when five cross.  There are respectively `2^4` and `2^5` choices, and
choosing the centre ends gives the displayed labelled separator.  Deleting
all five centres removes every possible cross-edge, so `S-Z` separates
`F`; the two sides remain nonempty by the same component-size bound.  Since
`F` is two-connected, `|S-Z|>=2`.  At most one centre lies in `S`, because
at least four of their incident matching edges cross.  Thus `S-Z` is a
two-cut if `S` contains a centre, and `S` is a three-cut otherwise.  If
`kappa(F)>=3`, only the latter case can occur.

For the remaining assertion in the five-crossing, order-eight row, take a
mixed endpoint transversal `X` and put `T=S union X`.  Every component `K`
of `G-T` has `N_G(K) subseteq T` and `|N_G(K)|>=7`.  If some such
neighbourhood has order seven, it is the asserted exact seven-cut.
Otherwise every component is full at `T`.  A selected matching end on the
`D`-side has only its matching mate as a neighbour across to the `A`-side,
so every component remaining on the `A`-side must contain that mate.  There
is therefore only one.  A selected end on the `A`-side proves the symmetric
statement for `D`.  Thus `G-T` has exactly two full components.

It remains that `H` is four-connected.  By (2.8), the four-connected
extremal theorem of Norin and Totschnig gives a `K_7^\vee` minor in `H`;
their exceptional graph `K_{2,2,2,2}` is impossible because `|V(H)|>=25`.
Absorb every unused component into an adjacent branch set to make the model
span `H`, and label its branch sets

\[
                         P,B,C,U_1,U_2,U_3,U_4,
\]

with only `PB,PC` possibly absent.  If either missing adjacency is present
in `G`, the model already contains `K_7^-`.  Target-freeness therefore
makes `P` anticomplete in `G` to `B,C`.  The cited exact dichotomy applies
to this spanning partition and gives the asserted actual separator.
`\square`

In the order-seven rows `(k,|P_A|)=(2,5),(3,4)`, the audited
[three-component seven-cut exclusion](hc7_k7minus_three_component_seven_cut_exclusion.md)
upgrades every endpoint-choice separator to exactly two full complementary
components.  In the order-eight row, (3.3) proves only that each named old
component is full at its own boundary; deleting five chosen endpoints can
split the opposite component.  The theorem does not assert two components
there for the two unmixed choices, or that all endpoint choices induce the
same boundary colouring.

### Corollary 3.3 (the dense-branch separator's response family)

In outcome 3 of Theorem 3.2, let `Y` be the connected set returned by the
exact `K_7^\vee` dichotomy, and put

\[
                         M_Y=\{e\in M:e\cap Y\ne\varnothing\}. \tag{3.4}
\]

For every nonempty `J subseteq M_Y`, a signature-`J` colouring of `H` is
a proper colouring of `G-Y`, and its exact precolouring of `N_G(Y)` does
not extend to `G[Y union N_G(Y)]`.  Thus, if `r=|M_Y|>0`, the separator
carries `2^r-1` literal exterior-realised, interior-rejected colouring
responses on the same graph.  Their boundary partitions need not be
distinct.

#### Proof

Take a six-colouring of `H` whose signature is exactly `J`.  After all
edges of `M` are restored, its monochromatic edges are precisely those in
`J`, and every one has an end in `Y`.  Deleting `Y` removes them all, so
the colouring is proper on `G-Y`.  If its restriction to `N_G(Y)` extended
over `G[Y union N_G(Y)]`, the two colourings would glue to a six-colouring
of `G`, a contradiction. `\square`

## 4. What this settles and what remains

The response-synchronisation problem is no longer the existence of a common
colouring host.  The graph `H` is a single, literal, exactly six-chromatic
host on which every nonempty subset of the five selected centre edges is
the exact monochromatic-edge set of some proper six-colouring.

The remaining alternatives are structural:

- in outcome 1, use the five simultaneous singleton contacts and the full
  Boolean response family to eliminate the two-cut;
- in outcome 2, eliminate the four-crossing exact order-seven row and the
  five-crossing order-eight row; or
- in outcome 3, make the returned model-bag separator retain one of the
  common matching signatures, or complete the spanning near-clique model
  directly.  Corollary 3.3 supplies the entire punctured Boolean response
  family supported on the matching edges met by the returned set; the first
  response-preservation gap is therefore a returned set disjoint from all
  ten ends.

None of those three conclusions is proved here.  In particular, the 31
colourings need not induce one fixed boundary partition, and the separator
in outcome 3 need not be an exceptional neighbourhood or an order-seven
cut.  Even the response in Corollary 3.3 still needs a terminal gluing,
minor-model or descent theorem.  The theorem replaces five unrelated
centre-deletion colourings by one common response geometry; it does not by
itself close either connectivity branch of `F=G-Z`.

## Dependencies and provenance

The exceptional-neighbourhood input and the five-centre two-cut theorem are
new audited results in this repository.  Corollary 2.3 uses the separately
audited minimal contraction-bag theorem cited there.  The use of `HC_6` is
the theorem of Neil Robertson, Paul Seymour and Robin Thomas,
[*Hadwiger's conjecture for `K_6`-free graphs*](https://doi.org/10.1007/BF01202354).
The four-connected density input is Theorem 6 of Sergey Norin and Agnès
Totschnig, [*Every graph with no `K_7^\vee` minor is
6-colorable*](https://arxiv.org/abs/2507.03244).  The final separator
alternative is the audited exact `K_7^\vee` dichotomy cited above.  Hall's
theorem is used only for the five representatives in (2.2); its condition
is immediate from `|R_z|=5`.
