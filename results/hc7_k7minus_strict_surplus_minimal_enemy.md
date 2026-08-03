# Strict-surplus minimal counterexamples at the `4n-2` threshold

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.  For a graph `G` of
order `n`, put

\[
                         q(G)=|E(G)|-(4n-2).
\]

## Theorem

Suppose that the assertion

\[
 \kappa(H)\ge7,\qquad |E(H)|\ge4|V(H)|-2
 \quad\Longrightarrow\quad K_7^-\preccurlyeq H                 \tag{1}
\]

is false.  Choose a counterexample `G` first with minimum order and then
with minimum size, and assume that `q=q(G)>=1`.  Write

\[
 L=\{x\in V(G):d_G(x)=7\},\qquad F=G-L,
\]

and put

\[
 \ell=|L|,\quad f=|V(F)|,\quad c=c(F),\quad
 e_L=|E(G[L])|.
\]

Then:

1. `G` is minimally seven-connected;
2. `F` is a forest and `c+e_L>=7`;
3. the exact identities

   \[
      6\ell=|E(G)|-|V(G)|+c+e_L
             =3|V(G)|-2+q+c+e_L,                    \tag{2}
   \]

   and

   \[
      3(\ell-f)=c+e_L+q-2                           \tag{3}
   \]

   hold.  In particular, `\ell>=f+2`, so more than half the vertices of
   `G` have degree seven;
4. one has

   \[
      |E_G(L,V(F))|=7\ell-2e_L,\qquad
      \sum_{z\in V(F)}(d_G(z)-8)=\ell-4+2q,          \tag{4}
   \]

   and every component of `F` has at least seven distinct neighbours in
   `L`; and
5. there is a set `R` of at least `\lceil\ell/2\rceil` distinct edges
   covering `L` such that, for every `xy\in R`,

   \[
                 |N_G(x)\cap N_G(y)|\le3,            \tag{5}
   \]

   the contraction satisfies `q(G/xy)>=q(G)`, and an
   order-seven vertex cut of `G` contains both `x` and `y`; and
6. `R` may be chosen to contain either an edge with both ends in `L`, or
   two edges `xz,x'z` with distinct `x,x'\in L` and `z\in V(F)`.

### Proof

If `G-e` were seven-connected for some edge `e`, then

\[
 q(G-e)=q-1\ge0.
\]

Edge deletion cannot create a `K_7^-` minor, so `G-e` would contradict
the choice of `G`.  Hence `G` is minimally seven-connected.

For a minimally `k`-connected graph, Mader's structure lemmas state that
the subgraph induced by the vertices of degree greater than `k` is a
forest and that

\[
 c_F+|E(G[V_k])|\ge k,                               \tag{6}
\]

where `V_k` is the set of degree-`k` vertices and `c_F` is the number of
components of `G-V_k`.  Schmidt's exact form of the associated degree
count is

\[
 |V_k|=\frac{|E(G)|-|V(G)|+c_F+|E(G[V_k])|}{k-1}.   \tag{7}
\]

Apply these results with `k=7`.  They give assertion 2 and the first
equality in (2).  Substitution of
`|E(G)|=4|V(G)|-2+q` gives the second equality.  Since
`|V(G)|=\ell+f`, rearranging (2) gives (3).  Now
`c+e_L>=7` and `q>=1`, so (3) gives `\ell-f>=2`.

Summing the degrees over `L` gives

\[
                         |E_G(L,V(F))|=7\ell-2e_L.
\]

Every vertex of `F` has degree at least eight.  If `C` is a component of
the forest `F`, then a leaf of `C` has at most one neighbour in `F` and
therefore at least seven distinct neighbours in `L` (a one-vertex
component has at least eight).  This proves the component assertion.
Finally,

\[
 \begin{aligned}
  2|E(G)|
    &=7\ell+\sum_{z\in V(F)}d_G(z)\\
    &=8|V(G)|-\ell+\sum_{z\in V(F)}(d_G(z)-8).
 \end{aligned}
\]

