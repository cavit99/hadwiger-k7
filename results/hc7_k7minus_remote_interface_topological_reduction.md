# Topological reduction of the remote-edge centre interface

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_remote_interface_topological_reduction_audit.md).
This theorem
eliminates the connected-exterior order-seven case and reduces every
remaining remote-edge interface to one operation-labelled exact-seven
return, one cross-miss/full exact-seven residue, or one of two explicit
order-eight residues.  None of the three residues is claimed terminal, and
the theorem does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## 1. Setting

Let `G` be a hypothetical critical host:

\[
 \begin{gathered}
  \chi(G)=7,
  \qquad \chi(J)\le6\text{ for every proper minor }J\text{ of }G,\\
  \kappa(G)\ge7,
  \qquad \delta(G)\ge8,
  \qquad |E(G)|\ge4|V(G)|,
  \qquad |V(G)|\ge25,
  \qquad K_7^-\npreccurlyeq G.
 \end{gathered}                                      \tag{1.1}
\]

Fix an exceptional degree-eight vertex `z`, an independent triple

\[
                         I=\{x_1,x_2,x_3\}\subseteq N_G(z),       \tag{1.2}
\]

and a remote seven-removable edge `f=uv` supplied by the audited
[remote-edge operation-cube theorem](../results/hc7_k7minus_remote_removable_edge_operation_cube.md).
Thus

\[
                         f\in E(G-N_G[z]),
                 \qquad G-f\text{ is seven-connected}.           \tag{1.3}
\]

Put

\[
 T=\{zx_1,zx_2,zx_3,f\},
 \qquad H=G-T.                                       \tag{1.4}
\]

For every nonempty `J\subseteq T`, fix a proper six-colouring `c_J` of
`H` whose equality signature on `T` is exactly `J`.  When the four edges
of `T` are restored, those in `J` are precisely the monochromatic ones.
The graph `H` also retains the fixed spanning exact `K_7^\vee` model from
the operation-cube theorem.

Let `C` be the component of `G-N_G[z]` containing `f` and put

\[
                              Q=N_G(C).                \tag{1.5}
\]

Then `Q\subseteq N_G(z)` and `7\le |Q|\le8`.

## 2. Exhaustive topological reduction

### Theorem 2.1 (connected order seven is impossible)

Let

\[
                         O=G-N_G[z].                   \tag{2.1}
\]

The graph `O` has one or two components.  Exactly one of the following
four outcomes holds.

1. **Full punctured-cube exact-seven return.**  There is a component
   `E` of `O`, distinct from `C`, such that

   \[
                    S=N_G(E)=N_G(z)-\{r\}             \tag{2.2}
   \]

   for some `r\in N_G(z)`.  The order-seven cut `S` has exactly two full
   complementary components.  Every one of the fifteen nonempty
   `T`-signatures restricts properly to `G[E\cup S]`, and its equality
   partition on `S` is rejected by the intact opposite closed shore.
   For every crossing edge `h=es`, with `e\in E` and `s\in S`, a
   six-colouring of `G-h` restricts properly to `G-E` and induces a
   partition rejected by the intact `E`-shore.  This last partition is
   different from every partition supplied by the fifteen `T`-signatures.
   Independently, the fixed exact `K_7^\vee` model remains available in
   the original host `H`; no claim is made that it survives deletion of
   `h`.

2. **Cross-miss/full order-seven residue.**  The exterior has exactly two
   components `C,E`.  There is a vertex `w\in N_G(z)` such that

   \[
       N_G(C)=N_G(z)-\{w\},
       \qquad N_G(E)=N_G(z),                          \tag{2.3}
   \]

   and `w` has a neighbour in `E`.  The original order-seven boundary
   `Q=N_G(C)` carries the seven nonempty centre-star responses in the
   `C` orientation and the remote-edge response in the opposite
   orientation, as in the operation-cube theorem.

3. **Connected-exterior order-eight residue.**  The graph `O=C` is
   connected and

   \[
                              Q=N_G(z).                \tag{2.4}
   \]

   Hence `G-Q` has exactly the two full components `C` and `{z}`.  The
   component `C` has order at least sixteen.  It contains the named edge
   `f`, deletion of `f` preserves seven-connectivity, and the full
   80-pattern mixed-operation cube and fixed exact model remain available.

