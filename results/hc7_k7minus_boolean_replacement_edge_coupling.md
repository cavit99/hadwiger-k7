# Linked Boolean replacement cuts and critical-edge colourings

**Status:** written proof with a separate hash-pinned internal audit.

This note identifies the literal graph structure carried by the Boolean
family of replacement cuts from the
[common-colouring theorem](hc7_k7minus_common_colouring_centre_change.md).
The separator coordinates are not merely formal choices: each replacement
edge lies on its own path in one common seven-path linkage.  Deleting one
coordinate edge produces an exact order-six separation, while deleting two
produces an exact order-five separation.  Proper-minor colourings realize
the punctured Boolean family of endpoint-equality signatures on the same
coordinates.

The results are unbounded and computation-free.  They do not prove the
`K_7^-` six-colour conjecture.  Section 6 does, however, eliminate one
genuine subcase of the four-region equality configuration.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,
 \qquad \delta(G)\ge8,
 \qquad |E(G)|\ge4|V(G)|.                           \tag{1.1}
\]

Let `U` be an independent set of four degree-eight vertices.  Retain the
four-region equality case and notation of Corollaries 4.2 and 4.3 of the
common-colouring theorem.  Thus, for every `P in mathcal P`, there is an
exact cut

\[
                         U\mathbin{\dot\cup}T_P,      \tag{1.2}
\]

with connected complementary components `P,O_P`, each adjacent to every
boundary vertex.  Put

\[
 W_P=\{u\in U:|N_G(u)\cap P|=1\},                   \tag{1.3}
\]

and denote the unique neighbour of `u in W_P` in `P` by `x_{uP}`.  The
vertices `x_{uP}` are distinct.  For `W subseteq W_P`, write

\[
 X(P,W)=\{x_{uP}:u\in W\},
 \qquad
 S_W=(U-W)\cup T_P\cup X(P,W).                      \tag{1.4}
\]

The cited corollaries show that `S_W` is an exact order-seven cut and that
its two open sides are

\[
                    P-X(P,W),\qquad O_P\cup W.       \tag{1.5}
\]

Both are connected and adjacent to every vertex of `S_W`, and the first
has at least two vertices.  We use the corresponding closed sides

\[
 \begin{aligned}
 A_W&=P\cup T_P\cup(U-W),\\
 B_W&=O_P\cup T_P\cup U\cup X(P,W).
 \end{aligned}                                      \tag{1.6}
\]

## 2. One linkage identifies every replacement coordinate

### Theorem 2.1 (coordinate paths through the Boolean family)

Fix `P in mathcal P` and a nonempty set `R subseteq W_P`.  Choose

\[
             a\in P-X(P,R),\qquad b\in O_P.           \tag{2.1}
\]

Then every family of seven internally vertex-disjoint `a`--`b` paths has
the following properties.

1. Every path meets every separator `S_W`, `W subseteq R`, in exactly one
   vertex.
2. Each vertex of `(U-R) union T_P` lies on one fixed path, which meets
   every `S_W` at that vertex.
3. For every `u in R`, one fixed path `Q_u` meets `S_W` at
   `u` when `u notin W` and at `x_{uP}` when `u in W`.
4. Traversed from `a` to `b`, the path `Q_u` contains the literal edge
   `x_{uP}u`, with `x_{uP}` immediately before `u`.

In particular, the edges `x_{uP}u`, `u in R`, lie on distinct paths.  The
whole Boolean family therefore has one simultaneous path identification of
its replacement coordinates; no permutation of coordinates occurs.

#### Proof

Seven-connectivity and Menger's theorem give seven internally
vertex-disjoint `a`--`b` paths.  Fix any such family.  Each `S_W` is an
`a`--`b` separator of order seven.  Every path therefore meets `S_W`, and
internal disjointness forces the seven intersections to be singletons
which exhaust `S_W`.

At `S_emptyset=U union T_P`, label the paths by their unique separator
vertices.  The separators `S_emptyset` and `S_{\{u\}}` have six common
vertices.  Those vertices remain on their six labelled paths, so the
remaining path `Q_u` contains both `u` and `x_{uP}`.  Since every `S_W`
contains exactly one of those two vertices and every path meets `S_W`
once, item 3 follows for all `W subseteq R`.  Distinct members of `R` label
distinct paths at `S_emptyset`.

