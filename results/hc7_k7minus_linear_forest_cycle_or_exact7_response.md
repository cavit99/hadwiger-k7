# A prescribed linear forest lies on one cycle or labels a minimum separation

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_linear_forest_cycle_or_exact7_response_audit.md).
The general
threshold theorem is computation-free.  Its critical-host corollary closes
the two-cycle portal-composition target, but it does not prove the
`K_7^-` six-colour conjecture or `HC_7`.

For a set `L` of edges and a colouring `c` of `G-L`, write

\[
 \Sigma_L(c)=\{uv\in L:c(u)=c(v)\}.                 \tag{0.1}
\]

A **linear forest of length `q`** is a vertex-disjoint union of nontrivial
paths having `q` edges in total.  Thus, if it has `t` components, it has
exactly `q+t` vertices.

## 1. The threshold theorem

### Theorem 1.1 (cycle or operation-labelled minimum separation)

Let `q\ge2` and `r\ge1`.  Let `G` be a `q`-connected graph which is
not `r`-colourable, and let `L` be a linear forest of length `q` in `G`.
Suppose that `G-g` is `r`-colourable for every `g\in E(L)`.  Then at least
one of the following holds.

1. One cycle of `G` contains every edge of `L`.
2. There are an order-`q` separation

   \[
       V(G)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
       \qquad N_G(A)=S,                              \tag{1.1}
   \]

   with `A,B` nonempty, an edge `g\in E(L)` having an end in `A`, and a
   proper `r`-colouring of `G-A` whose equality partition on `S` does not
   extend to a proper `r`-colouring of `G[A\cup S]`.  The colouring is the
   restriction of a proper colouring of `G-g`, and the two ends of `g` have
   the same colour before `A` is deleted.

#### Proof

If `G` is `(q+1)`-connected, apply the independent-path form of the theorem
of Haggkvist and Thomassen: independent paths of total length `k-1` in a
`k`-connected graph lie on one cycle.  The path components of `L` have
total length `q`, so `k=q+1` gives outcome 1.

It remains that `\kappa(G)=q`.  First suppose `|V(G)|=q+1`.  Then
`q`-connectivity forces `G=K_{q+1}`.  If `L` has `t` components, then
`q+t=|V(L)|\le q+1`, so `t=1` and `L` is a spanning path of length `q`.
Because `q\ge2`, the edge joining its distinct ends closes it into a cycle,
giving outcome 1.

We may therefore assume `|V(G)|\ge q+2`.  Now `\kappa(G)=q` supplies a
proper vertex cut `S` of order `q`.  Since `L` has `q+t>q` vertices, choose
`x\in V(L)-S`, and let `A` be the component of `G-S` containing `x`.
Since `G` is `q`-connected and another component remains outside
`A\cup S`,

\[
                              N_G(A)=S.               \tag{1.2}
\]

Choose an edge `g\in E(L)` incident with `x`.  Its other end belongs to
`A\cup S`: an edge of `G` cannot join two components of `G-S`.

Take a proper `r`-colouring `c` of `G-g`.  Its two ends have the same
colour, since otherwise `c` would be a proper `r`-colouring of `G`.
Deleting `A` removes an end of the sole possibly monochromatic restored
edge.  Thus `c|_{G-A}` is proper.

Let `Pi` be its equality partition on the literal set `S`.  If a proper
`r`-colouring of `G[A\cup S]` induced the same partition, a permutation of
its colour names would make the two colourings agree on `S`; the
permutation on the colours used by the boundary blocks extends to all
`r` colours.  The two colourings would then glue across (1.1), contrary to
the hypothesis that `G` is not `r`-colourable.  Therefore `Pi` is rejected
by the intact closed `A`-shore, proving outcome 2. `\square`

The theorem uses precisely the extra critical-colouring information absent
from the Lovasz--Woodall one-cycle problem.  At the missing unit of
connectivity it returns a labelled minimum separation rather than trying to
merge two cycles by connectivity alone.

## 2. Localising a complete signature cube

The threshold conclusion becomes substantially stronger in the critical
host because all edge-contraction signatures coexist on one graph.

### Theorem 2.1 (seven-coordinate cut localisation)

Let `G` be a minor-minimal non-six-colourable graph such that

