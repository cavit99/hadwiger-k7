# Exact shore-split profiles for an adjacent singleton pair

**Status.**  Written unbounded reduction; the adjacent audit identifies the
exact checked revision.  This theorem does not close the adjacent-singleton
case, the literal case of T44, T44, Conjecture 21, or `HC_7`.

## 1. Setting and theorem

Let `G` be a vertex-minimal seven-connected `K_7^-`-minor-free graph
containing a specified literal `K_{4,4}` with shores `S_0,S_1`.  Let
`a,p,b in V(G)-S` satisfy the exact adjacent-singleton conclusions of the
audited singleton-atom theorem:

\[
\begin{aligned}
 N_G(a)&=\{p,b\}\mathbin{\dot\cup}O,\\
 N_G(p)&=\{a,b\}\mathbin{\dot\cup}K,\\
 |O|&=|K|=5,\qquad N_G(a)\cap N_G(p)=\{b\},\\
 L(a)&\cap L(p)=\varnothing .                       \tag{1}
\end{aligned}
\]

Suppose that the contraction trace of `ap` gives an exact seven-cut

\[
                 E=\{a,p\}\mathbin{\dot\cup}T,
                 \qquad T=S_0\mathbin{\dot\cup}\{x\},             \tag{2}
\]

and that `G-E` has exactly two components `D,R`, each meeting `S_1-\{x\}`.
For `Y subseteq V(G)-E`, write

\[
                         N_E(Y)=N_G(Y)\cap E.        \tag{3}
\]

Then the following hold.

1. **Unbalanced split.**  Suppose

   \[
                             R\cap(S-T)=\{s\}.       \tag{4}
   \]

   There is an ordering `epsilon,eta` of `a,p` such that

   \[
          R-s\text{ is nonempty and connected},
          \qquad N_G(R-s)=(E-\{\epsilon\})\cup\{s\}.              \tag{5}
   \]

   Consequently `epsilon` has the unique neighbour `s` in `R`, while
   `eta` and `x` have neighbours in `R-s`.  Moreover

   \[
          \epsilon s\in E(G),\qquad
          \eta s,\eta x,\epsilon x,xs\notin E(G),\qquad
          x\ne b,\quad b\in D.                                  \tag{6}
   \]

   Put

   \[
                         U=S_1-(T\cup\{s\}),                       \tag{7}
   \]

   the opposite-shore core vertices in `D`.  If `x` is exterior, the graph
   `D` has a one-vertex separator between `N_D(x)` and
   `N_D(epsilon)`, in the set-Menger sense and possibly meeting either
   neighbour set.  If `x in S_1`, the two-set `U` separates these two
   neighbour sets in `D`.

   This covers the `1+3` split when `x` is exterior and the `1+2` split
   when `x in S_1`.

