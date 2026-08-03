# A density-preserving contraction at a degree-seven vertex

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.  For a graph `G` of
order `n`, put

\[
                         q(G)=|E(G)|-(4n-2).
\]

## Theorem 1 (safe incident contraction)

Let `G` be a seven-connected `K_7^-`-minor-free graph with `q(G)>=0`,
and let `v` be a vertex of degree seven.  Then some neighbour `s` of `v`
satisfies

\[
                 d_{G[N(v)]}(s)\le3.                   \tag{1}
\]

Consequently

\[
                    q(G/vs)=q(G)+3-d_{G[N(v)]}(s)\ge q(G). \tag{2}
\]

If `G-N[v]` has two components, then every neighbour `s` satisfies
`d_{G[N(v)]}(s)<=3`, and at least one satisfies
`d_{G[N(v)]}(s)<=2`.

### Proof

Put `S=N(v)`.  The density hypothesis is impossible at order eight, since
`4(8)-2>\binom82`; hence `|V(G)|>=9`.  Thus `V(G)-N[v]` is nonempty and
`S` is an order-seven vertex cut.  Every component of `G-S` is adjacent
to every vertex of `S`, by seven-connectivity.  The
[three-component seven-cut theorem](hc7_k7minus_seven_cut_three_component_bound.md)
therefore gives

\[
                    2\le \#\operatorname{comp}(G-S)\le3. \tag{3}
\]

Suppose first that `G-S` has three components.  The same theorem gives
`Delta(G[S])<=3`, so every `s\in S` satisfies (1).  The audited
[seven-boundary capacity theorem](hc7_k7minus_seven_boundary_component_descent.md)
also gives `|E(G[S])|<=9`; averaging the boundary degrees therefore gives
one `s` with `d_{G[S]}(s)<=2`.

It remains to consider the case in which `G-S` consists of `{v}` and one
other component `C`.  The
[seven-boundary capacity theorem](hc7_k7minus_seven_boundary_component_descent.md)
implies that `G[S]` has no `K_5` minor.  The audited
[seven-vertex structure theorem](hc7_seven_column_contact_structure.md)
now says that either `G[S]` has a vertex of degree at most three or
`G[S]` is the pentagonal bipyramid

\[
                         B_5=\overline{K_2\mathbin{\dot\cup}C_5}. \tag{4}
\]

The first outcome supplies the required vertex.  We show that the remaining
possibility `G[S]\cong B_5` is impossible.

Contract `C` to one vertex `c`.  Full attachment to `S` means that the
resulting minor contains `I_2\vee B_5`, where the two independent vertices
are `v` and `c`.  Label the nonadjacent poles of `B_5` by `p_0,p_1` and
its rim in cyclic order by `r_0,r_1,r_2,r_3,r_4`.  The seven sets

\[
 \{p_0,r_4\},\quad \{p_1\},\quad \{r_0,v\},\quad
 \{r_1\},\quad \{r_2\},\quad \{r_3\},\quad \{c\}       \tag{5}
\]

are disjoint and connected.  Every two are adjacent except possibly
`{r_1}` and `{r_3}`.  They are therefore an explicit `K_7^-`-minor model,
a contradiction.  This proves (1).

Contracting `vs` removes the edge `vs` and one duplicate edge for each
common neighbour of `v` and `s`.  Those common neighbours are exactly the
`d_{G[S]}(s)` neighbours of `s` in `S`.  Thus

\[
 |E(G/vs)|=|E(G)|-1-d_{G[S]}(s),
\]

which gives (2).  \(\square\)

## Corollary 2 (exact seven-cut returned by a minimal enemy)

Suppose that `G` is chosen first with minimum order and then with minimum
size among the counterexamples to

\[
 \kappa(G)\ge7,\qquad |E(G)|\ge4|V(G)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq G.       \tag{6}
\]

Then `G` has a degree-seven vertex `v`.  For the neighbour `s` supplied by
Theorem 1, the graph `G/vs` is not seven-connected.  Moreover, there is a
five-set `W` such that

