# The five-root atom slack forces an order-fifteen equality shore

**Status:** written proof; separate hash-pinned internal audit **GREEN** in
[`hc7_k7minus_five_centre_t5_atom_slack_audit.md`](hc7_k7minus_five_centre_t5_atom_slack_audit.md).
This note applies only to the minimally infeasible all-rainbow `t=5` row.
It proves that the equality-response component has order at least fifteen.
The proof first eliminates the rows through order eleven one atom at a
time.  At orders twelve through fourteen it uses all five atoms
simultaneously: first by packing their distinguished vertices around long
induced paths, and finally by coupling their mutual adjacencies to the two
path endpoints.  It does not close the five-centre two-cut branch.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting and the global scalar identities

Use the setting of the audited
[global five-root palette alternative](hc7_k7minus_five_centre_t5_global_palette.md)
and assume its all-rainbow outcome.  Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, the permitted response on `C`
has `p=q`, and the permitted response on `D` has `p\ne q`.  Both rooted
instances are infeasible and deleting any one root makes either instance
feasible.  Every centre `z` has degree eight and

\[
 d_z=|N_D(z)|=3,\qquad N_D(z)\cong K_3,
 \qquad c_z=|N_C(z)|=5-\rho_z,
 \qquad \rho_z=|N_{\{p,q\}}(z)|\in\{0,1\}.          \tag{1.1}
\]

The graph has no `K_5` subgraph.  In particular every degree-eight vertex
is exceptional, and the audited exceptional-neighbourhood theorem gives

\[
                         \alpha(G[N(u)])=3             \tag{1.2}
\]

for every degree-eight vertex `u`.

Put

\[
\begin{aligned}
 c&=|C|,&m&=e(C),&h&=e(C,\{p,q\}),\\
 g&=\sum_{v\in C}(d_G(v)-8),
 &b&=\sum_{z\in Z}\rho_z,\\
 s&=6c+1-\left(m+h+\sum_{z\in Z}c_z\right).
\end{aligned}                                        \tag{1.3}
\]

The full five-root Du--Li--Xie--Yu bound gives `s\ge0`.  Since
`\sum c_z=25-b`, its equality with the degree sum on `C` gives

\[
 \boxed{\ m=2c-1+s+g,\qquad
         2s=4c-23+b-g-h.\ }                         \tag{1.4}
\]

The four colour-distinguished `p`--`q` paths in `C` supplied by the
audited two-cut reduction have different first neighbours at `p` and
different last neighbours at `q`.  Consequently

\[
                              h\ge8.                  \tag{1.5}
\]

## 2. The full five-root atom identity

### Lemma 2.1 (coefficient-three atom identity)

For every `z\in Z`, there are an induced `p`--`q` path `P_z` in

\[
               G[C\cup(Z-\{z\})\cup\{p,q\}]
\]

and a component `L_z` after deleting `P_z` which contains `z` after the
literal vertex `z` is restored.  Put

\[
 r_z=|L_z\cap C|,
 \qquad
 U_z=N_{G[C\cup Z\cup\{p,q\}]}(L_z)-\{p,q\},
 \qquad k_z=|U_z|.                                  \tag{2.1}
\]

Then

\[
                         U_z\subseteq V(P_z)\cap C,  \tag{2.2}
\]

and there are nonnegative integer deficits
`\delta_{{\rm pl},z},\delta_{{\rm crit},z}` such that

\[
 \boxed{\ s=3r_z+\delta_{{\rm pl},z}
                    +\delta_{{\rm crit},z}.\ }      \tag{2.3}
\]

#### Proof

Let

\[
                         H=G[C\cup Z\cup\{p,q\}]
\]

and complete its seven terminals to a clique except for `pq`; call the
completed graph `\mathcal G`.  The terminal completion has twenty edges,
and the five-root density target is

\[
                         R_5=6v(H)-21.
\]

Therefore the definition in (1.3) is exactly

\[
                         s=R_5-e(\mathcal G).         \tag{2.4}
\]

Minimal infeasibility makes the four-root instance `H-z` feasible.  Follow
the constructive proof of Du--Li--Xie--Yu, Theorem 1.2: choose an induced
witness path `P_z` and, subject to the other four roots lying in one
component of its deletion, maximize the component `L_z` containing the
restored `z`.  The same maximality argument gives (2.2).

The two-linkage part of that construction gives a literal disc-planar atom
`A_z`.  Its vertex set is

\[
                 L_z\cup U_z\cup\{p,q\},
 \qquad v(A_z)=r_z+k_z+3,                            \tag{2.5}
\]

