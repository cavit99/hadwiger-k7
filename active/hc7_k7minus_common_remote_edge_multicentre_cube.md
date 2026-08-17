# One removable edge is simultaneously remote from several exceptional centres

**Status:** active written proof; adjacent cold audit GREEN after the two
precision repairs incorporated below.  All the theorems in this note are
unconditional deductions inside the critical-host setting.  They do not
prove the `K_7^-` six-colour conjecture or `HC_7`.

The point of this note is global.  It does not choose a different remote edge
at each degree-eight vertex.  Contracting an arbitrary edge and applying the
sharp defect ladder shows that **every edge is remote from at least fourteen
exceptional centres**, and hence from three independent exceptional
centres.  A second double count shows that one exceptional centre is remote
from three edges of one common seven-removable matching.

These two conclusions give complementary common hosts.  The first combines
three independent centres with one removable edge on a seven-edge forest
having eleven vertices.  It carries all `2186` nontrivial mixed minor
operations, all `127` nonempty equality signatures, and a spanning exact
`K_7^\vee` model.  The second combines one centre with two edges of the
matching on a four-edge forest.  Its deletion graph is exactly six-connected,
and its natural degree-six cut has a singleton side and one connected full
opposite side.  This latter conclusion uses all five matching coordinates:
three select the common remote centre and the other two survive in the exact
six-boundary host.

## 1. Critical-host setting

Let `G` be a minor-minimal counterexample to the proposed `K_7^-`
six-colour theorem.  We use the audited critical-host conclusions

\[
 \begin{gathered}
  \chi(G)=7,
  \qquad \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,\\
  \kappa(G)\geq7,
  \qquad \delta(G)\geq8,
  \qquad |E(G)|\geq4|V(G)|,
  \qquad |V(G)|\geq25,\\
  K_7^-\npreccurlyeq G,
  \qquad K_5\not\subseteq G.
 \end{gathered}                                                   \tag{1.1}
\]

Let

\[
 B=\{z\in V(G):d_G(z)=8\},\qquad b=|B|,                         \tag{1.2}
\]

and put

\[
 s(v)=\max\{d_G(v)-9,0\},
 \qquad
 \tau=\sum_{v\in V(G)}s(v)
      =\sum_{i\geq10}(i-9)n_i.                                  \tag{1.3}
\]

The degree identity and the audited connectivity defect ladder give

\[
                             b\geq27+\tau.                       \tag{1.4}
\]

Every member `z` of `B` is exceptional: its eight-vertex neighbourhood is
`K_4`-free and

\[
                         \alpha(G[N_G(z)])=3.                    \tag{1.5}
\]

For an edge `e=uv`, define its set of remote exceptional centres by

\[
 \mathcal R(e)=
 \{z\in B:\{u,v\}\cap N_G[z]=\varnothing\}.                    \tag{1.6}
\]

## 2. The global edge--centre incidence bound

Put

\[
                         D=b-\tau.                              \tag{2.1}
\]

The exact degree sum and the defect ladder give

\[
             2|E(G)|=9|V(G)|-D,
             \qquad D\geq27.                                   \tag{2.2}
\]

For an edge `e=uv`, write

\[
                         c(e)=|N_G(u)\cap N_G(v)|.              \tag{2.3}
\]

### Lemma 2.1 (the contraction defect of every edge)

Every edge `e` of `G` satisfies

\[
                            D+2c(e)\geq32.                       \tag{2.4}
\]

#### Proof

Contract `e`.  The resulting simple graph has `|V(G)|-1` vertices and

\[
                         |E(G)|-1-c(e)                           \tag{2.5}
\]

edges.  Contracting one edge of a seven-connected graph leaves a
six-connected graph.  The contraction remains target-free and has order at
least twenty-four.  It is neither base graph `K_6` or `K_{2,2,2,2}` nor a
nontrivial `(K_{2,2,2,2},K_6,4)`-cockade: every nontrivial such cockade has
a four-cut.  Jakobsen's theorem and integrality therefore give

\[
 2(|E(G)|-1-c(e))\leq9(|V(G)|-1)-25.                            \tag{2.6}
\]

Substitute (2.2) and rearrange. `\square`

### Theorem 2.2 (every edge is remote from fourteen centres)

For every edge `e=uv` of `G`,

\[
 |B-\mathcal R(e)|
      \leq16+s(u)+s(v)-c(e),                                    \tag{2.7}
\]

and consequently

\[
 |\mathcal R(e)|
   \geq14+\tau-s(u)-s(v)
   \geq14.                                                       \tag{2.8}
\]

#### Proof

