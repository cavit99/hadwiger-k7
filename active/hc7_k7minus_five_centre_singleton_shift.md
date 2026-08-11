# The singleton-contact shift to an exact six-cut

**Status:** computation-free written proof; separate internal audit GREEN in
[`hc7_k7minus_five_centre_singleton_shift_audit.md`](hc7_k7minus_five_centre_singleton_shift_audit.md).
The finite order-six and order-seven shore exclusions cited below
are computer-assisted results with separate GREEN audits.  This note does
not prove that the singleton-contact case is impossible and does not prove
the `K_7^-` six-colour conjecture.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting and statement

Use the setting and response orientation of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus `G` is seven-connected and seven-chromatic, every proper minor of `G`
is six-colourable, `G` has minimum degree at least eight and no `K_7^-`
minor, and

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
 \qquad pq\notin E(G).
\tag{1.1}
\]

Every member of `Z` is an exceptional degree-eight vertex, `Z` is
independent, and `G-S` has exactly two connected components `C,D`, each
adjacent to every vertex of `S`.  The `C`-side has the equal pole-colour
response and the `D`-side has the distinct pole-colour response.  In
particular,

\[
 \chi(G[C])\ge4,\qquad \chi(G[D])\ge5.
\tag{1.2}
\]

For `u\in Z`, put

\[
 c_u=|N_C(u)|,\qquad d_u=|N_D(u)|,
 \qquad \rho_u=|N_{\{p,q\}}(u)|,
\tag{1.3}
\]

so `c_u+d_u+rho_u=8`.  Suppose that one centre `z` has

\[
                         c_z=1,
\tag{1.4}
\]

and name its unique neighbour in `C` by `x`.  Put

\[
 Y=Z-\{z\},\qquad B=S-\{z\}=Y\mathbin{\dot\cup}\{p,q\},
 \qquad E=D\cup\{z\},\qquad H=G-zx.
\tag{1.5}
\]

### Theorem 1.1 (singleton-shift normal form)

Under (1.1)--(1.5), all of the following hold.

1. `H` is six-connected, `B` is an exact six-vertex cut, and

   \[
                         H-B=C\mathbin{\dot\cup}E,
   \tag{1.6}
   \]

   where both displayed components are connected and adjacent to every
   vertex of `B`.

2. The four-root instance `(G[C union Y union {p,q}],Y,p,q)` is infeasible,
   while every proper subset of `Y` is feasible.  Thus `Y` is an
   inclusion-minimal four-root circuit.

3. The exact identities (4.4)--(4.13) below hold.  In particular,

   \[
                  |E(G[C])|\ge3|C|-2,
                  \qquad |C|\ge8,
   \tag{1.7}
   \]

   so `G[C]` has an unrooted `K_5` minor.

4. Every edge of `G[S]` belongs to a matching of order two, and
   `nu(G[S])=2`.

5. There is a six-path fan from `x` to the six literal vertices of `B`,
   preserving the edge `xz` and five colour-indexed first edges.  After
   the `xz`-path is absorbed into `E`, the contact graph of the other five
   path limbs has at most eight edges.

Neither the unrooted `K_5` minor nor the fan contact bound is terminal: the
minor is not rooted at boundary contacts, and the fan theorem does not
control which boundary vertex receives the `xz`-path.

## 2. The exact six-cut

### Lemma 2.1

Assertion 1 of Theorem 1.1 holds.

#### Proof

Deleting one edge lowers vertex-connectivity by at most one, so `H` is
six-connected.  More explicitly, if a set `Q` of order at most five
separated `H`, seven-connectivity of `G` would force `H-Q` to have exactly
two components joined in `G-Q` only by `zx`.  Deleting `Q union {z}` would
then separate the nonempty `x`-side in `G`; the other side is not the
singleton `{z}`, because `d_H(z)=7>|Q|`.  This contradicts
seven-connectivity.

The set `C` is connected.  The set `E` is connected because `D` is
connected and `d_z=7-rho_z>=5`.  There is no edge from `C` to `E` in `H`:
`C,D` were different components of `G-S`, and `zx` was the only edge from
`z` to `C`.  Thus these are precisely the components of `H-B`.
Fullness of `C,D` at `S` makes both components adjacent to every vertex of
`B`.  Hence `B` is the asserted exact six-cut. `\square`

