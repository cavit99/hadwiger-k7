# Shared-pole saturated triangles: the exact two-helper residue

**Status:** archived written derivation; not separately audited.  This note
records a route nonclosure, not a counterexample.  It proves that
two saturated degree-eight centres at one pole either produce an explicit
`K_5^-` minor core or satisfy a precise path-packing obstruction.  It does
not complete that core to a `K_7^-` minor.

Throughout, `K_7^-` denotes `K_7` with one edge deleted.

## 1. Setting

Use the two-shore notation of the audited
[five-centre two-cut reduction](../../results/hc7_k7minus_five_centre_two_cut_reduction.md).
Thus

\[
 S=Z\mathbin{\dot\cup}\{p,q\},\qquad |Z|=5,
\]

`G-S` has connected full components `C,D`, and a fixed permitted colouring
of the distinct-response shore has

\[
 \phi_D(Z)=\alpha,\qquad \phi_D(p)=\beta,
 \qquad \phi_D(q)=\delta.                              \tag{1.1}
\]

Assume that both rooted instances have inclusion-minimal bad-root set `Z`.
Let `z,w in Z` be distinct centres adjacent to `p` and not to `q`, with

\[
 (c_z,d_z,\rho_z)=(c_w,d_w,\rho_w)=(4,3,1).            \tag{1.2}
\]

The contact sets

\[
 T_z=N_D(z),\qquad T_w=N_D(w)                          \tag{1.3}
\]

are triangles.  Call such a centre **saturated** when its triangle uses
the three colours outside `\{alpha,beta,delta\}` in (1.1).  Name those
colours

\[
                         \Gamma=\{\gamma_1,\gamma_2,\gamma_3\},
\]

and let `t_x^i` be the unique vertex of `T_x` having colour `gamma_i`, for
`x in \{z,w\}`.

The boundary centre--pole incidence graph has matching number two in the
surviving two-cut branch.  Since `z,w` both use `p`, there is therefore a
third centre `y in Z-\{z,w\}` adjacent to `q`.  The conclusions below do
not need to assume a profile or a palette mode for `y`.

## 2. The six simultaneous Kempe locks

### Lemma 2.1 (shared-pole lock family)

For every `x in \{z,w\}` and every `i in \{1,2,3\}`:

1. `t_x^i` lies in the `beta`--`gamma_i` component containing `p`; and
2. `t_x^i` lies in the `delta`--`gamma_i` component containing `q`.

Consequently, for each `i`, the two vertices `t_z^i,t_w^i` lie in one
common `beta`--`gamma_i` component and in one common
`delta`--`gamma_i` component.

#### Proof

Suppose first that `t_x^i` does not lie in the
`beta`--`gamma_i` component containing `p`.  Interchange `beta` and
`gamma_i` on the component containing `t_x^i`.  This keeps the colours on
`Z,p,q` fixed and makes `T_x` omit `gamma_i`.

The four-root transfer obtained by omitting `x` colours the other four
centres with `alpha` and the poles with `beta,delta`.  The pole edge `xp`
forces `x` to avoid `beta`.  If `x` had colour `alpha` or `delta`, it would
already avoid the saturated triangle and the two shore colourings would
glue.  Thus `x` has one of the three colours in `Gamma`.  Permuting the free
colours makes the colour of `x` equal to `gamma_i`.  The altered
`D`-colouring and this transferred
`C`-colouring now agree on the common boundary, and every edge from `x` to
`D` is proper because `T_x` omits `gamma_i`.  They glue to a six-colouring
of `G`, a contradiction.

The same argument, interchanging `delta` and `gamma_i` on a component not
containing `q`, proves the second assertion.  Applying both assertions to
`z` and `w` gives the final statement.  \(\square\)

For `epsilon in \{beta,delta\}`, let `mathcal P_{epsilon,i}` denote the
family of all `t_z^i`--`t_w^i` paths in their common
`epsilon`--`gamma_i` component.

## 3. Four-root witnesses forbid equal triangles

### Lemma 3.1 (overlap at most two)

The two contact triangles are distinct and

\[
                            |T_z\cap T_w|\le2.          \tag{3.1}
\]

More precisely, let `(P_z,K_z)` be a minimum-length `D`-side four-root
witness omitting `z`: `P_z` is a `p`--`q` path and `K_z` is the component
of its deletion containing `Z-\{z\}`.  Then

\[
                         T_z\cap T_w\subseteq V(P_z).  \tag{3.2}
\]

If the intersection is the edge `ab`, then `a,b` are consecutive on
`P_z`, and the third vertex of `T_w` belongs to `K_z` and is adjacent to
both `a,b`.  The symmetric statement holds for a minimum witness omitting
`w`.

