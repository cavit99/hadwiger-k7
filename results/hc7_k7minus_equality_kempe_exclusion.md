# Kempe-component allocation excludes the critical `4n-5` equality layer

**Status:** written proof; separate internal audit.

Here `K_7^-` denotes `K_7` with one edge deleted.  Let `G` satisfy

\[
 \kappa(G)\ge7,
 \qquad \chi(G)=7,
 \qquad \text{every proper minor of `G` is six-colourable},
 \qquad K_7^-\npreccurlyeq G.                          \tag{H}
\]

The purpose of this note is to exclude equality in the previously proved
bound `|E(G)|\ge4|V(G)|-5`.  It uses the exact equality structure and the
edge-critical Kempe-component statement proved in
[`hc7_k7minus_equality_connectivity_reduction.md`](hc7_k7minus_equality_connectivity_reduction.md).

## 1. Equality notation

Assume for a contradiction that

\[
                         |E(G)|=4|V(G)|-5.             \tag{1}
\]

The equality theorem supplies a literal `K_5`, denoted by `A`, whose five
private external neighbourhoods are pairwise disjoint triangles

\[
                         T_a=N_G(a)-A\qquad(a\in A).   \tag{2}
\]

Put `H=G-A`.  Fix `a_i\in A` and `x\in T_{a_i}`, and take a proper
six-colouring `phi` of `G-a_ix`.  Use the notation of Proposition 9 of the
equality theorem:

\[
 \phi(a_i)=\phi(x)=p,
 \qquad S_{a_i}:=\phi(T_{a_i})=\{p,q,r\},              \tag{3}
\]

where `q` is the unique colour absent from `phi(A)`.  Let `a_h` be the
member of `A-\{a_i\}` coloured `r`, and write

\[
 J=A-\{a_i,a_h\},
 \qquad c_j=\phi(a_j)\quad(a_j\in J).                 \tag{4}
\]

Thus the six colours are

\[
                         \{p,q,r\}\cup\{c_j:a_j\in J\}. \tag{5}
\]

For `a_j\in J`, let `P_j` be the component of `H[p,c_j]` containing
`x`.  Proposition 9 proves that `P_j` meets `T_{a_j}`.  Whenever `p` or
`q` occurs on `T_a`, denote its unique vertex there by `p_a` or `q_a`,
respectively.

## 2. The symmetric two-colour components

Let `y=q_{a_i}`.  For `a_j\in J`, let `Q_j` be the component of
`H[q,c_j]` containing `y`.

### Lemma 1

For every `a_j\in J`, the component `Q_j` meets `T_{a_j}`.

### Proof

Suppose that `Q_j` misses `T_{a_j}` and interchange `q,c_j` on `Q_j`.
The triangle `T_{a_i}` contains `q` only at `y` and contains no `c_j`, so
the interchange removes `q` from `T_{a_i}`.  Assign `q` to `a_i` and
retain the original colours on `A-\{a_i\}`.  The colour `c_j` remains
available at `a_j` because `Q_j` misses its private triangle; every other
retained colour lies outside `\{q,c_j\}`.  The restored edge `a_ix` has
colours `q,p`.  This gives a proper six-colouring of `G`, a contradiction.
\(\square\)

### Lemma 2 (the common four-triangle case)

Suppose

\[
 S_{a_j}=\{p,q,r\}
 \qquad\text{for every `a_j\in J`.}                   \tag{6}
\]

Then every `Q_j` contains the `q`-coloured vertex of each of the four
triangles

\[
                    T_{a_i},\qquad T_{a_t}\ (a_t\in J). \tag{7}
\]

### Proof

Lemma 1 gives the assertion for `T_{a_j}`, and the definition gives it for
`T_{a_i}`.  Suppose that `a_t\in J-\{a_j\}` and that the component `C` of
`H[q,c_j]` containing `q_{a_t}` differs from `Q_j`.  The component `C`
misses `T_{a_i}` and `T_{a_j}`: their unique `q`-vertices lie in `Q_j`,
and neither triangle contains `c_j` by (6).

