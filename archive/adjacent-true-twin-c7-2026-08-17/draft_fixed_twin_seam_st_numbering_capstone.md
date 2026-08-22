# The fixed true-twin seam closes by an `st`-support sweep

**Status.**  Complete self-contained proof under the fixed-seam hypotheses
listed below.  The proof constructs a literal seven-bag `K_7^-` model.  It
does not use packet transfer, a density estimate, or bounded computation.
Its application to a larger reduction is only as broad as the reduction
which supplies these hypotheses.

## 1. Fixed-seam hypotheses

Let `G` be a simple graph with

\[
                     \kappa(G)\ge 7,\qquad \delta(G)\ge 8.       \tag{1}
\]

Let `a,b` be adjacent true twins.  Their common external neighbourhood is

\[
 T=V(C)\mathbin{\dot\cup}\{e_1,e_2\},\qquad
 C=c_0c_1c_2c_3c_4c_0,                                    \tag{2}
\]

where `C` is induced, `e_1e_2` is an edge, and at most one edge joins
`{e_1,e_2}` to `C`.  Thus each of `a,b` is adjacent to all seven vertices
of `T`, and neither has a neighbour outside `T` and the other twin.

Put

\[
 D=G-(T\cup\{a,b\}),\qquad
 H=G-(V(C)\cup\{a,b\})=G[D\cup\{e_1,e_2\}].              \tag{3}
\]

There is no hypothesis on the number or structure of the components of
`D`, nor on their attachment sets.

## 2. A self-contained `st`-ordering lemma

### Lemma 2.1

If a graph `J` is two-connected and `st` is an edge, then its vertices have
an ordering

\[
                         v_1=s,v_2,\ldots,v_m=t             \tag{4}
\]

in which every `v_i`, `1<i<m`, has both an earlier and a later neighbour.
Consequently every prefix and every suffix of (4) induces a connected
subgraph.

### Proof

The edge `st` lies on a cycle.  Order the vertices of that cycle by starting
at `s`, following the cycle with the edge `st` deleted, and ending at `t`.
This has the required earlier--later property.

Suppose that a proper vertex set `W` has already been ordered with the same
property.  A component `K` of `J-W` has at least two distinct neighbours in
`W`; otherwise its sole neighbour would be a cut vertex of `J`.  Hence there
is a path with distinct ends `x,y` in `W` and all internal vertices in `K`.
If `x` precedes `y`, insert the internal vertices of the path, in path order,
between `x` and `y`; if `y` precedes `x`, use the reverse path order.  Every
new vertex has an earlier and a later neighbour, and all old vertices retain
the property.  Repeating absorbs every vertex of `J`.

In (4), each vertex other than `s` has an earlier neighbour, so induction on
the order makes every prefix connected.  Reversing the order proves the
same for suffixes. `square`

## 3. The pole graph is two-connected

### Lemma 3.1

The graph `H` in (3) is two-connected.

### Proof

It is connected.  Otherwise the edge `e_1e_2` puts both poles in one
component of `H`; any other component `Q` lies in `D` and has
`N_G(Q)\subseteq V(C)`, contrary to seven-connectivity.

Suppose that `x` is a cut vertex of `H`.  If `x` is not a pole, the edge
`e_1e_2` puts both poles in the same component of `H-x`.  If `x` is one
pole, only the other pole remains.  In either case some component `Q` of
`H-x` contains neither pole.  Thus `Q\subseteq D`.  Its vertices have no
neighbour in either twin, and by the definition of a component of `H-x`,

\[
                         N_G(Q)\subseteq V(C)\cup\{x\}.      \tag{5}
\]

The right side has order six, while another component of `H-x` remains
outside it.  Equation (5) contradicts `\kappa(G)\ge7`.  Hence `H` has no cut
vertex.  Moreover every `c\in V(C)` has outside `H` exactly its two cycle
neighbours and the two twins.  Thus

\[
                         d_H(c)=d_G(c)-4\ge4.                \tag{6a}
\]

In particular `|H|\ge4`, proving the lemma. `square`

## 4. The five-cycle interval lemma

### Lemma 4.1

Let `A,B\subseteq V(C_5)` satisfy

\[
                    |A|\ge2,\qquad |B|\ge2,\qquad
                    \max\{|A|,|B|\}\ge3.                   \tag{6}
\]

The cycle can be partitioned into three nonempty cyclic intervals
`I_1,I_2,I_3` so that among the six incidences

\[
                          A\cap I_k,\quad B\cap I_k
                          \qquad(k=1,2,3)                   \tag{7}
\]

at most one is empty.

### Proof

