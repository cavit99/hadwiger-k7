# Connectivity and overlap reduction at equality

**Status:** written proof; separate internal audit GREEN for this revision.
This theorem concerns the equality layer of the proposed `K_7^-`
six-colour route.  It does not prove the two-transversal target, the
`K_7^-` six-colour conjecture, or `HC_7`.

Here `K_7^-` is `K_7` with one edge deleted.  Let `G` be a graph satisfying

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G,                           \tag{H}
\]

and suppose

\[
                         |E(G)|=4|V(G)|-5.              \tag{1}
\]

The previously proved
[density and low-degree rigidity theorem](hc7_k7minus_five_exceptional_vertices_reduction.md)
shows that the ten degree-seven vertices of `G` form two disjoint literal
`K_5`s, say `A` and `B`, and that every other vertex has degree eight.
These are the only literal `K_5`s in `G`.

Put

\[
 R=G-(A\cup B),\qquad r=|V(R)|,
 \qquad M=E_G(A,B),\qquad k=|M|.                        \tag{2}
\]

## Lemma 1 (exact equality bookkeeping)

The set `M` is a matching.  For `a\in A`, put

\[
 T_a=N_G(a)-A,
 \qquad P_a=T_a\cap V(R),                               \tag{3}
\]

and define `T_b,Q_b` symmetrically for `b\in B`.  The five sets `T_a`
are pairwise disjoint triangles.  If `a` is matched to `b\in B`, then

\[
 T_a=\{b,x,y\},\qquad P_a=\{x,y\}=Q_b;                 \tag{4}
\]

otherwise `P_a=T_a` has order three.  Consequently

\[
 \left|\bigcup_{a\in A}P_a\right|
 =\left|\bigcup_{b\in B}Q_b\right|=15-k.               \tag{5}
\]

Every vertex `x\in V(R)` has at most one neighbour in `A` and at most one
neighbour in `B`.  If the two incidence indicators are
`alpha(x),beta(x)\in\{0,1\}`, then

\[
 d_R(x)=8-\alpha(x)-\beta(x),
 \qquad |E(R)|=4r-15+k.                                 \tag{6}
\]

Moreover, if `H_A=G-A`, then

\[
 |E(H_A)|=4|V(H_A)|-10                                 \tag{7}
\]

and its degree sequence is

\[
 6^k\,7^{20-2k}\,8^{|V(H_A)|-20+k}.                   \tag{8}
\]

The symmetric assertions hold for `H_B=G-B`.

### Proof

The exact degree-seven neighbourhood classification in the preceding
theorem gives the private triangles in (3), their pairwise disjointness,
and their anticompleteness to the other four vertices of the corresponding
`K_5`.  Thus no vertex of `B` has two neighbours in `A`, and symmetrically;
so `M` is a matching.  Equation (5) follows because a matched clique vertex
has two neighbours in `R`, while an unmatched one has three.

If `ab\in M` and `T_a=\{b,x,y\}`, trianglehood makes `b` adjacent to
`x,y`.  The degree-seven vertex `b` already has its four neighbours in `B`
and the neighbour `a`, so `T_b=\{a,x,y\}` and (4) follows.

The private-triangle disjointness on each side also says that a vertex of
`R` has at most one neighbour in either clique.  All vertices of `R` have
degree eight, which gives the first identity in (6).  Summing it over `R`
and using

\[
 \sum_{x\in R}(\alpha(x)+\beta(x))=2(15-k)
\]

gives the second identity.  Deleting `A` removes its ten internal edges and
its fifteen external edges, proving (7).  Among the vertices of `H_A`, the
`k` matched vertices of `B` have degree six, the other `5-k` vertices of
`B` have degree seven, and exactly `15-k` vertices of `R` lose an
`A`-neighbour.  This proves (8).  \(\square\)

## Theorem 2 (five-connected clique deletion)

Both `G-A` and `G-B` are five-connected.

### Proof

It is enough to consider `H_A=G-A`.  Suppose that `Z\subseteq V(H_A)`,
`|Z|=t\le4`, and that `H_A-Z` has at least two components.  For a component
`C`, put

\[
 I(C)=\{a\in A:C\cap T_a\ne\varnothing\}.              \tag{9}
\]

Every neighbour of `C` outside `C` lies in `Z\cup I(C)`.  This set
separates `C` from another component of `H_A-Z`, so seven-connectivity of
`G` gives

