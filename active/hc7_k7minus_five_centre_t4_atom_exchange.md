# The four-root equality-shore residue: atom and exchange reduction

**Status:** written derivation; separate internal audit GREEN in
[`hc7_k7minus_five_centre_t4_atom_exchange_audit.md`](hc7_k7minus_five_centre_t4_atom_exchange_audit.md).
This note gives an exact unbounded trichotomy for the minimal four-root row
of the five-centre two-cut attack.  It does not eliminate the three final
outcomes in Theorem 4.1.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and hypotheses of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus `C` is the equal-response component, `D` is the distinct-response
component, `Z` is the independent set of five degree-eight centres, and

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad pq\notin E(G).
\]

For `z\in Z`, put

\[
 c_z=|N_C(z)|,\qquad d_z=|N_D(z)|,
 \qquad \rho_z=|N_{\{p,q\}}(z)|,
\tag{1.1}
\]

so that

\[
                         c_z+d_z+\rho_z=8.           \tag{1.2}
\]

Assume the no-singleton-contact branch

\[
                         c_z,d_z\ge2\quad(z\in Z),  \tag{1.3}
\]

and assume that no inclusion-minimal infeasible root set has order at most
three.  The latter is the input supplied, in this branch, by the pair
feasibility argument and the
[three-root palette closure](hc7_k7minus_five_centre_t3_palette_gluing.md).
The audited exceptional-neighbourhood theorem gives
`\alpha(G[N(z)])=3` for every centre `z`, while the critical host's literal
`K_5` exclusion makes each `G[N(z)]` `K_4`-free.

Write

\[
 \begin{aligned}
 c&=|C|,&m&=e(C),&h&=e(C,\{p,q\}),\\
 g&=\sum_{v\in C}(d_G(v)-8),&
 s&=6c+1-\left(m+h+\sum_{z\in Z}c_z\right),&
 \xi&=g+h-8.
 \end{aligned}                                      \tag{1.4}
\]

The full five-root Du--Li--Xie--Yu bound and the degree sum on `C`
give

\[
 m=2c-1+s+g,
 \qquad
 \sum_{z\in Z}c_z=4c-6-2s-\xi.                    \tag{1.5}
\]

Suppose `T=Z-\{r\}` is an inclusion-minimal infeasible root set of order
four.  Define its restricted slack by

\[
 \sigma_r=5c+1-\left(m+h+\sum_{z\in T}c_z\right).
\tag{1.6}
\]

The restricted four-root density bound gives `sigma_r\ge0`.

## 2. Exchange between four-root circuits

### Lemma 2.1 (exact slack exchange)

For every `j\in Z` for which `Z-\{j\}` is infeasible, that four-set is
inclusion-minimal and

\[
             \sigma_j=s-c+c_j.                       \tag{2.1}
\]

In particular, if

\[
                            a=c-s,                    \tag{2.2}
\]

then

\[
                            \sigma_j=c_j-a.            \tag{2.3}
\]

Moreover, in a surviving counterexample,

\[
 c_j\le3\quad\Longrightarrow\quad Z-\{j\}
 \text{ is infeasible}.                              \tag{2.4}
\]

#### Proof

Every triple is feasible by the standing assumption, so an infeasible
four-set is inclusion-minimal.  Subtracting its four-root bound (1.6) from
the full five-root bound in (1.4) gives

\[
 s=(c-7)+(7-c_j)+\sigma_j=c-c_j+\sigma_j,
\]

which is (2.1)--(2.3).

For (2.4), suppose `Z-\{j\}` were feasible.  The equal-response transfer
lemma in
[the four-root palette note](hc7_k7minus_five_centre_four_root_transfer.md)
produces a proper six-colouring of the closed `D`-side in which
`Z-\{j\}` is monochromatic, `p,q` have one common different colour, and
`j` avoids the pole colour.  Align the two fixed block colours with the
permitted equal-response colouring of the `C`-side.  The only unglued
edges are the `c_j` edges from `j` to `C`.  Their `C`-ends avoid the root
colour, while the colour of `j` is either that safe root colour or one of
four freely permutable colours.  At most three contacts cannot use all
four free colours.  A permutation therefore glues the two colourings and
six-colours `G`, a contradiction.  \(\square\)

