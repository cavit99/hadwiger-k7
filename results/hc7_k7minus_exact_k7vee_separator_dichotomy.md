# An exact `K_7^\vee` model gives `K_7^-` or a nested separator

**Status:** written proof; separate internal audit in
[`hc7_k7minus_exact_k7vee_separator_dichotomy_audit.md`](hc7_k7minus_exact_k7vee_separator_dichotomy_audit.md).

This is a `K_7^-`-specific strengthening of the audited retained-core and
opposite-gate arguments for a spanning `K_7^\vee` model.  The strengthening
removes the former nonterminal `K_7^\vee` rotation: one transferable piece
already repairs one of the two missing centre adjacencies, while two
opposite unavoidable gates can monopolize only three remaining branch-set
labels.

## Theorem 1 (near-clique or nested separation)

Let `G` be seven-connected.  Suppose that

\[
                         X,B,C,U_1,U_2,U_3,U_4          \tag{1}
\]

are pairwise disjoint connected sets which partition `V(G)` and satisfy:

1. `B,C,U_1,U_2,U_3,U_4` form a `K_6`-minor model;
2. `X` is anticomplete to `B,C`; and
3. `X` is adjacent to every `U_i`.

Then at least one of the following holds.

1. `G` contains a `K_7^-` minor.
2. For some \(i\) there is a nonempty proper connected set
   \(Y\subset U_i\) such that \(U_i-Y\) is connected and \(N_G(Y)\) is an
   actual vertex separator.  In particular,

   \[
                              |N_G(Y)|\ge7.              \tag{2}
   \]

   If equality holds, every component of `G-N_G(Y)` is adjacent to every
   vertex of `N_G(Y)`.

### Proof

Since the seven sets in (1) span `G`, the first two hypotheses give

\[
                    N_G(X)\subseteq U_1\cup\cdots\cup U_4. \tag{3}
\]

The connected bag \(B\) lies outside \(X\cup N_G(X)\).  Thus \(N_G(X)\) is
an actual separator, and seven-connectivity gives \(\lvert N_G(X)\rvert\ge7\).
Some \(U_i\), say \(U\), consequently contains two distinct vertices
\(p,q\) adjacent to \(X\).

For each of the five foreign branch sets

\[
                         B,C,U_j\quad(j\ne i),           \tag{4}
\]

let its portal set in `U` be the set of its neighbours in `U`.  These five
sets are nonempty because the six foreign bags form a `K_6` model.  A
**retaining core based at \(p\)** is a connected subset of \(U\) containing
\(p\) and meeting all five portal sets.

For \(A\subseteq U\), let \(\Omega(A)\) be the set of foreign labels in (4)
whose whole portal set is contained in \(A\).  Thus \(A\) monopolizes exactly
the adjacencies indexed by \(\Omega(A)\).

Suppose first that a retaining core \(T\) based at \(p\) avoids \(q\), and
let \(Y\) be the component of \(G[U-T]\) containing \(q\).  Then \(Y\) and
\(U-Y\) are nonempty and connected, and \(U-Y\) retains an edge to every
branch set in (4).  In particular, `Y` monopolizes none of the five foreign
adjacencies of `U`.

If \(Y\) meets one of \(B,C\), say \(B\), move \(Y\) from \(U\) into \(B\).
The six sets

\[
                    B\cup Y,\ C,\ U-Y,\ U_j\quad(j\ne i) \tag{5}
\]

remain a `K_6` model: the cut edge between `Y` and `U-Y` restores the
donor--target adjacency, and the retaining core preserves every other
donor adjacency.  The bag \(X\) meets \(B\cup Y\) through \(q\), meets \(U-Y\)
through \(p\), and still meets every other \(U_j\).  Thus \(X\) and the six bags
in (5) form a `K_7^-` model, with only `X-C` possibly absent.

We may therefore assume that \(Y\) misses both \(B,C\).  Either twin bag is a
nonempty far side of \(N_G(Y)\), so \(N_G(Y)\) is an actual separator and
outcome 2 holds.  The same argument applies with `p,q` interchanged.

It remains that each of \(p,q\) belongs to every retaining core based at the
other.  Let \(C_q\) be the component of \(G[U-q]\) containing \(p\), and put

\[
                         Z_q=U-C_q.                      \tag{6}
\]

Define `Z_p` symmetrically.  The standard opposite-gate argument gives:

- \(Z_p,Z_q\) are nonempty connected sets with connected complements;
- their monopoly sets \(\Omega(Z_p),\Omega(Z_q)\) in the five labels (4) are
  nonempty and disjoint; and