\[
                         |I(C)|\ge7-t.                 \tag{10}
\]

For distinct components `C,D`, the sets `I(C),I(D)` are disjoint.  Indeed,
the surviving vertices of each `T_a-Z` form a clique and therefore lie in
at most one component.  Two components would consequently require

\[
 5\ge |I(C)|+|I(D)|\ge2(7-t)>5,
\]

a contradiction.  The proof for `G-B` is symmetric.  \(\square\)

## Corollary 3 (three-connected central subgraph)

The graph `R` is three-connected.

### Proof

Suppose that `Z\subseteq V(R)`, `|Z|=t\le2`, and that `R-Z` has at least
two components.  For a component `C`, put

\[
 J(C)=\{b\in B:C\cap Q_b\ne\varnothing\}.              \tag{11}
\]

In the five-connected graph `H_A=G-A`, every neighbour of `C` outside `C`
lies in `Z\cup J(C)`.  Hence

\[
                         |J(C)|\ge5-t.                 \tag{12}
\]

The label sets `J(C)` for distinct components are disjoint, since each
nonempty `Q_b-Z` is a clique.  Two components would require at least
`2(5-t)\ge6` of the five vertices of `B`, a contradiction.  \(\square\)

## Lemma 4 (cross-edge and overlap reduction)

The cross-edge matching has

\[
                              k\le3.                   \tag{13}
\]

Call `x\in V(R)` an **off-matching common neighbour** if

\[
 x\in P_a\cap Q_b
 \quad\text{for some `a\in A,b\in B` with `ab\notin M`.} \tag{14}
\]

Both owners `a,b` of such a vertex are unmatched.  Let `Z` consist of
off-matching common neighbours with distinct owners in `A`.  If `R-Z` is
connected and

\[
                         |Z|\ge4-k,                    \tag{15}
\]

then `G` contains a `K_7^-` minor.

### Proof

The seven connected branch sets

\[
 \{a\}\ (a\in A),\qquad B,\qquad R                    \tag{16}
\]

have every required adjacency except those between `B` and the unmatched
vertices of `A`.  Thus `k\ge4` gives a `K_7^-` model, proving (13).

If an off-matching common neighbour `x` had a matched owner `a`, then the
two vertices of `P_a` would already be adjacent to the unique vertex of
`B` matched to `a`, by (4).  Since `x` has at most one neighbour in `B`,
its `B`-owner in (14) would be that matched vertex, contrary to (14).
The symmetric argument treats its `B`-owner.

For the final assertion, retain the set `Z` from the hypotheses and put

\[
                         X=R-Z,\qquad Y=B\cup Z.        \tag{17}
\]

Both sets are connected: this is assumed for `X`, while every member of
`Z` has a neighbour in the clique `B`.  The set `X` is adjacent to every
vertex of `A`.  A selected external triangle has order three and loses only
one vertex, every unselected one remains intact, and none of the two-vertex
sets belonging to matched vertices of `A` meets `Z`.

The set `Y` is adjacent to the `k` matched vertices of `A` and to the
`|Z|` distinct owners selected by `Z`.  Thus among the five adjacencies
from the singleton branch sets in `A` to `Y`, at most one is missing.
Finally `X` and `Y` are adjacent: the five pairwise disjoint nonempty sets
`Q_b` have union of order `15-k`, whereas `Z` has at most `5-k` vertices
because its members have distinct unmatched owners in `A`.  Hence an edge
from `B` to `R-Z` remains.  The five singleton sets in `A`, together with
`X` and `Y`, are therefore a `K_7^-`-minor model.  \(\square\)

## Lemma 5 (small nonseparating selections)

Let `F` be a three-connected graph with

\[
                    6\le\delta(F)\le\Delta(F)\le8.     \tag{18}
\]

The following statements hold.

1. If `|V(F)|\le18`, `T` is a triangle, and `x,y` are distinct vertices
   outside `T`, then some `z\in T` has

   \[
                         F-\{x,y,z\}\text{ connected}. \tag{19}
   \]

2. Suppose `|V(F)|\le18`, the vertices `x,y,z` have degree six,
   `F-\{x,y,z\}` is connected, and `T` is a triangle disjoint from
   `\{x,y,z\}`.  Then some `w\in T` has

   \[
                    F-\{x,y,z,w\}\text{ connected}.    \tag{20}
   \]