Thus the four-root circuits are not independent scalar choices: the slack
of every bad omission is its contact number minus the one common integer
`a`.

## 3. The exact atom identity behind a four-root circuit

The next lemma follows the constructive proof of Du--Li--Xie--Yu,
Theorem 1.2, rather than only its stated edge inequality.  The bookkeeping
is included because the atom identity is not part of the theorem statement.

### Lemma 3.1 (four-root atom identity)

Fix `z\in T`.  There are an induced `p`--`q` path `P_z` in

\[
                    G[C\cup(T-\{z\})\cup\{p,q\}]
\]

and a component `L_z` after deleting `P_z` which contains `z` after the
literal vertex `z` is restored, with the following properties.  Put

\[
 r_z=|L_z\cap C|,
 \qquad
 U_z=N_{G[C\cup T\cup\{p,q\}]}(L_z)-\{p,q\},
 \qquad k_z=|U_z|.
\tag{3.1}
\]

Then `U_z\subseteq V(P_z)\cap C`.  There are nonnegative integers
`delta_{pl,z},delta_{crit,z}` such that

\[
            \boxed{\ \sigma_r
              =2r_z+\delta_{\mathrm{pl},z}
                    +\delta_{\mathrm{crit},z}.\ }    \tag{3.2}
\]

Here `delta_{pl,z}` is the deficit in the planar atom bound

\[
 e(A_z^+)\le3v(A_z)-7-2k_z,                           \tag{3.3}
\]

where `A_z` has vertex set `L_z\cup U_z\cup\{p,q\}` and only the edges
incident with `L_z`, and `A_z^+` is obtained by adding `zp,zq`.  The term
`delta_{crit,z}` is the deficit in the critically feasible three-root
bound on the complementary graph, with compulsory path set `U_z`.

#### Proof

Let

\[
 H=G[C\cup T\cup\{p,q\}]
\]

and let `mathcal G` be its four-root completion: all edges among the six
terminals `T\cup\{p,q\}` are added except `pq`.  Thus the completed terminal
subgraph has exactly `binom(6,2)-1` edges, including any centre--pole edges
already present in `H`.  Subtracting this fixed terminal-edge total from
the Du--Li--Xie--Yu bound shows that

\[
       \sigma_r=R_4-e(\mathcal G),                    \tag{3.4}
\]

where

\[
 R_t=(t+1)v(H)-\frac{t^2}{2}-\frac{3t}{2}-1
 \quad\text{at }t=4.                                 \tag{3.5}
\]

We now replay the part of the constructive proof which produces the
literal planar atom.  This is necessary because that construction occurs
inside the source's minimal-counterexample proof and is not part of the
statement of its theorem.

Minimality of `T` makes the three-root instance `H-z` feasible.  Choose an
induced `p`--`q` path `P_z` in `H-z` for which one component contains the
three roots in `T-{z}` and, subject to this, the component `L_z` of
`H-P_z` containing `z` has maximum order.  The two components are distinct,
since otherwise `P_z` would witness feasibility of the four-root instance.
Every neighbour of `L_z` in `H` consequently lies on `P_z`, and `P_z`
avoids the other three roots.  Hence

\[
 U_z=N_H(L_z)-\{p,q\}\subseteq V(P_z)\cap C.
\]

Let `K_z` be the component of `H-z-P_z` containing `T-{z}`, contract
`K_z` to `a^*`, and call the resulting graph `H^*`.  The two-rooted graph

\[
                    (H^*,\{a^*,z\},p,q)
\]

is infeasible: a linkage pair in it expands through the connected set
`K_z` to a `p`--`q` path disjoint from a connected subgraph containing all
four roots of `H`.  Seymour's two-linkage theorem therefore gives a
`\{a^*,z,p,q\}`-collection `\mathcal Y` of sets with neighbourhood at
most three such that the quotient has a disc representation with boundary
order `z,p,a^*,q`.  Choose `\mathcal Y` with maximum cardinality, so that
its members may be taken connected.

