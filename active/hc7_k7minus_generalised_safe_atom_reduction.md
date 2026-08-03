# Density-safe atoms in a strict-surplus minimal counterexample

**Status:** active draft; written proof with a separate internal audit for this
revision.  This is a strict-surplus reduction, not a proof of the `4n-2`
extremal target.

Here `K_7^-` denotes `K_7` with one edge deleted.  Let `G` be a
counterexample of minimum order and then minimum size to

\[
 \kappa(G)\ge 7,\qquad |E(G)|\ge 4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G,
\]

and suppose

\[
 q=q(G):=|E(G)|-(4|V(G)|-2)\ge1.
\]

Put

\[
 L=\{v:d_G(v)=7\},\qquad F=G-L,
\]

so the audited strict-surplus theorem says that `G` is minimally
seven-connected and `F` is a forest.  For an edge `xy`, write

\[
 c(xy)=|N(x)\cap N(y)|,
 \qquad q(G/xy)=q+3-c(xy).                         \tag{1}
\]

Let

\[
 \mathcal X=\{\{x,y\}:xy\in E(G),\ c(xy)\le q+3\}. \tag{2}
\]

Thus `\mathcal X` is the family of all density-safe edges.  We use Mader's
standard terminology: an `\mathcal X`-fragment is a fragment whose
order-seven boundary contains a member of `\mathcal X`, and an
`\mathcal X`-atom is one of minimum order.

## 1. The generalised-criticality entrance

### Theorem 1.1

The graph `G` is `\mathcal X`-critically seven-connected.  Consequently,
every `\mathcal X`-atom has order at most three.

#### Proof

First let `xy` be density-safe.  If `G/xy` were seven-connected, then (1)
would make it a smaller counterexample.  Hence `G/xy` is not
seven-connected.  Pulling back a cut through the contracted vertex gives an
order-seven cut of `G` containing `x,y`.  This verifies the first condition
in Mader's definition.

Let `A` be an `\mathcal X`-fragment and put `S=N(A)`.  Suppose first that
`A\cap L` is nonempty, and choose `x\in A\cap L`.  The audited safe-incident
contraction theorem supplies an edge `xy` with `c(xy)\le3`.  Since `y` lies
in `A\cup S`, the order-seven cut containing `x,y` meets `A` and contains
this member of `\mathcal X` inside `A\cup S`.

It remains that `A\cap L` is empty.  Choose a component `C` of `G-S`
contained in `A` and a leaf `z` of the tree `G[C]`.  All neighbours of `z`
lie in `C\cup S`, so

\[
             8\le d_G(z)\le 1+|S|=8.
\]

Thus `z` has one neighbour in `C` and is adjacent to every vertex of `S`.
The seven-cut theorem gives two or three components of `G-S`.  In the
three-component case `\Delta(G[S])\le3`.  In the two-component case
`G[S]` is `K_5`-minor-free, so the seven-vertex structure theorem gives a
vertex of boundary degree at most three unless `G[S]` is the pentagonal
bipyramid.  The latter graph is impossible: contracting the two components
of `G-S` gives `I_2\vee B_5`, and the seven sets

\[
 \{p_0,r_4\},\ \{p_1\},\ \{r_0,u\},\
 \{r_1\},\ \{r_2\},\ \{r_3\},\ \{v\}
\]

form a `K_7^-` model, where `p_0,p_1` are the two poles, the `r_i` are the
rim in cyclic order, and `u,v` are the two contracted components.

We may therefore choose `s\in S` with `d_{G[S]}(s)\le3`.  If `w` is the
unique neighbour of `z` in `C`, then

\[
 c(zs)=d_{G[S]}(s)+[sw\in E(G)]\le4\le q+3.          \tag{3}
\]

The edge `zs` is density-safe.  Its order-seven cut contains `z\in A` and
`s\in S`, so it supplies the second condition in Mader's definition.
Thus `G` is `\mathcal X`-critical.  Mader's generalised atom theorem now
gives

