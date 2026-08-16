# Cyclic stability of the remote edge in the order-seven and both-full two-component cases

**Status:** complete written reductions and one computer-assisted finite
lemma;
[separate internal audit GREEN](hc7_k7minus_remote_two_component_shore_stability_audit.md).
The retained standard-library
verifier is
[`hc7_k7minus_remote_two_component_shore_stability_verify.py`](hc7_k7minus_remote_two_component_shore_stability_verify.py).
This theorem eliminates every bridge realization of the remote edge in the
order-seven cross-miss/full case and in the order-eight both-full case.  It
does not eliminate the resulting connected full shore, the `K_7^-` six-colour
conjecture, or `HC_7`.

## 1. Setting and the three-shore response matrix

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

Fix an exceptional degree-eight vertex `z`, put `X=N_G(z)`, and let
`f=uv` be a remote seven-removable edge from the audited
[operation-cube theorem](../results/hc7_k7minus_remote_removable_edge_operation_cube.md).
Thus

\[
                  f\in E(G-N_G[z]),
                  \qquad G-f\text{ is seven-connected}.          \tag{1.2}
\]

Let `C` be the component of `G-N_G[z]` containing `f`.  Assume throughout
this note that there is exactly one other exterior component `E`.  Choose
an independent triple `I=\{x_1,x_2,x_3\}\subseteq X`, put

\[
       F_z=\{zx_1,zx_2,zx_3\},\qquad
       T=F_z\cup\{f\},\qquad H=G-T,                  \tag{1.3}
\]

and, for every nonempty `J\subseteq T`, choose a six-colouring `c_J` of
`H` with equality signature exactly `J`.  Write `pi_J` for its equality
partition on the full eight-set `X`.  When `A\subseteq I`, identify `A`
with its spoke set `\{zx:x\in A\}\subseteq F_z` and abbreviate the
corresponding partitions by `pi_A` and `pi_{A\cup\{f\}}`.

For `D\in\{C,E,\{z\}\}`, let `L_D(X)` be the set of equality partitions
on `X` induced by proper six-colourings of the closed shore `G[D\cup X]`.

### Theorem 1.1 (complete three-shore operation matrix)

The fifteen operation-labelled partitions satisfy

\[
 \begin{array}{rcl}
  \pi_J&\in&L_E(X)\qquad(\varnothing\ne J\subseteq T),\\
  \pi_A&\in&L_C(X)-L_{\{z\}}(X)
       \qquad(\varnothing\ne A\subseteq I),\\
  \pi_{\{f\}}&\in&L_{\{z\}}(X)-L_C(X),\\
  \pi_{A\cup\{f\}}&\notin&L_C(X)\cap L_{\{z\}}(X)
       \qquad(\varnothing\ne A\subseteq I).
 \end{array}                                         \tag{1.4}
\]

In particular, `pi_{\{f\}}` differs from all seven centre-star
partitions.  At least four of the seven centre-star partitions are
distinct, so the one-coordinate family

\[
        \{\pi_A:\varnothing\ne A\subseteq I\}
                   \cup\{\pi_{\{f\}}\}              \tag{1.5}
\]

contains at least five distinct partitions.  The seven mixed partitions
also contain at least four distinct members.

#### Proof

Every edge of `T` lies outside `G[E\cup X]`: the three spoke edges have
centre end `z`, while both ends of `f` lie in `C`.  Hence every `c_J`
restricts properly to the closed `E`-shore.

If `J=A\subseteq F_z` is nonempty, all its monochromatic restored edges
meet `z`, so `c_A` is also proper on `G[C\cup X]`.  If the same partition
were accepted on the closed `z`-shore, these two restrictions and the
`E`-restriction would align on `X` and glue to a six-colouring of `G`.
Thus `pi_A` is rejected at `z`.  The symmetric argument for the `f`-only
colouring gives proper restrictions on the `z`- and `E`-shores and
rejection on the `C`-shore.  For a mixed signature, the `E`-restriction is
proper.  Acceptance of its partition on both other closed shores would
again give three colourings with one common boundary partition and hence a
six-colouring of `G`.  This proves (1.4), including the disjointness in
(1.5).

In a colouring with star signature indexed by a nonempty
`A\subseteq I`, the colour block of `z` meets `X` in exactly `A`: the
unselected leaves differ from `z` by signature exactness, and every member
of `X-I` differs from `z` across a kept edge.  Two equal boundary
partitions cannot have intersecting unequal sets as blocks.  The four sets

\[
              I,\qquad I-\{x_1\},\qquad I-\{x_2\},
                         \qquad I-\{x_3\}             \tag{1.6}
\]

