# Strict-surplus `K_4`-reserve aggregation verdict

**Baseline:** `c61b10ab197d344ca531760cd1877c2b3f50819e`  
**Status:** unaudited working note.  The deductions below are intended for
hostile independent audit before any promotion.  They do not prove the
seven-connected `4n-2` extremal theorem, the auxiliary statement `(E5)`,
Conjecture 21, or `HC_7`.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.  Let `G` be a
counterexample of minimum order and then minimum size to

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G,
\]

and suppose

\[
 q=q(G):=|E(G)|-(4|V(G)|-2)\ge1.
\]

Put

\[
 L=\{v:d_G(v)=7\},\qquad F=G-L.
\]

The attack tests whether the audited six-cut `K_4`-reserve inequality can
be aggregated across the many degree-seven vertices supplied by the strict-
surplus structure.  The conclusion is negative: the reserve inequality is
visible only at degree-seven vertices lying in the unique possible literal
`K_5`, while a strict-surplus enemy has many degree-seven vertices outside
that clique.  The attack nevertheless isolates an exact rooted six-terminal
obstruction for those reserve-blind vertices.

---

## 1. Canonical six-cut at every degree-seven vertex

Fix `x in L` and `y in N_G(x)`.  Put

\[
 H=G-xy,\qquad T=N_G(x)-\{y\}.
\]

Then

\[
                 H-T=\{x\}\mathbin{\dot\cup}B_y,
\]

where `B_y` is connected, and both `{x}` and `B_y` are adjacent to every
vertex of `T`.

### Proof

The vertex `x` is isolated in `H-T`.  Let `C` be the component of
`H-T-x` containing `y`.  If another component `D` existed, restoring the
single edge `xy` would join `x` only to `C`; the component `D` would remain
separated in `G-T`, contrary to seven-connectivity because `|T|=6`.

The audited essential-edge six-separation theorem makes `H` six-connected,
so every component of `H-T` is full to `T`.  Its exact shore identity gives

\[
 \delta_{\{x\}}+\delta_{B_y}=21+q-|E(G[T])|.
\]

Since

\[
 \delta_{\{x\}}=6-4=2,
\]

one obtains

\[
 \boxed{\delta_{B_y}=19+q-|E(G[T])|.}                 \tag{1}
\]

Moreover, `G[T]` has no `K_5^-` minor.

Equivalently, with

\[
 J_x:=G-x=B_y\cup T,
\]

one has

\[
 \boxed{
 (J_x,T)\text{ internally six-connected},\qquad
 |E(J_x)|=4|V(J_x)|-5+q.}                            \tag{2}
\]

For `q>=1`, this is at least `4|V(J_x)|-4`.  A `T`-rooted `K_6` model in
`J_x`, together with the singleton `{x}`, would be a `K_7` model.  Thus no
such rooted model exists.

Direct inputs:

- [`essential-edge six-separation`](../../../results/hc7_k7minus_essential_edge_six_separation.md)
- [`degree-six cut capacity and excess`](../../hc7_k7minus_degree6_cut_capacity_excess.md)

---

## 2. Reserve visibility is confined to one literal `K_5`

For `x in L`, the neighbourhood `N_G(x)` contains a literal `K_4` if and
only if `x` belongs to a literal `K_5`.

The unconditional audited two-clique theorem says that a six-connected
`K_7^-`-minor-free graph contains at most one literal `K_5`.  Therefore
there is a single clique `K`, possibly nonexistent, such that

\[
 \boxed{
 \{x\in L:N_G(x)\text{ contains a literal }K_4\}=L\cap K.}
                                                               \tag{3}
\]

Hence the reserve inequality is available at at most five degree-seven
vertices.

Jakobsen's extremal inequality applied to `G` gives

\[
 2|E(G)|\le9|V(G)|-25.
\]

Since `|E(G)|=4|V(G)|-2+q`,

\[
 |V(G)|\ge21+2q.
\]

The audited strict-surplus identity gives

\[
 |L|-|F|\ge2
\]

with the same parity as `|V(G)|`.  Consequently

\[
 \boxed{|L|\ge13.}                                    \tag{4}
\]

Combining (3) and (4),

