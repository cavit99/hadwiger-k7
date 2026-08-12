# The five-edge star also gives a six-coordinate common host

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_six_coordinate_forest_reduction_audit.md).
This note does not prove the `K_7^-` six-colour conjecture or `HC_7`.

This note starts from the replacement-abundance construction in
[`replacement-abundance theorem`](hc7_k7minus_removable_matching_rotation_abundance.md).
Its point is that the five-edge star in the six-coordinate fork is not a
separate terminal obstruction.  The absence of a literal `K_5` turns two of
its edges into an induced three-vertex path, and that path has the same exact
contraction-signature property as two disjoint matching edges.

## 1. Setting

Let `G` be a minor-minimal non-six-colourable graph satisfying the critical
host conclusions

\[
 \kappa(G)\geq7,\qquad \delta(G)\geq8,
 \qquad |E(G)|\geq4|V(G)|,
 \qquad K_7^-\npreccurlyeq G,
 \qquad K_5\nsubseteq G,
 \qquad |V(G)|\geq25.                               \tag{1.1}
\]

Let `M_0` be a matching of order four.  Suppose that `A^*` is a set of five
distinct edges, each disjoint from `V(M_0)`, such that

\[
              G-(M_0\cup\{a\})\quad\hbox{is seven-connected}
              \qquad(a\in A^*).                       \tag{1.2}
\]

These are exactly the objects supplied by Theorem 4.1 and Corollary 4.3 of
the replacement-abundance draft.

For a forest `F` and a colouring `c` of `G-F`, put

\[
 \Sigma_F(c)=\{uv\in F:c(u)=c(v)\}.                  \tag{1.3}
\]

## 2. The star is absorbed by an induced path

### Theorem 2.1 (six-coordinate induced-forest host)

There are distinct edges `a,b\in A^*` such that, with

\[
                  F=M_0\cup\{a,b\},\qquad X=G-F,     \tag{2.1}
\]

all of the following hold.

1. `F` is a forest of size six, and every component of `F` is induced on
   its own vertex set in `G`.  More precisely, either `F` is a matching or
   its only nonsingle-edge component is an induced path on three vertices.
2. Both `X+a` and `X+b` are seven-connected.  Consequently `X` is at least
   six-connected and

   \[
                         |E(X)|\geq4|V(X)|-6.          \tag{2.2}
   \]

3. The exact signature language on the one graph `X` is

   \[
       \{\Sigma_F(c):c\text{ is a proper six-colouring of }X\}
                         =2^F-\{\varnothing\}.         \tag{2.3}
   \]

4. `X` has a spanning `K_7^vee`-minor model.  In a target-free `G`, its
   two nominally missing pairs are anticomplete even after all edges of
   `F` are restored, so this is an exact spanning model in `G`.

#### Proof

If `A^*` contains two disjoint edges, choose them as `a,b`.  Then `F` is a
matching, and item 1 is immediate.

Otherwise the elementary pairwise-intersection argument in the
replacement-abundance draft makes `A^*` a five-edge star.  Write it as

\[
                         A^*=\{rx_1,\ldots,rx_5\}.     \tag{2.4}
\]

The five leaves cannot induce a clique, since that would be a literal
`K_5` in `G`.  Choose nonadjacent leaves `x_i,x_j` and put
`a=rx_i`, `b=rx_j`.  The component `x_i r x_j` is then an induced path.
It is disjoint from the four matching edges in `M_0`, and all other
components are single edges.  This proves item 1 also in the star case.

Equation (1.2) gives

\[
             X+a=G-(M_0\cup\{b\}),\qquad
             X+b=G-(M_0\cup\{a\}),                   \tag{2.5}
\]

so both graphs are seven-connected.  Deleting one edge reduces vertex
connectivity by at most one, which proves the connectivity assertion for
`X`; the density bound follows by deleting the six distinct edges of `F`.