Let `\epsilon` be the number of ends of `e` which belong to `B`.  The
degree definition gives

\[
 d_G(u)+d_G(v)=18+s(u)+s(v)-\epsilon.                            \tag{2.9}
\]

Because `uv` is an edge, both ends belong to
`N_G(u)\cup N_G(v)`, and exactly `2-\epsilon` of those two known vertices
are not exceptional.  Hence

\[
\begin{aligned}
 |B\cap(N_G(u)\cup N_G(v))|
 &\leq d_G(u)+d_G(v)-c(e)-(2-\epsilon)\\
 &=16+s(u)+s(v)-c(e).
\end{aligned}                                                    \tag{2.10}
\]

The left side of (2.10) is exactly `B-\mathcal R(e)`, proving (2.7).
Lemmas 2.1 and (2.2), with integrality, imply

\[
 D+c(e)\geq30:                                                   \tag{2.11}
\]

for `27\leq D\leq31` this follows by minimizing
`D+\lceil(32-D)/2\rceil`, while for `D\geq32` it is immediate.
Using `b=D+\tau` in (2.7) now gives (2.8). `\square`

No removability hypothesis is used in Theorem 2.2.

### Lemma 2.3 (thirteen exceptional centres contain an independent triple)

Every subset `A\subseteq B` of order at least thirteen contains three
pairwise nonadjacent vertices.

#### Proof

Suppose `\alpha(G[A])\leq2`.  For each `z\in A`, the nonneighbours of `z`
inside `A` form a clique: two nonadjacent such vertices together with `z`
would be an independent triple.  The literal `K_5` exclusion says that
this clique has order at most four.  Hence

\[
                         d_{G[A]}(z)\geq|A|-5.                  \tag{2.12}
\]

If `|A|\geq14`, (2.12) contradicts `d_G(z)=8`.  If `|A|=13`, equality in
the degree bound makes every neighbour of every vertex of `A` lie in `A`.
Thus no edge joins `A` to its complement.  This contradicts connectedness
of `G`, since `|V(G)|\geq25`. `\square`

### Corollary 2.4 (an independent triple shares every edge)

For every edge `f` of `G`, there are independent exceptional centres
`z_1,z_2,z_3` such that

\[
                         f\in E(G-N_G[z_i])
                         \qquad(1\leq i\leq3).                  \tag{2.13}
\]

#### Proof

Apply Lemma 2.3 to the fourteen-vertex set supplied by Theorem 2.2.
`\square`

### Theorem 2.5 (one centre misses three edges of the common matching)

Let `M` be any matching of order five.  Then

\[
 \sum_{z\in B}|\{e\in M:z\in\mathcal R(e)\}|
      \geq5b-80-\tau+\sum_{e\in M}c(e)>2b.                     \tag{2.14}
\]

Consequently some exceptional centre is remote from at least three edges
of `M`.  This holds in particular for Chu's seven-removable matching.

#### Proof

Sum (2.7) over `M`.  Its ten endpoints are distinct, so their total
`s`-value is at most `\tau`.  Double-counting the complementary incidences
gives the weak inequality in (2.14).

For strictness, subtract `2b` and use `b=D+\tau`.  The result is at least

\[
 3D+2\tau-80+
 5\left\lceil\frac{\max\{32-D,0\}}2\right\rceil.                \tag{2.15}
\]

For `D=27,\ldots,31`, the expression without `2\tau` is respectively

\[
                         16,14,17,15,18,
\]

and for `D\geq32` it is at least sixteen.  Thus (2.14) is strict.  An
average larger than two forces one centre to occur at least three times.
`\square`

### Corollary 2.6 (Ramsey staircase for a low-excess matching edge)

Let `M` be a seven-removable matching of order five.  Some `f=uv\in M`
satisfies

\[
 |\mathcal R(f)|
    \geq14+\tau-\left\lfloor\frac{\tau}{5}\right\rfloor.       \tag{2.16}
\]

This set contains four independent centres if `\tau\geq9`, and five
independent centres if `\tau\geq23`.

#### Proof

Choose `f=uv` minimizing `s(u)+s(v)` and apply (2.8).  More generally, let
`A\subsetneq V(G)` be a subset of `B` with no independent set of order
`r+1`.  The nonneighbours of any `z\in A` contain neither an independent
`r`-set nor a `K_5`.
Therefore

\[
              d_{G[A]}(z)\geq|A|-R(r,5).                        \tag{2.17}
\]

The degree-eight and connectedness argument from Lemma 2.3 shows that
`|A|\geq R(r,5)+8` is impossible.  Apply this to the proper set
`A=\mathcal R(f)`, which omits both ends of `f`.  Now use the exact values
`R(3,5)=14` and `R(4,5)=25`, whose thresholds are twenty-two and
thirty-three, respectively. `\square`