\[
 \boxed{
 \text{at least eight degree-seven vertices have `K_4`-free neighbourhoods.}}
                                                               \tag{5}
\]

This is the decisive negative finding for the proposed aggregation:

> The `K_4`-reserve inequality cannot be aggregated over the many degree-
> seven vertices.  It is visible only on the unique-`K_5` stratum, which
> contains at most five of them.

Direct inputs:

- [`two literal K_5 subgraphs force K_7^-`](../../../results/hc7_k7minus_two_literal_k5_exclusion.md)
- [`strict-surplus minimal enemy`](../../../results/hc7_k7minus_strict_surplus_minimal_enemy.md)

---

## 3. What reserve aggregation proves on the visible stratum

Let `x in L cap K`.  Put

\[
 Z=K-\{x\},\qquad W=N_G(x)-Z.
\]

Thus `|Z|=4`, `G[Z]=K_4`, and `|W|=3`.

For every distinct `p,q in W`, let `y` be the third member of `W`.  The
canonical essential-edge boundary for `xy` is

\[
 T=Z\cup\{p,q\}.
\]

The audited reserve inequality gives

\[
 \boxed{d_G(p)+d_G(q)\ge15+q+\mathbf1_{pq\in E(G)}.}  \tag{6}
\]

Consequently:

1. `W` contains at most one degree-seven vertex.
2. Every literal `K_4` in `N_G(x)` contains at least
   `d_{G[L]}(x)-1` degree-seven neighbours of `x`.
3. Since `G[F]` is a forest, a literal `K_4` contains at most two vertices
   of `F`.  Therefore
   \[
   d_{G[L]}(x)\ge6
   \quad\Longrightarrow\quad
   N_G(x)\text{ is `K_4`-free}.
   \]
4. Summing (6) over the three pairs of `W` gives
   \[
   \boxed{
   2\sum_{w\in W}(d_G(w)-7)
   \ge3+3q+|E(G[W])|.}                                \tag{7}
   \]

No vertex outside `K` can have four neighbours in `K`, since that would
produce a second literal `K_5`.  Thus any high-degree vertex can receive
charge from at most three vertices of `L cap K`.  The global degree identities
nevertheless leave enough high-degree capacity for this charge to
concentrate in `F`, so (7) does not give a contradiction.

The reserve inequality remains useful as a unique-`K_5` local constraint,
not as the global positive-surplus mechanism.

Direct input:

- [`six-cut K_4-reserve inequality`](../../../results/hc7_k7minus_six_cut_k4_reserve_inequality.md)

---

## 4. The complementary `K_4`-free boundary is sharply sparse

Let `x in L-K`, choose any `y in N(x)`, and put

\[
 T=N(x)-\{y\}.
\]

Then `G[T]` is `K_4`-free.  The essential-edge theorem also says it has no
`K_5^-` minor.

### Lemma 4.1

Every six-vertex graph containing neither a literal `K_4` nor a `K_5^-`
minor has at most ten edges.

### Proof

Suppose it has at least eleven edges, and delete edges until exactly eleven
remain.  Its complement has four edges and independence number at most
three.

Up to isomorphism, a four-edge graph on six vertices with independence
number at most three is one of

\[
 K_1\mathbin{\dot\cup}K_2\mathbin{\dot\cup}K_3,
 \qquad
 K_2\mathbin{\dot\cup}P_4.
\]

In the first case, contract in the original graph an edge joining a vertex
of the complementary `K_2` to a vertex of the complementary `K_3`.  The two
ends have exactly one common neighbour, namely the vertex isolated in the
complement.

In the second case, write the complementary components as an edge `ab` and
a path `c-d-e-f`.  Contract `ae`.  Again the two ends have exactly one
common neighbour, namely `c`.

In either case the contraction removes two edges from an eleven-edge graph
and produces a five-vertex graph with nine edges, which is `K_5^-`.  This is
a contradiction.  Therefore

\[
                         |E(G[T])|\le10.               \tag{8}
\]

Substituting (8) into (1) gives

\[
                         \boxed{\delta_{B_y}\ge9+q.}   \tag{9}
\]

Thus every reserve-blind degree-seven vertex returns the exact rooted pair