The audited
[order-six cut localisation theorem](../results/hc7_k7minus_exact_six_cut_localisation.md)
therefore applies to `(H,B)`.  We will use its exact excess identity in
Section 4.

## 3. The shifted four-root circuit

For `T\subseteq Z`, call `T` feasible on `C` if
`G[C union T union {p,q}]` has a `p`--`q` path whose deletion leaves all
vertices of `T` in one component.

### Lemma 3.1

The set `Y` is infeasible on `C`.

#### Proof

Suppose `Y` were feasible.  The equal-response transfer in
[the four-root palette note](hc7_k7minus_five_centre_four_root_transfer.md),
Lemma 2.1, gives a proper colouring of `G[D union S]` in which `Y` is
monochromatic, `p,q` have a common different colour, and `z` avoids the
pole colour.  Align the first two colours with the equal-response colouring
of `G[C union S]`, and restrict the latter colouring after deleting `z`.

The only edge not contained in the two partial coloured graphs with common
boundary `Y union {p,q}` is `zx`.  On the `C`-side, `x` avoids the common
root colour because `z` has that colour.  If the transferred colour of `z`
is the root colour, `zx` is already proper.  Otherwise it is one of the
four colours outside the fixed root and pole colours; permute those four
colour names on the `D`-side so that it avoids the one colour on `x`.
The two colourings then glue to a six-colouring of `G`, a contradiction.
`\square`

### Lemma 3.2

Every proper subset of `Y` is feasible on `C`.

#### Proof

A singleton root is feasible: take a `p`--`q` path through connected `C`
which avoids that root.  Suppose that `T\subsetneq Y` is inclusion-minimal
infeasible and put `t=|T|`, `R=Z-T`.  The rooted density theorem of
Du--Li--Xie--Yu gives a nonnegative restricted slack `sigma_T`.  Its
terminal-avoiding collection is empty here: a member has neighbourhood at
most `t+1` in the restricted graph, and restoring the `5-t` omitted centres
gives a separator of `G` of order at most six between it and `D`.

Use the notation of Section 4 below.  Exact subtraction of the restricted
bound from the five-root bound gives, for `t=2`,

\[
 \sum_{u\in T}c_u
   =15-2c-\sum_{u\in R}(7-c_u)-2\sigma_T-\xi_C,
\tag{3.1}
\]

and, for `t=3`,

\[
 \sum_{u\in T}c_u
   =8-\sum_{u\in R}(7-c_u)-2\sigma_T-\xi_C.
\tag{3.2}
\]

The omitted set `R` contains `z`, whose contribution is `7-c_z=6`.
Every other summand is nonnegative because fullness of `D` gives
`c_u<=7`.  Also `c>=6` by the two-cut reduction and `xi_C>=0`.  The
right side of (3.1) is therefore negative, whereas its left side is at
least two.  The right side of (3.2) is at most two, whereas its left side
is at least three.  Both cases are impossible.  Consequently no pair or
triple in `Y` is infeasible.  Together with Lemma 3.1 this proves the
claim. `\square`

## 4. Exact scalar identities

Write

\[
 c=|C|,\quad d=|D|,\quad n=|V(G)|=c+d+7,
 \quad \eta=|E(G)|-4n,
\tag{4.1}
\]

and set

\[
 \begin{aligned}
 m_C&=e(C),&h_C&=e(C,\{p,q\}),
 &g_C&=\sum_{v\in C}(d_G(v)-8),\\
 m_D&=e(D),&h_D&=e(D,\{p,q\}),
 &g_D&=\sum_{v\in D}(d_G(v)-8),\\
 b&=e(H[B])=\sum_{u\in Y}\rho_u,
 &\lambda&=d_G(p)+d_G(q)-16.
 \end{aligned}
\tag{4.2}
\]

All of `eta,g_C,g_D,lambda` are nonnegative.  Define