\[
 \kappa(G)\ge7,
 \qquad K_7^-\npreccurlyeq G,                        \tag{2.1}
\]

and let `L` be a seven-edge componentwise-induced linear forest.  Suppose
`L` has one of the two forms

\[
                   7K_2
       \quad\hbox{or}\quad
                   5K_2\mathbin{\dot\cup}P_3.       \tag{2.2}
\]

Put `H=G-L`.  Then exactly all nonempty signatures occur on `H`:

\[
 \{\Sigma_L(c):c\in\operatorname{Col}_6(H)\}
                         =2^L-\{\varnothing\}.       \tag{2.3}
\]

Moreover, at least one of the following holds.

1. One cycle of `G` contains all seven edges of `L`.
2. There is a seven-cut `S` for which `G-S` has exactly two components
   `A,B`, both adjacent to every vertex of `S`.  Define

   \[
   \begin{aligned}
     L_A&=\{g\in L:V(g)\cap A\ne\varnothing\},\\
     L_B&=\{g\in L:V(g)\cap B\ne\varnothing\},\\
     L_S&=E(L[S]).
   \end{aligned}                                    \tag{2.4}
   \]

   Then `L=L_A\mathbin{\dot\cup}L_S\mathbin{\dot\cup}L_B`.  For every
   nonempty `J\subseteq L_A`, one fixed signature-`J` colouring from (2.3),
   after the other edges of `L` are restored, restricts to a proper
   six-colouring of `G[B\cup S]`; its equality partition on `S` is rejected
   by `G[A\cup S]`.  The symmetric statement holds for every nonempty
   `J\subseteq L_B`.

   If both `L_A,L_B` are nonempty, the two sets of boundary partitions
   obtained in these opposite orientations are disjoint.  Numerically,

   \[
   |L_A|+|L_B|\ge
   \begin{cases}
     4,&L\cong7K_2,\\
     3,&L\cong5K_2\mathbin{\dot\cup}P_3,
   \end{cases}                                      \tag{2.5}
   \]

   and hence one of the two closed shores carries at least the three
   nonempty responses of a two-coordinate subcube.  The set
   `L_A\cup L_B` also contains two vertex-disjoint edges.

#### Proof

Fix nonempty `J\subseteq L`.  Contract every edge in `J` and six-colour the
resulting proper minor.  On expansion, every edge of `J` has equal-coloured
ends.  No edge of `L-J` collapses because `L` is a forest.  No edge of
`G-L` collapses because each component of `L` is induced on its own vertex
set.  The expanded colouring is therefore proper on `H` and has signature
exactly `J`.  The empty signature would remain proper after restoring `L`
and would six-colour `G`.  This proves (2.3).

Apply Theorem 1.1 with `q=7,r=6`.  If it returns a cycle, outcome 1 holds.
Otherwise `\kappa(G)=7`.  Let `S` be any seven-cut.  The audited
three-component seven-cut exclusion for the critical host says that `G-S`
has exactly two components `A,B`, each full at `S`.  No edge joins `A` and
`B`, so (2.4) is a partition of `L`.

Fix nonempty `J\subseteq L_A` and a colouring `c_J` from (2.3).  Restore
all edges of `L`.  The only monochromatic restored edges are the members of
`J`, and each has an end in `A`.  Thus `c_J|_{G[B\cup S]}` is proper.  If
its boundary partition extended through `G[A\cup S]`, colour-name
alignment and gluing would six-colour `G`.  This proves the asserted
rejection, and the argument for `L_B` is symmetric.

Suppose a partition from a nonempty `J\subseteq L_A` equalled one from a
nonempty `K\subseteq L_B`.  The first is realised properly on `B\cup S`
and the second on `A\cup S`.  Aligning them on `S` and gluing would again
six-colour `G`.  Hence the two oriented partition languages are disjoint.

If `L\cong7K_2`, at most three of its edges lie in the seven-set `S`.  If
`L\cong5K_2\dot\cup P_3`, at most four lie in `S`: using all three path
vertices accounts for two edges and leaves room for at most two matching
edges.  This proves (2.5) and the two-coordinate pigeonhole statement.
Finally, four outside edges in the matching case plainly contain two
disjoint edges.  In the path case, among at least three outside edges either
two are already disjoint or the two adjacent path edges occur together
with a matching edge disjoint from both. `\square`