\[
 \boxed{
 \begin{aligned}
 &(G-x,T)\text{ is internally six-connected},\\
 &|T|=6,\quad G[T]\text{ is `K_4`-free and `K_5^-`-minor-free},\\
 &|E(G-x)|=4|V(G-x)|-5+q,\\
 &\delta_{B_y}\ge9+q,\\
 &G-x\text{ has no `T`-rooted `K_6` model}.
 \end{aligned}}                                      \tag{10}
\]

This is the exact positive-surplus obstruction.  It is also the unresolved
two-component row in the existing degree-six cut programme: that note
closes several three-component boundary ranges but explicitly leaves the
two-component case open.

---

## 5. Exact aggregate inequalities on the `K_4`-free stratum

Retain the strict-surplus notation

\[
 \ell=|L|,\quad f=|F|,\quad c=c(F),\quad
 t=|E(G[F])|=f-c,\quad d=\ell-f,
\]

and write

\[
 e_L=|E(G[L])|.
\]

The audited strict-surplus identities give

\[
                         \boxed{e_L=3d-c-q+2.}         \tag{11}
\]

Three `K_4`-free spanning subgraphs of `G`, followed by Jakobsen's
inequality, yield the following necessary conditions.

### 5.1 Deleting all `L`-edges

The graph `G-E(G[L])` is `K_4`-free because `L` is independent and `F` is
a forest.  Hence

\[
                         \boxed{7d+2t\ge4q+17.}        \tag{12}
\]

### 5.2 Keeping a maximum cut of `G[L]`

Let `M` be a maximum cut of `G[L]`, so `|M|>=e_L/2`.  Delete all other
`L`-edges and all `F`-edges.  The remaining graph is tripartite and hence
`K_4`-free.  This gives

\[
                         \boxed{4d+f+3t\ge3q+19.}      \tag{13}
\]

### 5.3 When `G[L]` is a matching

If `Delta(G[L])<=1`, deleting the forest edges leaves a `K_4`-free graph.
Then

\[
                         \boxed{2f+d+2t\ge2q+21.}      \tag{14}
\]

These inequalities do not contradict the strict-surplus identities.  For
example, the arithmetic tuple

\[
 (q,d,f,c,t,e_L)=(1,2,11,7,4,0)
\]

satisfies (11)--(14).  Counting plus `K_4`-free extremal theory alone does
not finish the positive-surplus layer.

---

## 6. Pair deletion supplies a common model interface

For distinct `a,b in L`, put

\[
 H=G-\{a,b\}.
\]

Then `H` is five-connected and

\[
 \begin{aligned}
 |E(H)|
   &=|E(G)|-14+\mathbf1_{ab\in E(G)}\\
   &=4|V(H)|-8+q+\mathbf1_{ab\in E(G)}.
 \end{aligned}
\]

Since `|V(G)|>=23`, the small Norin--Totschnig exception is impossible.
Thus `H` contains a spanning exact `K_7^vee` model.

The standard target-exclusion restrictions apply:

- each retained root meets at most four of the six mutually adjacent bags;
- if it meets the deficient bag `P`, it misses both deficient
  nonneighbours `B,C`;
- `a,b` cannot both meet all five bags
  \[
  P,U_1,U_2,U_3,U_4.
  \]

Absorbing `P` into a universal bag gives a spanning `K_6` model.  Optimising
one retained root's number of contacted bags and then minimising a branch
set containing at least two of its neighbours produces the forced portal
interface already developed in the repository: all but at most four target
portals are cutvertices of the donor branch set.

This is the right common framework for two reserve-blind degree-seven
roots.  It does not yet bound or split the potentially long cutvertex
interface.

Direct input:

- [`pair deletion and spanning K_7^vee model`](../../hc7_k7minus_pair_deletion_k7vee_reduction.md)

---

## 7. The `q>=3` layer is contraction-critical, but this is insufficient

Every common neighbour of an edge lies in the associated six-cut of its
deletion, so

\[
 |N(u)\cap N(v)|\le6.
\]

Consequently

\[
 q(G/uv)=q+3-|N(u)\cap N(v)|.
\]

