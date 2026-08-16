# A reverse crossing edge extends the remote operation cube and renews the exact model

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_remote_crossing_five_cube_model_renewal_audit.md).

This note treats exactly the full punctured-cube order-seven outcome of the
[remote-interface topological reduction](../results/hc7_k7minus_remote_interface_topological_reduction.md).
Its main point is that the fresh reverse crossing response is not merely a
sixteenth boundary partition.  It can be chosen vertex-disjoint from the
four old operation edges.  The resulting five-edge forest supports all 242
nontrivial mixed minor operations, all 31 nonempty equality signatures, and
a new common spanning exact `K_7^\vee` model after all five edges are
deleted.

The model is renewed by density.  It is not asserted to have the same bags
or labels as the model in the four-edge deletion host.

## 1. Setting and the disjoint crossing edge

Let `G` be a hypothetical critical host:

\[
 \begin{gathered}
  \chi(G)=7,
  \qquad \chi(J)\le6\text{ for every proper minor }J\text{ of }G,\\
  \kappa(G)\ge7,
  \qquad \delta(G)\ge8,
  \qquad |E(G)|\ge4|V(G)|,
  \qquad |V(G)|\ge25,\\
  K_7^-\npreccurlyeq G.
 \end{gathered}                                                   \tag{1.1}
\]

Fix an exceptional degree-eight vertex `z`, an independent triple

\[
                         I=\{x_1,x_2,x_3\}\subseteq N_G(z),        \tag{1.2}
\]

and a remote seven-removable edge `f=uv` in the exterior component `C` of
`G-N_G[z]`.  Put

\[
             T=\{zx_1,zx_2,zx_3,f\},
             \qquad H_0=G-T.                                      \tag{1.3}
\]

Assume outcome 1 of the remote-interface topological reduction.  Thus a
different exterior component `E` has

\[
                  S=N_G(E)=N_G(z)-\{r\},\qquad |S|=7,              \tag{1.4}
\]

and `G-S` has exactly two full components.  The previously fixed
six-colourings `c_J` of `H_0`, for every nonempty `J\subseteq T`, have
exact `T`-signature `J` and restrict properly to `G[E\cup S]`.

Choose

\[
                              s\in S-I.                            \tag{1.5}
\]

There are at least four choices.  Fullness of `E` at `S` supplies an edge

\[
                       h=es\qquad(e\in E).                         \tag{1.6}
\]

The edge `h` is vertex-disjoint from `T`: its boundary end is not in `I`,
its exterior end lies in `E`, and both ends of `f` lie in the different
exterior component `C`.  Hence

\[
       F=T\mathbin{\dot\cup}\{h\}
        \cong K_{1,3}\mathbin{\dot\cup}K_2\mathbin{\dot\cup}K_2   \tag{1.7}
\]

as a selected-edge forest.  Each of its three components is induced on
its own vertex set.  Edges between different components are immaterial.

Fix the displayed end `u` of `f`.  The three repair vertices satisfy

\[
                              z,u,e\text{ are independent}.        \tag{1.8}
\]

Indeed, `u,e\notin N_G[z]`, while an edge `ue` would put `u` and `e` in
the same component of `G-N_G[z]`.

For disjoint `A,D\subseteq F`, let `G/A-D` be the minor obtained by
contracting the edges in `A`, deleting the edges in `D`, and keeping every
edge in `F-(A\cup D)`.

## 2. The 242-pattern mixed-operation theorem

### Theorem 2.1 (full five-edge exact-six cube)

For all disjoint `A,D\subseteq F` with `A\cup D\ne\varnothing`,

\[
                              \chi(G/A-D)=6.                       \tag{2.1}
\]

Thus the five labelled edges support exactly

\[
                                3^5-1=242                           \tag{2.2}
\]

nontrivial keep/delete/contract patterns, and every one is an exactly
six-chromatic proper minor of the same graph.

#### Proof

Every graph in (2.1) is a proper minor of `G`, so it is at most
six-colourable.  Suppose that some `M=G/A-D` had a proper five-colouring.
Expand every contracted component of the selected forest, initially
giving all of its vertices the colour of its contraction image.

