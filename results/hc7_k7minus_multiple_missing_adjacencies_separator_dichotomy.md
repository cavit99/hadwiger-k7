# Multiple missing centre adjacencies give `K_7^-` or a nested separator

**Status:** written proof; separately internally audited in the adjacent
[`_audit.md`](hc7_k7minus_multiple_missing_adjacencies_separator_dichotomy_audit.md)
note.  The proof is computation-free and unbounded.

## 1. The structural dichotomy

### Theorem 1

Let `G` be a seven-connected graph.  Suppose

\[
                         X,U_1,\ldots,U_6                         \tag{1}
\]

are pairwise disjoint nonempty connected sets which partition `V(G)`, and
the six sets `U_1,...,U_6` are pairwise adjacent.  Put

\[
 M=\{i:E_G(X,U_i)=\varnothing\}.                               \tag{2}
\]

If `|M|>=2`, then at least one of the following holds.

1. `G` contains a `K_7^-` minor.
2. For some `j` there is a nonempty proper connected set `Y subset U_j`
   such that `U_j-Y` is connected and `N_G(Y)` is an actual vertex
   separator.

Every separator in outcome 2 has order at least seven.  If it has order
seven, every component of its deletion is adjacent to every separator
vertex.

#### Proof

Choose `m in M`.  The connected set `U_m` lies outside `X union N_G(X)`,
so `N_G(X)` is an actual separator.  Hence

\[
                              |N_G(X)|\ge7.                       \tag{3}
\]

All these neighbours lie in the at most four sets `U_i` with `i notin M`.
Some contacted set, say `U_1` after relabelling, therefore contains two
distinct vertices `p,q` adjacent to `X`.

For `i=2,...,6`, let

\[
                    P_i=N_G(U_i)\cap U_1.                         \tag{4}
\]

Each `P_i` is nonempty.  Call a connected subset `T subseteq U_1` a
`p`-retaining core when it contains `p` and meets every `P_i`.

Suppose first that a `p`-retaining core `T` avoids `q`.  Let `Y` be the
component of `G[U_1-T]` containing `q`, and put `W=U_1-Y`.  Every other
component of `G[U_1-T]` has an edge to the connected set `T`.  Consequently
`W` is connected, contains `T`, and retains an edge to every `U_i`.

If `Y` meets all but at most one of the sets `U_i` with `i in M`, then

\[
                        X\cup Y,\quad W,\quad U_2,\ldots,U_6       \tag{5}
\]

are seven disjoint connected branch sets with at most one missing
adjacency.  Indeed, `X union Y` is connected through the selected
`X-q` edge, it meets `W` across the cut `Y | W`, it retains every old
contact of `X`, and `Y` supplies all but at most one missing contact.  The
set `W` retains all five adjacencies in (4).  Thus (5) is a `K_7^-` model.

Otherwise `Y` is anticomplete to some `U_i` with `i in M`.  That connected
set is a nonempty far side of `N_G(Y)`, so the open neighbourhood is an
actual separator.  Both `Y` and its complement in `U_1` are connected, as
required.  The same argument applies with `p,q` interchanged.

It remains to assume that every `p`-retaining core contains `q` and every
`q`-retaining core contains `p`.  Let `C_q` be the component of
`G[U_1-q]` containing `p`, and define

\[
                         Z_q=U_1-C_q.                              \tag{6}
\]

Define `Z_p` symmetrically.  Each `Z_s` is nonempty and connected, and its
complement in `U_1` is connected.  Moreover,

\[
                              Z_p\cap Z_q=\varnothing.              \tag{7}
\]

To see (7), a vertex in both sets would make every path from `p` to that
vertex use `q` and every path from `q` to it use `p`; the suffix of a
simple path gives a contradiction.

For `Z subseteq U_1`, put

\[
 \Omega(Z)=\{i\in\{2,\ldots,6\}:P_i\subseteq Z\}.                 \tag{8}
\]

Both `Omega(Z_p)` and `Omega(Z_q)` are nonempty.  Otherwise the connected
complement of the relevant set would meet every `P_i` and would be a
retaining core avoiding the opposite marked vertex.  Choose
`i in Omega(Z_p)`.  Equations (7)--(8) show that `Z_q` is anticomplete to
`U_i`.  Hence `U_i` is a nonempty far side of `N_G(Z_q)`.  Taking
`Y=Z_q` gives outcome 2.

Finally, seven-connectivity gives `|N_G(Y)|>=7` for every returned
separator.  If equality holds and a separator vertex misses a component
of `G-N_G(Y)`, the other six separator vertices separate that component,
contrary to seven-connectivity.  This proves the fullness assertion.
\(\square\)

## 2. A fixed-operation version

### Corollary 2

Let `F` be an edge-star centred at a vertex `r in X`, and put `H=G-F`.
Assume that the labelled sets in (1) still form the stated spanning model
in `H`, that at least two of the other six sets are anticomplete to `X` in
`H`, and that one contacted `U_j` contains two distinct vertices adjacent
to `X` in `H`.  Then either `H` contains a `K_7^-` minor, or outcome 2 of
Theorem 1 holds in `G`.  In the latter case any fixed six-colouring of `H`
remains attached to the returned separator.

#### Proof

Run the retaining-core proof entirely in `H`, beginning with the two
specified surviving portals.  Every minor-model edge used in outcome 1
then belongs to `H`.  In a separator outcome, restoring `F` can add only
the centre `r` to the open neighbourhood of a selected donor piece; it
cannot add an edge from that piece to the foreign connected set used as a
far side.  Its open neighbourhood in `G` is therefore still an actual
separator.  No recolouring or second operation is introduced. \(\square\)

## 3. Scope

Theorem 1 generalizes the exact two-missing-adjacency argument in
[`hc7_k7minus_exact_k7vee_separator_dichotomy.md`](hc7_k7minus_exact_k7vee_separator_dichotomy.md).
Its extra point is that three or more missing centre adjacencies need no
multi-target linkage: an avoidable retaining core is absorbed into the
centre, while unavoidable opposite cores already expose a separator.

The separator conclusion is not a six-colouring and is not an exceptional
anti-neighbourhood descent.  Its order can exceed seven, and its boundary
need not equal `N_G(z)` for any degree-eight exceptional vertex `z`.
Corollary 2 retains one named operation, but it does not prove that the
fixed colouring is proper on either new closed shore.  These are separate
terminalization obligations.
