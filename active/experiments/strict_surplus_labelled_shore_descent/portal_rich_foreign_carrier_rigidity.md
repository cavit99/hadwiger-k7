# Rigidity of the portal-rich owned foreign carrier

**Status:** experimental application of the audited lexminimal-carrier
rigidity theorem; independent audit pending.

Use the sole-arm path state of
[`one_arm_path_rigidity.md`](one_arm_path_rigidity.md).  Choose an owned
foreign bag `M` which contains at least two distinct literal vertices
adjacent to the arm `A`; in the two-owned/no-cross row it may be chosen with
at least three such vertices.

Refine the model choice lexicographically after fixing the contact count and
the minimum multiply rooted donor `D`: minimize `|M|`, allowing every
label-preserving transfer which keeps the selected donor/root/missed-bag
state.  If `M` is contacted, its prescribed root is retained under every
allowed transfer.

## 1. Duty set

The five clique-model duties of `M` are adjacency to

\[
D\quad\text{and the other four foreign bags}.          \tag{1.1}
\]

If `M` is contacted, treat retention of its root, equivalently its contact
with the apex `x`, as a sixth protected duty.  Thus

\[
d=5\quad\text{or}\quad d=6.                           \tag{1.2}
\]

For a vertex `v in M`, a duty is owned when every literal witness of that
duty in `M` uses `v`.  The transfer-minimality hypotheses of the audited
lexminimal-carrier theorem apply: a non-cutvertex owning zero duties can be
removed from `M` and absorbed into an adjacent bag, while one owning a
single duty can be moved into that duty's bag.

## 2. The arm duty is mobile

The duty to `D` is witnessed, on the `D` side, entirely by the arm `A`,
and `M` has at least two distinct arm-portal vertices.  Therefore no single
vertex of `M` owns the `D` duty.

### Theorem 2.1

The carrier `G[M]` has exactly two non-cutvertices and is a path.  The duty
to `D` is one of at most

\[
                         d-4\le2                      \tag{2.1}
\]

mobile duties whose portal vertices may occur internally on that path.
Every other duty is concentrated at one of the two path endpoints.

### Proof

The audited non-cutvertex ownership lemma gives at least two pairwise
disjoint owned duties to every non-cutvertex of `M`.  Hence there are at
most `floor(d/2)<=3` such vertices.

If there were three, then necessarily `d=6`, each would own exactly two
duties, and the six owner pairs would exhaust the duty set.  The audited
three-owner corollary says that every duty is concentrated at its unique
owner.  This contradicts the two distinct portal vertices witnessing the
`D` duty.  Thus `M` has at most two non-cutvertices.

Every connected graph of order at least two has at least two
non-cutvertices, and `|M|>=2` because it has two distinct arm portals.
Thus it has exactly two.  A connected graph with exactly two global
non-cutvertices is a path, by the standard block-tree argument.

The two endpoints own disjoint sets of at least two duties, accounting for
at least four.  Therefore at most `d-4` duties remain mobile.  The `D` duty
is one of them. `\square`

### Corollary 2.2

If `M` is uncontacted, the `D` duty is the **only** mobile duty.  The other
four foreign-bag adjacencies are partitioned into two endpoint-owned pairs.

If `M` is contacted, there is at most one further mobile duty besides
`D`; the four or five remaining duties are endpoint-owned.

## 3. Literal portal interval

Write the path in order as

\[
                         m_1m_2\cdots m_r.
\]

At least two vertices, and in the strongest two-owned row at least three,
belong to the arm-portal set

\[
P_A=N_M(A).                                             \tag{3.1}
\]

All internal vertices which meet a foreign bag do so only for the at-most
one second mobile duty.  Thus a detachable bypass can fail only in the
following exact way:

1. every opposite-side foreign duty is endpoint-owned; or
2. the unique second mobile duty has its portal interval interlaced with
   every arm-portal interval in a way that taking a connected path segment
   destroys one of the endpoint-owned duties or the protected root.

This is the width-one locked-carrier terminal.  It is substantially
narrower than an arbitrary portal graph, but it is not eliminated by
transfer minimality alone.  In particular, when `M` is uncontacted the
quotient state is a path with one mobile duty and two endpoint duty pairs;
a reversible `K_3 join C_4` rotation can still occur.
