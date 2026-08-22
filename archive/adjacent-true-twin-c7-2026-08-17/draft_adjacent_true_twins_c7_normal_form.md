# Adjacent exceptional true twins reduce to the pure seven-cycle

**Status.**  Working theorem.  The support-sweep proof is unbounded and
computation-free.  It strictly strengthens the fixed-seam capstone by
allowing every triangle-free cross-edge pattern between the `C_5` and the
remaining edge.  The final `C_7` row is not eliminated.

## Theorem 1 (`C_5+K_2` factor completion)

Let `G` be a seven-connected graph with adjacent true twins `a,b`.  Let

\[
              T=N_G(a)-\{b\}=N_G(b)-\{a\}.
\]

Suppose `G[T]` is triangle-free and has a spanning subgraph consisting of
a five-cycle `C` and an edge `pq` on the two remaining vertices.  Then `G`
contains a `K_7^-` minor.

No bound is imposed on the number of `p,q`--`C` edges beyond
triangle-freeness.  In particular, each pole may have two cycle neighbours.

### Proof

Put

\[
                         H=G-(V(C)\cup\{a,b\}).       \tag{1}
\]

Thus `p,q\in V(H)` and `pq\in E(H)`.  Exactly as in the fixed-seam
capstone, `H` is two-connected.  If it were disconnected, the component
containing `pq` could be avoided and another component would have
neighbourhood contained in the five-set `V(C)`.  If `z` were a cut vertex,
a component of `H-z` avoiding the surviving pole or pole pair would have
neighbourhood contained in `V(C)\cup\{z\}`.  Both conclusions contradict
seven-connectivity.

Because `G[T]` is triangle-free, `C` has no chord.  A cycle vertex loses
only its two twin neighbours and its two cycle neighbours when (1) is
formed.  Seven-connectivity gives

\[
                         d_H(c)=d_G(c)-4\ge3
                         \qquad(c\in V(C)).             \tag{2}
\]

Take a `p,q` `st`-ordering

\[
                         p=v_1,\ldots,v_n=q
\]

of `H` (the self-contained ear proof is Lemma 2 of
`draft_fixed_twin_seam_st_numbering_capstone.md`).  For `1\le k<n`, let

\[
 L_k=\{v_1,\ldots,v_k\},\quad R_k=V(H)-L_k,
\]

and put

\[
 U_k=N_G(L_k)\cap V(C),\qquad
 V_k=N_G(R_k)\cap V(C).                                \tag{3}
\]

Every `L_k,R_k` is connected, and `L_k` is adjacent to `R_k` through
`pq`.  Equation (2) gives `U_k\cup V_k=V(C)`.

Triangle-freeness also makes each of `N_C(p),N_C(q)` an independent set of
the five-cycle.  Hence

\[
                         |U_1|\le2,\qquad |V_{n-1}|\le2. \tag{4}
\]

We claim that some cut has

\[
                         |U_k|\ge2,\qquad |V_k|\ge2.    \tag{5}
\]

Suppose not.  If `|U_1|=2`, then `|V_1|\le1`; every cycle vertex outside
`V_1` would have all its `H`-neighbours at `p`, contrary to (2).  Thus
`|U_1|\le1`.  Symmetrically, if `|V_{n-1}|=2`, the failure of (5) gives
`|U_{n-1}|\le1`, forcing every cycle vertex outside `U_{n-1}` to have all
its `H`-neighbours at `q`; hence `|V_{n-1}|\le1`.

Now choose the last `k` with `|U_k|\le1`.  The union identity and the last
inequality above make `k\le n-2`.  Then `|U_{k+1}|\ge2`, so failure of
(5) at `k+1` gives `|V_{k+1}|\le1`.  At least three vertices of

\[
                         C-(U_k\cup V_{k+1})
\]

have all their `H`-neighbours at the single middle vertex `v_{k+1}`, again
contradicting (2).  This proves (5).

Since `U_k\cup V_k=V(C)`, one support in (5) has order at least three.
The `(2,3)` five-cycle arc lemma (Lemma 3 of the capstone) partitions `C`
into three nonempty cyclic arcs with at most one failed incidence to
`L_k,R_k`.  The seven bags