and it retains precisely the edges incident with `L_z`.  After adding
`zp,zq`, write the result as `A_z^+`.  Its planar bound is

\[
 e(A_z^+)\le3v(A_z)-7-2k_z.                         \tag{2.6}
\]

Define `\delta_{{\rm pl},z}` to be the slack in (2.6).

For completeness, the collection used in the two-linkage quotient lifts
literally here.  A member which did not see the contracted component
containing the other four roots would lift to a nonempty subset of `C`
with neighbourhood of order at most three.  It has no neighbour in `D`,
contrary to seven-connectivity.  The standard path-direction argument then
shows that no collection member meets `L_z\cup U_z`.

Put `H_1=H-L_z`.  Critical feasibility of the complementary four-root
instance, with compulsory path set `U_z`, gives a completed graph
`\mathcal G_1` satisfying

\[
 e(\mathcal G_1)\le6v(H_1)-21-k_z.                 \tag{2.7}
\]

Its terminal-avoiding collection is empty.  Indeed, a member has
`H_1`-neighbourhood of order at most six, avoids `U_z\cup\{p,q\}`, and
hence has no neighbour in `L_z`; it also has no neighbour in `D`.  Its
whole-graph neighbourhood would therefore have order at most six,
contrary to seven-connectivity.  Define `\delta_{{\rm crit},z}` to be the
slack in (2.7).

The constructive decomposition is exact:

\[
\begin{aligned}
 e(\mathcal G)&=e(\mathcal G_1)+e(A_z^+)+4,\\
 v(H)&=v(H_1)+v(A_z)-k_z-2.                         \tag{2.8}
\end{aligned}
\]

The four extra edges in the first line join `z` to the other four roots.
Substitute (2.5)--(2.8) into (2.4).  All terms involving `H_1` and `k_z`
cancel, leaving

\[
 R_5-e(\mathcal G)
 =3\bigl(v(A_z)-k_z-3\bigr)
  +\delta_{{\rm pl},z}+\delta_{{\rm crit},z},
\]

which is (2.3). \(\square\)

## 3. A rainbow triangle makes every atom nontrivial

### Lemma 3.1

For every centre `z`,

\[
                              r_z\ge1.                \tag{3.1}
\]

Consequently

\[
                              s\ge3.                  \tag{3.2}
\]

#### Proof

Suppose `r_z=0`.  Then `L_z=\{z\}`, so all vertices of `N_C(z)` lie on
the induced path `P_z`.  The graph induced by these contacts is therefore
a subgraph of a path.  It is anticomplete to the triangle `N_D(z)`.

If `\rho_z=0`, then `|N_C(z)|=5`, so its path subgraph has an independent
triple.  Adding any vertex of `N_D(z)` gives an independent four-set in
`N(z)`, contrary to (1.2).

Suppose `\rho_z=1`, and let `p` be the pole adjacent to `z`.  Now
`|N_C(z)|=4`.  Since `p` is an endpoint of the induced path `P_z`, it is
adjacent to at most one of those four contacts.  The remaining at least
three path vertices contain an independent pair `a,b`, both nonadjacent to
`p`.  The pole `p` cannot be adjacent to all three vertices of `N_D(z)`,
because then `\{z,p\}\cup N_D(z)` would induce a `K_5`.  Choose
`t\in N_D(z)` missed by `p`.  The four vertices `p,t,a,b` are independent
in `N(z)`, again contradicting (1.2).  This proves (3.1), and (3.2) follows
from (2.3). \(\square\)

## 4. Exact local size estimates

### Lemma 4.1

Fix `z` and abbreviate `r=r_z`, `k=k_z`, and `\rho=\rho_z`.

1. If `r=1`, write `L_z=\{z,v_z\}`.  Then

   \[
    \delta_{{\rm pl},z}=k-d_G(v_z)-1+\rho,
    \qquad k\ge9-\rho,
    \qquad c\ge10-\rho.                             \tag{4.1}
   \]

   Moreover,

   \[
                  zv_z\in E(G),\qquad
                  N_Z(v_z)=\{z\}.                   \tag{4.2}
   \]

2. If `r\ge2`, then

   \[
                  k\ge2r+8-\rho,
                  \qquad c\ge3r+8-\rho.             \tag{4.3}
   \]

#### Proof

Suppose first that `r=1`.  Connectivity of `L_z` gives the edge `zv_z`.
Every neighbour of `v_z` lies in `H` and every edge incident with `L_z`
belongs to `A_z^+`.  In the all-rainbow profile the degree of `z` in
`A_z^+` is