\[
                          T=\{v,s\}\cup W              \tag{7}
\]

is an order-seven vertex cut of `G`.  Every component of `G-T` contains a
vertex of `N(v)-T`; in particular, `G-T` has at most three components.  If
it has three, then `Delta(G[T])<=3`.

If `G-N[v]` has two components `A,B`, the edge `vs` may be chosen
arbitrarily and every cut `T` returned as above meets both `A` and `B`.
Writing

\[
                         a=|T\cap N(v)|,
\]

one has `a<=4`, and `a<=3` if `G-T` has three components.

### Proof

If `q(G)=0`, then the average degree of `G` is less than eight, while
seven-connectivity gives minimum degree at least seven.  Hence `G` has a
degree-seven vertex.  If `q(G)>0`, deleting any edge would leave the
density in (6).  The minimal choice of `G` therefore makes it
edge-minimal seven-connected.  Halin's theorem then supplies a vertex of
degree seven.

Apply Theorem 1 at such a vertex `v`.  If `G/vs` were seven-connected,
(2) and minor-minimality would make it a smaller counterexample to (6).
Thus `G/vs` is not seven-connected.

Let `z` be the vertex obtained by contracting `vs`, and choose a cut `X`
of `G/vs` with `|X|<=6`.  The vertex `z` belongs to `X`, since otherwise
`X` would also be a cut of `G`.  Pulling the cut back gives

\[
                  (X-\{z\})\cup\{v,s\}
\]

as a cut of `G`.  Seven-connectivity forces this set to have order seven,
so `|X|=6` and (7) holds with `W=X-\{z\}`.

Let `D` be a component of `G-T`.  If `D` contained no vertex of
`N(v)-T`, then `v` would have no neighbour in `D`, and `N_G(D)` would be
contained in the six-set `T-\{v\}`.  This contradicts
seven-connectivity.  Thus every component contains a surviving neighbour
of `v`.  The remaining assertions about the number of components and the
subcubic boundary follow from the three-component seven-cut theorem.

Finally suppose that `G-N[v]` has two components `A,B`.  In this case
Theorem 1 showed that every incident contraction is density-preserving,
so `s` is arbitrary.  If, say, `T` missed `A`, then the connected set `A`
would remain and, by full attachment to `N(v)`, would lie in one component
of `G-T` together with every vertex of `N(v)-T`.  Since every component of
`G-T` contains such a vertex, `G-T` would be connected, a contradiction.
Thus `T` meets both `A` and `B`.  Besides `v`, the cut `T` has six
vertices, at least one in each of `A,B`, so `a<=4`.  If `G-T` has three
components, then

\[
                   a=d_{G[T]}(v)\le3,
\]

as required.  \(\square\)

## Scope

The theorem does not prove (6).  It replaces every degree-seven vertex in
a minimal enemy by a density-preserving failed contraction and an exact
order-seven cut.  In the two-exterior-component case, the cut necessarily
uses vertices of both exterior components; the only seven-vertex
`K_5`-minor-free obstruction to a low-degree boundary vertex is eliminated
by the explicit model (5).

The external input in Corollary 2 is Halin's theorem that a finite
`k`-connected graph either has a vertex of degree `k` or has an edge whose
deletion preserves `k`-connectivity: R. Halin, *A theorem on n-connected
graphs*, J. Combin. Theory **7** (1969), 150--154.

## Theorem 3 (the exact two-exterior fragment residue)

Retain the minimal-enemy hypotheses of Corollary 2.  Suppose that a
degree-seven vertex `v` has

\[
                         G-N[v]=A\mathbin{\dot\cup}B,  \tag{8}
\]

where `A,B` are the two components.  Put `H=G-v` and `S=N(v)`.  Then
`H` is `S`-locally `(6,1)`-critical in the following exact sense:

\[
 \kappa(H)=6,\qquad \kappa(H-s)=5\quad(s\in S),       \tag{9}
\]

and every fragment of `H-X` meets `S-X` whenever `X\subseteq S` and
`|X|<=1`.