Fix a nonempty `J\subseteq F`.  Contract every edge in `J` and six-colour
the resulting proper minor.  Expanding the contracted forest components
gives equal colours on the ends of every edge in `J`.  An edge of `F-J`
does not collapse under these contractions, since `F` has no cycle.  No
edge of `G-F` collapses either: both ends of such an edge could be joined
by a path in `J` only if they belonged to one component of `F`, contrary
to that component being induced.  The expansion is therefore a proper
six-colouring of `X` with signature exactly `J`.  An empty signature would
remain proper after `F` was restored and would six-colour `G`.  This proves
(2.3).

Finally, `X` is four-connected and satisfies the Norin--Totschnig density
threshold.  Their exceptional graph `K_{2,2,2,2}` is excluded by the order
hypothesis.  Their theorem supplies a `K_7^vee` minor, and unused vertices
may be absorbed to make it spanning.  If either nominally missing pair were
adjacent in `G`, the same seven branch sets would give a `K_7^-` minor.
Target exclusion therefore makes the model exact in `G`. `\square`

Thus the disjoint-pair and five-edge-star outcomes of the earlier fork have
one common conclusion.  The only difference is whether the last two
coordinates form `2K_2` or an induced `P_3`.

### Corollary 2.1A (critical-host form)

Every minor-minimal non-six-colourable graph satisfying (1.1) has a forest
`F` and deletion host `X` satisfying all four conclusions of Theorem 2.1.

#### Proof

The removable-matching theorem and the audited replacement-abundance
theorem supply `M_0` and `A^*` satisfying (1.2).  Apply Theorem 2.1.
`\square`

### Theorem 2.2 (one cycle through all six forest edges)

The forest `F` in Theorem 2.1 is contained in one cycle of `G`.
Consequently deleting the six edges of `F` from that cycle gives six
pairwise vertex-disjoint connected subgraphs of `X`.  In the matching case
they are six paths pairing the twelve ends cyclically.  In the induced-path
case one is the singleton common end `r`, and the other five are paths.

#### Proof

We use the theorem of Haggkvist and Thomassen that any `k` independent
edges in a `(k+1)`-connected graph lie on one cycle.

If `F` is a matching, apply that theorem directly with `k=6` in the
seven-connected graph `G`.

Otherwise write the nonsingle-edge component as `x-r-y`, where `xy` is
not an edge.  The graph `G-r` is six-connected, and adding the edge `xy`
preserves six-connectivity.  In `(G-r)+xy`, the artificial edge `xy` and
the four edges of `M_0` form five independent edges.  A cycle containing
all five exists by the same theorem with `k=5`.  Replace its artificial
edge `xy` by the path `x-r-y`.  The result is a cycle of `G` containing
every edge of `F`.

Removing the displayed forest edges from the cycle gives the asserted
components.  In the induced-path case both cycle edges incident with `r`
belong to `F`, so `r` is an isolated component; all other components are
paths. `\square`

The quantifiers here are simultaneous: one literal cycle contains all six
coordinates.  This avoids a choice of six separately existential linkage
systems.  It still gives no prescribed intersection between those paths
and the branch sets of the exact near-clique model.

### Theorem 2.3 (one prescribed vertex can be inserted)

For every vertex `v` of `G`, there is a cycle `C_v` which contains `v` and
all six edges of `F`.  Hence every one prescribed vertex can be put on the
same six-coordinate cyclic linkage.

#### Proof

Start with the cycle `C` from Theorem 2.2.  There is nothing to prove when
`v\in V(C)`.  Otherwise the Fan Lemma in the seven-connected graph `G`
gives seven paths from `v` to seven distinct vertices of `C`, pairwise
disjoint outside `v`; stop each at its first vertex of `C`.

The seven ends divide `C` into seven cyclic intervals.  Only six of those
intervals can contain one of the six distinguished edges of `F`.  Choose
an interval containing none, and replace it by the two fan paths from its
ends to `v`.  The complementary arc contains every edge of `F`, so the
result is the required cycle. `\square`