\[
                            c_z+2=7-\rho.
\]

Thus

\[
                         e(A_z^+)=d_G(v_z)+6-\rho.
\]

Since `v(A_z)=k+4`, subtracting this equality from (2.6) gives the first
identity in (4.1).  Minimum degree gives `k\ge9-\rho`, and
`U_z\subseteq C-\{v_z\}` gives the last inequality.  The other four roots
lie in a component of `H-P_z` distinct from `L_z`; hence none is adjacent
to `v_z`, proving (4.2).

Now let `r\ge2`.  The planar graph induced by `L_z` has `r+1` vertices,
so it has at most `3r-3` edges.  Sum degrees over `L_z` in `A_z^+` and
subtract its internal edges.  The `r` vertices in `C` have degree at least
eight and `z` has degree `7-\rho`, whence

\[
 e(A_z^+)\ge8r+7-\rho-(3r-3)=5r+10-\rho.           \tag{4.4}
\]

The right side of (2.6) is `3r+k+2`.  Comparison proves the first
inequality in (4.3), and `c\ge r+k` proves the second. \(\square\)

## 5. Preliminary order-eleven bound

### Theorem 5.1

In the minimally infeasible all-rainbow `t=5` row,

\[
                              |C|\ge11.               \tag{5.1}
\]

#### Proof

Equations (1.4), (1.5), and (3.2) give

\[
             2s\le4c-31+b,
             \qquad 4c+b\ge37.                      \tag{5.2}
\]

We exclude `c=8,9,10`.

If `c=8`, equality in (5.2) forces `b=5` and `s=3`.  Every atom has
`r=1` and `\rho=1`, but (4.1) gives `k\ge8>c-1`, a contradiction.

Let `c=9`.  If `b\le4`, then `s\le4`, so a pole-free centre has `r=1`
and (4.1) gives `k\ge9>c-1`.  If `b=5`, then `s\le5`; every centre has
`r=1`, `\rho=1`, and `k=8`.  Here `U_z=C-\{v_z\}` lies on the induced
path `P_z`, so `e(C[U_z])\le7`.  Also (4.1) gives
`d_G(v_z)\le8`, and the edge `zv_z` leaves at most seven `C`-edges at
`v_z`.  Hence `m\le14`, contrary to
`m=2c-1+s+g\ge20`.

Let `c=10`.  Equation (5.2) gives `s\le7`, so every atom has `r\le2`.
The estimate (4.3) excludes `r=2`, and hence every atom has `r=1`.

If `b\le4`, choose a pole-free centre.  Equation (4.1) gives `k=9`.
The same induced-path count gives

\[
                         m\le8+7=15,
\]

contrary to `m\ge22`.

It remains that `b=5`.  Every centre has `\rho=1` and `k\in\{8,9\}`.
The value `k=9` would give `m\le8+8=16`, again impossible.  Thus `k=8`
for every centre.  For fixed `z`, write

\[
                         C=U_z\mathbin{\dot\cup}
                           \{v_z,w_z\}.              \tag{5.3}
\]

The vertex `w_z` is anticomplete to `\{z,v_z\}`.  The induced path and
(4.1) give

\[
 m\le e(C[U_z])+e(v_z,U_z)+e(w_z,U_z)
    \le7+7+8=22.                                    \tag{5.4}
\]

The lower bound in (1.4) is also twenty-two.  Equality therefore holds
throughout: `s=3`, `g=0`, `m=22`, every vertex of `C` has degree eight,
`v_z` is adjacent to seven vertices of `U_z` and only to `z` outside
`C`, while `w_z` is adjacent to all eight vertices of `U_z` and has no
boundary neighbour.

By (4.2), the five vertices `v_z` are distinct.  No `w_z` equals one of
them, and distinct centres have distinct `w_z`: in `G[C]`, the vertex
`w_z` has degree eight and its unique nonneighbour is `v_z`.  Hence the
ten vertices of `C` are exactly the five pairs `\{v_z,w_z\}`.  In the
complement of `G[C]`, each `w_z` has degree one, with neighbour `v_z`,
whereas each `v_z` has degree two.  Its second complement-neighbour cannot
be any `w_y`, so it is another vertex `v_y`.  The graph induced in the
complement by the five vertices `v_z` would therefore be one-regular,
which is impossible on five vertices.  This excludes `c=10` and proves
(5.1). \(\square\)

## 6. Eliminating order eleven