3. If `|V(F)|=18` and `F` has degree sequence `6^{10}7^8`, then, for
   any two distinct degree-six vertices `x,y`, the graph `F-\{x,y\}` has at most
   three cutvertices.

### Proof

For the first assertion, put `Q=F-\{x,y\}`; this graph is connected.
Suppose every member `z` of `T` is a cutvertex of `Q`.  The other two
vertices of `T` lie in one component of `Q-z`, since they are adjacent.
Choose a component `L_z` of `Q-z` avoiding them.  The three sets `L_z` are
pairwise disjoint.  For example, a vertex common to `L_z,L_{z'}` would be
joined to `z'` in `Q-z` through `L_{z'}\cup\{z'\}`, contrary to the choice
of `L_z`.

Every neighbour of `L_z` outside it lies in `\{z,x,y\}`.  Minimum degree
six therefore gives

\[
                  6\le (|L_z|-1)+3,
 \qquad\text{so}\qquad |L_z|\ge4.                      \tag{21}
\]

Thus `Q` contains the three vertices of `T` and at least twelve vertices
in the three sets `L_z`.  This is impossible when `|V(F)|\le16`.  If
`|V(F)|=17`, equality must hold throughout: the sets `L_z` have order four
and, for each `v\in L_z`, all six possible neighbours in
`(L_z-\{v\})\cup\{z,x,y\}` are present.  In particular each of `x,y` has
at least twelve neighbours, contrary to `\Delta(F)\le8`.

If `|V(F)|=18`, the three lobe orders sum to at most thirteen, so at least
two lobes have order four.  Every vertex in either order-four lobe is
adjacent to both `x` and `y`, already giving each of `x,y` eight neighbours.
The external neighbourhood of the third lobe is all three of its possible
vertices `\{z,x,y\}`, by three-connectivity.  It supplies an additional
neighbour of each of `x,y`, again contradicting `\Delta(F)\le8`.  This
proves (19).

For the second assertion, put `Q=F-\{x,y,z\}` and suppose every `w\in T`
is a cutvertex of `Q`.  As above, choose pairwise disjoint components
`L_w` of `Q-w`, each avoiding the other two vertices of `T`.  Now

\[
 N_F(L_w)\subseteq\{w,x,y,z\}.
\]

Minimum degree six gives `|L_w|\ge3`, and

\[
                 \sum_{w\in T}|L_w|\le |V(Q)|-3\le12. \tag{22}
\]

If two of the sets `L_w` have order three, each induces a triangle and is
complete to `\{x,y,z\}`.  Those two sets already supply all six neighbours
of each of `x,y,z`.  The third set nevertheless has at least three external
neighbours by three-connectivity of `F`; besides its cutvertex `w`, at
least two lie in `\{x,y,z\}`, a contradiction.

The remaining sorted lobe orders allowed by (22) are `3,4,4`, `3,4,5`,
and `4,4,4`.  A three-vertex lobe contributes nine edges to
`\{x,y,z\}`.  A four-vertex lobe has at least twelve edges to its four
possible external neighbours, at most four of which end at its
corresponding member of `T`; it therefore contributes at least eight edges
to `\{x,y,z\}`.  Similarly, a five-vertex lobe contributes at least five
such edges.  The three possible patterns consequently contribute at least

\[
                         25,\qquad22,\qquad24
\]

edges incident with three vertices whose degree sum is eighteen, again a
contradiction.  This proves (20).

For the third assertion, put `Q=F-\{x,y\}`.  Three-connectivity makes `Q`
connected, and

\[
 |E(Q)|=58-d_F(x)-d_F(y)+{\bf1}_{xy\in E(F)}
       =46+{\bf1}_{xy\in E(F)}\ge46.                  \tag{22a}
\]

Suppose `Q` has `c\ge4` cutvertices, and consider its block--cut tree.  If
`B` is a leaf block with cutvertex `q`, then `L=V(B)-\{q\}` is a component
of `Q-q` and

\[
                         N_F(L)\subseteq L\cup\{q,x,y\}.
\]

Minimum degree six gives `|L|\ge4`.  If the block--cut tree has at least
three leaf blocks, then

\[
                    16=|V(Q)|\ge c+3\cdot4\ge16.
\]

