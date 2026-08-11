# A fan core for two saturated centre triangles

**Status:** archived written lemma; not separately audited.  The core
extraction and pole reservation below are unconditional.  The final
shore-confined two-helper placement is an explicit route nonclosure, not a
theorem.

Throughout, `K_t^-` denotes `K_t` with one edge deleted.

## 1. The unreserved core is automatic

### Lemma 1.1 (triangle--centre fan core)

Let `G` be seven-connected.  Let `z,w` be distinct nonadjacent vertices,
and suppose that `N_G(z)-{w}` contains a triangle

\[
                           T=\{t_1,t_2,t_3\}.
\]

Then `G` has five pairwise disjoint connected branch sets

\[
                    \{z\},\quad \{w\},\quad B_1,B_2,B_3
\tag{1.1}
\]

such that every two are adjacent except possibly `\{z\},\{w\}`.
Moreover, the three non-centre bags may be taken to be the arms, with
their common end removed, of a `w`--`T` fan in `G-z`.

#### Proof

The graph `G-z` is six-connected, and in particular is three-connected.
The fan lemma gives three paths `P_1,P_2,P_3` from `w` to the three
distinct vertices of `T`, pairwise disjoint except for their common end
`w`.  Relabel so that `P_i` ends at `t_i`, and put

\[
                         B_i=V(P_i)-\{w\}.
\tag{1.2}
\]

The sets in (1.1) are disjoint and connected.  The first edge of `P_i`
makes `B_i` adjacent to `\{w\}`; the edge `zt_i` makes it adjacent to
`\{z\}`; and the triangle edges `t_it_j` make distinct `B_i,B_j`
adjacent.  Only `zw` has not been asserted.  \(\square\)

In particular, the shared-pole saturated row does not need the six Kempe
locks merely to obtain an unrooted `K_5^-` core.  Apply Lemma 1.1 to the
literal triangle `T_z=N_D(z)`.  It works whether `T_z,T_w` are disjoint or
overlap, and it also bypasses the same-pole lock-packing obstruction.

### Lemma 1.2 (the two poles can be reserved)

In the five-centre two-cut setting, the fan in Lemma 1.1 can be chosen so
that all three bags avoid `p,q`.

#### Proof

The graph

\[
                              G-\{z,p,q\}
\]

is four-connected.  It contains `w` and the three vertices of `T_z`.
Apply the fan lemma there.  \(\square\)

This reservation is useful but not shore confinement: the resulting arms
may still use `C` or one of the other three centres.
Five-connectivity alone cannot reserve a connected subgraph from such a
fan; the exact clique-sum counterexample is recorded in the
[reserved triangle-fan barrier](../../barriers/hc7_five_connected_reserved_triangle_fan_barrier.md).

## 2. Exact terminal placement

Return to the five-centre two-cut setting.  Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},
\]

`G-S` has connected full components `C,D`, and the saturated centres
`z,w in Z` are both adjacent to `p` and not to `q`.

### Lemma 2.1 (reserved fan completion)

Suppose the fan in Lemma 1.1 can be chosen so that its bags
`B_1,B_2,B_3` lie in `D` and avoid `p,q`.  Suppose, in addition, that
there are disjoint connected subgraphs `X_p,X_q` of

\[
       G[(D\cup\{p,q\})-(B_1\cup B_2\cup B_3)]
\tag{2.1}
\]

with `p in X_p`, `q in X_q`, such that both are adjacent to every
`B_i`.  Then `G` contains a `K_7^-` minor.

#### Proof

Replace `X_q` by `X_q union C`.  This remains connected because `C` is
full at `q`, and it is adjacent to `X_p` through an edge from `p` to `C`.
Both completing bags are adjacent to `z,w`: `X_p` through the two edges
`zp,wp`, and `X_q union C` because `C` is full at the seven-vertex
boundary.  They are adjacent to the three fan bags by hypothesis.
Together with the five bags in (1.1), these are seven pairwise adjacent
connected bags except possibly for `\{z\},\{w\}`.  \(\square\)

## 3. Exact nonclosure

Lemma 1.1 removes the existence of a `K_5^-` core from the saturated-row
residue.  What remains is strictly a reservation problem.

Lemma 1.2 reserves the two poles, but it does not keep the fan inside `D`:
an arm may use `C` or another boundary centre.  Once such material is used
by a core bag, the connected opposite-side completion in Lemma 2.1 need
not remain available.  Applying Menger only inside
`D union {w}` would give the required shore-confined fan precisely when
there are three disjoint `T_w`--`T_z` routes in `D`; failure is an
order-at-most-two separation of that rooted instance, not a contradiction
to seven-connectivity of `G`.