\[
 \begin{aligned}
 \sigma&=5c+1-
   \left(m_C+h_C+\sum_{u\in Y}c_u\right),
 &\xi_C&=g_C+h_C-8,\\
 s_D&=6d+1-
   \left(m_D+h_D+\sum_{u\in Z}d_u\right),
 &\xi_D&=g_D+h_D-2.
 \end{aligned}
\tag{4.3}
\]

Here `sigma>=0` because `Y` is an inclusion-minimal infeasible four-root
set.  The full five-root instance on `D` is also infeasible: the proof of
Lemma 3.1 in
[the three-root palette note](hc7_k7minus_five_centre_t3_palette_gluing.md)
uses only seven-connectivity and the opposite shore responses for this
conclusion, not the later no-singleton-contact assumption.  Repeating its
short contraction argument, a feasible `D`-side path would split at two
contacts with the retained root component and force the forbidden distinct
response on `C`.  Thus Du--Li--Xie--Yu gives `s_D>=0`; its collection is
empty by seven-connectivity.  Finally, the four colour-distinguished paths
on `C` give `h_C>=8`, while the bichromatic `p`--`q` path on `D` gives
`h_D>=2`.  Hence `xi_C,xi_D>=0`.

For

\[
 \delta_C=e(C)+e_H(C,B)-4c,
 \qquad
 \delta_E=e(H[E])+e_H(E,B)-4(d+1),
\]

the exact six-cut identity is

\[
                  \delta_C+\delta_E=23+\eta-b.       \tag{4.4}
\]

Indeed, `e(H)=4n+eta-1=(4n-2)+(eta+1)`, so this is equation (5) of the
order-six cut theorem with `q_H=eta+1`.

The shifted four-root bound and the degree sum over `C` give

\[
 \boxed{
 \begin{aligned}
 m_C&=3c-2+\sigma+g_C,\\
 e_H(C,B)&=2c+3-2\sigma-g_C,\\
 \delta_C&=c+1-\sigma.
 \end{aligned}}                                      \tag{4.5}
\]

Separating the pole incidences gives

\[
 \boxed{
 \sum_{u\in Y}c_u=2c-5-2\sigma-\xi_C.}              \tag{4.6}
\]

Fullness at the four roots in `Y` therefore yields

\[
 2\sigma+\xi_C\le2c-9,
 \qquad \sigma\le c-5,
 \qquad \delta_C\ge6.                               \tag{4.7}
\]

On `D`, the five-root bound and degree sum give

\[
 \boxed{
 \begin{aligned}
 m_D&=2d-1+s_D+g_D,\\
 e(D,S)&=4d+2-2s_D-g_D,\\
 \sum_{u\in Z}d_u&=4d-2s_D-\xi_D.
 \end{aligned}}                                      \tag{4.8}
\]

Since `d_z=7-rho_z` and each of the other four centres has a neighbour
in `D`, (4.8) also gives

\[
                    2s_D+\xi_D\le4d-11+\rho_z.       \tag{4.8a}
\]

Moreover `d\ge7`.  Indeed, a five-critical subgraph on at most six
vertices has minimum degree four.  On five vertices it is `K_5`.  On six
vertices its complement has maximum degree one; at least two missing
disjoint edges make it four-colourable, while at most one missing edge
leaves a literal `K_5`.  This contradicts respectively criticality or the
literal `K_5` exclusion.

Since `d_z=7-rho_z`, adjoining `z` to `D` gives

\[
 \boxed{\delta_E=2d-3+\rho_z-s_D.}                  \tag{4.9}
\]

There is a useful second exact form.  Degree summation over `E` in `H`
gives

\[
 \delta_E={e_H(E,B)+g_D-1\over2}
 \ge\left\lceil{5+\rho_z+g_D\over2}\right\rceil.   \tag{4.10}
\]

The inequality uses the six incidences supplied by the `B`-full component
`D`, in addition to the `rho_z` pole incidences from `z`.

Summing the four centre degree identities over `Y`, and then using (4.4),
gives the two exact global exchanges

\[
 \boxed{\xi_C+\xi_D=2\eta+6-b-\rho_z,}              \tag{4.11}
\]