Interchange `q,c_j` on `C`, assign `q` to `a_t` and `c_t` to `a_i`, and
retain the original colours on the other three vertices of `A`.  The
interchange removes `q` from `T_{a_t}`; it leaves `T_{a_i}` and
`T_{a_j}` unchanged.  The five assigned colours are distinct, all are
available, and `a_ix` has colours `c_t,p`.  This again six-colours `G`, a
contradiction.  Hence (7) holds.  \(\square\)

## 3. Excluding the common four-triangle case

### Proposition 3

Equation (6) is impossible.

### Proof

Proposition 9(4) says that each `P_j` contains the `p`-coloured vertices of
all four triangles in (7).  Choose distinct `a_j,a_l\in J` and put

\[
                            X=P_j,
 \qquad                     Y=Q_l.                     \tag{8}
\]

The sets `X,Y` are connected and vertex-disjoint: every vertex of `X` has
colour in `\{p,c_j\}`, whereas every vertex of `Y` has colour in
`\{q,c_l\}`.  Both sets meet all four triangles in (7), and they are
adjacent through the edge `p_aq_a` in any one of those triangles.

If `T_{a_h}` already meets `X\cup Y`, retain the set that it meets.
Otherwise, take a shortest path in the connected graph `H` from
`T_{a_h}` to `X\cup Y`, stopped at its first vertex in that union.  Its
internal vertices avoid both `X` and `Y`; add the path to the set containing
its final vertex.  Call the resulting two disjoint connected sets
`X',Y'`.  One meets all five private triangles and the other meets the four
triangles in (7), and `X'` is adjacent to `Y'`.

The five singleton sets `\{a\}`, `a\in A`, together with `X',Y'`, are
seven pairwise disjoint connected branch sets.  Every required adjacency
is present except possibly the adjacency between `a_h` and the set not
enlarged to meet `T_{a_h}`.  They therefore form an explicit `K_7^-`-minor
model, contrary to (H).  \(\square\)

## 4. The all-five-triangles colour case

It remains to consider the other outcome of Proposition 9(3).  For each
`a\in A`, write

\[
                         S_a=\{p,q,s_a\}.              \tag{9}
\]

The third colours satisfy

\[
 s_{a_i}=r,
 \qquad s_{a_h}\in\{c_j:a_j\in J\},
 \qquad s_{a_j}\ne c_j\quad(a_j\in J).               \tag{10}
\]

Indeed, the first equality is (3), while the other two assertions follow
because the colour of a vertex of `A` is absent from its private triangle.
By Proposition 3, (6) fails, so there is some `a_u\in J` with

\[
                              s_{a_u}\ne r.            \tag{11}
\]

### Lemma 4 (component reach)

Fix `a_j\in J`.  If `a_t\in A` and `s_{a_t}\ne c_j`, then

\[
                         p_{a_t}\in P_j,
 \qquad                  q_{a_t}\in Q_j.              \tag{12}
\]

### Proof

For `a_t=a_i`, (12) follows from the definitions.  For `a_t=a_j`, the
`p` assertion is Proposition 9(2), and the `q` assertion is Lemma 1.

Let `a_t\in J-\{a_j\}`.  Suppose first that the component `C` of
`H[p,c_j]` containing `p_{a_t}` differs from `P_j`.  It misses
`T_{a_i}` and `T_{a_j}`, because their `p`-vertices lie in `P_j` and
neither triangle contains `c_j`.  The hypothesis `s_{a_t}\ne c_j` says
that `T_{a_t}` also contains no `c_j`.  Interchange `p,c_j` on `C`, assign
`p` to `a_t` and `c_t` to `a_i`, and retain the other three colours on
`A`.  This is a proper assignment: `p` has been removed from `T_{a_t}`;
`T_{a_i}` and `T_{a_j}` are unchanged; and the other retained colours lie
outside `\{p,c_j\}`.  It also makes the restored edge `a_ix` proper.  The
resulting six-colouring of `G` is a contradiction, so `p_{a_t}\in P_j`.
The same argument with `q,c_j` and the assignment `q` to `a_t` proves
`q_{a_t}\in Q_j`.

