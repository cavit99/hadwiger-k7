# Barrier: three natural boundary colourings do not force a clean two-linkage

**Status:** explicit computer-assisted counterexample to the intermediate
colouring-to-linkage inference stated below.  The construction is
eight-connected and seven-chromatic, and it satisfies the natural
six-boundary geometry and the full boundary-surjectivity consequence of
deleting a critical vertex.  It deliberately contains a `K_7^-` subgraph,
so it is not a counterexample to `HC_7` or to a statement which also uses
target exclusion, the full four-coordinate operation cube, or the exact
spanning model.

## 1. The inference that fails

Let `z` have eight neighbours

\[
 B=\{a,b,r,s,x_1,x_2,x_3,x_4\},\qquad
 T=\{r,s,x_1,x_2,x_3,x_4\}.
\]

The three spoke-signature colourings at the natural six-boundary have the
following partitions of `B`:

\[
\begin{array}{c|l}
c_0&ab\mid rs\mid x_1\mid x_2\mid x_3\mid x_4,\\
c_1&a\mid bs\mid x_1x_2\mid r\mid x_3\mid x_4,\\
c_2&b\mid as\mid x_3x_4\mid r\mid x_1\mid x_2.
\end{array}                                                    \tag{1.1}
\]

In `c_0`, call the colours on `\{a,b\}` and `\{r,s\}` respectively
`\gamma` and `\alpha`, and call the other four colours the beta colours.
The proposed terminal step was:

> the three colourings (1.1), together with all their Kempe-interchange
> consequences and an `\{x_1,x_2,x_3,x_4\}`-rooted `K_4` model in the four
> beta colour classes, force two vertex-disjoint paths in the
> `\alpha`--`\gamma` subgraph linking `\{r,s\}` to `\{a,b\}` with distinct
> ends.

The construction below refutes this statement even when every proper
six-colouring of `G-z` uses every colour on `B`.  The latter condition
means that **every finite sequence** of Kempe interchanges, not merely one
interchange or simultaneous interchanges on a fixed pair of colours,
preserves all six boundary colours.

## 2. What simultaneous interchanges actually prove

There is a useful sharp positive statement, but it is weaker than a
two-linkage.

### Lemma 2.1 (component-imbalance classification)

Let a proper six-colouring of a graph have two `\alpha`-coloured boundary
vertices `R=\{r,s\}` and two `\gamma`-coloured boundary vertices
`A=\{a,b\}`.  Let `D_1,\ldots,D_m` be the components of the
`\alpha`--`\gamma` subgraph and put

\[
 p_i=|D_i\cap R|,\qquad q_i=|D_i\cap A|,
 \qquad d_i=p_i-q_i.                                           \tag{2.1}
\]

Suppose that interchanging `\alpha,\gamma` on any union of the `D_i`
leaves both colours represented on the boundary.  Then either every
`d_i=0`, or exactly one `d_i=1`, exactly one `d_j=-1`, and all remaining
imbalances are zero.

#### Proof

For `I\subseteq\{1,\ldots,m\}`, interchange the two colours on
`\bigcup_{i\in I}D_i`.  The new boundary multiplicities are

\[
 2-\sum_{i\in I}p_i+\sum_{i\in I}q_i,
 \qquad
 2-\sum_{i\in I}q_i+\sum_{i\in I}p_i.                          \tag{2.2}
\]

Both are positive exactly when
`|\sum_{i\in I}d_i|\leq1`.  Taking `I` to be a singleton gives
`d_i\in\{-1,0,1\}`.  Taking all positive, and then all negative,
components shows that at most one `+1` and at most one `-1` occur.  Finally
`\sum_i d_i=|R|-|A|=0`, which gives the assertion. `\square`

The lemma controls only component traces.  A component of trace `(2,2)`
may still have a cutvertex separating the two terminal pairs.  That is the
obstruction realized below.

## 3. Construction