- If at least one star edge `zx_i` is operated, recolour `z` with one
  fresh sixth colour.
- If `f` is operated, recolour `u` with that same fresh colour.
- If `h` is operated, recolour `e` with that same fresh colour.

The recoloured vertices are independent by (1.8), and every other
neighbour of a recoloured vertex retains one of the original five colours.
The independence of `I` and componentwise inducedness of `F` ensure that
expansion creates no collapsed edge other than an operated selected edge.
Every operated edge is repaired by the indicated recolouring.  Every kept
selected edge was represented by a genuine edge of `M`, so its ends remain
differently coloured.  All other edges were already represented in the
minor and remain proper.

This is a proper six-colouring of `G`, contradicting (1.1).  Therefore no
minor in (2.1) is five-colourable, proving the theorem. `\square`

## 3. One common deletion host and all 31 signatures

Put

\[
                               K=G-F=H_0-h.                         \tag{3.1}
\]

For a proper six-colouring `c` of `K`, define its equality signature by

\[
                   \Sigma_F(c)=\{ab\in F:c(a)=c(b)\}.              \tag{3.2}
\]

### Theorem 3.1 (punctured five-cube with literal response inheritance)

The graph `K` is exactly six-chromatic and

\[
 \{\Sigma_F(c):c\in\operatorname{Col}_6(K)\}
                         =2^F-\{\varnothing\}.                     \tag{3.3}
\]

Moreover the old and new boundary responses coexist in the following
literal sense.

1. Each preselected colouring `c_J` of `H_0`, for
   `\varnothing\ne J\subseteq T`, restricts to a colouring of `K` with
   signature exactly `J`; in particular `h` is proper in that same
   colouring.
2. Every six-colouring `c_h` of `G-h` restricts to a colouring of `K`
   with signature exactly `\{h\}`; all four edges of `T` are proper in
   that same colouring.
3. Every `c_J` restricts properly to the closed `E`-shore `G[E\cup S]`.
   The colouring `c_h` restricts properly to the opposite closed shore
   `G-E`.  Their partitions on `S` are oppositely rejected, and the
   partition induced by `c_h` is different from all fifteen partitions
   induced by the `c_J`.

#### Proof

Exact six-chromaticity is the all-delete case of Theorem 2.1.  For each
nonempty `Q\subseteq F`, take a six-colouring of `G/Q` and expand the
contracted forest.  An edge of `Q` has equal-coloured ends.  An edge of
`F-Q` is kept in the quotient and, because `F` is a componentwise-induced
forest, its ends remain distinct quotient vertices with different colours.
The resulting colouring of `K` therefore has signature exactly `Q`.
An empty signature would remain proper after restoring all of `F` and
would six-colour `G`.  This proves (3.3).

The edge `h` is present in `H_0`, so it is proper in each already selected
`c_J`; restriction to `K` proves item 1.  In a six-colouring of `G-h`, the
ends of `h` must have the same colour, since otherwise `h` could be
restored.  All of `T` is present and proper there, proving item 2.

No edge of `T` lies in the closed `E`-shore, while `h` is proper in every
`c_J`.  Hence all fifteen old restrictions remain proper on that shore.
The only conflict in `c_h` is the edge `h`, whose exterior end is deleted
from `G-E`; hence its opposite restriction is proper.  The rejection and
distinctness assertions now follow by aligning colour names on `S` and
gluing the two closed-shore colourings.  Equality with any old partition
would give a proper six-colouring of `G`. `\square`

### Remark 3.2 (the exact limit of the old shore orientation)

The other fifteen signatures containing `h` and at least one edge of `T`
exist by (3.3), but they are not proper on either of the two original
closed shores.  Their `h`-conflict lies in `G[E\cup S]`, while every
`T`-conflict lies in `G-E`.  Thus Theorem 3.1 preserves all sixteen named
one-orientation responses and creates all mixed operation patterns, but it does not
turn the latter into additional legal responses on this same separation.

## 4. Connectivity, density, and model renewal

### Theorem 4.1 (a four- or five-connected dense common model host)

The common deletion host `K` satisfies