\[
                  |A|\le\frac12\kappa(G)=\frac72,
\]

and hence `|A|\le3`.  \(\square\)

## 2. Every atom contains a degree-seven vertex

### Theorem 2.1

Every `\mathcal X`-atom meets `L`.

#### Proof

Let `A` be an atom and put `S=N(A)`.  Seven-connectivity makes every
component of `G-S` adjacent to every vertex of `S`.  Since `S` contains a
density-safe edge, each such component is itself an `\mathcal X`-fragment.
It follows from minimality that `A` is one component and that every other
component has order at least `|A|`.

Suppose that `A\cap L` is empty.  Since `G[A]` is a connected subgraph of
the forest `F`, Theorem 1.1 leaves three cases.

If `|A|=1`, its unique vertex has degree seven, a contradiction.

If `A=\{a,b\}` with edge `ab`, both vertices have degree eight and are
adjacent to all seven vertices of `S`.  Hence `a,b` have seven common
neighbours.  The audited essential-edge theorem gives a six-separator of
`G-ab` separating `a` from `b`.  Every common neighbour must belong to that
separator, which is impossible.

Finally suppose `G[A]=a-b-c`.  The leaves `a,c` are adjacent to all of
`S`, while `b` has at least six neighbours in `S`.  Choose a four-set
`Q\subseteq N_S(b)` and `s\in S-Q`.  The complementary fragment
`\widetilde A=V(G)-(A\cup S)` has order at least three.  The closed-shore
rooted-connectivity lemma and Jørgensen's rooted-diamond theorem give a
`Q`-rooted `K_4^-` model `R_1,\ldots,R_4` in
`G[\widetilde A\cup Q]`.  The seven branch sets

\[
              \{a,s\},\quad\{b\},\quad\{c\},
              \quad R_1,R_2,R_3,R_4                 \tag{4}
\]

are connected and pairwise adjacent except for at most the one missing
adjacency among the rooted bags.  Indeed, `a,c` see every boundary vertex,
`b` sees every root in `Q`, the edges `ab,bc` join the three path-derived
bags, and `sc` joins the first path-derived bag to the third.  Thus (4) is a
`K_7^-` model, again a contradiction.  \(\square\)

## 3. A nonsingleton atom cannot have three opposite components

### Theorem 3.1

Let `A` be an `\mathcal X`-atom with `2\le |A|\le3`, and put `S=N(A)`.
Then `G-S` has exactly two components.

#### Proof

Suppose that `G-S` has three components `A,B,C`.  Both `B` and `C` have
order at least `|A|`, by atom minimality.  Consequently the rooted-diamond
theorem is available in `G[B\cup Q]` for every four-set `Q\subseteq S`.

We use the following elementary completion.  If
`A=A_1\mathbin{\dot\cup}A_2`, where `A_1,A_2` are connected and adjacent,
and at least five vertices of `S` have a neighbour in each of `A_1,A_2`,
choose four of them as `Q` and a fifth as `s`.  Let
`R_1,\ldots,R_4` be a `Q`-rooted `K_4^-` model in `G[B\cup Q]`.  Then

\[
       A_1,\quad A_2,\quad C\cup\{s\},
       \quad R_1,R_2,R_3,R_4                         \tag{5}
\]

is a `K_7^-` model.  Full attachment of `C` supplies all contacts from its
bag to the rooted bags, and `s` supplies its contacts to `A_1,A_2`.

If `|A|=2`, its two vertices have at least five common neighbours in `S`:
a degree-seven endpoint misses one boundary vertex, and the other endpoint
misses at most one.  Thus (5) applies.

Suppose next that `G[A]=a-b-c`.  For `x\in A`, put
`M_x=S-N_S(x)`.  A leaf has `|M_x|\le1`; the middle vertex has
`|M_b|\le2`.  For the split `\{a\}\mathbin{\dot\cup}\{b,c\}`, the set of
boundary vertices missing one of the two sides is

