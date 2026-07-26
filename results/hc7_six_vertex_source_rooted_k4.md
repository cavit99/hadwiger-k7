# A six-vertex rooted `K_4` lemma for five marked vertices

**Status:** written proof; [separately audited GREEN](hc7_six_vertex_source_rooted_k4_audit.md).
The dependency-free exhaustive regression verifier is
[`hc7_six_vertex_source_rooted_k4_verify.py`](hc7_six_vertex_source_rooted_k4_verify.py).

This note isolates the finite graph fact needed when a target column is
adjacent to all five response-source columns.  It does not use colouring
responses and does not close the remaining same-operation path problem.

## 1. Finite rooted-minor theorem

### Theorem 1.1

Let `Q` be a simple graph on six vertices.  Mark five vertices as the set
`R` and call the remaining vertex `q`.  Suppose

\[
             d_Q(r)\ge3\quad(r\in R),
             \qquad d_Q(q)\le3.                         \tag{1.1}
\]

Then `Q` has a `K_4`-minor model with four pairwise disjoint connected
branch sets, each containing a vertex of `R`.

### Proof

Put `H=Q[R]`, `m=|E(H)|` and `d=d_Q(q)`.  Each marked vertex loses at most
the edge to `q`, so `delta(H)>=2`, and

\[
             2m+d=\sum_{r\in R}d_Q(r)\ge15.             \tag{1.2}
\]

Since `d<=3`, one has `m>=6`.  If `m>=8`, then the complement of `H` has
at most two edges.  When two missing edges share an endpoint, deleting that
endpoint leaves a `K_4`.  When they are disjoint, say `ab,cd`, the bags

\[
                         \{a,c\},\{b\},\{d\},\{e\}
\]

form a `K_4` model.  The cases with at most one missing edge are immediate.
Thus assume `m` is six or seven.

If `m=6`, equality holds in (1.2): `d=3`, every marked vertex has degree
three in `Q`, and `H` has degree sequence `(3,3,2,2,2)`.  Its complement
has degree sequence `(1,1,2,2,2)`, so it is either `P_5` or the disjoint
union of `C_3` and `K_2`.

- In the second case write `H=K_{2,3}=I_2 join I_3`, with bipartition
  `{a,b}` and `{x,y,z}`.  The auxiliary vertex sees exactly `x,y,z`.  The
  four bags

  \[
                         \{x\},\{a\},\{y,b\},\{z,q\}
  \]

  give the required model.
- In the first case label the complementary path
  `p_1p_2p_3p_4p_5`.  The auxiliary vertex sees `p_2,p_3,p_4`, and

  \[
             \{p_1\},\{p_3\},\{p_5\},\{p_2,q,p_4\}
  \]

  are the required bags.

If `m=7`, the complement of `H` has three edges and maximum degree at most
two.  It is therefore one of `C_3` plus two isolated vertices, `P_4` plus
one isolated vertex, or `P_3` plus `P_2`.

- For complementary components `a-b-c` and `d-e`, use
  `\{a\},\{c\},\{b,d\},\{e\}`.
- If the complementary triangle has vertices `x,y,z` and the isolated
  vertices are `a,b`, then `H=K_2 join I_3`.  Degree condition (1.1) makes
  `q` adjacent to `x,y,z`; use `\{a\},\{b\},\{x\},\{q,y\}`.
- If the complementary path is `p_1p_2p_3p_4` and `a` is isolated, then
  `q` sees `p_2,p_3`; use
  `\{a\},\{p_1\},\{p_4\},\{p_2,q,p_3\}`.

Every displayed set is connected, the four sets are pairwise adjacent,
and each contains a marked vertex.  This exhausts the possibilities.
\(\square\)

## 2. Independent finite regression

The verifier represents the fifteen possible edges of `Q` by a bit mask and
checks all `2^15=32,768` graphs.  Exactly `1,656` satisfy (1.1).  For each,
it enumerates every system of four nonempty disjoint branch sets, allowing
unused vertices, and checks connectedness, the six pairwise contacts and
intersection of every branch set with `R`.  There are no failures.

For a compact independently inspectable certificate, the verifier also
deletes edges while retaining (1.1), canonically relabels the five marked
vertices, and obtains exactly five edge-minimal types.  Write
`R={0,1,2,3,4}` and `q=5`.  The table gives every edge set and one rooted
`K_4` model; omitted vertices are unused.

| type | edges | four branch sets |
|---:|---|---|
| 1 | `01 02 03 04 12 13 24 34` | `0; 12; 3; 4` |
| 2 | `01 02 03 04 12 13 24 35 45` | `0; 12; 35; 4` |
| 3 | `01 02 03 12 13 24 34 45` | `0; 1; 24; 3` |
| 4 | `01 02 03 12 14 25 34 35 45` | `01; 25; 3; 4` |
| 5 | `01 02 03 14 15 24 25 34 35` | `01; 25; 3; 4` |

The program checks the displayed branch sets directly.  It finds `175`
labelled edge-minimal graphs, whose five orbits are precisely the rows of
the table.  Every graph satisfying (1.1) contains an edge-minimal graph
satisfying (1.1), and adding edges preserves the displayed minor model.
This independently checks the written proof and provides a compact
certificate of the finite classification.

The expected verifier output is

```text
eligible_graphs 1656
edge_minimal_graphs 175
rooted_core_orbits 5
rooted_core_certificate_sha256 613efaf4a975e63ed872525e1c11a64fd78cc870f030b81535b21cb98e6a2abb
failures 0
PASS six_vertex_source_rooted_k4
```

## 3. Consequence for seven column contacts

### Corollary 3.1 (a source has low contact degree)

Let `J` be a `K_5`-minor-free graph on the seven labelled vertices

\[
                         t,c_0,c_1,c_2,c_3,c_4,q.
\]

Suppose `t c_i` is an edge for every `i` and `J` has a vertex of degree at
most three.  Then at least one source vertex `c_i` has degree at most three.

### Proof

The target `t` has degree at least five.  Suppose every source `c_i` has
degree at least four.  The low-degree vertex must then be `q`, so
`d_J(q)\le3`.

Put `Q=J-t`.  Every source loses exactly its edge to `t` and consequently
has degree at least three in `Q`; the auxiliary vertex still has degree at
most three.  Theorem 1.1 supplies a `K_4`-minor model in `Q` whose four
branch sets each contain a source.  Since `t` is adjacent to every source,
the singleton branch set `{t}` is adjacent to all four model bags.  This is
a `K_5`-minor model in `J`, a contradiction. \(\square\)

## 4. Scope

The corollary removes the possibility that the auxiliary column is the only
low-degree column when the target contacts all five sources.  It does not
make the resulting low-degree source nonadjacent to the target, and it does
not turn quotient degree into a bounded host separator.  The remaining
argument must use the proper-minor colouring response attached to that same
source.