Assign a triple in `\{1,\ldots,6\}^3` to each of the following twenty-one
vertices:

\[
\begin{array}{c|cccccccc}
v&a&b&r&s&x_1&x_2&x_3&x_4\\ \hline
\tau(v)&112&121&244&222&335&436&553&663
\end{array}                                                     \tag{3.1}
\]

For `1\leq i\leq6`, put `\tau(q_i)=(i,i,i)`, and set

\[
\begin{array}{c|rrrrrrr}
v&v_{34}&v_{56}&p_{12}&q_{12}&p_{21}&q_{21}&w\\ \hline
\tau(v)&312&512&324&413&532&641&321.
\end{array}                                                     \tag{3.2}
\]

Let `H` join two vertices when their triples differ in every coordinate,
except that the following four otherwise permitted edges are absent:

\[
 rx_3,\quad rx_4,\quad v_{34}q_5,\quad v_{56}q_3.               \tag{3.3}
\]

Put

\[
 e_1=v_{34}q_5,\qquad e_2=v_{56}q_3,                            \tag{3.4}
\]

add a new vertex `z`, and define

\[
 K=H+\{zt:t\in T\},\qquad
 G=K+\{za,zb,e_1,e_2\}.                                       \tag{3.5}
\]

Thus `K=G-\{za,zb,e_1,e_2\}`.  The two matching edges are remote from
`z`; moreover the oriented ends `v_{34},v_{56}` are nonadjacent.  Put
`J=G-\{e_1,e_2\}`.  This is the analogue of the seven-connected matching
deletion host in the natural construction.

### Theorem 3.1 (finite clean-linkage counterexample)

The graphs defined in (3.1)--(3.5) satisfy every item in the proposed
inference of Section 1, including boundary-surjectivity for every proper
six-colouring of `G-z`.  Nevertheless the required two disjoint
`\{r,s\}`--`\{a,b\}` paths do not exist in the first colouring's
`\alpha`--`\gamma` subgraph.

The structural and colouring hypotheses are checked below and by the
retained deterministic verifier.  The final nonlinkage has the explicit
cutvertex certificate in Section 5.

The finite verifier checks

\[
\begin{array}{c|rrrr}
 &|V|&|E|&\delta&\kappa\\ \hline
H&21&129&8&8\\
K&22&135&6&6\\
J&22&137&8&8\\
G&22&139&8&8.
\end{array}                                                     \tag{3.6}
\]

Also `N_G(z)=B`, and

\[
 \alpha(G[B])=\omega(G[B])=3.                                  \tag{3.7}
\]

The graph `H-T` is connected and is adjacent to every member of `T`.
Consequently `K-T` has exactly the two components `\{z\}` and `H-T`, and
both are `T`-full.  This is the exact natural order-six separation.

The diagonal vertices `q_1,\ldots,q_6` induce a `K_6`.  Exhaustive
six-colouring enumeration, with the diagonal clique used to fix colour
names, gives twenty-two proper six-colourings of `H`; every one uses all
six colours on `B`.  Eighteen of them remain proper after restoring
`e_1,e_2`, so every proper six-colouring of `G-z` is boundary-surjective.
It follows that `G` is not six-colourable.  Conversely the first-coordinate
colouring of `G-z`, followed by a fresh seventh colour on `z`, is proper.
Hence

\[
                              \chi(G)=7.                         \tag{3.8}
\]

This exhaustive statement is the only computer-assisted part needed for
the universal Kempe-sequence assertion.

## 4. The three colourings and the rooted beta model

For `j=0,1,2`, colour every vertex of `H` by coordinate `j+1` of its
triple and give `z` colour `1`.  Each is a proper six-colouring of `K`.
Relative to

\[
 F=\{za,zb,e_1,e_2\},                                          \tag{4.1}
\]

their equality signatures are respectively

\[
                 \{za,zb\},\qquad \{za\},\qquad \{zb\}.       \tag{4.2}
\]

