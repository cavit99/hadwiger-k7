# One-sidedness in the balanced adjacent-singleton shore split

**Status.** Written unbounded theorem; the adjacent audit identifies the
exact checked revision.  The input profile theorem is the audited revision
with SHA-256
`9234ff2c545608e7dcb3572dff3875137cbd2978a209826196dc111153d555ae`.
No finite computation is used.

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

Suppose there is an exact seven-cut

\[
 E=\{a,p\}\mathbin{\dot\cup}T,
 \qquad T=S_0\mathbin{\dot\cup}\{x\},               \tag{2}
\]

where `x` is exterior to the literal `K_{4,4}`, such that `G-E` has
exactly two components `D,R` and

\[
 |D\cap S_1|=|R\cap S_1|=2.                          \tag{3}
\]

Put

\[
 F=R\cap S_1,
 \qquad
 N_E(Y)=N_G(Y)\cap E                                  \tag{4}
\]

for `Y subseteq V(G)-E`.  For every component `W` of `R-F`, put

\[
 M_W=E-N_E(W).                                        \tag{5}
\]

Assume the conclusions of the audited
[adjacent-singleton shore-split profile theorem](hc7_k44_adjacent_singleton_shore_split_profiles.md):

\[
 M_W\cap\{a,p\}\ne\varnothing,
 \qquad |M_W|\le2,
 \qquad |N_G(W)\cap F|\ge |M_W|,                    \tag{6}
\]

and, if both endpoint-miss types occur, then every component missing `a`
but not `p`, and every component missing `p` but not `a`, respectively
satisfy