It remains to determine the segment between `x_{uP}` and `u`.  Relative
to `S_emptyset`, the part of `Q_u` before `u` lies in `P` and the part
after `u` lies in `O_P`.  Relative to `S_{\{u\}}`, the part before
`x_{uP}` lies in `P-x_{uP}` and the part after it lies in
`O_P union \{u\}`.  Hence `x_{uP}` precedes `u`.  An internal vertex
strictly between them would belong both to `P` and to `O_P union \{u\}`,
which is impossible.  Thus they are consecutive. \(\square\)

## 3. The punctured endpoint-colouring family

For `R subseteq W_P`, put

\[
                        M_R=\{ux_{uP}:u\in R\}.       \tag{3.1}
\]

These edges form a matching.

### Theorem 3.1 (critical-edge signatures and shore restrictions)

For every nonempty `I subseteq R`, the graph `G-M_R` has a proper
six-colouring `kappa_I` such that

\[
  \kappa_I(u)=\kappa_I(x_{uP})
       \quad\Longleftrightarrow\quad u\in I.          \tag{3.2}
\]

No proper six-colouring of `G-M_R` has unequal colours at both ends of
every edge in `M_R`.

If `E(kappa)` is the set of coordinates whose endpoints have equal colours
in a proper six-colouring `kappa` of `G-M_R`, then, for every
`W subseteq R`,

\[
 \begin{aligned}
  \kappa|G[A_W]\text{ is proper}
       &\quad\Longleftrightarrow\quad E(\kappa)\subseteq W,\\
  \kappa|G[B_W]\text{ is proper}
       &\quad\Longleftrightarrow\quad E(\kappa)\cap W=\varnothing.
 \end{aligned}                                      \tag{3.3}
\]

Every restriction `kappa|S_W` is a proper boundary colouring.

#### Proof

For nonempty `I`, contract all edges `ux_{uP}` with `u in I` and retain
the other edges of `M_R`.  The result is a proper minor of `G` and hence
has a proper six-colouring.  Expand the contracted vertices and then
delete all edges of `M_R`.  The contracted pairs have equal colours, while
every retained edge of `M_R` has differently coloured ends.  This proves
(3.2).

If all pairs had different colours, every edge of `M_R` could be restored,
giving a six-colouring of `G`.  This is impossible.

The closed side `A_W` contains both ends of `ux_{uP}` exactly when
`u notin W`; the closed side `B_W` contains both ends exactly when
`u in W`.  All edges outside `M_R` are proper under `kappa`.  This proves
(3.3).  Finally, `S_W` contains exactly one end of each edge in `M_R`, so
its restriction is always proper. \(\square\)

For `R=\{u,v\}`, Theorem 3.1 gives exactly the three signatures

\[
              (=,=),\qquad (=,\ne),\qquad (\ne,=),    \tag{3.4}
\]

while `(ne,ne)` is forbidden.  The three signatures may be realized by
three unrelated colourings.  The theorem does not place them in one Kempe
sequence or align their equality partitions on the common boundary.

## 4. Every coordinate edge exposes an exact order-six separation

### Theorem 4.1 (one-coordinate deletion)

Fix `u in W_P` and `W_0 subseteq W_P-\{u\}`.  Put

\[
 \begin{aligned}
  x&=x_{uP},\\
  Q&=(U-(W_0\cup\{u\}))\cup T_P\cup X(P,W_0),\\
  L&=P-X(P,W_0),\\
  R'&=O_P\cup W_0\cup\{u\},\\
  H&=G-ux.
 \end{aligned}                                      \tag{4.1}
\]

Then:

1. `|Q|=6`, and `H-Q` has exactly the two connected components `L,R'`.
   Both are adjacent to every vertex of `Q`.
2. The graph `H` is six-connected, exactly six-chromatic,
   `K_7^-`-minor-free, and

   \[
                         |E(H)|\ge4|V(H)|-1.          \tag{4.2}
   \]
3. The graph `G[Q]` has no `K_5^-` minor and

   \[
 |E(G[Q_0])|\le8\quad(Q_0\in\tbinom Q5),
 \qquad |E(G[Q])|\le11.                              \tag{4.3}
   \]