### Lemma 6.1 (forced order-eleven normal form)

If `c=11`, then all of the following hold.

1. Every centre is pole-incident:

   \[
                         b=5,\qquad \rho_z=1
                         \quad(z\in Z).              \tag{6.1}
   \]

2. Every atom has

   \[
    r_z=1,\qquad k_z=8,
    \qquad L_z=\{z,v_z\},
    \qquad d_G(v_z)=8,                              \tag{6.2}
   \]

   and

   \[
    \delta_{{\rm pl},z}=0,
    \qquad \delta_{{\rm crit},z}=s-3.              \tag{6.3}
   \]

3. The five vertices `v_z` are distinct and satisfy

   \[
                         N_Z(v_z)=\{z\}.             \tag{6.4}
   \]

   The two-set

   \[
            W_z=C-\bigl(U_z\cup\{v_z\}\bigr)       \tag{6.5}
   \]

   is anticomplete to `\{z,v_z\}`.

4. The graph `G[C-\{v_z\}]` is connected.  If

   \[
                         a_z=|N_{\{p,q\}}(v_z)|,
   \]

   then in fact

   \[
    a_z=2,
    \qquad \{p,q\}\subseteq N(v_z),
    \qquad d_C(v_z)=5.                               \tag{6.6}
   \]

   Exactly three vertices of `U_z` are nonadjacent to `v_z`; they are
   precisely the three vertices of `N_C(z)-\{v_z\}`.

5. The remaining scalars satisfy exactly

   \[
    3\le s\le9,
    \qquad g+h=26-2s,
    \qquad m=21+s+g.                                \tag{6.7}
   \]

#### Proof

Suppose first that `b\le4`.  Then `s\le8`.  Choose a pole-free centre.
The bound (4.3) excludes `r\ge2`, so `r=1` and
`k\in\{9,10\}`.  If `k=10`, the induced path and (4.1) give
`m\le9+8=17`, contrary to `m\ge24`.  If `k=9`, let `w` be the one
remaining vertex of `C`.  Then

\[
                         m\le8+7+9=24.               \tag{6.8}
\]

Equality with (1.4) would force `s=3` and `g=0`, while equality in (6.8)
makes `w` adjacent to all nine vertices of `U_z`.  This gives
`d_G(w)\ge9`, contradicting `g=0`.  Hence (6.1) holds.

Now `\rho_z=1` for every centre and (5.2) gives `s\le9`.  Equation (4.3)
again excludes `r\ge2`, so `r=1`.  The value `k=10` gives
`m\le9+9=18<24`.

Suppose `k=9`, and let `w` be the unique vertex outside
`U_z\cup\{v_z\}`.  Put

\[
 a=e(C[U_z]),\qquad d=e(v_z,U_z),\qquad e=e(w,U_z).
\]

Then `a\le8`, `d\le8`, `e\le9`, and `m=a+d+e`.  Define

\[
                         x=8-a,\quad y=8-d,\quad t=9-e.
\]

Using (1.4) gives

\[
                         x+y+t=25-m=4-s-g.           \tag{6.9}
\]

The right side is either zero or one.  If it is zero, then `y=t=0`.
The edge `zv_z` makes `d_G(v_z)\ge9`, while `e=9` makes
`d_G(w)\ge9`; hence `g\ge2`.  But (6.9), with `s\ge3`, permits
`g\le1`.  If the right side is one, then `s=3,g=0`, while at least one of
`y,t` is zero and therefore at least one of `v_z,w` has degree at least
nine.  This is again a contradiction.  Thus `k=8`.

The exact formula in (4.1) now gives `d_G(v_z)=8` and
`\delta_{{\rm pl},z}=0`; (2.3) gives (6.3).  Statements (6.4)--(6.5)
follow from (2.2), (4.2), and the definition of `U_z`.

The open interior of `P_z` is a connected path in `C` and contains
`U_z`.  Let `R` be a component of `C-V(P_z)` other than the singleton
`\{v_z\}`.  It has no edge to `v_z`, since such an edge would put `R` in
the component `L_z`.  Because `G[C]` is connected, `R` therefore has an
edge to an internal vertex of `P_z`.  It follows that every vertex of
`C-\{v_z\}` is joined to the open interior of `P_z` inside that graph,
which proves connectivity.

Put `a_z=|N_{\{p,q\}}(v_z)|`.  The degree-eight vertex `v_z` is
exceptional because `G` has no literal `K_5`, so (1.2) applies to it.
Every `C`-neighbour of `v_z` lies in `U_z` and hence on the induced path
`P_z`.  Its exact degree, its unique centre neighbour `z`, and (6.4) give

