# Contraction colourings eliminate the sharp three-root two-cut residue

**Status:** written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_t3_palette_gluing_audit.md`](hc7_k7minus_five_centre_t3_palette_gluing_audit.md).

This note proves a terminal colouring theorem for the sharp minimal-bad-root
triple arising in the five-centre two-cut analysis.  It does not treat a
singleton shore contact or a minimal bad-root set of order four or five.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Independent-boundary contraction and gluing

### Lemma 1.1 (contraction-colouring gluing criterion)

Let `G` be a graph every proper minor of which is six-colourable.  Suppose

\[
 V(G)=L\mathbin{\dot\cup}T\mathbin{\dot\cup}R,
\]

where `L,R` are nonempty, `T` is independent, and both `G[L union T]` and
`G[R union T]` are connected.  Assume also that `T` is nonempty.  Put

\[
                         M=E_G(L,R).
\]

There are proper six-colourings `phi_L` of `G[L union T]` and `phi_R` of
`G[R union T]` in which `T` is monochromatic.  After naming its colour
`gamma` in both colourings, every endpoint of an edge in `M` has a colour
different from `gamma`.

For colours `a,b != gamma`, put `(a,b) in F` when some edge `uv in M`, with
`u in L` and `v in R`, satisfies

\[
                       \phi_L(u)=a,
                       \qquad \phi_R(v)=b.             \tag{1.1}
\]

If the bipartite graph on two copies of the five colours different from
`gamma`, with edge set

\[
                  \{ba:(a,b)\notin F\},               \tag{1.2}
\]

has a perfect matching, then `G` is six-colourable.

#### Proof

Contract a spanning tree of `G[R union T]` to one vertex, six-colour the
resulting proper minor, and restrict the colouring to `L` and the
contraction vertex.  Expand only the literal vertices of `T`, giving all of
them the colour of the contraction vertex.  Independence of `T` makes this
a proper colouring `phi_L` of `G[L union T]`.  Every `L`-endpoint of an
edge in `M` was adjacent to the contraction vertex and therefore avoids
its colour.  Contracting `G[L union T]` gives `phi_R` symmetrically.

Align the two colours on `T`.  A perfect matching in (1.2) is a permutation
of the other five colour names on the `R`-side which makes the ends of
every edge in `M` different.  After that permutation, the two colourings
agree on `T` and glue.  Every edge internal to a closed side remains proper,
and the matching condition makes every edge in `M` proper.  This is a
proper six-colouring of `G`.  \(\square\)

### Lemma 1.2 (the six-position Hall criterion)

Let `F` be a set of at most six positions in a `5 by 5` array.  There is a
permutation avoiding every position of `F` unless `F` contains all five
positions of one row or all five positions of one column.

#### Proof

Suppose the complementary bipartite graph has no perfect matching.  By
Hall's theorem, some set `X` of `k` columns has at most `k-1` allowed row
neighbours.  Consequently `F` contains a rectangle with `k` columns and
at least `6-k` rows, and hence

\[
                         |F|\ge k(6-k).                \tag{1.3}
\]

For `k=2,3,4`, the right side is respectively `8,9,8`, contrary to
`|F|<=6`.  For `k=1`, `F` contains a full column.  For `k=5`, at least one
row is forbidden from all five columns.  These are the two stated
exceptions.  \(\square\)

## 2. The sharp three-root setting

Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \chi(N)\le6\text{ for every proper minor }N\text{ of }G.
                                                               \tag{2.1}
\]

Let `Z=A dotunion {r,s}` be an independent set of five degree-eight
vertices, where

\[
                         A=\{z_1,z_2,z_3\}.
\]

Let `p,q` be nonadjacent vertices outside `Z`, put `S=Z dotunion {p,q}`,
and suppose `G-S` has exactly two connected components `C,D`, both adjacent
to every vertex of `S`.

Assume the following sharp three-root data.

1. Neither `r` nor `s` is adjacent to `p` or `q`.
2. For every `z_i in A`,

   \[
                    |N_G(z_i) cap C|=2,               \tag{2.2}
   \]
3. The graph

   \[
                    J=G[C union \{r,s,p,q\}]          \tag{2.3}
   \]

   has a `\{r,s,p,q\}`-rooted `K^*_{4,2}` minor model.  Thus it has four
   disjoint connected root bags, one containing each named root, and two
   further disjoint connected helper bags.  Each helper is adjacent to all
   four root bags and the two helpers are adjacent.

### Theorem 2.1 (terminal three-root palette gluing)

Under (2.1)--(2.3), `G` is six-colourable.

#### Proof

Let

\[
       P=\{z_i in A:E_G(z_i,\{p,q\})\ne\varnothing\}. \tag{2.4}
\]

Suppose first that `|P|<=2`.  Put

\[
       L=C,\qquad T=S-P,\qquad R=D union P.            \tag{2.5}
\]

The set `T` is independent: `pq` is absent, `Z` is independent, every
centre--pole edge has its centre in `P`, and `r,s` have no pole edge.  Both
closed sides are connected because `C,D` are connected and full to `S`.
The only `L`--`R` edges are the two `C`-incidences of each member of `P`, so

\[
                         |E_G(L,R)|=2|P|\le4.          \tag{2.6}
\]

Lemmas 1.1 and 1.2 therefore give a proper six-colouring of `G`.

It remains that `P=A`; in particular, every `z_i` has a neighbour in
`{p,q}`.  Normalize the rooted model in `J` as follows.  Choose it first to
maximize the total order of its two helper bags `H_1,H_2` and, subject to
that, to minimize the total order of its four root bags
`R_r,R_s,R_p,R_q`.  Put `U=H_1 union H_2`.

For a root bag `R_t`, put

\[
 A_t=N_J(H_1)\cap R_t,
 \qquad B_t=N_J(H_2)\cap R_t,
 \qquad P_t=A_t\cup B_t.
\]

The usual normalized-helper argument gives

\[
                           |P_t|=1.                   \tag{2.7}
\]

For completeness, both `A_t` and `B_t` are nonempty.  If
`|A_t union B_t|>=2`, choose distinct vertices `u in A_t` and `v in B_t`
(interchanging the helper names if necessary), and replace `R_t` by a
minimal tree containing its root, `u`, and `v`.  One of `u,v` distinct
from the root is a leaf and can be moved into its corresponding helper,
contrary to the chosen maximality.  The only remaining possibility is that
`A_t=B_t` is one singleton, proving (2.7).  Moreover, no component outside
the six model bags meets `U`, since it could be absorbed into a helper.
Hence

\[
                         |N_J(U)|\le4.                 \tag{2.8}
\]

The component `D` is anticomplete to `U subseteq C`, so it lies outside
`U union N_G(U)`.  The only possible neighbours of `U` outside `J` are
`z_1,z_2,z_3`.  Seven-connectivity and (2.8) therefore imply that equality
holds in (2.8) and that every `z_i` has a neighbour in `U`.  By the
pigeonhole principle, one helper, say `H_2`, has a neighbour in two of the
three centres; relabel them `z_1,z_2`.

In a proper minor of `G`, contract spanning trees of the two disjoint
connected sets

\[
K_0=H_1 union R_r union R_s union R_p union R_q,
 \qquad K_2=H_2 union \{z_2\},                       \tag{2.9}
\]

and delete unused vertices of `C`.  Keep `D`, `z_1,z_3`, and the image of
`z_2` inside the second contracted set, together with every represented
incident edge.  Write `v_0,v_2` for the two contraction images.  The three
vertices

\[
                         v_0,v_2,z_1                 \tag{2.10}
\]

form a triangle: the helper--helper edge gives `v_0v_2`, the contact from
`z_1` to `H_2` gives `z_1v_2`, and a centre--pole edge from `z_1` to `p` or
`q` gives `z_1v_0`.

Six-colour this proper minor.  Restrict to the vertices of

\[
                  G[(D union A) union \{r,s,p,q\}],   \tag{2.11}
\]

give all four vertices `r,s,p,q` the colour of `v_0`, and give `z_2` the
colour of `v_2`.  This is proper: every retained edge to a contracted bag
was represented in the minor, while `\{r,s,p,q\}` is independent.  By
(2.10), `z_1,z_2` receive distinct colours, and all three members of `A`
avoid the common colour on `r,s,p,q`.

For the other closed shore, contract the connected set

\[
                         D union A union \{r,s,p,q\}  \tag{2.12}
\]

to one vertex, six-colour the proper minor, and expand only `r,s,p,q`.
This gives a proper colouring of `G[C union \{r,s,p,q\}]` in which those
four vertices are monochromatic.  Align their common colour with the one
in (2.11).

There are exactly six edges between `C` and `D union A`, namely the two
edges from each `z_i` to `C`.  Apply the matching step in Lemma 1.1 to
their forbidden colour-pair relation.  It has at most six positions.  It
cannot contain a full row, because its right endpoints are only the three
vertices of `A`
and therefore use at most three colours.  It cannot contain a full column:
the two vertices `z_1,z_2` have distinct colours, so a single right-side
colour occurs on at most two of the three centres and is incident with at
most four of the six crossing edges.  Lemma 1.2 supplies a permutation of
the five nonboundary colours avoiding every crossing equality.  The two
closed-shore colourings now glue to a proper six-colouring of `G`, as
claimed.  \(\square\)

## 3. Derivation from the unconditional two-cut reduction

This section records why the hypotheses in Section 2 are exactly the
minimal-triple equality case.  It is conditional only at the point stated
explicitly below: singleton shore contacts have not yet been eliminated.

Use the notation and conclusions of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus `C` has the equal response, `D` has the distinct response,

\[
 \chi(C)\ge4,\qquad \chi(D)\ge5,
\]

the full five-root instance on `C` is infeasible, `mu_S(C)=1`, and

\[
 e(C)+e(C,S)\le6|C|+1.
\]

The four critical-edge paths on `C` give

\[
                         e(C,\{p,q\})\ge8.            \tag{3.1}
\]

For this section assume the **no-singleton-contact branch**

\[
             e(C,z_i)\ge2,\qquad e(D,z_i)\ge2
             \quad(1\le i\le5).                      \tag{3.2}
\]

This is an assumption, not a consequence of the unconditional reduction.

For `X in {C,D}` and `T subseteq Z`, call `T` feasible on `X` if
`G[X union T union {p,q}]` has a `p`--`q` path whose deletion leaves all
vertices of `T` in one component.

### Lemma 3.1 (the dual shore)

The full five-root instance on `D` is infeasible,

\[
                         \mu_S(D)=1,                  \tag{3.3}
\]

and

\[
                    e(D)+e(D,S)\le6|D|+1.            \tag{3.4}
\]

Every pair of centres is feasible on `D`.

#### Proof

Suppose first that a `p`--`q` path `P` on the `D`-side leaves all of `Z`
in one component `K`.  Choose a component `W` of `K cap D`.  It is
nonempty, and

\[
                         N_G(W)\subseteq Z\cup N_P(W).
\]

The opposite component `C` witnesses that this is a genuine separation.
Seven-connectivity therefore gives two distinct contacts of `W` on `P`.
Splitting `P` between its first and last such contacts gives disjoint
connected `p`- and `q`-subpaths, each adjacent to `K` and adjacent to one
another.  Contracting these three pairwise adjacent sets produces, on the
untouched `C`-side, a six-colouring in which `Z`, `p`, and `q` have three
distinct colours.  This contradicts the equal response of `C`.

If `D` contained two disjoint connected `S`-full subgraphs `P_1,P_2`, then

\[
                  P_1\cup Z,\qquad P_2\cup\{p\},
                  \qquad\{q\}
\]

would again be three pairwise adjacent connected sets.  The same
contraction contradicts the equal response on `C`.  Since `D` itself is
connected and `S`-full, (3.3) follows.

Apply Du--Li--Xie--Yu, Theorem 1.2, to the now-infeasible five-root
instance on `D`.  A nonempty member of its terminal-avoiding collection
would lie in `D`, have neighbourhood at most six, and be separated from
`C`, contrary to seven-connectivity.  The collection is empty, and the
same completed-quotient calculation as on `C` gives (3.4).

Finally, suppose a pair `{x,y}` were infeasible on `D`.  The two-root
Seymour outcome quoted as Du--Li--Xie--Yu, Theorem 1.1, gives a terminal-avoiding
collection whose members have neighbourhood at most three and whose
completed quotient is planar.  Restoring the three omitted centres adds at
most three vertices to the neighbourhood of a collection member.  Thus a
nonempty member would have a `G`-neighbourhood of order at most six, again
impossible.  The collection is empty, so the uncontracted two-root graph,
and hence `D`, is planar.  This contradicts `chi(D)>=5`.  \(\square\)

### Lemma 3.2 (minimal-root algebra on the equality shore)

Put

\[
 \begin{aligned}
 c&=|C|,&m_C&=e(C),&h_C&=e(C,\{p,q\}),\\
 c_i&=e(C,z_i),&
 g_C&=\sum_{v\in C}(d_G(v)-8),&
 s_C&=6c+1-(m_C+h_C+\textstyle\sum_i c_i),\\
 \xi_C&=g_C+h_C-8.
 \end{aligned}                                         \tag{3.5}
\]

Then `s_C,xi_C>=0`, and

\[
 m_C=2c-1+s_C+g_C,
 \qquad
 \sum_i c_i=4c-6-2s_C-\xi_C.                          \tag{3.6}
\]

Let `T` be an inclusion-minimal infeasible root set, put `t=|T|`,
`R=Z-T`, and define

\[
 b_C(R)=\sum_{z_i\in R}(7-c_i),
 \qquad
 \sigma_C=(t+1)c+1-
       \left(m_C+h_C+\sum_{z_i\in T}c_i\right).       \tag{3.7}
\]

Then `sigma_C>=0` and

\[
 s_C=(5-t)(c-7)+b_C(R)+\sigma_C.                      \tag{3.8}
\]

In particular, every centre pair is feasible on `C`.  If `t=3`, then

\[
             \sum_{z_i\in T}c_i
              =8-b_C(R)-2\sigma_C-\xi_C.              \tag{3.9}
\]

#### Proof

The first identity in (3.6) follows by subtracting the Du--Li--Xie--Yu
edge bound with slack `s_C` from the degree sum

\[
                   8c+g_C=2m_C+h_C+\sum_i c_i.
\]

The second follows by substituting that identity into the degree sum and
using the definition of `xi_C`; (3.1) gives `xi_C>=0`.  For the restricted `t`-root instance,
any nonempty member of the Du--Li--Xie--Yu terminal-avoiding collection
lies in `C` and has neighbourhood of order at most `t+1`.  Restoring the
`5-t` omitted centres gives it a full `G`-neighbourhood of order at most
six, separating it from nonempty `D`; seven-connectivity excludes this.
Thus the collection is empty and the restricted edge bound gives
`sigma_C>=0`.  Equation (3.8) is the exact difference between the full
five-root bound and this restricted bound; (3.9) follows by substituting
(3.8) into (3.6).

A singleton is feasible because a `p`--`q` path can be chosen through the
connected component `C` without using the centre.  If an infeasible pair
were inclusion-minimal, the same calculation with `t=2` would give

\[
       \sum_{z_i\in T}c_i
          =15-2c-b_C(R)-2\sigma_C-\xi_C.              \tag{3.10}
\]

Here `c>=6`, while (3.2) and the centre degree equation give
`b_C(R)>=3`.  The right side of (3.10) is at most zero, whereas its left
side is at least four, a contradiction.  Thus every pair is feasible.
\(\square\)

### Proposition 3.3 (the sharp triple forces Section 2)

Suppose an inclusion-minimal infeasible set `A subseteq Z` has order
three, and write `Z=A dotunion {r,s}`.  Then all the hypotheses (2.2)--(2.3)
hold, and neither `r` nor `s` has a pole edge.

#### Proof

For every centre, degree eight gives

\[
                         c_i+d_i+\rho_i=8,
 \qquad \rho_i=e(z_i,\{p,q\}).                       \tag{3.11}
\]

Consequently (3.2) gives

\[
 b_C(\{r,s\})\ge2+\rho_r+\rho_s,
 \qquad \sum_{z_i\in A}c_i\ge6.                     \tag{3.12}
\]

Combining (3.9) and (3.12) yields the equality chain

\[
 6\le\sum_{z_i\in A}c_i
   =8-b_C(\{r,s\})-2\sigma_C-\xi_C
   \le6-\rho_r-\rho_s\le6.                           \tag{3.13}
\]

Thus

\[
 b_C(\{r,s\})=2,quad
 \rho_r=\rho_s=0,quad
 \sigma_C=\xi_C=0.                                  \tag{3.14}
\]

Equality term by term in (3.11)--(3.13) gives

\[
 (c_r,d_r,\rho_r)=(c_s,d_s,\rho_s)=(6,2,0),
 \qquad c_i=2\quad(z_i\in A).                        \tag{3.15}
\]
This proves (2.2).

It remains to derive (2.3).  Equations (3.8) and (3.14) give

\[
                         s_C=2c-12.                   \tag{3.16}
\]

Since `xi_C=0`, (3.1) and `g_C>=0` force `g_C=0` and `h_C=8`.  Hence

\[
                         m_C+h_C=4c-5.                \tag{3.17}
\]

Put `Q={r,s,p,q}` and `J=G[C union Q]`.  The set `Q` is independent by
(3.14), the independence of `Z`, and `pq notin E(G)`.  From (3.15) and
(3.17),

\[
          e(J)=m_C+h_C+c_r+c_s
              =4c+7=4|V(J)|-9.                       \tag{3.18}
\]

The audited
[closed-shore rooted-connectivity lemma](../results/hc7_closed_shore_rooted_connectivity.md)
makes `(J,Q)` internally four-connected.  Norin--Totschnig, Lemma 12,
says that an internally four-connected rooted graph with no
`Q`-rooted `K^*_{4,2}` model has at most `4|V(J)|-10` edges.  Equation
(3.18) exceeds that threshold by one, so the required rooted model exists.
This is (2.3).  \(\square\)

Since the full five-root set is infeasible, Lemmas 3.1--3.2 show that a
minimal bad set exists and has order three, four, or five.  Proposition
3.3 and Theorem 2.1 eliminate the order-three case throughout the
no-singleton-contact branch.

## 4. Exact scope

The proof is unbounded in `|C|` and `|D|`.  Its two essential inputs beyond
the critical-host hypotheses are the exact two-vertex `C`-contact at each
selected root and the rooted `K^*_{4,2}` model in (2.3).  It does not infer
either input for a singleton contact or for a minimal bad-root set of order
four or five.
