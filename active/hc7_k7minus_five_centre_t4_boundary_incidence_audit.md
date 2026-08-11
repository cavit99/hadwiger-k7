# Internal audit of the four-root boundary-incidence refinement

Audited file:
`active/hc7_k7minus_five_centre_t4_boundary_incidence.md`

Audited SHA-256:

```text
7074e236eea1bfd5ac38c605ff258e07a8de7c85fc2c5d5c05468f84e7997b91
```

**Verdict:** **GREEN.**  The exact boundary-matching lemma, the
three-contact path/triangle description, the exclusion of the
`(d_z,\rho_z)=(3,1)` four-contact row, the resulting literal `K_5^-`, and
Corollary 4.1 are correct under the stated cited inputs.  No unresolved gap
was found in this revision.

This is a hash-pinned internal mathematical audit, not external peer review.
Relative to the theorem revision originally checked, the source changes
only its audit-status metadata; no theorem or proof text changed, so the
GREEN verdict is retained.

## 1. Scope and dependencies

The audit takes as established the cited five-centre two-cut reduction, the
exceptional-neighbourhood conclusion `\alpha(G[N(z)])=3`, literal `K_5`
exclusion (and hence `K_4`-freeness of `G[N(z)]`), the GREEN four-root atom
identity and singleton table, and the separately audited distinct-side
palette transfer.  Those upstream theorems were not re-proved here.

The singleton-atom input used below is literal: all vertices of `N_C(z)`
lie on one induced `p`--`q` path.  Since `C,D` are different components of
`G-S`, the sets `N_C(z)` and `N_D(z)` are anticomplete.

## 2. Boundary matching

Fix an edge `zp`.  If `q` had no neighbour in `Z-\{z\}`, then

\[
 I=S-\{z,p\}=(Z-\{z\})\cup\{q\}
\]

would be independent.  The partition
`I\mid\{z\}\mid\{p\}` satisfies the exact reflection lemma: either full
connected component can be assigned to `I`, while the two retained
singleton vertices form the clique edge `zp`.  Reflecting in both
directions gives the same exact boundary partition on the two closed
shores, so their colourings glue after renaming colours.  This contradicts
seven-chromaticity.

Thus every centre--pole edge extends to a disjoint centre--opposite-pole
edge.  Since the two poles cover every edge of `G[S]`, its matching number
is at most two; since the two-cut theorem supplies one boundary edge and
that edge extends, its matching number is exactly two.  Lemma 2.1 is
therefore exact.

## 3. Three contacts

Let `U=N_C(z)` and `T=N_D(z)`.  The singleton table first gives

\[
 |U|=3,\qquad \rho_z=2,qquad G[T]\cong K_3.
\]

Because `T` is a nonempty clique anticomplete to `U` and
`\alpha(G[N(z)])=3`, one has `\alpha(G[U])=2`.  An induced subgraph of a
path on three selected vertices with independence number two is either
`P_3` or `K_2\mathbin{\dot\cup}K_1`.

For either pole `t`, inducedness of the atom path gives
`|N_U(t)|\le1`.  The pole cannot be complete to the triangle `T`, since
that would give a `K_4` in `N(z)`.  Choose `d\in T-N(t)`.  For every
independent pair `J\subseteq U`, the set `J\cup\{d,t\}` would be an
independent four-set unless `t` met `J`.  Hence the at most one vertex in
`N_U(t)` must hit every independent pair of `G[U]`.

If `G[U]=K_2\mathbin{\dot\cup}K_1`, its isolated vertex is the unique
one-vertex transversal of all independent pairs.  Both poles would be
adjacent to it.  Since it lies on the induced pole path, it would then be
consecutive to both endpoints, leaving no place for the other two
contacts.  Thus `G[U]=P_3`.

The only independent pair of this `P_3` is its two ends.  Each pole meets
one end, and the poles must meet different ends: otherwise that common
contact would again be consecutive to both pole endpoints of the induced
path.  Every displayed edge of the `P_3` and both pole-contact edges must
be consecutive on the induced path.  This proves, up to reversal,

\[
                         P_z=p-u_1-u_2-u_3-q.
\]

If a triangle vertex `d` missed both poles, then
`\{p,q,u_2,d\}` would be independent.  Therefore the two pole
neighbourhoods cover `T`, while `K_4`-freeness makes each a proper subset.
All assertions of Lemma 3.1 follow.

## 4. Four contacts

For `|U|=4`, the singleton table and the degree identity leave only

\[
 (d_z,\rho_z)=(3,1)\quad\text{or}\quad(2,2),
\]

and `T` is a clique.  Again `\alpha(G[U])=2`.  The only four-vertex
induced subgraphs of a path with independence number two are `P_4` and
`2K_2`; in either graph, no single vertex meets every independent pair.

In the `(3,1)` case, let `t` be the sole pole adjacent to `z`.  The
triangle `T` and `K_4`-freeness provide `d\in T-N(t)`.  The pole has at
most one neighbour in `U`, so an independent pair `J\subseteq U` avoids
that neighbour.  Then `J\cup\{d,t\}` is an independent four-set in
`N(z)`, a contradiction.  Thus `(d_z,\rho_z)=(2,2)`.

Now both poles lie in `N(z)` and `T\cong K_2`.  If a pole `t` missed an
endpoint `d` of `T`, the same independent-pair argument would again give
an independent four-set.  Each pole is therefore complete to `T`.  On the
five literal vertices `\{z,p,q\}\cup T`, every edge is present except
`pq`: `z` sees both poles and both members of `T`, the poles see `T`, and
`T` is an edge.  This is exactly a literal `K_5^-`, verifying Lemma 3.2.

The local `K_5^-` is not asserted to finish the global target.  Under the
additional hypotheses of Corollary 4.1, however, the audited distinct-side
transfer theorem applies directly to `\rho_z=2,d_z=2` and produces a
six-colouring of `G`.  Hence that four-contact row is impossible in the
stated opposite five-root-minimal branch.

## 5. Exact scope

The final nonclosure statement is accurate.  Boundary matching number two
does not synchronize the relevant Kempe connections, and the literal
five-vertex `K_5^-` need not be a shore-confined rooted model.  The note
does not claim either missing allocation, nor does it eliminate the
two- and three-contact singleton rows.