## 3. A universal two-centre five-edge forest

Choose a seven-removable edge `f=uv`; for example, take one edge of Chu's
seven-removable matching.  Corollary 2.4 gives three independent centres
remote from `f`; retain any two and call them `z_1,z_2`.

Choose a nonadjacent pair

\[
                         I_1=\{x_1,y_1\}\subseteq N_G(z_1).       \tag{3.1}
\]

This is possible by (1.5).  The set `N_G(z_2)-I_1` has order at least six
and is `K_4`-free, so it is not complete.  Choose a nonadjacent pair

\[
             I_2=\{x_2,y_2\}\subseteq N_G(z_2)-I_1.              \tag{3.2}
\]

The eight vertices displayed below are distinct: the centres are
nonadjacent, `f` is remote from both, and the two leaf pairs were chosen
disjointly.  Put

\[
 F=\{z_1x_1,z_1y_1,z_2x_2,z_2y_2,f\}
      \cong P_3\mathbin{\dot\cup}P_3\mathbin{\dot\cup}K_2.       \tag{3.3}
\]

Every component of this selected-edge forest is induced on its own vertex
set in `G`.  Edges between different components are allowed.

For disjoint `C,D\subseteq F`, let `G/C-D` denote the graph obtained by
contracting `C`, deleting `D`, and keeping the edges of
`F-(C\cup D)`.

### Theorem 3.1 (the full two-centre mixed-operation cube)

For every pair of disjoint sets `C,D\subseteq F` with
`C\cup D\ne\varnothing`, one has

\[
                              \chi(G/C-D)=6.                       \tag{3.4}
\]

Thus the five labelled edges in (3.3) support all

\[
                                  3^5-1=242                         \tag{3.5}
\]

nontrivial keep/delete/contract patterns as exactly six-chromatic proper
minors of the same graph.

#### Proof

Every graph in (3.4) is a proper minor of `G` and is therefore at most
six-colourable.  Suppose one has a proper five-colouring.  Expand each
contracted component of `F`, initially giving its vertices the colour of
its contraction image.

For `i=1,2`, if at least one selected edge at `z_i` is contracted or
deleted, recolour `z_i` with one fresh sixth colour.  If `f` is contracted
or deleted, recolour `u` with the same fresh colour.  The repair vertices

\[
                              z_1,z_2,u                             \tag{3.6}
\]

are independent: the centres were chosen nonadjacent and `f` is remote
from both.  Every other neighbour of a repair vertex retains one of the
original five colours.  Componentwise inducedness of `F` ensures that no
unselected edge was collapsed during contraction.  Every operated edge is
now proper, and each kept selected edge was represented in the minor and
remains proper.  This is a six-colouring of `G`, a contradiction.
`\square`

Put

\[
                                K=G-F.                              \tag{3.7}
\]

For a proper six-colouring `c` of `K`, write

\[
                  \Sigma_F(c)=\{ab\in F:c(a)=c(b)\}.              \tag{3.8}
\]

### Theorem 3.2 (connectivity, signatures, and exact models)

The graph `K` has all of the following properties.

1. It is exactly six-chromatic and

   \[
      \{\Sigma_F(c):c\in\operatorname{Col}_6(K)\}
                            =2^F-\{\varnothing\}.                  \tag{3.9}
   \]

2. Its connectivity and density satisfy

   \[
                    5\leq\kappa(K)\leq6,
                    \qquad |E(K)|\geq4|V(K)|-5.                  \tag{3.10}
   \]

3. It has a spanning `K_7^\vee` model.  In a target-free `G`, the two
   nominally missing bag pairs are anticomplete even after all five edges
   of `F` are restored.  Thus the model is exact in `G`.
4. The all-contraction quotient `G/F` is exactly six-chromatic and has a
   spanning `K_6` model.  On expansion, each of the two selected paths and
   the edge `f` is contained in one branch set; these three branch sets may
   coincide.

#### Proof

The exact chromatic statement for `K` is the all-delete case of Theorem
3.1.  For nonempty `Q\subseteq F`, six-colour `G/Q` and expand the
contracted components.  Forestness makes every edge of `F-Q` survive as a
genuine quotient edge, and componentwise inducedness prevents any other
edge of `K` from collapsing.  The resulting colouring of `K` has signature
exactly `Q`.  An empty signature would remain proper after restoring `F`
and would six-colour `G`.  This proves (3.9).

