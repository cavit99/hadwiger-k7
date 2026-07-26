# Independent audit of the six-vertex source-rooted `K_4` lemma

## Verdict

**GREEN** at the exact source and verifier revisions

```text
720b3a93f646f4515824c01f3da1ec7ce9ba90694d0227585c498d2740f6617c  results/hc7_six_vertex_source_rooted_k4.md
f9b0649fb9e5a7b4ec84027d614738e883c9b2b045a36f2dc8176117ccbce5ef  results/hc7_six_vertex_source_rooted_k4_verify.py
```

The written proof, all displayed branch sets, the finite regression and the
seven-column corollary are correct.  This is a separate internal audit, not
external peer review.

The only source change after the mathematical audit was replacing the
pending-audit status text with the link to this audit; no theorem or proof
content changed.

## 1. Written proof

For `H=Q[R]`, the identity

\[
       2|E(H)|+d_Q(q)=\sum_{r\in R}d_Q(r)\ge15
\]

and `d_Q(q)<=3` give `|E(H)|>=6`; every marked vertex has degree at least
two in `H`.  When `H` has at least eight edges, the proof's branch sets
correctly handle the only two-edge complement obstruction.

At six edges, equality forces complementary degree sequence
`(2,2,2,1,1)`, whose only forms are `P_5` and `C_3` disjoint union `K_2`.
The latter makes `H=K_{2,3}`.  The degree hypotheses force exactly the
stated neighbours of the auxiliary vertex, and both displayed models are
connected and pairwise adjacent.

At seven edges, the three-edge complement has maximum degree two.  The
three listed forms—`C_3` plus two isolated vertices, `P_4` plus one isolated
vertex, and `P_3` plus `P_2`—are exhaustive.  Each displayed model has four
disjoint connected pairwise adjacent bags meeting the marked set.

## 2. Exhaustive regression

The dependency-free verifier checks all `2^15` simple graphs.  It permits
unused vertices when enumerating minor models and requires all four branch
sets to meet the marked set.  It independently reproduces

```text
eligible_graphs 1656
edge_minimal_graphs 175
rooted_core_orbits 5
rooted_core_certificate_sha256 613efaf4a975e63ed872525e1c11a64fd78cc870f030b81535b21cb98e6a2abb
failures 0
PASS six_vertex_source_rooted_k4
```

The five embedded certificate rows are exactly the five source-relabelled
orbits of edge-minimal eligible graphs, and every displayed branch-set
certificate passes the direct connectivity and contact checks.

## 3. Column-contact corollary

If the target contacts all five sources and every source has contact degree
at least four, deleting the target leaves all five source degrees at least
three.  The auxiliary vertex must be the assumed low-degree vertex.  The
rooted `K_4` model returned by the theorem is completed to a `K_5` model by
the target because each branch set contains a source.  The contradiction to
`K_5`-minor exclusion is valid.

The result does not make the low-degree source nonadjacent to the target,
produce a bounded host separator, or close the response-column branch.