\[
 M_W=\{a,u\},\quad u\in T,\quad pu\notin E(G),
 \qquad
 M_{W'}=\{p,v\},\quad v\in T,\quad av\notin E(G).   \tag{7}
\]

Then `R-F` cannot contain both endpoint-miss types.  Equivalently, after
possibly interchanging `a` and `p`, every component `W` of `R-F` that
misses exactly one of `a,p` misses `a`.

Components with `M_W=\{a,p\}` are not excluded by the conclusion.

## 2. Forcing the second missed boundary vertex to be `x`

Suppose for a contradiction that `R-F` has an `a`-component `W_a` and a
`p`-component `W_p`; that is,

\[
 a\in M_{W_a},\ p\notin M_{W_a},
 \qquad
 p\in M_{W_p},\ a\notin M_{W_p}.                    \tag{8}
\]

By (7), write

\[
 M_{W_a}=\{a,u\},\qquad M_{W_p}=\{p,v\},
 \qquad u,v\in T.                                   \tag{9}
\]

We first prove `u=v=x`.

There is a `T`-rooted `K_5`-minor model on the `D` side whose three
opposite-shore additions may be assigned to any three distinct
`S_0`-rooted bags.  Indeed, begin with the four singleton `S_0` roots.
Since the component `D` is full to the exact cut `E`, choose an
`x`--`S_1` path through `D`, trimmed at its first vertex of `D\cap S_1`,
and use it as the `x`-rooted bag.  Of the three opposite-shore vertices

\[
             ((D\cap S_1)-V(B_x))\cup F,                        \tag{10}
\]

attach one to each of three prescribed, distinct `S_0` roots.  The
`x`-rooted bag contains an `S_1` representative, three `S_0` bags are
mixed, and only one `S_0` bag remains pure.  Thus all ten contacts of
`K_5` are present.

If `u in S_0`, assign a vertex of `F` to the `u`-rooted bag.  Such a
vertex is adjacent to `W_a`, because (6) and `|M_{W_a}|=2` imply that
`W_a` sees both vertices of `F`.  The connected bag

\[
                         A=W_a\cup\{p\}                         \tag{11}
\]

is then adjacent to all five rooted bags: `W_a` sees every root in
`T-\{u\}`, while its contact with the added `F` vertex repairs the
`u`-contact.  The connected bag

\[
                         P=W_p\cup\{a\}                         \tag{12}
\]

is adjacent to at least four of the five rooted bags.  Its only possible
failure is at the root `v`, and even that failure may be repaired by the
added vertex `a` or by an opposite-shore addition.  The bags `A,P` are
adjacent through the edge `ap`.  They are disjoint from one another and
from the five rooted bags, since distinct components of `R-F` are used
and the rooted model lies in `D\cup T\cup F`.

The seven bags therefore have at least

\[
                         10+5+4+1=20                         \tag{13}
\]

quotient contacts and form a `K_7^-`-minor model, a contradiction.  Thus
`u notin S_0`, and (2) gives `u=x`.  Interchanging `a,p` proves `v=x`.
Since the choices of `W_a,W_p` were arbitrary, every component of the two
types satisfies

\[
                         M_{W_a}=\{a,x\},
                         \qquad M_{W_p}=\{p,x\}.                 \tag{14}
\]

In particular, all these components see every vertex of `S_0` and, by
(6), both vertices of `F`.

## 3. The vertex `x` is anticomplete to `F`

Suppose `xf_1 in E(G)` for some `f_1 in F`, and write
`F=\{f_1,f_2\}`.  On the `D` side, take an `x`--`S_1` path through `D`,
again trimmed at its first core vertex, and put that path together with
`f_1` in the `x`-rooted bag, using the edge `xf_1` for connectedness.
Attach the remaining vertex of `D\cap S_1` and `f_2` to two distinct
`S_0`-rooted singleton bags.

These five `T`-rooted bags have at least nine contacts: the `x` bag is
adjacent to all four `S_0` bags, and among the four `S_0` bags the only
possible noncontact is the pair of bags that remain pure.  Hence they
form a `K_5^-`-minor model.

By (14), each of

\[
                         W_a\cup\{p\},
                         \qquad W_p\cup\{a\}                    \tag{15}
\]

sees all four `S_0` roots.  Although both components miss `x`, each sees
`f_1`, so both bags in (15) also contact the `x`-rooted bag.  They are
therefore universal to the five rooted bags and are adjacent through
`ap`.  The contact count is

\[
                          9+5+5+1=20,                            \tag{16}
\]

again a `K_7^-` minor.  This contradiction proves

\[
                          E_G(x,F)=\varnothing .                 \tag{17}
\]

## 4. The three components of `R-F`

Every component of `G-E` is full to `E`, since omitting a boundary vertex
would leave a vertex cut of order at most six.  In particular, `x` has a
neighbour in `R`.  By (17), that neighbour does not lie in `F`; by (14),
it lies in neither an `a`-component nor a `p`-component.  Thus some
component `W_0` of `R-F` misses both endpoints.  Equations (6) and (14)
give

\[
 M_{W_0}=\{a,p\},
 \qquad
 N_G(W_0)=T\cup F.                                    \tag{18}
\]

The equality includes the fact that `W_0` sees both vertices of `F`, by
(6).

There is exactly one such component.  If there were `k` components with
boundary `T\cup F`, deleting the seven-set `T\cup F` would leave each of
them as a separate component, together with a component containing
`D\cup\{a,p\}`.  The latter set lies in one component because `D` is
connected and full to `a,p`; every `a`-component attaches to it through
`p`, and every `p`-component through `a`.  The audited
[seven-cut component theorem](hc7_k7minus_seven_cut_three_component_bound.md)
therefore gives `k\le2`.  If `k=2`, deletion leaves exactly three
components, so the same theorem gives

\[
                         \Delta(G[T\cup F])\le3.                 \tag{19}
\]

But each vertex of `F subseteq S_1` is adjacent to all four vertices of
`S_0 subseteq T`, a contradiction.  Thus `k=1`.

There is also exactly one `a`-component.  Every such component has the
same exact seven-vertex boundary

\[
                         (E-\{a,x\})\cup F
                         =\{p\}\cup S_0\cup F.                  \tag{20}
\]

If there were `k_a` of them, deletion of (20) would leave them separately
from one component containing `D\cup\{a,x\}`.  The unique component
`W_0` attaches to this latter component through `x`, and every
`p`-component attaches through `a`.  Hence the seven-cut component theorem
gives `k_a\le2`; equality would again make (20) a three-component cut
whose induced boundary has a vertex of `F` adjacent to all four vertices
of `S_0`, contradicting the boundary-degree conclusion of that theorem.
Since `W_a` exists,
`k_a=1`.  Symmetrically, there is exactly one `p`-component.

Every component of `R-F` misses at least one endpoint by (6), so no fourth
type remains.  Consequently

\[
                         R-F=W_0\mathbin{\dot\cup}
                              W_a\mathbin{\dot\cup}W_p          \tag{21}
\]

is the decomposition into its three components, with missed boundary
sets as in (14) and (18).

## 5. The final seven branch sets

Because `D` is connected and full to `E`, choose a connected subgraph
`J subseteq D` containing a neighbour in `D` of each of `x,a,p`.  Define

\[
\begin{aligned}
 B_x&=W_0\cup\{x\}\cup V(J),\\
 B_a&=W_p\cup\{a\},\\
 B_p&=W_a\cup\{p\}.                                  \tag{22}
\end{aligned}
\]

These three sets are pairwise disjoint and connected.  The edge `ap`
joins `B_a` to `B_p`, while the chosen `a`- and `p`-neighbours in `J`
join `B_x` to `B_a` and `B_p`, respectively.  Thus the three bags in
(22) form a triangle.  Moreover, (14) and (18) show that each of
`W_0,W_a,W_p` sees every vertex of `S_0`; hence every bag in (22) is
adjacent to each of the four core bags defined next.

Write

\[
 S_0=\{q_1,q_2,q_3,q_4\},
 \qquad F=\{f_1,f_2\},                                \tag{23}
\]

and take

\[
 C_1=\{q_1,f_1\},\qquad C_2=\{q_2,f_2\},
 \qquad C_3=\{q_3\},\qquad C_4=\{q_4\}.              \tag{24}
\]

The four sets in (24) are connected and pairwise disjoint.  They have at
least five of the six mutual contacts: `C_1,C_2` are each adjacent to all
three other core bags through literal cross-shore edges, and only the
contact `C_3C_4` may be absent.  Thus they form a `K_4^-` quotient.

The seven bags

\[
                         B_x,B_a,B_p,C_1,C_2,C_3,C_4             \tag{25}
\]

are pairwise disjoint: they lie respectively in `D\cup E\cup(R-F)` and
in `S_0\cup F`, with the displayed allocations disjoint.  Their quotient
has at least

\[
 \underbrace{3}_{B_xB_aB_p\text{ triangle}}
 +\underbrace{12}_{\{B_x,B_a,B_p\}\text{ to all four }C_i}
 +\underbrace{5}_{C_1,C_2,C_3,C_4}
 =20                                                        \tag{26}
\]

contacts.  Therefore (25) is an explicit `K_7^-`-minor model, contrary
to the hypothesis on `G`.  The assumed coexistence of the two endpoint-
miss types is impossible, proving the theorem.  \(\square\)

## 6. Exact scope

This theorem closes the mixed endpoint-miss subcase of the balanced
two-component contraction profile.  In every surviving balanced profile,
the components of `R-F` that miss exactly one of `a,p` all miss the same
endpoint; components missing both endpoints may coexist with them.

The proof is conditional on all hypotheses of the audited adjacent-
singleton shore-split profile theorem, including the exact singleton
neighbourhood identities, the literal `K_{4,4}`, the exact two-component
cut, and the balanced `2+2` split.  It does not eliminate the remaining
one-sided balanced profiles, the core-concentrated profile, or the
unbalanced profile.  In particular, it does not by itself prove the full
adjacent-singleton case, the literal case of T44, T44, Conjecture 21, or
`HC_7`.