\[
                 4\le\kappa(K)\le5,
                 \qquad |E(K)|\ge4|V(K)|-5.                       \tag{4.1}
\]

It has a spanning `K_7^\vee` model which is exact even after all five
edges of `F` are restored in `G`.

#### Proof

The four-edge host `H_0` is exactly five-connected by the
[remote operation-cube theorem](../results/hc7_k7minus_remote_removable_edge_operation_cube.md).
Deleting one edge lowers vertex connectivity by at most one: if a set
`Z` of order at most `k-2` disconnects a graph after deletion of `ab`,
then `Z\cup\{a\}` or `Z\cup\{b\}` disconnects the original graph.  Hence
`\kappa(K)\ge4`.  The vertex `z` has degree five in `K`, giving the upper
bound.

Exactly five distinct edges were deleted from `G`, so

\[
                         |E(K)|=|E(G)|-5
                                  \ge4|V(K)|-5.                    \tag{4.2}
\]

In particular, `K` is four-connected and lies strictly above the
`4|V(K)|-8` threshold in Norin--Totschnig, Theorem 6.  Its exceptional
graph `K_{2,2,2,2}` is excluded by `|V(K)|\ge25`.  Therefore `K` has a
`K_7^\vee` minor model.  Absorb unused vertices to make the model spanning.

Write its bags as

\[
                         X,B,C',U_1,U_2,U_3,U_4,                    \tag{4.3}
\]

where the only nominally missing adjacencies are `XB` and `XC'`.  If an
edge of `G`, including any restored member of `F`, joined either missing
bag pair, the same seven bags would form a `K_7^-` model in `G`.  Target
exclusion in (1.1) therefore makes both missing pairs anticomplete in `G`.
The renewed spanning model is exact in the full original host. `\square`

The adjective *renewed* is essential.  The old exact model in `H_0` need
not survive deletion of `h`; Theorem 4.1 obtains a possibly different
model directly in the five-edge deletion host `K`.

### Corollary 4.2 (the all-contraction quotient)

The quotient `G/F` is exactly six-chromatic and has a spanning `K_6`
model.  On expansion in `G`, one branch set contains
`\{z,x_1,x_2,x_3\}`, one contains `\{u,v\}`, and one contains `\{e,s\}`;
these three branch sets are allowed to coincide.

#### Proof

The chromatic assertion is the all-contraction case of Theorem 2.1.  The
established case `HC_6` supplies a `K_6` model, which may be made spanning.
Each contracted vertex then belongs to a bag.  Expanding its preimage
gives the three asserted co-baggings. `\square`

## 5. What the renewed model forces

The next consequence is the strongest direct transfer currently available
from the common exact model to the operation-labelled colourings.

### Theorem 5.1 (singleton exposure or an eight-endpoint separator)

The exact model from Theorem 4.1 supplies a nonempty proper connected set
`Y` inside one universal bag `U_i` such that `U_i-Y` is connected and

\[
                               R=N_G(Y)                              \tag{5.1}
\]

is an actual separator of order at least seven.  In addition, one of the
following holds.

1. For at least one `q\in F`, the singleton-`q` colouring of `K` restricts
   properly to one closed side of `R`, and its boundary partition is
   rejected by the intact opposite closed side.
2. The set `Y` is disjoint from all eight vertices of `F` and

\[
                              V(F)\subseteq R,
                              \qquad |R|\ge8.                       \tag{5.2}
\]

Consequently, if the model dichotomy returns an order-seven separator,
that separator necessarily exposes one of the four old singleton
responses or the fresh reverse response.

#### Proof

Apply the
[exact-model separator dichotomy](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md)
to the spanning model (4.3) in the seven-connected graph `G`.  Its target
outcome is excluded by (1.1), so it gives `Y` and `R` as stated.

For `q=ab\in F`, let `c_q` be a colouring of `K` with signature
`\{q\}`, supplied by (3.3).  After the other four selected edges are
restored, `c_q` is a proper six-colouring of `G-q` whose only conflict in
`G` is `q`.

