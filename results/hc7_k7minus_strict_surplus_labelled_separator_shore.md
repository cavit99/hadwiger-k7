# A concentrated spanning `K_6` model yields a strict labelled separator shore

**Status:** written proof; separate internal audit in
[`hc7_k7minus_strict_surplus_labelled_separator_shore_audit.md`](hc7_k7minus_strict_surplus_labelled_separator_shore_audit.md).

This theorem advances the positive-surplus branch of the seven-connected
`4n-2` programme.  It converts concentration of seven prescribed neighbours
inside a spanning `K_6` model into a strictly smaller connected separator
side in the original graph, retaining the incident-edge labels and exact
coefficient-four accounting.  It does not eliminate positive surplus.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Canonical setting

Let `G` be a counterexample of minimum order and then minimum size to

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G,
\]

and suppose

\[
 q:=|E(G)|-(4|V(G)|-2)\ge1.
\]

By the
[canonical sparse six-boundary theorem](hc7_k7minus_strict_surplus_canonical_six_boundary.md),
there is a degree-seven vertex `x` such that, on putting

\[
 N=N_G(x),\qquad J=G-x,
\]

the following hold.

1. For each `y in N`, with
   \[
   T_y=N-\{y\},\qquad B_y=V(G)-(T_y\cup\{x\}),
   \]
   the set `B_y` is connected and
   \[
   (G-xy)-T_y=\{x\}\mathbin{\dot\cup}B_y.
   \]
   Every vertex of `T_y` is adjacent to both displayed components.
2. The graph `J` has a spanning `K_6`-minor model.
3. Every `K_6` model in `J` has at most four branch sets meeting any fixed
   set `T_y`.
4. If
   \[
   \delta_y=|E(G[B_y])|+|E_G(B_y,T_y)|-4|B_y|,
   \]
   then
   \[
   \delta_y=19+q-|E(G[T_y])|\ge9+q.
   \]

The seven sets `T_y` and shores `B_y` occur in the same graph; in particular,

\[
                         B_y=(V(G)-N[x])\cup\{y\}.       \tag{1.1}
\]

## 2. Splitting one multiply rooted branch set

### Lemma 1 (simultaneous four-branch-set bound)

In every spanning `K_6` model in `J`, the seven vertices of `N` lie in at
most four branch sets.

#### Proof

Suppose that `N` meets at least five branch sets.  Since seven vertices
occupy at most six branch sets, one branch set contains two of them.  Delete
one of these two vertices, say `y`.  The same branch set remains met by
`T_y=N-\{y\}`, so `T_y` still meets at least five branch sets.  This
contradicts item 3 of the canonical setting. \(\square\)

### Lemma 2 (completion after a connected split)

Let `D,Q_1,...,Q_5` be a spanning `K_6` model in `J`.  Call a branch set
**contacted** if it contains a vertex of `N`.  Suppose

\[
                         D=A\mathbin{\dot\cup}B,
\]

where `A,B` are nonempty connected sets, each contains a vertex of `N`, and
there is an `A-B` edge.  If every uncontacted `Q_i` is adjacent to both `A`
and `B`, then `G` contains a `K_7^-` minor.

#### Proof

Every `Q_i` is adjacent to at least one of `A,B`, because it is adjacent to
`D`.  Call it `A`-only, `B`-only, or crossing according as it is adjacent
only to `A`, only to `B`, or to both.  Every exclusive branch set is
contacted by hypothesis.  Lemma 1 permits at most four contacted branch
sets in the whole model, including `D`, so there are at most three exclusive
sets among `Q_1,...,Q_5`.  One of the two exclusive classes consequently
has order at most one.

Suppose, after interchanging `A,B` if necessary, that at most one `Q_i` is
`A`-only.  Use the seven branch sets

\[
                         A\cup\{x\},\quad B,\quad
                         Q_1,\ldots,Q_5.                 \tag{2.1}
\]