Equality holds throughout: there are exactly four cutvertices, three leaf
interiors of order four, and no other noncutvertex.  The leaf blocks
contribute at most `3\binom{5}{2}` edges, while every other block edge has both
ends among the four cutvertices and contributes in total at most
`\binom{4}{2}`.  Hence `|E(Q)|\le36`, contrary to (22a).

The block--cut tree therefore has exactly two leaves and is a path.  Its
`c+1` blocks may be listed as `B_0,\ldots,B_c`.  Let `a_i` count the
vertices of `B_i` that are not cutvertices of `Q`.  Then

\[
 \sum_{i=0}^c a_i=16-c,
 \qquad a_0,a_c\ge4,                                  \tag{22b}
\]

and the block orders are `a_0+1`, `a_c+1` at the ends and `a_i+2`
internally.  In particular `4\le c\le8`.  A block of order `b` has at most

\[
                   f(b)=\min\left\{\binom b2,
                                      \left\lfloor\frac{7b}{2}\right\rfloor
                               \right\}                \tag{22c}
\]

edges, because `\Delta(Q)\le7`.  Start with end-block orders five and all
internal block orders two.  Equation (22b) leaves `8-c` vertices to
distribute.  The successive gains in `f` at an end block are
`5,6,7,3`, while the first relevant gains at an internal block are
`2,3,4,5`.  The resulting exact upper bounds are

\[
\begin{array}{c|ccccc}
c&4&5&6&7&8\\ \hline
\max\sum_i f(|B_i|)&46&42&36&31&27.
\end{array}                                            \tag{22d}
\]

For `c=4`, equality in (22d) is possible only, up to reversal, for block
orders `8,2,2,2,6`.  Its order-eight end block must be a `K_8`; its unique
cutvertex has seven neighbours there and a further neighbour in the next
order-two block, contrary to `\Delta(Q)\le7`.  Thus `|E(Q)|\le45` in every
case, contradicting (22a).  This proves the third assertion.  \(\square\)

## Corollary 6 (order and overlap restrictions)

Every graph satisfying (H) and (1) has

\[
                              |V(G)|\ge29.              \tag{23}
\]

More precisely:

1. if `k=3`, then there is no off-matching common neighbour and
   `r\ge19`, so `|V(G)|\ge29`;
2. if `k=2`, all off-matching common neighbours have the same owner in
   `A`, and `r\ge19`, so `|V(G)|\ge29`;
3. if `k=1`, then `r\ge19`;
4. if `k=0`, then `r\ge19`.

### Proof

If `k=3`, one off-matching common neighbour would satisfy Lemma 4 with a
one-vertex set `Z`; Corollary 3 makes `R-Z` connected.  Hence the only
intersection between the two unions in (5) consists of the two vertices in
(4) for each of the three matched pairs.  Inclusion-exclusion gives

\[
 r\ge2(15-3)-2\cdot3=18.                               \tag{24}
\]

Suppose equality holds in (24), and put
`U_A=\bigcup_{a\in A}P_a`, `U_B=\bigcup_{b\in B}Q_b`.  Their only common
vertices are the six matched-port vertices, so `U_A\cup U_B=V(R)`.  The
two nonempty sets `U_A-U_B` and `U_B` partition `V(R)`.  Connectivity of
`R` gives an edge `uv` with `u\in U_A-U_B` and `v\in U_B`.

Let `a` be the unmatched owner of `u`, and put

\[
                       X=R-\{u,v\},\qquad
                       Y=B\cup\{u,v\}.
\]

Three-connectivity makes `X` connected, while the edge `uv` and the
`B`-neighbour of `v` make `Y` connected.  The vertex `v` does not belong
to `P_a`, since that would make it an off-matching common neighbour.
Consequently `X` remains adjacent to every member of `A`.  The set `Y` is
adjacent to the three matched members of `A` and to `a`, and `X` is
adjacent to `Y` through an edge from `B` to one of the eleven vertices of
`U_B-\{v\}`.  The five singleton `A`-bags together with `X,Y` give a
`K_7^-` model, a contradiction.  Hence `r\ge19` when `k=3`.

If `k=2`, off-matching common neighbours cannot have two distinct owners
in `A`: choosing one for each owner gives a two-vertex set whose deletion
leaves `R` connected, again contradicting Lemma 4.  They therefore occupy
at most one three-vertex set `P_a`.  The two matched pairs contribute four
further common vertices, so

