# Forcing prescribed roots with pendant four-cycles

**Status:** written proof with a separate internal audit at the exact
revision recorded beside this file. This is a repository deduction,
with no novelty or publication-priority claim.
No external universal weak-contractibility theorem is assumed or verified.

## 1. An exact reduction from rooted to unrooted minors

All graphs are finite and simple. An `H`-minor model in `G` consists of
pairwise disjoint nonempty connected vertex sets `C_v`, one for each
`v in V(H)`, with an edge between `C_u` and `C_v` whenever `uv in E(H)`.
Given distinct prescribed vertices `r_v in V(G)`, the model is rooted if
`r_v in C_v` for every `v`.

### Theorem 1

Let `V(H)={v_1,...,v_n}`, let `G` have order `m`, and let
`r_1,...,r_n` be distinct prescribed vertices of `G`. There is an explicit
polynomial-size construction of graphs `H^+` and `G^+` such that

\[
 H^+\preccurlyeq G^+
 \quad\Longleftrightarrow\quad
 G\text{ contains an }H\text{-minor rooted at }r_1,\ldots,r_n.
 \tag{1}
\]

The construction preserves bipartiteness of each input graph separately.
If `n>0`, the target `H^+` has minimum degree at least two. If `H` is
connected, then `H^+` is connected.

### Construction

The case `n=0` is immediate, so assume `1<=n<=m`. Put

\[
 N_i=i(m+1)\qquad(1\le i\le n).
\]

At `v_i` in `H`, attach `N_i` copies of `C_4`, each meeting the rest of
the graph only at `v_i`. At `r_i` in `G`, attach the same number of
copies in the same manner. All added vertices are distinct. These are
`H^+` and `G^+` respectively.

Each graph gains `3(m+1)n(n+1)/2` vertices and `2(m+1)n(n+1)` edges.
Four-cycles can be attached at any vertex without changing whether the
graph is bipartite. Every new target vertex has degree two, and

\[
 d_{H^+}(v_i)=d_H(v_i)+2N_i\ge2.
 \tag{2}
\]

### Proof of the reverse implication in (1)

Given the rooted model in `G`, retain its branch sets and use each added
vertex of `G^+` as the singleton branch set for its corresponding added
vertex of `H^+`. The attachments at `r_i in C_{v_i}` supply all additional
required edges. This is an unrooted `H^+` model in `G^+`.

### Proof of the forward implication in (1)

Fix an unrooted `H^+` model in `G^+`. Write `C_i` for the branch set of
the original target vertex `v_i`, and `R={r_1,...,r_n}`. For a vertex set
`C`, write `N(C)` for its outside vertex neighbourhood in `G^+`, not its
edge boundary. Distinct target neighbours of `v_i` have disjoint branch
sets, each containing a vertex in `N(C_i)`. Hence

\[
 |N(C_i)|\ge d_{H^+}(v_i)=d_H(v_i)+2N_i.
 \tag{3}
\]

First, every `C_i` contains a member of `R`. Otherwise connectivity puts
it either inside `G-R`, or inside the three-vertex path left by deleting
the attachment root from one added four-cycle. In the first case all its
neighbours are original host vertices, giving `|N(C_i)|<=m-1`; in the
second case `|N(C_i)|<=2`. Both contradict (3), since `2N_i>=2(m+1)`.
There are `n` disjoint sets `C_i` and exactly `n` vertices in `R`, so
each `C_i` contains precisely one of them. Let it be `r_{sigma(i)}`;
then `sigma` is a permutation of `{1,...,n}`.

Because `C_i` contains no other member of `R`, any added vertex in `C_i`
belongs to a four-cycle attached at `r_{sigma(i)}`. Its original-vertex
neighbourhood has size at most `m-1`. Each four-cycle at its attachment
root contributes at most two new vertices to `N(C_i)`: its intersection
with `C_i` is a connected subset of that cycle containing the attachment
root, and a connected proper subset of a cycle has at most two outside
neighbours. Thus

\[
 |N(C_i)|\le m-1+2N_{\sigma(i)}.
 \tag{4}
\]

If `sigma(i)<i`, then `N_i-N_{sigma(i)}>=m+1`, contradicting (3)--(4).
Consequently `sigma(i)>=i` for every `i`; a permutation with this property
is the identity. Each original target branch set therefore contains its
prescribed host root `r_i`.

Put `D_i=C_i cap V(G)`. These sets are nonempty and disjoint. They are
connected: a path in `C_i` between original vertices cannot use an added
cycle to travel between distinct original vertices, since that cycle has
only one attachment root. Equivalently, deleting excursions into added
cycles leaves a path in `G`.

Finally, any added cycle is met by at most one of the original target
branch sets `C_i`. A connected branch set containing another host root
cannot enter it without also containing its attachment root. Hence an
edge between distinct original target branch sets cannot use an added
vertex. Every contact required by `E(H)` is therefore an edge in `G`
between the corresponding sets `D_i`. They form the required rooted
model. This proves (1). QED

## 2. Consequence for bipartite graph schemes

An `H`-scheme in a graph `G` with prescribed roots consists of a path for
each edge `uv in E(H)`, joining its two prescribed roots and containing no
other root internally. Whenever a collection of scheme paths has a common
vertex, the corresponding target edges have a common endpoint.

A target is **weakly contractible** if every one of its schemes has an
unrooted target minor. It is **contractible** if every one has the minor
rooted at its prescribed vertices.

### Corollary 2

The following statements are equivalent:

1. Every finite bipartite graph is contractible.
2. Every finite bipartite graph is weakly contractible.
3. Every finite connected bipartite graph of minimum degree at least two
   is weakly contractible.

### Proof

The implications `1=>2=>3` are immediate. Assume statement 3. First let
`H` be connected with at least two vertices and let an `H`-scheme in `G`
be given. Form `H^+,G^+` by Theorem 1. The original scheme extends to an
`H^+`-scheme by using the literal edges of every added cycle. The new
paths satisfy the intersection condition, and no new root is internal to
an original path. The target `H^+` is connected, bipartite and of minimum
degree at least two. Statement 3 gives an unrooted `H^+` minor in `G^+`;
Theorem 1 then gives the prescribed rooted `H` minor in `G`.

For a disconnected target, the unions of scheme paths corresponding to
distinct components with edges are vertex-disjoint: a common vertex would
contradict the scheme intersection condition. An isolated prescribed root
lies on none of these paths, by the restriction on internal roots. Apply
the preceding argument to each component with edges and retain isolated
roots as singleton branch sets. Their union is the rooted model. Empty
targets cause no difficulty. This proves statement 1. QED

## 3. Scope and the external-input question

Theorem 1 is a root-forcing reduction, and Corollary 2 is a universal
equivalence. Neither proves that the equivalent statements are true.
The weak-contractibility hypothesis must apply to the enlarged target
`H^+`, which depends on the host order. Weak contractibility of one fixed
original target `H` alone does not supply this input.

No external unrooted claim attributed to BLR is used in these proofs.
Applying Corollary 2 to such a claim requires a separate check of its
statement, hypotheses and proof. The reduction cannot repair a gap in
that external argument.