Consequently there are `t\in S` and a connected fragment `F` of `H` such
that

\[
                         F\cap S=\{t\}.               \tag{10}
\]

Writing `Q=N_H(F)`, one has `|Q|=6`, and both

\[
                         Q\cup\{v\},\qquad Q\cup\{t\} \tag{11}
\]

are order-seven vertex cuts of `G`, unless `F=\{t\}`.  In that exceptional
case `t` is itself a degree-seven vertex adjacent to `v`.

More precisely, if `F\ne\{t\}`, every component `K` of `F-t` satisfies

\[
                         N_G(K)=Q\cup\{t\}.            \tag{12}
\]

There are at most two such components.  If deleting `Q\cup\{t\}` leaves
three components in total, then `G[Q\cup\{t\}]` is subcubic.

### Proof

Theorem 1 makes every edge `vs`, `s\in S`, density-preserving in the
two-exterior case.  Minimality therefore makes every such edge
noncontractible.  Since deleting one vertex from a seven-connected graph
leaves a six-connected graph, `H` is at least six-connected.  A failed
contraction of `vs` is witnessed by an order-seven cut containing `v,s`;
after deleting `v`, this is a five-cut of `H-s`.  Hence
`κ(H-s)=5`.  It follows that `\kappa(H)=6`, since a seven-connected
`H` would leave `H-s` six-connected.

Let `X` be empty or `{s}` with `s\in S`, and let `D` be a fragment of
`H-X`.  If `D` missed `S-X`, then `v` would have no neighbour in `D`, and

\[
 N_G(D)\subseteq
 \begin{cases}
 N_H(D),&X=\varnothing,\\
 N_{H-s}(D)\cup\{s\},&X=\{s\}.
 \end{cases}
\]

The right-hand side has order at most six, contrary to
seven-connectivity.  This proves the local criticality assertion.

Yuan's fragment theorem for a noncomplete `W`-locally `(n,1)`-critical
graph gives four fragments `F_1,F_2,F_3,F_4` of `H` for which the sets
`F_i\cap S` are nonempty and pairwise disjoint.  Since `|S|=7`, one of
these intersections is a singleton.  Choose that fragment as `F` and
write the singleton as `{t}`.

Let `Q=N_H(F)`, so `|Q|=6`.  Every component of `H-Q` contained in `F`
has neighbourhood exactly `Q`: a smaller neighbourhood would contradict
six-connectivity.  It is therefore itself a fragment and must meet `S`.
Equation (10) permits only one such component, so `F` is connected.
The set `Q\cup\{v\}` is an order-seven cut of `G`.

If `F={t}`, then `N_H(t)=Q`, and the additional edge `tv` gives
`d_G(t)=7`.  Suppose instead that `F-t` is nonempty, and let `K` be one
of its components.  Since `F` is a component of `H-Q`, and since `K`
contains no vertex of `S`,

\[
                         N_G(K)\subseteq Q\cup\{t\}.
\]

The set on the right has order seven.  Seven-connectivity forces equality,
which proves (12).  Thus `Q\cup\{t\}` is an order-seven cut.  The
three-component seven-cut theorem shows that its deletion leaves at most
three components and gives the subcubic conclusion in the three-component
case.  Since at least one component lies outside `F`, there can be at most
two components of `F-t`.  \(\square\)

The fragment input used here is X. Yuan, *A note on fragments in a locally
`k`-critical `n`-connected graph*, Ars Combin. **93** (2009), 25--31:
every noncomplete `W`-locally `1`-critical `n`-connected graph has four
fragments whose intersections with `W` are pairwise disjoint.

Theorem 3 is an exact residue, not a closure.  The unsupported next
inference would be that the root-only fragment `F` must be `{t}` or that
one of the two cuts in (11) yields a contractible edge.  Neither follows
from fragment uncrossing or from the present seven-cut theorem.  A proof
of the extremal target must eliminate the nested root-swap configuration
(11)--(12), or use its component interiors to construct the minor.