Applied to (4.1), this says that any one nominated vertex of any one branch
set can be made visible on a coordinate-compatible cycle.  It does not put
two nominated portals, or one nominated vertex in each of two branch sets,
on the same cycle: the cycle `C_v` may depend on `v`.  Exchanging

\[
           (\forall v)(\exists C_v)
           \quad\hbox{for}\quad
           (\exists C)(\text{several prescribed model labels lie on }C)
                                                               \tag{2.6}
\]

would be an additional linkage theorem, not a consequence of the fan
insertion.

## 3. Exact six-cuts and the singleton obstruction

The two selected edges retain more connectivity information than an
arbitrary six-edge forest.

### Theorem 3.1 (two restorers cross every six-cut)

Let `S` be a vertex cut of `X` of order six.  Then:

1. `X-S` has exactly two components, say `C,D`;
2. both `a` and `b` have one end in each of `C,D`;
3. both components are adjacent in `X` to every vertex of `S`, and
   `G[S]` has no `K_5^-` minor; in particular `|E(G[S])|\leq11`;
4. if `a,b` are disjoint, neither `C` nor `D` is a singleton;
5. if `a=rx` and `b=ry` form the induced path `xry`, the only possible
   singleton component is `\{r\}`.  In that case

   \[
             N_X(r)=S,\qquad d_G(r)=8,qquad
             N_G(r)=S\mathbin{\dot\cup}\{x,y\},       \tag{3.1}
   \]

   and `xy\notin E(G)`.
6. In the singleton case there is a proper six-colouring of `G-r` in
   which `x,y` form one colour class on `N_G(r)`, the six vertices of `S`
   use all five other colours, and hence the colour multiplicities on
   `N_G(r)` are

   \[
                              2,2,1,1,1,1.             \tag{3.2}
   \]
7. Write the original five-edge star as
   `A^*=\{rx_1,\ldots,rx_5\}`.  In the singleton case, every star leaf
   satisfies

   \[
          K_5^-\npreccurlyeq G[N_G(r)-\{x_i\}]
                          \qquad(1\leq i\leq5).        \tag{3.3}
   \]

#### Proof

The graph `X+a-S` is connected by Theorem 2.1.  A single added edge can
join all components of `X-S` only when there are exactly two, its ends lie
outside `S`, and they belong to different components.  This proves items
1--2 for `a`; applying the same argument to `X+b` proves it for `b`.

If a component missed a vertex of `S`, its open neighbourhood in `X`
would have order at most five, contrary to six-connectivity.  Thus both
components are full at `S`.  They are adjacent in `G` through either of
the crossing edges `a,b`.  A `K_5^-` model in `G[S]`, together with `C`
and `D`, would therefore give seven branch sets with at most one missing
adjacency.  Target exclusion proves item 3.

For the numerical consequence, take a spanning twelve-edge subgraph of any
six-vertex graph with at least twelve edges.  If it has a vertex of degree
at most three, deleting that vertex leaves at least nine edges on five
vertices.  Otherwise it is four-regular, hence `K_6-3K_2`; contracting an
edge whose ends belong to different missing pairs gives `K_5^-`.  Extra
edges only help.

If one component were a singleton, its sole vertex would be an end of both
`a` and `b`.  This is impossible when those edges are disjoint.  When they
form `xry`, their only common end is `r`, so the singleton must be `\{r\}`.
Then `N_X(r)\subseteq S`.  Six-connectivity of `X` gives
`d_X(r)\geq6`, and `|S|=6`, hence `N_X(r)=S`.  The matching `M_0` is
disjoint from `r`, and the only edges of `F` incident with `r` are `rx,ry`.
Thus restoring `F` adds precisely those two neighbours and proves (3.1).
The last assertion is the induced-path choice in Theorem 2.1.

