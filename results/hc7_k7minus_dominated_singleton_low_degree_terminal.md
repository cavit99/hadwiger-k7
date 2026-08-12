# Low-degree completion of the dominated singleton

**Status:** written proof with one computer-assisted finite lemma;
[separate internal audit GREEN](hc7_k7minus_dominated_singleton_low_degree_terminal_audit.md).
This is a conditional reduction inside the eight-coordinate campaign.  It
does not prove the `K_7^-` six-colour conjecture or `HC_7`.

The dominated-singleton reduction produces a triangle-free,
`K_5^-`-minor-free graph on the common neighbours of the operated edge and
a vertex cut of order at most two in that graph.  The fixed exact
`K_7^vee` model guarantees a deletion-persistent edge at degree eight and
two at degree nine.  The finite lemma below proves that either one such edge
lies beyond a common-neighbour cut, or an exterior component already
completes a `K_7^-` minor.

## 1. The finite marked-neighbourhood lemma

For a graph `Q`, call a set `M subseteq V(Q)` **cut-confined** if `Q` has a
vertex cut of order at most two and

\[
                         M\subseteq S                 \tag{1.1}
\]

for every such cut `S`.

### Lemma 1.1 (exact marked classification and exterior completion)

Let `Q` be triangle-free and `K_5^-`-minor-free, and suppose that `Q` has a
vertex cut of order at most two.

1. If `|V(Q)|=7` and `alpha(Q)=3`, then a cut-confined singleton `M`
   exists only when the marked graph `(Q,M)` is isomorphic to one of the
   two automorphic markings

   \[
                 (\texttt{FCxv?},\{0\}),\qquad
                 (\texttt{FCxv?},\{5\}).              \tag{1.2}
   \]

   The underlying graph is `K_{3,3}` with one edge subdivided, and its
   unique cut of order at most two is the pair consisting of the ends of
   that subdivided edge.
