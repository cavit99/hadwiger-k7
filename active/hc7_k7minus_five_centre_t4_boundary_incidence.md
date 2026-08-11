# Boundary incidence in the four-root atom residue

**Status:** written derivation; separate internal audit GREEN in
[`hc7_k7minus_five_centre_t4_boundary_incidence_audit.md`](hc7_k7minus_five_centre_t4_boundary_incidence_audit.md).
This note sharpens the singleton-atom row of the five-centre two-cut
attack.  It proves the exact centre--pole matching statement and eliminates
one contact profile when the opposite rooted instance is minimally
infeasible on all five roots.  It does not eliminate the remaining
four-root row.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the notation and hypotheses of the audited
[five-centre two-cut reduction](../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
 \qquad pq\notin E(G),
\tag{1.1}
\]

and `G-S` has exactly two connected components `C,D`, each adjacent to
every vertex of `S`.  The graph `G` is seven-chromatic, every proper minor
of `G` is six-colourable, and `G` is `K_7^-`-minor-free.

For `z\in Z`, put

\[
 c_z=|N_C(z)|,\qquad d_z=|N_D(z)|,
 \qquad \rho_z=|N_{\{p,q\}}(z)|,
\tag{1.2}
\]

so that `c_z+d_z+rho_z=8`.  Assume the no-singleton-contact branch
`c_z,d_z\ge2`.

When the four-root atom theorem is invoked, its source revision is the
hash-pinned GREEN draft
[four-root atom and exchange reduction](hc7_k7minus_five_centre_t4_atom_exchange.md).
In its singleton-atom row, a selected centre `z` has all of `N_C(z)` on
one induced `p`--`q` path `P_z`.

## 2. Every boundary edge extends to a two-edge matching

### Lemma 2.1 (exact centre--pole matching)

The boundary graph `G[S]` has matching number two.  More precisely, for
every edge `zp`, with `z\in Z`, there is a centre `w\in Z-\{z\}` such
that `wq\in E(G)`; the symmetric assertion holds after interchanging the
poles.

#### Proof

Suppose that `zp` is an edge and no edge `wq`, with `w\ne z`, exists.
Then

\[
                         I=S-\{z,p\}
\tag{2.1}
\]

is independent: `Z` is independent, `pq` is absent, and the only possible
edge from `q` to a centre of `I` was excluded.  Hence

\[
                         I\mid\{z\}\mid\{p\}
\tag{2.2}
\]

is a partition of `S` into independent blocks, while the two retained
singleton blocks induce the clique edge `zp`.

Apply the exact boundary-colouring reflection lemma from the audited
[critical seven-cut capacity theorem](../results/hc7_k7minus_critical_seven_cut_capacity.md)
with the full connected component `C` assigned to the block `I` and the
two clique singletons retained.  It gives a proper six-colouring of the
closed `D`-shore with exact boundary partition (2.2).  Interchanging `C`
and `D` gives a proper six-colouring of the closed `C`-shore with the same
exact partition.  After a permutation of colour names the two colourings
agree on `S` and glue, contradicting `chi(G)=7`.

Thus every boundary edge has a disjoint boundary edge.  The two poles form
a vertex cover of all boundary edges, so the matching number is at most
two.  The two-cut reduction says that `G[S]` has an edge, completing the
proof. \(\square\)

## 3. Exact local structure of a singleton atom

### Lemma 3.1 (three contacts)

Suppose a selected centre `z` has a singleton atom and `c_z=3`.  Then

\[
 \rho_z=2,\qquad d_z=3,
 \qquad G[N_D(z)]\cong K_3.                            \tag{3.1}
\]

Moreover, writing `N_C(z)=\{u_1,u_2,u_3\}`, the atom path is exactly

\[
                         p-u_1-u_2-u_3-q,              \tag{3.2}
\]

up to reversing the order.  Each pole misses at least one vertex of the
triangle `N_D(z)`, and together the two poles are adjacent to every vertex
of that triangle.

#### Proof

The singleton contact table gives (3.1).  Put `U=N_C(z)` and
`T=N_D(z)`.  The sets `U,T` are anticomplete, `T` is a triangle, and
`alpha(G[N(z)])=3`.  Since `U` is an induced subgraph of the path `P_z`,
one has `alpha(G[U])=2`.  Thus `G[U]` is either a three-vertex path or the
disjoint union of an edge and an isolated vertex.

Fix a pole `t\in\{p,q\}`.  The graph `G[N(z)]` is `K_4`-free, so `t`
misses some vertex `d\in T`; otherwise `T\cup\{t\}` would be a `K_4`.
For every independent pair `J\subseteq U`, the set `J\cup\{d,t\}`
cannot be independent.  Hence the at most one neighbour of `t` in `U`
meets every independent pair of `G[U]`.  The bound of one follows because
`P_z` is induced and `t` is one of its ends.