Every member `Y` of `\mathcal Y` has `a^*` in its neighbourhood.  Otherwise
it lifts to a nonempty terminal-avoiding subset of `C` with
`|N_H(Y)|\le3`.  In the whole graph it gains neighbours only at the one
omitted centre `r`: the opposite shore is anticomplete to `C`.  Thus its
whole-graph neighbourhood has order at most four and separates it from the
nonempty opposite shore, contrary to seven-connectivity.

This is precisely the replacement for property (2) in the source proof.
It also makes the quotient lift literal.  If a member `Y` meets `P_z`, the
two path directions and `a^*` exhaust its three possible neighbours.  Such
a member cannot meet `L_z\cup U_z`: adjoining the relevant vertex to the
connected graph `L_z` would force a fourth neighbour in `L_z`.  If a
member misses `P_z` but meets `L_z`, connectedness of `Y` and its adjacency
to `a^*` give an `a^*`--`L_z` path through `Y`; that path must cross
`P_z`, a contradiction.  Thus no member of `\mathcal Y` meets the literal
atom `A_z`.

Compressing the members which meet `P_z` leaves a `p`--`q` path with the
vertices of `U_z` in their original order.  In the disc representation of
the quotient, the closed region bounded by this path and the boundary arc
through `z` contains `L_z` and every edge incident with it.  Consequently
the uncontracted graph `A_z^+` has a disc representation with boundary
order

\[
                         p,U_z,q,z.
\]

Euler's formula after adding the `2k_z+1` noncrossing edges displayed in
the source proof gives (3.3).  Define `delta_{pl,z}` to be its nonnegative
integer slack.

Put `H_1=H-L_z`.  The same maximality argument makes the three-rooted graph
on `H_1` critically feasible with respect to `U_z`.  The critically
feasible theorem gives a terminal-avoiding collection whose members have
`H_1`-neighbourhood of order at most five.  That collection is empty in
the present host.  Indeed, any member lies in `C`; it gains in the whole
graph only the one omitted centre `r`.  It gains no neighbour in the
opposite shore, and no neighbour in `L_z` because it avoids
`N_H(L_z)\subseteq U_z\cup\{p,q\}`.  A nonempty member would therefore have
`G`-neighbourhood of order at most six, contrary to seven-connectivity.

Consequently the uncontracted complementary completion `mathcal G_1`
satisfies

\[
 e(\mathcal G_1)
 \le5v(H_1)-\frac{4^2}{2}-\frac{3\cdot4}{2}-1-k_z.
\tag{3.6}
\]

Let `delta_{crit,z}` be the slack in (3.6).  The edge and vertex
decompositions in the constructive proof are exact:

\[
 \begin{aligned}
 e(\mathcal G)&=e(\mathcal G_1)+e(A_z^+)+3,\\
 v(H)&=v(H_1)+v(A_z)-k_z-2.
 \end{aligned}                                      \tag{3.7}
\]

The first line has three additional completion edges from `z` to the other
three roots.  Also

\[
 v(A_z)=|L_z|+k_z+2=r_z+k_z+3.                       \tag{3.8}
\]

Substituting (3.3), (3.6)--(3.8) into (3.4) and cancelling gives

\[
 R_4-e(\mathcal G)
 =2\bigl(v(A_z)-k_z-3\bigr)
   +\delta_{pl,z}+\delta_{crit,z},
\]

which is (3.2).  \(\square\)

### Lemma 3.2 (singleton-atom contact table)

If `r_z=0`, then `c_z\le4`.  Under (1.3), the possibilities satisfy:

1. if `rho_z=0`, then `c_z=2`;
2. if `c_z=2`, its two `C`-contacts are adjacent;
3. if `c_z=3`, then `rho_z=2`, `d_z=3`, and `N_D(z)` is a triangle;
4. if `c_z=4`, then `rho_z\ge1`, `d_z\le3`, and `N_D(z)` is a clique.

