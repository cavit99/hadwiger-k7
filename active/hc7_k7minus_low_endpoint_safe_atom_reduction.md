# Low-endpoint density-safe atoms

**Status:** active draft; written proof with a separate hash-pinned internal
audit.  This is a strict-surplus reduction, not a proof of the `4n-2`
extremal target.

Here `K_7^-` is `K_7` with one edge deleted.  Let `G` be a counterexample,
chosen first with minimum order and then with minimum size, to

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G,
\]

and suppose that its surplus

\[
 q=|E(G)|-(4|V(G)|-2)
\]

is positive.  Put

\[
 L=\{z:d_G(z)=7\},\qquad F=G-L.
\]

The audited strict-surplus theorem says that `G` is minimally
seven-connected and `G[F]` is a forest.  For an edge `ab`, write

\[
 c(ab)=|N(a)\cap N(b)|.
\]

Contracting `ab` changes the surplus by

\[
 q(G/ab)=q+3-c(ab).                                      \tag{1}
\]

Define the low-endpoint safe family

\[
 \mathcal Y=
 \bigl\{\{a,b\}:ab\in E(G),\ c(ab)\le q+3,
                         \ \min\{d(a),d(b)\}\le8\bigr\}. \tag{2}
\]

We use Mader's terminology.  A `\mathcal Y`-fragment is a fragment whose
minimum boundary contains a member of `\mathcal Y`, and a
`\mathcal Y`-atom is such a fragment of minimum order.

## 1. Low-endpoint criticality

### Theorem 1.1

The graph `G` is `\mathcal Y`-critically seven-connected.  Consequently,
every `\mathcal Y`-atom has order at most three.

#### Proof

Let `ab` be an edge represented in `\mathcal Y`.  If `G/ab` were
seven-connected, (1) would make it a smaller counterexample.  Thus `G/ab`
is not seven-connected.  The density hypothesis forces `|V(G)|\ge9`, so
`G/ab` has a cut of order at most six.  That cut contains the contracted
vertex, since otherwise it would also disconnect `G`.  Splitting the
contracted vertex back into `a,b` gives a cut of `G` of order at most seven;
seven-connectivity makes its order exactly seven.  It contains `a,b`, as
required by the first condition in Mader's definition.

Let `A` be a `\mathcal Y`-fragment and put `S=N(A)`.  If `A\cap L` is
nonempty, choose `z\in A\cap L`.  The audited degree-seven safe-contraction
theorem gives `s\in N(z)` with `c(zs)\le3`.  The edge `zs` belongs to
`\mathcal Y`, lies in `A\cup S`, and its certifying order-seven cut meets
`A` at `z`.

Suppose instead that `A\cap L` is empty.  Choose a component `C` of `G-S`
contained in `A` and a leaf `z` of the forest `G[C]`.  Every neighbour of
`z` lies in `C\cup S`, and hence

\[
 8\le d_G(z)\le1+|S|=8.
\]

Thus `z` has one neighbour `w` in `C` and is adjacent to every vertex of
`S`.  There are two or three components of `G-S`.  In the three-component
case, the audited seven-cut theorem gives `\Delta(G[S])\le3`.  In the
two-component case, `G[S]` is `K_5`-minor-free.  The audited seven-vertex
structure theorem then gives a vertex of boundary degree at most three,
unless `G[S]` is the pentagonal bipyramid.

The exception is impossible.  Contracting the two components of `G-S`
would give `I_2\vee B_5`.  If `p_0,p_1` are the nonadjacent poles, the
vertices `r_0,\ldots,r_4` form the rim in cyclic order, and `u,v` are the
two contracted components, then

\[
 \{p_0,r_4\},\ \{p_1\},\ \{r_0,u\},\
 \{r_1\},\ \{r_2\},\ \{r_3\},\ \{v\}
\]

are the branch sets of a `K_7^-` model; only the fourth and sixth displayed
sets may be nonadjacent.

We may therefore choose `s\in S` with `d_{G[S]}(s)\le3`.  Since
`N(z)=S\cup\{w\}`,

\[
 c(zs)=d_{G[S]}(s)+[sw\in E(G)]\le4\le q+3.          \tag{3}
\]

The edge `zs` belongs to `\mathcal Y`, lies in `A\cup S`, and has a
certifying cut meeting `A`.  This verifies the second condition in Mader's
definition.  Mader's generalised atom theorem now gives

\[
 |A|\le\frac{7}{2},
\]