Let `J=G-f`, which is seven-connected.  The graph `K` is obtained from
`J` by deleting the four displayed spokes.  Suppose `S` of order at most
four disconnects `K`.  Let `Z_0` be the set of centres outside `S` whose
restored spokes join different components of `K-S`.  Then
`|S\cup Z_0|\leq6`.  Every component of `K-S` retains a vertex after
`Z_0` is removed.  Indeed, a component contained in `Z_0` would be a
singleton centre because the two centres are independent, but
`d_K(z_i)=6>|S|`.  Once `Z_0` is removed, no restored spoke joins two of
the old components.  Hence `S\cup Z_0` disconnects `J`, contradicting its
seven-connectivity.  Thus `\kappa(K)\geq5`.  Each centre has degree six in
`K`, proving the upper bound.  Deleting the five distinct edges gives the
density bound.

The graph `K` is four-connected and lies above the density threshold in
Norin--Totschnig, Theorem 6.  The exceptional graph `K_{2,2,2,2}` is
excluded by `|V(G)|\geq25`, so `K` has a `K_7^\vee` model.  Absorb unused
vertices to make it spanning.  If either nominally missing bag pair were
joined by an edge of `G`, the same bags would form a `K_7^-` model in `G`.
Target exclusion therefore makes both pairs anticomplete in `G`.

Finally, exact six-chromaticity of `G/F` is the all-contraction case of
Theorem 3.1.  The established case `HC_6` supplies a `K_6` model, which may
be made spanning.  Expanding the three contraction images gives the
asserted co-baggings. `\square`

### Corollary 3.3 (two simultaneous saturated neighbourhood partitions)

For `i=1,2`, let `c_i` be a colouring of `K` with signature precisely the
two spokes incident with `z_i`.  The colour multiplicities on
`N_G(z_i)` are

\[
                              2,2,1,1,1,1.                         \tag{3.11}
\]

One repeated pair is `I_i`; among the other six neighbours there is one
further repeated pair and four singleton colour classes.

#### Proof

The two vertices of `I_i` have the colour of `z_i`.  The other six edges
at `z_i` are present in `K`, so none of their ends has that colour.  If
some one of the six colours were absent from `N_G(z_i)`, assigning that
colour to `z_i` would repair its two monochromatic spokes.  Every other
edge of `F` is already proper in the chosen singleton-pair signature, so
this would six-colour `G`.  Thus all six colours occur on the eight
neighbours.  The asserted multiplicities follow. `\square`

### Proposition 3.4 (the exact five-cut residue)

If `K` is not six-connected and `S` is a five-vertex cut, then neither
centre lies in `S`, both selected two-spoke paths have a spoke joining
different components of `K-S`, and

\[
                         S\cup\{z_1,z_2\}                         \tag{3.12}
\]

is an order-seven cut of the seven-connected graph `J=G-f`.

#### Proof

Define `Z_0` from `S` as in the proof of Theorem 3.2.  If
`|Z_0|\leq1`, deleting `S\cup Z_0` disconnects `J`; the component-
survival argument remains valid because `d_K(z_i)=6>|S|`.  This contradicts
seven-connectivity.  Hence `Z_0=\{z_1,z_2\}`, which gives every assertion.
`\square`

### Theorem 3.5 (singleton exposure or an eight-vertex separator)

The exact model of Theorem 3.2 supplies a nonempty proper connected set
`Y` inside one universal branch set such that the remainder of that branch
set is connected and `R=N_G(Y)` is an actual separator of order at least
seven.  In addition, one of the following holds.

1. A singleton-edge signature from (3.9) is proper on one closed side of
   `R`, and its boundary partition is rejected by the intact opposite
   closed side.
2. The set `Y` avoids `V(F)` and

   \[
                              V(F)\subseteq R,
                              \qquad |R|\geq8.                    \tag{3.13}
   \]

#### Proof

Apply the audited exact-`K_7^\vee` model-separator dichotomy to the
spanning model in the seven-connected graph `G`.  The minor outcome is
excluded by (1.1), so it returns `Y` and `R`.

For `q=ab\in F`, choose a colouring of `K` with signature `{q}`.  After
restoring `F`, its only monochromatic edge is `q`.  If `Y` contains an end
of `q`, its restriction to `G-Y` is proper.  If `Y` contains neither end
and at most one end lies in `R`, then `q` is absent from the other closed
side `G[Y\cup R]`.  In either case, extension of the induced boundary
partition through the intact opposite side would glue to a six-colouring
of `G`.

If the first outcome fails for every selected edge, `Y` contains no
selected endpoint and both ends of every selected edge lie in `R`.  The
forest has eight distinct vertices, proving (3.13). `\square`