The first is connected because `A` contains a neighbour of `x`, and it is
adjacent to `B` because `B` also contains a neighbour of `x`.  It is
adjacent to every `Q_i`: adjacency to `A` supplies the edge unless `Q_i` is
`B`-only, in which case its vertex of `N` supplies an edge to `x`.  The set
`B` is adjacent to every `Q_i` except possibly the unique `A`-only set.
The five sets `Q_i` remain pairwise adjacent.  Thus (2.1) is a `K_7^-`
model. \(\square\)

### Lemma 3 (two one-root connected sides)

If a connected set `D` contains at least two vertices of `N`, then it has
disjoint connected subsets `C_1,C_2` such that, for `i=1,2`,

\[
 |C_i\cap N|=1,
 \qquad D-C_i\text{ is connected}.                     \tag{2.2}
\]

#### Proof

Take a spanning tree of `G[D]` and its minimal subtree containing `D\cap N`.
Every leaf of the latter subtree belongs to `N`.  Choose two leaves.  At
each leaf, delete its incident edge towards the rest of the minimal subtree
and take the leaf-side component of the spanning tree.  These two components
are disjoint, each contains exactly its selected root, and each has a
connected complement in the spanning tree.  The assertion follows.
\(\square\)

## 3. Strict labelled separator shore

### Theorem 4 (model concentration yields a strict separator shore)

For every spanning `K_6` model in `J`, there are branch sets `D,U`, a vertex
`y in N`, and a connected set `C` such that

\[
 C\subsetneq B_y,\qquad C\subseteq D,\qquad
 C\cap N=\{y\},                                        \tag{3.1}
\]

\[
 D-C\text{ is connected},\qquad E_G(C,U)=\varnothing,  \tag{3.2}
\]

where `U` is uncontacted.  Moreover,

\[
 N_G(x)\cap C=\{y\},                                   \tag{3.3}
\]

and `N_G(C)` is an actual vertex separator satisfying

\[
                         |N_G(C)|\ge7.                   \tag{3.4}
\]

#### Proof

Fix a spanning model.  Lemma 1 gives a branch set `D` containing at least
two vertices of `N`.  Apply Lemma 3 and obtain `C_1,C_2`.

If each `C_i` were adjacent to every uncontacted branch set other than `D`,
then the connected split

\[
                         D=C_1\mathbin{\dot\cup}(D-C_1)
\]

would satisfy Lemma 2: the second side contains `C_2`, so every uncontacted
branch set is adjacent to both sides.  This would give a `K_7^-` minor,
contrary to the choice of `G`.

Hence one `C_i`, call it `C`, is anticomplete to an uncontacted branch set
`U`.  Let `y` be the unique member of `C\cap N`.  Deleting `N_G(C)` leaves
the nonempty connected sets `C` and `U` in different components.  Thus
`N_G(C)` is an actual separator, and seven-connectivity gives (3.4).

Every vertex of `C-\{y\}` lies outside `N`, so (1.1) gives `C\subseteq B_y`.
The uncontacted set `U` contains no vertex of `N`, hence
`U\subseteq V(G)-N[x]\subseteq B_y`.  Since `U` is disjoint from `C`, the
containment in (3.1) is strict.  Finally, `x` is adjacent to `y` and to no
other vertex of `C`, proving (3.3). \(\square\)

The conclusion gives only the lower bound (3.4).  It does not assert that
`N_G(C)` is an exact order-seven cut or that `C` is another canonical
six-boundary shore.

## 4. Exact coefficient-four accounting

For a connected set `C`, put

\[
 k(C)=|N_G(C)|,
 \qquad
 \eta(C)=|E(G[C])|+|E_G(C,N_G(C))|-4|C|.               \tag{4.1}
\]

### Proposition 5 (shore and contraction identities)

For every `y in N`,

\[
 k(B_y)=7,
 \qquad
 \eta(B_y)=20+q-|E(G[T_y])|\ge q+10.                  \tag{4.2}
\]

Let `C` be supplied by Theorem 4.  Exactly one of the following numerical
alternatives holds.

1. The strict labelled separator shore is high:
   \[
                         \eta(C)>q+k(C)-4.              \tag{4.3}
   \]