\[
                         M_a\cup(M_b\cap M_c),
\]

which has order at most two.  Again (5) applies.

It remains that `G[A]` is a triangle.  Write its vertices as `a_1,a_2,a_3`;
then `|M_{a_i}|\le2`.  If at least four boundary vertices see all three
vertices, take them as `Q`.  A `Q`-rooted diamond in `B`, together with the
three singleton triangle bags, is a `K_7^-` model.

Otherwise, some singleton-versus-edge split has at least five common
boundary neighbours.  To see this, suppose the contrary.  For each
`\{i,j,k\}=\{1,2,3\}` one could choose

\[
 x_i\in(M_{a_j}\cap M_{a_k})-M_{a_i}.
\]

The three `x_i` are distinct, and the bounds `|M_{a_i}|\le2` force

\[
 M_{a_1}=\{x_2,x_3\},\quad
 M_{a_2}=\{x_1,x_3\},\quad
 M_{a_3}=\{x_1,x_2\}.
\]

Their union then has order three, leaving four boundary vertices adjacent
to all three triangle vertices, contrary to the present case.  Hence (5)
applies to a singleton-versus-edge split and completes the proof.
\(\square\)

## 4. Exact residue and the sparse-family nonclosure

For `q\ge1`, the preceding theorems leave only the following
`\mathcal X`-atoms:

1. a singleton degree-seven vertex; or
2. an edge, a three-vertex path, or a triangle which meets `L` and is one
   component behind an order-seven cut with exactly one opposite component.

For an edge, each degree-seven endpoint misses exactly one boundary vertex
and each higher-degree endpoint is boundary-full.  For a path, a
degree-seven leaf misses one boundary vertex and a degree-seven middle
vertex misses two; higher-degree leaves are boundary-full and a
higher-degree middle vertex misses at most one.  For a triangle, a
degree-seven vertex misses two boundary vertices and a higher-degree vertex
misses at most one.  No finite triangle classification is used here.

The separately retained four-distinct-miss `P_3` theorem removes one complete
path case by an operation-preserving, computer-assisted boundary lemma.  It
does not remove the singleton, edge, triangle, or remaining path cases.

A tempting sparsification does **not** follow from this proof.  Let
`\mathcal R` contain one selected edge of common-neighbour count at most
three incident with each degree-seven vertex.  Although every member of
`\mathcal R` lies in an order-seven cut and `\mathcal R` covers `L`, it is
not established that `G` is `\mathcal R`-critical.  If an
`\mathcal R`-fragment `D` is disjoint from `L`, the leaf argument in
Theorem 1.1 produces the crossing density-safe edge `zs`, but generally
neither endpoint has degree seven and `zs` need not belong to
`\mathcal R`.  The selected edge already lying in `N(D)` may have a
certifying cut equal to `N(D)` or otherwise disjoint from `D`.  No present
hypothesis forces one of its certifying cuts to meet `D`.

Thus replacing `\mathcal X` by the sparse family `\mathcal R` before
applying Mader's atom theorem is an unsupported inference.  This does not
refute the existence of a more carefully coupled sparse family; it identifies
the exact additional statement such a route would need.

## External inputs

The generalised-fragment definitions and atom bound are due to W. Mader,
*Generalizations of critical connectivity of graphs*, Discrete Mathematics
**72** (1988), 267--283.  We use them in the formulation of M. Kriesell,
*Minimal Connectivity*, in *Topics in Structural Graph Theory* (2013),
Theorems 5.1 and 5.2.  The equivalent explicit definitions are also recorded
in T. L. Chan, *Contractible edges*, doctoral dissertation, University of
Hamburg (2016), Section 7.2 and Lemma 7.7.

The other direct inputs are the adjacent audited repository results on
strict-surplus minimal counterexamples, density-safe degree-seven
contractions, essential-edge six-separations, seven-cut component capacity,
seven-vertex `K_5`-minor-free structure, closed-shore rooted connectivity,
and Jørgensen's rooted `K_4^-` theorem.