Comparison with `2|E(G)|=8|V(G)|-4+2q` proves the second identity in
(4).

It remains to prove assertion 5.  Apply the audited
[degree-seven safe-contraction theorem](hc7_k7minus_degree7_safe_contraction.md)
at each `x\in L`.  It supplies a neighbour `y` satisfying (5) and the
exact identity

\[
 q(G/xy)=q+3-|N_G(x)\cap N_G(y)|\ge q.               \tag{8}
\]

The graph `G/xy` is `K_7^-`-minor-free because it is a minor of `G`.  It
cannot be seven-connected: otherwise it would be a smaller counterexample
to (1).  Let `w` be the contracted vertex.  Since the density assumption
with `q>=1` forces `|V(G)|>=9`, the graph `G/xy` has more than seven
vertices, and it has a vertex cut `X` of order at most six.  Necessarily
`w\in X`; otherwise splitting `w` back into the adjacent vertices `x,y`
inside its component would show that `X` disconnects `G`.  When `w\in X`,
deleting `X` from `G/xy` and deleting

\[
                         (X-\{w\})\cup\{x,y\}         \tag{9}
\]

from `G` leave the same graph.  Thus (9) is a vertex cut of `G`.
Seven-connectivity forces it to have order seven.  Hence `|X|=6`, and
(9) is the required exact cut containing both ends of `xy`.

Choose one such edge for every `x\in L`, and let `R` be the set of
distinct chosen edges.  It covers `L`; since one edge covers at most two
vertices of `L`, `|R|>=\lceil\ell/2\rceil`.  This proves assertion 5.

If one chosen edge has both ends in `L`, the first alternative in
assertion 6 holds.  Otherwise every chosen edge joins its named vertex of
`L` to a vertex of `F`.  If no two chosen edges shared their endpoint in
`F`, these choices would define an injection from `L` into `V(F)`, contrary
to `\ell>f`.  Hence two chosen edges form the stated two-edge star.  This
proves assertion 6.
\(\square\)

## External input

The exact source used above is J. M. Schmidt, *Tight bounds for the
vertices of degree k in minimally k-connected graphs*, Journal of Graph
Theory **88** (2018), 146--153, Theorem 4,
doi:`10.1002/jgt.22202`.  Schmidt states the forest and component-count
inputs as Lemmas 1 and 2, attributing them respectively to:

- W. Mader, *Ecken vom Grad n in minimalen n-fach zusammenhängenden
  Graphen*, Archiv der Mathematik **23** (1972), 219--224, Korollar 1;
- W. Mader, *Zur Struktur minimal n-fach zusammenhängender Graphen*,
  Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg
  **49** (1979), 49--69, p. 66.

## Scope

This theorem is a strict-surplus reduction, not a proof of (1).  The
Mader--Schmidt forest structure does not apply to a minimal enemy at
`q(G)=0`, because such an enemy need not be minimally seven-connected.
The safe incident contractions themselves remain available there.  When
`q>=1`, the theorem produces many density-preserving failed contractions
and exact seven-cuts, but neither
the Mader--Schmidt forest nor (2)--(4) presently forces those cuts to be
laminar or to share enough branch-set adjacencies to form a `K_7^-`
model.  The remaining inference is to prove that one edge supplied by
assertion 5 is seven-contractible, or to convert the family of exact
seven-cuts witnessing their failure into an explicit `K_7^-` model.  Even
the safe edge or two-edge star in assertion 6 may have coincident or nested
cut certificates.  The first unsupported inference in the natural
Kawarabayashi-style uncrossing is that those certificates have a corner
containing another safe edge and strictly smaller than a selected shore;
the present hypotheses permit the nested root-swap residue instead.

The antecedent is K. Kawarabayashi, *Note on `k`-contractible edges in
`k`-connected graphs*, Australasian Journal of Combinatorics **24** (2001),
165--168, Theorem 5.  Its odd-connectivity argument assumes that the graph
contains no `K_4^-` subgraph and obtains a triangle-free edge; neither fact
follows from `K_7^-`-minor exclusion.