#### Proof

When `r_z=0`, the atom is the singleton `{z}`.  Hence every `C`-neighbour
of `z` lies on the induced path `P_z`.  The graph induced by these contacts
is an induced subgraph of a path, so its independence number is at least
`ceil(c_z/2)`.  The nonempty set `N_D(z)` is anticomplete to `N_C(z)`.
Since the exceptional neighbourhood has independence number three,

\[
 \alpha(G[N_C(z)])+\alpha(G[N_D(z)])\le3.            \tag{3.9}
\]

Thus `c_z\le4`.

If `c_z=2` and the two contacts were nonadjacent, the first term in (3.9)
would be two.  Then `N_D(z)` would be a clique, but (1.2) gives
`d_z=6-rho_z\ge4`, contradicting the absence of a `K_4` in `N(z)`.
This proves item 2.

For `c_z=3` or `4`, the path contacts contain an independent pair, so
`N_D(z)` is again a clique and hence has order at most three.  Identity
(1.2) now gives, respectively, `rho_z=2,d_z=3` and
`rho_z\ge1,d_z\le3`.  If `rho_z=0`, the last two alternatives are
impossible; (1.3) and `c_z\le4` leave `c_z=2`.  \(\square\)

## 4. Exact four-root split

### Theorem 4.1 (the surviving `t=4` trichotomy)

Under the standing hypotheses, put `a=c-s`.  At least one of the following
holds.

1. **All contacts are high on the equality shore:**

   \[
                         c_z\ge4\quad(z\in Z).
   \tag{4.1}
   \]

   Consequently every `N_D(z)` is a clique of order at most three.

2. **The equality shore is already dense:**

   \[
                         a\le1,
   \qquad
                         e(C)=3c-a-1+g\ge3c-2+g.
   \tag{4.2}
   \]

3. **Every centre has at most four equality-shore contacts:**

   \[
                         a\in\{2,3\},
   \qquad
                         c_z\le4\quad(z\in Z).
   \tag{4.3}
   \]

   More precisely, choose any `j` with `c_j\le3`.  Then `Z-\{j\}` is a
   four-root circuit with

   \[
                         \sigma_j=c_j-a\le1,          \tag{4.4}
   \]

   and every selected root `z\ne j` has a singleton atom and satisfies the
   complete contact table of Lemma 3.2.

#### Proof

If (4.1) holds, the anticomplete contact sets and
`alpha(N(z))=3` show exactly as in the four-root palette note that
`N_D(z)` is a clique of order at most three.

Otherwise choose `j` with `c_j\le3`.  Lemma 2.1 makes `Z-\{j\}` a
four-root circuit and gives `a\le c_j\le3`.  If `a\le1`, (1.5) and
`s=c-a` give

\[
                         m=3c-a-1+g\ge3c-2+g,
\]

which is outcome 2.

It remains that `a\in\{2,3\}`.  Equation (2.3) gives
`0\le\sigma_j=c_j-a\le1`.  Lemma 3.1 then forces `r_z=0` for every
selected root `z\in Z-\{j\}`.  Lemma 3.2 gives `c_z\le4` and its more
precise table.  The omitted root already has `c_j\le3`, proving outcome 3.
\(\square\)

## 5. Exact nonclosure

Theorem 4.1 replaces the unrestricted four-root row by three literal
mechanisms.

* In outcome 1, all five opposite contact sets are cliques of order at most
  three.  The remaining obstruction is the five-colour Hall rectangle in a
  contraction colouring of the `D`-side.
* In outcome 2, the scalar argument has reached the unbounded density
  threshold `e(C)\ge3c-2`; converting its `K_5` minor into a boundary-rooted
  model is not supplied by the Du--Li--Xie--Yu theorem.
* In outcome 3, every selected root is represented by a forced induced-path
  contact set of order two, three, or four.  Synchronizing the four witness
  paths, or extracting a smaller actual two-cut when they cannot be
  synchronized, remains necessary.

No finite bound on `c` follows from this trichotomy, and no conclusion here
eliminates the full two-cut branch.
