# Internal six-connectivity does not force a prescribed `K_6^-` minor

**Status:** written barrier to an intermediate rooted-minor claim; separate
internal audit GREEN in
[`hc7_k7minus_internal_six_rooted_k6minus_barrier_audit.md`](hc7_k7minus_internal_six_rooted_k6minus_barrier_audit.md).

This nine-vertex example shows that internal six-connectivity, an edge
between two nominated vertices, and even a rooted `K_4` on the other four
vertices do not force a `K_6^-` minor rooted at all six.  It is not a
counterexample to the `K_7^-` six-colour conjecture.

## 1. Construction

Let

\[
 R=U\mathbin{\dot\cup}\{a,b\},\qquad
 U=\{u_1,u_2,u_3,u_4\},\qquad
 W=\{w_1,w_2,w_3\}.
\]

Make every vertex of `R` adjacent to every vertex of `W`.  Let `ab` be the
only edge with both ends in `R`, and let `W` induce the path
`w_1w_2w_3`.  Call the resulting graph `J`.

### Proposition 1.1

The rooted pair `(J,R)` is internally six-connected, and `J` has a
`U`-rooted `K_4` minor, but no `R`-rooted `K_6^-` minor.

#### Proof

Let `(X,Y)` be a separation of `J` with `R subseteq X` and `Y-X` nonempty.
If `w in W cap (Y-X)`, every root is adjacent to `w`, so no root can lie in
`X-Y`.  Hence `R subseteq X cap Y`, and the separator has order at least
six.  This proves internal six-connectivity.

The four connected sets

\[
 \{u_1,w_1\},\quad \{u_2,w_2\},\quad
 \{u_3,w_3\},\quad \{u_4\}
\]

are pairwise adjacent and form a `U`-rooted `K_4`-minor model.

In an `R`-rooted minor model, the branch set rooted at a member of `R`
contains no other root.  Since the branch sets are disjoint, at most three
of them meet `W`.  At least three branch sets are therefore singleton
roots.  Among any three vertices of `R`, at most one pair is adjacent,
because `ab` is the only edge in `J[R]`.  At least two pairs of singleton
branch sets are nonadjacent.  An `R`-rooted `K_6^-` model permits only one
nonadjacent pair, so no such model exists.  \(\square\)

## 2. Scope

The graph `J` is `K_5`-free and its possible selected side `W` is connected.
The degrees of `u_1,...,u_4` are three, the degrees of `a,b` are four, and
`J` is only three-connected.  Thus it is not a critical host.

The obstruction persists even after imposing the local completed-side
condition.  Add a seventh boundary vertex `t` adjacent precisely to
`w_1,w_3`, put `T={a,b,t}`, and complete `T` to a triangle.  On `W union T`
the resulting completed graph is `K_6` with the independent edges
`w_1w_3` and `tw_2` deleted, so it is four-connected.  Each vertex of `W`
has degree eight before the boundary completion.  Nevertheless the two
singleton subgraphs `{w_1}` and `{w_3}` are each adjacent to all seven
vertices of `R union {t}`.  This violates the generalized-wheel conclusion
that no component contains two disjoint connected subgraphs with that
property.

Thus the example refutes only the implication

\[
 \text{internal six-connectivity + `ab` + rooted `K_4`}
 \quad\Longrightarrow\quad
 \text{an `R`-rooted `K_6^-` minor}.
\]

It does not refute a theorem forcing either the prescribed rooted `K_6^-`
minor or a trace-preserving exact-cut descent using the critical-host
colouring responses and the full generalized-wheel hypotheses, in
particular the restriction on two such connected subgraphs.