\[
                         d_C(v_z)=7-a_z.             \tag{6.8}
\]

If `a_z=0`, its seven `C`-neighbours induce a subgraph of a path and
contain an independent four-set in `N(v_z)`, contrary to (1.2).  If
`a_z=1`, let `t` be its unique pole neighbour.  Since `t` is an endpoint
of the induced path `P_z`, it sees at most one of the six `C`-neighbours
of `v_z`.  The other at least five induce a subgraph of a path and contain
an independent triple.  Together with `t` they again form an independent
four-set in `N(v_z)`.  Therefore `a_z=2`, proving (6.6).

Since `|U_z|=8`, exactly

\[
                         8-d_C(v_z)=3
\]

members of `U_z` miss `v_z`, and their membership in `U_z` forces them to
be adjacent to `z`.  Equation (1.1) says that `z` has exactly three
`C`-neighbours other than `v_z`, so these sets are equal.  Finally, (6.7)
is the specialization of (1.4), using `b=5`, together with (1.5) and
(3.2).
\(\square\)

### Theorem 6.2 (order-twelve equality shore)

In the minimally infeasible all-rainbow `t=5` row,

\[
                              |C|\ge12.               \tag{6.9}
\]

#### Proof

Theorem 5.1 leaves only `c=11` to exclude.  Fix a centre `z` and use the
notation of Lemma 6.1.  Put

\[
                         A_z=N_C(z)-\{v_z\}.
\]

By Lemma 6.1, the three vertices of `A_z` are precisely the members of
`U_z` nonadjacent to `v_z`.  They lie on the induced path `P_z`, so two of
them, say `x,y`, are nonadjacent.  Choose any `t\in N_D(z)`.  There are no
edges between `C` and `D`, and hence

\[
                              \{v_z,x,y,t\}
\]

is an independent four-set in `N(z)`, contrary to (1.2).  Thus `c=11`
is impossible, and Theorem 5.1 proves (6.9). \(\square\)

## 7. Eliminating order twelve

### Theorem 7.1 (order-thirteen equality shore)

In the minimally infeasible all-rainbow `t=5` row,

\[
                              |C|\ge13.               \tag{7.1}
\]

#### Proof

Assume `c=12`.  The estimate (4.3) excludes `r_z\ge2` for both
`\rho_z=0` and `\rho_z=1`, so every atom has `r_z=1`.  Fix `z`, abbreviate
`v=v_z`, `U=U_z`, `k=k_z`, and `\rho=\rho_z`, and put

\[
 B=N_C(z)-\{v\},\qquad X=N_C(v),\qquad
 a=|N_{\{p,q\}}(v)|,qquad j=|B\cap X|.              \tag{7.2}
\]

Then `|B|=4-\rho`, `U=B\cup X`, and `d_G(v)=1+a+|X|`.  Substitution in
(4.1) gives the exact identity

\[
                         \delta_{{\rm pl},z}=2-a-j.   \tag{7.3}
\]

The triangle `N_D(z)` is anticomplete to `N_C(z)=\{v\}\cup B`.  Hence
(1.2) gives

\[
                         \alpha(G[\{v\}\cup B])\le2. \tag{7.4}
\]

Because `B` lies on the induced path `P_z`, (7.4) says that the members
of `B` missed by `v` form a clique of order at most two.

Suppose first that `\rho=0`.  Then `|B|=4`, so `j\ge2`; equations
(7.3) and `a\ge0` force

\[
                  a=0,\qquad j=2,qquad
                  \delta_{{\rm pl},z}=0,qquad
                  d_G(v)=k-1.                       \tag{7.5}
\]

The value `k=9` makes `d_G(v)=8`.  The vertex `z` misses five of the seven
members of `X`; three of those five are independent on `P_z`, giving with
`z` an independent four-set in `N(v)`, contrary to (1.2).  The value
`k=11` gives

\[
                         m\le10+9=19<26.
\]

If `k=10`, let `w` be the unique member of
`C-(U\cup\{v\})`.  Then

\[
                         m\le9+8+10=27.              \tag{7.6}
\]

But (1.4), (2.3), and `d_G(v)=9` give `m\ge27`.  Equality would force
`s=3`, `g=1`, and `w` adjacent to all ten vertices of `U`.  Then
`d_G(w)\ge10`, so `v,w` contribute at least three to `g`, a contradiction.
Thus every centre is pole-incident.