so `|A|\le3`.  \(\square\)

## 2. Every low-endpoint atom meets the degree-seven set

### Theorem 2.1

Every `\mathcal Y`-atom contains a vertex of degree seven.

#### Proof

Let `A` be an atom and put `S=N(A)`.  Every component of `G-S` is adjacent
to every vertex of `S`.  Since `S` contains a member of `\mathcal Y`, each
component is itself a `\mathcal Y`-fragment.  Atom minimality implies that
`A` is one component and that every other component has order at least
`|A|`.

Suppose that `A\cap L` is empty.  The connected graph `G[A]` is contained
in the forest `G[F]`, and Theorem 1.1 leaves three possibilities.

If `A` is a singleton, its vertex has degree seven, a contradiction.  If
`G[A]=ab`, both ends have degree eight and are adjacent to all seven
vertices of `S`.  They therefore have seven common neighbours.  The
audited essential-edge theorem gives a six-vertex separator in `G-ab`
separating `a` from `b`; every common neighbour would have to lie in that
separator, which is impossible.

Finally let `G[A]=a-b-c`.  The leaves `a,c` are adjacent to every vertex of
`S`, while `b` has at least six neighbours in `S`.  Choose a four-set
`Q\subseteq N_S(b)` and `s\in S-Q`.  An opposite component has order at
least three.  The audited closed-shore lemma and Jørgensen's rooted-diamond
theorem give a `Q`-rooted `K_4^-` model `R_1,\ldots,R_4` in that opposite
closed shore.  The seven sets

\[
 \{a,s\},\quad\{b\},\quad\{c\},\quad R_1,R_2,R_3,R_4
\]

are connected and pairwise adjacent except for at most the missing pair in
the rooted diamond.  They form a `K_7^-` model, a contradiction.  Hence
`A\cap L\ne\varnothing`.  \(\square\)

## 3. The exact singleton reduction

### Theorem 3.1

Let `A=\{x\}` be a `\mathcal Y`-atom and put `S=N(x)`.  Then `d(x)=7`, and
there is an edge `uv` of `G[S]` such that

\[
 c(uv)\le q+3,\qquad d(u)\le8.                        \tag{4}
\]

Set

\[
 J=G-\{x,u\},\qquad T=S-\{u\}.
\]

Then

\[
 |T|=6,qquad \kappa(J)\ge5,qquad
 |E(J)|=4|V(J)|+q-d(u)\ge4|V(J)|-7.                 \tag{5}
\]

The rooted pair `(J,T)` is internally six-connected: it has no separation
`(A,B)` with

\[
 T\subseteq A,\qquad B-A\ne\varnothing,
 \qquad |A\cap B|\le5.                               \tag{6}
\]

Moreover, `J` has a spanning `K_6`-minor model.  In every spanning
`K_6`-minor model of `J`, at most four branch sets meet `T`.

#### Proof

Theorem 2.1 gives `d(x)=7`, so `S=N(x)` has order seven.  Since `A` is a
`\mathcal Y`-fragment, its boundary contains an edge represented in
`\mathcal Y`; label it `uv` so that `d(u)\le8`.  This proves (4).

Deleting two vertices from a seven-connected graph leaves a
five-connected graph, so `\kappa(J)\ge5`.  Since `xu` is an edge,

\[
\begin{aligned}
 |E(J)|
   &=|E(G)|-d(x)-d(u)+1\\
   &=4|V(J)|+q-d(u)\\
   &\ge4|V(J)|-7,
\end{aligned}
\]

which proves (5).

The graph `G-u` is six-connected.  If `(A,B)` were a separation as in
(6), then `(A\cup\{x\},B)` would be a separation of `G-u` of the same
order: every neighbour of `x` in `G-u` lies in `T\subseteq A`.  This
contradicts six-connectivity and proves the rooted assertion.

Norin and Totschnig's extremal theorem applies to the four-connected graph
`J`: its density is strictly above `4|V(J)|-8`, so the exceptional graph
`K_{2,2,2,2}`, which has exactly `4|V(J)|-8` edges, cannot occur.  Hence
`J` contains `K_7^\vee`, where `K_7^\vee` is obtained from `K_7` by deleting
two incident edges.

Enlarge such a model to a spanning one.  Write its branch sets as

\[
 P,B,C,U_1,U_2,U_3,U_4,
\]