## 4. The universal three-centre forest

Let `M` be a seven-removable matching of order five and choose any
`f=uv\in M`.  By Corollary 2.4, choose independent centres

\[
                         Z=\{z_1,z_2,z_3\}\subseteq\mathcal R(f). \tag{4.1}
\]

We may select pairwise disjoint nonadjacent pairs

\[
                         I_i=\{x_i,y_i\}\subseteq N_G(z_i)
                         \qquad(1\leq i\leq3).                    \tag{4.2}
\]

Indeed, choose `I_1` first.  At the second step at least six vertices of
the `K_4`-free neighbourhood remain, and at the third step at least four
remain.  A complete remaining set at either step would contain a literal
`K_4`.  The centres are independent and `f` is remote from all three, so
the eleven displayed vertices are distinct.  Put

\[
 F_7=\{z_ix_i,z_iy_i:1\leq i\leq3\}\cup\{f\}
       \cong3P_3\mathbin{\dot\cup}K_2.                            \tag{4.3}
\]

Again every component is induced on its own vertex set.

### Theorem 4.1 (the universal seven-edge cube)

For every nontrivial keep/delete/contract pattern on `F_7`, the resulting
proper minor is exactly six-chromatic.  Equivalently, `F_7` supports all

\[
                                 3^7-1=2186                         \tag{4.4}
\]

nontrivial mixed operation patterns.

For `L=G-F_7`,

\[
 \begin{gathered}
  \chi(L)=6,
  \qquad
  \{\Sigma_{F_7}(c):c\in\operatorname{Col}_6(L)\}
       =2^{F_7}-\{\varnothing\},\\
  4\leq\kappa(L)\leq6,
  \qquad |E(L)|\geq4|V(L)|-7.                                  \tag{4.5}
 \end{gathered}
\]

Thus all `127` nonempty equality signatures occur on one common graph.
The graph `L` has a spanning exact `K_7^\vee` model in `G`, and `G/F_7`
is exactly six-chromatic with a spanning `K_6` model co-bagging each of
the three selected paths and the edge `f`.

#### Proof

The proof of Theorem 3.1 applies verbatim with the independent repair set

\[
                              z_1,z_2,z_3,u.                         \tag{4.6}
\]

This gives (4.4).  Expanding contractions exactly as in Theorem 3.2 gives
all nonempty signatures and excludes the empty one.

Let `J=G-f`.  If a set `S` of order at most three disconnects `L`, remove
from `J-S` every centre whose restored spokes cross components of `L-S`.
At most three centres are removed, and every component survives because
the centres are independent and have degree six in `L`, greater than
`|S|`.  The resulting set of order at most six disconnects `J`, a
contradiction.  Hence `\kappa(L)\geq4`; the degree-six centres give the
upper bound.  The density statement follows by deleting seven distinct
edges.

Norin--Totschnig, Theorem 6, now supplies the spanning `K_7^\vee` model,
and target exclusion makes its two missing pairs anticomplete in `G`.
The all-contraction conclusion follows from (4.4) and `HC_6`, exactly as
in Theorem 3.2. `\square`

### Proposition 4.2 (the exact four-cut residue)

If `S` is a four-vertex cut of `L`, then all three centres lie outside
`S`, every selected two-spoke path has a crossing spoke in `L-S`, and

\[
                              S\cup Z                              \tag{4.7}
\]

is an order-seven cut of `J=G-f`.

#### Proof

If at most two centres have restored spokes crossing components of
`L-S`, deleting those centres together with `S` gives a cut of `J` of
order at most six.  The component-survival argument in Theorem 4.1 again
applies because `d_L(z_i)=6>|S|`.  Thus all three centres cross, and the
displayed seven-set disconnects `J`. `\square`

### Corollary 4.3 (singleton exposure or an eleven-vertex separator)

For the exact spanning model in `L`, the model-separator dichotomy either
exposes a singleton `F_7`-signature on an actual separator, or returns a
connected side `Y` disjoint from `V(F_7)` with

\[
                            V(F_7)\subseteq N_G(Y),
                            \qquad |N_G(Y)|\geq11.                 \tag{4.8}
\]

#### Proof

Repeat the proof of Theorem 3.5.  The forest `F_7` has eleven distinct
vertices. `\square`

## 5. A common-matching exact six-boundary host

Let `M` be Chu's seven-removable matching.  Theorem 2.5 supplies an
exceptional centre `z` and three edges of `M` remote from `z`.  Among those
three edges there are two, say

\[
                    e_1=u_1v_1,\qquad e_2=u_2v_2,                \tag{5.1}
\]