If `Y` contains an end of `q`, then `q` is absent from `G-Y`, so
`c_q|G-Y` is proper.  If `Y` contains neither end and at most one end lies
in `R`, then `q` is absent from `G[Y\cup R]`, so the restriction to that
closed side is proper.  In either case, an extension of the induced
partition through the intact other closed side would glue to a proper
six-colouring of `G`; hence the partition is rejected there.

If item 1 fails for every `q`, neither end of any selected edge belongs to
`Y` and both ends of every selected edge belong to `R`.  The forest in
(1.7) has eight distinct vertices, proving (5.2). `\square`

## 6. Exact scope and the remaining allocation obstruction

Theorems 2.1--4.1 are an unconditional strengthening of outcome 1 of the
remote-interface reduction: one literal five-edge common host carries the
full 242-pattern operation cube, the full 31-signature punctured equality
cube, all sixteen previously oriented response colourings, and a renewed
spanning exact near-clique model.  No identification between the old and
renewed model bags is used.

Theorem 5.1 is a genuine model-to-response transfer, but it is not a
terminal `K_7^-` construction.  Its sharp unresolved allocation is (5.2).
When all eight forest vertices lie in the separator boundary, every
nonempty signature has a monochromatic selected edge wholly inside that
boundary.  Since the boundary belongs to both closed shores, none of the
31 colourings is automatically proper on either shore.  Thus the whole
operation cube can become invisible to the separator response argument at
once.

Nor does Corollary 4.2 by itself split a bag of the renewed model.  Its
spanning `K_6` model lives in the all-contraction quotient and is not
labelled compatibly with the independently renewed `K_7^\vee` model in
`K`.  A branch-set proof identifying those two models is still required;
the existence of three contracted components alone does not supply it.
In particular, contracting the three spokes separately gives three
existential `K_6` models which need not have common bags, while contracting
them together deliberately puts `z,x_1,x_2,x_3` in one quotient vertex.
The audited
[three-split closure](../results/hc7_three_split_marked_mader_branch_closure.md)
does not apply: its three split edges are a matching supported by three
pairwise vertex-disjoint six-vertex `K_5` models, whereas the three spokes
here share `z` and Corollary 4.2 supplies no three disjoint supporting
models.

A falsifiable next lemma is therefore:

> **Eight-endpoint escape lemma.**  In the setting of this note, the set
> `Y` furnished by the exact-model separator dichotomy may be chosen so
> that `V(F)\nsubseteq N_G(Y)` or `Y\cap V(F)\ne\varnothing`.

By Theorem 5.1 this lemma would force a named singleton response on a
nested separator.  A stronger terminal version would have to give an
explicit split of one renewed branch bag and verify every required
branch-set adjacency; no such split is claimed here.

The note applies only to outcome 1 of the remote-interface topological
reduction.  It says nothing about the cross-miss/full order-seven residue
or either order-eight residue, and it does not prove the `K_7^-`
six-colour conjecture or `HC_7`.

The broader repository already contains common five- and six-coordinate
signature/model hosts, notably the
[six-coordinate forest reduction](../results/hc7_k7minus_six_coordinate_forest_reduction.md).
The contribution here is narrower and differently labelled: the fifth
coordinate is the literal reverse crossing edge at the same exact-seven
boundary, all 242 mixed operations are proved exactly six-chromatic, and
the fifteen old response colourings are retained verbatim alongside that
reverse response.

## 7. Dependencies

- [remote removable-edge operation cube](../results/hc7_k7minus_remote_removable_edge_operation_cube.md):
  the edge `f`, the old 80-pattern cube, exact connectivity of `H_0`, and
  the fifteen preselected colourings;
- [remote-interface topological reduction](../results/hc7_k7minus_remote_interface_topological_reduction.md):
  the full order-seven component `E`, the response orientations, and the
  fresh crossing response;
- [exact `K_7^\vee` separator dichotomy](../results/hc7_k7minus_exact_k7vee_separator_dichotomy.md):
  Theorem 5.1;
- S. Norin and A. Totschnig,
  [*Every graph with no `K_7^\vee` minor is 6-colourable*, Theorem 6](https://arxiv.org/html/2507.03244#S1.Thmtheorem6):
  the density-to-model implication in Theorem 4.1;
- the established case `HC_6`: Corollary 4.2.
