# Four independent degree-eight centres: a rooted model or an exact-cut lattice

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_four_centre_web_cut_lattice_audit.md`](hc7_k7minus_four_centre_web_cut_lattice_audit.md).
This note gives a computation-free structural reduction in the critical
host.  It does not eliminate the final exact-cut outcome or prove the
`K_7^-` six-colour conjecture.

Throughout, `K_7^-` is `K_7` with one edge deleted.  A minor model is
**rooted at** nominated vertices when its branch sets contain those vertices
one-to-one.

## 1. The four-centre setting

Let `G` satisfy

\[
 \chi(G)=7,\qquad
 \text{every proper minor of `G` is six-colourable},\qquad
 K_7^-\npreccurlyeq G,
 \tag{1.1}
\]

and suppose

\[
 \kappa(G)\ge 7,\qquad |E(G)|\ge4|V(G)|,\qquad |V(G)|\ge25.
 \tag{1.2}
\]

Let

\[
                         U=\{u_1,u_2,u_3,u_4\}
\tag{1.3}
\]

be an independent set of degree-eight vertices, and put `H=G-U`.
The critical-host theorem supplies all these hypotheses: its at least 25
degree-eight vertices contain such a set `U` by `R(5,4)=25`, because `G`
has no `K_5` subgraph.

### Lemma 1.1 (the common deleted host)

The graph `H` is three-connected, nonplanar, and exactly six-chromatic.
Moreover, `\kappa(G)` is either seven or eight; if it is eight, then `H`
is four-connected.

#### Proof

Deleting four vertices lowers connectivity by at most four, so `H` is
three-connected, and it is four-connected when `G` is eight-connected.
For any `u in U`, the set `N_G(u)` separates `u` from the other three
members of `U`.  Hence `\kappa(G)\le8`.

Since `U` is independent and every member has degree eight,

\[
 |E(H)|=|E(G)|-32\ge4|V(H)|-16.
\]

Here `|V(H)|\ge21`, so this is strictly greater than
`3|V(H)|-6`; consequently `H` is nonplanar.  Finally, `H` is
six-colourable by (1.1).  A five-colouring of `H` would extend to a
six-colouring of `G` by giving all four vertices of `U` one new colour.
Thus `\chi(H)=6`.  \(\square\)

## 2. A fixed-colouring rooted model or an exact order-seven cut

### Theorem 2.1 (four-centre rooted-web dichotomy)

Fix `r in U` and a proper six-colouring `phi` of `G-r`.  Choose four
colours which occur exactly once on `N_G(r)`, and let

\[
                         x_1,x_2,x_3,x_4
\tag{2.1}
\]

be their unique representatives.  Exactly one of the following holds.

1. **Rooted-model outcome.**  The graph `H` contains an
   `\{x_1,x_2,x_3,x_4\}`-rooted `K_4` model.  With the singleton branch
   set `\{r\}`, this is a `K_5` model in `G-(U-\{r\})`.  Its four literal
   roots have pairwise distinct `phi`-colours, each unique on `N_G(r)`.
2. **Rooted-web exact-cut outcome.**  The graph `H` has no
   `\{x_1,x_2,x_3,x_4\}`-rooted `K_4` model and is a spanning subgraph of
   a web rooted at those four vertices.  In that web there are a facial
   three-set `T subseteq V(H)` and a nonempty connected set
   `C subseteq V(H)-T` such that

   \[
              N_H(C)=T,\qquad N_G(C)=T\mathbin{\dot\cup}U.   \tag{2.2}
   \]

   Thus `S=T dotcup U` is an actual order-seven cut.  The graph `G-S`
   has exactly two components, namely `C` and a component `D`, and both
   are adjacent to every literal vertex of `S`.  Every `x_i` avoids `C`,
   and at least one `x_i` belongs to `D`.

The three vertices of `T` form a facial triangle in a containing web, but
they are not asserted to form a triangle in `H` or in `G`.

#### Proof

Every colour occurs on `N_G(r)`, since otherwise `phi` would extend to
`r`.  Distributing eight neighbours among six nonempty colour classes
leaves at least four singleton classes.  Independence of `U` puts their
representatives (2.1) in `H`.

Apply Theorem 8 of Fabila-Monroy and Wood to the three-connected graph `H`
with these four nominated vertices.  If `H` has the rooted `K_4` model,
then `r` is adjacent to every rooted bag through its nominated vertex, so
adjoining `\{r\}` proves outcome 1.  All five bags avoid `U-\{r\}`.

Otherwise, that theorem says that `H` is a spanning subgraph of an
`\{x_1,x_2,x_3,x_4\}`-web.  Its planar skeleton has the four nominated
vertices on the outer face.  Behind each facial triangle `T` it may have
an added clique `X_T`, complete to the three skeleton vertices and with no
other neighbours outside `X_T`.  Since `H` itself is nonplanar, some
`X_T` is nonempty.  Let `C` be a component of `H[X_T]`.  Web containment
gives `N_H(C) subseteq T`.  At least one of the four outer roots lies
outside `T`, so `C` has a genuine far side.  Three-connectivity now forces

\[
                             N_H(C)=T.                 \tag{2.3}
\]

In `G`, every neighbour of `C` lies in `T union U`.  The same outer root
shows that this seven-set separates `C` from another vertex.
Seven-connectivity forces all seven possible boundary vertices to occur,
proving (2.2).

Thus `C` is a component of `G-S`.  The audited two-component theorem for
order-seven cuts in the critical host says that there is exactly one other
component `D`.  Seven-connectivity makes both components adjacent to every
vertex of `S`.  Web-cell vertices are disjoint from the skeleton, so all
four `x_i` avoid `C`; since `|T|=3`, at least one lies in `D`.  The two
outcomes are exclusive by the same rooted-web theorem.  \(\square\)

### Corollary 2.2 (the eight-connected branch)

If `\kappa(G)=8`, outcome 1 of Theorem 2.1 holds for every choice of
`r`, `phi`, and the four singleton-colour neighbours.

#### Proof

Outcome 2 gives an actual cut of order seven, contrary to
eight-connectivity.  \(\square\)

### Lemma 2.3 (the retained one-sided colouring trace)

In outcome 2, choose `x_j in D-T` and put `gamma=phi(x_j)`.  The colouring
`phi` restricted to

\[
                         G[C\cup S]-r
\]

extends to a proper six-colouring of `G[C union S]` by assigning colour
`gamma` to `r`.  In addition, all neighbours of `r` in `C` use only the
two colours not represented by `x_1,x_2,x_3,x_4`.

#### Proof

The vertex `x_j` is the unique neighbour of `r` having colour `gamma`.
It lies outside `C union T`, and `r` has no neighbours in `U-\{r\}`.
Thus no neighbour of `r` in the closed `C`-shore has colour `gamma`, which
proves the extension.

For each selected colour, its only representative in `N_G(r)` is the
corresponding `x_i`, and no `x_i` belongs to `C`.  Hence none of those four
colours occurs on `N_G(r) cap C`.  \(\square\)

Only one such accepted boundary trace is guaranteed: as many as three of
the four nominated vertices may belong to `T`.

## 3. Lifted separation order

For an oriented separation `p=(A,B)` of `H`, write

\[
 L_p=A-B,\qquad R_p=B-A,\qquad S_p=A\cap B
\]

and define

\[
 C_U(p)=\{u\in U:N_H(u)\cap L_p\ne\varnothing\ne
                         N_H(u)\cap R_p\},             \tag{3.1}
\]

\[
                         \lambda_U(p)=|S_p|+|C_U(p)|.  \tag{3.2}
\]

A **trace-preserving lift** of `p` is a separation
`(widehat A,widehat B)` of `G` whose intersections with `V(H)` are exactly
`A` and `B`.

### Theorem 3.1 (minimum lift and submodularity)

For every separation `p` of `H`:

1. `lambda_U(p)` is the minimum order of a trace-preserving lift of `p`;
2. `lambda_U` is symmetric; and
3. for separations `p=(A,B)` and `q=(C,D)`, with

   \[
   p\wedge q=(A\cap C,B\cup D),\qquad
   p\vee q=(A\cup C,B\cap D),
   \]

   one has

   \[
   \lambda_U(p\wedge q)+\lambda_U(p\vee q)
       \le\lambda_U(p)+\lambda_U(q).                  \tag{3.3}
   \]

If equality holds in (3.3), equality holds separately for the crossing
indicator of every `u in U`.  If `G` is `k`-connected and `p` is proper,
then

\[
                             \lambda_U(p)\ge k.         \tag{3.4}
\]

#### Proof

Every lift contains `S_p` in its separator.  A member of `C_U(p)` has a
neighbour in each open `H`-shore and must also belong to that separator.
Conversely, put precisely these crossing roots in the separator.  Put each
remaining root which has a neighbour in `R_p` on the right and every other
root on the left.  No such root has a neighbour in the opposite shore, and
independence of `U` creates no root-to-root crossing edge.  This constructs
a lift of order `lambda_U(p)`.

Symmetry is immediate.  The ordinary separator terms satisfy

\[
 |S_p|+|S_q|=|S_{p\wedge q}|+|S_{p\vee q}|.           \tag{3.5}
\]

For a fixed root, its crossing indicator is submodular.  Indeed, the
corner open shores are

\[
\begin{aligned}
 L_{p\wedge q}&=L_p\cap L_q,&
 R_{p\wedge q}&=R_p\cup R_q,\\
 L_{p\vee q}&=L_p\cup L_q,&
 R_{p\vee q}&=R_p\cap R_q.
\end{aligned}                                         \tag{3.6}
\]

If a root crosses both corners, (3.6) makes it cross both inputs.  If it
crosses only the meet, its common-left neighbour and a neighbour in
`R_p union R_q` make it cross at least one input; the join case is
symmetric.  Summing these indicator inequalities with (3.5) proves (3.3).
Equality in the sum forces equality for every nonnegative rootwise slack.

Finally, a proper separation of `H` has two nonempty open shores in every
lift.  A minimum lift is therefore a proper separation of `G`, and
`k`-connectivity gives (3.4).  \(\square\)

### Theorem 3.2 (fixed-anchor exact uncrossing)

Let `G` be `k`-connected.  Suppose `p,q` are proper separations of `H`
with

\[
 \lambda_U(p)=\lambda_U(q)=k,
 \qquad x\in L_p\cap L_q,
 \qquad y\in R_p\cap R_q.                             \tag{3.7}
\]

Then `p wedge q` and `p vee q` are proper and both have lifted order `k`.
Every root which crosses both input separations crosses both corners.

Consequently the exact lifted-order-`k` separations oriented between fixed
opposite anchors `x,y` form a finite sublattice and have a canonical
inclusion-minimum `x`-shore.

#### Proof

The anchors keep both corners proper.  Equation (3.4) gives a lower bound
of `k` on each corner, while (3.3) bounds their sum by `2k`; equality holds
throughout.  Rootwise equality in Theorem 3.1 retains every root which
crosses both inputs.  Closure under meet and join follows, and the meet of
the finite family gives its unique minimum `x`-shore.  \(\square\)

### Corollary 3.3 (the exact four-centre cut lattice)

Assume `\kappa(G)=7`.  Every proper three-separation of `H` is crossed by
all four members of `U` and lifts to an exact order-seven cut with boundary

\[
                             U\mathbin{\dot\cup}T,
                             \qquad |T|=3.             \tag{3.8}
\]

Conversely, the trace in `H` of any exact order-seven cut with boundary
`U dotcup T` is such a separation.  Cuts of this form oriented between
fixed opposite `H`-vertices form a finite sublattice; both corner
separators again have the form (3.8).  Its canonical minimum anchored shore
is connected.

#### Proof

For a proper three-separation `p`, (3.4) gives
`3+|C_U(p)|\ge7`, so every root crosses and equality holds.  Conversely,
every vertex of an exact cut in a seven-connected graph has a neighbour in
both open shores; otherwise the other six boundary vertices would still
separate one shore.  The trace therefore has separator `T` and all four
roots cross it.

The lattice assertion follows from Theorem 3.2.  If its minimum anchored
shore were disconnected, take the component containing the left anchor.
Its neighbourhood lies in the same seven-vertex lifted boundary and hence,
by seven-connectivity, equals that boundary.  This component defines a
strictly smaller anchored four-centre shore, a contradiction.  \(\square\)

### Corollary 3.4 (crossing-region bound)

Let `p_1,...,p_m` be exact four-centre cuts as in (3.8).  For a sign vector
`sigma in \{+,-\}^m`, let `R_sigma` be the intersection of the open shores
selected by its signs.  If both `R_sigma` and `R_{-sigma}` are nonempty,
then every `u in U` has a neighbour in `R_sigma`.

Hence at most eight sign regions whose antipodal regions are also nonempty
can occur.  In particular:

- two fully crossing cuts force every centre to meet all four corner
  regions;
- three Boolean-independent cuts force every centre to have exactly one
  neighbour in each of the eight regions and no neighbour on any of their
  boundaries; and
- four Boolean-independent cuts are impossible.

#### Proof

Choose opposite anchors in `R_sigma` and `R_{-sigma}` and orient every cut
accordingly.  Repeated meets in Corollary 3.3 remain exact four-centre cuts,
and their left open shore is exactly `R_sigma`.  Every root crosses the
resulting cut and therefore has a neighbour in that region.  Distinct sign
regions are disjoint, while every root has degree eight.  The three listed
consequences follow.  \(\square\)

The common-anchor condition is essential.  Arbitrary disjoint or nested
cell shores need not have proper lattice corners, and the lifted order does
not preserve colouring traces or branch-set labels.

## 4. A web obstruction must use another named centre

The exact cut retains more than its seven boundary labels.  The colouring
which produced it forces a linkage through one of the other three centres.

### Theorem 4.1 (centre-supported Kempe linkage)

Assume the rooted-web exact-cut outcome of Theorem 2.1.  Relabel the four
nominated vertices in their cyclic order on the outer face of the web, and
write

\[
                         c_i=\phi(x_i)\quad(1\le i\le4).
\]

For each pair `i,j`, the vertices `x_i,x_j` lie in the same
`c_i,c_j`-component of `G-r`.  In particular, the two components for the
crossing pairs

\[
                         x_1x_3,\qquad x_2x_4           \tag{4.1}
\]

are vertex-disjoint, and at least one of them contains a vertex of
`U-\{r\}`.

Let `Delta` be the two colours outside `\{c_1,c_2,c_3,c_4\}`.  Some named
centre `s in U-\{r\}` satisfies

\[
                \Delta\cap
                \bigl([6]-\phi(N_H(s))\bigr)=\varnothing. \tag{4.2}
\]

Equivalently, both colours in `Delta` occur on `N_H(s)`.

#### Proof

Suppose first that `x_i` and `x_j` lie in different components of the
subgraph induced by colours `c_i,c_j`.  Interchange those colours on the
component containing `x_i`.  The vertex `x_i` was the unique
`c_i`-neighbour of `r`, while `x_j` is not interchanged, so colour `c_i`
is now absent from `N_G(r)`.  Assigning that colour to `r` would
six-colour `G`, a contradiction.  Thus the stated Kempe component exists
for every pair.

The two components in (4.1) use disjoint pairs of colours and are therefore
vertex-disjoint.  If they both avoided `U-\{r\}`, they would lie in `H`
and contain two disjoint paths joining the alternating outer pairs.  This
is the linkage excluded by the defining Two Paths property of the web.
Hence one component contains another named centre.

For (4.2), suppose instead that every `s in U-\{r\}` has a colour
`delta_s in Delta` absent from `N_H(s)`.  Recolour each such `s` with
`delta_s`.  These recolourings are simultaneous and proper because `U` is
independent, and they do not change any colour on `N_G(r)`.  In the new
six-colouring of `G-r`, all three other centres use colours in `Delta`.
Repeating the first paragraph gives the two disjoint crossing Kempe paths,
now wholly in `H`, again contradicting the web.  \(\square\)

The theorem does not confine either component to `C` or to `D`; it only
forces the crossing obstruction through a named member of `U-\{r\}`.

## 5. Exact static limit of the two-shore quotient

The next lemma explains why the returned cut is not terminal from boundary
adjacency alone.

### Lemma 5.1 (two independent universal vertices)

Let `F` be a graph and form `J` by adjoining two nonadjacent vertices
`c,d`, each complete to `V(F)`.  Then

\[
 K_7^-\preccurlyeq J
 \quad\Longleftrightarrow\quad
 \left[
 K_5\preccurlyeq F
 \ \text{or}\
 K_5^-\preccurlyeq F-x\text{ for some }x\in V(F)
                             \right].                                             \tag{5.1}
\]

#### Proof

The reverse implication is explicit.  A `K_5` model in `F`, together with
`\{c\},\{d\}`, gives a `K_7^-` model whose only possible missing adjacency
is `cd`.  If `F-x` has a `K_5^-` model, use its five bags together with
`\{c,x\}` and `\{d\}`.

For the forward implication, take a `K_7^-` model in `J`.  If neither
universal vertex is used, or only one is used, selecting suitable
boundary-only bags gives a `K_5` model in `F`.  Suppose both are used.  If
they are distinct singleton bags, their nonedge consumes the only allowed
missing adjacency, so the other five bags form a `K_5` model in `F`.

In every other case, some bag containing `c` or `d` also contains a vertex
`x` of `F`: this is automatic if both universal vertices occupy one
connected bag.  Discard the one or two bags meeting `c,d`.  At least five
remaining bags lie in `F-x` and have at most one missing mutual adjacency.
They form a `K_5^-` model there.  \(\square\)

### Corollary 5.2 (the nonclique residue)

In outcome 2 of Theorem 2.1:

1. `G[T]` is not a triangle;
2. `G[S]` has no `K_5` minor; and
3. `G[S]-x` has no `K_5^-` minor for every `x in S`.

#### Proof

If `G[T]` were a triangle, use the boundary partition

\[
                         U\mid\{t_1\}\mid\{t_2\}\mid\{t_3\}. \tag{5.2}
\]

On each closed shore, contract the opposite connected component together
with the independent block `U`, six-colour the resulting proper minor, and
pull the colouring back.  The three retained singleton vertices form a
clique, so this produces the exact partition (5.2) on both copies of `S`.
After permuting colour names, the two colourings agree on `S` and glue to a
six-colouring of `G`, contrary to (1.1).

For the remaining assertions, contract `C` and `D` separately.  The
resulting minor is the graph obtained from `G[S]` by adjoining two
nonadjacent vertices complete to `S`.  It has no `K_7^-` minor, so Lemma
5.1 gives both exclusions.  \(\square\)

The contracted picture alone still permits sparse boundary graphs, even
with `U` retained literally.  Thus the live obligation is dynamic:

> Use the one-sided trace of Lemma 2.3 and the colour-labelled paths forced
> by `phi` to obtain a common boundary partition, a rooted augmentation, or
> a strictly smaller four-centre cut in the lattice of Corollary 3.3.

Treating the three web-completion edges on `T` as host edges, confining a
Kempe interchange to `C`, or assuming that lifted-order uncrossing preserves
the colouring labels would be unsupported.

## External input and dependencies

- B. D. McKay and S. P. Radziszowski, *`R(4,5)=25`*, Journal of Graph
  Theory 19 (1995), 309--322,
  <https://doi.org/10.1002/jgt.3190190304>.  By Ramsey-number symmetry this
  is the equality `R(5,4)=25` used to extract `U`.
- R. Fabila-Monroy and D. R. Wood, *Rooted `K_4`-Minors*, Electronic
  Journal of Combinatorics 20(2) (2013), Paper P64, Lemma 2 and Theorem 8,
  <https://doi.org/10.37236/3476>.  For four nominated vertices in a
  three-connected graph, their theorem says that a rooted `K_4` minor
  exists exactly when the graph is not a spanning subgraph of a web rooted
  at those vertices; their Two Paths formulation gives the missing
  alternating-pair linkage in the displayed cyclic web order.
- [Critical-host degree and density closure](../results/hc7_k7minus_degree7_rooted_helper_closure.md).
- [Two-component normal form for an order-seven cut](../results/hc7_k7minus_three_component_seven_cut_exclusion.md).
- [Exact boundary-colouring reflection](../results/hc7_k7minus_critical_seven_cut_capacity.md),
  Lemma 1.
