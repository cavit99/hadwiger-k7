# Five-root atom boundary incidence and crossed overlap

**Status:** written proof; separate hash-pinned internal audit **GREEN** in
[`hc7_k7minus_five_centre_t5_atom_overlap_budget_audit.md`](hc7_k7minus_five_centre_t5_atom_overlap_budget_audit.md).
This note continues the audited
[order-fifteen equality-shore theorem](hc7_k7minus_five_centre_t5_atom_slack.md)
without an order bound.  It proves a boundary-incidence inequality for each
of the five atoms, identifies an exact order-seven cut whenever two atom
interiors have a tight overlap, and records an unbounded numerical family
showing why these counts alone cannot finish the all-rainbow `t=5` row.
It does not prove the `K_7^-` six-colour conjecture.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the minimally infeasible all-rainbow `t=5` setting of the cited
theorem.  Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`C,D` are the two full components of `G-S`, and, for every `z\in Z`,

\[
 |N_D(z)|=3,\qquad N_D(z)\cong K_3,
 \qquad |N_C(z)|=5-\rho_z,
 \qquad \rho_z=|N_{\{p,q\}}(z)|\in\{0,1\}.          \tag{1.1}
\]

Put

\[
 b=\sum_{z\in Z}\rho_z.
\]

The audited
[exact boundary matching theorem](hc7_k7minus_five_centre_t4_boundary_incidence.md)
gives

\[
                              2\le b\le5.             \tag{1.2}
\]

For every `z`, the constructive four-root witness supplies an induced
`p`--`q` path `P_z`, a component `L_z` containing `z`, and

\[
 R_z=L_z\cap C,\qquad r_z=|R_z|\ge1,
 \qquad U_z=N_H(L_z)-\{p,q\}\subseteq V(P_z)\cap C,
 \qquad k_z=|U_z|,                                  \tag{1.3}
\]

where `H=G[C\cup Z\cup\{p,q\}]`.  The other four centres lie in one
component of `H-P_z` distinct from `L_z`.  There are nonnegative deficits
such that

\[
 s=3r_z+\delta_{{\rm pl},z}+\delta_{{\rm crit},z}. \tag{1.4}
\]

The local atom estimates are

\[
\begin{array}{ll}
 r_z=1:& k_z\ge9-\rho_z,\\[2mm]
 r_z\ge2:& k_z\ge2r_z+8-\rho_z.
\end{array}                                         \tag{1.5}
\]

Finally, if

\[
 c=|C|,\quad m=e(C),\quad
 g=\sum_{x\in C}(d_G(x)-8),\quad h=e(C,\{p,q\}),
\]

then

\[
 m=2c-1+s+g,qquad 2s=4c-23+b-g-h,qquad h\ge8.    \tag{1.6}
\]

## 2. The atom boundary-incidence theorem

### Theorem 2.1

For `z\in Z`, put

\[
 W_z=C-(R_z\cup U_z),\qquad w_z=|W_z|,             \tag{2.1}
\]

and define

\[
\begin{aligned}
 q_z&=e(G[R_z\cup\{z\}]),& t_z&=e_G(z,U_z),\\
 \pi_z&=e_G(R_z,\{p,q\}),&
 g(Y)&=\sum_{x\in Y}(d_G(x)-8)\quad(Y\subseteq C).
\end{aligned}                                       \tag{2.2}
\]

Then `R_z,U_z,W_z` partition `C`, `R_z` is anticomplete to `W_z`,
`q_z\ge r_z`, and

\[
 \boxed{\ k_z(5-w_z)-3r_z+\delta_{{\rm pl},z}+q_z
              +\pi_z+t_z+g(U_z)\le20-b.\ }         \tag{2.3}
\]

Consequently,

\[
                              w_z\ge4.               \tag{2.4}
\]

If `w_z=4`, then a singleton atom has `c\le25`, while a nonsingleton atom
satisfies

\[
 c\le
 3\left\lfloor\frac{15+\rho_z-b}{2}\right\rfloor+24-b
 \le43.                                             \tag{2.5}
\]

In particular,

\[
\begin{aligned}
 c\ge41, w_z=4&\Longrightarrow b=2\text{ and }\rho_z=1,\\
 c\ge44&\Longrightarrow |W_z|\ge5\quad(z\in Z).
\end{aligned}                                       \tag{2.6}
\]

#### Proof

The definition of `U_z` gives the partition and the anticompleteness.
Connectedness of `L_z` gives `q_z\ge r_z`.  The planar atom `A_z^+` has

\[
 q_z+e(R_z,U_z)+t_z+\pi_z+2
\]