In particular,

\[
                             b+\rho_z\le6+2\eta.     \tag{4.11a}
\]

\[
 \boxed{\sigma+s_D=c+2d+b+\rho_z-25-\eta.}          \tag{4.12}
\]

Equivalently, (4.4)--(4.5) give

\[
 \boxed{\delta_E=22+\eta-b-c+\sigma.}               \tag{4.13}
\]

No inequality is lost in (4.4)--(4.13).  For reference, the pole degree
sum and the whole-graph degree sum are exactly

\[
 h_C+h_D+b+\rho_z=16+\lambda,
 \qquad 2\eta=g_C+g_D+\lambda.                       \tag{4.14}
\]

Jakobsen's sharp host bound, in the form used in the audited
[density and exceptional-vertex reduction](../results/hc7_k7minus_five_exceptional_vertices_reduction.md),
is `2e(G)<=9n-25`.  Hence

\[
 c+d\ge18+2\eta,
 \qquad
 \eta\le\left\lfloor{c+d-18\over2}\right\rfloor.   \tag{4.15}
\]

The contact set at the shifted centre also has an exact local form:

\[
 |N_D(z)|=7-\rho_z,qquad
 \alpha(G[N_D(z)])=2,qquad K_4\not\subseteq G[N_D(z)].
\tag{4.16}
\]

To see this, `x` is anticomplete to `N_D(z)`.  Theorem 2 of the audited
[exceptional-neighbourhood theorem](../results/hc7_k7minus_exceptional_neighbourhood_completion.md)
gives `alpha(G[N(z)])=3`, while literal `K_5` exclusion makes `G[N(z)]`
`K_4`-free.  Thus `alpha(G[N_D(z)])<=2`.
But `|N_D(z)|=7-rho_z>=5`, so this `K_4`-free graph is not complete and
has an independent pair.

Equation (4.5) proves the first inequality in (1.7).  The separately
audited order-six and order-seven equality-shore eliminations, specifically
[Corollary 3.1 of the order-seven theorem](../results/hc7_k7minus_order_seven_equality_shore_elimination.md),
give `c>=8`.  Since a `K_5`-minor-free graph on `c` vertices has at most
`3c-6` edges, the strict bound `m_C>=3c-2` gives an unrooted `K_5` minor
in `G[C]`.  This inference carries no boundary labels.

Finally, the proof of the GREEN
[four-root atom identity](hc7_k7minus_five_centre_t4_atom_exchange.md),
Lemma 3.1, reruns verbatim for this shifted circuit after Lemma 3.2 supplies
its minimality input.  That atom proof uses no lower bound on the omitted
root's shore contacts.  Thus, for each `u\in Y`,

\[
 \sigma=2r_u+\delta_{{\rm pl},u}+\delta_{{\rm crit},u}. \tag{4.17}
\]

In particular `r_u<=floor(sigma/2)`, and `sigma<=1` makes every one of
the four selected atoms a singleton.  The identity does not synchronize
their four separately chosen pole paths.

## 5. Boundary matching

### Lemma 5.1 (every boundary edge is covered)

For every edge `up` of `G[S]`, with `u\in Z`, there is a centre
`w\in Z-\{u\}` such that `wq\in E(G)`.  The symmetric statement holds
with the poles interchanged.  Consequently

\[
                             \nu(G[S])=2.             \tag{5.1}
\]

#### Proof

Suppose `up` is an edge and no centre of `Z-{u}` is adjacent to `q`.
Then

\[
                         I=S-\{u,p\}
\]

is independent.  Apply Lemma 1, the exact boundary-colouring reflection
lemma in the audited
[critical seven-cut capacity theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md),
to the partition

\[
                         I\mid\{u\}\mid\{p\}.
\]

Assign the full connected component `C` to `I` and retain the adjacent
singletons `u,p`; this gives the exact partition on the closed `D`-side.
Interchanging `C,D` gives the same exact partition on the closed `C`-side.
After renaming colours, the two colourings glue, a contradiction.