## 3. The portal application

### Corollary 3.1 (the two-cycle portal residue is eliminated)

Use the seven-connected row of the audited six-coordinate induced-forest
reduction.  Thus `F` has six edges and form `6K_2` or
`4K_2\dot\cup P_3`, `X=G-F` is seven-connected, and `X` has a fixed
spanning exact `K_7^\vee` model.  Let `e` be a model portal edge disjoint
from `V(F)`.  Assume, as in the portal construction, that the exceptional
bag has two distinct neighbours in the selected universal bag and that `e`
is one of the corresponding cross-bag edges.  Deleting `e` therefore leaves
the other edge as a witness of that required bag adjacency.  Put

\[
                         L=F\cup\{e\},
               \qquad H=G-L=X-e.                    \tag{3.1}
\]

Then all of the following hold.

1. `L` has one of the forms in (2.2), `H` is at least six-connected, the
   fixed exact model survives in `H`, and the signature language on `H` is
   the complete punctured seven-cube of order `127`.
2. Either one cycle contains the portal edge and all six original forest
   edges, or one actual order-seven separation carries the localised
   response families in Theorem 2.1(2) together with that same fixed model.
3. In the separation outcome, two vertex-disjoint edges `g,h` can be chosen
   from `L_A\cup L_B`.  Restoring `L-\{g,h\}` puts the three signatures

   \[
                     \{g\},\qquad\{h\},\qquad\{g,h\} \tag{3.2}
   \]

   on the single host `G-\{g,h\}`, while the fixed exact
   `K_7^\vee` model remains spanning.  If `g,h` lie on the same oriented
   side, all three colourings in (3.2) restrict properly to the opposite
   closed shore and are rejected by the intact side.  If they lie on
   opposite sides, the two singleton colourings give the two opposite
   rejected response families.

#### Proof

Cleanliness of `e` makes it a new single-edge component of `L`, so (2.2)
holds.  Deleting one edge from the seven-connected graph `X` leaves a
six-connected graph.  The stated alternative witness keeps the fixed model
valid after `e` is deleted.  The exactness of its two missing bag pairs is
unchanged; indeed any newly restored edge between either missing pair would
already give a `K_7^-` model in `G`.  Theorem 2.1 gives the signature cube,
the cycle-or-separation alternative and the two disjoint outside edges.

For each nonempty subset of `\{g,h\}`, take the corresponding colouring of
`H` and restore `L-\{g,h\}`.  Every restored edge has differently coloured
ends, which proves (3.2).  Adding those edges cannot disconnect a model bag
or remove a model adjacency, so the fixed model persists.  The final shore
statements are exactly the localisation assertion of Theorem 2.1. `\square`

## 4. Exact scope

Corollary 3.1 resolves the explicit **two-cycle portal-composition** target
in the earlier portal-threshold note.  It does not prove the parameter-seven
Lovasz--Woodall one-cycle assertion.  Instead it uses the critical
colourings at the precise point where connectivity is one below the
Haggkvist--Thomassen threshold, and returns an operation-labelled
order-seven separation carrying more information than the old unlabelled
edge-cut alternative.

The returned separation is not by itself terminal for the `K_7^-`
six-colour conjecture.  Existing exact-seven recursion can still return a
singleton shore, separator excess or a shore-filling list-critical core;
when `g,h` lie on opposite shores, the double-equality colouring is not
proper on either whole closed shore.  No conclusion requiring a shared
Kempe pivot or an unsupported branch-set/colouring identification is made.

## 5. Dependencies

- R. Haggkvist and C. Thomassen, *Circuits through specified edges*,
  Discrete Mathematics **41** (1982), 29--34: independent paths of total
  length `k-1` in a `k`-connected graph lie on one cycle.
- [six-coordinate induced-forest reduction](hc7_k7minus_six_coordinate_forest_reduction.md)
- [three-component seven-cut exclusion](hc7_k7minus_three_component_seven_cut_exclusion.md)
- [earlier portal-edge threshold reduction](hc7_k7minus_portal_edge_cycle_threshold.md),
  whose two-cycle next target is superseded by Corollary 3.1