whose ends may be oriented so that `u_1u_2` is not an edge.  Indeed, if
every two of the three endpoint pairs were cross-complete, the ends of two
matching edges would induce a `K_4`, and either end of the third edge would
complete a literal `K_5`.

Put

\[
                         J=G-\{e_1,e_2\}.                        \tag{5.2}
\]

The graph `J` is seven-connected, because it contains the seven-connected
spanning graph `G-M`.  The next selection makes the natural degree-six cut
connected on its nonsingleton side.

### Lemma 5.1 (two leaves with connected remainder)

There is an independent triple `I=\{a,b,t\}\subseteq N_G(z)` such that

\[
 J-\bigl((N_G(z)-\{a,b\})\cup\{z\}\bigr)                       \tag{5.3}
\]

is connected.

#### Proof

Start with any independent triple `I=\{p,q,r\}` in `N_G(z)` and put

\[
 Q=N_G(z)-I,
 \qquad
 R=J-(Q\cup\{z\}).                                               \tag{5.4}
\]

The graph `R` is connected, since only six vertices were deleted from the
seven-connected graph `J`.  For `x\in I`, the graph
`J-(Q\cup\{x\})` is also connected.  It is obtained from `R-x` by adding
`z`, whose neighbours there are exactly `I-\{x\}`.  Consequently every
component of `R-x` contains one of the two vertices of `I-\{x\}`.  Thus
`R-x` is disconnected precisely when `x` separates the other two members
of `I` in `R`.

The three cyclic separations cannot all occur.  For example, if `q`
separates `p` from `r`, a simple `p`--`r` path contains `q`; its
`p`--`q` initial segment avoids `r`, contrary to `r` separating `p` from
`q`.  Choose `t\in I` for which `R-t` is connected, and call the other two
members `a,b`.  Since

\[
 (N_G(z)-\{a,b\})\cup\{z\}=Q\cup\{t,z\},
\]

the graph in (5.3) is `R-t`. `\square`

Fix the leaves from Lemma 5.1 and put

\[
 F_4=\{za,zb,e_1,e_2\}
       \cong P_3\mathbin{\dot\cup}K_2\mathbin{\dot\cup}K_2,
 \qquad K_4=G-F_4.                                               \tag{5.5}
\]

The subscript on `K_4` records the four deleted coordinates, not its
connectivity.

### Theorem 5.2 (full four-cube and exact connected six-boundary)

The graph `K_4` has all of the following properties.

1. Every nontrivial keep/delete/contract pattern on `F_4` is exactly
   six-chromatic.  Thus all

   \[
                                3^4-1=80                           \tag{5.6}
   \]

   nontrivial mixed patterns occur.
2. The exact equality-signature language on `K_4` is

   \[
     \{\Sigma_{F_4}(c):c\in\operatorname{Col}_6(K_4)\}
                            =2^{F_4}-\{\varnothing\}.             \tag{5.7}
   \]

3. One has

   \[
                  \kappa(K_4)=6,
                  \qquad |E(K_4)|\geq4|V(K_4)|-4.                \tag{5.8}
   \]

4. With

   \[
                   T=N_{K_4}(z)=N_G(z)-\{a,b\},                 \tag{5.9}
   \]

   the graph `K_4-T` has exactly two components, the singleton `{z}` and
   one connected component `C`; both are full to the six-set `T`.
5. The graph `K_4` has a spanning exact `K_7^\vee` model in `G`.  The
   all-contraction quotient `G/F_4` is exactly six-chromatic and has a
   spanning `K_6` model which, on expansion, co-bags the path `a-z-b` and
   each of `e_1,e_2`.

#### Proof

For a nontrivial mixed pattern, five-colour the resulting proper minor and
expand its contracted selected components.  If either spoke was operated,
recolour `z` with one fresh sixth colour.  If `e_i` was operated, recolour
`u_i` with that same fresh colour.  The three repair vertices

\[
                              z,u_1,u_2                             \tag{5.10}
\]

are independent: the matching edges are remote from `z` and `u_1u_2` was
chosen to be a nonedge.  The leaves `a,b` are nonadjacent, so every
selected component is induced on its own vertex set.  The repaired
colouring is therefore a six-colouring of `G`, a contradiction.  This
proves item 1.

For nonempty `Q\subseteq F_4`, six-colour `G/Q` and expand.  Every edge in
`Q` is monochromatic and every edge in `F_4-Q` remains a genuine quotient
edge.  The resulting colouring of `K_4` has signature exactly `Q`.  An
empty signature would colour `G`.  This proves item 2.