2. It is contraction-eligible:
   \[
                         \eta(C)\le q+k(C)-4.           \tag{4.4}
   \]
   If `|C|>=2`, contracting `C` to the labelled vertex `y` gives a proper
   minor `G_C` satisfying
   \[
   |E(G_C)|-(4|V(G_C)|-2)
        =q+k(C)-4-\eta(C)\ge0.                          \tag{4.5}
   \]

#### Proof

The boundary of `B_y` in `G` is `T_y\cup\{x\}`, and `xy` is the only edge
from `x` to `B_y`.  Equation (4.2) follows from the canonical excess
identity after restoring this edge.

The alternatives (4.3) and (4.4) are complementary.  Contracting `C`
removes `|C|-1` vertices.  The

\[
 |E(G[C])|+|E_G(C,N_G(C))|=4|C|+\eta(C)
\]

internal and leaving edges are replaced by exactly `k(C)` edges from the
contracted vertex to `N_G(C)`.  Substitution in
`|E(G)|=4|V(G)|-2+q` gives (4.5). \(\square\)

The high alternative is a strict same-host localisation only.  Its boundary
may have order greater than seven, and no canonical internal-connectivity or
spanning-model property is inherited.

### Proposition 6 (failure of an eligible contraction)

Suppose `C` satisfies (4.4) and `|C|>=2`.  The graph `G_C` is not
seven-connected.  There are a set

\[
 Z\subseteq V(G)-C,\qquad |Z|\le5,                     \tag{4.6}
\]

and at least two components of `G-C-Z` such that every such component `A`
satisfies

\[
                         |N_G(A)\cap C|\ge7-|Z|.         \tag{4.7}
\]

If two components `A,B` can be separated in `G-Z` by a set
`K\subseteq C` of order `7-|Z|`, then `Z\cup K` is an actual order-seven
cut of `G`.

#### Proof

The minor `G_C` is target-free and satisfies the `4n-2` density threshold
by (4.5).  If it were seven-connected, it would be a smaller counterexample,
contrary to the choice of `G`.

Simplicity and (4.5) imply `|V(G_C)|>=9`, because
\(\binom n2<4n-2\) for `n<=8`.  Thus failure of seven-connectivity supplies
an actual cut `X` of `G_C` of order at most six.  Let `c` be the vertex
representing `C`.  The vertex `c` belongs to `X`; otherwise expanding `c`
back to the connected set `C` could not join two components of `G_C-X`, so
`X` would also be a cut of `G`.  Put `Z=X-\{c\}`.  Then (4.6) holds, and
`G-C-Z` is disconnected.

For each component `A` of this graph, all its external neighbours lie in
`C\cup Z`.  Seven-connectivity gives `|N_G(A)|>=7`, which proves (4.7).
If `K` has the stated property, then `Z\cup K` separates `A` from `B` in
`G` and has order seven. \(\square\)

One such exact cut need not cross another exact cut; the two may be nested.
If no separator `K` of the displayed order exists, further rooted linkage
information is required.  Neither case is closed here.

## 5. Scope

Theorem 4 is computation-free and unbounded.  It resolves the static
branch-set splitting question: failure to obtain five contacted `K_6`
branch sets now returns a strict, endpoint-labelled connected separator
side in the original graph, together with a branch set whose connected
remainder is retained and an uncontacted branch set anticomplete to that
side.

Three nonterminal cases remain.

1. The high shore (4.3) need not re-enter the canonical six-boundary
   theorem.
2. If `C=\{y\}`, then `N_G(C)=N_G(y)` has order `d_G(y)>=7`, but `d_G(y)=7`
   is not known; no proper whole-shore contraction is available.
3. A non-singleton eligible shore returns Proposition 6.  An exact local
   separator gives one, possibly nested, order-seven cut; otherwise a
   label-preserving rooted linkage argument is still needed.

Thus the result does not prove `q=0`, the seven-connected `4n-2` theorem,
Conjecture 21, or `HC_7`.
