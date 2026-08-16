# Every complete bipartite graph `K_{2,n}` is contractible

**Status:** written proof; separate internal audits GREEN.

This note settles, and strengthens, the explicit question of
Kündgen--Pelsmajer--Ramamurthi asking whether `K_{2,4}` is contractible.
The proof applies to the entire family `K_{2,n}`.  Its new step is to encode
the two hub sides of a coloured scheme as two graphic matroids on the same
ground set.  A path--component incidence count verifies Edmonds' matroid
union inequalities and produces two disjoint spanning trees.

## 1. Definitions and statement

Let `H` be a graph and let `G` contain `V(H)`.  An **`H`-scheme** in `G` is
a family of paths

\[
                         (P_{uv}:uv\in E(H))
\]

such that `P_{uv}` is a `u`--`v` path containing no other vertex of `H`,
and every nonempty family of scheme paths having a common vertex has a
common end in `H`.  The graph `H` is **contractible** if the existence of an
`H`-scheme always forces an `H`-minor rooted at `V(H)`.

Kündgen, Pelsmajer, and Ramamurthi proved that it is enough to consider a
**coloured `H`-scheme**: its underlying graph has a proper colouring

\[
                             f:V(G)\longrightarrow V(H),
\]

every path `P_{uv}` uses only the colours `u,v`, every edge of `G` belongs
to exactly one scheme path, and every vertex outside `V(H)` has degree at
least four.  More precisely, their Lemma 3.3 obtains such a coloured scheme
in a rooted minor of the original scheme graph.  We use that reduction once,
at the start of the proof.

### Theorem 1.1

For every integer `n\geq1`, the graph `K_{2,n}` is contractible.

In particular, `K_{2,4}` is contractible.

## 2. The two projection multigraphs

### Proof of Theorem 1.1

The case `n=1` follows from the contractibility of forests, so suppose
`n\geq2`.  Let the two vertices in the part of order two be `a,b`, and let
the other vertices be

\[
                             t_1,\ldots,t_n.
\]

By the coloured-scheme reduction, it is enough to consider an underlying
graph `G` of a coloured `K_{2,n}`-scheme.  Write

\[
 A=f^{-1}(a),\qquad B=f^{-1}(b),\qquad L_i=f^{-1}(t_i).
\]

Every vertex of `L_i` lies on both `P_{at_i}` and `P_{bt_i}`.  Indeed,
`t_i` has degree two in `K_{2,n}`, so this is Remark 3.2(7) of the
coloured-scheme reduction.  Consequently every vertex
`x\in L_i-\{t_i\}` has exactly two neighbours in `A` and exactly two
neighbours in `B`: it is internal on each of those two paths, and every
edge of `G` belongs to exactly one scheme path.

Put

\[
                         E=\bigcup_{i=1}^n(L_i-\{t_i\}).       \tag{2.1}
\]

Construct an abstract edge-labelled multigraph `M_a` with vertex set `A`
and edge set `E` by replacing each `x\in E` with an edge, labelled `x`,
joining its two neighbours in `A`.  The two neighbours are distinct because
a scheme path is a path.  Parallel edges are allowed.  Define the abstract
edge-labelled multigraph `M_b` on vertex set `B` analogously, using the same
set `E` of edge labels.

Suppressing the vertices of `L_i-\{t_i\}` on `P_{at_i}` gives a path
`Q_i^a` in `M_a`, from `a` to the `A`-neighbour of `t_i`.  If
`P_{at_i}=at_i`, regard `Q_i^a` as the trivial path at `a`.  The paths

\[
                           Q_1^a,\ldots,Q_n^a                 \tag{2.2}
\]

are edge-disjoint.  Put `E_i=L_i-\{t_i\}`.  The colours alternate on
`P_{at_i}`, so `E(Q_i^a)=E_i`: each non-root vertex of colour `t_i` gives
exactly one projected edge.  Thus the edge sets of the paths in (2.2)
partition `E`.  Every vertex in `A-\{a\}` lies on a scheme path incident
with `a`, and hence on one of the paths in (2.2).  Their union is therefore
all of `M_a`, including its vertices, and `M_a` is connected.  The analogous
paths `Q_1^b,\ldots,Q_n^b` satisfy `E(Q_i^b)=E_i`; they show that `M_b` is
connected and give a second partition of the same labelled ground set `E`.

Every vertex of `A-\{a\}` belongs to at least two paths in (2.2).  To see
this, a non-root vertex of colour `a` that lies on `k` of the paths
`P_{at_i}` has degree exactly `2k` in the underlying scheme graph.  The
minimum-degree clause for a coloured scheme gives `2k\geq4`.  The vertex
`a` itself belongs to all `n` paths in (2.2).  The same assertions hold on
the `b` side.

## 3. The component inequality

For `X\subseteq E`, let `c_a(X)` be the number of components of the
spanning subgraph `(V(M_a),X)`, including isolated vertices.  Put
`Y=E-X`.