To prove connectivity, suppose `S` of order at most five disconnects
`K_4`.  If `z\in S`, then `J-S=K_4-S`, contradicting seven-connectivity of
`J`.  If `z\notin S`, the component of `K_4-S` containing `z` has another
vertex because

\[
                              d_{K_4}(z)=6>|S|.                    \tag{5.11}
\]

Deleting `S\cup\{z\}` therefore leaves vertices from that component and
from another component, and
`J-(S\cup\{z\})=K_4-(S\cup\{z\})` is disconnected.  This contradicts
seven-connectivity of `J`.  Thus `K_4` is six-connected; (5.11) gives
equality.  Deleting four edges gives the density assertion.

Lemma 5.1 says that

\[
 C=K_4-(T\cup\{z\})
\]

is connected.  The definition of `T` makes `{z}` the other component of
`K_4-T`.  Six-connectivity says that neither component can miss a member
of the six-set `T`, proving fullness.

Finally, Norin--Totschnig's density theorem gives the spanning
`K_7^\vee` model, and target exclusion makes its two missing pairs
anticomplete even after `F_4` is restored.  Item 1 applied to the
all-contraction pattern makes `G/F_4` exactly six-chromatic.  The
established case `HC_6`, followed by absorption and expansion, gives the
stated co-bagging. `\square`

### Corollary 5.3 (the exact palette law at the connected cut)

Let `c` be any proper six-colouring of `K_4` in which both `e_1,e_2` are
bichromatic.  Every palette colour absent from `c(T)` occurs on at least
one of `a,b`.  Consequently `T` uses at least four colours.

In a colouring with signature exactly `\{za,zb\}`, the boundary `T` uses
the five colours different from `c(z)`, with multiplicity shape

\[
                              2+1+1+1+1.                          \tag{5.12}
\]

In a singleton-spoke signature, a second colour absent from `T`, if one
exists, is necessarily the colour of the other leaf.

#### Proof

The colour of `z` is absent from `T`.  If a palette colour `\gamma` were
absent from both `T` and `{a,b}`, recolour `z` with `\gamma` and restore
all four selected edges.  The matching edges are already proper, so this
would six-colour `G`.  This proves the first assertion.

If both spokes are the precise signature, the two leaves have colour
`c(z)`.  Any other colour absent from `T` would then be absent from the
leaves as well, contradicting the first assertion.  Thus five colours
occur on the six vertices of `T`, giving (5.12).  In a singleton-spoke
signature the same argument leaves only the other leaf available to carry
a second missing colour. `\square`

## 6. Global endpoint visibility and bounded labelled re-entry

The eleven-vertex forest `F_7` repairs a label loss in the exact-model
separator route.  The following conclusion uses only the exact spanning
model and singleton signatures already proved above, followed by the
audited large-actual-boundary descent.

### Theorem 6.1 (an original coordinate survives to order at most nine)

Either `G` has a `K_7^-` minor, or there are

* an actual boundary `R` with `7\leq|R|\leq9`;
* one closed side of that boundary; and
* an original edge `q\in F_7`

such that the singleton-`q` signature colouring from Theorem 4.1 is proper
on that closed side and its partition on `R` is rejected by the intact
opposite side.

#### Proof

Apply the exact-model separator dichotomy to the spanning model of Theorem
4.1.  A minor outcome is the first conclusion.  Otherwise it returns a
nonempty connected side `Y` with actual boundary

\[
                              S=N_G(Y),\qquad |S|\geq7.           \tag{6.1}
\]

If `|S|\geq10`, repeatedly apply Corollary 2.2 of the audited
[matching-lock actual-boundary reduction](../results/hc7_k7minus_matching_lock_boundary_reduction.md).
Boundary order strictly decreases, so the process ends
at a singleton-side actual boundary

\[
                         R=N_G(w),\qquad7\leq|R|\leq9.           \tag{6.2}
\]

If the original boundary already has order at most nine, put `R=S`.

The boundary `R` has fewer than the eleven distinct vertices of `F_7`, so
choose `q\in F_7` which is not contained in `R`.  Let `Y_0` be one open
side and let `Z_0=V(G)-N_G[Y_0]`, which is nonempty because the boundary is
actual.  No edge joins `Y_0` to `Z_0`.  Therefore `q` has an end in at least
one of these two open sides.  Restrict the singleton-`q` colouring to the
opposite closed side.  Its unique conflict has been removed, so this
restriction is proper.  If its boundary partition extended through the
intact side containing that conflict, the two colourings would glue and
six-colour `G`.  Hence the intact opposite side rejects it. `\square`