For item 6, take the signature-`\{a,b\}` colouring from (2.3).  Restoring
`M_0` leaves it proper, and deleting `r` removes its only two remaining
monochromatic edges.  It is therefore a proper six-colouring of `G-r`.
The vertices `x,y` have the colour of `r`, while every member of `S` avoids
that colour because `N_X(r)=S`.  Every one of the six colours must occur on
`N_G(r)`, since otherwise the missing colour could be assigned to `r`.
Thus the six vertices of `S` use all five remaining colours, proving
(3.2).

For item 7, fix a star leaf `x_i` and put

\[
                  H_i=G-(M_0\cup\{rx_i\}),\qquad
                  T_i=N_G(r)-\{x_i\}.                 \tag{3.4}
\]

The graph `H_i` is seven-connected by (1.2), while the singleton identity
gives `d_G(r)=8`; hence `N_{H_i}(r)=T_i` and `|T_i|=7`.  Let `Q_i` be the
component of `H_i-T_i` containing `x_i`.  Every vertex of `T_i` has a
neighbour in `Q_i`: otherwise at most six vertices would separate `Q_i`
from the singleton component `\{r\}` in `H_i`.  In `G`, the two connected
sets `\{r\}` and `Q_i` are adjacent through `rx_i`, and both are adjacent
to every vertex of `T_i`.  A `K_5^-` model in `G[T_i]` would therefore
combine with them to give a `K_7^-` model in `G`.  This proves (3.3) by
target exclusion. `\square`

For a nonsingleton component, deleting the endpoint of `a` on that side
together with `S` gives an actual order-seven separation of the
seven-connected one-edge completion `X+a`; the analogous statement holds
for `b`.  The theorem deliberately does **not** call this an order-seven
separation of `G`: any of the four edges of `M_0`, and in the matching case
the other selected edge, may also cross the two open shores.

The singleton in item 5 is therefore the exact exceptional geometry.  It
is not an arbitrary low-degree artefact: it returns a degree-eight critical
vertex whose neighbourhood is the six-cut together with the two
nonadjacent path leaves.  Eliminating that row requires the existing
degree-eight neighbourhood structure or an order-eight singleton theorem;
ordinary cut lifting does not eliminate it.

### Corollary 3.2 (the exact two-row matching lift)

Suppose that `F` is a matching and exactly two edges of `F` cross between
`C` and `D`.  For every choice `Z` of one end of each crossing edge, both
`C-Z` and `D-Z` are nonempty.  Consequently `S\cup Z` is the boundary of
an actual order-eight separation of `G`.

#### Proof

The selected vertices meet every edge of `G` between `C` and `D`, so
`S\cup Z` separates the two residual shores.  Suppose, by symmetry, that
`C-Z` is empty.  Theorem 3.1(4) excludes `|C|=1`.  Hence `C` consists of
the two selected vertices `c_1,c_2`, one on each crossing matching edge.
The only possible neighbours of `c_i` are the
six vertices of `S`, the other vertex of `C`, and its matching mate in
`D`.  Minimum degree eight forces every one of those eight adjacencies.

Use the signature colouring whose equality set is the two crossing edges.
The vertices `c_1,c_2` have distinct colours because they are adjacent;
their respective mates have those same two colours, while no vertex of
`S` has either colour.  Interchange the two colours on `c_1,c_2`.  All
edges inside `C` or from `C` to `S` remain proper, and both crossing
matching edges become proper.  There is no other edge from `C` to `D`,
and every other forest edge was already bichromatic.  This gives a proper
six-colouring of `G`, a contradiction.  The same argument applies to
`D`, proving the claim. `\square`

### Corollary 3.3 (the clean induced-path lift)

Suppose that `a=rx,b=ry` and no edge of `M_0` crosses between `C,D`.
Orient the components so that `r\in C`.  Then either `C=\{r\}` and the
singleton conclusions (3.1)--(3.2) hold, or `S\cup\{r\}` is the boundary
of an actual order-seven separation of `G`.

#### Proof

The only edges of `G` between `C,D` are then `rx,ry`, and deleting `r`
meets both.  The shore `D` remains nonempty.  If `C-\{r\}` is nonempty as
well, the two residual shores give the asserted separation.  The remaining
case is exactly the singleton in Theorem 3.1. `\square`