#### Proof

Full five-root infeasibility implies that `z` has no neighbour in `K_z`:
otherwise restoring `z` would put all five roots in one component after
deleting the same path.  Since `w in K_z`, every vertex of
`T_w-V(P_z)` is adjacent to `w` and hence also belongs to `K_z`.  Such a
vertex cannot belong to `T_z`, proving (3.2).

Suppose that all three vertices of the common triangle lie on `P_z`.
Choose their first and last occurrences along the path.  They are adjacent,
so replace the subpath between them by that triangle edge.  The resulting
`p`--`q` path restores the third triangle vertex.  The old connected set
`K_z` remains in one residual component; the restored vertex joins it
through `w` and joins `z` through its edge to `z`.  This is a full
five-root witness, a contradiction.  Hence (3.1) holds.

Now suppose that the intersection is `\{a,b\}`.  Both vertices lie on
`P_z`.  Minimum path length and the edge `ab` make them consecutive.  The
third vertex of `T_w` cannot also lie on `P_z`: shortcutting the first and
last of the three clique vertices either gives a shorter four-root witness
or restores one of `a,b` and gives a forbidden five-root witness.  The
third vertex is therefore outside `P_z` and, being adjacent to `w`, lies in
`K_z`.  Its two claimed adjacencies are the remaining edges of `T_w`.
\(\square\)

Thus the same literal edge is simultaneously met from the omitted centre
and from the retained four-root component in the overlap-two case.  This
strengthens the one-witness geometry, but it does not itself synchronize a
minor colouring: the contraction still permits all three free colours on
the omitted centre.

## 4. Positive overlap gives an explicit `K_5^-` core

### Lemma 4.1 (overlap-core extraction)

If `T_z\cap T_w` is nonempty, then `G[D\cup\{z,w,p,q\}]` contains a
`K_5^-` minor model whose only possibly missing adjacency is between the
singleton bags `\{z\},\{w\}`.

#### Proof

The equal-triangle case is excluded by Lemma 3.1.

Suppose first that the triangles share two vertices `a,b`.  Their remaining
vertices `c in T_z` and `d in T_w` have the same third free colour, say
`gamma_3`.  Choose any path

\[
                    R\in\mathcal P_{\beta,3}.          \tag{4.1}
\]

Its internal vertices avoid `a,b,z,w` by their colours.  The five bags

\[
                   \{z\},\quad\{w\},\quad\{a\},
                   \quad\{b\},\quad V(R)              \tag{4.2}
\]

are disjoint and connected.  The triangle edges make every pair adjacent
except `\{z\},\{w\}`: in particular `a,b` each see an end of `R`, while
`z` sees `c` and `w` sees `d`.

Suppose instead that the triangles share exactly one vertex `a`, of colour
`gamma_1`.  Let their two `gamma_2` vertices be `b_z,b_w`, and their two
`gamma_3` vertices be `c_z,c_w`.  Choose

\[
 R_2\in\mathcal P_{\beta,2},\qquad
 R_3\in\mathcal P_{\delta,3}.                          \tag{4.3}
\]

The two paths are vertex-disjoint because their colour sets are disjoint.
They also avoid `a,z,w`.  Now

\[
              \{z\},\quad\{w\},\quad\{a\},
              \quad V(R_2),\quad V(R_3)                \tag{4.4}
\]

are the required bags.  The two path bags are adjacent through both pairs
of triangle edges `b_zc_z,b_wc_w`; the other adjacencies follow directly
from the two triangles.  Again only `zw` is absent.  \(\square\)

The model in Lemma 4.1 is not shore-confined at five prescribed boundary
roots, so the existing shore-confined rooted completion theorem does not
apply to it.

## 5. The exact disjoint-triangle path obstruction

Assume now that `T_z,T_w` are disjoint.  A **coordinate core** is obtained
by choosing, for every `i`, a path

\[
 R_i\in\mathcal P_{\beta,i}\cup\mathcal P_{\delta,i}   \tag{5.1}
\]

so that `R_1,R_2,R_3` are pairwise vertex-disjoint.  Then

\[
                  \{z\},\quad\{w\},\quad
                  V(R_1),V(R_2),V(R_3)                 \tag{5.2}
\]

is a `K_5^-` model: distinct path bags are adjacent at their `T_z` ends
and at their `T_w` ends, and both centre bags see all three path bags.

### Lemma 5.1 (exact lock-packing residue)

A coordinate core exists if and only if, for at least one
`epsilon in \{beta,delta\}` and two distinct indices `i,j`, there are
vertex-disjoint paths