The coordinate in Theorem 6.1 is one of the six named centre spokes or the
common remote edge.  No fresh descent edge replaces it.

### Corollary 6.2 (multiplicity and the unique one-coordinate residue)

Put `\mathcal Q(R)` for the selected edges of `F_7` which are not wholly
contained in `R`.  Every member of this set supplies an original-coordinate
response on `R` by the proof of Theorem 6.1.  Its size is at least three,
two, or one when `|R|` is seven, eight, or nine, respectively.

At least one available coordinate is a centre spoke, except in the unique
one-coordinate configuration:

\[
 |R|=9,\qquad
 R=\bigcup_{i=1}^3\{z_i,x_i,y_i\},\qquad
 \mathcal Q(R)=\{f\}.                                           \tag{6.3}
\]

In configuration (6.3), if the boundary was produced by the singleton
descent, say `R=N_G(w)`, then `d_G(w)=9`, the vertex `w` is distinct from
every endpoint of `F_7`, and the removable edge `f` lies in `G-N_G[w]`.

#### Proof

The forest `F_7` has eleven vertices, and every selected vertex has positive
degree in `F_7`.  If `|R|=8`, at least three selected vertices are omitted;
one selected edge covers at most two of them, proving the asserted lower
bound two.  If `|R|=7`, four vertices are omitted.  Two selected edges could
cover four omitted vertices only if both were isolated `K_2` components:
using the centre of a selected `P_3` also exposes its other spoke.  There is
only one isolated `K_2`, proving the lower bound three.  The order-nine
lower bound is immediate.

Equality one at order nine forces the two omitted vertices to be the ends
of the only isolated component `f`.  This is exactly (6.3).  In every other
case some spoke is not contained in `R`, and the proof of Theorem 6.1
applies separately to each available coordinate.

In the singleton row, `N_G(w)=R` gives `d_G(w)=9`.  If `w` were an endpoint
of `f`, its matching mate would belong to `R`, impossible.  It is not a
path vertex either because all path vertices already lie in `R`.  Thus both
ends of `f` lie outside `N_G[w]`. `\square`

## 7. Exact scope

The two-centre theorem is universal in the critical host: it applies to
every seven-removable edge, not merely to an edge selected separately for
one exceptional centre.  It improves the one-centre deletion host from
exact connectivity five to connectivity five or six while retaining five
mixed-operation coordinates.  Proposition 3.4 gives the complete
low-connectivity alternative.

The three-centre theorem is universal, not a high-surplus branch.  Its
common edge and independent centres are chosen before the three leaf pairs,
and all seven coordinates live on the same deletion graph and the same
exact near-clique model.  Theorem 6.1 turns its eleven distinct vertices
into an original-coordinate response at an actual boundary of order seven,
eight or nine; the descent never substitutes a fresh operation label.

The common-matching theorem uses the removable matching in the opposite
direction.  One centre sees three matching edges remotely; two of those
edges, together with two carefully chosen spokes, produce an exactly
six-connected deletion host.  Its degree-six cut is not an arbitrary
separator: one side is the selected centre and the other side is connected,
both sides are full, all fifteen nonempty signatures occur, and the two
remote matching coordinates lie on the nonsingleton side before deletion.

Neither large boundary alone is a minor model.  In particular, the exact
`K_7^\vee` model in a deletion host and the spanning `K_6` model in its
all-contraction quotient need not have compatible branch sets.  No such
compatibility is inferred here.  The bounded labelled response of Theorem
6.1 is also not, by itself, a matching colouring on the opposite side of
its boundary.  Its significance is the elimination of both former global
losses: neither common remoteness nor the original operation label is lost.

## 8. Dependencies

- the audited critical-host density, connectivity defect ladder,
  exceptional-neighbourhood and literal `K_5` exclusion theorems;
- Hojin Chu,
  [*A sharp extension of Halin's removable-edge theorem to matchings*,
  Theorem 1.3](https://arxiv.org/abs/2608.09394), for a seven-removable
  matching of order five;
- Sergey Norin and Agnes Totschnig,
  [*Every graph with no `K_7^\vee` minor is 6-colorable*, Theorem 6](https://arxiv.org/abs/2507.03244),
  for the density-to-`K_7^\vee` implication;
- the audited exact-`K_7^\vee` model-separator dichotomy and the established
  case `HC_6`;
- Corollary 2.2 of the audited matching-lock actual-boundary reduction for
  Theorem 6.1; and
- R. E. Greenwood and A. M. Gleason, `R(3,5)=14`, and B. D. McKay and
  S. P. Radziszowski, `R(4,5)=25`, for the two exact Ramsey values in
  Corollary 2.6.