Now `\rho=1` and `|B|=3`.  Equation (7.4) gives `j\ge1`, while (7.3)
gives `a+j\le2`.  Thus

\[
                         (a,j)\in\{(0,1),(0,2),(1,1)\}. \tag{7.7}
\]

For `k=8`, minimum degree excludes `(a,j)=(0,1)`; in either remaining
case `d_G(v)=8`, and `z` misses five members of `X`.  Three independent
missed members together with `z` contradict (1.2) in `N(v)`.  The value
`k=11` gives `m\le20<26`.

Let `k=10` and again let `w` be the unique vertex outside `U\cup\{v\}`.
In the three cases of (7.7), respectively, the planar deficit, degree of
`v`, and edge upper bound are

\[
\begin{array}{c|c|c|c}
 (a,j)&\delta_{{\rm pl},z}&d_G(v)&m\text{ at most}\
 \hline
 (0,1)&1&9&27\\
 (0,2)&0&10&28\\
 (1,1)&0&10&27.
\end{array}                                         \tag{7.8}
\]

The first and third rows are smaller than the lower bound
`m=23+s+g`; in the first row use `s\ge4,g\ge1`, and in the third use
`s\ge3,g\ge2`.  In the middle row equality would require
`s=3,g=2,m=28` and would make `w` adjacent to every vertex of `U`.
Then `v` and `w` each have excess at least two, again a contradiction.
Consequently `k=9`.

For `k=9`, the case `(a,j)=(0,1)` has `d_G(v)=8`; the same independent-set
argument in `N(v)` excludes it.  Hence every centre has

\[
 k_z=9,qquad d_G(v_z)=9,qquad
 a_z\in\{0,1\},qquad d_C(v_z)=8-a_z.                \tag{7.9}
\]

The five vertices `v_z` are distinct by (4.2).  Fix `z` and put

\[
                         W_z=C-(U_z\cup\{v_z\}).      \tag{7.10}
\]

This set has order two.  For `w\ne z`, if `v_w\in U_z`, then the induced
path containing `U_z` gives `d_{G[U_z]}(v_w)\le2`.  Thus `v_w` has at
least six nonneighbours in `C`.  But (7.9) says that it has only

\[
                  11-d_C(v_w)=3+a_w\le4
\]

such nonneighbours.  Therefore all four vertices `v_w`, `w\ne z`, must
belong to the two-set `W_z`, an impossibility.  This excludes `c=12`;
Theorem 6.2 now proves (7.1). \(\square\)

## 8. Eliminating order thirteen

### Theorem 8.1 (order-fourteen equality shore)

In the minimally infeasible all-rainbow `t=5` row,

\[
                              |C|\ge14.               \tag{8.1}
\]

#### Proof

Assume `c=13`.  First suppose that some pole-incident centre has
`r_z=2`.  Equations (4.3) and `c\ge r_z+k_z` force `k_z=11`.  Both sides
of (4.4) and the planar upper bound are then nineteen, so equality holds
throughout their derivation.  If

\[
                         L_z\cap C=\{u,v\},
\]

then `u,v` both have degree eight and `G[L_z]` is the triangle `zuv`.
The vertices `u,v` have no neighbours in `D` or in `Z-\{z\}`.  Since
`U_z=C-\{u,v\}` induces a subgraph of `P_z`,

\[
 e(C)\le e(C[U_z])+e_C(\{u,v\},U_z)+1
      \le10+12+1=23.                                \tag{8.2}
\]

Here the middle term is at most twelve because the degree sum of `u,v`
spends two incidences on `z` and two on their internal edge; pole
incidences can only lower it.  But (2.3) gives `s\ge6`, and hence (1.4)
gives `m\ge25+6=31`, a contradiction.  The estimate (4.3) excludes every
larger atom, so all atoms have `r_z=1`.

Use the notation `B,X,a,j` from (7.2).  The identities (7.3)--(7.4) still
hold.  If `\rho_z=0`, they give (7.5).  The degree-eight neighbourhood
argument again excludes `k_z=9`; the induced-path edge count excludes
`k_z=12`.  At `k_z=11` it gives `m\le30`, while
`m=25+s+g\ge30`.  Equality would make the unique leftover vertex have
degree at least eleven; together with `d_G(v_z)=10`, this forces `g\ge5`
instead of the required `g=2`.  Therefore a pole-free singleton atom has

\[
                         k_z=10,qquad d_G(v_z)=9.     \tag{8.3}
\]