\[
                 \{a\},\ \{b\},\ L_k,\ R_k,
                 \text{the three cycle arcs}
\]

have every pairwise contact except possibly that one incidence: the twins
see `p\in L_k`, `q\in R_k` and all cycle bags; `L_kR_k` is supplied by
`pq`; and the three arc bags form a triangle in the quotient.  They give a
`K_7^-` minor. `square`

## Lemma 2 (seven-vertex factor lemma)

If a seven-vertex graph `T` is triangle-free and `alpha(T)\le3`, then
either

1. `T` is exactly a seven-cycle; or
2. `T` has a spanning subgraph `C_5\mathbin{\dot\cup}K_2`.

### Proof

The graph is not bipartite, because one side of a bipartition on seven
vertices would be an independent set of order at least four.  A shortest
odd cycle therefore has order five or seven.

If there is a seven-cycle and `T` has an additional edge, that edge is a
chord joining vertices at cyclic distance three (distance two would make a
triangle).  Label it `c_0c_3`; then

\[
             c_0c_3c_4c_5c_6c_0
\]

is a five-cycle and `c_1c_2` is the disjoint leftover edge.  Thus the only
unfactored seven-cycle row is the cycle itself.

It remains that `T` contains a five-cycle `C` and has outside vertices
`x,y`.  If `xy` is an edge, we are done.  Suppose `xy` is absent and put

\[
                         A=N_C(x),\qquad B=N_C(y).
\]

The sets `A,B` are independent on `C`, so each has order at most two.  The
set `C-(A\cup B)` contains no nonadjacent pair, since such a pair together
with `x,y` would be an independent four-set.

The following elementary observations on a five-cycle complete the cases.
Neither `A` nor `B` is empty and they cannot both be singletons, since then
their union has order at most two and its complement contains a nonadjacent
pair.  If, say, `A=\{c\}` and `|B|=2`, then the only independent two-set
whose union with `\{c\}` has a complement with no nonadjacent pair is the
pair of the two cycle neighbours of `c`.  If `|A|=|B|=2`, the pairs cannot
meet: two distinct intersecting independent pairs leave a nonadjacent
complementary pair (and equal pairs leave three vertices).  For two
disjoint independent pairs on a five-cycle, one of them is the pair of
cycle neighbours of a vertex in the other.

Consequently, after perhaps interchanging `x,y`, some `c\in A` has its two
cycle neighbours in `B`.  The graph `(C-c)+y` is a five-cycle, while `xc`
is the disjoint leftover edge.  This is the required spanning factor.
`square`

## Corollary 3 (exact adjacent-twin normal form in a critical host)

Let `G` satisfy the campaign's critical-host hypotheses: it is
seven-connected, seven-chromatic, every proper minor is six-colourable,
and it has no `K_7^-` minor.  If `a,b` are adjacent degree-eight true
twins, then their common external neighbourhood induces exactly `C_7`.

### Proof

The audited rooted-helper closure says that `G` contains no literal `K_5`.
If the seven-vertex common external neighbourhood `T` contained a triangle,
that triangle together with the universal neighbour `b` and centre `a`
would be a literal `K_5`.  Hence `T` is triangle-free.

Every degree-eight vertex is exceptional, and the audited exceptional-
neighbourhood theorem gives `alpha(G[N(a)])=3`.  The vertex `b` is universal
in `G[N(a)]`, so `alpha(T)=3`.  Lemma 2 and Theorem 1 now say that every
row except `T\cong C_7` contains the forbidden minor. `square`

## Exact remaining obstruction

The pure `C_7` row is not covered by the `st` sweep above.  Choosing one
cycle edge as the two anchor vertices leaves a five-vertex path, not a
five-cycle.  The three remaining path bags have only two of their three
mutual contacts, so the one possible support miss would be a second missing
edge.  Treating two connected exterior sides as bags also fails unless a
literal `T` vertex is absorbed into each, because the twins are anticomplete
to the exterior.  A valid closure must therefore prove an anchored
connected split/repacking theorem, or use critical colouring/Kempe data.

This corollary eliminates every adjacent exceptional true-twin boundary
except one natural infinite host class.  It does not prove exterior
connectivity, Conjecture 21, or the global density theorem.