edges, where the last term consists of the two completed pole edges at
`z`.  Hence the definition of the planar deficit gives

\[
 e(R_z,U_z)=3r_z+k_z-\delta_{{\rm pl},z}
                         -q_z-\pi_z-t_z.             \tag{2.7}
\]

The induced-path set `U_z` has at most `k_z-1` internal edges and at most
two edges to the poles.  Also `e(U_z,W_z)\le k_zw_z`.  Vertices of `C`
have no neighbours in `D`, so degree summation over `U_z`, followed by
(2.7), gives

\[
 e(U_z,Z)\ge k_z(5-w_z)-3r_z+\delta_{{\rm pl},z}
                         +q_z+\pi_z+t_z+g(U_z).      \tag{2.8}
\]

The centre `z` has a `C`-neighbour in `R_z`.  Every centre in `Z-\{z\}`
has a `C`-neighbour in its common component of `H-P_z`: the centres are
independent and the poles were deleted with the path.  Thus `U_z` omits a
`C`-contact of each centre.  Their total number of `C`-contacts is `25-b`,
and therefore

\[
                              e(U_z,Z)\le20-b.        \tag{2.9}
\]

This proves (2.3), and hence

\[
                         k_z(5-w_z)-2r_z\le20-b\le18. \tag{2.10}
\]

If `w_z\le2`, the left side is at least

\[
 3(9-\rho_z)-2>18
 \quad\text{when }r_z=1,
\]

and at least

\[
 3(2r_z+8-\rho_z)-2r_z>18
 \quad\text{when }r_z\ge2.
\]

Suppose `w_z=3`.  For `r_z=1`, (2.10) gives `k_z\le10`, so
`c=r_z+k_z+w_z\le14`.  For `r_z\ge2`, equations (1.5) and (2.10) force

\[
                         r_z=2,\quad \rho_z=1,\quad k_z=11. \tag{2.11}
\]

Set `\eta_z=3r_z-3-q_z`.  Planarity gives `\eta_z\ge0`, while exact
degree summation in the atom gives

\[
 k_z=2r_z+8-\rho_z+g(R_z)+\eta_z
                         +\delta_{{\rm pl},z}.       \tag{2.12}
\]

Equality in (2.11) makes `g(R_z)=\eta_z=
\delta_{{\rm pl},z}=0`, and hence `q_z=3`.  The left side of (2.3) is
then at least `2(11)-3(2)+3=19`, contrary to `20-b\le18`.  Since the
audited order theorem gives `c\ge15`, this proves (2.4).

Let `w_z=4`.  If `r_z=1`, then `q_z=1`, so (2.3) gives
`k_z\le22-b\le20` and `c\le25`.  If `r_z\ge2`, substitute (2.12) and
`q_z=3r_z-3-\eta_z` into (2.3).  This gives

\[
 2r_z+5-\rho_z+g(R_z)+2\delta_{{\rm pl},z}
                  +\pi_z+t_z+g(U_z)\le20-b.         \tag{2.13}
\]

Thus

\[
 r_z\le\left\lfloor\frac{15+\rho_z-b}{2}\right\rfloor. \tag{2.14}
\]

Since `q_z\ge r_z`, one has `\eta_z\le2r_z-3`.  Dropping nonnegative
terms in (2.13) and using (2.12) now gives

\[
 c=r_z+k_z+4\le3r_z+24-b,
\]

which proves (2.5).  Its displayed special cases give (2.6). \(\square\)

## 3. The whole witness path

### Theorem 3.1

Put

\[
 Q_z=V(P_z)\cap C,qquad \ell_z=|Q_z|,qquad f_z=c-\ell_z.
                                                               \tag{3.1}
\]

Then

\[
 \boxed{\ (c-f_z)(6-f_z)+g(Q_z)\le20-b\le18.\ }    \tag{3.2}
\]

Consequently

\[
 f_z\ge5,qquad c\ge24\Longrightarrow f_z\ge6.    \tag{3.3}
\]

#### Proof

The vertices `Q_z` induce a path with `\ell_z-1` edges.  Its endvertices
give exactly two edges to `p,q`, and
`e(Q_z,C-Q_z)\le\ell_zf_z`.  Since `C` is anticomplete to `D`, degree
summation gives

\[
                         e(Q_z,Z)\ge
                         \ell_z(6-f_z)+g(Q_z).       \tag{3.4}
\]

Every centre has a `C`-contact off `P_z`, as in (2.9), so
`e(Q_z,Z)\le20-b`.  This proves (3.2).  If `c\ge15` and `f_z\le4`, the
left side of (3.2) is at least `2(c-4)>18`.  Hence `f_z\ge5`.  If
`f_z=5`, then (3.2) gives `c-5\le18`, so `c\le23`. \(\square\)