If `\rho_z=1`, (7.7) holds.  The same arguments exclude `k_z=8` and
`k_z=12`.  At `k_z=11`, the three cases in (7.7) give respectively

\[
 (\delta_{{\rm pl},z},d_G(v_z),m_{\max})
       =(1,10,30),(0,11,31),(0,11,30).               \tag{8.4}
\]

The first and third are below `25+s+g`; equality in the middle makes the
leftover vertex contribute three further units of excess, a contradiction.
At `k_z=9`, its positive-deficit case again contradicts (1.2) in the
degree-eight neighbourhood of `v_z`.  Thus every pole-incident singleton
atom satisfies

\[
 k_z\in\{9,10\},qquad d_G(v_z)\in\{9,10\},qquad
 a_z\le1.                                            \tag{8.5}
\]

It follows from (8.3)--(8.5) that every atom vertex has at most five
nonneighbours in `C`.  Fix `z`.  If `w\ne z` and `v_w\in U_z`, then
`|U_z|\ge9` and the induced path gives `d_{G[U_z]}(v_w)\le2`.  Thus
`v_w` has at least six nonneighbours already inside `U_z`, a contradiction.
All four distinct vertices `v_w`, `w\ne z`, must therefore lie in

\[
                         C-(U_z\cup\{v_z\}),
\]

whose order is at most three.  This is impossible.  Hence `c=13` does not
occur, and Theorem 7.1 proves (8.1). \(\square\)

## 9. Eliminating order fourteen

### Theorem 9.1 (order-fifteen equality shore)

In the minimally infeasible all-rainbow `t=5` row,

\[
                              |C|\ge15.               \tag{9.1}
\]

#### Proof

Assume `c=14`.  We first exclude nonsingleton atoms.  The estimate (4.3)
leaves only `r_z=2`; it forces `k_z=12` when `\rho_z=0` and
`k_z\in\{11,12\}` when `\rho_z=1`.  Put

\[
                         L_z\cap C=\{u,v\},
\]

let `e_L=e(G[L_z])`, and let `A` count the edges from `\{u,v\}` to the
two poles.  The exact planar slack calculation is

\[
 \delta_{{\rm pl},z}
   =k_z+1+\rho_z-d_G(u)-d_G(v)+e_L.                  \tag{9.2}
\]

The vertices `u,v` see neither `D` nor a centre other than `z`, so the
number of `C`-edges having at least one end in `\{u,v\}` is

\[
 d_G(u)+d_G(v)-e_L-A
   =k_z+1+\rho_z-\delta_{{\rm pl},z}-A
   \le k_z+2.                                        \tag{9.3}
\]

For `k_z=12`, equations (9.3) and the induced-path bound give
`m\le11+14=25<33`.  The pole-free case is included here.  It remains to
consider `\rho_z=1,k_z=11`.  Let `w` be the unique vertex outside
`L_z\cup U_z`, and write

\[
 x=10-e(C[U_z]),qquad t=11-e(w,U_z).
\]

The set outside the attachment boundary is anticomplete to `L_z`, so
(9.3) is exact with its displayed deficits and

\[
 m=34-(x+t+\delta_{{\rm pl},z}+A).                  \tag{9.4}
\]

On the other hand, (1.4) and (2.3) give

\[
 m=27+s+g
   =33+\delta_{{\rm pl},z}
        +\delta_{{\rm crit},z}+g.                   \tag{9.5}
\]

Equations (9.4)--(9.5) imply `t+g\le1`.  But
`d_G(w)\ge e(w,U_z)=11-t`, so `g\ge3-t`, a contradiction.  Thus every
atom has `r_z=1`.

Use again the notation `B,X,a,j` from (7.2).  For `\rho_z=0`, equations
(7.3)--(7.5) and the degree-eight neighbourhood argument give `k_z\ge10`.
The values `k_z=13` and `k_z=12` have respective edge upper bounds
twenty-three and thirty-three.  The first is impossible; equality in the
second would require `s=3,g=3` but would make the degree-eleven atom vertex
and the degree-at-least-twelve leftover vertex contribute at least seven
to `g`.  Hence

\[
                 \rho_z=0\quad\Longrightarrow\quad
                 k_z\in\{10,11\}.                  \tag{9.6}
\]

For `\rho_z=1`, the possibilities (7.7) remain.  The degree-eight
neighbourhood argument excludes `k_z=8` and the positive-deficit case at
`k_z=9`.  The value `k_z=13` gives `m\le24`.  At `k_z=12`, the three
possibilities in (7.7) give