Thus every boundary edge has a disjoint mate.  All boundary edges join a
centre to a pole, so the two poles cover `E(G[S])` and the matching number
is at most two.  The two-cut reduction supplies at least one boundary edge;
its disjoint mate proves equality. `\square`

This is the same argument as the hash-pinned GREEN Lemma 2.1 of the
[four-root boundary-incidence note](hc7_k7minus_five_centre_t4_boundary_incidence.md),
repeated here because its proof uses no contact lower bound and remains
valid in the singleton-contact row.

## 6. A prescribed fan and its exact contact deficit

### Lemma 6.1 (palette six-fan)

There are six paths `Q_0,Q_1,...,Q_5` from `x` to `B` which share only
`x`, have the six distinct vertices of `B` as their ends, and satisfy the
following properties.

1. `Q_0` begins with `xz`; after deleting `x`, it lies in `E` until its
   end `b_0\in B`.
2. The other five paths preserve five distinct colour-indexed first edges
   at `x`; after deleting `x`, each lies in `C` until its boundary end.

The assignment of `Q_0` to `b_0` is not prescribed.

#### Proof

Take a proper six-colouring `phi` of the proper minor `H=G-zx`.  Necessarily
`phi(x)=phi(z)=alpha`, since otherwise `phi` would colour `G`.  Every one
of the other five colours is used: if one were absent, recolouring `x` with
that colour would again colour `G`.

For each `beta!=alpha`, the vertices `x,z` lie in one
`alpha`--`beta` component.  Otherwise interchange those colours on the
component containing `x`, making `xz` proper.  Choose a corresponding
`x`--`z` path and stop it at its first vertex of `B`.  Before that first
hit the path lies in `C`, and its first edge at `x` has a `beta`-coloured
other endpoint.  The five first edges are therefore distinct.

Apply Theorem 1.1 of the audited
[prescribed-spoke reduction](../results/hc7_order8_prescribed_spoke_reduction.md)
with `k=6`, base `x`, target set `B`, and prescribed edges `xz` together
with those five first edges.  Truncate each resulting path at its first
visit to `B`.  Pairwise disjointness makes the six first boundary vertices
distinct, hence they are exactly `B`.  The `xz`-path stays in `E` until
that visit, while each other path stays in `C`, because `C,E` are the two
components of `H-B`. `\square`

### Lemma 6.2 (five-limb contact bound)

Put

\[
 R_0=E\cup(V(Q_0)-\{x\}),
 \qquad L_i=V(Q_i)-\{x\}\quad(1\le i\le5).
\tag{6.1}
\]

Let `J` be the graph on `L_1,...,L_5`, with an edge when the corresponding
sets have an edge between them in `G`.  Then

\[
                              e(J)\le8.               \tag{6.2}
\]

#### Proof

The seven sets

\[
                   \{x\},\quad R_0,\quad L_1,\ldots,L_5
\tag{6.3}
\]

are pairwise disjoint and connected.  The singleton `{x}` is adjacent to
every other set through the six prescribed first edges.  The set `R_0` is
adjacent to every `L_i`: the limb contains a distinct end in `B`, while
the connected component `E\subseteq R_0` is adjacent to every vertex of
`B`.  If `J` had at least nine of its ten possible edges, (6.3) would be
an explicit `K_7^-` minor model.  Therefore `e(J)<=8`. `\square`

## 7. Exact nonclosure

The preceding information is jointly consistent at its sharpest scalar
level.  The following table is an exact arithmetic and local-incidence
witness; it is not asserted to be a graph satisfying every global host
hypothesis.

\[
\begin{array}{c|ccccccccccccc}
 &c&d&\eta&\lambda&b&\rho_z&\sigma&s_D&g_C&g_D&h_C&h_D&
   (\xi_C,\xi_D)\\ \hline
 \text{value}&8&10&0&0&2&2&2&5&0&0&8&4&(0,2)
\end{array}                                           \tag{7.1}
\]

Equations (4.5)--(4.10) then give