## 4. The exact crossed-overlap cut

### Theorem 4.1

For every `z`,

\[
 N_Z(R_z)\subseteq\{z\},\qquad N_C(R_z)-R_z\subseteq U_z, \tag{4.1}
\]

and `G[C-R_z]` is connected and adjacent to `p,q` and every centre in
`Z-\{z\}`.

Let `z\ne w`, and let `X` be a connected component of
`G[R_z\cap R_w]`.  Then `N_Z(X)=\varnothing` and

\[
 N_C(X)\subseteq
 (R_z\cap U_w)\cup(R_w\cap U_z)\cup(U_z\cap U_w).   \tag{4.2}
\]

Consequently

\[
 \left|\bigl((R_z\cap U_w)\cup(R_w\cap U_z)
              \cup(U_z\cap U_w)\bigr)
              \cup N_{\{p,q\}}(X)\right|\ge7.       \tag{4.3}
\]

If equality holds, the displayed set is `N_G(X)` and gives an exact
order-seven separation with open side `X\subsetneq C`.  Moreover,
`R_z\cap R_w\ne\varnothing` forces

\[
                         R_z\cap U_w\ne\varnothing,
              \qquad    R_w\cap U_z\ne\varnothing. \tag{4.4}
\]

#### Proof

The four centres distinct from `z` lie in a component of `H-P_z`
different from `L_z`, proving (4.1).  The `C`-vertices of `P_z` induce a
connected path.  Every component of `C-P_z` not contained in `R_z` meets
this path, because `G[C]` is connected.  Thus `G[C-R_z]` is connected and
contains neighbours of both poles.  The component containing the other
four centres contains a `C`-neighbour of each of them, because the centres
are independent and the poles lie on the deleted path.

A vertex in `R_z\cap R_w` has no centre neighbour and no neighbour in
`D`.  If a `C`-neighbour of `X` also lay in `R_z\cap R_w`, it would lie in
the same component `X`.  Expanding the two alternatives in (4.1) proves
(4.2).  The set displayed in (4.3) contains `N_G(X)`.  Since it separates
the nonempty set `X` from `D`, seven-connectivity proves (4.3); equality
forces the displayed set to equal `N_G(X)`.

Finally, take a path in `L_w` from a vertex of `R_z\cap R_w` to `w`.
Relative to `P_z`, its ends lie in the distinct components `L_z` and the
component containing `Z-\{z\}`.  Its first intersection with `P_z` lies in
`R_w\cap U_z`.  Interchanging `z,w` gives (4.4). \(\square\)

The equality case gives an actual smaller cut, but this proof does not show
that its boundary colouring is an equality-response five-centre trace.
If (4.3) is strict, the displayed boundary set has order at least eight,
but this gives no descent.  Thus overlap alone is not yet terminal.

## 5. Exact nonclosure of the scalar method

The coefficient `5-w_z` in (2.3) becomes nonpositive at `w_z=5`.
This threshold cannot be passed using only the displayed scalar identities.
For every integer `r\ge2`, assign the following data to every atom:

\[
\begin{gathered}
 \rho=1,\quad b=5,\quad q=r,\quad \eta=2r-3,
 \quad \delta_{\rm pl}=0,\\
 k=4r+4,\quad w=5,\quad c=5r+9,\quad m=20r+22,\\
 g=0,\quad h=8,\quad f=r+5,\\
 s=10r+5,qquad \delta_{\rm crit}=7r+5.             \tag{5.1}
\end{gathered}
\]

Take `t=3`, `\pi=0`, and let the internal graph counted by `q` be a tree
with one edge from `z` into `R`.  Then (1.4), (1.6), (2.3), (2.12), and
(3.2) all hold; the left side of (2.3) is `-2r+3\le15`.  Also
`|Q_z|=c-f=4r+4=k`, so the path-size data are consistent with
`U_z\subseteq Q_z\subseteq C-R_z`.

These are numerical data, not a graph construction and not a
counterexample to a graph-theoretic statement.  They prove the following
recorded negative finding / route nonclosure:

> The global slack identities, the exact atom identities, and the induced-
> path degree and boundary-incidence inequalities do not imply an upper
> bound on `c`.

A terminal continuation must therefore use additional structure of the
sets `W_z` of order at least five, or it must upgrade the crossed trace in
Theorem 4.1 to compatible shore colourings, a prescribed minor model, or an
anchored smaller equality-response cut.
