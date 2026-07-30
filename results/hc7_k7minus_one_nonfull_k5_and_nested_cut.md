# Literal-clique exclusion at a two-component exceptional vertex and nested cuts

**Status:** written proof; [separate internal audit](hc7_k7minus_one_nonfull_k5_and_nested_cut_audit.md) GREEN.  This result
strengthens one branch of the exceptional degree-eight programme.  It does
not prove the `K_7^-` six-colour conjecture or the remaining connected-
subgraph allocation theorem.

Throughout, let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(M)\le6\text{ for every proper minor }M\text{ of }G,
 \qquad K_7^-\npreccurlyeq G.                         \tag{H}
\]

Let `u` be an exceptional vertex of degree eight, put `X=N_G(u)`, and
suppose that `G-N_G[u]` has exactly two components `E,F`.  Thus `G[X]` is
`K_4`-free.  Seven-connectivity makes each exterior component adjacent to
at least seven of the eight vertices of `X`.

## 1. Two exterior components exclude every literal `K_5`

### Lemma 1 (common-attachment five-linkage)

Let `D` be either exterior component and let `D'` be the other.  Write
`N_X(D)=N_G(D)\cap X` and put

\[
 T=N_X(E)\cap N_X(F),\qquad J_D=G[D\cup N_X(D)].       \tag{1}
\]

Then `|T|\ge6`, and `J_D` contains no literal `K_5`.

#### Proof

Each of `E,F` misses at most one vertex of `X`, so `|T|\ge6`.  Suppose that
a five-set `L` induces a clique in `J_D`.  There are five pairwise
vertex-disjoint `L`--`T` paths in `J_D`, with distinct initial vertices in
`L` and distinct final vertices in `T`.
Otherwise, the set form of Menger's theorem gives a set
`W\subseteq V(J_D)` of order at most four meeting every `L`--`T` path
(paths of length zero are allowed when `L` meets `T`).  The nonempty clique
`L-W` lies in one component `Q` of `J_D-W`.  If `Q` met `T-W`, it would
contain an `L`--`T` path avoiding `W`; hence `Q` is disjoint from `T-W`.

Delete, in addition to `W`, the vertex `u` and the set `X-N_X(D)`, which
has order at most one.  The component `Q` then has no route out of `J_D`.
It has no edge to `D'`: every vertex of `N_X(D)` adjacent to `D'` belongs
to `T`, and `Q` avoids `T-W`.  Its only possible route through the rest of
`X` was deleted, as was its possible route through `u`.  Thus

\[
                         W\cup\{u\}\cup(X-N_X(D))      \tag{2}
\]

is a vertex cut of order at most six.  Both sides are nonempty because
`L-W` and `T-W` are nonempty.  This contradicts seven-connectivity.

Trim the five paths so that their interiors avoid `L\cup T`, and enlarge
each singleton clique vertex along its corresponding path.  The five
resulting branch sets remain pairwise disjoint, connected and pairwise
adjacent.  Each contains a different vertex of `T`, so each is adjacent
to both `\{u\}` and `D'`.  The seven branch sets

\[
              \{u\},\qquad D',\qquad
              \text{the five enlarged clique bags}     \tag{3}
\]

have every required adjacency except the one between `u` and `D'`.  They
form an explicit `K_7^-`-minor model, a contradiction. \(\square\)

### Theorem 2 (global literal-`K_5` exclusion)

The graph `G` contains no literal `K_5`.

#### Proof

A literal `K_5` containing `u` would have its other four vertices in `X`,
contrary to the fact that `G[X]` is `K_4`-free.  A clique avoiding `u`
cannot meet both `E` and `F`, which are anticomplete.  If it meets an
exterior component `D`, every one of its vertices in `X` belongs to
`N_X(D)`, so it lies in `J_D`, contrary to Lemma 1.  If it lies wholly in
`X`, it again contradicts `K_4`-freeness. \(\square\)

### Corollary 2.1 (degree and density jump)

Let `n_i` denote the number of degree-`i` vertices and put

\[
                 \tau=\sum_{i\ge10}(i-9)n_i.           \tag{4}
\]

Then

\[
 n_7=0,\qquad \delta(G)\ge8,\qquad |E(G)|\ge4|V(G)|,
 \qquad n_8\ge25+\tau.                                \tag{5}
\]

Every degree-eight vertex is exceptional, and in particular
`|V(G)|\ge25`.

#### Proof