\[
 \begin{array}{c|ccccccccc}
 &m_C&e_H(C,B)&\sum_Yc_u&\delta_C&m_D&e(D,S)&
 \sum_Zd_u&e_H(E,B)&\delta_E\\ \hline
 \text{value}&24&15&7&7&24&32&28&29&14.
 \end{array}                                          \tag{7.2}
\]

Thus `delta_C+delta_E=21=23-b`,
`sigma+s_D=7=c+2d+b+rho_z-25`, and
`xi_C+xi_D=2=6-b-rho_z`; also `c+d=18` makes (4.15) tight.

For literal centre data, take `Y={w,y_1,y_2,y_3}` and

\[
\begin{array}{c|ccc}
u&c_u&d_u&\rho_u\\ \hline
z&1&5&2\\
w&1&5&2\\
y_1,y_2,y_3&2&6&0.
\end{array}                                           \tag{7.3}
\]

Every row sums to eight, the `Y`-columns have the totals in (7.2), and
`G[S]` may be exactly the `K_{2,2}` on parts `\{z,w\}` and `\{p,q\}`.
It is edge-covered and has matching number two, while `H[B]` has exactly
the two edges `wp,wq`, so `b=2`.  The local constraint (4.16) is compatible
with `G[N_D(z)]\cong C_5`.  Even the full exceptional-neighbourhood
condition can be met locally with `xp\in E(G)`, `xq\notin E(G)`, one
`p`-edge and three `q`-edges into that cycle, with the `p`-neighbour also
a `q`-neighbour and the two nonneighbours of `q` consecutive.  This uses
exactly `h_D=4`, gives independence number three in `G[N(z)]`, and creates
no `K_4` there.  Split the eight `C`--pole incidences as five at `p` and
three at `q`; then both poles have degree eight, as required by
`lambda=0`.  At the internal-core level, the simultaneous values
`c=8,m_C=24,chi(C)=4` and literal `K_5` exclusion are realized as follows.
Write

\[
 V(C)=\{x,a,b,c',d',e,f,g\}
\]

and take `G[C]` to be `K_8` minus the perfect matching

\[
                         xg,\quad ab,\quad c'd',\quad ef.
\tag{7.4}
\]

Assign the boundary incidences

\[
\begin{array}{c|c}
\text{boundary vertex}&N_C(\text{boundary vertex})\\ \hline
p&\{x,a,b,c',d'\}\\
q&\{a,e,f\}\\
z&\{x\}\\
w&\{g\}\\
y_1&\{b,e\}\\
y_2&\{c',f\}\\
y_3&\{d',g\}.
\end{array}                                          \tag{7.5}
\]

Every vertex of `C` then has degree eight, and (7.5) realizes all the
`C`-side incidence totals above.

Now let the uncontrolled fan end be `b_0=w`.  The other five fan ends are

\[
                         p,q,y_1,y_2,y_3,
\]

which are independent in the displayed boundary graph.  The data
(7.4)--(7.5) admit the five `C`-side limbs

\[
 \{p\},\quad\{a,q\},\quad\{b,y_1\},\quad
 \{c',y_2\},\quad\{d',y_3\}.                        \tag{7.6}
\]

The first limb is adjacent to the other four through `p`, while the last
four induce `K_4` minus the two edges corresponding to `ab,c'd'`.
Consequently their contact graph has exactly eight edges, showing that
the bound (6.2) is sharp at the level of all displayed scalar, boundary,
core, and fan-incidence data.  The
internal vertices of the bichromatic `p`--`q` path on the distinct-response
shore lie in `D\subseteq R_0`, but its literal ends `p,q` lie in two
different limb bags.  Absorbing the whole path would therefore intersect
those limbs, while deleting its ends supplies no new connected branch set
with the required limb contacts.  The equality-shore `p`--`q` paths are
likewise not supplied disjointly from, or allocated among, the five limbs.
They therefore do not create two additional completing bags.

This identifies the exact missing step.  One needs either a theorem that
controls the pairing of the `xz` arm with `B`, a rooted placement of the
unrooted `K_5` minor in `C`, or a simultaneous `p`--`q` linkage allocated
to the five limbs.  The scalar identities, the boundary matching, and the
prescribed-first-edge fan alone do not imply any of these conclusions.