\[
 r\ge2(15-2)-(3+4)=19.                                 \tag{25}
\]

It remains to treat `k\le1`.  Let `O` be the set of off-matching common
neighbours.  Inclusion-exclusion and (4)--(5) give

\[
                         |O|\ge30-4k-r.                 \tag{26}
\]

Suppose first that `k=1` and `r\le17`.  The set `O` occupies the four
three-vertex sets `P_a` belonging to the unmatched vertices of `A`, and
`|O|\ge26-r\ge9`.  Hence `O` meets at least three of those triangles and
contains every vertex of at least one of them.  Let `T` be such a full
triangle, and choose `x,y\in O` with two other distinct owners in `A`.
Lemma 5 supplies `z\in T` such that `R-\{x,y,z\}` is connected.  The three
vertices are off-matching common neighbours with distinct owners, so
Lemma 4 gives a `K_7^-` minor, a contradiction.  Therefore `r\ge18`.

If `k=1` and `r=18`, then (26) gives `|O|\ge8`.  If `|O|\ge9`, the same
four triangles include one contained in `O` and two further triangles
meeting `O`.  Lemma 5(1), now at order eighteen, gives the same forbidden
three-owner selection.  Hence `|O|=8`.  If its distribution over the four
triangles were not `2,2,2,2`, one triangle would be contained in `O`, and
the other five members would occupy at least two further triangles; the
same selection would again be forbidden.  Thus each unmatched private
triangle contains exactly two members of `O`.  Together with the two
matched-port vertices, these are the ten vertices having both clique
incidences; the other eight vertices have one.  Equation (6) gives degree
sequence `6^{10}7^8` for `R`.

Choose `x,y\in O` from two of the four unmatched private triangles.  For
each of the four members `z\in O` in the other two triangles, the set
`\{x,y,z\}` has three distinct owners in `A`.  Lemma 4 and exclusion of a
`K_7^-` minor say that `R-\{x,y,z\}` is disconnected.  Thus all four such
vertices `z` are cutvertices of the connected graph `R-\{x,y\}`,
contrary to Lemma 5(3).  Therefore `r\ge19` also when `k=1`.

Finally suppose `k=0` and `r\le18`.  Here `O` lies in five disjoint
triangles and (26) gives `|O|\ge30-r\ge12`.  Thus at least four triangles
meet `O`, and at least two of them are contained in `O`.  Reserve one full
triangle `T_4`.  From a second full triangle `T_3` and two further triangles
meeting `O`, choose `x,y\in O` with distinct owners outside `T_3,T_4`.
Lemma 5(1) gives `z\in T_3` for which `R-\{x,y,z\}` is connected.  All
three selected vertices lie in `O`, so (6) gives them degree six in `R`.
Lemma 5(2),
applied to `T_4`, now supplies `w\in T_4` such that
`R-\{x,y,z,w\}` is connected.  Lemma 4 again gives a forbidden minor.
Consequently `r\ge19` when `k=0`.

Together with (24), (25), and (13), these bounds prove (23).
\(\square\)

## Corollary 7 (a cycle through all five private triangles)

There is a cycle in `G-A` containing all fifteen vertices of

\[
                         \bigcup_{a\in A}T_a.           \tag{27}
\]

The symmetric assertion holds after deleting `B`.

### Proof

The set in (27) is the union of five pairwise disjoint triangles, so its
independence number in `G-A` is at most five.  Theorem 2 says that `G-A` is
five-connected.  Fournier's cyclability theorem states that if `F` is a
`q`-connected graph and `W\subseteq V(F)` satisfies
`\alpha(F[W])\le q`, then one cycle of `F` contains every member of `W`.
Apply it with `F=G-A`, `q=5`, and the set in (27).  \(\square\)

## Proposition 8 (bond and colouring normal forms)

Put `H=G-A` and retain the five triangles `T_a`, `a\in A`.

1. The two-transversal target is equivalent to a bond of `H` meeting the
   edge set of every `T_a`.
2. In every proper six-colouring `phi` of `H`, at least one of the following
   holds:

   - four of the triangles use the same three colours; or
   - at least two colours occur on every one of the five triangles.

### Proof