- \(Z_p\cap Z_q=\varnothing\).

Indeed, if \(\Omega(Z_q)=\varnothing\), then the connected complement
\(C_q\) meets every portal set and is a retaining core based at \(p\) which
avoids \(q\), contrary to the present case.  The same proves
\(\Omega(Z_p)\ne\varnothing\).

For completeness, the last assertion follows because a vertex in both
gates would make every `p`-to-that-vertex path use `q` and every
`q`-to-that-vertex path use `p`; the suffix of a simple path contradicts
the second condition.  A nonempty portal set cannot be contained in two
disjoint gates, proving disjointness of the monopoly sets.

If either gate misses `B` or `C`, its open neighbourhood is an actual
separator with that connected twin bag on a far side, giving outcome 2.
Assume instead that both gates meet both `B,C`.  Each gate then contains a
`B`-portal and a `C`-portal outside the other gate.  Hence neither `B` nor
`C` belongs to either monopoly set.  The two nonempty disjoint monopoly
sets are therefore subsets of only the three labels \(U_j\), \(j\ne i\).
One of them, say \(\Omega(Z)\), has order one.

Put \(W=U-Z\) and \(X'=X\cup Z\).  The set \(X'\) is connected through the
selected edge from \(X\) to the marked vertex of \(Z\); it meets \(B,C\)
through \(Z\) and meets every \(U_j\), \(j\ne i\), through \(X\).  The set
\(W\) is connected, meets \(X'\) across the cut \(Z\mid W\), and retains
every foreign adjacency except possibly the unique label in \(\Omega(Z)\).
Consequently

\[
                    W,\ X',\ B,\ C,\ U_j\quad(j\ne i)   \tag{7}
\]

are seven disjoint connected branch sets with at most one missing
adjacency.  They form an explicit `K_7^-` model, proving outcome 1.

Finally, if an actual separator in outcome 2 has order seven and one of
its vertices misses a component of its deletion, the other six vertices
separate that component.  This contradicts seven-connectivity and proves
the fullness assertion.  \(\square\)

## Corollary 2 (preserving a fixed two-edge response)

Retain the hypotheses of Theorem 1.  Let

\[
                          H=G-\{rx,ry\}                 \tag{8}
\]

for two edges with \(r\in X\), and suppose the same labelled model (1)
survives in `H`.  If

\[
 |N_H(X)\cap(U_1\cup\cdots\cup U_4)|\ge5,             \tag{9}
\]

then either `H` contains a `K_7^-` model or outcome 2 of Theorem 1 holds
in `G`.  In particular, any fixed six-colouring of `H` remains attached
to the separator outcome.

### Proof

The surviving model gives at least one member of `N_H(X)` in every
`U_i`; (9) puts two in one donor.  Repeat the proof of Theorem 1 with those
two selected vertices.  Every edge used in the branch-set transfer from
`X` to a selected vertex belongs to `H`, so its target outcome is a
`K_7^-` model in `H`.  In the separator outcome, restoring `rx,ry` can add
only `r` to the boundary of the selected donor piece.  That piece already
has a neighbour in `X`, and either `B` or `C` remains a far side, so its
open neighbourhood in `G` is still an actual separator.  The fixed
colouring is not changed.  \(\square\)

When `N_G(X)` has order at least seven, deleting two incident edges removes
at most two boundary vertices.  Thus (9) is automatic whenever the
surviving model still meets all four universal bags.

## Dependencies and provenance

The proof specializes the audited
[retaining-core and opposite-gate lemmas](hc7_near_k7_surplus_core_gate.md)
and the
[one-admissible branch-set transfer](hc7_near_k7_surplus_root_transfer.md).
The new point is that, for a `K_7^-` target, two disjoint nonempty monopoly
sets are confined to only three neutral labels, so one gate loses at most
one adjacency.  No finite enumeration is used.

## Scope

The theorem is computation-free and unbounded.  It is a direct synthesis
and `K_7^-` sharpening of the retaining-core, opposite-gate, and
gate-to-centre arguments already developed in this repository; it is not
claimed as a literature-priority result.

The separator conclusion is not a six-colouring or an exceptional
anti-neighbourhood descent.  Its order need not be seven, and its boundary
need not equal `N_G(z)` for any exceptional degree-eight vertex `z`.
Minor-criticality supplies one-sided boundary colour partitions, but a
second operation producing the same partition is an additional theorem.