The exact degree-seven neighbourhood theorem says that every degree-seven
vertex of a graph satisfying (H) lies in a literal `K_5`.  Theorem 2 and
the established lower bound `\delta(G)\ge7` therefore give `n_7=0` and
`\delta(G)\ge8`, which imply the edge bound in (5).  A degree-eight vertex
is nonexceptional exactly when it lies in a literal `K_5`, so every such
vertex is exceptional.

Jakobsen's extremal inequality, in the already audited degree-defect form,
is

\[
              25\le 9|V(G)|-2|E(G)|
                 =2n_7+n_8-\tau.                      \tag{6}
\]

Substituting `n_7=0` proves `n_8\ge25+\tau` and hence `|V(G)|\ge25`.
\(\square\)

## 2. The one-nonfull specialization

Suppose now that `E` misses `x\in X` and `F` is adjacent to every vertex
of `X`.  Put

\[
                         S=X-\{x\}.                    \tag{7}
\]

The proved one-nonfull reduction says that `E` has `S`-full connected-
subgraph packing number one, while `F\cup\{u,x\}` has packing number two.
It also says that `G[S]` lies in the frozen 129-boundary residual and

\[
                         |N_G(x)\cap S|\le4.            \tag{8}
\]

A connected subgraph is **`S`-full** when it is adjacent to every literal
vertex of `S`.

### Corollary 2.2 (local order bounds)

One has

\[
            |N_G(x)\cap F|\ge7-|N_G(x)\cap S|\ge3,    \tag{9}
\]

and `|E|,|F|\ge3`.

#### Proof

The neighbours of `x` lie in `\{u\}\cup S\cup F`.  Equations (5) and (8)
give (9), so `|F|\ge3`.  If `|E|=1`, its vertex has degree at most seven.
If `|E|=2`, minimum degree eight makes both vertices adjacent to each other
and to all seven vertices of `S`; their two singleton subgraphs would then
be disjoint and `S`-full, contrary to the packing-one conclusion for `E`.
Thus `|E|\ge3`. \(\square\)

## 3. Six paths exist, but every one is blocked

### Lemma 3 (six-fan obstruction)

The graph `G[F\cup X]` contains six internally vertex-disjoint paths from
`x` to six distinct vertices of `S`, with no internal vertex in `S`.
Let `T` be their union after deleting their six ends in `S`.  Then `T` is
connected, lies in `F\cup\{x\}`, and is adjacent to six vertices of `S`.
In a graph satisfying (H), every such `T` meets every `S`-full connected
subgraph of `F`.

#### Proof

If no six-fan existed, the fan form of Menger's theorem would give an
`x`-avoiding set `W` of order at most five separating `x` from `S` in
`G[F\cup X]`.  The set `S-W` is nonempty.  Deleting `W\cup\{u\}` from
`G` would leave `x` separated from `S-W`:
the only omitted vertices are `u` and the component `E`, and `E` has no
edge to `x` or `F` and can only be entered through `S`.  This contradicts
seven-connectivity.  Truncating each path at its first visit to `S` gives
the stated fan.

If its open union `T` avoided an `S`-full connected subgraph `P\subseteq
F`, then `\{u\},P,T` would be three pairwise disjoint connected subgraphs
on the same side of the separation with boundary `S`: the first two are
`S`-full and `T` misses only one boundary vertex.  The opposite component
`E` is `S`-full.  The audited uniform defect-two connected-subgraph
reflection theorem would six-colour `G`, contrary to (H). \(\square\)

Thus the difficulty is not the existence of enough paths.  Every six-fan
is a transversal of the family of `S`-full connected subgraphs in `F`.

## 4. A failed allocation gives two overlapping cuts

### Theorem 4 (tight nested-cut reduction)

Fix any `S`-full connected subgraph `P\subseteq F`.  Let `K` be the
component containing `x` in

\[
                         G[(F\cup\{x\})-V(P)],         \tag{10}
\]

and put

\[
 A=N_G(K)\cap S,\qquad B=N_G(K)\cap V(P).             \tag{11}
\]

Then

\[
                         N_G(K)=\{u\}\mathbin{\dot\cup}A
                                  \mathbin{\dot\cup}B, \tag{12}
\]

and every surviving configuration satisfies

\[
                         |A|\le4,\qquad |A|+|B|\ge6.  \tag{13}
\]

If equality holds in (13), put

\[
 C=\{u\}\cup A\cup B,\qquad Z=\{x\}\cup A\cup B.  \tag{14}
\]

Then all of the following hold.

1. `C` is a seven-vertex cut and `G-C` has exactly two components, one of
   which is `K`.  The `C`-full packing number of `K` is one.  The other
   component has packing number one or two.  In the latter case

   \[
                     K_4^-\npreccurlyeq G[C]-c
                     \qquad(c\in C).                   \tag{15}
   \]

   In the former case `C` is an exact `(1,1)` cut.