\[
                 R_i\in\mathcal P_{\epsilon,i},
                 \qquad R_j\in\mathcal P_{\epsilon,j}. \tag{5.3}
\]

Consequently, if the lock mechanism does not already give a `K_5^-` core,
then for both `epsilon=beta,delta` and every pair of distinct indices `i,j`,

\[
 P_i\cap P_j\ne\varnothing
 \quad\text{for every }P_i\in\mathcal P_{\epsilon,i},
 P_j\in\mathcal P_{\epsilon,j}.                       \tag{5.4}
\]

Every intersection in (5.4) is an `epsilon`-coloured vertex.

#### Proof

If (5.3) holds, let `k` be the third index and choose any path in
`mathcal P_{epsilon',k}`, where `epsilon'` is the other pole colour.  Its
two colours are disjoint from the colour set of each path in (5.3), so all
three paths are vertex-disjoint and form a coordinate core.

Conversely, among the three paths of a coordinate core, two use the same
one of the two pole colours.  They give (5.3).  Negating this equivalence
gives (5.4).  Paths belonging to different free colours can share only
their common pole colour, proving the last assertion.  \(\square\)

Condition (5.4) is the exact smallest obstruction left by the six Kempe
locks.  It is a simultaneous same-colour pinch, not a failure of any one
lock.

## 6. What would make the `K_5^-` core terminal

The following elementary completion criterion isolates the missing graph
structure.

### Lemma 6.1 (two-helper completion)

Let

\[
                      \{z\},\{w\},B_1,B_2,B_3          \tag{6.1}
\]

be one of the `K_5^-` models above, chosen disjoint from
`C\cup\{p,q\}`.  Suppose there are disjoint connected subgraphs `X_p,X_q`
of

\[
             G[(D\cup\{p,q\})-\bigcup_{i=1}^3B_i]
\]

such that

\[
 p\in X_p,\qquad q\in X_q,                            \tag{6.2}
\]

and each of `X_p,X_q` is adjacent to `B_1,B_2,B_3`.  Then `G` contains a
`K_7^-` minor.

#### Proof

The set

\[
                              X_q\cup C                \tag{6.3}

\]

is connected because `C` is connected and has a neighbour at `q`.  It is
disjoint from `X_p` and the five core bags.  It is adjacent to `X_p`
through an edge from `p` to `C`.  The set `X_p` is adjacent to `z,w`
through the literal edges `pz,pw`, while `X_q\cup C` is adjacent to them
because `C` is full at the boundary.  Both completing bags are adjacent to
`B_1,B_2,B_3` by hypothesis.  These seven bags have only the one adjacency
already allowed to be missing inside the `K_5^-` core.  \(\square\)

Each individual Kempe lock gives a path from each pole to each relevant
triangle vertex.  It does not give the two disjoint *simultaneous* helpers in
Lemma 6.1.  Paths of different free colours can pinch at common
`beta`-coloured vertices on the `p` side and at common `delta`-coloured
vertices on the `q` side.  A coordinate path can also be forced through
one of the poles, preventing that pole from serving as a separate
completing bag.

The opposite-pole edge `yq` does not by itself repair this.  The connected
set `C\cup\{q,y\}` already supplies all required contacts to `p,z,w`, but
it sees a non-centre core bag only through an actual `q`- or `y`-contact in
`D`.  Neither the boundary matching nor the local clique structure of
`N_D(y)` forces those contacts to meet all coordinate bags.

## 7. Exact nonclosure and smallest repair

The shared-pole saturated row is therefore reduced to the following exact
residue.

1. The two triangles are distinct and overlap in at most two vertices.
2. Positive overlap gives a colour-anchored `K_5^-` core explicitly, but
   its path bags need not avoid `p,q`.
3. With disjoint triangles, failure to obtain that core from the locks is
   exactly the pairwise same-pole intersection condition (5.4).
4. Even when the core exists, it must be selected pole-clean simultaneously
   with the two-helper packing in Lemma 6.1.  The six separate locks do not
   supply either joint requirement.

The smallest useful repair lemma is consequently a **shared-pole two-helper
theorem**: under the present critical-host and four-root-witness hypotheses,
either produce a pole-clean core and the two completing helpers of
Lemma 6.1, produce a common
six-colouring, or expose an actual trace-preserving separation anchored at
the chosen minimum side.  In the disjoint-triangle case it must first break
the exact pinch condition (5.4), or return that anchored separation.

This does not refute such a theorem.  It shows why counting six Kempe paths,
using the opposite centre--pole edge, or extracting the unrooted `K_5^-`
core alone is nonterminal.
