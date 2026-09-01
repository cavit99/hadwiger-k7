# Elimination of the two-component literal-shore split

**Status.**  Written unbounded theorem; the adjacent audit identifies the
exact checked revision.  No finite computation is used.

Here `K_7^-` denotes `K_7` with one edge deleted.

## 1. Theorem

Let `G` be a vertex-minimal seven-connected `K_7^-`-minor-free graph
containing a specified literal `K_{4,4}` with shores `S_0,S_1`.  Let
`a,p,b in V(G)-(S_0 union S_1)` satisfy

\[
\begin{aligned}
 N_G(a)&=\{p,b\}\mathbin{\dot\cup}O,\\
 N_G(p)&=\{a,b\}\mathbin{\dot\cup}K,\\
 |O|&=|K|=5,\qquad N_G(a)\cap N_G(p)=\{b\},\\
 (N_G(a)\cap(S_0\cup S_1))
 &\cap(N_G(p)\cap(S_0\cup S_1))=\varnothing .       \tag{1}
\end{aligned}
\]

Here vertex-minimal means that no graph with fewer vertices is
seven-connected, `K_7^-`-minor-free, and contains a literal `K_{4,4}`.

Suppose that the contraction trace of `ap` gives an exact seven-cut

\[
 E=\{a,p\}\mathbin{\dot\cup}T,
 \qquad T=S_0\mathbin{\dot\cup}\{x\},                \tag{2}
\]

and that `G-E` has exactly two components `D,R`, each meeting
`S_1-\{x\}`.  Then `G` contains a `K_7^-` minor, a contradiction.

For sets `Y,Z subseteq V(G)`, write

\[
                         N_Z(Y)=N_G(Y)\cap Z.          \tag{2a}
\]

Equivalently, the literal-shore-split alternative in the audited exact
contraction trace of an adjacent singleton pair cannot occur.  This includes
the unbalanced `1+3` and `1+2` splits and the balanced `2+2` split.

The proof uses the audited exact
[shore-split profiles](hc7_k44_adjacent_singleton_shore_split_profiles.md)
and the audited
[one-sidedness theorem](hc7_k44_balanced_shore_split_one_sidedness.md).

## 2. The unbalanced split

Use the notation supplied by the unbalanced profile theorem.  Thus
`R cap(S-T)={s}`, there is an ordering `epsilon,eta` of `a,p`, and

\[
 R-s\text{ is nonempty and connected},\qquad
 N_G(R-s)=(E-\{\epsilon\})\cup\{s\},                 \tag{3}
\]

while `epsilon s` is an edge and the common neighbour `b` belongs to
`D`.  Put

\[
                         U=S_1-(T\cup\{s\}).          \tag{4}
\]

The set `U` has order three when `x` is exterior and order two when
`x in S_1`.  Since `D` is connected and contains `b` and `U`, choose a
`b`--`U` path in `D` and trim it at its first vertex `u in U`.  Denote
its vertex set by `B_b`.  It is connected and contains exactly one vertex
of `U`.

Define three branch sets

\[
 B_\epsilon=\{\epsilon,s\},\qquad
 B_\eta=(R-s)\cup\{\eta\},\qquad B_b.                \tag{5}
\]

They are pairwise disjoint and connected.  The edge `epsilon eta=ap`
joins the first two, and the edges `b epsilon,b eta` join `B_b` to both;
hence they form a triangle.  Each is adjacent to every vertex of `S_0`:
use `s` for `B_epsilon`, (3) for `B_eta`, and `u` for `B_b`.

It remains to form four core branch sets rooted at `S_0`.  If `x` is
exterior, use the two vertices of `U-\{u\}`.  If `x in S_1`, use the
unique vertex of `U-\{u\}` together with `x`.  In either case attach the
two available `S_1` vertices to two distinct singleton `S_0` roots.  The
four resulting connected branch sets have at least five of their six
mutual contacts: the two enlarged sets are universal to the other core
sets, and only the two pure `S_0` sets may be nonadjacent.

The three sets in (5) form a triangle and are universal to these four
core sets.  The seven-set quotient therefore has at least

\[
                     3+12+5=20                       \tag{6}
\]

contacts and is a `K_7^-` minor.  This eliminates both unbalanced splits.

## 3. A balanced split with exterior vertices in `R`

Suppose now that the split is balanced.  Then `x` is exterior.  Put

\[
                   F=R\cap S_1,\qquad H=D\cap S_1=\{d_1,d_2\},
                   \qquad |F|=|H|=2.                 \tag{7}
\]

For every component `W` of `R-F`, write