If `G[U]` were an edge plus an isolated vertex, that isolated vertex would
be the unique one-vertex transversal of its independent pairs.  Both `p`
and `q` would therefore be adjacent to that same path vertex.  Inducedness
would make `P_z` the length-two path through it, leaving no place for the
other two contacts.  This is impossible.

Consequently `G[U]` is the path `u_1u_2u_3`.  Its sole independent pair
is `\{u_1,u_3\}`.  The two poles must meet different ends of that pair;
otherwise one vertex of `P_z` would be adjacent to both path ends while
the third contact still lay on the path.  Inducedness now leaves no vertex
between a pole and its contact or between consecutive contacts, proving
(3.2).

Finally, if some `d\in T` missed both poles, then

\[
                         \{p,q,u_2,d\}
\]

would be an independent four-set in `N(z)`.  Thus the two pole
neighbourhoods cover `T`, while the earlier `K_4` argument says that each
is a proper subset of `T`. \(\square\)

### Lemma 3.2 (four contacts)

Suppose a selected centre `z` has a singleton atom and `c_z=4`.  Then

\[
 \rho_z=2,\qquad d_z=2,
 \qquad G[N_D(z)]\cong K_2,                            \tag{3.3}
\]

and both poles are adjacent to both vertices of `N_D(z)`.  In particular,

\[
                  G[\{z,p,q\}\cup N_D(z)]\cong K_5^- ,\tag{3.4}
\]

where `pq` is the unique missing edge.

#### Proof

Put `U=N_C(z)` and `T=N_D(z)`.  The singleton contact table makes `T` a
clique and leaves only

\[
             (d_z,\rho_z)=(3,1)\quad\hbox{or}\quad(2,2).
\tag{3.5}
\]

The anticompleteness of `U,T` and `alpha(G[N(z)])=3` give
`alpha(G[U])=2`.  Since `G[U]` is induced by four selected vertices of a
path, it is either a four-vertex path or two disjoint edges.  In either
case no one vertex meets every independent pair of `G[U]`.

Suppose first that `(d_z,rho_z)=(3,1)`, and let `t` be the pole adjacent
to `z`.  The triangle `T` and `K_4`-freeness give a vertex `d\in T`
missed by `t`.  The induced path gives `|N_U(t)|\le1`, so there is an
independent pair `J\subseteq U` missed by `t`.  Then
`J\cup\{d,t\}` is an independent four-set in `N(z)`, a contradiction.
Thus the second case of (3.5) holds.

Now fix either pole `t`.  If it missed a vertex `d\in T`, choose an
independent pair `J\subseteq U` disjoint from its at most one neighbour in
`U`.  Again `J\cup\{d,t\}` would be an independent four-set.  Therefore
both poles are complete to the edge `T`.  Together with the edges from
`z` to all four of these neighbours and the fixed nonedge `pq`, this is
exactly (3.4). \(\square\)

## 4. Consequence for the opposite five-root row

### Corollary 4.1

Assume the rooted instance on the distinct-response shore `D` is
infeasible on `Z` and feasible on every proper subset of `Z`.  Then no
selected singleton atom in a four-root circuit on `C` has four
`C`-contacts.

#### Proof

Such a centre would satisfy `rho_z=2` and `d_z=2` by Lemma 3.2.  The
terminal distinct-side transfer theorem in the audited
[four-root palette note](hc7_k7minus_five_centre_four_root_transfer.md)
then six-colours `G`, a contradiction. \(\square\)

## 5. Exact remaining obstruction

The matching conclusion of Lemma 2.1 is global, but it does not by itself
eliminate the singleton-atom row.  Boundary matching number two is already
compatible with all of the following surviving profiles:

1. selected centres with two adjacent `C`-contacts;
2. the exact five-vertex path and covered opposite triangle in Lemma 3.1;
3. unless the opposite rooted instance is minimal on all five roots, the
   literal `K_5^-` in Lemma 3.2.

In case 2, the proper-minor palette obstruction forces simultaneous Kempe
connections from both poles to the three opposite-triangle colours.  Those
six connections need not contain three disjoint two-pole trees.  In case 3,
the local `K_5^-` is not rooted in five boundary vertices on one closed
shore, so the existing shore-confined completion theorem does not apply.

Thus boundary matching number two sharpens the four-root row but does not
close it.  The remaining terminal task is a simultaneous two-pole packing
or an actual order-seven descent; another scalar contact count cannot
distinguish the surviving configurations.