2. **Balanced split.**  This can occur only when `x` is exterior.  Suppose
   each of `D,R` contains exactly two vertices of `S_1`, and put

   \[
                              F=R\cap S_1,\qquad |F|=2.             \tag{8}
   \]

   For every component `W` of `R-F`, put

   \[
                              M_W=E-N_E(W).                         \tag{9}
   \]

   Then

   \[
       M_W\cap\{a,p\}\ne\varnothing,qquad
       |M_W|\le2,\qquad |N_G(W)\cap F|\ge |M_W|.                 \tag{10}
   \]

   In particular, if `M_W={a,p}`, then `W` sees both vertices of `F`.
   Call `W` an `a`-component when `a in M_W` and `p notin M_W`, and a
   `p`-component symmetrically.  If both types occur, every `a`-component
   and every `p`-component have the respective forms

   \[
   M_W=\{a,u\},\quad u\in T,\quad pu\notin E(G),
   \qquad
   M_{W'}=\{p,v\},\quad v\in T,\quad av\notin E(G).               \tag{11}
   \]

Thus every two-component literal-shore split has an exact unbounded
boundary-incidence profile.  The unbalanced case is reduced to one
connected tight exterior shore and the displayed order-one or order-two
separation.  The balanced case is reduced to the three endpoint-miss
types in (10)--(11).

## 2. Seven roots when one opposite-shore vertex is separated

Assume (4).  The component `D` contains every vertex of `S-\{s\}` which
does not already lie in `E`.  Put

\[
                         I=E\cap S,qquad B=E-S.
\]

The closed-shore rooted-connectivity lemma, applied to `D`, the separator
`E`, and all seven roots, makes `(G[D union E],E)` internally
seven-connected.  Use the roots in `I` as trivial paths.  The remaining
target set is

\[
                         S-(I\cup\{s\}),
\]

and has order `|B|`.  A smaller `B`--target separator, together with `I`,
would be a rooted separation of order below seven.  Menger's theorem gives
`|B|` disjoint paths saturating both sets.  After trimming at first core
contact, these paths and the trivial roots are seven disjoint `E`-rooted
bags whose core representatives are exactly `S-\{s\}`.  In particular,
the bags rooted at `a,p` have representatives on shore `S_1`, and `s` is
the unique unused core vertex.

Let `W` be a component of `R-s`.  Since

\[
                         N_G(W)\subseteq E\cup\{s\},
\]

seven-connectivity says that `W` misses at most one vertex of `E`.  It
cannot miss none, `x`, or a member `m` of `S_0`.  To see this, discard the
`x`-rooted path bag.  The retained six representatives consist of all four
vertices of `S_0` and the `a,p` representatives in `S_1`; the two unused
core vertices are `s` and the former `x` representative.  Extend the six
bags to `K_6` minus a two-edge matching, prescribing the `a,p` bags as the
pure `S_1` pair.  The edge `ap` repairs that pair, so the six bags have at
least fourteen contacts.

If `W` misses no root or only `x`, it is adjacent to all six retained roots.
If it misses `m in S_0`, the boundary lower bound makes it adjacent to `s`;
attach `s` to the `m`-rooted bag as one of the two canonical unused core
vertices.  This repairs the missing contact from `W`.  In every case `W`
is a seventh bag adjacent to all six, giving at least twenty contacts.  The
contradiction proves that every component of `R-s` misses exactly one of
`a,p` and has boundary

\[
                         (E-\{a\})\cup\{s\}
             \quad\hbox{or}\quad
                         (E-\{p\})\cup\{s\}.         \tag{12}
\]

The two miss-types cannot both occur.  If `W_a,W_p` have the indicated
types, build a `T`-rooted `K_5^-` model in `G[D union T]`.  The four
`S_0` roots are trivial.  If `x` is exterior, link it through `D` to one
opposite-shore core vertex; if `x` is a core vertex, use it trivially.
Attach the two remaining `D`-side opposite-shore core vertices to two
`S_0`-rooted bags.  Only one pair of `S_0`-rooted bags may be nonadjacent.
The two additional bags

\[
                         W_a\cup\{p\},
                         \qquad W_p\cup\{a\}
\]

are disjoint, connected, universal to the five rooted bags, and adjacent
through `ap`.  They give `9+5+5+1=20` contacts.  Thus all components in
`R-s` miss one common endpoint `epsilon`; write the other endpoint as
`eta`.  Since `R` is full to `E`, only `s` can supply an
`epsilon`-neighbour in `R`, proving `epsilon s in E(G)`.

The set `R-s` is nonempty.  Otherwise fullness of the singleton component
`R={s}` would give both `as,ps`, contrary to the disjoint label sets in
(1).  It is also connected.  If `R-s` had `k` components, remove the exact
   boundary in (12) of any one of them.  The surviving endpoint `epsilon` is
adjacent to `D`, while no component of `R-s` is adjacent to it or to another
such component.  Hence the resulting graph has at least `k+1` components.
The audited seven-cut theorem gives `k<=2`.  If `k=2`, it also gives
maximum boundary degree at most three; but the boundary contains `s` and
all four vertices of `S_0`, so `s` has four literal boundary neighbours.
This contradiction proves connectedness and (5).

Finally, `R-s` is a connected tight exterior set.  Apply the audited tight
boundary colouring theorem to its boundary in (5).  The four vertices of
`S_0` fill the colour class of order four.  The other class consists of
`eta,x,s` and has order three, extending the literal colour of `s` and of
`x` when `x` is a core vertex.  Properness proves the three nonedges in
(6) not involving `epsilon x`.  Since the common neighbour `b` is adjacent
to `eta`, the nonedge `eta x` gives `x ne b`.

The common neighbour `b` is exterior and therefore does not equal `s`.
It lies outside `E` because `T=S_0 union {x}` and `x ne b`.  It cannot lie
in `R`: both endpoints see `b`, whereas `epsilon` has the unique
`R`-neighbour `s`.  Hence `b in D`, completing the location assertions in
(6).

It remains to prove the rooted-support obstruction and the nonedge
`epsilon x`.  Call a connected set `B_x subseteq D union {x}` forbidden if
it contains `x`, meets `N_D(epsilon)`, and either
`|B_x cap U|=1` when `x` is exterior or `B_x cap U` is empty when
`x in S_1`.  Suppose first that such a set exists.  Use `B_x` as the
`x`-rooted bag and use the four vertices of `S_0` as singleton rooted bags.
If `x` is exterior, `B_x` contains exactly one member of the three-set `U`;
if `x` is a core vertex, it is itself the opposite-shore representative and
`B_x` avoids the two-set `U`.  In either case attach two untouched vertices
of `U` to two distinct `S_0`-rooted bags.  The five bags form a `K_5^-`
model, with only the two pure `S_0` bags possibly nonadjacent.

The two further bags

\[
                         (R-s)\cup\{\eta\},
                         \qquad \{\epsilon,s\}
\]

are disjoint, connected and adjacent through `ap`.  The first is adjacent
to all five rooted bags through the roots in `T`.  The second sees the four
`S_0` bags through `s` and sees `B_x` through the chosen
`epsilon`-neighbour in `D`.  The contact count is `9+5+5+1=20`, a
contradiction.

If `epsilon x` were an edge, the same construction works without requiring
an `epsilon`-neighbour in `D`.  When `x` is exterior, take for `B_x` an
`x`--`U` path trimmed at its first vertex of `U`; when `x` is a core vertex,
take `B_x={x}`.  The edge `epsilon x` supplies the last helper contact.
Thus `epsilon x` is absent.

Suppose first that `x` is exterior and put

\[
                         A=N_D(x),\qquad B=N_D(\epsilon).
\]

Every `A`--`B` path in `D` contains at least two vertices of the three-set
`U`.  Indeed, a path containing exactly one member of `U`, together with
`x`, is a forbidden set `B_x`.  If it contains none, extend it inside the
connected graph `D` to the first vertex of `U`; the union is again a
forbidden `B_x`.  Two vertex-disjoint `A`--`B` paths would require four
distinct vertices of `U`.  Set-Menger therefore gives an `A`--`B` separator
of order at most one.  Both sets are nonempty, and connectedness of `D`
excludes order zero, so the separator has order one.

If `x in S_1`, a path in `D-U` from `N_D(x)` to `N_D(epsilon)`, together
with `x`, would be a forbidden connected set `B_x` avoiding `U`.  Hence `U`
is the asserted separator.  This completes (6)--(7) and the unbalanced
case.

## 3. Six roots in the balanced split

Assume (8), and let `W` be a component of `R-F`.  Since

\[
                         N_G(W)\subseteq E\cup F,
\]

the boundary lower bound gives

\[
             |N_G(W)\cap F|\ge |E-N_E(W)|=|M_W|.                 \tag{13}
\]

This proves `|M_W|<=2` and the last assertion in (10).

It remains to show that `W` misses `a` or `p`.  Apply closed-shore rooted
connectivity to `D` and the six roots

\[
                              Q=S_0\cup\{a,p\}.
\]

After using the four core roots trivially, Menger gives two disjoint paths
from `a,p` to the two vertices of `D cap S_1`.  These are six disjoint
rooted bags with representative distribution `4+2`.  Add the two vertices
of `F` to two distinct `S_0`-rooted bags.  The resulting quotient is
`K_6` minus the two pure same-shore pairs; the edge `ap` repairs the pure
`S_1` pair, leaving at most one missing contact.

Suppose `W` saw both `a,p`.  For every selected `S_0` root missed by `W`,
(13) supplies a distinct seen vertex of `F`; assign those vertices to the
corresponding `S_0`-rooted bags in the preceding completion.  Assign any
remaining vertex of `F` arbitrarily to another `S_0`-rooted bag.  Then `W`
is adjacent to all six rooted bags.  The quotient has at least
`14+6=20` contacts, a contradiction.  This proves the first assertion in
(10).

Suppose now that an `a`-component `W_a` and a `p`-component `W_p` both
exist.  There is a `T`-rooted `K_5` model using `D` and the two vertices of
`F`: link the exterior root `x` through `D` to one vertex of `D cap S_1`,
and attach the other such vertex and both members of `F` to three distinct
`S_0`-rooted bags.  The five bags are pairwise adjacent.

The connected helpers

\[
                         W_a\cup\{p\},
                         \qquad W_p\cup\{a\}
\]

are disjoint and adjacent through `ap`.  By (10), each misses at most one
`T`-rooted bag after its endpoint is included.  If their total effective
defect were at most one, the seven bags would have at least
`10+5+5+1-1=20` contacts.  Target-freeness forces both defects to be one.
Thus `W_a` misses, besides `a`, a vertex `u in T` which is not repaired by
the added endpoint `p`; in particular `pu notin E(G)`.  Symmetrically,
`M_{W_p}=\{p,v\}` for some `v in T` with `av notin E(G)`.  This proves
(11) and the theorem.  \(\square\)

## 4. Exact scope

The theorem uses the adjacent-singleton overlap and disjoint-label
conclusions, not merely adjacency of `a,p`.  It eliminates no full
shore-split configuration.  The remaining unbalanced configuration is the
single tight shore (5) together with its rooted-support obstruction; the
balanced configuration is the endpoint-miss system (10)--(11).  These are
profiles forced inside a hypothetical
counterexample, not examples satisfying all global hypotheses.