For a component `C` of `(V(M_a),X)`, let `d_a(C)` be the number of paths
among (2.2) that meet `C`.  The component containing `a` is met by all `n`
paths.  Every other component contains a vertex of `A-\{a\}`, and hence is
met by at least two paths.  Therefore

\[
 \sum_C d_a(C)\ \geq\ n+2(c_a(X)-1).                          \tag{3.1}
\]

On the other hand, after the components of `(V(M_a),X)` are contracted,
the path `Q_i^a` visits at most

\[
                         |E(Q_i^a)\cap Y|+1
\]

distinct components.  Since the edge sets of the paths (2.2) partition
`E`, summing over `i` gives

\[
 \sum_C d_a(C)\ \leq\ n+|Y|.                                 \tag{3.2}
\]

Combining (3.1) and (3.2) yields

\[
                         c_a(X)\leq {|Y|\over2}+1.             \tag{3.3}
\]

The identical argument in `M_b` gives

\[
                         c_b(X)\leq {|Y|\over2}+1.             \tag{3.4}
\]

Thus, for every `X\subseteq E`,

\[
                         c_a(X)+c_b(X)\leq |E-X|+2.            \tag{3.5}
\]

## 4. Matroid packing and the rooted model

Let `\mathcal M_a,\mathcal M_b` be the graphic matroids of `M_a,M_b`,
respectively, on their common ground set `E`, and let `r_a,r_b` be their
rank functions.  Since the two multigraphs are connected,

\[
 r_a(E)=|A|-1,\qquad r_b(E)=|B|-1,
\]

while for every `X\subseteq E`,

\[
 r_a(X)=|A|-c_a(X),\qquad r_b(X)=|B|-c_b(X).                  \tag{4.1}
\]

Equation (3.5) and (4.1) give

\[
 |E-X|+r_a(X)+r_b(X)\geq r_a(E)+r_b(E)                       \tag{4.2}
\]

for every `X\subseteq E`.  Edmonds' matroid union theorem gives

\[
 r_{\mathcal M_a\vee\mathcal M_b}(E)
   =\min_{X\subseteq E}
      \bigl(|E-X|+r_a(X)+r_b(X)\bigr).                       \tag{4.3}
\]

By (4.2), the right side is at least `r_a(E)+r_b(E)`; the reverse
inequality is automatic for the rank of a union.  Hence equality holds.
Choose independent sets `I_a,I_b` whose union has that size.  The chain

\[
 |I_a\cup I_b|\leq |I_a|+|I_b|
                  \leq r_a(E)+r_b(E)
\]

is equality throughout.  Thus `I_a,I_b` are disjoint bases.  Write them as
`T_a,T_b`; in graph language, they are edge-disjoint spanning trees of the
two projection multigraphs.

We now construct the rooted `K_{2,n}` model in the coloured scheme graph.
Let

\[
 \begin{aligned}
  C_a&=A\cup\{x\in E:x\in T_a\},\\
  C_b&=B\cup\{x\in E:x\in T_b\},\\
  C_i&=\{t_i\}\qquad(1\leq i\leq n).
 \end{aligned}                                                \tag{4.4}
\]

The sets in (4.4) are pairwise disjoint.  The tree `T_a` shows that
`G[C_a]` is connected, because every projected edge `x=uv` represents the
two-edge path `u-x-v`; likewise `G[C_b]` is connected.  Each singleton
`C_i` is connected.  The edge of `P_{at_i}` incident with `t_i` joins
`t_i` to a vertex of `A\subseteq C_a`, and the edge of `P_{bt_i}` incident
with `t_i` joins it to a vertex of `B\subseteq C_b`.  Hence each `C_i` is
adjacent to both `C_a` and `C_b`.  These are precisely the required
adjacencies of a rooted `K_{2,n}` model.

The coloured scheme occurs in a rooted minor of the original scheme graph,
so reversing those contractions gives a rooted `K_{2,n}` model in the
original graph.  This proves the theorem. `\square`

## 5. Significance and exact scope

Kündgen--Pelsmajer--Ramamurthi proved that `K_{2,3}` and `K_{1,1,3}` are
contractible and explicitly asked whether `K_{2,4}` or `K_{3,3}` is
contractible.  Theorem 1.1 answers the `K_{2,4}` half affirmatively and
does so uniformly for every `K_{2,n}`.  It does not settle `K_{3,3}` or
assert that every bipartite graph is contractible.

The proof is unbounded and computation-free.  The only external inputs are
the coloured-scheme reduction and Edmonds' matroid union theorem; the
path--component inequality (3.5) and the conversion of the two bases into
rooted branch sets are the new arguments.

## References

- J. Edmonds, *Submodular functions, matroids, and certain polyhedra*, in
  **Combinatorial Structures and Their Applications**, Gordon and Breach,
  1970, 69--87.  This contains the matroid union/intersection min--max
  theorem used in (4.3).
- A. Kündgen, M. J. Pelsmajer, and R. Ramamurthi,
  [*Finding minors in graphs with a given path structure*](https://arxiv.org/abs/1207.6141),
  Lemma 3.3, Remark 3.2, and Question 8.2.