4. **Both-full order-eight residue.**  The graph `O` has exactly two
   components `C,E`, and

   \[
                         N_G(C)=N_G(E)=N_G(z).          \tag{2.5}
   \]

   The audited
   [both-full shore reduction](../results/hc7_k7minus_both_full_shore_reduction.md)
   applies.  Consequently `G[N_G(z)]` is one of its seven named boundary
   types and the three full components `{z},C,E` have full-subgraph
   packing vector

   \[
                              (1,1,1).                 \tag{2.6}
   \]

   The centre-star and remote-edge response labels remain present, but the
   both-full theorem does not identify them with boundary partitions or
   minor-model branch-set contacts.

In particular, `|Q|=7` is impossible when `G-N_G[z]` is connected.

### Proof

The audited
[low-degree exterior-component theorem](../results/hc7_low_degree_exterior_component_bounds.md)
gives

\[
                         1\le \operatorname{comp}(O)\le2.          \tag{2.7}
\]

We first eliminate the only connected order-seven possibility.  Suppose
`O=C` and `|Q|=7`.  Write

\[
                         N_G(z)=Q\mathbin{\dot\cup}\{w\}.          \tag{2.8}
\]

The definition `Q=N_G(C)` says that `w` has no neighbour in `C`; the
definition of the exterior says the same for `z`.  Thus `G-Q` has exactly
the components `C` and the literal edge `{z,w}`.  Every neighbour of `w`
belongs to `Q\cup\{z\}`.  Since `\delta(G)\ge8`, the vertex `w` is
adjacent to every member of `Q`.  Therefore

\[
                         C,\quad\{z\},\quad\{w\}                    \tag{2.9}
\]

are three pairwise disjoint connected subgraphs full at `Q`, and the last
two are adjacent.

