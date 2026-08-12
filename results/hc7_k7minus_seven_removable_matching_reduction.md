# A seven-connected common response host from a removable matching

**Status:** written proof; [separate internal audit GREEN](hc7_k7minus_seven_removable_matching_reduction_audit.md).
The only new external input is Theorem 1.3 of Hojin Chu's 10 August 2026
preprint cited below.  This reduction does not prove the `K_7^-` six-colour
conjecture or `HC_7`.

Throughout, `K_7^-` denotes `K_7` with one edge deleted and `K_7^vee`
denotes `K_7` with two incident edges deleted.

## 1. Setting

Let `G` be a finite simple graph satisfying

\[
 \chi(G)=7,\qquad
 \chi(J)\leq6\text{ for every proper minor }J\text{ of }G,
 \qquad K_7^-\npreccurlyeq G,                       \tag{1.1}
\]

and

\[
 \kappa(G)\geq7,\qquad \delta(G)\geq8,
 \qquad |E(G)|\geq4|V(G)|,
 \qquad |V(G)|\geq25.                              \tag{1.2}
\]

These hypotheses hold in a minor-minimal counterexample to the `K_7^-`
six-colour conjecture by the existing critical-host reduction.  The order
bound is used only to exclude the exceptional graph `K_9` in the removable
matching theorem and the small extremal exception `K_{2,2,2,2}`.

For a matching `M` and a proper six-colouring `c` of `G-M`, put

\[
 \Sigma_M(c)=\{uv\in M:c(u)=c(v)\}.                 \tag{1.3}
\]

Here a six-colouring may use fewer than six colours.

## 2. The removable matching and its response cube

### Theorem 2.1 (seven-removable common host)

There is a matching `M` of order five such that, for

\[
                              H=G-M,                 \tag{2.1}
\]

all of the following hold.

1. `H` is seven-connected and

   \[
                       |E(H)|\geq4|V(H)|-5.          \tag{2.2}
   \]

2. The exact matching-signature language on `H` is

   \[
       \{\Sigma_M(c):c\text{ is a proper six-colouring of }H\}
                         =2^M-\{\varnothing\}.       \tag{2.3}
   \]

3. For every `e\in M`,

   \[
                         \chi(G-e)=\chi(G/e)=6.      \tag{2.4}
   \]

4. For every `e\in M`, there is a nonempty connected set `Y_e`
   containing exactly one end of `e` such that `N_G(Y_e)` is an actual
   separator of order at least seven.  A signature-`{e}` colouring of
   `H` is proper on `G-Y_e`, and its boundary precolouring does not extend
   through `Y_e`.

#### Proof

Apply Theorem 1.3 of Chu's removable-matching theorem with `k=7` and
`m=5`.  Its degree threshold is

\[
                  \max\{k+1,2m-2\}=8.              \tag{2.5}
\]

The only relevant exception is `K_{2m-1}=K_9`, which is excluded by
`|V(G)|\geq25`.  Hence `G` has a matching `M` of order five for which
`G-M` remains seven-connected.  This proves the connectivity assertion,
and (2.2) follows by deleting five edges from (1.2).

Fix a nonempty `J\subseteq M`.  Six-colour the proper minor `G/J` and
expand every contracted edge into `H`.  The ends of every edge in `J`
have equal colours.  Every edge of `M-J` remains an edge of `G/J`, because
`M` is a matching, so its ends have different colours.  Thus the expanded
colouring has signature exactly `J`.  A colouring with empty signature
would remain proper after every edge of `M` was restored and would
six-colour `G`.  This proves (2.3).

For a single edge `e=uv`, both `G-e` and `G/e` are proper minors and hence
at most six-chromatic.  A five-colouring of `G/e` could be expanded by
leaving `u` in the contracted colour and assigning a fresh sixth colour
to `v`; this would six-colour `G`.  Similarly, a five-colouring of `G-e`
would either already colour `G`, if `u,v` had different colours, or could
be extended to `G` by assigning a fresh sixth colour to one end.  This
proves (2.4).

Apply the audited minimal contraction-bag normalization to `G/e`.  Its
lift splits the contraction bag into connected adjacent sets containing
the two ends of `e`.  If both retained all five foreign branch-set
contacts, the split would give a `K_7` minor.  Hence one side, called
`Y_e`, has an actual open-neighbourhood separator; seven-connectivity gives
`|N_G(Y_e)|\geq7`.  A signature-`{e}` colouring has `e` as its only
monochromatic edge after `M` is restored.  Deleting `Y_e` removes that
edge.  If the induced boundary precolouring extended through `Y_e`, the
two colourings would glue to a six-colouring of `G`.  This proves item 4.
`\square`

### Lemma 2.2 (direct endpoint traces)

Every nonempty proper set `X` meeting `V(M)` carries a rejected exterior trace:
there is a proper six-colouring of `G-X` whose induced boundary
precolouring does not extend through `X`.

#### Proof

Choose `v\in X\cap V(M)`, let `e` be the matching edge incident with `v`,
and take a signature-`{e}` colouring of `H`.  After all edges of `M` are
restored, `e` is its only monochromatic edge.  Since deleting `X` removes
one end of `e`, the restriction is proper on `G-X`.  An extension through
`X` agreeing on `N_G(X)` would glue to a six-colouring of `G`, a
contradiction. `\square`

### Scope of the cube

Unlike the centre-edge matching in the earlier common-host theorem, the
matching supplied by Chu need not have one end at each exceptional
degree-eight vertex.  Accordingly, (2.3) does **not** imply that
`\chi(G/J)=6` for a multi-edge set `J`, nor does it supply centre-saturation
data or one common `K_6` model co-bagging all five pairs.  The exact
signatures and the seven-connectivity of `H` are the conclusions retained
here.