\[
 (\delta_{{\rm pl},z},d_G(v_z),m_{\max})
       =(1,11,33),(0,12,34),(0,12,33).               \tag{9.7}
\]

The first and third are below `m=27+s+g`; equality in the middle makes
the leftover vertex contribute four further units of excess beyond the
four from `v_z`.  Therefore every pole-incident singleton atom has
`k_z\in\{9,10,11\}`, and in every surviving singleton atom

\[
                         d_G(v_z)\ge9,qquad a_z\le1. \tag{9.8}
\]

Thus every atom vertex has at most six nonneighbours in `C`.  If some
`k_z\ge10`, then no other atom vertex can lie in `U_z`: membership in its
induced path would give at least `k_z-3\ge7` nonneighbours.  All four
other atom vertices would have to lie in
`C-(U_z\cup\{v_z\})`, whose order is at most three.  Consequently every
atom has the exact form

\[
 \rho_z=1,quad r_z=1,quad k_z=9,quad d_G(v_z)=9,
 \quad \delta_{{\rm pl},z}=0,quad |W_z|=4,          \tag{9.9}
\]

and, with `a_z,j_z` as in (7.2),

\[
                         (a_z,j_z)\in\{(0,2),(1,1)\}. \tag{9.10}
\]

It remains to couple the five exact atoms.  Let

\[
                         V=\{v_z:z\in Z\},
                         \qquad F=G[V].               \tag{9.11}
\]

For distinct centres `z,w`, the definition `U_z=B_z\cup X_z` and
`N_Z(v_w)=\{w\}` give

\[
                         v_w\in U_z
              \quad\Longleftrightarrow\quad
                         v_zv_w\in E(F).              \tag{9.12}
\]

If `a_w=0`, then `v_w` has five nonneighbours in `C`; (9.12) cannot put
it in a nine-vertex path subgraph, where it would have at least six.
Hence `v_w` is isolated in `F`.

Suppose `v_zv_w` is an edge of `F`.  Then `a_w=1`, and `v_w` has exactly
six nonneighbours in `C`.  Its membership in `U_z` puts all six of them
inside `U_z`.  Every member of `V` nonadjacent to `v_z` lies in `W_z` by
(9.12), and is therefore adjacent to `v_w`.  Thus every edge of `F` is a
dominating edge.  If `F` is nonempty, it has no isolated vertex, so every
`a_z=1`.  Moreover, nonadjacency is transitive, and hence `F` is a complete
multipartite graph.

For fixed `z`, every neighbour `v_w` of `v_z` lies on the induced path
`P_z` and is adjacent to exactly one of its endpoints `p,q`.  Each endpoint
has at most one neighbour among the vertices of an induced path.  Therefore

\[
                              d_F(v_z)\le2.            \tag{9.13}
\]

In a complete multipartite graph on five vertices with maximum degree at
most two, every part would have order at least three.  Two nonempty parts
would then have total order at least six.  Thus `F` cannot be nonempty.

Finally suppose `F` is empty.  Equations (9.9) and (9.12) give

\[
                         W_z=V-\{v_z\},qquad
                         U_z=C-V                       \tag{9.14}
\]

for every `z`.  Each other atom vertex has at least seven neighbours in
the common nine-set `C-V`, so none can lie on the induced path `P_z`,
which already contains that entire nine-set.  Hence the internal
`C`-vertices of `P_z` are exactly `C-V`.  Each pole has at most one
neighbour in `C-V`, while (9.10) gives at most five pole--`V` edges.
Therefore `h\le2+5=7`, contrary to (1.5).  This eliminates `c=14`, and
Theorem 8.1 proves (9.1). \(\square\)

## 10. Exact scope

The order bound and normal form use all of the following: minimal
five-root infeasibility, the all-rainbow contact triangles, the
degree-eight and neighbourhood-independence conclusions, the four
equality-shore critical-edge paths, and the constructive atom inside the
Du--Li--Xie--Yu proof.  They do not apply to the critical-completion row of
the global palette alternative or to an arbitrary five-root-infeasible
shore.

The rows through order fourteen are empty by Theorems 6.2, 7.1, 8.1, and
9.1.  At order fifteen and above, the atom identity still gives
`s=3r_z+\delta_{{\rm pl},z}+\delta_{{\rm crit},z}` separately for each
centre, but it does not force singleton atoms or synchronize their witness
paths.  The theorem therefore removes seven finite rows without yet aligning
the two shore colourings or constructing a terminal `K_7^-` minor.