## 4. What the exact near-clique model does and does not force

Fix a spanning exact model

\[
                         P,B,C,U_1,U_2,U_3,U_4        \tag{4.1}
\]

in `X`, with only `PB,PC` absent.  Every edge of `F` avoids those two bag
pairs, since an edge across either pair would complete (4.1) to a
`K_7^-` model in `G`.

### Theorem 4.1 (the seven-connected row sees one model portal)

Suppose that `X` is seven-connected.  Then, in the target-free case, there
are a universal bag `U_i`, a connected nonempty proper set `Y\subset U_i`
with connected complement in `U_i`, and a vertex

\[
                         v\in Y\cap N_X(P)             \tag{4.2}
\]

such that `N_G(Y)` is an actual separator.  Moreover one cycle of `G`
contains all six edges of `F` and the literal portal vertex `v`.

#### Proof

The connected bag `B` lies outside `P\cup N_X(P)`, so `N_X(P)` is an
actual separator in `X`.  Seven-connectivity gives `|N_X(P)|\geq7`.
Those neighbours lie in the four universal bags, hence some `U_i`
contains distinct vertices `p,q\in N_X(P)`.

Run the retaining-core/opposite-gate proof of the exact `K_7^vee`
separator dichotomy with this prescribed pair.  In the retaining-core
case, the returned component contains the avoided vertex `p` or `q`.  In
the opposite-gate case, the two gates contain `p` and `q`, respectively.
The alternative to a gate separator in that proof is an explicit
`K_7^-` model.  Target exclusion therefore returns the asserted `Y` and
one selected portal `v\in\{p,q\}`.  The final cycle is Theorem 2.3 applied
to `v`. `\square`

This is a genuine exchange upgrade: the six coordinate edges and one
literal model portal coexist on one cycle.  It stops one edge short of the
model-labelled composition.  If `x\in P` and `xv\in E(X)` is the selected
portal edge, Theorem 4.1 does not say that the cycle uses `xv`; its two
cycle edges at `v` may both lie inside `Y`.  Forcing `xv` would ask for a
cycle through the six forest coordinates and a seventh prescribed edge.
That conclusion is not supplied by seven-connectivity or by the
Haggkvist--Thomassen theorem used above.

This is the placement information obtained immediately from exactness.  In
particular,
the punctured cube (2.3) is automatic for every componentwise-induced
forest in a minor-critical graph.  It does not force an endpoint of `F`
to be a `P`-portal, does not put two endpoints in one universal bag, and
does not co-bag a forest edge in a common `K_6` model.  Inferring any of
those incidences from (2.3) would be the first unsupported step.

The next terminal theorem must therefore use one of the two pieces of
nonautomatic information:

1. both distinguished edges separately restore seven-connectivity, giving
   Theorem 3.1 at every exact six-cut; or
2. the internal retaining-core/opposite-gate geometry of the exact model
   (4.1).

A theorem based only on the 63 signatures and the seven bag labels cannot
distinguish this host from an arbitrary componentwise-induced forest
deletion and cannot close the branch.

## Dependencies and scope

The `K_5`-free critical-host conclusion is Corollary 3 of
[`hc7_k7minus_degree7_rooted_helper_closure.md`](../results/hc7_k7minus_degree7_rooted_helper_closure.md).
The replacement edges and their seven-connected deletions are supplied by
the replacement-abundance theorem cited above.  The density input is
Theorem 6 of Norin and Totschnig, *Every graph with no `K_7^vee` minor is
6-colorable*.  The cycle input is Roland Haggkvist and Carsten Thomassen,
*Circuits through specified edges*, Discrete Mathematics **41** (1982),
29--34: `k` independent edges in a `(k+1)`-connected graph lie on one
cycle.

This reduction is unbounded and computation-free.  It closes the apparent
five-edge-star fork, but it does not terminalise the resulting
six-coordinate induced-forest host.