When `q>=3`, every edge contraction is density-safe.  A seven-contractible
edge would therefore produce a smaller counterexample.  Hence

\[
 \boxed{
 q\ge3
 \quad\Longrightarrow\quad
 G\text{ is both minimally and contraction-critically seven-connected}.}
                                                               \tag{15}
\]

Published contraction-critical results do not supply the required
adjacency among degree-seven vertices.  Known examples can have independent
degree-seven vertices.  Thus contraction-criticality cannot repair the
reserve-blind stratum by itself.

---

## 8. Short four-root `K_6`-placement screen

The secondary conjecture tested was:

> If `J` is four-connected, `Z` induces `K_4`, and `J` has a `K_6` minor,
> then `J` has a `Z`-rooted `K_{4,2}` model.

No counterexample was found in the following diagnostic searches:

- all graph-atlas graphs of order at most seven: `128` eligible rooted
  instances;
- all order-eight extensions of a fixed literal `K_6`: `56,295` eligible
  rooted instances;
- `12,304` order-eight hosts containing a specified split-bag `K_6` model:
  `211,015` eligible rooted instances.

These searches were not retained, independently checked, or used in any
proof.  The literature pass found no theorem at the required connectivity
and coefficient-four density.  This conjecture should remain a short
secondary target rather than become another open-ended programme.

---

## 9. Complementary bipartite route

Let

\[
 A=\{x\in L:d_{G[L]}(x)\le1\}.
\]

Every member of `A` has at least six neighbours in `F`.  If

\[
 |A|\ge|F|,
\]

then the bipartite graph consisting of the `A`--`F` edges contains an
unrooted `K_6` minor by the known bipartite `K_6`-minor theorem.

Since at most `e_L` vertices of `L` can have `L`-degree at least two,

\[
 |A|\ge\ell-e_L.
\]

Thus this route applies whenever

\[
 d\ge e_L.
\]

Using (11), its complementary arithmetic case is

\[
                         2d>c+q-2.
\]

This is a useful non-enumerative dichotomy.  The bipartite theorem supplies
an unrooted `K_6`; upgrading it to `K_7^-` still requires a degree-seven
vertex to meet five named bags or a label-preserving split.  It therefore
does not close the proof by itself.

---

## 10. Final conclusion and exact next theorem

The reserve-aggregation campaign establishes the following working
conclusion:

\[
 \boxed{
 \begin{array}{l}
 \text{the `K_4`-reserve sees only degree-seven vertices in one literal `K_5`;}\\
 \text{there are at most five such vertices and at least eight outside it;}\\
 \text{the outside vertices return the exact rooted pair in (10).}
 \end{array}}
\]

The correct next theorem is therefore not a further aggregate of
`K_4`-reserve inequalities.

> **Canonical six-root placement-or-descent theorem.**  Let `G` be a
> strict-surplus minimum counterexample, let `x in L` lie outside the unique
> possible literal `K_5`, choose `y in N(x)`, and put
> \[
> T=N(x)-\{y\},\qquad J=G-x.
> \]
> Under the exact properties in (10), prove at least one of:
>
> 1. `J` has a `T`-rooted `K_6` model, giving a `K_7` model with `{x}`;
> 2. `G` has a density-preserving seven-connected proper minor;
> 3. there is another canonical instance in the same host with a strictly
>    smaller connected high shore; or
> 4. two canonical instances cross to give an explicit `K_7^-` model.

At least eight suitable vertices `x` exist, so this theorem would eliminate
the entire positive-surplus layer.

The most efficient current architecture is:

1. use the bipartite `K_6` theorem when `d>=e_L`;
2. use the pair-deletion spanning `K_7^vee/K_6` interface when `d<e_L`;
3. preserve two selected degree-seven labels through every donor transfer;
4. convert a blocked transfer into an actual order-seven cut ranked by the
   order of its connected operated shore; and
5. use the `q>=3` contraction-critical structure only as an additional
   constraint, not as the principal engine.

This note is experimental provenance.  Before promotion, every displayed
new lemma and inequality must receive a separate hostile audit, including
verification of the complement classification in Lemma 4.1 and the three
aggregate inequalities in Section 5.