Apply the exact `(1,2)` consequence in the audited
[three-full-subgraph completion theorem](../results/hc7_k7minus_exact7_three_full_subgraph_completion.md#2-lift-to-an-exact-12-separation).
It gives

\[
                              \chi(G[Q])\le3.                     \tag{2.10}
\]

We include the short colouring contradiction which finishes this case.
Choose a proper three-colouring of `G[Q]`; if three colours are used,
delete a smallest colour class `Z`, and if at most two are used take
`Z=\varnothing`.  In either case

\[
 |Z|\le2,
 \qquad Q-Z=P\mathbin{\dot\cup}R,                    \tag{2.11}
\]

where `P,R` are independent.  Contract a spanning tree of each of

\[
                         \{z\}\cup P,
                   \qquad\{w\}\cup R.                \tag{2.12}
\]

At least one contraction is nontrivial, so the resulting graph is a
proper minor and is six-colourable.  The edge `zw` makes the two
contraction images adjacent.  Keep the colouring on `G[C\cup Z]` and
expand the two image colours over `P,R`.  This properly colours
`G[C\cup Q]` and uses at most

\[
                              2+|Z|\le4                \tag{2.13}
\]

colours on `Q`.  Give `z,w` two distinct colours absent from `Q`.  Both
vertices are complete to `Q`, neither has a neighbour in `C`, and `zw` is
an edge, so this is a proper six-colouring of `G`, a contradiction.  The
connected order-seven case is therefore impossible.

Suppose now that `|Q|=7`.  By (2.7), the exterior has exactly one other
component `E`.  Let `w` again be defined by (2.8).  Every order-seven cut
in the critical host has exactly two complementary components, by the
audited
[three-component seven-cut exclusion](../results/hc7_k7minus_three_component_seven_cut_exclusion.md).
After deleting `Q`, the component opposite `C` contains `z,w,E`.  The
vertex `z` has no neighbour in `E`, so connectedness of that component
forces an edge from `w` to `E`.  Since

\[
             N_G(E)\subseteq N_G(z),
             \qquad |N_G(E)|\ge7,
             \qquad w\in N_G(E),                     \tag{2.14}
\]

either `N_G(E)=N_G(z)` or
`N_G(E)=N_G(z)-\{r\}` for some `r\in Q`.  The first choice is outcome 2;
the second will give outcome 1.

It remains to consider `|Q|=8`, when necessarily `Q=N_G(z)`.  If `O` is
connected, outcome 3 holds.  Its order bound follows from

\[
                      |C|=|V(G)|-9\ge16.              \tag{2.15}
\]

If `O` has two components `C,E`, then seven-connectivity gives
`|N_G(E)|\ge7`.  Thus `E` is full at `N_G(z)`, giving outcome 4, or it
misses exactly one member of `N_G(z)`, giving outcome 1.  These cases and
the preceding order-seven cases are exhaustive.

We prove the response assertions in outcome 1.  Let

\[
                         S=N_G(E)=N_G(z)-\{r\}.         \tag{2.16}
\]

The set `S` is an order-seven cut, so the critical seven-cut theorem makes
its two complementary components full.  Every edge of `T` lies outside
the open component `E`: the three star edges have centre end `z` and leaf
ends in `N_G(z)`, while `f` lies in the different exterior component `C`.
Consequently, after restoring `T`, the restriction

\[
                           c_J|G[E\cup S]              \tag{2.17}
\]

is proper for every nonempty `J\subseteq T`.  If its equality partition
on `S` extended through the intact opposite closed shore, align the colour
names on the boundary blocks and glue; this would six-colour `G`.
Therefore every displayed partition is rejected on the opposite shore.

Now choose a crossing edge `h=es`, with `e\in E` and `s\in S`, and
six-colour `G-h`.  Its ends have one colour, since otherwise `h` could be
restored.  Deleting `E` removes the sole conflict, so the restriction to
`G-E` is proper, and the same gluing argument shows that its boundary
partition is rejected by the intact `E`-shore.  If this partition equalled
one of those from (2.17), the two legal oppositely oriented shore
colourings would align and glue to a six-colouring of `G`.  Hence it is
different from all fifteen.  These shore restrictions do not alter the
fixed model already present in the original host `H`.  Since the fresh
crossing edge `h` belongs to `H`, however, we make no claim that this model
survives in `H-h`.  This proves outcome 1 and completes the theorem.
`\square`

## 3. Exact contribution and first obstruction

The theorem removes an entire topology rather than returning another
unlabelled separator: a remote order-seven component cannot be the whole
anti-neighbourhood of its exceptional centre.  Whenever the other exterior
component is nonfull, all fifteen nonempty operation signatures, including
the mixed star/remote signatures which were not proper on either original
closed shore, become proper on one new exact-seven closed shore.  A fresh
crossing-edge response supplies the opposite orientation and is partition-
disjoint from all fifteen.

Outcomes 2--4 are the exact first obstructions, not claimed closures.

- In outcome 2 the original order-seven interface retains the seven
  centre-star labels in one orientation and the remote-edge label in the
  other.  The audited exact-seven theorems do not turn those separately
  chosen responses into one common partition or assign them to contacts of
  the fixed exact model.

- In outcome 3 the full boundary has only the singleton `{z}` opposite an
  unbounded connected component.  The operation-coupled order-eight
  theorems return response fans or fresh exact-seven responses, but do not
  convert the remote edge or a star coordinate into a prescribed branch-
  set contact.
- In outcome 4 the existing both-full reduction gives seven finite boundary
  types and packing vector `(1,1,1)`.  Its demand allocations arise from
  separately chosen colourings; the present operation signatures do not
  identify those demands with the fixed exact-model labels.

Thus the first unsupported inference is an operation-preserving
response-to-model allocation on the cross-miss/full exact-seven interface
or on one of the two order-eight interfaces.  No common boundary partition,
common Kempe pivot, or common branch-set ownership is inferred here.

## 4. Dependency map

1. The
   [remote-edge operation cube](../results/hc7_k7minus_remote_removable_edge_operation_cube.md)
   supplies `f,T`, all fifteen nonempty signatures, the fixed exact model,
   and the initial order-seven/eight boundary.
2. The
   [low-degree exterior-component bound](../results/hc7_low_degree_exterior_component_bounds.md)
   reduces `G-N_G[z]` to one or two components.
3. The
   [exact three-full-subgraph completion](../results/hc7_k7minus_exact7_three_full_subgraph_completion.md)
   gives `\chi(G[Q])\le3` in the hypothetical connected order-seven row.
4. The
   [three-component seven-cut exclusion](../results/hc7_k7minus_three_component_seven_cut_exclusion.md)
   supplies the exact two-component topology behind every order-seven cut.
5. The
   [both-full shore reduction](../results/hc7_k7minus_both_full_shore_reduction.md)
   gives the seven boundary types and packing vector in outcome 4.

The decisive two-vertex-shore colouring argument is proved directly in
Theorem 2.1, so no active or unaudited dependency is used.