Finally let `a_t=a_h`, and suppose that the relevant `p,c_j` component
through `p_{a_h}` differs from `P_j`.  Since `s_{a_h}\ne c_j`, its
interchange removes `p` from `T_{a_h}`.  Use the vertex `a_u` from (11),
assign

\[
                p\text{ to }a_h,
 \qquad          c_u\text{ to }a_i,
 \qquad          r\text{ to }a_u,                     \tag{13}
\]

and retain the original colours on the other two vertices of `J`.  The
colour `r` is available at `a_u` by (9) and (11).  If `a_u=a_j`, no vertex
of `A` retains `c_j`; if `a_u\ne a_j`, the interchanged component misses
`T_{a_j}`, so `c_j` remains available there.  Every other retained colour
lies outside the interchanged pair, `c_u` remains available at `a_i`, and
`a_ix` has colours `c_u,p`.  Thus (13) would six-colour `G`, a
contradiction.  Replacing `p` by `q` gives the identical conclusion for
`Q_j`.  This proves (12).  \(\square\)

### Proposition 5

The all-five-triangles colour case (9) is impossible.

### Proof

For `a_j\in J`, put

\[
              n_j=|\{a\in A:s_a=c_j\}|.               \tag{14}
\]

Only `a_h` and the three vertices in `J` can contribute to these three
counts, because `s_{a_i}=r`.  Hence

\[
                         \sum_{a_j\in J}n_j\le4.       \tag{15}
\]

Choose `a_l\in J` with `n_l\le1`, and write
`J=\{a_j,a_k,a_l\}`.  Define

\[
                         X=P_j\cup P_k,
 \qquad                  Y=Q_l.                        \tag{16}
\]

The set `X` is connected because `P_j` and `P_k` both contain `x`, and
`Y` is connected.  They are vertex-disjoint because their respective
colour sets are

\[
                         \{p,c_j,c_k\},
 \qquad                  \{q,c_l\}.                   \tag{17}
\]

For every `a\in A`, the colour `s_a` cannot equal both `c_j` and `c_k`.
Lemma 4 therefore puts `p_a` in `X`, so `X` meets all five triangles.
The same lemma puts `q_a` in `Y` except possibly when `s_a=c_l`; by the
choice of `a_l`, there is at most one such triangle.  Moreover, `X` and
`Y` are adjacent through `p_aq_a` in any nonexceptional triangle.

The five singleton vertices of `A`, together with `X,Y`, consequently form
a `K_7^-`-minor model: the only possibly missing adjacency is between `Y`
and the owner of the one exceptional triangle.  This contradicts (H).
\(\square\)

## 5. Strict density consequence

### Theorem 6 (equality exclusion)

No graph satisfying (H) has `|E(G)|=4|V(G)|-5`.

### Proof

Proposition 9(3) of the equality theorem says that either (6) holds or
`p,q` occur on all five private triangles.  Proposition 3 excludes the
first outcome, and Proposition 5 excludes the second.  \(\square\)

### Corollary 7 (improved critical-host density)

Every graph satisfying (H) has

\[
                         |E(G)|\ge4|V(G)|-4.           \tag{18}
\]

### Proof

The previously audited density theorem gives
`|E(G)|\ge4|V(G)|-5`.  Theorem 6 excludes equality, and the number of
edges is integral.  \(\square\)

## 6. Trust boundary

The proof is unbounded and uses no finite enumeration.  After the equality
structure and Proposition 9 have been invoked, it uses only Kempe
interchanges, explicit colour assignments, and connectedness of `H`.

The argument deliberately does **not** claim to construct a bond meeting
all five private triangles in a wider class of five-connected graphs.  In
Proposition 5, `X` is a connected transversal of all five triangles, while
`Y` is certified to meet at least four; when `n_l=1`, the fifth contact is
not proved.  Likewise, Proposition 3 attaches the remaining triangle to
only one of the two connected sets.  One missing adjacency is permitted in
a `K_7^-` model, and that is enough to contradict (H) and exclude the
entire critical-host equality layer.  Consequently the requested conditional
two-transversal statement has no surviving equality host to which it must
be applied, but no standalone bond theorem is inferred.