## 3. The connectivity trichotomy collapses to one exact model

### Theorem 3.1 (exact near-clique reduction)

The graph `H` has a spanning `K_7^vee`-minor model.  Label its branch sets

\[
                         P,B,C,U_1,U_2,U_3,U_4,       \tag{3.1}
\]

so that only `PB,PC` may be absent.  In a target-free `G`, both
adjacencies are absent even after the edges of `M` are restored.  Hence the
same partition is an exact spanning `K_7^vee` model in `G`.

Consequently there is a nonempty proper connected set `Y` in one universal
bag `U_i` such that `U_i-Y` is connected and `N_G(Y)` is an actual
separator of order at least seven.

If `Y\cap V(M)\ne\varnothing`, then `Y` carries a rejected exterior trace
from a singleton matching signature.

#### Proof

The graph `H` is four-connected and satisfies

\[
                         |E(H)|\geq4|V(H)|-5
                                      \geq4|V(H)|-8.
\]

Theorem 6 of Norin and Totschnig therefore gives a `K_7^vee` minor in
`H`; the exceptional graph `K_{2,2,2,2}` is excluded by the order bound.
Absorb unused components into adjacent branch sets to make the model
spanning.

If restoring `M` supplied either `PB` or `PC`, the seven displayed bags
would have at most one missing adjacency and would form a `K_7^-` model in
`G`.  Target exclusion therefore leaves both pairs anticomplete.  The
audited exact `K_7^vee` dichotomy, applied in `G`, now gives the asserted
set `Y` and separator.

The final assertion is Lemma 2.2.
`\square`

## 4. Exact endpoint-support residue

### Theorem 4.1 (two endpoint portals)

Retain the model (3.1).  If some universal bag contains two distinct
vertices

\[
                   p,q\in N_G(P)\cap U_i\cap V(M),  \tag{4.1}
\]

then `G` contains a `K_7^-` minor or the separator in Theorem 3.1 can be
chosen so that its connected side meets `V(M)` and therefore carries a
singleton-signature rejected trace.

Thus a target-free residue without such a forced trace satisfies

\[
                  |N_G(P)\cap U_i\cap V(M)|\leq1
                         \qquad(1\leq i\leq4),        \tag{4.2}
\]

and consequently

\[
                         |N_G(P)-V(M)|\geq3.          \tag{4.3}
\]

#### Proof

Rerun the proof of the exact `K_7^vee` dichotomy with `p,q` as its two
selected neighbours of `P` in `U_i`.  Every separator outcome in that
proof contains one of the two selected vertices; the alternative is an
explicit `K_7^-` model.  Theorem 3.1 attaches the singleton signature of
the matching edge incident with the selected endpoint.

If (4.1) never occurs, (4.2) follows.  The branch set `B` lies outside
`P\cup N_G(P)`, so `N_G(P)` is an actual separator.  Seven-connectivity
gives `|N_G(P)|\geq7`; summing (4.2) over the four universal bags proves
(4.3). `\square`

### Corollary 4.2 (hybrid exceptional-centre support)

If five independent exceptional degree-eight centres `Z` have also been
fixed, let `W_Z` be their response-support set from the audited dense
rotation-visibility theorem and put

\[
                              W^+=W_Z\cup V(M).       \tag{4.4}
\]

Every connected set meeting `W^+` carries either a centre-star trace or a
singleton matching-signature trace.  Theorem 4.1 therefore remains true
with `V(M)` replaced by `W^+`.  Its trace-invisible residue satisfies

\[
 |N_G(P)\cap U_i\cap W^+|\leq1\quad(1\leq i\leq4),
 \qquad |N_G(P)-W^+|\geq3.                           \tag{4.5}
\]

#### Proof

The direct trace statement for `W_Z` is Lemma 1.1 of the cited visibility
theorem; the statement for `V(M)` is Lemma 2.2 above.  Rerun the same
two-selected-portal proof and then repeat the count in Theorem 4.1.
`\square`

## 5. Exact remaining theorem

The low-connectivity alternatives of the centre-edge common host are not
present here: `H=G-M` is seven-connected by construction.  The surviving
problem is entirely inside one exact spanning near-clique model.

> **Seven-removable matching terminalization target.**  Under (1.1)--(1.2),
> a seven-removable matching of order five and its punctured signature
> family force a `K_7^-` minor.

At the current boundary, a valid proof must eliminate both outcomes left
above:

1. a response-bearing model-bag separator whose order and boundary
   partition are uncontrolled; and
2. the exact support-sparse model in (4.2), or in the stronger hybrid form
   (4.5).

The punctured signature family alone does not identify colour classes with
branch bags.  A contact-only split of a co-bagged `K_6` model is also
insufficient: explicit quotient obstructions can make every split lose two
branch-set adjacencies.  The next argument must couple a matching endpoint
to the internal geometry of the exact `K_7^vee` model, or turn its failure
into an exact labelled separator; further low-cut enumeration is not
relevant to this host.

## Dependencies and provenance

The removable matching is Theorem 1.3 of Hojin Chu,
[*A sharp extension of Halin's removable-edge theorem to matchings*](https://arxiv.org/abs/2608.09394),
arXiv:2608.09394v1 (10 August 2026).  This is a recent preprint, not an
externally peer-reviewed input at the time of writing.

The density-to-`K_7^vee` input is Theorem 6 of Sergey Norin and Agnès
Totschnig,
[*Every graph with no `K_7^vee` minor is 6-colorable*](https://arxiv.org/abs/2507.03244).
The contraction-bag normalization, exact near-clique dichotomy and
five-centre response-support theorem cited above are separately audited
results in this repository.