\[
                         M_W=E-N_E(W).                \tag{8}
\]

The profile theorem gives

\[
 M_W\cap\{a,p\}\ne\varnothing,\qquad |M_W|\le2,
 \qquad |N_G(W)\cap F|\ge |M_W|.                    \tag{9}
\]

The one-sidedness theorem permits us, after interchanging `a,p`, to assume
that every component missing exactly one endpoint misses `a`.  Every other
component misses both endpoints.  Thus `a` is anticomplete to `R-F`.
Fullness of `R` and the disjoint core label sets in (1) then give distinct
vertices

\[
                 f_a\in N_F(a),\qquad f_p\in N_F(p),
                 \qquad F=\{f_a,f_p\}.               \tag{10}
\]

First suppose that an `a`-component `W` exists.  Then

\[
                    M_W=\{a\}\quad\hbox{or}\quad
                    M_W=\{a,u\}\quad(u\in T).        \tag{11}
\]

The exterior common neighbour `b` does not lie in `R`: it is not in the
core set `F`, and `a` has no neighbour in `R-F`.  Hence `b in D\cup\{x\}`.
Take a path from `b` through `D` to `H`, trimming it at its first vertex
`h_1 in H`; if `b=x`, begin with an edge from `x` to `D`, supplied by
fullness.  Let `B_b` be this path bag and write `H-\{h_1\}=\{h_2\}`.

The three connected branch sets

\[
              A=\{a,f_a\},\qquad P=W\cup\{p\},
              \qquad B_b                              \tag{12}
\]

form a triangle through the edges `ap,ab,pb`.  They are universal to four
core sets rooted at `S_0`, constructed as follows.  Attach `h_2` and
`f_p` to two distinct roots.  If the second vertex `u` in (11) lies in
`S_0`, attach `f_p` specifically to the `u`-rooted set; equation (9) says
that `W` sees both vertices of `F`, so this repairs its unique missed core
root.  In every other case `W` sees all of `S_0`.  The set `A` is universal
through `f_a`, and `B_b` is universal through `h_1`.  The four core sets
form a `K_4^-` quotient, so (6) again gives the target.

Suppose instead that `R-F` is nonempty but has no `a`-component.  Every
component then misses both endpoints.  Choose one, say `W_0`.  Equations
(8)--(9) give

\[
                         M_{W_0}=\{a,p\},             \tag{13}
\]

and `W_0` sees both members of `F`.  The three sets

\[
          W_0\cup\{x\},\qquad \{a,f_a\},
          \qquad \{p,f_p\}                           \tag{14}
\]

are connected and form a triangle: use `ap` for the last two contacts and
the two `W_0`--`F` contacts for the others.  They are universal to `S_0`.
Attach the two vertices of `H` to two distinct `S_0` roots to form the
four-set `K_4^-` quotient.  The count (6) gives another contradiction.

Consequently a surviving balanced split would have to satisfy

\[
                              R=F.                   \tag{15}
\]

## 4. The two-core-vertex balanced residue

Write `F=\{f,g\}`.  The component `R` is connected, so `fg` is an edge.
Every member of `F` is adjacent to all four vertices of `S_0`, and has no
neighbour in `D`.  Minimum degree seven, fullness of `R` to `E`, and the
disjoint core label sets in (1) therefore force, after interchanging
`f,g`,

\[
\begin{aligned}
 N_G(f)&=S_0\cup\{g,x,a\},\\
 N_G(g)&=S_0\cup\{f,x,p\}.                            \tag{16}
\end{aligned}
\]

In particular the two connected sets

\[
                         A=\{a,f\},\qquad P=\{p,g\}  \tag{17}
\]

are adjacent and each is universal to the four `S_0` roots.

Put `D^circ=D-H`.  Suppose first that `x` has a neighbour in a component
`C` of `D^circ`, and put `h=|N_H(C)|`.  Since

\[
                         N_G(C)\subseteq E\cup H
\]

and `C` sees `x`, seven-connectivity gives

\[
                     |N_{S_0}(C)|+h\ge4.             \tag{18}
\]

Thus `C` misses at most `h` roots in `S_0`.  Attach `d_1,d_2` to two
distinct `S_0` roots, assigning every missed root to a distinct member of
`N_H(C)`.  The four core sets form a `K_4^-` quotient, and
`C\cup\{x\}` is adjacent to all four.  Together with the sets in (17), it
forms a triangle through `xf,xg,ap`.  Equation (6) gives the target.

We may therefore assume that `x` is anticomplete to `D^circ`.  Put