Suppose first that `X,Y` are disjoint connected subgraphs of `H`, each
meeting all five triangles.  Contract `X,Y` to distinct vertices, take a
spanning tree of the resulting connected graph, and delete one edge on the
tree path between the two contraction vertices.  The two tree components
lift to a partition

\[
                         V(H)=D_1\mathbin{\dot\cup}D_2 \tag{28}
\]

such that both `H[D_1],H[D_2]` are connected and each contains one of
`X,Y`.  Conversely, the two sides of any such partition are the required
connected transversals.  A cut `\delta_H(D_1)` is a bond exactly when both
sides are connected.  Since `T_a` is a triangle, the bond meets `E(T_a)`
exactly when `T_a` has vertices on both sides.  This proves the first
assertion.

For the second, let the colour set be `[6]`.  Write

\[
 S_a=\phi(T_a),
 \qquad L_a=[6]-S_a.                                   \tag{29}
\]

Every `S_a` and every `L_a` has order three.  The colouring `phi` extends
over the clique `A` precisely when the five lists `L_a` have a system of
distinct representatives.  Such an extension would six-colour `G`, so
Hall's theorem supplies a subfamily `I` with

\[
                     \left|\bigcup_{a\in I}L_a\right|<|I|. \tag{30}
\]

Because all lists have order three, `|I|\ge4`.  If `|I|=4`, their union
has order three and the four lists are identical; their complementary
triangles therefore use the same three colours.  If `|I|=5`, the union of
all five lists has order at most four, and

\[
 \left|\bigcap_{a\in A}S_a\right|
 =6-\left|\bigcup_{a\in A}L_a\right|\ge2.              \tag{31}
\]

This is the second alternative.  \(\square\)

## Proposition 9 (edge-critical Kempe fork)

Fix `a_i\in A` and `x\in T_{a_i}`.  Choose a proper six-colouring `phi`
of the edge-deleted graph `G-a_ix`, which is a proper minor, and put
`H=G-A`.  Necessarily

\[
                         \phi(a_i)=\phi(x)=p.           \tag{32}
\]

The clique `A` uses five distinct colours.  Let `q` be the unique colour
absent from `\phi(A)`, put `S_a=\phi(T_a)`, and write

\[
                         S_{a_i}=\{p,q,r\}.             \tag{33}
\]

Let `a_h` be the unique vertex of `A-\{a_i\}` coloured `r`, put

\[
                         J=A-\{a_i,a_h\},
 \qquad c_j=\phi(a_j)\quad(a_j\in J).                  \tag{34}
\]

Then the following statements hold.

1. For every `a_j\in J`, both `p` and `q` occur on `T_{a_j}`.
2. For every `a_j\in J`, the component of the two-colour graph
   `H[p,c_j]` containing `x` also meets `T_{a_j}`.
3. Either `p,q` occur on all five private triangles, or

   \[
                         S_{a_j}=S_{a_i}=\{p,q,r\}
                         \quad\text{for every `a_j\in J`.} \tag{35}
   \]

4. If the second alternative in part 3 holds, then, for every `a_j\in J`,
   the component of `H[p,c_j]` containing `x` meets all four triangles

   \[
                         T_{a_i},\qquad T_{a_ell}\ (a_ell\in J). \tag{36}
   \]

### Proof

If the two colours in (32) were different, `phi` would already colour
`G`.  The four vertices of `A-\{a_i\}` receive four distinct colours
different from `p`, leaving the unique sixth colour `q`.

The colour `q` must occur on `T_{a_i}`.  Otherwise `a_i` has no
`q`-coloured neighbour in `G-a_ix`: its exact neighbourhood is
`(A-\{a_i\})\cup T_{a_i}`, and the edge to the only `p`-coloured vertex
of `T_{a_i}` is deleted.  Recolouring `a_i` with `q` would then make the
deleted edge proper and give a six-colouring of `G`.  This proves (33).

For each `a\in A`, let

\[
                         L_a=[6]-S_a                  \tag{37}
\]

be the colours available at `a` over the fixed colouring of `H`.  The four
colours on `A-\{a_i\}` are the four colours outside `\{p,q\}`.  Hence
`a_h` in (34) exists uniquely and

\[
                         L_{a_i}=\{c_j:a_j\in J\}.      \tag{38}
\]