with nominal missing pairs `PB` and `PC`.  Neither missing pair can become
adjacent while the model is enlarged, since one gained adjacency would
already give a `K_7^-` model.  Absorbing `P` into any `U_i` therefore gives
a spanning `K_6` model of `J`.

Let `\mathcal M` be any spanning `K_6` model in `J`.  If five of its bags
met `T`, adjoining the singleton bag `\{x\}` would give seven branch sets
with at most one missing adjacency: `x` is adjacent to every vertex of
`T`, and the six bags of `\mathcal M` are pairwise adjacent.  This would be
a `K_7^-` model.  Therefore at most four bags meet `T`.  \(\square\)

### Corollary 3.2 (joint contact restriction)

For a spanning `K_6` model `\mathcal M` in `J`, let `\Gamma_z(\mathcal M)`
be the set of its bags having a neighbour of `z` in `G`.  Then

\[
 |\Gamma_x(\mathcal M)|\le4,qquad
 |\Gamma_u(\mathcal M)|\le4.                         \tag{7}
\]

If `|\Gamma_x(\mathcal M)|=4`, then

\[
 \Gamma_u(\mathcal M)\subseteq\Gamma_x(\mathcal M). \tag{8}
\]

The symmetric assertion also holds; in particular, if both sets have
order four, they are equal.

#### Proof

The first inequality is Theorem 3.1, because `N_J(x)=T`.  Five bags seen
by `u`, together with `\{u\}`, would likewise give a `K_7^-` model, proving
the second.

Suppose that `x` sees exactly four bags and that `u` sees a fifth bag `D`.
Absorb `u` into `D`.  The six modified bags remain a `K_6` model, and the
edge `xu` makes the new bag adjacent to `\{x\}`.  The singleton `\{x\}`
now sees five bags, giving a `K_7^-` model.  This proves (8); symmetry gives
the remaining assertions.  \(\square\)

## 4. Exact nonclosure

Theorem 3.1 reduces a singleton atom to the following rooted statement:

> `J` has a `K_6`-minor model in which at least five branch sets meet the
> prescribed six-set `T`.

This statement would immediately contradict the last conclusion of the
theorem and close the singleton case.  Norin--Totschnig supplies an
unrooted spanning model, but it does not control how its bags meet `T`.
The internal six-connectivity of `(J,T)` and the density in (5) have not
yet been converted into the required rooted model.

There is also a specific crossing inference which must not be used.  The
boundary edge `uv` in (4) has a failed density-safe contraction, but its
certifying cut need not meet the atom.  Indeed, after contracting `uv`, the
six-vertex image of `S` already separates `x`.  Pulling it back gives the
original boundary `S`, not an order-seven cut containing `x,u`.  Mader's
atom crossing lemma applies only to a certifying separator which meets the
atom.  Low-endpoint criticality supplies such a separator for some safe
edge incident with `x`, but its other endpoint is not known to have degree
at most eight.  Consequently one may not combine the low degree of `u`
with a hypothetical cut of the form `\{x,u\}\cup Q`.  No component count,
excess identity, or crossed-miss analysis derived from that hypothetical
cut is established.

For orientation, connectivity and an unrooted `K_6` model alone are
insufficient.  The graph `K_3\vee C_5` is five-connected, contains a
`K_6` minor, and contains no `K_7^-` minor.  It has 23 edges on eight
vertices, however, which is only `4|V|-9`; it does not meet (5).  Thus the
remaining issue is genuinely the two-edge density margin together with the
six prescribed roots.

## Inputs and scope

The direct repository inputs are the audited results on strict-surplus
minimal enemies, degree-seven safe contractions, essential-edge
six-separations, seven-cut component capacity, seven-vertex
`K_5`-minor-free structure, and closed-shore rooted connectivity.

The generalised-fragment definitions and atom bound are due to W. Mader,
*Generalizations of critical connectivity of graphs*, Discrete Mathematics
**72** (1988), 267--283.  We use the formulation in M. Kriesell,
*Minimal Connectivity*, in *Topics in Structural Graph Theory* (2013),
Theorems 5.1 and 5.2.  Jørgensen's rooted-diamond theorem is used only in
Theorem 2.1.  The extremal input in Theorem 3.1 is Theorem 6 of S. Norin and
A. Totschnig, *Every graph with no `K_7^\vee`-minor is 6-colorable*,
arXiv:2507.03244.

All conclusions here require positive surplus.  They do not address a
minimum counterexample with `q=0`, do not eliminate the singleton atom,
and do not prove the `4n-2` extremal theorem.