Their boundary partitions are exactly (1.1).  In every row, `T` has
multiplicity shape `2+1+1+1+1` and omits the colour of `z`.

In the first row the following four branch sets lie entirely in the beta
colour classes:

\[
 \{x_1,q_4\},\qquad
 \{x_2,v_{34}\},\qquad
 \{x_3,q_6\},\qquad
 \{x_4,v_{56}\}.                                               \tag{4.3}
\]

They are pairwise disjoint and connected.  The first two are adjacent
through `q_4v_{34}`, the last two through `q_6v_{56}`, and every other
pair is adjacent through its two boundary roots.  Thus (4.3) is an
explicit `\{x_1,x_2,x_3,x_4\}`-rooted `K_4` model in the beta subgraph.

## 5. Failure of the clean two-linkage

Restore `e_1,e_2` and work in `G-z`.  In the first-coordinate colouring,
the `\alpha`--`\gamma` subgraph has vertex set

\[
                    \{a,b,r,s,q_1,q_2\}                         \tag{5.1}
\]

and precisely the five edges

\[
                 ar,\quad br,\quad rq_1,\quad sq_1,\quad q_1q_2.
                                                                    \tag{5.2}
\]

It is one connected component with trace `(2,2)`, so it satisfies the
strongest balanced outcome of Lemma 2.1.  Nevertheless both `a` and `b`
have unique neighbour `r` in this subgraph.  Any path from `s` to either
member of `\{a,b\}` therefore contains `r`, while the path whose other
terminal is `r` also contains `r`.  There are no two vertex-disjoint
`\{r,s\}`--`\{a,b\}` paths with distinct ends.

Because every proper six-colouring of `G-z` is boundary-surjective, no
sequence of Kempe interchanges starting from any of the three displayed
colourings can evade this obstruction by producing a missing boundary
colour.  Simultaneous swaps therefore strengthen the trace bookkeeping to
Lemma 2.1, but do not strengthen connectedness into a two-linkage.

## 6. Exact trust boundary

The construction proves that the terminal step cannot be obtained from
the following data alone:

* the natural connected order-six separation;
* eight-connectivity of `G` and seven-chromaticity;
* `\alpha(G[N(z)])=\omega(G[N(z)])=3`;
* remote disjoint matching edges with independent oriented repair ends;
* the three pair-equality colourings (1.1);
* boundary-surjectivity for **every** proper six-colouring of `G-z`, hence
  the consequences of arbitrary Kempe-interchange sequences; and
* a rooted `K_4` model in the four beta colour classes.

The seven vertices `\{q_1,\ldots,q_6,s\}` induce `K_7^-`: `s` is adjacent
to every `q_i` except `q_2`.  Thus the example deliberately fails target
exclusion.  It also does not claim the full eighty mixed-operation patterns
or the exact spanning `K_7^\vee` model.  Those additional inputs may still
force a terminal outcome, but a valid proof must use one of them to rule out
the balanced cutvertex in (5.2); the three-colouring/Kempe route by itself
cannot do so.

## 7. Verification

Run

```text
python3 barriers/hc7_natural_six_boundary_three_colouring_clean_linkage_barrier_verify.py
```

Expected output:

```text
GREEN natural-six-boundary three-colouring clean-linkage barrier
graphs: H=(21,129,kappa=8) K=(22,135,kappa=6) J=(22,137,kappa=8) G=(22,139,kappa=8,chi=7)
boundary: alpha=3 omega=3 H_colourings=22 G_minus_z_colourings=18 all_surjective=yes
signatures: both=za,zb first=za second=zb beta_rooted_K4=yes
alpha_gamma: trace=(2,2) edges=5 disjoint_terminal_paths=no arbitrary_Kempe_sequences_safe=yes
scope: induced_K7_minus=q1,q2,q3,q4,q5,q6,s
```