are pairwise intersecting and unequal, proving four-way distinctness.
The same visible-block argument applies to the mixed signatures.  The
`f`-only partition lies outside the entire star family by (1.4), proving
the five-partition assertion. `\square`

Theorem 1.1 is deliberately a language matrix, not an assertion that the
fixed exact `K_7^\vee` model survives any fresh edge deletion or that a
partition names one of its branch sets.

## 2. The order-seven shore is operation-stable

Assume now that

\[
                         Q=N_G(C)=X-\{w\}.             \tag{2.1}
\]

The promoted
[topological reduction](../results/hc7_k7minus_remote_interface_topological_reduction.md)
says that `E` is full at `X` or misses exactly one vertex `r\in Q`, and in
either case `w` has a neighbour in `E`.

For a component `D` of `G-Q`, let `\mu_Q(D)` be the maximum number of
pairwise vertex-disjoint connected subgraphs of `D` that are each adjacent
to every vertex of `Q`.

### Theorem 2.1 (the remote edge is nonseparating in the packing-one shore)

The order-seven cut `Q` has full-subgraph packing vector exactly `(1,2)`,
with `\mu_Q(C)=1`.  Moreover,

\[
                         G[C]-f\text{ is connected}               \tag{2.2}
\]

and is still `Q`-full.  Thus `f` lies on a cycle wholly contained in
`G[C]`.

#### Proof

The set `Q` is a seven-cut, so its two complementary components are full.
If `E` is `X`-full, the joined component
`E\cup\{w,z\}` contains the two disjoint connected `Q`-full subgraphs `E`
and `{z}`.

Suppose instead that `E` misses `r\in Q`.  The components `C,E` then have
the distinct misses `w,r`.  The audited
[distinct nonadjacent-miss elimination](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md)
forces `wr\in E(G)`; otherwise the host is already impossible.  The sets
`E\cup\{w\}` and `{z}` are now disjoint connected `Q`-full subgraphs in the
joined component.  Indeed `E` sees `Q-\{r\}`, the edge `wr` repairs its
one missing boundary contact, and the forced `wE` edge gives
connectedness.

In either case the joined component has full-subgraph packing number at
least two, while `C` itself contains one connected `Q`-full subgraph.  The
critical seven-cut capacity theorem bounds the sum of the two packing
numbers by three and makes one side have packing number one.
Consequently the vector is exactly `(1,2)` with

\[
                             \mu_Q(C)=1.               \tag{2.3}
\]

If `G[C]-f` were disconnected, deleting the one edge `f` would leave
exactly two components `A,B`.  In the seven-connected graph `G-f`, each of
their external neighbourhoods is contained in the seven-set `Q` and is an
actual separator.  Hence

\[
                         N_{G-f}(A)=N_{G-f}(B)=Q.       \tag{2.4}
\]

The two sets `A,B` would be disjoint connected `Q`-full subgraphs of `C`,
contrary to (2.3).  This proves (2.2).  Deleting the internal edge does not
remove any `C-Q` contact, so the connected graph `G[C]-f` remains `Q`-full.
An edge whose deletion leaves its connected component connected lies on an
internal cycle. `\square`

## 3. The finite bridge-split lemma at order eight

The following exact quotient is the only computer-assisted input new to
this note.  Let `K_7^-` mean any seven-bag minor model having at least
twenty of the twenty-one pairwise bag adjacencies.

### Lemma 3.1 (seven boundary types reject every near-full bridge split)

Let `B` be any of the seven graph6 boundary types

