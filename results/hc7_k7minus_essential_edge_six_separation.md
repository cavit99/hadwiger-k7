# Essential-edge six-separations at the `4n-2` threshold

**Status:** written proof; separate internal audit GREEN for this revision.

Here `K_7^-` denotes `K_7` with one edge deleted.  For a graph `G` of
order `n`, put

\[
                         q(G)=|E(G)|-(4n-2).
\]

## Theorem

Let `G` be an edge-minimal seven-connected graph with no `K_7^-` minor,
and let `xy` be any edge of `G`.  Then `H=G-xy` is six-connected and has
a vertex cut `S` of order six such that:

1. `H-S` has exactly two components `A,B`, with `x in A` and `y in B`;
2. every vertex of `S` has a neighbour in each of `A,B`;
3. `xy` is the only edge of `G` between `A` and `B`;
4. at least one of `A,B` has more than one vertex; and
5. `G[S]` has no `K_5^-` minor; and
6. for `X in {A,B}` and every nonempty `Q subseteq S`, the rooted pair
   `(H[X union Q],Q)` is internally `|Q|`-connected: there is no separation
   `(U,W)` with

   \[
      Q\subseteq U,\qquad W-U\ne\varnothing,
      \qquad |U\cap W|<|Q|.
   \]

For `X in {A,B}`, define

\[
 \delta_X=|E(G[X])|+|E_G(X,S)|-4|X|.
\]

Then

\[
             \delta_A+\delta_B=21+q(G)-|E(G[S])|.     \tag{1}
\]

Moreover, contracting either shore gives the exact formula

\[
                         q(G/X)=q(G)+2-\delta_X.       \tag{2}
\]

### Proof

Edge-minimality gives `kappa(H)<=6`.  We first prove the reverse
inequality.  Suppose that a set `Z` of at most five vertices disconnects
`H`.  Neither `x` nor `y` lies in `Z`, since otherwise `G-Z=H-Z` would be
disconnected.  The graph `G-Z` is connected and differs from `H-Z` only
by the edge `xy`.  Hence `H-Z` has exactly two components, one containing
`x` and the other containing `y`.

The component containing `x` is not the singleton `{x}`: otherwise

\[
                         N_G(x)\subseteq Z\cup\{y\},
\]

contrary to `d_G(x)>=7`.  After deleting `Z union {x}`, the remaining
vertices of that component are still separated from the component
containing `y`.  This is a cut of order at most six in `G`, contradicting
seven-connectivity.  Thus `H` is six-connected.

Choose a cut `S` of order six in `H`.  Since `G-S` is connected, neither
endpoint of `xy` belongs to `S`, and adding `xy` must join all components
of `H-S`.  It follows that there are exactly two such components `A,B`,
that the endpoints lie in different components, and that `xy` is the only
edge of `G` between them.  Each component is adjacent to every vertex of
`S`: if, for example, `s in S` had no neighbour in `A`, then
`S-{s}` would disconnect `H`, contrary to six-connectivity.  This proves
items 1--3.

If both components were singletons, then `G` would have eight vertices.
Seven-connectivity would force every vertex to have degree seven, so
`G=K_8`, which contains `K_7^-`.  This proves item 4.

Contract `A` and `B` separately.  The resulting two vertices are adjacent
to one another and to every vertex of `S`.  Thus the resulting minor
contains

\[
                         K_2\mathbin{\vee}G[S].
\]

A `K_5^-` model in `G[S]`, together with these two universal singleton
branch sets, would be a `K_7^-` model in `G`.  Hence `G[S]` has no
`K_5^-` minor.

It remains to verify the rooted-connectivity assertion.  Fix a shore `X`,
write `Y` for the opposite shore, and suppose that `(U,W)` were a
separation as excluded in item 6.  Put

\[
                         Z=(U\cap W)\cup(S-Q).
\]

Then `|Z|<=5`.  Every vertex of `W-U` lies in `X`; it has no neighbour in
`Y`, and the separation gives no edge from `W-U` to `U-W` inside
`H[X union Q]`.  Hence `H-Z` separates the nonempty set `W-U` from the
nonempty opposite shore `Y`, contrary to six-connectivity.  This proves
item 6.  In particular, when `|X|>=2` and `|Q|=4`, the hypotheses of
Jørgensen's rooted `K_4^-` theorem apply to this literal closed shore.

Write `a=|A|`, `b=|B|`, and `e_S=|E(G[S])|`.  The edge partition above
gives

\[
 \begin{aligned}
 |E(G)|
   &=(4a+\delta_A)+(4b+\delta_B)+e_S+1,\\
 |V(G)|&=a+b+6.
 \end{aligned}
\]

Subtracting `4|V(G)|-2` proves (1).

Finally, contracting `X` removes `|X|-1` vertices.  It replaces the
`|E(G[X])|+|E_G(X,S)|+1` edges internal to or leaving `X` by the seven
edges from the contracted vertex to `S` and to the opposite shore.
Consequently

\[
 |E(G/X)|=|E(G)|-4|X|-\delta_X+6,
\]

which is equivalent to (2).  \(\square\)

## Scope

In a counterexample to the proposed `4n-2` extremal theorem chosen first
with minimum order and then with minimum size, positive surplus makes the
graph edge-minimal seven-connected.
The theorem therefore turns every edge into a full two-shore
six-separation with a `K_5^-`-minor-free boundary and exact shore-excess
accounting.  Equation (2) identifies exactly when a shore contraction
preserves the density threshold.

This does not yet prove that either shore contraction remains
seven-connected.  Nor does the rooted-connectivity conclusion imply that
`G[S]` is subcubic.  If `z in S` has four boundary neighbours `Q`,
Jørgensen's theorem gives four `Q`-rooted branch sets in a nonsingleton
shore.  Those four sets, the opposite shore enlarged by the remaining
boundary vertex, and `{z}` give only six branch sets, not seven.  A valid
completion needs either a fifth rooted branch set, a disjoint connected
residual set with the required adjacencies, or a density-preserving shore
contraction.  The attempted subcubic inference therefore remains an exact
nonclosure, not a theorem.