2. If `|V(Q)|=8` and `alpha(Q)<=4`, then a cut-confined two-set exists only
   when `Q` has graph6 encoding ``G?rF`w`` and

   \[
                              M=\{6,7\}.               \tag{1.3}
   \]
3. In either exceptional underlying graph, add adjacent vertices `u,v`
   complete to `Q`, and add a vertex `c` which is nonadjacent to `u` and
   adjacent to at least seven vertices of

   \[
                              \{v\}\cup V(Q).          \tag{1.4}
   \]

   The resulting graph contains a `K_7^-` minor.

#### Computer verification

The deterministic verifier is
[`verify.py`](../active/experiments/dominated_singleton_low_degree_completion/verify.py),
with its method and reproduction command recorded in the adjacent
[`README`](../active/experiments/dominated_singleton_low_degree_completion/README.md).
It uses nauty's `geng -t` to enumerate every unlabelled triangle-free graph
of orders seven and eight.  It checks the independence bound and excludes a
`K_5^-` minor by exact deletion and contraction.  It then tests every marked
singleton or pair against every vertex cut of order at most two.

The exact counts are

\[
\begin{array}{c|c|c|c}
 |V(Q)|&\text{eligible graphs}&\text{marked instances}
      &\text{surviving marked instances}\\ \hline
 7&9&63&2\\
 8&158&4424&1.
\end{array}                                             \tag{1.5}
\]

They give precisely (1.2) and (1.3).  For item 3 the verifier checks every
possible missed set in (1.4): nine profiles for (1.2) and forty-six for
(1.3).  Its independent exact minor routine finds a `K_7^-` minor in every
profile.  Positive and negative controls test that routine before the
enumeration.  Thus the computation proves only the finite statement above;
no unbounded hypothesis is encoded as a search bound.

## 2. Low-degree model-persistent component alignment

Retain the setting of the audited
[dominated-singleton theorem](hc7_k7minus_dominated_singleton_twocut_response.md).
Thus `G` is seven-connected and seven-chromatic, every proper minor is
six-colourable, and `G` contains neither a `K_7^-` minor nor a literal
`K_5`.  Let

\[
                 e=uv,\qquad
                 Q=G[N_G(u)-\{v\}],\qquad
                 O=G-N_G[u],                           \tag{2.1}
\]

where `v` is adjacent to every vertex of `Q`.  Assume that `uv` is the
retained forest coordinate and that `G-uv` contains a spanning labelled
exact `K_7^vee` model.  Let `R` be the branch set containing `u`, suppose
that `R={u}` or `R-u` is connected, and let `D` be a named foreign branch
set anticomplete to `u`.

### Theorem 2.1 (degree-eight/nine component alignment)

If

\[
                              d_G(u)\in\{8,9\},          \tag{2.2}
\]

then there are a set `S subseteq V(Q)` of order at most two, a component
`A` of `Q-S`, and a vertex `x in A` such that deleting `ux` leaves the same
labelled exact `K_7^vee` model in

\[
                              G-\{uv,ux\}.              \tag{2.3}
\]

The graph in (2.3) has exactly the two equality signatures

\[
                              \{uv\},\qquad\{ux\}       \tag{2.4}
\]

on the selected edges.  The first may be realised by the original
singleton-signature colouring of `G-uv`, while a colouring with signature
`{ux}` induces a rejected exterior trace on the actual side `A`.  Its
boundary satisfies

\[
                              |N_G(A)|\ge7.              \tag{2.5}
\]

#### Proof

The dominated-singleton theorem gives

\[
 |V(Q)|=d_G(u)-1,\qquad Q\text{ triangle-free},\qquad
                         K_5^-\npreccurlyeq Q,           \tag{2.6}
\]

and the Wood--Woodall classification gives a vertex cut of `Q` of order at
most two.  If `d_G(u)=8`, the absence of a literal `K_5` makes `u`
exceptional, so the audited exceptional-neighbourhood theorem gives

\[
                              \alpha(Q)=3.              \tag{2.7}
\]

Here `v` is complete to `Q`, so adjoining it does not change the maximum
independent-set order.  If `d_G(u)=9`, the standard contraction-critical
neighbourhood bound gives instead

\[
                              \alpha(Q)\le4.             \tag{2.8}
\]

Call `ux`, for `x in V(Q)`, **persistent** when its deletion leaves the
fixed branch sets as the same exact model.  The essential-edge count from
the dominated-singleton theorem is exact for the present purpose: at most
one edge can be the sole attachment from `u` to `R-u`, and at most one can
be the sole edge witnessing each required adjacency from `R` to a foreign
branch set.  The named `u`-anticomplete bag removes one foreign possibility
when the label of `R` is universal.  In every case at most six members of

\[
                              \{ux:x\in V(Q)\}          \tag{2.9}
\]

are nonpersistent.  Hence there is at least one persistent edge at degree
eight and at least two at degree nine.

At degree eight mark one persistent endpoint; at degree nine mark any two.
Apply Lemma 1.1.  Unless the marked graph is exceptional, some vertex cut
`S` of order at most two fails to contain all marked vertices.  Choose a
marked vertex `x outside S` and let `A` be its component in `Q-S`.  The
proof of the dominated-singleton two-cut theorem applies to this cut: a
different component remains on the far side, `N_G(A)` is an actual
separator, and seven-connectivity gives (2.5).  Persistence gives (2.3).
The triangle `uvx` makes the signature language exactly (2.4), and the
signature-`{ux}` colouring restricts properly outside `A`; gluing proves
that its boundary partition is rejected by the intact closed `A`-side.

It remains to exclude the exceptional marked graphs.  The set `O` in
(2.1) is nonempty: the common-neighbour cut theorem gives every component
of `Q-S` at least `5-|S|>=3` neighbours in `O`.  Choose a component `C` of
`G[O]` and contract it to one
vertex `c`.  Every neighbour of `C` outside `C` belongs to

\[
                              N_G(u)=\{v\}\cup V(Q),    \tag{2.10}
\]

and `N_G(C)` is an actual separator from `u`.  Seven-connectivity therefore
gives

\[
                              |N_G(C)|\ge7.             \tag{2.11}
\]

After deleting all unused vertices, the resulting simple minor is one of
the augmented graphs described in Lemma 1.1(3).  That lemma supplies a
`K_7^-` minor, contrary to the host
hypothesis.  Thus the exceptional cases cannot occur, and the selected
`S,A,x` have all the asserted properties. `\square`

### Corollary 2.2 (all-degree dominated alignment)

Under the hypotheses preceding Theorem 2.1, the same conclusion holds for
every `d_G(u)>=8`.

#### Proof

Theorem 2.1 treats degrees eight and nine.  For degree at least ten, the
audited high-degree component-alignment corollary counts at least three
persistent endpoints, one of which avoids the Wood--Woodall cut of order at
most two, and gives precisely the same model and response conclusion.
`\square`

## 3. Exact gain and remaining obligation

The low-degree obstruction is eliminated: a dominated singleton can no
longer concentrate all model-persistent incident edges on the
Wood--Woodall cut.  At every degree it now supplies one common graph
carrying

- the original exact `K_7^vee` model;
- the original forest-coordinate colouring;
- an exclusive switch between the original coordinate and a fresh
  incident edge; and
- an actual response side containing the persistent fresh endpoint.

This does not yet terminalise the arbitrary-order response side.  Its
boundary has the lower bound (2.5), but no upper bound, and the theorem
does not select persistent endpoints in two different components or make
one boundary partition extend through both intact shores.  Those are
model-and-colouring composition obligations beyond the finite low-degree
placement problem proved here.

## Dependencies

- [coordinate responses at a singleton side](hc7_k7minus_singleton_coordinate_localisation.md);
- [dominated-singleton two-cut and persistence](hc7_k7minus_dominated_singleton_twocut_response.md);
- [exceptional-neighbourhood structure](../results/hc7_k7minus_exceptional_neighbourhood_completion.md);
- the contraction-critical bound
  `alpha(G[N(u)])<=d_G(u)-5`; and
- Wood--Woodall, *Defective Choosability of Graphs without Small Minors*,
  Lemma 4.2.1.