\[
       s_x=|N_{S_0}(x)|,\qquad h_x=|N_H(x)|.          \tag{19}
\]

If `s_x+h_x\ge4`, the same allocation, now with the third branch set
`\{x\}`, gives (6).  Hence `s_x+h_x\le3`.  The only possible neighbours
of `x` are `f,g`, the vertices counted in (19), and `a,p`.  Minimum degree
seven and (16) force

\[
             s_x+h_x=3,\qquad xa,xp\in E(G).         \tag{20}
\]

The unique-common-neighbour identity in (1) therefore gives `x=b`.

We record the elementary allocation used for the remaining case.  Let
`Q` be a four-set, let `H_0` be a two-set, and suppose

\[
 |X_Q|+|X_H|=3,\qquad X_Q\subseteq Q,\qquad X_H\subseteq H_0,
 \qquad Y\subseteq Q,\qquad |Y|\ge3.               \tag{21}
\]

Either the two elements of `H_0` can be assigned to distinct roots of
`Q` so that the two unassigned roots lie in `Y` and the items of
`X_Q\cup X_H` occupy three resulting root sets, or

\[
 |X_Q|=1,\qquad X_H=H_0,\qquad Y=Q-X_Q.            \tag{22}
\]

Indeed, when `|X_H|=0` there is nothing to arrange.  When it is one,
assign the seen element outside `X_Q`, while also assigning the sole root
outside `Y` if there is one.  When it is two, assign both elements outside
the unique root of `X_Q`; the only obstruction to leaving both unassigned
roots in `Y` is that `Y` misses precisely that root, which is (22).

Assume `D^circ` is nonempty and choose a component `C`.  The vertex `x`
misses `C`, so seven-connectivity and `N_G(C)\subseteq E\cup H` give

\[
 |N_{S_0}(C)|+|N_H(C)|+|N_{\{a,p\}}(C)|\ge7.
                                                               \tag{23}
\]

In particular `|N_{S_0}(C)|\ge3`.  Apply (21) with

\[
 X_Q=N_{S_0}(x),\quad X_H=N_H(x),\quad
 Y=N_{S_0}(C).                                      \tag{24}
\]

In the first outcome, attach `d_1,d_2` as prescribed.  The vertex `x`
contacts three of the four resulting `K_4^-` core sets, and `C` sees both
pure roots.  Enlarge one pure root set by `C`; this repairs the sole
possible missing core contact, so the four core sets now form a `K_4`.
With the triangle `A,P,\{x\}`, the core contributes six contacts and the
three outside sets contribute eleven cross contacts.  Thus

\[
                         6+11+3=20.                  \tag{25}
\]

In the exceptional outcome (22), `x` sees both vertices of `H` and a
unique root `q in S_0`, while `C` sees exactly `S_0-\{q\}`.  Equation
(23) forces `C` to see both `d_1,d_2` and both `a,p`.  Attach one of the
two `C`-seen vertices of `H` to the `q`-rooted core set and attach the
other to a distinct root.  Then `C` is universal to a `K_4^-` core and
forms a triangle with `A,P`.  The count (6) gives the target.

It remains only to consider `D^circ` empty, so `D=H`.  In the residual
case (20), `x=b`.  Fullness of `D` and `R`, together with the disjoint
label sets in (1), gives each of `a,p` exactly one neighbour in `H` and
exactly one neighbour in `F`, with the choices distinct.  Besides these
two core neighbours, each endpoint has the fixed neighbours consisting of
the other endpoint and `x`.  There are no vertices outside

\[
                 S_0\cup H\cup F\cup\{a,p,x\}.
\]

Minimum degree seven therefore forces each endpoint to have at least three
neighbours in the four-set `S_0`.  Their core label sets are disjoint, so
this would require at least six distinct vertices of `S_0`, a contradiction.

This eliminates (15), and hence every balanced split.  Together with
Section 2 it proves the theorem.  \(\square\)

## 5. Exact scope

The theorem closes the complete two-component literal-shore-split
alternative in the adjacent-singleton contraction trace.  Its branch-set
constructions are explicit and computation-free.  It is conditional on the
audited singleton neighbourhood identities, exact contraction trace,
shore-split profiles, and balanced one-sidedness theorem.

The two-component core-concentrated rooted-contact profile remains open.
The three-component whole-shore trace is eliminated by the separately
audited three-component theorem.  Thus the two results together leave only
the core-concentrated response, but do not close the adjacent-singleton case,
the literal `K_{4,4}` case, the weighted splitter theorem, T44,
Conjecture 21, or `HC_7`.
