# Six exceptional centres in the bounded-feedback branch

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_feedback_six_centre_common_matching_audit.md).
This is a conditional refinement of the bounded-feedback outcome in the
[coordinate-growth theorem](hc7_k7minus_six_coordinate_growth_or_feedback.md).
It does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` be a minor-minimal non-six-colourable graph satisfying

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J,\qquad
 K_7^-\npreccurlyeq G,
\]

and the critical-host conclusions

\[
 \kappa(G)\geq7,\qquad |E(G)|\geq4|V(G)|,
 \qquad K_5\nsubseteq G,
\]

with at least twenty-five degree-eight vertices.  Suppose that `T` is a
feedback vertex set of `G` with

\[
                              |T|\leq14.              \tag{1.1}
\]

Thus `G-T` is a forest.  Every degree-eight vertex is exceptional, since
`G` has no literal `K_5`; the audited exceptional-neighbourhood theorem
therefore gives

\[
                         \alpha(G[N_G(z)])=3          \tag{1.2}
\]

at each such vertex.

For a matching `M` and a proper six-colouring `c` of `G-M`, put

\[
 \Sigma_M(c)=\{uv\in M:c(u)=c(v)\}.                 \tag{1.3}
\]

## 2. Six independent centres and six distinct representatives

### Theorem 2.1 (six-centre selection)

There are six independent degree-eight vertices

\[
                         Z=\{z_1,\ldots,z_6\}\subseteq V(G)-T, \tag{2.1}
\]

independent triples `I_i subseteq N_G(z_i)`, and pairwise distinct vertices

\[
              x_i\in R_i:=N_G(z_i)-I_i\qquad(1\leq i\leq6).  \tag{2.2}
\]

Consequently

\[
                         M=\{z_ix_i:1\leq i\leq6\}             \tag{2.3}
\]

is a matching of order six.

#### Proof

At least eleven of the twenty-five degree-eight vertices lie outside `T`.
Their induced graph is a subgraph of the forest `G-T`, and hence is
bipartite.  One of its two colour classes contains at least six vertices;
choose six of them as `Z`.

For each `z_i`, choose an independent triple `I_i` using (1.2) and put
`R_i=N_G(z_i)-I_i`.  Every `R_i` has order five.  We verify Hall's
condition for the six sets `R_i`.  A subfamily of order at most five has
union of order at least five, and hence at least the order of the
subfamily.  Thus Hall can fail only on all six sets.  In that event their
union has order at most five, so all six five-sets are one common set

\[
                              R=\{r_1,\ldots,r_5\}.              \tag{2.4}
\]

Then `G[Z,R]` contains `K_{6,5}`.  The seven connected branch sets

\[
 \{z_1,r_1\},\ \{z_2,r_2\},\ \{z_3,r_3\},\ \{z_4,r_4\},
 \ \{z_5\},\ \{z_6\},\ \{r_5\}                    \tag{2.5}
\]

are pairwise adjacent except possibly for `\{z_5\},\{z_6\}`.  They form
an explicit `K_7^-`-minor model, contrary to the hypothesis.  Hall's
theorem therefore supplies distinct representatives `x_i in R_i`.

The vertices of `Z` are independent, so no representative belongs to
`Z`.  The six centre edges in (2.3) are consequently pairwise
vertex-disjoint. `\square`

## 3. The common response host

### Theorem 3.1 (punctured six-cube)

Let `M` be the matching from Theorem 2.1 and put

\[
                              H=G-M.                            \tag{3.1}
\]

Then all of the following hold.

1. `H` is connected,

   \[
                    |E(H)|\geq4|V(G)|-6,\qquad \chi(H)=6.       \tag{3.2}
   \]

2. For every nonempty `J subseteq M`,

   \[
                         \chi(G-J)=\chi(G/J)=6.                 \tag{3.3}
   \]

3. The exact signature language on the one graph `H` is

   \[
       \{\Sigma_M(c):c\in\operatorname{Col}_6(H)\}
                              =2^M-\{\varnothing\}.             \tag{3.4}
   \]

4. For each `i`, there is a proper six-colouring of `H` with signature
   exactly `\{z_ix_i\}`.
5. For every nonempty `J subseteq M`, one may choose a signature-`J`
   colouring whose restriction `theta_J` to `G-Z` satisfies

   \[
       \varnothing\ne\operatorname{Sat}(\theta_J)
          \subseteq\{z_i:z_ix_i\in J\},                         \tag{3.5}
   \]

   where a centre is saturated when all six colours occur on its
   neighbourhood.
6. For every nonempty `J subseteq M`, the graph `G-J` has a spanning
   `K_6`-minor model, and `G` has a spanning `K_6`-minor model in which
   both ends of every edge in `J` lie in one branch set.  In particular,
   taking `J=M` co-bags all six selected pairs in one spanning model.

#### Proof

Fix `i`.  Contract the star on `z_i` and the independent triple `I_i`, and
six-colour the resulting proper minor.  Expanding gives a colouring
`phi_i` of `G-z_i` in which `I_i` is monochromatic.  Every member of `R_i`
avoids that colour.  If the five vertices of `R_i` used at most four
further colours, a missing sixth colour could be assigned to `z_i`.
Therefore the five vertices of `R_i` have pairwise distinct colours.
Extending `phi_i` to `z_i` with the colour of `x_i` makes `z_ix_i` the
unique monochromatic matching edge.  This proves item 4.

Let `J` be a nonempty subset of `M`.  Both `G-J` and `G/J` are proper
minors, so they are at most six-chromatic.  If `G-J` had a five-colouring,
recolour every centre incident with an edge of `J` using one fresh sixth
colour.  Those centres are independent, and the fresh colour occurs
nowhere else, so this restores all edges of `J` and six-colours `G`.  A
five-colouring of `G/J` expands to a five-colouring of `G-J` and gives the
same contradiction.  This proves (3.3), including `chi(H)=6` when `J=M`.

Six-colour `G/J` and expand every contracted matching edge.  On `H`, the
ends of precisely the edges in `J` are equal-coloured; every edge of
`M-J` remains an edge between distinct contraction bags and is
bichromatic.  This realizes every nonempty signature.  An empty signature
would remain proper after restoring `M` and would six-colour `G`, proving
(3.4).

For (3.5), use a colouring obtained by expanding a six-colouring of `G/J`.
If `z_i x_i` is not in `J`, the displayed colour of `z_i` is absent from
its neighbourhood, so `z_i` is not saturated.  If none of the centres
indexed by `J` were saturated, independently recolour each of them with a
colour missing from its neighbourhood.  This would again six-colour `G`.

Seven-connectivity implies seven-edge-connectivity, so deleting at most
six edges leaves `G-J` connected.  The contraction `G/J` is connected as
well.  By `HC_6`, each exactly six-chromatic graph has a `K_6` minor; unused
vertices can be absorbed to make the models spanning.  Expanding the
contracted matching edges inside their branch sets gives the claimed
co-bagged model in `G`.

Finally, connectedness and the density statement for `H` follow by
deleting the six distinct edges of `M`. `\square`

## 4. Exact information retained from the forest

### Proposition 4.1 (placement relative to the feedback set)

Put

\[
                 t=|\{i:x_i\in T\}|.                          \tag{4.1}
\]

Every centre `z_i` lies in the forest `G-T`.  If `x_i notin T`, then
`z_i x_i` is an edge of the same tree component of `G-T`; the `6-t` such
edges form a matching of tree edges.  Consequently

\[
        c(H-T)=c(G-T)+(6-t),                                  \tag{4.2}
\]

where `c` denotes the number of components.

#### Proof

The centres were chosen outside `T`.  An endpoint `x_i` outside `T` is
joined to its centre by an edge of the forest `G-T`, and every edge of a
forest is a bridge.  The selected edges are pairwise disjoint.  Removing
the `6-t` selected forest edges therefore increases the number of forest
components by exactly `6-t`; selected edges with their other endpoint in
`T` do not occur in either `G-T` or `H-T`. `\square`

## 5. A matching across the feedback set

### Theorem 5.1 (a matching crossing the feedback boundary)

There are six independent degree-eight vertices

\[
                    Z=\{z_1,\ldots,z_6\}\subseteq V(G)-T
\]

and pairwise distinct vertices `y_i in N_G(z_i) cap T`.  Hence

\[
                     M_T=\{z_iy_i:1\leq i\leq6\}               \tag{5.1}
\]

is a matching of order six.  Put `H_T=G-M_T`.  Then:

1. `H_T` is connected,

   \[
       |E(H_T)|\geq4|V(G)|-6,\qquad \chi(H_T)=6;                \tag{5.2}
   \]

2. for every nonempty `J subseteq M_T`,

   \[
                        \chi(G-J)=\chi(G/J)=6;                 \tag{5.3}
   \]

3. the exact signature language on `H_T` is

   \[
       \{\Sigma_{M_T}(c):c\in\operatorname{Col}_6(H_T)\}
                               =2^{M_T}-\{\varnothing\};       \tag{5.4}
   \]

4. for every nonempty `J subseteq M_T`, a signature-`J` colouring may be
   chosen whose restriction `theta_J` to `G-Z` satisfies

   \[
       \varnothing\ne\operatorname{Sat}(\theta_J)
          \subseteq\{z_i:z_iy_i\in J\};                       \tag{5.5}
   \]

5. every `G-J`, for nonempty `J subseteq M_T`, has a spanning `K_6`-minor
   model, and `G` has a spanning `K_6`-minor model co-bagging the ends of
   every edge of `J`; and
6. the feedback forest is retained literally:

   \[
                              H_T-T=G-T.                       \tag{5.6}
   \]

#### Proof

Choose the six centres `Z` exactly as in Theorem 2.1.  Since `G-T` is a
forest, two neighbours of one `z_i` outside `T` cannot be adjacent: such
an edge would form a triangle with `z_i` in `G-T`.  Thus

\[
       N_G(z_i)-T\text{ is independent},\qquad
       |N_G(z_i)-T|\leq\alpha(G[N_G(z_i)])=3.                  \tag{5.7}
\]

Every `z_i` has degree eight, so

\[
                              |N_G(z_i)\cap T|\geq5.           \tag{5.8}
\]

Apply Hall's theorem to the six sets `N_G(z_i) cap T`.  Any subfamily of
order at most five has a union of order at least five and therefore
satisfies Hall's condition.  If Hall failed on all six sets, their union
would have order at most five.  By (5.8), the six sets would then be one
common five-set.  Together with `Z` this gives a `K_{6,5}` subgraph, and
the seven branch sets displayed in (2.5) give a `K_7^-` minor.  This is
excluded.  Hall therefore supplies distinct representatives `y_i in T`.
Because the centres lie outside `T` and are independent, (5.1) is a
matching.

The chromatic and signature arguments from Theorem 3.1 use only that the
selected edges form a matching whose centre ends are independent.  For
clarity, if nonempty `J subseteq M_T`, then `G-J` and `G/J` are proper
minors.  A five-colouring of either one could be expanded and the centres
incident with `J` recoloured with one fresh sixth colour, six-colouring
`G`.  This proves (5.3).  Expanding a six-colouring of `G/J` realises
signature exactly `J` on `H_T`, while an empty signature would six-colour
`G`.  This proves (5.4), including all six singleton signatures.

In such an expanded colouring, a centre not incident with `J` has its
displayed colour absent from its whole neighbourhood.  If no centre
incident with `J` were saturated, all those independent centres could be
recoloured with colours missing from their respective neighbourhoods,
again six-colouring `G`.  This proves (5.5).

Seven-connectivity implies seven-edge-connectivity, so deleting at most
six edges leaves `G-J` connected.  Contractions preserve connectedness.
The exactly six-chromatic graphs `G-J` and `G/J` therefore have spanning
`K_6` models by `HC_6` and absorption; expanding the contracted edges
inside their bags proves item 5.  Finally every edge of `M_T` has one end
in `T`, so deleting `T` removes all six edges already and gives (5.6).
`\square`

### Information not retained by Theorem 5.1

The boundary-crossing representatives `y_i` need not belong to the
five-set complementary to a prescribed independent triple in `N_G(z_i)`.
Consequently Theorem 5.1 does **not** retain the stronger construction in
which an independent triple is monochromatic and its five-vertex
complement is rainbow.  It retains the exact singleton signatures and the
saturation inclusion (5.5), since those follow from minor-criticality and
the matching itself.

## 6. Scope

The theorem converts the bounded-feedback outcome into a common
six-centre response host with all `63` nonempty equality signatures and a
single spanning `K_6` model co-bagging all six pairs.  The forest gives the
exact placement statement (4.2), but it does **not** ensure that a selected
representative avoids `T`, that `H` is six- or seven-connected, or that the
co-bagged model respects the components of `H-T`.

Thus the remaining unsupported inference is a connectivity or
model-placement theorem coupling the six co-bagged centre pairs to the
feedback forest.  The punctured signature cube alone does not provide that
coupling.

Theorem 5.1 provides a second choice of matching for which every selected
edge crosses the feedback boundary and the forest is unchanged after the
matching is deleted.  It need not be the independent-triple matching from
Theorem 2.1, so the two useful features must not be silently combined.

## Dependencies

The degree-eight count and literal `K_5` exclusion are the audited
critical-host conclusions.  The independent triples are supplied by
[`hc7_k7minus_exceptional_neighbourhood_completion.md`](../results/hc7_k7minus_exceptional_neighbourhood_completion.md).
The feedback set is the second outcome of the active
[coordinate-growth theorem](hc7_k7minus_six_coordinate_growth_or_feedback.md).
The `K_6`-minor input is Hadwiger's conjecture for six colours, proved by
Robertson, Seymour and Thomas.