Interchange `A,B` if necessary and shrink them, so it is enough to take
`|A|=3` and `|B|=2`.  Regard the three vertices of `A` as cyclic markers.
Put one cut edge in each of the three gaps between consecutive markers.
This partitions the cycle into three cyclic intervals, each containing
exactly one marker and hence meeting `A`.

The cut edges can be chosen so that the two vertices `x,y` of `B` lie in
different intervals.  If both are markers this is automatic.  If exactly
one, say `x`, is a marker, then `y` lies in a gap between two markers; put
it into the interval of the endpoint marker different from `x` (or either
one if `x` is not an endpoint of that gap).  If neither is a marker and
they lie in the same gap, cut that gap between them.  If they lie in
different gaps, assign `x` to either endpoint interval of its gap and then
assign `y` to an endpoint interval of its gap different from the one used
for `x`; the second gap has two distinct endpoint markers.  Each assignment
is realised by the position of the cut edge in that gap.  Thus all three
intervals meet `A` and two meet `B`. `square`

The independent verifier `verify_c5_23_arc_partition.py` enumerates the ten
three-interval partitions directly from the three cut edges of the cycle.
It checks all `576` ordered pairs satisfying (6), without using the orbit
table.

## 5. The support sweep

### Theorem 5.1 (fixed true-twin seam completion)

Every graph satisfying the hypotheses of Section 1 contains a `K_7^-`
minor.

### Proof

Apply Lemma 2.1 to the edge `e_1e_2` of the two-connected graph `H`, and
write the resulting order as

\[
                     v_1=e_1,v_2,\ldots,v_m=e_2.            \tag{8}
\]

For `1\le i<m`, put

\[
 P_i=\{v_1,\ldots,v_i\},\qquad
 Q_i=\{v_{i+1},\ldots,v_m\},                               \tag{9}
\]

and define their cycle supports

\[
 A_i=N_C(P_i),\qquad B_i=N_C(Q_i).                          \tag{10}
\]

Every `P_i` and `Q_i` is connected.  The optional pole--cycle edge gives

\[
                             |A_1|\le1.                     \tag{11}
\]

At the other end `|B_{m-1}|\le1`.  Every cycle vertex has an `H`-neighbour
by (6a), so

\[
              A_i\cup B_i=V(C)\quad(1\le i<m),
              \qquad |A_{m-1}|\ge4.                        \tag{12}
\]

Let `j` be the first index with `|A_j|\ge2`.  Then `j\ge2` and
`|A_{j-1}|\le1`.

Suppose first that `|B_j|\le1`.  The vertices of `H` are partitioned as

\[
                         P_{j-1},\quad\{v_j\},\quad Q_j.    \tag{13}
\]

At least three cycle vertices lie outside `A_{j-1}\cup B_j`.  Every
neighbour in `H` of any such cycle vertex must be `v_j`, by (10) and (13).
But (6a) gives `d_H(c)\ge4`, contradicting
`N_H(c)\subseteq\{v_j\}`.  Hence

\[
                         |A_j|\ge2,\qquad |B_j|\ge2.        \tag{14}
\]

By (12), `A_j\cup B_j=V(C)`.  In view of (14), at least one of the two supports
has order at least three.  Lemma 4.1 supplies a partition of `C` into three
nonempty cyclic intervals `I_1,I_2,I_3` for which at most one of the six
prefix/suffix--interval incidences is absent.

Now take the seven pairwise disjoint connected bags

\[
              \{a\},\quad\{b\},\quad P_j,\quad Q_j,
              \quad I_1,\quad I_2,\quad I_3.               \tag{15}
\]

The twin bags are adjacent and each sees all five other bags: they see
`P_j,Q_j` through `e_1,e_2`, respectively, and see every interval on `C`.
The prefix and suffix bags are adjacent through the edge `e_1e_2`.  The
three interval bags are pairwise adjacent through the three cut edges of
the cycle.  Finally, Lemma 4.1 says that among the six contacts from
`P_j,Q_j` to the interval bags, at most one is absent.  Thus the quotient of
(15) is `K_7` with at most one edge missing. `square`

## 6. Audit boundary

The proof uses exactly the following inherited facts.

1. Seven-connectivity is used only in Lemma 3.1.
2. Minimum degree eight is used only in (6a).
3. No connectedness, fullness, packet, or even nonemptiness hypothesis is
   imposed on `D`; connectivity and support coverage follow from (1), (5),
   and (6a).
4. The exact boundary type is used for `e_1e_2`, the pole endpoint support
   bound (11), the induced five-cycle interval bags, and the degree
   subtraction in (6a).
5. No assertion about packet number, excess, colouring, or transfer across
   a derived separator occurs.

Accordingly, this theorem eliminates the entire fixed true-twin seam once
that seam has been reduced to Section 1.  It does not by itself establish
that every branch of the ambient Hadwiger campaign reaches this seam.
