# Separate internal audit: model-anchored response hull

**Verdict:** **GREEN.**  Theorem 2.1 and Corollaries 2.2 and 3.1 are
correct at the pinned revision.  The construction preserves the fixed
edge-deletion response and the connected complement inside its named branch
set.  It gives a strict descent exactly under the condition stated in
(2.1); a proper list-critical core alone does not ensure strictness.

This is a separate internal mathematical audit, not external peer review.

## Exact revision

The audited source is
[`hc7_k7minus_model_anchored_response_hull.md`](hc7_k7minus_model_anchored_response_hull.md),
with SHA-256

```text
7cc1da7567f05e10bb7089c4b6dcd0706e9a0daa406063e7ba986d3d283c9512
```

The mathematical text is unchanged from the originally checked revision;
the pinned revision updates only its status line to link this audit.

The proof is computation-free.  Its positive statements require only the
displayed fixed colouring and branch-set topology.  Seven-connectivity is
used solely for the lower bound on the order of the actual boundary.

## 1. Hull containment and connectivity

Because `K subseteq Y`, the connected set `R-Y` is contained in `R-K`.
It consequently lies in one component `W` of `G[R-K]`.  This gives

\[
                       R-Y\subseteq W,
       \qquad \widehat K=R-W\subseteq Y.             \tag{1.1}
\]

The sets `W` and `K` are nonempty.  Every component of `G[R-K]` other
than `W` has an edge to `K`: on a path in the connected graph `G[R]` from
that component to `K`, the first edge leaving the component cannot enter a
different component of `G[R-K]`.  Since `K` is connected, adjoining all
those components to it gives a connected set, exactly `widehat K`.
Therefore both sides of the split of `R` are nonempty and connected.

No whole-graph connectivity has been inferred from connectivity of
`G[R]`; the proof uses only edges internal to the named branch set.

## 2. Actuality and the fixed trace

The named set `D` is anticomplete to `Y`, and `widehat K subseteq Y`.
Thus `D` is nonempty and lies outside `N_G[widehat K]`.  It is a genuine
far side after deletion of `N_G(widehat K)`, while `widehat K` is the
other nonempty side.  The asserted separator is therefore actual.

The critical core contains the relevant end or ends of `e`, and
`K subseteq widehat K`.  Since the fixed colouring can fail in `G` only
on `e`, deleting `widehat K` makes its exterior restriction proper.  An
intact extension with the same literal boundary partition would align by a
permutation of the six colour names and glue to a six-colouring of `G`.
This verifies the rejected-trace statement without assuming boundary
fullness or an upper bound on the boundary.

## 3. Direction of list containment

For `x in K`, every neighbour of `x` in the old boundary remains outside
`widehat K` and adjacent to it.  Explicitly,

\[
 N_G(x)\cap N_G(Y)
     \subseteq N_G(x)\cap N_G(\widehat K).           \tag{3.1}
\]

The new boundary may additionally contain neighbours in
`Y-widehat K`.  It therefore displays a superset of the old boundary
colours and gives the smaller lists

\[
                 L_{\widehat K}(x)\subseteq L_Y(x).  \tag{3.2}
\]

Noncolourability of `G[K]` from the larger lists implies
noncolourability from the smaller ones.  Any list-colouring of the whole
hull would restrict to the forbidden colouring of `K`.  Item 3 is thus in
the correct direction.

## 4. Contact retention and the strictness criterion

Equation (1.1) puts the entire old complement `R-Y` inside the new
complement `W=R-widehat K`.  Hence every external branch-set adjacency
which already had a witness in `R-Y` remains literally witnessed after the
replacement.  The theorem does not claim to preserve an adjacency owned
only by `Y`, which is the correct trust boundary.

The partition

\[
                   R-K=(R-Y)\mathbin{\dot\cup}(Y-K)
\]

and `R-Y subseteq W` give

\[
 \widehat K=Y
 \iff R-W=Y
 \iff W=R-Y
 \iff W\cap(Y-K)=\varnothing.
\]

This is exactly (2.1).  In particular, `K subsetneq Y` does not imply
`widehat K subsetneq Y`; no unsupported strict descent is hidden in the
iteration.

At a terminal iterate with proper critical core `K_Z`, failure of
strictness says that the component `W` containing `R-Z` contains no vertex
of `Z-K_Z`.  Since `R-Z` is already connected, `W=R-Z`; all other
components of `G[R-K_Z]` lie inside `Z-K_Z` and are separated from the
exterior complement by `K_Z`.  This verifies Corollary 3.1.

## 5. Sharpness examples

The path `r-k-a` correctly realises the topological failure:
`R-Y={r}`, `K={k}`, and the component of `R-K` containing `r` is
`{r}`, so the hull is all of `Y={k,a}`.

The fixed-response example also satisfies the displayed local hypotheses.
In `K_7-e`, the six-colouring gives `u,v` one colour and the five `a_i`
the other five colours.  With `R={a_1,u,t}`, `Y={u,t}`, and `K={u}`,
the boundary of `u` includes `v,a_1,\ldots,a_5,t`, so all six colours
occur and its boundary list is empty.  The set `D={d}` is disjoint from
`R` and anticomplete to `Y`, while `R-Y={a_1}` is connected.  Removing
`K` leaves the two components `{a_1}` and `{t}`, so the anchored hull is
again all of `Y`.

This example contains the displayed literal `K_7` and is not a critical
host.  The source therefore classifies it correctly as sharpness for the
hull mechanism, not as a counterexample to target-free terminalisation.

## Scope

There are no unresolved assumptions in the proved hull statements.  The
source does **not** prove that the hull is proper whenever the list core is
proper, bound the new separator, eliminate the terminal appendages, prove
the eight-coordinate terminalisation theorem, or prove Conjecture 21 or
`HC_7`.
