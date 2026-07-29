# Exact degree-seven neighbourhoods under `K_7^-` exclusion

**Status:** written proof; separate internal audit GREEN for this revision.
This is a theorem about the proposed `K_7^-` intermediate conjecture.  It
does not prove that conjecture or `HC_7`.

Here `K_7^-` denotes `K_7` with one edge deleted.

## Theorem 1 (uniform rooted `K_5`)

Let `G` be a seven-connected graph with

\[
 \chi(G)=7,
 \qquad
 \text{every proper minor of `G` six-colourable},
 \qquad
 K_7^-\npreccurlyeq G.
\]

Let `v` have degree seven, put `H=G[N(v)]`, and let `ab` be any nonedge of
`H`.  If

\[
                              U=N(v)-\{a,b\},
\]

then `G-v-\{a,b\}` contains a `U`-rooted `K_5` minor: there are pairwise
disjoint, connected, pairwise adjacent branch sets

\[
                              (B_x:x\in U)
\]

with `x\in B_x` for every `x\in U`.

### Proof

Contract the two edges `va` and `vb` to one vertex.  This is a proper minor,
so it has a six-colouring.  Expanding the contracted vertex and then
deleting `v` gives a six-colouring `phi` of `G-v` in which `a` and `b` have
one common colour, say `0`.  Every vertex of `U` avoids colour `0`.

The five vertices of `U` use the other five colours distinctly.  Otherwise
some colour would be absent from `N(v)`, and assigning that colour to `v`
would extend `phi` to a six-colouring of `G`.

Put `F=\overline H`.  Dirac's contraction-critical neighbourhood inequality
gives

\[
                              \alpha(H)\le2,             \tag{1}
\]

so `F` is triangle-free.  Let `xy` be an edge of `F[U]`, and let the colours
of `x,y` be `i,j`.  The vertices `x,y` lie in the same component of the
subgraph of `G-v` induced by colours `i,j`.  If not, interchange `i,j` on
the component containing `x`.  Since `U` was rainbow, colour `i` would then
be absent from `N(v)` and could be assigned to `v`, again six-colouring
`G`.

Delete the colour-`0` class from `G-v`, and call the resulting five-coloured
graph `J`.  The set `U` is a transversal of its five colour classes, and
every edge of `F[U]` has its ends in one corresponding bichromatic component
of `J`.  Since `F[U]` is a triangle-free graph on five vertices, Mantel's
theorem gives

\[
                              |E(F[U])|\le6.             \tag{2}
\]

Kriesell--Mohr's Theorem 7 says that every graph on five vertices with at
most six edges has property `(*)`.  Applied to the demand graph `F[U]` and
the fixed colouring of `J`, it gives five pairwise disjoint connected
branch sets rooted at `U`, adjacent for every edge of `F[U]`.  For every
other pair of roots, the literal edge of `H[U]` joins the corresponding two
branch sets.
Thus all ten branch-set adjacencies are present, and these branch sets form
the required `U`-rooted `K_5` model in `G-v-\{a,b\}`.  \(\square\)

## Theorem 2 (exact neighbourhood classification)

Under the hypotheses of Theorem 1, every degree-seven vertex `v` has

\[
 G[N(v)]\cong
 K_4\mathbin{\dot\cup}K_3
 \quad\text{or}\quad
 K_1\vee(K_3\mathbin{\dot\cup}K_3).                  \tag{3}
\]

Consequently, `v` lies in a literal `K_5`.  In the first case it lies in
exactly one literal `K_5`.  In the second it lies in exactly two, and those
two cliques meet in `v` and the universal vertex of `G[N(v)]`.

### Proof

Again put `H=G[N(v)]` and `F=\overline H`.  By (1), `F` is triangle-free.
It is nonempty, since otherwise `G[N[v]]` would be a literal `K_8` and hence
contain a `K_7^-` minor.

We claim that every nonisolated vertex of `F` has degree at least three.
Let `a` be nonisolated and choose a neighbour `b` in `F`.  Theorem 1 gives
a rooted `K_5` model `(B_x:x\in U)` for
`U=N(v)-\{a,b\}`.

If `d_F(a)=1`, then `a` is adjacent in `H` to every vertex of `U`.  Hence

\[
                         \{v\},\quad \{a\},\quad(B_x:x\in U)
\]

are seven pairwise adjacent branch sets and give a `K_7` minor, a
contradiction.

Suppose instead that `d_F(a)=2`, with neighbours `b,x`.  Triangle-freeness
gives `bx\in E(H)`.  In the rooted model for the edge `ab`, replace `B_x`
by the connected branch set

\[
                              D=\{b\}\cup B_x.
\]

The seven branch sets

\[
                    \{v\},\quad\{a\},\quad D,
                    \quad(B_y:y\in U-\{x\})
\]

have every required adjacency except possibly the one between `\{a\}` and
`D`.  They therefore give a `K_7^-` minor, or a `K_7` minor if that last
adjacency is also present.  This is again impossible, proving the claim.

Every nontrivial component of `F` consequently has minimum degree at least
three.  Such a triangle-free component has at least six vertices: for four
or five vertices its degree lower bound contradicts Mantel's theorem.
Since `F` has seven vertices, it has one nontrivial component `C`, of order
six or seven, and at most one isolated vertex.

If `|V(C)|=6`, then minimum degree three and Mantel's theorem give exactly
nine edges.  Equality in Mantel's theorem yields `C\cong K_{3,3}`, so

\[
                              F\cong K_{3,3}\mathbin{\dot\cup}K_1.
\]

Now suppose `|V(C)|=7`.  No vertex of `F` has degree at least five.  Indeed,
the neighbourhood of such a vertex is independent, and one of its
neighbours would then have degree at most two.  Thus every degree is three
or four.  The degree sum is even, so some vertex `z` has degree four.
Its four neighbours are independent.  Each must be adjacent to both of the
two vertices outside `N_F[z]` in order to have degree at least three, and
triangle-freeness forbids an edge between those two vertices.  Therefore

\[
                              F\cong K_{3,4}.
\]

Taking complements gives exactly (3).  The stated literal `K_5` incidence
is immediate from the `K_4`s in the two displayed neighbourhoods.  \(\square\)

## Dependencies and scope

The local input is Dirac's contraction-critical neighbourhood inequality,
in the modern form recorded as Lemma 1.6(i) by Michael Rolek and Zi-Xia
Song, [*Coloring graphs with forbidden minors*](https://arxiv.org/abs/1606.05507).
The rooted-minor conversion is Matthias Kriesell and Samuel Mohr,
[*Kempe Chains and Rooted Minors*](https://arxiv.org/abs/1911.09998),
Theorem 7: every graph on five vertices with at most six edges has property
`(*)`.  Mantel's theorem, including its equality case, supplies the two
elementary triangle-free edge bounds.

No finite census, anti-neighbourhood connectivity theorem, aligned
near-`K_7` theorem, or exterior-component classification is a logical
dependency.  The seven-connectivity hypothesis is retained to match the
critical-host application; the proof itself uses only the displayed
chromatic criticality and `K_7^-` exclusion.