Even a shore-confined fan is not terminal by itself.  The two completing
subgraphs must simultaneously contain the prescribed poles and meet all
three fan bags.  An unlabelled rooted `K_{3,2}` or tripod supplies two
connected subgraphs meeting the three roots, but it does not place `p` and
`q` in different subgraphs.  This is the first unsupported inference in a
direct connectivity/tripod proof.

Consequently the smallest remaining statement for this row is the
following labelled alternative:

> either choose a `D`-confined `w`--`T_z` fan and disjoint `p`- and
> `q`-rooted completing subgraphs as in Lemma 2.1, or return a proper-minor
> boundary colouring that glues across `S`, or return an exact separation
> carrying the same two pole labels and a strict anchored descent.

The theorem that every seven-connected graph contains a `K_4`
subdivision through four prescribed branch vertices does not supply this
alternative.  With branch vertices `w,t_1,t_2,t_3`, its three arms give
exactly the unreserved fan core of Lemma 1.1; it has no clause reserving
`p,q` or placing them in two different complementary connected sets.

## 4. The direct RST placement test

There is one clean use of the Robertson--Seymour--Thomas triangular
theorem which needs no contraction.  It sharpens the remaining incidence
condition, but still does not place the second contact triangle.

Put

\[
                         H=G-\{z,w\}.
\tag{4.1}
\]

This graph is five-connected.  It is nonplanar because it contains the
induced subgraph `G[D]`, whose chromatic number is at least five.  Let

\[
 A=\{i:pt_i\in E(G)\},\qquad
 B=\{i:qt_i\in E(G)\},
\tag{4.2}
\]

where `T_z={t_1,t_2,t_3}`, and let `W` be the subgraph of `H` induced by
`T_z union {p,q}`.

### Lemma 4.1 (the exact five-vertex triangular table)

The graph `W` is not triangular with respect to `T_z` if and only if

1. one of `A,B` is the full three-set and the other is nonempty; or
2. `A=B` and `|A|=2`.

#### Proof

If `A cap B` is empty, all degrees are at most three, at most one of
`p,q` has degree three, and `W-T_z` is acyclic.  This is the second case
in the RST definition of triangularity.

Suppose `A cap B={i}`.  If neither set is the full three-set, delete
`t_i`.  The remaining graph has maximum degree at most two and is a
forest, so the first RST case applies.  If one set is full and the other
is nonempty, a direct degree check shows that deleting any root either
leaves a vertex of degree at least three or leaves a circuit together
with additional vertices; the second and third RST cases also fail.

Finally, if `|A cap B|>=2`, then either one set is full and the other is
nonempty, or the two sets are the same two-set.  Every common root has
degree four in `W`, so the second and third RST cases fail.  Deleting one
root leaves either another vertex of degree at least three or a circuit
with an additional vertex, so the first case fails as well.  These are
exactly the two alternatives in the statement.  \(\square\)

### Corollary 4.2 (what the nontriangular outcome supplies)

If either alternative of Lemma 4.1 holds, then `H` has a `T_z`-rooted
`K_5` model

\[
                    \{t_1\},\{t_2\},\{t_3\},X_p,X_q
\tag{4.3}
\]

with `p in X_p` and `q in X_q`.  Consequently, adding the singleton bag
`{z}` gives a `K_6^-` model whose only possibly missing adjacency is
between `{z}` and `X_q`.

#### Proof

Apply Robertson, Seymour, and Thomas,
[*Hadwiger's conjecture for `K_6`-free graphs*](https://thomas.math.gatech.edu/PAP/hadwiger.pdf),
statement (3.6), in the four-connected nonplanar graph `H`, using the
induced subgraph `W`.  Its two non-root bags both meet
`W`.  They are disjoint from the three singleton root bags, so they meet
the two-set `{p,q}`.  Disjointness forces one pole into each bag.  The
last assertion uses `zt_i` for the three root adjacencies and `zp` for
the fourth.  \(\square\)

The critical host contains no literal `K_5`, so `A` cannot be the full
three-set: otherwise `{z,p,t_1,t_2,t_3}` is a `K_5` subgraph.  Thus the
only nontriangular incidence rows still possible are

\[
 B=\{1,2,3\},\ A\ne\varnothing,
 \qquad\text{or}\qquad A=B,\ |A|=2.
\tag{4.4}
\]

Neither output is terminal for the saturated pair.  The RST model is not
confined to `D`, and Corollary 4.2 does not make `w` adjacent to the three
singleton root bags.  That would require the three contacts of `T_w` to
be placed one per root bag (or an equivalent paired-root model).  In the
triangular rows, RST supplies no model at all.  Hence direct use of the
five-connected nonplanar host stops exactly at the same paired-root and
shore-reservation requirement as Section 3.