4. If

   \[
    \delta_Z=|E(H[Z])|+|E_H(Z,Q)|-4|Z|
       \qquad (Z\in\{L,R'\}),                        \tag{4.4}
   \]

   and `sigma=|E(G)|-4|V(G)|`, then

   \[
            \delta_L+\delta_{R'}
              =\sigma+23-|E(G[Q])|\ge\sigma+12.     \tag{4.5}
   \]
5. The edge `ux` is not double-critical:

   \[
                         \chi(G-\{u,x\})=6.           \tag{4.6}
   \]

   Consequently `G-\{u,x\}` has a spanning `K_6`-minor model, and the
   audited adjacent-pair palette theorem applies to `ux`.
6. For `Z in \{L,R'\}` and every nonempty `Q_0 subseteq Q`, the rooted
   pair

   \[
                         (H[Z\cup Q_0],Q_0)           \tag{4.7}
   \]

   is internally `|Q_0|`-connected.

#### Proof

The two exact cuts indexed by `W_0` and `W_0 union \{u\}` show that `L`
and `R'` are connected.  Every vertex of `Q` has a neighbour in both.
The only edge of `G-Q` between them is `ux`: the original components
`P,O_P` are anticomplete; each centre in `W_0` has had its unique
`P`-neighbour removed into `Q`; `u` has the unique remaining neighbour
`x` in `P`; and `U` is independent.  Deleting `ux` proves item 1.

Suppose that a set `Z` of at most five vertices disconnects `H`.  Since
`G` is seven-connected, neither `u` nor `x` lies in `Z`, and adding `ux`
must join the components of `H-Z`.  If an endpoint component were a
singleton, that endpoint would have degree at most six in `G`, contrary
to minimum degree eight.  Deleting `Z` together with either endpoint now
gives a cut of `G` of order at most six, a contradiction.  Thus `H` is
six-connected.

The edge deletion is a proper minor operation, so `H` is six-colourable
and remains `K_7^-`-minor-free.  A five-colouring of `H` would either
already colour `G`, if `u,x` had different colours, or could be extended
to a six-colouring of `G` by giving one endpoint a fresh colour.  Hence
`chi(H)=6`.  The density bound follows from (1.1).

A `K_5^-` model in `G[Q]`, together with the connected sets `L,R'`, would
give a `K_7^-` model in `G`: both sets are adjacent to every boundary bag,
and `ux` supplies their mutual adjacency.  Thus no such boundary model
exists.

Apply the audited order-six-cut localisation theorem to `H,Q`.  Its
two-component case gives (4.3).  Relative to the threshold
`4|V(H)|-2`, the surplus of `H` is `sigma+1`.  The exact identity in that
theorem gives (4.5).

Finally, every common neighbour of `u,x` belongs to `Q`.  It cannot be
another centre because `U` is independent, and it cannot belong to
`X(P,W_0)` because `x` is the unique neighbour of `u` in `P`.  Therefore

\[
                       N_G(u)\cap N_G(x)\subseteq T_P,
                                                               \tag{4.8}
\]

so the pair has at most three common neighbours.  If
`G-\{u,x\}` had a proper five-colouring, each colour class would contain
a common neighbour of `u,x`.  Indeed, if colour `i` had no common
neighbour, recolour all `i`-coloured neighbours of `u` with one fresh sixth
colour, give `u` colour `i`, and give `x` the fresh colour.  The recoloured
vertices are independent and none is adjacent to `x`, so this would be a
proper six-colouring of `G`.  Five distinct common neighbours contradict
(4.8).  The reverse inequality follows because vertex deletion gives a
proper minor of `G`, proving (4.6).

Hadwiger's conjecture for chromatic number six gives a `K_6` minor in
`G-\{u,x\}`; connectedness lets it be enlarged to a spanning model.  The
remaining assertion is exactly the hypothesis of the audited
adjacent-pair palette theorem.

For item 6, a forbidden rooted separation of `H[Z union Q_0]` of order
below `|Q_0|`, after adjoining `Q-Q_0` to its separator, would give a cut
of `H` of order below six separating part of `Z` from the opposite
component.  This contradicts six-connectivity. \(\square\)

### Proposition 4.2 (the exact endpoint-type obstruction)

Use the exact order-six separation in Theorem 4.1.  Suppose that
`H[L union Q]` and `H[R' union Q]` have proper six-colourings which induce
the same equality partition `Pi` on `Q`.  Permute colour names so that the
two colourings agree on `Q`.

For an endpoint `z in \{x,u\}`, call its colour type a **boundary type**
if its colour occurs on `Q`, naming the corresponding block of `Pi`; call
it an **unused type** otherwise.  The two shore colourings can be aligned
to give a proper six-colouring of `G` unless exactly one of the following
holds:

1. `x` and `u` have the same boundary type; or
2. `Pi` has five blocks and both endpoints have the unique unused type.

In every proper six-colouring of `H`, one of these two obstructions occurs.
If the common endpoint colour is absent from `Q`, then `Pi` has shape

\[
                         2+1+1+1+1.                  \tag{4.9}
\]

#### Proof

After the boundary colours have been aligned, the two closed-shore
colourings glue to a proper colouring of `H`.  Restoring `ux` is proper
exactly when the endpoint colours differ.  Different boundary blocks give
different colours, and a boundary colour differs from every unused colour.
If both endpoint colours are unused and at least two palette colours are
absent from `Q`, permute those unused colours on one shore so that the
endpoints differ.  The two displayed cases are precisely the situations
in which this is impossible.

Every six-colouring of `H=G-ux` gives `u,x` the same colour, since otherwise
it would colour `G`.  If that colour is absent from `Q`, item 5 and Lemma 2.2
of the audited adjacent-pair palette theorem give, for each of the other
five colours, a bichromatic `x`--`u` path in `H`.  Every such path meets the
separator `Q`, and its
intersection contains the corresponding other colour.  All five colours
therefore occur on the six-set `Q`, giving exactly five blocks and (4.9).
\(\square\)

## 5. A replacement square exposes an exact order-five separation

### Corollary 5.1 (two-coordinate deletion)

Let `u,v in W_P` be distinct, put `x=x_{uP}`, `y=x_{vP}`, and define

\[
 e=ux,\qquad f=vy,\qquad
 F=(U-\{u,v\})\cup T_P,\qquad J=G-\{e,f\}.           \tag{5.1}
\]

Then:

1. `J-F` has exactly two connected components,

   \[
                         P,\qquad O_P\cup\{u,v\},    \tag{5.2}
   \]

   and both are adjacent to every vertex of `F`.
2. The graph `J` is five-connected, exactly six-chromatic and
   `K_7^-`-minor-free, with

   \[
                         |E(J)|\ge4|V(J)|-2.          \tag{5.3}
   \]

   In particular, it has a spanning `K_6`-minor model.
3. Its six-colour endpoint signatures are exactly those in (3.4), and
   their proper restrictions to the four closed sides are governed by
   (3.3).
4. In a double-contraction colouring of `J`, one of the pairs `ux,vy` is
   joined by bichromatic paths for at least three alternate colours.  If
   `xy in E(G)`, one pair has at least four such bichromatic connections.

#### Proof

Deleting `e,f` removes every edge from `P` to `O_P union \{u,v\}`.  Both
sets in (5.2) are connected and full to `F` by the replacement-cut
theorem, proving item 1.

We verify five-connectivity directly.  Suppose that a set `Z` of at most
four vertices disconnects `J`.  The component graph of `J-Z` becomes
connected after adding only `e,f`, so it has at most three vertices.  If it
has three, a leaf component is incident with one deleted edge.  Delete the
endpoint of that edge in the leaf component; if the leaf is that singleton,
delete the opposite endpoint instead.  Together with `Z`, this gives a cut
of `G` of order at most five.

If `J-Z` has two components, choose one of them, say `K`, and let `T_K`
be the endpoints in `K` of the deleted edges crossing the two components.
If `K-T_K` is nonempty, then `Z union T_K` is a cut of `G` of order at
most six.  If `K=T_K`, delete the opposite crossing endpoints instead.
The other component has a vertex left unless `G` has at most eight
vertices; a seven-connected graph of order eight is `K_8` and contains
`K_7^-`.  Every case contradicts (1.1).  Thus `J` is five-connected.  The
displayed five-set `F` is a cut, so its order is exact.

The common edge-deletion graph is a proper minor and hence six-colourable.
It cannot be five-colourable: repair every monochromatic member of
`\{e,f\}` by assigning one fresh sixth colour to its endpoint in
`\{u,v\}`.  The selected endpoints are nonadjacent because `U` is
independent.  This would six-colour `G`.  Thus `chi(J)=6`, and the known
case of Hadwiger's conjecture supplies the spanning `K_6` model.  The
density and minor-exclusion assertions are immediate.

Theorem 3.1 gives item 3.  Item 4 is the audited common-host
double-contraction bichromatic-connection theorem.  When `xy` is an edge, the two
contracted images are adjacent and hence receive distinct colours, giving
the four-connection conclusion. \(\square\)

## 6. A terminal adjacency subcase

Let `Gamma` be the interaction graph on the four inclusion-minimal
opposite-side regions from Corollary 4.1 of the common-colouring theorem.
In the equality case

\[
                         \Gamma\in\{2K_2,P_4,C_4\}.  \tag{6.1}
\]

The fifth member `C` of `mathcal P` is anticomplete to those four regions.

### Proposition 6.1

Suppose `Gamma in \{P_4,C_4\}`.  For every `P in mathcal P` and every
distinct `u,v in W_P`, the two replacement vertices

\[
                         x=x_{uP},\qquad y=x_{vP}     \tag{6.2}
\]

are nonadjacent.

#### Proof

Suppose that `xy` is an edge.  The five pairwise disjoint connected sets
in `mathcal P` will supply five branch sets, using `P-\{x,y\}` in place
of `P`.  This remainder is connected and has at least two vertices.

This replacement preserves every interaction edge incident with `P`.
Indeed, if another piece `Q'` is adjacent to `P`, then some vertex of
`Q'` belongs to `N_{G-U}(P)=T_P`.  The component `P-\{x,y\}` is full to the
replacement boundary `S_{\{u,v\}}`, so it has a neighbour at that same
vertex of `Q'`.

Choose one endpoint region of `Gamma=P_4`, or any region of
`Gamma=C_4`.  Add one of the two centres in `U-\{u,v\}` to that region,
and add the other remaining centre to `C`.  Each enlarged set is connected
and adjacent to all five piece branch sets.  Every centre has a neighbour
in every original member of `mathcal P`.  Fullness at `S_{\{u,v\}}`
supplies each remaining centre with a neighbour in `P-\{x,y\}`, so the
same conclusion holds for the modified `P`-bag.  After the bags containing
`C` and the selected region have
been made universal among the five piece bags, the other three regions
induce a `P_3`.  Hence among the five piece branch sets at most one pair
is nonadjacent.

Add the two branch sets

\[
                         \{u,x\},\qquad\{v,y\}.       \tag{6.3}
\]

They are connected and adjacent to one another through `xy`.  Each is
adjacent to the four piece branch sets other than the remainder of `P`,
because its centre is adjacent to every piece.  It is also adjacent to
`P-\{x,y\}`.  Indeed, connectedness of both `P-x` and `P-y` forces `x`
and `y` each to have a neighbour in that remainder.  Thus the seven
displayed branch sets are pairwise adjacent except possibly for the one
missing adjacency among the five piece bags.  They form a `K_7^-` model,
contrary to (1.1). \(\square\)

The proposition is not asserted for `Gamma=2K_2`: after two piece bags are
made universal, the remaining three need not induce a path.

## 7. Exact remaining interface

The linkage and colouring conclusions live on the same Boolean
coordinates, but they do not yet identify the relevant boundary
partitions.  In particular:

- the colourings `kappa_I` for different `I` may be unrelated;
- replacing `u` by `x_{uP}` is not a Kempe change, since `ux_{uP}` is an
  edge and its ends have different colours in every intact closed shore;
- a square guaranteed by the counting argument need not be based at the
  minimum selected component `C`; and
- the exact order-five and order-six separations above retain density and
  path coordinates, but existing rooted-minor theorems do not yet preserve
  the required boundary partition through them.

The next one-coordinate statement is therefore precise.  For adjacent
cuts differing by `u` versus `x_{uP}`, simultaneous rejection of the two
coherent boundary partitions must force one of:

1. connected subgraphs that realize the required boundary partition and
   permit the two shore colourings to be combined;
2. the prescribed rooted `K_6^-` minor on the selected closed side; or
3. a strict trace-admissible exact-cut descent.

Theorem 4.1 and Corollary 5.1 show that this is not an abstract partition problem:
the transfer edge lies simultaneously in a seven-path linkage, an exact
order-six separation of its deletion graph, a non-double-critical
adjacent-pair palette frame, and, with a second coordinate, an exact
order-five separation with a common spanning `K_6` model.

## Dependencies

- [A common colouring at several degree-eight vertices](hc7_k7minus_common_colouring_centre_change.md), Corollaries 4.1--4.3.
- [Localisation at an order-six cut](hc7_k7minus_exact_six_cut_localisation.md).
- [Palette-permutation linkage at a non-double-critical adjacent pair](hc7_adjacent_pair_palette_linkage.md).
- [Bichromatic connections after two named edge contractions](hc7_common_host_double_contraction_lock_allocation.md).
- N. Robertson, P. Seymour and R. Thomas,
  *Hadwiger's conjecture for `K_6`-free graphs*, Combinatorica **13**
  (1993), 279--361, <https://doi.org/10.1007/BF01202354>.
