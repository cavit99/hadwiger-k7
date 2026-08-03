# Exact density of a minimum `4n-7` enemy

**Status:** written computation-free theorem; separate hash-pinned internal
audit GREEN for this revision.

Write `K_7^-` for `K_7` with one edge deleted.  Recall the auxiliary
extremal statement

> **(E5).** Every five-connected graph `G` with
> \[
> |E(G)|\ge 4|V(G)|-7
> \]
> contains a `K_7^-` minor.

An **E5 enemy** satisfies the connectivity and density hypotheses of `(E5)`
but has no `K_7^-` minor.  A minimum enemy is chosen first with minimum
order and, subject to that, with minimum size.

## Theorem (strict surplus is impossible)

If an E5 enemy exists, every minimum enemy `G` satisfies

\[
                    |E(G)|=4|V(G)|-7.
\]

### Proof

Put

\[
 n=|V(G)|,\qquad m=|E(G)|,
 \qquad q=m-(4n-7).
\]

Suppose for a contradiction that `q>=1`.

#### Every edge is deletion-critical and has at most four common neighbours

For every edge `e`, the graph `G-e` is still `K_7^-`-minor-free and has at
least `4n-7` edges.  Hence `G-e` is not five-connected, by the minimum-size
choice of `G`.  Thus `G` is minimally five-connected.

Let `e=xy`.  Choose a vertex cut `X` of `G-e` with `|X|<=4`.  Neither end
of `e` belongs to `X`, since otherwise `G-X=(G-e)-X` would be disconnected.
Moreover, `x` and `y` lie in different components of `(G-e)-X`: adding the
single edge `xy` is what makes `G-X` connected.  Every common neighbour of
`x` and `y` therefore belongs to `X`.  Consequently

\[
                  c(xy):=|N_G(x)\cap N_G(y)|\le4.       \tag{1}
\]

#### Every edge is also contraction-critical

Contracting `xy` and suppressing parallel edges gives a graph of order
`n-1` and size `m-1-c(xy)`.  By (1),

\[
\begin{aligned}
 |E(G/xy)|
   &=m-1-c(xy)\\
   &\ge 4n-7+q-5\\
   &\ge 4(n-1)-7.
\end{aligned}                                           \tag{2}
\]

The graph `G/xy` is a proper target-free minor of `G`.  It cannot be
five-connected, since (2) would then make it a smaller E5 enemy.  Thus no
edge of `G` is five-contractible.  In particular, `G` is both minimally
five-connected and contraction-critically five-connected.

#### The degree-five count is contradictory

Let

\[
 L=\{v:d_G(v)=5\},\qquad F=G-L,
\]

and write

\[
 \ell=|L|,\quad f=|V(F)|,\quad c=c(F),\quad
 e_L=|E(G[L])|.
\]

Schmidt's exact degree count for a minimally `k`-connected graph, with
`k=5`, is

\[
              \ell=\frac{m-n+c+e_L}{4}.               \tag{3}
\]

Substituting `m=4n-7+q` and `n=\ell+f` into (3) gives

\[
              \ell-e_L=3f-7+q+c.                      \tag{4}
\]

Su's theorem says that every vertex of a contraction-critically
five-connected graph has at least two neighbours of degree five.  Applied
to vertices of `L`, it gives

\[
                 \delta(G[L])\ge2,qquad e_L\ge\ell.   \tag{5}
\]

Equations (4) and (5) imply

\[
                       3f+c+q\le7.                    \tag{6}
\]

The graph `F` is nonempty.  Otherwise `G` is five-regular, and
`2m=5n`, together with `m=4n-7+q`, gives

\[
                         3n=14-2q\le12,
\]

contrary to five-connectivity.  Therefore `f>=1` and `c>=1`.  Since
`q>=1`, (6) forces `f=1`; hence `c=1`.  Let `V(F)={z}`.  Equation (4) now
gives

\[
                         e_L=\ell+3-q.                 \tag{7}
\]

All edges incident with `z` join it to `L`.  Summing the degrees of the
vertices in `L` and using (7),

\[
\begin{aligned}
 d_G(z)
   &=5\ell-2e_L\\
   &=3\ell-6+2q.
\end{aligned}                                           \tag{8}
\]

Simplicity gives `d_G(z)<=\ell`.  Thus (8) implies

\[
                         \ell\le3-q\le2.
\]

But `n=\ell+1<=3`, impossible for a five-connected graph.  This final
contradiction proves `q=0`.  \(\square\)

## External inputs

The exact identity (3) is Theorem 4 of J. M. Schmidt, *Tight bounds for
the vertices of degree k in minimally k-connected graphs*, Journal of
Graph Theory **88** (2018), 146--153,
<https://doi.org/10.1002/jgt.22202>.

The degree-five-neighbour theorem used in (5) is due to J. Su,
*Vertices of degree 5 in contraction-critical 5-connected graphs*, Journal
of Guangxi Normal University **17** (3) (1997), 12--16 (in Chinese).  Its
exact statement is reproduced as Theorem 1 of C. Qin, X. Yuan and J. Su,
*Some properties of contraction-critical 5-connected graphs*, Discrete
Mathematics **308** (2008), 5742--5756,
<https://doi.org/10.1016/j.disc.2007.10.041>.

## Scope

The theorem eliminates the positive-surplus branch of the minimum-enemy
analysis for `(E5)`.  It does **not** prove `(E5)`: a minimum enemy at the exact threshold
`|E(G)|=4|V(G)|-7` remains possible, because deleting an edge then falls
below the density hypothesis and need not make the graph minimally
five-connected.
