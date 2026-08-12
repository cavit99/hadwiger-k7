# Seven-coordinate growth or a bounded feedback set

**Status:** written proof;
[separate internal audit GREEN](hc7_k7minus_six_coordinate_growth_or_feedback_audit.md).
This is a conditional refinement of the six-coordinate induced-forest
reduction.  It does not prove the `K_7^-` six-colour conjecture or `HC_7`.

## Theorem 1 (growth-or-feedback alternative)

Let `G` satisfy the critical-host hypotheses in the
[six-coordinate induced-forest reduction](hc7_k7minus_six_coordinate_forest_reduction.md).
Let `F` be the six-edge componentwise-induced forest supplied there, and
put

\[
                              X=G-F.                 \tag{1}
\]

Suppose, in addition, that `X` is seven-connected.  Then at least one of
the following holds.

1. There is an edge `f` disjoint from `V(F)` such that

   \[
                              F'=F\cup\{f\}          \tag{2}
   \]

   is a seven-edge componentwise-induced forest and `G-F'` is
   seven-connected.  Moreover,

   \[
      |E(G-F')|\geq4|V(G)|-7                         \tag{3}
   \]

   and the exact signature language on `G-F'` is the full punctured
   seven-cube

   \[
      \{\Sigma_{F'}(c):c\in\operatorname{Col}_6(G-F')\}
                              =2^{F'}-\{\varnothing\}. \tag{4}
   \]

   The graph `G-F'` also has a spanning `K_7^vee` model which is exact
   even in target-free `G`.

2. `V(F)` is a feedback vertex set of `G`.  Its order is twelve when `F`
   is a matching and eleven when the only nonsingle-edge component of `F`
   is an induced three-vertex path.  In either case

   \[
                              \chi(G[V(F)])\geq5.    \tag{5}
   \]

### Proof

Put `R=V(G)-V(F)`.  Every vertex of `R` retains all its incident edges when
`F` is deleted, and hence

\[
                              d_X(v)=d_G(v)\geq8
                              \qquad(v\in R).        \tag{6}
\]

Suppose first that `X[R]` contains a cycle `C`.  If `X-f` failed to be
seven-connected for every `f\in E(C)`, all edges of `C` would be critical
for seven-connectivity in the seven-connected graph `X`.  Mader's
critical-cycle theorem would then give a vertex of `C` of degree seven in
`X`, contrary to (6).  Thus some `f\in E(C)` leaves `X-f` seven-connected.

The edge `f` is vertex-disjoint from `F`, so adding it creates a new
single-edge component.  Thus `F'` in (2) remains componentwise induced.
Also

\[
                              G-F'=X-f,
\]

which proves the connectivity and density claims.

For completeness, fix nonempty `J\subseteq F'` and six-colour the proper
minor `G/J`.  Because `F'` is a forest, no edge of `F'-J` has both ends in
one contracted component.  Because every component of `F'` is induced, no
edge of `G-F'` has both ends in one contracted component.  Expanding gives
a proper colouring of `G-F'` with signature exactly `J`.  An empty
signature would six-colour `G`.  This proves (4).

The graph `G-F'` is four-connected and satisfies the Norin--Totschnig
density threshold strictly, which already excludes `K_{2,2,2,2}`.  Their
theorem gives a `K_7^vee` model.  Make it spanning by absorption.  If
either nominally missing pair became adjacent when `F'` was restored, the
same bags would form a `K_7^-` model.  Target exclusion therefore makes
the model exact in `G`.

It remains that `X[R]` is a forest.  Since all deleted edges of `F` have
both ends in `V(F)`,

\[
                              G-V(F)=X[R],           \tag{7}
\]

so `V(F)` is a feedback vertex set.  Its stated order follows from the two
possible component types of `F`.  Finally, colour `G[V(F)]` and the forest
`G-V(F)` with disjoint palettes.  This gives

\[
                    7=\chi(G)\leq\chi(G[V(F)])+2,
\]

and proves (5). `\square`

## Scope

The theorem does not claim that the feedback-set outcome is impossible.
It identifies the exact obstruction to adding a seventh independent
coordinate by the critical-cycle method: after at most twelve vertices are
removed, the entire remaining graph is a forest, while those at most twelve
vertices already induce a graph of chromatic number at least five.

The same argument may be applied once more without crossing the
Norin--Totschnig density threshold.

### Corollary 2 (eight coordinates or feedback order at most fourteen)

Under the hypotheses of Theorem 1, at least one of the following holds.

1. There is an eight-edge componentwise-induced forest `F_8` such that

   \[
      G-F_8\text{ is seven-connected},\qquad
      |E(G-F_8)|\geq4|V(G)|-8,                       \tag{8}
   \]

   its exact signature language is

   \[
                              2^{F_8}-\{\varnothing\}, \tag{9}
   \]

   and it has a spanning `K_7^vee` model which is exact in `G`.
2. `G` has a feedback vertex set `S` with

   \[
      |S|\leq14,\qquad \chi(G[S])\geq5.             \tag{10}
   \]

   In the induced-path case, the sharper bound `|S|<=13` holds.

#### Proof

If Theorem 1 returns a feedback set, it already has order at most twelve.
Otherwise apply its cycle argument to the seven-coordinate forest `F'` and
the seven-connected graph `G-F'`.  A surviving cycle outside `V(F')`
supplies a disjoint eighth edge and gives outcome 1.  If there is no such
cycle, `V(F')` is a feedback vertex set.  Adding the seventh single-edge
component increased the original vertex set by two, so its order is
fourteen in the matching case and thirteen in the induced-path case.  The
same disjoint-palette inequality proves chromatic number at least five.
`\square`

The number eight is a natural stopping point for this iteration: deleting
eight edges leaves exactly the density `4|V(G)|-8` at which the common exact
near-clique model remains automatic.  Further growth is logically possible
but would require a different density input.

The critical-cycle input is Wolfgang Mader, *Ecken vom Grad n in minimalen
n-fach zusammenhängenden Graphen*, Archiv der Mathematik **23** (1972),
219--224, Satz 1.  The density input is Norin--Totschnig, Theorem 6.