2. The component `K` is not the singleton `\{x\}`.  The graph `K-x` has
   one or two components.  Every component `Q` of `K-x` satisfies

   \[
                            N_G(Q)=Z.                   \tag{16}
   \]

   Consequently `Z` is a second seven-vertex cut.  If `K-x` is connected,
   `G-Z` has exactly two components.  If `K-x` has two components, `G-Z`
   has exactly three, `\chi(G[Z])=3`, and every proper three-colouring of
   `G[Z]` has colour-class sizes `3,2,2`.

#### Proof

The vertex `x` has no neighbour in `E`, while vertices of `F` have no
neighbour in `E\cup\{u\}`.  Different components of `F-P` are
anticomplete, and every component adjacent to `x` belongs to `K`.
Therefore the only neighbours of `K` outside it are `u`, the set `A` in
`S`, and the attachment set `B` in `P`, proving (12).
Seven-connectivity now gives `|A|+|B|\ge6`.  If `|A|\ge5`, the three
disjoint connected subgraphs `\{u\},P,K` satisfy the uniform defect-two
connected-subgraph reflection theorem against the `S`-full component `E`,
six-colouring `G`.
Thus a surviving configuration has `|A|\le4`, proving (13).

Suppose `|A|+|B|=6`.  Equation (12) makes `C=N_G(K)` an order-seven cut.
Every component of `G-C` is adjacent to every vertex of `C`, by
seven-connectivity.  In particular, every component other than `K` has a
neighbour of `u`.  The only neighbours of `u` outside `C\cup K` are the
vertices of `S-A`, and all of those lie in one component together with
`E`.  Hence there is exactly one component besides `K`.

Every `C`-full connected subgraph in `K` contains `x`, because `x` is the
only vertex of `K` adjacent to `u`.  Its packing number is therefore one.
The critical seven-cut capacity theorem gives packing number one or two
on the other component.  If it is two, the connected-rich diamond-deletion
lemma gives (15); if it is one, the packing vector is `(1,1)`.  This proves
item 1.

If `K=\{x\}`, then (12) and equality give `d_G(x)=7`, contrary to
Corollary 2.1.  Thus `K-x` is nonempty.  Let `Q` be one of its components.
By (11)--(12),

\[
                         N_G(Q)\subseteq\{x\}\cup A\cup B=Z.
\]

The right side has order seven, while seven-connectivity gives
`|N_G(Q)|\ge7`; hence equality holds, proving (16).

The components of `K-x` are therefore components of `G-Z`.  If `D` is any
other component of `G-Z`, seven-connectivity and `|Z|=7` give
`N_G(D)=Z`; in particular, `D` is adjacent to `x`.  Outside `Z` and the
components of `K-x`, the only neighbour of `x` is `u`: its `S`-neighbours
are in `A`, its neighbours in `P` are in `B`, and every other `F`-neighbour
belongs to `K-x`.  Thus all vertices outside the components of `K-x` lie in one
component containing `u`.  The critical seven-cut capacity theorem says
that deleting `Z` leaves at most three components, so `K-x` has at most
two.  In the two-component case that theorem also gives the asserted
three-colour boundary conclusion and the `3,2,2` colour-class sizes.
This proves item 2. \(\square\)

## 5. Exact stopping point

The direct topological allocation claim is stronger than what
seven-connectivity supplies.  Lemma 3 forces a six-fan, but that fan can
meet every possible `S`-full connected subgraph.  Theorem 4 converts a
tight failed choice into two order-seven cuts overlapping in the six-set
`A\cup B`; it
also removes the former singleton terminal case.  The remaining cases are:

1. the non-tight bridge case `|A|+|B|\ge7`; and
2. the tight nested `(1,1)` or connected-rich cut cases described above.

Closing either case still requires compatible proper-minor colouring
responses or an exchange between connected subgraphs.  No general
two-subgraph allocation theorem is claimed.

## Inputs

- [one-nonfull attachment reduction](hc7_k7minus_nonfull_attachment_reduction.md)
- [degree-seven neighbourhood classification](hc7_k7minus_degree7_clique_incidence.md)
- [seven exceptional vertices and degree defect](hc7_k7minus_seven_exceptional_vertices_corollary.md)
- [critical seven-cut capacity](hc7_k7minus_critical_seven_cut_capacity.md)
- [uniform defect-two connected-subgraph reflection](hc7_exact7_all_residual_defect2_carrier.md)