```text
GCOcaO  GCOcbO  GCOcbW  GCOe`W  GCOebW  GCQQV?  GCQR@O
```

on the literal eight-set `X`.  Add four vertices `z,e,a,b` such that

1. `z` and `e` are complete to `X`;
2. each of `a,b` is adjacent to at least seven vertices of `X`;
3. `ab` is an edge; and
4. there is no other edge among `z,e,a,b`.

The resulting graph contains a `K_7^-` minor.

#### Finite verification

If `a` or `b` is complete to `X`, delete one arbitrary incident edge.
It is therefore enough to check that each of `a,b` misses exactly one
boundary vertex.  Interchanging `a,b` makes their ordered miss pair
irrelevant, leaving

\[
                         7\binom{8+1}{2}=252           \tag{3.1}
\]

cases.  The retained verifier decodes the seven promoted graph6 strings
and, in every case, performs an exact deletion/contraction search from the
twelve singleton objects.  At seven surviving connected bags it accepts
exactly when at least twenty bag pairs are adjacent, and independently
rechecks connectedness, disjointness and every contact of the returned
certificate.  It reports

```text
boundary_types=7 digest=bf063de64c772c1c9c1c83cba7dc39d11bb9c214f3e101595889fe63f25861a0
bridge_split_cases=252 terminal=252 survivors=0
certificate_digest=311f08b508413fdc416b5af98e20abe0c45b86dafe890c8c88402b73e1565c8c
PASS remote two-component shore stability finite lemma
```

The search is exact because deletion discards unused quotient vertices and
contracting touching bags generates every connected branch set.  Conversely
every reported family is checked directly and is therefore a literal
minor certificate. `\square`

## 4. The both-full shore is operation-stable

Assume now that `C,E` are both full at

\[
                              X=N_G(z).                \tag{4.1}
\]

The audited both-full reduction makes `G[X]` one of the seven types in
Lemma 3.1 and gives full-subgraph packing vector

\[
                   (\mu_X(\{z\}),\mu_X(C),\mu_X(E))=(1,1,1).     \tag{4.2}
\]

### Theorem 4.1 (the both-full remote edge is nonseparating)

One has

\[
                         G[C]-f\text{ connected and }X\text{-full}.       \tag{4.3}
\]

In particular, `f` lies on a cycle wholly contained in `G[C]`.

#### Proof

Suppose `G[C]-f` is disconnected.  It has exactly two components `A,B`,
one containing each end of `f`.  In `G-f`, the neighbourhood of each is
contained in `X`; seven-connectivity therefore gives

\[
                         |N_{G-f}(A)|,|N_{G-f}(B)|\ge7.            \tag{4.4}
\]

Contract `A,B,E` separately, retain the singleton `z` and every literal
vertex of `X`, and restore `f` as the edge between the two first
contraction images.  Different exterior components are anticomplete and
`z` has no exterior neighbour.  The resulting minor is exactly a graph
from Lemma 3.1, possibly with one extra image-to-boundary edge at each full
image.  Deleting one such edge from every full image if necessary gives the
verified quotient and
hence a `K_7^-` minor of `G`, a contradiction.  Thus `G[C]-f` is connected.
The edge `f` is internal to `C`, so its deletion preserves all literal
`C-X` contacts and the connected remainder is `X`-full.  The cycle
conclusion follows. `\square`

The finite step is used only to rule out a bridge.  It does not replace the
seven-type both-full classification or assert a rooted model in the
connected remainder.

## 5. Boundary-partition demand forced by the operation

For a proper partition `Pi` of a boundary graph `B`, put

\[
 d_B(\Pi)=|\Pi|-\omega\bigl(B[\operatorname{sing}(\Pi)]\bigr),   \tag{5.1}
\]

the exact number of pairwise disjoint connected full subgraphs needed by
the reflection construction after retaining a maximum clique of singleton
blocks.

### Lemma 5.0 (order-free exact boundary-colouring reflection)

Let

\[
 V(G)=L\mathbin{\dot\cup}S\mathbin{\dot\cup}R,
\]

where `L` and `R` are nonempty and anticomplete, and suppose every proper
minor of `G` is six-colourable.  Let `Pi` be a partition of `S` into at
most six independent blocks.  If `G[L]` contains `t` pairwise
vertex-disjoint connected subgraphs that are each adjacent to every vertex
of `S`, and

\[
                  1\le d_{G[S]}(\Pi)\le t,             \tag{5.2}
\]

then `G[R\cup S]` has a proper six-colouring whose equality partition on
`S` is exactly `Pi`.

#### Proof

Let `U` be a maximum clique in the subgraph of `G[S]` induced by the
singleton blocks of `Pi`.  Retain the vertices of `U`, assign each of the
remaining `d_{G[S]}(\Pi)` blocks injectively to one of the connected full
subgraphs, and contract a spanning tree of the union of each assigned
subgraph with its boundary block.  At least one edge is contracted by
(5.2), so the resulting minor is proper.  The contraction images together
with `U` form a clique, one vertex for each block of `Pi`, of order at most
six.  Six-colour the minor, keep its colours on `R\cup U`, and give every
vertex of an assigned block the colour of its contraction image.  All
crossing adjacencies were represented in the minor, and distinct blocks
receive distinct colours, so this is the required colouring. `\square`

### Theorem 5.1 (high-demand operation partitions)

1. In the order-seven case, on `Q=N_G(C)`, the `f`-only response partition
   has at most five blocks and demand at least three.  Every nonempty
   centre-star response on the same boundary has demand at least two.
2. In the order-eight both-full case, every centre-star partition and the
   `f`-only partition on `X` has demand at least three.  Every mixed
   star-plus-`f` partition has demand at least two.

#### Proof

In the order-seven case, the `f`-only colouring is proper on the rich
closed shore and rejected by the intact `C`-shore.  The rich component has
two disjoint connected `Q`-full subgraphs by Theorem 2.1.  If its partition
had demand at most two, Lemma 5.0 would reproduce it exactly on the
`C`-shore, and the two colourings would glue.  Thus its demand is at least
three.  The colour of `z` is absent from `Q\subseteq N(z)` in this response,
so at most five
colours occur on `Q`.  A centre-star response is proper on `C` and rejected
on the rich shore.  Since `C` contains one connected `Q`-full subgraph,
demand at most one would let Lemma 5.0 reproduce that partition on the
rich shore, again a contradiction.  This proves item 1.

In the both-full case, a star response is proper simultaneously on the
`C`- and `E`-shores.  If its demand were at most two, the two connected
full subgraphs `C,E` would reproduce that partition on the `z`-shore by
Lemma 5.0, contradicting the first rejection in (1.4).  The `f`-only case
is symmetric, using the connected full subgraphs `{z},E` to reproduce the
partition on `C`.  Finally a mixed response is proper on the `E`-shore.
Demand at most one would let the single connected full subgraph `E`
reproduce it on the combined opposite shore `C\cup\{z\}` by Lemma 5.0,
producing a matching partition and a six-colouring of `G`.  Hence mixed
demand is at least two. `\square`

These are operation-forced partitions, not minimum-demand claims about the
boundary.  The existing shore-allocation barrier correctly shows that
boundary counting and independent-triple rotation alone do not concentrate
the underlying Kempe demands.

### Corollary 5.2 (five visible partitions at the exact-seven boundary)

In the order-seven case one may choose `I\subseteq Q`.  For that choice the
seven centre-star partitions and the remote partition on `Q` contain at
least five distinct partitions, with the remote partition having at most
five blocks and demand at least three.

#### Proof

The one-nonfull and distinct-adjacent-miss reductions both give
`\alpha(G[Q])=3`, so choose an independent triple in `Q`.  The visible
block argument in Theorem 1.1 gives four distinct star partitions.  The
remote partition differs from every one by opposite-shore gluing, and Theorem 5.1
gives its block and demand bounds. `\square`

## 6. Four literal cycle placements

### Corollary 6.1 (one internal and three centre cycles)

In either two-component case, the remote edge `f` belongs to four distinct
literal cycles:

1. one cycle is wholly contained in `G[C]`; and
2. for each two-set `\{x_i,x_j\}\subseteq I`, one cycle contains all
   three edges `f,zx_i,zx_j`.

#### Proof

The internal cycle is Theorem 2.1 or 4.1.  For a two-set of leaves, the
three selected edges form the componentwise-induced linear forest

\[
                         K_2\mathbin{\dot\cup}P_3.     \tag{6.1}
\]

The audited
[linear-forest cycle-or-separation theorem](../results/hc7_k7minus_linear_forest_cycle_or_exact7_response.md)
uses the Haggkvist--Thomassen independent-path theorem; because `G` is
seven-connected, well above the four-connectivity threshold for this
three-edge forest, one cycle contains all three edges.  The three leaf
pairs give different cycles, since a simple cycle uses exactly two edges
at `z`.  None is the internal cycle, which avoids `z`. `\square`

## 7. Existing closures and frozen dead ends

The preceding theorems sit after, rather than before, the established
two-component reductions.

1. If `E` is full and `C` misses `w`, the
   [one-nonfull reduction](../results/hc7_k7minus_nonfull_attachment_reduction.md)
   already gives the `(1,2)` cut, its 28 boundary types and the attachment
   bounds at `w`.  The
   [six-fan and nested-cut theorem](../results/hc7_k7minus_one_nonfull_k5_and_nested_cut.md)
   and the
   [shore-localized non-double-critical response](../active/hc7_k7minus_one_nonfull_nondouble_palette.md)
   leave a non-tight attachment or response-to-rooted-model allocation.
   The verified
   [two-entrance barrier](../barriers/hc7_k7minus_nonfull_two_entrance_allocation_barrier.md)
   rules out deriving the missing third branch set from connectivity and the
   two entrances alone.  Theorem 2.1 adds the information those arguments
   did not spend: their packing-one shore contains the fixed operation as a
   nonseparating internal edge.
2. If both exterior components are nonfull, the
   [nonadjacent-miss theorem](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md)
   leaves only adjacent misses.  The
   [adjacent-miss operation descent](../active/hc7_k7minus_adjacent_miss_operation_descent.md)
   supplies four operated paths, two full shore fans and a rooted `K_4`,
   or a smaller exact-seven response separation.  Its clean residue needs
   set-rooted absorption; an ordinary point-rooted model can intersect a
   foreign operated path.  Repeating that point-rooted step is therefore
   not a valid continuation.
3. In the both-full case, the
   [seven-type boundary reduction](../results/hc7_k7minus_both_full_shore_reduction.md),
   [rooted-diamond alternative](../active/hc7_k7minus_both_full_diamond_or_exact7.md)
   and
   [component-contraction dichotomy](../active/hc7_k7minus_both_full_component_contraction_dichotomy.md)
   leave rooted-model allocation or a wide cutvertex-block residue.  The
   [shore-allocation barrier](../barriers/hc7_k7minus_shore_allocation_barrier.md)
   shows that static nonedge labels, fullness and independent-triple
   rotation do not force the required concentration.  The high-demand
   partitions in Theorem 5.1 are compatible with that warning; they are new
   dynamic restrictions, not a boundary-only closure.
4. The fixed exact `K_7^\vee` model still exists in the original host
   `G-T`, but none of the results above identifies the colour block of the
   remote operation with one of its bags.  The response matrix does not
   justify reselecting the model independently for each partition, and a
   fresh crossing-edge deletion need not preserve it.

Thus boundary enumeration, whole-component contraction, unlabelled rooted
models and operation-independent shore splitting are already exhausted.
The internal cyclic operation is the new datum that a continuation must
use.

## 8. Exact surviving configurations and next lemma

The two requested cases no longer contain a tree-like or bridge-supported
remote operation.

- **Order seven:** `C-f` is connected and `Q`-full with
  `\mu_Q(C)=1`.  The actual `f`-response has at most five boundary blocks
  but boundary-partition demand at least three, and a triple chosen in `Q`
  gives five distinct visible partitions.  The full, one-nonfull and
  adjacent-miss results do not align those partitions with a rooted model.
- **Order eight both-full:** `C-f` is connected and full, all three full
  components have packing number one, every one-coordinate operation partition
  has demand at least three, and the boundary remains one of the seven
  promoted types.  The whole-component contraction and static
  shore-allocation routes do not use the internal cycle and remain
  nonterminal.

The exact next sufficient statement is therefore the following
operation-sensitive split lemma.

> **Cyclic full-shore split-or-response lemma.**  Let `S` be the displayed
> order-seven or order-eight boundary, let `C` be its packing-one connected
> full shore, and let `f=uv` be an internal edge such that `C-f` is
> connected and `G-f` is seven-connected.  Using the fixed `f`-deletion
> colouring, either:
>
> 1. split `C` into connected endpoint sides `A,B`, with `u\in A`,
>    `v\in B`, such that each side meets at least seven vertices of `S`;
> 2. return an actual order-seven separator with a proper restriction of
>    the same `f`-response and a strictly smaller open side; or
> 3. construct a `K_7^-` minor.

Outcome 1 is already terminal here: at order seven it contradicts the
packing-one conclusion, while at order eight Lemma 3.1 gives the explicit
minor.  Outcome 2 supplies a genuine operation-preserving descent.  Thus
this split-or-response lemma, rather than another boundary-only demand
allocation or whole-component contraction, is the smallest concrete
missing theorem for both two-component cases.

## 9. Dependencies and trust boundary

- [remote removable-edge operation cube](../results/hc7_k7minus_remote_removable_edge_operation_cube.md);
- [remote-interface topological reduction](../results/hc7_k7minus_remote_interface_topological_reduction.md);
- [critical seven-cut capacity](../results/hc7_k7minus_critical_seven_cut_capacity.md);
- [distinct nonadjacent-miss elimination](../results/hc7_k7minus_distinct_miss_fan_tree_elimination.md);
- [one-nonfull attachment reduction](../results/hc7_k7minus_nonfull_attachment_reduction.md);
- [both-full seven-type and full-subgraph packing reduction](../results/hc7_k7minus_both_full_shore_reduction.md);
- [boundary-demand identity](../results/hc7_exact7_packet_demand_identity.md);
- [linear-forest cycle-or-separation theorem](../results/hc7_k7minus_linear_forest_cycle_or_exact7_response.md); and
- [exact boundary-colouring reflection](../results/hc7_k7minus_critical_seven_cut_capacity.md#lemma-1-exact-boundary-colouring-reflection).

Theorem 4.1 inherits the finite trust boundary of the seven-type
classification and adds the independently retained 252-case quotient
verification in Lemma 3.1.  All other arguments are computation-free.