Fix `a_j\in J`.  If `p\in L_{a_j}`, assign colour `c_j` to `a_i`, colour
`p` to `a_j`, and retain the original colour on the other three vertices
of `A`.  These are five distinct permissible colours.  If instead
`q\in L_{a_j}`, use `q` at `a_j` in the same assignment.  Either assignment
would extend the colouring of `H` over `A` and colour `G`.  Thus
`p,q\in S_{a_j}`, proving part 1.

Let `K_j` be the component of `H[p,c_j]` containing `x`.  Suppose it misses
`T_{a_j}` and interchange `p,c_j` on `K_j`.  The triangle `T_{a_i}`
contains `p` only at `x` and contains no `c_j`, by (33)--(38).  After the
interchange, colour `a_i` with `p` and retain the original colour on every
vertex of `A-\{a_i\}`.  The list at `a_i` now contains `p`; the list at
`a_j` is unchanged; and every other retained original colour is different
from `p,c_j`, so the interchange cannot remove it from its list.  This
again colours `G`, a contradiction.  Hence `K_j` meets `T_{a_j}`, proving
part 2.

By part 1, write

\[
                         S_{a_j}=\{p,q,s_j\}
                         \quad(a_j\in J).              \tag{39}
\]

Suppose `p,q` do not both occur on `T_{a_h}`.  Choose
`t\in\{p,q\}\cap L_{a_h}`.  If some `s_j\ne r`, then `r\in L_{a_j}`.
Assign `t` to `a_h`, `r` to `a_j`, `c_j` to `a_i`, and retain the two
original colours on `J-\{a_j\}`.  These are five distinct permissible
colours, again a contradiction.  Therefore every `s_j=r`, which is (35)
and proves part 3.

Finally assume (35), fix `a_j\in J`, and retain `K_j`.  It contains `x`
and, by part 2, the unique `p`-coloured vertex of `T_{a_j}`, because none
of the four triangles in (36) contains colour `c_j`.  If it missed the
`p`-coloured vertex of some `T_{a_ell}` with
`a_ell\in J-\{a_j\}`, interchange `p,c_j` on the component containing
that vertex.  This component is disjoint from `K_j`, so `x` keeps colour
`p`.  It also misses `T_{a_j}`, whose unique `p`-coloured vertex lies in
`K_j` and which contains no `c_j`.  Now assign `p` to `a_ell`, `c_ell` to
`a_i`, and retain the original colours on the other three vertices of `A`.
Thus `c_j` remains available at `a_j`; as before, colours outside
`\{p,c_j\}` remain available.  This assignment colours `G`, and the
contradiction proves (36).  \(\square\)

## Remaining obstruction and trust boundary

Theorem 2 upgrades the former three-connectivity reduction to
five-connectivity, while Corollary 3 isolates a three-connected central
subgraph with exact degree and overlap data.  The equality layer is not
closed.  Its first possible order is now twenty-nine.  In any surviving
`k=1` case, every three off-matching common neighbours with distinct owners
in `A` must separate `R`; for `k=0`, the analogous statement holds for
every four such vertices.  When `k=3` there is no off-matching common
neighbour, and when `k=2` all such vertices have one common owner in `A`.

Corollary 7 does not by itself give two connected transversals.  For
example, arrange five disjoint triangles in a ring, with exactly one edge
between each consecutive pair, and use two edges inside each triangle to
form a cycle through all fifteen vertices.  Any connected subgraph meeting
all five triangles uses at least four of the five inter-triangle edges, so
two vertex-disjoint such subgraphs cannot exist.  This example is only
two-connected.  The remaining task is therefore a bridge or rerouting
argument that uses five-connectivity, the exact overlap restrictions, and
the critical colouring dichotomy in Proposition 8.

Proposition 9 strengthens that dichotomy but still does not supply two
disjoint connected transversals.  In its rigid branch, the three forced
Kempe components share the same four `p`-coloured triangle vertices.  The
remaining positive step is a first-common-vertex splitting or bridge
rerouting argument that turns this shared four-triangle spine into two
disjoint connected subgraphs; edge deletion and contraction of the same
edge do not by themselves give independent spines.

The external input in Corollary 7 is Fournier's cyclability theorem, in the
form already checked in the separate internal audit of
[the reserved-cycle theorem](hc7_reserved_cycle_or_two_cut_audit.md).  All
other deductions above are elementary consequences of the previously
audited equality structure and the explicit hypotheses (H).  No finite
enumeration is used.
